#!/usr/bin/env python3
"""Draft-time battery for adduckivity CURRENT FORM / TECH drafts.

Strips the HTML comment header, then grades the BODY (plus hashtags tail):
  wc-w, H1/H2/H3 counts, beat dots, blockquotes, pronouns (พร/เรา/คุณ/คับ/ผม
  with Thai negative lookahead), CUT survivors (exit 1 if any), non-Thai
  codepoint scan, Thai–Latin adjacency scan.

Usage:
  python3 draft_battery.py <draft.md> [--cut "term1,term2,..."] [--expect-keep "t1,t2"]

--cut terms are graded -> 0 (any survivor = exit 1). Match is case-insensitive
for pure-Latin terms, exact for Thai. --expect-keep prints counts for terms
allowed to stay (e.g. a critic-kept phrase family) without failing.
Exit codes: 0 = all CUT terms zero, 1 = survivors found, 2 = usage/IO error.
"""
import argparse
import re
import sys
import unicodedata


def strip_header(raw: str) -> str:
    body = re.sub(r"<!--.*?-->\s*", "", raw, flags=re.S)
    assert "<!--" not in body, "HTML comment leaked into body"
    return body


def thai_lookahead_count(text: str, word: str) -> int:
    # 'พร' must not count inside 'พรอ่าน' etc.; 'เรา' inside 'เราจะ' etc. —
    # only Thai VOWEL MARKERS follow the base word in these pronouns, so the
    # lookahead blocks consonant-starting syllables (e.g. พร+อ is a real hit).
    return len(re.findall(re.escape(word) + r"(?![ก-ฮ])", text))


def codepoint_scan(text: str) -> dict:
    odd = {}
    for ch in text:
        o = ord(ch)
        if 0x0E00 <= o <= 0x0E7F:  # Thai block
            continue
        if o < 128 and (ch.isalnum() or ch in "\n .#>-*\"'():"):
            continue
        if ch in "\u2014\u2013":  # em/en dash are house style
            continue
        odd[ch] = odd.get(ch, 0) + 1
    return odd


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--cut", default="", help="comma-separated zero-count terms")
    ap.add_argument("--expect-keep", default="", help="comma-separated terms to report without failing")
    args = ap.parse_args()

    try:
        raw = open(args.draft, encoding="utf-8").read()
    except OSError as e:
        print(f"IO error: {e}", file=sys.stderr)
        return 2

    body = strip_header(raw)
    issues = []

    print(f"wc-w (file incl. header): {len(raw.split())}")
    print(f"wc-w (body):              {len(body.split())}")
    print(f"H1: {len(re.findall(r'(?m)^# ', body))}  H2: {len(re.findall(r'(?m)^## ', body))}  "
          f"H3: {len(re.findall(r'(?m)^### ', body))}")
    print(f"beat dots: {len(re.findall(r'(?m)^\.$', body))}  "
          f"blockquotes: {len(re.findall(r'(?m)^> ', body))}")

    pronouns = {}
    for w in ("พร", "เรา", "คุณ", "คับ", "ผม"):
        n = thai_lookahead_count(body, w) if w in ("พร", "เรา") else len(re.findall(re.escape(w), body))
        pronouns[w] = n
    print("pronouns:", " / ".join(f"{k} {v}" for k, v in pronouns.items()))

    survivors = {}
    if args.cut:
        for term in [t.strip() for t in args.cut.split(",") if t.strip()]:
            flags = re.I if term.isascii() else 0
            n = len(re.findall(re.escape(term), body, flags))
            if n:
                survivors[term] = n
        if survivors:
            issues.append(f"CUT survivors: {survivors}")
        else:
            print(f"CUT zero-count: all {len([t for t in args.cut.split(',') if t.strip()])} terms -> 0")

    for term in [t.strip() for t in args.expect_keep.split(",") if t.strip()]:
        print(f"keep-count {term!r}: {len(re.findall(re.escape(term), body))}")

    odd = codepoint_scan(body)
    if odd:
        issues.append(f"odd codepoints: {odd}")
    adj = re.findall(r"[ก-๙][A-Za-z]|[A-Za-z][ก-๙]", body)
    if adj:
        issues.append(f"Thai-Latin adjacency: {adj}")

    if odd or adj:
        print(f"scans: odd={odd or 'none'} adjacency={adj or 'none'}")
    else:
        print("scans: CLEAN (codepoint + adjacency)")

    if issues:
        print("\nFAIL:")
        for i in issues:
            print(f"  - {i}")
        return 1
    print("\nPASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
