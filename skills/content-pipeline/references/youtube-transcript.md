# YouTube video as a content source

When the user gives a `youtube.com/watch?v=...` URL (or asks for a post "in angle ..." off a video), get the actual content BEFORE drafting — never draft off the title alone.

## 1. Disambiguate first (cheap, no auth)

```
curl -s "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<ID>&format=json"
```
→ `title` + `author_name` + `provider_name`. Confirms what the video actually is before writing. Titles are often clickbait: the number/claim in the title (e.g. "99% chance of extinction") is the packaging, not necessarily the speaker's stated position — verify the real position in the transcript and cite the real quote, noting the discrepancy in the source comment.

## 2. Fetch the transcript

Use the `~/.venvs/yt` venv (youtube-transcript-api installed). **The installed version is the v2 API:**

```python
import os, youtube_transcript_api as yta
api = yta.YouTubeTranscriptApi()
tr = api.fetch(vid, languages=["en"])      # iterable of snippets, each has .text
txt = " ".join(s.text.strip() for s in tr)
```
- The OLD classmethods `YouTubeTranscriptApi.get_transcript(...)` and `.list_transcripts(...)` are **gone** (AttributeError) — do not use them; the v2 flow is `api = YouTubeTranscriptApi()` then `api.list(vid)` (to inspect available languages / `is_generated`) and `api.fetch(vid, languages=[...])`.
- The venv is minimal — `import os` explicitly inside any `python -c` code (a bare `os` reference fails with NameError).
- Run via `subprocess` with the venv python: `subprocess.run([os.path.expanduser("~/.venvs/yt/bin/python"), "-c", code], ...)`.

## 3. Save + mine

- Save the full transcript to `~/hermes-agent/content-study/references/<topic>-transcript.txt` (commit it) — it's the primary source for the draft's source comment.
- Mine verbatim quotes with a regex `grab(term, before=..., after=...)` helper (find all occurrences, print surrounding window) — quote the speaker's exact words, not a paraphrase.

## Environment note

On this host `web_extract` is a **search-only (ddgs) backend** and cannot extract URLs ("search-only backend and cannot extract URL content"). So for YouTube (and any URL you need to fetch the body of) use `urllib` inside `execute_code` or the yt venv — not `web_extract`.
