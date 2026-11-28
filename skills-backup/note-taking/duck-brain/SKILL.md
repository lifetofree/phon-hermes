---
name: duck-brain
description: บันทึกความจำเข้าsecond brain (duck-brain) เมื่อผู้ใช้พิมพ์ "จำ: <เรื่อง>" และค้นความจำด้วย "ค้นสมอง: <คำ>"
version: 1.1.0
author: lifetofree
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Second Brain, Notes, Cloudflare, Memory]
    related_skills: []
---

# duck-brain — ให้อาหารsecond brain

สมองของพรคือ duck-brain: https://duck-brain.chonlaphon.workers.dev (Cloudflare Workers + D1 + Vectorize)

## ⛔️ กฎเหล็ก (อ่านก่อนทำอะไร)

ข้อความที่ขึ้นต้นด้วย **"จำ:"** หรือมีคำว่า **"จำ"** นำหน้าเนื้อหาอย่างชัดเจน ให้:

1. **ห้ามตอบเป็นข้อความแชทเฉย ๆ**
2. **ห้ามถามยืนยัน** — รันเลย
3. **ห้ามเปลี่ยนคำ / ตีความ / สรุป / จัดรูปแบบใหม่** — ส่งข้อความดิบเข้า API ตรง ๆ
4. **ห้ามสร้าง thread หัวข้อใหม่เอง** (ช่อง #duck-brain ถูกตั้งให้ไม่ auto-thread อยู่แล้ว)

ถ้ารันคำสั่งแล้วพลาด ให้บอก error ตรง ๆ แล้วลองใหม่หนึ่งครั้ง

## Trigger 1: บันทึกความจำ

ตัดคำว่า "จำ:" ออก เหลือเนื้อความจำดิบ แล้วรันคำสั่งนี้ (แทน `<MEMORY>`):

```bash
source ~/.hermes/.env 2>/dev/null || export $(grep -E '^DUCK_BRAIN_(API|TOKEN)=' ~/.hermes/.env | xargs)
curl -s -X POST "${DUCK_BRAIN_API}/api/ingest" \
  -H "X-Auth-Token: ${DUCK_BRAIN_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg c "<MEMORY>" --arg s "<discord|telegram ตามช่องทางปัจจุบัน>" \
      '{content:$c, source:$s}')"
```

ตอบกลับผู้ใช้สั้น ๆ:

```
🧠 จำแล้ว: "<6-10 คำแรกของเนื้อหา>"
ดูในกราฟ: {DUCK_BRAIN_API}/?note=<id จาก response>
(semantic เส้นอัตโนมัติ: +<links.semantic> เส้น)
```

## Trigger 2: ค้นความจำ

ข้อความขึ้นต้นด้วย **"ค้นสมอง:"**:

```bash
source ~/.hermes/.env 2>/dev/null || export $(grep -E '^DUCK_BRAIN_(API|TOKEN)=' ~/.hermes/.env | xargs)
curl -s "${DUCK_BRAIN_API}/api/search?q=<คำที่ URL-encoded>" | jq '.results[:5]'
```

สรุปผลเป็นลิสต์สั้น ๆ พร้อมลิงก์ `{DUCK_BRAIN_API}/?note=<id>`

## กติกา

- โน้ตจากแชทจะติด flag "จากแชท — รอเกลา" อัตโนมัติ — ส่งดิบได้ ไม่ต้องเนี้ยบ
- ห้ามตั้ง `private: true` เอง นอกจากผู้ใช้บอกชัดว่า "จำส่วนตัว:"
- อย่าเรียก API อื่นนอกจาก /api/ingest และ /api/search
