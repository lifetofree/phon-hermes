# เมื่อโฟลเดอร์เดียวรัน 4 Agent พร้อมกันไม่ได้: จัดการฝูง Coding Agents ด้วย Orca (Git Worktree Isolation)

**Excerpt:** การรัน Agent หลายตัวในโฟลเดอร์เดียวกันคือการสั่งให้ระบบ Crash Orca จัดระเบียบด้วย Git Worktree แยกพื้นที่ประมวลผล เพื่อให้คุณทำหน้าที่เป็น Single Source of Truth ในการ Review และ Merge โค้ด
**Site Category:** [[📚 Asset Library]]
**Tags:** [[Adduckivity]] · [[DuckOS]] · #CodingAgent · #Orca · #ADE · #ParallelAgents · #GitWorktree · #DeveloperTools

---

เคยมีคืนที่เราเปิด terminal 4 อัน — อันหนึ่ง Claude Code, อันหนึ่ง Codex, อันหนึ่ง OpenCode — แล้วทุกอันต่าง rewrite ไฟล์เดียวกันใน working directory เดียวกัน — พอมาเช็ก git status ตอนเช้า ระบบ crash เพราะ agent ทั้ง 4 ตัวเขียนทับกันเองมั้ยคับ
.
แล้วทางแก้ที่คนส่วนใหญ่ทำคือ “เปิดทีละอันแล้วรอ” — ซึ่งช้า — หรือ “เขียน script tmux เอง” — ซึ่งเหนื่อย
.
วันนี้พรจะพาไปรู้จัก Orca — app ที่แก้ปัญหานี้ตรง ๆ: ADE (Agent Development Environment) สำหรับรัน coding agent หลายตัวพร้อมกัน — แยก worktree ของตัวเอง — ใน cockpit เดียว
.
## Orca คืออะไร — “Cockpit” ไม่ใช่ “IDE”
Orca คือ desktop app (macOS / Windows / Linux) สำหรับรัน coding agent หลายตัวขนานกัน — แต่ละตัวรันใน git worktree ของตัวเอง, terminal ของตัวเอง, browser tab ของตัวเอง — แล้วดูทุกอย่างในหน้าต่างเดียว
.
ตัวเลขจริง (ตรวจจาก GitHub API 2026-09-17): 70,672 stars / 4,627 forks / MIT license / สร้างเมื่อ มี.ค. 2026 (อายุแค่ ~6 เดือน) — โดย Stably AI ทีมเล็กจาก San Francisco (YC-backed, เขียนด้วย TypeScript บน Electron) — และ cadence การ ship โหดจริง: release ใหม่ทุกวัน — ตัวล่าสุด v1.4.205 ออก 17 ก.ย. 2026 (วันเดียวกับที่พร research)
.
จุดยืนของ Orca คือ:
.
แนวคิด ADE ต่างจาก IDE ที่ใช้ทุกวันยังไง — IDE สมมติว่า คน คือตัวสร้างโค้ด (invest ใน autocomplete, inline error) — ADE สมมติว่า agent คือตัวสร้างโค้ด (invest ใน isolation, monitoring, comparison) — หน่วยความสนใจเปลี่ยนจาก “ไฟล์” เป็น “task attempt” — dispatch intent แล้วได้รับคำตอบหลายเวอร์ชัน แต่ละเวอร์ชันคือ worktree ทั้งก้อน ที่ accept หรือ discard ได้ทั้งก้อน
.
## Features หลัก — มากกว่า “terminal หลายอัน”
1. Parallel Worktrees — หัวใจของ Orca
Fan prompt เดียวไป 5 agents — แต่ละตัวรันใน git worktree แยก — เปรียบเทียบผลแล้ว merge ผู้ชนะ — หรือ 3 งานที่ไม่เกี่ยวข้องกัน → 3 agents, 3 worktrees — zero branch juggling, zero stash — docs มี recipe “Race three agents on the same task” เป็นทางการ
.
2. Terminal Splits
Terminal ระดับ Ghostty (WebGL rendering), split ได้ไม่จำกัด, scrollback survive restart — เหมาะกับคนที่รัน agent หลายตัวแล้วต้องเฝ้า output พร้อมกัน
.
3. Embedded Browser + Design Mode
browser จริง (Chromium) ในตัว — Design Mode = คลิก UI element ใดก็ได้ แล้ว HTML + CSS + screenshot ของมันถูกส่งเข้า prompt ของ agent โดยตรง — แก้ UI bug โดยไม่ต้อง copy CSS manual
.
4. GitHub / Linear / Jira Native
ดู PR, issues, project boards ใน app — เปิด worktree จาก task ใด ๆ แล้ว review โดยไม่ context switch — Annotate AI Diffs = ใส่ comment ที่บรรทัด diff ใดก็ได้ แล้วส่งกลับไปที่ agent — review loop ปิดใน Orca
.
5. Mobile Companion (iOS + Android) — BETA
ดู agent จากมือถือ: สถานะ (working / done / waiting on input), scrollback, ตอบ prompt จากโทรศัพท์ (พิมพ์/แนบรูป/พูดผ่านไมค์), sleep worktree, review source control, commit จากมือถือ, switch agent account + ดู usage — iOS อยู่ใน App Store แล้ว, Android ยังเป็น APK 0.0.48 — desktop คือ source of truth เสมอ
.
6. Remote: SSH Worktrees + Orca Server
4 modes (จาก docs/ways-to-run):
.
7. Orca CLI + Orchestration
agent สั่ง Orca ได้เอง: orca worktree create --agent codex --prompt "..." --json / orca worktree ps (fleet view — คิดเป็น ps aux แต่ process = attempt ของงานเรา) / orca terminal wait --for tui-idle — block รอ event แทน sleep loop — บวก Scheduled Automations + Computer Use + Worktree Checkpoints + Skills registry & MCP
.
8. Account Switcher + Usage Tracking
ดู usage + rate-limit reset ของ Claude/Codex ใน app — hot-swap account โดยไม่ต้อง login ใหม่ — ตัวเล็ก ๆ ที่ประหยัดเวลาได้จริง
.
9. Others — Quick Open (search ทุกอย่าง), session restore + agent hibernation, Monaco editor + autosave, drag ไฟล์/รูปเข้า prompt, rich previews (Markdown/Mermaid/PDF), notifications + unread state
.
## Supported Agents — “ถ้ามันรันใน terminal มันรันใน Orca”
กฎเดียว: any CLI agent — list ทางการยาวมาก (README): Claude Code, Codex, Grok, Cursor CLI, GitHub Copilot, OpenCode, Hermes Agent, Devin, Goose, Cline, Kimi, Kilo, Qwen Code, Mistral Vibe, Amp, Continue, Droid, Kiro, Rovo Dev + อื่น ๆ — vendor-neutral — ไม่ต้อง bet กับ model provider ตัวเดียว — subscription เป็นของเรา Orca เป็นแค่ cockpit
.
## Pros ✅
.
## Cons ❌
.
## เปรียบเทียบ — Orca vs ทางเลือกอื่น
.
## เหมาะกับ
.
## ไม่เหมาะกับ
.
## Pricing
Orca ตัว app: $0 — MIT, free, open source (brew cask / AUR / dmg / exe / AppImage) — ค่าใช้จ่ายจริง = subscription ของ agent ที่เลือก (เช่น Claude Max/Pro, Codex plan, GLM) — ไม่มี pricing page สำหรับ consumer — Enterprise = contact (SOC 2 readiness, rollout guidance, org-level defaults)
.
## มุมของ Duck OS
ในภาษาของระบบ — การรัน agent หลายตัวใน working directory เดียว = processes ที่เขียนทับ shared memory โดยไม่มี mutex — crash เป็นเรื่องเวลาไม่ใช่คำถาม — Orca คือการ containerize โดย git worktree — แต่ละ agent ได้ address space ของตัวเอง — ส่วนเรา (human) คือ ผู้ตัดสิน — ผู้ตัดสินที่ไม่มีวันถูก replace — เพราะการ merge คือ decision ว่า asset ชิ้นไหน ที่ผ่าน review
.
Protocol FLEET-01 — 3 commands สำหรับรันฝูง agent:
.
Success Criteria: สัปดาห์นี้ — งาน 1 ตัวที่ถูก fanout แล้ว merge ผู้ชนะ 1 ก้อนจริง — และ zero ไฟล์ที่ agent เขียนทับกัน
.
## #สรุปแบบวิศวกรเป็ด
Orca ไม่ได้ทำให้ agent เร็วขึ้น — มันทำให้เรา รัน agent หลายตัวโดยไม่ให้มันชนกัน — และบังคับให้เป็นผู้ตัดสินที่ดีขึ้น — เพราะทุก parallel ที่ launch ออกมา ต้องจบที่ diff ที่เราอ่าน — เครื่องที่เร็วขึ้นคือเครื่อง review ของเรา ไม่ใช่เครื่อง generate
.
Cockpit for the fleet — launch five, review all, merge one.
.
System > Single Thread. ตั้ง worktree แล้วรันฝูงของเราคับ 🦆
.
#Adduckivity #DuckOS #CodingAgent #Orca #ADE #ParallelAgents #GitWorktree #DeveloperTools
===========
FB version
===========
.
Orca vs ทางเลือกอื่น
.
===========

*Synced: 2026-11-02 19:54 +07 · [Notion](https://www.notion.so/3dedf8d88d8c8030a7a8c73c13438a18) · ✅ Published*