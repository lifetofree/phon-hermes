<!--
pair #99 (anthropic-personal-finance) — CURRENT FORM — LEVEL: L3 (believing-wrong-unnoticed: เชื่อว่า "โปร่งใส/ไม่ทำอะไรเอง = ปลอดภัย" — แต่การให้ AI ถือข้อมูลทั้งบัญชีเพื่อตอบคำถามง่าย ๆ คือการเปลี่ยนว่าใครถือข้อมูล)

ORIGIN: owner brief (2026-11-06): "research Anthropic upgrades Claude with new Personal Finance feature แล้วนำข้อมูลที่ได้มา draft content แล้วลง notion"

RESEARCH (primary, 2026-11-05 launch):
- Anthropic official (claude.com/resources): Personal Finance in Claude — connect bank+card ผ่าน Plaid, read-only (ย้าย/จัดการ/ลงทุนไม่ได้), beta สัปดาห์นี้, Pro/Max/Ultra, US only; ตอบภาษาคนจาก balance+transactions, อธิบาย term; ไม่มี ads/sponsored recs; ไม่ขาย card/loan/savings เอง; ตัวอย่าง: "เงินหายไปไหนเดือนนี้" → รวม $4,309.37, ครึ่งหนึ่ง rent+utilities, food $1,024.51 → ไล่เจอ membership renewal → บอก 4 รายการก่อน payday เหลือ $1,393.22; จับ duplicate charges, unexpected fees, bill ที่ไต่ขึ้นทั้งปี; อธิบาย APR + รวม interest ที่จ่ายไป; สร้าง chart/calendar/dashboard ให้ปรับได้
- ข้อมูลที่ Claude เห็น (เฉพาะบัญชีที่เชื่อม): ชื่อธนาคาร, ชื่อ/type account, เลข 4 ตัวท้าย, balance, credit limit, transactions 2 ปี; sign-in ผ่าน Plaid เอง (Claude ไม่เห็นรหัส); แชทใน hub ไม่ถูกใช้ train; unlink ได้ทุกเมื่อ; ไม่ใช่ investment advice; "Claude can make mistakes — ask which transactions are behind a number, check with your bank"
- TechCrunch: Claude = playing catch-up ต่อ ChatGPT (เปิด personal finance เดือน พ.ค. 2026, Pro users, Plaid เหมือนกัน); ต่อจาก Claude for Legal + Claude for Financial Services ที่เปิดก่อนหน้า; จุดขาย = financial companion ไม่ใช่ generic advice
- Reuters: launch ก่อน IPO ที่ตลาดจับตา; ZDNET: "Claude and ChatGPT now offer financial analysis tools" — สนามเดียวกันแล้ว
- เงื่อนตัดเชิงออกแบบ: read-only = Anthropic ตัดความเสี่ยง "AI ทำพลาดกับเงิน" ทิ้ง — เหลือความเสี่ยงเดียวคือ "ใครถือข้อมูล"

SPINE: ข่าวว่า Claude ต่อธนาคารได้แล้ว (reported) → เสียงในหัว: read-only แปลว่าปลอดภัย → อ่านรายละเอียด: สิ่งที่แลกไปคือ balance + 2 ปี transactions ทั้งบัญชี อยู่ในมือคนถือข้อมูลใหม่ → คำถามง่าย ๆ ตอบได้เพราะถือข้อมูลครบ → read-only ปิดความเสี่ยงที่ตีค่าเป็นตัวเงินได้ แต่ไม่ปิดความเสี่ยงที่เป็นเรื่องความเป็นส่วนตัว → เช็คตัวเอง: เรายินดีให้ AI ถือทั้งบัญชีเพื่อตอบ "เงินไปไหน" ไหม → ยังตอบไม่ได้ แต่คำถามที่ถูกต้องเปลี่ยนจาก "มันทำอะไรได้" เป็น "ใครถือข้อมูล"
INSIGHT-ONCE: bold เป็ด dispatch จุดเดียว
EVIDENCE STATUS: no-case class-level (เราล้วน) — ข่าวเป็น reported ("ข่าวว่า", "ว่ากันว่า"), ไม่ตัดสินว่า Anthropic ดี/ชั่ว, ไม่มีชื่อคนจริง; ตัวเลขจากตัวอย่าง official = ที่มาชัด แต่บทนี้ไม่ยกเลข (ไม่จำเป็น)
SIBLING GUARDS: #81 (blind spot = 0), #98 (harness/คู่ = 0), 9router (keyring/ความปลอดภัย key = 0 — อันนั้นเรื่องของที่ถูกขโมย, อันนี้เรื่องข้อมูลที่เราส่งให้ไปเอง); ledger ล่องหน: "ความเสี่ยงสองชนิด" — ไม่เรียกชื่อแนวคิดในบท
CUT LIST (zero-count): พร, คุณ, คับ, ผม, เพราะ, พร้อม, วินัย, feedback, ระบบ, เครื่องมือ, เสมอ, ทุกครั้ง, ความมั่นใจ, IPO, ธุรกิจ, ตลาดหุ้น, ตัวเลข (ยกเว้น 2 ปี / read-only ไม่นับ), ?(ในเนื้อ — dispatch ผ่าน quote ไม่มี ?)
FORMAT: line-per-sentence + จุดขั้น + H2 #สรุปแบบวิศวกรเป็ด + quote bold 1 + closer bold 1 + hashtag tail; ชื่อแบรนด์ Claude/Anthropic/Plaid/ChatGPT ได้ (tech news post ต่างจาก idea post — บ้านเคยทำกับ LM Studio/llama.cpp/Ollama) แต่ไม่ตัดสินแบรนด์
LEVEL: L3 — L-check: บทส่งมอบ "ความเชื่อ read-only = ปลอดภัย ถูกสอบว่าครอบคลุมแค่ความเสี่ยงฝั่งเงิน ไม่ใช่ฝั่งข้อมูล"
Notion: Content Drafts DB 3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520, Platform TECH + general
-->

# Claude ต่อธนาคารได้แล้ว — read-only หมายความว่าปลอดภัยจริงไหม

.

ข่าวว่า Claude เปิด feature ให้ต่อบัญชีธนาคารและบัตรเครดิตแล้ว

ถามเรื่องเงินเป็นภาษาคน มันจะรวมยอด จัดหมวด จับค่ายิงซ้ำ และบิลที่ไต่ขึ้นทั้งปีให้ดู

เสียงแรกในหัวคือ อ่านอย่างเดียว ย้ายเงินไม่ได้ งั้นก็ปลอดภัย

แต่ความสามารถที่จะตอบว่าเงินเดือนนี้ไปไหน มาจากการถือ balance กับรายการย้อนหลังสองปีของทุกบัญชีที่เชื่อมไว้

คำตอบที่ลื่นเวลาถาม มีต้นทุนเป็นข้อมูลที่อยู่กับคนถือใหม่

.

> **read-only ปิดความเสี่ยงที่ตีราคาเป็นเงินได้ แต่ไม่ได้ปิดความเสี่ยงที่เป็นเรื่องส่วนตัว**

.

บัญชีเราสรุปได้จากรายการทั้งหมด แต่เราสรุปไม่ได้เลยว่าข้อมูลชุดนี้จะอยู่ที่ไหนต่อ

ที่ผ่านมาเราถือข้อมูลนี้คนเดียว ตั้งแต่วันที่เปิดบัญชี

วันที่ต่อ AI วันแรก จึงไม่ใช่วันที่เพิ่มตัวช่วย แต่เป็นวันที่ข้อมูลมีคนถือเพิ่ม

คำถามที่เคยถามว่ามันทำอะไรได้ จึงเปลี่ยนเป็นว่าใครถือข้อมูลเรา

เชื่อว่าปลอดภัยได้ ถ้าตอบคำถามนี้ได้ ไม่ใช่เพียงเห็นคำว่า read-only

.

## #สรุปแบบวิศวกรเป็ด

read-only ทำให้ AI แตะเงินไม่ได้ แต่การถือข้อมูลทั้งบัญชีเพื่อตอบคำถามง่าย ๆ คือการแลกที่เงามากกว่าตัวเงิน

**ความปลอดภัยที่เห็นในข่าวคือฝั่งเงิน ฝั่งข้อมูลต้องตัดสินเองหลังปิดโหมดอ่านอย่างเดียว**

#Adduckivity #DuckOS #NeuroDivergent #AI
