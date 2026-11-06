<!--
pair #103 (zcode-review-2026) — TECH form (v2 line-per-sentence ground truth) — news/tool-review lane
ORIGIN: owner brief (2026-11-06): "research หาข้อมูลเกี่ยวกับ ZCode ของ z.ai และเอามาทำ draft review แบบ adduckivity แล้วเอาลง notion เลย"

RESEARCH (primary, ตรวจ 2026-11-06):
- zcode.z.ai/en: "Official Harness for GLM-5.3, taking multi-agent development further — Simple, Fast, Vibe-Ready"; multi-agent + control from anywhere
- Products: desktop app (macOS/Windows/Linux) + browser view + terminal agent; repo github.com/zai-org/ZCode (Apache-2.0 ตาม munderdifflin — verify เองใน repo ถ้าจะอ้าง license)
- Core features (docs nav): ZCode Agent (default self-dev agent), Goal Mode, Browser Automation, Task & File Management, Wiki Memory, Automations, Idle-time Task, Edit History, Remote Development, Remote Control, Bot Channel (WeChat/Feishu/Telegram), Subagents, Plugin, Skill, MCP, Command Hooks, Usage Stats, Safety Confirmation
- Goal Mode (docs/goal): /goal <objective> → agent ทำงานเป็นรอบ, จบรอบมี verification แยก — เช็คว่าเป้าสำเร็จจาก "real evidence: changed files, command output, test results" ไม่นับ plan/checklist/เสียงสรุป; to-do ค้าง = ไม่ปิด goal; pause/resume/clear, state อยู่รอดข้าม session; งบหมด = หยุดเอง
- GLM-5.3 (agents docs): 1M context "stable", long-horizon coding benchmark ใกล้/เกิน closed frontier บางตัว (claim ของผู้ผลิต), flexible effort = thought level toggle, RL-trained agentic + anti-hack mechanisms
- Pricing: Lite $12.6/mo (ปกติ $18) 10,000 credits/สัปดาห์ · Pro $56 (ปกติ $80) 6× Lite + MCP curated · Max $117.6 (ปกติ $168) 14× Lite — "Prices may change. Final details on z.ai"; plans ใช้ได้กับ 20+ agent tools รวม Claude Code
- Bot control: สั่ง/เสริมงานจาก WeChat, Feishu, Telegram
- ต่างจากโพสต์เก่า (sibling 20260904 autoclaw-zcode-combo): อันนั้นเป็น combo-workflow (ZCode+AutoClaw ในแผนเดียว) — บทนี้ review ZCode ตัวเดียว ณ วันนี้: harness ครบทั้ง desktop+web+terminal, Goal Mode semantics เข้มขึ้น (verification evidence-based + budget), ราคา Lite ลดจาก $18 → $12.6 promo ยังอยู่

ANGLE (เลือกให้ต่างจาก sibling): "harness ที่โตมากับโมเดลตัวเอง" — รีวิวผ่านสายตา harness (ต่อ KB AI Harness: ผู้ให้บริการ model เขียน harness เอง = vertical integration) — จุดขายไม่ใช่โมเดลเก่ง แต่คือวงจร goal → รอบ → verification ที่ออกแบบมาให้โมเดล long-horizon ใช้กำลังได้เต็ม
CUT LIST (zero-count): โปรโมชั่น 20% เป็นตัวเลขหลัก (ลดได้), คำสรรเสริญเกิน, ?(ในเนื้อ), โจมตีแบรนด์อื่น
FORMAT: TECH v2 line-per-sentence — stat-line opener, ตารางได้ (TECH lane), real benchmark + disclaimer, two-fork ending, หัวข้อ ## 0N:, bold ตาม TECH form, ท้าย #สรุปแบบวิศวกรเป็ด + hashtags
Notion: Content Drafts DB 3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520, Platform TECH + general
-->

# ZCode (z.ai) รีวิว 2026 — harness ทางการของ GLM-5.3 ที่ทำงานยาวได้จริงไหม

## 01: ข่าวเปิด — ทางการประกาศเป็น harness ของโมเดลตัวเอง

ZCode คือ coding workbench ของ z.ai ประกอบด้วย desktop app, มุมมองแบบเว็บ และ agent ในเทอร์มินัล

ตัวเลขเปิด: แผน GLM Coding Lite $12.6 ต่อเดือน (ราคาปกติ $18) ให้ 10,000 credits ต่อสัปดาห์ ใช้ได้กับ agent ฝั่งอื่นด้วยมากกว่า 20 ตัว

repo เปิดสาธารณะที่ github.com/zai-org/ZCode และมี docs ครบทั้งตัว agent, Goal Mode, Bot Channel, Remote Control

## 02: สเปกหลัก — อ่านจาก docs ราย feature

| ชิ้นส่วน | ของจริงในเอกสาร |
|---|---|
| โมเดลหลัก | GLM-5.3 + GLM-5.3-Flash ในตัว (มัลติโมดัล เช่น อ่าน screenshot) |
| บริบท | 1M tokens — จุดขายคือ "เสถียรตลอดงานยาว" ไม่ใช่จำนวน token ล้วน ๆ |
| Goal Mode | /goal → ทำงานเป็นรอบ จบรอบมี verification แยก ถ้ายังไม่ถึงเป้าจะเริ่มรอบใหม่เอง |
| หลักฐานจบงาน | เช็คจาก changed files, command output, test results — ไม่นับแผนหรือประโยคสรุป |
| ควบคุมระยะไกล | Bot Channel + Remote Control ผ่าน WeChat / Feishu / Telegram |
| ระบบเสริม | Subagents, Skill, MCP, Command Hooks, Wiki Memory, Automations, Idle-time Task, Safety Confirmation |
| โอเพนซอร์ส | repo เผยแพร่สาธารณะ (license ตรวจที่ repo ก่อนอ้าง) |

หัวใจที่ docs ย้ำ: verification มองหา "หลักฐานจริง" — ไฟล์ที่ถูกแก้ ผลรันคำสั่ง ผลเทสต์ ส่วนแผนการทำงานหรือประโยคที่ฟังดูจบแล้วไม่นับ

และตราบใดที่ to-do ยังค้าง ระบบจะไม่ประกาศว่าเป้าสำเร็จ

## 03: ทดลองอ่านเป็น harness — จุดที่ต่างจาก IDE coding tool ทั่วไป

จาก KB ฝั่ง AI Harness (บทแม่): โมเดลเปล่ายังไม่ใช่ agent สิ่งรอบโมเดลคือ harness

จุดที่ ZCode ต่างคือ ผู้ผลิตโมเดลเขียน harness เอง แล้วออกแบบมาให้จุดแข็งของโมเดลทำงานได้เต็ม

Goal Mode ไม่ใช่แค่ปุ่มวนงานอัตโนมัติ — มันคือกลไกบังคับคุณภาพ 3 ชั้น

ชั้นแรก ปั้นงานเป็นรอบ แต่ละรอบจบด้วยการตรวจแยกต่างหาก

ชั้นสอง บังคับหลักฐาน ไม่ยอมรับคำสรุปลอย ต้องเป็นไฟล์ที่แก้ ผลรัน ผลเทสต์

ชั้นสาม งบใช้จ่ายต่อ goal หมดเมื่อไหร่ หยุดเอง ไม่กิน quota แบบเงียบ ๆ

ส่วนโมเดลถูกเทรนด้วย RL สำหรับงาน agent ยาว และมีกลไกกันตีโพย (anti-hack) ไม่ให้โมเดลหาทางลัดเพื่อตอบแต้มผิวเผิน

คู่นี้จึงอ่านเป็นการออกแบบระบบรอบโมเดลเพื่อปล่อยความสามารถ long-horizon ของมัน ไม่ใช่แค่หุ้ม UI สวย

## 04: จุดบวก ✅

- **Goal Mode มีฟันจริง** — verification แยกชั้น + ต้องพิสูจน์ด้วยหลักฐานจริง (ไฟล์/คำสั่ง/เทสต์) ไม่ใช่เสียงฟันธงของโมเดล
- **ควบคุมจากมือถือได้จริง** — Bot Channel WeChat/Feishu/Telegram + Remote Control ใน docs ไม่ใช่แค่มุมโฆษณา
- **แผนครอบข้ามเครื่องมือ** — credits ใช้ได้กับ 20+ agent tools รวม Claude Code ลดความเสี่ยงล็อกขา
- **repo สาธารณะ + docs ละเอียดระดับกลไก** — Goal Mode อธิบายถึงระดับการเก็บ state, การหยุดเมื่องบหมด, และเคสที่ set goal ไม่ได้
- **ราคาจุดต่ำสุดของตลาดแผน coding** — Lite $12.6 ต่อเดือน ในระดับเดียวกับกาแฟสัปดาห์ละสองแก้ว

## 05: ข้อสังเกต ⚠️

- ตัวเลข benchmark ฝั่งโมเดลมาจากผู้ผลิตเอง — ยังไม่มีหลักฐานอิสระในสิ่งที่อ่านมา ใช้เป็น "ที่อ้างสิทธิ์" ไม่ใช่ข้อสรุป
- license ของ repo ควรเช็คเองที่ repo ก่อนอ้างว่าโอเพนซอร์สแบบไหน
- ราคาเป็นโปรโมชั่นที่หน้าเว็บระบุว่าเปลี่ยนได้ — ตรวจราคาจริงวันตัดสินใจ
- Goal Mode ใช้คู่กับ execution mode อื่นไม่ได้ทุกแบบ (ขัดกับ Plan mode ตาม docs) — ต้องเลือกโหมดก่อนตั้งเป้า
- ระบบรอบตัวใหญ่ (subagents, hooks, automations, wiki memory) = โค้งการเรียนรู้จริง ถ้าแค่ถาม-ตอบ+แก้โค้ด ใช้ไม่ถึงครึ่ง

## 06: เทียบหน้าต่างเวลา — กับโพสต์ combo เดือน ก.ย.

เดือน ก.ย. เราเขียนมุมจับคู่ (ZCode + AutoClaw ในแผนเดียว) — จุดขายคือสองเครื่องมือใช้ credits ร่วมกัน

วันนี้มุมที่ชัดขึ้นคือ เจ้าของโมเดลลงทุนเขียน harness ของตัวเองเต็มตัว — desktop, web, terminal, bot, ระบบตรวจงานอัตโนมัติ

สิ่งที่เปลี่ยนไม่ใช่ฟีเจอร์ แต่คือทิศทาง: การแข่งขันย้ายจากโมเดลเดี่ยว ไปเป็นคู่ (model × harness) แล้ว

## 07: Two-fork — ควรใช้ไหม

**ใช่ ถ้า** — งานเรามีเป้าหมายที่พูดจบในประโยคเดียวแต่ต้องทำหลายรอบ (refactor ทั้งโมดูล เก็บเทสต์ให้ผ่าน), มีงบรายเดือนอยากจุดต่ำ, และอยากสั่ง/เสริมงานจากมือถือระหว่างวัน

**เลี่ยง ถ้า** — งานสั้นตอบจบในรอบเดียว (โหมดปกติก็พอ Goal Mode ใช้ไม่ถึง), ต้องการ benchmark อิสระก่อนตัดสินใจ, หรือจะอ้าง license/ราคา — อย่าลืมว่าสองอย่างนี้ยังต้องเช็คที่ต้นทางวันตัดสินใจ

## บทสรุปจากพร

ZCode น่าจับตาไม่ใช่เพราะโมเดลเก่ง แต่เพราะมันเป็นหลักฐานชัดชิ้นแรก ๆ ที่เห็นว่า เจ้าของโมเดลเขียน harness ให้โมเดลตัวเองแบบจริงจัง

Goal Mode ที่บังคับหลักฐานจบงาน คือสิ่งที่ทุก harness ต้องมีไม่ช้า — ไม่ใช่แค่ของ z.ai

จับตาต่อว่าสนามรายอื่นจะตามด้วยระบบ verification แบบไหน

**โมเดลเดี่ยวเคยเป็นสินค้า — วันนี้คู่ (model × harness) ต่างหากที่เป็นสินค้า**

#Adduckivity #DuckOS #AI #GLM #ZCode
