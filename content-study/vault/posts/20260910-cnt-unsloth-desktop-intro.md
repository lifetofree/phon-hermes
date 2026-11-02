# Unsloth Desktop — "App เดียว ครบทั้ง รัน เทรน และ สร้าง" (Local LLM part 6)

<!--
ContentID: 20260910-CNT-UNSLOTHDESKTOP-LF
Series: Local LLM (part 6) — ต่อจาก Ollama (laptop / server), LM Studio (+Bionic), llama.cpp, Unsloth Studio, Unsloth Core
Type: Long Form
Status: Draft — รอ review
Sources (researched 2026-09-10, primary):
- unsloth.ai/docs/desktop (fetch 2026-09-10) — "Unsloth Desktop (Beta) is a free, open-source app...", Tauri based, features, FAQ (no telemetry, offline, GPU not required, OpenAI-compat API)
- unslothai.substack.com/p/introducing-unsloth-desktop — launch post, dated Aug 11, 2026, "first desktop app to run and train models locally"
- GitHub releases API: v0.1.70x-beta "Unsloth Desktop is here!" = 2026-08-11/13 (first desktop releases); latest v0.1.808-beta (2026-09-09); Desktop assets v0.1.808: Windows .exe 21MB (dl 4,691), MacOS.dmg 22.5MB (557), ARM64 22.2MB (1,032), Ubuntu.deb 24.2MB (612), Linux.AppImage 178.2MB (636)
- GitHub API repo stats (2026-09-10): 75,961 stars / Apache-2.0 (Core) + AGPL-3.0 (Studio UI — README dual license)
- unsloth.ai/download — "complete open-source local AI interface to run and train models"
- README main — three products (Desktop/Studio/Core), free Colab notebooks, install.sh
- Cross-ref: unsloth-core-research.md (VRAM table, methods), unsloth-studio-research.md (no-code pipeline, Data Recipes), llamacpp-research.md (engine, llama-server)
-->

ถ้า part 1-5 คือ "รัน Ollama → เปิด LM Studio → ดึง engine llama.cpp มาใช้เอง → กดปุ่มเทรนใน Studio → เขียนโค้ดเทรนด้วย Core" — part นี้คือคำตอบของคำถามที่ง่ายที่สุด: **"แล้วถ้าผมไม่ต้องการ 5 อย่างนั้นเลย ผมต้องลงแค่ตัวเดียว ตัวไหน?"**

คำตอบ: **Unsloth Desktop** — app เดียวที่ดาวน์โหลดแล้วรันโมเดล, เทรนโมเดล, และสร้างภาพ/วิดีโอ/เสียง ได้เลย โดยไม่ต้องติดตั้งอะไรเพิ่มเลยแม้แต่คำสั่งเดียว

## 01: Unsloth Desktop คืออะไร — "เครื่อง 3 เครื่องในเครื่องเดียว"

Unsloth Desktop (Beta) คือ **native app ฟรี open-source** สำหรับ macOS, Windows, Linux — ออกมาอย่างเป็นทางการ **กลางเดือน ส.ค. 2026** (release แรก "Unsloth Desktop is here!" = 11-13 ส.ค. 2026, โพสต์ประกาศ 11 ส.ค.) — ตัวล่าสุดวันนี้คือ v0.1.808-beta (9 ก.ย.)

จำ 3 ตัวของ Unsloth จาก part 5 ได้มั้ยครับ — **Desktop = wrapper ที่ห่อ Studio + Core ไว้ใน app เดียว** แปลว่าทุกอย่างที่คุณเคยเห็นใน 2 บทความก่อน (no-code fine-tuning, Data Recipes, 2x เร็ว/VRAM น้อยลง 70%, GGUF export) — **อยู่ใน app นี้ทั้งหมด** โดยไม่ต้องติดตั้งผ่าน terminal เลย

ตัวเลข (ตรวจ GitHub 10 ก.ย. 2026): repo 75,961 stars, ไฟล์ติดตั้งตัวเดียว ~21MB (Windows .exe), และ download ของ release ล่าสุด: **Windows 4,691, ARM64 1,032, Ubuntu 612, macOS 557, AppImage 636** — หนึ่งเดือนหลัง launch ตัว Windows นำห่างชัดเจน (ตลาด local LLM = คนใช้ Windows อยู่มาก)

มันเขียนด้วย **Tauri** (framework native app ที่เบากว่า Electron) — เปิด app → เลือกโมเดล → คุยได้เลย "no setup required" ตาม docs ตรงตัว

_license: ตัว Core = Apache-2.0 / UI = AGPL-3.0 (dual — เหมือน part 5) — สำหรับคนใช้ทั่วไป: ฟรี 100% ไม่มี tier ไม่มี paywall_

## 02: สามบทบาทของ app เดียว — Run / Train / Create

**บทบาท 1: Run — คุยกับโมเดล local**
- คุย 100% offline, **parallel chatting** (คุยหลาย conversation พร้อมกัน)
- **Self-healing tool calls** — docs claim แม่นยำกว่า ~50%: เมื่อโมเดลเรียก tool พลาด ระบบจะ "detect, repair and retry" อัตโนมัติ + execute Bash/Python ใน **sandbox** (ไม่แตะไฟล์จริงถ้าคุณไม่อนุญาต)
- **Permission controls** — เหมือน Claude Code/Codex: โมเดลจะเข้าถึงไฟล์/อินเทอร์เน็ตไม่ได้โดยไม่มี approval ของคุณ — สำหรับใครที่กลัว agent local "หลุด" อันนี้คือ kill switch
- **Unlimited private web search + Deep Research** (plan ก่อน แล้ว search แล้วออก report พร้อม citations)
- **MCP server** — ต่อไฟล์, apps, databases เข้ากับโมเดล local ได้
- **OpenAI-compatible API** — app อื่นชี้มาที่มันได้ทันที
- **LAN + Cloudflare HTTPS** — แชร์ให้เครื่องอื่นในเน็ตบ้าน หรือเอา URL HTTPS ฟรีมาเช็คงานจากมือถือ (เหมือน Tailscale serve ใน series ที่แล้ว — แต่ตรงนี้มันมาในตัว)
- **Connect Providers** — คุยกับ Cloud (OpenAI, Anthropic, vLLM, Ollama) ใน chat เดียวกับ local model — สลับ model ได้ตาม session

**บทบาท 2: Train — fine-tune โดยไม่ต้องแตะโค้ด**
- โยน **PDF, CSV, JSON** เข้าไป → ได้ dataset → train LoRA/QLoRA/full fine-tune/pretraining
- เทรนได้ทั้ง **text, diffusion (ภาพ), audio, embedding** — 2x เร็ว VRAM น้อยลง 70% (engine คือ Core จาก part 5)
- Multi-GPU + โมเดลใหม่ล่าสุด — VRAM requirement เท่ากับตารางใน part 5 เลย (27B QLoRA = 22GB — เครื่อง 2× 5060 Ti ของพรยังพอ)
- Export → GGUF/safetensors/LoRA → ใช้ต่อในเครื่องเดิมหรือ Ollama/llama.cpp

**บทบาท 3: Create — สร้างสื่อแบบ local**
- **Image**: FLUX, Z-Image, LTX, Wan + LoRA adapters ที่คุณเทรนเอง — transform, inpaint, extend, upscale, reference
- **Video**: diffusion video models (เช่น MiniMax-H3) — ตัวเลขจาก docs: 960×544 / 124 frames / 8 steps บน B200 = 70+ วิ → **13 วิ**
- **Audio**: TTS, speech-to-text (Whisper, Qwen3-ASR) — generate + transcribe + fine-tune ได้ทั้งหมดในเครื่อง
- **Train diffusion LoRA** — ถ่ายรูป 20 รูป → caption ใน app → train → ได้ LoRA ของตัวเอง → กลับไป generate ใน app เดียวกัน — loop ปิดในเครื่องเดียว

## 03: Day Zero — โมเดลใหม่ "ออกวันไหน เล่นได้วันนั้น"

จุดที่ Desktop แข็งมากสำหรับสาย local คือ **day-zero support**: Qwen3.8-27B, Kimi K3, DeepSeek-V4 Flash, Muse Glimmer (Meta Superintelligence Labs), Gemma 4, MiniMax-H3 — โมเดลออกใหม่ในสัปดาห์นั้น app รองรับในสัปดาห์นั้น

เหตุผลคือมันยืนบนบ่าของ **llama.cpp** (part 4) + Hugging Face + Dynamic GGUFs ของ Unsloth เอง — release notes ยืนยัน cadence: 8 ก.ย. 2026 Qwen3.8-Flash-Next + GLM-5.3-Flash รัน local ได้ 100% RAM (75-102GB) — **โมเดล 125B รันบนเครื่อง RAM 75GB** คืออะไรที่ 6 เดือนก่อนต้องเป็น server

## 04: ข้อดี ✅

**1. Zero setup — จุดที่มันชนะทุกคน** — Ollama = terminal, LM Studio = app แต่ไม่มี train, Unsloth Core = โค้ด, Studio = curl ติดตั้ง — Desktop = **ดับเบิลคลิก**. สำหรับคนที่ไม่ใช่ dev นี่คือ gap ที่ใหญ่สุดใน series ทั้ง 6 ส่วน

**2. ครบสุดในบรรดา app local ทั้งหมดยอดนิยม** — app ตัวเดียวที่มี "run + train + diffusion + audio + web search + MCP + agent connection" ครบ — Ollama/LM Studio ชนะที่ความเบา แต่ไม่มี train; Colab ชนะที่ฟรีแต่ต้องขึ้น cloud

**3. Permission controls + sandbox** — agent local ส่วนใหญ่ "trust by default" — Desktop ให้เลือกได้ว่า tool จะรันใน sandbox หรือแตะไฟล์จริง — ปลอดภัยระดับเดียวกับ Claude Code แต่บนโมเดลของคุณเอง

**4. ฟรี 100% + offline 100%** — docs FAQ ตรง ๆ: **"No telemetry"** — app รันได้โดยไม่มีเน็ตเลย, โมเดลเก่าที่โหลดไว้แล้ว (Ollama/HF) **detect อัตโนมัติ** — ไม่ต้องโหลดซ้ำ

**5. Day-zero + cadence โหด** — 2-3 release ต่อสัปดาห์, release ล่าสุด 250+ bug fixes — app 1 เดือนที่ iterate เร็วกว่า enterprise หลายตัว

**6. ไม่ lock-in** — export GGUF → Ollama, vLLM, LM Studio ใช้ได้ — คุณ "เช่า" app ไม่ได้ "ซื้อ" ecosystem

## 05: ข้อเสีย ❌

**1. ยัง Beta — app ตัวจริงอายุ ~1 เดือน** — v0.1.808-beta, launch 11 ส.ค. — มี 250+ bug fixes ใน release เดียว = มัน fix หนักทุกวัน ซึ่งดี แต่แปลว่า UI/flow อาจยังเปลี่ยน

**2. ไม่ใช่ inference engine ที่เร็วสุด** — FAQ ของมันเองตอบตรง ๆ: "web search, code execution และ tool-call healing กินเวลา — ปิดแล้ว speed = เท่ากับ app llama.cpp อื่น ๆ" — ถ้าต้องการ pure speed: llama.cpp/llama-server ยังเป็น king (part 4)

**3. UI ไม่ deep เท่า code** — ทุกอย่างทำได้ใน UI แต่ hyperparameter control / dataset pipeline / RL fine-grained = ยังจบที่ Core (part 5) — Studio/Desktop = 80% ของความสามารถที่เหลือ 20% ต้องลงโค้ด

**4. Hardware เก่า "อาจไม่ support ดี"** — FAQ: "Older hardware however may not be well supported" — GPU ยุคก่อน Turing/ Ampere = zone เสี่ยง

**5. Linux = AppImage 178MB** — ใหญ่กว่า Windows 8 เท่า (เพราะต้อง bundle backend) — Ubuntu .deb = 24MB ดีกว่า แต่ Linux support ยังไม่เท่า Win/Mac

**6. AGPL-3.0 สำหรับ UI** — ใช้ส่วนตัว/ธุรกิจ = ไม่มีปัญหา แต่ถ้าจะ **embed UI ของมันใน commercial product** — ต้องคิดเรื่อง AGPL (Core = Apache-2.0 ปลอดภัยกว่า)

**7. 1 app = 1 จุด failure** — ถ้า app down = ทุกอย่าง down (chat + train + API) — team ที่ต้องการ uptime แยก concern = ใช้ Ollama (serve) + Core (train) แยก

## 06: เทียบกับ app local ตัวอื่น (ก.ย. 2026)

| | **Unsloth Desktop** | **Ollama** | **LM Studio** | **Unsloth Studio** (web) |
| --- | --- | --- | --- | --- |
| ติดตั้ง | ดับเบิลคลิก | 1 binary / app | ดับเบิลคลิก | curl + port 8888 |
| คุย local | ✅ parallel | ✅ | ✅ | ✅ |
| **Fine-tune** | ✅ no-code + RL | ❌ | ❌ (Bionic = agent) | ✅ no-code |
| **Diffusion/TTS** | ✅ | ❌ | ❌ | ✅ (Studio) |
| **Web search + MCP** | ✅ private | ❌ | ✅ MCP | ✅ |
| **Agent connect (Claude Code/Codex)** | ✅ `unsloth start` | ❌ (API เท่านั้น) | ✅ Bionic | ✅ |
| API (OpenAI-compat) | ✅ | ✅ | ✅ | ✅ |
| Remote/LAN | ✅ LAN + Cloudflare | ✅ LAN | ✅ LM Link (Tailscale) | ✅ LAN + Cloudflare |
| Telemetry | ❌ (none) | ❌ | มี (opt-out) | ❌ |
| เบาสุด? | ❌ (178MB Linux) | ✅ (เล็กสุด) | กลาง | ❌ (web) |
| เหมาะกับ | all-in-one + train | serve/API | คุย + RAG + MCP | no-code train (browser) |

_หมายเหตุ: "เร็วสุด pure inference" = llama.cpp/llama-server (part 4) — ทั้ง 4 ตัวนี้ใช้มัน (หรือ backend คล้าย) เป็น engine อยู่แล้ว_

## 07: เหมาะกับใคร (และใครควรข้ามไป)

**1. คนที่อยากมี "AI machine" ของตัวเองแบบจบ** — อยากคุย, อยากทดลองเทรนโมเดล, อยากสร้างภาพ — โดยไม่ต้องรู้ว่า GGUF คืออะไร หรือ CUDA คืออะไร — Desktop คือคำตอบที่เดียว

**2. คนที่เขียนโค้ด + อยาก local agent $0** — ต่อ Claude Code/Codex เข้ากับโมเดล local ของตัวเอง + web search + sandbox = coding agent ที่ไม่จ่าย per-token — `unsloth start claude` ตัวเดียวจบ

**3. คนที่อยากลอง fine-tuning แต่ยังไม่ ready สำหรับโค้ด** — เริ่มที่ Desktop (no-code) → ถ้าติด ceiling → ขยับไป Core (part 5) — เส้นทางที่ docs ออกแบบมาให้ชัด

**4. คนที่เก็บโมเดลไว้เยอะแล้ว** — โมเดลเก่าในเครื่อง (Ollama/HF cache) detect อัตโนมัติ — ไม่ต้องเริ่มใหม่

**ข้ามไปถ้า:**
- ต้องการ pure inference speed (production serving) → **llama.cpp / Ollama** (part 1, 4)
- เป็น dev ที่ต้องการควบคุมทุกอย่าง + CI/CD → **Unsloth Core** (part 5)
- ต้องการ multi-user production API → **vLLM** (fine-tune ด้วย Core, serve ด้วย vLLM)
- เครื่องเก่ามาก (pre-Turing) → ลอง **Ollama** ก่อน (support hardware เก่าดีกว่า)

## 08: Pro Tips แยกตามระดับ

**มือใหม่:**
- เริ่มที่ Qwen3.8-27B (UD-Q4_K_XL) — day-zero, 17GB RAM — คุย + web search + image gen ครบใน app เดียว
- ถ้าเครื่อง VRAM น้อย → 8B (Gemma 4 / Llama 3.1) QLoRA-ready
- **ปิด web search / tool healing** ถ้าต้องการ speed (docs FAQ บอกตรง ๆ)

**ใช้จริงจัง:**
- **Permission = sandbox โดย default** — เปิด direct access เฉพาะเมื่อจำเป็น
- **LAN + Cloudflare** = เช็คงานจากมือถือ — `unsloth studio --secure` หรือ LAN access card ใน app
- เทรน LoRA จาก PDF ของตัวเอง → export GGUF → chat กับโมเดล "ของตัวเอง" ใน app เดียวกัน — loop ปิด
- ต่อ **MCP** เข้ากับ files/databases ของคุณ — agent local ที่รู้ context ของคุณจริง ๆ

**องค์กร:**
- Docker `unsloth/unsloth` สำหรับ pipeline ที่ repeatable (Studio + notebooks ใน container)
- เทรนใน Desktop (no-code) → export GGUF (edge) + vLLM FP8/AWQ (server) — จาก run เดียว
- **No telemetry + offline** = pass compliance สำหรับ data ที่ไม่ออกเครื่อง
- ถ้าต้องการ multi-user production → serve ด้วย Ollama/vLLM แยก (อย่าให้ Desktop เป็น SPOF)

## 09: สรุปแบบวิศวกรเป็ด

ถ้า series นี้เป็น "เส้นทางจาก 0 → มี AI machine ของตัวเอง":

- **Part 1-2 (Ollama)** = คุณ "มี" local LLM แล้ว
- **Part 3 (LM Studio + Bionic)** = คุณ "คุย + agent" กับมัน
- **Part 4 (llama.cpp)** = คุณเข้าใจ "engine" ที่ทำงานอยู่ข้างใต้
- **Part 5 (Unsloth Core)** = คุณ "สร้าง" โมเดลของคุณเอง
- **Part 6 (Unsloth Desktop)** = คุณ "มีเครื่องเดียวที่ครบทั้ง 4 อย่าง" โดยไม่ต้องจำ command อะไรเลย

จุดยืนของ Unsloth Desktop ที่พรสรุปจาก research คือ: **"the first app that runs AND trains"** — และมันทำได้จริง เพราะมันไม่ได้สร้าง engine ใหม่ — มันเอา llama.cpp (run) + Core (train) + diffusion stack (create) มาห่อไว้ใน Tauri app เดียว — แล้วให้ permission controls + sandbox + no telemetry มาเป็นของแถม

สำหรับเครื่องพรเอง: 2× RTX 5060 Ti + 128GB RAM = รัน Qwen3.8-27B (17GB) + fine-tune 27B QLoRA (22GB) + generate image/video ใน app เดียวกัน — loop ปิดทั้งหมดบนเครื่องเดียว โดยพรไม่ต้องเปิด terminal เลยแม้แต่ครั้งเดียว

พรจะลองลงจริงแล้ว report ตัวเลขในบทความนี้ก่อน publish ครับ — เหมือนที่ทำมาทุก part

#Adduckivity #DuckOS #NeuroDivergent #Unsloth #UnslothDesktop #LocalLLM #FineTuning #Diffusion #LocalAI
