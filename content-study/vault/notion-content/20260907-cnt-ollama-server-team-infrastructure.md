# Local LLM บน Server — ทีมเล็กมี AI Infrastructure ของตัวเองได้

**Excerpt:** ค่า API เดือนละเท่าไหร่ถ้าเปลี่ยนเป็นศูนย์ได้ การรัน Ollama บน Server ส่วนตัวคือการสร้าง AI Infrastructure ให้ทั้งทีมใช้ร่วมกัน ไม่ต้องส่งโค้ดหรือเอกสารลับออกนอกเครือข่าย ไม่มีบิลต่อโทเคนกวนใจ และปลดแอกจากข้อจำกัดของผู้ให้บริการภายนอก
**Laws:** [[🛡️ Law 3: Protect System]] · [[🛠️ Decision Protocol]]
**Site Category:** [[📚 Asset Library]]
**Tags:** [[Adduckivity]] · [[DuckOS]] · [[NeuroDivergent]] · #Ollama · [[LocalLLM]] · #SelfHosted · [[AIDev]] · #LLM · #Inference · #Server · #MiniDatacenter

---

## “ค่า API เดือนละเท่าไหร่ — แล้วถ้าเป็น $0 ล่ะ”
ทีมที่เริ่มใช้ AI จริงจังจะเจอ bill เดียวกัน — agent loop + code gen + RAG + support bot — prompt เข้าไปทุกวัน ตัวเลขบน pricing page: deepseek-v4-flash off-peak $0.22 per 1M input / $0.66 per 1M output — กัน 10,000 prompts/วัน ≈ $1-3/วัน = $30-90/เดือน ต่อ agent — team 5 agent = $150-450/เดือน — และ peak pricing (01:00-04:00 และ 06:00-10:00 UTC วันทำการ — เสาร์อาทิตย์คิด off-peak ทั้งวัน) ทำให้ bill กระโดดอีก 2x ($0.44/$1.32)
pain point จริงไม่ใช่เงิน — เป็น 3 อย่าง:
วันนี้จะเล่ามุมที่โพสต์ก่อนหน้านี้ยังไม่ได้แตะ: Local LLM บน server ของทีมตัวเอง — mini datacenter / home lab / 1 เครื่อง GPU ที่ทีมทั้ง 5-50 คนใช้ร่วมกัน — same runtime (Ollama) แต่ architecture เปลี่ยนจาก “laptop 1 คน” เป็น team AI infrastructure
## ต่างจาก part 1 ตรงไหน — 3 axes
key insight: Ollama เดียว — ต่อจาก terminal คือ laptop, เปิดเป็น API service คือ datacenter — install เดียว, model library เดียว, command เดียว — ที่เปลี่ยนคือ access pattern (CLI → API) และ hardware budget
.
## มันทำงานยังไง — architecture 3 layer
.
3 layer ที่ต้องเข้าใจ:
1. API layer — Ollama serve HTTP ที่ http://<server>:11434/api — endpoints: /api/generate, /api/chat, /api/embed (RAG!), /api/tags, /api/push, /api/pull — และจุดที่ทีมชอบที่สุด: OpenAI-compatible + Anthropic-compatible endpoint — meaning ทุก tool ที่ต่อ OpenAI ได้ (Claude Code, Codex, Hermes, n8n, Open WebUI, VS Code extensions) ต่อ Ollama server ได้ โดยไม่ต้องเปลี่ยน code — เปลี่ยน base URL + model name เท่านั้น
2. Scheduling layer — multi-GPU: CUDA_VISIBLE_DEVICES (UUID จาก nvidia-smi -L) จำกัด Ollama ใช้ subset ของ GPU — force CPU ด้วย invalid ID (-1) — server 4 GPU = 4 model pool ได้, workload แยก: 1 GPU รัน coding model, 1 GPU รัน RAG embeddings, 2 GPU รัน long-context
3. Storage layer — models อยู่ใน volume (/root/.ollama หรือ Docker volume) — 1 model q4 = 5-20GB — server SSD 1-2TB = 50-200 models — pull/push จาก registry — backup = copy folder
.
## Deploy — 3 paths (verified)
Path 1: Bare metal (ง่ายสุดสำหรับ 1 server)
Path 2: Docker + NVIDIA Container Toolkit (production pattern)
Path 3: AMD ROCm / Vulkan
.
Model library ที่เหมาะกับ server (จาก ollama.com/models, 2026-09):
.
## Hardware — server ของทีมวิ่งอะไรได้ (real numbers)
Context default ตาม VRAM: <24GiB = 4k · 24-48GiB = 32k · ≥48GiB = 256k — server ที่ VRAM 80GB = default 256k context — นี่คือ game changer สำหรับ RAG pipeline ที่ต้องอ่าน whole document
Disk: 100 models q4 ≈ 500GB-1TB — SSD 2TB recommended for team library
RAM: GPU server — RAM 64-128GB standard — model ที่ไม่ fit VRAM จะ spill to RAM (slow) — plan VRAM first
.
## Pros ✅
.
## Cons ❌
.
## เทียบกับคู่แข่ง (server angle)
Bottom line:
ถ้า team <10 คน + ใช้ light = cloud tier (Pro $20/mo — 10 concurrent requests + $300 usage credits/mo) คุ้มกว่า;
ถ้า team 10-50 + ใช้ heavy + data sensitive = Ollama server 1×4090 payback 12-18 เดือน;
ถ้า team 50++ production SOTA = vLLM/TGI + A100/H100 หรือ cloud frontier
.
## เหมาะกับใคร (Pro Tips แยกตามการใช้งาน)
Home lab / solo dev ที่อยาก team AI — 1×RTX 4090 + Docker + 1 model (qwen3.8 27b) + Open WebUI — 1 วัน setup — API สำหรับทุก tool — $0/month after capex
ทีม 5-15 คน, data sensitive, ใช้ daily — 1×RTX 4090 + Tailscale (access from office) + 2 models (coding + RAG) + reverse proxy auth — budget $3,000 — payback 12-18 เดือน — เริ่มที่ 1 GPU, scale เมื่อ queue เต็ม
ทีม 20-50, production — 4×RTX 4090 หรือ 1×A100 + K8s/Docker compose + monitoring + backup + runbook — budget $8,000-30,000 — hire part-time sysadmin หรือ budget 2-4 hr/week — ถ้าไม่มี = ใช้ cloud frontier แทน
ไม่เหมาะ:
.
## สรุปแบบวิศวกรเป็ด
Ollama server = “AI infrastructure ของทีมตัวเอง” คับ — same runtime ที่ part 1 ใช้บน laptop แต่ scale เป็น team: API endpoint เดียว, multi-GPU scheduling, Docker production pattern, OpenAI/Anthropic-compatible — per-token = $0, data = inside your network, latency = LAN
exchange ที่ต้องแลก: capex $2,000-3,500 + admin 2-4 hr/week + uptime = your problem — 3 อย่างนี้คือ cost ที่ cloud tier ($20-500/mo) hide ให้อยู่ใน subscription
ระบบ > subscription: ถ้า team ใช้ AI daily + data sensitive + 10 คน+ — build infrastructure ของตัวเอง (local, 1×4090) payback 12-18 เดือน — ปล่อย cloud เมื่อ frontier reasoning ต้องการ — คุมได้, พอรอด, ไม่ตกอยู่ใน per-token bill ไม่มีกำหนด
Part 2 ของ series — part 1 (laptop/portable) = “AI ที่ยกไปด้วย”, part 2 (server) = “AI infrastructure ของทีม” — 2 angle เดียว runtime เดียว (Ollama) — scale จาก 1 คน → ทีม
.
#Adduckivity #DuckOS #NeuroDivergent #Ollama #LocalLLM #SelfHosted #AIDev #LLM #Inference #Server #MiniDatacenter
===========
FB version
===========
Local LLM บน Server — ทีมเล็กมี AI Infrastructure ของตัวเองได้ ($0 ต่อเดือน ไม่มี per-token)
เคยคิดมั้ยคับว่าทีมที่ใช้ AI จริงจัง ค่า API มันไต่เร็วแค่ไหน — agent loop + code gen + RAG + support bot — 10,000 prompts/วัน ≈ $1-3/วัน ต่อ 1 agent = $30-90/เดือน คูณ 5 agents = $150-450/เดือน แถม peak pricing ของ DeepSeek (ช่วง 01:00-04:00 กับ 06:00-10:00 UTC วันทำการ) โดดขึ้นอีก 2 เท่า ($0.44/$1.32)
แต่ pain point จริงไม่ใช่เงินครับ — มันคือ 3 อย่างนี้:
วันนี้พรเล่ามุมที่โพสต์ก่อนยังไม่ได้แตะ: ยก Local LLM ขึ้น server ของทีมเอง — home lab 1 เครื่อง GPU ให้ทีม 5-50 คนใช้ร่วมกัน — same runtime (Ollama) แต่เปลี่ยนจาก "AI ของ 1 คน" เป็น "AI Infrastructure ของทีม"
.
🖥️ มันทำงานยังไง — 3 layer ง่ายๆ
Deploy มี 3 ทาง: bare metal (install script เดียว), Docker + NVIDIA Container Toolkit (production pattern), และ AMD ROCm/Vulkan สำหรับค่ายแดง
.
💪 Hardware วิ่งอะไรได้บ้าง
Context default ตาม VRAM: ต่ำกว่า 24GiB = 4k · 24-48GiB = 32k · 48GiB+ = 256k
.
✅ Pros
❌ Cons
.
🎯 สรุปว่าใครควรทำ
.
🦆 สรุปแบบวิศวกรเป็ด
Ollama ตัวเดียว เล่นได้ทั้ง 2 บท — ต่อจาก terminal = laptop ส่วนตัว, เปิดเป็น API = datacenter ของทีม แลกกับ capex + admin + uptime ที่ต้องรับผิดชอบเอง แต่แทนที่ด้วย $0 per-token + data อยู่ใน network ตัวเอง + ความเร็ว LAN
ระบบ > subscription คับ — ถ้าทีมใช้ AI daily + data sensitive + 10 คนขึ้นไป build infrastructure ของตัวเอง คุ้มกว่าจ่าย per-token ที่ตัวเลขไม่มีวันหยุดนิ่ง
.
อ่านฉบับเต็มได้ใน comment นะค้าบ
.
#Adduckivity #DuckOS #NeuroDivergent #Ollama #LocalLLM #SelfHosted #AIDev #MiniDatacenter
===========

*Synced: 2026-11-02 19:48 +07 · [Notion](https://www.notion.so/3d4df8d88d8c80428841eef3abb9d536) · ✅ Published*