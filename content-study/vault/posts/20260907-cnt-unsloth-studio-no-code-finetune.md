# Unsloth Studio — Fine-tune AI บนเครื่องตัวเอง ไม่ต้องเขียนโค้ด ไม่ต้องเช่า GPU

<!--
ContentID: 20260907-CNT-UNSLSTH-STUDIO-LF
Series: (standalone — ข้ามอ้างอิง series Ollama/Local LLM ได้ แต่ไม่ใช่ภาคต่อ)
Type: Long Form (~2000-2500 words)
Status: Draft — รอ review
Sources (verified 2026-09-07):
- https://unsloth.ai/docs/new/studio (intro: Beta launch, no-code web UI, run GGUF/MLX/diffusion local, train 500+ models 2x faster / 70% less VRAM, 10 features)
- https://unsloth.ai/docs/new/studio/install (install: Desktop app or curl install.sh, port 8888, password first run, --secure = Cloudflare HTTPS, -H 0.0.0.0 LAN)
- https://unsloth.ai/docs/new/studio/start (get started: chat offline, model selection from HF, GGUF quant pick, connect to Claude Code/Codex)
- https://unsloth.ai/docs/new/studio/data-recipe (Data Recipes: PDF/CSV → synthetic dataset, visual graph-node workflow, powered by NVIDIA Nemo Data Designer, export/import recipes)
- https://unsloth.ai/docs/new/studio/export (export trained checkpoint → GGUF / 16-bit safetensor / LoRA adapter; deploy to llama.cpp, Ollama, vLLM, LM Studio)
- https://unsloth.ai/docs/get-started/fine-tuning-for-beginners/unsloth-requirements (3 modes: Desktop/Studio/Core; Windows 10/11 + NVIDIA, Python 3.11-3.13 (not 3.14); macOS 12+ Intel/Apple Silicon full training+MLX+GGUF; Linux Ubuntu 20.04+ CUDA 12.4+/12.8+ blackwell; CPU-only = Chat + Data Recipes only)
- https://unslothai.substack.com/p/introducing-unsloth-studio (launch post 2026-03-17, Beta)
- https://api.github.com/repos/unslothai/unsloth (Apache-2.0, 75,748 stars, 6,895 forks, 1,352 open issues, repo created 2023-11-29, push 2026-09-07; latest release v0.1.806-beta 2026-09-02: MTP 2x for Qwen3.8-Flash/GLM-5.3-Flash, 170+ improvements)
Vendor: Unsloth (Unsloth AI), Apache-2.0, free & open source
Note: "Unsloth" = fine-tuning library (2023, 75k stars); "Unsloth Studio" = web UI launched 2026-03-17 (Beta); "Unsloth Desktop" = native app wrapper
-->

## 00: Hook — "Fine-tune เคยเป็นเรื่องของคนที่เขียน Python เก่ง… ตอนนี้มันคือปุ่มใน browser"

ทุกคนที่เล่น local LLM จะชนกำแพงเดียวกัน: model ที่โหลดมา (Qwen, Gemma, GLM) มัน "smart ทั่วไป" แต่ไม่รู้จัก domain ของคุณ — ไม่รู้ format เอกสารบริษัท, ไม่รู้ tone ของแบรนด์, ไม่รู้ workflow ของทีม

วิธีแก้ที่ "ถูกต้อง" คือ fine-tuning — แต่มันเคยต้องการ 3 อย่าง:
1. เขียน Python (LoRA, trainer, dataset collator, hyperparameters)
2. เช่า GPU บน Colab/cloud (A100 $2-3/ชม.)
3. Data preparation ด้วยมือ (format JSONL, split, validate)

วันนี้กำแพงทั้ง 3 หายไป — **Unsloth Studio** คือ no-code web UI ที่ fine-tune open model บนเครื่องตัวเอง: upload PDF/CSV → build dataset เป็น visual node → press train → export GGUF — ทั้งหมดใน browser บน port 8888

บทความนี้จะเล่าครบ: มันคืออะไร, ทำงานยังไง, features, ราคา (ฟรี), ข้อดีข้อเสียตรงๆ, เทียบ Ollama/LM Studio/Unsloth Core, และเหมาะกับใคร

## 01: Unsloth Studio คืออะไร — "Control plane สำหรับ local LLM"

> Unsloth Studio = open-source (Apache-2.0) web UI บนเครื่องคุณ ที่รวม **run + fine-tune + export + agent tools** ของ open models ไว้ที่เดียว — เบื้องหลังคือ Unsloth runtime (2x faster training, 70% less VRAM) + inference engine

แยกเป็น 3 ตัวให้ชัด (คนสับสนบ่อย):

| ตัว | คืออะไร | ใช้เมื่อ |
|---|---|---|
| **Unsloth Core** | Python library (2023, 75,748 stars) | คนที่เขียนโค้ดเอง, Colab |
| **Unsloth Studio** | Web UI (2026-03, Beta) | คนที่ไม่อยากเขียนโค้ด — บทความนี้ |
| **Unsloth Desktop** | Native app (macOS/Windows/Linux) | ติดตั้งง่ายสุด — Studio อยู่ในนี้ |

key insight: **Ollama/LM Studio = inference layer (รัน model)** — **Unsloth Studio = training + inference + agent layer (สอน model + รัน + ต่อ agent)** — มันเติมชั้นที่ runtime ทั่วไปไม่มี

## 02: มันทำงานยังไง — 3 workflow

**Workflow 1: Chat / Inference (เหมือน LM Studio แต่ +agentic)**
- เปิด browser → `http://127.0.0.1:8888` (ตั้ง password ครั้งแรก)
- ค้นหา model จาก Hugging Face ตรงใน app หรือใช้ local files — GGUF, safetensors, fine-tuned adapters
- เลือก quantization ตาม RAM/VRAM (เช่น UD-Q4_K_XL)
- chat 100% offline — upload documents/images/audio, tune temperature/top-p/top-k/system prompt, **compare outputs ของ 2 model ข้างกัน**

**Workflow 2: Fine-tune (killer feature — no-code)**
- ขึ้น training page — เลือก base model + training type: **QLoRA / LoRA / full fine-tuning** (defaults กรอกให้แล้ว)
- **Data Recipes** — upload PDF/CSV/JSON/DOCX/TXT → app สร้าง synthetic dataset ให้อัตโนมัติ — edit เป็น **visual graph-node workflow** (powered by NVIDIA Nemo Data Designer) — validate → preview sample rows → run full build
- Train — **live progress, GPU stats, charts** — ไม่ต้องเปิด Jupyter ดู log
- จบ = checkpoint + adapters

**Workflow 3: Export + Deploy**
- เลือก training run → checkpoint → export: **GGUF / 16-bit safetensors / LoRA adapter**
- ใช้ได้ตรงๆ กับ **llama.cpp, Ollama, vLLM, LM Studio** — model ที่ train มาจาก Studio = deploy เข้า ecosystem ที่คุณใช้อยู่แล้ว

## 03: Features เด่น (verified จาก docs)

1. **No-code fine-tuning** — QLoRA/LoRA/full fine-tune จาก UI, config tools สำหรับ splits/column mapping/hyperparameters + YAML
2. **Data Recipes** — document → structured dataset, visual workflow, recipes export/import ได้ (share workflow กับคนอื่น)
3. **Self-healing tool calling + sandboxed code execution** — LLM รัน Bash + Python ใน sandbox (ไม่ใช่แค่ JavaScript) — model test code, generate files, verify คำตอบด้วย real computation — "50% more accurate tool calls" (claim ของ Unsloth)
4. **Private web search ใน agent** — unlimited, ไป visit หน้าเว็บจริง (ไม่ใช่แค่ scan summary) — search เกิดขึ้นใน thinking trace ของ model
5. **API endpoint** — local LLM ของคุณต่อ **Claude Code, Codex, Hermes, OpenClaw, OpenCode** ได้ — หรือ connect provider ภายนอก (OpenAI/Anthropic/vLLM) เข้ามาใน Studio — model swapping ได้
6. **Remote access** — `unsloth studio --secure` = **HTTPS ผ่าน free Cloudflare tunnel** (ทำงานได้บน Windows/Mac/Linux) — หรือ `-H 0.0.0.0` สำหรับ LAN
7. **Multi-modal** — run/train: text, diffusion image/video (เช่น MiniMax H3), TTS audio, embedding models
8. **Mac-first training** — **MLX training + GGUF inference บน Apple Silicon** — macOS 12+ (Intel ได้ด้วย) — จุดที่ runtime อื่นส่วนใหญ่ไม่มี
9. **500+ models** — Qwen3.8, DeepSeek-V4, GLM-5.3, Gemma 4, Kimi K3, Muse Glimmer — + MTP (Multi-Token Prediction) 2x faster สำหรับ flash models (v0.1.806)
10. **Integrations** — Python SDK, curl/HTTP, VS Code, MCP server, Docker

## 04: Pricing — ฟรี + open-source (และเบื้องหลัง)

| | รายละเอียด |
|---|---|
| ราคา | **ฟรี 100%** — Apache-2.0, ไม่มี tier, ไม่มี license key |
| GPU | ของคุณเอง (training) — หรือ free Colab notebook (team ให้) |
| Cloud | ไม่มี cloud service — remote access = Cloudflare tunnel ของคุณ (ฟรี) |
| Update | Free — latest release v0.1.806-beta (2026-09-02) |

เบื้องหลัง: Unsloth เป็น fine-tuning library ที่คนใน ecosystem ใช้กันมานาน — **75,748 stars ใน GitHub** (repo สร้าง 2023), 6,895 forks, active push **วันนี้** (2026-09-07) — Studio = การห่อ unsloth ที่ people trust อยู่แล้วให้เป็น no-code — 170+ improvements ใน release ล่าสุด (multi-GPU planning, AMD/ROCm detection, MCP/Deep Research reliability)

## 05: ข้อดี ✅

- **No-code fine-tuning ที่ real** — ไม่ใช่ demo — QLoRA/LoRA/full + data pipeline + export ครบ — ระดับที่ раньше ต้องเขียน Python 100+ lines
- **2x faster training, 70% less VRAM** (claim ของ Unsloth, no accuracy loss) — model ที่เช่า A100 $3/ชม. ทำได้บน RTX 4090/5060 Ti ของคุณ
- **Data Recipes จาก documents** — PDF/CSV ที่คุณมีอยู่แล้ว = training data ได้เลย — visual workflow ที่ debug/preview ได้
- **ฟรี + open-source (Apache-2.0)** — ตรวจสอบ code ได้, ไม่มี vendor lock-in
- **Agent features ที่ inference-only tools ไม่มี** — self-healing tool calls, sandboxed code, private web search — local model ที่ใช้กับ Claude Code/Codex/Hermes ได้
- **Mac/MLX support** — train บน Apple Silicon ได้ — ครอบคลุม Mac → Windows → Linux + NVIDIA/AMD/Intel
- **Ecosystem bridge** — export GGUF เข้า Ollama/llama.cpp/LM Studio/vLLM — train ที่นี่ deploy ที่นั่น
- **Active + big community** — 75k stars, 1,352 issues (สัญญาณว่าคนใช้จริงเยอะ), release cycle เร็ว

## 06: ข้อเสีย ❌ — ตรงๆ ไม่อวย

- **ยัง Beta** — Studio เปิดตัว 2026-03-17 (~6 เดือน) — features ใหม่ (agentic, data recipes) ยังอยู่ใน polish stage — 1,352 open issues = bug อยู่ (normal สำหรับ project ที่โตเร็ว)
- **Training ต้องมี GPU** — CPU-only = Chat + Data Recipes เท่านั้น (export "coming soon") — Windows training = **NVIDIA เท่านั้น** — คนที่ไม่มี GPU = ใช้ Colab notebook แทน (ต้อง upload/download weights)
- **VRAM ceiling ยังอยู่** — 70% less VRAM ก็ยังเป็น 70% ของจำนวนเดิม — full fine-tune 27B ต้องการ VRAM ใหญ่ (QLoRA ช่วย) — 5060 Ti 16GB = QLoRA 7-14B สบาย, 27B ต้องวัด
- **ไม่ใช่ production serving** — Studio = control plane — ถ้าจะ serve production multi-user → vLLM/Ollama ยังเป็น answer (Studio export เข้าไปตรงๆ — complement ไม่ใช่ compete)
- **Port 8888 + password = basic auth** — `--secure` (Cloudflare) ดีกว่า localhost — แต่ multi-tenant/SSO ไม่มี — plan access เอง
- **Windows = setup หนักกว่า** — ต้อง Python 3.11-3.13 (3.14 ไม่ได้), CUDA toolkit, build tools (setup script ช่วย แต่ steps เยอะกว่า Mac)
- **Data recipes ยังไม่มี "template library" ใหญ่** — มี learning recipes + community sharing ผ่าน Discord — workflow niche เฉพาะตัวต้อง build เอง
- **No experiment tracking ระดับ MLOPT** — live progress/charts มี แต่ W&B-style tracking/compare runs ลึกๆ ยังไม่ใช่จุดแข็ง

## 07: เทียบกับคู่แข่ง

| | Unsloth Studio | Ollama | LM Studio | Unsloth Core (code) | Colab + notebooks |
|---|---|---|---|---|---|
| Price | ฟรี (OSS) | ฟรี (OSS) | ฟรี (proprietary) | ฟรี (OSS) | ฟรี (GPU limited) / $ |
| **Fine-tuning** | ✅ no-code | ❌ | ❌ | ✅ code | ✅ code |
| Chat/inference | ✅ GGUF/MLX | ✅ | ✅ | ✅ | ✅ |
| Agentic tools | ✅ self-healing + sandbox | ❌ | ❌ | ⚠️ manual | ⚠️ manual |
| Data prep | ✅ visual recipes | ❌ | ❌ | manual | manual |
| Export GGUF | ✅ | — | — | manual | manual |
| Mac MLX training | ✅ | ❌ | inference เท่านั้น | ⚠️ | ❌ |
| Learning curve | Low (UI) | Very low | Very low | High | High |

**Bottom line:** Ollama = serve, LM Studio = playground, **Unsloth Studio = train + serve + agent** — ถ้าต้องการ fine-tune = ไม่มีตัวอื่นใน tier no-code นี้ (ตัวเลือกคือเขียน code เอง)

## 08: เหมาะกับใคร (Pro Tips แยกตามระดับ)

**มือใหม่ / คนอยากลอง fine-tune ครั้งแรก** — ลง Desktop app → เลือก Qwen3.5 4B หรือ Gemma 4 2B → upload PDF 5-10 หน้า → Data Recipe → QLoRA defaults → train → export GGUF → chat กับ model ของคุณ — 1-2 ชม. ครั้งแรก

**Dev/creator ที่ทำ local AI stack** — train model สำหรับ domain (format เอกสาร, tone) → export LoRA → deploy เข้า Ollama/llama.cpp (เครื่องเดิม) → connect Claude Code/Hermes เข้า Studio API — local model ของทีมที่ "รู้เรื่อง" ของคุณ

**Mac user (Apple Silicon)** — MLX training = ทางที่ง่ายสุดในการ train บน Mac — ไม่ต้อง rent GPU — 16GB unified memory = QLoRA 7-14B — 32GB = 27B

**ไม่เหมาะ:**
- **ไม่มี GPU เลย** — ใช้ Colab notebook ของ Unsloth แทน (แต่ upload/download เหนื่อย)
- **ต้องการ production multi-user serving** — vLLM/Ollama + Ollama server (ดู part 2 Ollama series) — Studio ใช้ train เท่านั้น
- **ต้องการ MLOps/enterprise tracking** — ยังไม่พอ — ใช้ platform ที่ครบกว่า
- **Windows + AMD/Intel GPU** — training Windows = NVIDIA only (AMD/Intel ใช้ทาง Linux/WSL)

## 09: สรุปแบบวิศวกรเป็ด

Unsloth Studio = **"fine-tuning ที่เคยเป็น script กลายเป็น button"** คับ — no-code training pipeline (data recipes → QLoRA/LoRA/full → live monitor → export GGUF) + agentic layer (self-healing tool calls, sandboxed code, private web search) + Mac/MLX support — ทั้งหมด free + Apache-2.0 + 75k stars community

exchange ที่ต้องแลก: **ยัง Beta (6 เดือน), training ต้องมี GPU, ไม่ใช่ production serving, Windows setup หนัก** — แต่ใน tier "no-code local fine-tuning" นี้ **ยังไม่มีตัวที่สอง**

**ระบบ > rent:** ปล่อยให้ machine ของคุณ train model (local, 5060 Ti/4090/Apple Silicon) แล้วใช้ Colab/cloud เฉพาะตอน VRAM ไม่พอ — คุมได้, พอรอด, data ของคุณไม่ออกจากเครื่อง (ยกเว้นตอน pull model)

ถ้าคุณอยู่ใน ecosystem local LLM (Ollama, llama.cpp, LM Studio) — Unsloth Studio คือชั้น "training" ที่ขาดไป — train ที่นี่, deploy ที่ ecosystem เดิม

#Adduckivity #DuckOS #NeuroDivergent #Unsloth #FineTuning #LocalLLM #NoCode #QLoRA #MLX #AIDev #OpenSource
