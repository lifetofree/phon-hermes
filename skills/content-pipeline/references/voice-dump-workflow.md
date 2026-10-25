# Voice-dump intake — worked classification

Depth for skill item 226. The owner streams half-formed ideas by speech-to-text mid-session; the agent's job is to CAPTURE, CLASS, and GATE — not to draft on the spot.

## Procedure

1. **Archive raw, verbatim, same session** → `content-study/voice-dumps/<date>-voice-dump-<topic>.md`. Structure: `## Raw (verbatim)` (quote blocks, no cleanup — transcription artifacts like "ดัตตา" for Data or "speed to text" for speech-to-text are part of the record), `## Parse` (beats extracted + classification per beat), `## Status` (what is pending and from whom).
2. **Parse into beats.** One voice dump usually carries 2-3 separate things: a recalled scene, a definition the owner improvises, a candidate example, a workflow instruction ("ลองเอาไปกรุบดูละกัน"). Split them — they class differently.
3. **Class each beat, then report the classing back before writing:**
   - **Own case** — an event the owner lived (app trial, work moment). Proceed toward drafting, but confirm scope via clarify when the draft needs specifics the dump lacks.
   - **Parked branch** — the beat collides with an existing post (scene already owned, definition = existing thesis). Park with the collision named; do not summarize it into the current post.
   - **Candidate** — a product/example the owner mentions as a possible case. Verify from primary sources BEFORE proposing; propose 1-3 with receipts, let the owner pick.
   - **Instruction** — workflow meta ("เก็บไว้ reverse engineer"). Becomes procedure, not content.
4. **Gate:** no prose is written until an owner-confirmed case exists. A generic paraphrase of the dump ("someone tries a free app...") is NOT a case — if the owner then supplies a real one (the app they are actually trialing), archive the generic v1 and re-spine on the real case rather than editing v1 in place.

## Case upgrade via primary sources

When the owner names a concrete product they use, the generic case becomes verifiable:

- Fetch the official pricing page AND the official docs/help article for the specific mechanism the post needs (quota, trial, exemption). Both, not one — pricing pages carry prices, docs carry the mechanism.
- Date every receipt in the draft header ("ตรวจ <date>").
- If the vendor's own docs state a metering rule that CONFIRMS the post's thesis (e.g. "active trials are exempt from counting" when the thesis is "the decision-relevant number starts counting when the free period ends"), promote it into the spine — the product demonstrating the thesis itself is stronger than any analogy.
- Keep owner-attested facts (what the owner saw, did, decided) separate from vendor facts in the header; the body may only claim what each source supports.

## Pitfalls

- Do NOT treat a fast voice fragment as a decision to write now — the speed of the medium hides that it is usually material for chewing, not a brief. The archive-first step exists to make the deferral safe.
- Do NOT clean up transcription artifacts when archiving — the raw text is the evidence; the parse section is where interpretation lives.
- A generic-case draft written before the real case arrives will be thrown away — cheap to archive, expensive to edit. Prefer waiting one turn for the owner to name the concrete case.
