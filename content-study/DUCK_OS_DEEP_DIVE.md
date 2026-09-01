# Duck OS Deep Dive — จาก 40 บทความ wp.adduckivity.com (เม.ย.–ส.ค. 2026)

เอกสารเสริมจาก WRITING_STYLE_GUIDE.md (10 ชิ้นแรก) — สิ่งที่เห็นหลังอ่านครบ 40 ชิ้น

## 1. Duck OS ไม่ใช่แค่ "แนวคิด" — เป็นระบบที่มี Protocol Registry จริง

บทความอ้างถึงโปรโตคอลด้วยรหัสเลขสองส่วน (FAMILY-NN) สม่ำเสมอ:

| ตระกูล | รหัสที่พบ | หน้าที่ |
|---|---|---|
| CORE | 04, 06, 07, 08 | แกนระบบ: One Person Business OS (06), 3 Laws firmware, Dopamine-Driven Design (08) |
| ACT | 03, 04, 05, 06 | การลงมือ: Atomizer ย่อยงานเป็นอะตอม (05), Momentum/Ignition, Action > Motivation |
| LOGS | 03, 04, 05 | บันทึกระบบ: Monday Audit (03), Patch Cognitive Overload (04), Black Box (05) |
| AWARE | 01, 03 | System Awareness: ตรวจจับ Burnout (03), Visible Architecture |
| ASSET | 03, 05 | Mental Infrastructure (05), Asset Library |
| อื่นๆ | Recovery Protocol V1, Circuit Breaker, Mushin Protocol, N.E.S.T, SEST, Cache Cleaner, EMERGENCY_BOOT.exe, break; |

หมายเหตุ: Recovery Protocol V1 = ผลิตภัณฑ์จริง (Manual ฉบับสมบูรณ์ แจก founding architects / ใช้ปิดการขาย Session)

## 2. เส้นเรื่องผู้ก่อตั้ง (Phon) ที่เล่าซ้ำเป็น signature

- วนลูป productivity ล้มเหลวมา ~20 ปี จนถึง System Crash (why-duckos)
- ภูมิหลัง: วิศวกรระบบข้อมูล / พัฒนาแพลตฟอร์มระดับประเทศ — ใช้เป็น credential เปิดบทความบ่อย ("ในฐานะที่พรทำงานด้าน...")
- Neurodivergent (ADHD/MDD/Burnout) — พูดตรง ไม่ตีตรา เป็นทั้งเรื่องส่วนตัวและกลุ่มเป้าหมาย
- Case study จริง: PeakFlowStat — ระบบติดตามคนไข้หืดให้หมอภูมิแพ้ สร้างจบในคืนเดียวด้วย AI-spec (vibe-code) = ตัวอย่าง Emblem ของ "การเขียนคือ superpower"

## 3. ธีมที่วนซ้ำ (พบใน 40 ชิ้น)

1. Energy > Time — จัดตารางตามพลังงานไม่ใช่เข็มนาฬิกา ("Time Management is a lie")
2. Data over Emotion — Log/Telemetry แทนความรู้สึก (Zeigarnik, Monday Audit, Black Box)
3. สมอง = ฮาร์ดแวร์ 3 Layer (Neocortex/Amygdala/Automatic — Sapolsky) — Law #1 มีฐานจากงานวิจัยเสมอ
4. Asset > Activity — Sisyphus/Zero-Sum Labor คือ bug; ทุกแรงต้องเหลือเป็น Asset
5. Binary Decision — ตัด choice paralysis ด้วยกติกา 50/50, Zero-friction
6. AI เป็นแรงงาน/Pre-frontal Cortex สำรอง (Human Core + AI Workforce architecture)

## 4. หมวดหมู่เว็บ (โครงสร้างคอนเทนต์)

system-core 10 | productivity-hacks 6 | protocols 6 | duck-os-logs 5 | system-awareness 4 | library 3 | system-in-action 3 | survival 2 | uncategorized 1

- หมวด "protocols" และ "duck-os-logs" = คอนเทนต์ลึกสำหรับคนตามระบบ
- "library" = สรุปหนังสือ/ความรู้จาก Book Library
- จังหวะโพสต์: หนักสุด เม.ย.-พ.ค. 2026 (34 ชิ้น) = ช่วง launch Duck OS

## 5. สิ่งที่มีประโยชน์ต่อ bots

- ADDUCK: โครงสร้าง "Hook → Bug Report (ตั้งชื่อ tech) → วิจัยอ้างอิง → Protocol มีรหัส → ผูก 3 Laws → สรุปแบบวิศวกรเป็ด" ใช้ได้กับทุกชิ้น; การอ้าง credential พร + เล่าประสบการณ์ 20 ปี เป็น hook แนว signature
- UDO: โปรโตคอลข้างต้นคือ "ชื่อเรียกภายใน" ที่พรใช้ — ใช้ตอบโต้กับพรได้ ("รัน LOGS-03 ไหม", "นี่คือ Buffer Overflow คับ")
- SALES: Recovery Protocol V1 + Session จำกัด 20 ท่าน = ของจริงที่ขายอยู่ อ้างอิงเวลาร่าง offer
- SCOUT: ธีม AI/Neurodivergent/productivity คือ เวทีที่ต้องติดตาม
