#!/usr/bin/env python3
"""Generate the Obsidian-style vault (markdown + wiki-links) from content-study/index.json.

Creates/refreshes:
  vault/pairs/pair-0NN.md          (1 file per pair — grouped by slug; multiple slugs of
                                    the same pair land in ONE file, e.g. v1 + publish)
  vault/index.md                   (MOC: recent pairs, open pairs, families)

Known collision fix: two 2026-10-06 posts were both labelled "pair #40" in the corpus
history — embrace-the-limit is emitted as pair-040b, daily-repetition keeps 040.

Merge-safe: existing pair files are only rewritten when their content hash changes
(hash in the file header). branches/ and families/ files are NEVER touched.

Usage: python3 skills/content-pipeline/scripts/generate_vault.py
"""
import hashlib
import json
import os
import re

CS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))), "content-study")
VAULT = os.path.join(CS, "vault")
PAIRS = os.path.join(VAULT, "pairs")

COLLISION = {"20261006-cnt-embrace-the-limit": "040b"}
FAMILIES = [
    ("family-ai-brief-chain", "ยุค AI/Agentic: ถูกเทรน vs ผู้เทรน → เจได→ซิธ → Let them fight (#57 #64 #80)"),
    ("family-locked-system", "ระบบที่ล็อกไว้: commitment device → วันที่ระบบพัง (#22 #79 + กิ่ง B/C stock)"),
    ("family-explore-exploit", "Explore vs Exploit (#55 #56)"),
    ("family-signal-triad", "Signal triad: Attention / Explore / Exploit (#54 #55 #56)"),
]

# research node back-links: pair key -> research files (in vault/research/)
RESEARCH_LINKS = {
    "001": ["autoclaw-research"], "086": ["autoclaw-research"], "087": ["autoclaw-research"],
    "007": ["dopamine-nation-research"], "008": ["dopamine-nation-research"],
    "009": ["essentialism-research"],
    "017": ["four-thousand-weeks-research"],
    "083": ["grokbot-research"],
    "084": ["jev-research"],
    "005": ["llamacpp-research"],
    "011": ["lmstudio-research"], "013": ["lmstudio-research"],
    "018": ["memento-mori-research"],
    "090": ["muse-research"],
    "003": ["ollama-research"], "006": ["ollama-research"],
    "091": ["orca-research"],
    "021": ["rework-research"], "024": ["rework-research"], "025": ["rework-research"],
    "030": ["scientific-advertising-research"], "035": ["scientific-advertising-research"],
    "015": ["snapzy-research"], "045": ["snapzy-research"],
    "002": ["superclick-research"],
    "012": ["tailscale-serve-research"],
    "004": ["unsloth-core-research", "unsloth-studio-research"],
    "010": ["unsloth-desktop-research"],
    "049": ["wispr-flow-research"], "061": ["wispr-flow-research"],
}


def ehash(e):
    return hashlib.sha1(json.dumps(e, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:10]



def gen_tags(CS, VAULT, groups):
    """Scan publish archives (fallback posts) of each pair for hashtags -> tags/<tag>.md"""
    TAGDIR = os.path.join(VAULT, "tags")
    os.makedirs(TAGDIR, exist_ok=True)
    EXCLUDE = {"สรุปแบบวิศวกรเป็ด"}
    tagmap = {}  # tag -> [(pairkey, date)]
    for key, g in groups.items():
        # prefer a publish archive, else the posts file
        chosen = None
        for slug in sorted(g["slugs"]):
            p = os.path.join(CS, "web-archive", slug + ".md")
            if os.path.exists(p) and ("publish" in slug or "closed" in slug):
                chosen = p; break
        if chosen is None:
            for slug in sorted(g["slugs"]):
                p = os.path.join(CS, "web-archive", slug + ".md")
                if os.path.exists(p):
                    chosen = p; break
        if chosen is None:
            for slug in sorted(g["slugs"]):
                p = os.path.join(CS, "posts", slug + ".md")
                if os.path.exists(p):
                    chosen = p; break
        if chosen is None:
            continue
        txt = open(chosen).read()
        seen = set()
        for line in txt.splitlines():
            if line.lstrip().startswith("#"):   # markdown heading — skip
                continue
            for tok in re.findall(r"#([^\s#]+)", line):
                if tok in EXCLUDE or tok.isdigit():
                    continue
                if not re.fullmatch(r"[A-Za-z0-9\u0E00-\u0E7F_-]{2,}", tok):
                    continue
                if re.fullmatch(r"\d+", tok):
                    continue
                if tok not in seen:
                    seen.add(tok)
                    tagmap.setdefault(tok, []).append((key, g["date"]))
    # write tag files
    valid = set()
    written = created = 0
    for tag, pairs in sorted(tagmap.items()):
        path = os.path.join(TAGDIR, f"{tag}.md")
        h = hashlib.sha1(json.dumps(sorted(pairs), ensure_ascii=False).encode()).hexdigest()[:10]
        valid.add(f"{tag}.md")
        body = "---\ntype: tag\nhash: " + h + "\ncount: " + str(len(pairs)) + "\n---\n\n#" + tag + " — ใช้ใน " + str(len(pairs)) + " คู่\n\n"
        for k, d in sorted(pairs, key=lambda t: t[1], reverse=True):
            body += f"- [[pair-{k}]] — {d}\n"
        if os.path.exists(path):
            mm = re.search(r"^hash: (\S+)$", open(path).read(), re.M)
            if mm and mm.group(1) == h:
                continue
            written += 1
        else:
            created += 1
        open(path, "w").write(body)
    # stale cleanup
    for f in os.listdir(TAGDIR):
        if f.endswith(".md") and f not in valid:
            os.remove(os.path.join(TAGDIR, f))
    return len(tagmap), created, written


def main():
    idx = json.load(open(os.path.join(CS, "index.json")))
    os.makedirs(PAIRS, exist_ok=True)

    # 1) collect entries per -cnt- slug
    by_slug = {}
    for e in idx:
        s = e.get("slug") or ""
        if "-cnt-" in s:
            by_slug.setdefault(s, []).append(e)

    # 2) pair number per slug (majority vote; explicit collision fix)
    rows = {}
    for slug, entries in by_slug.items():
        m = re.match(r"(\d{8})-cnt-(.+)", slug)
        if not m:
            continue
        date = m.group(1)
        entries.sort(key=lambda e: e.get("date") or "")
        texts = [json.dumps(e, ensure_ascii=False) for e in entries]
        nums = [int(x.group(1)) for t in texts for x in re.finditer(r"pair #(\d+)", t)]
        n = max(set(nums), key=nums.count) if nums else None
        if slug in COLLISION:
            n = None
        rows[slug] = {"n": n, "date": date, "entries": entries}

    # 3) fallback numbers for unnumbered slugs
    used = {r["n"] for r in rows.values() if r["n"]}
    fallback = 0
    for slug, r in rows.items():
        if r["n"] is None:
            if slug in COLLISION:
                r["key"] = COLLISION[slug]
                continue
            fallback += 1
            while fallback in used:
                fallback += 1
            r["n"] = fallback
            used.add(fallback)

    # 4) group multiple slugs of the same pair into one file
    groups = {}
    for slug, r in rows.items():
        key = r.get("key") or f"{r['n']:03d}"
        g = groups.setdefault(key, {"n": r["n"], "date": r["date"], "slugs": []})
        g["slugs"].append(slug)
        g["date"] = min(g["date"], r["date"])
        pub = [e for e in r["entries"] if "published" in (e.get("status") or "")]
        fin = (pub or r["entries"])[-1]
        if "published" in (fin.get("status") or "") or g.get("final") is None:
            g["final"] = fin

    # 5) write pair files
    def slug_rel(slug):
        for sub in ("posts", "web-archive"):
            p = os.path.join(CS, sub, slug + ".md")
            if os.path.exists(p):
                return os.path.join("..", sub, slug + ".md")
        return None

    created = updated = 0
    for key, g in groups.items():
        path = os.path.join(PAIRS, f"pair-{key}.md")
        fin = g["final"]
        h = ehash(fin) + "-" + hashlib.sha1((",".join(sorted(g["slugs"])) + "|" + ",".join(sorted(RESEARCH_LINKS.get(key, [])))).encode()).hexdigest()[:6]
        L = ["---", f"pair: {key}", f"hash: {h}", f"date: {g['date']}", "---", "",
             f"# {fin.get('title', '(no title)')}", ""]
        L.append(f"- **status:** {fin.get('status', '')}")
        L.append(f"- **date:** {g['date']}")
        if fin.get("words"):
            L.append(f"- **words:** {fin['words']}")
        if fin.get("form"):
            L.append(f"- **form:** {fin['form']}")
        if fin.get("link"):
            L.append(f"- **Notion:** {fin['link']}")
        L.append("- **ไฟล์โพสต์:**")
        for s in sorted(g["slugs"]):
            rel = slug_rel(s)
            L.append(f"  - [{s}]({rel})" if rel else f"  - {s} (ไม่พบไฟล์)")
        rlinks = RESEARCH_LINKS.get(key)
        if rlinks:
            L.append("- **Research:** " + " · ".join(f"[[{r}]]" for r in rlinks))
        if fin.get("note"):
            L.append(f"\n## บันทึก\n\n{fin['note']}")
        body = "\n".join(L) + "\n"
        if os.path.exists(path):
            mm = re.search(r"^hash: (\S+)$", open(path).read(), re.M)
            if mm and mm.group(1) == h:
                continue
            updated += 1
        else:
            created += 1
        open(path, "w").write(body)

    # 5b) remove stale pair files (old flat numbering / retired keys)
    valid = {f"pair-{k}.md" for k in groups}
    for f in os.listdir(PAIRS):
        if f.endswith(".md") and f not in valid:
            os.remove(os.path.join(PAIRS, f))

    # 6) MOC
    open_pairs = [(k, g) for k, g in groups.items() if "published" not in (g["final"].get("status") or "")]
    closed_pairs = [(k, g) for k, g in groups.items() if "published" in (g["final"].get("status") or "")]
    rec = sorted(groups.items(), key=lambda kv: kv[1]["date"], reverse=True)[:12]
    M = ["---", "type: moc", "---", "", "# Content Study — สารบัญกลาง", "",
         f"- คู่ทั้งหมด: **{len(groups)}** | published: **{len(closed_pairs)}** | ยังเปิด: **{len(open_pairs)}**",
         "- กติกา: [[README]]", "", "## คู่ล่าสุด", ""]
    for k, g in rec:
        M.append(f"- [[pair-{k}]] — {g['date']} · {(g['final'].get('status') or '')[:50]}")
    M += ["", "## คู่ที่ยังเปิด", ""]
    for k, g in sorted(open_pairs, key=lambda kv: kv[1]["date"], reverse=True):
        M.append(f"- [[pair-{k}]] — {g['date']} · {(g['final'].get('status') or '')[:50]}")
    M += ["", "## กิ่งที่ยังเปิด", ""]
    brdir = os.path.join(VAULT, "branches")
    if os.path.isdir(brdir):
        for f in sorted(os.listdir(brdir)):
            if f.endswith(".md"):
                txt = open(os.path.join(brdir, f)).read()
                if re.search(r"^status: (open|stock)$", txt, re.M):
                    M.append(f"- [[{f[:-3]}]]")
    M += ["", "## บทเรียนที่วนซ้ำ (lessons — curated)", ""]
    lesdir = os.path.join(VAULT, "lessons")
    if os.path.isdir(lesdir):
        for f in sorted(os.listdir(lesdir)):
            if f.endswith(".md"):
                M.append(f"- [[{f[:-3]}]]")
    M += ["", "## เหตุการณ์ (events — curated)", ""]
    evdir = os.path.join(VAULT, "events")
    if os.path.isdir(evdir):
        for f in sorted(os.listdir(evdir)):
            if f.endswith(".md"):
                M.append(f"- [[{f[:-3]}]]")
    tag_count, tc, tw = gen_tags(CS, VAULT, groups)
    M += ["", f"## แท็ก ({tag_count} ตัว — เรียงตามจำนวนคู่ที่ใช้)", ""]
    TAGDIR = os.path.join(VAULT, "tags")
    tagfiles = []
    for f in os.listdir(os.path.join(VAULT, "tags")):
        if f.endswith(".md"):
            c = re.search(r"^count: (\d+)$", open(os.path.join(TAGDIR, f)).read(), re.M)
            tagfiles.append((int(c.group(1)) if c else 0, f[:-3]))
    for c, t in sorted(tagfiles, reverse=True)[:20]:
        M.append(f"- [[{t}]] — {c} คู่")
    M += ["", "## Research", ""]
    resdir = os.path.join(os.path.dirname(CS), "research")
    if os.path.isdir(resdir):
        for f in sorted(os.listdir(resdir)):
            if f.endswith(".md") and f not in ("README.md", "index.md"):
                M.append(f"- [[{f[:-3]}]]")
    M += ["", "## สายเรื่อง (families)", ""]
    for name, desc in FAMILIES:
        M.append(f"- [[{name}]] — {desc}")
    M.append("")
    open(os.path.join(VAULT, "index.md"), "w").write("\n".join(M) + "\n")
    print(f"pairs: {created} created, {updated} updated, {len(groups)} total; index.md refreshed")


if __name__ == "__main__":
    main()
