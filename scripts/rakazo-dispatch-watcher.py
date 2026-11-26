#!/usr/bin/env python3
"""Rakazo dispatch watcher — อ่านคำขอ dispatch จาก Chief (ไฟล์ใน shared/dispatch-requests)
แล้ว dispatch ตรงให้บอทปลายทางผ่าน DB (ช่องทางที่พิสูจน์แล้ว) — ทดแทน message chain ที่ flaky
House pattern: ไฟล์คือคิว, ประมวลผลแล้วย้ายเข้า processed/, พังย้ายเข้า failed/ + log
"""
import subprocess, json, uuid, datetime, sys, re

CONTAINER = "rakazo-bot-team-e139f7aba02dcd875b4ea3ebce1beb7e"
SPC = "47b98329ab2ebec3a6bb65c2ca2e240a"
UID = "Y4aTxhNrF9OTEEwLDx9zqqQ0yNYK1wKp"
REQ_DIR = "/home/rakazo/shared/dispatch-requests"
LOG = "/home/lifetofree/rakazo-inbox/alerts/dispatch-queue.log"

def log(msg):
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    line = f"[{stamp}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass

def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)

def psql(sql):
    r = subprocess.run(["docker","exec","rakazo-postgres-1","psql","-U","rakazo","-d","rakazo","-t","-A","-c",sql],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[:200])
    return r.stdout.strip()

def list_files():
    r = sh(f"docker exec {CONTAINER} sh -c 'ls -1 {REQ_DIR}/*.md 2>/dev/null || true'")
    return [x for x in r.stdout.strip().splitlines() if x.strip()]

def read_file(path):
    r = sh(f"docker exec {CONTAINER} cat '{path}'")
    return r.stdout

def move(path, sub):
    sh(f"docker exec {CONTAINER} sh -c 'mkdir -p {REQ_DIR}/{sub} && mv \"{path}\" {REQ_DIR}/{sub}/'")

def parse(txt):
    to_m = re.search(r'^to:\s*(.+)$', txt, re.M)
    task_m = re.search(r'^task:\s*(.+)$', txt, re.M | re.S)
    if not to_m or not task_m:
        return None
    to = to_m.group(1).strip()
    task = task_m.group(1).strip()
    if not to or not task:
        return None
    return {"to": to, "task": task}

RULES = ("\n\n[กฎบ้าน: คำว่า คุณ ผม ฉัน คับ เพราะ = 0 · ห้าม em dash · ประโยคสั้นหนึ่งข้อเท็จจริง · "
         "ห้าม dispatch บอทอื่น ห้ามแตะฐานอื่น · เสร็จรายงานสั้นๆ ในแชทตัวเอง]")

def dispatch(to_name, task, src):
    bot_id = psql(f"SELECT id FROM bots WHERE name='{to_name.replace(chr(39),'')}' AND \"archivedAt\" IS NULL LIMIT 1")
    if not bot_id:
        return False, f"ไม่พบบอทชื่อ '{to_name}'"
    now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S")
    rid = "cmxrt" + uuid.uuid4().hex[:20]
    prompt = (task + RULES).replace("'", "''")
    nm = f"[HQ dispatch] จาก Chief: {task[:40]}".replace("'", "''")
    psql(f"""INSERT INTO routines (id, "spaceId", "botId", "userId", name, prompt, timezone, active, notify, "nextRunAt", crons, "createdAt", "updatedAt")
    VALUES ('{rid}', '{SPC}', '{bot_id}', '{UID}', '{nm}', '{prompt}', 'UTC', true, true, '{now}'::timestamp, '{{"@once"}}', '{now}', '{now}')""")
    log(f"DISPATCH ✓ {to_name} (routine {rid}) จากไฟล์ {src}")
    return True, rid

def main():
    files = list_files()
    if not files:
        return
    log(f"พบคำขอ dispatch {len(files)} ไฟล์")
    for f in files:
        try:
            txt = read_file(f)
            req = parse(txt)
            if not req:
                move(f, "failed")
                log(f"FAILED (format ไม่ครบ to:/task:): {f}")
                continue
            ok, info = dispatch(req["to"], req["task"], f.split("/")[-1])
            if ok:
                move(f, "processed")
            else:
                move(f, "failed")
                log(f"FAILED ({info}): {f}")
        except Exception as e:
            log(f"ERROR {f}: {str(e)[:150]}")

if __name__ == "__main__":
    main()
