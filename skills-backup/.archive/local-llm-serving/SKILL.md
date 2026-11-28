---
name: local-llm-serving
description: Use when serving local LLMs (llama.cpp) with Hermes.
---

# Local LLM serving with Hermes

Class: running local GGUF models (llama.cpp llama-server, Ollama, LM Studio) as a Hermes custom provider and getting the model picker (`/model`, `hermes model`) to match reality.

## Core model of the system

- **Hermes sees what `GET {base_url}/v1/models` returned, persisted into config.yaml.** The picker is NOT a pure live view: successful probes are saved into the provider entry under `models:` with `models_discovered: true`, and later reads merge that catalog with fresh probes.
- **llama.cpp `llama-server` serves exactly one model per instance** (`-m <file>`). So the live list always has 1 entry; anything else in the picker is a stale cached entry.
- Model id = whatever the server reports in `/v1/models` (for llama.cpp, the full file path — that's why `model.default` holds an absolute path).

## Diagnosis: 'the picker shows a model I didn't load' (ghost models)

1. `curl -s {base}/v1/models` → ground truth of what's loaded.
2. `grep -A8 "<provider name>" ~/.hermes/config.yaml` → the persisted `models:` mapping + `models_discovered` flag.
3. `~/.hermes/provider_models_cache.json` → per-provider cache (fingerprint-keyed).
4. Mismatch = stale catalog from a previous probe when a different quant was loaded. Fix with `/model --refresh` (re-probes and overwrites the Hermes-owned catalog) or hand-edit the `models:` mapping. Selecting a ghost model 404s because the server never had it loaded in this session.

## Multi-model serving (want N models in one picker)

- **Two servers, two ports** → two provider entries in config.yaml. Simplest; VRAM = sum of both models.
- **llama.cpp router mode**: `--models-dir ~/models --models-max N` (one server, multiple models, INI presets via `--models-preset`).
- Always check VRAM first (`nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv`). Two 27B-class quants on 16Gx2 GPUs does not fit with a real context; plan one big + one small, or accept CPU offload.

## Context / KV-cache fit ("can I run -c N?")

Recipe verified 2026-09-09 on this box (Qwen3.8-27B-UD-Q4_K_M, 2x16GB 5060 Ti + 61GB RAM):
1. Run `scripts/kv-fit.py <model.gguf> [ctx...]` (with `~/llama.cpp/llama-env/bin/python`) — reads arch fields from the GGUF, prints KV GB at f16/q8_0/q4_0 for each ctx. Formula: KV bytes/token = 2 x layers x kv_heads x head_dim; quant bytes f16=2.0, q8_0=1.0625, q4_0=0.5625.
2. Compare against GPU free + system RAM free (`free -h`): KV that doesn't fit in VRAM spills to RAM (works, slower prefill on long prompts).
3. GGUF gotchas hit: field names are **arch-prefixed** (`qwen35.block_count`, `qwen35.attention.head_count_kv` — not bare `block_count`); `ReaderField.contents` is a **method** (call it); `head_size` may be absent -> derive as `embedding_length // attention.head_count` (floor) — same fallback llama.cpp uses; `context_length` metadata tells the model's native max (Qwen3.8-27B = 262144).
4. Qwen3.8-27B UD-Q4_K_M numbers: ~15.3GB weights, KV q8_0 ~69KB/tok (128k=~17GB, 256k=~32GB) — 256k fits with RAM overflow on this box. Full GPU offload (`-ngl 95`) of weights + q8_0 KV at 262144 ctx fits both 16GB cards combined (~14+15GB used) — quantizing KV is what makes it fit; the same ctx with f16 KV does not.
5. **If the server in question is the one serving THIS session** (check `ps aux | grep llama-server` vs `base_url` in config.yaml) — do NOT restart it yourself; the session drops. Give the user the exact kill+restart command to run after the session, or accept it as a trade-off they choose.

## Keeping llama-server up (persistent serving + cron pinned to a local model)

- A cron job pinned to a local model fails with `RuntimeError: Connection error.` whenever llama-server is down — the job is fine, the endpoint is gone. Diagnose in order: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8080/health` (000 = down), `pgrep -af llama-server`, `nvidia-smi --query-gpu=index,memory.used --format=csv,noheader` (weights loaded?), then restart the unit.
- Serve persistently via a user systemd unit, not a loose process: copy `templates/llama-server.service` to `~/.config/systemd/user/`, adjust the ExecStart flags, then `systemctl --user daemon-reload && systemctl --user enable --now llama-server`. Survives reboots, auto-restarts on failure; the box already runs hermes-gateway this way.
- Anything that must outlive the current tool call goes in systemd — processes launched inside a terminal-tool call (nohup, background=true, setsid) are reaped when the call's scope ends, dying silently mid-model-load with no error line in the log.
- Startup takes seconds even for ~16GB GGUFs (lazy mmap). If health is still 000 past ~30s with near-zero VRAM used, the process died — read the log/exit path instead of waiting longer.
- **Boot-race CPU-only fallback (seen 2026-09-25):** if the unit starts while NVIDIA driver init is still finishing, llama-server logs `ggml_cuda_init: failed to initialize CUDA: unknown error` + `warning: no usable GPU found, --gpu-layers option will be ignored` and then serves CPU-only FOREVER — health 200, process alive, but prefill ~11 tok/s and VRAM near zero while nvidia-smi later looks perfectly healthy. Diagnose by comparing tok/s + `nvidia-smi` VRAM, not by health alone. Fix = `ExecStartPre=/home/lifetofree/.hermes/scripts/wait-for-cuda.sh` in the unit (waits for nvidia-smi + /dev/nvidia-uvm major matching /proc/devices, 120s cap); a plain restart after driver is up also recovers.
- Smoke-test a thinking model (Qwen3.x) with `max_tokens` >= ~200: a tiny budget returns EMPTY content with `finish_reason: length` because reasoning tokens eat it. The answer lands in `content` after reasoning; thinking is in `reasoning_content`. An empty completion at max_tokens=5 is not a failure.
- `systemctl --user restart llama-server` drops any session currently served by it, same as a manual kill — apply the session-safety rule below before touching a live server.
- **"couldn't bind HTTP server socket" on a manual `llama-server` start almost always means the systemd unit already holds the port** — the unit auto-starts on boot and serves the same model. Diagnose with `ss -tlnp | grep :8080` + `systemctl --user status llama-server` before treating it as a config error; if a healthy unit is running, the correct move is to fold the new flags into the unit's ExecStart (`daemon-reload` + `restart`), never a second manual server. A manual run would also be reaped with the shell that launched it.
- After changing serving flags, verify with a real completion, not just `/health`: send one small `/v1/chat/completions` request and read `eval time` in `journalctl --user -u llama-server` — that single number catches CPU-only fallback, bad offload splits, and KV-spill slowness at once. On 2x16GB, full offload (`-ngl 95`) with KV q8_0 gave ~24 tok/s generation where partial offload (`-ngl 44`, f16 KV) gave ~8; prompt processing ~180-560 tok/s is normal, single digits means CPU path.

## Key config knobs (provider entry)

- `discover_models: false` → skip `/v1/models` entirely; use only the configured `models:` as an explicit allowlist (picker shows exactly that, no probe).
- `models_discovered: true` (auto-set by Hermes) → `models:` is Hermes-owned and refreshed on stale probes; never treat it as a user pin.
- Hand-curated `models:` mapping WITHOUT the flag → treated as allowlist for keyless/custom endpoints.
- `extra_headers`, `api_mode`, per-model meta (`context_length`, `prompt_caching`) supported on provider entries.

## Reference

- `references/hermes-model-list-internals.md` — verified internals (code paths, config shapes, diagnosis recipe, this box's environment facts).
- `scripts/kv-fit.py` — run with `~/llama.cpp/llama-env/bin/python scripts/kv-fit.py <model.gguf> [ctx...]` to estimate KV cache GB per context length (f16/q8_0/q4_0) from GGUF arch fields.
- `templates/llama-server.service` — user systemd unit for persistent serving on port 8080.

## Do NOT

- Don't add duplicate `model.default` entries or duplicate GGUF paths to `models:` to fake a multi-model setup — it just creates ghosts that 404.
- Don't restart llama-server with a different `-m` and expect the old picker entry to 'just work' — re-probe or edit the catalog.
- Don't run two 27B GGUFs concurrently on 16Gx2 GPUs without checking VRAM math; you'll get CPU offload or OOM, not a working second model.
