# Ollama + Local LLM on Server — ทีมเล็กมี "AI Infrastructure" ของตัวเองได้

<!--
ContentID: (placeholder — fill on publish, e.g. 20260907-CNT-OLLAMA-SERVER)
Slug: ollama-local-llm-server-datacenter
Series: Local LLM Tools — part 2 of 2 (part 1 = laptop/portable angle, Notion page 3d2df8d8-8d8c-81dc-87db-fbc91cf9e1d1)
Status: draft
Written: 2026-09-07
Topic: Ollama + Local LLM on YOUR OWN server / mini datacenter — team AI infrastructure, API, Docker, multi-GPU
Angle: "ทีม 5-50 คน ไม่ต้องซื้อ AI จาก vendor — build infrastructure ของตัวเอง, per-token = $0, data never leaves your network"
Verified primary sources (fetched 2026-09-07):
- https://docs.ollama.com/api (base URL http://localhost:11434/api, cloud base https://ollama.com/api, endpoints generate/chat/embed/tags/show/create/copy/pull/push/delete/version, API stable & backwards compatible, official Python/JS libs)
- https://docs.ollama.com/api/authentication + OpenAI/Anthropic compatibility (from API index)
- https://docs.ollama.com/docker (CPU-only / Nvidia --gpus=all + NVIDIA Container Toolkit / AMD rocm tag / Vulkan bundled & enabled by default, JETSON_JETPACK env)
- https://docs.ollama.com/gpu (Nvidia compute cap 5.0+, driver 550+; multi-GPU: CUDA_VISIBLE_DEVICES by UUID, nvidia-smi -L, force CPU with -1; suspend/resume UVM workaround; AMD ROCm v7 Linux; GPU list incl. RTX 50xx Blackwell 12.0, H100/H200 9.0, A100 8.0, V100 7.0)
- https://ollama.com/pricing (2026-09): Free local always free; Pro $20/mo $60 credits; Max $100/mo $300 credits; Team $500/mo $1,000 shared credits; peak pricing 12:00-18:00 UTC Mon-Fri; per-M-token: deepseek-v4-flash $0.22/$0.66, glm-5.3 $1.40/$4.40
- part 1 facts (verified 2026-09-05, see references/ollama-research.md): 9M+ devs, 195.6 tok/s claim, context defaults <24GiB=4k / 24-48GiB=32k / >=48GiB=256k
Note: part 2 = SERVER angle — ต่างจาก part 1 (laptop): target = mini datacenter / home lab / team server, ไม่ใช่ laptop
-->

## 00: Hook — "ค่า API เดือนละเท่าไหร่ — แล้วถ้าเป็น $0 ล่ะ"

ทีมที่เริ่มใช้ AI จริงจังจะเจอ bill เดียวกัน — agent loop + code gen + RAG + support bot — prompt เข้าไปทุกวัน ตัวเลขบน pricing page: deepseek-v4-flash $0.22 per 1M input / $0.66 per 1M output — กล้อง 10,000 prompts/วัน ≈ $1-3/วัน = **$30-90/เดือน ต่อ agent** — team 5 agent = $150-450/เดือน — และ peak pricing (12:00-18:00 UTC วันทำการ) ทำให้ bill กระโดดอีก 2x

pain point จริงไม่ใช่เงิน — เป็น 3 อย่าง:
1. **Data ของทีมต้องส่งไป vendor** — prompt = code, เอกสารลูกค้า, internal docs — ไปอยู่ server คนอื่น
2. **Vendor lock-in** — API ราคาขึ้นได้, model ลง shelf ได้, rate limit เปลี่ยนได้ — team ที่ build workflow บน API คนเดียว = build บน ground ที่ไม่ใช่ของตัวเอง
3. **Latency + uptime ขึ้นกับคนอื่น** — network hop ไป datacenter vendor ทุก request

วันนี้จะเล่ามุมที่ part 1 ยังไม่ได้แตะ: **Local LLM บน server ของทีมตัวเอง** — mini datacenter / home lab / 1 เครื่อง GPU ที่ทีมทั้ง 5-50 คนใช้ร่วมกัน — same runtime (Ollama) แต่ architecture เปลี่ยนจาก "laptop 1 คน" เป็น **team AI infrastructure**

## 01: ต่างจาก part 1 ตรงไหน — 3 axes

| | Part 1 (laptop) | Part 2 (server) |
|---|---|---|
| User | 1 คน portable | ทีมทั้ง org ผ่าน API |
| Hardware | M1/RTX 3050-4080 | RTX 4090/A100/H100, multi-GPU |
| Access | `ollama run` CLI/app | **HTTP API :11434** — ทุก tool ต่อได้ |
| Cost model | $0 (ไฟบ้าน) | $0 + ค่าไฟ — **no per-token** |
| Failure mode | battery, disk | uptime, RAM, thermal, admin |

key insight: **Ollama เดียว — local mode คือ laptop, serve mode คือ datacenter** — install เดียว, model library เดียว, command เดียว — ที่เปลี่ยนคือ access pattern (CLI → API) และ hardware budget

## 02: มันทำงานยังไง — architecture 3 layer

```
[Team tools: IDE / agents / support bot / RAG pipeline]
        │  HTTP (OpenAI-compatible / Anthropic-compatible / native /api)
[Ollama server — localhost:11434 / tailscale / internal LB]
        │  model loading + GPU scheduling
[GPUs: RTX 4090 24GB ×1-4 / A100 80GB / H100 — models in /root/.ollama or volume]
```

**3 layer ที่ต้องเข้าใจ:**

**1. API layer** — Ollama serve HTTP ที่ `http://<server>:11434/api` — endpoints: `/api/generate`, `/api/chat`, `/api/embed` (RAG!), `/api/tags`, `/api/push`, `/api/pull` — และจุดที่ทีมชอบที่สุด: **OpenAI-compatible + Anthropic-compatible endpoint** — meaning ทุก tool ที่ต่อ OpenAI ได้ (Claude Code, Codex, Hermes, n8n, Open WebUI, VS Code extensions) ต่อ Ollama server ได้ **โดยไม่ต้องเปลี่ยน code** — เปลี่ยน base URL + model name เท่านั้น

**2. Scheduling layer** — multi-GPU: `CUDA_VISIBLE_DEVICES` (UUID จาก `nvidia-smi -L`) จำกัด Ollama ใช้ subset ของ GPU — force CPU ด้วย invalid ID (`-1`) — server 4 GPU = 4 model pool ได้, workload แยก: 1 GPU รัน coding model, 1 GPU รัน RAG embeddings, 2 GPU รัน long-context

**3. Storage layer** — models อยู่ใน volume (`/root/.ollama` หรือ Docker volume) — 1 model q4 = 5-20GB — server SSD 1-2TB = 50-100 models — pull/push จาก registry — backup = copy folder

## 03: Deploy — 3 paths (verified)

**Path 1: Bare metal (ง่ายสุดสำหรับ 1 server)**
```bash
curl -fsSL https://ollama.com/install.sh | sh
# แล้ว run service — API auto-serve ที่ :11434
```

**Path 2: Docker + NVIDIA Container Toolkit (production pattern)**
```bash
# install NVIDIA Container Toolkit (deb/rpm — ดู docs.ollama.com/docker)
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker

docker run -d --gpus=all \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama ollama/ollama

docker exec -it ollama ollama run <model>
```

**Path 3: AMD ROCm / Vulkan**
```bash
# AMD ROCm v7 (Linux)
docker run -d --device /dev/kfd --device /dev/dri \
  -v ollama:/root/.ollama -p 11434:11434 \
  --name ollama ollama/ollama:rocm
# Vulkan: bundled ใน image, enabled by default ถ้า container เห็น GPU
```

**Model library ที่เหมาะกับ server (จาก ollama.com/models, 2026-09):**
- **qwen3.8 27b** — coding + tools + thinking — sweet spot 24GB VRAM
- **glm-5.3 / glm-5.3-flash** — tools/thinking — ถ้าใช้ cloud version = $1.40/$4.40 per 1M — local = $0
- **gemma4 e2b–31b** — vision/tools/thinking/audio
- **nemotron-3.5-lightning 30b (MoE, 3b active)** — fast inference on big cards
- **granite4.2 3b–30b (IBM, Apache 2.0)** — RAG/JSON structured output — เหมาะ pipeline

## 04: Hardware — server ของทีมวิ่งอะไรได้ (real numbers)

| GPU | VRAM | Model size (q4) | Context | Use case |
|---|---|---|---|---|
| RTX 4090 | 24GB | 27b | 4k-32k | Coding + tools, team ≤10 |
| RTX 3090 (used, ~$800-1200) | 24GB | 27b | 4k-32k | Budget build — used market |
| A100 | 80GB | 70b+ | 256k | Long-doc, RAG heavy, org |
| H100 | 80GB | 70b+ | 256k+ | Production SOTA open model |
| Multi-GPU (4×4090) | 96GB | 70b (split) | 32k+ | Team 20-50, concurrent |

**Context default ตาม VRAM:** <24GiB = 4k · 24-48GiB = 32k · ≥48GiB = 256k — **server ที่ VRAM 80GB = default 256k context** — นี่คือ game changer สำหรับ RAG pipeline ที่ต้องอ่าน whole document

**Disk:** 100 models q4 ≈ 500GB-1TB — SSD 2TB recommended for team library

**RAM:** GPU server — RAM 64-128GB standard — model ที่ไม่ fit VRAM จะ spill to RAM (slow) — plan VRAM first

## 05: Pros ✅

- **Per-token = $0** — team 5 agent × 10,000 prompts/วัน = $0/month (vs $150-450 cloud) — pay only electricity + hardware amortization
- **Data never leaves your network** — prompt/code/docs = inside your LAN — compliance-ready (HIPAA/PCI/ISO — no data crosses your boundary)
- **OpenAI/Anthropic-compatible API** — zero code change จาก tool ที่ต่อ OpenAI อยู่แล้ว — base URL + model name เปลี่ยน
- **Multi-GPU scheduling** — `CUDA_VISIBLE_DEVICES` = pool ของ workload — coding model + RAG + long-context 1 server
- **Docker + official image** — production pattern 1 command, GPU passthrough, volume persistence
- **Open weights + no vendor lock-in** — model library open (Apache 2.0, MIT, custom) — pull/push registry — backup = folder copy
- **Latency = LAN** — 1-5ms round trip (vs 50-200ms cloud hop)
- **No peak pricing, no rate limit, no downtime window** — uptime = uptime ของ server ตัวคุณ

## 06: Cons ❌ — ตรงๆ ไม่อวย

- **Hardware capex** — RTX 4090 $1,600-2,000 + server build $500-1,500 = **$2,000-3,500 up front** (vs cloud $0 upfront) — payback period ≈ 12-24 เดือน ถ้าใช้ heavy — **ถ้าใช้ light = cloud ถูกกว่า**
- **Admin burden** — driver updates, thermal management, disk monitoring, model pulls, version upgrades — **1 person part-time = 2-4 hr/week** — ถ้าทีมไม่มี sysadmin = pain
- **Uptime = your problem** — server down = ทุก agent stop — no 99.9% SLA ของ vendor — ต้อง plan restart, watchdog, backup
- **VRAM ceiling** — 24GB VRAM = 27b q4 — model 70b ต้อง A100/H100 ($10,000-30,000+) — **frontier open model ยังด้อยกว่า closed SOTA บน hardest reasoning**
- **Concurrency limit** — 1 GPU 1 model = sequential requests (queue) — team 20 คน = 1 GPU ไม่พอ — ต้อง multi-GPU = capex ×2-4
- **Docker + GPU = moving parts** — NVIDIA Container Toolkit, driver version, CUDA version, model arch — **3 layers ที่ต้อง align** — suspend/resume บน Linux = UVM driver bug (workaround: `sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm`)
- **No built-in auth/multi-tenancy** — Ollama = single-server runtime — ถ้า team 50 คน = ต้องต่อ auth layer (reverse proxy, Tailscale, API gateway) เอง
- **Model rotation** — open model library หมุนเร็ว — qwen3.8 วันนี้ = best, เดือนหน้า = model ใหม่ — ต้อง test + pull + re-deploy — **continuous maintenance ไม่ใช่ set-and-forget**

## 07: เทียบกับคู่แข่ง (server angle)

| | Ollama server | Cloud API (OpenAI/Anthropic) | Self-hosted vLLM/TGI | Ollama cloud tier |
|---|---|---|---|---|
| Upfront | $2,000-3,500 (1×4090) | $0 | $2,000-10,000+ | $0 |
| Per-token | $0 | $0.07-4.40 per 1M | $0 | $20-500/mo tier |
| Data stays local | ✅ | ❌ | ✅ | ❌ |
| OpenAI-compatible API | ✅ | ✅ | ⚠️ (some) | ✅ |
| Multi-tenancy | ❌ (DIY proxy) | ✅ | ✅ | ✅ |
| Admin effort | Low (1 service) | None | High (K8s, CUDA, config) | None |
| Uptime SLA | Your problem | 99.9%+ | Your problem | 99.9%+ |
| Frontier model | ❌ (open weights) | ✅ | ❌ | ✅ (hosted) |

**Bottom line:** ถ้า team <10 คน + ใช้ light = **cloud tier (Pro $20/mo)** คุ้มกว่า; ถ้า team 10-50 + ใช้ heavy + data sensitive = **Ollama server 1×4090** payback 12-18 เดือน; ถ้า team 50+ + production SOTA = **vLLM/TGI + A100/H100** หรือ **cloud frontier**

## 08: เหมาะกับใคร (Pro Tips แยกตามระดับ)

**Home lab / solo dev ที่อยาก team AI** — 1×RTX 4090 + Docker + 1 model (qwen3.8 27b) + Open WebUI — 1 วัน setup — API สำหรับทุก tool — $0/month after capex

**ทีม 5-15 คน, data sensitive, ใช้ daily** — 1×RTX 4090 + Tailscale (access from office) + 2 models (coding + RAG) + reverse proxy auth — budget $3,000 — payback 12-18 เดือน — **เริ่มที่ 1 GPU, scale เมื่อ queue เต็ม**

**ทีม 20-50, production** — 4×RTX 4090 หรือ 1×A100 + K8s/Docker compose + monitoring + backup + runbook — budget $8,000-30,000 — **hire part-time sysadmin หรือ budget 2-4 hr/week** — ถ้าไม่มี = ใช้ cloud frontier แทน

**ไม่เหมาะ:**
- **ทีม <5 คน, ใช้ light** — cloud Pro $20/mo ถูกกว่า capex
- **ต้องการ frontier SOTA reasoning** — open model ยังด้อยกว่า closed — cloud frontier
- **ไม่มี sysadmin** — self-host = 2-4 hr/week maintenance — ถ้าไม่มีคน = pain > value
- **data ไม่ sensitive + budget tight** — cloud = $0 upfront + no admin

## 09: สรุปแบบวิศวกรเป็ด

Ollama server = **"AI infrastructure ของทีมตัวเอง"** คับ — same runtime ที่ part 1 ใช้บน laptop แต่ scale เป็น team: API endpoint เดียว, multi-GPU scheduling, Docker production pattern, OpenAI/Anthropic-compatible — **per-token = $0, data = inside your network, latency = LAN**

exchange ที่ต้องแลก: **capex $2,000-3,500 + admin 2-4 hr/week + uptime = your problem** — 3 อย่างนี้คือ cost ที่ cloud tier ($20-500/mo) hide ให้อยู่ใน subscription

**ระบบ > subscription:** ถ้า team ใช้ AI daily + data sensitive + 10 คน+ — **build infrastructure ของตัวเอง** (local, 1×4090) payback 12-18 เดือน — ปล่อย cloud เมื่อ frontier reasoning ต้องการ — คุมได้, พอรอด, ไม่ตกอยู่ใน per-token bill ไร้กำหนด

**Part 2 ของ series — part 1 (laptop/portable) = "AI ที่ยกไปด้วย", part 2 (server) = "AI infrastructure ของทีม"** — 2 angle เดียว runtime เดียว (Ollama) — scale จาก 1 คน → ทีม

#Adduckivity #DuckOS #NeuroDivergent #Ollama #LocalLLM #SelfHosted #AIDev #LLM #Inference #Server #MiniDatacenter
