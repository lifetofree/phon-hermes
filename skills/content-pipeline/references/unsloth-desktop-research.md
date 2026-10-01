# Unsloth Desktop — verified research 2026-09-10

## Scope
Unsloth **Desktop** = native app (Tauri) wrapping Studio + Core, for macOS/Windows/Linux. Part of 3-product family (Core=Python lib, Studio=web UI, Desktop=native app). Local LLM series part 6 (after Core=part 5).

## Verified facts (2026-09-10, primary)
- **Launch: 2026-08-11/13** — substack post dated Aug 11 2026; first GitHub desktop releases v0.1.70x-beta ("Unsloth Desktop is here!") 2026-08-11/13. Still **Beta**. Latest v0.1.808-beta (2026-09-09).
- **Downloads (v0.1.808 assets, 1 month in): Windows .exe 21MB = 4,691 dl (dominant), ARM64 22.2MB = 1,032, Ubuntu.deb 24.2MB = 612, Linux.AppImage 178.2MB = 636, macOS .dmg 22.5MB = 557** — Linux AppImage is 8x bigger than Windows (bundles backends).
- **Tauri-based** (not Electron) — "Install it, download models and start chatting", no setup required.
- Three roles: **Run** (100% offline chat, parallel chatting, self-healing tool calls +50% accuracy claim, sandboxed Bash/Python, permission controls like Claude Code/Codex, unlimited private web search + Deep Research, MCP server, OpenAI-compat API, LAN + free Cloudflare HTTPS, Connect Providers = OpenAI/Anthropic/vLLM/Ollama in same chat), **Train** (no-code: PDF/CSV/JSON → dataset → LoRA/QLoRA/FFT/pretrain; text+diffusion+audio+embedding; 2x faster/70% less VRAM = Core engine; multi-GPU; export GGUF/safetensors/LoRA), **Create** (image FLUX/Z-Image/LTX/Wan + own LoRAs; video diffusion — docs number: MiniMax-H3 FP8 on B200 960×544 124-frame 8-step 70+s→13s; audio TTS/STT Whisper/Qwen3-ASR; train diffusion LoRA in-app).
- **Day-zero support**: Qwen3.8-27B, Kimi K3, DeepSeek-V4 Flash, Muse Glimmer (Meta Superintelligence Labs), Gemma 4, MiniMax-H3; stands on llama.cpp + HF + Unsloth Dynamic GGUFs (Qwen3.8-Flash-Next 125B on 75GB RAM).
- **FAQ (docs/desktop, direct quotes)**: "No telemetry"; app runs fully offline; existing models (Ollama/HF cache) auto-detected; GPU NOT required (CPU/Mac setups work); "Older hardware however may not be well supported"; inference slower with web search/tool healing on → "turn them off and speed should match any other llama.cpp app".
- License dual: Core=Apache-2.0, Studio UI=AGPL-3.0 (same as Core part). Free, no tiers.
- Cross-ref: VRAM table from unsloth-core-research.md (27B QLoRA 22GB), unsloth-studio-research.md (Data Recipes, agentic layer), llamacpp-research.md (engine, 127k stars).

## Draft status
- Long form: `content-study/posts/20260910-cnt-unsloth-desktop-intro.md` (pushed)
- Notion Content Drafts page `3d7df8d8-8d8c-818e-a12f-f980509200ad` (Status: draft, 99 blocks verified read-back incl. tail hashtags; URL https://app.notion.com/p/3d7df8d88d8c818ea12ff980509200ad)
- Angle: "เครื่อง 3 เครื่องในเครื่องเดียว" — closes the series: part 1-5 = individual pieces, part 6 = one app with run+train+create, zero setup; comparison table vs Ollama/LM Studio/Studio(web); 4 who-it's-for + 4 skip-to; promise in draft: real install + report numbers before publish.
