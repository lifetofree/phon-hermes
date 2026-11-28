# Lessons 68–70 — deployment-evidence TECH drafts, evidence-article fact-check, critic-answered gates

Depth file for `content-pipeline-sessions`. SKILL.md points here; the operative wording lives below. Two amendment clauses for existing lessons 32 and 52 sit at the end — merge them into SKILL.md at the next repo touch (the SKILL.md was at its size cap when these were written).

## 68. TECH brief about a system THIS machine runs — the deployment is the primary source

Trigger: the brief asks for a TECH post about infrastructure this machine actually runs (self-hosted stacks, docker services, bot workers). Dig evidence from live artifacts BEFORE drafting — machine-verifiable first-party facts are the post's spine, and vendor prose is a different evidence class:

- One-pass artifact sweep: `docker ps --format` / `docker images --format` (names, created timestamps, sizes), `docker volume ls`, `git log` + `git ls-remote` for bot-authored branches and commits, file mtimes in the app directory, `curl -sI localhost:<port>` for any live-web claim, `tailscale serve status` for exposure claims. Every number in the post must trace to one of these; an untraceable number is a claim, not evidence.
- Fetch the upstream README raw (`raw.githubusercontent.com/<org>/<repo>/main/README.md`) for identity, and enter EVERY vendor positioning sentence reported speech with an attribution tag ("ทีมผู้ทำระบุว่า…") — the product's self-description is a claim about itself, never a fact the post asserts.
- Build a FACT LEDGER in the draft header: each figure plus where it was verified. The critique round grades the ledger, not session memory.
- Secret hygiene: deployment directories keep `.env` beside the compose file — never print, paraphrase, or allude to any value from it; internal-only hostnames (tailnet/VPN) go in the Source prop, never the body; scan the extracted body for token shapes before filing.
- Battery on TECH drafts: `odd codepoints` survivors are DECLARED form-legitimate per class instead of stripped — ASCII commas inside tech lists, `/` inside branch names and term pairs. Eye-audit every pronoun hit with context before writing the header numbers (the counter undercounts compound subjects like เรา+กริยา and overcounts lookalike families like พร้อม), and the header carries the EYE number plus declared FP families — critique rounds grade against the header.
- Sibling guard runs across tool-review lanes: a self-host deployment post and a SaaS product review are different lanes — hold the other lane's product vocabulary at 0 and name the separating axis in the header.

## 69. Evidence-article fact-check recipe: raw fetch everything, check authors, quarantine owner measurements

- Raw-fetch primaries instead of trusting search snippets: publisher full text for open-access papers, PubMed eutils (`esearch` then `efetch rettype=abstract`) for abstracts, Crossref `/works/<doi>` for title/authors/venue. When the extraction backend is search-only, go through urllib in code — and blocked fetches rotate to the remaining outlets of the same result set.
- **Author-surname trap: check the Crossref author list before an institutional-sounding name stands in the text as a source.** A review "by Cochrane" can be a person named Cochrane, not the Cochrane Collaboration — a famous-sounding name quietly inflates authority in exactly the posts whose thesis is evidence rigor.
- Owner-supplied measurements he did not take himself stay reported speech inside his own story ("ตามตัวเลขที่สถานที่แจ้งไว้") — drop the attribution clause and the unmeasured number reads as his measurement.
- An owner real-world case in a science explainer is a LIVE EXAMPLE of the evidence boundary, not a confirming witness: make the gap between his protocol and the studied protocol the point (it shows protocols are not standardized), and class his subjective outcome as the same subjective measure the research itself used — never as proof the mechanism works.

## 70. A gate the critic answers himself — the forwarded paste is the adoption

When a critique closes with a gate AND the critic's own pick of an axis ("Benz-DNA เลือก B เป็นแกนหลัก"), and the owner forwards the paste without contradiction, that forward IS the adoption per the one-paste pattern — do not wait for a separate gate answer. Archive the critique with the gate marked in-paste; keys grade the chosen axis; the un-chosen axes park exactly where the critique assigns them (opener beat, limitation layer) — never as competing theses. Honor an "add no more information" order if present: the round becomes reorder-and-sharpen only, and the publish keys state that ceiling explicitly.

## Operative extensions to existing lessons (merge into SKILL.md at next repo touch)

- **Lesson 32 (hashtag tail) — mechanism clause:** put the tail assert inside the filing CODE itself (build payload → assert tail → POST), not in prose — an assert that lives only in a checklist gets skipped, and the read-back is the wrong place to first meet it. Inserting a missed beat on a live page: PATCH /blocks/{page_id}/children with `after` = the id of the last content block and the beat in the JSON body; appending without `after` lands the beat AFTER the hashtags and fails the shape it was fixing.
- **Lesson 52 (sim-vs-real) — round-5 miss class:** grade the TITLE as its own claim — hedge verb, measured scope, absolute-register words; a title may quote the paper's own conclusion and still overreach at head level ("really/ได้จริง" needs the hedged spine sentence standing behind it, and "no one has proven" is absolute-register where the evidence class says "little evidence"). And two review populations fused by a time-bridge ("a decade later") = different context — bridge by context ("another setting where the method is used"), not by chronology.
