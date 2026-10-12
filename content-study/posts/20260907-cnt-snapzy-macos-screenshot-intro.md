# Snapzy — สกรีนช็อต Mac ตัวฟรี open-source: CleanShot X ที่ไม่ต้องจ่าย $35

<!--
ContentID: 20260907-CNT-SNAPZY-LF
Series: (standalone — ไม่มีภาคก่อนหน้าใน index.json)
Type: Long Form (~2,200 words)
Status: Draft — rewritten as long form 2026-10-12 (v2 ของ draft 2026-09-07 — Notion page เดิม)

CHANGELOG รอบ rewrite (2026-10-12):
- ราคา CleanShot X อัปเดต: $29 → $35 one-time (Basic) + Pro subscription $10/mo billed annually — ณ วันนี้ title และ hook แก้ตาม
- Snapzy v2.0.0 (28 ก.ย. 2026) = Liquid Glass redesign (breaking) + Delayed Capture + record whole display + drag-to-draw crop; v2.1.0-beta.3 (10 ต.ค.)
- Security model แก้ให้ตรง README วันนี้: **NOT sandboxed** (draft เดิมเขียน "sandboxed" จาก macmenubar.app listing — ผิด) — จริงคือ Hardened Runtime + Developer ID signed + notarized + minimal entitlements + library validation + network allowlist + no telemetry
- Cloud เพิ่ม Google Drive (นอกจาก S3/R2) + OAuth loopback
- Feature ใหม่: Smart Capture (element snapping), Capture Markup (วาดบนจอจริงก่อน capture), Pin to Screen, camera overlay + Continuity Camera, live annotation ระหว่าง record, snapzy:// URL scheme, Combine images, uninstall/reset-permissions scripts
- Repo: 3,068 → 3,334 stars, 170 → 190 forks, 67 → 77 issues, push ล่าสุด 11 ต.ค. 2026, อายุ ~9 เดือน
- Contributors: เริ่มมี external (adrianocr, archibald-nice, thanhthai3010, mvanhorn, tukuyomil032) — ไม่ใช่คนเดียวเต็มตัวแล้ว แต่ core ยัง duongductrong
- Mac App Store: ตัดออก (README/site วันนี้ไม่มี MAS — install = brew / DMG / install.sh)
- OCR benchmark = ของทีมโปรเจกต์เอง บน corpus สังเคราะห์ (19 เม.ย. 2026) — ใส่แบบ Anti-Hype + caveat verbatim

Sources (re-verified 2026-10-12):
- https://snapzy.app/ (site — features 20, localization 10 ภาษา ES/FR/DE "Soon" ใน UI rotate แต่ README นับครบ 10, Reddit testimonials verbatim)
- https://raw.githubusercontent.com/duongductrong/Snapzy/master/README.md (features เต็ม, shortcuts, snapzy:// URLs, OCR benchmark table, Security section, install/uninstall scripts)
- https://api.github.com/repos/duongductrong/Snapzy (3,334 stars / 190 forks / 77 issues / BSD-3-Clause / created 2026-01-15 / pushed 2026-10-11)
- https://api.github.com/repos/duongductrong/Snapzy/releases (v2.0.0 2026-09-28 + v2.1.0-beta.3 2026-10-10 + release notes มี external contributors)
- https://cleanshot.com/pricing + /buy (CleanShot Basic $35 one-time + cloud 1GB + renewal $19/yr; CleanShot Pro $10/user/mo billed annually = unlimited cloud; ณ 12 ต.ค. 2026)
Vendor: duongductrong (OSS maintainer + external contributors), BSD 3-Clause
Note: "Snapzy" ชื่อซ้ำกับ snapzy.ai (mobile camera apps) และ Snapzy burst camera (App Store) — บทความนี้เกี่ยวกับ snapzy.app เท่านั้น
Honesty: เครื่องที่เขียนบทความนี้เป็น Linux server — ไม่มี Mac จริงไว้ยิง benchmark เอง ตัวเลข performance ทั้งหมด = ของทีมโปรเจกต์ + อ้างแหล่งชัด
-->

## 00: Hook — "จ่าย $35 ก็ยังถูก… ถ้ามีตัวฟรีที่ทำได้เท่ากัน"

คนทำงานบน Mac เกือบทุกคนเจอ flow เดียวกัน: กด ⌘Shift+4 → ถ่าย → เปิด Preview → ดึงลูกศร วาดวงกลม เขียนข้อความ → export → แชร์

ปัญหาจริงไม่ใช่ screenshot — ปัญหาคือ **capture pipeline กระจาย** — macOS builtin ถ่ายได้แต่ annotate ไม่ได้เต็มที่, Preview ช้า, การแชร์ต้องผ่าน AirDrop/อีเมล/ลิงก์ — ทุกครั้งที่อยาก "ส่งหน้าจอให้คนอื่นเห็น" ต้อง context switch 2-3 รอบ

CleanShot X คือคำตอบมาตรฐานของตลาดมา 10 ปี — และณ วันที่ 12 ต.ค. 2026 ราคาอยู่ที่ **$35 สำหรับ CleanShot Basic (one-time, รวม cloud 1GB + อัปเดต 1 ปี, ต่ออายุ optional $19/ปี)** หรือจะจ่าย **CleanShot Pro แบบ subscription $10 ต่อเดือน (จ่ายรวมรายปี)** เพื่อ cloud ไม่จำกัด — ราคาต่อใบอนุญาตเดิมที่หลายคนจำกันคือ $29

แต่ตอนนี้มีทางเลือกที่ **ฟรี 100% open-source** ฟีเจอร์ไล่เลี่ยกัน โตจาก 3,000 กว่า stars ขึ้นไปเกือบ 3,400 ในเวลา 9 เดือน ชื่อ **Snapzy**

บทความนี้เล่าครบ: มันคืออะไร, ทำงานยังไง, 12 features เด่น, ราคา (มีเรื่องสนุกเบื้องหลัง), ข้อดีข้อเสียตรง ๆ รวมถึงข้อที่หลายรีวิวเขียนผิด, เทียบกับ CleanShot X, และเหมาะกับใคร

## 01: Snapzy คืออะไร — "Menu bar capture pipeline ตัวเดียว"

> Snapzy = native macOS app (SwiftUI + AppKit + ScreenCaptureKit + Vision + Sparkle) ที่ทำ screenshot, screen recording, annotation, OCR, และ share — ทั้งหมดจาก menu bar, ฟรี, open-source สัญญาอนุญาต BSD-3-Clause

คิดแบบนี้คับ: ทุกครั้งที่คุณ "จับหน้าจอ" มันคือ pipeline 4 ขั้น —

| ขั้น | macOS builtin | CleanShot X | Snapzy |
|---|---|---|---|
| Capture | ✅ (⌘Shift+3/4/5) | ✅ | ✅ |
| Annotate | ❌ (ต้องเปิด Preview) | ✅ in-place | ✅ in-place |
| Record/GIF | ⚠️ (QuickTime) | ✅ | ✅ |
| Share | ❌ | ✅ (cloud ของมัน) | ✅ (cloud ของคุณเอง) |

Snapzy รวม 4 ขั้นนี้เข้า menu bar app ตัวเดียว — กด shortcut → พื้นที่เลือก → ลูกศร/blur/ข้อความ → copy/upload/save — จบในไม่กี่วินาที

เรื่อง technical ที่ตัวมันภูมิใจ: เป็น native app จริง ๆ (ไม่ใช่ Electron), signed + notarized โดย Apple, เปิด Hardened Runtime — และ **privacy by design**: offline-first, ไม่มี telemetry, network requests ถูกจำกัดเป็น allowlist ชัด ๆ (เดี๋ยวเล่าต่อข้างล่าง — จุดนี้หลายรีวิวเขียนกันผิด)

## 02: Security model ที่ควรอ่านก่อนใช้ — ตรงจาก README ไม่ผ่านคนกลาง

ข้อนี้ draft รอบแรกของบทความนี้เขียนผิด ต้องแก้ให้ตรงก่อนขายต่อ: **Snapzy ไม่ได้ทำงานใน macOS App Sandbox** — มันรันด้วยสิทธิ์ของ user account คุณเต็ม ๆ

สิ่งที่มันใช้แทนคือ: Hardened Runtime + Developer ID signing + notarization โดย Apple + entitlements น้อยชิ้น + library validation เปิด (โหลดได้แค่ code ที่เซ็นโดย Snapzy หรือ Apple)

network side เขียนไว้ชัดใน README: network ทั้งหมดมีแค่ (1) เช็คอัปเดตผ่าน Sparkle (2) OAuth callback บน local loopback (3) upload ที่คุณกดเอง ไปยัง storage ของคุณ (S3 / R2 / Google Drive) (4) โหลด OCR model เสริมจาก HTTPS/Hugging Face ที่คุณระบุเอง — catalog model เริ่มต้นว่างเปล่า ไม่มีอะไรถูก fetch จนกว่าคุณจะเพิ่ม

credentials ทั้งหมดอยู่ใน macOS Keychain + ตั้งรหัสคุ้มครองเพิ่มได้ + export/import แบบเข้ารหัสด้วย passphrase ที่คุณตั้ง

มุมตรง ๆ: การไม่ sandbox ของ app จับหน้าจอไม่ใช่เรื่องแปลก แต่มันแปลว่าขอบเขตความปลอดภัยจริง ๆ ของตัวนี้คือ "code เปิดตรวจสอบได้ + Apple ตรวจ notarize + network allowlist" — ถ้าคุณเป็นสายรีวิว code ก่อนใช้ มันสร้างมาให้ตรวจได้จริง ถ้าคุณต้องการ sandbox guarantee เฉพาะตัว อ่านส่วนข้อเสียก่อนติดตั้งคับ

## 03: มันทำงานยังไง — 4 workflow

**1. Quick capture** — กด shortcut (ปรับได้หมด มี conflict detection กับ shortcut ระบบ) → drag เลือกพื้นที่ มี magnifier + pixel grid + crosshair + กด copy ค่าสี RGB/HEX ระหว่างเลือก → โหมด `Application Capture` (default ปุ่ม `A`) จับหน้าต่างแบบมีเงา และจับ **popover ของ menu bar app ตัวอื่นได้ด้วย** — popover ปกติหายทันทีที่เริ่ม capture แต่ Snapzy restore ให้เลือกแล้ว save ออกมาเป็นมุมโค้งโปร่ง — อันนี้ยังเป็น killer feature สำหรับคนทำ blog/docs เหมือนเดิม — capture เสร็จ **Quick Access** panel ลอยขึ้นมา: copy / edit / drag ใส่ app / pin / upload / delete พร้อม shortcut บนการ์ด (⌘C, ⌘S, ⌘E, ⌘U, ⌘P)

**2. Annotate + OCR** — editor ในตัว: ลูกศร (มี Bezier control สำหรับเส้นโค้ง), shape, text, highlighter ที่ snap กับข้อความ, watermark, blur/pixelate, counter, crop แบบ snap ขอบ — ใหม่เด่นคือ **mockup backgrounds กับ 3D renderer** ทำ hero image ได้ในตัว — และ **automatic redaction** ตรวจจับข้อมูล sensitive ในภาพเพื่อ blur เองอัตโนมัติ — **OCR** ดึงตัวอักษรจากภาพ (หรือ frame วิดีโอ) ลง clipboard: engine default คือ Apple Vision รันบนเครื่อง ฟรี ไม่ออก net, ถ้าอยากได้ engine อื่นต่อ custom endpoint แบบ OpenAI-compatible ได้ (API key อยู่ใน Keychain เหมือนกัน)

**3. Record + Video Editor** — record เป็นวิดีโอหรือ GIF, system audio + mic, **camera overlay รองรับ iPhone Continuity Camera**, mouse click highlight, keystroke overlay, และ **live on-screen annotation** — วาดบนจอระหว่าง record ได้ — record ทั้งจอเพิ่งง่ายขึ้นใน v2.0.0 (คลิกหรือกด Enter) — จบแล้วเข้า Video Editor: trim บน timeline + frame strip, zoom segment แบบ Follow Mouse (ซูมตามเมาส์สำหรับ video tutorial), wallpaper background + padding, ตั้ง resolution export, ปรับ GIF ขนาด, undo/redo

**4. หลังจับ — เก็บและหาคืน** — **Pin to Screen** ตรึงรูปลอยบนจอไว้เทียบงาน (zoom ปักหมุดปรับได้ใน v2.1 beta), **Capture History** ค้นหา + กรองตามชนิด/เวลา + เปิดกลับเข้า editor ได้ทีเดียว + ตั้ง retention policy ลบของเก่าเอง, และ cloud upload แบบ BYO (เดี๋ยวโผล่อีกรอบในส่วน features)

มี workflow ที่ 5 แบบไม่ต้องแตะหน้าจอ: **Delayed Capture** — ตั้ง countdown แล้วเปิด dropdown/tooltip/hover state ที่ต้องใช้เวลา จับตอนพร้อมแทนที่จะจับก่อนแล้วเสียใจ

shortcut ที่ใช้บ่อย (default จาก README — ปรับใหม่ได้ทุกตัว):

| Action | Shortcut |
|---|---|
| Fullscreen screenshot | `⇧⌘3` |
| Area screenshot | `⇧⌘4` |
| ↳ Toggle โหมด Application Capture | `A` (ตอนลากเลือก) |
| Area + inline annotate (วาดก่อน save) | `⇧⌘7` |
| Scrolling screenshot | `⇧⌘6` |
| Record start/stop | `⇧⌘5` |
| OCR ดึงข้อความ | `⇧⌘2` |
| Object cutout | `⇧⌘1` |
| เปิดรายการ shortcut ทั้งหมด | `⇧⌘K` |

ข้อสังเกตจากตาราง: Snapzy พยายามขึ้น shortcut ชุดเดียวกับ macOS builtin (⇧⌘3/4/5) ให้มือจำเดิมได้เลย แล้วเพิ่มตัวเลขใหม่ (6/7/2/1) เป็นชั้นความสามารถที่ builtin ไม่มี — กลยุทธ์ที่ทำให้ต้นทุนการย้ายจาก builtin ต่ำมาก: กดเหมือนเดิมทุกอัน แค่ได้ editor กับ history ตามมา

## 04: Features เด่น 12 ข้อ (verified จาก README + changelog ถึง v2.1.0-beta.3, ต.ค. 2026)

1. **Scrolling capture** — จับหน้าเว็บยาว/เอกสารยาวเป็นภาพเดียว พร้อม live stitched preview
2. **OCR 10 ภาษา** — Apple Vision on-device หรือ custom endpoint + โหลด PP-OCR model เสริมได้ (ทีมโปรเจกต์ publish benchmark ของตัวเองไว้ — วิเคราะห์ในหัวข้อข้อเสีย)
3. **Smart Capture** — auto-detect จับเป็น element: ปุ่ม, การ์ด, เมนู, section ของ UI แทนการลากเอง
4. **Capture Markup** — วาดลูกศร/คำอธิบาย/เลขขั้นตอน **บนหน้าจอจริงก่อนกดจับ** ไม่ต้องรอเปิด editor
5. **Subject cutout** — ตัด background ออกจากวัตถุในรูป + safe auto-crop + mockup background ด้วย 3D renderer
6. **Window shadow capture** (macOS 14+) — จับหน้าต่างแบบมีเงาสวยพร้อมโพสต์
7. **Delayed Capture** — countdown timer สำหรับ state ที่จับยาก
8. **Pin to Screen** — ตรึงภาพลอย ๆ ไว้เทียบข้อมูลระหว่างทำงาน
9. **Capture History + retention** — ค้น/กรอง/เปิดแก้ซ้ำ + นโยบายเก็บกี่วันลบเอง
10. **Cloud share แบบ BYO** — S3 หรือ Cloudflare R2 หรือ **Google Drive ของคุณ** (เพิ่มในช่วงหลัง), ลิงก์ share + auto-expiration 1-90 วัน + custom domain, credentials อยู่ Keychain
11. **Automation ครบ** — `snapzy://` URL scheme เรียกทุก action จาก script/Raycast/Alfred (เช่น `snapzy://capture/ocr`) + Raycast extension ทางการ + Combine images รวมหลายรูป
12. **TOML config export/import + 10 ภาษา** — backup ตั้งค่าใส่ dotfiles ย้ายเครื่องได้ (มี uninstall.sh / reset-permissions.sh ให้ล้างครบถึง TCC permission), UI รองรับ EN/VI/简中/繁中/ES/JA/KO/RU/FR/DE สลับ per-app ไม่ต้อง restart

## 05: Pricing — ฟรี… และมีเรื่องสนุกอยู่เบื้องหลัง

| | รายละเอียด |
|---|---|
| ราคา | **ฟรี 100%** — open-source BSD-3-Clause, ไม่มี subscription, ไม่มี ads, ไม่มี license key, ไม่ต้อง login |
| อัปเดต | ฟรีตลอด — in-app updater (Sparkle), stable + beta channel |
| Cloud storage | ไม่มีของ vendor — เอา S3/R2/Google Drive ของคุณมาเอง (bucket R2 ปกติไม่กี่ cent ถึง ~$1/เดือน) |
| ติดตั้ง | `brew install --cask snapzy` / DMG จาก GitHub release / install.sh |

เรื่องที่อยากเล่า: ช่วงเปิดตัว maintainer **ขาดเงินค่า Apple Developer Program $99** — community ช่วยกัน crowdfund จนครบ goal — ตัว app จึงผ่าน notarization และโหลดได้โดยไม่ต้อง trust เครื่องคอมไพล์ลอย ๆ — วันนี้เขาเปิด GitHub Sponsors + Ko-fi ไว้แล้วถ้าใครอยากคืนกำลังใจ

และ social proof สด ๆ จากหน้าเว็บทางการ (คัดมาจาก Reddit, เก็บคำ verbatim): *"Thanks man i am using it since 10 days. Didn't had any money to purchase cleanshot, this came very handy to me."* — u/Candid_Advertising — หรือคนที่ใช้ CleanShot ที่ทำงานแล้วเอา Snapzy กลับบ้าน — กลุ่ม user จริงมันคือ "คนที่อยากได้ CleanShot แต่ยังไม่จ่าย"

repo data (ณ 2026-10-12): **3,334 stars, 190 forks, สร้าง 15 ม.ค. 2026 (อายุ ~9 เดือน), push ล่าสุด 11 ต.ค. (เมื่อวาน), latest stable v2.0.0 (28 ก.ย. 2026) + beta v2.1.0-beta.3 (10 ต.ค.)** — 77 open issues กับ release cycle เกือบรายสัปดาห์ — และจุดที่เปลี่ยนจากรอบก่อน: **release notes เริ่มมี external contributors แล้ว** (5-6 ชื่อใน 2 เดือนล่าสุด) ไม่ใช่ commit คนเดียวเต็มตัว

v2.0.0 เองคือ milestone ใหญ่ของ project อายุ 9 เดือน: ย้าย UI ทั้งตัวไป **Liquid Glass** (design language ใหม่ของ Apple — ถือเป็น breaking change ตัวแรกของ repo) พร้อม Delayed Capture + จับ record ทั้งจอแบบหนึ่งคลิก + crop ลากวาดใหม่

## 06: ข้อดี ✅

- **ฟรี + open-source** — feature set ระดับ $35 โดยไม่จ่ายเลย, code ตรวจสอบได้ (vs CleanShot X closed-source)
- **ครบ pipeline** — capture → annotate → OCR → record → video edit → pin → share ในตัวเดียว + URL scheme สำหรับคนทำ automation
- **Privacy model เปิดเผยแบบโต้ตอบได้** — ไม่มี telemetry, network allowlist เขียนใน README, OCR default ไม่ออกจากเครื่อง, credentials ใน Keychain — ข้อนี้ผ่านการอ่านจริงไม่ใช่คำโฆษณา
- **Notarized + Hardened Runtime** — เปิดจาก DMG ได้เลยไม่ต้องปลด Gatekeeper
- **Native performance** — menu bar app footprint เบา มี Activity Monitor ของตัวเองแสดง CPU/RAM ที่มันกิน, fluid ทั้ง Intel และ Apple Silicon
- **Feature ใหม่ต่อเนื่องจริง** — v2.0.0 ใหญ่ระดับ redesign, beta channel ไหลเรื่อย ๆ, momentum 9 เดือนไม่มีวี่แววหยุด
- **Power-user hooks ครบ** — Raycast, global shortcuts ปรับได้ + conflict detection, TOML config, URL scheme

## 07: ข้อเสีย ❌ — ตรง ๆ ไม่อวย

- **ไม่ได้ sandboxed** — ตัวนี้ต้องพูดสองรอบเพราะหลาย directory listing เขียนผิด: มันรันด้วยสิทธิ์ user เต็มรูปแบบ ความปลอดภัยพึ่ง notarization + code เปิด + network allowlist — ถ้า threat model ของคุณต้องการ sandbox เป็นขอบเขตหลัก นี่คือข้อที่ควรพิจารณาก่อนติดตั้ง
- **Project ยังอายุน้อย** — ~9 เดือน vs CleanShot X ~10 ปี — edge cases ยังมี (ล่าสุด beta.3 แก้เรื่อง crop placement ตอน restore หน้าจอ), Liquid Glass ยังติด tag Beta
- **Cloud share ต้อง DIY** — CleanShot จ่ายแล้วได้ cloud 1GB แบบ zero-config; Snapzy ฟรีแต่ต้องมี bucket ตัวเองก่อน (Google Drive ช่วยลดอุปสรรคเรื่องนี้ได้แล้วบางส่วน) — คนที่ไม่อยากแตะ AWS/Cloudflare เลือกใช้ copy/drag แทน share link ได้
- **OCR benchmark บนเว็บ = ของทีมโปรเจกต์เอง** — ตัวเลขสวย (English/Vietnamese 100% character accuracy, ภาษาอื่น 99+%) แต่วัดบน corpus สังเคราะห์ที่ project สร้างเอง — README ยอมรับเองว่า *"Real-world screenshots can score lower, especially with emoji, low-contrast footers, unusual punctuation, gradients, blur, or decorative fonts"* — ใช้เป็นสัญญาณ อย่าใช้เป็นสัญญา
- **macOS only** — ไม่มี Windows/Linux/iOS (CleanShot X ก็ macOS only — ข้อนี้เสมอกัน)
- **UI ไม่มีภาษาไทย** — รองรับ 10 ภาษา แต่ไม่มี TH (มี VI/中文/JA/KO ตั้งแต่รุ่นแรก ๆ) — ใช้ EN ไปก่อน
- **Bus factor ยังสูงกว่า vendor ที่มี team** — repo นำโดย duongductrong คนเดียว (external contributors เริ่มเข้าแล้ว แต่ core decision ยังคนเดียว)
- **OCR custom endpoint ต้องจัดการเอง** — Apple Vision ฟรีบนเครื่อง แต่ถ้าต่อ endpoint ภายนอก คุณดูแล key และความเป็นส่วนตัวของภาพที่ส่งออกเอง

## 08: เทียบกับคู่แข่ง

| | Snapzy | CleanShot X | macOS builtin | ตัวฟรีอื่น (Shottr ฯลฯ) |
|---|---|---|---|---|
| ราคา (ณ 12 ต.ค. 2026) | ฟรี (OSS) | Basic $35 one-time + renewal $19/yr (optional) / Pro $10/mo | ฟรี | ฟรี |
| Scrolling capture | ✅ | ✅ | ❌ | ⚠️ ไม่ครบทุกตัว |
| OCR | ✅ (Vision on-device + custom) | ✅ | ⚠️ (Live Text) | ❌/⚠️ |
| Video + GIF editor | ✅ (Follow Mouse + camera overlay) | ✅ | ⚠️ (QuickTime) | ❌ ส่วนใหญ่ |
| Auto-redaction | ✅ | ✅ | ❌ | ⚠️ |
| Cloud share | BYO S3/R2/GDrive | ✅ 1GB (Basic) / ไม่จำกัด (Pro) | ❌ | ❌ |
| Automation | ✅ URL scheme + Raycast | ⚠️ จำกัดกว่า | ❌ | ⚠️ |
| Maturity | ~9 เดือน | ~10 ปี | 15+ ปี | หลากหลาย |
| Source | เปิด (BSD-3) | ปิด | ปิด | ผสม |

**Bottom line จากตาราง:** ตัวเลือกเปลี่ยนจาก "จ่ายหรือไม่จ่าย" เป็นเรื่องของ **cloud + maturity**: ถ้าต้องการ share link zero-config + polish 10 ปี = CleanShot X ยังคุ้มกับ $35; ถ้าต้องการ feature set เกือบเท่ากัน + ควบคุมข้อมูลเอง + ฟรี + เปิด code = Snapzy ชนะในราคาที่ไม่มีใครลดต่ำกว่านี้ได้

## 09: เหมาะกับใคร (แยกตามระดับ)

**มือใหม่ / อยากลอง** — `brew install --cask snapzy` → อนุญาต Screen Recording ครั้งแรก (มี onboarding นำทีละ step) → ตั้ง shortcut โหมด `Application Capture` (`A`) ไว้จับหน้าต่างมีเงา → 15 นาทีแรกพอ ใช้แทน ⌘Shift+4 ไปเลย

**Content creator / dev ที่ทำ docs** — เปิด auto-redaction ไว้ก่อน capture ทุกครั้ง (กัน secret/credential หลุดใน screenshot ที่แชร์ออกไป), ใช้ Capture Markup วาดเลขขั้นตอนบนจอจริง, Subject cutout + mockup background ทำ hero image, OCR เพื่อยก text จาก design ตรง ๆ

**Power user / self-hoster** — ต่อ BYO bucket (R2 free tier 10GB) + auto-expiration 7 วัน + custom domain → share pipeline ไม่ผ่าน vendor ไหน, export TOML config ใส่ dotfiles ตั้งค่า sync ทุกเครื่อง, ผูก `snapzy://` เข้า Raycast/Alfred ให้ capture เป็นส่วนหนึ่งของ automation ใหญ่

**ไม่เหมาะถ้า:** คุณใช้ Windows (ไม่มี version), คุณต้องการ cloud share zero-config จริง ๆ ไม่อยากแตะ storage เองเลย (CleanShot ง่ายกว่าตรงนี้), คุณต้องการ sandbox เป็นเส้นตายด้านความปลอดภัย, หรือคุณต้องการ UI ภาษาไทย (ยังไม่มี)

## 10: สรุปแบบวิศวกรเป็ด

Snapzy คือคำตอบของคำถาม "CleanShot X แต่ $0" — pipeline capture→annotate→OCR→record→share ครบ, native, privacy-first แบบที่ตรวจสอบได้ (offline-first, network allowlist, BYO cloud), open-source BSD-3 — แลกกับ: อายุ 9 เดือน, cloud ต้อง DIY, UI ยังไม่มีไทย, และไม่ได้ sandboxed

บทเรียนจากรอบ rewrite ข้อความนี้: ตัวเลขใน tech post มีอายุ — ราคา CleanShot เลื่อนจาก $29 เป็น $35 + มี subscription tier ในเวลาเดือนกว่า, Snapzy โหวตข้ามจาก v1.31 ไป v2.0.0 แบบ redesign — ตัวฟรีโตเร็วขึ้นกว่าที่ตัวจ่ายเมื่อก่อนเคยเป็น และนั่นทำให้ "รออีกนิดดูก่อน" เป็นกลยุทธ์ที่เป็นไปได้สำหรับคนที่ยังไม่เจ็บปวดกับ pipeline กระจายอยู่แล้ว

มาตรฐานที่แนะนำตอนนี้: **builtin สำหรับจับทีเดียวจบ, Snapzy สำหรับจับแล้วต้อง edit/share, CleanShot X สำหรับคนที่จ่าย $35 แล้วอยากได้ cloud zero-config กับ polish 10 ปี** — feature ที่ลองแล้วลืมไม่ได้คือ auto-redaction + OCR ในตัวเดียวกัน ฟรี

ถ้าคุณใช้ Mac + screenshot เป็น daily tool — ลอง Snapzy ก่อนคิดเงินครับ — มันฟรีจริง, open-source จริง, community ใหญ่พอ (3,300+ stars) และ release notes ที่มี contributor คนอื่นเริ่มเข้ามาคือสัญญาณว่า project นี้ไม่ได้พึ่งคนเดียวอีกต่อไป

#Adduckivity #DuckOS #NeuroDivergent #Snapzy #CleanShotX #macOS #Screenshot #OpenSource #Productivity
