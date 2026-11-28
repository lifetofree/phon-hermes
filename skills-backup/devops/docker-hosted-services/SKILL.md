---
name: docker-hosted-services
description: Use when debugging auth/network for Docker apps here.
version: 1.0.0
author: Phon Chantararat (lifetofree), Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Docker, Rakazo, GitHub, Auth, Debugging]
---

# Docker-Hosted Services on PHON-SERVER

Operate and debug self-hosted Docker app stacks (rakazo) on this server: container→host endpoints, GitHub auth for bot containers, secret wiring. Stack facts live here; the llama-server side of the endpoint is in the local-llm-serving skill.

## When to Use
- A Docker-hosted app can't reach a host service (e.g. llama-server at :8080) or a GitHub push from inside a container fails (403).
- User asks to wire/verify an endpoint into rakazo, or re-authenticate a bot container.

## Stack facts (rakazo, PHON-SERVER)
- Compose project at `~/rakazo`: `docker-compose.images.yml` + `.env`, prebuilt GHCR images `ghcr.io/elie222/rakazo/*:edge` (NOT a git clone — upstream repo github.com/elie222/rakazo). Services: api/web/worker/supervisor/postgres + bot computer containers named `rakazo-bot-team-<hash>`.
- llama-server endpoint for containers: `http://host.docker.internal:8080/v1`. It resolves because compose sets `extra_hosts: ["host.docker.internal:host-gateway"]` → 172.17.0.1, and llama-server binds 0.0.0.0. Fallback host IPs (verified reachable): LAN `192.168.1.148`, tailscale `100.73.21.109`.
- rakazo images have NO curl/wget — test HTTP from inside with `docker exec <svc> node -e "fetch('...').then(r=>r.text()).then(console.log).catch(e=>console.log('ERR:',e.message))"`.
- Thinking-model caveat for consumers: Qwen empties `content` when `max_tokens` is consumed by `reasoning_content` — raise max_tokens or disable thinking in the client.

## Procedure: container→host endpoint check
1. `docker inspect <svc> --format '{{json .HostConfig.ExtraHosts}}'` — `host.docker.internal` resolves on Linux only with the `host-gateway` mapping.
2. `docker exec <svc> getent hosts host.docker.internal` — confirm what it resolves to (172.17.0.1 here).
3. Real HTTP proof from inside: node fetch against `/health` (see command above). Done when health JSON comes back.

## Procedure: GitHub push 403 from a bot container
1. `git -C <repo> remote get-url origin` — confirm target repo; if credentials are embedded, mask them in any printed output (`sed -E 's#(https://)[^@/]+@#\1[MASKED]@#g'`).
2. `git config --list | grep credential` — rakazo bot uses `gh auth git-credential`, so the push credential = whatever `gh auth` holds in THAT container. Check the container that performs the push, never the api container: secrets wiring differs per service (a `GITHUB_TOKEN` secret defined in rakazo is verified to NOT reach the bot container env).
3. `gh auth status` — "You are not logged into any GitHub hosts" = anonymous push = the 403. Fixing the secret's value alone does not fix pushes; the credential must land in the container.
4. Fix: `gh auth token` (host side) piped → `docker exec -i <bot> gh auth login --with-token`. Verify: `gh auth status` shows account lifetofree; `gh api repos/lifetofree/phon-hermes --jq .permissions` returns push:true; `git -C <repo> push --dry-run origin <branch>` succeeds.
5. Recurring maintenance: rakazo recreating a bot computer wipes `~/.config/gh` → 403 returns. Re-run step 4 (owner decision: master PAT during trial phase; switch to a fine-grained phon-hermes-only token later).

## Pitfalls
- Never print/echo a PAT. Compare "same token?" claims by piping the token string to `sha256sum` and comparing fingerprints. If the sed extraction from a URL doesn't match, the hash is of the whole URL — and hash `e3b0c442…` is the empty string (gh auth token while logged out); confirm token length before trusting any comparison.
- Empty `content` + `finish_reason: length` from a Qwen-style thinking model is a client budget issue, not a server failure — re-test with a larger `max_tokens` before diagnosing further.
- Diagnose in the container that performs the action: host-level `.env` and the api container's env can both be clean while the bot container lacks the credential entirely.
