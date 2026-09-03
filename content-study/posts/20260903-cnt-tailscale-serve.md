# โมเดลรันบนเครื่องที่บ้านแล้ว เหลือแค่ "ลิงก์" ที่คนนอกเข้าถึงได้

<!--
ContentID: 20260903-CNT-XXSERVE
Series: Tailscale (ภาคต่อของ 20260824-CNT-Tailscale-Remote-Access)
Type: Tutorial/How-to
Status: Draft — รอ review
Target: ~1000 words, 8-12 min read
Tone: Technical-but-approachable (ภาคต่อ: ผู้อ่านรู้จัก Tailscale แล้วจากภาคก่อน)
Sources (verified 2026-09-03):
- https://tailscale.com/docs/features/tailscale-serve (validated Jan 20, 2026)
- https://tailscale.com/docs/reference/tailscale-cli/serve (validated Jan 26, 2026)
- https://tailscale.com/docs/features/tailscale-funnel
- https://tailscale.com/pricing
-->

เดือนก่อนผมเขียนเรื่อง "เลิกรัน Local LLM นอกบ้าน" — จบด้วยการรัน SSH เข้าเซิร์ฟเวอร์ที่บ้านแล้ว forward port 8080 กลับเครื่องตัวเอง มันได้ผล แต่ก็มีข้อเสียที่ผมบอกไปตั้งแต่ตอนนั้น: ทุกครั้งที่ต้องใช้ ต้อง SSH ก่อนทุกครั้ง, terminal window ต้องเปิดค้าง, และถ้า laptop หลับไป connection ก็หลุด

ครั้งนี้ผมเจอวิธีที่สะอาดกว่ามาก — `tailscale serve`

มันคือคำสั่งเดียวที่เอา HTTP server ที่รันบน `localhost:8080` ของเครื่องที่บ้าน (คือ llama-server ที่รัน Qwen 27B ของเรา) มาเสิร์ฟเป็น **HTTPS จริงๆ บนโดเมนของตัวเอง** — `https://home-server.tailnet.ts.net` — โดยไม่ต้อง port-forward, ไม่ต้อง VPN tunnel ค้าง, ไม่ต้องตั้งค่า reverse proxy ตัวเอง

## ทดลองจริง: LLM server ของผม

สถานการณ์จริงของผมตอนนี้:

- เซิร์ฟเวอร์ PHON-SERVER, GPU 2 ใบ, รัน `llama-server` ที่ port 8080
- โมเดล Qwen3 27B quant Q4_K_M (~16GB) offload ลง GPU
- ผมอยู่ข้างนอก อยากให้ notebook และมือถือใน tailnet เปิดเว็บ UI ของ LLM ได้ทันที

คำสั่งที่ต้องรัน **แค่ครั้งเดียว** บนเครื่องที่บ้าน:

```bash
tailscale serve localhost:8080
```

เท่านี้เอง ผลลัพธ์ที่ CLI พิมพ์กลับมา:

```
Available within your tailnet:
https://home-server.tailnet.ts.net

|-- / proxy http://127.0.0.1:8080
```

หลังจากนี้ ทุก device ที่อยู่ใน tailnet (และ login แล้ว) เปิด `https://home-server.tailnet.ts.net` ได้เลย — TLS certificate จัดให้อัตโนมัติ, ไม่มีการแจ้งเตือน browser ไม่ trusted, และถ้า device หลับ/หลุดแล้ว reconnect มันก็กลับมาได้เอง เพราะ traffic โดน route ผ่าน Tailscale daemon ไม่ใช่ SSH session

**ตัวเลขที่ควรรู้ก่อน** (จากหน้า pricing ของ Tailscale, เช็คเดือน 9/2026):

- แผน Personal (ฟรีตลอดกาล): devices ไม่จำกัด, 6 users, ACL groups 3 ตัว — พอสำหรับ homelab แบบผมสบายๆ
- แผน Standard: $8/user/เดือน — เพิ่ม SCIM, MDM, ACL 10 groups
- แผน Premium: $18/user/เดือน — ACL 300 groups, flow logs, JIT access

## Serve vs Funnel — อย่าสับสน

คนส่วนใหญ่ติดตรงจุดนี้ เพราะ Tailscale มี feature สองตัวที่คล้ายกันมาก:

| | **Serve** | **Funnel** |
|---|---|---|
| ใครเข้าถึงได้ | คนใน tailnet (คนที่ login แล้ว) | **ทุกคน** บนอินเทอร์เน็ต |
| ใช้ทำอะไร | แชร์ service ให้เพื่อน/ทีม/ตัวเอง | เปิด service สาธารณะ |
| Identity headers | ✅ มี (รู้ว่าเป็นใคร) | ❌ ไม่มี |
| Port ที่ใช้ได้ | ทุก port (HTTP/HTTPS/TCP) | 443, 8443, 10000 เท่านั้น |
| สถานะ | Stable | Beta |
| ต้องเปิดใน policy | ไม่บังคับ | ต้องมี funnel node attribute |

กฎที่จำง่าย: **`serve` = ส่วนตัว, `funnel` = สาธารณะ** — และ port เดียวกันจะรันทั้ง Serve + Funnel พร้อมกันไม่ได้ (คำสั่งล่าสุด wins — ถ้าสั่ง funnel หลัง serve port นั้นจะกลายเป็น public)

ถ้าอยากเปิด LLM server ให้คนนอกที่ไม่ใช่ Tailscale user เข้าถึง:

```bash
tailscale funnel localhost:8080
```

มันสร้าง URL funnel ที่ชี้ไปที่ relay server ของ Tailscale — relay ตั้ง TCP proxy แบบ encrypt เข้ามาที่เครื่องเรา (relay มองไม่เห็น IP เครื่องเรา และ decrypt ข้อมูลไม่ได้) แต่คิดดีๆ ก่อนใช้กับ LLM server: public = ใครก็ได้ยิง query ได้ = กิน resource คุณฟรี

## ตัวที่ killer จริงๆ: Identity Headers

นี่คือ feature ที่ผมคิดว่าถูกออกแบบมาเพื่อ use case แบบ "shared LLM server" พอดี

เมื่อ traffic มาผ่าน `tailscale serve` (ไม่ใช่ funnel) Tailscale จะเติม HTTP headers เหล่านี้เข้าไปให้ backend ของเรา:

- `Tailscale-User-Login` — เช่น `phon@example.com`
- `Tailscale-User-Name` — display name
- `Tailscale-User-Profile-Pic` — URL รูปโปรไฟล์ (ถ้ามี)

หมายความว่า backend สามารถรู้ได้ **ว่าใคร** กำลังถามโมเดล — โดยไม่ต้องมี API key, ไม่ต้องมี login page, ไม่ต้องทำ auth system อะไรเลย (Tailscale ยัง strip header เหล่านี้จาก incoming request ด้วย เพื่อไม่ให้มีใคร spoof)

กรณีของผม: ถ้าเปิด server ให้ทีมใช้ร่วมกัน ผมแค่ log `Tailscale-User-Login` ในแต่ละ request — รู้ได้เลยว่าใครถามอะไร, quota ใครกินเท่าไหร่, และถ้าวันหนึ่งมี request แปลกๆ มา ผมรู้ว่าต้องไปคุยกับใคร

**ข้อควรระวังที่ doc บอกตรงๆ**: ให้ backend listen บน `localhost` เท่านั้น — ถ้าเปิดให้ LAN/tailnet เข้าถึง port 8080 โดยตรง ใครก็ได้ตั้ง header ตัวเองได้

## คำเตือนเรื่อง version: CLI เปลี่ยนแล้วใน v1.52

ถ้าคุณตาม tutorial เก่าๆ (2024-2025) มาจะเจอปัญหา — syntax เดิม:

```bash
# แบบเก่า (v<1.52)
tailscale serve 443 --bg http://127.0.0.1:8080
```

ตอนนี้ (client v1.52 ขึ้นไป) กลายเป็น target-based:

```bash
# แบบใหม่
tailscale serve localhost:8080
tailscale serve --https=443 localhost:8080
tailscale serve --http=80 localhost:8080      # เข้าได้ผ่าน MagicDNS: http://home-server
tailscale serve --tcp=2222 tcp://localhost:22 # raw TCP forward (SSH-over-Tailscale แบบไม่ต้อง SSH client)
tailscale serve --tls-terminated-tcp=8443 tcp://localhost:9899
tailscale serve --proxy-protocol=2 --tls-terminated-tcp=443 tcp://127.0.0.1:9899
```

target เป็นได้ 4 แบบ: port number, partial URL, full URL (รวม path เช่น `tcp://localhost:3000/foo`), หรือ `text:"Hello"` สำหรับ static response (ใช้ debug)

มี subcommands ใหม่ด้วย: `tailscale serve status`, `reset`, `get-config`, `set-config`, `drain`, `advertise` — config แบบ declarative แทนที่จะเป็น flag ยาวๆ

**ต้องรู้ก่อนใช้**: tailnet ต้องเปิด HTTPS certificates ไว้ (ถ้าไม่ได้เปิด CLI จะมี web consent page ให้กดอนุญาตครั้งแรก), และ access control rules (ACL) ของ tailnet ใช้กับ traffic ของ Serve เหมือนกัน — ถ้า ACL ของคุณ block device บางตัว มันจะเข้าไม่ได้

## Limitations ที่ควรรู้

- DNS name ถูกจำกัดในโดเมน tailnet เท่านั้น (`device-name.tailnet-name.ts.net`)
- macOS: serve ไฟล์/โฟลเดอร์ได้เฉพาะ version open-source ของ client (App Store version ไม่ได้เพราะ sandbox)
- Funnel จำกัด port 443/8443/10000, TLS เท่านั้น, และมี bandwidth limit ที่ปรับไม่ได้
- Identity headers ไม่มีสำหรับ traffic จาก tagged devices

## สรุป: ใช้เมื่อไหร่ตัวไหน

| สถานการณ์ | คำสั่ง |
|---|---|
| เปิด LLM/web server ให้คนใน tailnet | `tailscale serve localhost:8080` |
| เปิดให้คนนอก (public) | `tailscale funnel localhost:8080` (คิดดีก่อน) |
| แชร์ไฟล์/โฟลเดอร์ให้ทีม | `tailscale serve /path/to/dir` |
| ให้ backend รู้ว่าใครขอ | อ่าน `Tailscale-User-Login` header |
| ใช้ TCP protocol อื่น (เกม, RDP, DB) | `tailscale serve --tcp=<port> tcp://localhost:<port>` |

ภาคก่อนผมใช้ SSH + port forwarding — มันได้ผล แต่ต้อง "เปิด tunnel" ทุกครั้ง ภาคนี้ `tailscale serve` ทำให้ service ของผมกลายเป็น URL HTTPS ที่เสถียร เปิดเมื่อไหร่ก็ได้ จาก device ไหนก็ได้ที่ login อยู่ — และที่สำคัญ: ผมรู้เลยว่าใครกำลังคุยกับ Qwen 27B ของผมอยู่

คราวหน้าถ้าอยากทำให้ public จริงๆ จะมาเล่าเรื่อง Funnel + rate limiting กัน (เพราะ public = ต้องคิดเรื่อง quota หนักขึ้นอีกมาก)

---

**คิดเห็นอย่างไร? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้ผมทำภาคต่อเรื่องไหน (เช่น Funnel + rate limiting, หรือ identity headers กับ Grafana/auth proxy) บอกได้เลย**

ติดตามคอนเทนต์เพิ่มเติมได้ที่:
- YouTube: https://www.youtube.com/@adduckivity
- Instagram: https://www.instagram.com/adduckivity
- Facebook: https://www.facebook.com/adduckivity
- X: https://x.com/adduckivity
