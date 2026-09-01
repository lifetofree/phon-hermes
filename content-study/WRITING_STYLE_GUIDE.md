# Phon Writing Style Guide — วิเคราะห์จาก 10 บทความ wp.adduckivity.com

ศึกษาจาก: content-study/posts/ (10 ชิ้นล่าสุด, พ.ค.–ส.ค. 2026)

## สรุปแนวการเขียน (Voice)

"วิศวกรเป็ด" — อธิบายปัญหา/ศาสตร์การทำงาน (productivity, neuroscience, stoicism) ผ่านอุปมาวิศวกรรมซอฟต์แวร์และโครงสร้างระบบ นิ่ง ตรง มีไหวพริบ ไม่อวย ไม่โอ๋

## 2 ประเภทหลักของบทความ

### ประเภท A: System / Mindset Content (คอนเทนต์แกน)
ตัวอย่าง: system-failure-not-lazy, context-switching-hidden-cost, the-black-box-protocol-logs-05, 4-background-apps, brain-runtime-error-404, one-person-business-os-ai

โครงสร้าง:
1. เปิดด้วย Hook — ยกสถานการณ์จริงที่คนอ่านเจอ ("คุณเคยสงสัยมั้ยคับ...", บทสนทนา LINE) แล้วหักมาว่า "คุณกำลังวินิจฉัยโรคผิด"
2. Bug Report / Diagnostic — ตั้งชื่อปัญหาเป็น Error ภาษา tech (System Freeze, Memory Leak, Error 404, Context Switching, Attention Residue) อธิบายผ่านอุปมา: สมอง = CPU/RAM/Server, อารมณ์ = Background App, การพัก = Maintenance
3. อ้างอิงจริง — งานวิจัย/ผู้เชี่ยวชาญ (Sophie Leroy, Sapolsky) และประสบการณ์ตัวเอง ("ในฐานะที่พรทำงานด้านระบบวิศวกรรมข้อมูล...")
4. วิธีแก้เป็น Protocol — ตั้งชื่อโค้ดเล่น (CORE-06, LOGS-05, EMERGENCY_BOOT.exe, break;, Circuit Breaker, Digital Bunker) พร้อมขั้นตอนชัดเจน
5. ผูกกับ Duck OS Laws — Law #1 System > Emotion, Law #2 Asset > Activity, Law #3 Protect System (ทุกบทความจบด้วยการผูกกลับระบบ)
6. ปิดท้ายด้วย "บทสรุปจากพร" / "สรุปแบบวิศวกรเป็ด" + CTA นุ่มๆ (Session/ผลิตภัณฑ์ กระจุกคุณภาพ "จำกัด 20 ท่าน")

หัวข้อกำกับแบบ Debug: "00: Ingestion Phase", "01: The Prefrontal Cortex Server", "02: Diagnostic Logs"

### ประเภท B: Tool Review / How-to (Productivity Hacks)
ตัวอย่าง: rustdesk, tailscale, git-worktree, dependabot

โครงสร้าง:
1. ชื่อเครื่องมือ + เหตุผลที่ต้องใช้ (มุม "ไม่ต้องง้อ X" / "แก้ปัญหา Y แบบขี้เกียจ")
2. มันทำงานยังไง (อธิบายแบบเข้าใจง่าย + ตารางเทียบ component)
3. Features เด่น
4. ข้อดี ✅ / ข้อเสีย ❌ — ตรงไปตรงมา ไม่โฆษณา (Cons ละเอียดพอกับ Pros)
5. เปรียบเทียบคู่แข่งเป็นตาราง + Pricing ปัจจุบัน (ระบุเดือน/ปี)
6. Pro Tips แยกตามระดับผู้ใช้ (มือใหม่/ใช้จริงจัง/องค์กร)
7. สรุปสั้น + hashtags

## Voice & ภาษา (ทุกประเภท)

- สรรพนาม: "พร" ลงท้าย "คับ/ค้าบ/คร้าบ" — กันเอง มีมุก (เช่น "แป๊บเดียวจริงๆ", "โคตรดี")
- อุปมาวิศวกรรมสม่ำเสมอ: RAM, Cache, Server, Reboot, Telemetry, Firmware, Single Source of Truth
- คำยืมอังกฤษใช้ทับศัพท์แล้วอธิบายไทยกำกับ ("Decision Fatigue หรือการต้องตัดสินใจ...")
- ประโยคกลางๆ ยาว 1-3 บรรทัด เล่าเรื่องต่อเนื่อง สลับ bullet เมื่อลงรายละเอียด
- กลุ่มเป้าหมายที่พูดถึงตรงๆ: Neurodivergent (ADHD/MDD/Burnout) — สื่อสารแบบเข้าใจไม่ตีตรา ("คุณไม่ได้ขี้เกียจ แต่เครื่องมันค้าง")
- ตัวเลขจริงเสมอ: 23 นาที, 1 นาที, 20 ท่าน, $5-10/เดือน

## Firewall (สิ่งที่ไม่เคยปรากฏในงานเขียน)

- คำสัญญาเปลี่ยนชีวิต / ปลดล็อกศักยภาพ
- ขยี้ปมเชิงขาย ("แอดเข้าใจความเจ็บปวดคุณ")
- คำปลอบใจ (กอดๆ สู้ๆ) — ใช้ System Words แทน: ระบบ ประคอง ขั้นต่ำ พอรอด คุมได้
- ชื่อยา/อาการป่วยตรงๆ — ใช้ "แบต/พลังงาน/ระบบค้าง" แทน

## Hashtags ประจำ

#Adduckivity #DuckOS #NeuroDivergent + topic tags (ต่อท้ายบทความ)

## ความยาว

- Tool review: 400-900 คำ | System content: 400-650 คำ (เว็บ; กฎ Draft Long Form 2500-3000 คำใช้กับ Core Content ฉบับเต็ม)
