# GPU อยู่ที่บ้าน ใช้จากเครื่องไหนก็ได้ — เริ่มจาก "ใช้เองก่อน" ด้วย tailscale serve

<!--
ContentID: 20260903-CNT-XXSERVE
Series: Tailscale (ภาคต่อของ 20260824-CNT-Tailscale-Remote-Access)
Type: Tutorial/How-to
Status: Draft — รอ review (ปรับมุม 2026-09-03: เปิดด้วย "serve ตัวเองก่อน" — unsloth/ComfyUI จากเครื่องตัวเอง ไม่ต้อง fixed IP — แล้วค่อยขยายไปแชร์ทีม)
Target: ~1000 words, 8-12 min read
Tone: Technical-but-approachable (ภาคต่อ: ผู้อ่านรู้จัก Tailscale แล้วจากภาคก่อน)
Sources (verified 2026-09-03):
- https://tailscale.com/docs/features/tailscale-serve (validated Jan 20, 2026)
- https://tailscale.com/docs/reference/tailscale-cli/serve (validated Jan 26, 2026)
- https://tailscale.com/docs/features/tailscale-funnel
- https://tailscale.com/pricing
-->

เดือนก่อนผมเขียนเรื่อง "เลิกรัน Local LLM นอกบ้าน" — จบด้วยการรัน SSH เข้าเซิร์ฟเวอร์ที่บ้านแล้ว forward port กลับเครื่องตัวเอง มันได้ผล แต่ก็มีข้อเสียที่ผมบอกไปตั้งแต่ตอนนั้น: ทุกครั้งที่ต้องใช้ ต้อง SSH ก่อนทุกครั้ง, terminal window ต้องเปิดค้าง, และถ้า laptop หลับไป connection ก็หลุด

ครั้งนี้ผมเจอวิธีที่สะอาดกว่ามาก — `tailscale serve` — และผมอยากเล่าจากมุมที่คนมองข้ามที่สุดก่อน: ไม่ใช่การแชร์โมเดลให้คนอื่น แต่คือการ **ใช้เครื่อง GPU ที่บ้านจากเครื่องไหนก็ได้ ของตัวเอง** แบบไม่ต้อง fixed IP ไม่ต้อง SSH ไม่ต้องไปกา port ที่ router

## สถานการณ์จริงบนเครื่องผม

ตอนนี้ PHON-SERVER ของผม (Linux, GPU 2 ใบ) มีของที่ใช้ประจำอยู่ 3 อย่าง:

- `llama-server` ที่ port 8080 — รัน Qwen3 27B quant Q4_K_M offload ลง GPU
- ComfyUI ที่ port 8188 — งานรูป
- unsloth (Jupyter notebook) ที่ port 8888 — งาน fine-tune

ผมนั่ง MacBook อยู่นอกบ้าน อยากแตะงานอันไหนก็เปิด browser ไปที่ `http://phon-server:8888` — พิมพ์ชื่อเครื่องเฉยๆ ไม่ใช่ IP ไม่ต้องจำว่าวันนี้ router แจกเลขอะไรให้เครื่อง server

คำสั่งที่ต้องรันบนเครื่อง server **ครั้งเดียว** ต่อ service:

```bash
tailscale serve --http=8888 localhost:8888   # unsloth/Jupyter
tailscale serve --http=8188 localhost:8188   # ComfyUI
tailscale serve localhost:8080               # llama-server (ได้ HTTPS เป็น default)
```

เท่านี้ — ทุก device ที่ login อยู่ใน tailnet (notebook, มือถือ) เปิด URL พวกนี้ได้เลย ไม่มี SSH ไม่มี terminal ค้าง และถ้า device หลับ/สลับเครือข่ายแล้วกลับมา มันใช้ได้ทันที เพราะ traffic โดน route ผ่าน Tailscale daemon ไม่ผูกกับ session ของใคร

## แยกให้ออกก่อน: อะไรทำให้ "ไม่ต้อง fixed IP" — ตอบว่าไม่ใช่ serve

จุดนี้คนเข้าใจผิดกันเยอะมาก รวมตัวผมก่อนหน้านี้ด้วย

**ชั้นที่ทำให้ไม่ต้อง fixed IP คือ tailnet + MagicDNS** — ทุกเครื่องที่ลง Tailscale จะได้ IP ถาวรใน range 100.x.x.x พร้อมชื่อเครื่องที่เรียกได้เลย (`phon-server`) นี่มีมาตั้งแต่ติดตั้ง Tailscale แล้ว ยังไม่ต้องมี serve เลย อย่างเครื่องผม: `llama-server` bind `0.0.0.0:8080` อยู่ ดังนั้นวันนี้เปิด `http://phon-server:8080` จาก MacBook ก็ใช้ได้แล้ว

**งั้น serve แก้ปัญหาอะไร?** สองอย่างที่เจ็บกว่านั้น:

1. **เครื่องมือ AI ส่วนใหญ่ bind `127.0.0.1` โดย default** — Jupyter/unsloth (8888), ComfyUI (ก่อนจะสั่ง `--listen 0.0.0.0`) นั่นแปลว่าจากเครื่องอื่นเข้าไม่ได้เลย ทางแก้แบบตรงๆ คือสั่งให้ app เปิด `0.0.0.0` — ซึ่งแปลว่า**ทั้ง LAN เห็น** รวมถึงคนที่ไม่ควรเห็นด้วย และ app พวกนี้ส่วนใหญ่ไม่มี login ให้ด้วย
2. **HTTPS ที่ browser เชื่อ** — certificate จัดให้อัตโนมัติ ไม่มีหน้าเตือน ไม่ต้องทำ cert เอง

`tailscale serve` คือ reverse proxy ที่รันอยู่ใน daemon ของเครื่อง server เอง: app ยัง bind localhost อยู่อย่างนั้น (ปลอดภัยกับ LAN) แต่คนใน tailnet เข้าได้ผ่าน URL — สอง requirements ที่ขัดกันได้ทั้งคู่

กฎจำง่ายๆ: **tailnet ให้ชื่อและเส้นทาง, serve เปิดประตูให้ service ที่ lock อยู่ใน localhost**

## พอใช้เองได้แล้ว — Serve vs Funnel

ขั้นถัดไปคือขยายจาก "ใช้เอง" เป็น "ให้คนอื่นใช้" และตรงนี้ Tailscale มี feature สองตัวที่คนสับสนกันมาก:

| | **Serve** | **Funnel** |
|---|---|---|
| ใครเข้าถึงได้ | คนใน tailnet (คนที่ login แล้ว) | **ทุกคน** บนอินเทอร์เน็ต |
| ใช้ทำอะไร | ใช้เอง/แชร์ service ให้ทีม | เปิด service สาธารณะ |
| Identity headers | ✅ มี (รู้ว่าเป็นใคร) | ❌ ไม่มี |
| Port ที่ใช้ได้ | ทุก port (HTTP/HTTPS/TCP) | 443, 8443, 10000 เท่านั้น |
| สถานะ | Stable | Beta |

กฎเหล็ก: **`serve` = ส่วนตัว, `funnel` = สาธารณะ** — และ port เดียวกันรันทั้ง Serve + Funnel พร้อมกันไม่ได้ (คำสั่งล่าสุด wins — ถ้าสั่ง funnel หลัง serve port นั้นจะกลายเป็น public ทันที)

ถ้าจะเปิดให้คนนอกที่ไม่ใช่ Tailscale user:

```bash
tailscale funnel localhost:8080
```

มันสร้าง URL ที่ชี้ไปที่ relay server ของ Tailscale — relay มองไม่เห็น IP เครื่องเราและ decrypt ไม่ได้ แต่คิดดีๆ ก่อนใช้กับ GPU box: public = ใครก็ยิงได้ = กิน VRAM คุณฟรี

## ตัวที่ killer ตอนขยายไปหาทีม: Identity Headers

ใช้คนเดียวไม่ต้องสน แต่พอเชิญเพื่อนเข้า tailnet (แผนฟรีได้ 6 users) เพื่อมาใช้โมเดลร่วมกัน — feature นี้คือของฟรีที่แพงที่สุด

เมื่อ traffic มาผ่าน `tailscale serve` (ไม่ใช่ funnel) daemon จะเติม headers เหล่านี้เข้าไปให้ backend:

- `Tailscale-User-Login` — เช่น `phon@example.com`
- `Tailscale-User-Name` — display name
- `Tailscale-User-Profile-Pic` — URL รูปโปรไฟล์ (ถ้ามี)

backend รู้ได้ทันทีว่า**ใคร**กำลังใช้ — ไม่ต้องมี API key, ไม่ต้องมี login page, ไม่ต้องเขียน auth system สักบรรทัด และ Tailscale strip headers พวกนี้จาก incoming request เสมอ ทำให้ spoof ไม่ได้

**ข้อควรระวังที่ doc บอกตรงๆ**: ให้ backend listen บน `localhost` เท่านั้น — ถ้าเปิด port ตรงสู่ LAN ใครก็ตั้ง header ตัวเองได้

## คำเตือนเรื่อง version: CLI เปลี่ยนแล้วใน v1.52

ถ้าตาม tutorial เก่า (2024-2025) จะเจอ syntax เดิม:

```bash
# แบบเก่า (v<1.52)
tailscale serve 443 --bg http://127.0.0.1:8080
```

ตอนนี้กลายเป็น target-based:

```bash
# แบบใหม่
tailscale serve localhost:8080
tailscale serve --https=443 localhost:8080
tailscale serve --http=80 localhost:8080      # เข้าผ่าน MagicDNS: http://phon-server
tailscale serve --tcp=2222 tcp://localhost:22 # raw TCP forward
tailscale serve --bg localhost:8080           # รันเป็น background ไม่ต้องเปิด terminal
```

และมี subcommands: `tailscale serve status`, `reset`, `get-config`, `set-config` — config สะสมได้ (serve หลาย service พร้อมกัน ดูทั้งหมดด้วย `status`)

**ต้องรู้ก่อนใช้**: tailnet ต้องเปิด HTTPS certificates (ถ้ายังไม่เปิด CLI จะพาไปกดอนุญาตครั้งแรกครั้งเดียว) และ ACL ของ tailnet ใช้กับ traffic ของ Serve ด้วย

## Limitations ที่ควรรู้

- DNS name จำกัดอยู่ในโดเมน tailnet เท่านั้น (`device.tailnet-name.ts.net`)
- macOS: serve ไฟล์/โฟลเดอร์ได้เฉพาะ open-source client (App Store version โดน sandbox)
- Funnel จำกัด port 443/8443/10000, TLS เท่านั้น, bandwidth limit ปรับไม่ได้
- Identity headers ไม่มีสำหรับ traffic จาก tagged devices
- ต้องรัน serve ใหม่หลัง reboot ถ้าไม่ได้ใช้ `--bg` หรือทำ systemd unit

**ตัวเลขราคา** (หน้า pricing ของ Tailscale, เช็ค 9/2026): แผน Personal ฟรีตลอดกาย — devices ไม่จำกัด, 6 users — สำหรับ "ใช้เอง + แชร์เพื่อนไม่กี่คน" เกินพอ

## สรุป: ใช้เมื่อไหร่ แบบไหน

| สถานการณ์ | คำสั่ง |
|---|---|
| ใช้ GPU box ของตัวเองจากเครื่องไหนก็ได้ | `tailscale serve --http=8888 localhost:8888` แล้วเปิด `http://phon-server:8888` |
| เปิด LLM/web server ให้คนใน tailnet | `tailscale serve localhost:8080` |
| เปิดให้คนนอก (public) | `tailscale funnel localhost:8080` (คิดดีก่อน) |
| ให้ backend รู้ว่าใครขอ | อ่าน `Tailscale-User-Login` header |
| ใช้ TCP protocol อื่น (เกม, RDP, DB) | `tailscale serve --tcp=<port> tcp://localhost:<port>` |

ภาคก่อนผมใช้ SSH + port forwarding — เหมือนต่อสายชาร์จยาวจากบ้านมาที่ร้านกาแฟทุกครั้งที่จะใช้ ภาคนี้เริ่มจากตัวเอง: เครื่อง GPU อยู่บ้าน แต่ notebook กับมือถือของผมเปิด `http://phon-server:<port>` ได้จากไหนก็ได้ โดย app บน server ยัง lock อยู่บน localhost อย่างปลอดภัย — และเมื่อวันหนึ่งจะเชิญทีมเข้ามาใช้ ผมก็รู้เลยว่าใครกำลังคุยกับ Qwen 27B ของผมอยู่

คราวหน้าถ้าอยากทำให้ public จริงๆ จะมาเล่าเรื่อง Funnel + rate limiting กัน (เพราะ public = ต้องคิดเรื่อง quota หนักขึ้นอีกมาก)

---

**คิดเห็นอย่างไร? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้ผมทำภาคต่อเรื่องไหน (เช่น Funnel + rate limiting, หรือ identity headers กับ Grafana/auth proxy) บอกได้เลย**

ติดตามคอนเทนต์เพิ่มเติมได้ที่:
- YouTube: https://www.youtube.com/@adduckivity
- Instagram: https://www.instagram.com/adduckivity
- Facebook: https://www.facebook.com/adduckivity
- X: https://x.com/adduckivity

#Adduckivity #DuckOS #Tailscale #LocalLLM #NeuroDivergent
