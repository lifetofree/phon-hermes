# ROUND RECORD (provisional — inline chat paste, transcribed; no paste file) — pair #123 reposition round 2026-11-19

Source: owner paste ในแชต (document: "REVERSE ENGINEERING & SKILL EXTRACTION — Case Study: Rakazo Automation / AI Team Article") — ผลิตจากบทสนทนา owner × Benz DNA หลัง draft #123 (20261119-cnt-rakazo-automation-use-cases) — transcribed verbatim สำหรับ Part 1/4 (เนื้อหา operative ของรอบ), Parts 2-5 (ข้อเสนอ skill ใหม่ทั้งชุด) = structured summary + สถานะการตัดสินใจ (owner directive: "ไม่ต้องเอาทั้งหมดมาแทนที่ skill ที่เรามี — วิเคราะห์เรียนรู้แล้วเอามาปรับปรุง skill ของเรา" → fold เป็น 439-442 + round-type ใน critique-cycle แทนการสร้าง skill ใหม่)

## MACHINE VERIFICATION ที่รันแล้ว (2026-11-19 หลัง paste)
- bots: **9 ตัว as-of 12:42 วันนี้** (Design Keeper สร้าง 12:42 — เอกสารเขียน 8 ตัว = ถูกตามเวลาสนทนา, ledger ต้องมี as-of date; roster: Chief 09:37 / Idea Keeper 10:22 / Research Distiller 10:29 / Research Scout 10:34 / Adduck Writer 11:35 / Stall Watcher 16:57 / Product Lead 03:12 18 พ.ย. / Book Keeper 18 พ.ย. / Design Keeper 19 พ.ย.)
- **"Add Dark Writer" ในตาราง role = STT garble ของ "Adduck Writer"** (lesson 53 class — ชื่อที่ query ได้ต้องเช็คกับ roster จริง)
- 3.3% ✓ (9/270 = 3.33%)
- หลักฐานเครื่องสนับสนุน workflow ที่ owner เล่า (จากชื่อ routine จริง): "ตรวจ pipeline ice-bath (Scout→AW→draft)" / "ยิงบรีฟ SLT revert+apply ให้ AW (ช่องทาง dispatch พังชั่วคราว)" / "ยิงบรีฟ Body คั่น 14 หน้า (คำสั่ง Phon 10:04) ให้ PL + ปิดจุดค้าง ping 09:41" / "เช็ค mockup PL + re-verify" / "เช็คส่งมอบบท AW (e-book Rakazo)" — = dispatch, PL re-verification, human command, e-book deliverable ล้วนมีร่องรอยจริงในระบบ
- runs 270 = chat 261 + routine 9 ยืนยันซ้ำ ✓

## PART 1 — 8 CHANGES (verbatim core)
Change 1 (270 runs): 270 = จำนวนประวัติการรัน ไม่ใช่จำนวนงาน 270 งาน; routine runs 9 ไม่ได้แปลว่า automation ทั้งหมดมี 9 ครั้ง เพราะมีการส่งต่องานระหว่างบอตในรูปแบบอื่น → เก็บ 270/261/9 ไว้แต่ demote เป็นหลักฐานประกอบ ไม่ใช่ข้อสรุปหลัก
Change 2 (AI Team workflow): ข้อมูลใหม่จากผู้ใช้ — Chief กระจายงานให้ทีม + ตัวอย่าง E-book (Chief ออกแบบ→กระจายงาน→ผลส่งกลับมนุษย์ตรวจอนุมัติ) → เพิ่ม AI Team Workflow + E-book case study เป็นกรณีศึกษาหลัก; "ห้ามยึดโครงสร้างเดิมเพียงเพราะเริ่มเขียนไปแล้ว"
Change 3 (roles): Chief = กระจายงาน+คุมภาพรวม / Idea Keeper = รับ-เก็บ-ส่งต่อไอเดีย / Research Scout = ค้นคว้า / Adduck Writer = เขียน (ต้นฉบับ garble "Add Dark Writer") / Product Lead = ออกแบบผลิตภัณฑ์+ตรวจทาน — 8 ตัว (ตอนสนทนา) แต่ระบุหน้าที่ไว้บางตัว → "ไม่ควรสร้างหน้าที่ให้บอตที่ยังไม่มีข้อมูลรองรับ" + "รักษาชื่อเฉพาะของ Bot ตามข้อมูลต้นทาง"
Change 4 (Chief mental model): "Chief คุม Flow แต่ไม่ต้องผ่านทุกงาน" — Chief = Workflow Orchestrator ไม่ใช่ Universal Pass-through; บอตส่งงานต่อถึงกันได้ตรง ๆ เมื่อเส้นทางชัด; Chief เข้ามาเมื่อต้องประสานภาพรวม/มีจุดตัดสินใจ; "ต้องเปลี่ยนโมเดลความคิดของบทความ ไม่ใช่เพียงเติมข้อความอธิบายเข้าไป"
Change 5 (Chief ≠ Product Lead): Chief = คุมภาพรวม+เส้นทาง / Product Lead = ตรวจทานตามขอบเขตหน้าที่ (ตรวจ research → ส่ง Writer → รับกลับ → ตรวจงานเขียน → ส่ง Chief) / Human = กำหนดเป้าหมาย+อนุมัติ; "อย่ารวมหน้าที่ของ Agent หลายตัวเข้าด้วยกันเพียงเพื่อให้เรื่องเล่าง่ายขึ้น — ความง่ายในการเขียนต้องไม่ทำให้ Architecture ผิดไปจากความจริง"
Change 6 (workflow scope): E-book chain Human→Chief→Research Scout→Product Lead→Writer→Product Lead→Chief→Human Approval = เส้นทางของตัวอย่างนี้เท่านั้น ไม่ใช่กฎทุกงาน — บางงานส่งตรง / บางงานกลับ Chief / บางงานผ่าน PL / บางงานต้องกลับมนุษย์ / บางงานเดินต่อได้ไม่รอมนุษย์; "อย่าเปลี่ยนตัวอย่างหนึ่งให้กลายเป็นกฎของระบบทั้งหมด"
Change 7 (Trigger ≠ Orchestration): Trigger = จุดเริ่ม (schedule/watch/webhook/git/email ตามเอกสาร) / Chief = ควบคุม workflow หลังเริ่ม; "การมี Trigger ไม่ได้หมายความว่าระบบมี Orchestration ที่ดีโดยอัตโนมัติ"
Change 8 (Human-directed): ปัจจุบันมนุษย์ส่งโจทย์ให้ Chief เป็นหลัก + อนุมัติจุดตัดสินใจ → เรียกสถานะนี้ว่า **Human-directed Automation**; watch/git-event/webhook เริ่ม workflow แล้วส่ง Chief พิจารณา = แนวทางอนาคตที่ยังต้องทดลอง ไม่ใช่ใช้จริง; "ห้ามใช้คำว่า Autonomous หากยังมีมนุษย์เป็นผู้เริ่มงานหลัก"

## เพิ่ม/ลด/ย้าย/ตัด (verbatim core)
เพิ่ม: Chief Bot / Bot Roles / E-book Case Study / Bot-to-Bot Handoff / Product Lead Review / Human Approval / Human-directed Automation / Future Autonomous Trigger (แสดงทิศทางโดยไม่อ้างว่าใช้แล้ว)
ลดน้ำหนัก: Routine+Trigger (จากประเด็นหลัก → ส่วนหนึ่งของภาพรวม), Group Chat/Teach a task/Pages (ฟีเจอร์สนับสนุน), 270 runs (เก็บในบทนำ ไม่ใช้เป็นหลักฐาน success)
ไม่กล่าวอ้าง (10 ข้อ): 270 runs ≠ 270 tasks; ≠ autonomous ทั้งหมด; routine 9 ≠ automation มี 9 ครั้ง; Chief ไม่ผ่านทุกงาน; Chief ไม่ตรวจทุกขั้น; PL ไม่ได้ตรวจทุกงานในระบบ; บอตทั้ง 8 ไม่ได้ร่วม e-book workflow หากไม่มีข้อมูล; trigger 5 แบบยังไม่เปิดใช้; autonomous ยังไม่สมบูรณ์; future possibility ไม่ใช่ actual capability — "สิ่งที่ถูกตัดไม่จำเป็นต้องผิด แต่เป็นข้อมูลที่ยังไม่มีหลักฐานพอ หรือไม่จำเป็นต่อแก่น"

## REPOSITION (verbatim)
ก่อน: automation ใช้จริงมี trigger แบบไหน + routine ทำงานอย่างไร
หลัง: มนุษย์ส่งโจทย์ให้ Chief แล้ว AI แต่ละตัวรับผิดชอบงานและส่งต่อกันอย่างไร โดย Chief ควบคุมภาพรวม และมนุษย์เข้ามาตัดสินใจในจุดที่จำเป็น
ชื่อใหม่ (Benz เสนอ): **"คนสั่งงานครั้งเดียว — แล้ว AI ทั้งทีมทำงานต่อกันอย่างไร?"**
Subtitle ใหม่: "เบื้องหลัง Chief Bot ที่ควบคุม Workflow ของทีม AI ตั้งแต่การแบ่งงาน การส่งต่องาน ไปจนถึงจุดที่ต้องให้มนุษย์อนุมัติ"
แก่นใหม่: การสร้าง AI Team ไม่ใช่การเพิ่มจำนวนบอต แต่คือการออกแบบหน้าที่ เส้นทางการส่งต่องาน และจุดตัดสินใจให้ชัดเจน

## PART 2-5 (summary — สถานะ: ไม่รับทั้งชุด)
Part 2 ข้อเสนอ skill ใหม่ "OPB Article Reverse Engineering & Editorial Intelligence" (8 stages Extract/Detect/Challenge/Reconstruct/Reposition/Restructure/Rewrite/Final Audit + behavior rules + patterns + expected output 9 ชิ้น) — **owner directive: ไม่แทนที่ skill เดิม; วิเคราะห์แล้ว fold ของที่ไม่ซ้ำ**: stages ทับซ้อนกับ intake→verify→gate→rebuild ของ content-critique-cycle อยู่แล้ว; ของใหม่จริง = reposition-round shape + deliverable order → fold 443 ใน critique-cycle; Part 4 patterns ที่ไม่ซ้ำ → folds 439-442 ใน content-pipeline; ข้อควรระวังที่ปฏิเสธ: ตาราง role ในเอกสารใช้ชื่อ garble ("Add Dark Writer") — ตัวเอกสารก็ต้องผ่าน name-check กับแหล่งจริงก่อนเชื่อ

## REWRITE DIRECTION (pending owner approval ตาม Stage 7 ของเอกสารเอง "เมื่อผู้ใช้อนุมัติทิศทางแล้วจึงเขียนใหม่")
- #123 rewrite: thesis ใหม่ตาม reposition + title/subtitle ที่ Benz เสนอ + fact ledger ใหม่ (roles attested 5 จาก 9, e-book case owner-attested + machine traces, 270/261/9 = supporting evidence, Human-directed label, roster as-of date)
- ยังไม่ได้สั่ง rewrite — รอ owner go
