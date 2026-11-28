---
name: video-transcribe-pipeline
description: Use when transcribing videos → markdown → Notion summaries.
version: 1.0.0
author: Hermes Agent (lifetofree)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Transcription, whisper, Notion, Markdown, SSH]
---

# Video Transcription Pipeline (Mac → PHON-SERVER → Notion)

Working pipeline, built 2026-11-16 for OPB course videos (reusable for the remaining ~75). All code lives in `~/hermes-agent/opb-notes/` (git-backed).

## When to Use
- User asks to transcribe videos from the MacBook (`focusroom-opb-notes/videos`), save transcripts as markdown, and store summaries in a Notion database.

## Procedure
1. **Copy videos over LAN IP, not Tailscale IP.** `tailscale status` shows each node's LAN address (e.g. macbook = 192.168.1.34). rsync via that IP ≈ 7 MB/s vs 4-5 via 100.x. Add `-o StrictHostKeyChecking=accept-new` — a new host IP means a new known_hosts entry and BatchMode can't prompt. Verify byte-exact with `stat -c %s` (Linux) vs `stat -f %z` (macOS).
2. **whisper.cpp must build with CUDA 13.3, not PATH nvcc.** GPU = RTX 5060 Ti (sm_120/Blackwell); `/usr/bin/nvcc` is 12.4 and dies on `compute_120a`. Build: `cmake -S ~/whisper.cpp -B ~/whisper.cpp/build -DGGML_CUDA=1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_CUDA_COMPILER=/usr/local/cuda/bin/nvcc` (same nvcc that built ~/llama.cpp). CLI: `~/whisper.cpp/build/bin/whisper-cli`.
3. **Model: `bash models/download-ggml-model.sh large-v3-turbo`.** If the .bin is ~29 bytes containing 'Invalid username or password', DELETE it first — the script skips existing files. Verify `stat -c %s` > 1 GB. 60 s Thai audio ≈ 7 s wall incl. load → ~1 h video ≈ 4-6 min.
4. **Transcribe per video:** `scripts/transcribe.sh <video.mp4>` = ffprobe duration → ffmpeg 16 kHz mono wav → whisper `-l th -oj -ojf -of <base>` → `scripts/md_from_json.py` writes `transcripts/<name>.md` with [HH:MM:SS] paragraph markers. Gotcha: -ojf output is `<base>.json`, NOT `.json.json`. Running 2 whisper jobs concurrently is fine (16 GB VRAM).
5. **Summarize:** read the transcript via read_file (may need 2-3 calls), write Thai lesson summary to `summaries/<name>.md` — สรุปสั้น + Key Takeaways + คำศัพท์ table + disclaimer that names may be mis-transcribed.
6. **Notion DB 'OPB Summary'** (database_id 41adf8d8-8d8c-8075-90ee-dc619d82619d, data_source_id ...809c-9125-000b44710508): 13 properties (Name/File/Group/Duration/Size GB/File Date/Status/Language/Summary/Key Lessons/Tags/Transcript/Source Path) — schema in /tmp/notion_schema.json, recreate if needed. Insert per video: `scripts/notion_insert.py <meta.json>` (build meta JSON like /tmp/meta_01a.json — bash heredoc with Thai text is fine). Body = สรุปบทเรียน + Key Takeaways + full transcript inside `<details>` toggle; `markdown` param accepted ~190 KB directly. Transcript .md attached via files & media (upload flow: POST /file_uploads → POST {id}/send multipart with auth — see notion skill).
7. **Backup:** transcripts/ + summaries/ + scripts/ are gitignored-clean (`json/`, `__pycache__/`, `*.mp4`, `*.wav` excluded); commit + push to origin main. Never hand-count rows — query the data_source and compare against expected N; watch for the user's manual empty row in the DB (don't delete it without asking).

## Pitfalls
- curl to HuggingFace: always `--fail -L` — a 401 page saved with -o looks like a valid file and breaks later silently.
- rsync `--partial` resumes but counts existing bytes in progress2 %; trust byte-stat verification, not the %.
- ffmpeg smoke-test with a 60 s clip (`-ss 0 -t 60`) before committing to full runs.
- Notion rich_text property cap 2000 chars — script truncates; keep สรุปย่อ tight.

## Verification
- Row count in DB == number of videos processed (query data_source, print Name/Status/Duration/files per row).
- Toggle block inside each page holds ~full transcript char count (query blocks/children of toggle).
- `git ls-files` shows no json/pyc/mp4/wav.