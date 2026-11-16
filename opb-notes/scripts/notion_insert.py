#!/usr/bin/env python3
"""Insert one OPB video row into the Notion 'OPB Summary' database.
Usage: notion_insert.py <meta.json>
meta.json keys: name, file, group, duration, size_gb, file_date, status, language,
                summary (short), key_lessons (str, <=2000 chars), tags[], source_path,
                transcript_md (path), body_md (path)  [optional overrides]
"""
import json, os, sys, time, urllib.request, urllib.error

DB_ID = "41adf8d8-8d8c-8075-90ee-dc619d82619d"
API = "https://api.notion.com/v1"
HDRS = {
    "Authorization": f"Bearer {os.environ['NOTION_API_KEY']}",
    "Notion-Version": "2025-09-03",
    "Content-Type": "application/json",
}

def req(method, path, payload=None, raw=False):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request(f"{API}{path}", data=data, headers=HDRS, method=method)
    with urllib.request.urlopen(r) as resp:
        body = resp.read()
    return json.loads(body) if not raw else body

def upload_file(path, filename):
    up = req("POST", "/file_uploads", {"filename": filename, "content_type": "text/markdown", "mode": "single_part"})
    uid = up["id"]
    # send bytes: POST /file_uploads/{id}/send as multipart form-data (auth headers required)
    boundary = "----hermesboundary7d1a6c"
    data = open(path, "rb").read()
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: text/markdown\r\n\r\n"
    ).encode() + data + f"\r\n--{boundary}--\r\n".encode()
    r = urllib.request.Request(f"{API}/file_uploads/{uid}/send", data=body, method="POST")
    r.add_header("Authorization", HDRS["Authorization"])
    r.add_header("Notion-Version", HDRS["Notion-Version"])
    r.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(r) as resp:
        resp.read()
    return uid

def chunked(md_text, limit=1900):
    """Split text into <=limit chunks on line boundaries."""
    parts, cur = [], ""
    for line in md_text.split("\n"):
        if len(cur) + len(line) + 1 > limit and cur:
            parts.append(cur)
            cur = line
        else:
            cur = f"{cur}\n{line}" if cur else line
    if cur:
        parts.append(cur)
    return parts

def main():
    meta = json.load(open(sys.argv[1]))
    tr_md = meta["transcript_md"]
    tr_name = os.path.basename(tr_md)
    body = open(meta.get("body_md", tr_md)).read()

    # 1) upload transcript file
    uid = upload_file(tr_md, tr_name)
    print("uploaded file_upload:", uid)

    # 2) properties
    props = {
        "Name": {"title": [{"text": {"content": meta["name"]}}]},
        "File": {"rich_text": [{"text": {"content": meta["file"]}}]},
        "Group": {"select": {"name": meta["group"]}},
        "Duration": {"rich_text": [{"text": {"content": meta["duration"]}}]},
        "Size GB": {"number": meta["size_gb"]},
        "File Date": {"date": {"start": meta["file_date"]}},
        "Status": {"select": {"name": meta.get("status", "Done")}},
        "Language": {"select": {"name": meta.get("language", "TH")}},
        "Summary": {"rich_text": [{"text": {"content": meta["summary"][:2000]}}]},
        "Key Lessons": {"rich_text": [{"text": {"content": meta["key_lessons"][:2000]}}]},
        "Tags": {"multi_select": [{"name": t} for t in meta.get("tags", [])]},
        "Transcript": {"files": [{"type": "file_upload", "file_upload": {"id": uid}}]},
        "Source Path": {"rich_text": [{"text": {"content": meta["source_path"]}}]},
    }

    # 3) create page with summary-first body (transcript inside details toggle)
    full_md = meta.get("body_override") or (
        "## 📌 สรุปบทเรียน\n\n" + meta["summary"] + "\n\n### 🎯 Key Takeaways\n\n" +
        meta["key_lessons"] +
        "\n\n<details>\n<summary>📜 Transcript เต็ม (กดเพื่อเปิด)</summary>\n\n" +
        body + "\n\n</details>\n"
    )
    payload = {"parent": {"database_id": DB_ID}, "properties": props, "markdown": full_md}
    try:
        page = req("POST", "/pages", payload)
        print("PAGE_CREATED", page["id"], page["url"])
        return
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:300]
        print("FULL_BODY_FAILED -> chunked append:", err)

    # 4) fallback: create page with summary-only body, append transcript in chunks
    payload["markdown"] = "## 📌 สรุปบทเรียน\n\n" + meta["summary"] + "\n\n### 🎯 Key Takeaways\n\n" + meta["key_lessons"]
    page = req("POST", "/pages", payload)
    pid = page["id"]
    print("PAGE_CREATED(slim)", pid, page["url"])
    chunks = chunked(body)
    for i, ch in enumerate(chunks):
        req("PATCH", f"/blocks/{pid}/children", {"children": [{"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"text": {"content": ch}}]}}]})
        time.sleep(0.4)
        print(f"appended chunk {i+1}/{len(chunks)}")

if __name__ == "__main__":
    main()
