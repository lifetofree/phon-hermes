# บรีฟ Rakazo: YouTube Library → Markdown → GitHub

> บรีฟนี้ใช้วางใน Rakazo เป็น (1) Skill สำหรับสั่งเป็นครั้ง ๆ หรือ (2) Routine prompt สำหรับรันตามตาราง
> ฝั่ง Hermes: bot push ไป branch `rakazo/youtube-library` เท่านั้น — Hermes เป็นผู้ merge กลับเข้า main เมื่อ owner สั่ง

## บรีฟ (วางทั้งก้อนนี้ใน Rakazo)

หน้าที่ของคุณ: แปลงทุกแถวของ Notion database "YouTube Library" เป็นไฟล์ markdown แล้วอัปโหลดขึ้น GitHub repo `lifetofree/phon-hermes` บน branch `rakazo/youtube-library` (ห้ามแตะ main)

### ขั้นตอน

1. ดึงข้อมูลจาก Notion: อ่านทุกแถวของ database "YouTube Library" ผ่าน MCP ที่ connect ไว้ ให้ครบทุกแถว (ถ้ามี pagination/cursor ให้วนจนหมด) — เอาทั้ง properties (Name, video URL, Date, Status, Channel) และเนื้อหา (body/summary) ของแถว พร้อม `last_edited_time` ของแต่ละแถว
   - ห้ามเดาหรือสร้างข้อมูลแถวเอง — ถ้า MCP ล่มหรือ 401 ให้รายงานและหยุด

2. เทียบ state เดิม: อ่านไฟล์ `~/youtube-sync/processed.json` ในเครื่องของคุณ (ถ้ายังไม่มีให้ถือว่าว่าง) — ทำงานเฉพาะแถวที่ (ก) ยังไม่เคยทำ หรือ (ข) `last_edited_time` เปลี่ยนจากที่บันทึกไว้

3. แปลงแต่ละแถวเป็นไฟล์ `youtube-library/<slug>.md`:
   - slug = ชื่อคลิป (Name) แปลงเป็น kebab-case ตัวพิมพ์เล็ก ตัด emoji/อักขระพิเศษ/วรรณยุกต์ไทยออกจาก slug, ชื่อซ้ำให้ต่อท้าย -2, -3
   - โครงไฟล์:

     ```
     ---
     title: <Name>
     video_url: <URL>
     date: <Date จาก Notion>
     status: <Status>
     channel: <Channel>
     notion_page_id: <page id>
     synced_at: <YYYY-MM-DDTHH:mm:ss+07:00>
     ---

     # <Name>

     <เนื้อหา body ของแถว คง markdown เดิม>
     ```

   - ถ้า body ว่าง ให้ใส่บรรทัด "_(ยังไม่มีสรุปใน Notion)_" แทน

4. อัปโหลดขึ้น GitHub:
   - เรียกใช้ token จาก secret ชื่อ `GITHUB_TOKEN` เท่านั้น — ห้ามแสดง token ใน output, ห้าม log URL ที่ฝัง token
   - โฟลเดอร์ทำงาน: `~/youtube-sync/repo` — ถ้ายังไม่มี ให้ clone:
     `git clone --branch main https://x-access-token:$GITHUB_TOKEN@github.com/lifetofree/phon-hermes.git ~/youtube-sync/repo`
     แล้ว `git checkout -b rakazo/youtube-library` (ถ้า branch นี้มีบน remote แล้วให้ `git checkout rakazo/youtube-library` + `git pull --rebase origin rakazo/youtube-library`)
   - เขียนไฟล์ใหม่/อัปเดตเฉพาะใน folder `youtube-library/` — ห้ามแก้/ลบไฟล์นอก folder นี้เด็ดขาด ห้าม merge ลง main ห้าม force-push
   - commit รวมรอบละครั้ง: `sync(youtube-library): N new, M updated (<YYYY-MM-DD HH:mm>)`
   - push: `git push origin rakazo/youtube-library` (ครั้งแรกใช้ `-u`) — ถ้าโดนปฏิเสธให้ `git pull --rebase origin rakazo/youtube-library` แล้ว push ซ้ำได้อีกครั้งเดียว ถ้ายังพังให้รายงาน

5. บันทึก state: อัปเดต `~/youtube-sync/processed.json` (page_id → last_edited_time ของแถวที่ทำสำเร็จ) **หลัง push สำเร็จเท่านั้น** — push พัง = ห้ามบันทึก เพื่อรอบหน้าลองใหม่

6. รายงานกลับสั้น ๆ: จำนวนแถวใหม่ / อัปเดต / ข้าม, รายชื่อไฟล์, commit hash, ลิงก์ branch

### ขอบเขตความปลอดภัย
- ใช้ `GITHUB_TOKEN` (fine-grained, สิทธิ์ Contents: Read+Write เฉพาะ repo `lifetofree/phon-hermes`) จาก secret ของ Rakazo เท่านั้น
- อ่าน Notion ผ่าน MCP ที่ connect ไว้เท่านั้น ไม่ใช้ token อื่น
- พื้นที่เขียนบน GitHub มีแค่ branch `rakazo/youtube-library` + folder `youtube-library/`
- ทุกครั้งที่รันต้อง idempotent: รันซ้ำโดยไม่มีแถวเปลี่ยน = push 0 commit และรายงาน "no changes"

### Trigger
- สั่งมือ: "sync youtube library"
- หรือผูก Routine: ทุกวัน เวลาที่เลือก (แนะนำหลังเที่ยงคืน GMT+7 ก่อน daily-news 08:00 จะไม่ชนงาน Hermes)

## สิ่งที่ owner ต้องเตรียมครั้งแรก (ครั้งเดียวจบ)
1. Notion MCP: Rakazo → Integrations → + → MCP server → `https://mcp.notion.com/mcp` → OAuth → เลือกแชร์เฉพาะ YouTube Library DB
2. GitHub token: สร้าง fine-grained PAT (Contents: Read+Write, เฉพาะ repo phon-hermes) ที่ github.com → Settings → Developer settings → แล้วเก็บเป็น secret ชื่อ `GITHUB_TOKEN` ใน Rakazo (bot secrets)
3. เลือก trigger: สั่งมือหรือ routine

## ฝั่ง Hermes (ผมจัดการเองเมื่อ owner สั่ง)
- merge `rakazo/youtube-library` → main, แล้ว push — ทำเมื่อ owner บอก หรือผูกกับ weekly sweep
- ถ้าต้องการให้ไฟล์ชุดนี้เข้า vault/Obsidian ด้วย แจ้งเพิ่มแล้วผมต่อ generator ให้
