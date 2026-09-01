#!/usr/bin/env python3
"""Fetch page 26 (last 4 posts) from wp.adduckivity.com."""
import json, re, html, time, urllib.request, pathlib

API = "https://wp.adduckivity.com/wp-json/wp/v2/posts"
OUT = pathlib.Path.home() / "hermes-agent" / "content-study" / "posts"
IDXP = OUT.parent / "index.json"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)

def clean(t):
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"</p>", "\n\n", t)
    t = re.sub(r"<br\s*/?>", "\n", t)
    t = re.sub(r"<h([2-4])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", t)
    t = re.sub(r"<li[^>]*>", "\n- ", t)
    t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(re.sub(r"\n{3,}", "\n\n", t)).strip()

have = {p["slug"] for p in json.loads(IDXP.read_text(encoding="utf-8"))}
index = []
for p in fetch(API + "?per_page=10&page=26&_fields=id,slug,title,date,link,content"):
    if p["slug"] in have:
        continue
    title = html.unescape(p["title"]["rendered"])
    body = clean(p["content"]["rendered"])
    path = OUT / f"{p['slug']}.md"
    path.write_text(f"# {title}\n\nSource: {p['link']}\nDate: {p['date']}\n\n{body}\n", encoding="utf-8")
    index.append({"slug": p["slug"], "title": title, "date": p["date"], "link": p["link"],
                  "words": len(body.split()), "file": str(path)})
    print(f"saved {p['slug']} ({len(body.split())} words)")

old = json.loads(IDXP.read_text(encoding="utf-8"))
merged = old + index
IDXP.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Total: {len(merged)}")
