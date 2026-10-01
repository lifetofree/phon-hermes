# Snapzy (snapzy.app) — verified research 2026-09-07

## Disambiguation
"Snapzy" = 3 different products: (1) snapzy.app = native macOS screenshot/screen recording app (THIS one), (2) snapzy.ai = camera-first mobile apps (PLATE/BLOOM/LABEL/COIN/ROCK), (3) "Snapzy" App Store id6762074068 = burst camera app (dev 洋 刘, $2.99). User clarify call timed out 2026-09-07 → proceeded with snapzy.app per recommendation (tech tool, fits adduckivity audience).

## Core facts (primary sources)
- Vendor: duongductrong (individual OSS maintainer), BSD-3-Clause, GitHub duongductrong/Snapzy
- Repo: 3,068 stars, 170 forks, 67 open issues, created 2026-01-15, latest push 2026-09-05, default branch `master` (NOT main)
- Latest release v1.31.0 (2026-08-15): OCR, magnifier + pixel grid + color picker, window-shadow pref, Raycast integration, repeat-last-area shortcut
- Stack: SwiftUI + AppKit + ScreenCaptureKit + Vision + Sparkle; native, sandboxed, minimal entitlements, notarized, Hardened Runtime; macOS 13+ Ventura, Intel & Apple Silicon
- Free 100% — community crowdfunded the $99 Apple Developer Program fee (100% goal reached, banner still on site) → now on Mac App Store + GitHub releases + `brew install --cask snapzy`
- Privacy: offline-first; network = Sparkle checks + user-initiated uploads to user's own AWS S3 / Cloudflare R2 only; credentials in Keychain; auto-expiration 1-90 days; custom domain support
- Features: area/fullscreen/Application capture (captures other apps' menu-bar popovers, transparent rounded corners), scrolling capture, OCR (Apple Vision on-device OR custom OpenAI-compatible endpoint + downloadable PP-OCR models), subject cutout, window shadow (macOS 14+), PNG/JPG/WebP, annotation editor (arrows/blur/watermark/auto-redaction/counters), video + GIF recording (system audio+mic, mouse highlights, keystroke overlays), video editor (trim, Follow Mouse zoom), Quick Access panel, Capture History browser, configurable global shortcuts, 10 languages (EN VI 简 繁 ES JA KO RU FR DE — NO THAI), TOML config export/import, Raycast integration, activity monitor
- CleanShot X comparison anchor (Aug 2026, toolradar verified): $29 one-time, 1GB cloud, 1yr updates, optional $19/yr renewal, ~10 yrs maturity

## Draft status
- Long form: `content-study/posts/20260907-cnt-snapzy-macos-screenshot-intro.md` (push b69782a)
- Notion Content Drafts DB page `3d4df8d8-8d8c-81f2-b274-da7e704aa141` (Status: draft, 59 blocks verified read-back)
- Angle: "CleanShot X แต่ $0" — Type B tool review; cons: project 8 months, cloud share DIY, no Thai UI, single maintainer, 67 open issues
- Potential follow-ups: short version for social, or "BYO cloud share pipeline with R2