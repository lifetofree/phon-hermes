# Bionic — agent ตัวแรกที่ code ของคุณไม่เคยออกจากเครื่อง

**Excerpt:** Local LLM ติดอยู่ในกรอบ Chat Box มานานเกินไป Bionic คือ Agent ประจำเครื่องที่สั่งงาน แก้ไขไฟล์จริง และรันคำสั่งโดยที่โค้ดไม่เคยหลุดออกจากเครื่อง ควบคุมความปลอดภัยให้อยู่ใน Boundary ของตัวเอง
**Laws:** [[🔥 Law 2: Action > Motivation]] · [[🛡️ Law 3: Protect System]]
**Site Category:** [[📚 Asset Library]]
**Tags:** [[Adduckivity]] · [[DuckOS]] · [[NeuroDivergent]] · #LMStudio · #Bionic · [[LocalLLM]] · [[AIAgent]] · #OpenModels · #PrivacyFirst · #CodingAgent

---

## Local LLM เคยติดอยู่ใน chat box มาตลอด
ลองคิดตามดูคับ — คนส่วนใหญ่ที่ลง local LLM แล้วทำอะไรได้บ้าง?
ถามจริง: chat
.
download model มาได้, chat ได้, บางที attach PDF — แล้วจบตรงนั้น เพราะ “agent” ที่เราเคยเห็นในข่าว (Claude Code, Codex, Cursor) ทั้งหมดรันบน model ของ cloud — code ของคุณเดินทางออกจากเครื่องไปทุก request
.
Bionic คือ agent ตัวแรกที่แก้ปัญหานี้ตรงๆ — มันคือ agent ของ open models ที่รันบน เครื่องคุณเอง — launch 16 กรกฎาคม 2026 — จุดขายเดียว: agent ที่ code ของคุณไม่เคยออกจากเครื่อง — และถ้าวันไหนงานหนักเกิน hardware ของคุณ มันค่อยส่งต่อให้ frontier open models ใน cloud แบบ Zero Data Retention — จ่ายตาม token
.
บทความนี้คือ deep-dive: Bionic ทำงานยังไง, features ครบ, ราคา, ข้อดีข้อเสียตรงๆ, เทียบ Claude Code/Codex/Cursor, และเหมาะกับใคร — บทความนี้เจาะลึกเฉพาะชั้น Execution Layer ของ Bionic ต่อเนื่องจากโครงสร้างพื้นฐานของ LM Studio — เพราะ Bionic กินทุกอย่างจาก ecosystem นั้น
.
## Bionic คืออะไร — “agent ที่ไม่ได้อยู่ใน chat”
> **LM Studio Bionic = desktop app แยกจาก LM Studio app (download แยก ใช้คู่กันได้) — agent สำหรับ open models — ทำ coding, research, และงานเอกสาร/ไฟล์จริง — model เลือกได้ per session: local (เครื่องคุณ, $0) / cloud (frontier open models, LM Studio Secure Cloud, US-based ZDR, pay-per-token) / remote (model ของเครื่องอื่นผ่าน LM Link)**
สิ่งที่คนเข้าใจผิด: Bionic ไม่ใช่ “tab ใหม่ใน LM Studio” — เป็น app ตัวใหม่ที่มี positioning ของตัวเอง — “the next generation of LM Studio designed for agentic work” — LM Studio ตัวเดิมยังอยู่สำหรับ low-level config (presets, offload, server) — Bionic = ชั้น agent ที่ซ้อนอยู่ด้านบน
.
structure ของ Bionic = Projects → Sessions (นี่คือ architectural choice ที่ทำให้มันใช้ทำงานจริงได้):
session ทำงานเป็น tabs — แทรก session tab ไปครึ่งซ้าย/ขวา = side-by-side เปรียบเทียบงาน 2 task ได้ — กด Fork ที่ response = แตก branch ของ conversation ไปลองทางอื่น — และจุดที่คนชอบ: background sessions — ปิด tab / สลับ project = session ที่รันอยู่ ไม่หยุด — มันทำงานต่อในเบื้องหลัง (เหมือน CI ที่รันบนเครื่องคุณ)
.
## โหมดการทำงาน — Code กับ Work
Bionic แยกงานเป็น 2 project types — แยกตั้งแต่ตอน create project:
.
Code project — เปิด “Allow coding” → เลือก working directory (root ของ repo) — Bionic index โฟลเดอร์ เพื่อ search ทั้งโปรเจกต์ — ถ้าเป็น Git repo = Files panel โชว์ repo + branch ปัจจุบัน — features: search repo, edit files, ใช้ Git, รัน shell commands ใน working directory — docs แนะนำ workflow ปลอดภัยแบบ inspect → change → test: ให้มัน inspect + อธิบายโค้ดก่อน → ยืนยัน intent ของ change → ปล่อยให้ edit → ให้รันเฉพาะ test ที่เกี่ยวข้อง → review inline diffs + Git diff ก่อน keep — งานที่ยาวๆ มันแตกเป็น sub-sessions รัน parallel เพื่อ investigate หลายจุดพร้อมกัน
.
Work project — sandbox สำหรับเอกสาร — attach ไฟล์หรือให้มันสร้างใหม่: documents, decks, spreadsheets, PDFs, images, text — use cases ที่ docs ยก: research + เปรียบเทียบ sources, สรุป notes, ร่าง/แก้ reports, สร้าง presentation, วิเคราะห์ tables — ตัวอย่าง prompt ใน docs: “Compare the three attached proposals. Create a concise decision memo with a recommendation, risks, and a comparison table. Save it as decision-memo.md” — หรือ “Turn these meeting notes into a 6-slide presentation for a project review” — toggle Web Search (Settings → General) ให้มันดึง context สดจากเว็บได้ (web search ของ ecosystem ใช้ ZDR — ต้อง login, มี limit)
.
detail ที่ต้องรู้: Project Files = ไฟล์ที่ managed โดย project (drag เข้ามา หรือ Bionic สร้าง) — share ระหว่าง sessions ใน project เดียว — External Files = ไฟล์ข้างนอกที่ยังอยู่ตำแหน่งเดิม — Bionic แก้ไขได้ ที่ไฟล์ต้นฉบับโดยตรง — ดีและอันตรายในเวลาเดียวกัน (review ทุก change) — การให้ Agent เข้าถึง Working Directory โดยไม่มี Git Version Control หรือ Sandbox คือ System Vulnerability ขั้นร้ายแรง
.
## Model Picker — “3 ที่ ที่ model ของคุณรันได้”
หัวใจของ Bionic คือ เลือก model ได้ per session — และ 3 ตัวเลือกนี้คือเหตุผลที่ ecosystem LM Studio มีค่า:
remote mode คือของดีที่คนมองข้าม: conversation อยู่ที่เครื่องคุณ แต่ inference อยู่ที่เครื่องที่ link — desktop 5060 Ti ที่บ้านรัน GLM-5.3 ให้ laptop ในคาเฟ่ใช้ผ่าน app Locally — ฟรี 5 devices (ถ้าอ่าน Tailscale series มา — LM Link = Tailscale ที่ Element Labs ห่อมาให้) — model picker ยังให้ตั้ง reasoning level per session (ถ้า model รองรับ) และตั้ง Root model default ที่ Settings → General
.
local models download ใน Bionic ได้เลย (Settings → Local Models → Explore) — มี device-fit info บอกว่า model ไหน fit hardware ของคุณ — pause/resume/cancel/retry — โหลดไปเครื่องอื่นผ่าน LM Link ก็เลือกได้
.
## Voice + Skills — 2 features ที่ทำให้ Bionic “ไม่ใช่แค่ coding agent”
Voice input — local — พูดกับ Bionic แบบพูดงานจริงๆ → transcribe บนเครื่อง ด้วย Voxtral ของ Mistral AI — realtime + หลายภาษา — “your voice data is processed locally and never leaves your device” — ตั้ง Auto load voice model ได้ (ถ้าไม่ตั้ง รอบแรกมันต้อง load model ก่อน) — สำหรับคนที่คิดงานด้วยปาก = workflow ที่ไม่ต้องพิมพ์
.
Skills — format เดียวกับ Codex/Claude Code — Bionic ใช้ Agent Skills standard (SKILL.md + ไฟล์เสริม) — 4 วิธีจัดการ:
.
ข้อนี้สำคัญกว่าที่คิด: ถ้าทีมสะสม skills มาแล้วใน Claude Code/Codex — มันไม่ใช่ sunk cost — มันย้ายมา Bionic ได้ และ skill ที่ Bionic สร้างใหม่จาก workflow ของเรา = asset ที่ใช้ซ้ำได้ทุกระบบที่รองรับ Agent Skills format
.
use cases ที่ docs แนะนำ: checklist review เอกสาร, สร้าง deliverables (reports/decks/spreadsheets) ตาม template, style guide ของทีม, research workflow ที่ทำซ้ำ, file format/tool เฉพาะทาง — tips: ทบทวน skill ใหม่ทุกครั้งก่อนใช้กับงานสำคัญ (skill ที่ install มาจาก URL = untrusted input)
.
## Pricing — ฟรีจริง
ราคา cloud credits ต่อ 1M tokens (input / cached / output):
Billing page โชว์ usage 30 วันล่าสุด เป็น totals (ไม่ใช่ fixed cost per task — model + ขนาด request กำหนด) — credit หมดเมื่อไหร่ local mode ยังทำงานต่อไม่สะดุด — นี่คือ architectural point: Bionic ไม่ได้บังคับให้คุณมี subscription — ต่างจาก coding agent mainstream ที่ $20/เดือนเป็น floor
.
## Pros ✅
.
## Cons ❌
.
## เทียบคู่แข่ง
Bottom line: Bionic ไม่ได้แข่งกับ Claude Code ในเรื่อง “model เก่งสุด” — มันแข่งในมุม “agent ที่รันบน model ของคุณได้ $0” — ถ้า privacy + hardware พร้อม = Bionic — ถ้าต้องการ frontier quality ทุก task = coding agents mainstream หรือ burst ไป cloud ใน Bionic เอง — และ complement กับ ecosystem: Unsloth Studio (train) → LM Studio app (config/serve) → Bionic (agent) — chain เดียว
.
## เหมาะกับใคร
Dev ที่ code ไม่ออกจากเครื่องคือ hard requirement — repo ลูกค้า, code internal, งานที่ NDA — ชี้ Bionic ไปที่ repo, local model (Qwen3/GLM ระดับ 27B ถ้า VRAM 16-24GB) — inspect → change → test → review diffs — burst ไป GLM-5.3/DeepSeek V4 Pro เฉพาะ task ยาก ($1.32-1.50/M input) — code ส่วนใหญ่ไม่เคยออก LAN ของเรา
.
One-person business / คนทำเอกสาร — meeting notes → 6-slide deck, เปรียบเทียบ proposal → decision memo, วิเคราะห์ spreadsheet — work project + web search + voice input (พูดไอเดียตอนเดินคิด แล้ว Bionic ร่างให้) — ไม่ต้องมี subscription $20/เดือน สำหรับงานที่ local model ทำได้
.
คนที่มี hardware เดิม + LM Link — desktop ที่บ้านรัน model ใหญ่, laptop/iPhone ใช้ผ่าน Locally — remote mode = inference ที่เครื่องบ้าน แต่ agent อยู่ที่มือเรา — ฟรี 5 devices — (Tailscale series ใน archive = DIY path ของเรื่องเดียวกัน)
.
ทีมที่สะสม skills มาแล้ว — SKILL.md ใน Claude Code/Codex = port มา Bionic ได้ + “Use skills found in other apps” toggle — workflow ที่ทีมพิสูจน์แล้วไม่หาย — สร้าง skill ใหม่จาก workflow ที่สำเร็จ = ทรัพย์สินทีม
.
ไม่เหมาะ:
.
## #สรุปแบบวิศวกรเป็ด
LM Studio Bionic = “agent ที่รันบน model ของเรา” — coding (index repo, edit, Git, shell, sub-sessions parallel) + documents (sandbox: decks/memos/spreadsheets) + voice local (Voxtral) + skills ที่ port จาก Codex/Claude Code — model 3 ชั้น: local $0 / cloud ZDR per-token / remote ผ่าน LM Link — ฟรีจริง, $0 floor, ไม่บังคับ subscription
.
exchange ที่ต้องแลก: quality = hardware × open model ของเรา, cloud terms ยังบาง, Bionic Pass ยังไม่มีราคา, app closed source, scope ยังไม่เปิด multi-agent orchestration, ยังใหม่ 2 เดือน — แต่ถ้า trust boundary คือ “code ต้องไม่ออกเครื่อง” — นี่คือ agent ตัวเดียวในตลาดที่ตอบได้โดยไม่ต้อง config เอง
.
ระบบ > friction: Law #3 Protect System — agent ที่ข้อมูลของเราไม่เดินทาง = attack surface ที่คุมได้ — Bionic ทำให้ “private agentic workflow” ไม่ใช่คำโฆษณา แต่เป็น default mode — และ Law #2 Asset > Activity — skills ที่ Bionic สร้างจาก workflow ที่สำเร็จ + project files + model ที่โหลดไว้ = asset สะสม — ไม่ใช่ $20/เดือนที่หายไปเมื่อเลิกจ่าย — ส่วน Law #1 System > Emotion: background sessions ที่ทำงานต่อตอนเราไปพัก = ระบบที่ทำงานโดยไม่พึ่งวินัยของเรา
.
ถ้า LM Studio คือ “control plane ของ local LLM” — Bionic คือ engine room — ที่ที่ model ของเราเริ่ม ทำงาน แทนเรา — ฟรี — บนเครื่องของเรา
.
#Adduckivity #DuckOS #NeuroDivergent #LMStudio #Bionic #LocalLLM #AIAgent #OpenModels #PrivacyFirst #CodingAgent
===========
FB version
===========
Local LLM เคยติดอยู่ใน chat box มาตลอด
ลองคิดตามดูคับ — คนส่วนใหญ่ที่ลง local LLM แล้วทำอะไรได้บ้าง? ถามจริง: chat
download model มาได้, chat ได้, บางที attach PDF — แล้วจบตรงนั้น เพราะ "agent" ที่เราเคยเห็นในข่าว (Claude Code, Codex, Cursor) ทั้งหมดรันบน model ของ cloud — code ของเราเดินทางออกจากเครื่องไปทุก request
.
Bionic คือ agent ตัวแรกที่แก้ปัญหานี้ตรงๆ — agent ของ open models ที่รันบนเครื่องเราเอง (launch 16 ก.ค. 2026) — จุดขายเดียว: code ของเราไม่เคยออกจากเครื่อง — ถ้างานหนักเกิน hardware ค่อยส่งต่อ frontier open models ใน cloud แบบ Zero Data Retention จ่ายตาม token
.
มันคือ desktop app แยกจาก LM Studio (ใช้คู่กันได้) — โครงสร้างคือ Projects → Sessions:
.
โหมดทำงานมี 2 แบบ
Code project — Allow coding → ชี้ working directory → Bionic index repo ทั้งโปรเจกต์ → search, edit files, ใช้ Git, รัน shell commands — docs แนะนำ workflow inspect → change → test → review diffs ก่อน keep ทุกครั้ง
Work project — sandbox เอกสาร: สร้าง documents/decks/spreadsheets/PDFs, เปรียบเทียบ proposals → decision memo, meeting notes → presentation — มี Web Search toggle ให้ดึง context สด (ZDR)
.
Model picker เลือกได้ per session — 3 ที่:
ลองนึกภาพ: desktop 5060 Ti ที่บ้านรัน GLM-5.3 ให้ laptop ในคาเฟ่ใช้ — conversation อยู่ที่เครื่องเรา inference อยู่ที่บ้าน
.
สอง features ที่ทำให้ไม่ใช่แค่ coding agent:
.
ราคา: Free $0 — local + voice + LM Link 5 devices ไม่จำกัด, cloud pay-per-token (US, ZDR) — มี Bionic Pass ประกาศไว้แต่ยังไม่เปิดราคา
ตัวอย่าง cloud ต่อ 1M tokens: DeepSeek V4 Flash $0.13/$0.26 · GLM-5.3-Flash $0.15/$0.50 · Kimi K3 $3.00/$15.00 — credit หมด local ยังทำงานต่อไม่สะดุด — ไม่บังคับ subscription
.
✅ Pros: agent ฟรีที่ code ไม่ออกเครื่อง · $0 floor ต่ำกว่าตลาด $20 · 3-tier routing · skills portability · parallel + background sessions · voice local · ecosystem เดียวกับ LM Studio
❌ Cons: output quality = hardware × open model ของเรา (ไม่ magic) · cloud terms ยังบาง · Bionic Pass ยังไม่มีราคา · app closed source · scope ไม่มี multi-agent orchestration · external files = แก้ที่ต้นฉบับต้อง review diff จริง · ยังใหม่ ~2 เดือน · ไม่ใช่ fine-tuning tool
.
ใครควรใช้
ไม่เหมาะ: ต้องการ frontier ทุก task / เครื่อง 8GB / Intel Mac / ต้องการ multi-user SSO / อยากได้ multi-agent orchestration เต็มตัว
.
#สรุปแบบวิศวกรเป็ด
Bionic = "agent ที่รันบน model ของเรา" — coding + documents + voice + skills — model 3 ชั้น: local $0 / cloud ZDR / remote ผ่าน LM Link — ฟรีจริง ไม่บังคับ subscription
แลกด้วย: quality = hardware × open model, cloud terms ยังบาง, app closed source — แต่ถ้า trust boundary คือ "code ต้องไม่ออกเครื่อง" นี่คือ agent ตัวเดียวในตลาดที่ตอบได้โดยไม่ต้อง config เอง
ระบบ > friction: skills ที่ Bionic สร้าง + project files = asset ที่สะสม ไม่ใช่ $20/เดือนที่หายไปเมื่อเลิกจ่าย — และ background sessions ทำงานต่อตอนเราไปพัก โดยไม่พึ่งวินัย
ถ้า LM Studio คือ control plane — Bionic คือ engine room ที่ model เริ่มทำงานแทนเรา — ฟรี บนเครื่องของเรา
อ่านฉบับเต็ม (รายละเอียด Code/Work project + ตารางเทียบ Claude Code/Codex/Cursor + ตารางราคาครบ 8 models) → ลิงก์ในคอมเมนต์
#Adduckivity #DuckOS #LMStudio #Bionic #LocalLLM #AIAgent #PrivacyFirst #CodingAgent
===========

*Synced: 2026-11-02 19:48 +07 · [Notion](https://www.notion.so/3dedf8d88d8c8012873ee6cc80b995a5) · ✅ Published*