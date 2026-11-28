# ComfyUI model URLs — verified 2026-09-05/06 on PHON-SERVER (all 14 files + antelopev2 downloaded OK)

All verified via HF tree API (`/api/models/<repo>/tree/main?recursive=true`) with matching sizes; sizes below are the ACTUAL on-disk byte counts after the 2026-09-06 complete run. Download with `curl -L -C - -A "Mozilla/5.0"` (resumable), into `~/ComfyUI/models/<subdir>/`.

## Baseline (8 files)

| Local path (under ~/ComfyUI/models) | HF repo / file | Size |
|---|---|---|
| checkpoints/sd_xl_base_1.0.safetensors | stabilityai/stable-diffusion-xl-base-1.0 :: sd_xl_base_1.0.safetensors | 6.9G |
| diffusion_models/z_image_turbo_bf16.safetensors | Comfy-Org/z_image_turbo :: split_files/diffusion_models/z_image_turbo_bf16.safetensors | 12G |
| text_encoders/qwen_3_4b.safetensors | Comfy-Org/z_image_turbo :: split_files/text_encoders/qwen_3_4b.safetensors | 8G (8044982048) |
| vae/z_image_vae.safetensors | Comfy-Org/z_image_turbo :: split_files/vae/**ae.safetensors** (real name!) | 335M |
| clip_vision/clip_vision_g.safetensors | **comfyanonymous**/clip_vision_g :: clip_vision_g.safetensors (hubert23 copy = 401) | 3.7G (3689911098) |
| ipadapter/ip-adapter-plus_sdxl_vit-h.safetensors | h94/IP-Adapter :: **sdxl_models**/ip-adapter-plus_sdxl_vit-h.safetensors (not models/) | 847M |
| ipadapter/ip-adapter_sdxl_vit-h.safetensors | h94/IP-Adapter :: sdxl_models/ip-adapter_sdxl_vit-h.safetensors | 698M |
| ipadapter/ip-adapter-faceid-plusv2_sdxl_lora.safetensors | **h94/IP-Adapter-FaceID** :: ip-adapter-faceid-plusv2_sdxl_lora.safetensors (separate repo!) | 372M |

## Extras (KB: ComfyUI Workflow Guide)

| Local path | HF repo / file | Size | Notes |
|---|---|---|---|
| diffusion_models/wan2.2_ti2v_5B_fp8.safetensors | meimeilook/Wan2.2-TI2V-5B_FP8 :: wan2.2_ti2v_5B_fp8.safetensors | 5.0G | |
| text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors | Comfy-Org/Wan_2.2_ComfyUI_Repackaged :: umt5_xxl_fp8_e4m3fn_scaled.safetensors | 6.7G | |
| vae/wan2.2_vae.safetensors | Comfy-Org/Wan_2.2_ComfyUI_Repackaged :: wan2.2_vae.safetensors | 1.4G | |
| diffusion_models/flux1-dev-fp8.safetensors | black-forest-labs/FLUX.1-dev-FP8 :: flux1-dev-fp8.safetensors | 11.9G | Official URL downloaded fine without token 2026-09-05. Fallback mirror: jellyhe/flux1-dev-fp8 (ungated, ~3% size diff). |
| controlnet/controlnet_union_sdxl_1.0.safetensors | xinsir/controlnet-union-sdxl-1.0 :: diffusion_pytorch_model.safetensors | 2.5G | One union model covers canny+depth+openpose |
| upscale_models/RealESRGAN_x4plus.pth | schwghao/RealESRGAN_x4plus :: RealESRGAN_x4plus.pth | 67M | xinntai/Real-ESRGAN repo has NO model file (code only) |
| insightface/antelopev2/*.onnx | GitHub deepinsight/insightface v0.7 release :: antelopev2.zip (unzip) | 360M | Needed by IPAdapter FaceID |

## NOT downloaded (user decision 2026-09-05)

- Minimax H3 (4 files, ~42.4G: Comfy-Org/MiniMax-H3) — user explicitly deferred. Requires ComfyUI ≥ 0.30.0 (machine has 0.34.0), CPU offload on 16GB VRAM (61GB RAM ok). Turbo Lightning LoRA + SageAttention optional speedups.

## Pitfalls seen in the wild

- `hf-mirror.com` returned 0 bytes for a 3.4G file on this IP (2026-09-05) — not a reliable mirror.
- HF throttling is transient: `comfyanonymous/clip_vision_g` ran ~400KB/s on 2026-09-05 then ~3.5MB/s on 2026-09-06. Wait on a resumable download rather than switching mirrors.
- HEAD requests to HF resolve URLs returned 401 earlier without a browser UA, but with `-A "Mozilla/5.0"` they return 302 + `x-linked-size` (exact remote byte count) for ungated files — use this to verify download completeness against on-disk size.
