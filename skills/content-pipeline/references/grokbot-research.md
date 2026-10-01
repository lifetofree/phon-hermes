# Grok Bot (xAI) — verified research (2026-09-11)

Disambiguation: **Grok** (chatbot, Grok 4.x, SuperGrok) ≠ **Grok Bot** (agent product, launched beta 2026-08-11). User asked about "grokbot" → it's the agent product. Sources: x.ai/news/introducing-grok-bot (official) + deeperinsights.com + ayautomate.com (hands-on, launch week) + layer3labs.io.

## Core facts
- xAI's always-on AI agent product, beta 11 Aug 2026. Distributed jointly with Cursor (xAI acquiring Cursor, ~$60B).
- Each Bot: own persistent **cloud computer** (real browser, filesystem, terminal), own logins (connect once, reused), assigned **role** (email / LinkedIn outreach / research / scheduling). Work continues after laptop closes — cloud instance, not local.
- Platforms: macOS, iOS, Windows, Linux at launch; Android shipped on Google Play. Mobile = full parity (bots, routines, live bot-screen view, session takeover from phone).
- **No model selection** — model auto-selected per task, no advanced mode. Limitation for compliance/cost-sensitive teams.
- Login handoff pattern: bot navigates to login screen itself, hands control to user ("sign in, then hand it back"), resumes on its own browser instance.
- Plugin library one-click: Notion, Slack, Google Drive, AWS Agents, SageMaker, Browserbase, Composio, Context7 + custom plugin builder. Bot picks plugin (faster) vs raw browser control (works on no-API sites) per task. ~80% of internet has no API/MCP (their claim).
- Teach-by-demonstration: record a screen session of a workflow → bot saves as routine → repeatable on demand or schedule (routines panel). Closest thing to a no-code automation builder.
- Multi-Bot teams: parallel bots, group chats, bots message each other, share context in threads, pass work/assign ownership; "chief of staff" bot pattern. Approval checkpoints only on judgment calls.
- xAI internal use cases: sales outbound (overnight account research, intent scoring, drafts in each seller's voice, CRM updates), demo readiness, ops (new-hire seating, Gmail invoices), engineering (repro bug in UI → file ticket → hand to debugging bot).
- Real hands-on use cases (ayautomate launch-week test): Beehiiv newsletter stats via one screen recording (no API), X-account watch with self-built 30-min browser routine, Gmail triage via MCP plugin, Salesforce research via full computer access.

## Pricing (beta, no free tier, no standalone price)
- SuperGrok Heavy ~$300/mo, SuperGrok Plus ~$100/mo (deeperinsights lists Plus as having Grok Bot access; ayautomate lists only Heavy/Cursor Ultra/Teams Premium — **treat tier details as inconsistent between sources**, verify before publishing). Cursor Pro+/Ultra ~$60–200/mo, Cursor Teams Standard/Premium ~$40–120/seat. Enterprise: waitlist, contact sales. Separate usage pool — bot work doesn't count against Grok/Cursor plan usage (official).

## Pros (verified across sources)
- Own-computer model = genuine edge over chat-bound agents; device-independent overnight work.
- No-API app access via real browser.
- Teach-by-demonstration removes workflow-specification cost (the RPA bottleneck).
- Low setup bar: message like a coworker, no workflow/config building.
- Native multi-agent coordination.
- Full mobile parity incl. live session takeover.

## Cons / gaps
- Price gate: $120–300/mo, no free tier, no standalone price; tied to Cursor/xAI subscription tiers.
- No model selection/constraint (compliance, cost, reliability).
- Early beta: capable-but-uneven reliability; xAI hasn't published granular safety guardrails → supervision required for live-account actions.
- No live conversational voice mode (dictation only).
- Account-risk: bot acts in real inbox/CRM — mistakes are real.
- Comparison table (deeperinsights): always-on Yes/Partial/Partial vs OpenAI+Claude agents; setup demo vs prompt; maturity Beta vs Established.

## Notion draft status
- Page: 3d8df8d8-8d8c-8198-8a18-c65ad7364d05 (Content Drafts DB, Status=draft, Platform=WordPress+general, Date 2026-09-11).
- Note: created WITHOUT the GitHub markdown draft + commit step (steps 4–5) — only filed in Notion per the request. Backfill `~/hermes-agent/content-study/posts/YYYYMMDD-cnt-grok-bot.md` + commit if this becomes a real post.

## Content angles ("อื่นๆ ที่เหมาะสม" per user request style)
- Hook: "AI ที่จ้างเป็นทีม" — not a chatbot, a junior teammate roster you hire 24/7.
- Direct comparison with **AutoClaw** (already reviewed, in this series): both are "agent with own computer" pattern — Grok Bot = frontier validation of the same architecture we documented.
- Duck OS angle: role-scoped agents with own credentials + state, coordinated — the architectural trend, not the specific product.
- Open verification needed before publishing: tier-access discrepancy (Plus vs Heavy only), whether $120-300 figure is stable post-launch.