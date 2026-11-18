<!--
Status: draft v1 (2026-11-18 — owner brief: "draft content การติดตั้งและการใช้งานเบื้องต้นของ rakazo ใน local ผ่าน docker ในมุมของผู้ใช้จริงอย่างพร + ขุดหลักฐานจากการใช้จริง")
FORM: TECH v2 — first-look review จาก deployment จริงบนเครื่องเรา (ไม่ใช่ข่าวประกาศ, ไม่ใช่ docs recap — ทุกตัวเลขยืนยันจากเครื่องนี้ได้)
REGISTER: TECH — เลขอารบิก form-legitimate, ชื่อผลิตภัณฑ์/ไฟล์/commit ในเนื้อได้, พร 1 (ผู้ใช้จริงของเซิร์ฟเวอร์), เรา = มุมผู้ใช้
FACT LEDGER (ยืนยันจากเครื่องจริง 2026-11-18): (1) ไฟล์ติดตั้ง 3 ไฟล์ ~/rakazo — docker-compose.images.yml + install-images.sh + restrict-computer-egress.sh (mtime 15:51 16 พ.ย.) (2) images ghcr.io/elie222/rakazo/app:edge 2.82GB + computer:edge 2.39GB (3) compose up 15:52 16 พ.ย. — 6 containers (web/api/worker/supervisor/postgres:16 + bot sandbox) — 4 ตัวรายงาน healthy ตอนเช็ค (4) web 127.0.0.1:5173 HTTP 200 + tailscale serve tailnet-only (5) sandbox mounts: /mnt/hermes-agent ro + /mnt/inbox rw + volume rakazo_appdata (6) โมเดลผ่าน llama-server พอร์ต 8080 host.docker.internal (7) งานจริงชุดแรก: 16 พ.ย. 23:05 ซิงก์ 3 ไฟล์ YouTube Library push branch rakazo/youtube-library (eedbcb1 บน origin ยืนยัน ls-remote) → 403 (token เขียน 23:33 หลัง push, bot ไม่ retry — รายงานสถานะเก่า) → 18 พ.ย. cherry-pick ขึ้น main เป็น 3e6f0eb (3 ไฟล์ 225 แถว) (8) ข้อจำกัด: egress script ยังไม่รัน, token scope กว้าง, RAM cap 2GB
VENDOR CLAIMS (reported speech เท่านั้น): upstream README (github.com/elie222/rakazo) — "open source, self-hosted… persistent AI teammates with their own memory, routines, apps, and computer… your own model" — ทุกประโยคติดป้ายทีมผู้ทำ
SIBLING GUARD: #103 zcode-review (TECH review SaaS) + 20260904 autoclaw-zcode-combo — axis แยก = self-host deployment จริงบนเครื่องเรา + หลักฐาน machine-verifiable (containers/git/ports) vs รีวิวจาก docs; คำ ZCode/GLM/Autoclaw = 0
GUARDS: พร 1 real (เครือข่ายส่วนตัวของพร) + FP พร-lookalike ×2 (ขึ้น**พร้อม**กัน / ไฟล์**พร้อม** — ตระกูล พร้อม, ตัวนับรายงาน 3 = รวม FP ตาม lesson 5) / เรา 5 real (ตัวนับรายงาน 3 = undercount จาก compound เราเอง/เรา compose) / คุณ-ผม-คับ-ฉัน 0 / เพราะ 0 / sibling ZCode/GLM/Autoclaw 0 / odd codepoints form-legitimate (TECH): ',' ×9 ใน tech-lists + '/' ×2 (ชื่อ branch rakazo/youtube-library + retry/rebase)
SECRET HYGIENE: ไม่มีค่าใดจาก .env ในเนื้อ; hostname tailscale (tailnet-only) อยู่ header เท่านั้น — เนื้อพูดถึงแบบ "โดเมนผ่าน tailscale"
Notion: POST ใหม่ Content Drafts DB หลัง slug-check | Status draft รอ Benz r1
-->

# Rakazo บนเครื่องเราเอง — บันทึก 3 วันแรกที่ทีม AI ทำงานจริงบน Docker

### ทุกตัวเลขในบทนี้ยืนยันได้จากเครื่องที่ติดตั้งจริง — containers, git log, และเหตุการณ์แรกที่เจอตามเวลาจริง

.

## Rakazo คืออะไร

ทีมผู้ทำระบุใน README ว่า Rakazo เป็น open source ที่ self-host ได้ — ทีม AI ที่มีความจำ กิจวัตร แอป และคอมพิวเตอร์ของตัวเอง รันบนเครื่องของเราด้วยโมเดลที่เราเลือกเอง

โครงจริงบนเครื่องเรากว้างกว่าที่คิด — 5 containers หลัก (web, api, worker, supervisor, postgres:16) รันบน image เดียว และอีกหนึ่ง container แยกต่างหากคือ "คอมพิวเตอร์" ที่บอตแต่ละตัวลงไปทำงาน

.

## ติดตั้งผ่าน Docker จริง ๆ แล้วเบากว่าที่คิด

ของที่ต้องมีจริง ๆ มี 3 ไฟล์ — docker-compose.images.yml, สคริปต์ดึง image จาก ghcr.io, และสคริปต์ล็อกการออกอินเทอร์เน็ตของ sandbox ที่ยังเก็บไว้ไม่ได้รัน

สอง image หลักขนาดรวมประมาณ 5.2GB — ตัวแอป 2.82GB กับตัวคอมพิวเตอร์ของบอต 2.39GB

เรา compose up ตอนบ่ายวันที่ 16 พ.ย. — 15:52 ทั้งหก container ขึ้นพร้อมกันหมด และเมื่อเช็คอีกครั้งหลังผ่านไปสองวัน สี่ตัวหลักยังรายงานสถานะ healthy

เข้าใช้งานได้สองทาง — พอร์ต 5173 บน localhost ของเครื่อง และผ่านโดเมนของ tailscale ที่เปิดให้เฉพาะอุปกรณ์ในเครือข่ายส่วนตัวของพรเท่านั้น

.

## จุดที่ต่างจากเว็บ AI ทั่วไป — sandbox แตะของจริงในเครื่อง

sandbox ของแต่ละบอต mount โฟลเดอร์จริงเข้าไป — repo งานเห็นแบบ read-only, โฟลเดอร์รับส่งงานเห็นแบบอ่าน-เขียน นี่คือชั้นที่ทำให้บอตทำงานกับไฟล์จริงได้ ไม่ใช่แค่แชต

โมเดลก็ไม่ต้องจ่ายค่า API ใหม่ — บอตเรียกใช้ llama-server ที่รันอยู่บนเครื่องนี้อยู่แล้วผ่านพอร์ต 8080

บอตตัวแรกได้งานจริงไป — ซิงก์ไลบรารีคลิป YouTube จาก Notion ขึ้น branch ของตัวเองใน repo

.

## เหตุการณ์จริงวันแรก — push โดน 403

16 พ.ย. 23:05 บอตซิงก์เสร็จ 3 ไฟล์สรุปคลิป แล้ว push ขึ้น branch rakazo/youtube-library — โดน 403

สาเหตุที่ขุดเจอสอนอะไรหลายอย่าง — token ของบอตถูกเขียนลงไฟล์ credential ตอน 23:33 แต่มัน push ก่อนไฟล์พร้อม แล้วไม่มีกลไก retry ก็เลยค้างรายงานว่ายังติด 403 ทั้งที่ตอนหลัง push ได้สบาย

**บทเรียนอยู่ที่กระบวนการ ไม่ใช่ตัวโมเดล**

บอตต้องถูกออกแบบให้ pull --rebase ก่อน push และถ้าโดน 403 ต้องลองซ้ำอีกรอบก่อนสรุปว่าล้มเหลว

18 พ.ย. งานชุดแรกปิดจริง — cherry-pick 3 ไฟล์นั้นขึ้น main เป็น commit 3e6f0eb รวม 225 บรรทัดสรุปคลิป

.

## ข้อจำกัดที่ยังค้างตอนนี้

สคริปต์ล็อก egress ยังไม่ได้รัน — sandbox ยังออกอินเทอร์เน็ตได้เต็ม ๆ

token ของบอตยังเป็น scope กว้าง ควรย่อยเป็น fine-grained ที่แตะได้เฉพาะ repo ของมัน

ทรัพยากรต่อบอตถูกจำกัด RAM 2GB — งานหนักอาจต้องขยับเพดาน

.

## #สรุปแบบวิศวกรเป็ด

การติดตั้ง — compose up ครั้งเดียว 6 containers ขึ้นครบ ใช้ต่อได้ทันที

ที่แพงกว่าการติดตั้ง — กระบวนการ บอตที่แตะไฟล์จริงต้องมีกติกา retry/rebase ออกแบบไว้ก่อน ไม่งั้นงานแรกก็ค้างแบบ 403

ที่ควรทำต่อ — ล็อก egress ย่อย scope ของ token แล้วค่อยปล่อยงานถัดไป

.

#Adduckivity #DuckOS #NeuroDivergent #SelfHosted #Docker #AI
