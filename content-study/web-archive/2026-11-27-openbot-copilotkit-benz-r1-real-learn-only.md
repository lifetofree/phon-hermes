# Benz r1 REAL — learn-only — OpenBot by CopilotKit draft (pair #OpenBot-copilotkit)

- **วันที่:** 2026-11-27 · **คลาส:** PROVISIONAL-inline (paste จากแชต — ยังไม่มีไฟล์ byte-true)
- **Draft ที่ critic อ่าน:** หน้า Notion `424df8d8-8d8c-8163-acf1-c52be46c7c35` "รู้จัก OpenBot by CopilotKit: แพลตฟอร์ม AI Coworker ระดับองค์กร กับข้อสังเกตเรื่องความปลอดภัยและต้นทุน" — 63 blocks, last edit 2026-11-26 21:40 ICT, Status draft, Slug `openbot-copilotkit-intro`, Platform FB+Website
- **Directive ของ owner:** "it was engineering, analysis, learning, and anything that you can do to improve skill in writing content" = LEARN-ONLY — ไม่ rewrite, ไม่แตะหน้า Notion, โฟกัสถอดวิธีคิด critic + ตรวจ fact ฝั่ง Hermes (โดยเฉพาะรายการ "ตรวจก่อนเผยแพร่" ที่ Benz ประกาศว่าเขายังไม่ได้ตรวจ)
- **รอบก่อนหน้าในซีรีส์:** pair #OpenBot-local (OpenBot.run ชิ้น 424df8d8-8126, publish 26 พ.ย.) + บทความเปรียบเทียบ (423df8d8-81cb, published)

---

## คอมเมนต์ Benz (verbatim)

**ภาพรวม:** เนื้อหาละเอียดและเป็นประโยชน์ ส่วนข้อจำกัดมีรายละเอียดจับต้องได้ เช่น Kubernetes, EKS 3 เครื่อง t3.large และตัวติดตั้ง macOS ที่ยังไม่ผ่านการรับรอง จุดแข็งอีกอย่างคือแยกชื่อ OpenBot ของ CopilotKit ออกจาก OpenBot.run ซึ่งผู้อ่านสับสนจริง ผมยังไม่ได้ตรวจข้อมูลกับเว็บทางการ ข้อวิจารณ์ด้านล่างเป็นเรื่องความสอดคล้องและการเขียน

**ต้องแก้ก่อน**

1. **ชื่อผู้พัฒนา OpenBot.run ขัดกัน** บทความก่อนหน้าเขียนว่า Synthetify Labs แต่ชิ้นนี้เขียนว่า Nightly Labs อย่างน้อยหนึ่งในสองผิด ตรวจกับเว็บทางการแล้วแก้ให้ตรงกันทั้งสองชิ้น
2. **ขัดกับบทความเปรียบเทียบ** ตารางเปรียบเทียบเขียนว่าความสามารถ "บอทมีคอมจริง" ของ CopilotKit ได้ "ผ่าน coding agents" แต่ชิ้นนี้บอกว่าเอเจนต์แต่ละตัวมี Chromium พื้นที่ไฟล์ และเทอร์มินัลของตัวเอง เปรียบเทียบเขียนเรื่องสัญญาอนุญาตแค่ "ฟรี personal" แต่ชิ้นนี้บอกว่าโค้ดเป็น MIT และบางส่วนเป็นกรรมสิทธิ์เชิงพาณิชย์ ต้องกลับไปแก้บทความเปรียบเทียบให้ตรงกัน
3. **ที่มาไม่ชัด** "เอกสารวิจัย OpenBot ของ CopilotKit" คือเอกสารอะไร เป็นของ CopilotKit เอง หรือรายงานที่คนอื่นหรือ AI สรุปให้ ถ้าไม่ใช่เอกสารทางการ ผู้อ่านควรรู้ ใส่ลิงก์ของเอกสารทางการและคลิปสัมมนา
4. **ไม่ได้บอกว่ายังไม่ได้ลองใช้** ชิ้นเกี่ยวกับ OpenBot.run บอกในชื่อเรื่อง ชิ้นนี้ไม่บอก ผู้อ่านอาจเข้าใจว่าทดสอบแล้ว ประโยค "พร พบว่า" ท้ายบทความทำให้เข้าใจแบบนั้น เปลี่ยนเป็น "พรสังเกตจากเอกสาร" และใส่สถานะเอกสารไว้ต้นบทความ
5. **ไม่มีคำเปิดเผยผลประโยชน์** ชิ้น OpenBot.run บอกว่าไม่เกี่ยวกับผู้พัฒนาและคุณใช้ Rakazo ชิ้นนี้ไม่มี ทั้งที่เนื้อหาเป็นการประเมินคู่แข่งของ Rakazo ใส่ซ้ำให้ครบ
6. **ย่อหน้า "ในขั้นตอนการทดสอบเบื้องต้นบนคลัสเตอร์ ตัวระบบทำงานแบบใช้คอมพิวเตอร์ร่วมกัน"** อ่านแล้วไม่เข้าใจว่าหมายถึงอะไร ถ้าหมายถึงเอเจนต์หลายตัวใช้เครื่องร่วมกันจนข้อมูลอาจปนกัน ให้เขียนตรงๆ ถ้าไม่แน่ใจว่าเข้าใจถูก ตัดออกก่อน

**ควรปรับ**

- **เสียงผู้เขียน** กลับไปใช้ "พร" บุคคลที่สาม ทั้งที่ชิ้นก่อนเปลี่ยนเป็น "ผม" แล้ว เลือกให้เหมือนกันทั้งซีรีส์
- **ภาษาแข็งและเป็นทางการ** เช่น "ระบบเปลี่ยนรูปแบบจากการเป็นแชตบอทเดี่ยว" และคำว่า "เสมือน" ซ้ำหลายครั้ง ซีรีส์วิศวกรเป็ดควรอ่านเป็นคนพูด ลองอ่านออกเสียงแล้วแก้ประโยคที่ติด
- **ศัพท์ไม่อธิบาย** AGUI, A2A, MCP, Fail-Closed, Generative UI และ SKILL.md ถ้าผู้อ่านเป็นคนทั่วไป เลือกอธิบายสั้นๆ 2 คำที่สำคัญ ที่เหลือตัดหรือใส่ในวงเล็บ
- **หัวข้อ "ข้อจำกัด" ปนกับ "ความเสี่ยงด้านความปลอดภัย"** การถูกแทรกคำสั่งผ่านหน้าเว็บ และ SKILL.md ที่กระจายวิธีผิด เป็นความเสี่ยง ไม่ใช่ข้อจำกัดด้านต้นทุน แยกเป็น 2 กลุ่ม (ต้นทุนและการดูแล / ความปลอดภัย) และใช้รูปแบบการนับเดียวกันทั้งส่วน
- **คำสัญญาเรื่องต้นทุนยังไม่ครบ** ชื่อเรื่องมี "ต้นทุน" แต่เนื้อหามีแค่ทรัพยากรคร่าวๆ ไม่มีตัวเลขเงิน ถ้าไม่มีตัวเลขที่ตรวจได้ ให้บอกว่าต้องคำนวณเอง และอย่าลืมใส่ค่า Business $29 ต่อ user ต่อเดือนที่เขียนไว้ในบทความเปรียบเทียบ
- **"การประมวลผลแบบตัดขาดจากเครือข่าย"** อยู่ในส่วนข้อดี แต่ข้อควรระวังเรื่องข้อมูลเดินทางผ่านโมเดลภายนอกอยู่ไกลลงไป ย้ายมาไว้ติดกัน
- **ย่อหน้าเปิด** (บรรทัดที่ 3 ถึง 11) พูดกว้างและเป็นแบบทั่วไป ตัดเหลือ 2 ประโยค หรือเริ่มด้วยเหตุผลที่คุณสนใจตัวนี้
- **บทสรุปไม่ได้ตอบ "ใครควรใช้"** มีแต่ "ขึ้นอยู่กับ" ใส่ 2 บรรทัด ใครเหมาะ ใครไม่เหมาะ และลิงก์ไปบทความเทียบ
- **แฮชแท็ก** ชิ้นก่อนมี #Adduckivity #DuckOS #NeuroDivergent ชิ้นนี้ไม่มี

**ตรวจก่อนเผยแพร่:** ตัวเลข t3.large 3 เครื่อง ขอบเขตสัญญา MIT และส่วนที่เป็นกรรมสิทธิ์ สถานะ notarization ของ macOS และข้อความว่า AGUI "พัฒนาร่วมกับ LangChain" (ผมไม่แน่ใจว่าตรงกับเอกสารต้นทาง)

**จุดที่ควรเก็บ:** ย่อหน้าแยกชื่อกับ OpenBot.run, รายการข้อจำกัดเชิงปฏิบัติ, ประโยคเรื่องให้คนเข้าควบคุมเบราว์เซอร์เมื่อเจอ 2FA แทนการส่งรหัสผ่านให้โมเดล และรูปแบบ [สาระ] [เงื่อนไข] [มุมสังเกต]

**ลำดับแก้ที่แนะนำ:** แก้ชื่อผู้พัฒนา ใส่สถานะ "ยังไม่ได้ลอง" และคำเปิดเผยผลประโยชน์ แทนที่ที่มาด้วยลิงก์ แยกหัวข้อความเสี่ยง ตัดย่อหน้าที่อ่านไม่เข้าใจ แล้วปรับเสียงให้เหมือนชิ้นอื่น ถ้าต้องการ ผมเขียนใหม่ให้ได้เลยในรูปแบบเดียวกับชิ้น OpenBot.run

---

## Quote-verify กับหน้า Notion (63 blocks)

| # | Quote ของ Benz | ผล | Block |
|---|---|---|---|
| 1 | "ทีม Nightly Labs" | HIT | 9 |
| 2 | "ผ่าน coding agents" (ตารางเทียบ) | HIT | ตาราง 423df8d8 row 2 "✓ ผ่าน coding agents" |
| 3 | "ฟรี personal" (ตารางเทียบ) | HIT | ตาราง 423df8d8 row 6 "ฟรี personal / Business สูงสุด $29 ต่อ user ต่อเดือน" |
| 4 | "เอเจนต์แต่ละตัวมีสภาพแวดล้อมเสมือนของตนเองแยกเป็นอิสระ" | HIT | 13 |
| 5 | "เบราว์เซอร์ Chromium พื้นที่จัดเก็บไฟล์ และเทอร์มินัล" | HIT | 14 |
| 6 | "สัญญาอนุญาตแบบเปิด MIT ในส่วนของตัวโค้ดแอปพลิเคชัน" | HIT | 8 |
| 7 | "กรรมสิทธิ์เฉพาะที่มีค่าใช้จ่ายเชิงพาณิชย์" | HIT | 37 |
| 8 | "เอกสารวิจัย OpenBot ของ CopilotKit และคลิปสัมมนาทางการ" | HIT | 2 |
| 9 | "พร พบว่า" | HIT | 59 |
| 10 | "ในขั้นตอนการทดสอบเบื้องต้นบนคลัสเตอร์ ตัวระบบทำงานแบบใช้คอมพิวเตอร์ร่วมกัน" | HIT verbatim | 49 |
| 11 | "การประมวลผลแบบตัดขาดจากเครือข่ายภายนอก" | HIT | 23 |
| 12 | "ระบบเปลี่ยนรูปแบบจากการเป็นแชตบอทเดี่ยว" | HIT | 12 |
| 13 | title มี "ต้นทุน" / เนื้อไม่มีเลขเงิน | HIT | title เต็ม "…ความปลอดภัยและต้นทุน" · ต้นทุน×0 ค่าใช้จ่าย×2 $29×0 |
| 14 | เสียง พร ในชิ้นนี้ vs ผม ในชิ้นก่อน | HIT | draft: พร×2 (b5,b59) ผม×0 เรา×3 · เทียบ 423df8d8: ผม×6 |
| 15 | #Adduckivity #DuckOS #NeuroDivergent ไม่มี | HIT | 0 ทั้งสาม (มีแต่ #ProductivityHacks #SystemInAction #OpenBot #CopilotKit #AIAgents #EnterpriseAI ที่ b62) |
| 16 | บทสรุปมีแต่ "ขึ้นอยู่กับ" | HIT | 60 |
| 17 | ไม่มีคำเปิดเผยผลประโยชน์ (Rakazo×0) | HIT | Rakazo×0 ทั้ง draft |
| 18 | "ข้อจำกัด" ปน "ความเสี่ยง" หัวเดียว | HIT | H2 b30 "สิ่งที่ต้องระวังและข้อจำกัดสำคัญ" ครอบ b31-43 (ข้อจำกัด) + b44-48 (ความเสี่ยง) |
| 19 | "เสมือน" ซ้ำ | HIT | ×3 (b12, b13, b29) |
| 20 | ศัพท์ AGUI/A2A/MCP/Fail-Closed/Generative UI/SKILL.md ไม่อธิบาย | HIT | AGUI×2 A2A×1 MCP×1 Fail-Closed×1 Generative UI×1 SKILL.md×1 — ไม่มี block ไหนอธิบาย |

**ผล: 20/20 HIT — ไม่มี version drift (critic อ่านหน้าปัจจุบัน) · คำ "บรรทัดที่ 3 ถึง 11" ตรงกับ blocks 0-5 ใน export**

## ตรวจข้อที่ Benz อ้างข้ามบทความ (ยืนยันกับหน้าจริงทั้งสอง)

1. **ชื่อผู้พัฒนา:** ชิ้น OpenBot.run (424df8d8-8126, published) b13/b70 = "พัฒนาโดย Synthetify Labs แจกจ่ายภายใต้ PolyForm Noncommercial 1.0.0" — ชิ้นนี้ b9 = "ของทีม Nightly Labs" → ขัดกันจริงตามที่ Benz ชี้
2. **ตารางเทียบ vs ชิ้นนี้:** row 2 "บอทมีคอมพิวเตอร์จริง | ✓ ผ่าน coding agents" ขัดกับ b13-14 (เอเจนต์มี Chromium/ไฟล์/เทอร์มินัลเป็นของตัวเอง) · row 6 ไม่มีข้อมูล MIT/กรรมสิทธิ์ ขัดกับ b8+b37
3. **หน้า OpenBot.run (424df8d8-8126) ยังมีบล็อกซ้ำ 2 ชุด:** 100 blocks = สองชุดเนื้อหาเดียวกัน (b13≡b70, b1≡b58 ยืนยันด้วยสายตา) — residual defect จากรอบก่อนยังไม่หาย

---

## FACT AUDIT โดย Hermes 27 พ.ย. 2026 (ส่วน engineering — ตอบรายการ "ตรวจก่อนเผยแพร่" ของ Benz)

| # | Claim ใน draft | ผลตรวจ | แหล่ง |
|---|---|---|---|
| F1 | b9 "OpenBot.run ของทีม Nightly Labs" | **ผิดชื่อ** — ผู้พัฒนาทางการ = Synthetify Labs sp. z o.o. (บริษัทโปแลนด์, KRS 0000895882) ตาม App Store seller + privacy policy; "nightly-labs" = ชื่อ GitHub org เท่านั้น → ชิ้น OpenBot.run ที่เขียน Synthetify Labs ถูกแล้ว ชิ้นนี้ต้องแก้ | apps.apple.com/us/app/openbot-run/id6807024266 · openbot.run/privacy-policy (Nov 20, 2026) · github.com/nightly-labs/openbot |
| F2 | b33 "EKS 3 เครื่อง t3.large" | **ตรงเป๊ะ** — README: "on EKS that is three t3.large nodes, not two" | github.com/CopilotKit/OpenBot README (อ่าน 27 พ.ย. 2026) |
| F3 | b8+b37 "MIT ส่วนโค้ด + ส่วนจัดการความจำ/เรียนรู้อัตโนมัติ = กรรมสิทธิ์มีค่าใช้จ่าย" | **ตรง** — FAQ: "The application source is MIT-licensed. OpenBot for Business has its own license, which covers CopilotKit Intelligence" · README: "Separately licensed" | open.bot/blog/openbot-for-business-webinar FAQ · README |
| F4 | b35 "macOS ยังไม่ผ่าน notarization" | **ล้าสมัย** — README วันนี้: "Notarized .dmg for Apple silicon and Intel Macs · signed installer for Windows x64" → ต้องแก้ก่อนเผยแพร่ (จุดที่ Benz ขอตรวจ ตรวจแล้วเจอขัด) | README (27 พ.ย. 2026) |
| F5 | b16 "AGUI พัฒนาร่วมกับ LangChain" | **เกินจริง** — AG-UI เป็น open standard ที่ CopilotKit สร้างเอง ("AG-UI, the open standard CopilotKit created" · "From CopilotKit, creators of AG-UI"); LangChain = partner อินทิเกรชันวันเปิดตัว (day-0) ร่วมกับ CrewAI/Mastra/AG2 → ข้อสงสัยของ Benz ถูก | copilotkit.ai/openbot · open.bot/blog/openbot-for-business-webinar · github.com/ag-ui-protocol/ag-ui README "born from CopilotKit's initial partnership with LangChain and CrewAI" |
| F6 | $29 Business (ที่ Benz ขอใส่) | **ตรง แต่ต้องเขียน "สูงสุด"** — pricing page: "Pay as you go Up to $29/user/month. A per-user rate that falls as your team grows" · annual = custom · +5% บน model spend เกิน $5,000/องค์กร/เดือน | open.bot/pricing (27 พ.ย. 2026) |
| F7 | "ฟรี personal" | **ตรง แต่มีเงื่อนไข** — desktop self-contained ฟรี · OpenBot Cloud ฟรีถึง 500 completed runs แล้ว $5/user/เดือน | open.bot/pricing |
| F8 | b24 Fail-Closed | **ครึ่งจริง** — rule gateway "deny always wins" จริง แต่ default action policy = allow ทุก action จนกว่า admin เขียนกฎ ("OpenBot is trusting on purpose", webinar 35:35) → ต้องเขียนด่านนี้ในส่วนความเสี่ยง | webinar blog (watch 35:35) |
| F9 | b13+b29 แยกคอมเสมือนรายตัว | **ครึ่งจริง** — default: "agents share one computer per person"; เฉพาะบอทที่ตั้ง "Isolated" ได้คอมของตัวเอง (webinar 34:47 · 1.0 blog "Isolated computers: mark a Bot as Isolated") → ประโยค "แต่ละตัวแยกเป็นอิสระ" ฟ่อนเกิน ต้อง scope เป็น opt-in รายบอท | webinar blog FAQ · copilotkit.ai/blog/introducing-openbot-1-0 |
| F10 | b46-47 SKILL.md กระจายวิธีผิด | **ครึ่งจริง** — มีด่านที่ draft ไม่ได้พูด: "Every skill Automatic Learning proposes waits for review, and nothing reaches a Bot until someone publishes it" (admin approve ก่อนกระจาย) → ความเสี่ยงยังจริง (ถ้า approve พลาด) แต่ต้องบอกว่ามีด่าน | 1.0 blog "Learning your admins approve" |
| F11 | b23 ตัดขาดจากเครือข่าย | **มีเงื่อนไข** — air-gapped installs ได้เฉพาะแผน annual | webinar blog "Air-gapped installs come with the annual plan" |
| F12 | b17 เฟรมเวิร์ก LangGraph/Google ADK/CrewAI/LlamaIndex | LangGraph ✓ Google ADK ✓ (webinar FAQ + 1.0 blog) · CrewAI ✓ (AG-UI partner) · **LlamaIndex = ไม่เจอในแหล่งที่เปิดจริง** — ต้องมีแหล่งก่อนคงในเนื้อ | webinar FAQ · 1.0 blog · AG-UI README |
| F13 | b2 ที่มา "เอกสารวิจัย OpenBot ของ CopilotKit" | **ไม่มีเอกสารวิจัย** — แหล่งจริง: (1) webinar "OpenBot for Business: AI Governance, Control & Ownership" 12 พ.ย. 2026 นาน 54 นาที (David McKay + Guido Vizoso, host Nathan Tarbert) (2) blog "Introducing OpenBot 1.0" 10 พ.ย. 2026 (3) blog "OpenBot for Business Webinar: AI Governance" 17 พ.ย. 2026 (4) README/docs → ต้องแทน genre-label "เอกสารวิจัย" + ใส่ลิงก์ตามที่ Benz สั่ง | open.bot/blog/openbot-for-business-webinar · luma.com/lxgxohto · copilotkit.ai/blog/introducing-openbot-1-0 |

**ข้อสังเกตเพิ่ม:** Source property ของหน้าระบุ "https://open.bot/ · YouTube Library · Knowledge Base — ตรวจ 26 พ.ย. 2026" ตรงกับ webinar 12 พ.ย. — draft จริงเรียบเรียงจาก webinar + blogs ไม่ใช่ research paper

## Publish-keys (รายการ "ต้องแก้ก่อน" = key เกรด publish ในอนาคต พร้อมข้อ 4/ควรปรับ เสียง/ต้นทุน/ย่อหน้าเข้าใจยาก)

K1 ชื่อผู้พัฒนา OpenBot.run = Synthetify Labs ตรงทั้งซีรีส์ (หรือระบุ "GitHub org nightly-labs" ถ้าต้องการ nuance นั้น)
K2 ตารางเทียบ (423df8d8) แก้ row 2 + เติม license row ให้ตรงกับข้อเท็จจริงที่ F9 ยืนยัน
K3 ที่มา = ลิงก์ webinar 12 พ.ย. + blogs แทนคำ "เอกสารวิจัย" (ตาม F13)
K4 สถานะ "อ่านจากเอกสาร ยังไม่ได้ลอง" อยู่ใน title/ต้นบท + ประโยคท้าย "พรพบว่า"→"พรสังเกตจากเอกสาร"
K5 disclosure Rakazo + อคติ + ลิงก์เทียบ ในชิ้นนี้เอง
K6 ย่อหน้า b49-50 แก้ตรงตามความหมายจริง (เอเจนต์แชร์คอมเดิมที่ไม่ได้ตั้ง Isolated — F9) หรือตัด
K7 เสียงชุดเดียวทั้งซีรีส์ (พร หรือ ผม — ตามที่ owner เลือก)
K8 ส่วนข้อจำกัด/ความเสี่ยงแยก 2 กลุ่ม รูปแบบนับเดียว
K9 เลขต้นทุนจริง (สูงสุด $29/user/เดือน Business + Cloud $5/500 runs) หรือประโยค "ต้องคำนวณเอง"
K10 แฮชแท็กแบรนด์ #Adduckivity #DuckOS #NeuroDivergent ครบ
K11 F4/F5/F8/F9/F10/F12 แก้ตาม fact audit ก่อนเผยแพร่
K12 บทสรุปตอบ "ใครควรใช้ / ใครไม่ควร" + ลิงก์บทเทียบ

**Keep-list (protected anchors):** ย่อหน้าแยกชื่อ OpenBot vs OpenBot.run (b9-11) · รายการข้อจำกัดเชิงปฏิบัติ (b31-43) · ประโยคคนควบคุมเบราว์เซอร์แทนบอทตอน 2FA (b26-27) · รูปแบบ [สาระ][เงื่อนไข][มุมสังเกต] (b52-60)

## สถานะ

- NO rewrite, NO Notion PATCH (learn-only directive) — publish-keys รอเกรดเมื่อ publish มา
- Residual: หน้า 423df8d8 ยังผิด row 2 + ไม่มี license row · หน้า 424df8d8-8126 ยังซ้ำ 2 ชุด (100 blocks) · เสียงซีรีสียัง ผม/พร ปนกัน — ทั้งหมด = decision list ให้ owner
