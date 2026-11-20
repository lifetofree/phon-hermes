# git push fix — youtube-sync (20 พ.ย. 2026 โดย Hermes, ตามคำสั่งพร)

1. commit 3081967 ของบอท (catalog.md 251 books + sync script fix) **ขึ้น branch แล้ว** เป็น commit ใหม่ **20557d6** บน origin/rakazo/youtube-library (landing ผ่าน GitHub API เพราะ container DNS พัง ห้าม git push จนกว่าจะแก้)
2. **บอทต้อง reset ก่อน sync รอบหน้า** (local 3081967 ไม่ตรงกับ origin 20557d6 แล้ว):
   git fetch origin && git checkout rakazo/youtube-library && git reset --hard origin/rakazo/youtube-library
3. container ของบอทมีปัญหา DNS (resolv.conf ไม่มี nameserver → resolve github.com ไม่ได้) — ถ้า git push ฟ้อง "Could not resolve host" ให้หยุด รายงาน Phon ผ่าน Chief แล้วให้ Hermes จัดการ landing ผ่าน API แทน (ห้าม retry รัว)
