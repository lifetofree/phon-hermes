# วัตถุดิบเคสจริง — การใช้งาน Rakazo ของพร (สำหรับ e-book ติดตั้ง Rakazo)

> เตรียมโดย Product Lead 18 พ.ย. 2026 01:15 — ตามสั่ง Phon "ของานจริง ตามการใช้จริงของพรผ่าน Rakazo"
> **กฎเหล็ก:** AW เล่าได้เฉพาะข้อเท็จจริงในไฟล์นี้ + docs จริง rakazo.com เท่านั้น — ห้ามแต่งเคส ฉาก บทสนทนา ตัวเลข หรือวันเวลาที่ไม่มีที่มา
> จุดไหนเล่าต่อไม่ได้เพราะไม่มีวัตถุดิบ ให้เว้นไว้ `[รอพรเติม: ...]` แล้ว PL รวบรวมจากพรเอง
> ที่มาตรวจย้อนได้: repo lifetofree/phon-hermes (mount `/mnt/hermes-agent` — STATE.md, kit/), ระบบ Rakazo ที่ใช้จริง (ทีมบอท), เล่ม DuckOS Field Guide v0.3 (PDF จริง 20 หน้า, โฮม Chief)

## 1. ทีมบอทจริงที่พรใช้อยู่ (fleet จริงใน Rakazo)
- พรใช้บอท 7 ตัวแบบ "หนึ่งบอทต่อหนึ่งงาน" (ตรงหลัก "One bot per job works best" ใน docs):
  Chief (คุม fleet + re-verify งาน), Idea Keeper (เก็บไอเดียลง Notion), Research Scout (วิจัยเว็บลง Knowledge Base), Research Distiller (สรุปคลิป YouTube สองภาษา), Adduck Writer (เขียน draft content), Stall Watcher (สรุป "งานค้าง" ให้พร), Product Lead (คุมสายผลิต product จากไอเดีย)
- จัดกลุ่มแชทจริง 2 ห้อง: Content Drafting (ห้อง brainstorm/handoff สายคอนเทนต์) และ Product Production (ห้องสายผลิต product)
- ทุกบอทมีคอมพิวเตอร์ของตัวเอง — แชร์ Team Computer ในพื้นที่ทำงานเดียวกัน ส่งไฟล์งานกันผ่านโฟลเดอร์ `shared/` มีเบราว์เซอร์ git และเครื่องมือแปลงไฟล์ใช้จริง

## 2. งานจริงที่ระบบนี้ทำได้ (หลักฐาน STATE.md ใน repo — git-backed live)
- ผลงานคอนเทนต์จริง: คู่บทความ #79–#107 ปิด/published ต่อเนื่อง (เว็บ wp.adduckivity.com + ฐาน Notion) — ล่าสุด #107 (Amazon Alexa text-to-shop) publish 9 พ.ย. 2026 โดยพรเขียน publish เวอร์ชันตัวเอง
- ระบบตรวจงานหลายรอบจริง (critique gate หลายรอบต่อชิ้น) — จุดตัดสินสำคัญทุกจุดเป็นของพร: approve/deny เอง (ตรงกับหลัก Approvals ใน docs)
- มี content vault (Obsidian) + สคริปต์ generate ไฟล์อัตโนมัติที่บอทจัดการเอง
- แก้ปัญหาจริงที่เจอ: cache bug ตอน sync โพสต์ WordPress — ระบบ re-run แล้ว backfill สำเร็จ 11 โพสต์

## 3. เชื่อมแอปจริงผ่านบอท
- Notion workspace "lifetofree" = ฐานข้อมูลกลางจริงของทีม: Idea, Content Drafts, Products, YouTube Library, Books Library — บอทอ่าน/เขียนผ่าน token ที่พร approve เอง
- GitHub repo lifetofree/phon-hermes = แหล่ง kit/identity/skill ของทีม — ไฟล์ live ทุกบอทอ่านก่อนทำงานทุกครั้ง (เช่น phon-identity.md)

## 4. ผลงานเล่มจริงที่ผลิตด้วยระบบนี้
- DuckOS Field Guide v0.3 — เล่มจริง 20 หน้า A4 เสียงพรเล่าเรื่องจริง + Field Sheet หน้าเดียว = ต้นแบบ format ของ e-book เล่มนี้ (จาก mockup ถึงเล่ม ใช้ทีมบอทช่วยผลิตทั้งสาย)

## 5. ยังไม่มีวัตถุดิบ — ห้ามอ้าง (ให้เว้น [รอพรเติม] แทน)
- ฉากใช้งานวันแรกของพร, บทสนทนาจริงกับบอท, เวลา/วันที่ใช้จริงเป็นรายจุด, จำนวนชั่วโมงที่ประหยัดได้
- กรณี "พร import เอเจนต์จาก Hermes" — ยังไม่มีหลักฐานว่าใช้ช่องทาง import-an-agent (ทีมนี้สร้างเป็นบอทในระบบโดยตรง) ห้ามเล่าว่า import
