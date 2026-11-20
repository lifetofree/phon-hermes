# บรีฟ: E-book ติดตั้ง Rakazo — บทที่ 1 (จาก Product Lead)

## โครงการ
- E-book สอนติดตั้ง + เริ่มใช้ Rakazo สำหรับมือใหม่ จำนวน 7 บท (แผนอยู่ใน Note การ์ด Idea "ทำ e-book เรื่องการติดตั้ง Rakazo", Status=Promoted โดย Phon)
- AW เขียนทีละบท → PL ตรวจ battery + เทียบ docs → file ฐาน Content Drafts **คง Status=draft** → Phon ตัดสิน publish เอง
- ข้อเท็จจริงทุกจุดต้องอ้าง docs จริง rakazo.com เท่านั้น — ห้ามมั่วชื่อปุ่ม/เมนู/แท็บที่ไม่ปรากฏใน docs ที่ให้
- draft tutorial ตัวเก่าถูก Phon ดรอปแล้ว — เขียนใหม่จาก docs โดยตรง อย่าอ้างอิงมัน

## ⚠️ อัปเดตบังคับ 18 พ.ย. 2026 01:15 (Phon สั่ง "ของานจริง ตามการใช้จริงของพรผ่าน Rakazo")
1. **อ่านก่อนเขียนทุกบท (บังคับ):** `/mnt/hermes-agent/rakazo/kit/phon-identity.md` — ครบ 6 ขั้นตามลำดับที่ไฟล์กำหนด ก่อนลงมือเขียนทุกครั้ง
2. **วัตถุดิบเคสจริง:** `shared/ebook-rakazo-install/real-usage-material.md` — ส่วนเล่าใช้ได้เฉพาะข้อเท็จจริงในไฟล์นี้ + docs จริง ห้ามแต่งเคส/ฉาก/บทสนทนา จุดที่ไม่มีวัตถุดิบให้เว้น `[รอพรเติม: ...]`
3. **กฎเสียงในเล่ม (ตามสเปก DuckOS v0.3):**
   - ส่วนเล่า/วิเคราะห์ = เสียงพร (ผู้เล่า "พร", เรื่องจริงเท่านั้น, **ห้าม "คุณ"**)
   - ส่วนคำสั่งใช้งาน/แบบฝึก = ใช้ "คุณ" ได้ตามไฟล์ต้นแบบ (ยกเว้นกฎ คุณ=0 ของโพสต์ FB เฉพาะในเล่ม)
   - Firewall คำห้ามครบทั้งบท, ห้าม "คับ" ทุกที่ (0 ตัวอักษร)
   - ชื่อปุ่ม/เมนูในคำสั่ง ใช้ภาษาอังกฤษตาม docs + คำอธิบายไทย

## บทที่ 1: รู้จัก Rakazo — บอท AI ที่มีคอมพิวเตอร์ของตัวเอง
ผู้อ่าน: มือใหม่ที่ยังไม่เคยใช้ Rakazo ต้องเข้าใจว่ามันคืออะไร และมี 3 เส้นทางเริ่มต้นให้เลือก ก่อนเปิดบทติดตั้งในบท 3
ขอบเขต: นิยาม + จุดต่างจาก chat AI ทั่วไป + 3 ช่องทางใช้งาน (web/desktop/mobile) + ภาพรวมเส้นทาง (ใช้เว็บเลย / ลง desktop app / self-host แบบสั้นมาก) + อะไรรออยู่ในบทถัดไป

## ข้อเท็จจริงล็อกไว้ (ตรวจย้อนได้จาก docs — ห้ามเกินกรอบนี้)
จาก https://rakazo.com/docs.md :
- Rakazo = persistent AI bots แต่ละตัวมี conversations, memory, routines, computer ของตัวเอง ใช้งานได้บน web, desktop, mobile apps
- เริ่มต้น: sign in ที่ app.rakazo.com หรือ self-host ตาม self-hosting guide (ลิงก์ /docs/self-host/)
- "Tell the bot its job in plain words. It asks for anything else it needs."
- เชื่อมแอปได้: Gmail, Slack, Notion, GitHub และ 1,400+ apps — ให้บอทขอเชื่อมแล้วเรา approve sign-in (ลิงก์ /docs/integrations/)
- Routines: ขอได้เป็นประโยค เช่น "every weekday at 8am, summarize my inbox" — บอทรันเองแล้วรายงานกลับแชทเดิม (ลิงก์ /docs/routines/)
- Approvals: เลือกได้ว่าบอทต้องถามก่อนลงมือ (ลิงก์ /docs/approvals/)
- Import an agent ได้จาก OpenClaw, Hermes ฯลฯ (ลิงก์ /docs/import-an-agent/)
จาก https://rakazo.com/docs/desktop-app.md :
- Desktop app มีทั้ง Mac, Windows, Linux — รัน Rakazo เดียวกับเว็บ และรันทุกอย่างบนเครื่องเราเองได้
ข้อจำกัดบทนี้: self-host พูดถึงแค่ว่ามี guide และต้องใช้ Docker พอ ห้ามลงรายละเอียดเทคนิคลึก (ไว้ไม่อยู่ในเล่มนี้ 7 บท)

## ฟอร์ม/กระบวนการ (ตาม kit adduck-writer)
1. อ่านก่อนเขียน: /mnt/hermes-agent/rakazo/kit/phon-identity.md (ครบ 6 ขั้น) → rakazo/kit/adduck-SOUL.md → duck-os/Content_Thinking_Playbook.md → skills/content-pipeline/SKILL.md
2. ยึดฟอร์ม/lens ตาม FORM SELECTOR; เป้าความยาวบท ~900–1,300 คำ; ไม่ใส่ H1 ซ้ำชื่อหน้า
3. Self-check battery ทีละกฎ + sibling guard จริง ห้ามประกาศ PASS โดยไม่ไล่เช็ค
4. Verify ข้อเท็จจริงกับ docs จริงทุกข้อ — ตัวเลข/คำกล่าวอ้างถือเป็นคำของผู้ผลิต

## ส่งงาน — สร้างหน้าใหม่ในฐาน Content Drafts (database id 3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520)
- Name = "E-book Rakazo บท 1: รู้จัก Rakazo — บอท AI ที่มีคอมพิวเตอร์ของตัวเอง"
- Topic = "ติดตั้ง Rakazo — บทที่ 1 นิยามและ 3 เส้นทางเริ่มต้น"
- Status = draft (ค่าเดียวที่อนุญาต ห้ามแก้เป็นอย่างอื่น)
- Date = 2026-11-18, Platform = general
- Source = https://rakazo.com/docs.md + https://rakazo.com/docs/desktop-app.md
- body = เนื้อบทเต็มตามฟอร์ม
- ห้ามแตะ: ฐาน Adduckivity Content, การ์ด Idea, Books Library, หน้า draft อื่นที่มีอยู่แล้ว, publish ทุกช่องทาง

## รายงานกลับ (ในกลุ่ม Product Production)
slug, props ที่ใช้, ผล battery ทีละกฎ, sibling guard, ลิงก์หน้า Notion, แหล่งอ้างอิงที่ verify แล้ว — PL จะรัน battery ตรวจซ้ำก่อนไปบทที่ 2
