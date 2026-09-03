# จะรัน Local LLM ให้คนอื่นใช้ได้ ต้องมีอะไรบ้าง? — คู่มือ tailscale serve ฉบับ Long Form

<!--
ContentID: 20260903-CNT-XXSERVE-LF
Series: Tailscale (ภาคต่อของ 20260824-CNT-Tailscale-Remote-Access)
Type: Long Form (2500-3000 words)
Status: Draft — รอ review (ปรับมุม 2026-09-03: เปิดด้วย "serve ตัวเองก่อน" — unsloth/ComfyUI/llama-server จากเครื่องตัวเอง ไม่ต้อง fixed IP — แล้วค่อยขยายไปแชร์ทีม)
Sources (verified 2026-09-03):
- https://tailscale.com/docs/features/tailscale-serve
- https://tailscale.com/docs/reference/tailscale-cli/serve
- https://tailscale.com/docs/features/tailscale-funnel
- https://tailscale.com/pricing
-->

เดือนก่อนผมเขียนเรื่อง "เลิกรัน Local LLM นอกบ้าน" — จบด้วยการ SSH เข้าเซิร์ฟเวอร์ที่บ้านแล้ว forward port 8080 กลับเครื่องตัวเอง

มันได้ผลจริงคับ แต่มีข้อแม้ที่ผมบอกไปตั้งแต่ตอนนั้น:

- ทุกครั้งที่จะใช้ ต้องรันคำสั่ง SSH ก่อนทุกครั้ง
- Terminal window ต้องเปิดค้างไว้ตลอด ปิดปุ๊บ link ตาย
- ถ้า laptop หลับหรือสลับ Wi-Fi connection หลุด ต้องต่อใหม่
- และที่แย่ที่สุด: มีแค่ผมคนเดียวที่ใช้ได้ — เพราะต้องมี SSH key ของเครื่อง server ด้วย

ครั้งนี้ผมจะเล่าวิธีที่สะอาดกว่ามาก — `tailscale serve` — และผมจะเล่าจากมุมที่คนมองข้ามที่สุดก่อน: ไม่ใช่เรื่องแชร์โมเดลให้คนอื่น แต่คือเรื่อง **การใช้เครื่อง GPU ที่บ้านของตัวเองจากเครื่องไหนก็ได้** แบบไม่ต้อง fixed IP ไม่ต้อง SSH ไม่ต้องเข้าไปกา port ที่ router

พอใช้เองได้มั่นคงแล้ว ค่อยขยายไปคำถามถัดไป: เปิดให้ทีมหรือเพื่อนใช้ร่วมกัน พร้อมระบบ "รู้ว่าใครกำลังใช้" ที่ใช้งานได้ทันทีโดยไม่ต้องเขียน auth system แม้แต่บรรทัดเดียว

บทความนี้ยาวหน่อยนะคับ (อ่านสัก 15-20 นาที) — เพราะผมจะเล่าตั้งแต่ concept, คำสั่งจริง, จนถึงเรื่อง security ที่มีคนถามผมเยอะที่สุด: "เปิดแบบนี้แล้วใครก็เข้าได้ไหม?" คำตอบคือ ไม่ และเดี๋ยวผมพิสูจน์ให้ดู

## 01: ปัญหาที่แท้จริง — เครื่อง GPU ของคุณเป็นเกาะที่ติดกุญแจ

TL;DR ก่อน สำหรับคนที่เข้าใจ infrastructure อยู่แล้ว:

> รัน `tailscale serve --http=8888 localhost:8888` บนเครื่อง server แล้วเปิด `http://phon-server:8888` จากเครื่องไหนก็ได้ที่อยู่ใน tailnet — จบ ไม่ต้องตั้งค่าอะไรอีกเลย

สำหรับคนที่อยากเข้าใจว่ามันเกิดอะไรขึ้นตอนรันคำสั่งนี้ — เดี๋ยวไปดูทีละชั้น

ตอนนี้ PHON-SERVER ของผมมีสถานะแบบนี้:

- GPU 2 ใบ (16GB ต่อใบ)
- รัน `llama-server` โหลด Qwen3 27B quant Q4_K_M (ไฟล์ ~16GB) — offload ลง GPU ทั้งหมด, listen ที่ port 8080
- ComfyUI (port 8188) สำหรับงานรูป
- unsloth บน Jupyter notebook (port 8888) สำหรับงาน fine-tune

ผมนั่ง MacBook อยู่นอกบ้าน อยากเปิด notebook ของ unsloth ที่รันอยู่บนเครื่อง server — เปิด browser พิมพ์ `http://phon-server:8888` แค่นั้นเอง พิมพ์ชื่อเครื่อง ไม่ใช่เลข IP ที่วันนี้ router แจกเป็น 192.168.1.x พรุ่งนี้เปลี่ยนเป็นเลขอื่น

คำสั่งที่ต้องรันบนเครื่อง server ครั้งเดียวต่อ service:

```bash
tailscale serve --http=8888 localhost:8888   # unsloth/Jupyter
tailscale serve --http=8188 localhost:8188   # ComfyUI
tailscale serve localhost:8080               # llama-server (HTTPS default)
```

Terminal พิมพ์กลับมาแบบนี้:

```
Available within your tailnet:
https://phon-server.my-tailnet.ts.net

|-- / proxy http://127.0.0.1:8080

Press Ctrl+C to exit.
```

จากตรงนี้ ทุก device ที่ login อยู่ใน tailnet เปิด URL พวกนี้ได้เลย — และถ้า device หลับ/สลับเครือข่ายแล้วกลับมา มันก็ใช้ได้ทันที เพราะ traffic ถูก route ผ่าน Tailscale daemon ที่รันเป็น service อยู่แล้ว ไม่ผูกกับ SSH session ของใคร

ห้าบรรทัดล้มค่า SSH tunnel ที่ผมใช้มาตลอดหลายเดือนคับ

## 02: แยกชั้นให้ออกก่อน — อะไรทำให้ "ไม่ต้อง fixed IP" (คำตอบไม่ใช่ serve)

จุดนี้สำคัญเพราะคนเข้าใจผิดกันเยอะมาก — รวมตัวผมเองก่อนเขียนบทความนี้ด้วย

คำถาม: อะไรทำให้เราพิมพ์ `http://phon-server:8888` แล้วเข้าได้โดยไม่ต้อง fixed IP?

คำตอบ: **tailnet + MagicDNS** ไม่ใช่ serve

ทุกเครื่องที่ลง Tailscale จะได้ IP ถาวรใน range 100.x.x.x (ไม่หายไปไหนแม้เปลี่ยน Wi-Fi) พร้อมชื่อเครื่องที่เรียกได้จากใน tailnet (`phon-server`) — อันนี้มีมาตั้งแต่ติดตั้ง Tailscale แล้ว ยังไม่ต้องพิมพ์คำสั่ง serve เลย

อย่างเครื่องผม: `llama-server` สั่ง bind `0.0.0.0:8080` ดังนั้นแม้ไม่มี serve ผมก็เปิด `http://phon-server:8080` จาก MacBook ได้อยู่แล้ว

**งั้น serve แก้ปัญหาอะไร?** สองอย่างที่เจ็บกว่า:

1. **เครื่องมือ AI ส่วนใหญ่ bind `127.0.0.1` โดย default** — Jupyter/unsloth (8888), ComfyUI (ก่อนจะสั่ง `--listen 0.0.0.0`) เรียกจากเครื่องอื่นไม่ได้เลย ทางแก้ตรงๆ คือสั่งให้ app เปิด `0.0.0.0` — แปลว่า**ทั้ง LAN เห็น** รวมถึงคนที่ไม่ควรเห็น แถม app พวกนี้ส่วนใหญ่ไม่มี login
2. **HTTPS ที่ browser เชื่อ** — certificate อัตโนมัติ ไม่ต้องทำเอง

`tailscale serve` คือ reverse proxy ที่รันอยู่ใน daemon ของเครื่อง server: app ยัง bind localhost อยู่อย่างนั้น (มองไม่เห็นจาก LAN) แต่คนใน tailnet เข้าได้ผ่าน URL — ได้ความสะดวกและความปลอดภัยพร้อมกัน

จำง่ายๆ สามชั้น (สองชั้นแรกมาจาก Tailscale ตั้งแต่ติดตั้ง ชั้นที่สามคือคำสั่งที่เราเพิ่มเข้าไป):

- **tailnet** = อาคาร (เครือข่าย + ชื่อเครื่องถาวร 100.x.x.x)
- **MagicDNS** = ป้ายชื่อห้อง (`phon-server` แทนเลข IP)
- **serve** = เปิดประตูห้องให้คนในอาคารเข้าได้ โดยของในห้องยัง lock อยู่ข้างใน (localhost)
- (**funnel** = เปิดประตูอาคารให้คนนอก — เดี๋ยวคุยท้ายบทความ)

## 03: Serve vs Funnel — ตารางเทียบที่ควรจริงจัง

พอใช้เองคล่องแล้ว คำถามถัดไปคือขยายไปหาคนอื่น และตรงนี้ Tailscale มี feature สองตัวที่ชื่อคล้ายกันมาก:

ผมทำตารางนี้จาก docs ปัจจุบันของ Tailscale (ตรวจสอบเดือน ก.ย. 2026) เพราะเจอ tutorial เก่าที่ข้อมูลไม่ตรงกันเยอะมาก:

| | **Serve** | **Funnel** |
|---|---|---|
| ใครเข้าถึงได้ | เฉพาะคน/อุปกรณ์ใน tailnet | ทุกคนบนอินเทอร์เน็ต |
| Identity headers | ✅ มี (รู้ว่าใครส่ง request) | ❌ ไม่มี |
| Port ที่ใช้ได้ | ทุก port (HTTP/HTTPS/TCP) | จำกัด 443, 8443, 10000 |
| สถานะ | Stable | Beta |
| ต้องตั้งค่าเพิ่ม | เปิด HTTPS ใน tailnet (มี wizard) | ต้องเพิ่ม funnel node attribute ใน policy |
| Bandwidth | ไม่จำกัด (P2P) | มี limit ที่ปรับไม่ได้ |
| IP เครื่องคุณถูกเปิดไหม | ไม่ | ไม่ (ผ่าน relay) |

กฎเหล็กข้อเดียวที่ต้องจำ: **serve = ส่วนตัว, funnel = สาธารณะ**

และข้อจำกัดที่คนพลาดบ่อย: **port เดียวกันรันทั้ง Serve และ Funnel พร้อมกันไม่ได้** — คำสั่งหลัง wins เสมอ ถ้าคำสั่งล่าสุดคือ `serve` port นั้น private, ถ้าคำสั่งล่าสุดคือ `funnel` port นั้น public ทันที

## 04: Funnel ทำงานยังไง — ทำไม IP คุณไม่รั่ว

เรื่องนี้เจ๋งพอที่จะเล่าแยกเป็น section คับ

เวลาคุณรัน `tailscale funnel localhost:8080` Tailscale จะสร้าง URL สาธารณะที่ชี้ไปที่ **Funnel relay server ของ Tailscale** — ไม่ใช่เครื่องคุณโดยตรง

Flow เต็มๆ เวลามีคนแปลกหน้าเรียก URL นั้น:

1. DNS ของ URL นั้น resolve ไปที่ IP ของ relay server ของ Tailscale (IP เครื่องคุณไม่ถูกเปิดเป็นสาธารณะแม้แต่ตัวเดียว)
2. Relay server ตั้ง TCP proxy ผ่าน Tailscale tunnel เข้ามาที่เครื่องคุณ
3. Tailscale daemon บนเครื่องคุณ terminate TLS แล้วส่งต่อไปที่ localhost:8080
4. คำตอบวิ่งกลับไปตามทางเดิม

จุดที่ผมว่าน่าสนใจที่สุด: **relay server decrypt ข้อมูลไม่ได้** — TLS connection เป็นแบบ end-to-end ระหว่าง browser ของคนเรียกกับเครื่องคุณ Tailscale แค่หล่อ traffic ผ่าน ซึ่งหมายความว่าแม้แต่ Tailscale เองก็อ่านข้อมูลที่วิ่งผ่าน funnel ไม่ได้

แต่ — และนี่คือ but ที่สำคัญ — **public คือ public** ใครก็ได้ยิง request เข้ามา กิน GPU ของคุณฟรีๆ ถ้าไม่มีระบบกันไว้ ผมเคยเห็นคนเปิด LLM endpoint ด้วย funnel แล้วโดนยิงจนเล่นไม่ได้ทั้งคืน

ถ้าจำเป็นต้องเปิดสาธารณะจริงๆ อย่างน้อยที่สุดควรทำสิ่งนี้:

- ตั้ง rate limit ที่ backend (llama-server มี `--threads` ให้จำกัด concurrency)
- ใช้แผนฟรีของ Cloudflare Tunnel เป็นชั้นเสริม (มี WAF และ rate limiting ให้)
- หรือทำแบบที่ผมทำ: ไม่เปิด public เลย ใช้ Serve + เชิญคนเข้า tailnet แทน (ฟรี สูงสุด 6 users)

## 05: Identity Headers — feature ที่คนลืมบ่อยที่สุด

ใช้คนเดียวไม่ต้องสน feature นี้ แต่พอขยายจาก "ใช้เอง" ไป "ให้ทีมใช้ร่วมกัน" — นี่คือของฟรีที่แพงที่สุดตัวหนึ่งเลย

เมื่อ traffic มาผ่าน `tailscale serve` (เฉพาะ serve — funnel ไม่มี) daemon จะเติม HTTP headers ต่อไปนี้เข้าไปใน request ก่อนส่งให้ backend:

- `Tailscale-User-Login` — login name ของคนส่ง (เช่น `phon@example.com`)
- `Tailscale-User-Name` — display name
- `Tailscale-User-Profile-Pic` — URL รูปโปรไฟล์ (ถ้า IdP ให้มา)

ความหมายใช้งานจริง: backend ของคุณ **รู้ว่าใคร** กำลังถามโมเดล — โดยไม่ต้องมี API key, ไม่ต้องมี login page, ไม่ต้องเขียนระบบ auth สักบรรทัด

และเพื่อกัน spoof: Tailscale จะ **strip headers เหล่านี้ออกจาก incoming request เสมอ** — ถ้ามีใครพยายามส่ง `Tailscale-User-Login: billgates@microsoft.com` มาเอง header นั้นจะถูกลบทิ้งก่อนถึง backend แล้วเติมของจริงลงไป ทำให้ backend วางใจค่าพวกนี้ได้เต็มที่ (ถ้ามาทางนี้)

ตัวอย่างที่ใช้ได้จริงกับ backend อย่าง FastAPI:

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/whoami")
async def whoami(request: Request):
    user = request.headers.get("Tailscale-User-Login", "unknown")
    return {"user": user}
```

จากนั้น `curl https://phon-server.my-tailnet.ts.net/whoami` จากเครื่องที่ login แล้ว ได้ `{"user": "phon@example.com"}` ทันที

กรณีใช้งานจริงของผม: เปิด server ให้ทีมใช้ร่วมกัน แล้ว log `Tailscale-User-Login` ทุก request — รู้ทันทีว่าใครถามอะไร, ใครกิน quota เยอะสุด, และถ้ามี query แปลกๆ ผมรู้ว่าต้องไปคุยกับใคร

> **ข้อควรระวังที่ docs บอกตรงๆ**: backend ต้อง listen บน `127.0.0.1` เท่านั้น — ถ้าเปิดให้ LAN หรือ tailnet เข้าถึง port โดยตรง (ไม่ผ่าน serve) ใครก็ตั้ง header เหล่านี้เองได้ง่ายๆ และ backend จะเชื่อ เพราะฉะนั้น localhost-only เสมอ

## 06: คำเตือนที่ต้องรู้ — CLI syntax เปลี่ยนไปแล้วใน v1.52

ถ้าคุณตาม tutorial ปี 2024-2025 มา จะเจอ syntax แบบนี้:

```bash
# แบบเก่า (client < v1.52)
tailscale serve 443 --bg http://127.0.0.1:8080
```

ตั้งแต่ client v1.52 เป็นต้นมา syntax เปลี่ยนเป็น target-based:

```bash
# แบบใหม่ (v1.52+)
tailscale serve localhost:8080
```

และมี flag เสริมตาม use case:

```bash
tailscale serve --https=443 localhost:8080  # กำหนด port HTTPS เอง
tailscale serve --http=80 localhost:8080    # HTTP เข้าผ่าน MagicDNS: http://phon-server
tailscale serve --http=8888 localhost:8888  # ใช้กับ Jupyter/unsloth ที่ bind localhost
tailscale serve --bg localhost:8080         # รันเป็น background (ไม่ต้องเปิด terminal ค้าง)
```

target เป็นได้หลายแบบ:

- **Port number** — `tailscale serve 3000`
- **Partial URL** — `tailscale serve localhost:3000`
- **Full URL** — `tailscale serve tcp://localhost:3000/foo`
- **Static text** — `tailscale serve text:"Hello, world!"` (ใช้ debug ได้ดี)

นอกจากนี้ยังมี TCP forwarder สำหรับ protocol ที่ไม่ใช่ HTTP:

```bash
tailscale serve --tcp=2222 tcp://localhost:22  # forward SSH
tailscale serve --tls-terminated-tcp=8443 tcp://localhost:9899
```

และชุด subcommands สำหรับจัดการ config:

- `tailscale serve status` — ดูว่า serve อะไรอยู่บ้าง (config สะสมได้ หลาย service พร้อมกัน)
- `tailscale serve reset` — ล้าง config ทั้งหมด
- `tailscale serve get-config` / `set-config` — อ่าน/ตั้งค่าแบบ structured

**สิ่งที่ต้องเปิดก่อนใช้**: tailnet ต้องเปิด HTTPS certificates ไว้ — ถ้ายังไม่เปิด CLI จะพาไปหน้า web consent ให้กดอนุญาตครั้งเดียวแล้วจบ และ ACL rules ของ tailnet ก็ยังใช้กับ traffic ของ Serve — ถ้า ACL block device ตัวไหน device นั้นเข้าไม่ได้แม้จะเห็น URL ก็ตาม

## 07: Limitations ที่ควรรู้ก่อนวางแผน

- DNS name ถูกจำกัดอยู่ในโดเมน tailnet เท่านั้น (`device.tailnet-name.ts.net`) — ใช้โดเมน custom เองไม่ได้
- macOS: serve ไฟล์/โฟลเดอร์ได้เฉพาะ open-source variant ของ client (App Store version โดน sandbox จำกัด)
- Funnel จำกัด port 443/8443/10000, รับ TLS เท่านั้น, และมี bandwidth limit ที่ปรับไม่ได้
- Identity headers ไม่ถูกเติมสำหรับ traffic จาก tagged devices (เครื่องที่ใช้ tag แทน user identity เช่น server ที่ tag เป็น infra)
- ต้องรัน `tailscale serve` ใหม่หลัง reboot ถ้าไม่ได้ใช้ flag `--bg` หรือทำ systemd unit (ซึ่งก็ทำได้ไม่ยาก)

## 08: เรื่องราคา — ตัวเลขล่าสุด (ก.ย. 2026)

จากหน้า pricing ทางการของ Tailscale:

| แผน | ราคา | จุดเด่น |
|---|---|---|
| Personal | ฟรีตลอดกาล | devices ไม่จำกัด, 6 users, ACL 3 groups, tagged resources 50 ตัว |
| Standard | $8/user/เดือน | users ไม่จำกัด, SCIM, MDM, ACL 10 groups |
| Premium | $18/user/เดือน | ACL 300 groups, flow logs, JIT access, log streaming |
| Enterprise | Custom | ทุกอย่าง + SLA/support แบบ dedicated |

สำหรับ use case ของผม (ใช้เองได้ทุกเครื่อง + แชร์ให้เพื่อนไม่กี่คน): แผน Personal ฟรีเกินความจำเป็น — 6 users กับ devices ไม่จำกัด ครอบคลุมทุกอย่างที่ผมต้องการ และ Serve/Funnel ใช้ได้ทุกแผนไม่มี lock

สังเกตว่าราคาเป็น seat-based — จ่ายตามจำนวน user ไม่ใช่จำนวน devices (devices ของ user ไม่จำกัดทุกแผน) ซึ่งเหมาะกับ pattern "คนเดียวหลายเครื่อง" แบบผมดีมาก: server + notebook + มือถือ + iPad นับเป็น device เดียวกันในแงะ user

## 09: Pro Tips แยกตามระดับ

**มือใหม่ (เพิ่งเริ่ม):**

- เริ่มจาก service ที่ใช้เองก่อน: รัน `tailscale serve --http=8888 localhost:8888` แล้วเปิด `http://<ชื่อเครื่อง>:8888` จากมือถือที่ลง Tailscale ไว้ — ทดสอบว่าทุกอย่างทำงานก่อนเลย ใช้เวลาไม่กี่นาที
- ใช้ flag `--http=<port>` เพื่อเข้าผ่าน MagicDNS: `http://phon-server:8888` ได้เลย ไม่ต้องพิมพ์ชื่อเต็ม
- ทดสอบว่า serve ทำงานไหมด้วย `tailscale serve text:"hello"` แล้วเปิด URL ดู — ถ้าเห็นข้อความ แปลว่าทุกชั้นทำงานครบ

**ใช้จริงจัง (มีทีม/หลายเครื่อง):**

- ใช้ `--bg` เพื่อรัน serve เป็น background — ไม่ต้องเปิด terminal ค้าง
- ทำ systemd unit ให้ serve เริ่มทำงานหลัง reboot อัตโนมัติ
- Serve config สะสมได้ — ผม serve ทั้ง llama-server (8080), ComfyUI (8188), unsloth (8888) พร้อมกัน ตรวจด้วย `tailscale serve status`
- อ่าน `Tailscale-User-Login` จาก backend เพื่อทำ per-user logging/quota — ฟรี และไม่ต้องเขียน auth เอง

**องค์กร:**

- ใช้ `set-config` ร่วมกับ infrastructure-as-code เพื่อจัดการ serve config แบบ declarative
- Funnel ต้องมี funnel node attribute ใน policy — ควบคุมที่ ACL ให้เฉพาะเครื่องที่จำเป็นจริงๆ
- พิจารณา PROXY protocol (`--proxy-protocol=2`) ถ้า backend ต้องการรู้ source IP ของ client จริงๆ

## 10: สรุปแบบวิศวกรเป็ด

ถ้าจะให้ย่อทั้งบทความเหลือบรรทัดเดียว:

**การเข้าถึงเครื่องของตัวเองไม่ใช่ปัญหา networking — มันปัญหาการตั้งชื่อและเปิดประตูที่ถูกคน ให้ระบบที่เรียบร้อยแล้วช่วยจัดการแทน**

สิ่งที่ `tailscale serve` ทำคือดึงงาน "จำ IP ไม่ได้ + ตั้ง reverse proxy + TLS + auth" ที่เรามักเก็บไว้ทำ "วันหลัง" ออกไปจากสมการ ทำให้เหลือคำสั่งเดียว: app ของผมยัง lock อยู่บน localhost อย่างปลอดภัย แต่จาก MacBook หรือมือถือที่ไหนก็ได้ ผมเปิด `http://phon-server:8888` แล้วเจอ unsloth notebook ของตัวเองได้เลย

และเมื่อวันหนึ่งขยายไปให้ทีมใช้ ผมก็รู้ด้วยว่าใครกำลังเดินเข้ามาในห้องนี้

Duck OS Law #3: Protect System — ระบบที่ดีไม่ได้แปลว่าปิดทุกอย่าง แต่แปลว่าเปิดในสิ่งที่ควรเปิด พร้อมมองเห็นว่าใครเข้ามา และปิดได้ทันทีเมื่อไม่พึงประสงค์

คราวหน้าถ้าสนใจภาคต่อ — Funnel + rate limiting สำหรับ public endpoint หรือการทำ auth proxy กับ Grafana โดยใช้ identity headers — บอกได้เลยคับ

---

**คิดเห็นอย่างไร? คอมเมนต์ด้านล่างได้เลยคับ**

ติดตามคอนเทนต์เพิ่มเติมได้ที่:
- YouTube: https://www.youtube.com/@adduckivity
- Instagram: https://www.instagram.com/adduckivity
- Facebook: https://www.facebook.com/adduckivity
- X: https://x.com/adduckivity

#Adduckivity #DuckOS #Tailscale #LocalLLM #NeuroDivergent
