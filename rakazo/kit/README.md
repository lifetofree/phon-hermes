# Rakazo Kit — adduck writing kit (ฝั่ง Hermes เป็นผู้ดูแล)

Kit นี้ทำให้ bot ของ Rakazo เขียน content ด้วยกรอบความคิดเดียวกับ Hermes (adduck voice + content-pipeline)
แล้วส่งเข้า **Content Drafts** ตาม pipeline เดิม โดยมี Hermes เป็นผู้กำกับสูงสุดรองจาก owner

## ลำดับอำนาจ (ตามที่ owner กำหนด 2026-11-16)

owner (สั่งทาง Telegram ถึง Hermes เหมือนเดิม) → Hermes agent → Rakazo bots

- คุณช่องทางสั่งงานหลักยังเป็น Telegram ถึง Hermes — Hermes แปลงเป็นงาน/ตรวจงาน Rakazo ต่อ
- Rakazo จบที่ Status=draft / branch ของตัวเอง / inbox เสมอ
- ผู้ถือสิทธิ์ขั้นสุด: publish, merge → main, WordPress backup sync, Books chapter-notes sync, การแก้ SKILL.md กลาง

## ไฟล์ใน kit

- `adduck-writer.md` — skill เขียน สำหรับวางใน Rakazo (Skills → New skill → วางเนื้อหา)
- `benz-critic.md` — skill **ตรวจ** (fact-check ข้ามแหล่ง + Benz-DNA critique) สำหรับวางเป็น skill ที่สองชื่อ "benz-critic"
- `adduck-SOUL.md` — สำเนา SOUL ของ adduck สำหรับให้ bot อ่านผ่าน mount (ต้นฉบับ: ~/.hermes/profiles/adduck/SOUL.md — แก้ที่ต้นฉบับแล้ว sync มาที่นี่เท่านั้น)
- `../youtube-library-sync-brief.md` — บรีฟ sync ตาราง YouTube Library → markdown → GitHub (แยกต่างหากจาก kit เขียนบท)

## Full loop เขียน → ตรวจ (kit คู่)

1. **adduck-writer** เขียน draft → Content Drafts (Status=draft) เสมอ
2. **benz-critic** ตรวจ: fact-check ทุก claim ข้ามแหล่ง ≥3 (primary ก่อน, คำกล่าวผู้ผลิต = reported speech) + quote-verify ในโค้ด + baselines + critique 5-8 จุด + gate A/B/C → archive `/mnt/inbox/critiques/`
3. **Hermes** รับ archive + gate → ยกรายงาน owner → owner ตอบ gate (ทาง Telegram เดิม)
4. การ rewrite ตาม gate = adduck-writer (หรือ Hermes) — benz-critic **ไม่ rewrite งานตัวเอง และ critique ไม่ใช่การรับรอง** (Benz r1 จริง/owner ยังตัดสินขั้นสุด)

ข้อจำกัดของ benz-critic: บอทต้องมี computer sandbox + network (fact-check ต้องค้นเว็บจริง) — ถ้าค้นไม่ได้ ทุก claim อยู่สถานะ UNVERIFIED และต้องรายงานตามจริง

## Setup ฝั่ง Rakazo (owner ทำครั้งเดียว)

1. Notion MCP: Integrations → + → MCP server → `https://mcp.notion.com/mcp` → OAuth
   เลือกแชร์ **เฉพาะ 2 DB: Content Drafts + Books Library** (ห้ามรวม Adduckivity Content / publish master)
2. Skills: สร้าง skill ใหม่ชื่อ "adduck-writer" แล้ววางเนื้อหา `adduck-writer.md`
   (หรือ import จาก GitHub folder `rakazo/kit/` ของ repo นี้ — จำไว้ว่าแบบ import script ไม่รัน kit นี้ออกแบบให้ไม่พึ่ง script จึงปลอดภัย)
3. บอทต้องมี computer (sandbox) คู่กับงาน เพื่ออ่าน mount `/mnt/hermes-agent`

## วงรับงานหลัง bot ส่ง draft (ฝั่ง Hermes ทำอยู่แล้ว)

- notion_drafts_watcher ping Telegram เมื่อเจอ draft ใหม่จากโมเดลอื่น
- Hermes ตรวจ battery ซ้ำ + sibling guard + verify ฟอร์แมต Notion → ผ่านแล้วค่อยขึ้นวง Benz r1 ตาม pipeline เดิม
- ผลตัดสิน (gate/publish) เป็นของ owner เท่านั้น — bot ไม่มีส่วนในขั้นนี้

## ทดสอบครั้งแรก (trial)

เลือกหัวข้อ 1 ชิ้น สั่งผ่าน bot ใน Rakazo ด้วยรูปแบบ:
"เขียน draft หัวข้อ <X> ตาม skill adduck-writer แล้ว file ลง Content Drafts"
→ Hermes รับตรวจ → Benz r1 ตัดสินคุณภาพเสียงเขียนก่อนใช้เป็นงานประจำ
