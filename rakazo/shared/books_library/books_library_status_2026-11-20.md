# Books Library — สถานะจริง + แผนที่รออนุมัติ (20 พ.ย. 2026)

จัดทำโดย Book Keeper · ตรวจจาก Notion REST API สด (ไม่ใช่จากหน้าจอ) · สคริปต์ตรวจซ้ำได้ที่ `shared/books_library/bk_audit_live.py`, `bk_audit_ch2.py`, `bk_body_check.py`

## 1) ตัวเลขจริง ณ 20 พ.ย. 2026 (ยืนยันจาก API แล้ว — รอบตรวจสุดท้ายหลังทุกการแก้)

| หัวข้อ | ผล |
|---|---|
| หนังสือในฐาน | **251 แถว** · ไม่มีแถวที่ค่า Author / Energy Group / Status ว่าง |
| Tags | `multi_select` · **76 option** · tag ที่ใช้จริง **76** · tag slots **532** · แถว tag ว่าง **0** |
| Energy Group | 🟢 G.1 **10** · 🟡 G.2 **74** · 🟠 G.3 **136** · 🔴 Boss **31** |
| Status ระดับหนังสือ | ⬜ QUEUED **210** · ⏳ LOADING... **41** · ✅ INSTALLED **0** |
| Chapter List (child DB) | **251 ชิ้น ชื่อเดียวกันหมด `Chapter List`** (เคยมีชื่อเพี้ยน/ชื่อว่าง/DB ทดลอง รวม 253 → แก้ครบ) |
| Chapter rows | **620 แถว** ใน **41 เล่ม** · ⬜ QUEUED **565** · ⏳ LOADING... **20** · ✅ INSTALLED **22** · ว่าง **13** (แถวหัวข้อ PART/Section = ไม่ใช่บท ตาม convention เดิมเว้นว่างไว้) |
| โครงสร้าง body | **251/251** = ปกเป็นบล็อกแรก + Chapter List ที่ index 1 + page cover ตั้งครบ 251/251 (ตรวจแบบ paginate + retry) |
| หนังสือที่อ่านครบทุกบท | **0 เล่ม** |

## 2) รอบที่ 1 — บุ๊คแก้เองเสร็จ (`bk_round1.py --apply` ผ่านทุกขั้น)

1. **rename คอลัมน์ให้ชื่อเดียวกัน** — `Core Message (สรุปแก่นฉบับ PHON)` / `(ฉบับ PHON/Duck OS)` → `Core Message (ฉบับ PHON)` (7 DB) · `Chapter Title` → `Chapter Title (Original)` (1 DB) · `Name` → `#` (8 DB ที่คอลัมน์ title เก็บเลขบทจริง)
2. **เพิ่มคอลัมน์ที่ขาดใน 12 child DB** — `Status` (select 3 ตัว) + `Core Message (ฉบับ PHON)` + `Chapter Title (Original)` แล้วเขียน `Status = ⬜ QUEUED` **232 แถว**
3. **เติม Status ที่ว่างของบทจริง 10 แถว** → `⬜ QUEUED` (Brain Hacks 1, Meditations 1, Dopamine Nation 4, Almanack(TH) 1, The Obstacle is the Way 3)
4. **rename child DB** `New database` → `Chapter List` (Brain Hacks — มี 7 บทที่ sync script เดิมมองไม่เห็น)
5. **archive ของที่เป็นสิ่งซ้ำ/ทดลอง** (archive = ย้อนกลับได้ ไม่ลบถาวร) — `ZZ test db` (HBR Guide to Generative AI, 0 แถว) · Chapter List ซ้ำของ Essentialism (ตรวจแล้วเนื้อหาเหมือนกัน 100% ทั้ง 24 แถว) · ภาพปกซ้ำบล็อกที่ 2 ของ Essentialism
6. **normalize child DB ว่าง** อีก 1 ชิ้น ($100M Offers Money Models) ให้มีคอลัมน์ครบ
7. หลัง Chief สร้าง Chapter List ใหม่ให้ Essentialism (คอลัมน์ชื่อเก่า) → rename กลับเป็น `Core Message (ฉบับ PHON)` + ตรวจว่า 24 แถวยังมี Status ครบ (5 INSTALLED / 10 QUEUED / 5 LOADING / 4 PART)

**ผลสุดท้าย:** schema child DB ตรงมาตรฐาน **247/251** · เหลือ 4 เล่มที่คอลัมน์ title มีบทบาทต่าง (ดูข้อ 4 ของรายการรออนุมัติ)

## 3) ปัญหาที่เจอ + หลักฐาน (สำหรับคนอ่านโค้ดต่อ)

- **`final_verify.py` (ของ Chief) รายงานผิด** — ไม่มี retry ตอนเจอ 429 → เดิมอ่านว่า "79 เล่มไม่ครบ" แต่ตรวจซ้ำแบบ paginate + retry ได้ 251/251 ครบจริง
- **child_database block id ≠ data_source id** — query ด้วย id ของ data source จะ 404 ต้อง GET `/databases/{id}` เพื่อเอา `data_sources[0].id` ก่อน
- **Notion API แทรกบล็อกได้แค่ "ท้ายหน้า"** — `after` ใช้ได้กับ PATCH `/blocks/{id}/children` แต่ **POST `/databases` ไม่รับ `after`** (ทดสอบแล้ว) → ถ้าจะได้ลำดับ [ปก, Chapter List, เนื้อหา] ต้อง archive หน้าแล้วสร้างใหม่ทั้งหน้า (เสี่ยง) หรือ **ลากใน UI**
- **sync script จะทำ tag หาย** — `prop()` ใน `sync_books_library.py` ไม่รู้จัก `multi_select` → รอบ sync หน้าถัดไป `research/books/catalog.md` จะไม่มี tag เลย (แพตช์เสนออยู่ที่ `proposed_sync_prop_patch.md`)
- **หมวดพลังงานของชั้นบน** — Energy Group มีแค่ 4 ตัวเลือก (กรองตามแบตได้อย่างเดียว) ถ้าจะกรองตาม "ต้องโหวตเพราะไม่มีเวลา" ต้องเพิ่ม property ใหม่
- **13 แถวที่ Status ว่าง = หัวข้อ PART/Section** ไม่ใช่บทความที่ตกหล่น (Ego 3, Clear Thinking 5, Essentialism 4, Deep Work 2 รวมชื่อแปลง) → ตั้งใจเว้นว่างตาม convention เดิม ไม่ใช่หนี้งาน

## 4) เรื่องที่เจ้าของต้องรู้ — สคริปต์ของ Chief ยังแก้ฐานอยู่ระหว่างที่บุ๊คตรวจ

ระหว่างที่บุ๊คตรวจรอบสุดท้าย (20 พ.ย. ~11:00–11:40) เจอโปรเซสของ Chief ที่ยังแก้ฐานอยู่:

| โปรเซส | เริ่ม | ผลกับฐาน |
|---|---|---|
| `fix_essentialism.py` | 10:52 | archive เนื้อหา Essentialism ทั้งหน้าแล้ว rebuild กลับจาก snapshot → เนื้อหาเป็น **บล็อกแบน** (nested ถูก flatten, annotations หาย) + Chapter List ซ้ำ + ปกไม่อยู่บล็อกแรก (สคริปต์สร้าง DB ก่อนค่อย archive) |
| `fix_last1.py` | 06:07 | แก้ Steal Like an Artist (ตอนนี้ปก+Chapter List อยู่บนสุดแล้ว 63 บล็อก) แต่โปรเซสยังค้างสลีป ~5 ชั่วโมง — **แนะนำให้หยุด** |
| `fix_ess2.py` | 11:07 | แก้ Essentialism รอบสองด้วยวิธีถูก (archive ทั้งหน้า → ใส่ปก index 0 → สร้าง Chapter List index 1 + คัดลอก 24 แถว → คืนเนื้อหา 350 บล็อก) → **ตอนนี้ Essentialism ได้โครงสร้างถูกต้องแล้ว** แต่ **บล็อกที่ API สร้างไม่ได้หายไป 1 บล็อก** (กู้ได้จาก Trash ของ Notion) |

**ข้อสังเกตสำคัญ:** วิธี "archive ทุกบล็อกแล้วสร้างใหม่" ทำให้ nesting/annotations หาย และบล็อกบางชนิด API สร้างคืนไม่ได้ → ควรหยุดใช้วิธีนี้กับหน้าเนื้อหาของเจ้าของ (หน้าที่มีแต่ [ปก + Chapter List] ไม่ต้องแตะอยู่แล้ว)

## 5) รอเจ้าของอนุมัติ (3 ข้อ — บุ๊คไม่ลงมือเอง)

| # | เรื่อง | ขนาด | หมายเหตุ |
|---|---|---|---|
| B | ทำ schema child DB ให้เหมือนกัน 41 เล่ม — 4 เล่มที่คอลัมน์ title เก็บ **ชื่อบท** (Atomic Habits, Thinking Fast and Slow, Four Thousand Weeks, The Obstacle is the Way) | 112 แถว | ต้องคัดลอกชื่อบทไป `Chapter Title (Original)` แล้วใส่เลข/label บทในคอลัมน์ title + rename title เป็น `#` — ทำให้ทุกเล่มกรอง/อ้างอิงแบบเดียวกัน |
| C | เพิ่ม property ชั้นบน 14 ตัว ตามดีไซน์ v3 | schema ของฐานหลัก | รายละเอียดอยู่ที่ `books-library-schema-design-v1.md` (เจ้าของตัด Language/Published/Started At/OPB ออกแล้ว) |
| D | patch `sync_books_library.py` ใน repo + รัน sync คืน tag | 1 ไฟล์ | push ไป `phon-hermes` ยังติด 403 → แก้ได้แค่ในเครื่องนี้ก่อน · ต้องแก้ `prop()` ให้รู้จัก `multi_select` ไม่งั้น catalog.md รอบหน้าจะไม่มี tag |

## 6) ข้อเสนอเพิ่ม (เล็ก)

- **ยกเลิก convention "Status ว่าง = PART divider"** หรือทำให้ชัด (เช่นใส่ค่า `—` แทนว่าง) เพื่อไม่ให้สับสนกับข้อมูลตกหล่นเวลา filter
- **หยุดโปรเซส `fix_last1.py`** ของ Chief (ค้างมา ~5 ชม. ไม่ได้ทำอะไร)
- **กู้บล็อกที่หาย 1 บล็อกของ Essentialism** จาก Trash ของ Notion (ถ้าจำเป็น)
