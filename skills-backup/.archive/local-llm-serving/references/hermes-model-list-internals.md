# Hermes local model list internals (verified 2026-09-05)

Source: this box's config.yaml + hermes-agent source (hermes_cli/model_switch.py, hermes_cli/config.py).

## How the model list in `/model` and `hermes model` is built

1. Provider entry in `custom_providers` (or `providers:` dict) with `base_url` pointing at an OpenAI-compatible endpoint (llama.cpp, Ollama, LM Studio, ...).
2. Hermes probes `GET {base_url}/v1/models` and **persists the result** into the provider entry:
   ```yaml
   - name: local:8080
     base_url: http://localhost:8080/v1
     models:
       /home/lifetofree/models/Qwen3.8-27B-GSQ-RCO-IQ3_S.gguf: {}
     models_discovered: true
   ```
   Written by `_save_discovered_models_to_config` (model_switch.py). It rewrites `entry["models"] = {model_id: {} ...}` and sets `models_discovered: True` only when the list is stale; it never overwrites a hand-curated (non-discovered) mapping.
3. `models_discovered: true` marks the `models` mapping as **Hermes-owned** (auto-discovered, not a user allowlist). A hand-curated dict/list WITHOUT the flag is treated as an allowlist for keyless endpoints (`_allowlist_shapes` in model_switch.py).
4. Separate cache file: `~/.hermes/provider_models_cache.json`, keyed by provider fingerprint; used to dedupe refreshes.

## The 'ghost model' symptom

**Symptom:** model picker shows 2 models (or a model that errors when used) while only one is actually loaded on the server.

**Cause:** the picker merges the persisted `models:` catalog (stale — from a previous probe when a *different* quant/version was loaded) with the live `/v1/models` probe. llama.cpp `llama-server` serves exactly ONE model per instance (`-m <file>`), so the old entry in config is a ghost — selecting it 404s because the server has no such model loaded in this session.

**Diagnosis recipe:**
```bash
# what the server ACTUALLY has loaded right now
curl -s http://localhost:8080/v1/models
# what Hermes thinks the catalog is (entry + models_discovered)
grep -A8 "local:8080" ~/.hermes/config.yaml
# the persisted per-provider cache
python3 -c "import json; print(json.load(open('$HOME/.hermes/provider_models_cache.json')))"
```

**Fixes:**
- `/model --refresh` (or `--refresh` flag) forces a re-probe; overwrites the stale `models:` mapping when it's Hermes-owned (`models_discovered: true` or legacy `__discovered_model_catalog__` sentinel).
- Hand-edit: delete the dead entry from `models:` in config.yaml.
- Drop `models_discovered` and pin `models:` yourself → it becomes an explicit allowlist (picker shows only what you list; no live probe for keyless endpoints).
- `discover_models: false` on the provider entry → skip `/v1/models` entirely, use only the configured `models:` (website/docs/user-guide/configuring-models.md).

## Serving multiple models at once

llama.cpp options (verified from `llama-server --help`, build 0eadefebd):
- **Two servers, two ports** (simplest): port 8080 + 8081, each `-m <file>`; add two provider entries to config.yaml. VRAM cost is the sum of both models — check `nvidia-smi` first.
- **Router mode** (one server): `llama-server --models-dir ~/models --models-max 2` (max simultaneous loads; `--models-preset PATH.ini` for INI presets; `--models-autoload` default on). `/v1/models` then lists loaded models.
- VRAM arithmetic on 16G x2 GPUs: two 27B GGUF quants (~11G + 16G) + KV context does NOT fit comfortably; expect CPU offload (slow) or `--split-mode layer` (default) across both GPUs. One 27B + one small model (e.g. 4B) fits; two 27Bs does not.

## Environment facts (this box, 2026-09-05)
- llama.cpp: `~/llama.cpp`, binaries `~/llama.cpp/build/bin/llama-server|llama-cli`, run with no venv.
- Current provider: `model.provider: custom`, `base_url: http://localhost:8080/v1`, key via env `HERMES_CUSTOM_LOCALHOST_8080_API_KEY`; fallback provider zai/glm-5.3.
- `model.default` = full file path of the GGUF (works because llama.cpp reports model ids as the file path).
- ComfyUI plan: port 8188, GPU 0; Hermes LLM should use GPU 1 (`CUDA_VISIBLE_DEVICES=1 llama-server ...`) once ComfyUI models finish.
