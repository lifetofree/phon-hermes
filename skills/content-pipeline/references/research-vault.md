# Research & Content Vault — layout map (post-2026-11 restructure)

Single-source-of-truth map for where content/research files live, what generates what, and how the Obsidian graph stays connected. SKILL.md carries the standing rules; this file carries the full map.

## Directory tree (real files vs symlinks)

```
~/hermes-agent/
  research/                      ← RESEARCH VAULT (real files)
    README.md  index.md          ← vault docs + MOC
    *-research.md                ← topic research (21+ files; front-matter below)
    books/
      catalog.md                 ← GENERATED from Notion "Books Library" DB (never hand-edit)
      .chapters-cache.json       ← gitignored cache (keyed by last_edited_time)
      <slug>/                    ← per-book folder — HAND-CREATED only when a book goes active
        book.md  quotes.md  notes.md
  content-study/
    vault/                       ← CONTENT VAULT (Obsidian graph)
      index.md                   ← MOC (GENERATED)
      pairs/                     ← pair-0NN.md files (GENERATED, hash-gated)
      tags/                      ← tag index nodes (GENERATED from hashtags)
      lessons/ events/ branches/ families/   ← hand-curated node types
      posts/                     ← real draft files (moved in)
      web-archive/               ← real publish/critique archives (moved in)
      research/                  ← symlink → ../../research
    posts/  web-archive/         ← symlinks → vault/… (legacy entry points, all scripts keep working)
  skills/content-pipeline/
    references/*-research.md     ← symlinks → ~/hermes-agent/research/ (skill's own references stay stable)
    scripts/
      generate_vault.py          ← regenerates vault pairs/ + tags/ + index.md from index.json (idempotent, stale-cleanup)
      sync_books_library.py      ← syncs Notion Books Library → research/books/catalog.md
      sync_wp_posts.py           ← (pre-existing) WP archive sync, path-unaffected
      draft_battery.py           ← (pre-existing) draft battery
```

Rule: a real file exists in exactly ONE place; every other path to it is a symlink. Never "fix" a symlink by replacing it with a copy.

## Research file front-matter (canonical shape)

```markdown
---
type: research
topic: <human topic label>
kind: TECH|book|philosophy
used_by: [[pair-049]] [[pair-061]]
---
```

- `used_by` is space-separated wiki-links (no commas — Obsidian treats each token as a link).
- New research → `~/hermes-agent/research/<slug>-research.md`; wire the content side by adding one key to `RESEARCH_LINKS` in generate_vault.py.

## Node-type contract (content vault)

| type | dir | created by | generator behavior |
|---|---|---|---|
| pair | pairs/ | generator (from index.json) | create/refresh by hash; deletes stale files |
| tag | tags/ | generator (hashtag scan of archives) | create/refresh by hash; deletes stale |
| research | (outside vault) | hand (front-matter + used_by) | untouched; listed in MOC |
| branch | branches/ | hand (status: open/stock/graduated/dead) | untouched; open/stock listed in MOC |
| family | families/ | hand (≥2 pairs sharing a chain) | untouched; listed in MOC |
| lesson | lessons/ | hand (recurring critique pattern, ≥2 occurrences) | untouched; listed in MOC |
| event | events/ | hand (ONE real event spawning ≥2 works) | untouched; listed in MOC |

Adding a new node type = decide generated (needs data source + hash + stale cleanup) vs curated (hand + MOC section), add one row to this table, add one MOC block to the generator.

## Books flow

1. Notion "Books Library" DB (id 2ffdf8d8-8d8c-8096-934a-c05c3b5d93a0) = catalog of record (Title/Author/Status ⏳⬜✅/Energy Group G.1-G.3+Boss/Tags).
2. `sync_books_library.py` → `research/books/catalog.md`, grouped by status then energy, chapters indented under each book.
3. Chapter extraction: `child_database` titled *chapter* → its row titles (skip template rows); fallback `heading_3` matching `chapter\s*#?\s*\d+`; strip emoji prefix and `*** Loc …` annotations. No chapters found → leave blank (never invent).
4. Cache: `.chapters-cache.json` keyed by page `last_edited_time` — re-sync queries only changed books (full sweep ≈ 253 blocks + 0.2s/page throttle).
5. When a book goes ACTIVE (reading/quote extraction): hand-create `books/<slug>/{book.md,quotes.md,notes.md}`. **Quote gate: a post may cite a book quote only after the quote (with source + location) lands in that book's quotes.md.** This extends the corpus quote-provenance rule (#52 precedent) — a quote with no verified single source is never cited, and the quotes.md file is where verification lives.

## Obsidian

- Open the vault at repo root `~/hermes-agent/`. Obsidian does not follow symlinks under a nested vault root — opening `content-study/vault` alone hides research/ entirely (graph shows content side only). At repo root, content vault + research vault render as one graph and all `[[wiki-links]]` (pair↔research, lessons→pairs, tags→pairs) resolve by bare filename.
- Filter `node_modules`/dist paths in graph settings; group by `path:` for color layers.
