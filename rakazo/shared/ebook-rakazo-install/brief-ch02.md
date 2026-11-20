# บรีฟ AW: บท 2 — เริ่มบนเว็บ — สมัคร สร้างบอทแรก พื้นฐานการแชท (หน้าเล่ม 6)

ออกโดย Product Lead · 18 พ.ย. 2026 11:1x ICT · งานอันดับ 1 ตามคำสั่ง Phon (ผ่าน Chief 10:46) · ห้าม publish · ห้ามแตะไฟล์ HTML ทุกไฟล์ (HTML จะเขียนหลังครบ 14 หน้า + Phon approve Body)

## บังคับอ่านก่อนเขียน (ตามลำดับ)
1. /mnt/hermes-agent/rakazo/kit/phon-identity.md — ครบ 6 ขั้น
2. kit adduck-writer (Playbook/SOUL/SKILL)
3. สเปกเล่ม shared/ebook-format-reference-duckos-v03.md (ความยาว/จังหวะบทช่วยใช้งาน ตามสเปก)
4. โครงหน้า 6 ใน shared/ebook-rakazo-install/mockup-duckos-v01.html (section sheet ที่ 5 ของไฟล์) — โครงล็อก ห้ามเปลี่ยนลำดับหัวข้อ
5. วัตถุดิบเคสจริง shared/ebook-rakazo-install/real-usage-material.md

## ขอบเขต (จากโครงหน้า 6)
- ส่วนเล่า = เสียงพร: ทำไมเส้นทางเว็บเหมาะเป็นจุดเริ่ม — ไม่ต้องติดตั้ง เห็นระบบทำงานก่อนตัดสินใจลงเครื่อง; คง marker [เคสจริงรอพรเติม — ห้ามแต่ง] ไว้ตำแหน่งเคส
- ส่วนคำสั่งใช้งาน = ใช้ "คุณ" ได้ตามสเปก: สมัคร app.rakazo.com → สร้างบอทแรก → พื้นฐานการแชท
- TECH form ต้องมี disclaimer + อ้าง docs จริงทุกข้อเท็จจริง

## แหล่งข้อเท็จจริง (ตรวจสด 18 พ.ย. ห้ามใช้ความจำ)
- https://rakazo.com/docs.md
- bots-and-chats (พาธจริงตามที่ docs ชี้ — อ้างพาธที่ใช้จริงใน draft)

## เงื่อนไข QC ของ PL (PASS นอกเหนือจาก draft_battery)
คับ=0 ทั้งชิ้น · ไม่แต่ง evidence · firewall คำห้าม · ตัวเลขจริง+วันตรวจ · โครงหัวข้อ+ปุ่ม Print ตาม mockup หน้า 6

## ส่งมอบ
1. battery: uv run --python 3.12 ตาม kit — PASS
2. file ฐาน Content Drafts (POST databases/3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520): Name="บท 2 เริ่มบนเว็บ — สมัคร สร้างบอทแรก พื้นฐานการแชท (E-book Rakazo)", Platform=general, Source=rakazo.com/docs.md, Date=2026-11-18, Status=draft เท่านั้น
3. วางไฟล์ ebook-rakazo-install-ch02-v1.md ในโฟลเดอร์ drafts/ ของตัวเอง (ถ้าเทิร์นถูกตัด ให้เซฟไฟล์ระหว่างทางทุกครั้ง ไม่ต้องรอจบ)
4. รายงาน draft page id ในกลุ่ม Product Production — PL sync Body หน้า PRD-1 + HTML เอง (AW ไม่ต้องทำ)
