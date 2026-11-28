# Gate rounds & research recipes (session lessons 62, 65-70)

Depth for the content-pipeline session flow: research-file recipe for roundup briefs, and the rules governing critique-gate rounds, compound owner messages, publish-first variants, repo-state discovery, and heading-anchored patches.

## 62. Research-file body format for roundup-source briefs: facts → catches → parked → SOURCES, with per-number primary cross-check

When a brief cites a ROUNDUP article (a listicle claiming "X beats Y"), the research file's body follows one shape: verified facts (each claim with its source) → per-item catches (what each win does NOT prove: language scope, size-class-only claims, stale comparators, ranking drift, license limits) → parked material (unused raw data held for later critique rounds) → SOURCES (primary first, secondaries labeled). The cross-check rule that sets the draft's claim ceiling: verify EVERY number the roundup cites against the PRIMARY source (model card, paper, official blog) — roundups carry small discrepancies (their table vs the card), stale comparators (a 2023-era model inside a 2026 article), and stale rankings ("#1 at launch" is no longer #1); the catch lines are what the critique round probes, so they must exist in the file even when the draft never uses them.

## 65. Gate-follow round — the answer follows the critic, and the publish rides in the same message

When a critique's gate is answered with the option the critic RECOMMENDED (after a run of overrides is on record) and the publish text arrives with it, no rewrite round exists: grade the publish against the critique's publish-keys (PASS/NOTE/FAIL), log the gate answer into the critique archive, and close the pair in one pass. Record the gate-follow in the same ledger that carries the override precedents — sovereignty means considered choice in BOTH directions, and a ledger that only lists overrides misrepresents the pattern as contrarianism.

## 66. Compound owner message — critique + gate answer + publish + a directive in one intake

One owner message can carry the critique text, the gate answer, the publish version, and a meta-order ("learn from this critique for our writing skill") — treat it as ONE intake, not four rounds: (a) archive each artifact verbatim as its own file, (b) quote-verify the critique against the on-disk draft it reviewed (the critic quotes the CURRENT draft, not the paste), (c) grade the publish against the critique's own keys, (d) execute the meta-order in the SAME session WITHOUT a separate fold-approval ask — the directive inside the compound message IS the fold approval (contrast: a publish-only paste gets folds PROPOSED and waits). Analysis-only rules still protect the Notion production surface.

## 67. Publish-first variant — no production page exists: the Drafts page becomes the production surface

Lesson 58 assumes the owner already built the Content DB page; when a title query of BOTH databases returns no production row, do not leave the pair half-open: rebuild the DRAFTS page with the publish text (delete-all + re-append on the same page id, retitle, flip its Status to published) so the live body exists somewhere queryable, never create the production page yourself, and record the variant plus the Content-DB absence in index.json/pair-history — the weekly Content-DB sync absorbs the page when the owner creates it later, and the WP URL still binds on announcement (lesson 56).

## 68. Repo state discovery at round start — STATE.md lags the disk

STATE.md records what the LAST session believed; `git status --short` and file mtimes record what IS. Reconcile before acting on any pair — a draft believed to be "awaiting critique" may already be a rewritten version with its Notion page retitled, all uncommitted. Commit hygiene: inherited uncommitted work goes in its OWN commit containing only that work; never mix an inherited backlog into a commit carrying this round's new files — messages then describe what actually changed, and a revert/audit can take one round back without dragging the other.

## 69. Patch anchored on a heading replaces the heading — re-anchor, then read back

A targeted patch whose old_string IS a section heading and whose new_string prepends new content before re-stating the heading silently REPLACES the heading — the fuzzy matcher consumes the anchor, the section below loses its title, and the diff still reports success. When inserting a section adjacent to an existing one, repeat the existing heading VERBATIM at the end of new_string (or anchor on heading + first body line), and read back the touched region after patching shared living files — the same miss twice in one session means the rule, not the luck.

## 70. Dated-newsletter brief — verify the brief's own link and sweep for later developments before drafting

When the brief quotes a dated newsletter/digest line ("[Tech]" items from a weekly archive), the research file's ต้นฉบับ section records the brief link, and the verify chain runs: (a) FETCH the brief's own URL and confirm its text matches the brief's framing — the digest line is an idea brief, never evidence; (b) search the topic's LATER developments before choosing the lens — a launch can already have a block/ban/sequel by draft day, and that continuation usually belongs in the draft as a bounded catch line (it is what the real critique round probes); (c) if the event is days-to-months old, the draft opens with the explicit event DATE — freshness words (ล่าสุด/เมื่อวาน) over an old event are a factual error even when every detail is right. Canonical home is the content-research skill's research standards (repo-backed — move this lesson there at the next repo touch; until then it lives here).

