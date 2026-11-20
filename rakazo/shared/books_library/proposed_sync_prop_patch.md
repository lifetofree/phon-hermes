# Proposed patch (ยังไม่แตะ repo — รอเจ้าของอนุมัติ)

ไฟล์เป้าหมาย: `~/youtube-sync/repo/skills/content-pipeline/scripts/sync_books_library.py`
สาเหตุ: หลังเปลี่ยน `Tags` จาก `rich_text` → `multi_select` ฟังก์ชัน `prop()` ไม่รู้จักชนิด
`multi_select` จึงคืน `""` → **รอบ sync ถัดไป `research/books/catalog.md` จะไม่มี tag ขึ้นเลย**
(ยืนยันด้วยการรัน `prop()` จริงกับข้อมูลสด: ทุกแถวได้ `''`)

## แก้ `prop()` — เพิ่ม 2 บรรทัด

```python
def prop(p):
    t = p["type"]
    if t == "title":
        return "".join(x["plain_text"] for x in p["title"]).strip()
    if t == "rich_text":
        return "".join(x["plain_text"] for x in p["rich_text"]).strip()
    if t == "select":
        return p["select"]["name"] if p["select"] else ""
    if t == "multi_select":                                    # <-- เพิ่ม
        return " ".join(x["name"] for x in p["multi_select"]).strip()   # <-- เพิ่ม
    return ""
```

รูปแบบที่ได้: `#Business #ValueEquation #ProductDesign` (คั่นด้วยช่องว่าง — ตรงกับที่เคยเป็นใน rich_text)

## แก้ `fetch_chapters()` — เห็น child DB ครบ 41 เล่ม

ปัจจุบันสคริปต์เลือกเฉพาะ child_database ที่ **title มีคำว่า "chapter"** →
เจอแค่ **7/41 เล่ม** (34 เล่ม title ว่าง) และ 15 เล่มได้ chapter = 0 บท

```python
    for b in blocks:
        if b["type"] == "child_database":
            t = b["child_database"].get("title", "").lower()
            if "chapter" in t or not t.strip():      # <-- title ว่าง = chapter list เช่นกัน
                db_ids.append(b["id"])
```

(ทางเลือกที่สะอาดกว่า: rename child DB 34 เล่มที่ title ว่าง ให้เป็น "Chapter List" — ต้องขออนุมัติเจ้าของ)

## ผลกระทบหลังแก้

- catalog.md ได้ tag กลับมา 251 แถว
- chapter list ใน catalog.md เพิ่มจาก 27 เล่ม (77 บท) → 41 เล่ม (620 บท)
- ไฟล์ที่แตะ: 1 ไฟล์ ใน repo (ต้องขออนุมัติ — push ไป phon-hermes ยังติด 403)
