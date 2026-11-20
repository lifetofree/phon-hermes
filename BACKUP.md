# hermes-home-backup — คู่มือ backup/restore

- ตัวสำรองรายสัปดาห์ (อาทิตย์ 03:00, systemd user timer `backup-hermes-home.timer`)
- สคริปต์: `~/hermes-agent/scripts/backup-hermes-home.sh` · log: `~/.hermes/logs/backup.log`
- ตัวเฝ้า: cron `backup-freshness-check` (จันทร์ 08:00, แจ้ง Telegram เมื่อ stale > 8 วัน)
- secrets (`.env`, `auth.json`): **วางเปล่าใน private repo นี้** (ตัดสินใจ owner 20 พ.ย. — ทาง B)
- `state.db` (296 MB, ประวัติแชต) + rakazo appdata เต็ม (1.3 GB) = **backup แบบ local เท่านั้น** เก็บที่ `~/hermes/backups/` (ไม่ขึ้น GitHub ตามขนาด)

## มีอะไรใน repo นี้

```
hermes/            ~/.hermes ทั้งต้น (config, SOUL, skills/, profiles/ ทั้ง 5 ตัว, cron/jobs,
                   memories, sessions, plugins, secrets .env+auth.json) — ตัด runtime/cache ทิ้ง
rakazo/            rakazo-db-latest.sql.gz (pg_dump) + bot-home-essential-*.tar.gz
                   (credentials + shared/ + work/ ของ bot computer)
home-extras/       ~/duck-os, ~/notes, ~/scripts, ~/rakazo (compose), ~/rakazo-inbox
```

Local-only (ไม่อยู่ใน GitHub): `~/hermes/backups/state-db/` (4 รุ่น), `~/hermes/backups/appdata/` (tar เต็ม 2 รุ่น), `~/hermes/backups/rakazo-db/` (3 รุ่น)

## กู้คืนบนเครื่องใหม่

1. `gh auth login` (lifetofree) → `gh repo clone lifetofree/hermes-home-backup ~/backups/hermes-home`
2. ติดตั้ง Hermes (installer) ครั้งเดียวให้สร้าง `~/.hermes` ว่า ๆ ก่อน แล้ว `systemctl --user stop` gateway (ถ้ารันอยู่)
3. คืน hermes home: `rsync -a ~/backups/hermes-home/hermes/ ~/.hermes/` (ครอบคลุม config/skills/profiles/cron/memories/secrets ทั้งหมด)
4. คืน rakazo DB:
   ```
   docker compose -f ~/rakazo/docker-compose.images.yml up -d rakazo-postgres-1
   gunzip -c ~/backups/hermes-home/rakazo/rakazo-db-latest.sql.gz | docker exec -i rakazo-postgres-1 sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'
   ```
5. คืน bot homes (รันบน volume เดิม): `gunzip -c ~/hermes/backups/appdata/homes-<วันที่>.tar.gz | docker run --rm -i -v rakazo_appdata:/dst alpine sh -c 'cd /dst && tar -xzf -'` (ใช้ local tar — repo ไม่มีไฟล์นี้)
6. คืน home extras: `rsync -a ~/backups/hermes-home/home-extras/duck-os ~/` ฯลฯ
7. อัปเดต nvidia driver/โมเดลตาม skill local-llm-serving → `hermes gateway run` (หรือ systemd unit เดิม) → verify: `curl -s http://127.0.0.1:8080/health`, getMe ผ่าน, `/props` n_ctx = 262144

## ตรวจว่า backup ยังทำงาน

`git -C ~/backups/hermes-home log -1 --format=%ci` — ต้องอายุ ≤ 7 วัน · log รายรัน: `~/.hermes/logs/backup.log` · cron `backup-freshness-check` แจ้งเองถ้าเกิน 8 วัน
