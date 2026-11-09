---
type: research
topic: Meta Muse — consumer personal AI agent (pair ใหม่ #108 รอ owner ยืนยันเลข)
used_by: []
---

# Meta เปิดตัว Muse — ตัวช่วยส่วนตัว consumer AI — research 2026-11-09

## ต้นฉบับ (idea brief จาก owner)
- "Meta introduces 'Muse' consumer AI agent [AI] — connects to apps like email and payments, Secure VM for privacy, available web/iOS/Android/WhatsApp"
- Source: https://aipolicydaily.org/archive/daily/2026-09-09/ (ตรวจสอบแล้ว — สรุปจาก TechCrunch ตรงตาม brief ทุกข้อ: US users / connectors email-calendar-payments / Link by Stripe checkout / Muse Spark / connector ผ่าน API+credentials หรือ browser)

## Primary (verify 2026-11-09)
- **About Facebook (newsroom เจ้าตัว)** "Introducing Muse" (8 ก.ย. 2026): personal AI agent "doesn't just answer questions, it actually does the work" / runs on **Muse Secure VM** = VM เฉพาะบุคคลในคลาวด์ บ้านของ agent + ข้อมูล + credentials / **Sentinel agent** แยกขั้นระบบ — ทุก action ที่ออกอินเทอร์เน็ตต้องผ่าน Sentinel ก่อน / Muse ไม่เห็นพาสเวิร์ด+บัตร (secure storage) / **asks before sensitive actions — sending an email, making a purchase** / audit trail ครบทั้งที่ทำและจะทำ / เลือก app+ระดับ access ได้ / disconnect ได้ทุกเมื่อ / opt-out training / ไม่แชร์เข้า ad systems / "forget" ได้ / งานยาวเดินต่อ **after people close the app** แล้วกลับมาเมื่อต้อง approval หรือสิ่งแวดล้อมเปลี่ยน / จ่ายผ่าน **Link by Stripe — single-use card number** (บัตรจริงไม่โผล่) + purchase protections ครั้งแรกของ AI agent / Shop Pay + 1Password coming / Confidential VM (key ถือโดย user เท่านั้น) มาปลายปี / roll out US: iOS, Android, muse.ai (+AI glasses soon), WhatsApp ใช้ได้ / free ส่วนใหญ่ + subscription
- https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- **research.meta.ai "How We Built Safety Into Muse"** (technical primary): "assume the agent may be under attack" / systemd-nspawn cell, root≠host root / Sentinel = sole permission authority สำหรับ connector+network egress / **email connector กรอง one-time token, password-reset link, magic link** (อีเมล = ช่อง reset พาสเวิร์ดทุกเว็บ) / purchase = ตรวจหน้า checkout + human-in-the-loop ทุกครั้ง + single-use card ผูก merchant+จำนวนเงิน+อายุสั้น "even if stolen via prompt injection... not particularly useful"
- https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse

## Secondary (independent outlets)
- **Reuters (8 ก.ย.)**: launch แม้มีข้อกังวลภายใน — **internal tests showed the product stalling and unauthorized exposure of sensitive data** (ชื่อภายใน = Hatch) / centerpiece ของแผน "personal superintelligence" / ต่อยอดรายได้นอกโฆษณา / connectors: email, calendar, payments, health, smart home
- https://www.reuters.com/business/meta-launches-ai-agent-that-can-access-other-apps-send-emails-make-payments-2026-09-08/
- **WIRED (8 ก.ย.)**: สายเก็บตก "built to be private... needs you to trust it" — สาย personal agent ที่มาช้า ต่างตัวด้วยการขาย security ก่อน / ยืนยัน platforms + Stripe Link single-use + free-with-subscription
- https://www.wired.com/story/meta-releases-muse-a-personal-ai-agent-with-privacy-built-into-it/

## เหตุการณ์ต่อเนื่อง (สำคัญ — จุดจบของเส้นทาง "ทำแทนได้ทั่วเว็บ")
- **Amazon ปิด Muse (21 ก.ย. — TechCrunch/The Verge/Forbes/Yahoo):** user Muse ซื้อของบน Amazon.com โดน error — Amazon ระบุ **"never agreed to participate"** / เดือนพ.ย. Amazon เปิดทางซื้อของผ่านตัวช่วงตัวเอง (text-to-shop = **pair #107**) ก่อน holiday season — TechCrunch เชื่อมสองเหตุการณ์นี้เอง ("After blocking Muse, Amazon now lets users text Alexa...")
- https://techcrunch.com/2026/09/21/metas-ai-agent-has-been-blocked-from-using-amazon-com/ · https://www.theverge.com/tech/998078/amazon-blocks-meta-muse-ai-agent-shopping

## มุมที่เลือก (ผ่าน lens สาย adduckivity)
- **DELEGATION → APPROVAL-SEAT (L3 believing-wrong-unnoticed: "มอบงานให้หมด = เราตัดสินใจน้อยลง/งานจบเอง"):** งานยังอยู่ครบ สิ่งที่เปลี่ยน = ตำแหน่งของเรา — เวลาส่วนใหญ่หลุดออกจากขั้นตอน กลับเข้ามาเฉพาะจุดที่ agent หยุดถาม (จุดถามถูกเลือกไว้แล้วโดยดีไซน์: ก่อนส่งเมล ก่อนจ่าย) — เมื่อเจองานเฉพาะตอนถูกดึงกลับ บริบทไม่ได้อยู่ในหัวเรา การตอบ "ตกลง" จึงหนักขึ้น = ทักษะใหม่คืออ่านจุดอนุมัติ (ทำมาถึงไหน / ขออะไร / ยังจำที่มาได้ไหม)
- ตัวเอกฝั่งหลักฐานแน่น = ประกาศเจ้าตัว (งานรู้ตัว: ส่งเมล จอง กรอกฟอร์ม ชำระเงิน) / ฝั่งข้อสังเกต hedge = จุดอนุมัติเป็นดีไซน์ + Reuters internal-test catch + Amazon block เป็นประโยคขอบเขต ไม่พัฒนา (ไม่ลงซื้อของ — sibling #107)

## Parked (กิ่ง stock — ห้ามขึ้นบทแรก ห้าม 2 thesis)
- มุม trust-by-architecture: Sentinel/VM/assume-under-attack = บริษัทตอบคำถามความปลอดภัยด้วยสถาปัตยกรรม ไม่ใช่คำสัญญา (ใกล้ #106 — ต้อง sibling guard ก่อนใช้)
- มุม platform walls: "agent เดินได้ทั่วเว็บ" เจอรั้งแพลตฟอร์ม — Amazon ปิด → เจ้าของร้านสร้าง agent ของตัวเองแทน (ต่อยอด #107 ตรง ๆ — ควรอยู่กิ่ง)
- มุม confidential VM (key ถือโดย user) + "ไม่เข้า ad systems" — trust ระยะยาว
- มุมภายใน: ชื่อ Hatch, internal tests, "let it run unattended — didn't always work out" จาก research.meta.ai

## Sibling guards (ต้อง 0 ทุกสาย)
- #107 amazon-text-shopping (จุดพัก/การซื้อ/ข้อความเดียว/สั่งของ) · #106 gpt6-cyber (ช่องโหว่/แพตช์/ยืนยัน-ช่อง/discovery-speed) · #100 anthropic-personal-finance (ใครถือข้อมูล/ถอนบัญชี/read-only) · #105 specialist models (โมเดลเล็ก/เลือกให้ถูกงาน)

## Discrepancies
- brief ว่า "available across web, iOS, Android, and WhatsApp" — ตรงประกาศ (US ก่อน, AI glasses coming) — เขียน "แอปมือถือ เว็บ WhatsApp" ได้ ไม่ต้องเอ่ย "across"
- "Secure VM to address user privacy concerns" — ตรงประกาศ แต่ Reuters มี catch ด้านเดียวกัน (internal tests) — บทต้อง label ทั้งสองสถานะ
- ข่าวเก่า 2 เดือน (8 ก.ย. → วันนี้ 9 พ.ย.) — บทต้องเปิดด้วย date anchor ไม่ใช่ "เมื่อวาน/ล่าสุด" + เหตุการณ์ Amazon 21 ก.ย. ยืนยันแล้วว่าเกิดจริง (ห้ามเขียนเป็นการคาดเดา)
