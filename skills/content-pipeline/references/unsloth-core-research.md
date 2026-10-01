# Unsloth Core — verified research 2026-09-10

## Scope
Unsloth **Core** = the original code-based Python fine-tuning library (repo unslothai/unsloth, created 2023-11-29). NOT Unsloth Studio (no-code web UI, Beta, 2026-03-17 — separate draft 2026-09-07) nor Unsloth Desktop (native app wrapper of Studio). Series: Local LLM part 5 (after Ollama laptop/server, LM Studio+Bionic, llama.cpp, Unsloth Studio).

## Verified stats (2026-09-10, GitHub API + README main)
- 75,961 stars / 6,915 forks / 1,316 open issues / pushed 2026-09-10
- **License dual (NEW — README changed since 2026-09-07 draft said plain Apache-2.0): Core = Apache-2.0, Studio UI = AGPL-3.0**
- Latest release v0.1.808-beta (2026-09-09): 250+ bug fixes, 60% smaller binaries, PyTorch 2.11, diffusion 1.2-1.7x faster, AMD Vulkan default (+20% prefill vs ROCm); 5 releases in 2 weeks (v0.1.804→808)

## Core requirements (docs/get-started/fine-tuning-for-beginners/unsloth-requirements)
- Linux/Windows (+WSL), NVIDIA since 2018 GPUs — compute capability 7.0+ (V100/T4/Titan V/RTX 20xx-50xx/A100/H100/L40, Blackwell RTX 50, DGX Spark); AMD/Intel via separate guides; **Apple/MLX = "in the works" for Core** (Mac training goes through Studio/MLX)
- Python 3.11–3.13 (not 3.14); install `uv venv --python 3.13` + `uv pip install unsloth --torch-backend=auto`; advanced pip = torch×CUDA matrix (cu118/cu121/cu124 × torch 2.1-2.5, ampere variants); Docker `unsloth/unsloth` + tag `:core`
- VRAM minimums (QLoRA 4-bit / LoRA 16-bit): 3B 3.5/8GB, 7B 5/19, 8B 6/22, 14B 8.5/33, **27B 22/64**, 32B 26/76, 70B 41/164, 405B 237/950

## Features (README + fine-tuning guide)
- Methods: SFT, LoRA, QLoRA, FFT, pretraining, RL (GRPO/GSPO/DPO/ORPO), FP8, QAT; docs: "LoRA done correctly can match FFT", "train+serve in same precision"
- Models: LLM + diffusion + TTS + embedding + vision
- Performance claims: 2x faster / 70% less VRAM no accuracy loss; MoE 12x faster 35% less VRAM; embedding 1.8-3.3x; Triton RoPE/MLP kernels + padding-free+packing = 3x + 30% less VRAM; 500K ctx on 80GB GPU (20B); 7x longer ctx RL; FastLanguageModel 2x inference; dynamic `unsloth-bnb-4bit` quant = higher accuracy than stock bnb-4bit
- Free Colab/Kaggle notebooks (8B QLoRA on T4 = entry path for no-GPU)
- Export: GGUF (→Ollama/llama.cpp/LM Studio), vLLM (FP8/AWQ multi-user), LoRA adapter ~100MB → HF
- `unsloth start` connects local models to Claude Code/Codex/Hermes (OpenAI/Anthropic-compat)

## Draft status
- Long form: `content-study/posts/20260910-cnt-unsloth-core-finetune-intro.md` (push bd1ea0e)
- Notion Content Drafts DB page `3d7df8d8-8d8c-8170-ad46-c056f60d08fe` (Status: draft, 109 blocks verified read-back incl. tail hashtags; URL https://app.notion.com/p/3d7df8d88d8c8170ad46c056f60d08fe)
- Angle: "loop ปิดของ series" — part 1-4 = รัน (Ollama/LM Studio/llama.cpp/Studio), part 5 = สร้างโมเดลเองแล้ว export GGUF กลับลงเครื่องเดิม; machine math: 2× RTX 5060 Ti (32GB) ≥ 27B QLoRA (22GB) → same box that serves Qwen3.8-27B can fine-tune it
- Promise in draft: real QLoRA 27B benchmark on the user's box before publish (like llama.cpp part)
- Notion pitfall CONFIRMED again: block children pagination param is `start_cursor` (not `cursor`) — 400 validation_error otherwise
