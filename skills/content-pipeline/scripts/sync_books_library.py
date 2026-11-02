#!/usr/bin/env python3
"""Sync Notion "Books Library" DB -> research/books/catalog.md (single generated file).

DB: 2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0 (title/author/status/energy/tags)
Catalog is GROUPED, not 1-folder-per-book: 253 queued rows would be graph noise.
Per-book folders (books/<slug>/book.md + quotes.md + notes.md) are created BY HAND
only when a book graduates to active reading / quote extraction (rule: evidence first).

Merge-safe: catalog.md carries a content hash; identical run = no rewrite.

Usage: python3 skills/content-pipeline/scripts/sync_books_library.py
"""
import hashlib
import json
import os
import re
import urllib.request

DB_ID = "2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0"
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
OUT = os.path.join(REPO, "research", "books", "catalog.md")
ENV = os.path.join(os.path.expanduser("~"), ".hermes", ".env")


def token():
    for line in open(ENV):
        if line.startswith("NOTION_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("NOTION_API_KEY not found")


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request("https://api.notion.com/v1" + path, data=data, method=method,
        headers={"Authorization": f"Bearer {token()}", "Notion-Version": "2022-06-28",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode() or "{}")


def prop(p):
    t = p["type"]
    if t == "title":
        return "".join(x["plain_text"] for x in p["title"]).strip()
    if t == "rich_text":
        return "".join(x["plain_text"] for x in p["rich_text"]).strip()
    if t == "select":
        return p["select"]["name"] if p["select"] else ""
    return ""


CH_CACHE = os.path.join(os.path.dirname(OUT), ".chapters-cache.json")


def clean_chapter(t):
    t = re.sub(r"^[^\w(\[\"']+", "", t).strip()
    t = re.split(r"\*{2,}", t)[0].strip()
    return t.strip(" -\u2013\u2014:.")


def fetch_chapters(api, page_id, edited):
    """Chapters จาก child_database ชื่อ *chapter* (row titles) หรือ heading_3 'Chapter #N' — cache ด้วย last_edited_time; ไม่มี = [] (ปล่อยว่าง)"""
    cache = {}
    if os.path.exists(CH_CACHE):
        try:
            cache = json.load(open(CH_CACHE))
        except Exception:
            cache = {}
    hit = cache.get(page_id)
    if hit and hit.get("edited") == edited:
        return hit["chapters"]

    blocks, cursor = [], None
    while True:
        d = api("GET", f"/blocks/{page_id}/children?page_size=100" + (f"&start_cursor={cursor}" if cursor else ""))
        blocks += d.get("results", [])
        if not d.get("has_more"):
            break
        cursor = d.get("next_cursor")

    chapters = []
    db_ids = []
    for b in blocks:
        if b["type"] == "child_database" and "chapter" in b["child_database"].get("title", "").lower():
            db_ids.append(b["id"])
        if b["type"] == "heading_3":
            txt = "".join(x["plain_text"] for x in b["heading_3"]["rich_text"]).strip()
            if re.search(r"chapter\s*#?\s*\d+", txt, re.I):
                chapters.append(clean_chapter(txt))

    if db_ids:
        db_chapters = []
        for db_id in db_ids:
            cur = None
            while True:
                try:
                    q = api("POST", f"/databases/{db_id}/query", {"page_size": 100, **({"start_cursor": cur} if cur else {})})
                except Exception:
                    break
                for r in q.get("results", []):
                    for pv in r["properties"].values():
                        if pv["type"] == "title":
                            t = "".join(x["plain_text"] for x in pv["title"]).strip()
                            if t and "template" not in t.lower():
                                db_chapters.append(clean_chapter(t))
                            break
                if not q.get("has_more"):
                    break
                cur = q.get("next_cursor")
        if db_chapters:
            chapters = db_chapters

    chapters = [c for c in chapters if c and "template" not in c.lower()]
    cache[page_id] = {"edited": edited, "chapters": chapters}
    json.dump(cache, open(CH_CACHE, "w"), ensure_ascii=False)
    return chapters


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower()).strip()
    return re.sub(r"[\s_]+", "-", s)[:48]


def main():
    rows, cursor = [], None
    while True:
        q = api("POST", f"/databases/{DB_ID}/query", {"page_size": 100, **({"start_cursor": cursor} if cursor else {})})
        rows += q["results"]
        if not q.get("has_more"):
            break
        cursor = q.get("next_cursor")

    books = []
    for r in rows:
        P = r["properties"]
        books.append({
            "title": prop(P["Title"]) or "(untitled)",
            "author": prop(P["Author"]),
            "status": prop(P["Status"]) or "—",
            "energy": prop(P["Energy Group"]) or "—",
            "tags": prop(P["Tags"]),
            "id": r["id"],
            "edited": r.get("last_edited_time", ""),
        })

    import time
    n_cached = 0
    for i, b in enumerate(books):
        try:
            b["chapters"] = fetch_chapters(api, b["id"], b["edited"])
        except Exception as e:
            b["chapters"] = []
            print(f"  chapters fail: {b['title'][:30]} ({e})")
        if i % 25 == 0:
            print(f"  chapters {i}/{len(books)}...")
        time.sleep(0.2)
    n_with = sum(1 for b in books if b.get("chapters"))
    print(f"chapters present: {n_with}/{len(books)} (ที่เหลือ = ปล่อยว่าง)")

    body = ["---"]
    blob = json.dumps(books, ensure_ascii=False, default=str)
    body.append("hash: " + hashlib.sha1(blob.encode()).hexdigest()[:10])
    body.append(f"count: {len(books)}")
    body.append("source: Notion Books Library " + DB_ID)
    body.append("synced: see git log")
    body.append("---")
    body.append("")
    body.append("# Books Library — catalog (synced จาก Notion)")
    body.append("")
    body.append(f"รวม **{len(books)} เล่ม** — ต้นทาง: [Notion Books Library]"
                f"(https://www.notion.so/{DB_ID.replace('-', '')}) — แก้ข้อมูลที่ Notion แล้วรัน sync อีกครั้ง")
    body.append("")
    body.append("> กติกา: ไฟล์นี้ = แคตตาล็อกเท่านั้น (generated — ห้ามแก้มือ)")
    body.append("> เล่มที่เริ่มอ่านจริง/สกัด quote → เปิดโฟลเดอร์รายเล่ม `books/<slug>/` "
                "(book.md + quotes.md + notes.md) ตาม README — quote ที่โพสต์อ้างได้ต้องอยู่ใน quotes.md ก่อนเสมอ")
    body.append("")

    order = ["⏳ LOADING...", "⬜ QUEUED", "✅ INSTALLED"]
    for status in order:
        group = [b for b in books if b["status"] == status]
        if not group:
            continue
        body.append(f"## {status} ({len(group)})")
        body.append("")
        for energy in ["🟢 G.1", "🟡 G.2", "🟠 G.3", "🔴 Boss", "—"]:
            sub = [b for b in group if b["energy"] == energy]
            if not sub:
                continue
            body.append(f"### {energy} ({len(sub)})")
            body.append("")
            for b in sorted(sub, key=lambda x: x["title"].lower()):
                line = f"- **{b['title']}**"
                if b["author"]:
                    line += f" — {b['author']}"
                if b["tags"]:
                    line += f" · {b['tags']}"
                line += f" · [Notion](https://www.notion.so/{b['id'].replace('-', '')})"
                body.append(line)
                for ch in b.get("chapters", []):
                    body.append(f"  - {ch}")
            body.append("")

    text = "\n".join(body) + "\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if os.path.exists(OUT):
        mm = re.search(r"^hash: (\S+)$", open(OUT).read(), re.M)
        if mm and mm.group(1) == hashlib.sha1(blob.encode()).hexdigest()[:10]:
            print("catalog unchanged — no rewrite")
            return
    open(OUT, "w").write(text)
    print(f"catalog.md written: {len(books)} books")


if __name__ == "__main__":
    main()
