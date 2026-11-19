# Hermes Restore Guide

What to do if this Mac dies and you need Hermes back.

---

## What is in this repo

| Path | Contents | Restores what |
|---|---|---|
| `hermes-skills/` | All 90 skill dirs, symlinks already resolved into real files | Every skill, reference, script, template |
| `hermes-profile/SOUL.md` | Persona / core instruction | Agent voice and behaviour rules |
| `hermes-profile/config.yaml` | Agent behaviour: model, personalities, toolsets, guardrails, compression, TTS/STT, plugins | How the agent is wired |
| `content-study/`, `research/`, `duck-os/`, `skills/content-*` | Content pipeline state, vault, research notes | The content work itself |

Everything above restores **the agent definition**. That is the part that is hard to rebuild by hand.

---

## What is NOT in this repo (deliberately)

| Missing | Where it lives | Why excluded |
|---|---|---|
| `.env` (24 keys, 6 real secrets) | `~/.hermes/.env` | Public repo — secrets must never land here |
| `auth.json`, `google_token.json`, `google_client_secret.json` | `~/.hermes/` | OAuth credentials |
| `memories/MEMORY.md`, `memories/USER.md` | `~/.hermes/memories/` | Personal profile (email, channel ids, routines) |
| `state.db` (80 MB, 3,921 messages, 18 sessions) | `~/.hermes/state.db` | Chat history — private |
| `channel_directory.json` | `~/.hermes/` | Chat/channel mapping |
| `cron/` (job definitions), `plugins/` (homeassistant, orca-status) | `~/.hermes/` | Runtime wiring, may hold ids |

**Consequence:** a restore from this repo alone gets you a working agent that does not yet talk to Telegram/Discord/Google and has no memory of past work. Those three pieces must come from somewhere else.

---

## Restore steps

### 0. Prerequisites
- macOS on Apple Silicon
- Homebrew, git, Python 3.11+ (`python3 --version`)
- A GitHub account with access to this repo

### 1. Install Hermes
```bash
# follow the official installer, then confirm:
hermes --version
```

### 2. Clone this repo
```bash
git clone https://github.com/lifetofree/phon-hermes.git ~/Desktop/hermes-restore
cd ~/Desktop/hermes-restore
```

### 3. Restore skills
```bash
mkdir -p ~/.hermes/skills
rsync -a hermes-skills/ ~/.hermes/skills/
```
Skills are self-contained — no external symlinks needed.

### 4. Restore agent identity and config
```bash
mkdir -p ~/.hermes
cp hermes-profile/SOUL.md ~/.hermes/SOUL.md
cp hermes-profile/config.yaml ~/.hermes/config.yaml
```

### 5. Restore secrets (NOT from this repo)
Rebuild `~/.hermes/.env` with these 6 secrets plus the non-secret settings:

Secrets:
- `TELEGRAM_BOT_TOKEN`
- `DISCORD_BOT_TOKEN`
- `OPENROUTER_API_KEY`
- `KILOCODE_API_KEY`
- `HERMES_CUSTOM_LOCALHOST_20128_API_KEY`
- (any additional provider keys you use)

Non-secret values to copy verbatim:
```
TERMINAL_ENV=local
TERMINAL_TIMEOUT=60
TERMINAL_LIFETIME_SECONDS=300
BROWSER_INACTIVITY_TIMEOUT=120
BROWSER_SESSION_TIMEOUT=300
TELEGRAM_ALLOWED_USERS=8780418515
TELEGRAM_HOME_CHANNEL=8780418515
DISCORD_ALLOWED_USERS=<your discord user id>
DISCORD_HOME_CHANNEL=general
DISCORD_REQUIRE_MENTION=false
GOOGLE_CHAT_PROJECT_ID=khaoklong-claw
KILOCODE_BASE_URL=https://api.kilo.ai/api/gateway
```

Set permissions:
```bash
chmod 600 ~/.hermes/.env
```

### 6. Restore memory (personal, if you have a copy)
```bash
mkdir -p ~/.hermes/memories
cp <your-secure-copy>/MEMORY.md ~/.hermes/memories/
cp <your-secure-copy>/USER.md    ~/.hermes/memories/
```

### 7. Re-authenticate Google (tokens cannot be copied meaningfully)
```bash
hermes auth google
```

### 8. Verify
```bash
hermes --version
hermes doctor          # if available
hermes                 # start a session, ask it to list its skills
```
Checks:
- skills appear and load
- Telegram bot responds
- Google Tasks/Calendar works
- agent tone matches SOUL.md

---

## The honest gap

A backup is only as good as its weakest layer. Current state:

| Layer | Status | Risk |
|---|---|---|
| Agent definition (skills, SOUL, config) | Backed up weekly to GitHub | Low |
| Secrets (`.env`, OAuth) | **Not backed up anywhere** | Disk failure = re-issue every key by hand |
| Memory + chat history (`state.db`, 80 MB) | **Not backed up** | Loss of all continuity |
| Whole-machine backup (Time Machine) | **Not configured at all** | Any SSD failure = total loss |

Time Machine is the single highest-value fix: it covers all four layers at once with zero manual work.
