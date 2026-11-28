# YouTube Library DB filing (lesson 65)

The owner's YouTube Library database (`418df8d8-8d8c-8039-b58a-de967eaa3da0`, child of the "Youtube" page in Notion) collects video material. A filing is DISTILLATION; a follow-up "เอามาดราฟเป็น content" runs the same source through the main skill's idea-brief loop (lesson 23).

## Procedure

1. Get video identity from the public oEmbed endpoint — `youtube.com/oembed?url=<watch-url>&format=json` returns title + author_name (channel) without scraping; use them verbatim for Title and Speaker / Channel.
2. Fetch the REAL transcript, never summarize from title/description: `youtube-transcript-api` imports in `~/llama-env` — `YouTubeTranscriptApi().fetch(video_id, languages=["en","en-US","en-GB"])`, join segment `.text` with spaces, read the whole thing before writing.
3. Create the row (POST page, parent = the database id) with props built by TYPE (lesson 46):
   - Title = title
   - Link = rich_text — NOT url-typed; a `{"url": …}` build fails on this DB
   - Speaker / Channel = rich_text
   - Format = select: ⚡ Short-Clip / 🎙️ Podcast
   - Status = select: ⬜ Queued → 🟦 Distilled once summarized (🗑️ Dropped = retired)
   - Asset Residue (แก่นที่ได้) = rich_text — ONE short core-idea phrase
   - Category = rich_text free text (#Topic style)
   - Date Added = created_time — auto on create, NEVER send it
4. Body (children or markdown) follows the FIRST ROW as template: EN summary first — intro paragraph, then `###` section headings with bulleted_list_item points → a `===========` divider paragraph → TH summary MIRRORING the EN structure with BOLD paragraph headers (not headings) and the same points per section. The owner orders both languages by default ("สองเวอร์ชัน ทั้งอังกฤษและไทย").
5. Read-back verify: props by type + block census + every TH section header carries bold annotations.

## Rules

- COVERAGE HONESTY (the closing rule): a clip that NAMES five steps but walks through two gets an explicit "covers steps 1–2" coverage note in BOTH languages — never fill the cut steps from outside knowledge; the row is distilled source material future drafts cite as ground truth (no-fabrication applied to library rows).
- Every claim stays reported-speech of the speaker ("her lab's research", "the top-regret data") — the row is a distillation, not an adduckivity post; brands/sources live in the props (Link, Speaker / Channel), never editorialized into the summary voice.
- When the owner then asks to draft content from the row, the draft's ORIGIN/SOURCES header cites the row's Source URL and the transcript — the row itself is never modified by the drafting loop.
