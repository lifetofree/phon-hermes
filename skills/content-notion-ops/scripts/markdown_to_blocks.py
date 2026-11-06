#!/usr/bin/env python3
"""Canonical markdown -> Notion blocks converter (segment-level inline bold).

Battle-tested through pair #100-#103 (2026-11): whole-line bold parsers leak raw
`**` (6-7 spots on the ZCode page); this segment-level version is the fix.

Conventions (the adduckivity markdown dialect):
- `# H1`      -> page title (returned separately, NOT a block)
- `## H2`     -> heading_2
- `### H3`    -> heading_3
- `> text`    -> quote (inline bold preserved)
- `- text`    -> bulleted_list_item
- ```fences``` -> code block (language bash)
- `.` alone   -> beat paragraph (kept as paragraph)
- `**x**`     -> inline bold at ANY position in the line (segment split)
- `---`       -> divider, but only if a previous block exists (divider-before-first
                 is dropped: Notion renders it as an empty paragraph)

Usage:
    from markdown_to_blocks import markdown_to_blocks
    name, blocks, leaks = markdown_to_blocks(open(path).read())
"""
import re
import json


def parse_line(s: str):
    """One markdown line -> Notion rich_text array with segment-level bold."""
    parts = s.split("**")
    items = []
    for i, seg in enumerate(parts):
        if not seg:
            continue
        it = {"text": {"content": seg}}
        if i % 2 == 1:
            it["annotations"] = {"bold": True}
        items.append(it)
    return items


def strip_comment(raw: str) -> str:
    """Strip the HTML-comment draft header (unanchored — the comment is not
    always at byte 0; an H1-first file defeats `^<!--` stripping)."""
    return re.sub(r"<!--.*?-->\s*", "", raw, flags=re.S)


def markdown_to_blocks(raw: str):
    """Returns (page_name, blocks, leaks). `leaks` = count of raw `**` surviving
    in any rich_text segment — MUST be 0 before shipping."""
    text = strip_comment(raw)
    assert "<!--" not in text, "HTML comment survived the strip — abort"

    name = None
    blocks = []
    pending_hr = False
    in_code = False
    code_buf = []

    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            if in_code:
                blocks.append({"object": "block", "type": "code",
                               "code": {"rich_text": [{"text": {"content": "\n".join(code_buf)}}],
                                        "language": "bash"}})
                in_code = False
                code_buf = []
            else:
                in_code = True
            continue
        if in_code:
            code_buf.append(line)
            continue
        if not s:
            continue
        if s == "---":
            pending_hr = True
            continue
        if pending_hr:
            if blocks:
                blocks.append({"object": "block", "type": "divider", "divider": {}})
            pending_hr = False
        if s.startswith("# ") and name is None:
            name = s[2:].strip()
            continue
        if s.startswith("### "):
            blocks.append({"object": "block", "type": "heading_3",
                           "heading_3": {"rich_text": parse_line(s[4:].strip())}})
            continue
        if s.startswith("## "):
            blocks.append({"object": "block", "type": "heading_2",
                           "heading_2": {"rich_text": parse_line(s[3:].strip())}})
            continue
        if s.startswith("# "):
            # extra H1s (e.g. duck closer) ship as heading_2
            blocks.append({"object": "block", "type": "heading_2",
                           "heading_2": {"rich_text": parse_line(s[2:].strip())}})
            continue
        if s.startswith("> "):
            blocks.append({"object": "block", "type": "quote",
                           "quote": {"rich_text": parse_line(s[2:].strip())}})
            continue
        if s.startswith("- "):
            blocks.append({"object": "block", "type": "bulleted_list_item",
                           "bulleted_list_item": {"rich_text": parse_line(s[2:].strip())}})
            continue
        blocks.append({"object": "block", "type": "paragraph",
                       "paragraph": {"rich_text": parse_line(s)}})

    leaks = 0
    for b in blocks:
        inner = b.get(b["type"]) or {}
        for rt in inner.get("rich_text", []):
            if "**" in rt.get("text", {}).get("content", ""):
                leaks += 1
    return name, blocks, leaks


def verify_readback(blocks: list, expect_markers=(), forbidden=()):
    """Read-back checklist against GET /v1/blocks/{page_id}/children results.
    Returns (ok, report_lines)."""
    def btxt(b):
        inner = b.get(b["type"]) or {}
        return "".join(x.get("plain_text", "") for x in inner.get("rich_text", []))

    report = []
    ok = True
    report.append(f"blocks: {len(blocks)}")
    empty = sum(1 for b in blocks if b["type"] == "paragraph" and not btxt(b))
    if empty:
        ok = False
    report.append(f"empty paragraphs: {empty} (want 0)")
    allt = "\n".join(btxt(b) for b in blocks)
    leaks = allt.count("**")
    if leaks:
        ok = False
    report.append(f"raw **: {leaks} (want 0)")
    for w in forbidden:
        n = allt.count(w)
        report.append(f"forbidden {w!r}: {n} (want 0)")
        if n:
            ok = False
    for m in expect_markers:
        hit = m in allt
        report.append(f"marker {'PASS' if hit else 'FAIL'}: {m[:40]}")
        if not hit:
            ok = False
    return ok, report


if __name__ == "__main__":
    import sys
    raw = open(sys.argv[1], encoding="utf-8").read()
    name, blocks, leaks = markdown_to_blocks(raw)
    print(json.dumps({"name": name, "blocks": len(blocks), "leaks": leaks},
                     ensure_ascii=False))
