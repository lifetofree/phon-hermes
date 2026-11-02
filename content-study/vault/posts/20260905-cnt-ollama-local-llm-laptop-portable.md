<!--
ContentID: (placeholder — fill on publish, e.g. 20260905-CNT-OLLAMA-LAPTOP)
Slug: ollama-local-llm-laptop-portable
Series: Local LLM Tools (standalone tool review — part 1 of 2, part 2 = server/datacenter angle, pending)
Status: draft
Written: 2026-09-05
Topic: Ollama + Local LLM on YOUR laptop — portable, offline, private (angle: NOT the server, our own laptop)
Angle: "Local LLM ไม่ใช่ของเซิร์ฟเวอร์ — พกไปทุกที่บน laptop ตัวเอง, offline, data ไม่ออกจากเครื่อง"
Verified primary sources (fetched 2026-09-05):
  - https://ollama.com/ (homepage: 9M+ devs, local models always free, privacy: local data never leaves machine)
  - https://docs.ollama.com/quickstart (install + `ollama run gemma4` / `gemma4:cloud` / `/bye`)
  - https://docs.ollama.com/gpu.md (Nvidia compute cap 5.0+, driver 550+; RTX 30xx/40xx/50xx supported)
  - https://docs.ollama.com/macos.md (macOS Sonoma+, Apple M series full support, models in ~/.ollama, tens-hundreds of GB disk)
  - https://docs.ollama.com/windows.md (Win 10 22H2+, NVIDIA+AMD ROCm/Vulkan, API localhost:11434, no admin required)
  - https://docs.ollama.com/context-length (default context by VRAM: <24GiB=4k, 24-48GiB=32k, >=48GiB=256k)
  - https://ollama.com/pricing (local = always free; cloud tiers separate)
  - https://ollama.com/models (qwen3.8 27b, gemma4 2b-31b, glm-5.3, muse-glimmer 30b, nemotron-3.5-lightning 30b)
Note: "Olamma" = Ollama (typo). Disambiguated. This part = LAPTOP angle (part 2 = server angle separate).
-->

# Ollama + Local LLM บน laptop ตัวเอง — พก "AI" ไปได้ทุกที่ โดยไม่ต้องง้อเน็ต

เคยทำงานแล้วเน็ตหลุดมั้ยคับ — หรือต้องบิน/ไปต่างจังหวัด/ไปไซต์ที่ wifi ไม่มี — แล้ว "AI assistant" ของคุณ... **หายไป** ทันที เพราะมันอยู่บน cloud

นั่นคือ pain point ที่ "Local LLM" แก้ — **run LLM บน hardware ของคุณเอง** โดยไม่ต้อง send prompt ใดๆ ออกจากเครื่อง — ไม่มี API key, ไม่มี per-token bill, ไม่มี data รั่ว, และ**ไม่ขึ้นกับเน็ต** — ใช้ได้ทั้ง offline, ทั้งบนเครื่องบิน, ทั้งที่ไร่

แต่ "Local LLM" มักถูกเล่าในมุม "เซิร์ฟเวอร์ + GPU ตัวใหญ่" — ซึ่งทำให้คนคิดว่า "นั่นไม่ใช่ของพร" วันนี้พรจะเล่ามุมอื่น: **Local LLM บน laptop ตัวเอง** — เครื่องที่ถือขึ้นรถไฟฟ้าทุกวันที่คุณใช้

## Ollama = runtime สำหรับรัน Local LLM บน laptop

Ollama คือ open-source runtime ที่ทำให้ "download model + run + chat" ง่ายเป็นคำสั่งเดียว:

```bash
# 1) Install — ดาวน์โหลด Ollama app (macOS/Windows) หรือ CLI
#    Windows 10 22H2+ (NVIDIA/AMD ROCm/Vulkan)
#    macOS Sonoma+ (Apple M series full support)
#    Linux — install script จาก GitHub
# 2) เปิด interactive menu
ollama
# 3) เริ่ม chat (local — offline เต็มรูปแบบ)
ollama run gemma4
# 4) ออกจาก chat
/bye
```

**ทำไมต้อง "local" — ไม่ใช่ cloud:**
- **Offline** — model โหลดลงเครื่อง, inference รันบน CPU/GPU ของ laptop, **ไม่มี prompt ไหนส่งออก**
- **Private** — data สัมพันธ์ (code, เอกสาร, conversation) **ไม่ออกจากเครื่อง**
- **Free** — local models = always free, ไม่มี per-token bill
- **Portable** — model ที่โหลดแล้ว = อยู่ใน `~/.ollama` บนเครื่อง — คุณยก laptop ไปที่ไหนก็ได้, AI ยังตามไปด้วย

## Features เด่น (laptop angle)

- **Local model ฟรีตลอด** — 0 cost, 0 API key
- **Model library ครอบคลุม** — qwen3.8 (27b), gemma4 (2b–31b), glm-5.3, muse-glimmer (30b), nemotron-3.5-lightning — มีทั้ง "small fast" และ "medium smart"
- **Quantized models** — Ollama ใช้ GGUF quantization — model 8b/14b/27b ใช้งานได้บน laptop RAM 16GB+ โดยไม่ต้อง GPU ตัวแรง
- **Desktop app (macOS/Windows)** — drag-and-drop ไฟล์, reason จาก text/PDF, code files, ส่งรูป (multimodal)
- **API on localhost:11434** — เชื่อมเข้า agent/IDE (Claude Code, Codex, Hermes, Open WebUI) ใช้งานได้เหมือน cloud แต่ localhost
- **Open weights** — open model library, ฝึกต่อ/ปรับแต่งได้, ไม่มี vendor lock-in
- **9M+ developers** ใช้ (ตัวเลขบน ollama.com)

## Hardware — laptop ของคุณวิ่งอะไรได้บ้าง (verified)

Ollama รองรับ GPU ของ laptop — ตัวเลขจริง:

| Laptop spec | Model size ที่ใช้ได้ดี | หมายเหตุ |
|---|---|---|
| **Apple M1/M2/M3 (unified 8–16GB)** | 7b–14b (q4) | Apple Silicon full support, memory = RAM, speed ดีมาก |
| **Intel/AMD + NVIDIA GTX 1650/RTX 3050 (4GB)** | 7b (q4) | VRAM 4GB → context 4k, speed พอไหว |
| **RTX 4060 (8GB)** | 13b (q4) | 8GB VRAM → context 4k, speed ดี |
| **RTX 4070/4080 (8–16GB)** | 27b (q4) | VRAM 16GB+ → context 32k (default 24–48 GiB = 32k) |
| **CPU only (RAM 32GB+)** | 7b (q4) | ช้า, ใช้ได้, แต่ไม่ใช่ main use case |

**Context length default (ตาม VRAM):** <24GiB = 4k · 24–48GiB = 32k · ≥48GiB = 256k — task ที่ใช้ context ยาว (web search, agent, coding tools) = 64k+ tokens — **กิน RAM/VRAM เพิ่ม** — เพิ่มได้แต่ต้องมี memory พอ

**Disk space:** models กิน "tens to hundreds of GB" — laptop SSD 512GB+ พอสำหรับ 3–5 models

## Pros ✅ / Cons ❌ (ตรงไปตรงมา)

**Pros:**
- ✅ **Portable + offline** — ยก laptop ไปไหนก็ได้, AI ยังอยู่ — ใช้บนเครื่องบิน/ไร่/ไซต์งาน
- ✅ **Data stays on machine** — code/เอกสาร/conversation **ไม่ send ออก**, ไม่มี tracking, เหมาะงาน sensitive
- ✅ **Free** — local = 0 cost, 0 API key, 0 per-token bill
- ✅ **Open weights** — ฝึกต่อ/ปรับแต่งได้, ไม่มี vendor lock-in
- ✅ **Simple** — `ollama run <model>` = chat — ไม่ยุ่งยาก
- ✅ **CPU+GPU support** — Apple M, NVIDIA, AMD ROCm/Vulkan — laptop ทั่วไปใช้ได้

**Cons (ตรงไปตรงมา, ไม่อวย):**
- ❌ **Hardware-dependent** — laptop สเปกต่ำ (CPU only, 8GB RAM) → model 7b ช้ามาก, 14b/27b ใช้ไม่ได้ — ต้องเลือก quantization ให้พอดี
- ❌ **VRAM/RAM limited** — context ยาวกิน memory — laptop 16GB RAM → context 4k (default <24GiB VRAM) — ไม่พอสำหรับ long-doc / long-agent
- ❌ **Battery drain** — run model = GPU+CPU ทำงานหนัก — laptop battery 100% → 50% ใน 1 ชม. ถ้าไม่ต่อไฟ
- ❌ **Local ยังด้อยกว่า top closed** — open model "approach" GPT/Claude บน reasoning ยากๆ แต่ไม่ได้เสมอตัวทุก task
- ❌ **Disk space** — 1 model = 5–20GB (q4), 10 models = 50–100GB — laptop SSD 256GB → full เต็ม
- ❌ **ต้อง download model ทุกเครื่อง** — ถ้า laptop ใหม่ = pull model ใหม่ (มี cache ถ้าเครื่องเดิม)
- ❌ **Slow vs cloud** — 195.6 tok/s (cloud, Ollama claim) vs 30–80 tok/s (laptop 8GB) — **local = slower แต่ private**

## เหมาะกับใคร (และใครที่ควร skip)

**เหมาะ:**
- **นักพัฒนา/คนทำ automation ที่ทำงาน offline** — ไร, ไซต์งาน, เครื่องบิน, wifi ไม่ stable — ใช้ local model = ยังทำงานได้
- **คนทำงานกับ data sensitive** — code, client docs, financial data — ไม่อยาก send ไป cloud
- **คนที่ laptop สเปกกลาง–บน (16GB+ RAM, M1+/RTX 3050+)** — ใช้ 7b/14b/27b ได้
- **คนที่อยากลดค่า API** — agent loop, code generation — 100 prompts/วัน × cloud $0.01–$0.03/prompt = $1–$3/วัน — local = $0

**ไม่เหมาะ (ตามตรง):**
- **Laptop สเปกต่ำ (CPU only, 8GB RAM, 256GB SSD)** — ใช้ได้แต่ช้า + disk full — แนะนำ cloud
- **คนที่อยาก frontier reasoning (SOTA)** — local open model ยังด้อยกว่า top closed — ต้อง cloud
- **คนที่ไม่มี patience** — local = slower (30–80 tok/s vs cloud 195+) — ถ้าไม่แคร์ speed = OK

## Pro Tips (laptop angle)

- **มือใหม่:** install app (mac/Win) → `ollama run gemma4` (e4b,เล็ก,เร็ว) → drag PDF/โค้ด → chat — จบ
- **ใช้จริงจัง:** เลือก model ตาม RAM/VRAM (M1 16GB = qwen3.8 27b q4, RTX 4060 8GB = 13b q4) · context ยาว → เพิ่ม settings (RAM ต้องพอ) · เชื่อมเข้า Claude Code/Hermes/Open WebUI · **ต่อไฟ** ตอน run model
- **ประหยัด disk:** ใช้ quantization q4 (เล็กลง 50%) · ลบ model ที่ไม่ใช้ (`ollama rm <name>`) · เก็บ model ใน drive ใหญ่

## สรุปแบบวิศวกรเป็ด

Ollama + Local LLM บน laptop = **"AI ที่ยกไปด้วย"** คับ — local mode = offline + private + free + portable — ใช้ได้ทุกที่ที่ laptop ไป — ไม่ขึ้นกับเน็ต, ไม่มี per-token bill, data ไม่ออกจากเครื่อง

**ระบบ > ค่า token:** ปล่อยให้ AI อยู่บนเครื่อง (local, laptop) แล้วค่อย cloud เมื่อ hardware ไม่พอ — คุมได้, พอรอด, ไม่ตกอยู่ใน per-token bill ไร้กำหนด

(ส่วน server/datacenter angle = part 2 — มาแล้ว)

#Adduckivity #DuckOS #NeuroDivergent #Ollama #LocalLLM #PortableAI #OfflineAI
