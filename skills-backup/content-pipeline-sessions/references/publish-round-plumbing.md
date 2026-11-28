# Publish-round plumbing lessons (59–63b, relocated from SKILL.md)

## 59. Consumption-unit claims: attribute the unit to its system or strip the family (pair #103 zcode)

A TECH hands-on draft that mentions consumption/pricing units must use the VENDOR'S OWN unit vocabulary — when two systems in one ecosystem count differently (GLM counts tokens; AutoClaw counts credits), a line carrying either unit unattributed reads as cost information and misleads. Owner strip-orders cascade within one round: removing one priced/unit claim typically extends to the whole unit family (ราคา → credits → token → โควตา) — strip the FAMILY on the first order, scan family-wide in file AND Notion read-back, and keep the removed figures in the draft header only (re-verify against the vendor at ship time). If the unit story cannot be attributed cleanly, the claim dies rather than picking a unit by guesswork — a body with zero unit lines is a legal TECH publish (main item 308's data-ceiling rule extends to pricing/units).

## 60. Page-title PATCH accepts the `title` alias; read-back keys properties by their REAL name (pair #103 zcode)

PATCH /v1/pages/{id} accepts a literal `"title"` property key (`{"properties":{"title":{"title":[...]}}}`) and lands on the page's title property regardless of its schema name. The GET read-back does NOT: `properties` is keyed by the REAL property name (`Name` on the Drafts DB), so reading `pg["properties"]["title"]` KeyErrors even though the write succeeded. Rule: write may use the alias; read-back must find the title-typed property by TYPE (`next(k for k,v in properties.items() if v["type"]=="title")`) — lesson 46's branch-on-type rule extends from DB rows to page property dicts. And never trust a `-o /dev/null` PATCH: confirm the landed title by GET, not by the absence of a curl error.

## 61. Owner asks for real details on a filed draft = APPEND-ONLY update to the SAME page (pair #105)

When the owner asks for verified details behind a filed draft's claims ("ขอรายละเอียดจริงมาด้วย…research มาให้หน่อย"), the deliverable is a section appended to the existing Notion page — never a second page, never a body rewrite: (a) the details' source is the research file (lesson 42's node; body format in lesson 62), and the appended section mirrors it — one block per item: bold lead-in naming the thing + numbers, then the catch; (b) IDEMPOTENCY GUARD — GET the page's children and scan for the section's marker text BEFORE appending; a blind retry duplicates the whole block run; (c) append-only means existing body blocks stay untouched — PATCH /v1/blocks/{page_id}/children with NO `after` appends at end; lesson 25's delete+rebuild is for re-spines, not for adding a section; (d) rich_text bold mechanics — canonical copy is the main skill's item (366): bold goes in `annotations` (top-level `bold: true` 400s), and the read-back verifier must check `annotations.bold`, not `bold` — a wrong-key check prints 0/0 against a write that succeeded. Side rule from the same round: a draft header's pair number is a CLAIM — verify it against the index.json entry before quoting it (a #104 vs #105 mismatch shipped once) and fix the header in the same commit.

## 62. Research-file body format for roundup-source briefs — in references

The full recipe (facts → per-item catches → parked → SOURCES, with every roundup number verified against its PRIMARY source before it sets the draft's claim ceiling) lives in `references/gate-rounds-and-research-recipes.md` together with the gate-round lessons 65-69 (gate-follow rounds, compound owner intake, publish-first variant without a production page, STATE-vs-disk reconciliation, heading-anchored patch replacement).

## 63. Hand-formatted repo JSON (index.json): targeted patch only

A json.dump round-trip on `content-study/index.json` re-indents EVERY line and buries the real change — edit with a targeted find/replace on the single entry, never commit the re-indent (full lesson: `references/repo-tooling-plumbing.md`).

## 63b. Over-100k tool output spills to a file — process the spill, never re-request

A skill_view (or any tool) returning >100k chars lands as a JSON blob with the full text saved under `~/.hermes/cache/spillover/` — re-calling the same tool re-pays the whole cost, so read the spill file instead. When the target is a SKILL.md near the limit, expect the in-band preview to be a truncation artifact and go to the spill file for the true body. Keep THIS skill lean by moving topic-cluster lessons into `references/` (this file and gate-rounds-and-research-recipes.md are the pattern).
