# Ollama research (verified 2026-09-05)

Disambiguation: user asked for "Olamma" — no product by that name exists; it is a typo for **Ollama** (dominant local-LLM runtime, matches user's own llama.cpp local setup). Drafted for Ollama.

## Key current angle (fresh vs most older tutorials)
Ollama is now **local + cloud dual-mode in one runtime**, NOT just the old free local CLI:
- Local: `ollama run <model>` — weights download to your machine, inference on CPU/GPU, offline, no API key, no per-token bill, **data never leaves the machine** ("data stays yours").
- Cloud: `ollama run <model>:cloud` — larger models hosted by Ollama in US/Europe/Singapore; prompts NOT trained on. Same commands, same integrations, one token switch.
This is the content hook: most 2024/25 "run a local LLM" posts predate the cloud tier + peak pricing.

## Verified sources (all fetched 2026-09-05)
- https://ollama.com/ — homepage: "9M+ developers", Reliably fast (195.6 tok/s DeepSeek v4 Flash vs providers 63–97.6), frontier open models, integrations (Claude Code, Codex, OpenCode, Hermes Agent, OpenClaw, VS Code, Pi, n8n), privacy (prompts never tracked/trained; cloud hosted US/EU/SG), pricing tiers.
- https://ollama.com/docs — docs index; **docs now live at `docs.ollama.com`** (https://ollama.com/llms.txt is the index; `ollama.com/docs/quickstart` is 404 — the real path is `https://docs.ollama.com/quickstart`). Capabilities: streaming, thinking, structured outputs, vision, embeddings, tool calling, web search.
- https://docs.ollama.com/quickstart — install (macOS/Windows/Linux), `ollama` opens interactive menu, `ollama run gemma4`, `ollama run gemma4:cloud`, `/bye`.
- https://ollama.com/blog/new-app — macOS/Windows desktop app: file drag-and-drop (text/PDF/code), multimodal (e.g. Gemma images), context length setting (more memory for long docs).
- https://ollama.com/pricing — see pricing below.
- https://ollama.com/models — library examples (2026-09): qwen3.8 (27b, vision/tools/thinking), gemma4 (e2b–31b, vision/tools/thinking/audio), glm-5.3 + glm-5.3-flash (Z.ai, cloud, tools/thinking), muse-glimmer (Meta 30b, Apache 2.0, always-on local agent), nemotron-3.5-lightning (NVIDIA 30b/3b-active MoE), granite4.2 (IBM 3b–30b, RAG/JSON, Apache 2.0), ornith-1.5.

## Pricing (2026-09, ollama.com/pricing)
| Tier | Price | Includes |
|---|---|---|
| Free | $0 | local models (always free) + starter usage credits |
| Pro | $20/mo ($200/yr → $16.67/mo annual) | $60 usage credits/mo, larger pro models, concurrent runs, fast mode (coming soon) |
| Max | $100/mo | $300 credits/mo, early access, 10 concurrent requests |
| Team | $500/mo | unlimited users, $1,000 shared credits/mo, centralized billing, priority support |
| Enterprise | custom | model access controls, cost budgets, private Slack, security questionnaires |

Per-1M-token model prices (input / cached / output): glm-5.3 $1.40/$0.26/$4.40 · deepseek-v4-flash $0.22/$0.007/$0.66 · gpt-oss:20b $0.07/$0.035/$0.30 · nemotron-3-super $0.015/$0.015/$0.60 · kimi-k3 $3.00/$0.30/$15.00.
**Peak pricing** 12:00–18:00 UTC Mon–Fri (e.g. deepseek-v4-flash input $0.22→$0.44). Angle: schedule heavy jobs off-peak.

## Pro/cons framing used in the draft
Pros: data-stays-yours (local), free/no per-token bill, offline, simple + fast, open weights (no closed-API lock-in), dual mode (scale to cloud when needed).
Cons: hardware-dependent (RAM/VRAM; longer context = more memory), local open models still below top closed on hardest reasoning, cloud mode = data LEAVES the machine (privacy pitch is local-only), cloud pricing new + peak hours, it's a runtime not a full agent (pair with Claude Code/Hermes/Open WebUI), model list turns over fast.

## Draft status
`content-study/posts/20260905-cnt-ollama-local-llm-intro.md` (pushed 9c1868c). Notion Content Drafts filing was BLOCKED pending user approval (curl POST held, approval prompt timed out) — payload at /tmp/ollama_payload.json, DB 3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520, Status: draft. Resume: `curl -X POST .../v1/pages -d @/tmp/ollama_payload.json` then read back + give URL. Possible follow-up: short-version post + a "local vs cloud" cost comparison.

## Part 2 (server/datacenter) — done 2026-09-07
- Draft: `content-study/posts/20260907-cnt-ollama-local-llm-server-datacenter.md` (push e1750cb); Notion Content Drafts page `3d4df8d8-8d8c-8139-a89f-cf4038cbdde0` (71 blocks, verified read-back, Status: draft)
- Verified additions (docs.ollama.com, fetched 2026-09-07): API base `http://localhost:11434/api` (cloud twin `https://ollama.com/api`); endpoints generate/chat/embed/tags/show/create/copy/pull/push/delete/version; **OpenAI-compatible + Anthropic-compatible** endpoints; API stable/backwards-compat. Docker: CPU-only, `--gpus=all` + NVIDIA Container Toolkit, AMD `:rocm` tag, Vulkan bundled & on by default, JETSON_JETPACK env. Multi-GPU: `CUDA_VISIBLE_DEVICES` by UUID (`nvidia-smi -L`), force CPU with `-1`; Linux suspend/resume UVM bug workaround `sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm`. GPU list: RTX 50xx (Blackwell 12.0) → H100/H200 (9.0) → A100 (8.0) → V100 (7.0) → GTX 10xx (6.x).
- Angle: team 5-50 builds own AI infra — per-token $0, capex $2-3.5k (1×4090), admin 2-4 hr/week, no multi-tenancy (DIY proxy), open models < closed frontier. Compared vs cloud API / vLLM-TGI / Ollama cloud tier.
- Part 1 (laptop) Notion page `3d2df8d8-8d8c-81dc-87db-fbc91cf9e1d1`. Series complete (2/2).