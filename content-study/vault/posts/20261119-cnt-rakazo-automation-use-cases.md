<!--
PAIR: #123 rakazo-automation-use-cases (TECH lane)
Status: draft v1 (2026-11-19 — owner brief: "research rakazo เรื่อง automation ยกตัวอย่าง use case เพราะยังไม่ได้ใช้ครบทุกฟังก์ชัน" + steer "เหมือนรีวิว tech นิดๆ แต่เป็นสไตล์ adduckivity")
FORM: TECH v2 — first-look review มุม automation ที่อ่านสถานะจริงจาก DB ก่อน แล้วเทียบกับความสามารถที่ docs บอก + use cases ผูกของจริงบนเครื่อง
REGISTER: TECH — เลขอารบิก form-legitimate, ชื่อฟีเจอร์/path ในเนื้อได้, พร 1, เรา = มุมผู้ใช้
RESEARCH: research/rakazo-automation-research.md (verified 2026-11-19)
FACT LEDGER (ยืนยันจากเครื่อง 2026-11-19, query Postgres): (1) routines = 9 — ทุกตัวมี cron 1 แถว, webhookEnabled=false, githubEnabled=false, watch=NULL, messageProvider=NULL, emailSenders=NULL ทั้ง 9 → ทริกเกอร์ที่เคยใช้ = schedule อย่างเดียว (2) ทุกตัว active=false แต่ lastRunAt มีค่าทุกตัว = เคยรันแล้วปิดหมด — ลักษณะการใช้ = ตัวจับเวลาตรวจงานชั่วคราว (ตรวจงานซ้ำ/ตรวจ pipeline/dispatch บรีฟ/เช็คส่งมอบ) (3) runs รวม 270 = chat 261 + routine 9 (4) chat_groups = 4, agent_skills = 1, computers = 1, memory_documents = 9, bots 8 ตัว (5) /mnt/inbox = mount จริงแบบอ่าน-เขียนบน computer ของบอต (ตรวจแล้ว 16 พ.ย.)
VENDOR CLAIMS (reported speech เท่านั้น): docs/routines.md (ดึง 2026-11-19) — ทริกเกอร์ 5 แบบ: schedule รับ cron / watch เช็คไฟล์-โฟลเดอร์-output คำสั่ง-tool ของแอปที่ต่อ ทุก 5 นาทีถึง 1 วัน (ใช้คู่ schedule ไม่ได้) / webhook = URL+key รับ POST จากบริการใดก็ได้ / Git event = GitHub webhook จุดจาก push-issue-PR / email = บอตมีที่อยู่เมลเอง ต้องเปิดรับเมลฝั่ง server ก่อน · run ที่จุดจาก webhook-email-Slack อยู่ใต้ approval mode — card อนุมัติหมดอายุ 30 นาที ไม่มีคนกด action ไม่เกิด · routine มีโมเดล+thinking ของตัวเองได้ · docs/groups.md: group 2-10 บอต, @mention, บอตส่งงานถึงบอต, subagents รายงานกลับเป็น card · docs/skills.md: "save that as a skill" + Teach a task (ทำให้ดูครั้งเดียว → draft skill → test → Add to routine) · docs/pages.md: บอตสร้าง dashboard และ routine อัปเดตหน้าเดิมต่อได้
SIBLING GUARD: #121 rakazo-local-docker-first-days (published) — คำ guard = 0: 403, cherry-pick, egress, RAM 2GB, compose up, 5.2GB, YouTube Library, token, 5173; ไม่รีเลย์เรื่องติดตั้ง/push; sibling อีกตัว (#122 app-connections — เขียนพร้อมกัน) — axis แยก = กลไกจุดงานเอง + use case vs แผนที่ช่องทางเชื่อมต่อ; ช่องทาง integration (catalog/messaging) แตะได้แค่ 1 ประโยคเป็นเงื่อนไขของ trigger — คำ Gmail/Linear/Telegram/Slack/MCP ในเนื้อ = 0 (ยกเว้นชื่อ folder /mnt/inbox + Git event ซึ่งเป็นฟีเจอร์ automation)
GUARDS (วัดจริงรอบสุดท้าย): พร 1 real (ส่งสรุปมาให้พร) / FP พร-lookalike ×1 (พร้อม — "สองอันพร้อมใช้ทันที" declared lesson 5) / เรา 2 real (body + closer) / คุณ-ผม-คับ-ฉัน 0 / sibling guard terms 0 (battery CUT 14 terms all-zero PASS) / odd codepoints form-legitimate (TECH): '/' ×6 (path /mnt/inbox + push/PR) + ',' ×1 + '@' ×1 (@mention)
SECRET HYGIENE: ไม่มีค่าจาก .env, ไม่มีชื่อบอตจริง, ไม่มีชื่อ routine จริง (เล่าหน้าที่ class-level), ไม่มี hostname
Notion: POST ใหม่ Content Drafts DB หลัง battery PASS | Status draft รอ Benz r1
-->

# บอต 8 ตัวรันงานไปแล้ว 270 รอบ — automation ที่ใช้จริงมีทริกเกอร์เดียว

### ฐานข้อมูลของเซิร์ฟเวอร์จริง 19 พ.ย. — 9 routine ที่เคยตั้งปิดหมดแล้ว และทั้ง 9 จุดด้วยตารางเวลาเท่านั้น

.

## อ่านสถานะจริงจากฐานข้อมูลก่อน

ระบบมี routine ค้างอยู่ 9 ตัว — ทุกตัวเคยรันงานจริง และตอนนี้ปิดทั้งหมด ไม่มีตัวไหนเปิดค้าง

ลักษณะที่ใช้จริงไม่ใช่ตารางเวลาประจำ แต่เป็นตัวจับเวลาชั่วคราวที่ตั้งทำงานกลางวันทำงาน — ตั้งให้ตรวจงานซ้ำอีกรอบ ตรวจ pipeline สามขั้น ยิงบรีฟไปหาบอตตัวอื่น เช็คว่างานถึงมือคนรับหรือยัง จบงานก็ปิด

ตัวเลขรวมบอกอะไรตรง ๆ — run ทั้งหมด 270 รอบ ผ่านแชต 261 ผ่าน routine 9 งานที่ระบบเริ่มเองโดยไม่มีใครสั่ง มีราวสามเปอร์เซ็นต์

.

## เอกสารระบุว่าจุดงานเองได้ห้าทาง

ทริกเกอร์ตามเอกสารของทีมผู้ทำมีห้าแบบ — ตารางเวลาที่รับ cron expression ได้ / watch ที่จับการเปลี่ยนของไฟล์ โฟลเดอร์ output คำสั่ง หรือ tool ของแอปที่ต่อ เช็คตั้งแต่ทุก 5 นาทีถึงวันละครั้ง / webhook ที่รับ POST จากบริการใดก็ได้ / Git event ที่จุดจาก push, issue และ pull request / email ที่บอตมีที่อยู่เมลของตัวเอง

ห้าทางนี้บนเครื่องเราใช้จริงแล้วทางเดียว — อีกสี่ทางยังไม่เคยถูกตั้งค่า และสองทางจากสี่นั้นต้องเปิดช่องทางฝั่ง server ก่อนถึงจุดรันได้

กติกาด้านความปลอดภัยที่ทีมผู้ทำระบุสมควรจดไว้ — run ที่จุดจากของภายนอกอยู่ใต้ approval mode การอนุมัติหมดอายุใน 30 นาที ถ้าไม่มีใครกด งานไม่เกิด

อีกจุดที่เอกสารบอกคือ routine แต่ละตัวเลือกโมเดลและระดับการคิดของตัวเองได้ — งานง่ายใช้ตัวถูก งานยากใช้ตัวคิดลึก

.

## นอกจากตารางเวลา — ทีมงานและการสอนงาน

group chat รับบอตได้ 2 ถึง 10 ตัว — @mention ปลุกรายตัว บอตส่งงานถึงบอตได้ และบอตตัวใหญ่แตกงานเป็น subagent ทำขนานกันแล้วรายงานกลับเป็น card บนแชต

Teach a task คือการสอนด้วยการทำให้ดู — เปิดหน้าจอบอต ทำงานให้มันดูครั้งเดียว มันเขียนขั้นตอนเป็น skill ให้ทดสอบก่อน แล้วเอาไปติดตารางต่อได้ บนเครื่องนี้มี skill แล้วหนึ่งตัว เป็นของบอตสายเขียน

ส่วน pages คือ dashboard ที่บอตสร้างจากคำสั่งในแชต และ routine ตัวไหนดูแลมัน ก็แก้หน้าเดิมต่อได้เรื่อย ๆ ไม่ต้องสร้างใหม่ทุกครั้ง

.

## use case ที่ลองได้เร็วที่สุดบนเครื่องนี้

อันแรกคือ watch โฟลเดอร์รับส่งงาน — folder /mnt/inbox คือ mount จริงที่บอตเห็นแบบอ่าน-เขียน ตั้ง watch ไว้แล้วพอมีไฟล์ใหม่โผล่ บอตทำงานต่อทันทีโดยไม่ต้องมีใครสั่ง

อันที่สองคือ Git event — repo ที่บอตดูแลมี push หรือ pull request เข้ามา บอตสรุปความเปลี่ยนแปลงกลับมาให้ฟังเอง

อันที่สามคือ routine แบบ habit ที่ไม่ปิดหลังงานจบ — เช้าวันจันทร์รวมงานค้างทุกบอตส่งสรุปมาให้พรที่เดียว ต่างจาก 9 ตัวเดิมที่ตั้งใช้ครั้งเดียวแล้วเลิก

.

## #สรุปแบบวิศวกรเป็ด

ใช้จริงแล้วหนึ่งจากห้าทริกเกอร์ — ตารางเวลาแบบตั้งครั้งเดียวทิ้ง

อีกสี่ทริกเกอร์ สองอันพร้อมใช้ทันที สองอันรอช่องทางฝั่ง server

automation เริ่มจริงเมื่องานมาถึงเอง ไม่ใช่เราไปเรียกมันทุกครั้ง

.

#Adduckivity #DuckOS #NeuroDivergent #SelfHosted #AIAgent #Automation
