# v1 Chief draft snapshot — Rakazo x 9Router fallback (the state BEFORE the Benz rule-ledger round)

- Source: Notion Content Drafts `421df8d8-8d8c-81a8-b3bc-ee925e3cc6f1` (created 2026-11-23 05:33Z, last edited 05:55Z — same-day Chief draft ตามคำสั่งพร 12:0x)
- Status at snapshot: draft — page UNTOUCHED by this learn-only round
- Note: the critic read a LATER owner-updated draft (owner experiments added); this v1 is the earlier state kept as quote-verify ground truth
- Topic prop: Rakazo self-host + 9Router — ตั้งค่าโมเดลให้ router ตัดสินใจก่อนยิง · Sources prop: rakazo.com/docs/models, rakazo.com/docs/self-host-models.md, docs.9router.com, 9router.wiki/guides/fallback, npm registry (ตรวจ 23 พ.ย. 2026) · content_id 20261123-cnt-rakazo-9router-model-fallback

===== blocks verbatim =====

# Model โดนลิมิต — ให้ router เลือกปลายทางก่อนยิง (เร็วกว่าเชิงกลไก ยังไม่ได้วัดเวลา)
### 9router v0.5.123 (npm, 23 พ.ย. 2026) — 32,758 ดาวบน GitHub (ตรวจ 23 พ.ย. 2026) — เอกสาร Rakazo เขียนว่าโมเดลหลัก fail หรือชน limit บอทจะย้ายไปตัวสำรอง (ตอนนี้ยังไม่ได้ติดตั้ง 9Router บนเครื่องนี้ และยังไม่ได้วัดเวลาเทียบสองกลไก)
.
วันที่ 20 พฤศจิกายน ทีมบอทของพรยิงงานพร้อมกันจนโดน 429 (กฎที่ทีมเขียนไว้วันนั้นเลยบันทึกไว้ว่า "หลังพบ 429 จาก burst")
งานที่ยิงไปรอบนั้นไม่ได้ผล กฎในทีมเลยต้องเขียนใหม่ให้ยิงพร้อมกันได้ทีละตัว เพราะถ้ายิงพร้อมกันเมื่อโควตาของโมเดลใกล้หมด ผลคือทุกตัวโดน error พร้อมกัน
.
เอกสารของ Rakazo เขียนไว้ตรง ๆ ว่า "if the main model fails or hits a limit, the bot moves to the next one" — ถ้าโมเดลหลัก fail หรือชน limit บอทจะย้ายไปตัวสำรอง (rakazo.com/docs/models, ตรวจ 23 พ.ย. 2026)
นั่นไม่ใช่ข้อบกพร่อง นั่นคือกลไก fallback ที่มีอยู่แล้วในตัว แต่เป็นกลไกที่ตัดสินใจหลังยิง รอบแรกที่โมเดลชน limit คือรอบที่เสียไป
.
พรเลยเปลี่ยนคำถาม จากโมเดลไหนดีที่สุด เป็นว่าเราจะรู้ได้เร็วแค่ไหนว่าโมเดลที่เลือกไว้ใช้ไม่ได้แล้ว แล้วจะเดินไปทางไหนต่อ
เพราะงานที่ค้างรอ error ไม่ได้ค้างฟรี มันคืองานที่รออยู่บนจอโดยไม่มีอะไรมาขยับ และถ้าหลายบอทชนลิมิตพร้อมกัน เราจะเสียเวลารอทีละรอบโดยที่ยังไม่ได้รู้ด้วยซ้ำว่าทำไม
เมื่อโมเดลติดลิมิต เราอยากให้บอทรู้ก่อนยิงว่าจะเดินไปทางไหน หรือยอมให้มันเจอ error ก่อนแล้วค่อยหาทางออก
.
## สองจุดที่ตัดสินใจต่างกัน
Rakazo ตัดสินใจในตัวบอท หลังจากโมเดลหลักตอบไม่ได้ ข้อมูลที่มันมีตอนนั้นคือ error ที่เพิ่งได้รับ
9Router คือ local gateway ที่รับ request แบบ OpenAI-compatible แล้วค่อยเลือกปลายทางเอง ตามเอกสารผู้ผลิต มันมีสถานะโควตาสด นับถอยหลังรีเซ็ต และสลับไปทางอื่นเองเมื่อโควตาหมด (docs.9router.com, ตรวจ 23 พ.ย. 2026)
ต่างกันตรงจังหวะ (ตามที่ผู้ผลิตเขียน) ไม่ใช่ตรงจำนวนโมเดล และต้องพูดตรง ๆ ด้วยว่าคู่มืออิสระของ 9Router เองเตือนว่า "It does not guarantee identical answers, unlimited capacity, or a lower bill" — ไม่รับประกันว่าคำตอบเหมือนกัน ความจุไม่จำกัด หรือบิลจะถูกลง และ route ที่ล้มก็ยังลองตามลำดับหลังเจอ error เหมือนกัน (9router.wiki/guides/fallback, เนื้อหาตรวจ 30 ต.ค. 2026)
ข้อความว่า "ตัดสินใจก่อนยิง" เป็นสิ่งที่เห็นจากฝั่ง router ส่วนคู่มืออิสระเตือนว่าคำตอบที่ได้อาจซ่อนความล้มเหลวของตัวแรกไว้ เราจึงยังบอกไม่ได้ว่าจะเสียเวลาน้อยกว่าเท่าไร
.
## ด่านที่คนส่วนใหญ่จะติดตอนชี้ Rakazo ไปที่ router
เอกสาร Rakazo เขียนว่า private endpoint จะถูกปฏิเสธ "unless MCP_ALLOW_PRIVATE_ENDPOINT=true is set on the API and worker" และย้ำว่าเช็กทั้งตอนบันทึก ตอนค้นหาโมเดล และทุกรอบที่รัน ไม่มีบัญชีไหนข้ามได้ (rakazo.com/docs/self-host-models, ตรวจ 23 พ.ย. 2026)
แปลว่าต้องตั้งค่าใน environment ของทั้ง container API และ worker ไม่ใช่แค่ตัวที่เปิดหน้าเว็บอยู่ ถ้ารันผ่าน Docker Desktop ให้ใช้ host.docker.internal แทน localhost และถ้าเป็น Linux เซิร์ฟเวอร์โมเดลต้องรับการเชื่อมต่อที่ Docker bridge เข้าถึงได้ ไม่ใช่ผูกแค่กับ 127.0.0.1
ตัว router เองติดตั้งด้วย npm install -g 9router แล้วชี้ Rakazo ไปที่ http://localhost:20128/v1 (address ตามเอกสาร 9Router) ตรงนี้คือจุดที่คนส่วนใหญ่ติด เพราะเปิด flag อย่างเดียวแล้วแต่ใส่ address ผิดที่ ระบบก็ยังไม่รู้ว่าจะยิงไปที่ไหน
.
## สองทางที่เลือกได้ตอนนี้
ถ้าอยากได้แค่ไม่พัง เก็บ fallback ในตัว Rakazo ไว้ก็พอ ตั้ง Add fallback ใส่โมเดลสำรองสักตัว งานเดินต่อได้แม้โมเดลหลักชน limit และไม่ต้องแตะตัวแปรระบบใด ๆ
ถ้าอยากไม่ต้องเสียเวลารอบแรกที่โดน limit ย้ายการตัดสินใจไปที่ router คือติดตั้ง 9Router แล้วชี้ Rakazo ไปที่ http://localhost:20128/v1 พร้อมตั้ง MCP_ALLOW_PRIVATE_ENDPOINT=true ให้ทั้ง API และ worker แล้วเก็บ fallback ใน Rakazo ไว้เป็นแผนสำรอง เพราะทั้งสองทางยังตกได้
เรื่องคีย์ที่ตัว router ถือไว้ พรเขียนไปแล้วเมื่อ 30 ส.ค. ถ้าจะต่อไปจริง ควรอ่านบทนั้นก่อน
.
## #สรุปแบบวิศวกรเป็ด
สาระ — Rakazo มี fallback อยู่แล้ว แต่ตัดสินใจหลังโดน error ส่วน 9Router ตัดสินใจก่อนยิงจากสถานะโควตาที่มันติดตามเอง (ตามเอกสารผู้ผลิต)
เงื่อนไข — เร็วกว่าในที่นี้คือเร็วกว่าเชิงกลไก ไม่ใช่ตัวเลขเวลาที่วัดแล้ว เพราะเรายังไม่ได้ติดตั้ง 9Router บนเครื่องนี้ และยังไม่ได้วัดเวลาเทียบสองกลไก
มุมสงเกต — ถ้าอยากได้แค่ไม่พัง เก็บ fallback ในตัว Rakazo ไว้ก็พอ ถ้าอยากไม่เสียเวลารอบแรก ค่อยย้ายการตัดสินใจไปที่ router แล้วเก็บ fallback เดิมไว้เป็นแผนสำรอง
.
#Adduckivity #DuckOS #NeuroDivergent #Rakazo #AIRouter