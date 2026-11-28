# Full-Corpus Fetch and Product-Site Survey

Extensions to voice-analysis-from-wordpress.md for two follow-up requests: "read EVERYTHING ever written" (full corpus) and mapping a second, related web property (e.g. an interactive product site alongside the blog).

## Full-corpus fetch (254 posts, validated)

1. **Get the total first**: `curl -sI "<site>/wp-json/wp/v2/posts?per_page=1" | grep -i x-wp-total` → `x-wp-total: 254`, `x-wp-totalpages` with per_page=1; with per_page=10 the last page is 26 holding a remainder of 4 — loop to that page too, don't stop at a round 25.
2. **Dedupe by slug**: load existing index.json into a `have` set before fetching; skip slugs already stored. Re-runs then fetch 0 new safely (verify output says `Fetched: 0 new`).
3. **Run as a background process** (`terminal(background=true)`) — 20+ pages × ~1s throttle takes minutes; then `process(wait)`.
4. **Keep one generic fetch script** parameterized by page range (`~/hermes-agent/scripts/fetch_wp_posts_all.py`) rather than one script per batch; append new posts to the same index.json.

## Era/timeline analysis (the payoff of a full corpus)

A partial corpus (10-40 recent posts) shows current voice; ONLY the full corpus shows evolution. Produce a timeline table in the deep-dive doc:

- **Monthly histogram** from index.json dates — spots launch bursts (e.g. 75 posts in one month = pre-system high-volume era) and the later quality-over-frequency shift.
- **Narrator-name grep**: `grep -l "แอด" *.md | wc -l` vs current pronoun — an old persona persisting in ~40% of files marks the pre-system era; the rename point is the system's birth.
- **Archive-category count** — the owner formally archived their own early era; that count ≈ size of era 1.
- Read 1-2 posts from the OLDEST pages to characterize the early tone (here: soft, encouraging, personal-blog, no engineering metaphors yet).
- Table columns: era, date span, ~count, traits. Note which era the current bots' SOUL.md personas come from (the latest).

## Product-site survey (the blog's sibling app)

When the user mentions a second site (e.g. immersive.adduckivity.com), map it the same session:

1. `curl -sL <url> -o /tmp/site.html` then extract `href="..."` values; filter to same-host paths — a Next.js/SPA still server-renders links, and `/tool/guide` pages carry the full explanatory text.
2. Fetch each internal page, strip tags to text (same script pattern as WP cleaner) — app shells return ~200 chars of UI labels; `/guide` pages return 5-9k chars of real content. Don't conclude "no content" from an app shell.
3. Write `content-study/<SITE>_MAP.md`: tagline, per-tool table (tool, role, problem solved, which blog protocol it implements), hard numbers from the app (durations, step counts — sales/content bots quote these), language (an English app over a Thai blog means language switching per surface).
4. Append the map path to the content + sales bots' SOUL.md; commit + push with the rest.

This completed the three-layer business picture for the user: Knowledge (blog corpus) → Tools (product site) → Staff (the bot team) — a useful frame to report back.
