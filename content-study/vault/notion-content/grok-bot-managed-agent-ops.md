# Grok Bot — จ้าง AI ลูกทีมที่มีคอมของตัวเอง เข้า app ทำงานแทนเราได้จริง

**Excerpt:** ความต่างระหว่างงานเสร็จ 90% กับ 100% คือการมีคอมพิวเตอร์เป็นของตัวเอง Grok Bot ย้าย Agent ไปรันบน Cloud VM ตลอด 24 ชั่วโมง แต่ราคาที่ต้องแลกคือ On-demand Meter ที่ไม่มีแคป และสิทธิ์การเข้าถึงข้อมูลที่ต้องคุมไฟร์วอลล์ให้ดี
**Laws:** [[🛡️ Law 3: Protect System]] · [[🛠️ Decision Protocol]]
**Site Category:** [[📚 Asset Library]]
**Tags:** [[Adduckivity]] · [[DuckOS]] · #GrokBot · #xAI · #AITeam · #AgentOps · [[NeuroDivergent]] · #AIWork · [[Productivity]]

---

โลก AI agent ตอนนี้แยกเป็น 2 แบบชัดๆ:
Grok Bot ของ xAI เป็นแบบที่ 2 คับ — ประโยคทางการของ xAI: “Grok Bot is your team of always-on agents. They have their own computer, work inside tools and apps like you do, and keep working 24/7.”
จุดที่สำคัญที่สุด: Bots แชร์คอมเสมือน (managed Linux VM) ใน cloud — งานไม่หยุดเมื่อเราปิดเครื่อง และมันทำงานใน app จริง รวมถึง platform ที่ไม่มี API สวยๆ หรือ MCP ให้ต่อ — ทำใน browser เหมือนคนทำ
ตัวอย่างจริงจากทีมภายใน xAI: Bot ขายอัปเดต CRM จาก call transcript + ร่าง follow-up, Bot ops จัดที่นั่งพนักงานใหม่ + ประมวลผล invoice จาก Gmail, Bot engineering reproduce bug ใน UI จริง → ไฟล์ ticket → ส่งต่อให้ Bot debug
> “There is a huge difference between 90% done and 100% done. Most AI gets you almost there. Grok Bot can finish the swing, because the work lands where a human would put it, in the actual tool.” — Roman, Product (xAI)
.
### Features เด่น
1. Message เหมือนคุยกับเพื่อนร่วมทีม
ไม่ต้อง setup workflow ก่อน — เปิด thread พิมพ์งานส่งไปได้เลย จากมือถือหรือ desktop ใช้ thread เดียวกันต่อได้ทั้งคู่
.
2. รันหลาย Bot พร้อมกัน (แบบมี Chief of Staff)
แนวที่ทีม xAI ใช้จริง: Bot หนึ่งตัวเป็น chief of staff คุมภาพรวม แล้วมี specialist แยก lane — inbox, expenses, recruiting, bug fix — Bot คุยกันเองได้ แชร์ context กันเองใน thread เดียวกัน วางไว้ใน group chat แล้วมันส่งงานต่อกัน แบ่ง ownership กันเอง เราถูกดึงเข้ามาเฉพาะจุดที่ต้องตัดสินใจ
.
3. Teach by demonstration — โชว์ครั้งเดียว ทำต่อเอง
วิธีสอน Bot ที่ดีที่สุดคือพามันดูงานหนึ่งรอบ มันจดทุก step บันทึกเป็น routine รับ correction จากเรา แล้วรันเองรอบต่อไป — ไม่ต้อง re-explain อีก
.
4. เก่งขึ้นตามเวลา
Bot จำ context ว่าเราชอบงานแบบไหน หยิบ edge case แบบเรา รู้ว่าเมื่อไหร่ควร ping หาเรา และเริ่ม proactive — ทำงานก่อนที่เราจะสั่ง ตาม thread ที่เราทิ้งค้าง ดันงานที่ค้างให้คืบหน้า
.
5. ทำงานกับ X ได้แล้ว (อัปเดต 29 ส.ค.) — เชื่อม X connector: ให้ Bot ค้นโพสต์ อ่าน timeline เช็ค mention รวบข่าวจาก X — ผู้ใช้ Grok Bot แบบ paid ได้ X API credits ฟรี
.
6. Jobs ที่คนใช้จริงว่าจ้างทำวันนี้ (จาก xAI):
.
### Pricing — รู้ก่อนเจ็บ
ไม่มี subscription แยกชื่อ “Grok Bot” — มันมาแถมในแผนที่มีอยู่ (อัปเดต 26 ส.ค. 2026):
กลไกค่าใช้จ่าย 4 ชั้น — ตรงนี้สำคัญ อ่านก่อนคิดว่า “แถม” = ฟรี:
Free trial: มีครั้งเดียว — เป็น usage credit ที่หมดตาม agent steps + tokens (ไม่ใช่ตามจำนวนข้อความ) ภายใน 7 วัน — task ยาว task เดียวอาจกินเกือบหมด — เปิด trial ด้วยงานเล็กๆ ที่จบไว แล้วค่อยขยาย
Platform: macOS (Apple Silicon + Intel), Windows (x64/Arm64), iPhone (iOS 18+) — ยังไม่มี Android/iPad/Linux client (คอมของ Bot เป็น Linux VM แต่ไม่มี client ฝั่ง Linux)
เข้าทางไหนดี? — โค้ดอยู่แล้ว = ผ่าน Cursor Pro $20 (ถูกสุด) / อยากได้ Grok chat + Imagine + Voice ด้วย = ผ่าน SuperGrok $30 (แต่จำไว้: linking SuperGrok → Cursor account เป็น แบบถาวร ย้ายคืนไม่ได้)
.
### Pros ✅
### Cons ❌
.
### เทียบกับที่เราเคยพูดถึง
จุดตัดสิน: ถ้างาน sensitive + อยากคุม data เอง = ทาง local/self-host — ถ้างาน ops ที่ต้องเข้า SaaS เยอะๆ และอยากได้ทีมทำงาน 24/7 โดยไม่อยากดูแลเครื่อง = ทาง Grok Bot
.
### เหมาะกับใคร (Pro Tips)
Solo founder / One Person Business — เริ่ม Bot เดียวแบบ chief of staff คุม inbox + calendar + สรุปงานรายวัน — ใช้ Cursor Pro $20 เป็นประตูที่ถูกสุด
ทีมเล็ก 5-15 คน — แยก specialist: inbox manager + refunds manager + meeting stand-in — จัด group chat ให้มันส่งงานกันเอง — อย่าลืมตั้ง account-level on-demand limit ก่อนวันแรก
สาย content/monitoring X — X connector + API credits ฟรี — ให้ Bot รวบ mention/trend แล้วสรุปส่งเข้า inbox
ไม่เหมาะ:
.
### #สรุปแบบวิศวกรเป็ด
Grok Bot = “จ้างพนักงานที่มีคอมของตัวเอง” คับ — ไม่ใช่ chatbot ที่ช่วยคิด แต่คือทีมที่ล็อกอินเข้าระบบจริง ทำงานจนจบ แล้วกลับมาถามเฉพาะจุดตัดสินใจ
exchange ที่ต้องแลก: quota ไม่โปร่งใส + on-demand ไม่มี cap เฉพาะ + เลือก model ไม่ได้ + ยัง beta — แลกกับไม่ต้อง setup workflow, ไม่ต้องดูแลเครื่อง, งานจบใน tool จริง
Duck OS Law #2: Asset > Activity — ถ้า routine ของคุณ repeat ทุกสัปดาห์ การสอน Bot ครั้งเดียวคือ asset ที่ทำงานแทนไปเรื่อยๆ — แต่ต้องเป็น Admin ที่ตั้ง firewall ให้ดี ไม่ใช่ปล่อย meter วิ่งแทนเรา
ลองวันนี้: เปิด Bot → สอนงานที่ทำซ้ำที่สุดในสัปดาห์ → ดู usage ทุกวันเป็นสัปดาห์แรก → ค่อยขยายคับ
.
#Adduckivity #DuckOS #GrokBot #xAI #AITeam #AgentOps #NeuroDivergent #AIWork #Productivity
===========
FB Cover
===========
xAI ปล่อยของใหม่ที่พรว่าเรื่องใหญ่ของปีนี้เลยคับ — Grok Bot
ไม่ใช่ chatbot คับ แต่คือ AI ลูกทีมที่มีคอมของตัวเองใน cloud — มันล็อกอินเข้า Gmail/CRM/Slack ที่เราใช้จริง ทำงานใน browser เหมือนคนทำ แล้วกลับมาหาเราเฉพาะจุดที่ต้องตัดสินใจ ที่เหลือมันทำเอง 24/7
.
ราคา: ไม่มี subscription แยก — แถมในแผน Cursor Pro ($20) / SuperGrok ($30) ขึ้นไป มี weekly usage ของตัวเอง แต่ quota หมดจะเข้า on-demand ที่คิดตาม token (ไม่มี cap เฉพาะตัว Bot — ต้องไปตั้ง limit ที่ account เอง)
.
Cons ตรงๆ: ยัง beta, quota ไม่บอกตัวเลข, เลือก model ไม่ได้, ไม่มี Android, และ Bot ทุกตัวแชร์คอมเดียวกัน (security ระดับ account ไม่ใช่ระดับ Bot)
.
เหมาะกับ: คนที่มี routine ทำซ้ำทุกสัปดาห์ (inbox, refunds, meeting notes) และอยากได้ลูกทีมทำงาน 24/7 โดยไม่อยากดูแลเครื่องเอง
.
#สรุปแบบวิศวกรเป็ด
Duck OS Law: สอน Bot ครั้งเดียว = asset ที่ทำงานแทนไปเรื่อยๆ — แต่ต้องเป็น Admin ที่ตั้ง firewall เอง ไม่ใช่ปล่อย meter วิ่ง
.
อ่านฉบับเต็ม (กลไก 4 ชั้นของค่าใช้จ่าย + งานจริงที่คนใช้ว่าจ้าง + เทียบกับ AutoClaw/OpenClaw) ได้ใน comment นะค้าบ
.
#Adduckivity #DuckOS #GrokBot #xAI #AITeam #AgentOps #Productivity
===========

*Synced: 2026-11-02 19:54 +07 · [Notion](https://www.notion.so/3d9df8d88d8c8039aaaadaed819af690) · ✅ Published*