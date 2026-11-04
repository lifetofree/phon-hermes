---
type: research
topic: Pegasus spyware — zero-click, selection, system-side fix
used_by: []
---

# Pegasus spyware — research (2026-11-04, สำหรับ draft news-event single)

## ข้อเท็จจริงที่ใช้ได้ (verify ข้าม ≥3 แหล่งแล้ว)

### 1. กลไก zero-click (FORCEDENTRY)
- NSO Group (บริษัท cyber-arms อิสราเอล ก่อตั้ง 2010) ทำสปายแวร์ Pegasus ติดตั้งเงียบ ๆ ระยะไกลบน iOS/Android ขายให้รัฐบาลโดยตลาดว่าใช้ต่ออาชญากร/ผู้ก่อการร้าย — แต่ถูกใช้เฝ้าดูนักหนังสือพิมพ์ ทนาย นักกิจกรรม (Wikipedia + Britannica + European Parliament)
- Zero-click = ไม่ต้องมี action จากเจ้าของเครื่อง: ติดผ่านข้อความ/สาย; ลบข้อความหรือไม่รับก็ติด (Britannica)
- FORCEDENTRY = zero-click exploit จับได้ในเครื่องจริง (in the wild) ประกาศโดย Citizen Lab 2021-09-13 จากเครื่องนักกิจกรรมซาอุฯ — โจมตี iMessage/ไลบรารีเรนเดอร์รูปของ Apple ผ่าน BlastDoor ของ iOS 14 ด้วย; ใช้ได้กับ iOS/macOS/WatchOS (Citizen Lab + Wikipedia FORCEDENTRY)

### 2. ขนาดของการเลือกเป้า (Pegasus Project, ก.ค. 2021)
- สื่อ 17 องค์กร 10 ประเทศ นักข่าว 80+ คน ประสานโดย Forbidden Stories + พิสูจน์โดย Amnesty Security Lab
- หมายเลขโทรศัพท์ 50,000+ **ในระบบเลือกเป้าหมาย** (potential targets — ไม่ใช่จำนวนเครื่องติดยืนยัน) — มีนักหนังสือพิมพ์ นักกิจกรรม นักการเมืองฝ่ายค้าน ผู้นำประเทศ ครอบครัว Khashoggi (Amnesty + OCCRP + Wikipedia)
- NSO ไม่เปิดเผยรายชื่อลูกค้า; รายงานปี 2021: ~40 ประเทศมีสิทธิ์เข้าถึง, เป้าหมายใน 50+ ประเทศ (Britannica)

### 3. เคสไทย (GeckoSpy — Citizen Lab + iLaw + DigitalReach, 18 ก.ค. 2022)
- คนไทย **อย่างน้อยสามสิบคน** ยืนยันติด Pegasus ด้วยหลักฐานเชิงนิติวิทยาศาสตร์ (forensic) ช่วง ต.ค. 2020 – พ.ย. 2021 — นักกิจกรรม (FreeYOUTH/UFTD/WEVO), ทนาย (Arnon Nampa โดน 5 ครั้ง เจาะครั้งแรกหลังตั้งข้อกล่าว 112 เพียงไม่กี่วัน), นักวิชาการ, NGO, แม้ผู้บริจาค/ผู้สนับสนุน (Inthira Charoenpura) (Citizen Lab + Reuters + AP + iLaw — 4 แหล่ง)
- จุดติดไฟสืบสวน: Apple แจ้งเตือนผู้ใช้ไทยที่ถูก "state-sponsored attackers" ในเดือน พ.ย. 2021
- รูปแบบการเลือก: เจาะซ้ำหลายครั้งตรงช่วงกิจกรรม (Jutatip เจาะ 6 ครั้ง; ครั้งหนึ่ง 2 วันก่อนชุมนุม 20 มี.ค. 2021); คนในวงการเดียวกันบางส่วนตรวจแล้ว **ไม่ถูกโจมตี** (Amnesty International Thailand / TLHR) — iLaw สรุป: เลือกเป้ารายบุคคล ไม่ใช่ mass surveillance
- State attribution: Citizen Lab เขียนว่า "หลักฐานโดยรอบชี้ว่า หนึ่งหรือหลายส่วนของรัฐไทยอาจรับผิดชอบ" — **circumstantial/low-confidence → ห้ามยกเป็นข้อเท็จจริงในบท** (lesson 51 CUT)

### 4. ช่องถูกปิดที่ฝั่งระบบ
- Apple ออกแพตช์ปิด FORCEDENTRY เดือน ก.ย. 2021 (Citizen Lab report + Wikipedia)
- ปี 2026 เจอการใช้ exploit ตระกูลเดียวกันในเซอร์เบียเทียบนักศึกษา (ก.ย. 2026, Citizen Lab+Amnesty) — exploit เชื่อว่าถูกปิดตั้งแต่ iOS 18.4.1 (เม.ย. 2025) → ประเด็น "ระบบปิด-ระบบเปิดใหม่" ยังวน (infosecurity-magazine + thehackernews)

## Parked (ไม่ใส่ draft รอบนี้ — กิ่ง)
- WhatsApp ฟ้อง NSO ชนะ: คณะลูกขุนสั่งจ่าย ~168 ล้านดอลลาร์ (compensatory ~$444,719 + punitive $167.25M) จากการเจาะผู้ใช้ WhatsApp 1,400 ราย — เทศกาล accountability (cybersecuritynews + courthousenews + accessnow; พิสูจน์วันที่ exact ก่อนใช้ — รายงานระบุ "Tuesday", คดี 6 ปีจากปี 2019 = คำพิพากษา 2025)
- Khashoggi chain (โทรศัพท์ภรรยาถูกติดก่อนฆาตกรรม), El Chapo — มุม power-over-individual
- เซอร์เบีย 2026 — มุม "ยังไม่จบ" / cat-and-mouse

## มุมที่เลือกสำหรับ draft (ONE lens)
**เหยื่อไม่ได้ทำอะไรผิด — เครื่องถูกเลือก ไม่ใช่พลาด; ช่องแบบนี้ปิดที่ฝั่งระบบ ไม่ใช่ความระวังของเจ้าของเครื่อง** — ต่อกับปรัชญาบ้าน (ระบบ > วินัย/ความระวัง) และต่างจาก #99 (สิทธิ์ในการสั่ง) ชัดเจน

## SOURCES
- https://citizenlab.ca/research/forcedentry-nso-group-imessage-zero-click-exploit-captured-in-the-wild/
- https://citizenlab.ca/research/geckospy-pegasus-spyware-used-against-thailands-pro-democracy-movement/
- https://en.wikipedia.org/wiki/Pegasus_(spyware) / https://en.wikipedia.org/wiki/FORCEDENTRY
- https://www.britannica.com/topic/Pegasus-spyware
- https://securitylab.amnesty.org/case-study-the-pegasus-project/ / https://www.occrp.org/interactives/project-p
- https://www.reuters.com/technology/pegasus-phone-spyware-used-target-30-thai-activists-cyber-watchdogs-say-2022-07-18/
- https://apnews.com/article/technology-software-spyware-democracy-31b877b0f2d5e725460ad65c60db9e04
- https://www.ilaw.or.th/articles/35057
