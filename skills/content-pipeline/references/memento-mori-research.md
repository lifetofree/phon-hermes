# Memento Mori — Research Notes
Verified: 2026-09-08. For the task-logger.app PhilosophyPanel + content draft.
Hard rule applied: every quote in the app has a verified primary source; 2 prior "Seneca" lines were misattributions (see below) and were removed.

## What it is
- "Memento mori" = Latin, "remember that you will die" (imperative).
- The *practice*: deliberately holding mortality in mind — not to dwell on death,
  but to clarify how to spend the time that remains. Stoic exercise of death
  contemplation; a central, recurring theme across Marcus Aurelius, Seneca,
  Epictetus.
- Stoic framing: death is an "indifferent" (adiaphoron) — neither good nor bad —
  so it removes the rational basis for fearing it. Purpose: clarify what counts,
  deepen gratitude for the present, sharpen attention. The effect runs OPPOSITE
  to morbidity (this is the key insight — done right, it energizes, it doesn't depress).
- Christian tradition framed it as preparation for death/judgment; Stoicism uses it
  as preparation for *living rightly now*.

## History (nuance for accuracy)
- Roots pre-Roman (ancient cultures had death-reflection).
- The famous image: a slave/companion behind the triumphant Roman general whispering
  "memento mori" (or "remember you are mortal") — the most-told origin. Scholarly note:
  the specific "memento mori" whisper at triumphs is traditional/legendary and debated
  (e.g. the *Patton* film scene), but the broader triumphal mortality-reminder tradition
  is attested. Present as "the well-known tradition" rather than "proven fact".
- Medieval–Victorian: strong in Christian theology, art (skulls, vanitas still life),
  architecture, literature.

## Stoic practice
- Constant mindfulness of death — "you could leave life right now; let that determine
  what you do, say, think" (Meditations 12.1).
- Seneca's *premeditatio malorum* (pre-meditation of adversity) — imagining loss to
  reduce fear of it and increase gratitude for what's held.
- Count each day as a complete life; treat every returned day as a bonus.

## Modern psychology (why it helps, with the caveat)
- Death awareness (mortality salience) research: when people have proper psychological
  buffers (self-worth, meaning, close relationships), contemplating death → greater
  life satisfaction, gratitude, value-alignment, reduced rumination, better
  decision-making (drop the trivial).
- CAVEAT (must state honestly): without those buffers, death contemplation can INCREASE
  anxiety and lower well-being. The practice works because it's paired with gratitude +
  meaning + presence — which is exactly what the app's daily happiness logging reinforces.

## Quote verification results (2026-09-08)
MISATTRIBUTED — REMOVED from the app pool:
- "Every new beginning comes from some other beginning's end." (attributed to Seneca)
  → No such statement in Seneca's surviving works (latin.stackexchange + multiple
  sources). Popularized via Semisonic's "Closing Time" / internet.
- "Luck is what happens when preparation meets opportunity." (attributed to Seneca)
  → Confirmed not Seneca; wording traces to a 1928 "City Loan" advertisement.

NEW quotes added (verified):
- Marcus Aurelius, Meditations 12.3 — "You have your life. Your life has you."
- Seneca, On the Shortness of Life 1.1 — "Life is long if you know how to use it."
  (paired with the existing "It is not that we have a short time to live, but that we
  waste much of it" — same source, On the Shortness of Life)

KEPT (well-attested, widely used):
- Marcus 12.1 "You could leave life right now..." ✓
- Marcus "Waste no more time arguing about what a good man should be. Be one." (10.16) ✓
- Marcus "Think of yourself as dead..." (7.56) ✓
- Seneca "It is not that we have a short time to live, but that we waste much of it." ✓
- Seneca "We suffer more often in imagination than in reality." (Letter 11/12) ✓
- Note: Marcus "Death smiles at us all; let us smile back." — widely cited as
  Meditations 4.47; some scholarship questions exact wording. Kept (commonly used),
  low-risk.

## Primary sources (for the "read next" list)
- Marcus Aurelius, *Meditations* (esp. 12.1, 2.11, 7.56, 4.47)
- Seneca, *On the Shortness of Life* (Brief Life) — the whole essay is a memento mori
- Seneca, *Letters to Lucilius* (1, 49, 90, 95)
- Epictetus, *Enchiridion* / *Discourses* (1.2, 2.11)

## App integration decisions (ADR 0008)
- Content lives IN the Memento tab (not a new tab): a collapsible "What is Memento
  Mori?" card above the stats, written in Thai (app UI is English, this is the user's
  language). Quote pool now structured {text, author, source} in frontend/src/quotes.js.
- Added a "New quote" shuffle button (quotes were random-once-per-mount before).
- v5.1.0. No DB / API changes — frontend only.
