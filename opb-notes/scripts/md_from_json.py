#!/usr/bin/env python3
"""Convert whisper.cpp full JSON output to a readable Thai-friendly markdown transcript.
Usage: md_from_json.py input.json.json output.md "Title" "Source file" """
import json, sys

def ts(sec: float) -> str:
    sec = int(sec)
    return f"{sec//3600:02d}:{(sec%3600)//60:02d}:{sec%60:02d}"

def main():
    jpath, mpath, title, src = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    d = json.load(open(jpath))
    segs = d.get("transcription", [])
    paras, cur, start = [], [], None
    for s in segs:
        t = s["timestamps"]["from"]; off = s["offsets"]["from"] / 1000.0
        txt = s["text"].strip()
        if not txt:
            continue
        if start is None:
            start = off
        cur.append(txt)
        # break paragraph: >6s gap to next or >=5 sentences-ish length
        gap_next = False
        paras.append if False else None
        if len(" ".join(cur)) > 600:
            paras.append((start, " ".join(cur)))
            cur, start = [], None
    if cur:
        paras.append((start, " ".join(cur)))
    total = segs[-1]["offsets"]["to"] / 1000.0 if segs else 0
    lines = [
        f"# Transcript — {title}",
        "",
        f"- **Source file:** `{src}`",
        f"- **Duration:** {ts(total)}",
        f"- **Segments:** {len(segs)}",
        f"- **Transcribed:** whisper large-v3-turbo (CUDA) — whisper.cpp",
        "",
        "---",
        "",
    ]
    for start, text in paras:
        lines.append(f"**[{ts(start)}]** {text}")
        lines.append("")
    open(mpath, "w", encoding="utf-8").write("\n".join(lines))
    print(f"WROTE {mpath}: {len(paras)} paragraphs, {sum(len(t) for _,t in paras)} chars, duration {ts(total)}")

if __name__ == "__main__":
    main()
