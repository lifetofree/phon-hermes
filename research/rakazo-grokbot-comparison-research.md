---
type: research
topic: "Rakazo vs Grok Bot — คู่แฝดหรือไม่ (สายพันธุ์เดียว / ที่อยู่ต่างกัน) + pain point ฝั่งบ้านเช่า"
used_by: "[[pair-124]]"
verified: 2026-11-19
---

# Rakazo vs Grok Bot — comparison research (verify 2026-11-19)

## คำตอบแกน: แฝดสายพันธุ์เดียว — เลี้ยงคนละบ้าน
- rakazo README (primary): "Rakazo is an open source, self-hosted alternative to Grok Bot" + หน้าเทียบ rakazo.com/grok-bot-alternative/ (Updated November 18, 2026) มีส่วน "Move your Grok Bot to Rakazo"
- สายพันธุ์เดียว = named bots + computer ของตัวเอง + routines + memory + ทำงานขนาน + approvals — ฟีเจอร์ mirror กัน 1:1

## Grok Bot (ฝั่ง xAI — primary ทุกตัว ดึง 2026-11-19)
1. **x.ai/bot**: "AI teammates that finish the work" — บอตทำงานใน Slack, มี computer ของตัวเอง, ทำงานขนาน 24/7 แม้ปิด laptop, ส่งงานต่อกัน, เรียนรู้วิธีทำงานของทีม
2. **x.ai/news/grok-bot-1-0** (datePublished **2026-11-11**): Grok Bot 1.0 — (a) Multiplayer: แชร์บอตให้ทีม + พาเข้า Slack/Teams/video calls + "Bots learn from everyone they work with" (b) Proactive: บอตเห็นงานที่ต้องทำแล้วเสนอรับเอง + ตามงานค้าง (c) เก่งขึ้น: browser + เขียนเอกสาร + presentation; Team Bots ต้องแผน Team/Enterprise; **Meetings เฉพาะ Team, Enterprise และ Ultra**
3. **x.ai/pricing + docs.x.ai/x-subscription/pricing** (ตรวจ 19 พ.ย. 2026): Free $0 / Plus $8 / Premium $30 / Super $100 / Ultra $200; **Grok Bot อยู่เฉพาะ Premium ขึ้นไป — Plus ไม่รวม**; โควตา = **shared weekly pool** ครอบ Chat/Imagine/Voice/Bot + Cursor ("allowance refreshes weekly... top-ups"); **โมเดล 3rd-party มีเฉพาะใน Cursor จ่ายแยกตาม API list price**; Teams จ่ายต่อ seat ตาม tier; ราคาไม่รวมภาษี, "prices subject to change"

## คำโปรยฝั่ง rakazo (vendor-vs-vendor — ติดป้ายทุกจุด)
- grok-bot-alternative page: "Grok Bot is xAI's hosted product for named bots, a computer they can use, routines, and approvals. The public docs describe a cloud computer on your account. They do not describe installing the service yourself or connecting your own model provider."
- **จุดขยี้แหลมสุด (มาจาก docs rakazo เอง): "Move your Grok Bot to Rakazo — Import a bot's instructions, memory, skills, and supported routines. Routines come over paused... Chat history, computer files, and sign-ins stay in Grok Bot."** = ยกบอตย้ายบ้านได้แต่ไม่ครบทุกอย่าง
- "How to choose: Choose an agent you run yourself when the computer and the model key should stay with you"
- License rakazo = Apache-2.0 (GitHub API: 9,074 stars, Apache License 2.0)

## ภูมิประเทศรอบตัว (จากหน้าเดียวกัน — ใช้เป็นบริบทได้ ไม่ต้องลงเนื้อ)
OpenClaw (MIT, เครื่องเรา) · Hermes Agent (Nous Research, MIT) · Meta Muse (hosted VM ของ Meta, ประกาศ 8 ก.ย. 2026) · OpenAI Dots (ประกาศ 29 ก.ย. 2026, cloud computer ต่อ dot) · Hark Pro (6 ต.ค. 2026, $20/$100) · Claude Duet (21 ต.ค. 2026, cloud computer ของ Anthropic) — **ตลาด AI-teammates แตกเป็นสองค่าย: hosted subscription vs self-host** ตั้งแต่ ก.ย.–พ.ย. 2026

## Pain point ฝั่งบ้านเช่า (ทุกจุดมี primary source ยึด)
1. เกณฑ์แผน: บอตถูกขั้นไว้ที่ $30+; Plus $8 มี chat/voice/imagine แต่ไม่มีบอต; Team Bots/Meetings ไล่ขั้นตามแผนทีม
2. Pool รายสัปดาห์แชร์: งานบอตหนักวันเดียวกินโควตาที่ใช้ร่วมกับ chat/Cursor — ต้อง top-up หรือรอหมดสัปดาห์
3. โมเดลล็อก: บอตใช้ได้แต่ Grok models — third-party ไม่ได้อยู่ในบอต
4. ความจำอยู่บ้านเช่า: cloud computer บนบัญชี xAI; ย้ายบ้านก็ยกไม่ได้หมด (chat history/computer files/sign-ins ค้าง)

## Pain point ฝั่งบ้านเรา (ความจริงใจ — จากเครื่องจริง)
- จ่ายด้วยงานดูแล: credential/scope/การ harden — จาก lane #121-#123 ยังมีค้าง (Notion MCP ลงซ้ำ 2 รายการ = cleanup candidate, token ยัง scope กว้าง) — เขียนระดับ class ไม่รีเทลเรื่อง 403 (guard)

## สำหรับ draft (#124)
- โครง: สายพันธุ์เดียวจริง → ตาราง 6 แกน → ขยี้ 4 pain point (ราคาไล่ขั้น / pool / โมเดลล็อก / ความจำบ้านเช่า+ย้ายไม่ครบ) → ราคาฝั่งเรา = งานดูแล → duck
- ทุก fact Grok Bot = reported speech "ตามหน้าราคา/เอกสารของทีมผู้ทำ" + วันตรวจ 19 พ.ย. 2026; fact rakazo-import = "ทีมผู้ทำ Rakazo เขียนไว้"
- Sibling guard: #121/#122/#123 — ไม่รีเทล deployment/403, ไม่ซ้ำเลข connections 0 / routines 9 / Notion MCP (ห้ามใช้เลข DB ของเครื่องซ้ำ); axis ของ #124 = การวางตัวสินค้า + custody
