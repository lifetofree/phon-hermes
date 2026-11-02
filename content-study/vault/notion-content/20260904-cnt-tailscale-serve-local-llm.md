# LocalLLM, GPU อยู่ที่บ้าน แต่อยากแบกเป้เที่ยว แล้วงานไม่เสีย — จัดการได้ด้วย Tailscale serve

**Excerpt:** เลิกเปิด terminal ค้าง เลิกปวดหัวกับการ forward port ด้วย tailscale serve เปลี่ยนเครื่อง GPU ที่บ้านให้กลายเป็น private reverse proxy เข้าถึง ComfyUI และ llama-server ผ่านเบราว์เซอร์ได้จากทุกที่
**Laws:** [[🛡️ Law 3: Protect System]] · [[🛠️ Decision Protocol]]
**Site Category:** [[🛠️ Productivity Hacks]]
**Tags:** [[Adduckivity]] · [[DuckOS]] · [[NeuroDivergent]] · #Tailscale · [[LocalLLM]] · #HomeLab · [[SystemsFirst]] · [[DevOps]]

---

คราวที่แล้วพรเขียนเรื่อง "เลิกรัน Local LLM นอกบ้าน" — จบด้วยการรัน SSH เข้าเซิร์ฟเวอร์ที่บ้านแล้ว forward port กลับเครื่องตัวเอง มันได้ผล แต่ก็มีข้อเสียที่พรบอกไปตั้งแต่ตอนนั้น: ทุกครั้งที่ต้องใช้ ต้อง SSH ก่อนทุกครั้ง, terminal window ต้องเปิดค้าง, และถ้า laptop หลับไป connection ก็หลุด
.
ครั้งนี้พรเจอวิธีที่ง่ายกว่ามาก — tailscale serve — และพรอยากเล่าจากมุมที่คนมองข้ามที่สุดก่อน: ไม่ใช่การแชร์โมเดลให้คนอื่น แต่คือการใช้เครื่อง GPU ที่บ้านจากเครื่องไหนก็ได้ของตัวเอง แบบไม่ต้อง fixed IP ไม่ต้อง SSH ไม่ต้องไป forward port ที่ router ไม่ต้องปวดหัวกับการแปลงร่างเป็น Network Engineer
.
ตัวอย่างบนเครื่อง LocalLLM ของพร
ตอนนี้ PHON-SERVER ของพร (Linux, GPU 2 ใบ) มีของที่ใช้ประจำอยู่ 3 อย่าง:
พอนั่งอยู่นอกบ้าน อยากแตะงานอันไหนก็เปิด browser ไปที่ http://phon-server:8888 — พิมพ์ชื่อเครื่องเฉยๆ ไม่ใช่ IP ไม่ต้องจำว่าวันนี้ router แจกเลขอะไรให้เครื่อง server
ตัวอย่างคำสั่งที่ต้องรันบนเครื่อง server ครั้งเดียว ต่อ service:
.
เท่านี้ — ทุก device ที่ login อยู่ใน tailnet (notebook, มือถือ) เปิด URL พวกนี้ได้เลย ไม่มี SSH ไม่มี terminal ค้าง และถ้า device หลับหรือสลับเครือข่ายแล้วกลับมา มันใช้ได้ทันที เพราะ traffic โดน route ผ่าน Tailscale daemon ไม่ผูกกับ session ของใคร
.
ความลับที่ไม่ลับ → พรไม่ได้เขียนคำสั่งพวกนี้เอง ให้ ai เขียนให้ … จนจะเขียนอะไรไม่เป็นแล้ว!!
.
ออกแบบ → สั่งงาน → รอดูผลลัพธ์ → เที่ยว เอ้ย! ใช้งาน
.
แยกให้ออกก่อน: อะไรทำให้ "ไม่ต้อง fixed IP" — ตอบว่าไม่ใช่ serve
จุดนี้คนเข้าใจผิดกันเยอะมาก รวมตัวพรก่อนหน้านี้ด้วย
ชั้นที่ทำให้ไม่ต้อง fixed IP คือ tailnet + MagicDNS — ทุกเครื่องที่ลง Tailscale จะได้ IP ถาวรใน range 100.x.x.x พร้อมชื่อเครื่องที่เรียกได้เลย (phon-server) นี่มีมาตั้งแต่ติดตั้ง Tailscale แล้ว ยังไม่ต้องมี serve เลย อย่างเครื่องพร: llama-server bind 0.0.0.0:8080 อยู่ ดังนั้นวันนี้เปิด http://phon-server:8080 จาก laptop ก็ใช้ได้แล้ว
.
งั้น serve แก้ปัญหาอะไร? สองอย่างที่อ่านแล้วจี๊ด แต่โดน!!:
.
tailscale serve คือ reverse proxy ที่รันอยู่ใน daemon ของเครื่อง server เอง: app ยัง bind localhost อยู่อย่างนั้น (ปลอดภัยกับ LAN) แต่คนใน tailnet เข้าได้ผ่าน URL — สอง requirements ที่ขัดกันได้ทั้งคู่
กฎจำง่ายๆ: tailnet ให้ชื่อและเส้นทาง, serve เปิดประตูให้ service ที่ lock อยู่ใน localhost
.
พอใช้เองได้แล้ว — Serve vs Funnel
ขั้นถัดไปคือขยายจาก "ใช้เอง" เป็น "ให้คนอื่นใช้" และตรงนี้ Tailscale มี feature สองตัวที่คนสับสนกันมาก:
กฎเหล็ก: serve = ส่วนตัว, funnel = สาธารณะ — และ port เดียวกันรันทั้ง Serve + Funnel พร้อมกันไม่ได้ (คำสั่งล่าสุด wins — ถ้าสั่ง funnel หลัง serve port นั้นจะกลายเป็น public ทันที)
.
ถ้าจะเปิดให้คนนอกที่ไม่ใช่ Tailscale user:
.
มันสร้าง URL ที่ชี้ไปที่ relay server ของ Tailscale — relay มองไม่เห็น IP เครื่องเราและ decrypt ไม่ได้ แต่คิดดีๆ ก่อนใช้กับ GPU box: public = ใครก็ยิงได้ = กิน VRAM คุณฟรี
.
ฟีเจอร์ killer ตอนขยายไปหาทีม: Identity Headers
ใช้คนเดียวไม่ต้องสน แต่พอเชิญเพื่อนเข้า tailnet (แผนฟรีได้ 3 users) เพื่อมาใช้โมเดลร่วมกัน — feature นี้คือของฟรีที่แพงที่สุด
เมื่อ traffic มาผ่าน tailscale serve (ไม่ใช่ funnel) daemon จะเติม headers เหล่านี้เข้าไปให้ backend:
.
backend รู้ได้ทันทีว่าใครกำลังใช้ — ไม่ต้องมี API key, ไม่ต้องมี login page, ไม่ต้องเขียน auth system สักบรรทัด และ Tailscale strip headers พวกนี้จาก incoming request เสมอ ทำให้ spoof ไม่ได้
.
ข้อควรระวังที่ doc บอกตรงๆ: ให้ backend listen บน localhost เท่านั้น — ถ้าเปิด port ตรงสู่ LAN ใครก็ตั้ง header ตัวเองได้
.
คำเตือนเรื่อง version: CLI เปลี่ยนแล้วใน v1.52
.
ถ้าตาม tutorial เก่า (2024-2025) จะเจอ syntax เดิม:
.
ตอนนี้กลายเป็น target-based:
.
และมี subcommands: tailscale serve status, reset, get-config, set-config — config สะสมได้ (serve หลาย service พร้อมกัน ดูทั้งหมดด้วย status)
.
ต้องรู้ก่อนใช้: tailnet ต้องเปิด HTTPS certificates (ถ้ายังไม่เปิด CLI จะพาไปกดอนุญาตครั้งแรกครั้งเดียว) และ ACL ของ tailnet ใช้กับ traffic ของ Serve ด้วย
.
ข้อจำกัดของวิธีนี้:
.
สรุป: ใช้เมื่อไหร่ แบบไหน
.
สรุปแบบวิศวกรเป็ด
คราวก่อนพรใช้ SSH + port forwarding — เหมือนต่อสายชาร์จยาวจากบ้านมาที่ร้านกาแฟทุกครั้งที่จะใช้ ภาคนี้เริ่มจากตัวเอง: เครื่อง GPU อยู่บ้าน แต่ notebook กับมือถือของพรเปิด http://phon-server:<port> ได้จากไหนก็ได้ โดย app บน server ยัง lock อยู่บน localhost อย่างปลอดภัย — และเมื่อวันหนึ่งจะเชิญทีมเข้ามาใช้ พรก็รู้เลยว่าใครกำลังคุยกับ LocalLLM ของพรอยู่
.
คราวหน้าถ้าอยากทำให้ public จริงๆ จะมาเล่าเรื่อง Funnel + rate limiting กัน (เพราะ public = ต้องคิดเรื่อง quota หนักขึ้นอีกมาก)
.
ลองแล้วเป็นยังไงกันบ้าง? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้พรทำภาคต่อเรื่องไหน บอกได้เลยค้าบ
.
#Adduckivity #DuckOS #NeuroDivergent #Tailscale #LocalLLM #HomeLab #SystemsFirst #DevOps
===========
FB Version
===========
คราวที่แล้วพรเขียนเรื่อง "เลิกรัน Local LLM นอกบ้าน" — จบด้วยการรัน SSH เข้าเซิร์ฟเวอร์ที่บ้านแล้ว forward port กลับเครื่องตัวเอง มันได้ผล แต่ก็มีข้อเสียที่พรบอกไปตั้งแต่ตอนนั้น: ทุกครั้งที่ต้องใช้ ต้อง SSH ก่อนทุกครั้ง, terminal window ต้องเปิดค้าง, และถ้า laptop หลับไป connection ก็หลุด
.
ครั้งนี้พรเจอวิธีที่ง่ายกว่ามาก — tailscale serve — และพรอยากเล่าจากมุมที่คนมองข้ามที่สุดก่อน: ไม่ใช่การแชร์โมเดลให้คนอื่น แต่คือการใช้เครื่อง GPU ที่บ้านจากเครื่องไหนก็ได้ของตัวเอง แบบไม่ต้อง fixed IP ไม่ต้อง SSH ไม่ต้องไป forward port ที่ router ไม่ต้องปวดหัวกับการแปลงร่างเป็น Network Engineer
.
ตัวอย่างบนเครื่อง LocalLLM ของพร
ตอนนี้ PHON-SERVER ของพร (Linux, GPU 2 ใบ) มีของที่ใช้ประจำอยู่ 3 อย่าง:
พอนั่งอยู่นอกบ้าน อยากแตะงานอันไหนก็เปิด browser ไปที่ http://phon-server:8888 — พิมพ์ชื่อเครื่องเฉยๆ ไม่ใช่ IP ไม่ต้องจำว่าวันนี้ router แจกเลขอะไรให้เครื่อง server
ตัวอย่างคำสั่งที่ต้องรันบนเครื่อง server ครั้งเดียว ต่อ service:
.
tailscale serve --http=8080 localhost:8080   # llama-server
.
เท่านี้ — ทุก device ที่ login อยู่ใน tailnet (notebook, มือถือ) เปิด URL พวกนี้ได้เลย ไม่มี SSH ไม่มี terminal ค้าง และถ้า device หลับหรือสลับเครือข่ายแล้วกลับมา มันใช้ได้ทันที เพราะ traffic โดน route ผ่าน Tailscale daemon ไม่ผูกกับ session ของใคร
.
ความลับที่ไม่ลับ → พรไม่ได้เขียนคำสั่งพวกนี้เอง ให้ ai เขียนให้ … จนจะเขียนอะไรไม่เป็นแล้ว!!
ออกแบบ → สั่งงาน → รอดูผลลัพธ์ → เที่ยว เอ้ย! ใช้งาน
.
แยกให้ออกก่อน: อะไรทำให้ "ไม่ต้อง fixed IP" — ตอบว่าไม่ใช่ serve
จุดนี้คนเข้าใจผิดกันเยอะมาก รวมตัวพรก่อนหน้านี้ด้วย
ชั้นที่ทำให้ไม่ต้อง fixed IP คือ tailnet + MagicDNS — ทุกเครื่องที่ลง Tailscale จะได้ IP ถาวรใน range 100.x.x.x พร้อมชื่อเครื่องที่เรียกได้เลย (phon-server) นี่มีมาตั้งแต่ติดตั้ง Tailscale แล้ว ยังไม่ต้องมี serve เลย อย่างเครื่องพร: llama-server bind 0.0.0.0:8080 อยู่ ดังนั้นวันนี้เปิด http://phon-server:8080 จาก laptop ก็ใช้ได้แล้ว
.
งั้น serve แก้ปัญหาอะไร? สองอย่างที่อ่านแล้วจี๊ด แต่โดน!!:
.
tailscale serve คือ reverse proxy ที่รันอยู่ใน daemon ของเครื่อง server เอง: app ยัง bind localhost อยู่อย่างนั้น (ปลอดภัยกับ LAN) แต่คนใน tailnet เข้าได้ผ่าน URL — สอง requirements ที่ขัดกันได้ทั้งคู่
กฎจำง่ายๆ: tailnet ให้ชื่อและเส้นทาง, serve เปิดประตูให้ service ที่ lock อยู่ใน localhost
.
สรุปแบบวิศวกรเป็ด
คราวก่อนพรใช้ SSH + port forwarding — เหมือนต่อสายชาร์จยาวจากบ้านมาที่ร้านกาแฟทุกครั้งที่จะใช้ ภาคนี้เริ่มจากตัวเอง: เครื่อง GPU อยู่บ้าน แต่ notebook กับมือถือของพรเปิด http://phon-server:<port> ได้จากไหนก็ได้ โดย app บน server ยัง lock อยู่บน localhost อย่างปลอดภัย — และเมื่อวันหนึ่งจะเชิญทีมเข้ามาใช้ พรก็รู้เลยว่าใครกำลังคุยกับ LocalLLM ของพรอยู่
.
คราวหน้าถ้าอยากทำให้ public จริงๆ จะมาเล่าเรื่อง Funnel + rate limiting กัน (เพราะ public = ต้องคิดเรื่อง quota หนักขึ้นอีกมาก)
.
อ่านฉบับเต็มได้ใน comment นะค้าบ
.
ลองแล้วเป็นยังไงกันบ้าง? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้พรทำภาคต่อเรื่องไหน บอกได้เลยค้าบ
.
#Adduckivity #DuckOS #NeuroDivergent #Tailscale #LocalLLM #HomeLab #SystemsFirst #DevOps
===========

*Synced: 2026-11-02 19:48 +07 · [Notion](https://www.notion.so/3d1df8d88d8c802cb65df318450ba851) · ✅ Published*