# AutoClaw (Zhipu AI / Z.ai) — verified research (2026-09-03)

Condensed from primary sources for the AutoClaw content series. Long-form draft filed 2026-09-03 (Notion page 3d0df8d8-8d8c-81ef-a414-c7cf29cea032, file posts/20260903-cnt-autoclaw-intro-longform.md). Short version (400-900 words) was OFFERED but not yet written — reuse these facts.

## Disambiguation (IMPORTANT)
"AutoClaw" names 4+ distinct products. The adduckivity one is **Zhipu AI's (Z.ai / 智谱) one-click local OpenClaw installer**, Chinese name 澳龙. The others (autoclaw.dev managed hosting, autoclaw.co trading agents, in-car copilot) are NOT the same product — do not conflate facts across them.

## What it is
- One-click desktop installer packaging the open-source OpenClaw agent framework + GLM-5.3-Flash model + 50+ pre-built skills + visual dashboard (no CLI/Docker/terminal).
- Platforms: Windows 10+, macOS (Apple Silicon + Intel), iOS, Android.
- Models: GLM series (default GLM-5.3-Flash), DeepSeek series, model switching, Custom Model via any OpenAI-compatible endpoint (Base URL + API Key + Model ID) — Tencent Cloud docs show the exact config flow (Models & API → Add Custom Model → Connectivity Test → Set Default).
- Loop: goal in chat → reason → act (browser/file/code/IM tools) → observe → loop → results back in chat.
- Browser automation via "AutoGLM Browser-Use" (screenshot-driven: fill forms, screenshot, data collection, scheduled tasks).
- Multi-agent: specialized roles (Collector / Strategist / Mind), Hive Mind dashboard shows agent thoughts real-time.
- IM integration built-in: Slack, Telegram, WhatsApp, Discord, Lark — @ the agent in group chat/DM to assign tasks.
- 6 capability areas (official): Office Automation (Word/Excel/PPT), Content Operations (IG/TikTok/Substack/X/Telegram), Investment Research, Web Product Building (frontend code + preview), Browser Automation, IM Integration.

## Free tokens & pricing (verified 2026-09-03)
- New users: **5,000 credits**; daily free credits; free basic usage (docs, data analysis, browser automation, IM workflows).
- GLM Coding Plan: Lite $18 / Pro $72 / Max $160 per month; annual = 30% off.
- Monthly login bonus credits (claim monthly): Lite 5,000 · Pro 10,000 · Max 26,000.
- Limited-time: connecting a GLM Coding Plan gives a 150% quota boost (Individual + Team).
- Per-token (Z.ai): GLM-5.3-Flash list $0.15 in / $0.03 cached / $0.50 out per 1M; promo $0.075 / $0.015 / $0.25 (promo window ended ~Sep 9, 2026 — re-verify before publishing). GLM-5.2 $1.40/$4.40; GLM-4.7 $0.60/$2.20; GLM-4.7 Flash & GLM-4.5 Flash = $0 free on API.
- GLM-5.3-Flash on Coding Plan: 3x quota of GLM-5.3 in points system; half points off-peak + all weekend.

## GLM-5.3-Flash model facts
- MoE 320B total / ~18B active; revealed 2026-08-26 after a week topping OpenRouter as anonymous "ox-alpha"; MIT-licensed, weights on Hugging Face (zai-org/GLM-5.3-Flash); natively multimodal (text+image+video in); 1M-token context; hybrid sparse+linear attention; attention compute -3.01x, KV cache -4.44x vs GLM 5.3.
- Artificial Analysis: intelligence 57.5 (≈ Claude Opus 4.8's 57.3), coding 71.5 (BEHIND GLM 5.3's 74.8 and Opus 4.8's 74.3), agentic 58.2 (ahead of Opus 4.8's 49.4).
- Quirks: thinking CANNOT be disabled (mandatory, default effort max) → budget reasoning output tokens; recommended temp 1 / top_p 0.95 / reasoning_effort max.
- Price context vs Opus 4.8 ($5/$25): ~1/70 input, ~1/100 output at promo; ~1/33 and ~1/50 at list.

## Independent assessment (BestClaw, 2026-08-29)
- Overall 6.9/10, #25 leaderboard; user rating 3.8/5 (31 ratings).
- Dimension highlights: installer 4.5/5, Zhipu model fit 4.4/5, vendor neutrality 2.9/5, team scale 3.3/5, security defaults 3.5/5.
- Cons: heavy Zhipu vendor lock-in (multi-vendor needs adapter), modest multi-team governance/IAM-SSO (enterprise edition), limited plugin/skill ecosystem, production ops/HA/DR DIY, Chinese-language strength neutralized for English-led workflows.
- Security notes: defaults route to Zhipu cloud (declare allowed paths for residency-bound work), scope file/browser/shell perms, centralize+rotate API keys, disable auto-update in enterprise (staged/signed rollout).
- OpenClaw base framework itself has had security researcher attention since Jan 2026 — local-first helps but permissions still matter.

## Sources
- https://autoclaw.z.ai/ (official: features, FAQ, pricing, 5,000 credits, bonus tiers)
- https://www.tencentcloud.com/document/product/1300/81504 (custom model config; confirms "zero-threshold local AI agent by Zhipu AI" + OpenAI-compatible endpoint)
- https://openclawlaunch.com/guides/openclaw-glm-5-3-flash (GLM-5.3-Flash specs, benchmarks, pricing incl. promo expiry Sep 9)
- https://felloai.com/glm-pricing/ (GLM pricing table, Coding Plan tiers, free-tier models)
- https://bestclaw.io/agents/autoclaw (independent review 6.9/10, pros/cons, security checklist)
- https://hyscaler.com/insights/autoclaw-local-ai-agent-guide/ (architecture: observe-reason-act, multi-agent roles, Hive Mind dashboard)
