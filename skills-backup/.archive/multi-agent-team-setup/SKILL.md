---
name: multi-agent-team-setup
description: "Build role-divided Hermes agent teams from Gem/GPT prompts."
---

# Multi-Agent Team Setup

Use when the user wants a persistent team of agents split by role — typically a one-person business (OPB) delegating coach/core, content, sales, research, admin/KB. Converts existing AI-assistant prompts (Google Gems, Custom GPTs, system prompts) into Hermes profiles.

## Workflow (validated)

1. **Interview before building.** Ask (via clarify): what the business is, which functions to delegate, model per bot, CLI vs desktop. Multi-select for responsibilities. If the clarify times out or the user answers partially, proceed with the answered parts and ask the rest conversationally — do not stall.
2. **Collect source material FIRST.** If the user already has AI-assistant prompts or master-data files, wait for ALL of them before creating anything. They may paste files mid-task (delivered as paste paths under ~/.hermes/pastes/ — read them). Creating profiles before the source material arrives means rewriting SOUL.md from scratch later.
3. **Centralize knowledge — inside the git-synced repo.** Copy all pasted knowledge files to a task folder under the user's backup repo (this user: `~/hermes-agent/<task>/`, e.g. `~/hermes-agent/duck-os/`): master instruction file, core-system/frameworks file, master data, libraries. Every profile's SOUL.md points to this dir as Single Source of Truth — never duplicate content into each profile. The user's standing rule: file-based work lives in `~/hermes-agent/`, new folders may be created per task, and everything is committed + pushed to their GitHub repo for backup. Do the initial commit/push yourself (gh is authenticated).
4. **Create profiles:** `hermes profile create <name> --clone --description "<role>"` for each. `--clone` copies config.yaml/.env/credentials from the active profile so bots work immediately with the same model/keys. Loop over names in one shell command; verify with `hermes profile list`.
5. **Write SOUL.md per profile** at ~/.hermes/profiles/<name>/SOUL.md. Distill — do not paste the whole source instruction into every bot. Each SOUL.md: identity/role, personality + tone rules (exact words allowed/forbidden), which sections of the shared knowledge files apply, routing rules, scope limits (e.g. draft-only, never posts on its own), slash commands if the source system had them.
6. **Verify each bot**: `hermes -p <name> chat -q "introduce yourself in 2 lines: name, role, first rule you follow" -Q`. Persona (pronouns, tone markers like Thai 'คับ/คร้าบ') must show up in the reply. Fix SOUL.md and re-test if a bot answers generically. If a verification question is answered with rules instead of the asked artifact (e.g. asked for a structure, got a rules list), re-ask more specifically before concluding the SOUL.md is wrong.
7. **Voice analysis for the content bot (when the user publishes).** If the user has a WordPress site, pull their real posts via the WP REST API and distill a writing style guide the content bot must read before every piece. See `references/voice-analysis-from-wordpress.md`. Point the content bot's SOUL.md at the style guide + post corpus, then re-verify it can recite the structure unprompted.
8. **Moving the knowledge dir later?** Fix every SOUL.md path with a sed replace (e.g. `~/duck-os/` → `~/hermes-agent/duck-os/`), keep the old dir as a copy or remove it per user's word, and commit the repo change.

## Pitfalls
- Role split that worked for an OPB business: core coach/filter (the 'system' persona), content creator (brand persona), sales/customer replies (same forbidden-words firewall), research/news (digests with links), admin/KB (files + Notion). One shared knowledge dir; one distilled SOUL.md per role.
- Forbidden-word lists and tone rules travel to EVERY customer-facing bot, not just the content one.
- Bots referencing health/medication details must use the user's euphemism convention (e.g. 'แบต/พลังงาน' for battery/energy), never literal terms — copy this verbatim from the source instructions.
- Routines/cron and external tool routing (Google Tasks/Calendar) are follow-ups, not part of initial creation — offer them after the team passes verification.

## Related
- hermes-agent skill: spawning/orchestration mechanics, profile CLI reference, Bot Mode (desktop UI over the same profile primitive).
- references/voice-analysis-from-wordpress.md — pulling the user's published posts and distilling a style guide for the content bot.
- references/full-corpus-and-product-sites.md — fetching the ENTIRE archive (X-WP-Total, slug dedupe, era/timeline analysis) and surveying a sibling product site (guide pages, tool map).
