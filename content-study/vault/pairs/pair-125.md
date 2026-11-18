---
pair: 125
hash: e87e89fd36-507104
date: 20261118
---

# Rakazo บนเครื่องเราเอง — บันทึก 3 วันแรกที่ทีม AI ทำงานจริงบน Docker

- **status:** draft v1 (TECH first-look จาก deployment จริง — ทุกตัวเลขยืนยันจากเครื่อง: 6 containers compose up 16 พ.ย. 15:52, images 2.82+2.39GB, web 5173 + tailscale tailnet-only, sandbox mounts ro/rw, โมเดลผ่าน llama-server 8080, งานจริงชุดแรก 23:05 ซิงก์ 3 ไฟล์ → 403 (token timing) → cherry-pick 3e6f0eb 18 พ.ย.; battery 269wc PASS (พร 1 + FP พร้อม 2, เรา 5, CUT 0, odd-codepoints ','/' form-legitimate TECH); Notion 41cdf8d8-8d8c-81d5-89ba-e9c0600baa3a 35 blocks verify ครบ — รอ Benz r1)
- **date:** 20261118
- **ไฟล์โพสต์:**
  - [20261118-cnt-rakazo-local-docker-first-days](../posts/20261118-cnt-rakazo-local-docker-first-days.md)

## บันทึก

sibling guard: #103 zcode-review + 20260904 autoclaw-zcode-combo — axis = self-host deployment + machine-verifiable evidence; secrets 0 (ไม่มีค่าจาก .env, hostname tailnet-only อยู่ Source prop เท่านั้น)
