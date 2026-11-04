---
type: research
topic: blood-bank fridge hack (EFS France) — คลังเลือดถูกสั่งให้ร้อน
used_by: []
---

# Blood-bank hack (EFS France) — research 2026-11-04

## ข้อเท็จจริง (verify ข้าม 6+ แหล่งอิสระ)
- **เหตุการณ์:** คืนวันที่ 1-2 พ.ย. 2026 แฮ็กเกอร์โจมตี **Coolworld** ผู้ให้บริการตู้เย็น/ห้องเย็น (refrigerated containers + maintenance) ของ **EFS (Établissement français du sang)** — สถาบันเลือดแห่งชาติของฝรั่งเศส (AP + cybersecuritynews + indiatoday + undercodenews + ladepeche + 20minutes + generation-nt)
- **พฤติกรรม:** ปรับตั้งอุณหภูมิตู้เก็บพลาสมาจาก ~−30°C → **110°C** (ทุกแหล่งตรงกัน)
- **จับได้อย่างไร:** ช่างประจำ (on-call technician) สังเกตความผิดปกติตอนกลางคืน → ทีมฉุกเฉินเข้าแทรกแซง **ก่อนความเสียหาย** (AP headline "thwarted before damage" + Health Ministry: contained, ไม่กระทบโรงพยาบาล/การถ่ายเลือด; indiatoday + undercodenews ยืนยัน)
- **พื้นที่:** Bourgogne-Franche-Comté (ผ่าน Le Canard enchaîné — รายงานรอง)
- **บริบทเชื่อมโยง:** มาหลังคลื่นโจมตีตู้แช่ซูเปอร์มาร์เก็ตยุโรป (≥11 ประเทศ — indiatoday) — รูปแบบเดียวกัน (โจมตี supplier ไม่ใช่ตัวหน่วยงาน)
- **ผู้ถูกโจมตี = supplier** ไม่ใช่ระบบของ EFS โดยตรง (undercodenews + cybersecuritynews ตรงกัน)

## จุดสำคัญที่ต้องแยกชั้น
1. เป้าโจมตีจริง = บริษัทผู้ให้บริการระบบเย็น (supply chain) ไม่ใช่โรงพยาบาล/EFS โดยตรง
2. ความเสียหาย "ไม่เกิด" เพราะคนเฝ้าสังเกตทัน + เข้าแทรกแซงทัน — **ไม่ใช่เพราะระบบกันเอง** (มนุษย์ on-call คือส่วนของระบบที่จับได้)
3. อุณหภูมิ 110°C = ตั้งได้จากระยะไกลจริง (ความสามารถของระบบ) — ข่าวบางแหล่งเถียงเทคนิคว่า −30→110 จะถึงจริงช้า/แจ้งเตือนไหม — ห้ามตีความเกิน
4. ยังไม่มีการชี้ผู้ก่อเหตุ — ห้าม speculative attribution (lesson 51)

## มุมที่ draft ได้ (candidate lenses)
1. **มนุษย์เฝ้ารอบดึก = ส่วนของระบบ** (ระบบที่ดีไม่ได้แปลว่าไม่ต้องมีคนตื่น) — ต่อสาย OPB ระบบ-ไม่ใช่-ความระวัง แต่เพิ่มมิติ "คนในระบบ"
2. **โจมตีผ่าน supplier** (ความปลอดภัยของเราอยู่ที่คนที่เราจ้างเฝ้าของด้วย) — ต่อ #99 (สิทธิ์สั่ง) ได้
3. **ระบบอนุญาตให้ตั้ง 110°C จากระยะไกลได้เลย** (ความสามารถที่รอให้ใครสักคนใช้) — คล้าย #99
4. **สายเลือด-vs-ตู้แช่**: ของที่เก็บคือเลือดสำหรับคนไข้ — น้ำหนักทางศีลธรรมทำให้ "สั่งได้จากระยะไกล" จับต้องได้
- ทุกมุมต้องต่างจาก #99 (ตู้แช่ = สิทธิ์ในการสั่งระบบ) ให้ชัด — มุม 1 ต่างสุด (บทแม่พูดว่า "ใครมีสิทธิ์สั่ง" บทนี้พูดว่า "ระบบยังต้องมีคนตื่น")

## Parked (ไม่ใช้รอบนี้)
- คลื่นตู้แช่ 11 ประเทศ (เคยใช้แล้วใน #99)
- เถียงเทคนิคเรื่องการแจ้งเตือนอุณหภูมิ
- attribution

## SOURCES
- https://apnews.com/article/france-plasma-blood-bank-cyberattack-temperature-fridge-12b80bcf93b8404264209e519c204919 (AP — "thwarted before damage", Ministry contained)
- https://cybersecuritynews.com/french-blood-plasma-freezers-hacked/ (Coolworld, −30→110)
- https://www.indiatoday.in/technology/news/story/after-supermarket-food-hackers-target-blood-bank-in-france-and-almost-boil-blood-3032162-2026-11-04 (technician overnight, Nov 1-2, 11 ประเทศ)
- https://undercodenews.com/hackers-target-frances-blood-plasma-freezers-in-alarming-refrigeration-system-sabotage-attempt/ (Coolworld scope, Bourgogne-Franche-Comté, Le Canard enchaîné)
- https://www.ladepeche.fr/2026/11/04/... (ฝรั่งเศส)
- https://www.20minutes.fr/societe/4260219-20261104-cyberattaque-30-110-refrigerateurs-don-sang-pirates-tour (ฝรั่งเศส)
- https://www.generation-nt.com/actualites/piratage-installations-frigorifiques-efs-sang-plasma-2083935 (ฝรั่งเศส)
