# Benz-DNA critique — rule-ledger round (learn-only) — Rakazo x 9Router fallback draft

- Date received: 2026-11-23 (owner paste in chat, inline — PROVISIONAL-INLINE class, replace with byte-true file if it surfaces later)
- Owner framing: "คอมเมนต์จาก benz dna สำหรับ draft ล่าสุด"
- Owner directive: "ลองเอาไป reverse engineer, analyze เรียนรู้ learning ทุก ๆ อย่างที่ comment มา แล้วเอาไปปรับปรุง skill writing เพื่อให้เขียนเป็นเหมือนน้ำเสียงของพร ไม่ใช่ ai เขียน ส่วนฉบับ publish ไม่ต้องแก้แล้ว เพราะพรจัดการแก้เรียบร้อยแล้ว เดียวพรส่งไปให้ อันนี้เป็นฉบับที่แก้เรียบร้อยพร้อมขึ้นแล้ว" → LEARN-ONLY round (left-digit precedent): NO draft rewrite, NO Notion touch, NO publish edit.
- Version the critic read: an OWNER-UPDATED draft — the critique's "ก่อน" lines (title "ลองใช้ Rakazo x 9Router (เร็วกว่า fallback ในตัว)", owner experiments: cron ยิงเช็กโควตา, error 4-5 งาน, ยิงทีละตัวก็ยัง error, token หายไปกับตัวงาน, ฉาก "งานเสียไป 5-6 งานพร้อมกัน") do NOT all exist in the Notion v1 (Chief draft). The owner-updated draft text was not pasted to us; the Notion v1 is archived separately as the earlier state (`20261123-rakazo-9router-fallback-v1-chief-notion.md`).
- Pair/content id: 20261123-cnt-rakazo-9router-model-fallback (Notion Content Drafts `421df8d8-8d8c-81a8-b3bc-ee925e3cc6f1`, Status draft — UNTOUCHED this round per learn-only rule)

## Quote-verify + doc re-verification (run by Hermes 23 พ.ย. 2026, curl live pages)

- Quote 1 "if the main model fails or hits a limit, the bot moves to the next one" — **HIT on rakazo.com/docs/models/** (the page the v1 cited for it: "Choose Add fallback to list backup models; if the main model fails or hits a limit, the bot moves to the next one."). Benz's cut cited its absence from rakazo.com/docs/self-host-models — a DIFFERENT page (true: absent there; that page has only approval-model backups). Two bare-domain rakazo citations in one draft invite a critic's wrong-page check.
- Quote 2 "It does not guarantee identical answers, unlimited capacity, or a lower bill" — **HIT on 9router.wiki/guides/fallback/** (the page the v1 cited: "Fallback helps when a chosen route cannot complete a request. It does not guarantee identical answers, unlimited capacity, or a lower bill."). True that it is absent from docs.9router.com (vendor docs) — and the v1's label "คู่มืออิสระของ 9Router เอง" for a third-party wiki was a self-contradicting source label.
- Kept fact (MCP flag) — **TRUE verbatim on rakazo.com/docs/self-host-models.md**: "refused unless `MCP_ALLOW_PRIVATE_ENDPOINT=true` is set on the API and worker… This is checked on save, on model discovery, and on every run." + "no app account bypasses that policy".
- Kept fact (Docker) — **TRUE same page**: "a `localhost` or `127.0.0.1` connection reaches the computer running Docker (through `host.docker.internal`). On Linux, the model server must listen on an address the Docker bridge can re[ach]" — matches fix #11's rewording exactly (both work on Docker Desktop; only Linux carries the ต้อง).
- Kept fact (9Router docs) — docs.9router.com homepage: "Free AI routing with smart 3-tier fallback… auto-switch to cheap/free models" (producer claim, labeled as such in both draft and publish).
- Verdict recorded: Benz's three kept facts verify TRUE; the two cut quotes DO exist on the pages cited in the Notion v1 — the critic re-verified against different pages and the owner accepted the cuts. The owner's publish (zero English quotes) is the standing resolution; this verification record exists so the next quote-discipline fold is grounded in evidence, not in deference.

===== คอมเมนต์ verbatim =====

นี่คือสรุปครบ แต่ละข้อมีสี่ส่วน คือ ก่อนแก้ หลังแก้ เหตุผล และกฎที่ถอดออกมาได้ กฎพวกนี้นำไปใส่ให้ AI ใช้ตอนเขียนครั้งต่อไปได้เลย

ข้อที่แก้ในบทความ Rakazo x 9Router

1. ชื่อเรื่อง

ก่อน: "ลองใช้ Rakazo x 9Router (เร็วกว่า fallback ในตัว)"
หลัง: "ตั้งโมเดลสำรองใน Rakazo แล้ว งานก็ยังพัง 5-6 งานพร้อมกัน: 9Router จะช่วยได้ไหม (ยังไม่ได้ลอง)"
เพราะ: ชื่อเดิมอ้างว่าลองแล้วและเร็วกว่า แต่ในตัวบทพรเขียนเองว่ายังไม่ได้ติดตั้งและไม่ได้วัด
กฎ: ชื่อเรื่องอ้างได้เท่าที่ทดสอบจริง ถ้ายังไม่ได้ลองให้ใส่ "(ยังไม่ได้ลอง)" ในชื่อ

2. "9Router ตัดสินใจก่อนยิง"

ก่อน: เขียนเป็นข้อเท็จจริงทั้งในหัวข้อและสรุป
หลัง: "เอกสารไม่ได้บอกว่าเช็กก่อนส่งทุก request หรือสลับหลังเจอ error เรื่องนี้พรยังไม่รู้"
เพราะ: เอกสารที่เปิดตรวจบอกแค่ว่าติดตามโควตาและสลับเมื่อโควตาหมด ไม่ได้บอกจังหวะ และบรรทัดเดิมในบทความก็เขียนขัดกันเองว่า route ที่ล้มยังลองหลังเจอ error
กฎ: ถ้าเอกสารไม่ได้พูดถึงสิ่งไหน ให้เขียนว่า "เอกสารไม่ได้บอก" อย่าเติมให้ครบ

3. คำพูดอ้างอิงสองก้อนถูกตัดออก

ก่อน: อ้าง "if the main model fails or hits a limit..." ของ Rakazo และ "It does not guarantee identical answers..." ของ 9Router
หลัง: ตัดทั้งคู่
เพราะ: ก้อนแรกไม่อยู่ในหน้า rakazo.com/docs/self-host-models ที่พรอ้างอีกก้อน หน้านั้นมีแต่ backups ของ approval model ก้อนที่สองไม่อยู่ใน docs.9router.com และค้นเว็บไม่เจอ ทั้งยังเขียนว่า "คู่มืออิสระของ 9Router เอง" ซึ่งขัดกันเอง
กฎ: ใช้เครื่องหมายคำพูดเฉพาะประโยคที่ตรวจแล้วว่าอยู่ในหน้านั้นจริง พร้อม URL และวันที่ตรวจ ถ้าตรวจไม่ได้ให้ตัด

4. ข้อความจากเอกสารที่ตรวจแล้วถูก คงไว้

คง: MCP_ALLOW_PRIVATE_ENDPOINT=true ต้องตั้งทั้ง API และ worker เช็กตอนบันทึก ตอนค้นหาโมเดล และทุกรอบที่รัน และ 9Router เป็น local gateway ที่มี OpenAI-compatible endpoint ติดตามโควตา มีนับถอยหลัง และสลับเมื่อโควตาหมด
เพราะ: เปิดหน้าเอกสารตรวจเองแล้วตรงกัน
กฎ: ส่วนที่ตรวจผ่านให้ใส่ที่มาและวันที่ ส่วนที่ไม่ผ่านให้ตัดหรือแก้ ไม่ใช่ทิ้งไว้เฉย ๆ

5. คำแนะนำขัดกับหลักฐานของพรเอง

ก่อน: "ถ้าอยากได้แค่ไม่พัง ตั้งโมเดลสำรองใน Rakazo ไว้ก่อน"
หลัง: "ตั้งสำรองแล้ว ยิงทีละงานแล้ว งานก็ยัง error"
เพราะ: บรรทัดต้นบทความบอกว่าตั้งสำรองแล้วยังพังทุกตัว คนอ่านที่ทำตามคำแนะนำเดิมจะเจอปัญหาเดียวกับพร
กฎ: ก่อนแนะนำอะไร ให้เช็กว่าขัดกับสิ่งที่ผู้เขียนเพิ่งเล่าไปหรือไม่

6. ลำดับเหตุการณ์ไม่สอดคล้อง

ก่อน: ตั้งกฎยิงทีละ 1 งาน แต่ตอนลอง cron งาน error 4-5 งาน
หลัง: "ตอนลอง พรปลดกฎยิงทีละ 1 งาน ยิงเต็มที่"
เพราะ: ถ้ากฎยังใช้อยู่ จะมีงานพังพร้อมกันหลายงานไม่ได้
กฎ: เมื่อมีหลายการทดลองต่อกัน ต้องบอกเงื่อนไขของแต่ละรอบ ว่าอะไรเปิดหรือปิดอยู่

7. ผลทดลองจริงที่พรเพิ่มมา

เพิ่ม: "ยิงทีละตัวก็ยัง error แปลว่าการยิงพร้อมกันไม่ใช่ต้นเหตุเดียว" และ "token หายไปกับตัวงาน โดยที่งานไม่เสร็จสักงาน"
เพราะ: สมมติฐานเดิมของพรคือยิงพร้อมกันเป็นต้นเหตุ ผลทดลองบอกว่าไม่ใช่ทั้งหมด เลยปรับคำจาก "ไม่ใช่ต้นเหตุ" เป็น "ไม่ใช่ต้นเหตุเดียว" เพราะหลักฐานบอกได้แค่นั้น
กฎ: เมื่อผลทดลองหักล้างสมมติฐาน ให้เขียนลงไปตรง ๆ และใช้คำที่ตรงกับน้ำหนักของหลักฐาน

8. เพิ่มหัวข้อ "cron ลอง รู้ก่อนแล้วสลับ ไปแล้ว" และแตกเป็นสามกรณี

เพิ่ม: งานพังตอนเริ่ม พังกลางทาง หรือโมเดลสำรองก็เต็ม
เพราะ: cron ของพรคือการทดลองที่ใกล้กับสิ่งที่ 9Router อ้างมากที่สุด และมันไม่ได้ผล บทความต้องตอบว่าทำไม router ถึงจะต่าง สามกรณีให้ข้อสรุปต่างกัน กรณีสุดท้ายคือสมมติฐานที่ซ่อนอยู่ว่ามีโมเดลอื่นที่ยังมีโควตา
กฎ: ถ้าอาการเดียวมีหลายต้นเหตุ ให้แตกกรณีและบอกว่าแต่ละกรณีให้ข้อสรุปต่างกันอย่างไร

9. ช่องที่ยังไม่รู้ เขียนไว้ตรง ๆ

เขียน: "โมเดลสำรองตอนเกิดเหตุมีโควตาเหลือไหม ตรงนี้พรยังไม่ได้เช็ก" และใส่ในช่อง "เงื่อนไข" ของสรุปด้วย
เพราะ: พรเลือกไม่เช็กก่อนลง บทความเลยต้องบอกคนอ่านว่านี่คือสิ่งที่ยังไม่รู้
กฎ: สิ่งที่ยังไม่ได้ตรวจ ให้เขียนเป็น "ยังไม่ได้เช็ก" และใส่ซ้ำในสรุป ไม่ปล่อยให้เงียบ

10. ประโยคที่ผู้เขียนไม่ได้เจอเอง ถูกตัด

ตัด: "ถ้าหลายบอทชนลิมิตพร้อมกัน เราจะเสียเวลารอทีละรอบ" และ "เพราะมันถูกใช้จนติดลิมิต"
เพราะ: เป็นการคาดการณ์ ไม่ใช่สิ่งที่พรเล่าว่าเกิดขึ้นหรือวัดได้
กฎ: ในบันทึกประสบการณ์ ใช้เฉพาะสิ่งที่ผู้เขียนเห็นหรือวัดเอง ถ้าเป็นการคาดเดาต้องเขียนเป็นเงื่อนไข

11. Docker

ก่อน: "ให้ใช้ host.docker.internal แทน localhost"
หลัง: "ทั้ง host.docker.internal และ localhost เข้าถึงเครื่องที่รัน Docker ได้ ถ้าเป็น Linux ต้องให้ Docker bridge เข้าถึงได้"
เพราะ: เอกสาร Rakazo บอกว่าบน Docker Desktop ใช้ได้ทั้งสองแบบ คำว่า "แทน" แรงเกินไป
กฎ: ใช้คำว่า "แทน" หรือ "ต้อง" เฉพาะเมื่อเอกสารเขียนแบบนั้น

12. แผนวัด

ก่อน: "รอดูว่า error ไหม"
หลัง: บันทึกโควตาก่อนเริ่ม ทดสอบตอนโมเดลหลักใกล้เต็ม ใช้งานชุดเดียวกัน 5-6 งาน ปลดกฎยิงทีละงาน วัดจำนวนงานที่ error กับเวลาจนมีงานแรกเดินต่อได้ ทดสอบสองแบบ
เพราะ: "รอดู" วัดอะไรไม่ได้ และถ้าไม่ทดสอบตอนใกล้เต็ม จะไม่เกิดการชนลิมิตให้วัด
กฎ: แผนต้องมีเงื่อนไขเริ่มต้น ตัวชี้วัด และวิธีเปรียบเทียบ

13. จุดเล็ก

แก้: พล เป็น พร, สงเกต เป็น สังเกต, เช็ค เป็น เช็ก, ai เป็น AI, ตัดประโยคซ้ำเรื่อง token และเรื่องผู้ให้บริการ
กฎ: ตรวจคำสะกดและประโยคซ้ำก่อนลงทุกครั้ง

เรื่อง emotion
สิ่งที่คงไว้: ประโยคฉากที่พรเขียนเองหนึ่งประโยค ("ตอนเห็นหน้า error นั้นปุ๊บ ก็เห็นแล้วว่างานเสียไป 5-6 งาน") กับประโยค "งานที่ค้างรอ error ไม่ได้ค้างฟรี มันคืองานที่รออยู่บนจอโดยไม่มีอะไรมาขยับ"
เพราะ: อารมณ์ในบทความสายตัวเลขมาจากช่วงเวลาที่ผู้เขียนเจอจริง ไม่ใช่คำที่ AI เติม
กฎ: ให้ผู้เขียนเขียนฉากหนึ่งประโยคก่อนตัวเลขแรก ให้ AI เรียบเรียงต่อ แต่ห้ามเติมความรู้สึกที่ผู้เขียนไม่ได้พูด

กฎรวม สำหรับ train AI
ชื่อเรื่องและสรุปอ้างได้เท่าที่ทดสอบจริง
ใช้เครื่องหมายคำพูดเฉพาะประโยคที่ตรวจในหน้านั้นแล้ว ใส่ URL และวันที่
แยกสามอย่างให้ชัด: เอกสารบอกอะไร, ผู้เขียนเห็นอะไร, ยังไม่รู้อะไร
คำแนะนำต้องไม่ขัดกับผลที่ผู้เขียนเจอเอง
ระบุเงื่อนไขของทุกการทดลอง
ผลทดลองที่หักล้างสมมติฐาน ให้เขียนลงไปและใช้คำตามน้ำหนักหลักฐาน
ถ้าอาการเดียวมีหลายต้นเหตุ ให้แตกกรณี
สิ่งที่ยังไม่ตรวจ เขียนว่า "ยังไม่ได้เช็ก" และใส่ในสรุป
ไม่เขียนประโยคคาดการณ์ที่ผู้เขียนไม่ได้เจอ
แผนต้องวัดได้ มีเงื่อนไขเริ่มต้น ตัวชี้วัด และวิธีเทียบ
อารมณ์มาจากฉากที่ผู้เขียนเขียนเอง AI ไม่เติมความรู้สึกให้
