# STATE.md — UDO

## Current State
- Knowledge Base DB created in Notion (2026-08-27)
  - Name: "Knowledge Base"
  - DB ID: `3c9df8d8-8d8c-81ac-ba5e-fa129e493638`
  - URL: https://app.notion.com/p/3c9df8d88d8c81acba5efa129e493638
  - Parent page: "Hermes agents" (`3c7df8d8-8d8c-801c-87f9-e845700178af` = PARENT_PAGE_ID in .env)
  - Schema: Title, Summary, Category (tech/life/work/reference), Tags, Source, Created, Updated, Status (active/archived/deprecated)
- Notion token: valid (bot "Hermes-connection"), stored as NOTION_TOKEN in /home/lifetofree/hermes-agent/.env
- **ComfyUI (2026-09-03): ติดตั้งแล้ว แต่ models ยังไม่ได้โหลด — หยุดพักก่อน restart เครื่อง**
  - Repo: `~/ComfyUI` (git clone comfyanonymous/ComfyUI, depth 1)
  - Venv: `~/ComfyUI/.venv` (Python 3.12, สร้างด้วย uv)
  - torch **2.14.0+cu130** + torchvision 0.29.0 — **CUDA verify ผ่าน** (2 GPUs, dev0 = RTX 5060 Ti, compute cap 12.0/Blackwell)
  - `requirements.txt` install เสร็จ
  - Models: **0/8 เสร็จ → download resume 2026-09-05** (background job, single instance)
  - Download script สำรอง: `~/ComfyUI/download_models.sh` — **resumable** (curl -C -) รันซ้ำได้ปลอดภัย
  - **⚠️ URL แก้แล้ว 2026-09-05** — 5 ไฟล์ baseline ใช้ URL เดิมผิด (404/401) แก้แล้ว:
    - z_image VAE: จริงชื่อ `ae.safetensors` (save as z_image_vae)
    - clip_vision_g: repo `comfyanonymous/clip_vision_g` (ไม่ใช่ hubert23)
    - IPAdapter plus/standard: `h94/IP-Adapter/sdxl_models/` (ไม่ใช่ models/)
    - faceid plusv2 sdxl lora: `h94/IP-Adapter-FaceID/` (แยก repo)
    - fix job: `~/ComfyUI/download_models_fix.sh` (rerun 5 ไฟล์นี้)
  - **Extras (2026-09-05): `~/ComfyUI/download_models_extra.sh`** — Wan2.2 5B fp8, umt5 fp8, wan2.2_vae, flux1-dev-fp8, controlnet union sdxl, RealESRGAN x4plus, antelopev2 (URLs verify ผ่าน HF tree API) — extras 19.6GB + antelopev2 360MB
- **DONE (2026-09-06 11:13): Models ครบทั้ง set** — ALL_DONE 11:13 (+07). baseline 8 + extras 7 ครบ (verify ls ครบ 14 ไฟล์ + antelopev2): sd_xl_base 6.9G, z_image_turbo_bf16 12G, qwen_3_4b 8G, z_image_vae 335M, clip_vision_g 3.7G, ip-adapter plus 847M / standard 698M / faceid lora 371M, wan2.2 4.7G, umt5 fp8 6.7G, wan2.2_vae 1.4G, flux1-dev-fp8 11.9G, controlnet_union_sdxl 2.5G, RealESRGAN 67MB, antelopev2 360MB

## Open Tasks
- **DONE (2026-09-07): LM Studio intro long-form draft** — research primary (lmstudio.ai home + docs: system-requirements, basics, lmstudio-vs-llmster-vs-lms, rag, mcp, bionic, lmlink, rest quickstart, pricing + api.github.com lms) + draft ลง Content Drafts DB:
  - Notion page: `3d4df8d8-8d8c-8171-bc39-de13b7c6d7a7` (71 blocks, has_more=False, Status: draft — verify read-back ครบ; URL: https://app.notion.com/p/3d4df8d88d8c8171bc39de13b7c6d7a7)
  - ไฟล์: `content-study/posts/20260907-cnt-lm-studio-local-llm-intro.md` (pushed)
  - มุม: "GUI-first local LLM" — 3+1 tools (app/llmster/lms + Bionic agent), LM Link (Tailscale E2E, 5 dev, app Locally), RAG, MCP host, port 1234 OpenAI/Anthropic compat; cons: app proprietary (CLI MIT), no Intel Mac, Linux AppImage-only, Bionic plans TBA; เทียบ 4 ตัว (vs Ollama/Unsloth Studio/llama.cpp); cross-ref Ollama + Tailscale + Unsloth series
  - Notion pitfall: Content Drafts DB `Date` prop = date type (not title) + ต้อง header `Notion-Version: 2022-06-28`
- **DONE (2026-09-07): Unsloth Studio no-code fine-tuning long-form draft** — research primary (unsloth.ai/docs/new/studio + /install + /start + /data-recipe + /export, unsloth.ai/docs requirements, unslothai.substack.com launch post, GitHub unslothai/unsloth API) + draft ลง Content Drafts DB:
  - Notion page: `3d4df8d8-8d8c-812e-8816-fc5ba5623c13` (77 blocks, has_more=False, Status: draft — verify read-back ครบ; URL: https://app.notion.com/p/Unsloth-Studio-Fine-tune-AI-GPU-long-form-3d4df8d88d8c812e8816fc5ba5623c13)
  - ไฟล์: `content-study/posts/20260907-cnt-unsloth-studio-no-code-finetune.md` (push fb9e401)
  - มุม: "Fine-tuning ที่เคยเป็น script กลายเป็น button" — no-code training pipeline (Data Recipes visual workflow powered by NVIDIA Nemo → QLoRA/LoRA/full fine-tune → live monitor → export GGUF/safetensors/LoRA), agentic layer (self-healing tool calls, sandboxed Bash/Python, private web search), MLX/Mac training, 2x faster / 70% less VRAM, free Apache-2.0, 75,748 stars, v0.1.806-beta; cons: still Beta ~6 months, training needs GPU (Windows=NVIDIA only), not production serving, 1,352 open issues; เทียบ 5 ตัว (vs Ollama/LM Studio/Unsloth Core/Colab)
  - Disambiguation: user พิมพ์ "Unsloth Studio" (รอบแรก typo แล้วแก้, รอบ 2-3 ยืนยันชัด = Unsloth ไม่ใช่ LM Studio) — ทำตาม Unsloth
- **DONE (2026-09-07): Ollama local-LLM part 2 — server/datacenter angle** — research primary (docs.ollama.com/api: base URL localhost:11434, OpenAI/Anthropic-compatible, /api/chat|generate|embed; /docker: NVIDIA Container Toolkit + --gpus=all, rocm tag, Vulkan bundled; /gpu: compute cap 5.0+, multi-GPU CUDA_VISIBLE_DEVICES by UUID, GPU list 50xx→V100) + draft ลง Content Drafts DB:
  - Notion page: `3d4df8d8-8d8c-8139-a89f-cf4038cbdde0` (71 blocks, has_more=False, Status: draft — verify read-back ครบ; URL: https://app.notion.com/p/Ollama-Local-LLM-on-Server-AI-Infrastructure-part-2-server-datacenter-3d4df8d88d8c8139a89fcf4038cbdde0)
  - ไฟล์: `content-study/posts/20260907-cnt-ollama-local-llm-server-datacenter.md` (push e1750cb)
  - มุม: "ทีม 5-50 คน build AI infra ของตัวเอง" — per-token $0, OpenAI/Anthropic-compatible API (zero code change), multi-GPU scheduling, Docker prod pattern, capex $2-3.5k (1×4090), cons: admin 2-4hr/week, uptime your problem, no multi-tenancy, open < closed frontier; เทียบ 4 ทาง (Ollama server / cloud API / vLLM-TGI / Ollama cloud tier)
- **DONE (2026-09-07): Snapzy (snapzy.app) intro long-form draft** — research primary (snapzy.app site, docs getting-started, GitHub README/release v1.31.0 API, macmenubar.app, CleanShot X pricing Aug 2026) + draft ลง Content Drafts DB:
  - Notion page: `3d4df8d8-8d8c-81f2-b274-da7e704aa141` (59 blocks, has_more=False, Status: draft — verify read-back ครบทุก section + hashtags; URL: https://app.notion.com/p/Snapzy-Mac-open-source-CleanShot-X-29-long-form-3d4df8d88d8c81f2b274da7e704aa141)
  - ไฟล์: `content-study/posts/20260907-cnt-snapzy-macos-screenshot-intro.md` (push b69782a)
  - มุม: "CleanShot X แต่ $0" — free OSS (BSD-3), 3,068 stars, crowdfund $99 Apple Dev Program goal, BYO S3/R2 cloud, OCR/auto-redaction, macOS 13+; cons: project 8 เดือน, cloud DIY, no Thai UI, single maintainer
  - Disambiguation: "Snapzy" มี 3 ตัว — user clarify timeout → เลือก snapzy.app (recommend) ตาม style guide audience
- **DONE (2026-09-05): Ollama laptop/portable local-LLM draft (part 1, laptop angle)** — research primary (ollama.com + docs.ollama.com quickstart/gpu/macos/windows/context-length/pricing) + draft ลง Content Drafts DB:
  - Notion page: `3d2df8d8-8d8c-81dc-87db-fbc91cf9e1d1` (60 blocks, has_more=False, Status: draft — verify read-back ครบ: h1+h2, 1 hardware table, closing, hashtags; URL: https://app.notion.com/p/Ollama-Local-LLM-laptop-AI-offline-portable-3d2df8d88d8c81dc87dbfbc91cf9e1d1)
  - ไฟล์: `content-study/posts/20260905-cnt-ollama-local-llm-laptop-portable.md` (push 2743a43)
  - มุม (ตามที่ user สั่ง): NOT server — "laptop ตัวเอง พก LocalLLM ไปได้ทุกที่" offline + private + portable; hardware table (Apple M / RTX / CPU-only), quantization, battery/disk cons; **part 2 DONE 2026-09-07** (server/datacenter angle — see below)
  - "Olamma" ใน request = typo ของ Ollama (disambiguated)
  - Note: part 1 มีอีกไฟล์ `20260905-cnt-ollama-local-llm-intro.md` (push 9c1868c) = intro/generic angle, ยังไม่ได้ลง Notion (รอ user ตัดสินใจ)
- **DONE (2026-09-04): AutoClaw x ZCode combo content** — draft ลง Content Drafts DB:
  - Notion page: `3d1df8d8-8d8c-815e-9bcf-d1ed68a2b49d` (46 blocks, verify read-back ครบ — 2 ตาราง + hashtags + social footer; URL: https://app.notion.com/p/AutoClaw-ZCode-2-1-Workflow-Design-Deploy-draft-3d1df8d88d8c815e9bcfd1ed68a2b49d)
  - ไฟล์: `content-study/posts/20260904-cnt-autoclaw-zcode-combo.md` (push 90812fc)
  - มุม: "2 เครื่องมือ 1 แผน" — GLM Coding Plan เป็น shared subscription layer ของ ZCode + AutoClaw + Claude Code; workflow design->code (ZCode Goal Mode) -> deploy/verify/content ops (AutoClaw) -> สั่งจากมือถือทั้งคู่; pricing Lite $12.6/Pro $56/Max $117.6 (โปร 20%); cons: vendor lock-in, "local" != data-stays-local, access contract แยก
- **Models (2026-09-05 ~17:40):** โหลดเสร็จ 3 — sd_xl_base (6.5G), z_image_turbo_bf16 (12G), wan2.2_ti2v_5B_fp8 (4.7G). กำลังโหลด 2 — qwen_3_4b (3.2/~4.2G), umt5_xxl_fp8 (2.2/~6.7G). ยังไม่เริ่ม ~13G: z_image_vae (จำเป็นสำหรับ Z-Image), clip_vision_g, IP-Adapter ×3, flux1-dev-fp8, controlnet_union_sdxl, RealESRGAN, antelopev2. ทั้ง 2 script รันอยู่ (main PID 934365, extras PID 985052), รวม ~3.5-4 ชม. จะครบ
- หลัง models ครบ: เริ่ม ComfyUI ตาม KB — port **8188**, ComfyUI ใช้ **GPU 0**, Hermes LLM ใช้ GPU 1
  - `cd ~/ComfyUI && .venv/bin/python main.py --listen 0.0.0.0 --port 8188`
- Resume command (รันตัวเดียวเท่านั้น!): `cd ~/ComfyUI && nohup bash download_models.sh > /tmp/models_download.log 2>&1 &`
- (จากก่อนหน้า) slug + excerpt content 9router — user ยังไม่ได้เลือกตัวเลือก

## Pitfalls เรียนรู้วันนี้ (ComfyUI setup)
- **`download.pytorch.org` ถูก throttle ~246 B/s** (ใช้ไม่ได้) — ติด torch จาก PyPI ปกติแทน (`uv pip install torch torchvision`) ได้ 1.6 MB/s และ PyPI torch = build cu128+/cu130 รองรับ Blackwell ได้เลย
- pypi.nvidia.com ช้ามาก (~100 KB/s) — อย่าใช้ index-url ของ torch directly
- **อย่ารัน download script ซ้ำซ้อน 2 ตัว** — เขียนทับ .part เดียวกัน → corrupt (เจอจริงวันนี้)
- huggingface.co จากเครื่องนี้ ~1.5 MB/s — ถ้าช้าให้ลอง mirror `hf-mirror.com` แทน `huggingface.co` ใน URL (path เดียวกัน)

## Recent Activity
- 2026-09-06: **Weekly WP archive sync ตั้งแล้ว** — cron `972b24976bf0` "weekly-wp-archive-sync" (no_agent=true, script-only, free token) ทุกวันอาทิตย์ 10:00 +07; script `~/.hermes/scripts/sync_wp_posts.py`: fetch wp.adduckivity.com via WP REST API (paginated) → diff slug vs `content-study/index.json` → post ใหม่ save เป็น markdown ที่ `content-study/web-archive/<slug>.md` (header มี title/date/link) + append index.json (link = live URL) + git commit+push. Watchdog: ถ้าไม่มี post ใหม่ = silent (no delivery). ทดสอบจริงวันตั้ง: archive 4 post (9router, tailscale-serve, autoclaw x2) — index.json 259. ถ้าเว็บ add post ระหว่างสัปดาห์ job จะเก็บรอบถัดไป
- 2026-09-06: Content draft **System Audit (Dopamine Nation Ch.8)** — standalone (ไม่ผูก series ตาม user), ~860 words, มุม "The System Audit = Truthful Autobiography + scan Foibles" (ไม่ซ้ำ radical-honesty-patch เดิม: มี protocol AUDIT-08 3-step + case Maria + 4 checks); ไฟล์ `content-study/posts/20260906-cnt-system-audit-foibles-scan.md` (push b7b00d9) + index.json (255); ลง Content Drafts DB page `3d3df8d8-8d8c-8151-8d6f-ff05152550c2` (Status: draft, verify read-back 115 blocks ครบ + closing hashtags)
- 2026-09-06: ComfyUI models ครบทั้ง set (14 ไฟล์ + antelopev2) — ALL_DONE 11:13
- 2026-09-04: AutoClaw x ZCode combo draft เสร็จ — research primary (zcode.z.ai/en, docs.z.ai setup, Goal Mode, Bot Channel, autoclaw.z.ai quota boost) + daisuke.masuda.tokyo stack overview; draft "2 เครื่องมือ 1 แผน" ลง Content Drafts DB (page 3d1df8d8-8d8c-815e-9bcf-d1ed68a2b49d, verify read-back 46 blocks + ตาราง 2 ตัว ครบ); ไฟล์ posts/20260904-cnt-autoclaw-zcode-combo.md push 90812fc; Notion pitfall ใหม่: POST /v1/pages ใส่ `children: []` ควบกับ `markdown` = 400 — ใช้ `markdown` อย่างเดียว
- 2026-09-04: sync Tailscale Serve longform **v2** (commit 083f2ba) ขึ้น Notion แทนเนื้อเดิม — PATCH markdown `type: replace_content` (body shape: `{"type":"replace_content","replace_content":{"new_str": md,"old_str":""}}`) ที่ page `3d0df8d8-8d8c-81d2-9756-d310044ae3a0` (Status: draft); verify read-back 172 lines ครบ (first/last + markers ตรง)
- 2026-09-03: Superclick long-form draft เสร็จ — research จาก superclick.app (site/pricing/faq/eula) + Reddit r/macapps launch thread (1i7klqu); draft ลง Content Drafts DB (draft): notion page 3d0df8d8-8d8c8175-a34e-fcbbee3194d9, verify read-back 95 blocks ครบ; ไฟล์ ~/hermes-agent/content-study/posts/20260903-cnt-superclick-intro-longform.md push (967e0e7)
- 2026-09-03: AutoClaw (Zhipu/Z.ai) long-form draft เสร็จ — research จาก primary sources (autoclaw.z.ai, GLM-5.3-Flash specs, GLM pricing, BestClaw review 6.9/10) + draft ลง Content Drafts DB:
  - Notion page: `3d0df8d8-8d8c-81ef-a414-c7cf29cea032` (132 blocks, verify read-back ครบ — headings, pricing tables, tail hashtags)
  - ไฟล์: `content-study/posts/20260903-cnt-autoclaw-intro-longform.md` (push แล้ว b362f02)
  - มุม: "one-click OpenClaw สำหรับคนที่ไม่อยาก configure" — free 5,000 credits + daily, Coding Plan $18/72/160, promo GLM-5.3-Flash $0.075/$0.25 หมด 9 ก.ย.
- 2026-09-03: ท้ายวัน — ปรับ draft Tailscale serve ทั้ง 2 ตัวเป็นมุม "ใช้เองก่อน" (unsloth 8888 / ComfyUI 8188 / llama 8080 จากเครื่องตัวเอง + section แยกชั้น MagicDNS-vs-serve) แล้วลง Content Drafts DB (`3ccdf8d8-8d8c-81ae-bdf8-cb9eb1821520`) Status: draft — verify read-back ครบทั้ง 2 หน้า:
  - short: `3d0df8d8-8d8c-810d-9892-cc1a1bc89e01` (74 blocks)
  - longform: `3d0df8d8-8d8c-81d2-9756-d310044ae3a0` (144 blocks)
  - ไฟล์ต้นฉบับ: `content-study/posts/20260903-cnt-tailscale-serve.md` + `-longform.md` (push แล้ว a872c86)
  - Note: Content Drafts DB props = Name/Topic/Status/Date/Platform/Source — ใช้ `POST /v1/pages` พร้อม `markdown` param ได้
- 2026-09-03: ComfyUI setup — clone repo, venv, torch cu130 verify GPU OK, requirements สำเร็จ; models 0/8 (หยุดตาม request ก่อน restart)
- 2026-08-27: สร้างหน้า "Tailscale — Mesh VPN บน WireGuard สำหรับเข้าถึงอุปกรณ์ส่วนตัว" ใน KB
  - Page ID: `3c9df8d8-8d8c-8121-925f-ed6030d82b76`
  - Category: tech | Tags: networking, vpn, wireguard, security, self-hosted | Status: active
