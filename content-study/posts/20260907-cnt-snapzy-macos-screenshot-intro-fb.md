# Snapzy FB — social line-break variant (ของ long form 2026-10-12)

<!--
ContentID: 20260907-CNT-SNAPZY-FB
Type: FB re-flow (skill form b) ของ posts/20260907-cnt-snapzy-macos-screenshot-intro.md
Status: Draft — รอ review
Format: plain text ล้วน (FB ไม่ render markdown), 1 line = 1 thought, "." = beat break,
  title แยก 2 ย่อหน้า (< 80 chars ต่อบรรทัด), open loop หัว+ท้าย, ตารางยุบเป็น — bullets,
  ตัวเลขใหญ่ปัดตามกฎ FB (3,334 → 3,300+), ราคาเป๊ะ ($35 / $10 / $19), CTA ตอบคำเดียว
Sources: เดียวกับ long form (re-verified 2026-10-12) — quotes/caveat คง verbatim
-->

Snapzy — สกรีนช็อต Mac ตัวฟรี open-source

กับคำถามที่คนใช้ Mac ถามกันมา 10 ปี: ต้องจ่าย $35 ให้ CleanShot X จริงไหม

ราคาวันนี้ (12 ต.ค. 2026):

CleanShot Basic $35 one-time — รวมอัปเดต 1 ปี ต่ออายุ optional $19 ต่อปี

หรือ Pro subscription $10 ต่อเดือน

แต่ก่อนเปิดกระเป๋า — มีตัวฟรี 100% open-source ที่ฟีเจอร์ไล่เลี่ยกัน

ชื่อ Snapzy — อายุ 9 เดือน กับ 3,300+ stars

คำตอบอยู่ท้ายโพสต์

.

ปัญหาจริงไม่ใช่ screenshot

ปัญหาคือ pipeline กระจาย

กด ⌘Shift+4 → เปิด Preview → ดึงลูกศร วาดวงกลม → export → หาทางส่ง

ทุกครั้งที่อยากส่งหน้าจอให้คนอื่นเห็น ต้องสลับ app 2-3 รอบ

.

คำถามที่แท้จริงของโพสต์นี้:

"ตัวฟรีตัวนึง ปิดช่องว่างกับของ $35 ได้จริงไหม — และแลกด้วยอะไร"

ถ้าของที่ใช้อยู่โอเคอยู่แล้ว ใช้ต่อไป

โพสต์นี้ไม่ได้มาให้ใครเลิกใช้อะไร

มาให้คนที่ยังไม่จ่าย เห็นทางเลือกที่สองก่อนกดซื้อ

.

Snapzy คือ native macOS app ตัวเดียวใน menu bar

Screenshot, record, annotation, OCR, share — ครบในตัวเดียว

สร้างด้วย SwiftUI + AppKit + ScreenCaptureKit + Vision — ไม่ใช่ Electron

ฟรี — open-source สัญญาอนุญาต BSD-3-Clause

ไล่เทียบ pipeline 4 ขั้นกับของเดิม:

— Capture: builtin ก็จับได้ แต่จับแล้วต่ออะไรไม่ได้
— Annotate: builtin ต้องเปิด Preview / CleanShot กับ Snapzy ทำในที่เดียวจบ
— Record/GIF: builtin มีแต่ QuickTime เปล่า ๆ / อีกสองตัวมี editor ครบ
— Share: CleanShot ให้ cloud ของเขา / Snapzy ให้ cloud ของคุณเอง

.

ข้อที่หลายรีวิวเขียนผิด — ต้องพูดให้ชัดก่อน

Snapzy ไม่ได้ทำงานใน macOS App Sandbox

มันรันด้วยสิทธิ์ของ user คุณเต็ม ๆ

สิ่งที่มีแทนคือ: Hardened Runtime + Developer ID signed + notarized โดย Apple

network มี allowlist เขียนไว้ใน README ชัด ๆ ว่ามีแค่ 4 อย่าง

เช็คอัปเดต / OAuth callback บน loopback
upload ที่คุณกดเอง / โหลด OCR model ที่คุณระบุ

ไม่มี telemetry

OCR default รันบนเครื่องด้วย Apple Vision — ภาพไม่ออกจากเครื่อง

credentials ทั้งหมดอยู่ใน Keychain

ขอบเขตความปลอดภัยของตัวนี้คือ
code เปิดตรวจได้ + Apple notarize + network allowlist

ไม่ใช่ sandbox — ใครต้องการ sandbox guarantee ต้องรู้ก่อนติดตั้ง

.

ใช้จริงเป็น 4 workflow

1. Quick capture — กด shortcut → ลากเลือก → Quick Access panel ลอยขึ้นมา

copy / edit / drag ใส่ app / pin / upload — จบในไม่กี่วินาที

โหมด Application Capture จับ popover ของ menu bar app อื่นได้ด้วย

popover ปกติหายทันทีที่เริ่ม capture — Snapzy restore กลับมาให้เลือก

save ออกมาเป็นมุมโค้งโปร่ง — killer feature สำหรับคนทำ blog/docs

2. Annotate + OCR — ลูกศร shape blur counter highlighter ครบ

automatic redaction ตรวจจับข้อมูล sensitive ในภาพแล้ว blur เอง

OCR ดึงข้อความจากรูปหรือ frame วิดีโอลง clipboard ตรง ๆ

3. Record — วิดีโอหรือ GIF, system audio + mic

camera overlay รองรับ iPhone Continuity Camera

live annotation — วาดบนจอระหว่าง record ได้

Video Editor: trim บน timeline, Follow Mouse zoom สำหรับ tutorial, export GIF

4. เก็บและหาคืน — Pin to Screen ตรึงรูปลอยไว้เทียบงาน

Capture History ค้นหา กรอง เปิดแก้ซ้ำ — ตั้ง retention policy ลบของเก่าเอง

.

มี workflow ที่ 5 แบบไม่ต้องแตะ: Delayed Capture

ตั้ง countdown → ไปเปิด dropdown หรือ tooltip ที่จับยาก → มันจับเองตอนพร้อม

shortcut เดินตาม macOS builtin ทั้งชุด: ⇧⌘3 ⇧⌘4 ⇧⌘5

แล้วเพิ่มชั้นใหม่: ⇧⌘6 scrolling / ⇧⌘7 annotate / ⇧⌘2 OCR / ⇧⌘1 cutout

มือจำเดิมย้ายมา ไม่ต้องเรียน shortcut ใหม่เลย

.

features เด่นที่ใช้ได้จริง ไม่ใช่ checklist สวย

— Scrolling capture: จับหน้าเว็บยาวเป็นภาพเดียว
— Smart Capture: ชี้เอาเฉพาะ element — ปุ่ม การ์ด เมนู
— Capture Markup: วาดลูกศร เลขขั้นตอน บนจอจริงก่อนกดจับ
— Subject cutout + mockup background 3D — ทำ hero image ในตัว
— OCR 10 ภาษา หรือต่อ custom endpoint เองได้
— BYO cloud: S3, Cloudflare R2, Google Drive — ลิงก์ share + ตั้งหมดอายุเอง
— snapzy:// URL scheme — เรียกทุก action จาก Raycast/Alfred/script
— TOML config export/import — ใส่ dotfiles ตั้งค่า sync ทุกเครื่อง
— 10 ภาษา สลับได้ไม่ต้อง restart

.

เดือน ก.ย. ที่ผ่านมา มันขึ้น v2.0.0

ย้าย UI ทั้งตัวไป Liquid Glass — design language ใหม่ของ Apple

breaking change ตัวแรกของ repo

พร้อม Delayed Capture + record ทั้งจอแบบคลิกเดียว + crop ลากวาดใหม่

project อายุ 9 เดือน — release cycle เกือบรายสัปดาห์

และจุดที่สำคัญกว่า feature: release notes เริ่มมี contributor คนอื่นเข้ามาแล้ว

ไม่ใช่งานคนเดียวอีกต่อไป

.

เรื่องราคา — ฟรี 100%

ไม่มี subscription ไม่มี ads ไม่มี license key ไม่ต้อง login

ตอนเปิดตัว maintainer ขาดเงินค่า Apple Developer Program $99

community ช่วยกัน crowdfund จนครบ goal

เลยได้ app ที่ notarized โดย Apple และเปิด code ตรวจได้ทั้งหมด

วันนี้ติดตั้ง: brew install --cask snapzy — หรือโหลด DMG จาก GitHub

.

ข้อเสีย — ตรง ๆ ไม่อวย

— ไม่ได้ sandboxed — ข้อที่หลายรีวิวเขียนผิดไปเอง
— Project อายุ 9 เดือน เทียบกับ CleanShot ที่ polish มา 10 ปี — edge cases ยังมี
— Cloud ต้อง DIY — อยากได้ share link zero-config ต้องมี bucket เองก่อน
— OCR benchmark บนเว็บคือทีมโปรเจกต์วัดเอง บน corpus สังเคราะห์
— README เขียนเองว่างานจริงได้คะแนนต่ำกว่า
— macOS only — ไม่มี Windows/Linux (CleanShot ก็ macOS only — เสมอกัน)
— UI ไม่มีภาษาไทย — รองรับ 10 ภาษา ไม่มี TH
— core decision ยังเป็น maintainer คนเดียว — contributor เพิ่งเริ่มเข้า

.

สรุปแบบเลือกง่าย ๆ

ตัวเลือกวันนี้ไม่ได้อยู่ที่ "จ่ายหรือฟรี" แล้ว

มันอยู่ที่ cloud กับความอายุของโปรเจกต์

อยากได้ share link zero-config + polish 10 ปี → CleanShot X $35 ยังคุ้ม

อยากได้ feature set เกือบเท่ากัน + ข้อมูลอยู่กับคุณ + ฟรี + code เปิด → Snapzy

.

ถ้าจะลอง

มือใหม่: brew install --cask snapzy → อนุญาต Screen Recording → 15 นาทีพอ

คนทำ content/docs: เปิด auto-redaction ก่อน capture ทุกครั้ง
กัน secret หลุดใน screenshot ที่แชร์ออกไป

สาย self-host: ต่อ bucket + custom domain + TOML ใส่ dotfiles
share pipeline ไม่ผ่าน vendor ไหน

ไม่เหมาะถ้า: ใช้ Windows / ต้องการ cloud zero-config จริง ๆ / ต้องการ UI ภาษาไทย

.

คำตอบของโพสต์นี้ — ตามที่บอกตอนต้น

มาตรฐานที่แนะนำตอนนี้:

จับทีเดียวจบ → builtin

จับแล้วต้อง edit หรือ share → Snapzy

จ่าย $35 เองแล้วอยากได้ cloud zero-config กับ polish 10 ปี → CleanShot X

feature ที่ลองแล้วลืมไม่ได้คือ auto-redaction + OCR — ในตัวเดียวกัน ฟรี

ถ้าใช้ Mac + screenshot เป็น daily tool — ลอง Snapzy ก่อนคิดเงินคับ

มันฟรีจริง open-source จริง และ community ใหญ่พอที่จะอยู่ต่อ

.

ใช้ตัวไหนอยู่ — คอมเมนต์ตอบชื่อเดียว: CleanShot หรือ Snapzy

#Adduckivity #Snapzy #CleanShotX #macOS #Screenshot #OpenSource #Productivity
