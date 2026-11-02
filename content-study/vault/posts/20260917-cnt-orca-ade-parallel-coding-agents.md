# Orca — ADE สำหรับ "ฝูง" Coding Agent ( cockpit ที่รวม Claude Code, Codex และทุก CLI Agent ไว้ในที่เดียว )

<!--
ContentID: 20260917-CNT-ORCA-ADE
Series: standalone — ref: 20260904-cnt-autoclaw-zcode-combo (2026-09-04), 20260913-cnt-real-artifact-single-source-of-truth (2026-09-13)
Type: Long Form Tool Review (~2600 words)
Status: Draft — รอย review
Sources (researched 2026-09-17, primary):
- github.com/stablyai/orca — README main (fetched live 2026-09-17): "The AI Orchestrator for 100x builders. Run Codex, ClaudeCode, OpenCode or Pi side-by-side — each in its own worktree, tracked in one place." + full feature table + supported agent list + install (brew cask stablyai/orca/orca, AUR stably-orca-bin, dmg/exe/AppImage) + MIT + privacy/telemetry links
- GitHub API repo stats (fetched 2026-09-17): 70,672 stars, 4,627 forks, 6,195 open issues, created 2026-03-17, pushed 2026-09-17, license MIT, topics: ade/agent-ide/parallel-agents/worktrees/ghostty/yc-backed, homepage onOrca.dev
- Releases API: v1.4.205 (2026-09-17), v1.4.204 (09-16), v1.4.203 (09-15) = daily ship cadence; latest release notes mention native chat message rail, worktree archive hooks, terminal PTY persistence, Codex usage scan perf
- onorca.dev (fetched live): "Ship 100x with the agent IDE" + docs index (57 docs pages)
- onorca.dev/docs "What is Orca?": 60-second pitch — desktop IDE for multiple AI coding agents side by side; "every task gets its own git worktree, its own agent terminal, and its own browser tab"; "Who it's for: people who already write code for a living... assumes you read diffs, care about commits"; "What Orca is not: not a model (BYO subscription), not a git replacement, not a hosted VPS product"
- onorca.dev/docs/ways-to-run: 4 modes — Local / SSH target / Remote Orca Server (orca serve, headless, mobile reconnect) / Cloud VM per-workspace (BYO provider); "Orca does not sell managed VPS hosting"
- onorca.dev/docs/mobile: iOS App Store (id6766130217) + Android APK 0.0.48 + TestFlight; BETA; read-mostly: status/scrollback/reply/sleep worktree/SC review/account switch/dictate voice
- onorca.dev/docs/telemetry: anonymous random local ID; NO file contents/prompts/agent output/terminal output/repo names/branch names/URLs/paths/commit messages/IP; opt out DO_NOT_TRACK=1 or ORCA_TELEMETRY_DISABLED=1; no account system
- onorca.dev/enterprise: SOC 2 (AICPA) readiness, self-hostable, "no model in the middle" (Orca never inspects/stores prompts/code), contact-based
- Secondary: rickhigh.substack.com (ADE essay: Stably AI = 4-person SF team, YC-backed, TypeScript/Electron; "ADE bounded by how many diffs you can review"; "10-100 agents at once" = company framing not measured) + volanea.com review (isolation needs explicit rendezvous strategy — GitHub first-time-user issue; review capacity is the real ceiling) + aistarted.com (MIT, desktop + mobile)
-->

เคยมีคืนที่คุณเปิด terminal 4 อัน — อันหนึ่ง Claude Code, อันหนึ่ง Codex, อันหนึ่ง OpenCode — แล้วทุกอันต่าง rewrite ไฟล์เดียวกันใน working directory เดียวกัน — พอมาเช็ก git status ตอนเช้า ระบบของคุณ crash เพราะ agent ทั้ง 4 ตัวเขียนทับกันเองมั้ยคับ

แล้วทางแก้ที่คนส่วนใหญ่ทำคือ "เปิดทีละอันแล้วรอ" — ซึ่งช้า — หรือ "เขียน script tmux เอง" — ซึ่งเหนื่อย

วันนี้พรจะพาไปรู้จัก **Orca** — app ที่แก้ปัญหานี้ตรง ๆ: **ADE (Agent Development Environment) สำหรับรัน coding agent หลายตัวพร้อมกัน — ตัวละคร์ก worktree ของตัวเอง — ใน cockpit เดียว**

.

## 01: Orca คืออะไร — "Cockpit" ไม่ใช่ "IDE"

Orca คือ **desktop app** (macOS / Windows / Linux) สำหรับรัน coding agent **หลายตัวขนานกัน** — แต่ละตัวรันใน git worktree ของตัวเอง, terminal ของตัวเอง, browser tab ของตัวเอง — แล้วคุณดูทุกอย่างในหน้าต่างเดียว

ตัวเลขจริง (ตรวจจาก GitHub API 2026-09-17): **70,672 stars** / 4,627 forks / **MIT license** / สร้างเมื่อ มี.ค. 2026 (อายุแค่ ~6 เดือน) — โดย **Stably AI** ทีมเล็กจาก San Francisco (YC-backed, เขียนด้วย TypeScript บน Electron) — และ cadence การ ship โหดจริง: release ใหม่ทุกวัน — ตัวล่าสุด **v1.4.205 ออก 17 ก.ย. 2026** (วันเดียวกับที่พร research)

จุดยืนของ Orca (จาก docs ตรง ๆ) คือสิ่งที่ไม่ใช่:

- **ไม่ใช่ model** — Orca รัน agent ที่คุณมีอยู่แล้ว — bring your own Claude Code / Codex / OpenCode subscription — ไม่ขาย inference
- **ไม่ใช่ git replacement** — ทุก worktree คือ git worktree จริง ๆ — `cd` เข้าไปใช้ git ธรรมดาได้ตลอด
- **ไม่ใช่ hosted VPS** — รันบน desktop ของคุณโดย default — remote compute ใช้เครื่อง/คลาวด์ที่คุณควบคุม

แนวคิด ADE ต่างจาก IDE ที่คุณใช้ทุกวันยังไง — IDE สมมติว่า **คน** คือตัวสร้างโค้ด (invest ใน autocomplete, inline error) — ADE สมมติว่า **agent** คือตัวสร้างโค้ด (invest ใน isolation, monitoring, comparison) — หน่วยความสนใจเปลี่ยนจาก "ไฟล์" เป็น **"task attempt"** — คุณ dispatch intent แล้วได้รับคำตอบหลายเวอร์ชัน แต่ละเวอร์ชันคือ worktree ทั้งก้อน ที่ accept หรือ discard ได้ทั้งก้อน

.

## 02: Features หลัก — มากกว่า "terminal หลายอัน"

**1. Parallel Worktrees — หัวใจของ Orca**

Fan prompt เดียวไป **5 agents** — แต่ละตัวรันใน git worktree แยก — เปรียบเทียบผลแล้ว **merge ผู้ชนะ** — หรือ 3 งานที่ไม่เกี่ยวข้องกัน → 3 agents, 3 worktrees — **zero branch juggling, zero stash** — docs มี recipe "Race three agents on the same task" เป็นทางการ

**2. Terminal Splits**

Terminal ระดับ Ghostty (WebGL rendering), split ได้ไม่จำกัด, scrollback **survive restart** — เหมาะกับคนที่รัน agent หลายตัวแล้วต้องเฝ้า output พร้อมกัน

**3. Embedded Browser + Design Mode**

browser จริง (Chromium) ในตัว — **Design Mode = คลิก UI element ใดก็ได้** แล้ว HTML + CSS + screenshot ของมันถูกส่งเข้า prompt ของ agent โดยตรง — แก้ UI bug โดยไม่ต้อง copy CSS manual

**4. GitHub / Linear / Jira Native**

ดู PR, issues, project boards ใน app — เปิด worktree จาก task ใด ๆ แล้ว review โดยไม่ context switch — **Annotate AI Diffs** = ใส่ comment ที่บรรทัด diff ใดก็ได้ แล้วส่งกลับไปที่ agent — review loop ปิดใน Orca

**5. Mobile Companion (iOS + Android) — BETA**

ดู agent จากมือถือ: สถานะ (working / done / waiting on input), scrollback, ตอบ prompt จากโทรศัพท์ (พิมพ์/แนบรูป/**พูดผ่านไมค์**), sleep worktree, review source control, commit จากมือถือ, switch agent account + ดู usage — iOS อยู่ใน App Store แล้ว, Android ยังเป็น APK 0.0.48 — desktop คือ source of truth เสมอ

**6. Remote: SSH Worktrees + Orca Server**

4 modes (จาก docs/ways-to-run): **Local** (default) / **SSH target** (รัน agent บนเครื่องไกล — VPS, Mac mini, GPU box — ส่วน editor+diff ยังอยู่บน laptop) / **Remote Orca Server** (`orca serve` headless — agents รันต่อแม้ laptop นอน — มือถือ reconnect ได้) / **Cloud VM per-workspace** (BYO provider) — Orca **ไม่ขาย managed VPS** — เครื่องเป็นของคุณเสมอ

**7. Orca CLI + Orchestration**

agent สั่ง Orca ได้เอง: `orca worktree create --agent codex --prompt "..." --json` / `orca worktree ps` (fleet view — คิดเป็น `ps aux` แต่ process = attempt ของงานคุณ) / `orca terminal wait --for tui-idle` — **block รอ event แทน sleep loop** — บวก Scheduled Automations + Computer Use + Worktree Checkpoints + Skills registry & MCP

**8. Account Switcher + Usage Tracking**

ดู usage + rate-limit reset ของ Claude/Codex ใน app — **hot-swap account** โดยไม่ต้อง login ใหม่ — ตัวเล็ก ๆ ที่ประหยัดเวลาได้จริง

**9. Others** — Quick Open (search ทุกอย่าง), session restore + agent hibernation, Monaco editor + autosave, drag ไฟล์/รูปเข้า prompt, rich previews (Markdown/Mermaid/PDF), notifications + unread state

.

## 03: Supported Agents — "ถ้ามันรันใน terminal มันรันใน Orca"

กฎเดียว: **any CLI agent** — list ทางการยาวมาก (README): Claude Code, Codex, Grok, Cursor CLI, GitHub Copilot, OpenCode, **Hermes Agent**, Devin, Goose, Cline, Kimi, Kilo, Qwen Code, Mistral Vibe, Amp, Continue, Droid, Kiro, Rovo Dev + อื่น ๆ — **vendor-neutral** — ไม่ต้อง bet กับ model provider ตัวเดียว — subscription เป็นของคุณ Orca เป็นแค่ cockpit

.

## 04: Pros / Cons — ตรงไปตรงมา

**Pros ✅**

- **Agent-agnostic** — ใช้ subscription ที่จ่ายอยู่แล้ว (Claude Max / Codex / GLM) — Orca $0 (MIT) — ไม่มี lock-in
- **Worktree isolation** — agent ไม่เขียนทับกัน — ไฟล์/branch/สถานะแยกกันจริง (git worktree ไม่ใช่ sandbox จำลอง)
- **Review loop เป็น native** — diff viewer + annotate + commit/push + GitHub/Linear — คำถามเปลี่ยนจาก "โค้ดนี้ถูกไหม" เป็น "**ตัวไหนดีที่สุด**" ซึ่ง IDE ธรรมดาช่วยไม่ได้
- **Mobile + Remote = kick off แล้วเดินไปกินข้าว** — agents รันต่อหลัง laptop นอน — triage จากมือถือ — supported workflow ไม่ใช่ hack
- **Privacy/Local-first** — telemetry = anonymous ID + version/OS เท่านั้น — **ไม่ส่ง** file contents / prompts / agent output / repo names / paths / commit messages — ปิดได้ด้วย `DO_NOT_TRACK=1` — ไม่มีการ login ระบบ account
- **Self-hostable + SOC 2 (readiness)** — enterprise page: "no model in the middle" — prompts/โค้ดไป provider ของคุณตรง ๆ Orca ไม่ inspect ไม่ store
- **Cadence** — ship รายวัน, 70.7k stars, community ใหญ่ (Discord + WeChat groups)

**Cons ❌**

- **Young + issue stack หนา** — อายุ ~6 เดือน (มี.ค. 2026) + **6,195 open issues** — feature set กว้างมากแต่บางมุมยังขรุขระ — README เองก็ยอมรับ: "we ship daily, so this list is perpetually behind"
- **Onboarding มี learning curve** — worktree model + isolation = agent **ไม่แชร์ in-progress files กันอัตโนมัติ** — มี GitHub issue จากผู้ใช้ใหม่ชม orchestration แต่สับสนเรื่อง worktree แลกเปลี่ยน context กันยังไง — ต้องมี "rendezvous strategy" (planning doc ที่ commit, issues, หรือ orchestration messaging) เอง
- **Review = bottleneck ตัวจริง** — parallelism ลดเวลาถึง "first result" แต่ **ไม่ลดเวลาถึง merged result** — agent 5 ตัว = diff 5 ก้อนที่ต้องอ่าน — "100x builders" / "10-100 agents" คือ framing ของบริษัท **ไม่ใช่ตัวเลขที่วัดได้** — ceiling จริงของคุณ = จำนวน diff ที่อ่านไหว
- **Electron = กิน resource** — เทียบกับ terminal เดียว ๆ มันหนักขึ้น (RAM/CPU) — สำหรับเครื่องเล็ก ๆ ที่รัน agent หนักอยู่แล้วต้องคิด
- **Mobile ยัง beta** — iOS ใน App Store แล้ว แต่ Android ยังเป็น APK ตรง (ไม่ผ่าน Play Store)
- **ไม่ขาย managed VPS** — remote = BYO เครื่อง/คลาวด์ — ถ้าอยาก "one-click cloud" ต้องจัดการเอง

.

## 05: เปรียบเทียบ — Orca vs ทางเลือกอื่น

| | Orca | Claude Code / Codex ตรง ๆ | IDE + plugin (Cursor ฯลฯ) | DIY (tmux + git worktree) |
|---|---|---|---|---|
| รัน agent พ่วงหลายตัว | ✅ worktree แยก ตัวละ worktree | ❌ 1 terminal = 1 agent | ⚠️ ได้แต่ไม่ได้ออกแบบมา | ✅ ต้องสร้างเอง |
| Isolation | ✅ git worktree native | ❌ working dir เดียว | ❌ working dir เดียว | ✅ ถ้า setup เอง |
| Review loop (diff+annotate) | ✅ ใน app | ⚠️ terminal | ✅ (IDE strength) | ❌ |
| Mobile/Remote | ✅ App + `orca serve` | ⚠️ SSH เอง | ❌ | ⚠️ SSH เอง |
| Cost | $0 (MIT) + BYO subscription | ค่า subscription | ค่า subscription + ค่า IDE | $0 + เวลา setup |
| ความสุ่มเสี่ยง | Young, 6k+ issues | เสถียร ( mature ) | เสถียร | เสถียรแต่ brittle |

.

## 06: เหมาะกับใคร / ไม่เหมาะกับใคร

**เหมาะกับ**

- Dev ที่ใช้ CLI agent **2 ตัวขึ้นไป** อยู่แล้ว (Claude Code + Codex ฯลฯ) แล้วเริ่มชนกันเอง
- คนที่ **review diff เป็นกิจวัตร** — อ่าน diff, ใส่ใจ commit, ดูแล worktree — docs พูดตรง ๆ: "If you're looking for a no-code tool, Orca is not that"
- คนที่ต้องการ **agent รันต่อหลัง laptop นอน** + triage จากมือถือ
- ทีมที่อยาก standardize agent หลายตัวใน workflow เดียว (enterprise: approved providers, audit trail ผ่าน git/PR)

**ไม่เหมาะกับ**

- มือใหม่ที่ไม่เคยอ่าน diff — ADE จะทำให้คุณ **ต้อง** อ่าน diff เยอะขึ้น ไม่ใช่меньลง
- คนที่ agent ตัวเดียวพอ — overhead ไม่คุ้ม
- คนที่อยาก all-in-one ไม่ต้อง configure — Orca = BYO subscription + BYO remote machine เสมอ

.

## 07: Pricing

**Orca ตัว app: $0 — MIT, free, open source** (brew cask / AUR / dmg / exe / AppImage) — ค่าใช้จ่ายจริง = **subscription ของ agent ที่คุณเลือก** (เช่น Claude Max/Pro, Codex plan, GLM) — ไม่มี pricing page สำหรับ consumer — Enterprise = contact (SOC 2 readiness, rollout guidance, org-level defaults)

.

## มุมของ Duck OS

ในภาษาของระบบ — การรัน agent หลายตัวใน working directory เดียว = **processes ที่เขียนทับ shared memory โดยไม่มี mutex** — crash เป็นเรื่องเวลาไม่ใช่คำถาม — Orca คือการ **containerize โดย git worktree** — แต่ละ agent ได้ address space ของตัวเอง — ส่วนคุณ (human) คือ **arbiter** — arbiter ที่ไม่มีวันถูก replace — เพราะการ merge คือ decision ว่า **asset ชิ้นไหน** ที่ผ่าน review

Protocol **FLEET-01** — 3 commands สำหรับรันฝูง agent:

1. `fleet --fanout` — เลือกงานที่ **independent** (docs / a11y / test coverage / API validation) หรือ **race** งานยากเดียวด้วย 3 agents — อย่า fanout งาน coupled 5 ตัว — review burden จะไม่จ่ายค่า 5x
2. `fleet --diff` — อ่าน diff ทุกก้อนผ่าน **REAL-01** — ชี้ artifact เทียบกับ spec — comment ที่บรรทัดที่ผิด แล้วส่งกลับ agent — อย่าวาง diff ไว้แล้วไปทำอย่างอื่น
3. `fleet --merge` — merge เฉพาะก้อนที่ผ่าน tests + ผ่าน eye ของคุณ — แล้ว commit "rendezvous doc" (สิ่งที่ agent เรียนรู้) กลับ main — ให้ worktree ถัดไปเริ่มจาก asset ไม่ใช่จากศูนย์

Success Criteria: สัปดาห์นี้ — งาน 1 ตัวที่ถูก fanout แล้ว **merge ผู้ชนะ 1 ก้อนจริง** — และ zero ไฟล์ที่ agent เขียนทับกัน

.

## สรุปแบบวิศวกรเป็ด

Orca ไม่ได้ทำให้ agent เร็วขึ้น — มันทำให้คุณ **รัน agent หลายตัวโดยไม่ให้มันชนกัน** — และบังคับให้คุณเป็น arbiter ที่ดีขึ้น — เพราะทุก parallel ที่ launch ออกมา **ต้องจบที่ diff ที่คุณอ่าน** — เครื่องที่เร็วขึ้นคือเครื่อง review ของคุณ ไม่ใช่เครื่อง generate

**Cockpit for the fleet — launch five, review all, merge one.**

ใครลอง Orca แล้วเป็นยังไงบ้าง — fanout กี่ตัว review ไหว? คอมเมนต์ด้านล่างได้เลย — ถ้าอยากให้พรทำภาคต่อเรื่อง agent tool ตัวไหน บอกได้เลยคร้าบ

System > Single Thread. ตั้ง worktree แล้วรันฝูงของคุณคับ! 🦆⚡

#Adduckivity #DuckOS #CodingAgent #Orca #ADE #ParallelAgents #GitWorktree #DeveloperTools
