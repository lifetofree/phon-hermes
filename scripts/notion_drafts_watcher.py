#!/usr/bin/env python3
"""Watch Notion "Content Drafts" DB for NEW pages (watchdog for cron no_agent job).

- Baseline run (no state file): records current pages silently, prints nothing.
- Later runs: any page id not in state = new draft -> print ping lines (delivered verbatim).
- No new pages / API failure handled: failure exits nonzero (recorded in cron history, delivery suppressed).
Deterministic output; state at ~/.hermes/scripts/notion_drafts_watcher.state.json
"""
import json
import os
import re
import sys
import urllib.request

STATE_PATH = os.path.expanduser("~/.hermes/scripts/notion_drafts_watcher.state.json")
DB_ID = "3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520"  # Content Drafts DB
ENV_FILES = ("~/.hermes/.env", "~/hermes-agent/.env")


def load_token():
    for path in ENV_FILES:
        path = os.path.expanduser(path)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"\s*(?:NOTION_API_KEY|NOTION_TOKEN)\s*=\s*(\S+)", line)
                if m:
                    return m.group(1).strip().strip("'\"")
    return None


def notion_query(token):
    url = "https://api.notion.com/v1/databases/%s/query" % DB_ID
    body = {
        "sorts": [{"timestamp": "created_time", "direction": "descending"}],
        "page_size": 100,
    }
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"))
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Notion-Version", "2022-06-28")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as fh:
        return json.load(fh)


def collect_pages(payload):
    pages = {}
    for r in payload.get("results", []):
        props = r.get("properties", {})
        title = "".join(x.get("plain_text", "") for x in props.get("Name", {}).get("title", []))
        status = ""
        st = props.get("Status", {})
        if st.get("type") == "select" and st.get("select"):
            status = st["select"].get("name", "")
        pages[r["id"]] = {"title": title, "status": status, "created": r["created_time"]}
    return pages


def main():
    token = load_token()
    if not token:
        print("notion-drafts watcher: NOTION token not found in env files", file=sys.stderr)
        return 2

    pages = collect_pages(notion_query(token))

    state = {"known": {}}
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, encoding="utf-8") as fh:
                state = json.load(fh)
        except Exception:
            state = {"known": {}}
    known = state.setdefault("known", {})

    if not known:
        known.update({pid: p["created"] for pid, p in pages.items()})
        with open(STATE_PATH, "w", encoding="utf-8") as fh:
            json.dump(state, fh, ensure_ascii=False, indent=1)
        return 0  # baseline: silent

    new_items = [(pid, p) for pid, p in pages.items() if pid not in known]
    if new_items:
        lines = ["📝 Draft ใหม่ใน Notion (Content Drafts)"]
        for pid, p in sorted(new_items, key=lambda kv: kv[1]["created"]):
            link = "https://app.notion.com/p/" + pid.replace("-", "")
            lines.append("• %s" % (p["title"] or "(ไม่มีชื่อ)"))
            lines.append("   Status: %s | %s" % (p["status"] or "-", link))
        print(re.sub(r"(https?://[^\s<]+)", r"<\1>", "\n".join(lines)))

    known.update({pid: p["created"] for pid, p in new_items})
    with open(STATE_PATH, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
