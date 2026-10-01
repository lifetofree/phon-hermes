# LM Studio research (verified 2026-09-07, Bionic deep-dive 2026-09-08)

No disambiguation needed — LM Studio = Element Labs, Inc. (lmstudio.ai) local-LLM GUI/stack. Homepage now leads with **Bionic** (their new agent app) — intro content should cover both the classic app AND Bionic or it reads stale.

## Bionic deep-dive (verified 2026-09-08)

**Launch 16 July 2026** (bestaiagents.app review, verified 2026-08-01). Separate download from LM Studio app; use alongside. Doc URL gotcha: real paths = `/docs/bionic/agent/code-project`, `/docs/bionic/agent/work-project`, `/docs/bionic/voice-input`, `/docs/bionic/models`, `/docs/bionic/models/download-local-models`, `/docs/bionic/accounts-plans-and-billing/credits-and-usage` (NOT /agent/coding, /agent/documents, /models/voice-input — those 404). `llms.txt` does NOT list Bionic pages; resolve real paths by scraping `href` from `/docs/bionic`.
- Structure: **Projects → Sessions**. Session = tabs, side-by-side (drag tab to half-pane), Fork response, **background sessions** continue when switching tabs/projects.
- **Code projects**: "Allow coding" toggle + working directory; indexes folder; Git repo+branch shown; search/edit/Git/shell; docs recommend **inspect → change → test** + review inline diffs/Git diff before keeping; sub-sessions investigate in parallel.
- **Work projects**: managed sandbox — documents, decks, spreadsheets, PDFs, images, text; **Project Files** (shared, managed) vs **External Files** (edited in place at original location); Web Search toggle (Settings→General, ZDR, login, limits).
- **Models per session**: Cloud (frontier open, Secure Cloud US ZDR, needs account+billing, credits) / Local (on-device, $0, no billing) / **Remote via LM Link** (inference on linked device, conversation stays local). Reasoning level per session; Root model default.
- **Voice**: local realtime multilingual transcription via **Voxtral (Mistral AI)**; "Auto load voice model" setting.
- **Skills**: standard Agent Skills (SKILL.md); auto-use or `@` reference palette; create from successful workflow ("Create a skill based on what we just did"); install from URL / `@Install Skill`; **use skills from Codex & Claude Code** (Settings→Skills→"Use skills found in other apps").
- **Credits**: consumed ONLY for cloud models; local+remote = no billing; Billing and Usage = 30-day totals.
- **Pricing 09/2026 (lmstudio.ai/pricing)**: Free $0 = local LLMs + local voice + ZDR web search (login, limits) + LM Link 5 devices. Cloud per-1M in/cached/out: GLM-5.3-Flash $0.15/$0.03/$0.50; Kimi K3 $3.00/$0.30/$15.00; DeepSeek V4 Flash $0.13/$0.028/$0.26; **DeepSeek V4 Pro $1.32/$0.132/$3.96 (new 09-08)**; GLM-5.2 $1.50/$0.30/$4.50; GLM-5.3 $1.40/$0.14/$4.40; Kimi K2.6 $0.95/$0.16/$4.00; Kimi-K2.7-Code $0.95/$0.16/$4.00. **Bionic Pass** = subscription announced, "Pricing and plan details coming soon" (bestaiagents.app confirms the name).
- Cons used in draft: quality = hardware × open model; cloud credit terms thin (no expiry/context-limit detail); Bionic Pass unpriced; app proprietary; no browser/computer-use autonomy yet; external files edited in place; ~2 months old.

## Ecosystem = 3+1 tools (docs/app/basics/lmstudio-vs-llmster-vs-lms)
- **LM Studio app** — GUI: Discover (HF download), Chat, RAG (docx/pdf/txt; short docs = full in-context, long = RAG retrieval), presets, prompt templates, Developer server, MCP host.
- **llmster** — headless daemon (no GUI) for Linux server / headless GPU rig / CI / boot service.
- **lms** — CLI (GitHub lmstudio-ai/lms: MIT, 5,273 stars, 452 forks, 333 open issues, created 2024-04, active push 2026-09). `lms get|load|ls|server start|chat|link`. Server at **http://localhost:1234**, no auth by default (optional API token). `/api/v0` REST + **OpenAI-compatible + Anthropic-compatible** endpoints; stateful /api/v1/chat; ephemeral MCP via API.
- **Bionic** (2026, separate app) — agent for open models: projects/sessions; work (docs, auto-save) + coding (search/edit/Git/shell in chosen dir); model per session = local ($0, no account) / cloud (frontier open models, US-based **Zero Data Retention**) / remote via LM Link; **Skills** (standard Agent Skills SKILL.md, compatible with Codex/Claude Code); real-time **local** voice transcription (multilingual, Voxtral). Bionic Pass plans TBA.
- **LM Link** — cross-device access to local models, **E2E encrypted via partnership with Tailscale**, free ≤5 devices; mobile app **Locally** (iPhone/iPad); usable via CLI/REST/Claude Code/Codex. Content hook: ties into the Tailscale series already written (20260824 + 20260904 parts).
- Runtime: **llama.cpp + MLX** (Apple Silicon). MCP Host since v0.3.17 (mcp.json, Cursor notation; docs warn untrusted MCP = arbitrary code + token bloat on local models).

## System requirements (docs/app/system-requirements)
macOS: Apple Silicon M1-M4, macOS 14+, 16GB RAM rec (8GB = small models/modest ctx), **Intel Mac NOT supported**. Windows: x64 + ARM (Snapdragon X Elite), AVX2, 16GB RAM rec, ≥4GB VRAM rec. Linux: AppImage only, x64/ARM64, Ubuntu 20.04+ (>22 not well tested).

## Pricing (lmstudio.ai/pricing, 09/2026)
Free $0 = local LLMs + local voice + ZDR web search (login, limits) + LM Link 5 devices. Cloud = pay-as-you-go credits (local/LM Link never consume). Per-1M-token (in/cached/out): DeepSeek V4 Flash $0.13/$0.028/$0.26; DeepSeek V4 Pro $1.32/$0.132/$3.96; GLM-5.3-Flash $0.15/$0.03/$0.50; GLM-5.2 $1.50/$0.30/$4.50; GLM-5.3 $1.40/$0.14/$4.40; Kimi K2.6/K2.7-Code $0.95/$0.16/$4.00; Kimi K3 $3.00/$0.30/$15.00. Bionic Pass: coming soon.
License: **desktop app proprietary (closed)**; lms CLI = MIT.

## Pro/cons framing used in draft
Pros: lowest-friction GUI (3 clicks), GUI→CLI→daemon growth path, 100% offline, privacy (local + ZDR cloud), OpenAI/Anthropic compat API, LM Link/Tailscale, Bionic free for local, MLX+llama.cpp coverage.
Cons: app not open source, Intel Mac unsupported, Linux AppImage-only, Bionic new (plans TBA), cloud = data leaves machine (ZDR ≠ local), MCP double-edged, RAG needs tuning, API no auth by default, no fine-tuning (→ Unsloth Studio).

## Draft status
- Intro: `content-study/posts/20260907-cnt-lm-studio-local-llm-intro.md` (pushed). Notion Content Drafts page `3d4df8d8-8d8c-8171-bc39-de13b7c6d7a7` (71 blocks, has_more=False, verified read-back incl. tail hashtags; Status: draft; URL https://app.notion.com/p/3d4df8d88d8c8171bc39de13b7c6d7a7). Cross-refs: Ollama series (part1/2), Tailscale series, Unsloth Studio draft.
- **Bionic deep-dive (2026-09-08)**: `content-study/posts/20260908-cnt-lm-studio-bionic-intro.md` (~2725 words, pushed). Notion page `3d5df8d8-8d8c-8191-a0ef-e1fed9f2fc0b` (73 blocks, has_more=False, verified read-back incl. tail hashtags; Status: draft; URL https://app.notion.com/p/LM-Studio-Bionic-Agent-Local-LLM-Code-Lo-3d5df8d88d8c8191a0efe1fed9f2fc0b). Follow-ups: Bionic Pass pricing post when it lands; "Bionic vs Claude Code on the same repo" hands-on.

## Notion DB schema note (2026-09-07)
Content Drafts DB GET `/v1/databases/3ccdf8d8...` requires `Notion-Version: 2022-06-28` header (missing → 400 `missing_version`). Date prop is **date** (use `"date": {"start": "YYYY-MM-DD"}`), NOT title — an earlier payload attempt used title and was fixed before submit.
