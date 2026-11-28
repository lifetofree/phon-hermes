# Fold-ledger maintenance — editing content-pipeline/SKILL.md safely

## Layout facts

- `content-pipeline/SKILL.md` stores its fold ledger ABOVE the frontmatter (newest folds first, then `---` frontmatter, then the body). Folds append by PREPENDING at the top.
- The skill indexer takes the file's first line as the description — after any prepend, the listed description in skills_list becomes the topmost fold's text. Expected, not a defect; the real description lives in the frontmatter.
- The SKILL.md is at/over the ~100K character cap — do not plan to grow it. New topical depth goes into a `references/<topic>.md` supporting file; the fold ledger keeps growing by prepending one-line-ish folds only.

## Prepend mechanics (pitfall: header-glue)

Anchor old_string on the TOPMOST fold's full header line (`**(N) name — rule (pair …):`) and re-emit that header verbatim at the end of new_string. A partial anchor (matching only the header prefix) strips the old fold's header and glues its body onto your last new fold — found and repaired once by reading the patch diff; verify every time.

Verify after every prepend:
1. Fold count `**(` before vs after grows by exactly the number of new folds.
2. The topmost TWO fold headers each begin their own line (no glued bodies).
3. The frontmatter `---` block still follows the last old fold.

## Naming conventions

- Fold format: `**(N) name — rule (pair #X round):** evidence → fix → gate`, numbered continuing from the highest existing number. Extends/supersedes links to earlier folds stated explicitly.
- Round archives: `content-study/web-archive/<date>-<slug>-benz-r<N>-<kind>.md`; draft snapshots `…-v<N>.md`. Provenance = pair #, no PR/date-as-content inside the rule text.
