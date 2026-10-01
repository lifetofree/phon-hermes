# Tailscale Serve/Funnel — verified research (2026-09-03)

Sources: tailscale.com/docs/features/tailscale-serve (validated Jan 20, 2026), /docs/reference/tailscale-cli/serve (Jan 26, 2026), /docs/features/tailscale-funnel, /pricing. For the adduckivity Tailscale series (part 1: 20260824-CNT-TAILSCALE-REMOTE-ACCESS, part 2: 20260903-CNT-TAILSCALE-SERVE long form; draft in posts/20260903-cnt-tailscale-serve-longform.md). Planned part 3: Funnel + rate limiting/quota for public LLM endpoints.

## Serve essentials
- `tailscale serve localhost:8080` → HTTPS on https://device.tailnet.ts.net; TLS auto-provisioned; no port-forward; survives device sleep (traffic via tailscaled, not an SSH session).
- CLI syntax CHANGED in client v1.52: target-based (`serve localhost:8080`); old `serve 443 --bg http://...` tutorials are outdated. Subcommands: status, reset, drain, advertise, get-config, set-config.
- Target types: port, partial URL, full URL (tcp://…/foo, https+insecure://…), file/dir path, text:"…". Reverse proxy only supports http://127.0.0.1 backends.
- Flags: --https/--http (HTTP reachable via short MagicDNS name http://my-node), --tcp, --tls-terminated-tcp, --proxy-protocol=2 (preserves client source IP to backend), --set-path, --bg, --accept-app-caps (v1.92+).
- Requires HTTPS certs enabled in tailnet (interactive consent page sets it up); ACLs apply to Serve traffic.

## Identity headers (Serve only, not Funnel)
- Injected: Tailscale-User-Login (alice@example.com), Tailscale-User-Name, Tailscale-User-Profile-Pic. Stripped from incoming requests to prevent spoofing. Not populated for tagged devices. RFC2047 Q-encoding for non-ASCII.
- Killer use case: shared local LLM server — backend knows who's asking with zero auth system; per-user quota from the header.
- Best practice: backend must listen on localhost only, else anyone can forge headers. Grafana auth-proxy compatibility documented.

## Funnel (public)
- Beta; all plans. Internet → Funnel relay → encrypted TCP proxy → device. Relay can't decrypt; device IP hidden.
- Requires v1.38.3+, MagicDNS, HTTPS, funnel node attribute in policy. Ports 443/8443/10000 only, TLS only, non-configurable bandwidth limits.
- Same port can't be both Serve and Funnel — last command wins (funnel last = port becomes public).

## Pricing (checked Sep 2026, seat-based)
- Personal: $0 forever — unlimited user devices, up to 6 users, 3 ACL groups, 50 tagged resources.
- Standard $8/user/mo; Premium $18/user/mo (300 groups, flow logs, JIT); Enterprise custom.

## Limitations
- DNS names only under device.tailnet-name.ts.net.
- macOS: file/dir serving only in the open-source client variant (App Store sandbox).

## Content angles used / left
- Used (part 2): SSH-tunnel pain → serve one-liner; identity headers for LLM auth; v1.52 syntax change (old tutorials wrong); serve-vs-funnel table.
- Left for part 3: Funnel + rate limiting/quota (public = anyone burns your GPU), identity headers + Grafana auth-proxy walkthrough.
