---
doc: "Open-weights model specs"
kind: reference
scope: "models with published open weights"
last_verified: "2026-08-09"
---

# Open-weights model specs

Known native resolutions, recommended sampler settings, and timing for models with published open
weights. This is a lookup table, not a prescription. A value here is what the owner publishes as
native or recommended, which makes it a sound default and a good explanation for why an odd size
degrades. It is not the only setting that works, and nothing here overrides a model's prompting
guide.

## How to read a cell

<rules id="specs">

- An unmarked value is stated by the model OWNER, on its own repository, model card, or technical
  report.
- A value tagged with a provider name is stated only by that provider, with the owner silent. It is
  weaker; say so when reporting it.
- `not published` means nothing in this project's trust order states it. Do not fill the gap with a
  guess, and do not infer it from a sibling checkpoint. Say it is not published.
- Rows are per MODEL, not per guide. Checkpoints that share one prompting guide routinely disagree
  on every parameter, so never carry a row's numbers across to a sibling.
- Resolution and step counts are generation settings, not prompt text. Give them when asked; do not
  volunteer them alongside a prompt unless the request was about settings.
- A dash in Notes means no caveat was recorded for that model, not that the model has none.

</rules>

## Shared resolution sets

- `SDXL 1024 set`: total area around 1024x1024, chosen from 768x1344, 832x1216, 896x1152, 1024x1024,
  1152x896, 1216x832, 1344x768.
- `Qwen 1328 set`: 1:1 is 1328x1328, 16:9 is 1664x928, 9:16 is 928x1664, 4:3 is 1472x1140, 3:4 is
  1140x1472, 3:2 is 1584x1056, 2:3 is 1056x1584.

## Image

| Model | Capabilities | Native or recommended resolution | Steps | CFG | Sampler | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| anima-base | text-to-image | 512x512 through 1536x1536 | 30 to 50 | 4 to 5 | several work; euler_a gives softer, thinner lines and tolerates higher CFG | the HF card says CFG 4 to 5 and the CivitAI page says 4 to 6; the beta57 scheduler from the RES4LYF node pack is suggested for painterly texture |
| flux-2-dev | text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts | not published | 50; the card notes 28 as a good trade-off | 4.0 guidance scale | not published | 32B rectified flow transformer, trained with guidance distillation. Non-commercial license. A 4-bit quantized build fits an RTX 4090 |
| flux-2-klein-4b | text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts | 1024x1024 in the reference snippet | 4 | 1.0 guidance scale | not published | 4B, step-distilled for sub-second generation. Fits about 13 GB of VRAM and runs on an RTX 3090 or 4070. Apache 2.0. Undistilled counterpart is flux-2-klein-base-4b |
| flux-2-klein-9b | text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts | 1024x1024 in the reference snippet | 4 | 1.0 guidance scale | not published | 9B flow model with an 8B Qwen3 text embedder, step-distilled to 4 steps. Non-commercial license, unlike the Apache-2.0 4B. Undistilled counterpart is flux-2-klein-base-9b |
| flux-2-klein-base-4b | text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts | 1024x1024 in the reference snippet | 50 | 4.0 guidance scale | not published | the undistilled 4B, trained without step or guidance distillation, so guidance responds and output diversity is higher than the distilled klein. The checkpoint to fine-tune and train LoRAs on. Apache 2.0 |
| flux-2-klein-base-9b | text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts | 1024x1024 in the reference snippet | 50 | 4.0 guidance scale | not published | the undistilled 9B, same role as the 4B base with more capacity. Non-commercial license |
| HiDream-O1-Image | text-to-image, image-edit, multi-image-reference, subject-personalization, text-rendering | 2048x2048 in the reference command | 50 | 5.0 guidance scale | default scheduler | shift 3.0 |
| HiDream-O1-Image-Dev | text-to-image, image-edit, multi-image-reference, subject-personalization, text-rendering | not published | 28 | 0.0 guidance scale | flash scheduler with predefined timesteps | shift 1.0; for editing with exactly one reference image this variant defaults to flow_match, which the owner recommends for editing. Guidance 0.0 against the full model's 5.0 means steering cues have little to push against, so prefer the full model when a prompt needs wrestling |
| HiDream-O1-Image-Dev-2604 | text-to-image, text-rendering | 2048x2048 in the reference command | 28 | not published | not published | text-to-image only; no editing or personalization |
| hunyuan-image-3.0 | text-to-image, text-rendering, structured-layout | image size defaults to auto; accepts an explicit size such as 1280x768 or a ratio such as 16:9 | 50 | not published | not published | 80B total with 13B active; needs at least 3 x 80 GB of VRAM |
| hunyuan-image-3.0-instruct | text-to-image, image-edit, multi-image-fusion, text-rendering, structured-layout, reasoning | as above | 50 | not published | not published | needs at least 8 x 80 GB of VRAM |
| hunyuan-image-3.0-instruct-distil | text-to-image, image-edit, multi-image-fusion, text-rendering, structured-layout, reasoning | as above | 8 | not published | not published | distilled for short sampling; needs at least 8 x 80 GB of VRAM |
| ideogram-4 | text-to-image, text-rendering, layout-control, color-control | any multiple-of-16 size from 256 to 2048 on each side; 2048x2048 for the highest quality | set by a named sampler preset, for example V4_QUALITY_48 | a guidance SCHEDULE rather than a scalar, auto-adjusted per resolution | named presets in `ideogram4.PRESETS`, selected with `--sampler-preset` | the owner's release is quantized: fp8 and nf4 rather than full precision. Ideogram's first open-weight model |
| illustrious-xl-v0.1 | text-to-image | not published | 20 to 28 | 5 to 7.5 | Euler a | the card notes these may vary by use case |
| illustrious-xl-v1.0 | text-to-image | native 1536x1536; handles 512x512 through 1536x1536 | not published | not published | not published | non-standard sizes such as 1248x1824 work without modification |
| illustrious-xl-v2.0 | text-to-image | not published | not published | not published | not published | the card carries no generation settings |
| Krea-2-Raw | text-to-image | 1024x1024 in the reference command | 52 | 3.5 | not published | 12B diffusion transformer. CFG is live here, so guidance responds and seeds vary. The owner calls Raw a finetuning base and says it is not recommended for inference; read that as a steer toward Turbo, not as a defect. Train LoRAs on Raw and run them on Turbo |
| Krea-2-Turbo | text-to-image | 2048x2048 in the official codebase command; the SGLang example uses 1024x1024 | 8 | 0.0 | not published | 12B diffusion transformer distilled from Krea-2-Raw; the reference command also sets mu 1.15. CFG 0.0 means no classifier-free guidance, so exclusions must be phrased positively and output is more deterministic across seeds |
| noobai-xl-1.1 | text-to-image | SDXL 1024 set | 25 to 30 | 5 to 6 | Euler a | - |
| noobai-xl-vpred-1.0 | text-to-image | SDXL 1024 set | 28 to 35 | 4 to 5 | Euler | v-prediction checkpoint; the card warns that other samplers will not work properly |
| Qwen-Image | text-to-image | Qwen 1328 set | 50 in the reference snippet, 40 in a second one | true CFG 4.0 | not published | true CFG is a distinct knob from ordinary CFG; the reference pipeline appends ", Ultra HD, 4K, cinematic composition." to the prompt |
| Qwen-Image-2512 | text-to-image | not published; the Qwen-Image card states the Qwen 1328 set for the original release | not published | not published | not published | current open text-to-image foundation |
| Qwen-Image-Edit | image-edit | not published | not published | not published | not published | first open editor; one reference image only |
| Qwen-Image-Edit-2509 | image-edit, multi-image-edit | not published | not published | not published | not published | - |
| Qwen-Image-Edit-2511 | image-edit, multi-image-edit | not published | not published | not published | not published | current open editor |
| Qwen-Image-Layered | image-edit, layer-separation | not published | not published | not published | not published | a finetune of Qwen-Image that decomposes a scene into separately editable layers |
| z-image | text-to-image, text-rendering, bilingual | 512x512 through 2048x2048 by total pixel area, any aspect ratio | 28 to 50 | supported | not published | undistilled base, so full classifier-free guidance applies |
| z-image-turbo | text-to-image, text-rendering, bilingual | not published; the reference snippet uses 1024x1024 | 8 | none; distilled, so CFG is inert | not published | the snippet passes 9, which yields 8 DiT forward passes |

## Video

| Model | Capabilities | Resolution | Duration | Frame rate | Steps | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| h3-base-fl2va | text-to-video, image-to-video, keyframe-interpolation, native-audio, dialogue, text-rendering | up to 2K | up to 15 seconds | 24 fps (fal) | not published | the reference workflow ships a 768p path and a separate 2K regeneration path |
| h3-base-ref2va | reference-to-video, video-editing, video-continuation, native-audio, dialogue, text-rendering | up to 2K | up to 15 seconds | 24 fps (fal) | not published | as above |
| ltx-2 | text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, video-extend, native-audio, dialogue, singing, control-adapters | not published for this generation | not published | not published | not published | previous LTX generation; the 2.3 grid below is not stated to apply to it |
| ltx-2.3-22b | text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, video-extend, native-audio, dialogue, singing, control-adapters | 1080p 1920x1080, 1440p 2560x1440, 4K 3840x2160, and the 9:16 transposes of each | 6, 8 or 10 seconds; up to 20 at 1080p on the fast tier | 24, 25, 48, 50 | the distilled pipeline runs 8 steps in stage 1 and 4 in stage 2; gradient estimation cuts a 40-step run to 20 to 30 | frame count is duration x frame rate + 1; the resolution grid is stated in the owner's API documentation, and the open-weights 22B is described as the same model |
| ltx-2.5-22b | text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, native-audio, dialogue, singing, control-adapters, multi-shot | 720p 1280x720, 1080p 1920x1080, 1440p 2560x1440, 4K 3840x2160, and the 9:16 transposes of each; width and height must divide by 32 | 6 to 20 seconds at 24 or 25 fps, 6 to 10 at 48 or 50; an optional duration head picks the length from the prompt when no frame count is given | 24, 25, 48, 50 | distilled runs a fixed 8-step schedule at CFG 1; the reference pipeline generates at half resolution then latent-upsamples 2x for a second stage | 22B DiT with a custom Gemma 4 12B text encoder; a diffusion video decoder replaces the VAE reconstruction stage; frame count must satisfy frames modulo 8 = 1; ships bf16, ComfyUI int8 and NVFP4 packs, and still calls the 2.3 spatial upscaler |
| unianimate-dit | character-animation | 720P | not published | not published | not published | shipped as a LoRA over Wan2.1-I2V-14B-720P, so it inherits that checkpoint's grid |
| wan-dancer-14b | music-to-dance | not published | not published | not published | not published | - |
| wan-move-14b | motion-control | 832x480 | 5 seconds | not published | not published | released as a 480P checkpoint |
| wan2.1-flf2v-14b | first-last-frame | 720P | not published | 16 | not published | - |
| wan2.1-i2v-14b | image-to-video | 480P and 720P, shipped as two separate checkpoints | not published | 16 | not published | - |
| wan2.1-t2v-1.3b | text-to-video | 480P | not published | 16 | not published | needs 8.19 GB of VRAM; the owner suggests guide scale 6 for this checkpoint; 720P runs but is less stable and the owner recommends 480P |
| wan2.1-t2v-14b | text-to-video | 480P and 720P | not published | 16 | not published | flow shift 5.0 at 720P and 3.0 at 480P; UniPC multistep scheduler with flow prediction |
| wan2.1-vace-14b | video-edit, reference-to-video | 480P and 720P | 5 second clips recommended | 16 | not published | for longer work the owner recommends generating 5 second clips and chaining them with the firstclip extension task |
| wan2.2-animate-14b | character-animation | not published | not published | 30 in the reference example | not published | - |
| wan2.2-fun-a14b-control | control-to-video | 512, 768 or 1024 | 81 frames, about 5 seconds | 16 | not published | a finetune of Wan2.2-I2V-A14B; takes Canny, Depth, Pose, MLSD and trajectory control |
| wan2.2-fun-a14b-control-camera | control-to-video | 512, 768 or 1024 | 81 frames, about 5 seconds | 16 | not published | a finetune of Wan2.2-I2V-A14B; camera movement supplied as a trajectory |
| wan2.2-fun-a14b-inp | image-to-video, first-last-frame | trained multi-resolution; the card states no grid for this variant | not published | not published | not published | a finetune of Wan2.2-I2V-A14B; first-and-last-frame prediction |
| wan2.2-i2v-a14b | image-to-video | 480P and 720P | not published | not published | not published | - |
| wan2.2-s2v-14b | speech-to-video | 480P and 720P | not published | not published | not published | - |
| wan2.2-t2v-a14b | text-to-video | 480P and 720P | not published | not published | not published | - |
| wan2.2-ti2v-5b | text-to-video, image-to-video | 720P | not published | 24 | not published | high-compression Wan2.2-VAE; the only 2.2 checkpoint with an owner-stated frame rate |
| wan2.2-vace-fun-a14b | video-edit, reference-to-video | 480P and 720P, inherited from the base | not published | not published | not published | a finetune of Wan2.2-T2V-A14B, so it takes that checkpoint's grid |

## Sources

Owner surfaces first. A provider value is carried only where the owner is silent, and is tagged in
the cell that uses it.

- Image, official: [Anima](https://huggingface.co/circlestone-labs/Anima),
  [Anima on CivitAI](https://civitai.com/models/2458426/anima),
  [FLUX.2 announcement](https://bfl.ai/blog/flux-2),
  [FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev),
  [FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B),
  [FLUX.2-klein-9B](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B),
  [FLUX.2-klein-base-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B),
  [FLUX.2-klein-base-9B](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B),
  [HiDream-O1-Image](https://github.com/HiDream-ai/HiDream-O1-Image),
  [HiDream-O1-Image-Dev-2604](https://huggingface.co/HiDream-ai/HiDream-O1-Image-Dev-2604),
  [HunyuanImage-3.0](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0),
  [HunyuanImage-3.0-Instruct](https://huggingface.co/tencent/HunyuanImage-3.0-Instruct),
  [ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8),
  [ideogram-4-nf4](https://huggingface.co/ideogram-ai/ideogram-4-nf4),
  [Illustrious XL v0.1](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0),
  [Krea-2-Raw](https://huggingface.co/krea/Krea-2-Raw),
  [Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo),
  [Illustrious XL v1.0](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.0),
  [Illustrious XL v2.0](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0),
  [NoobAI-XL 1.1](https://huggingface.co/Laxhar/noobai-XL-1.1),
  [NoobAI-XL V-Pred 1.0](https://huggingface.co/Laxhar/noobai-XL-Vpred-1.0),
  [Qwen-Image](https://huggingface.co/Qwen/Qwen-Image),
  [Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512),
  [Qwen-Image-Edit](https://huggingface.co/Qwen/Qwen-Image-Edit),
  [Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509),
  [Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511),
  [Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered),
  [Qwen-Image on GitHub](https://github.com/QwenLM/Qwen-Image),
  [Z-Image](https://huggingface.co/Tongyi-MAI/Z-Image),
  [Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- Video, official: [LTX-2](https://github.com/Lightricks/LTX-2),
  [LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3),
  [LTX model reference](https://docs.ltx.video/models),
  [MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3),
  [MiniMax-H3 model card](https://huggingface.co/MiniMaxAI/MiniMax-H3),
  [Wan 2.1](https://github.com/Wan-Video/Wan2.1),
  [Wan 2.2](https://github.com/Wan-Video/Wan2.2),
  [VACE](https://github.com/ali-vilab/VACE),
  [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun),
  [Wan2.2-Fun-A14B-Control](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control),
  [Wan2.2-Fun-A14B-Control-Camera](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control-Camera),
  [Wan2.2-Fun-A14B-InP](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-InP),
  [Wan2.2-VACE-Fun-A14B](https://huggingface.co/alibaba-pai/Wan2.2-VACE-Fun-A14B),
  [Wan-Move](https://github.com/ali-vilab/Wan-Move),
  [UniAnimate-DiT](https://github.com/ali-vilab/UniAnimate-DiT),
  [Wan-Dancer-14B](https://huggingface.co/Wan-AI/Wan-Dancer-14B)
- Provider: [fal MiniMax H3 prompting guide](https://fal.ai/learn/devs/minimax-h3-prompting-guide)

Last verified: 2026-08-09.
