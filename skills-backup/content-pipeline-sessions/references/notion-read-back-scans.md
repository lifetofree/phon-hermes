# Notion read-back scans — tables and empty-block counting

Rules for verifying Notion pages whose bodies carry tables, and for counting empty blocks correctly. Companion to lesson 15 (create mechanics) in this skill; canonical transport contract lives in `content-notion-ops`.

## Markdown-param CREATE converts pipe-tables natively

The top-level `markdown` body on POST /v1/pages renders `|`-tables into a proper `table` block + `table_row` children — no typed-block recipe is needed on the create path. The typed-block table recipe (lesson 15) still governs REBUILD/append paths where blocks are built by hand.

Verify a table by GETting the table block's OWN children (`GET /v1/blocks/{table_id}/children`) and reading `table_row.cells` per row — cell text lives in `cells` (a list of lists of rich_text), not in child blocks; a flat page-level text scan misses it and reports table facts MISSING.

## Scope the empty-block check to text-carrying types

Count empty blocks only among `paragraph` and `quote`. `table`, `divider`, and other non-rich_text block types carry no rich_text BY DESIGN — a flat scan that treats every block with zero rich_text as an "empty" flags valid structure blocks as defects and starts a ghost-defect hunt. On an "empty block" signal: re-scan grouped by block type first; delete nothing on the flat-scan signal alone.

## Number-unit discipline for read-back claims (companion to main-skill fold on number-unit fidelity)

When a draft restates a machine count (a DB column's value), the unit word must sit adjacent to the number in the sentence, and the (number, unit) pair is what later rounds grade — a rewrite that re-attaches the same number to a different noun (tools → bots → pages) is a factual FAIL even though the digits never changed. When a critique asks "what does N mean", re-derive the answer by re-running the source query in code; an answer negotiated in conversation is not evidence.