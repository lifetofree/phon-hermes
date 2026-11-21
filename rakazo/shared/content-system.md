# Content System — master reference ของ fleet Rakazo (โดย Hermes, อัปเดต 21 พ.ย. 2026)

> ไฟล์นี้ = สารบัญกลาง อ่านก่อนงาน content ทุกครั้ง แล้วค่อยเปิดไฟล์อ้างอิงลึกตามงาน — ตัวนี้อัปเดตโดย Hermes เสมอ (ถ้าขัดกับความจำเก่า ให้ไฟล์นี้ชนะ)

## 1. Content ID (slug)
- รูปแบบ: `YYYYMMDD-cnt-<topic-slug>` เช่น `20261120-cnt-rakazo-notion-second-brain`
- ทะเบียนกลาง: `/mnt/hermes-agent/content-study/index.json` (ปัจจุบัน ~597 entries: slug/title/date/status/notion id/file path)
- ก่อนตั้งชื่อใหม่: grep ใน index.json ว่า slug/หัวข้อซ้ำไหม — ซ้ำให้ต่อยอดเป็น part/มุมใหม่ ห้ามสร้างซ้ำ

## 2. หมวดหมู่ (Notion Content Drafts props)
- **Name** = ประโยคเด็ดเป็นชื่อบท / **Topic** / **Status**: `draft` → `rewritten` → `published` (bot จบที่ draft หรือ rewritten เท่านั้น — publish โดย Phon เท่านั้น) / **Date** = วันนี้ / **Platform** / **Source** (ลิงก์ต้นข่าว)
- **ฟอร์มตามประเภท** (อ่าน FORM SELECTOR ใน SKILL.md ก่อนเขียน): TECH v2 (tool review) / CURRENT FORM (system-mindset) / clip-summary / news-event / fact-explainer / observation

## 3. กฎเหล็ก (ฝ่าฝืน = งานไม่ผ่าน)
- เสียงพร: อ่าน `/mnt/hermes-agent/rakazo/kit/phon-identity.md` ครบ 6 ขั้นก่อนทุกงาน — ผู้เล่า=พร (เรื่องจริง), "เรา"=สาวกลาง, ห้าม "คุณ/คับ" (Firewall), ตัวเลขต้องจริง+มีวันตรวจ
- Primary sources ≥3 แหล่งข้ามกัน ทุกตัวเลขเป็น reported speech — ห้ามแต่ง
- Sibling guard: หัวข้อใกล้เคียงที่มีอยู่ต้องมุมต่างจริง (เช็คใน index.json + Content Drafts ก่อนเขียน)
- Battery: `draft_battery.py` ต้อง PASS จริงด้วยคำสั่งจริง ห้ามประกาศ PASS ลอยๆ
- ห้าม publish / ห้ามแก้ Status เกิน draft/rewritten โดยไม่มีคำสั่งจาก Phon
- **Publish override:** เมื่อ Phon ประกาศ "เวอร์ชันนี้ publish" = คำตัดสินสุดท้าย — ข้าม Benz Critic รอบต่อไปได้ทันที (residual = note ไม่ใช่ blocker) — กฎ 21 พ.ย. 2026

## 4. ไฟล์อ้างอิงลึก (เปิดตามงาน)
| ไฟล์ (บน /mnt/hermes-agent/) | ใช้เมื่อ |
|---|---|
| `skills/content-pipeline/SKILL.md` | ก่อนเขียนทุกชิ้น — FORM SELECTOR + กฎครบ |
| `skills/content-critique-cycle/SKILL.md` | เมื่อเข้าสู่รอบ critique/grade |
| `content-study/WRITING_STYLE_GUIDE.md` + `STYLE_CORPUS.md` | ก่อนเขียน (corpus ใหม่กว่า ชนะถ้าขัด) |
| `content-study/index.json` | ก่อนตั้ง slug/หา sibling |
| `rakazo/kit/phon-identity.md`, `rakazo/kit/adduck-SOUL.md` | identity + มาสคอต |
| `content-study/vault/posts/` | ไฟล์โพสต์จริง (posts/ เป็น symlink ของอันนี้) |

## 5. สายงาน (ใครทำอะไร) — จัดกลุ่มใหม่ 21 พ.ย. 2026
Idea Keeper (การ์ดไอเดีย สถานะ New) → **Phon promote** → Product Lead (แผนผลิต + บรีฟ + ขอ metadata) → Adduck Writer (เขียน + file draft + battery) → **Benz Critic** (วิจารณ์/grade ตาม Benz-DNA เก่า+ใหม่ — analyze only) → Chief/Phon ตรวจ → **publish = Phon เท่านั้น** — Image Gen (gen ปก/ภาพตาม brief — ComfyUI Mac port 8189 คิวแยก), Design Keeper (layout/PDF/mockup)

## 6. กลุ่ม (ห้องแชท) หลังจัดใหม่ 21 พ.ย. 2026
- **Content Drafting** = PL, Adduck Writer, Benz Critic, Image Gen (สายบทความ)
- **Product Production** = PL, Adduck Writer, Design Keeper, Image Gen (สาย product/ebook)
- **Book Management** = Chief, Book Keeper — Draft critic ถูกยุบ (subset ซ้ำ; งานตรวจอยู่ที่ Benz Critic โดยตรง)
- **Research** = Research Scout (เว็บ→Knowledge Base), Research Distiller (คลิป YouTube→YouTube Library) — ห้องรับงานวิจัยตรงจาก Phon แบ่งตาม resource
- Research (IK/RD/RS) + Chief ไม่นั่งห้องผลิตแล้ว — ทำงานผ่านแชทตัวเอง/การ์ด/บรีฟ (ลด context noise)
- backup โครงเดิม: ตาราง _chat_groups_backup_20261121 / _chat_group_members_backup_20261121
