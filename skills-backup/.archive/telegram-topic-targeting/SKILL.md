---
name: telegram-topic-targeting
description: "Use when routing delivery to a named Telegram forum topic."
---

# Telegram topic targeting

When a request names a Telegram FORUM TOPIC (e.g. "move the job to topic Contents") and the delivery target must be `telegram:<chat_id>:<thread_id>`. The chat_id is usually already known from the job's current deliver (cronjob_manage list); only the thread_id needs resolving.

## Resolving topic name → thread_id

The Bot API cannot enumerate forum topics: `getChat` on a forum group returns no `forum_topics`/`active_forum_topics` key (verified against the live bot token), and there is no list-topics endpoint for bots. Work the local sources in order:

1. `~/.hermes/channel_directory.json` — lists known `chat:thread` targets (generic "topic N" names only, no topic names).
2. `sqlite3 ~/.hermes/state.db "SELECT thread_id, title FROM sessions WHERE thread_id IS NOT NULL ORDER BY started_at"` — thread → session-title heuristic (a topic's past session titles hint at its purpose); the `gateway_routing` origin JSONs carry thread_id + message_id per thread too.
3. `~/.hermes/logs/gateway.log` inbound-message lines carry `reply_to_id` (weak signal only).
4. If the name still doesn't resolve: ask the user for the topic's shared link (the link's `thread-id=XXXX`) — the ONLY authoritative name source. Present the known mapping table (from 1–3) plus a free-text option; never guess between candidate IDs (a wrong ID delivers every run of the job into the wrong topic, and a clarify built on guesses can time out before it lands).

## Applying the target

cronjob_manage action=update, job_id=<id>, deliver="telegram:<chat_id>:<thread_id>" → list again and verify the deliver field changed. Failure notices follow deliver unless failure_deliver is set.

## Pitfalls
- Thread id 1 in a forum group is General, not "the first topic" — don't conflate.
- A session title is a heuristic, not a topic name; only the user-provided shared link is authoritative for the name.
- The constraint is on ENUMERATION, not delivery: posting to any `chat:thread` works fine — don't carry "the API can't do X" into future refusals.
