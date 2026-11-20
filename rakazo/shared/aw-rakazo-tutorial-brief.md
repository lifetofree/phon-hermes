# บรีฟจาก Chief → Adduck Writer: draft ใหม่ (B) — Tutorial มือใหม่ "ติดตั้งและเริ่มใช้ Rakazo"

**ภารกิจ:** สร้าง draft **ใหม่** ลงฐาน Content Drafts — มุมที่ผู้ใช้เลือก: **บทความ tutorial สำหรับมือใหม่** (ต่างจากชิ้น A ที่เป็น adduckivity — ทำคู่กันในรอบนี้ อ่านบรีฟ A ด้วย)

## โทนและโครง

บทความสอนลงมือทำจริง ลำดับตามที่คนใหม่เจอจริง: ติดตั้ง → เลือก server → สร้างบอทแรก → ต่อ app → ให้ทำเองตามรอบ → จุดตัดสินใจเรื่องสิทธิ์ (approvals / computer access)
**ฟอร์แมต:** เป็น **tech post** ไม่ใช่ system/mindset — ให้ใช้สถาปัตยกรรม **v2** ตาม FORM SELECTOR ใน SKILL.md (อ่านสเปก v2 จาก SKILL.md เองก่อนเขียน — ห้ามเดาโครง) · battery ยังต้อง PASS ทุกด่าน

## ข้อเท็จจริงล็อก — ใช้ได้เฉพาะลิสต์นี้ ห้ามมั่วปุ่ม/เมนู/ขั้นตอนนอกลิสต์

แหล่ง: https://rakazo.com/docs.md และ https://rakazo.com/docs/desktop-app.md (ดึงจริง 17 พ.ย. 2026)

**ติดตั้ง:**
1. Desktop app รองรับ Mac, Windows, Linux — โหลดจาก rakazo.com (Linux AppImage ต้องมี FUSE 2)
2. ใช้บนเว็บก็ได้โดยไม่ต้องติดตั้ง: sign in ที่ app.rakazo.com
3. อัปเดตอัตโนมัติ — พร้อมแล้วจะมีปุ่ม Install update ให้กด

**เลือก server (เปิด app ครั้งแรก):**
4. Rakazo Cloud — sign in ด้วยบัญชี rakazo.com
5. This computer — รัน Rakazo ของตัวเองในเครื่องผ่าน Docker (ไม่มี Docker app จะพาไปหน้าโหลดให้เอง)
6. Existing instance — กรอก Server address แล้วกด Check connection
7. เปลี่ยนภายหลังได้: Change Rakazo Server… (Cmd+Shift+K / Ctrl+Shift+K)
8. หมายเหตุ docs: server บนเครื่องยังรันต่อแม้ปิด app — routine ยังทำงาน; จะหยุดให้กด Quit and Stop Bots ในเมนู

**หลังติดตั้ง (จาก docs.md):**
9. สร้างบอทแรก: บอกมันด้วยคำพูดธรรมดาว่างานมันคืออะไร — มันจะขอสิ่งที่ขาดเอง
10. ต่อ app: Gmail, Slack, Notion, GitHub ฯลฯ (1,400+) — สั่งบอทต่อ แล้วอนุมัติ sign-in ที่มันส่งมา
11. Routine: สั่งเป็นประโยค เช่น "ทุกวันธรรมดา 8 โมง สรุป inbox ให้หน่อย" — รันบนคอมของบอทเอง รายงานกลับในแชทเดิม
12. Approvals: เลือกได้ว่าบอทต้องขอก่อนลงมือหรือไม่

**สิทธิ์เข้าถึงคอมพิวเตอร์จริง:**
13. เปิดได้: "Let bots use this computer" ใน Settings → General — app จะถาม "Allow bots to use this computer?" ก่อนเปิดสิทธิ์ทุกครั้ง
14. คำเตือน docs: โหมดใช้เครื่องตรง ๆ บอทรันคำสั่งได้โดยไม่ถาม — **อย่าเลือกบนเครื่องที่คนอื่นใช้ด้วย**

## กติกาบังคับ (เหมือนชิ้น A)

1. โหลด skill `/adduck-writer` ก่อนลงมือ · battery ต้อง PASS (`uv run --python 3.12`) · พร/เรา เท่านั้น ห้าม "คุณ" ห้าม "คับ"
2. **Story seed ห้ามตัด** — ฉาก "พร" เป็น seed รอเจ้าของยืนยันก่อน publish (flag ใน header)
3. **คง Status=draft ห้าม publish เด็ดขาด**
4. ลิงก์ docs ใส่แบบ citation ธรรมชาติ ไม่ใช่รายการลิงก์ท้ายบท

## File ลง Notion

- data source `collection://3ccdf8d8-8d8c-8163-bbd4-000b3cf26f81` (ฐานเดียวกับชิ้น A — **Name ต้องต่างจากชิ้น A ชัดเจน**)
- Properties: Name = ชื่อโพสต์ (title property จริงคือ Name) · Topic = label ภายใน · Status = draft · Source = https://rakazo.com/docs/desktop-app.md · Date = 2026-11-17
- Header บนหน้า: form + ข้อเท็จจริงที่ใช้ + ผล battery + seed flag · quote หนาใช้ `<quote><b>` tag form

## เมื่อเสร็จ (ทั้ง 2 ชิ้น)

- รายงาน Phon ในแชทของคุณ: ลิงก์ 2 หน้า + ผล battery ทั้งคู่
- โพสต์ผลในกลุ่ม **Content Drafting** แจ้ง Chief — **Chief จะ re-verify ทั้ง 2 หน้า (รัน battery บนหน้าจริง + checklist) ก่อนปิดงาน**
