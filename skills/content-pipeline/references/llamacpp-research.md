# llama.cpp research (verified 2026-09-09)

No disambiguation needed — llama.cpp = ggml-org/llama.cpp, the C/C++ LLM inference engine; the only project by that name.

## Verified facts (primary sources, fetched 2026-09-09)
- **README (master)**: goal = "LLM (and VLM) inference with minimal setup and state-of-the-art performance on a wide range of hardware"; plain C/C++ **zero dependencies**; built on **ggml** tensor library; Apple silicon first-class (NEON/Accelerate/Metal); AVX/AVX2/AVX512/AMX x86; RISC-V; **quantization 1.5/2/3/4/5/6/8-bit integer**; custom CUDA kernels + HIP (AMD) + MUSA (Moore Threads); Vulkan + SYCL; CPU+GPU hybrid inference for models > VRAM.
- **17 backends** (README table): BLAS, BLIS, CANN (Ascend NPU), CUDA, HIP, Hexagon (Snapdragon), IBM zDNN, MUSA, Metal, OpenCL (Adreno), OpenVINO (in progress), RPC, SYCL, VirtGPU, Vulkan, WebGPU, ZenDNN.
- **GitHub API stats (2026-09-09)**: 127,574 stars, 22,927 forks, 2,445 open issues, MIT license, created 2023-03-10, active pushes daily. Nightly releases several per day (b10868–b10871 on 2026-09-09 alone).
- **v0.4.0 (published 2026-09-04)**: initial Qwen3.8-Flash-Next (`qwen4exp`, optimization pending) + Nemotron-3-Puzzle-75B support; lazy tensor reading (`--lazy-mode`); per-slot server context limits; video input (mtmd helper); quantizer RAM cap + row-slab streaming (convert big models on low-RAM machines); KV-cell token tracking; sparse flash attention for DeepSeek-V4/GLM; Apple RDMA RPC transport; ggml 0.23.0.
- **llama-server (tools/server/README.md)**: OpenAI-compatible chat/completions/responses/embeddings + **Anthropic Messages API compatible**; reranking endpoint; continuous batching + parallel multi-user; multimodal w/ OpenAI-compat; schema-constrained JSON output; assistant prefill; function calling ~any model; speculative decoding; built-in web UI. New quick-start CLI form: `llama serve -hf ggml-org/Qwen3.5-0.8B-GGUF` (the `-hf` flag pulls from Hugging Face — no separate model hunt).
- **Tools**: cli, completion, server, GBNF grammars (grammar-constrained output beyond JSON schema).

## Research technique that worked (web_extract was search-only this session)
- `https://raw.githubusercontent.com/<org>/<repo>/master/README.md` → clean markdown, no HTML stripping.
- `https://api.github.com/repos/<org>/<repo>` → stars/forks/license/dates (JSON).
- `https://api.github.com/repos/<org>/<repo>/releases?per_page=5` and `/releases/tags/v0.4.0` → full release-note bodies.
- All fetched fine with plain urllib in `execute_code` (GitHub needs a User-Agent header or it 403s).
- Also verified against the LOCAL install: `~/llama.cpp` build, `./build/bin/llama-server --version/--help`, and a running instance (`ss -tlnp` → port 8080, `ps aux` for exact flags, `curl localhost:8080/v1/models` for model + params). Local ground truth > docs when both exist.

## Real benchmark (PHON-SERVER, 2026-09-09)
- Running: `llama-server -m ~/models/Qwen3.8-27B-UD-Q4_K_M.gguf -ngl 44 -t 12 -c 262144 -fa on --split-mode layer --port 8080 --host 0.0.0.0 --jinja` on 2× RTX 5060 Ti (16GB each).
- Measured via POST `/v1/chat/completions` (59 prompt / 150 completion tokens, non-stream): 19.3s total → **~7.8 tok/s including prompt processing** (conservative figure — generation-only is higher).
- Framing used: 27B Q4_K_M file ~16.5GB (vs ~55GB fp16); human reading speed ~5-7 words/s so ~8 tok/s reads comfortably; 7-8B on a single card = 40-60+ tok/s.
- Pitfall noted in draft: VRAM contention matters — other GPU jobs (e.g. ComfyUI models resident) tank tok/s when layers spill to CPU.
- Benchmark method: time a non-streaming chat completion, divide completion_tokens by wall time; state that it includes prompt processing.

## Angle + pro/cons used in draft
- Angle: **"the engine everyone borrows"** — Ollama/LM Studio/etc. use llama.cpp underneath; the missing layer of the local-LLM picture; series Local LLM part 4 (Ollama laptop → Ollama server → LM Studio+Bionic → llama.cpp → Unsloth Studio).
- Pros: $0/MIT/no phone home; most portable (17 backends, phone→mainframe→browser, single binary); finest performance control (quant grades, layer split, batch/ctx/thread) — why serious local benchmarks run on it; OpenAI+Anthropic API compat; very alive project; birthplace of GGUF.
- Cons: CLI-first, no real GUI; overwhelming flag surface (`--help` thousands of lines); full self-management of models/VRAM; brand-new architectures land as "initial support" before optimization; no multi-tenancy/auth/quota (inference engine only); not a frontier-quality competitor — wins on $0/token for routine work.
- Who it's for (4 profiles): dev wanting a real local API server; odd hardware (AMD/Intel Arc/NPU/Snapdragon); performance optimizers; local-first app builders. NOT for: casual first-timers (→ Ollama/LM Studio), teams needing multi-tenant platform (→ vLLM).

## Draft status
- `content-study/posts/20260909-cnt-llama-cpp-engine-intro.md` (push a175acc). Notion Content Drafts page `3d6df8d8-8d8c-8165-9aff-dc40e9f3d832` (81 blocks, has_more=False, verified read-back incl. 9 headings + tail hashtags; Status: draft; URL https://app.notion.com/p/llama-cpp-Engine-Local-LLM-introduction-features-pros-cons-3d6df8d88d8c81659affdc40e9f3d832). index.json 260.
- Possible follow-ups: short version for FB/Threads; "llama.cpp flags that matter" cheat-sheet post; Unsloth-exported GGUF → llama-server end-to-end post (closes the series loop).
