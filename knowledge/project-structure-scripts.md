# UDO Project Structure — Scripts & Knowledge Workflow

## สรุป
สคริปต์ที่ UDO ใช้ถูกรวมไว้ที่ `~/hermes-agent/scripts/` แล้ว: `create_kb_page.py` คือสคริปต์หลักสำหรับสร้างหน้าใน Notion KB, `crud_operations.py` เป็น helper สำหรับ CRUD. กฎใหม่: ความรู้ทุกชิ้นต้อง save ทั้ง 2 ที่ — Notion KB และ folder ล็อกัล `~/hermes-agent/knowledge/`.

## โครงสร้างไฟล์ (as of 2026-08-27)
| ไฟล์ | หน้าที่ |
|---|---|
| `~/hermes-agent/AGENT.md` | Persona + conventions ของ UDO (canonical, อยู่ root) |
| `~/hermes-agent/STATE.md` | สถานะ Notion ปัจจุบัน + recent activity |
| `~/hermes-agent/.env` | `NOTION_TOKEN` (bot "Hermes-connection") — source ก่อนเรียก API เสมอ |
| `~/hermes-agent/scripts/create_kb_page.py` | สคริปต์หลักสร้างหน้า KB (helpers: `h2/h3/p/li`, `create_page()`) |
| `~/hermes-agent/scripts/crud_operations.py` | CRUD helpers (create/read/update/delete) |
| `~/hermes-agent/scripts/crud_operations_root_backup.py` | สำเนา backup ของ root-level copy เก่า (ย้าย 2026-08-27) |
| `~/hermes-agent/knowledge/` | โน้ตความรู้แบบ markdown ล็อกัล — mirror กับ Notion KB |

## Knowledge workflow (บังคับใช้)
1. สรุปเนื้อหา → Title + Summary (1-3 ประโยค)
2. สร้างหน้าใน Notion KB ผ่าน:
   ```python
   import sys; sys.path.insert(0, "/home/lifetofree/hermes-agent/scripts")
   from create_kb_page import create_page, h2, h3, p, li
   url = create_page(title=..., summary=..., category="tech", tags=[...], body=[...])
   ```
   (token อ่านจาก `NOTION_TOKEN` ใน `.env` อัตโนมัติ — ห้าม hard-code)
3. เขียนไฟล์ markdown mirror ที่ `~/hermes-agent/knowledge/<slug>.md`
4. อัปเดต Recent Activity ใน `STATE.md`

## Reference
- AGENT.md §2.4 (CRUD Operations flow)
- Notion KB: https://app.notion.com/p/3c9df8d88d8c81acba5efa129e493638
