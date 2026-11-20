# บรีฟจาก Chief → Adduck Writer: draft ใหม่ มุม adduckivity — Rakazo เป็นเคสตัวอย่าง

**ภารกิจ:** สร้าง draft **ใหม่** (ไม่มีหน้าเดิม) ลงฐาน Content Drafts — Phon สั่งเมื่อ 17 พ.ย. 2026
มุมที่ผู้ใช้เลือก: **บทความสไตล์ adduckivity (system/mindset)** — Rakazo เป็น "เคสตัวอย่าง" ไม่ใช่บทความ tutorial

## ไอเดียร์ระบบ (แนว — ปรับถ้อยคำได้ ให้เหลือ dispatch question เดียว)

**คำถาม dispatch:** มอบงานให้ AI ทำเองได้จริง ต้องวางอะไรก่อน — สองโหมดพัง: **คุมแน่นเกิน** (ต้องกดอนุมัติทุกขั้น = ก็ยังทำเองอยู่) vs **ปล่อยหลวมเกิน** (ไม่วางสิทธิ์/กติกา = รอวันพัง)
**แก่น:** การมอบงานให้ทำเองได้ ต้องมี 3 อย่าง: (1) บอกงานด้วยภาษาธรรมดาให้ชัด (2) ให้สิทธิ์เท่าที่จำเป็น + กำหนดจุดที่ต้องขออนุมัติ (3) กติกาเวลา — ทำเองตามรอบและรายงานกลับเอง
Rakazo ใช้เป็น worked example ของ 3 ข้อนี้ได้พอดี (ดูข้อเท็จจริงล็อกด้านล่าง)

## ข้อเท็จจริงล็อก — ใช้ได้เฉพาะที่อยู่ในลิสต์นี้ ห้ามมั่วปุ่ม/เมนู/ขั้นตอนนอกลิสต์

แหล่ง: https://rakazo.com/docs.md และ https://rakazo.com/docs/desktop-app.md (ดึงจริง 17 พ.ย. 2026)
1. Rakazo ให้ AI bot ถาวร — แต่ละตัวมีบทสนทนา ความจำ routine และคอมพิวเตอร์ของตัวเอง
2. เริ่ม: sign in ที่ app.rakazo.com (หรือ self-host) แล้วบอกบอทว่างานมันคืออะไรด้วยคำพูดธรรมดา — มันจะขอสิ่งที่ขาดเอง
3. ต่อ app ที่ใช้อยู่: Gmail, Slack, Notion, GitHub ฯลฯ (1,400+) — สั่งบอทต่อ แล้วอนุมัติ sign-in ที่มันส่งมา
4. Routine: สั่งเป็นประโยค เช่น "ทุกวันธรรมดา 8 โมง สรุป inbox ให้หน่อย" — บอทรันบนคอมของตัวเองแล้วรายงานกลับในแชทเดิม
5. Approvals: เลือกได้ว่าบอทต้องขอก่อนลงมือหรือไม่
6. Desktop app (Mac/Windows/Linux): โหลดจาก rakazo.com (Linux AppImage ต้องมี FUSE 2) — เปิดครั้งแรกให้เลือก server: Rakazo Cloud / รันบนเครื่องตัวเองผ่าน Docker / ต่อ existing instance
7. เปิดให้บอทใช้คอมพิวเตอร์จริงได้ ("Let bots use this computer" ใน Settings → General) — app จะถาม "Allow bots to use this computer?" ก่อนเปิดสิทธิ์ทุกครั้ง
8. คำเตือนใน docs: โหมดใช้เครื่องตรง ๆ บอทรันคำสั่งได้โดยไม่ถาม — อย่าเลือกบนเครื่องที่คนอื่นใช้ด้วย

## กติกาบังคับ

1. โหลด skill `/adduck-writer` ก่อนลงมือ — **CURRENT FORM** (โจทย์นี้เป็น system/mindset ตาม FORM SELECTOR)
2. ต้อง **PASS draft_battery.py** — รันด้วย `uv run --python 3.12` (ความยาว, H1×1, H3×1, quote ×2, พร/เรา เท่านั้น ห้าม "คุณ" ห้าม "คับ", scans CLEAN)
3. **Story seed ห้ามตัด** — ฉาก "พร" ต้องเป็น seed ที่รอเจ้าของยืนยันก่อน publish (flag ไว้ใน header)
4. อ้างเว็บเมื่อจำเป็นเท่านั้น — ถ้าใส่ลิงก์ docs ให้เป็น citation ธรรมชาติไม่ใช่รายการลิงก์
5. **คง Status=draft ห้าม publish เด็ดขาด**

## File ลง Notion

- สร้างหน้าใหม่ในฐาน Content Drafts: data source `collection://3ccdf8d8-8d8c-8163-bbd4-000b3cf26f81`
- Properties: **Name** = ชื่อโพสต์ (title property จริงคือ Name — เช็คกับหน้าพี่น้องได้) · **Topic** = label ภายใน · **Status** = draft · **Source** = https://rakazo.com/docs.md · **Date** = 2026-11-17
- Header บนหน้า: form + ข้อเท็จจริงที่ใช้ + ผล battery + seed flag (ตาม convention เดิม)
- Quote หนาใช้ `<quote><b>` tag form ให้ bold รอดตั้งแต่สร้าง

## เมื่อเสร็จ

- รายงาน Phon ในแชทของคุณ: ลิงก์หน้า + สรุปมุมที่เลือก + ผล battery
- โพสต์ผลในกลุ่ม **Content Drafting** แจ้ง Chief — **Chief จะ re-verify (รัน battery บนหน้าจริง + เช็ค checklist) ก่อนปิดงาน**

---
## เพิ่ม 17 พ.ย. 2026 12:31 — กฎอ่านก่อนเขียน (owner สั่ง — ใช้กับทุกงานเขียน รวมงานนี้)
ก่อนเขียนต้องอ่าน /mnt/hermes-agent/rakazo/kit/phon-identity.md ให้ครบตามลำดับ 6 ขั้นที่ไฟล์กำหนด: SOUL → Playbook → SKILL ช่วง 79–182 + 186–201 (ห้ามอ่านทั้งไฟล์) → Style Guide + Corpus + ตัวอย่างจริง ≤3–4 ไฟล์ → คู่ critique จริง 1 คู่ → STATE
mount /mnt/hermes-agent อ่านอย่างเดียว · ไฟล์ live git-backed อ่านซ้ำทุกงาน · งานเครื่องมือ = v2 TECH form (ตาราง+disclaimer, product-identity gate 3 ทาง, ตรวจ claim repo จริงวันเดียวกัน) · ลำดับถ้าขัด: SOUL > Playbook > kit > corpus (สไตล์ corpus ชนะ)
