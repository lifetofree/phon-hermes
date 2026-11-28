# Voice Analysis from WordPress

Turn the user's published writing into a machine-readable style guide so a content-bot profile writes in the owner's voice instead of generic AI prose. Used for wp.adduckivity.com (Duck OS / Adduckivity); generalizes to any WordPress site.

## Why
A persona SOUL.md alone produces tone-adjacent output. Reading the owner's real corpus (10-40 posts) surfaces the actual article archetypes, section grammar, signature phrases, forbidden-word discipline, and length norms — enough for the bot to reproduce structure unprompted.

## Procedure (validated)

1. **Fetch via WP REST API** — no scraping needed:
   - List: `https://<site>/wp-json/wp/v2/posts?per_page=10&_fields=id,slug,title,date,link,content` (paginate with `&page=N` for more).
   - Save each post as markdown: title, Source URL, date, then `content.rendered` stripped of tags (convert `</p>` to blank line, `<br>` to newline, `<h2-4>` to `##`, `<li>` to `- `). Store under `<repo>/content-study/posts/` with an `index.json` (slug, title, date, link, word count).
   - Working scripts: `~/hermes-agent/scripts/fetch_wp_posts.py` and `fetch_wp_posts_p2.py` (urllib, no deps).
2. **Read closely first, count second.** Read at least 4-5 full posts before grepping anything — the archetypes are visible in narrative flow, not in token counts. Then confirm with greps: section-header scan (`grep -E "^#{1,3} "`), category counts from URL paths, date histogram from index.json (spots launch bursts).
3. **Write the style guide** (`content-study/WRITING_STYLE_GUIDE.md`):
   - Voice in one line (e.g. "วิศวกรเป็ด" — engineer-metaphor explainers).
   - Article archetypes with per-archetype section grammar. Duck OS had two: System/Mindset (Hook → Bug Report with tech-named errors → cited research → named Protocol → tie to system Laws → sign-off) and Tool Review (how it works → blunt Pros/Cons → comparison table + dated pricing → tiered Pro Tips).
   - Voice markers verbatim: pronouns, sentence-closers, loanword handling, recurring metaphors.
   - **Forbidden words actually absent from the corpus** — verify by reading; the firewall is only credible because the owner never violates it.
   - Length norms per archetype (measured, not assumed — e.g. web posts 400-900 words vs a separate 2500-3000 rule for full Core drafts).
4. **For deeper systems, add a deep-dive doc** (`DUCK_OS_DEEP_DIVE.md`): protocol/code registry harvested by grepping for code patterns (e.g. `\b(CORE|ACT|LOGS|AWARE|ASSET)[-]\d+\b` + frequency sort), founder storyline, recurring themes, category structure, and which bot each finding serves.
5. **Wire into the content bot**: append to its SOUL.md a "read before writing" section pointing at the style guide, deep-dive, and post corpus. Give the core-coach bot the protocol registry too (it's the internal language the owner speaks).
6. **Verify**: `hermes -p <bot> chat -q "before writing a new tool review: which files do you read, and list the section structure" -Q`. Pass = correct file paths + full section list + correct length norm without hints.

## Pitfalls
- Titles come HTML-escaped (`&#8220;`) — unescape or quotes render as entities.
- WP `content.rendered` mashes tables into one line; acceptable for style study, don't promise table fidelity.
- `<h2>` inside content becomes `##` but the site may also strip real H1s — the post's own title is the H1.
- 10 posts is enough for voice; ~40 reveals registries, product names, and launch timing — worth the extra fetches when the user asks to "know the system better". The FULL corpus additionally reveals persona eras and volume shifts — see references/full-corpus-and-product-sites.md.
