<!-- Archived from https://wp.adduckivity.com/tech-string-tax-jev-calib-01/ on 2026-09-20 by sync_wp_posts.py -->
Title: Co-creator ของ ChatGPT ปล่อย model ที่ “ไม่พูด” — และนั่นคือเหตุผลที่มันน่าเชื่อถือกว่า
Date: 2026-09-20T15:30:00
Link: https://wp.adduckivity.com/tech-string-tax-jev-calib-01/
-->

Co-creator ของ ChatGPT ปล่อย model ที่ “ไม่พูด” — และนั่นคือเหตุผลที่มันน่าเชื่อถือกว่า

The String Tax — คุณจ่ายภาษีให้ AI ทุกครั้งที่มัน “พูด” แทนที่จะ “ตัดสินใจ”

.

15 กันยายน 2026 — TypeSafe AI เปิดตัว model ชื่อ Jev — model ที่ ถูกออกแบบมาให้ “ไม่พูด” — ไม่ generate text — ไม่เขียนโค้ด — ไม่อธิบายตัวเอง — มันรับ “state” + “คำถามแบบมี type” — แล้วคืน decision แบบมี type พร้อมความน่าจะเป็น ใน query เดียว (parallel) — latency 70–500ms — input $0.042 ต่อ 1M tokens — output ฟรี

.

ผู้ก่อตั้งคือ Diogo Almeida — คนที่ช่วยสร้าง methods ที่ทำให้ LLM ฟังคำสั่งได้ที่ OpenAI (research เบื้องหลัง ChatGPT) — เทคครัชเรียกเขาว่า “ChatGPT co-creator” — คนที่ตั้งคำถามมา 4 ปีว่า “models เก่ง chat มาหลายปีแล้ว — แล้ว automation ล่ะ?”

.

ฟังดูเหมือน spec ของ tool ตัวใหม่ — แต่มันจริง ๆ คือ statement ทางสถาปัตยกรรม — ว่า “ภาษา” อาจไม่ใช่ interface ที่ถูกต้อง ระหว่าง intelligence กับ software

.

วันนี้พรจะ debug เรื่องนี้แบบ engineer — พร้อมโพรโทคอล CALIB-01 ที่พรจะรันกับ workflow ของตัวเอง

.

เคยมีมั้ยคับ — AI “ตอบผิด format” — หรือ “บอกมาเต็มปากว่ามั่นใจ” — แล้วระบบพัง?

ถ้าตอบเป็น “จำนวน” ได้ — กำลังจ่ายภาษีตัวหนึ่งที่เพิ่งรู้ว่ามันมีชื่อ: The String Tax

.

ปัญหาส่วนใหญ่ไม่ใช่ model ยังไม่เก่ง — ปัญหาอยู่ที่ interface — เรากำลังบังคับให้ “นักเขียน” ทำ “งานบัญชี” — และทุก error (format พัง, tool call ปลอม, มั่นใจเกินจริง) คือ ภาษี ที่จ่ายเพราะเลือก interface ผิด

.

ใครที่ยัง “parse JSON จาก chatbot” อยู่ทุกวันนี้ — นั่นแหละกลุ่มที่พรตั้งชื่อไว้: “คนจ่าย String Tax” — คนที่จ่ายภาษีทุกครั้งที่ AI “พูด” แทนที่จะ “ตัดสินใจ”

.

และส่วนที่แปลกสุด: model ที่ทำให้โลก developer สั่นสัปดาห์นี้ — คือ model ที่ “ไม่พูด” — แล้ว “การไม่พูด” ทำให้ AI น่าเชื่อถือขึ้นได้ยังไง? — คำตอบอยู่ตอนท้ายโพสต์นี้

.

.

Model ที่ “ไม่พูด” — และชื่อที่ซ่อน thesis ไว้

แก้ความเข้าใจผิด 2 ตัวก่อนคับ:

ตัวที่ 1: Jev ไม่ใช่ LLM ตัวเล็ก — มันคือ class model ตัวใหม่ที่ TypeSafe ตั้งชื่อว่า System One Models

ชื่อ class มาจาก System 1 ใน Thinking, Fast and Slow ของ Daniel Kahneman

— System 1 = คิดเร็ว / สัญชาตญาณ

— System 2 = คิดช้า / ตรรกะ

LLM แบบ chain-of-thought ที่ใช้กันอยู่ทุกวันอยู่ฝั่ง System 2 — ช้า (3–329 วินาที) แพง — และถูก design มาเพื่อ “คุยกับคน” ไม่ใช่ “คุยกับ code”

.

ตัวที่ 2: ชื่อ Jev ไม่ได้มาจาก Kahneman — TypeSafe บอกตรง ๆ ใน FAQ ของ launch post: ตั้งชื่อตาม William Stanley Jevons — นักเศรษฐศาสตร์อังกฤษที่เขียนไว้ปี 1865 ว่า ยิ่งเครื่องจักรไอน้ำใช้ถ่านหินมีประสิทธิภาพขึ้น — การบริโภคถ่านหินกลับ “เพิ่มขึ้น” ไม่ใช่ลดลง (Jevons Paradox) — และนั่นคือ thesis ทั้งตัวของบริษัท: ทุก ๆ order-of-magnitude ที่ต้นทุน intelligence ถูกลง — จะปลดล็อก order-of-magnitude ของ use case — AI ถูกขึ้น 100x ≠ ประหยัด 100x — = จำนวน decision ที่ระบบทำได้ ×100

.

(นี่คือ correction ที่น่าอ่านของโพสต์นี้ — สื่อหลายเจ้าเขียนว่าชื่อ Jev มาจาก Kahneman — ที่จริง class name = Kahneman แต่ ชื่อ model = Jevons — และ Jevons ตัวหลังแหละคือ soul ของเรื่อง)

.

Error 1 — The String Tax — ภาษีที่จ่ายเพราะให้ “นักเขียน” ทำ “งานบัญชี”

ลองดู flow ที่เราทุกคน build อยู่:

application → ถาม LLM → LLM เขียน คำตอบ (string) → application parse → validate → ภาวนา → branch

ปัญหาไม่ใช่ model ตอบผิด — ปัญหาคือ “การตัดสินใจ” ถูกห่ออยู่ใน “ภาษา” — application ต้องการ decision — แต่ model ผลิต “token ที่เป็นตัวแทนของ decision” — และ application ต้อง trust ตัวแทน — Anthony Maio สรุปได้เจ็บมาก:

“The application needs a decision. The model produces tokens that represent one, and the application has to trust the representation.”

“ภาษี” ของการ trust ตัวแทนมีตัวเลขจริง (จาก eval ของ TypeSafe):

Structured output error rate (test เดียวกัน): OpenAI luna/terra 0.58% — Claude Opus 5 5.73% — Claude Haiku 4.5 45.5% — ตัวหลัง = format พังเกือบทุกเคสที่ 2

Tool call error rate: GPT-5.6 Sol 17.0% — tool call “ปลอม” (hallucinated) ~1 ใน 6

Hallucinated tool call ใน agent ที่มีคนนั่งดู = รำคาญ — แต่ใน pipeline ที่รันเอง + latency guarantee = deal-breaker — เพราะ error แบบนี้ไม่ predict ได้ — ไม่รู้เลยว่ามันจะพังตอนไหน

.

Jev แก้ที่โครงสร้าง: possible outputs ถูก define ไว้ใน schema ก่อนเรียก — type error เป็นไปไม่ได้ทางคณิตศาสตร์ (0% โดย construction — “it would be easy to falsify with just a single counter-example, but it is mathematically impossible” — TypeSafe) — และคำตอบทั้งหมด ออกมาพร้อมกันใน query เดียว (parallel sampler) — ไม่ใช่ token-by-token:

“Think of Jev as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out.”

— TypeSafe AI (launch post, 2026-09-15)

คำถามที่ Jev รองรับมี 3 type (จาก docs + LangChain guide): Choice (เลือกจากตัวเลือก — คืน probability ของแต่ละตัว) / Score (ระดับ low → high — คืน score + distribution) / Noul (ใช่/ไม่ใช่ — คืน probability ว่าจริง) — และถาม หลายคำถามต่อ state เดียวใน request เดียว — เพิ่มคำถาม ≈ ไม่เพิ่ม latency (เพราะ evaluate แบบ parallel)

.

Error 2 — The Overconfidence Trap — “น้ำเสียงมั่นใจ” ≠ “ความน่าจะเป็น”

Error ที่ลึกกว่า String Tax — คือ เราไม่มี “ตัวเลขความมั่นใจที่ trust ได้” จาก LLM — TypeSafe บอกตรง ๆ:

“Even if prompted for a confidence estimate, models tend to be overconfident and inconsistent.”

และนี่คือ kill shot ของ automation:

“If a model can do a task 95% of the time but doesn’t say when it’s in the 5%, it can’t automate that task.”

model ที่เก่ง 95% แต่ ไม่บอกตอนไหนที่มันอยู่ใน 5% นั้น — automation ไม่ได้ — เพราะไม่รู้จะ trust คำตอบไหน — “น้ำเสียง” ของคำตอบที่เขียนมาไม่ได้ช่วยอะไร — model ที่ “เขียน” มั่นใจ กับ model ที่ “ถูก” 70% เป็นคนละตัว

.

Jev แก้ด้วย calibration — ในหมู่ prediction ทั้งหมดที่ model ให้ค่า “80%” — มันถูกจริง ~80% — confidence สูงขึ้น = accuracy สูงขึ้นจริง — และทุก output มาพร้อม confidence — ทำให้ตั้ง threshold ได้:

confidence ≥ threshold → auto-execute (log ทุกครั้ง)

confidence < threshold → route ไป LLM ช้ากว่า / ไปคน

และนี่คือบรรทัดที่สำคัญสุดของโพสต์ — Maio สรุป division of labor:

“The model supplies the semantic judgment and does not own the policy.”

model ให้ “ความเห็นเชิงความหมาย” — แต่ threshold, policy, permission, side effect = ของ code — นี่คือ Power Test ของ Duck OS ในรูป AI: ดึงอำนาจตัดสินใจกลับ — model ไม่เคยเป็น load-bearing wall

.

แต่ต้องพูดตรง ๆ (Anti-Hype):

— calibration เป็นคุณสมบัติของ กลุ่ม prediction — ไม่ได้การันตีคำตอบเดียว

— “ไม่ hallucinate” = shape ถูกจำกัด (ไม่ invent field / ไม่ผิด type) — แต่ judgment ไม่ได้ถูกจำกัด — มันเลือก option ผิดพร้อม probability สูงได้ — schema ที่ออกแบบมาไม่ดี (ไม่มีตัวเลือก “unknown / ไม่มีข้อใด”) จะบีบให้ probability ไปลงที่ตัวเลือกที่ผิด

— calibration drift ได้ — policy เปลี่ยน / fraud pattern ใหม่ / customer หน้าใหม่ = ตัวเลขที่แม่นเดือนก่อน อาจเพี้ยนเดือนนี้

— ตัวเลขทั้งหมดในโพสต์นี้ = vendor-reported — TypeSafe ออกตัวเองว่า workflow eval สร้างโดยทีมตัวเอง — ยังไม่มี independent benchmark

.

Error 3 — The Jevons Ceiling — “เพดานต้นทุน” ที่เราจินตนาการขึ้นเอง

Error สุดท้ายไม่ใช่ของ model — เป็นของเรา — เราคิดด้วย unit cost เก่า

เพราะ LLM แพง (input $0.20–$10 ต่อ 1M tokens, output ~5x ของ input) — เราเลยอนุญาตให้ AI ตัดสินใจเฉพาะเคสที่ “สำคัญ” — และ “สำคัญ” คือตัวกรองที่สร้างจากความกลัวค่า token

ตัวเลขจาก workflow eval ของ TypeSafe (4 workflows: security incident response, agent-trace observability, invoice processing, customer service — reference = ค่าเฉลี่ยของ GPT-6 Astra + Fable 5.1):

Jev: accuracy 67.8% — $0.0004/case — 0.4s

GPT-5.6 Terra: 67.9% — $0.0304 — 10.1s (Jev เท่ากันแต่ถูกกว่า ~76x เร็วกว่า ~25x)

GPT-5.6 Sol: 74.1% — $0.0836 — 23.3s / Claude Opus 5: 73.1% — $0.1761 — 37.8s (ยังนำอยู่ 5–6 คะแนน — invoice processing = gap ใหญ่สุด Jev 61.8% vs Sol 79.1%)

ถ้า error แพง (เช่น approve ธุรกรรม) — ความต่าง 17 คะแนนอาจแพงกว่าค่า inference ทั้งหมด — ตรงนั้น Jev ไม่ควรได้แตะ

.

แต่ unit cost = $0.0004/decision เปลี่ยนคำถามทั้งระบบ: คำถามไม่ใช่ “decision นี้ worth AI ไหม” — คำถามคือ “ต้องการเพิ่ม decision ตรงไหนอีก” — TypeSafe ให้ตัวอย่าง: scoring 50 ล้านแถวของ product review = ~$20 — สิ่งที่เคยเดาว่า “แพงเกินไป” กลายเป็น “ถูกกว่ากาแฟ” — และ demo ของ TypeSafe เล่น Doom โดยอ่าน structured game state ~10 ครั้ง/วินาที (~$7/ชม.) — สิ่งที่เคย “ทำไม่ได้” เพราะ LLM ใช้เวลา 3–329 วินาที — กลายเป็น real-time

นี่คือ Jevons Paradox ทำงานจริง — efficiency → ค่าใช้ลดลง → demand เพิ่ม → total consumption พุ่ง — และชื่อ model ก็ตั้งเพื่อ bet นี้เอง: “We expect machine intelligence to follow a similar path to coal.” (TypeSafe FAQ)

.

.

โปรโทคอล CALIB-01 — ใช้กับทุก workflow ที่เรา build

ไม่ว่าจะรันด้วย Jev, LLM ธรรมดา, หรือ logic ธรรมดา:

.

Step 1: calib --interface (แยก “decision” ออกจาก “text”)

Audit ทุก workflow — หาทุกจุดที่ “การตัดสินใจ” ถูกห่ออยู่ใน “คำตอบภาษา”:

เขียน decision space ของมันออกมา — มีกี่ตัวเลือก? (Choice) / กี่ระดับ? (Score) / ใช่/ไม่ใช่? (Noul)

ถ้า decision space จำกัด + รู้ล่วงหน้า → ห้าม generate text — ถามเป็น typed question แทน

ถ้า decision space เปิด (ต้องเขียนโค้ด / อีเมล / อธิบาย) → LLM ธรรมดาถูกแล้ว — อย่าฝืน

rule: ถ้าคำตอบถูกจำกัด — อย่าใช้ interface ที่เปิด (แก้ String Tax)

.

Step 2: calib --threshold (ความไม่แน่นอน = ตัวเลข — threshold = ของ code)

ทุก decision ที่ auto-execute ต้องมี confidence threshold ระบุชัด:

confidence ≥ threshold → auto-execute + log

confidence < threshold → route ไป LLM ช้ากว่า / คน — ห้าม auto

threshold อยู่ใน code — ห้ามฝังใน prompt — model ให้ probability — เรา ตัดสินใจว่าเท่าไหร่ถึง “พอ”

ทุก decision space ต้องมีทางออก “unknown / insufficient evidence” — ห้ามบีบให้ probability ไปลงตัวเลือกที่ผิด

rule: model ไม่มีสิทธิ์ “own” policy (แก้ Overconfidence Trap)

.

Step 3: calib --volume (Jevons Check — ต้นทุนลด = decision เพิ่ม)

ทุกครั้งที่ unit cost ของ decision ลดลง (tool ใหม่ / ถูกกว่าเดิม / เร็วขึ้น) — อย่าแค่ “ประหยัด”:

ถาม: “ด้วย unit price ตัวนี้ — มี decision ไหนที่เคยเดาว่า ‘not worth it’ ที่ตอนนี้ worth แล้ว?”

เพิ่ม 1 decision layer ใหม่ ต่อการลดต้นทุน 1 รอบ (guardrail ทุก tool call / scoring ทุก row / verify ทุก output)

log KPI: จำนวน decision ที่ระบบทำต่อสัปดาห์ — ไม่ใช่ “ค่า API ลดลงกี่ %”

rule: ถ้า “ประหยัด” แล้วจำนวน decision ไม่เพิ่ม = ยังไม่เข้าใจ Jevons Paradox (แก้ The Ceiling)

.

Success Criteria: สัปดาห์นี้ — 1 workflow — audit decisions (Step 1) → ตั้ง threshold ทุกจุด (Step 2) → เพิ่ม 1 decision layer ที่เคย “not worth it” (Step 3) — วัดผล: จำนวน decisions logged ต่อสัปดาห์ + จำนวน auto-execute ที่ confidence < threshold (ต้อง = 0)

.

มุม Duck OS

Law #1: System > Emotion — “น้ำเสียงมั่นใจ” ของ LLM = อารมณ์ของ machine — คำตอบที่ “เขียน” มั่นใจ ≠ probability สูง — ระบบที่ดีไม่ trust น้ำเสียง — มัน trust ตัวเลขที่ calibrated + threshold ที่ code คุม — System > Verbal Confidence

Law #2: Asset > Activity — Chat กับ LLM = Activity — ปิด tab = หาย — แต่ typed decision + calibrated probability ที่ wired เข้า code = Asset — re-run ได้ — audit ได้ (log ทุก decision) — compose ได้ — และตาม Jevons: asset ที่ถูก = asset ที่ถูกเรียกใช้ ×100

Law #3: Protect the System — hallucinated tool call ที่ฝังลึกหลายชั้นใน dependency chain = Single Point of Failure ที่ไม่ predict ได้ — schema-constrained output = Circuit Breaker ระดับ type system — มันตัด error class ทั้ง class ทิ้งก่อนถึง runtime — Protect System = อย่าให้ interface ที่ unpredictable นั่งอยู่ใน loop ที่มี latency guarantee

โพสต์ System Vision (2026-09) บอกว่า “อย่า trust forecast — build ระบบที่ไม่ว่าพายุจะแรงยังไงก็ไม่พัง” — โพสต์นี้คือ machine version ของเรื่องเดียวกัน: calibrated probability = forecast ที่ model “บอก” ว่ามันไม่แน่ใจ — threshold = firewall ที่เราคุม — ทั้งสองจบที่ pull the control back (ref: Chunking Engine 2026-09 — decomposition คือรากของทั้งสอง / Orca FLEET-01 2026-09-17 — agent loop ที่ code คุมทุก step)

“how much more dependable could AI get if we stopped requiring every intelligent component to talk?” — คำถามนี้ควรติดอยู่เหนือทุก workflow ของเรา

.

#สรุปแบบวิศวกรเป็ด

เราจ้าง “นักเขียน” ให้ทำ “งานบัญชี” — และทุก error (format พัง / tool call ปลอม / มั่นใจเกินจริง) คือ String Tax — Jev คือการเปลี่ยน interface: state + typed questions in → typed decisions + calibrated probabilities out

Calibration = model ที่ “บอก” ว่ามันไม่แน่ใจ — และ threshold อยู่ใน code ของเรา — model ให้ opinion — เรา ตัดสินใจ — นี่คือ System > Verbal Confidence + Power Test (ดึงอำนาจตัดสินใจกลับ) ในรูป AI

Jevons Paradox = ชื่อของ model = thesis: ต้นทุน decision ลด 100x ≠ ประหยัด 100x — = จำนวน decision ที่ระบบทำได้ ×100 — KPI = decision ต่อสัปดาห์ — ไม่ใช่ “ค่า API ลดลงกี่ %”

.

และสำหรับคำถามเปิดต้นโพสต์ — ทำไม “การไม่พูด” ทำให้ AI น่าเชื่อถือขึ้น? — ความน่าเชื่อถือไม่ได้มาจากการ “รู้มากขึ้น” — มันมาจากการที่ model “บอก” ว่ามันไม่แน่ใจ + threshold ที่ code ของเราคุม — model ที่พูดเก่ง = model ที่เราต้อง trust “ตัวแทน” — model ที่ไม่พูดแต่ให้ probability = model ที่ระบบ “คุม” ได้

.

Challenge 5 นาทีวันนี้ — เปิด workflow / ระบบที่ใช้บ่อยสุด — นับว่ามี “decision” กี่ตัวที่ห่ออยู่ใน “ข้อความที่ AI เขียน” (ไม่ใช่ตัวเลข / ไม่ใช่ type) — คอมเมนต์ตัวเลขด้านล่าง — พรจะนับค่าเฉลี่ยไว้ให้โพสต์ถัดไป

.

#Adduckivity #DuckOS #NeuroDivergent #SystemOne #Jev #JevonsParadox #AIAutomation #SystemThinking
