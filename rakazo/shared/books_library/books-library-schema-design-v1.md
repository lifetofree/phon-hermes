# ดีไซน์ property ชั้นบน — Books Library (v3) · 19 พ.ย. 2026

> **สถานะ: รอเจ้าของอนุมัติก่อนสร้าง property (schema change)**
>
> **การตัดสินใจของเจ้าของ (19 พ.ย. 2026) — ล็อกแล้ว ไม่ต้องถามซ้ำ**
> 1. **ชุดกลาง** (ไม่เอา "ชุดเต็ม" = ตัด `Language` + `Published` ออก) เพราะ **บางเล่มถูกใช้เขียนเป็นหลาย post** → ห้ามผูก 1 หนังสือ : 1 content
> 2. **เพิ่ม `Recommendation` (คำแนะนำ) มาด้วย** → ใช้เป็นแกน/hook บทความได้ทันที
> 3. **ไม่เอาคู่มือ Rakazo มาผูกกับ Books Library** — คู่มืออยู่ฐาน **Products** (แถว "Rakazo local manual") ไม่ใช่ฐาน Books Library → อยู่นอกขอบเขตของงานนี้
> 4. `Format` + `Language` ต้องเป็น **select** (ไม่ใช่ multi_select) เพื่อไม่ให้บุ๊คอ่านคอลัมน์ผิด
> 5. relation ทุกตัว = **many-to-many** (Notion relation เป็น many-to-many โดยธรรมชาติ → ไม่ต้องทำอะไรเพิ่ม)

จัดทำโดย Chief · ตรวจสอบจาก Notion REST API สด (ไม่ใช่จากหน้าจอ)

---

## 0. สถานะปัจจุบันที่ยืนยันแล้ว

**Books Library** (database `2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0` · data source `2ffdf8d8-8d8c-80d6-913d-000b102ca15a`)

| property | ชนิด | หมายเหตุ |
|---|---|---|
| Title | title | |
| Author | rich_text | ยังไม่ normalize (คนละรูปแบบ) |
| Tags | multi_select | 76 options (แก้เมื่อ 19 พ.ย.) |
| Energy Group | select | 🟢 G.1 / 🟡 G.2 / 🟠 G.3 / 🔴 Boss |
| Status | select | ⏳ LOADING... / ⬜ QUEUED / ✅ INSTALLED |

**Chapter List** (child DB ของแต่ละเล่ม — 41 DB แยกกัน)

| property | ชนิด |
|---|---|
| Chapter Title (Original) | title |
| # | rich_text (เลขบท) |
| Core Message (ฉบับ PHON) | rich_text |
| Status | select (3 ตัว เหมือนชั้นบน) |

**ฐานปลายทางที่จะลิงก์เข้ามาได้ (ยืนยัน id จาก API แล้ว)**

| ฐาน | data_source_id | property ที่มีอยู่ตอนนี้ |
|---|---|---|
| Content Drafts | `3ccdf8d8-8d8c-8163-bbd4-000b3cf26f81` | Topic, Status, Date, Platform, **Source (rich_text)**, Name |
| Knowledge Base | `3c9df8d8-8d8c-81ac-ba5e-fa129e493638` | Category, Tags, Summary, Source (url), Status, Title |
| YouTube Library | `418df8d8-8d8c-8039-b58a-de967eaa3da0` | Link, Speaker/Channel, Format, Status, Asset Residue, Category, Title |
| Idea | `41adf8d8-8d8c-8163-86ef-000ba005975c` | Name, Note, Type, Status, **Products (relation)**, Created |
| OPB Summary | `41adf8d8-8d8c-8075-90ee-dc619d82619d` | Name, Summary, Key Lessons, Transcript (files), Status |

> **Convention ที่มีอยู่แล้วในเวิร์กสเปซ:** `Products.Drafts` ชี้ไป Content Drafts แต่ **ฝั่ง Content Drafts ไม่มี property สะท้อนกลับ** → คือ relation ทางเดียว (`single_property`) → Books Library ใช้แบบเดียวกัน เพื่อไม่ไปเพิ่ม property ในฐานของบอทอื่น (Adduck Writer / Research Scout / Research Distiller)

> **สิ่งที่อยู่นอกขอบเขต (เจ้าของตัดออก 19 พ.ย.):** คู่มือ Rakazo อยู่ฐาน **Products** (data source `41bdf8d8-8d8c-81a4-82e5-000bd7dfded6`, แถว "Rakazo local manual" มี Format/Drafts/Chapters/Progress/Cover อยู่แล้ว) → **ไม่เพิ่ม property ของ Books Library เพื่อผูกคู่มือ** และไม่แตะฐาน Products

---

## 1. หลักการออกแบบ

**ชั้นบน (แถวของหนังสือ) เก็บ 3 อย่างเท่านั้น**
1. **ตัวระบุ** — อะไร (ปี, รูปแบบ, ปก, ลิงก์ต้นฉบับ)
2. **สถานะการอ่าน + ใจความ** — อ่านถึงไหน, ได้คะแนนไหม, จบเมื่อไหร่, **จำอะไรได้**, **ควรอ่านทำไม**
3. **ลิงก์ไปทางล่าง** — หนังสือเล่มนี้ก่อให้อะไรออกมา (บทความ / งานวิจัย / คลิป / ไอเดีย) — **many-to-many ทั้งหมด**

**ชั้นล่าง (body + child DB) เก็บรายละเอียดบท** — ไม่ต้องย้ายขึ้นมา

**หลักการลิงก์:** ลิงก์จาก "ต้นทาง" (หนังสือ) ไป "ผลลัพธ์" (บทความ/งานวิจัย) เพราะถามว่า "หนังสือเล่มนี้ให้อะไรเราบ้าง" ได้ตรงกว่า "บทความนี้มาจากไหน"

---

## 2. property ที่เสนอ (14 ตัว = ชุดกลาง 13 + `Recommendation`)

### ชั้นที่ 1 — ตัวระบุ (4)

| property | ชนิด | ตัวอย่าง | ทำไมต้องมี | ใครใส่ |
|---|---|---|---|---|
| `Year` | number | 2019 | กรอง/เรียงตามยุค, ผูกกับแผนอ่านรายปี, เทียบกับศักรชีวิต | สคริปต์ (backfill) |
| `Format` | **select** | 📖 E-book / 🎧 Audio / 📄 PDF / 📚 Print | เล่มเสียงกับเล่มข้อความให้ content ต่างกัน | สคริปต์ + มือ |
| `Source URL` | url | publisher page | ย้อนตรวจต้นฉบับ / ซื้อซ้ำ / ใส่ลิงก์อ้างอิงในบทความ | มือ + สคริปต์ |
| `Cover` | files | รูปปก | ใช้ทำภาพประกอบบทความ | สคริปต์ |

> `Language` — **ตัดออก** (เจ้าของ: ไม่เอาชุดเต็ม) · ถ้าจะเพิ่มทีหลัง: ทำเป็น **select** ไม่ใช่ multi_select

### ชั้นที่ 2 — สถานะการอ่าน + ใจความ (6)

| property | ชนิด | ตัวอย่าง | ทำไมต้องมี | ใครใส่ |
|---|---|---|---|---|
| `Key Takeaway` | rich_text | "1 ประโยค ต้องจำ" | คู่กับ Core Message ระดับบท — "สรุปทั้งเล่ม" 1 บรรทัด ใช้เป็นแกนบทความได้ทันที | มือ/ผู้อ่าน |
| `Recommendation` | rich_text | "อ่านเพื่อแก้ปัญหา X — ใช้ได้กับ Y" | **คำแนะนำของเล่มนี้** (ใครควรอ่าน / อ่านแล้วได้อะไร) → เป็น "แกน" ที่ Adduck Writer ใช้เขียน hook ได้เลย และเป็นเกณฑ์ตัดสินใจอ่านต่อ | มือ/ผู้อ่าน |
| `Progress` | number (%) | 67 | เห็นว่าอ่านถึงไหนโดยไม่ต้องเปิด child DB | สคริปต์ sync เขียนกลับ |
| `Chapter Count` | number | 73 | ขนาดหนังสือ (ใช้คิดเวลาอ่าน) | สคริปต์ sync |
| `Rating` | number 1–5 | 4 | คะแนนส่วนตัว → "เล่มที่คุ้มที่สุด" / ตัดสินใจอ่านต่อ | มือ |
| `Finished At` | date | 2026-11-18 | reading log + สถิติรายปี + เลื่อนเล่มใหม่อัตโนมัติ | มือ |

> `Started At` — **ตัดออก** (ไม่อยู่ในชุดกลาง) · ถ้าอยากได้ reading log ครบ เพิ่มทีหลังได้ทันที

### ชั้นที่ 3 — ลิงก์ไปทางล่าง (4) ← แกนที่เจ้าของขอ

| property | ชนิด | ลิงก์ไป | ตอบคำถามอะไร |
|---|---|---|---|
| `Drafts` | relation | Content Drafts | "หนังสือเล่มนี้ถูกเขียนเป็นบทความอะไรบ้าง" (**1 เล่ม → N content**) |
| `Knowledge` | relation | Knowledge Base | "มีงานวิจัย/notes อะไรที่อ้างหนังสือเล่มนี้" |
| `Clips` | relation | YouTube Library | "คลิปไหนที่ distill มาแล้วเกี่ยวกับเล่มนี้" |
| `Ideas` | relation | Idea | "ไอเดียไหนเกิดจากการอ่านเล่มนี้" |

> **ไม่มี `Published` (Adduckivity Content)** — เจ้าของตัดออก: บางเล่มถูกใช้เป็น **หลาย post** → การผูก 1:1 จะทำให้ตัดหนังสือที่ยังไม่ publish ทิ้ง · ถ้าภายหลังอยากวัดผล ให้ดูจาก `Drafts` → Content Drafts → (ลิงก์ไป publish ภายหลัง) แทน
>
> `OPB` (→ OPB Summary) — อยู่ในชั้นที่ 3 เดิม แต่ **ไม่อยู่ในชุดกลาง** → ยังไม่รวม · เพิ่มทีหลังได้ทันที

> ชื่อ relation ตั้งตาม convention เดิมของ `Products` (`Drafts`, `Idea Card`) → ตั้งชื่อตาม "สิ่งที่ปลายทางคือ"

---

## 3. ผังลิงก์

```
                      ┌──────────────────────────────┐
                      │  Books Library (251 เล่ม)     │
                      │ Year · Format · Cover · URL  │
                      │ Key Takeaway · Recommendation│
                      │ Progress · Rating · Finished │
                      └──────────────┬───────────────┘
                                     │ relation (ทางเดียว, many-to-many)
        ┌──────────────┬─────────────┼──────────────┐
        ▼              ▼             ▼              ▼
  Content Drafts  Knowledge    YouTube Lib        Idea
  (บทความที่เขียน  Base        (คลิป)          (ไอเดีย)
   จากเล่มนี้)    (งานวิจัย)
        │  1 เล่ม → N บทความ (ไม่ผูก 1:1)
        ▼
  (publish ภายหลัง — ยังไม่ผูกในรอบนี้)

  Chapter List (child DB ของแต่ละเล่ม)  ── ชั้นล่าง: รายละเอียดบท
  หน้า body: list / catalog.md (สคริปต์ sync สร้าง)
```

---

## 4. ผลการตัดสินใจ (ปิดแล้ว — ไม่ต้องถามซ้ำ)

| # | ประเด็น | ผล |
|---|---|---|
| ก | relation ทางเดียว หรือ สองทาง? | **ทางเดียว (`single_property`)** — ปลายทางไม่โดนเพิ่ม property → ปลอดภัยกับบอทอื่น (ตาม convention `Products.Drafts`) |
| ข | `Progress` คำนวณยังไง? | **ให้สคริปต์ sync เขียนตัวเลขกลับ** (มันเดินทุก child DB อยู่แล้ว) — ไม่ย้ายข้อมูล ไม่รวม child DB |
| ค | `Year` / `Format` / `Cover` / `Source URL` ได้ข้อมูลจากไหน? | **สคริปต์ backfill ผ่าน Google Books API** (ค้น title+author → year, format, page count, cover, canonical URL) — dry-run + ตารางเทียบก่อนเขียนจริง |
| ง | รอบนี้เพิ่มกี่ตัว? | **14 ตัว** = ชุดกลาง 13 + `Recommendation` · ตัด `Language`, `Published`, `Started At`, `OPB` ออก (เจ้าของ) |
| จ | คู่มือ Rakazo? | **ไม่เกี่ยว** — อยู่ฐาน Products ไม่ใช่ Books Library → นอกขอบเขต ไม่แตะ |

---

## 4.5 ผลกระทบต่อบุ๊ค (Book Keeper) — ตรวจจากโค้ดจริงทุกสคริปต์

**ข้อสรุป: เพิ่ม 14 property แล้วบุ๊คทำงานเดิมได้ปกติ — มี 1 กับดักที่เลี่ยงแล้ว**

| ตรวจอะไร | ผล |
|---|---|
| มีสคริปต์ไหน assert / เทียบ "จำนวน property ต้องเท่าเดิม" | **ไม่มี** (0 จุด) → เพิ่ม property ไม่ทำพัง |
| สคริปต์ที่ PATCH/POST property | ทุกตัวเขียน **ระบุชื่อ** (Title/Author/Energy Group/Status/Tags) → property ใหม่คงว่าง ไม่ชนกัน |
| API version ที่บุ๊คใช้ | ทั้ง 20 สคริปต์ใช้ `2022-06-28` → ไม่เกี่ยวกับการเพิ่ม property |
| ⚠️ 4 สคริปต์อ่าน multi_select "ตัวแรกที่เจอ" ไม่ได้อ่านชื่อ 'Tags' | `bk_semantic_diff.py`, `bk_verify_post_merge.py`, `bk_title_anomaly.py`, `bk_add_book.py` → ถ้าเพิ่ม property ที่เป็น **multi_select** มีโอกาสอ่านคอลัมน์ผิด |

**วิธีเลี่ยง (เลือกแล้ว):** ไม่เพิ่ม multi_select ใหม่ในฐาน → `Format` เป็น **select** → บุ๊คไม่กระทบเลย
(ทางเลือก: อยากได้ multi_select จริง → ต้อง patch 4 สคริปต์ให้อ่าน by name = แตะไฟล์ → ต้องขออนุมัติเจ้าของ)

**สิ่งที่ไม่กระทบบุ๊ค แต่ต้องรู้:**
- relation แบบ `single_property` → ฐานปลายทาง (Content Drafts / Knowledge Base / YouTube Library / Idea) **ไม่โดนเพิ่ม property** → Adduck Writer, Research Scout, Research Distiller ไม่กระทบเลย
- `Progress` / `Chapter Count` ให้ sync script เขียนกลับ → ค่าว่างจนกว่า sync รับ และหนังสือที่บุ๊คสร้างใหม่จะได้ค่าว่าง → **ไม่พัง**
- ถ้าภายหลังอยากให้บุ๊ค "กรอก Key Takeaway / Recommendation / ลิงก์ Drafts" ต้อง → **อัปเดต instruction ของบุ๊ค (เจ้าของอนุมัติ)**

**แผนตรวจหลังสร้าง property (ทำทีละตัว):**
1. สร้าง `Year` (number — ปลอดภัยสุด) → query ยืนยันว่าเป็น number และแถวเดิม 251 ไม่เปลี่ยน
2. รัน dry-run ของบุ๊ค 4 ตัวนั้น + `bk_add_book.py` → **เทียบกับ baseline ก่อนหน้า ต้องเหมือนเดิมทุกตัว**
3. ผ่าน → สร้างตัวถัดไป → ทำจนครบ 14 ตัว

---

## 5. ลำดับลงมือ (ถ้าได้รับอนุมัติ)

1. **A — สร้าง property** (schema change → ต้องอนุมัติเจ้าของ): ทำทีละตัว + verify ทุกตัว ทดสอบ relation 1 ตัวก่อน (`Drafts`) เพื่อยืนยันว่า payload ถูกและฝั่ง Content Drafts ไม่โดนเพิ่ม property
2. **B — patch `sync_books_library.py`**: `prop()` เพิ่ม `multi_select` (แก้ปัญหาที่ค้างอยู่จากรอบ merge) + เขียน `Progress`/`Chapter Count` กลับ Notion + ใส่ `Year`/`Key Takeaway`/`Recommendation` ลง `catalog.md` → **นี่คือจุดที่ "list ใน body ข้างล่าง" ดึงข้อมูลจากชั้นบนได้**
3. **C — backfill** Year/Format/Cover/Source URL (dry-run ก่อน → ตารางข้อมูลเทียบ → เขียน)
4. **D — link ย้อนหลัง**: หา draft ที่ `Source` พูดถึงหนังสือเล่มไหน → เติม relation `Drafts` (Content Drafts.Source เป็น rich_text ที่มีทั้งชื่อแหล่งและ Notion page id อยู่แล้ว → parse ได้)

> ⚠️ ข้อจำกัดที่ต้องรู้: **push repo ยัง 403** (`Permission to lifetofree/phon-hermes.git denied`) → ข้อ B แก้ได้แค่ในเครื่องนี้ จนกว่าจะแก้สิทธิ์ token (fine-grained PAT: Contents R/W + repo `lifetofree/phon-hermes`)
> ข้อ B ควรเปลี่ยน `Notion-Version` จาก `2022-06-28` → `2025-09-03` และ endpoint `/databases/{id}/query` → `/data_sources/{id}/query` พร้อมกัน

---

## 6. ผลกระทบต่อบอทอื่น

| บอท | ผลกระทบ |
|---|---|
| Book Keeper | เพิ่ม property ในฐานที่เขาดูแล — ต้องแจ้งก่อน (ผู้ใช้อนุมัติแล้วถึงลงมือ) |
| Adduck Writer | อ่าน Books Library แบบ read-only → ไม่กระทบ · จะได้ `Key Takeaway` + `Recommendation` เป็นแกนบทความ (ข้อดี) |
| Research Scout / Research Distiller | relation ทางเดียว → ไม่กระทบเลย |
| Product Lead | ไม่กระทบ (ชั้นบนของ Books Library ไม่เกี่ยบกับการผลิต e-book) |
