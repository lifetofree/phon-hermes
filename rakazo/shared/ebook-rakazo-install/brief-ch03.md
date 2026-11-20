# บรีฟ AW: บท 3 — ติดตั้งบนเครื่อง — Desktop app และ This Computer (หน้าเล่ม 8)

ออกโดย Product Lead · แก้ตามมุม v3/v6 เมื่อ 18 พ.ย. 2026 ~15:30 ICT · **คิว: ส่งให้ AW ทันทีที่ ch1 v2 + ch2 v2 ปิด QC** (ch2 v2 QC ผ่านแล้ว 15:0x) · ห้าม publish · ห้ามแตะไฟล์ HTML ทุกไฟล์ (HTML จะเขียนหลังครบ 14 หน้า + Phon approve Body)

## บังคับอ่านก่อนเขียน (ตามลำดับ)
1. /mnt/hermes-agent/rakazo/kit/phon-identity.md — ครบ 6 ขั้น (อ่านซ้ำทุกงาน)
2. kit adduck-writer (Playbook/SOUL/SKILL)
3. addendum-v6-aw.txt ใน shared/ebook-rakazo-install/ — มุมเล่ม Docker-first + แหล่งอ้างเหลือ 2 อย่าง (docs จริง + real-usage-material.md) — **ห้ามอ้าง DuckOS Field Guide v0.3 ทุกรูปแบบ**
4. โครงหน้า 8 (SHEET 7) ใน shared/ebook-rakazo-install/mockup-sheets-full.txt — โครงล็อก ห้ามเปลี่ยนลำดับหัวข้อ
5. วัตถุดิบเคสจริง shared/ebook-rakazo-install/real-usage-material.md

## มุมบทนี้ (v3 — ต่างจากโครง mockup เดิม)
- จุดที่คนติดตั้งสะดุดบ่อย = หน้าเลือก server ครั้งแรก → บทนี้วางแผนให้ตัดสินใจก่อนถึงหน้านั้น
- **ตอนเลือก server ครั้งแรก: เรียง This computer ไว้ก่อน Rakazo Cloud** พร้อมเหตุผล (ฟรี — ไม่ต้องเสียเงินผ่านเว็บ, บอทอยู่บนเครื่องเรา, คอมพิวเตอร์ของบอทเป็นของเราคนเดียวหลังสร้างบัญชี) · Rakazo Cloud = ทางเลือกสำหรับคนที่ไม่อยากลง Docker ในเครื่อง (ห้าม hard-sell) · Existing instance = กรณีทีม (ยกไปบท 5)
- ส่วนเล่า = เสียงพร: ทำไมถึงย้ายจากเว็บลงเครื่อง — บอทมีคอมพิวเตอร์ทำงานบนเครื่องตัวเอง ไฟล์งานอยู่กับเรา; เคสจริงที่ใช้ได้: ทีมบอท 7 ตัวของพร แต่ละตัวมีคอมพิวเตอร์ประจำตัว แชร์ Team Computer ส่งไฟล์กันผ่าน shared/ (วัตถุดิบ §1) — จุดที่เป็นฉากส่วนตัวคง marker `[เคสจริงรอพรเติม — ห้ามแต่ง]`

## ข้อเท็จจริงล็อกไว้ (docs จริง rakazo.com/docs/desktop-app.md ตรวจสด 18 พ.ย. 2026 — ห้ามใช้ความจำ ห้ามเพิ่มนอกนี้)
- โหลดจาก rakazo.com · Linux AppImage ต้องมี FUSE 2
- เปิดครั้งแรกเลือกเซิร์ฟเวอร์ (เรียงตามมุมเล่ม): **This computer** (รัน Rakazo ของตัวเองใน Docker ในเครื่อง — ถ้าไม่มี Docker แอปชี้ดาวน์โหลด Docker Desktop (Docker Engine บน Linux) ให้แล้วไปต่อเอง; ถ้า Docker ติดตั้งแล้วแต่หยุด แอปเปิดให้; ทุกอย่างรวมคอมพิวเตอร์ของบอทรันบนเครื่องคุณ เป็นของคุณคนเดียวหลังสร้างบัญชี) → **Rakazo Cloud** (sign in บัญชี rakazo.com — ทางเลือกเสริม) → **Existing instance** (กรอก Server address + กด Check connection)
- เปลี่ยนภายหลัง: เมนูแอป **Change Rakazo Server…** (Cmd+Shift+K / Ctrl+Shift+K)
- เซิร์ฟเวอร์ local ยังรันต่อหลังปิดแอป (routine ยังทำงาน) — ปิดจริงใช้เมนู **Quit and Stop Bots**
- ให้บอทใช้เครื่อง: ทาง This computer แอปถาม **Where should bots run?** → Docker (บอทอยู่คอมพิวเตอร์แยกของตัวเอง) หรือ **Use this computer** (ทำงานบนเครื่องคุณตรง ๆ); เปลี่ยนทีหลังด้วยเมนู **Computer Access…** / ปิดด้วย **Revoke Local Computer Access**
- ทาง HTTPS/loopback server: เปิด **Let bots use this computer** ใน **Settings → General** หัวข้อ Computers — สถานะโชว์ **Connected/Offline** · แอปถาม **Allow bots to use this computer?** ก่อนให้สิทธิ์ทุกกรณี
- คำเตือน docs: โหมด Use this computer บอทรันคำสั่งได้โดยไม่ถาม — อย่าเลือกบนเซิร์ฟเวอร์ที่คนอื่นใช้
- อัปเดตแอปตรวจเอง โหลดพื้นหลัง ปุ่ม **Install update** โผล่ท้าย sidebar

## เงื่อนไข QC ของ PL (PASS นอกเหนือจาก draft_battery)
คับ=0 ทั้งชิ้น · ไม่แต่ง evidence · firewall คำห้าม · ตัวเลขจริง+วันตรวจ (อ้าง "docs desktop-app ดึง 18 พ.ย. 2026") · โครงหัวข้อ+ปุ่ม Print ตาม mockup หน้า 8 (SHEET 7) · ตัวเลขทีมบอท = 7 ตัว 2 ห้องแชท ตามวัตถุดิบ §1 เท่านั้น · คุณ ปรากฏเฉพาะกล่องคำสั่งตามสเปกเล่ม

## ส่งมอบ
1. battery: uv run --python 3.12 ตาม kit — PASS
2. file ฐาน Content Drafts (POST databases/3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520): Name="บท 3 ติดตั้งบนเครื่อง — Desktop app และ This Computer (E-book Rakazo)", Platform=general, Source=rakazo.com/docs/desktop-app.md, Date=2026-11-18, Status=draft เท่านั้น
3. วางไฟล์ ebook-rakazo-install-ch03-v1.md ในโฟลเดอร์ drafts/ ของตัวเอง (ถ้าเทิร์นถูกตัด ให้เซฟไฟล์ระหว่างทางทุกครั้ง ไม่ต้องรอจบ)
4. รายงาน draft page id ในกลุ่ม Product Production — PL sync Body หน้า PRD-1 + HTML เอง (AW ไม่ต้องทำ)
