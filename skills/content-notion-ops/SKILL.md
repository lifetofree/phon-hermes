---
name: content-notion-ops
version: 1.0.0
author: KhaoKlong (Hermes)
license: internal
metadata:
  hermes:
    tags: [adduckivity, notion, publish, api]
    related_skills: [content-pipeline, content-critique-cycle]
description: "Use when shipping adduckivity pages into Notion: create, patch, verify."
---

# Content Notion Ops (adduckivity)

## When to Use

Load this when the job is the Notion leg of an adduckivity pair: creating draft pages, patching/rewriting existing ones, full-body rebuilds, read-back verification, or debugging a Notion API error. Drafting rules belong to `content-pipeline`; critique rounds belong to `content-critique-cycle`. This skill owns the transport layer and its verification contract.

## Canonical tooling

- `scripts/markdown_to_blocks.py` — the markdown → blocks converter (segment-level inline bold; whole-line parsers leak raw `**` — never hand-roll a parser per session again). `markdown_to_blocks(raw)` returns `(name, blocks, leaks)`; `leaks` MUST be 0 before shipping. Handles the full adduckivity dialect: H1→title, `##`/`###`→headings, `>`→quote, `-`→bullets, fences→code, `.` beat paragraphs, `---`→divider (dropped if it would precede the first block).
- `scripts/rebuild_page.py <md> <page_id> --forbidden w1,w2 --marker "keep line" --suffix " — pair #N"` — the standard rebuild loop: title PATCH → delete-all → insert (≤100/request) → read-back verify (blocks / empty 0 / raw `**` 0 / forbidden 0 / markers PASS) → title read-back. Use it instead of ad-hoc curl chains.
- Legacy per-pair scripts in `content-pipeline/scripts/` still work, but new rounds should call these two.

## Credentials & environment

- Token: `NOTION_API_KEY` in `~/.hermes/.env` (Hermes home env — NOT the repo .env, which is often absent). In `execute_code` the kernel does NOT inherit shell-sourced env vars: read the env file inside the process and pass the token explicitly to each `curl`. Never print it.
- Payloads: write JSON to a temp file and `curl -d @file` — never shell-quote a large Thai/English body. ALWAYS pass `-H 'Content-Type: application/json'` (without it, curl form-encodes and Notion returns a misleading 400 about `parent`), and ALWAYS pass `-X PATCH` explicitly (`-d` alone defaults to POST → 400 `invalid_request_url` that reads like a bad page ID).

## Databases (workspace: adduckivity)

- Content Drafts DB: `3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520` — props Name (title), Topic (rich), Status (select: `draft`/`rewritten`/`sent-khao-klong`/`published`), Date, Platform (multi_select: FB, IG, Threads, X, WordPress, Shopee affiliate, general), Source (rich). Select/multi_select values must match exactly — unknown option names return 200 but silently pollute the option list.
- Content DB (published CNT): `303df8d8-8d8c-8013-baa1-c2fd25e7c9a5` — props incl. ContentID, Slug, FileName, Headline, Status.
- Date prop is date-typed: send `{"date": {"start": "YYYY-MM-DD"}}` — the `{year, month, day}` shape 400s.
- Title prop reads back under key `Name` (payload key `title` is accepted on writes; `properties["title"]` on GET is empty).

## Page lifecycle

- **Create draft:** `POST /v1/pages` with `parent: {database_id}`, typed properties, and a `markdown` body param (markdown-in-payload is CREATE-only — PATCH rejects it). Move the H1 into `Name` and send only the remainder. Strip the HTML comment FIRST (unanchored `re.sub(r"<!--.*?-->\s*", "", raw, flags=re.S)` — the comment is not always at byte 0), assert no `<!--` survives, THEN partition the title by line split (never regex — Thai/English titles contain spaces and a space in the stop class truncates the Name to a fragment). Do NOT send `children` alongside `markdown` (400). Create can take ~200s for long bodies — set generous timeouts; before retrying an unclear create, `POST /v1/search` the exact title (blind retry duplicates).
- **Patch in place (rewrite):** PATCH properties first (`PATCH /v1/pages/{id}`), then body via `PATCH /v1/pages/{id}/markdown` `{"type":"replace_content","replace_content":{"new_str":...,"old_str":""}}`. Two-step is mandatory — a props PATCH rejects a `markdown` param. Before ANY create, check `index.json` by slug: an untracked posts/ file does NOT mean unfiled (pair #49 paid a duplicate page).
- **Full-body rebuild (publish/critique rounds):** the delete-and-rebuild path — list children with `has_more` pagination, `DELETE /v1/blocks/{block_id}` individually (bulk delete 400s in this workspace), then insert ≤100 blocks per request. `scripts/rebuild_page.py` does all of it. If block-append 400s on a pinned API version, create a fresh page and archive the old one (`PATCH {"archived": true}` — DELETE on pages 400s here; archive IS the delete path).
- **Block-level fixes:** `PATCH /v1/blocks/{block_id}` changes heading LEVEL only (heading_1↔heading_2), never KIND — a paragraph can't be PATCHed into a heading (pair #51); the repair is a full markdown replace. `PATCH /v1/blocks/{page_id}/children` only APPENDS — no insert-position parameter; placing a block near the top requires a full body replace.

## Read-back verification contract

A Notion write is NOT done when the API returns 200 — it is done when the read-back passes:

1. `GET /v1/pages/{id}` → Name/Status/Topic read from PROPERTIES (a missing title is a property miss, not a body miss).
2. `GET /v1/blocks/{id}/children` (paginate) → block count, empty paragraphs 0, raw `**` 0, forbidden words 0 (CUT list, secrets, prices), keep-markers PASS, heading TYPES verified (markdown replace does not guarantee heading types).
3. Tail shape: `[..., '.', '#Adduckivity ...']` (beat dot before hashtags).

Never reconstruct page IDs from truncated prints (a shortened ID 404s on PATCH and sends you debugging the wrong thing) — carry the full `id` from the JSON response. Write the page URL into index.json FROM the API response (`entry['link'] = resp['url']`), never hand-typed.

## Error triage (observed in this workspace)

- 400 `invalid_request_url` on PATCH → usually a missing `-X PATCH` (POST defaulted) or a truncated page ID — check transport before suspecting the token.
- 400 `Provide a parent.page_id or parent.database_id` with a valid payload → missing JSON content-type header (curl form-encoded the body).
- 401 → token expired; re-verify from `~/.hermes/.env`, ask the owner if still failing (it has 401'd transiently before and recovered).
- `object_not_found` on a "valid-looking" ID → truncated ID or archived page.
- Local DNS down → the request never leaves (curl error 6, `%{http_code}` = 000): resolve via DoH (`https://1.1.1.1/dns-json?name=api.notion.com&type=A`) and pass `--resolve api.notion.com:443:<IP>`, re-resolving per call.
