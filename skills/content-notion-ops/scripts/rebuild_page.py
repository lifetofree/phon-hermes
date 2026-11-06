#!/usr/bin/env python3
"""Rebuild an adduckivity Notion page from a markdown draft — the standard
publish/patch loop (delete-all + insert + read-back verify).

Battle-tested pairs #100-#103. Rules encoded here:
- token comes from ~/.hermes/.env (NOTION_API_KEY), read INSIDE the process
- payload via temp JSON file + `curl -d @file` (no shell-quoting of Thai bodies)
- <=100 blocks per insert request (API hard limit)
- DELETE each old block individually (bulk delete 400s in this workspace)
- title goes to the `Name` property (payload key `title` is accepted on PATCH,
  read-back lives under properties["Name"])
- read-back verify: block count, empty 0, raw ** 0, forbidden 0, markers PASS

Usage:
    python3 rebuild_page.py <markdown_path> <page_id> [--forbidden w1,w2] \
        [--marker "keep line 1"] [--marker "keep line 2"] [--suffix " — pair #N"]
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from markdown_to_blocks import markdown_to_blocks, verify_readback

API = "https://api.notion.com/v1"


def token():
    for line in open(os.path.expanduser("~/.hermes/.env"), encoding="utf-8"):
        if line.startswith("NOTION_API_KEY="):
            return line.strip().split("=", 1)[1]
    raise SystemExit("NOTION_API_KEY not found in ~/.hermes/.env")


def curl(method, url, tok, payload=None):
    cmd = ["curl", "-s", "-w", "%{http_code}", "-X", method, url,
           "-H", f"Authorization: Bearer {tok}", "-H", "Notion-Version: 2022-06-28"]
    if payload is not None:
        f = tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                        encoding="utf-8")
        json.dump(payload, f, ensure_ascii=False)
        f.close()
        cmd += ["-H", "Content-Type: application/json", "-d", f"@" + f.name]
    r = subprocess.run(cmd + ["-o", "/tmp/nops_resp.json"], capture_output=True,
                       text=True)
    body = {}
    try:
        body = json.load(open("/tmp/nops_resp.json", encoding="utf-8"))
    except Exception:
        pass
    return r.stdout, body


def list_children(pid, tok):
    out, blocks = [], []
    cursor = None
    while True:
        url = f"{API}/blocks/{pid}/children?page_size=100"
        if cursor:
            url += f"&start_cursor={cursor}"
        code, d = curl("GET", url, tok)
        if code != "200":
            raise SystemExit(f"list children failed: {code} {d}")
        out.extend(d.get("results", []))
        if not d.get("has_more"):
            return out
        cursor = d.get("next_cursor")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("markdown_path")
    ap.add_argument("page_id")
    ap.add_argument("--forbidden", default="")
    ap.add_argument("--marker", action="append", default=[])
    ap.add_argument("--suffix", default="")
    args = ap.parse_args()

    tok = token()
    name, blocks, leaks = markdown_to_blocks(open(args.markdown_path, encoding="utf-8").read())
    assert leaks == 0, f"{leaks} raw ** leaks — fix the draft parser output first"
    assert name, "no H1 title found"

    title = name + args.suffix
    code, _ = curl("PATCH", f"{API}/pages/{args.page_id}", tok,
                   {"properties": {"Name": {"title": [{"text": {"content": title}}]}}})
    print("title PATCH:", code)

    old = list_children(args.page_id, tok)
    deleted = 0
    for b in old:
        code, _ = curl("DELETE", f"{API}/blocks/{b['id']}", tok)
        if code == "200":
            deleted += 1
    print(f"deleted: {deleted}/{len(old)}")

    for i in range(0, len(blocks), 100):
        code, _ = curl("PATCH", f"{API}/blocks/{args.page_id}/children", tok,
                       {"children": blocks[i:i + 100]})
        print(f"insert batch {i // 100 + 1}: {code} ({len(blocks[i:i + 100])} blocks)")
        if code != "200":
            raise SystemExit("insert failed — inspect /tmp/nops_resp.json")

    final = list_children(args.page_id, tok)
    forbidden = [w for w in args.forbidden.split(",") if w]
    ok, report = verify_readback(final, expect_markers=args.marker, forbidden=forbidden)
    print("\n".join(report))
    code, page = curl("GET", f"{API}/pages/{args.page_id}", tok)
    props = page.get("properties", {})
    tkey = next((k for k, v in props.items() if v.get("type") == "title"), None)
    print("title read-back:", props[tkey]["title"][0]["plain_text"] if tkey else "?")
    print("VERIFY:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
