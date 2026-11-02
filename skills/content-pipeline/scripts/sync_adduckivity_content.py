#!/usr/bin/env python3
"""Sync Notion DB "Adduckivity Content" (publish master) -> content-study/vault/notion-content/.

ฝั่ง publish เป็นหลัก (owner): แถว ✅ Published = body เต็มจาก Notion (จะทับไฟล์เก่าทุกรอบ)
แถวอื่น (Idea/Drafting/Ready/ไม่ระบุ) = ไฟล์ index-only สั้น ไม่แตะ body (เจ้าทาง body คือ content-study loop)
Match กลับ content-study loop: ชื่อไฟล์ md ในนี้ = <slug lowercase>; ถ้า match กับไฟล์ใน vault/posts/
จะได้บรรทัด `Paired: [[pair-NNN]]` + backlink ใน pair node ฝั่ง loops/*  (hub: laws/, categories/, tags/)
Merge-safe: เขียนเฉพาะไฟล์ที่ hash เปลี่ยน — ไฟล์ที่ไม่มีใน DB อีก (ลบใน Notion) จะถูกทิ้งไว้ + รายงาน
"""
import hashlib, json, os, re, sys, urllib.request, urllib.error
from datetime import datetime, timezone

REPO = "/home/lifetofree/hermes-agent"
OUT = os.path.join(REPO, "content-study", "vault", "notion-content")
PAIRS_DIR = os.path.join(REPO, "content-study", "vault", "pairs")
STATE = os.path.join(REPO, "content-study", "vault", "notion-content", ".sync-state.json")
STATE_KEY = "adduckivity-content"

def token():
    for line in open(os.path.expanduser("~/.hermes/.env")):
        if line.startswith("NOTION_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("NOTION_API_KEY missing")

def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        "https://api.notion.com/v1" + path, data=data, method=method,
        headers={"Authorization": f"Bearer {token()}", "Notion-Version": "2022-06-28",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        t = r.read().decode()
        return json.loads(t) if t else {}

DB_ID = "303df8d8-8d8c-8013-baa1-c2fd25e7c9a5"

# --- secret redaction: body จาก Notion ห้ามพา token ลง repo (GH push protection เคยจับ Discord/CF token) ---
SECRET_RES = [
    re.compile(r"\b[\w-]{24,}\.[\w-]{6}\.[\w-]{27,}\b"),                     # Discord bot token (ตัวแรก 24-40 ตัว)
    re.compile(r"\bcf[a-z]{0,6}_[A-Za-z0-9_-]{20,}\b"),                      # Cloudflare-style token
    re.compile(r"\b(?:xox[baprs]-|ghp_|gho_|github_pat_|sk-|rk_)[A-Za-z0-9_-]{20,}\b"),  # Slack/GitHub/OpenAI-style
    re.compile(r"\b[a-f0-9]{40}\b"),                                         # 40-hex API token
]
def redact(t):
    for rx in SECRET_RES:
        t = rx.sub("[REDACTED]", t)
    return t

def fetch_rows():
    rows, cur = [], None
    while True:
        d = api("POST", f"/databases/{DB_ID}/query",
                {"page_size": 100, **({"start_cursor": cur} if cur else {})})
        rows += d["results"]
        if not d["has_more"]:
            break
        cur = d["next_cursor"]
    return rows

def prop_sel(p): return p["select"]["name"] if p.get("select") else None
def prop_txt(p): return "".join(x["plain_text"] for x in p.get("rich_text", []))
def prop_ms(p): return [x["name"] for x in p.get("multi_select", [])]
def prop_date(p):
    if not p.get("date"): return None
    s = p["date"]["start"]
    return s[:10] if len(s) >= 10 else s

def fetch_body(page_id):
    parts, cur = [], None
    while True:
        d = api("GET", f"/blocks/{page_id}/children?page_size=100" +
                (f"&start_cursor={cur}" if cur else ""))
        for b in d.get("results", []):
            t = b["type"]
            if t in ("paragraph", "heading_1", "heading_2", "heading_3", "quote"):
                txt = redact("".join(x["plain_text"] for x in b[t]["rich_text"]).strip())
                if not txt:
                    continue
                if t == "heading_1": parts.append("# " + txt)
                elif t == "heading_2": parts.append("## " + txt)
                elif t == "heading_3": parts.append("### " + txt)
                elif t == "quote":
                    bold = any(x.get("annotations", {}).get("bold") for x in b[t]["rich_text"])
                    parts.append(("> **" + txt + "**") if bold else ("> " + txt))
                else:
                    parts.append(txt)
            elif t == "divider":
                parts.append(".")
        if not d.get("has_more"):
            break
        cur = d.get("next_cursor")
    return parts

# ---------- matching ----------
def build_pair_index():
    """slug/core-name -> (pair_node_name, vault_post_filename)"""
    idx = {}
    for fn in os.listdir(PAIRS_DIR):
        if not fn.endswith(".md"): continue
        stem = fn[:-3]
        idx[stem.lower()] = stem
    return idx

VAULT_POSTS = set()
def refresh_vault_posts():
    global VAULT_POSTS
    VAULT_POSTS = {fn[:-3].lower() for fn in os.listdir(os.path.join(REPO, "content-study", "vault", "posts"))
                   if fn.endswith(".md")}

def match_pair(slug, headline):
    """ลองหา pair จาก: (1) vault/posts filename == slug (2) slug core หลังตัดตัวเลขวันที่ (3) headline เป๊ะ"""
    s = slug.lower().strip()
    if s in VAULT_POSTS:
        return s
    core = re.sub(r"^\d{8}-cnt-", "", s)
    if core in VAULT_POSTS:
        return core
    for v in VAULT_POSTS:
        if core and (core in v or v.endswith(core)):
            return v
    for v in VAULT_POSTS:
        if headline and v.endswith(re.sub(r"[^\w\u0E00-\u0E7F]+", "-", headline.lower()).strip("-")):
            return v
    return None

# ---------- render ----------
def fm(row, body_mode):
    L = ["---",
         f'type: notion-content',
         f'dbid: {row["id"]}',
         f'headline: "{row["headline"].replace(chr(34), chr(39))}"',
         f'content_id: "{row["content_id"]}"',
         f'status: "{row["status"] or "UNSPECIFIED"}"',
         f'slug: "{row["slug"]}"',
         f'date: {row["date"] or "null"}',
         f'type_class: "{row["type"] or "-"}"',
         f'engagement: "{row["engagement"] or "-"}"',
         f'site_category: "{row["site_cat"] or "-"}"',
         f'laws: [{", ".join(chr(34)+l+chr(34) for l in row["laws"])}]',
         f'platforms: [{", ".join(row["platforms"])}]',
         f'hashtags: [{", ".join(chr(34)+h+chr(34) for h in row["hashtag"].split() if h.startswith("#"))}]',
         f'notion_url: https://www.notion.so/{row["id"].replace("-", "")}']
    for k, v in (("fb", "fb_url"), ("site", "site_url"), ("short", "short_url")):
        if row.get(k): L.append(f'{v}: {row[k]}')
    if row.get("paired"):
        L.append(f'paired_post: "[[{row["paired"]}]]"')
    if body_mode == "index":
        L.append('body: index-only')
    L.append("---")
    return "\n".join(L)

def render(row, pair_of, hub_tags):
    body_mode = "full" if (row["status"] == "✅ Published") else "index"
    body_blocks = []
    head = [f'# {row["headline"]}']

    if body_mode == "full":
        body_blocks = fetch_body(row["id"])
        if not body_blocks:
            body_mode = "index"           # ไม่มี body ใน Notion → ตกไปเป็น index-only
    meta_lines = []
    if row["excerpt"]:
        meta_lines.append(f'**Excerpt:** {row["excerpt"]}')
    if row["mood"]:
        meta_lines.append(f'**Audience Mood:** {row["mood"]}')
    if row["note"]:
        meta_lines.append(f'**Note:** {row["note"]}')
    if pair_of:
        meta_lines.append(f'**Paired loop draft:** [[{pair_of}]]')
    if row["laws"]:
        meta_lines.append("**Laws:** " + " · ".join("[[" + l + "]]" for l in row["laws"]))
    if row["site_cat"]:
        meta_lines.append("**Site Category:** [[" + row["site_cat"] + "]]")
    tags = [h for h in row["hashtag"].split() if h.startswith("#")]
    if tags:
        meta_lines.append("**Tags:** " + " · ".join(
            ("[[" + t.lstrip("#") + "]]") if t.lstrip("#") in hub_tags else t for t in tags))

    out = head
    if meta_lines:
        out.append("")
        out += meta_lines
    if body_mode == "full":
        out.append("")
        out.append("---")
        out.append("")
        out += body_blocks
    elif body_mode == "index":
        out.append("")
        out.append(f'> สถานะ: **{row["status"] or "ไม่ระบุ"}** — ยังไม่ Published → เก็บเฉพาะ index (body อยู่ฝั่ง content-study loop / จะดึงเมื่อ Published)')
    out.append("")
    out.append(f'*Synced: {datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M %Z")} · '
               f'[Notion]({row["notion_url"]}) · {row["status"] or "UNSPECIFIED"}*')
    return "\n".join(out), body_mode

# ---------- hubs ----------
def render_hubs(rows_with_meta):
    hubs = {}
    def hub_file(name):
        return re.sub(r'[\\/:*?"<>|]+', "-", name).strip() + ".md"
    for r in rows_with_meta:
        for l in r["laws"]:
            hubs.setdefault(("laws", l), []).append(r)
        if r["site_cat"]:
            hubs.setdefault(("categories", r["site_cat"]), []).append(r)
        for h in [x for x in r["hashtag"].split() if x.startswith("#")]:
            hubs.setdefault(("tags", h.lstrip("#")), []).append(r)
    os.makedirs(os.path.join(OUT, "laws"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "categories"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "tags"), exist_ok=True)
    lines_by_file = {}
    for (kind, name), rs in sorted(hubs.items()):
        if kind == "tags" and len(rs) < 3:
            continue  # tag hub เฉพาะ tag ที่ใช้ ≥3 ครั้ง — กันกราฟท่วม
        rel = {"laws": "laws", "categories": "categories", "tags": "tags"}[kind]
        f = os.path.join(OUT, rel, hub_file(name))
        pub = [r for r in rs if r["status"] == "✅ Published"]
        other = [r for r in rs if r["status"] != "✅ Published"]
        L = ["---", f"type: hub", f"hub: {kind}", f'name: "{name}"', "---", "",
             f"# {name}", "",
             f"{len(rs)} content ({len(pub)} published, {len(other)} ยังไม่ published)", ""]
        for label, group in (("✅ Published", pub), ("· ยังไม่ published", other)):
            if group:
                L.append(f"## {label}")
                L.append("")
                for r in sorted(group, key=lambda x: x["date"] or "9999"):
                    star = " 🔥" if r["engagement"] == "🔥 Viral" else ""
                    L.append(f'- [[{r["fname_stem"]}|{r["headline"][:48]}]]{star} — {r["date"] or "no date"}')
                L.append("")
        lines_by_file[f] = L
    return lines_by_file

# ---------- main ----------
def main():
    os.makedirs(OUT, exist_ok=True)
    refresh_vault_posts()
    rows = fetch_rows()
    print(f"rows: {len(rows)}")

    existing = {fn[:-3]: fn for fn in os.listdir(OUT) if fn.endswith(".md")}
    state = {}
    if os.path.exists(STATE):
        state = json.load(open(STATE)).get(STATE_KEY, {})

    written, skipped, errors = 0, 0, 0
    rows_with_meta = []
    for r in rows:
        P = r["properties"]
        row = {
            "id": r["id"],
            "headline": "".join(x["plain_text"] for x in P["Headline"]["title"]).strip(),
            "content_id": prop_txt(P["ContentID"]),
            "status": prop_sel(P["Status"]),
            "slug": prop_txt(P["Slug"]),
            "hashtag": prop_txt(P["Hashtag"]),
            "excerpt": prop_txt(P["Excerpt"]),
            "engagement": prop_sel(P["Engagement"]),
            "date": prop_date(P["Publish Date"]),
            "mood": prop_txt(P["Audience Mood"]),
            "note": prop_txt(P["Note"]),
            "laws": prop_ms(P["Law / Category"]),
            "platforms": prop_ms(P["Platform"]),
            "site_cat": prop_sel(P["Site Category"]),
            "type": prop_sel(P["Type"]),
            "fb": P["Facebook URL"].get("url") if P["Facebook URL"].get("url") else None,
            "site": P["Site URL"].get("url") if P["Site URL"].get("url") else None,
            "short": P["Shorten link"].get("url") if P["Shorten link"].get("url") else None,
            "paired": None,
            "notion_url": f"https://www.notion.so/{r['id'].replace('-', '')}",
            "edited": r.get("last_edited_time", ""),
        }
        base = (row["slug"] or row["headline"] or row["id"]).lower()
        fname = re.sub(r'[\\/:*?"<>|\s]+', "-", base).strip("-")[:80] or row["id"][:8]
        row["fname_stem"] = fname
        # pair match: จาก slug กับ vault/posts
        row["paired"] = match_pair(row["slug"], row["headline"])
        rows_with_meta.append(row)

    from collections import Counter as _C
    _tag_ct = _C(t.lstrip("#") for r in rows_with_meta for t in r["hashtag"].split() if t.startswith("#"))
    HUB_TAGS = {t for t, n in _tag_ct.items() if n >= 3}
    any_changed = False
    for row in rows_with_meta:
        fpath = os.path.join(OUT, row["fname_stem"] + ".md")
        if state.get(row["fname_stem"] + ".edited") == row["edited"] and os.path.exists(fpath):
            skipped += 1
            continue
        any_changed = True
        try:
            md, mode = render(row, row["paired"], HUB_TAGS)
        except Exception as e:
            errors += 1
            print(f"  render fail {row['headline'][:30]}: {e}")
            continue
        h = hashlib.sha256(md.encode()).hexdigest()
        open(fpath, "w").write(md)
        state[row["fname_stem"]] = h
        state[row["fname_stem"] + ".edited"] = row["edited"]
        written += 1

    # hub files (rebuild เฉพาะเมื่อมีแถวเปลี่ยน หรือ hub หาย)
    need_hubs = any_changed or not os.path.isdir(os.path.join(OUT, "laws")) or \
                not os.path.isdir(os.path.join(OUT, "categories")) or \
                not os.path.isdir(os.path.join(OUT, "tags"))
    if need_hubs:
        hub_lines = render_hubs(rows_with_meta)
        for f, L in hub_lines.items():
            h = hashlib.sha256("\n".join(L).encode()).hexdigest()
            key = "hub:" + os.path.relpath(f, OUT)
            if state.get(key) == h:
                skipped += 1
                continue
            open(f, "w").write("\n".join(L))
            state[key] = h
            written += 1
    else:
        hub_lines = {}
        skipped += 1

    # stale cleanup: ไฟล์ใน OUT ที่ไม่มีใน state (จากรอบนี้) และไม่ใช่ไฟล์ระบบ
    live = {row["fname_stem"] + ".md" for row in rows_with_meta}
    live |= {k[4:].split("/")[-1] for k in state if k.startswith("hub:")}
    removed = 0
    for fn in os.listdir(OUT):
        if fn.endswith(".md") and fn not in live and fn not in ("index.md", ".gitignore"):
            os.remove(os.path.join(OUT, fn))
            removed += 1

    json.dump({STATE_KEY: state, "_updated": datetime.now(timezone.utc).isoformat()},
              open(STATE, "w"), ensure_ascii=False)

    # MOC index.md
    pub = [r for r in rows_with_meta if r["status"] == "✅ Published"]
    idx = ["---", "type: moc", "---", "",
           "# Adduckivity Content — Notion publish master (synced)",
           "",
           f"{len(rows_with_meta)} content · {len(pub)} published · synced {datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M')}",
           "",
           "## ตามสถานะ",
           ""]
    from collections import Counter
    for st, n in Counter(r["status"] or "ไม่ระบุ" for r in rows_with_meta).most_common():
        idx.append(f'- {st}: {n}')
    idx += ["", "## Hub", "",
            "- Laws → `laws/` (5 hubs)", "- Categories → `categories/` (8 hubs)", "- Tags → `tags/` (รวม #Adduckivity #DuckOS ฯลฯ)", "",
            "## Published ล่าสุด", ""]
    for r in sorted(pub, key=lambda x: x["date"] or "9999")[:12]:
        idx.append(f'- [[{r["fname_stem"]}|{r["headline"][:56]}]] — {r["date"] or "?"}')
    open(os.path.join(OUT, "index.md"), "w").write("\n".join(idx))

    paired = sum(1 for r in rows_with_meta if r["paired"])
    print(f"written {written} (stale-removed {removed}) | skipped {skipped} | errors {errors}")
    print(f"paired (match กลับ vault/posts): {paired}/{len(rows_with_meta)}")

if __name__ == "__main__":
    main()
