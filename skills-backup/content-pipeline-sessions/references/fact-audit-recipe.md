# Fact-audit recipe — grounding a critic's unverified-fact checklist (provenance: pair #OpenBot-copilotkit r1; extends content-critique-cycle OC2)

When the critique declares facts unverified and ships an itemized pre-publish checklist ("ตรวจก่อนเผยแพร่: …"), the agent runs the whole checklist against official sources — the round's engineering half, not an optional extra. The audit may surface findings the critic did NOT catch (draft written days earlier, official docs have flipped); those go to the owner as decision items, never silent fixes.

## Output shape

Table F1..Fn in the round archive: **claim as drafted | verdict | source URL**. Verdicts: ตรง · ตรงแต่มีเงื่อนไข · ครึ่งจริง · ผิด/ผิดชื่อ · เกินจริง · ล้าสมัย · ตรวจยืนยันไม่ได้. Quote the official line verbatim next to the drafted line — never paraphrase the source into the verdict. Every source carries its as-of date.

## Source priority (fastest authoritative first)

1. **Vendor blog FAQ / webinar recap** — a release or webinar recap post usually carries an explicit FAQ answering most checklist items verbatim, with watch timestamps ("How much does it cost?", "Is it X-licensed?", "How is Y isolated?"). Search for it before raw specs; it also establishes the artifact's true genre (webinar vs research paper) for the source-provenance fix.
2. **GitHub README** — fetch the raw file directly (`raw.githubusercontent.com/<org>/<repo>/main/README.md` via urllib in execute_code) instead of scraping the HTML page. It carries license scope, deploy requirements (exact node counts/sizes), installer-certification claims, and architecture wording you can quote.
3. **Official pricing page** — fetch + strip HTML with regex. Record exact plan wording: ceiling pricing is usually "up to $X" (pay-as-you-go), and free tiers carry run quotas or conditions the draft will have flattened to just "free".
4. **Legal identity of the developer** — App Store listing seller field + the product's privacy policy (legal entity, country, registry number). A GitHub org handle is NOT the developer name; a draft naming the org as developer is a real finding. Authorship claims ("พัฒนาร่วมกับ X") check against the protocol/product's own repo and landing page authorship language ("creators of", "the protocol we wrote") — partnership ≠ co-development.

## Mechanics

- **Cross-piece claims verify against the sibling pages themselves**, not the critique's word: fetch the published sibling's Notion page; read tables via `table_row.cells` (comparison-table quotes live in cells, not paragraphs). Newest-truth-wins: if the new piece matches the official docs and the published sibling doesn't, the sibling is the fix target.
- **"Still true today" facts** (installer certification, status flags, versions, pricing) flip within days — re-verify on publish day, not draft day; record each source's as-of date so the flip is visible.
- **Unverifiable with current sources** → mark it as such and hand the decision to the owner. Do not confirm, do not silently cut.
- Run the audit BEFORE reporting to the owner, so the reply answers the critic's checklist with verdicts instead of echoing questions.
