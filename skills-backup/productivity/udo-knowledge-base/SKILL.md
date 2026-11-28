---
name: udo-knowledge-base
description: "Use when working in ~/hermes-agent or the Notion KB."
---

# UDO Knowledge Base (Notion)

Every session involving this repo or the KB:

1. READ `~/hermes-agent/AGENT.md` (canonical copy at `scripts/AGENT.md`) — UDO persona, Notion KB CRUD flows, schema, safety rules.
2. READ `~/hermes-agent/STATE.md` — current KB state, open tasks, recent activity.
3. Search KB before answering (via Notion API, token in `~/hermes-agent/.env` as NOTION_TOKEN — never print it).
4. Confirm with user before Create/Update/Delete on Notion.
5. Update STATE.md when state changes or a session ends.

## Key facts
- Repo: github.com/lifetofree/phon-hermes → ~/hermes-agent, branch main.
- KB DB: "Knowledge Base", ID 3c9df8d8-8d8c-81ac-ba5e-fa129e493638, parent page "Hermes agents" (3c7df8d8-8d8c-801c-87f9-e845700178af).
- Schema: Title, Summary, Category (tech/life/work/reference), Tags, Source, Created, Updated, Status (active/archived/deprecated).
- Known inconsistency: crud scripts expect AGENT.md at repo root; actual location is scripts/AGENT.md.
