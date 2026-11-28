# Discord Gateway — Thread Handling

How to run threads on the user's Discord server: when a thread may exist, how to get the first post INSIDE it, and how to prove placement. Verified against the live gateway.

## Standing policy

- Channels listed in `discord.no_thread_channels` (config.yaml) get INLINE replies with an @mention — never create a thread there unprompted, even for a test.
- Create a thread ONLY on an explicit owner command, and say so when reporting.
- Once the owner has posted inside the thread, the gateway routes replies there automatically ("Hermes replies in the same thread") — normal chat replies just work from then on. The special delivery below is needed only for the FIRST post after creation, while the conversation's source chat is still the parent channel.

## Workflow: owner-ordered thread

1. **Create** — discord tool `create_thread(channel_id, message_id, name)` anchored to the owner's triggering message. The returned `thread_id` equals the anchor message_id and IS the real thread channel ID (type 11, parent = channel id — cross-check via Discord REST `GET /guilds/{guild}/threads/active` with bot authentication, if in doubt).
2. **Post the reply INSIDE the thread** — the normal chat reply goes to the source channel (the parent), and the discord tool has no send action. Deliver the first in-thread post from the shell:

   ```bash
   hermes send --to discord:<channel_id>:<thread_id> "message"
   ```

   Target format is `platform:chat_id:thread_id`.
3. **Verify by read-back** — a successful CLI delivery returns only the word `sent` as its whole output; exit 0 does not prove placement. Call discord `fetch_messages(channel_id=<thread_id>)` and confirm the new message id and thread name before reporting success.
4. **Report in the parent channel** with one line (thread created + reply posted inside), so the owner sees status where they are.

## Pitfalls

- After `create_thread`, replying normally lands the message in the PARENT channel, not the thread — the gateway routes chat replies to the conversation's source chat, and nothing in the discord toolset can post into a thread. Use the CLI delivery above for the first in-thread post.
- To enumerate threads or find a thread's real channel ID, query Discord REST `GET /guilds/{guild}/threads/active` with bot authentication — the parent channel's message list does not show thread membership or IDs.
