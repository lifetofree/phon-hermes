# Tailscale Serve — ใช้เครื่อง GPU ที่บ้านได้จากที่ไหนก็ได้ (ไม่ต้อง SSH, ไม่ต้อง fixed IP)

<!--
ContentID: 20260903-CNT-XXSERVE-LF
Series: Tailscale (ภาคต่อของ 20260824-CNT-Tailscale-Remote-Access)
Type: Long Form (~2200-2500 words)
Status: Draft v2 — ปรับ 2026-09-03: ตัด Funnel ออกทั้งหมด เหลือ Serve อย่างเดียว, มุม "ใช้เองก่อน" (unsloth/ComfyUI/llama-server จากเครื่องตัวเอง), ภาษาเข้าใจง่ายขึ้น
Sources (verified 2026-09-03):
- https://tailscale.com/docs/features/tailscale-serve
- https://tailscale.com/docs/reference/tailscale-cli/serve
- https://tailscale.com/pricing
-->

เดือนก่อนผมเขียนเรื่อง "เลิกรัน Local LLM นอกบ้าน" — ตอนนั้นวิธีที่ผมใช้คือ SSH เข้าเครื่องที่บ้าน แล้ว forward port 8080 กลับเครื่องตัวเอง

มันได้ผลคับ แต่เจ็บทุกครั้งที่ใช้:

- ทุกครั้งที่ต้องใช้ ต้องจำคำสั่ง SSH ยาวๆ มาพิมพ์ใหม่
- Terminal window ต้องเปิดค้างไว้ตลอด — ปิดปุ๊บ ทุกอย่างตาย
- Laptop หลับหรือสลับ Wi-Fi — link หลุด ต่อใหม่
- แย่สุด: มีแค่ผมคนเดียวที่ใช้ได้ เพราะต้องใช้ SSH key ของเครื่อง server

ครั้งนี้ผมจะเล่าวิธีที่สบายกว่ามาก — **`tailscale serve`** — แต่ผมจะเล่าจากมุมที่คนมองข้ามที่สุดก่อน

ไม่ใช่ "เปิด server ให้ทีมใช้" — แต่คือเรื่องง่ายๆ ที่ผมทำทุกวัน: **เปิด notebook ของ unsloth, ComfyUI, หรือหน้าเว็บของ LLM ที่รันอยู่บนเครื่อง GPU ที่บ้าน — จาก MacBook หรือมือถือที่ไปนั่งคาเฟ่**

โดยไม่ต้อง fixed IP, โดยไม่ต้อง SSH, โดยไม่ต้องเข้าไปที่ router กา port อะไรทั้งนั้น

## 01: สถานะเครื่องของผม — เพื่อให้เห็นภาพ

PHON-SERVER ที่บ้านมีของแบบนี้คับ:

- GPU 2 ใบ (16GB ต่อใบ)
- **llama-server** — รัน Qwen3 27B (ไฟล์ ~16GB) อยู่ที่ port 8080
- **ComfyUI** — งานรูป อยู่ที่ port 8188
- **unsloth** — Jupyter notebook สำหรับ fine-tune อยู่ที่ port 8888

ปัญหาคือ: ผมอยู่คาเฟ่ เปิด MacBook อยากเข้า notebook ของ unsloth — ทำยังไง?

วิธีเก่าคือ SSH tunnel — คำสั่งยาว, terminal ค้าง, หลับปุ๊บหาย

วิธีใหม่คือคำสั่ง 3 บรรทัดที่รันบนเครื่อง server **ครั้งเดียว**:

```bash
tailscale serve --http=8888 localhost:8888   # unsloth
tailscale serve --http=8188 localhost:8188   # ComfyUI
tailscale serve localhost:8080               # llama-server
```

เสร็จแล้วจากเครื่องไหนก็ได้ที่ลง Tailscale ไว้ ผมแค่เปิด browser พิมพ์:

```
http://phon-server:8888
```

**ชื่อเครื่อง — ไม่ใช่เลข IP.** วันนี้ router แจก 192.168.1.4 พรุ่งนี้เปลี่ยนเป็น 192.168.1.9 ก็ไม่เกี่ยว พิมพ์ชื่อเดิมได้ตลอด และถ้า laptop หลับหรือสลับ Wi-Fi แล้วกลับมา — เข้าได้เลย ไม่ต้องต่ออะไรใหม่

ห้าบรรทัดนี้จบ SSH tunnel ที่ผมทนใช้มาหลายเดือนคับ

## 02: แยกให้ออก — ตัวไหนทำอะไร (จำแค่ 3 ชั้น)

ตรงนี้คนสับสนเยอะ (ผมเองก็เคยสับสนก่อนเขียนบทความนี้) — ว่า "ไม่ต้อง fixed IP" มาจากตัวไหน จริงๆ แล้วมันมี 3 ชั้นทำงานด้วยกัน:

| ชั้น | ทำหน้าที่ | เปรียบง่ายๆ |
|---|---|---|
| **tailnet** | ทุกเครื่องที่ลง Tailscale จะได้ IP ถาวร (100.x.x.x) ที่ไม่เปลี่ยนแม้ย้าย Wi-Fi | **ตัวอาคาร** — ห้องของทุกคนมีเลขห้องถาวร |
| **MagicDNS** | เรียกเครื่องด้วยชื่อ (`phon-server`) แทนเลข IP | **ป้ายชื่อห้อง** — ไม่ต้องจำเลขห้อง พิมพ์ชื่อห้องได้เลย |
| **serve** | เปิดให้คนในอาคารเข้าหา app ที่ล็อกอยู่ในห้องได้ + ให้ HTTPS ฟรี | **พนักงานเปิดประตูห้อง** — คนนอกอาคารเข้าไม่ได้ |

สองชั้นแรกได้มาฟรีตั้งแต่ลง Tailscale — ยังไม่ต้องพิมพ์คำสั่ง serve ด้วยซ้ำ

**แล้ว serve แก้ปัญหาอะไรที่อีกสองชั้นแก้ไม่ได้?** สองข้อ:

**ข้อ 1 — เครื่องมือ AI เกือบทุกตัวล็อกตัวเองไว้**

Jupyter/unsloth และ ComfyUI (ค่า default) จะ listen ที่ `127.0.0.1` — หมายความว่า **เครื่องอื่นเรียกเข้าไม่ได้เลย** แม้แต่ใน LAN

ทางแก้แบบเก่าคือสั่งให้ app เปิดรับจาก `0.0.0.0` — แต่พอทำแบบนั้น **ทั้งบ้านเห็นได้หมด** รวมถึงคนข้างบ้านถ้า Wi-Fi หลุด — และ app พวกนี้ส่วนใหญ่ไม่มีหน้า login เลย

serve แก้แบบตรงข้าม: **app ยังล็อกอยู่ตรงที่มันอยู่ (localhost)** แล้ว serve ยืนหน้าประตู — คนใน tailnet เดินมาเคาะประตู serve เปิดให้ คนนอกตึกไม่มีสิทธิ์เคาะ

**ข้อ 2 — HTTPS ที่ browser ไว้ใจ**

serve จัด certificate ให้เองอัตโนมัติ — ไม่ต้องทำเอง ไม่ต้องซื้อโดเมน ไม่ต้องจำว่า expire วันไหน

จำง่ายๆ แค่นี้: **app ยังอยู่ของมันอย่างปลอดภัย, serve คือคนกลางที่รับแขกให้ — และแขกคือแค่คนที่อยู่ในตึกเดียวกับคุณ**

## 03: คำสั่งจริง — แบบที่ทำงานได้วันนี้

เริ่มจากคำสั่งหลัก:

```bash
tailscale serve localhost:8080
```

Terminal จะตอบกลับมาแบบนี้:

```
Available within your tailnet:
https://phon-server.my-tailnet.ts.net

|-- / proxy http://127.0.0.1:8080

Press Ctrl+C to exit.
```

**ภายใน tailnet** — คำนี้สำคัญ: URL นี้เข้าได้เฉพาะเครื่องที่ login อยู่ใน tailnet ของคุณ

flags ที่ใช้ประจำ:

```bash
tailscale serve --http=8888 localhost:8888   # เข้าทาง http://phon-server:8888 (MagicDNS ชื่อย่อ)
tailscale serve --bg localhost:8080          # รันหลังพื้น — ไม่ต้องเปิด terminal ค้าง
tailscale serve text:"hello"                 # test ง่ายๆ — เปิด URL เห็นข้อความ = ทุกชั้นทำงาน
```

จัดการ:

```bash
tailscale serve status   # ดูว่าตอนนี้ serve อะไรอยู่บ้าง (สะสมได้หลาย service)
tailscale serve reset    # ล้างหมด
```

ผมรันทั้ง 3 service ค้างไว้พร้อมกัน — ตรวจด้วย `tailscale serve status` ได้ตลอด

**จุดที่ต้องรู้ 2 ข้อ:**

1. **syntax เปลี่ยนไปแล้ว** — tutorial เก่าๆ ที่เห็น `tailscale serve 443 --bg http://127.0.0.1:8080` เป็นของ client รุ่นเก่า (ก่อน v1.52) — ตอนนี้ใช้แบบใหม่ `tailscale serve localhost:8080` — เจอ tutorial แบบเก่าให้ข้ามไปได้เลย
2. **ต้องเปิด HTTPS certificates ของ tailnet ครั้งแรก** — รันคำสั่งแล้วถ้ายังไม่ได้เปิด CLI จะพาไปหน้าเว็บให้กดอนุญาตครั้งเดียว — จบตลอดไป

## 04: "เปิดแบบนี้แล้วใครก็เข้าได้ไหม?" — ไม่ (และนี่คือคำถามที่ถูกถามบ่อยที่สุด)

ตอบตรงๆ: **เข้าไม่ได้ — มีแค่เครื่องที่คุณ invite เข้า tailnet**

- ใครจะเข้าได้ = ขึ้นอยู่กับว่าคุณ invite ใครเข้า tailnet (แผนฟรี invite ได้ 6 users)
- เครื่องที่ลง Tailscale แต่ไม่ใช่สมาชิก tailnet ของคุณ → เข้าไม่ได้
- คนบนอินเทอร์เน็ตทั่วไป → ไม่มีทางเห็น URL นี้ด้วยซ้ำ (โดเมน `.ts.net` resolve เฉพาะจากใน tailnet)
- ACL ของ tailnet ยังคุมอีกชั้น — ถ้า ACL บล็อกเครื่องไหน เครื่องนั้นเข้าไม่ได้แม้รู้ URL

และเพราะ app ของคุณยัง bind อยู่แค่ `localhost` — แม้แต่คนใน LAN บ้าน (เช่น มือถือที่ต่อ Wi-Fi บ้าน) ก็เรียก port 8888 โดยตรงไม่ได้ ต้องผ่าน serve เท่านั้น

**ของแถมที่คุ้มมากตอนเริ่มให้คนอื่นใช้:** serve จะบอก backend ของคุณว่า **request นี้มาจากใคร** ผ่าน header `Tailscale-User-Login` — โดยไม่ต้องทำระบบ login, API key, หรือเขียน auth แม้แต่บรรทัดเดียว

ตัวอย่างกับ FastAPI:

```python
@app.post("/whoami")
async def whoami(request: Request):
    user = request.headers.get("Tailscale-User-Login", "unknown")
    return {"user": user}
```

เปิด URL นี้จากเครื่องที่ login แล้ว → ได้ `{"user": "phon@example.com"}` — รู้ทันทีว่าใครกำลังถามโมเดล, ใครกิน GPU เยอะสุด, มี query แปลกๆ ก็รู้ว่าจะไปคุยกับใคร

(ข้อเดียวที่ต้องจำ: backend ต้อง listen ที่ `127.0.0.1` เท่านั้น — ถ้าเปิดให้ใครก็เรียก port โดยตรงได้ คนนั้นปลอม header นี้เองได้)

## 05: ค่าใช้จ่าย — ฟรี

| แผน | ราคา | ได้มา |
|---|---|---|
| **Personal** | **$0 ตลอดกาล** | devices ไม่จำกัด, users สูงสุด 6, serve ใช้ได้ |
| Standard | $8/user/เดือน | users ไม่จำกัด, SCIM, MDM |
| Premium | $18/user/เดือน | ACL 300 groups, flow logs, JIT access |

สำหรับ use case "ใช้เองทุกเครื่อง + ปล่อยให้เพื่อนไม่กี่คน" — **แผนฟรีเหลือเฟือ** — devices ไม่จำกัดแปลว่า server + MacBook + มือถือ + iPad ของคนเดียวกันนับเป็น user คนเดียว

ราคาคิดเป็น **seat** (ตามจำนวนคน) ไม่ใช่จำนวนเครื่อง — เหมาะมากกับ pattern "คนเดียวหลายเครื่อง"

## 06: ข้อจำกัดที่ควรรู้ก่อนวางแผน

- **โดเมนถูกจำกัด** — ชื่อ URL เป็น `ชื่อเครื่อง.ชื่อ-tailnet.ts.net` เท่านั้น ใช้โดเมน custom เองไม่ได้
- **หลัง reboot ต้องรัน serve ใหม่** — ถ้าไม่ได้ใช้ `--bg` หรือทำ systemd unit (ทำไม่ยาก)
- **macOS:** serve โฟลเดอร์/ไฟล์ได้เฉพาะ client แบบ open-source (ตัวจาก App Store โดน sandbox จำกัด) — ถ้าใช้แค่ proxy HTTP แบบในบทความนี้ ไม่มีผล
- **เครื่องแบบ "tagged device"** (server ที่ใช้ tag แทน user) จะไม่ได้รับ identity headers — ถ้าใช้ feature "รู้ว่าใครใช้" ให้ login แบบ user ปกติ

## 07: Pro Tips แยกตามระดับ

**เพิ่งเริ่ม (ทำวันนี้ได้):**

1. ลง Tailscale ทั้งเครื่อง server และเครื่องที่ถือ (MacBook/มือถือ) — login อีเมลเดียวกัน
2. รัน `tailscale serve text:"hello"` บน server แล้วเปิด URL ที่มันโชว์จากอีกเครื่อง — เห็น "hello" แปลว่าทุกชั้นทำงาน
3. ค่อยรัน serve จริง: `tailscale serve --http=8888 localhost:8888` → เปิด `http://ชื่อเครื่อง:8888`
4. ใช้ `--bg` — แล้วไม่ต้องเปิด terminal ค้างอีกเลย

**ใช้จริงจัง (ทุกวันที่เครื่อง GPU):**

- ทำ systemd unit ให้ serve เริ่มเองหลัง reboot (server ผมทำทั้ง 3 service — reboot แล้วทุกอย่างกลับมาเอง)
- เช็ค `tailscale serve status` เป็นระยะ — ดูว่าอะไรค้างอยู่บ้าง
- อ่าน `Tailscale-User-Login` ทุก request — log ไว้ว่าใครใช้เมื่อไหร่ — ฟรี และไม่ต้องเขียน auth เอง
- ถ้าเริ่มให้เพื่อนใช้ — จำกฎเดียว: **app bind localhost เสมอ, เข้าทาง serve เท่านั้น**

## 08: สรุปแบบวิศวกรเป็ด

ถ้าย่อทั้งบทความเหลือบรรทัดเดียว:

**การเข้าถึงเครื่องของตัวเองไม่ใช่ปัญหา networking — มันคือปัญหา "จำชื่อไม่ได้ + เปิดประตูให้คนผิด" — ให้ระบบที่เสร็จแล้วจัดการแทนเรา**

serve ดึงงาน 4 อย่างที่เราชอบเก็บไว้ทำ "วันหลัง" (ตั้ง reverse proxy, จัด HTTPS, ทำ auth, จำ IP) ออกไปจากสมการ — เหลือคำสั่งเดียว: app ยังล็อกอยู่บน localhost อย่างปลอดภัย แต่จากคาเฟ่ไหนก็ได้ ผมเปิด `http://phon-server:8888` แล้วเจอ notebook ของตัวเอง

Duck OS Law #3: Protect System — ระบบที่ดีไม่ได้แปลว่าปิดทุกอย่าง แต่แปลว่า **เปิดในสิ่งที่ควรเปิด, มองเห็นว่ามีใครเข้ามา, และปิดได้ทันทีเมื่อไม่พึงประสงค์** — serve ทำสามอย่างนี้ให้ครบโดยไม่ต้องเขียนโค้ดแม้แต่บรรทัดเดียว

---

**คิดเห็นอย่างไร? คอมเมนต์ด้านล่างได้เลยคับ**

ติดตามคอนเทนต์เพิ่มเติมได้ที่:
- YouTube: https://www.youtube.com/@adduckivity
- Instagram: https://www.instagram.com/adduckivity
- Facebook: https://www.facebook.com/adduckivity
- X: https://x.com/adduckivity

#Adduckivity #DuckOS #Tailscale #LocalLLM #ComfyUI
