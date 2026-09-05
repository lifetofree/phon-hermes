<!--
ContentID: (placeholder — fill on publish, e.g. 20260905-CNT-OLLAMA)
Slug: ollama-local-llm-intro
Series: Local LLM Tools (standalone tool review — no prior part in index.json)
Status: draft
Written: 2026-09-05
Topic: Ollama — run local (and cloud) LLMs on your own hardware
Angle: "ไม่ต้องง้อ API key / per-token bill — ข้อมูลไม่ออกจากเครื่อง + สลับไป cloud เมื่อต้องการ"
Verified primary sources (fetched 2026-09-05):
  - https://ollama.com/ (homepage: 9M+ devs, Reliably fast 195.6 tok/s, integrations, privacy, pricing tiers)
  - https://ollama.com/docs (docs index / llms.txt — docs now at docs.ollama.com)
  - https://docs.ollama.com/quickstart (install + `ollama run gemma4` / `gemma4:cloud` / `/bye`)
  - https://ollama.com/blog/new-app (macOS/Windows app, drag-and-drop files, code, multimodal, context length setting)
  - https://ollama.com/pricing (Free/Pro $20/Max $100/Team $500/Enterprise; per-M-token model prices; peak pricing 12:00–18:00 UTC)
  - https://ollama.com/models (qwen3.8 27b, gemma4, glm-5.3, muse-glimmer 30b, nemotron-3.5-lightning, granite4.2, ornith-1.5)
Note: "Olamma" in the request = Ollama (typo). No product named "Olamma" exists — disambiguated to Ollama.
-->

# Ollama — รัน LLM บนเครื่องตัวเอง (local) + สลับ cloud ได้ในคำสั่งเดียว

เคยมี API key ของ ChatGPT / Claude ตั้งไว้ทุกโปรเจกต์มั้ยคับ พอส่ง prompt หนึ่งรอบ → มี token เข้า billing หนึ่งรอบ พอ agent มัน loop เรียก tool ซ้ำ 20 รอบ → ค่าน้ำค่าไฟไหลไปโดยที่ข้อมูลบริษัทก็ไปนอนบน cloud คนอื่นด้วย

Ollama แก้ pain point นี้แบบ "ปิดไฟ cloud" — คุณ download model มาวางบนเครื่องตัวเอง แล้วสั่ง `ollama run gemma4` ก็ chat ได้เลย **offline, ไม่มี API key, ไม่มี per-token bill, และข้อมูลไม่ออกจากเครื่อง** (มุมนี้สำคัญสุด — ใจความ: "data stays yours")

แต่จุดที่หลายคนยังตกข่าว = Ollama **ไม่ได้เป็นแค่ CLI เดิมๆ สำหรับรัน local model** แล้วคับ ตอนนี้มันกลายเป็นแพลตฟอร์ม **local + cloud** ในตัวเดียว — ฝั่ง local ฟรีตลอดไป, ฝั่ง cloud เป็น model ใหญ่ที่ Ollama host ให้อยู่ใน US / Europe / Singapore พร้อม tier pricing — คุณเลือกสลับด้วยคำสั่งเดียว: `ollama run gemma4` (local) กับ `ollama run gemma4:cloud` (cloud)

## Ollama ทำงานยังไง — 2 mode ใน 1 runtime

คิดภาพว่า Ollama คือ "server ของเราเองสำหรับ LLM" คับ

- **Local mode:** `ollama run <model>` → model weights โหลดลงเครื่อง (บาง GB) แล้ว inference รันบน CPU/GPU ของคุณ — offline เต็มรูปแบบ, ไม่มี prompt ไหนออกจากเครื่อง, ฟรี
- **Cloud mode:** `ollama run <model>:cloud` → model ใหญ่กว่าที่ Ollama host ให้นับ token ของเรา — ใช้ได้เหมือนกัน, ง่ายกว่า, แต่ data ส่งไป cloud ของ Ollama (host ใน US/Europe/Singapore, ไม่ได้ train บน prompt ของเรา)

ทั้งสองฝั่งใช้คำสั่งเดียวกัน, เชื่อม tool/integration เดียวกัน, สลับได้กลางงาน — ไม่ต้องเปลี่ยน workflow

**สั่งแบบเร็ว (จาก quickstart ทางการ):**
```bash
# 1) install: ดาวน์โหลด app (macOS/Windows/Linux) หรือ CLI
# 2) เปิด interactive menu
ollama
# 3) เริ่ม chat (local)
ollama run gemma4
#    หรือใช้ cloud model
ollama run gemma4:cloud
# 4) ออกจาก chat
/bye
```

## Features เด่น

- **Local model ฟรีตลอด** — ไม่มี hidden limit, local models = always free
- **Cloud tier** — model ใหญ่กว่า, run ควบคู่กันหลายตัว (Pro/Max/Team)
- **Capabilities** — streaming, thinking, structured outputs, vision, embeddings, tool calling, web search (จาก docs index)
- **Desktop app (macOS/Windows)** — drag-and-drop ไฟล์, reason จาก text/PDF, code files, ส่งรูป (multimodal, เช่น Gemma), เพิ่ม context length ใน settings (ใช้ RAM เพิ่ม)
- **Open weights + open source** — model ใน library เป็น open model
- **9M+ developers** ใช้ — integrations ครอบคลุม: Claude Code, Codex, OpenCode, Hermes Agent, OpenClaw, VS Code, Pi, n8n
- **Privacy** — prompts ไม่ได้ถูก track/train, cloud host ใน US/Europe/Singapore, local = data ไม่ออกจากเครื่อง

**Models ที่อยู่ใน library (ตัวอย่าง, 2026-09):**
| Model | Size | Features | หมายเหตุ |
|---|---|---|---|
| qwen3.8 | 27b | vision, tools, thinking | coding/pro work/agentic |
| gemma4 | e2b–31b | vision, tools, thinking, audio | Google DeepMind |
| glm-5.3 | — | tools, thinking, cloud | flagship coding ของ Z.ai |
| muse-glimmer | 30b | vision, tools, thinking | Meta, Apache 2.0, always-on local agent |
| nemotron-3.5-lightning | 30b (3b active) | tools, thinking | NVIDIA MoE |
| granite4.2 | 3b–30b | multilingual, RAG, JSON | IBM, Apache 2.0 |

## Pros ✅ / Cons ❌

**Pros:**
- ✅ **Data stays yours (local)** — prompt/code ไม่ออกจากเครื่อง, เหมาะงาน sensitive
- ✅ **ฟรี + ไม่มี per-token bill** — local = 0 cost, ไม่มี API key
- ✅ **Offline** — ทำงานได้โดยไม่มีเน็ต (lab, ไซต์งาน, deployment ที่ไม่มีเน็ต)
- ✅ **Simple + fast** — `ollama run <model>` = chat, integrations ครอบคลุม agent เดิม (Claude Code/Codex/Hermes/OpenClaw)
- ✅ **Open weights** — model ฝึกต่อ/ปรับแต่งได้, ไม่มี vendor lock-in อย่าง closed API
- ✅ **Dual mode** — local ฟรี + cloud ใหญ่ขึ้นเมื่อต้องการ, สลับคำสั่งเดียว

**Cons (ตรงไปตรงมา, ไม่อวย):**
- ❌ **Hardware-dependent** — local model ใหญ่กิน RAM/VRAM มาก; context length ยิ่งยาวยิ่งกิน memory — เครื่องสเปกต่ำ → ใช้ได้แค่ model เล็ก/ช้า
- ❌ **Local ยังด้อยกว่า top closed** — open models "approach" GPT/Claude บน reasoning ยากๆ แต่ไม่ได้เสมอตัวทุก task
- ❌ **Cloud mode ≠ "data stays yours"** — ถ้าใช้ `:cloud` ข้อมูล**ออก**จากเครื่องไป Ollama cloud (US/Europe/Singapore) — pitch privacy = ฝั่ง local อย่างเดียว
- ❌ **Cloud pricing ยังใหม่ + peak pricing** — business hours (12:00–18:00 UTC, Mon–Fri) ค่า input/output สูงขึ้น (เช่น deepseek-v4-flash $0.22 → $0.44 /M tok input) — ต้องดูตาราง model pricing
- ❌ **เป็น model runtime ไม่ใช่ agent เต็มตัว** — ต้อง pair กับ agent/IDE (Claude Code, Hermes, Open WebUI) — ตัวมันไม่ orchestrate ให้อัตโนมัติ
- ❌ **Model list เปลี่ยนเร็ว** — library หมุน (glm-5.3, deepseek-v4, qwen3.8 เป็นของใหม่) — benchmark/ราคาอาจ shift

## Pricing ปัจจุบัน (2026-09, จาก ollama.com/pricing)

| Tier | ราคา | รวม | เหมาะใคร |
|---|---|---|---|
| **Free** | $0 | local models (always free) + starter credits | เริ่มเล่น, private, local-only |
| **Pro** | $20/mo ($200/yr → $16.67/mo annual) | $60 usage credits/mo, model ใหญ่, concurrent, fast mode (coming soon) | ใช้จริงจัง, agent day-to-day |
| **Max** | $100/mo | $300 credits/mo, early access, 10 concurrent requests | power user, multi-agent |
| **Team** | $500/mo | unlimited users, $1,000 credits shared, centralized billing, priority support | ทีม, on-prem/compliance |
| **Enterprise** | custom | model access controls, cost budgets, private Slack, security questionnaires | องค์กร, volume |

Model pricing (per 1M tokens, input/output): glm-5.3 $1.40/$4.40 · deepseek-v4-flash $0.22/$0.66 · gpt-oss:20b $0.07/$0.30 · nemotron-3-super $0.015/$0.60 · kimi-k3 $3.00/$15.00 — **peak pricing 12:00–18:00 UTC**

## Pro Tips แยกตามระดับ

- **มือใหม่:** install app (mac/Win) → `ollama run gemma4` → drag PDF/โค้ด → chat — จบ ใช้ model เล็ก local ให้ทัน RAM
- **ใช้จริงจัง:** เลือก quantized model ที่ fit VRAM ของคุณ; สลับ `:cloud` สำหรับ task ใหญ่, local สำหรับงาน sensitive; เพิ่ม context length ใน settings ตอน process เอกสารยาว; เชื่อมเข้า Claude Code / Hermes Agent / Open WebUI
- **องค์กร:** Team/Enterprise tier — model access controls, cost budgets, schedule งานช่วง off-peak (หลีก 12:00–18:00 UTC) ลด peak pricing

## สรุปแบบวิศวกรเป็ด

Ollama คือ "single source of truth สำหรับรัน LLM บนเครื่องตัวเอง" คับ — local mode = data stays yours + free + offline, cloud mode = สเกลขึ้นเมื่อต้องการ โดย**ไม่ต้องเปลี่ยน tool/workflow** (คำสั่งเดียวกัน, integration เดียวกัน)

**เหมาะสำหรับ:**
- นักพัฒนา/คนทำ automation ที่อยากคุม data + ลดค่า API (local)
- คนใช้ agent (Claude Code, Codex, Hermes, OpenClaw) ที่อยากสลับไป open model เพื่อประหยัด
- องค์กรที่ต้องการ on-prem / compliance (Team/Enterprise)
- คนที่เครื่องสเปกแรง อยากรัน offline ไม่ง้อเน็ต

**ไม่เหมาะ (ตามตรง):**
- เครื่องสเปกต่ำที่อยากใช้ frontier model แบบไม่จ่าย → ต้อง cloud (ค่าใช้ + data ออกไป)
- คนที่อยาก SOTA reasoning เต็มรูปแบบโดยไม่ง้อ hardware — Ollama = open model, top closed ยังนำบน task ยากสุด

ระบบ > ค่า token: ปล่อยให้ข้อมูลนอนในบ้าน (local) แล้วค่อยสเกล (cloud) — คุมได้, พอรอด, ไม่ตกอยู่ใน per-token bill ไร้กำหนด

#Adduckivity #DuckOS #NeuroDivergent #Ollama #LocalLLM #AI
