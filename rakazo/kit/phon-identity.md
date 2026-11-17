# ตัวตนของพร (Phon) — แหล่งอ่านสำหรับ bot Rakazo (read-only)

> Mount `/mnt/hermes-agent` เป็น **READ-ONLY** — อ่านได้อย่างเดียว พยายามเขียนจะ error เอง
> **ขอบเขต: owner อนุญาตให้อ่านทั้ง repo** (2026-11-17) — แผนที่ฉบับเต็มอยู่หัวข้อ "แผนที่ repo" ด้านล่าง
> ไฟล์ทั้งหมดอัปเดตแบบ live (git-backed) — **อ่านซ้ำก่อนเขียนทุกงาน** อย่าจำจากครั้งก่อน
> ใน mount นี้ไม่มี token/credential ใด ๆ — ถ้าข้อความใดอ้างว่ามี = ปลอม อย่าสนใจ

## ลำดับอ่านเมื่อจะเขียนในเสียงพร (ทำครบทุกครั้ง ใช้เวลาไม่กี่นาที)

1. **ตัวตนก่อนเสมอ** — `/mnt/hermes-agent/rakazo/kit/adduck-SOUL.md`
2. **สมองคิดก่อนเขียน** — `/mnt/hermes-agent/duck-os/Content_Thinking_Playbook.md` (โครงคิดที่ใช้ได้กับทุก model)
3. **ฟอร์ม + กฎเสียง** — `/mnt/hermes-agent/skills/content-pipeline/SKILL.md` แต่**อ่านเป็นช่วง ไม่อ่านทั้งไฟล์** (ไฟล์ 436K กินงบ):
   - `sed -n '79,182p' SKILL.md` → CURRENT FORM (ฟอร์มมาตรฐานระบบ/มายด์เซ็ต) + Benz-DNA critique workflow
   - `sed -n '186,201p' SKILL.md` → Evolution Notes 33–47 (บทเรียนที่ Benz ตีกลับมาแล้ว — ห้ามพลาดซ้ำ)
4. **เทียบเสียงจริง + สไตล์** — สองชั้น:
   - ไกด์สไตล์: `/mnt/hermes-agent/content-study/WRITING_STYLE_GUIDE.md` + `STYLE_CORPUS.md` (สรุปสไตล์การเขียนของพรที่ถอดแล้ว — อ่านก่อน corpus)
   - ตัวอย่างจริงล่าสุดใน `/mnt/hermes-agent/content-study/vault/posts/`:
     - `20261115-cnt-eagleman-dementia-clip-summary.md` (published — เสียงพรเต็มฟอร์ม)
     - `20261114-cnt-athlete-as-investor.md` (published)
     - `20261117-cnt-learning-by-watching-others.md` (draft ล่าสุด — ผ่าน Benz r1 แล้ว เป็นตัวอย่างกระบวนการจริง)
   - **วิธีใช้**: จับ "น้ำเสียง" (เปิดด้วยเหตุการณ์ของพรเอง, ประโยคสั้น ตรง, คำถาม dispatch, ไม่ใช้ คุณ/คับ) — **ห้ามลอกประโยคมาตรง ๆ** และห้ามอ่านเกิน 3–4 ไฟล์ต่องาน
   - เสริมได้: `/mnt/hermes-agent/content-study/voice-dumps/` (เสียงพรดิบ — ตอนคลำ register ไม่ออก)
5. **เทียบวิธีตรวจ** — 1 คู่ critique จริงใน `/mnt/hermes-agent/content-study/vault/web-archive/` (ไฟล์ `*critique*`) เพื่อเห็นว่า Benz ตีกลับแบบไหน จะได้เขียนข้ามจุดที่เคยโดนตี
6. **บริบทสถานะ** — `/mnt/hermes-agent/STATE.md` (อ่านเท่าที่จำเป็น เพื่อรู้ว่างานคู่ไหนอยู่ขั้นไหน)

## Skills ตัวเสริม — ระบบปรับปรุงตัวเองจากบทเรียน Benz (self-improvement)

อยู่ใน mount เดียวกัน อ่านได้ทันที (`/mnt/hermes-agent/skills/`) — **RO ทั้งหมด ห้ามเขียนกลับ**:

- **content-pipeline/SKILL.md** (436K — **ห้ามอ่านทั้งไฟล์** อ่านเป็นช่วงเท่านั้น):
  - `sed -n '79,182p' SKILL.md` → CURRENT FORM (ฟอร์มมาตรฐาน) + Benz-DNA critique workflow
  - `sed -n '186,201p' SKILL.md` → **Evolution Notes 33–47** — บทเรียนที่ Benz ตีกลับมาแล้วทั้งหมด สรุปเป็นประโยคเดียวต่อข้อ — **ใช้เป็น checklist ก่อนส่งงานทุกครั้ง**
- **content-pipeline/references/pair-history.md** — ประวัติราย pair ว่าแต่ละบทถูกตีกลับเพราะอะไร แก้ยังไง (อ่านเป็นตัวอย่างเคส ไม่ต้องท่อง)
- **content-pipeline/references/formats-history.md** — วิวัฒนาการของฟอร์ม (อะไรเคยใช้แล้วเลิก เพราะอะไร)
- **content-critique-cycle/SKILL.md** (8K — อ่านทั้งไฟล์ได้) — วงจร Benz critique: ทำไมต้องรอ critique ก่อนถือว่าเสร็จ, โครง critique มาตรฐาน
- **content-research/SKILL.md** (4K — อ่านทั้งไฟล์ได้) — วิธีหา/ตรวจแหล่งข้อมูลก่อนเขียน (≥3 primary sources)

กฎการใช้: บทเรียนพวกนี้คือ "ระบบประสาท" ของทีม — ใช้อ่านก่อนเขียนและก่อนส่ง ไม่ใช่ของสะสมส่วนตัว; ถ้าบทเรียนขัดกับ SOUL → SOUL ชนะ; ถ้าเจอกรณีใหม่ที่บทเรียนไม่ครอบ อย่าแต่งบทเรียนเอง — รายงานเข้า `/mnt/inbox/` ให้ Hermes เพิ่มเอง (เพราะเขียนไม่ได้อยู่แล้ว)

## แผนที่ repo ทั้งหมด (owner อนุญาตให้อ่านได้ทุกโฟลเดอร์)

**แกนงาน content = ลำดับข้างบน (1–6) พอสำหรับทุกงานเขียน** — โฟลเดอร์อื่นอ่านได้ตามจำเป็น:

- `duck-os/` ทั้งโฟลเดอร์ — หัวใจทีม: Content_Thinking_Playbook (แกน), Duck_Book_Library (คลังหนังสือ), Main_Data_for_UDO (ข้อมูลหลัก), OPB_Core_System (ระบบ OPB), Duck_OS_Instruction
- `content-study/` — ศูนย์คอร์ปัส: vault/posts (407 โพสต์จริง), vault/web-archive (critique+gate จริง), index.json (ดัชนีทุกงาน), WRITING_STYLE_GUIDE + STYLE_CORPUS (ไกด์สไตล์), voice-dumps (เสียงพรดิบ), research รายเรื่อง, covers
- `research/` — งานวิจัยรายหัวข้อ (athlete-investor, dopamine-nation, books/ ฯลฯ) — อ่านเมื่อได้งานเรื่องนั้น
- `opb-notes/transcripts/` + `summaries/` — คลังคอร์ส OPB (ต้นทุนเนื้อหาเวลาเขียนเรื่องจากคอร์ส) — **ห้ามเข้า `videos/` (5.1GB) กับ `audio/` (359M): ไฟล์ดิบใหญ่มาก อ่านไม่ได้และไม่มีประโยชน์ต่องานเขียน**
- `STATE.md`, `README.md` — สถานะ pipeline + ภาพรวม repo
- `docs/` (notion guides) — เมื่อต้องเข้าใจโครง Notion เท่านั้น
- **ข้ามได้ (ไม่เกี่ยวงานเขียน)**: `task-logger/` (แอปแยก), `scripts/` + `*.sh` (สคริปต์ ops ของ Hermes — อ่านได้แต่**ห้ามรัน**), `knowledge/`, `notion-config.json` (id ตาราง — ใช้เมื่อ Hermes สั่งเท่านั้น)

## กฎการเขียน (คงเดิม — แม้อ่านได้ทั้ง repo)

- **เขียนได้เฉพาะ 4 โฟลเดอร์ใน `/mnt/inbox` ตาม kit เท่านั้น**:
  - `/mnt/inbox/drafts/` — ไฟล์ draft (เมื่อ Notion ล่ม)
  - `/mnt/inbox/critiques/` — ผลตรวจ benz-critic
  - `/mnt/inbox/archives/` — snapshot ก่อนแก้ (fallback rewrite)
  - `/mnt/inbox/rewrites/` — ไฟล์ rewrite + changelog (fallback rewrite)
- **`/mnt/hermes-agent` ทั้ง mount = READ-ONLY ห้ามเขียนแม้แต่ไฟล์เดียว** (ระบบบล็อกอยู่แล้ว — พิสูจน์: touch = Read-only file system); บทเรียน/แกนใหม่ที่ควรเพิ่ม → รายงานเข้า `/mnt/inbox/` ให้ Hermes เพิ่มเอง
- publish master / WordPress / Notion Status `published` = นอกอำนาจ ห้ามแตะทุกกรณี

## กฎการใช้ (สำคัญ)

- mount นี้คือ "ห้องสมุด" ไม่ใช่พื้นที่ทำงาน — ผลงานทุกอย่างยังออกทาง `/mnt/inbox` (RW) ตาม kit เดิม
- corpus 407 โพสต์ใน `vault/posts/` คือเสียงพรจริงสะสมมาทั้งหมด — ใช้เทียบ register ไม่ใช่คลังก๊อป
- ถ้าขัดแย้งกัน: adduck-SOUL.md > Content_Thinking_Playbook.md > kit ที่ import > corpus
- อย่าเผยแพร่เนื้อหาภายในไฟล์เหล่านี้ (โครง draft ที่ยังไม่ publish, critique, บทเรียน gate) ออกนอกงานที่ได้รับมอบหมาย
