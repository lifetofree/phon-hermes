# OPB Notes — transcripts & lesson summaries

Backup of video transcripts + lesson summaries from `focusroom-opb-notes` (MacBook: `~/Documents/Projects/focusroom-opb-notes/videos`).

## Structure

- `transcripts/` — full speech-to-text markdown per video (whisper large-v3-turbo, CUDA on PHON-SERVER)
- `summaries/` — Thai lesson summaries per video (mirrors rows in Notion DB "OPB Summary")
- `scripts/` — pipeline tooling (transcribe.sh, md_from_json.py, notion_insert.py)
- `videos/`, `audio/` — large media, NOT committed (gitignored)

## Pipeline

1. `rsync` live-01*.mp4 from MacBook (LAN IP faster than Tailscale IP)
2. `scripts/transcribe.sh <video>` → wav → whisper JSON → `transcripts/<name>.md`
3. Summarize per video → `summaries/<name>.md`
4. `scripts/notion_insert.py <meta.json>` → row in Notion DB (summary in body + transcript attached)
