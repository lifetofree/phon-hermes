# Content System — master reference ของ fleet Rakazo (โดย Hermes, อัปเดต 21 พ.ย. 2026)

> ไฟล์นี้ = สารบัญกลาง อ่านก่อนงาน content ทุกครั้ง แล้วค่อยเปิดไฟล์อ้างอิงลึกตามงาน — ตัวนี้อัปเดตโดย Hermes เสมอ (ถ้าขัดกับความจำเก่า ให้ไฟล์นี้ชนะ)

## 1. Content ID (slug)
- รูปแบบ: `YYYYMMDD-cnt-<topic-slug>` เช่น `20261120-cnt-rakazo-notion-second-brain`
- ทะเบียนกลาง: `/mnt/hermes-agent/content-study/index.json` (ปัจจุบัน ~597 entries: slug/title/date/status/notion id/file path)
- ก่อนตั้งชื่อใหม่: grep ใน index.json ว่า slug/หัวข้อซ้ำไหม — ซ้ำให้ต่อยอดเป็น part/มุมใหม่ ห้ามสร้างซ้ำ

## 2.1 Metadata & Content Taxonomy ทางการ (ตาม duck-os/Main_Data_for_UDO.md PART 5 — บังคับทุกชิ้น)
- **Asset ID/Slug:** `{YYYYMMDD}-{TYPE}-{SLUG}` ตัวพิมพ์ใหญ่ เช่น 20261122-CNT-WISPR-FLOW-37DAY-USAGE
- **Categories (เลือกจาก 8):** System Core / Decision Protocols / Survival Guide / Asset Library / Productivity Hacks / System in Action / System Awareness / Duck OS Logs
- **Content Type:** 🔴 Core Content / 🟢 Casual Content (+ คำกำกับหัวข้อในวงเล็บ)
- **Status:** ⬜ Idea · 🟨 Drafting · 🟧 Visualizing · 🟦 Ready · ✅ Published
- **Law Alignment:** ⚙️ Law 1 System > Emotion · 🔥 Law 2 Action > Motivation · 🛡️ Law 3 Protect System · 🛠️ Decision Protocol · 🏛️ Philosophy/Stoicism
- **Target Energy Level:** 🟢 G.1 · 🟡 G.2 (สั้น จบในตัว) · 🟠 G.3 (storytelling) · 🔴 Boss
- **Excerpt:** สรุปสำหรับ social preview
- **Hashtags:** #Adduckivity #DuckOS #NeuroDivergent + ที่เหมาะสม (IG ≤5)
- **Cover Image:** **606x370** (เปลี่ยนจาก 1080x1080 — 23 พ.ย. 2026) ห้ามมี Text/Logo/Headline (พรใส่เอง) · ชื่อไฟล์ `{slug}-cover-606x370.jpeg` + **Alt Text (EN)** · gen ผ่าน ComfyUI ใช้ 608x376 (ทวีคูณ 8) แล้ว resize เป็น 606x370 — template: shared/comfyui/z-image-template-cover-server.json
- ช่องตรวจภายใน (grade history / evidence class / open findings / Notion id) เก็บคู่กันในเมตาดาต้า audit

## Workflows — แยก 2 Lane (บังคับ — 23 พ.ย. 2026 ตามสั่ง Phon: สองสายนี้ไม่เหมือนกัน)
**CONTENT Lane (บทความ/โพสต์ — สั้น รายวัน):**
วัตถุดิบ: ไอเดีย/ข่าว/วิจัย (Idea, Research Scout, Distiller) → AW เขียนบทเดียวตามฟอร์มบทความ → Benz Critic เป็น gate หลัก (Benz-DNA + ledger) → Phon publish — ติดตาม: ฐาน Content Drafts (draft → rewritten → published)
เกณฑ์ตรวจ: article criteria (คุณ 0 คับ 0 / evidence / firewall / TECH form disclaimer) + identity + draft_battery
**PRODUCT Lane (e-book/product — ยาว หลายบท):**
วัตถุดิบ: PRD/DIRECTIVE + Books Library + OPB 3 Laws → PL วางแผนแตกบท → AW เขียนทีละ chapter (คิวทีละชิ้น — บังคับ) → PL ตรวจด้วย ebook checklist (โครงบท/DIRECTIVE/docs จริง/แยกแพลตฟอร์ม — อยู่ใน instruction ของ PL) → Design Keeper ปก 606x370 /layout/PDF → PL รวมสถานะผลิต (ฐาน Products) → Phon อนุมัติ
เกณฑ์ตรวจ: ebook checklist + identity + DIRECTIVE — **ห้ามใช้ article criteria ตรวจ chapter**
กติกาข้าม lane:
- Benz Critic ไม่ใช่ gate ของ PRODUCT Lane — ถ้าส่งให้ดู chapter ให้ตรวจแค่ภาษา/สไตล์ ห้ามตัดสินโครง (เจ้าของโครง = PL)
- Book Keeper ติดตาม "การอ่าน" (Chapter List/INSTALLED) เท่านั้น — สถานะ "การเขียน ebook" อยู่กับ PL/ฐาน Products — ห้ามปนสองชุด
- Chief จำแนก lane ก่อน dispatch ทุกงาน ไม่ชัดให้ถาม Phon
- Metadata: ทั้งสอง lane ใช้ PART 5 taxonomy ร่วมกัน (Categories/Content Type/Law/Energy ต่างกันตามชิ้น)
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
