#!/usr/bin/env python3
"""Notion alerts — กฎ deterministic (ไม่ผ่าน LLM): ตรวจ Job Desk + Content Drafts แล้วส่ง Telegram
กฎ (27 พ.ย. อนุมัติ):
- Job Desk: เตือน (1) เงินค้าง: Payment ≠ ชำระเต็ม (ส่งมอบแล้วก็เตือน) (2) งานค้าง: ยังไม่ส่งมอบ + Due ≤ วันนี้
  ไม่เตือน: ชำระเต็มทุกกรณี / ❌ ยกเลิก / Due อนาคต
- Content Drafts: รายงานเฉพาะ draft ที่แก้ไฟล์ภายใน 28 วันล่าสุด (เก่ากว่านั้นไม่รบกวน) สูงสุด 8 รายการ
"""
import os, json, urllib.request, datetime, subprocess, sys

KEY = os.environ.get("NOTION_API_KEY", "")
TELEGRAM_TARGET = "telegram:8780418515"
JOB_DESK = "425df8d8-8d8c-811f-af55-cb90e2f8c37d"
CONTENT_DRAFTS = "3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520"
TODAY = datetime.date.today()

def api(path, body=None):
    req = urllib.request.Request("https://api.notion.com/v1" + path, method="POST" if body else "GET",
        data=json.dumps(body).encode() if body else None,
        headers={"Authorization": "Bearer " + KEY, "Notion-Version": "2022-06-28", "Content-Type": "application/json"})
    return json.loads(urllib.request.urlopen(req, timeout=50).read())

def query_db(did):
    rows, cursor = [], None
    while True:
        body = {"page_size": 100}
        if cursor: body["start_cursor"] = cursor
        r = api(f"/databases/{did}/query", body)
        rows += r.get("results", [])
        if not r.get("has_more"): break
        cursor = r.get("next_cursor")
    return rows

def prop(row, name):
    p = row.get("properties", {}).get(name, {})
    t = p.get("type")
    if t == "title": return "".join(x.get("plain_text","") for x in p.get("title",[]))
    if t == "rich_text": return "".join(x.get("plain_text","") for x in p.get("rich_text",[]))
    if t == "select": return (p.get("select") or {}).get("name","")
    if t == "date": return (p.get("date") or {}).get("start","")
    if t == "number": return p.get("number")
    if t == "url": return p.get("url") or ""
    return ""

def jobdesk_alerts():
    out = []
    today_s = TODAY.isoformat()
    for row in query_db(JOB_DESK):
        name = prop(row, "Name")
        status = prop(row, "Status")
        pay = prop(row, "Payment")
        due = prop(row, "Due")
        if status == "❌ ยกเลิก": continue
        closed = (status == "✅ ส่งมอบแล้ว" and pay == "ชำระเต็ม")
        if closed: continue
        overdue_days = None
        if due:
            try:
                d = datetime.date.fromisoformat(due[:10])
                overdue_days = (TODAY - d).days
            except Exception: pass
        money_pending = pay != "ชำระเต็ม"
        work_pending = (status != "✅ ส่งมอบแล้ว") and (overdue_days is None or overdue_days >= 0)
        if money_pending:
            label = "💰 เงินค้าง" + (f" (Due เกิน {overdue_days} วัน)" if overdue_days and overdue_days > 0 else "")
            out.append(f"• {name} — {status} — {pay} — {label}")
        elif work_pending and overdue_days is not None and overdue_days >= 0:
            out.append(f"• {name} — {status} — {pay} — ⏰ Due วันนี้/เกิน {overdue_days} วัน")
    return out

def drafts_alerts():
    out = []
    cutoff = TODAY - datetime.timedelta(days=28)
    for row in query_db(CONTENT_DRAFTS):
        title = prop(row, "Name")
        if not title: continue
        st = prop(row, "Status")
        if "published" in st.lower(): continue
        edited = row.get("last_edited_time","")[:10]
        try: ed = datetime.date.fromisoformat(edited)
        except Exception: continue
        if ed >= cutoff:
            out.append(f"• {title[:60]} — {st or '(ไม่มีสถานะ)'} — แก้ล่าสุด {edited}")
    return out[:8]

def main():
    if not KEY:
        print("no NOTION_API_KEY"); sys.exit(1)
    jd = jobdesk_alerts()
    cd = drafts_alerts()
    if not jd and not cd:
        print("วันนี้ไม่มี alert (งาน Job Desk ปิดหมด + draft เงียบ) — ไม่ส่งข้อความ")
        return
    msg = "🔔 สรุปงานค้าง (ระบบตรวจอัตโนมัติ " + TODAY.isoformat() + ")\n"
    if jd:
        msg += "\n💼 Job Desk — งานค้าง " + str(len(jd)) + " งาน:\n" + "\n".join(jd) + "\n"
    if cd:
        msg += "\n📝 Content Drafts — draft ที่ยังไม่เผยแพร่ (แก้ใน 28 วันล่าสุด):\n" + "\n".join(cd)
    print(msg)
    subprocess.run(["/home/lifetofree/.local/bin/hermes", "send", "-t", TELEGRAM_TARGET, msg], capture_output=True, text=True, timeout=60)

if __name__ == "__main__":
    main()
