# Snapzy — สกรีนช็อต Mac ตัวฟรี open-source: CleanShot X ที่ไม่ต้องจ่าย $29

<!--
ContentID: 20260907-CNT-SNAPZY-LF
Series: (standalone — ไม่มีภาคก่อนหน้าใน index.json)
Type: Long Form (~2000-2500 words)
Status: Draft — รอ review
Sources (verified 2026-09-07):
- https://snapzy.app/ (official site — features, free & OSS, community $99 goal, macOS 13+, Intel & Apple Silicon, notarized)
- https://snapzy.app/docs/getting-started/ (docs — system requirements, 3-step install, permissions)
- https://github.com/duongductrong/Snapzy (README — full feature list, brew install, security model, BYO-S3/R2 cloud, TOML config, Raycast integration)
- https://api.github.com/repos/duongductrong/Snapzy (repo meta — BSD-3-Clause, 3,068 stars, 170 forks, 67 open issues, created 2026-01-15, latest push 2026-09-05)
- https://api.github.com/repos/duongductrong/Snapzy/releases/latest (v1.31.0, 2026-08-15 — OCR, magnifier/pixel grid/color picker, window shadow pref, Raycast integration)
- https://macmenubar.app/app/snapzy (directory listing — feature summary, sandbox + minimal entitlements, no third-party data)
- CleanShot X pricing: https://cleanshot.com/buy + https://toolradar.com/tools/cleanshot/pricing (Aug 2026: $29 one-time, 1GB cloud, 1yr updates, optional $19/yr renewal)
Vendor: duongductrong (individual OSS maintainer), BSD 3-Clause License, Mac App Store (post Apple Developer Program goal)
Note: "Snapzy" ชื่อซ้ำกับ snapzy.ai (mobile camera apps) และ Snapzy burst camera (App Store) — บทความนี้เกี่ยวกับ snapzy.app เท่านั้น
-->

## 00: Hook — "จ่าย $29 ก็ถูก… ถ้ามีตัวฟรีที่ทำได้เท่ากัน"

คนที่ทำงานบน Mac เกือบทุกคนเจอ flow เดียวกัน: กด ⌘Shift+4 → ถ่าย → เปิด Preview → ดึงลูกศร วาดวงกลม เขียนข้อความ → export → แชร์

ปัญหาจริงไม่ใช่ screenshot — ปัญหาคือ **capture pipeline กระจาย** — macOS builtin ถ่ายได้แต่ annotate ไม่ได้เต็มที่, Preview slow, แชร์ต้องผ่าน airdrop/อีเมล/ลิงก์ — ทุกครั้งที่อยาก "ส่งหน้าจอให้คนอื่นเห็น" ต้อง context switch 2-3 รอบ

CleanShot X คือคำตอบมาตรฐานของตลาด: $29 one-time, ฟีเจอร์ครบ, คนใช้กัน 10 ปี — แต่ทุกวันนี้มีตัวเลือกที่ **ฟรี 100% open-source** ฟีเจอร์ไล่เลี่ยกัน ชื่อ **Snapzy**

บทความนี้จะเล่าครบ: มันคืออะไร, ทำงานยังไง, features, ราคา (มีเรื่องสนุกเบื้องหลังราคา), ข้อดีข้อเสียตรงๆ, เทียบ CleanShot X, และมันเหมาะกับใคร

## 01: Snapzy คืออะไร — "Menu bar capture pipeline ตัวเดียว"

> Snapzy = native macOS app (SwiftUI + AppKit + ScreenCaptureKit + Vision) ที่ทำ screenshot, screen recording, annotation, OCR, และ share — ทั้งหมดจาก menu bar, ฟรี, open-source (BSD-3-Clause)

คิดแบบนี้คับ: ทุกครั้งที่คุณ "จับหน้าจอ" มันคือ pipeline 4 ขั้น —

| ขั้น | macOS builtin | CleanShot X | Snapzy |
|---|---|---|---|
| Capture | ✅ (⌘Shift+3/4/5) | ✅ | ✅ |
| Annotate | ❌ (ต้องเปิด Preview) | ✅ in-place | ✅ in-place |
| Record/GIF | ⚠️ (QuickTime) | ✅ | ✅ |
| Share | ❌ | ✅ (cloud ของมัน) | ✅ (cloud ของคุณเอง) |

Snapzy รวม 4 ขั้นนี้เข้า menu bar app ตัวเดียว — กด shortcut → พื้นที่เลือก → ลูกศร/blur/ข้อความ → copy/upload/save — จบใน 10 วินาที

ข้อ technical ที่น่าภูมิใจ: มัน native จริงๆ (ไม่ใช่ Electron), signed + notarized โดย Apple, Hardened Runtime, sandboxed — และ **privacy by design**: offline-first, data ของคุณไม่ออกจากเครื่องยกเว้นตอนที่คุณสั่ง upload ด้วยตัวเอง (รายละเอียดข้อนี้สำคัญ — อยู่ในข้อเสียด้วย)

## 02: มันทำงานยังไง — 3 workflow

**1. Quick capture** — กด shortcut (default ตั้งเองได้) → drag เลือกพื้นที่ (มี magnifier + pixel grid + crosshair + color picker ใน v1.31) → capture เสร็จแล้ว **Quick Access** panel ลอยขึ้นมา — copy / edit / drag ไปใส่ app / open / delete — ได้เลย

**2. Annotate + OCR** — รูปที่จับได้เปิดใน editor ในตัว: ลูกศร, shape, text, highlighter, watermark, blur/pixelate, counter — มีฟีเจอร์ที่โคตรเหมาะกับงาน dev: **automatic redaction** (blur ข้อมูล sensitive ที่ตรวจจับได้เองอัตโนมัติ) และ **OCR** — extract ตัวอักษรจากภาพ (หรือ frame จากวิดีโอ) ลง clipboard โดยตรง — ใช้ Apple Vision บนเครื่อง (ฟรี) หรือต่อ custom endpoint แบบ OpenAI-compatible

**3. Record + Video Editor** — record screen เป็น video หรือ GIF, system audio + mic, mouse click highlight, keystroke overlay — record เสร็จเปิด Video Editor: trim, zoom segment (Follow Mouse — ซูมตามเมาส์แบบ video tutorial), background/panning, export GIF

killer feature ที่คนใช้ CleanShot X อาจไม่ได้คิดว่าจะเจอ: **Application Capture ที่จับ popover ของ menu bar app ตัวอื่นได้ด้วย** — ปกติคุณกด capture เดี๋ยว popover ของ app ที่เปิดอยู่ก็หาย แต่ Snapzy จับมันไว้ restore visually ให้เลือก แล้ว save ออกมาเป็น transparent rounded corner — ใช้ทำ screenshot UI สำหรับ blog/docs ได้เลย

## 03: Features เด่น (verified จาก README + changelog v1.31.0)

1. **Scrolling capture** — จับหน้าเว็บยาว/เอกสารยาวเป็นภาพเดียว live stitched preview
2. **OCR** — Apple Vision on-device หรือ custom endpoint + downloadable PP-OCR models (ใหม่ใน v1.31.0)
3. **Subject cutout** — ตัด background ออกจากวัตถุในรูป + safe auto-crop
4. **Window shadow capture** (macOS 14+) — จับหน้าต่างแบบมี shadow สวยๆ
5. **Capture History** — panel ประวัติ screenshot/video/GIF ทั้งหมด: search, filter by type/time, one-click re-open in editor
6. **Cloud share แบบ BYO** — upload รูป/วิดีโอ/GIF เข้า **S3 หรือ Cloudflare R2 ของคุณเอง** ได้ลิงก์ share + auto-expiration 1-90 วัน + custom domain — credentials อยู่ใน Keychain
7. **Raycast integration** + global shortcuts ที่ custom ได้หมด (มี conflict detection)
8. **10 ภาษา** — EN, VI, 简中, 繁中, ES, JA, KO, RU, FR, DE — per-app language, สลับได้ไม่ต้อง restart
9. **Multi-format** — PNG/JPG/WebP, hide desktop icons/widgets, quick screenshot ระหว่าง recording
10. **TOML config export/import** — backup ตั้งค่าย้ายไปเครื่องอื่น/ใส่ dotfiles ได้

## 04: Pricing — ฟรี… และมีเรื่องสนุกอยู่เบื้องหลัง

| | รายละเอียด |
|---|---|
| ราคา | **ฟรี 100%** — open-source BSD-3-Clause, ไม่มี subscription, ไม่มี ads, ไม่มี license key |
| อัปเดต | ฟรีตลอด — in-app updater (Sparkle) |
| Cloud storage | ไม่มีของ vendor — คุณต้อง自备 S3/R2 (ถ้าใช้) — ค่า bucket R2 ปกติไม่กี่ cent ถึง $1/เดือน |
| Mac App Store | ✅ (เพิ่งเข้า — ดูข้างล่าง) |

เรื่องที่ต้องเล่า: Snapzy **crowdfund เงิน $99 ของ Apple Developer Program** — community ช่วยกันจ่ายจน goal 100% แล้ว (หน้าเว็บ official ยังมี banner "Goal Reached! 100% of $99 goal") — นั่นคือเหตุผลที่วันนี้มันโหลดได้ทั้งจาก GitHub release, `brew install --cask snapzy`, และ Mac App Store — app ฟรีที่ไม่ต้อง trust vendor ที่ไม่รู้จัก เพราะ code เปิดตรวจสอบได้ทั้งหมด + notarized โดย Apple

repo data (ณ 2026-09-07): **3,068 stars, 170 forks, สร้าง 2026-01-15, active push 2026-09-05, latest v1.31.0 (2026-08-15)** — project ยังอายุน้อยแต่ momentum จริง

## 05: ข้อดี ✅

- **ฟรี + open-source** — feature set ระดับ $29 โดยไม่จ่ายเลย, code ตรวจสอบได้ (vs CleanShot X closed-source)
- **Privacy model ที่ชัดเจน** — offline-first, sandboxed + minimal entitlements, network requests จำกัดแค่ Sparkle update check + upload ที่คุณสั่งเองไปที่ bucket ของคุณ — ไม่มี telemetry, ไม่มี third-party server
- **Native performance** — menu bar app footprint เบา, มี Activity Monitor ในตัว (CPU/RAM ของตัวมันเอง) — fluid บนทั้ง Intel และ Apple Silicon
- **ครบ pipeline** — capture → annotate → OCR → record → video edit → share ในตัวเดียว
- **Feature ใหม่ต่อเนื่อง** — v1.31.0 เพิ่ม OCR, magnifier + color picker, Raycast — release cycle เร็ว (67 open issues แต่ push ล่าสุดคือ 2 วันก่อนบทความนี้)
- **Raycast + shortcuts + TOML config** — เข้ากับ power user workflow ได้ลึก

## 06: ข้อเสีย ❌ — ตรงๆ ไม่อวย

- **Project ยังอายุน้อย** — เริ่ม ม.ค. 2026 (~8 เดือน) vs CleanShot X ที่ polish มา ~10 ปี — edge cases บางอย่าง (non-Retina rendering, retina annotation) ยังอยู่ใน bug fix stage ของ changelog
- **Cloud share ต้อง DIY** — CleanShot X จ่าย $29 ได้ cloud 1GB + ลิงก์ share แบบ zero-config; Snapzy ฟรี แต่ **ต้องไปมี S3/R2 bucket ตัวเองก่อน** — คนที่ไม่อยากแตะ AWS/Cloudflare ต้องข้ามฟีเจอร์นี้ไป (หรือใช้ copy/edit แทน)
- **macOS only** — ไม่มี Windows/Linux/iOS (CleanShot X ก็ macOS only — ข้อนี้ tie ไม่ได้ต่าง)
- **UI ไม่มีภาษาไทย** — รองรับ 10 ภาษา แต่ไม่มี TH (มี VI/中文/JA/KO) — อ่านเมนูภาษาอังกฤษก่อน
- **Single maintainer** — repo หลักคือ duongductrong คนเดียว (มี contributors แต่ core เป็นคนเดียว) — bus factor สูงกว่า vendor ที่มี team
- **OCR custom endpoint ต้องมี API key** — ฝั่ง Apple Vision ใช้ฟรีบนเครื่อง แต่ถ้าอยากต่อ endpoint ภายนอกต้องจัดการ key เอง
- **67 open issues** — project ที่โตเร็วจะมี bug อยู่ — acceptable สำหรับ free tool, แต่คนที่ต้องการ "ตั้งแล้วไม่แตะเลย 5 ปี" อาจยังเร็วไป

## 07: เทียบกับคู่แข่ง

| | Snapzy | CleanShot X | macOS builtin | ShotX / OSS อื่นๆ |
|---|---|---|---|---|
| Price | ฟรี (OSS) | $29 one-time + $19/yr renewal (optional) | ฟรี | ฟรี (OSS) |
| Scrolling capture | ✅ | ✅ | ❌ | ⚠️ ไม่ครบทุกตัว |
| OCR | ✅ (Vision/endpoint) | ✅ | ⚠️ (Live Text) | ❌/⚠️ |
| Video + GIF editor | ✅ | ✅ | ⚠️ (QuickTime) | ❌ |
| Cloud share | BYO S3/R2 | ✅ 1GB รวม | ❌ | ❌ |
| Redaction/blur | ✅ + auto-redaction | ✅ | ❌ | ⚠️ |
| Maturity | ~8 เดือน | ~10 ปี | 15+ ปี | หลากหลาย |
| Source | Open (BSD-3) | Closed | Closed | Open |

**Bottom line:** ถ้าต้องการ zero-config cloud + maturity 10 ปี = CleanShot X $29 ยังคุ้ม; ถ้าต้องการ feature set เกือบเท่ากัน + privacy-first + free + open-source = Snapzy ชนะในราคา

## 08: เหมาะกับใคร (Pro Tips แยกตามระดับ)

**มือใหม่ / คนอยากลอง** — `brew install --cask snapzy` → อนุญาต Screen Recording ครั้งแรก → ใช้แทน ⌘Shift+4 ไปเลย — ตั้ง shortcut ของ Application Capture (`A`) ไว้จับหน้าต่างแบบมี shadow — 15 นาทีแรกพอ

**Content creator / dev ที่ทำ docs** — เปิด auto-redaction ไว้ก่อนทุกครั้ง (ป้องกัน secret/credential รั่วใน screenshot), ใช้ Subject cutout + mockup backgrounds สำหรับ hero image, OCR เพื่อยก text จาก screenshot ตรงๆ, window shadow capture สำหรับ UI shots

**Power user / self-hosters** — ต่อ BYO S3/R2 bucket (R2 free tier 10GB) + auto-expiration 7 วัน + custom domain → share pipeline ของคุณไม่ผ่าน vendor ไหน, export TOML config ใส่ dotfiles → ตั้งค่า sync ทุกเครื่อง, Raycast integration เข้า command palette เดียวกับ tool อื่น

**ไม่เหมาะถ้า:** คุณใช้ Windows (ไม่มี version), คุณไม่แตะ cloud storage เลยและต้องการ share zero-config (CleanShot X ง่ายกว่า), หรือคุณต้องการ UI ภาษาไทย (ยังไม่มี — ใช้ EN ไปก่อน)

## 09: สรุปแบบวิศวกรเป็ด

Snapzy คือคำตอบของคำถาม "CleanShot X แต่ $0" — pipeline capture→annotate→OCR→record→share ครบ, native, fast, privacy-first (offline-first, BYO cloud), open-source ตรวจสอบได้ — exchange ที่ต้องแลก: project ยัง 8 เดือน, cloud share ต้อง DIY, และ UI ยังไม่มีภาษาไทย

ในฐานะคนที่ใช้ Mac เป็น production machine ทุกวัน — มาตรฐานใหม่ตอนนี้คือ: **builtin สำหรับจับ 1 ที, Snapzy สำหรับจับแล้วต้อง edit/share, CleanShot X สำหรับคนที่จ่าย $29 แล้วอยากได้ cloud zero-config** — เครื่องพรเองลง Snapzy ไว้คู่กับ builtin ไปก่อน — เพราะ feature ที่เจอแล้วลืมไม่ได้คือ auto-redaction + OCR ในตัวเดียวกัน

ถ้าคุณใช้ Mac + screenshot เป็น daily tool — ลอง Snapzy ก่อนคิดเงินครับ — มันฟรีจริง, open-source จริง, และ community ใหญ่พอ (3,000+ stars) ที่จะอยู่ต่อ

#Adduckivity #DuckOS #NeuroDivergent #Snapzy #CleanShotX #macOS #Screenshot #OpenSource #Productivity
