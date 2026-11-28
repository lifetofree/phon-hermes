---
name: huggingface-model-downloads
description: Use when downloading HF model weights or a fetch 404s/401s.
---

# Hugging Face model downloads

Use when downloading model weights from Hugging Face (ComfyUI models, GGUF, diffusion checkpoints, any large `.safetensors`/`.pth`/`.gguf` fetch), or when a download 404s/401s and you need to find the real repo path.

## Verify repo path FIRST — never download from a guessed URL

The #1 failure mode is a 404 because the KB/wiki/memory lists the file under a path that doesn't exist in the repo (real filenames differ from display names: e.g. the Z-Image VAE file is actually `ae.safetensors`, not `z_image_vae.safetensors`). Always verify with the HF tree API before downloading:

```bash
curl -s "https://huggingface.co/api/models/<repo>/tree/main?recursive=true" | \
  python3 -c "import sys,json; [print(x['path'], x['size']) for x in json.load(sys.stdin) if x['type']=='file' and 'safetensors' in x['path']]"
```

- Repo name is case-sensitive in API calls; a wrong case may return a text redirect instead of JSON — follow it.
- The model search API needs URL-encoded params (`curl -sG --data-urlencode 'search=...'`); plain `?search=` returns non-JSON.

## 401 on resolve = GATED repo, not a network problem

`https://huggingface.co/<repo>/resolve/main/<file>` returns **401 for gated repos regardless of User-Agent**. 404 = wrong path; 401 = repo needs an HF token + license acceptance. The models search API shows `gated: true` — check before burning time.

FLUX.1-dev weights were gated (401) in early 2026-09, but `black-forest-labs/FLUX.1-dev-FP8` downloaded FINE without a token on 2026-09-05 (11.9G, official URL) — gates may be per-file/IP/transient, so test the official URL first before assuming it is blocked. Fallback: ungated community mirror `jellyhe/flux1-dev-fp8` (11.9G, `resolve` 302→CDN works, size within ~3% of official). If the machine has `~/.cache/huggingface/token` and the user has accepted the license, prefer the official repos — ask, don't assume.

## Download mechanics

- `curl -L -C - -A "Mozilla/5.0" -o dest.part <url>` then `mv dest.part dest` — resumable, safe to re-run.
- Concurrent download jobs are fine AS LONG AS every job's targets are unique — the 2026-09-05 corruption incident was two instances writing the SAME `.part` file. One script per target set.
- HF throttles some repo+IP combos (seen `comfyanonymous/clip_vision_g` at ~400KB/s on 2026-09-05, then the same file at ~3.5MB/s on 2026-09-06) — throttling is TRANSIENT, not permanent; just wait on a resumable download. `hf-mirror.com` was NOT a reliable fallback (tested 2026-09-05: 0 bytes on a 3.4G file). If a file is slow, report the honest ETA rather than hunting mirrors blindly.
- Verify download completeness: `curl -sI -A "Mozilla/5.0" <resolve-url> | grep -i x-linked-size` gives the exact remote byte count (works on ungated files with a browser UA; 302 + `x-linked-size` header). Compare against the on-disk `ls -l` size — exact match = complete. Better than re-reading the whole log.
- Launching long downloads in Hermes: a foreground terminal command containing `nohup ... &` is REJECTED by the runtime. Use `terminal(command="bash download_models.sh", background=true)` with watch patterns (`notify=["OK:", "FAIL:", "ALL_DONE"]`) and poll via `process(action='wait'/'log')`. Keep scripts idempotent-resumable per file: `if [ -f dest ]; skip; fi` + `curl -C - -o dest.part && mv dest.part dest`, so re-running after a crash/timeout is safe.
- Background job output buffers are capped (~2580 lines): audit a long download job from the persisted log file, not from what you remember seeing.

## Verified model URL bank (ComfyUI)

See `references/comfyui-model-urls.md` for the verified repo/file pairs from this machine (SDXL, Z-Image, Wan 2.2 5B, FLUX.1-dev fp8, ControlNet union, RealESRGAN, IPAdapter, insightface) and the correct on-disk layout for `~/ComfyUI/models/`.