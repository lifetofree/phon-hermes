---
name: macos-services
version: 1.0.0
author: KhaoKlong (Hermes)
license: internal
metadata:
  hermes:
    tags: [macos, launchd, launchagents, comfyui, services]
    related_skills: [rakazo-ops, local-llm-serving]
description: "Operate macOS background services (LaunchAgents) over SSH."
---

# macOS background services over SSH (owner's Mac, Tailscale)

## When to Use
- Any task that starts/stops/disables/installs a background service on the owner's Mac remotely (`ssh lifetofree@100.107.249.87`) — LaunchAgents, always-on servers, auto-start cleanup, or checking why a Mac-side service (e.g. ComfyUI for image generation) is or isn't reachable.

## Standing rules
- Everything reversible: disabling = `launchctl bootout gui/$(id -u)/<label>` + move the plist to `~/Library/LaunchAgents-disabled/` (never delete — restore is move back + `launchctl load`); installing = scp the plist + `launchctl load`. RunAtLoad + KeepAlive for always-on servers.
- Verify with three independent probes before reporting success: `launchctl list | grep <label>`, `pgrep -f <process-pattern>`, and the service's own port/endpoint (`lsof -iTCP:<port> -sTCP:LISTEN` + curl a health path). "plist moved" is not "service down" — bootout can leave the process running, so pgrep and kill the leftover PID explicitly.
- Never run the Comfy Desktop app alongside the headless ComfyUI agents — port 8188 collision.
- The Mac sleeps after ~1h idle: long generation queues stall until it is woken; plan around it for batch jobs.

## ComfyUI instances (queue isolation)
- One ComfyUI instance = one shared FIFO queue: a bulk batch head-of-line-blocks every other client, so "isolate by queue" means "separate instance on another port with its own `--output-directory`" — port-level isolation does not exist within one instance.
- Current split: 8188 = production/ebook (`com.lifetofree.comfyui-headless`), 8189 = image-gen bot only (`com.lifetofree.comfyui-imagegen`, output `ComfyUI-Shared/output-imagegen`). Point only the owning bot's instruction + template at its port; a shared template file at the old port defeats the isolation.
- Both instances share one GPU: concurrent generation works but per-image throughput drops — expected, not a fault.
