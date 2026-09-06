<!-- Archived from https://wp.adduckivity.com/20260904-cnt-tailscale-serve-local-llm/ on 2026-09-04 by sync_wp_posts.py -->
Title: LocalLLM, GPU อยู่ที่บ้าน แต่อยากแบกเป้เที่ยว แล้วงานไม่เสีย — จัดการได้ด้วย Tailscale serve
Date: 2026-09-04T16:10:49
Link: https://wp.adduckivity.com/20260904-cnt-tailscale-serve-local-llm/
-->

LocalLLM, GPU อยู่ที่บ้าน แต่อยากแบกเป้เที่ยว แล้วงานไม่เสีย — จัดการได้ด้วย Tailscale serve

คราวที่แล้วพรเขียนเรื่อง “เลิกรัน Local LLM นอกบ้าน” — จบด้วยการรัน SSH เข้าเซิร์ฟเวอร์ที่บ้านแล้ว forward port กลับเครื่องตัวเอง มันได้ผล แต่ก็มีข้อเสียที่พรบอกไปตั้งแต่ตอนนั้น: ทุกครั้งที่ต้องใช้ ต้อง SSH ก่อนทุกครั้ง, terminal window ต้องเปิดค้าง, และถ้า laptop หลับไป connection ก็หลุด

.

ครั้งนี้พรเจอวิธีที่ง่ายกว่ามาก — tailscale serve — และพรอยากเล่าจากมุมที่คนมองข้ามที่สุดก่อน: ไม่ใช่การแชร์โมเดลให้คนอื่น แต่คือการใช้เครื่อง GPU ที่บ้านจากเครื่องไหนก็ได้ของตัวเอง แบบไม่ต้อง fixed IP ไม่ต้อง SSH ไม่ต้องไป forward port ที่ router ไม่ต้องปวดหัวกับการแปลงร่างเป็น Network Engineer

.

ตัวอย่างบนเครื่อง LocalLLM ของพร

ตอนนี้ PHON-SERVER ของพร (Linux, GPU 2 ใบ) มีของที่ใช้ประจำอยู่ 3 อย่าง:

llama-server ที่ port 8080 — รัน Qwen3 27B quant Q4_K_M offload ลง GPU หรือ model อื่นๆ

ComfyUI ที่ port 8188 — งานรูป, คลิป

Unsloth Studio ที่ port 8888 — รัน model บางตัวที่อยากลองแบบไวๆ หรือ custom model ที่ทาง Unsloth custom มาเป็นพิเศษ (PS. ตอนนี้ Huggingface ถูกซื้อโดย Nvidia ไปแล้ว มารอดูราคาการ์ดจอ Nvidia กันคับ)

พอนั่งอยู่นอกบ้าน อยากแตะงานอันไหนก็เปิด browser ไปที่ http://phon-server:8888 — พิมพ์ชื่อเครื่องเฉยๆ ไม่ใช่ IP ไม่ต้องจำว่าวันนี้ router แจกเลขอะไรให้เครื่อง server

ตัวอย่างคำสั่งที่ต้องรันบนเครื่อง server ครั้งเดียว ต่อ service:

.

tailscale serve --http=8888 localhost:8888 # Unsloth Studio
tailscale serve --http=8188 localhost:8188 # ComfyUI
tailscale serve --http=8080 localhost:8080 # llama-server

เท่านี้ — ทุก device ที่ login อยู่ใน tailnet (notebook, มือถือ) เปิด URL พวกนี้ได้เลย ไม่มี SSH ไม่มี terminal ค้าง และถ้า device หลับหรือสลับเครือข่ายแล้วกลับมา มันใช้ได้ทันที เพราะ traffic โดน route ผ่าน Tailscale daemon ไม่ผูกกับ session ของใคร

.

ความลับที่ไม่ลับ → พรไม่ได้เขียนคำสั่งพวกนี้เอง ให้ ai เขียนให้ … จนจะเขียนอะไรไม่เป็นแล้ว!!

.

ออกแบบ → สั่งงาน → รอดูผลลัพธ์ → เที่ยว เอ้ย! ใช้งาน

.

แยกให้ออกก่อน: อะไรทำให้ “ไม่ต้อง fixed IP” — ตอบว่าไม่ใช่ serve

จุดนี้คนเข้าใจผิดกันเยอะมาก รวมตัวพรก่อนหน้านี้ด้วย

ชั้นที่ทำให้ไม่ต้อง fixed IP คือ tailnet + MagicDNS — ทุกเครื่องที่ลง Tailscale จะได้ IP ถาวรใน range 100.x.x.x พร้อมชื่อเครื่องที่เรียกได้เลย (phon-server) นี่มีมาตั้งแต่ติดตั้ง Tailscale แล้ว ยังไม่ต้องมี serve เลย อย่างเครื่องพร: llama-server bind 0.0.0.0:8080 อยู่ ดังนั้นวันนี้เปิด http://phon-server:8080 จาก laptop ก็ใช้ได้แล้ว

.

งั้น serve แก้ปัญหาอะไร? สองอย่างที่อ่านแล้วจี๊ด แต่โดน!!:

เครื่องมือ AI ส่วนใหญ่ bind 127.0.0.1 โดย default — Unsloth Studio (8888), ComfyUI (8188) ก่อนจะสั่ง -listen 0.0.0.0 นั่นแปลว่าจากเครื่องอื่นเข้าไม่ได้เลย ทางแก้แบบตรงๆ คือสั่งให้ app เปิด 0.0.0.0 — ซึ่งแปลว่าทั้ง LAN เห็น รวมถึงคนที่ไม่ควรเห็นด้วย และ app พวกนี้ส่วนใหญ่ไม่มี login ให้ด้วย

HTTPS ที่ browser เชื่อ — certificate จัดให้อัตโนมัติ ไม่มีหน้าเตือน ไม่ต้องทำ cert เอง

.

tailscale serve คือ reverse proxy ที่รันอยู่ใน daemon ของเครื่อง server เอง: app ยัง bind localhost อยู่อย่างนั้น (ปลอดภัยกับ LAN) แต่คนใน tailnet เข้าได้ผ่าน URL — สอง requirements ที่ขัดกันได้ทั้งคู่

กฎจำง่ายๆ: tailnet ให้ชื่อและเส้นทาง, serve เปิดประตูให้ service ที่ lock อยู่ใน localhost

.

พอใช้เองได้แล้ว — Serve vs Funnel

ขั้นถัดไปคือขยายจาก “ใช้เอง” เป็น “ให้คนอื่นใช้” และตรงนี้ Tailscale มี feature สองตัวที่คนสับสนกันมาก:

หัวข้อServeFunnel
ใครเข้าถึงได้คนใน tailnet (คนที่ login แล้ว)ทุกคนบนอินเทอร์เน็ต
ใช้ทำอะไรใช้เอง / แชร์ service ให้ทีมเปิด service สาธารณะ
Identity headers✅ มี (รู้ว่าเป็นใคร)❌ ไม่มี
Port ที่ใช้ได้ทุก port (HTTP/HTTPS/TCP)443, 8443, 10000 เท่านั้น
สถานะStableBeta

กฎเหล็ก: serve = ส่วนตัว, funnel = สาธารณะ — และ port เดียวกันรันทั้ง Serve + Funnel พร้อมกันไม่ได้ (คำสั่งล่าสุด wins — ถ้าสั่ง funnel หลัง serve port นั้นจะกลายเป็น public ทันที)

.

ถ้าจะเปิดให้คนนอกที่ไม่ใช่ Tailscale user:

.

tailscale funnel localhost:8080

มันสร้าง URL ที่ชี้ไปที่ relay server ของ Tailscale — relay มองไม่เห็น IP เครื่องเราและ decrypt ไม่ได้ แต่คิดดีๆ ก่อนใช้กับ GPU box: public = ใครก็ยิงได้ = กิน VRAM คุณฟรี

.

ฟีเจอร์ killer ตอนขยายไปหาทีม: Identity Headers

ใช้คนเดียวไม่ต้องสน แต่พอเชิญเพื่อนเข้า tailnet (แผนฟรีได้ 3 users) เพื่อมาใช้โมเดลร่วมกัน — feature นี้คือของฟรีที่แพงที่สุด

เมื่อ traffic มาผ่าน tailscale serve (ไม่ใช่ funnel) daemon จะเติม headers เหล่านี้เข้าไปให้ backend:

Tailscale-User-Login — เช่น phon@example.com

Tailscale-User-Name — display name

Tailscale-User-Profile-Pic — URL รูปโปรไฟล์ (ถ้ามี)

.

backend รู้ได้ทันทีว่าใครกำลังใช้ — ไม่ต้องมี API key, ไม่ต้องมี login page, ไม่ต้องเขียน auth system สักบรรทัด และ Tailscale strip headers พวกนี้จาก incoming request เสมอ ทำให้ spoof ไม่ได้

.

ข้อควรระวังที่ doc บอกตรงๆ: ให้ backend listen บน localhost เท่านั้น — ถ้าเปิด port ตรงสู่ LAN ใครก็ตั้ง header ตัวเองได้

.

คำเตือนเรื่อง version: CLI เปลี่ยนแล้วใน v1.52

.

ถ้าตาม tutorial เก่า (2024-2025) จะเจอ syntax เดิม:

.

# แบบเก่า (v<1.52)
tailscale serve 443 --bg <http://127.0.0.1:8080>

ตอนนี้กลายเป็น target-based:

.

# แบบใหม่
tailscale serve localhost:8080
tailscale serve --https=443 localhost:8080
tailscale serve --http=80 localhost:8080 # เข้าผ่าน MagicDNS: <http://phon-server>
tailscale serve --tcp=2222 tcp://localhost:22 # raw TCP forward
tailscale serve --bg localhost:8080 # รันเป็น background ไม่ต้องเปิด terminal

และมี subcommands: tailscale serve status, reset, get-config, set-config — config สะสมได้ (serve หลาย service พร้อมกัน ดูทั้งหมดด้วย status)

.

ต้องรู้ก่อนใช้: tailnet ต้องเปิด HTTPS certificates (ถ้ายังไม่เปิด CLI จะพาไปกดอนุญาตครั้งแรกครั้งเดียว) และ ACL ของ tailnet ใช้กับ traffic ของ Serve ด้วย

.

ข้อจำกัดของวิธีนี้:

DNS name จำกัดอยู่ในโดเมน tailnet เท่านั้น (device.tailnet-name.ts.net)

macOS: serve ไฟล์/โฟลเดอร์ได้เฉพาะ open-source client (App Store version โดน sandbox)

Funnel จำกัด port 443/8443/10000, TLS เท่านั้น, bandwidth limit ปรับไม่ได้

Identity headers ไม่มีสำหรับ traffic จาก tagged devices

ต้องรัน serve ใหม่หลัง reboot ถ้าไม่ได้ใช้ -bg หรือทำ systemd unit

แผน Personal ฟรีตลอดชีพ — devices สูงสุด 100 เครื่อง, 3 users — สำหรับ “ใช้เอง + แชร์เพื่อนไม่กี่คน” เหลือเฟือ

.

สรุป: ใช้เมื่อไหร่ แบบไหน

สถานการณ์คำสั่ง
ใช้ GPU box ของตัวเองจากเครื่องไหนก็ได้tailscale serve --http=8888 localhost:8888 แล้วเปิด http://phon-server:8888
เปิด LLM/web server ให้คนใน tailnettailscale serve localhost:8080
เปิดให้คนนอก (public)tailscale funnel localhost:8080 (คิดดีๆ ก่อน)
ให้ backend รู้ว่าใครขออ่าน Tailscale-User-Login header
ใช้ TCP protocol อื่น (เกม, RDP, DB)tailscale serve --tcp=<port> tcp://localhost:<port>

.

สรุปแบบวิศวกรเป็ด

คราวก่อนพรใช้ SSH + port forwarding — เหมือนต่อสายชาร์จยาวจากบ้านมาที่ร้านกาแฟทุกครั้งที่จะใช้ ภาคนี้เริ่มจากตัวเอง: เครื่อง GPU อยู่บ้าน แต่ notebook กับมือถือของพรเปิด http://phon-server:<port> ได้จากไหนก็ได้ โดย app บน server ยัง lock อยู่บน localhost อย่างปลอดภัย — และเมื่อวันหนึ่งจะเชิญทีมเข้ามาใช้ พรก็รู้เลยว่าใครกำลังคุยกับ LocalLLM ของพรอยู่

.

คราวหน้าถ้าอยากทำให้ public จริงๆ จะมาเล่าเรื่อง Funnel + rate limiting กัน (เพราะ public = ต้องคิดเรื่อง quota หนักขึ้นอีกมาก)

.

ลองแล้วเป็นยังไงกันบ้าง? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้พรทำภาคต่อเรื่องไหน บอกได้เลยค้าบ

.

#Adduckivity #DuckOS #NeuroDivergent #Tailscale #LocalLLM #HomeLab #SystemsFirst #DevOps
