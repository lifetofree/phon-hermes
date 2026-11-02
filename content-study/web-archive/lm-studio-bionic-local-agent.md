<!-- Archived from https://wp.adduckivity.com/lm-studio-bionic-local-agent/ on 2026-09-17 by sync_wp_posts.py -->
Title: Bionic — agent ตัวแรกที่ code ของคุณไม่เคยออกจากเครื่อง
Date: 2026-09-17T13:09:49
Link: https://wp.adduckivity.com/lm-studio-bionic-local-agent/
-->

Bionic — agent ตัวแรกที่ code ของคุณไม่เคยออกจากเครื่อง

Local LLM เคยติดอยู่ใน chat box มาตลอด

ลองคิดตามดูคับ — คนส่วนใหญ่ที่ลง local LLM แล้วทำอะไรได้บ้าง?

ถามจริง: chat

.

download model มาได้, chat ได้, บางที attach PDF — แล้วจบตรงนั้น เพราะ “agent” ที่เราเคยเห็นในข่าว (Claude Code, Codex, Cursor) ทั้งหมดรันบน model ของ cloud — code ของคุณเดินทางออกจากเครื่องไปทุก request

.

Bionic คือ agent ตัวแรกที่แก้ปัญหานี้ตรงๆ — มันคือ agent ของ open models ที่รันบน เครื่องคุณเอง — launch 16 กรกฎาคม 2026 — จุดขายเดียว: agent ที่ code ของคุณไม่เคยออกจากเครื่อง — และถ้าวันไหนงานหนักเกิน hardware ของคุณ มันค่อยส่งต่อให้ frontier open models ใน cloud แบบ Zero Data Retention — จ่ายตาม token

.

บทความนี้คือ deep-dive: Bionic ทำงานยังไง, features ครบ, ราคา, ข้อดีข้อเสียตรงๆ, เทียบ Claude Code/Codex/Cursor, และเหมาะกับใคร — บทความนี้เจาะลึกเฉพาะชั้น Execution Layer ของ Bionic ต่อเนื่องจากโครงสร้างพื้นฐานของ LM Studio — เพราะ Bionic กินทุกอย่างจาก ecosystem นั้น

.

Bionic คืออะไร — “agent ที่ไม่ได้อยู่ใน chat”

LM Studio Bionic = desktop app แยกจาก LM Studio app (download แยก ใช้คู่กันได้) — agent สำหรับ open models — ทำ coding, research, และงานเอกสาร/ไฟล์จริง — model เลือกได้ per session: local (เครื่องคุณ, $0) / cloud (frontier open models, LM Studio Secure Cloud, US-based ZDR, pay-per-token) / remote (model ของเครื่องอื่นผ่าน LM Link)

สิ่งที่คนเข้าใจผิด: Bionic ไม่ใช่ “tab ใหม่ใน LM Studio” — เป็น app ตัวใหม่ที่มี positioning ของตัวเอง — “the next generation of LM Studio designed for agentic work” — LM Studio ตัวเดิมยังอยู่สำหรับ low-level config (presets, offload, server) — Bionic = ชั้น agent ที่ซ้อนอยู่ด้านบน

.

structure ของ Bionic = Projects → Sessions (นี่คือ architectural choice ที่ทำให้มันใช้ทำงานจริงได้):

ระดับคืออะไรตัวอย่าง
Projectกลุ่มงานที่ share context เดียวกัน (ไฟล์ + codebase + instructions)“โปรเจกต์เว็บร้าน” — ชี้ไปที่ repo, attach ไฟล์ spec ไว้ที่เดียว
Sessionงาน task-wise ใน project — history แยกกันsession 1 = fix bug, session 2 = เขียน docs, session 3 = refactor

session ทำงานเป็น tabs — แทรก session tab ไปครึ่งซ้าย/ขวา = side-by-side เปรียบเทียบงาน 2 task ได้ — กด Fork ที่ response = แตก branch ของ conversation ไปลองทางอื่น — และจุดที่คนชอบ: background sessions — ปิด tab / สลับ project = session ที่รันอยู่ ไม่หยุด — มันทำงานต่อในเบื้องหลัง (เหมือน CI ที่รันบนเครื่องคุณ)

.

โหมดการทำงาน — Code กับ Work

Bionic แยกงานเป็น 2 project types — แยกตั้งแต่ตอน create project:

.

Code project — เปิด “Allow coding” → เลือก working directory (root ของ repo) — Bionic index โฟลเดอร์ เพื่อ search ทั้งโปรเจกต์ — ถ้าเป็น Git repo = Files panel โชว์ repo + branch ปัจจุบัน — features: search repo, edit files, ใช้ Git, รัน shell commands ใน working directory — docs แนะนำ workflow ปลอดภัยแบบ inspect → change → test: ให้มัน inspect + อธิบายโค้ดก่อน → ยืนยัน intent ของ change → ปล่อยให้ edit → ให้รันเฉพาะ test ที่เกี่ยวข้อง → review inline diffs + Git diff ก่อน keep — งานที่ยาวๆ มันแตกเป็น sub-sessions รัน parallel เพื่อ investigate หลายจุดพร้อมกัน

.

Work project — sandbox สำหรับเอกสาร — attach ไฟล์หรือให้มันสร้างใหม่: documents, decks, spreadsheets, PDFs, images, text — use cases ที่ docs ยก: research + เปรียบเทียบ sources, สรุป notes, ร่าง/แก้ reports, สร้าง presentation, วิเคราะห์ tables — ตัวอย่าง prompt ใน docs: “Compare the three attached proposals. Create a concise decision memo with a recommendation, risks, and a comparison table. Save it as decision-memo.md” — หรือ “Turn these meeting notes into a 6-slide presentation for a project review” — toggle Web Search (Settings → General) ให้มันดึง context สดจากเว็บได้ (web search ของ ecosystem ใช้ ZDR — ต้อง login, มี limit)

.

detail ที่ต้องรู้: Project Files = ไฟล์ที่ managed โดย project (drag เข้ามา หรือ Bionic สร้าง) — share ระหว่าง sessions ใน project เดียว — External Files = ไฟล์ข้างนอกที่ยังอยู่ตำแหน่งเดิม — Bionic แก้ไขได้ ที่ไฟล์ต้นฉบับโดยตรง — ดีและอันตรายในเวลาเดียวกัน (review ทุก change) — การให้ Agent เข้าถึง Working Directory โดยไม่มี Git Version Control หรือ Sandbox คือ System Vulnerability ขั้นร้ายแรง

.

Model Picker — “3 ที่ ที่ model ของคุณรันได้”

หัวใจของ Bionic คือ เลือก model ได้ per session — และ 3 ตัวเลือกนี้คือเหตุผลที่ ecosystem LM Studio มีค่า:

Modeรันที่ไหนค่าใช้จ่ายใช้เมื่อ
Localเครื่องคุณ (llama.cpp + MLX)$0 — ไม่ต้อง set billingงานประจำวัน, code ที่ “ต้องไม่ออกเครื่อง”, เครื่องแรงพอ
CloudLM Studio Secure Cloud (US) — ZDRCredits pay-per-tokenงานหนักเกิน hardware, ต้องการ frontier open models
Remoteเครื่องอื่นผ่าน LM Link (Tailscale E2E)$0 — inference อยู่ที่เครื่องที่ linklaptop/มือถือใช้ model ใหญ่บน desktop ที่บ้าน

remote mode คือของดีที่คนมองข้าม: conversation อยู่ที่เครื่องคุณ แต่ inference อยู่ที่เครื่องที่ link — desktop 5060 Ti ที่บ้านรัน GLM-5.3 ให้ laptop ในคาเฟ่ใช้ผ่าน app Locally — ฟรี 5 devices (ถ้าอ่าน Tailscale series มา — LM Link = Tailscale ที่ Element Labs ห่อมาให้) — model picker ยังให้ตั้ง reasoning level per session (ถ้า model รองรับ) และตั้ง Root model default ที่ Settings → General

.

local models download ใน Bionic ได้เลย (Settings → Local Models → Explore) — มี device-fit info บอกว่า model ไหน fit hardware ของคุณ — pause/resume/cancel/retry — โหลดไปเครื่องอื่นผ่าน LM Link ก็เลือกได้

.

Voice + Skills — 2 features ที่ทำให้ Bionic “ไม่ใช่แค่ coding agent”

Voice input — local — พูดกับ Bionic แบบพูดงานจริงๆ → transcribe บนเครื่อง ด้วย Voxtral ของ Mistral AI — realtime + หลายภาษา — “your voice data is processed locally and never leaves your device” — ตั้ง Auto load voice model ได้ (ถ้าไม่ตั้ง รอบแรกมันต้อง load model ก่อน) — สำหรับคนที่คิดงานด้วยปาก = workflow ที่ไม่ต้องพิมพ์

.

Skills — format เดียวกับ Codex/Claude Code — Bionic ใช้ Agent Skills standard (SKILL.md + ไฟล์เสริม) — 4 วิธีจัดการ:

ใช้ — Bionic auto-select skill ที่ relevant เอง หรือพิมพ์ @ ใน composer → reference palette → เลือก skill/ไฟล์ตรงๆ

สร้าง — ทำงานเสร็จแล้วที่ work → สั่ง “Create a skill based on what we just did” — Bionic ถามกลับ + ร่าง skill ให้

install — ให้ URL (GitHub repo / link ตรง) → Bionic install — หรือ @Install Skill

ยืมจาก app อื่น — Settings → Skills → “Use skills found in other apps” — skills ที่ใช้กับ Codex/Claude Code อยู่แล้ว port มาได้โดยตรง — disable ทีละตัวได้

.

ข้อนี้สำคัญกว่าที่คิด: ถ้าทีมสะสม skills มาแล้วใน Claude Code/Codex — มันไม่ใช่ sunk cost — มันย้ายมา Bionic ได้ และ skill ที่ Bionic สร้างใหม่จาก workflow ของเรา = asset ที่ใช้ซ้ำได้ทุกระบบที่รองรับ Agent Skills format

.

use cases ที่ docs แนะนำ: checklist review เอกสาร, สร้าง deliverables (reports/decks/spreadsheets) ตาม template, style guide ของทีม, research workflow ที่ทำซ้ำ, file format/tool เฉพาะทาง — tips: ทบทวน skill ใหม่ทุกครั้งก่อนใช้กับงานสำคัญ (skill ที่ install มาจาก URL = untrusted input)

.

Pricing — ฟรีจริง

รายละเอียด (lmstudio.ai/pricing • docs, 09/2026)
Free — $0app + local LLMs + local voice ไม่จำกัด • web search tool (ZDR, ต้อง login, มี limit) + LM Link 5 devices — local + remote = ไม่แตะ billing
Cloud creditsPay-as-you-go — US-based inference, Zero Data Retention by default — ใช้ credit เฉพาะตอน session เลือก cloud model
Bionic PassSubscription ที่ประกาศแล้ว — “Pricing and plan details coming soon” — ยังไม่มีราคา (third-party review ยืนยันชื่อ “Bionic Pass”)

ราคา cloud credits ต่อ 1M tokens (input / cached / output):

ModelPrice
DeepSeek V4 Flash$0.13 / $0.028 / $0.26
GLM-5.3-Flash$0.15 / $0.03 / $0.50
Kimi K2.6 / Kimi-K2.7-Code$0.95 / $0.16 / $4.00
DeepSeek V4 Pro$1.32 / $0.132 / $3.96
GLM-5.3$1.40 / $0.14 / $4.40
GLM-5.2$1.50 / $0.30 / $4.50
Kimi K3$3.00 / $0.30 / $15.00

Billing page โชว์ usage 30 วันล่าสุด เป็น totals (ไม่ใช่ fixed cost per task — model + ขนาด request กำหนด) — credit หมดเมื่อไหร่ local mode ยังทำงานต่อไม่สะดุด — นี่คือ architectural point: Bionic ไม่ได้บังคับให้คุณมี subscription — ต่างจาก coding agent mainstream ที่ $20/เดือนเป็น floor

.

Pros ✅

Agent ฟรีที่ code ไม่ออกเครื่อง — local model = source code, เอกสาร, voice — ไม่ไปไหน — coding agent ตัวอื่น (Claude Code/Codex/Cursor) = code ผ่าน cloud ทุก request — Bionic คือทางเลือกเดียวที่ “agentic” + “local” จริง

$0 floor = ต่ำกว่า industry — coding agents ใน index เปรียบเทียบมี entry price ปานกลาง $20/เดือน — Bionic = $0 + จ่ายเฉพาะ burst ที่ต้องการ frontier model

3-tier model routing — local/cloud/remote per session — งานเบา=ฟรี, งานหนัก=frontier, เครื่องบ้าน=remote via LM Link — 1 agent 3 compute layers

Skills portability — SKILL.md standard — skills ที่มีจาก Codex/Claude Code ใช้ได้ + สร้างใหม่ได้ — workflow ที่พิสูจน์แล้ว = asset ที่ย้ายได้

Parallel + background sessions — tabs, side-by-side, fork, background continuation — agent ที่ “ทำงานต่อแม้เราไปกินข้าว” (บนเครื่องเรา)

Voice local (Voxtral) — dictation ที่ไม่ส่งเสียงไป cloud — multilingual realtime

Ecosystem เดียวกับ LM Studio — model ที่โหลดไว้ใช้ร่วมกัน, LM Link 5 devices ฟรี, OpenAI/Anthropic-compat API ของ app เดิมยังอยู่ — ไม่เริ่ม ecosystem ใหม่

.

Cons ❌

Output quality = hardware × model ของคุณ — นี่คือข้อเสียที่ใหญ่ที่สุด: agent ที่ “ฟรี” แต่รันบน Qwen 7B Q4 กับ agent ที่รันบน GLM-5.3 = คนละระดับกับ Claude/GPT frontier — open models ยังตาม closed frontier ใน agentic tasks ยาวๆ — Bionic ให้ harness ที่ดี แต่ไม่ magic model — (ทางออก: burst ไป cloud — ซึ่งก็คือจ่าย)

Cloud credit terms ยังบาง — pay-as-you-go page ยังไม่มี detail เรื่อง credit expiry / context limits — budget-sensitive teams ควรอ่าน term ก่อน commit (third-party review ติตรงจุดนี้เหมือนกัน)

Bionic Pass ยังไม่มีราคา — subscription ที่ประกาศแล้วแต่ “coming soon” — ถ้า workflow ต้องการ frontier model บ่อยๆ — ตอนนี้ยังไม่มีราคาผูกขาดที่คุ้มกว่า pay-per-token (หรืออาจคุ้ม — ยังไม่รู้)

App proprietary (closed source) — เช่นเดียวกับ LM Studio app — ฟรีแต่ inspect code ไม่ได้ — trust boundary = policy ZDR ของ vendor

Scope หลัก = code + documents + files + web search + computer control ใน project sandbox — ไม่มี multi-agent orchestration แบบ Grok Bot, ไม่มี autonomy ข้ามแอปอิสระ — ปลอดภัยดี แต่แลกกับ reach

External files = แก้ที่ต้นฉบับ — Bionic edit external file ตรงๆ ไม่มี copy — repo ใหญ่ + session ที่ปล่อยไว้ = ต้อง review Git diff จริงๆ ทุกครั้ง (docs เองบอก: “review Bionic’s diffs and command output before keeping the changes”)

ยังใหม่ (launch 16 ก.ค. 2026) — ~2 เดือน — agent ที่โตเร็ว = features ยังเปลี่ยน — skill/voice/coding ยัง polish

ไม่ใช่ fine-tuning tool — inference + agent เท่านั้น — อยาก train model ของเรา → Unsloth Studio → export GGUF → load ใน Bionic/LM Studio

.

เทียบคู่แข่ง

LM Studio BionicClaude CodeCodexCursorOllama (raw)
Price$0 local • cloud per-token$20/เดือน (subscription)$20/เดือน (หรือ ChatGPT plan)$20/เดือนฟรี (OSS)
Local model✅ (default!)⚠️ ต้อง config API เอง⚠️ ต้อง config เอง⚠️ ต้อง config เอง✅ (แต่ไม่มี agent)
Code stays on-device✅ (local mode)❌ cloud❌ cloud❌ cloud✅ (ไม่มี agent)
Documents/decks/spreadsheets✅ (work sandbox)⚠️ ผ่าน files⚠️ ผ่าน files⚠️❌
Voice (local)✅ Voxtral❌❌❌❌
Skills standard✅ SKILL.md (port จาก Codex/Claude)✅✅⚠️ rules❌
Cross-device (LM Link/Tailscale)✅ 5 devices❌❌❌⚠️ DIY
Frontier model⚠️ open frontier (ZDR)✅✅✅❌
Parallel/background sessions✅✅✅✅❌

Bottom line: Bionic ไม่ได้แข่งกับ Claude Code ในเรื่อง “model เก่งสุด” — มันแข่งในมุม “agent ที่รันบน model ของคุณได้ $0” — ถ้า privacy + hardware พร้อม = Bionic — ถ้าต้องการ frontier quality ทุก task = coding agents mainstream หรือ burst ไป cloud ใน Bionic เอง — และ complement กับ ecosystem: Unsloth Studio (train) → LM Studio app (config/serve) → Bionic (agent) — chain เดียว

.

เหมาะกับใคร

Dev ที่ code ไม่ออกจากเครื่องคือ hard requirement — repo ลูกค้า, code internal, งานที่ NDA — ชี้ Bionic ไปที่ repo, local model (Qwen3/GLM ระดับ 27B ถ้า VRAM 16-24GB) — inspect → change → test → review diffs — burst ไป GLM-5.3/DeepSeek V4 Pro เฉพาะ task ยาก ($1.32-1.50/M input) — code ส่วนใหญ่ไม่เคยออก LAN ของเรา

.

One-person business / คนทำเอกสาร — meeting notes → 6-slide deck, เปรียบเทียบ proposal → decision memo, วิเคราะห์ spreadsheet — work project + web search + voice input (พูดไอเดียตอนเดินคิด แล้ว Bionic ร่างให้) — ไม่ต้องมี subscription $20/เดือน สำหรับงานที่ local model ทำได้

.

คนที่มี hardware เดิม + LM Link — desktop ที่บ้านรัน model ใหญ่, laptop/iPhone ใช้ผ่าน Locally — remote mode = inference ที่เครื่องบ้าน แต่ agent อยู่ที่มือเรา — ฟรี 5 devices — (Tailscale series ใน archive = DIY path ของเรื่องเดียวกัน)

.

ทีมที่สะสม skills มาแล้ว — SKILL.md ใน Claude Code/Codex = port มา Bionic ได้ + “Use skills found in other apps” toggle — workflow ที่ทีมพิสูจน์แล้วไม่หาย — สร้าง skill ใหม่จาก workflow ที่สำเร็จ = ทรัพย์สินทีม

.

ไม่เหมาะ:

ต้องการ frontier quality ทุก task — open models ยังตาม — Bionic เป็น harness ไม่ใช่ model (burst cloud ได้แต่มีค่า)

เครื่องเล็ก — 8GB RAM = local model เล็ก = agent quality จำกัด (Bionic ต้อง tool calls ยาว = context กิน memory)

Intel Mac — ecosystem LM Studio ไม่รองรับ

ต้องการ multi-user/SSO/audit — เป็น desktop agent — ยังไม่มี team/enterprise control layer (Bionic Pass + Enterprise = coming)

ต้องการ multi-agent orchestration / autonomy ข้ามแอปแบบเต็มตัว — scope ปัจจุบันคือ code + work + web search + computer control ใน project sandbox

.

#สรุปแบบวิศวกรเป็ด

LM Studio Bionic = “agent ที่รันบน model ของเรา” — coding (index repo, edit, Git, shell, sub-sessions parallel) + documents (sandbox: decks/memos/spreadsheets) + voice local (Voxtral) + skills ที่ port จาก Codex/Claude Code — model 3 ชั้น: local $0 / cloud ZDR per-token / remote ผ่าน LM Link — ฟรีจริง, $0 floor, ไม่บังคับ subscription

.

exchange ที่ต้องแลก: quality = hardware × open model ของเรา, cloud terms ยังบาง, Bionic Pass ยังไม่มีราคา, app closed source, scope ยังไม่เปิด multi-agent orchestration, ยังใหม่ 2 เดือน — แต่ถ้า trust boundary คือ “code ต้องไม่ออกเครื่อง” — นี่คือ agent ตัวเดียวในตลาดที่ตอบได้โดยไม่ต้อง config เอง

.

ระบบ > friction: Law #3 Protect System — agent ที่ข้อมูลของเราไม่เดินทาง = attack surface ที่คุมได้ — Bionic ทำให้ “private agentic workflow” ไม่ใช่คำโฆษณา แต่เป็น default mode — และ Law #2 Asset > Activity — skills ที่ Bionic สร้างจาก workflow ที่สำเร็จ + project files + model ที่โหลดไว้ = asset สะสม — ไม่ใช่ $20/เดือนที่หายไปเมื่อเลิกจ่าย — ส่วน Law #1 System > Emotion: background sessions ที่ทำงานต่อตอนเราไปพัก = ระบบที่ทำงานโดยไม่พึ่งวินัยของเรา

.

ถ้า LM Studio คือ “control plane ของ local LLM” — Bionic คือ engine room — ที่ที่ model ของเราเริ่ม ทำงาน แทนเรา — ฟรี — บนเครื่องของเรา

.

#Adduckivity #DuckOS #NeuroDivergent #LMStudio #Bionic #LocalLLM #AIAgent #OpenModels #PrivacyFirst #CodingAgent
