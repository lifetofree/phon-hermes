---
type: research
topic: "Rakazo — automation: routines (5 ทริกเกอร์) / ทีมบอต (groups, subagents) / สอนงาน (teach→skill) / pages + สถานะการใช้จริงบนเครื่อง + use cases"
used_by: "[[pair-123]]"
verified: 2026-11-19
---

# Rakazo automation — docs upstream + สถานะจริงบน DB (2026-11-19)

## ชั้น 1 — เอกสาร upstream (docs/routines.md, groups.md, skills.md, pages.md — ดึง 2026-11-19)

### Routines = prompt ที่บอตรันเองได้ — 5 ทริกเกอร์
1. **On a schedule** — ชั่วโมง/วัน/weekday/สัปดาห์/เดือน/custom interval; **รับ cron expression**; timezone ตาม Settings
2. **When something changes (watch)** — เช็คทุก 5 นาที–1 วัน, รันเมื่อเปลี่ยน; ดูได้: ไฟล์/โฟลเดอร์บน computer, output ของ command, tool จากแอปที่ต่อ (argument รับวันที่เลื่อนได้ เช่น `{{today+2d}}`); toggle "Post No changes"; **ใช้คู่กับ schedule ไม่ได้**
3. **Webhook** — ได้ URL+key, POST จากบริการใดก็ได้มาจุดรัน
4. **Git event** — URL ไปใส่เป็น GitHub webhook → push / issue / pull request จุดรัน
5. **Email** — บอตมีที่อยู่เมลเอง (เช่น scout@bots.example.com); forward หรือ CC (ต้อง forward ไม่ใช่ redirect); เลือกได้ Only me / ทั้งโดเมน; **โผล่เฉพาะ server รับ email ได้**
6. (บนแชต Slack message ก็จุดรันได้)

### กติกาความปลอดภัย (docs ระบุ)
- run ที่จุดจาก webhook/email/Slack อยู่ใต้ **approval mode + Always allow list** เดิม — เครื่องมือที่เปลี่ยนของถูกตรวจแม้ไม่มีคนดู; **approval card หมดอายุ 30 นาที ถ้าไม่มีใครกด = action ไม่เกิด**
- Test run / พัก (Active off) / Run history ทุก run; mobile ดู+สร้าง routine ได้ (webhook/git/watch ตั้งบน web/desktop)
- **Advanced: routine มีโมเดล + thinking level ของตัวเองได้** (จับคู่ schema จริง: modelProvider/modelId/thinkingLevel)

### นอกจากตารางเวลา — การจัดทีม + การสอนงาน
- **groups.md**: group chat 2–10 บอต; @Name ปลุกรายตัว, @everyone ปลุกหมด; บอตส่งงานถึงบอต (Messaged/Message from — view-only); **subagents** = ตัวช่วยอายุสั้นแยกขนาน รายงานกลับเป็น card (Running/Completed/Failed) แล้วจบไป; บอตสร้างบอตใหม่ได้
- **skills.md**: "save that as a skill" หลังงานหลายขั้น → บอตเขียน skill ให้ตัวเองและทีมใช้ซ้ำ; **Teach a task** = เปิดหน้าจอบอต อัดทำให้ดูครั้งเดียว → บอตเขียน Draft skill (ขั้นตอน+เมื่อไรควรถามก่อน) → แก้ → Test → **Add to routine**; password ใช้ Protected input ไม่ถูกอัด
- **pages.md**: บอตสร้าง page (dashboard/status board/report) จากแชต; **routine อัปเดตหน้าเดิมต่อได้** (bot แก้หน้าเดิม ไม่สร้างใหม่); share ด้วยลิงก์ได้

## ชั้น 2 — สถานะจริงบนเครื่อง (DB query 2026-11-19)

### routines = 9 ตัว — ภาพการใช้จริง
- **ทริกเกอร์: ทุกตัวเป็น schedule (cron 1 แถว/ตัว) — webhook/git/watch/email/messageProvider = NULL/false ทั้ง 9** → ใช้จริง 1 จาก 5 ทริกเกอร์
- **ทุกตัว inactive แล้ว (active=f 9/9) แต่ ever_ran=t ทุกตัว** → ใช้แบบ "ตัวจับเวลาตรวจงานชั่วคราว" ระหว่างวันทำงาน ไม่ใช่ habit ประจำ — ตัวอย่างหน้าที่จากชื่อ (ไม่ลงชื่อจริงในบท): ตรวจงาน design ซ้ำ, ตรวจ pipeline 3 ขั้น, dispatch บรีฟให้บอตตัวอื่น, เช็คการส่งมอบบท
- ชื่อ routine มีคำไทยปนเชิงงานจริง (แก้คิว/ยิงบรีฟ/ตรวจรอบสุดท้าย) = ภาษาคนใช้จริง

### เลขรอบตัว
- `runs` รวม **270** = chat 261 + **routine 9** → ~3% ของงานผ่าน automation
- `chat_groups` = 4 (แชตทีมภายใน) · `agent_skills` = 1 (skill ของบอตสายเขียน) · `computers` = 1 · `memory_documents` = 9 · bots 8 ตัว
- ทริกเกอร์ email/slack ยังจุดไม่ได้เพราะช่องทางยังไม่ตั้ง (ดู research rakazo-integrations)

## Use cases ที่ผูกกับของจริงบนเครื่องนี้ (เสนอเป็น "ลองได้ถัดไป" — ไม่ใช่ที่เคยทำ)
1. **Schedule แบบ habit** — เช้าวันจันทร์รวมงานค้างทุกบอตส่งสรุป; ต่างจาก 9 ตัวเดิมที่ตั้งใช้ครั้งเดียวแล้วปิด
2. **Watch โฟลเดอร์** — /mnt/inbox (mount rw จริงบน computer) มีไฟล์ใหม่ = บอตทำงานต่อทันที ไม่ต้องรอคำสั่ง
3. **Git event** — push/PR เข้า repo ที่บอตดูแล → บอตสรุป diff/รายงานกลับ
4. **Email trigger** — ส่งงานโดย forward เมลถึงที่อยู่บอต (ต้องเปิดรับ email ฝั่ง server ก่อน — ยังไม่ได้ตั้ง)
5. **Teach → skill → routine** — สอนงานที่ทำซ้ำด้วยการทำให้ดูครั้งเดียว แล้วติดตาราง
6. **Page + routine** — dashboard ตารางงานทีมที่ routine อัปเดตให้เอง

## สำหรับ draft (#123)
- docs = vendor claims ติดป้าย; ตัวเลข DB = machine-verifiable
- หลีกเลี่ยงรีวิว integration catalog ซ้ำกับ #122 — พูดถึงช่องทางแค่เป็นเงื่อนไขของ trigger (1 ประโยค)
- Sibling guard vs #121: คำ 403/cherry-pick/egress/RAM 2GB/compose up/YouTube Library = 0
- จุดขายความจริงใจ: "routines ใช้แล้วแต่แบบตัวจับเวลาชั่วคราว — 5 ทริกเกอร์ใช้จริง 1"
