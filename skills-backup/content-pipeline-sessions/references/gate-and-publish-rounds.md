# Gate-and-publish round variants

Companion to SKILL.md lessons 27 / 52 / 54 / 58 — round shapes that deviate from the standard publish-first intake. SKILL.md carries them as pointers only (file hit the curator size ceiling); this file holds the rules.

## 58b. Publish-first with NO production page — the Drafts mirror is the close surface

Lesson 58 assumes the owner already built the Content-DB production page. When the publish paste arrives and a BOTH-DBs title query (Headline + Name, each hit's title-TYPE property read per lesson 58) finds no production page, close by rebuilding the EXISTING Drafts page with the publish text (delete-all + re-append typed blocks per lesson 25), PATCH the title, and flip the Drafts `Status` → `published` — the Drafts mirror serves as the production record until the owner builds the Content page (the weekly Adduckivity sync absorbs it later).

- NEVER create the Content-DB production page yourself — production identity (Platform multi-select, laws/categories, cover image) is owner-authored; the agent's vocabulary is the Drafts-DB `draft`/`published` instrument.
- The WP close still applies unchanged (lesson 56): on the live-URL announce, fetch the page and diff the key sentences against the publish archive before binding `wp_link`. WP headlines may differ from the Notion title while the body matches verbatim — record the divergence, verify the BODY.
- Git staging during the close: `content-study/posts/` is a symlink into `vault/posts` — `git add content-study/posts/<file>` fails with "pathspec … is beyond a symbolic link"; stage the resolved path `content-study/vault/posts/<file>`.
- When the repo carries an uncommitted parallel-session backlog, commit the backlog FIRST and the new pair SECOND so the pair's diff stays readable in history.

## 58c. A critique round can be STYLE-ONLY — grade rhythm with counts, gate on the image

When the owner asks to critique "ด้านสไตล์", run the Benz-voice sim but scope the keys to FORM, not evidence-class. Style keys are MEASURABLE — put the counts in the archive header baselines so the rewrite round grades against numbers, not vibes:

- **Metronome dash** — one rhetorical "A — B" per paragraph is a dead pulse; keep dashes at real pivots (quote, closer) and let other paragraphs end as plain sentences.
- **Negation crutch** — "ไม่ได้X(แต่)Y" density is capped per length; at least two paragraphs must lead with a positive sentence. A post about repetitive reactions that itself repeats one sentence-shape is a self-indicting form.
- **Particle stacking** — ≥3 "ที่/ว่า" layers in one sentence must split into two sentences (a short post pays a clarity tax for every nested clause).
- **Summary echo** — summary bubbles must compress with a NEW angle, not re-quote the body; ≥2 of 3 bubbles must add what the body did not say.

KEEP anchors (best beat line, title pair, closer couplet, verb set) and a **style gate**: abstract-only throughout vs ONE concrete micro-scene (≤2 sentences, never a storytelling paragraph, never a protocol) as the reader's handle. Quote-verify as always.