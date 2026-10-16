# Wispr Flow — verified research (2026-10-16)

Voice dictation app (Wispr, ~$81M raised). Draft: `content-study/posts/20261016-cnt-wispr-flow-voice-dictation.md` (v2 TECH form, 796 wc-w). Notion page `3fbdf8d8-8d8c-81c0-ab74-d9085e7b2b1c` (Content Drafts DB, Status: draft, 74 blocks + 1 table 4col×7rows verified, read-back 2026-10-16).

## Core facts (primary, fetched live 2026-10-16)
- **What:** speech→text with post-processing (filler removal, punctuation, formatting, self-correction capture, personal dictionary, snippets, per-app style Formal/Casual/Very-casual). Works in any text field, no plugins — "If you can type there, you can Flow there" (FAQ). Mac/Windows/iPhone/Android.
- **Speed claims (VENDOR, not measured):** keyboard 45 wpm vs Flow 220 wpm = "4x faster" (homepage demo); "most people save over an hour a day" (why-flow FAQ).
- **Zero-Edit Rate Benchmark (VENDOR-RUN, wisprflow.ai/why-flow):** Wispr Flow 90% / OpenAI 71% / ElevenLabs 63% / Siri 52%. No independent replication found — must stay labeled vendor-reported.
- **Not wrapper-only claim:** "we predate OpenAI's Whisper" + proprietary post-processing models retrained on user feedback (why-flow FAQ).
- **Pricing:** Free $0 = 2,000 words/wk desktop + 1,000/wk mobile, no card/no trial countdown; Pro $15/mo monthly = $12/mo annual (unlimited + Notetaker full + shared dictionary + team analytics); Growth $33→$23 annual (SSO/SAML, enforced HIPAA BAA, admin model-training control); Enterprise custom (SCIM, audit logs, MDM, training locked off). Students/educators 50% off. Notetaker full-access promo "through October 31" (time-sensitive — re-check before publish).
- **Notetaker:** Mac+Windows only (mobile roadmap); NO bot joins the meeting (runs on your device); transcript w/ named speakers + topic summary + next steps; "What did I miss?"; ask-across-meetings + web; MCP export to Claude/ChatGPT.
- **Docs gotchas (not marketing):** internet REQUIRED for transcription; desktop inserts completed text AFTER stop (not live word-by-word); avoid AirPods/Bluetooth earbuds (audio compression); dictation history on-device, deletion permanent; Mac default hotkey = Fn, Windows = Ctrl+Win (customizable; no-Fn Mac = Ctrl+Option).
- **Privacy:** data never sold; opt-in use for improvement; SOC 2 Type II + ISO 27001 + HIPAA (BAA; BAA accounts have Notetaker/Scratchpad disabled).
- **Funding:** $25M new round led by Notable Capital + Steven Bartlett's Flight Fund, total ~$81M, 2025-11-20, "to build the Voice OS" (wisprflow.ai/new-funding; secondary: vctavern 2026-04-26, aivoicenewsletter 2026-04-14).
- **Testimonials (homepage):** Steven Bartlett (gap thought→delivery collapses), Alex Lieberman (Morning Brew: "I literally do not use my fingers to type anymore"), Elena Verna (Lovable), Dave Gilboa (Warby Parker CEO). WSJ: "replaces built-in voice transcription with a model that's scary good".

## Draft status / reuse
- v2 TECH form: stat-line (45/220) + 5 signals + mental model (Post-Processing Layer, honesty caveat) + 4-way table + vendor-numbers honesty section (NO self-run benchmark on this box — all numbers vendor-reported) + Notetaker + pricing + Duck OS angle (input-channel ceiling, User≠Machine, First Principle verified Main_Data_for_UDO.md:38) + two-fork closer (ถ้าของเดิมพอ: อย่าลงมา / ถ้าต้องแก้ทุกครั้ง: ค่อยลงมา) + EN pull-quote "The bottleneck was never your head — it was the pipe." + #สรุปแบบวิศวกรเป็ด closer.
- Battery: 796 wc-w, H1 1/H2 14, beats 14, คุณ 28 (TECH form register), codepoint scan clean (fixed Guillain-Barré→Guillain-Barre + table emoji→Thai words).
- Candidate hooks parked in header: (2) พิมพ์มาทั้งชีวิตแต่ไม่เคยถามว่ามือเร็วได้สุดเท่าไร (3) คุณไม่ได้พิมพ์ช้า — คุณใช้ช่องทางที่ช้ากว่าคิด.
- Follow-up candidates: FB micro-variant (table→flat list), real trial report if user installs (2,000-word free tier = test window), Notetaker deep-dive separate post.
- Shelf life: pricing promo (Oct 31) + $81M funding numbers are date-sensitive — re-verify before publish per tech-post shelf-life rule.
