# Unsloth Studio — verified research 2026-09-07

## Disambiguation
User typed "Unsloth Studio" (typo'd twice, then confirmed 2x = Unsloth NOT LM Studio). **Unsloth Studio** = open-source no-code web UI for training/running/exporting open models, launched 2026-03-17 (Beta) by the Unsloth team (the 2023 fine-tuning library, 75,748 stars). NOT to confuse with LM Studio (separate tool by Element Labs).

## Three products (people confuse)
- **Unsloth Core** — Python fine-tuning library (2023, 75,748 stars, Apache-2.0), code-based, Colab.
- **Unsloth Studio** — web UI (2026-03-17 Beta), no-code, browser on port 8888.
- **Unsloth Desktop** — native app (macOS/Windows/Linux) wrapping Studio, easiest install.

## Verified sources (fetched 2026-09-07)
- https://unsloth.ai/docs/new/studio — intro: run GGUF/MLX/diffusion local, train 500+ models 2x faster / 70% less VRAM (no accuracy loss), self-healing tool calling + sandboxed code, private web search, API endpoint for Claude Code/Codex/Hermes, no-code training, export GGUF/safetensors, Cloudflare HTTPS remote.
- https://unsloth.ai/docs/new/studio/install — install: Desktop app OR `curl -fsSL https://unsloth.ai/install.sh | sh`; starts `http://127.0.0.1:8888`, first-run password; `unsloth studio --secure` = free Cloudflare HTTPS tunnel (Win/Mac/Linux); `-H 0.0.0.0` for LAN.
- https://unsloth.ai/docs/new/studio/start — chat 100% offline, pick model from HF search or local files, choose GGUF quant (e.g. UD-Q4_K_XL), connect to Claude Code/Codex.
- https://unsloth.ai/docs/new/studio/data-recipe — **Data Recipes**: upload PDF/CSV/JSON/DOCX/TXT → synthetic dataset, **visual graph-node workflow**, powered by **NVIDIA Nemo Data Designer**; validate→preview→run; recipes export/import.
- https://unsloth.ai/docs/new/studio/export — export trained checkpoint → GGUF / 16-bit safetensors / LoRA adapter; deploy to llama.cpp, Ollama, vLLM, LM Studio.
- https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements — 3 modes (Desktop/Studio/Core). Training: NVIDIA/AMD/Intel + Mac. Windows 10/11 + NVIDIA (NO WSL needed), Python 3.11–3.13 (NOT 3.14). macOS 12+ (Intel or Apple Silicon) full training+MLX+GGUF. Linux Ubuntu 20.04+, CUDA 12.4+ (12.8+ Blackwell). **CPU-only = Chat + Data Recipes only** (export "coming soon").
- https://unslothai.substack.com/p/introducing-unsloth-studio — launch 2026-03-17, Beta.
- GitHub unslothai/unsloth: Apache-2.0, 75,748 stars, 6,895 forks, 1,352 open issues, created 2023-11-29, push 2026-09-07. Latest release v0.1.806-beta (2026-09-02): MTP 2x for Qwen3.8-Flash-Next/GLM-5.3-Flash, 170+ improvements (multi-GPU, AMD/ROCm, MCP/Deep Research).

## Pricing
Free 100%, Apache-2.0, no tiers. Training on your own GPU (or free Colab notebook). No cloud service; remote access = your own free Cloudflare tunnel.

## Pro/cons framing used in draft
Pros: real no-code fine-tuning (QLoRA/LoRA/full + data pipeline + export), 2x faster / 70% less VRAM, Data Recipes from documents, free OSS, agentic features inference-only tools lack, Mac/MLX training, ecosystem bridge (export GGUF), big active community.
Cons: still Beta ~6 months (1,352 issues), training needs GPU (CPU-only = chat+data only; Windows training = NVIDIA only), VRAM ceiling still exists, not production serving (vLLM/Ollama for that), basic auth (no SSO/multi-tenant), Windows setup heavy (Python 3.11-3.13 + CUDA + build tools), no big recipe template library, no MLOPS-grade experiment tracking.

## Draft status
- Long form: `content-study/posts/20260907-cnt-unsloth-studio-no-code-finetune.md` (push fb9e401)
- Notion Content Drafts DB page `3d4df8d8-8d8c-812e-8816-fc5ba5623c13` (Status: draft, 77 blocks verified read-back)
- Angle: "Fine-tuning ที่เคยเป็น script กลายเป็น button"; standalone (not a series part)
- Potential follow-ups: short social version, or "Unsloth Studio + Ollama server" combined workflow (train in Studio → deploy in Ollama).