<!--
pair #98 (ai-harness-same-model-different-loop) — CURRENT FORM — LEVEL: L2 (doing-wrong-unnoticed: เทียบ harness ทีละชื่อ แต่สิ่งที่ลงงานคือคู่ harness×model)

ORIGIN: owner brief (2026-11-03): "Storytelling about what's harness from KB latest and try to draft with 6 level of content" — ต่อยอดหน้า KB "AI Harness — นิยาม + วิธีเลือก harness สำหรับ AI agent" (40ddf8d8-8d8c-8194-ace5-f2772f2ceae7, ขยาย landscape 2026-11-03) — owner เลือก L2 จาก 6 ร่าง (สมรภูมิ 6 level อยู่ใน git history ของไฟล์ six-levels)

SPINE: ทุกครั้งที่จะเลือก harness เราเปิดลิสต์เทียบทีละชื่อ (ฟีเจอร์/ความครอบคลุม/คนพูดถึง) → มีประโยคว่ากันว่า Agent = model + harness (LangChain มี.ค. 2026 — reported) → สิ่งที่ลงงานจริง = คู่ ไม่ใช่ชิ้นเดียว → ลิสต์เทียบชื่อจึงเทียบแค่ครึ่งเดียวของสิ่งที่จะลงไปทำงาน → อาการที่ตามมา: ของที่รีวิวดีมาก มาอยู่กับงานเราแล้วไม่เหมือนรีวิว → model เดิมสลับ harness แล้วผลงานเปลี่ยน กลับกันก็เปลี่ยน (Warp ส.ค. 2026: performance เป็นฟังก์ชันของ harness × model — reported) → คู่ที่ดีไม่ได้ดีเพราะตัวไหนเก่ง แต่เข้ากันแล้วเข้ากับงาน → ครั้งหน้าเจอลิสต์เทียบชื่อ ถามกลับว่า model ฝั่งไหน
INSIGHT-ONCE: bold เป็ด dispatch จุดเดียว — ประโยคอื่นไม่ bold ซ้ำ
EVIDENCE STATUS: no-case class-level (เราล้วน) — LangChain/Warp เป็น "ว่ากันว่า" ไม่ยืนยันแทน; ไม่ตั้ง benchmark ของตัวเอง (ยังไม่มีเคสจริงในบ้าน); ไม่มีเลข
SIBLING GUARDS: #74 (LocalLLM — เครื่อง/GPU = 0), #81 (blind spot — ตัวเลขที่นับตัวเองไม่ได้ = 0), #82 (ป้องกัน vs แก้ = 0), 9router (WP archive, ชื่อเฉพาะ = 0), llama.cpp post (engine/benchmark = 0); ledger ล่องหน: "comparison-list vs working pair" — ไม่เรียกชื่อแนวคิดในบท
CUT LIST (zero-count): พร, คุณ, คับ, ผม, เพราะ, พร้อม, วินัย, feedback, ระบบ, เครื่องมือ, เสมอ, ทุกครั้ง, ความมั่นใจ, benchmark ตัวเลขจากงานวัดของเรา, ชื่อ harness/model เฉพาะ (Claude Code/Codex/OpenCode/Qwen/GLM = 0 — กติกาห้ามชื่อจริงตาม #81), ?, ธุรกิจ
FORMAT: line-per-sentence + จุดขั้น + H2 #สรุปแบบวิศวกรเป็ด + quote bold 1 + hashtag tail; '?' 0
LEVEL: L2 — หัวเรื่อง/เนื้อไม่มีคำบอก level ตรง ๆ (L-check: บทส่งมอบ "กำลังทำผิดโดยไม่รู้ตัว" ผ่านการชี้พฤติกรรมเทียบลิสต์ที่อ่านแล้วผ่าน)
Notion: Content Drafts DB 3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520, Platform general
-->

# เลือก AI harness ด้วย model เดิม — แต่ลืมว่าเราเปลี่ยนทั้งคู่

.

เวลาจะเลือก AI harness เรามักเปิดลิสต์ แล้วเทียบกันทีละชื่อ

ฟีเจอร์เยอะกว่า เปิดให้ครบกว่า คนพูดถึงเยอะกว่า

แต่มีประโยคหนึ่งว่ากันว่า Agent คือ model บวก harness

แปลว่าสิ่งที่ลงงานจริง ไม่ใช่ harness ชิ้นเดียว แต่เป็นคู่ของมันกับ model

ลิสต์ที่เทียบชื่อ เทียบแต่ครึ่งเดียวของสิ่งที่จะลงไปทำงาน

จบแล้วแปลกใจว่าทำไมของที่รีวิวดีมาก มาอยู่กับงานเราแล้วไม่เหมือนรีวิว

.

> **เราไม่ได้เลือก harness เราเลือกทั้งคู่โดยดูฝั่งเดียว**

.

model เดิม สลับ harness แล้วผลงานเปลี่ยน กลับกันก็เปลี่ยน

คู่ที่ดีในงานนี้ ไม่ได้มาจากความเก่งของตัวใดตัวหนึ่ง แต่มาจากการที่ทั้งคู่เข้ากันแล้วเข้ากับงาน

ครั้งหน้าเจอลิสต์เทียบชื่อ ให้ถามกลับว่า model ฝั่งไหน — เรากำลังเลือกคู่ ไม่ได้เลือกของชิ้นเดียว

.

## #สรุปแบบวิศวกรเป็ด

การเทียบ harness ทีละชื่อ คือการดูครึ่งเดียวของคู่ที่จะลงงาน

**สิ่งที่ลงงานคือคู่ การเทียบชื่อจึงเห็นครึ่งเดียวตั้งแต่ยังไม่เริ่ม**

#Adduckivity #DuckOS #NeuroDivergent #AI
