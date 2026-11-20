<!--
PAIR: #124 rakazo-vs-grokbot-twins (TECH lane)
Status: draft v2 (2026-11-19 เย็น — owner: "เช็คข้อมูล เหมือนตอนนี้ grokbot อัปเดตเวอร์ชันแล้ว" → re-verify + เพิ่ม section "เมื่อคืนแฝดอัปเดตทั้งคู่" + subtitle ใหม่; v1 filed 19 พ.ย. เช้า, Notion 41ddf8d8-8d8c-81b5-aafd-c22aed3b5337 — PATCH replace ตาม v2)
FORM: TECH v2 — comparison review (ตารางเทียบ form-legitimate ตาม spec TECH) — คำตอบแกน: แฝดสายพันธุ์เดียว เลี้ยงคนละบ้าน
REGISTER: TECH — เลขอารบิก/$ form-legitimate, ชื่อผลิตภัณฑ์/version ในเนื้อได้, พร 0, เรา = มุมผู้ใช้ Rakazo
RESEARCH: research/rakazo-grokbot-comparison-research.md (verified 2026-11-19 เช้า + re-verify เย็น)
FACT LEDGER (primary sources ดึง 2026-11-19): (1) rakazo README: "open source, self-hosted alternative to Grok Bot" + license Apache-2.0 (GitHub API) (2) rakazo.com/grok-bot-alternative/ updated 18 พ.ย. 2026 — Grok Bot = "xAI's hosted product for named bots, a computer they can use, routines, and approvals"; docs describe cloud computer on your account, no self-install, no own model provider (3) import claim: ยกมาได้ instructions/memory/skills/routines (มาแบบ paused); "Chat history, computer files, and sign-ins stay in Grok Bot" (4) x.ai/news/grok-bot-1-0 datePublished 2026-11-11 — multiplayer (Slack/Teams/video calls + learns team knowledge), proactive (เห็นงาน เสนอรับเอง ตามงานค้าง), browser+docs+presentations; Team Bots = Team/Enterprise; Meetings = Team/Enterprise/Ultra (5) x.ai/pricing + docs.x.ai (ตรวจ 19 พ.ย.): Free $0 / Plus $8 / Premium $30 / Super $100 / Ultra $200 — Grok Bot เฉพาะ Premium+; Plus ไม่รวม; usage = shared weekly pool (Chat/Imagine/Voice/Bot/Cursor) + top-ups; 3rd-party models เฉพาะใน Cursor จ่ายแยก API list price
VENDOR CLAIMS (reported speech): fact Grok Bot ทั้งหมด = ประกาศ/หน้าราคา/changelog ของทีมผู้ทำ (xAI) — ติดป้าย "ตามหน้าราคา/changelog/ประกาศของทีมผู้ทำ"; fact import = ทีมผู้ทำ Rakazo เขียนไว้ (vendor-vs-vendor) — ทุกจุดระบุเจ้าของคำพูด
FACT LEDGER v2 (re-verify 2026-11-19 เย็น): (10) Grok Bot app **v1.2.3 (18 พ.ย.)** — changelog: tool permissions 4 ระดับ (Always allow/Auto-review/Needs approval/Blocked) + routine reconnect cards; แอปอัปเดตแล้ว restart เอง (11) เวอร์ชันลำดับใน changelog: 0.70.2 → 0.79.2 → 1.1.0 → 1.2.x — จาก 1.0 (11 พ.ย.) ถึง 1.2.3 (18 พ.ย.) ใน 7 วัน (12) **Grok 4.7** — ประกาศ 22 ก.ย., grok-4.7 บน API 13 พ.ย. (release notes, context 500k) (13) **Rakazo v0.13.0 (18 พ.ย. 23:25 UTC)** — approval settings ข้าม routines + connected chat apps; unattended approvals expire 30 นาที (14) pricing ตรวจซ้ำเย็น 19 พ.ย. — ไม่เปลี่ยน; rakazo stars 9,245 (+171 จากเช้า)
SIBLING GUARD: #121 rakazo-local-docker + #122 app-connections + #123 automation-use-cases (ทั้งสาม published/draft สายเดียวกัน) — axis แยก = #124 การวางตัวสินค้า + ที่อยู่ของความจำ/โมเดล/โควตา (ไม่รีวิวช่องทางต่อ ไม่รีวิวทริกเกอร์ ไม่รีเทล deployment); คำ guard = 0: 403, cherry-pick, egress, RAM 2GB, compose up, 5.2GB, YouTube Library, token, 5173, /mnt/inbox, Git event, watch, webhook; เลข DB เครื่อง (connections 0 / routines 9 / 77 tools / 270 runs) = 0 — บทนี้ไม่ใช้เลขเครื่องเลย (หมายเหตุ: คำ routine ใช้ได้ในฐานะชื่อฟีเจอร์ของสองผลิตภัณฑ์ ไม่ใช่การวิเคราะห์ทริกเกอร์)
GUARDS v2 (วัดจริงหลังเพิ่ม section): พร 0 real / FP พร-lookalike ×1 ("เมื่อพร้อม" declared lesson 5), เพราะ 0 / เรา 14 raw (battery นับ 9 = undercount compound — register เดิม) / คุณ-ผม-คับ-ฉัน 0 / sibling guard terms 0 ทั้ง 17 (battery PASS) — เลข DB เครื่องจาก #121-#123 ไม่ปรากฏ / odd codepoints form-legitimate (TECH comparison): '|' ×32 (ตาราง) + '$' ×5 + ',' ×3 + '/' ×2
SECRET HYGIENE: ไม่มีค่าจาก .env, ไม่มี hostname
Notion: POST ใหม่ Content Drafts DB หลัง battery PASS | Status draft รอ Benz r1
-->

# Grok Bot กับ Rakazo — AI teammates สายพันธุ์เดียวกัน ที่ถูกเลี้ยงคนละบ้าน

### เทียบกันค่ำวันที่ 19 พ.ย. — แฝดอัปเดตเมื่อคืนทั้งคู่ (18 พ.ย.) ฝั่งโน้นเริ่มที่แผน $30 ต่อเดือน ฝั่งเราเป็นซอฟต์แวร์ฟรีที่วิ่งบนเครื่องนี้อยู่แล้ว

.

## สายพันธุ์เดียวกันจริง

บอตที่มีชื่อของตัวเอง มีคอมพิวเตอร์ให้ใช้ มีความจำ มีตารางงาน ทำงานขนานได้ และขออนุมัติก่อนแตะของสำคัญ — นิยามนี้ตรงกันทั้งสองฝั่ง

Grok Bot 1.0 ตามประกาศของทีมผู้ทำ เพิ่มสามอย่าง — บอตแชร์ให้ทั้งทีมใช้และเข้า Slack, Microsoft Teams กับวิดีโอคอลได้ / บอตเห็นงานที่ค้างแล้วเสนอรับทำเอง / ใช้ browser เขียนเอกสารกับทำ presentation ได้เร็วขึ้น

Rakazo มีของคู่กันทุกช่อง — ทีมบอตในแชตกลุ่มแบ่งงานกัน มีตารางงาน และบอตแต่ละตัวมีคอมพิวเตอร์ของตัวเองบนเครื่องที่เราถือ

ที่ README เขียนไว้ตรง ๆ คือ Rakazo เป็น open source alternative ของ Grok Bot — ไม่ได้แอบอ้างเป็นอย่างอื่น

.

## ตารางเทียบ

| แกนเทียบ | Grok Bot — บ้านเช่า | Rakazo — บ้านเรา |
|---|---|---|
| ที่อยู่ของบอต | cloud computer บนบัญชีผู้ให้บริการ | เครื่องที่เรา self-host |
| โมเดล | Grok เท่านั้น | อะไรก็ได้ — key เราหรือโมเดลบนเครื่อง |
| เข้าถึงได้ที่แผน | Premium $30 ขึ้นไป (Plus $8 ไม่รวมบอต) | ซอฟต์แวร์ฟรี Apache-2.0 |
| โควตา | pool รายสัปดาห์แชร์กับแชต ภาพ เสียง และ Cursor | เพดานเครื่องของเราเอง |
| ความจำของทีม | บนเซิร์ฟเวอร์ผู้ให้บริการ | ในเครื่องที่เราถือกุญแจ |
| ย้ายบ้านออก | — | ยกมาได้บางส่วน บางอย่างค้างบ้านเดิม |

.

## เมื่อคืนแฝดอัปเดตทั้งคู่

วันที่ 18 พ.ย. ทั้งสองฝั่งปล่อยเวอร์ชันใหม่ในคืนเดียวกัน

ฝั่งบ้านเช่า — changelog ของ Grok Bot ระบุเวอร์ชันแอปล่าสุด v1.2.3 เพิ่มการกำหนดสิทธิ์เครื่องมือเป็นสี่ระดับ ตั้งแต่ปล่อยผ่านอัตโนมัติจนถึงบล็อก และระบบแจ้งเตือนให้ reconnect เมื่อ routine หมดการ sign-in

ฝั่งบ้านเรา — Rakazo ออก v0.13.0 ขยายกฎ approval ให้ครอบคลุมทั้ง routine และแชตที่เชื่อมต่อ

โมเดลหลังบอตฝั่งโน้นก็เป็นรุ่นใหม่ Grok 4.7 เข้า API เมื่อ 13 พ.ย. ตาม release notes

จังหวะนี้เห็นความต่างที่ตารางไม่ได้บอก — บ้านเช่าได้เวอร์ชันใหม่เองโดยที่เราไม่ต้องทำอะไร แอปอัปเดตแล้วรีสตาร์ทเองเมื่อพร้อม ส่วนบ้านเราจะได้ v0.13.0 ก็ต่อเมื่อเราเป็นคนดึงมา

ทั้งคู่ปล่อยเร็วพอ ๆ กัน — ต่างกันที่ว่าใครเป็นคนกดปุ่ม

.

## ราคาของบ้านเช่า

ตามหน้าราคา บอตไม่ได้อยู่ในแผนถูกสุดที่มี — แผน $8 มีแชต เสียง และสร้างภาพ แต่ไม่มีบอต ต้องขยับไป $30 ขึ้นไป บอตแบบทีมทั้งทีมใช้ร่วมกันต้องแผน Team ขึ้นไป และการให้บอตเข้าประชุมก็ไล่ขั้นอีกที

โควตาเป็น pool รายสัปดาห์ที่แชร์กันทั้งแชต ภาพ เสียง บอต และ Cursor — งานบอตหนักวันเดียวกินโควตาของทั้งสัปดาห์ จะต่อต้อง top-up เพิ่ม

โมเดลก็ล็อกอยู่กับ Grok — โมเดลอื่นไม่ได้อยู่ในบอต มีเฉพาะใน Cursor ตัวเขียนโค้ด และจ่ายแยกตามราคา API

จุดที่แหลมที่สุดคือความจำ — ความจำของบอตและทีมอยู่บน cloud computer ในบัญชีของผู้ให้บริการ และทีมผู้ทำ Rakazo เขียนวิธีย้ายบอตมาฝั่งตัวเองไว้ สิ่งที่ยกมาได้มีแค่ชุดคำสั่ง ความจำ skills และตารางงานที่มาแบบหยุดรอเปิด — chat history ไฟล์บนเครื่อง และ sign-in ทั้งหมดยังค้างอยู่บ้านเดิม

.

## ราคาของบ้านเรา

ซอฟต์แวร์ฟรี Apache-2.0 แต่ค่าใช้จ่ายอีกด้านคืองานดูแล — credential, scope, การเก็บกวาด ทั้งหมดเป็นงานของเรา บนเครื่องนี้ก็ยังมีงานเก็บกวาดค้างรายการหนึ่ง

สิ่งที่แลกกลับมา — โมเดลเลือกเอง งานไม่ออกนอกบ้าน และความจำของทีมอยู่ในเครื่องที่เราถือกุญแจเอง

.

## #สรุปแบบวิศวกรเป็ด

แฝดสายพันธุ์เดียว — ความสามารถพอ ๆ กัน ทั้งสองฝั่ง

ต่างกันที่กุญแจบ้าน — ฝั่งหนึ่งจ่ายรายเดือนเช่าทั้งโควตา โมเดล และความจำ อีกฝั่งจ่ายด้วยงานดูแล

คำถามตัดสินไม่ใช่ฝั่งไหนเก่งกว่า — แต่สิ่งไหนยอมให้คนอื่นถือ ระหว่างโควตา โมเดล กับความจำของทีม

.

#Adduckivity #DuckOS #NeuroDivergent #SelfHosted #AIAgent #AIComparison
