# P-H3-Image: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08. Sources: the HF model card (`PrunaAI/P-H3-Image`, read through the HF
tools including the example images `assets/prompt.jpg` and `assets/edits.jpg`), the ComfyUI card
(`PrunaAI/P-H3-Image-Comfy`), Pruna's launch post (`pruna-blog-p-h3-image-launch.md`), and the diffusers docs and
pipeline source at commit 84532a058702c74ae5d1dd6ceb05683fc5d5e768 (`diffusers-*.py`, `diffusers-docs-*.md`).

## 1. Its own scheme, not MiniMax H3 and not Pruna Video

P-H3-Image is a fine-tune of MiniMax-H3 (card: `base_model_relation: finetune`; launch post: prompt upsampler,
text encoder, schedule, timestep block, decoder all replaced or retrained, DMD-distilled to 8 steps). It is a
still-image model prompted in prose with its own four rules and its own edit form, so the H3 video guide does not
apply. It is open-weights from Pruna, unlike the hosted P-Video line, so it is not part of `pruna-video`.

## 2. Tier and distillation cost

Tier `distilled`: 8 steps, guidance-distilled, no guider, negative prompt or guidance scale. Owner claim: "for most
prompts, the 8-step model matches the 50-step original". The cost recorded in the guide: no negative field and no
guidance, so the prompt text is the only control, which matches the owner's "sensitive to prompting".

## 3. Edit forms come from the pipeline's validator

`prompt_upsampler.py` `is_edit_prompt()` accepts exactly two forms: a one-paragraph prompt that starts
`Edit <Picture 1>.` and contains `Keep`, or a six-section brief (`subject_definitions`, `summary`,
`retention_analysis`, `detailed_description`, `overall_soundscape`, `non_diegetic_music`, with `[keyframe
completion]` once and each retention line `<Picture i>` or `<Subject i>` plus fully_preserved, partially_preserved,
attribute_transfer or weak_reference). The brief is MiniMax-H3's Ref2VA structure. `encoders.py` prefixes any other
instruction with `Edit <Picture 1>. ` and encodes each image as `<Picture i>: ` plus its vision tokens.

Taught: the paragraph form for hand-written edits (the model card's own template); the brief is mentioned as what
the upsampler writes, not taught as a hand-written form. Reference naming in hand-written edits uses `<Picture N>`
to match the encoder's labels; the card's prose says "Picture 2, Picture 3", and the upsampler accepts any naming
("the hat from the second photo", ComfyUI card).

## 4. Upsampler

Fine-tuned Qwen3.5-9B, on by default in diffusers and in every ComfyUI workflow. Input for text-to-image is two
lines, `Aspect ratio: {ratio}` and `Request: {request}`; for edits, a `<Picture N>:` block per image then
`Edit <Picture 1>. {request}`. Greedy decoding, so a request always gives the same prompt. Its output is returned
with the image. Taught as technique: short requests are its input, keep ratio and canvas consistent, switch it
off for hand-written full prompts, exact text and comparisons.

## 5. Owner-internal discrepancy

Launch post: edits "with up to 9 input images" and renders "from 2 to 16 megapixels". Model and ComfyUI cards: up
to 8 images, 8 MP best, 2 and 4 MP work with more artifacts. Counts are out of scope for the guide; the spec
table follows the cards.

## 6. Examples

Owner verbatim: the recipe-card prompt (transcribed from `assets/prompt.jpg`; it keeps the degree sign and middle
dot because they are rendered text), the Kirchner quickstart prompt, and the upsampler request "a red fox in fresh
snow at first light". Guide-built to the owner's rules: the risograph print, and three edits built from the
owner's requests "give him a red beanie" and "give the woman in picture 1 the hat from picture 2".

## 7. Kept out of the guide (spec table only, or nowhere)

Resolutions and the 8 MP size list, step count, sigma grid, VRAM and download sizes, timings, precision builds'
file names, `max_new_tokens`, image-count limits, licence region terms.
