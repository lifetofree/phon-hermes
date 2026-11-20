# บรีฟ AW: บท 1 v2 — E-book "การติดตั้ง Rakazo" (mockup v0.1 APPROVED)

ออกโดย Product Lead · 18 พ.ย. 2026 01:3x ICT · Phon APPROVE โครง 01:24 ผ่าน Chief
สถานะเดิม: บท 1 ร่างเก่าถูกลบจาก Content Drafts 01:19 → เขียนใหม่บนโครงเล่มที่ล็อกแล้ว ห้ามใช้ร่างเก่า

## ลำดับงาน (สำคัญ)
1. จบบท 2 ที่คำสั่ง Phon ให้เขียนค้างไว้ให้เสร็จ + file ก่อน (โครงบท 2 ตรง mockup หน้า 6 อยู่แล้ว ไม่ต้องแก้)
2. แล้วหยิบบรีฟนี้ทำบท 1 v2 ทันที

## บังคับอ่านก่อนเขียน (ตามลำดับ)
1. /mnt/hermes-agent/rakazo/kit/phon-identity.md — ครบ 6 ขั้น (อ่านผ่าน shell, read-only mount)
2. kit adduck-writer รอบใหม่ (Playbook/SOUL/style guide/SKILL ทั้งหมด)
3. สเปกเล่ม: shared/ebook-format-reference-duckos-v03.md
4. โครงบท 1 ที่ล็อก: shared/ebook-rakazo-install/mockup-duckos-v01.html ส่วน "หน้า 4 : บท 1" (โครงถูกคัดลอกมาให้ด้านล่างแล้ว)

## โครงบท 1 ที่ล็อก (เติม copy จริง ห้ามเปลี่ยนโครง/หัวข้อ/ลำดับ)
- หัวบท: 01 · "รู้จัก Rakazo — และ 3 เส้นทางเริ่มต้น" (Chapter One)
- กล่องเสียงพร (phvoice): แท็ก "เปิดบทด้วยเรื่องจริงของพร" → **คง marker [เคสจริงรอพรเติม — ห้ามแต่ง] ไว้ตามเดิม** (Phon เติมเอง) เขียงนำสั้น 1–2 ประโยคเสียงพรได้ แต่ห้ามแต่งเคสแทน
- ส่วน body: ย่อหัวใจ "Rakazo คืออะไร" — บอทที่สั่งงานผ่านแชท + เครื่องมือ/แอปที่เชื่อมได้ + คอมพิวเตอร์ที่บอทใช้งานได้เอง (เสียง "เรา")
- กล่องคำสั่ง (cmd): เลือกเส้นทาง 3 ทาง — (1) เริ่มเบาสุด ใช้บนเว็บ ไม่ต้องติดตั้ง (2) ใช้ประจำ ติดตั้ง desktop app เลือก server ที่ใช่ (3) ใช้ร่วมทีม ต่อ Existing Instance ที่ทีมตั้งไว้ (ส่วนนี้ใช้ "คุณ" ได้)
- ตารางเทียบสั้น 3 แถว: Cloud / เครื่องเรา (This computer) / self-host (Existing instance) ต่างกันตรงไหน
- บรรทัดแหล่งอ้างอิง: "rakazo.com/docs.md (ดึง 18 พ.ย. 2026)" — ใส่วันที่ดึงจริงของวันนี้
- งบหน้า: บท 1 = หน้า 4–5 ของเล่ม (2 หน้า A4)

## ล็อกข้อเท็จจริง (ตรวจสดกับ docs จริงก่อนเขียน ห้ามแต่ง — ยืนยันแล้วจาก QC รอบ 17 พ.ย. 15:50)
- persistent bots: บอทแต่ละตัวมี conversations / memory / routines / computer ของตัวเอง
- เชื่อมแอปได้ 1,400+ · routines รายงานกลับแชทเดิม · ระบบ Approvals ถามก่อนทำงานอ่อนไหว
- desktop app (Mac/Win/Linux) คือ "the same Rakazo as the web" + โหมด Docker
- แหล่ง: https://rakazo.com/docs.md (+ docs/desktop-app.md ถ้าจำเป็น) — เปิดอ่านสดวันนี้และใส่วันที่ดึงจริง

## เสียง + Firewall (เงื่อนไข PASS)
- ส่วนเล่า/วิเคราะห์ = เรา · คำสั่งใช้งาน = "คุณ" ได้เฉพาะในกล่อง cmd · ผม 0 · พร 0 (ระวังคำ "เพราะ" โดน scan) · คับ 0
- Firewall คำห้ามตาม kit/battery ครบ · ตัวเลขต้องจริงจาก docs + มีวันที่ดึง · ห้ามสัญญาฮือฮา/ขยี้ปม/ชื่อโรคตรง ๆ
- บทนี้ไม่มี benchmark จึงไม่ต้องมี disclaimer เทียบเครื่อง

## กระบวนการส่งมอบ
1. เขียน markdown (โครงตามหัวข้อด้านบน) · body ~430–500 tokens ให้ลง 2 หน้า A4
2. รัน draft_battery ผ่าน (uv run --python 3.12 ตาม kit) + sibling guard
3. file ฐาน Content Drafts (db 3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520): Name บอกบทชัด, Platform=general, Source=rakazo.com/docs.md, Date=2026-11-18, **Status=draft เท่านั้น ห้าม publish เด็ดขาด**
4. แจ้งในกลุ่ม Product Production พร้อม draft page id — PL จะ QC (battery เอง + เทียบ docs + identity) แล้วเป็นคน sync ลง HTML เล่ม + Body หน้า PRD-1 เอง (AW ไม่ต้องทำ)
