#!/usr/bin/env python3
"""Morning Brief — ปฏิทินวันนี้+พรุ่งนี้ (เวลาไทย) + ส่วน newsletter (รอ App Password)
เส้นทาง: ดึง ICS ลับของ phon@adduckivity.com → กรอง event วันนี้+พรุ่งนี้ (ICT) → รวมรายงาน
"""
import os, urllib.request, datetime, json, sys, subprocess, imaplib, email, re

ENV = os.path.expanduser("~/hermes-agent/secrets/morning-brief.env")
ICT = datetime.timezone(datetime.timedelta(hours=7))

def load_env():
    env = {}
    if os.path.exists(ENV):
        for line in open(ENV):
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                env[k] = v
    return env

def unfold(ics_text):
    lines = []
    for raw in ics_text.splitlines():
        if raw.startswith((" ", "\t")) and lines:
            lines[-1] += raw[1:]
        else:
            lines.append(raw)
    return lines

def parse_events(lines):
    evs, cur = [], None
    in_vevent = in_alarm = False
    for l in lines:
        l = l.strip()
        if l == "BEGIN:VEVENT":
            in_vevent, in_alarm, cur = True, False, {}
        elif l == "BEGIN:VALARM":
            in_alarm = True
        elif l == "END:VALARM":
            in_alarm = False
        elif l == "END:VEVENT":
            if cur: evs.append(cur)
            in_vevent, cur = False, None
        elif in_vevent and not in_alarm:
            if l.startswith("DTSTART"):
                cur["start_raw"] = l.split(":", 1)[-1].strip()
            elif l.startswith("DTEND"):
                cur["end_raw"] = l.split(":", 1)[-1].strip()
            elif l.startswith("SUMMARY"):
                cur["title"] = l.split(":", 1)[-1].strip().replace("\\,", ",").replace("\\;", ";")
            elif l.startswith("LOCATION"):
                cur["loc"] = l.split(":", 1)[-1].strip().replace("\\,", ",")
    return evs

def to_ict(start_raw):
    s = start_raw
    try:
        if s.endswith("Z"):
            dt = datetime.datetime.strptime(s[:15], "%Y%m%dT%H%M%S").replace(tzinfo=datetime.timezone.utc)
            return dt.astimezone(ICT)
        if "VALUE=DATE" in s or len(s) == 8:
            d = datetime.datetime.strptime(s[:8], "%Y%m%d")
            return d.replace(tzinfo=ICT, hour=0, minute=0)
        dt = datetime.datetime.strptime(s[:15], "%Y%m%dT%H%M%S").replace(tzinfo=ICT)
        return dt
    except Exception:
        return None

def calendar_today_tomorrow(urls):
    now = datetime.datetime.now(ICT)
    window = {now.date(), (now + datetime.timedelta(days=1)).date()}
    out = []
    for ics_url in urls:
        try:
            req = urllib.request.Request(ics_url, headers={"User-Agent": "morning-brief/1.0"})
            ics = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "ignore")
        except Exception as e:
            out.append({"when": "error", "title": f"(ดึงปฏิทินล้มเหลว: {str(e)[:40]})", "loc": ""})
            continue
        for e in parse_events(unfold(ics)):
            dt = to_ict(e.get("start_raw", ""))
            if dt and dt.date() in window:
                when = dt.strftime("%d/%m %H:%M") if dt.hour or dt.minute else dt.strftime("%d/%m (เต็มวัน)")
                out.append({"when": when, "title": e.get("title", "(ไม่มีหัวข้อ)"), "loc": e.get("loc", "")})
    out.sort(key=lambda x: x["when"])
    return out

def newsletter_items():
    """จดหมาย 24 ชม.ล่าสุดจาก newsletter (มี List-Unsubscribe) — คืน [(sender, subject)]"""
    try:
        env = load_env()
        M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        M.login(env["GMAIL_USER"], env["GMAIL_APP_PASSWORD"])
        M.select("INBOX", readonly=True)
        since = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%b-%Y")
        typ, data = M.search(None, f"(SINCE {since})")
        out = []
        for i in data[0].split():
            typ, md = M.fetch(i, "(BODY.PEEK[HEADER])")
            msg = email.message_from_bytes(md[0][1])
            if not msg.get("List-Unsubscribe"):
                continue
            frm = msg.get("From", "")
            m = re.search(r"<(.+?)>", frm) or re.search(r"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+)", frm)
            sender = m.group(1) if m else frm[:30]
            out.append((sender, (msg.get("Subject", "(ไม่มีหัวข้อ)"))[:70]))
        M.logout()
        return out
    except Exception as e:
        return [("error", str(e)[:60])]

def main():
    env = load_env()
    urls = [v for k, v in sorted(env.items()) if k.startswith("ICAL_URL") and v]
    if not urls:
        print("ไม่มี ICAL_URL ใน env"); sys.exit(1)
    evs = calendar_today_tomorrow(urls)
    lines = ["📅 ปฏิทินวันนี้-พรุ่งนี้ (" + datetime.datetime.now(ICT).strftime("%d/%m") + ")"]
    if evs:
        for e in evs:
            lines.append("• [" + e["when"] + "] " + e["title"] + ((" — " + e["loc"]) if e["loc"] else ""))
    else:
        lines.append("• ไม่มีนัดหมายในช่วงนี้")
    # Tasks (ไฟล์จากทีมบอท — routine 07:40 ไทย)
    tasks_path = "/home/lifetofree/rakazo-inbox/morning-brief/tasks.json"
    try:
        tasks = json.load(open(tasks_path, encoding="utf-8"))
        lines.append("")
        lines.append("✅ Tasks (ค้าง + วันนี้-พรุ่งนี้)")
        today_s = datetime.datetime.now(ICT).date().isoformat()
        tom_s = (datetime.datetime.now(ICT).date() + datetime.timedelta(days=1)).isoformat()
        shown = 0
        for tk in tasks if isinstance(tasks, list) else []:
            due = tk.get("due", ""); od = tk.get("overdue")
            if not od and due not in (today_s, tom_s):
                continue
            mark = "⚠️ ค้าง! " if od else ""
            lines.append("• " + mark + tk.get("title", "?") + ((" — กำหนด " + due) if due and not od else ""))
            shown += 1
        if shown == 0:
            lines.append("• ไม่มี task ค้าง/ใกล้ครบ")
    except FileNotFoundError:
        pass
    except Exception as e:
        lines.append("")
        lines.append("✅ Tasks: (อ่านไฟล์ล้มเหลว " + str(e)[:40] + ")")
    if env.get("NEWSLETTER_ENABLED", "0") == "1":
        nl = newsletter_items()
        lines.append("")
        lines.append("📰 Newsletter (24 ชม.ล่าสุด)")
        if nl:
            for sender, subj in nl:
                lines.append("• " + subj + "  — " + sender)
        else:
            lines.append("• ไม่มี")
    report = "\n".join(lines)
    import re as _re
    report = _re.sub(r"(https?://[^\s<]+)", r"<\1>", report)  # กัน Discord unfurl รูป/พรีวิว
    print(report)
    json.dump({"calendar": evs, "report": report}, open("/tmp/morning-brief-preview.json", "w"), ensure_ascii=False)
    if "--send" in sys.argv:
        subprocess.run(["/home/lifetofree/.local/bin/hermes", "send", "-t", "discord:#morning-brief", report],
                       capture_output=True, text=True, timeout=60)
        print("(ส่ง #morning-brief ✓)")

if __name__ == "__main__":
    main()
