---
guide: "FLUX.2 (image)"
prompt_scheme: "flux-2"
models:
  # hosted
  - { id: "flux-2-pro",           access: "closed-weights", tier: "std",       caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "production at scale; balanced quality, speed, and cost" }
  - { id: "flux-2-flex",          access: "closed-weights", tier: "std",       caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "typography and fine detail; exposes step and guidance control" }
  - { id: "flux-2-max",           access: "closed-weights", tier: "flagship",  caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts, grounding-search], best_for: "highest quality and editing consistency; grounding search for real-world and current subjects" }
  # open weights. The klein line ships in PAIRS: a plain checkpoint that is step- and guidance-distilled,
  # and a `-base` checkpoint that is neither. They are different models with different settings, not
  # different downloads of one model, so never carry a step count or CFG across the pair.
  - { id: "flux-2-dev",           access: "open-weights",   tier: "base",      caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "32B open model for local use, research, and fine-tuning; full generation and editing" }
  - { id: "flux-2-klein-base-4b", access: "open-weights",   tier: "base",      caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "the undistilled 4B: guidance is live and seeds stay diverse, so this is the one for LoRA training, fine-tuning and any prompt that needs steering. Apache 2.0, so commercial use is allowed" }
  - { id: "flux-2-klein-base-9b", access: "open-weights",   tier: "base",      caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "the undistilled 9B, same role as the 4B base with more capacity. Non-commercial license, unlike the Apache-2.0 4B pair" }
  - { id: "flux-2-klein-4b",      access: "open-weights",   tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "fastest tier, runs on consumer hardware in about 13 GB; real-time and high-volume. Step- and guidance-distilled, so exclusions have little to push against and seeds converge: reach for flux-2-klein-base-4b when a prompt needs wrestling. Apache 2.0" }
  - { id: "flux-2-klein-9b",      access: "open-weights",   tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts], best_for: "higher-quality klein; also served on the API. Same distillation trade as the 4B, with flux-2-klein-base-9b as its undistilled counterpart. Non-commercial license" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, json-prompts, grounding-search]
prompt:
  languages: ["en", "multilingual"]
  formula: "Subject + Action, then Style, then Context (setting, lighting, mood), then Technical (camera, lens, composition); front-load the subject because FLUX weights earlier words more"
  literal_text: "quote the exact words, then state placement, font, size, capitalization, and color (a hex code for brand text)"
  length_strategy: "start short and add only what changes the image; a few sentences is usually ideal; do not pad or contradict, and do not bury the subject at the end"
  auto_expand_behavior: "hosted models can upsample a basic prompt; klein does NOT upsample, so write the full self-contained prompt yourself"
  negatives: "no negative prompt in the core scheme; describe the desired state ('sharp focus', not 'no blur'); some hosts expose a negative field for klein, keep it short and subject-specific"
  references: "name multiple inputs positionally (image 1, image 2, or first/second/third image) and give each one a role (subject from image 1, style from image 2)"
  color: "associate a hex code with a specific object ('the car is #FF0000'); for a gradient give start and end colors"
  json: "FLUX.2 reads structured JSON prompts (scene, subjects, style, color_palette, lighting, camera); paste JSON or flatten it to natural language, the model reads both"
sources:
  official: ["https://docs.bfl.ai/guides/prompting_guide_flux2", "https://docs.bfl.ai/guides/prompting_unified_building", "https://docs.bfl.ai/flux_2/flux2_image_editing", "https://bfl.ai/models/flux-2-max", "https://bfl.ai/blog/flux-2", "https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence", "https://huggingface.co/black-forest-labs/FLUX.2-dev", "https://huggingface.co/black-forest-labs/FLUX.2-klein-4B", "https://huggingface.co/black-forest-labs/FLUX.2-klein-9B", "https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4B", "https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9B"]
  provider: ["https://fal.ai/learn/devs/flux-2-prompt-guide", "https://fal.ai/learn/devs/flux-2-klein-prompt-guide", "https://fal.ai/learn/devs/flux-2-max-prompt-guide"]
  community: []
last_verified: "2026-08-09"
---

# FLUX.2: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and step limits, reference counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the whole FLUX.2 family: the API models [pro], [flex], [max], and the open-weight models [dev] and [klein] (4B and 9B). They share one prompt scheme; the differences are capability, not grammar, and are flagged in Per-variant notes.
- Generation, editing, and multi-reference are built into every main model. FLUX.2 has no separate Kontext or Fill/Canny/Depth/Redux tool models; one model does all of it.
- Write natural language, not keyword lists, and front-load the subject. FLUX.2 weights earlier words more heavily.
- There is no negative prompt in the core scheme. Describe what you want, not what you want to avoid.
- FLUX 3 is a different model on a different prompt scheme, and only its video half has shipped. For video, use the FLUX 3 Video guide; do not carry the hex-pinning and JSON rules below across to it. FLUX 3 Image is announced but unreleased, so image work stays here.

</rules>

## TL;DR

<template id="quickstart">

{subject with key attributes} {action or pose}, {style or medium}, {setting and lighting}, {a camera or composition cue}. For in-image words: the text "{exact words}" in {font, size, color} at {placement}.

</template>

## Models and when to use which

All six share one prompt scheme; a prompt written for one transfers to the others. Pick by access and job.

- `flux-2-pro` (API): the production default. Balanced quality, speed, and cost for high-volume work.
- `flux-2-flex` (API): the typography and fine-detail specialist; also exposes step and guidance knobs (those are API params, out of scope here).
- `flux-2-max` (API): the highest quality and editing consistency, the strongest prompt following, and the only variant with grounding search (see Per-variant notes).
- `flux-2-dev` (open weights, 32B): run locally or self-host; for research, custom pipelines, and fine-tuning. Full generation and editing.
- `flux-2-klein` (open weights, 4B and 9B): the fastest tier, for consumer hardware, real-time, and high volume. 4B is Apache 2.0; 9B is higher quality and also on the API.

## How the model reads prompts

- Front-load the subject. FLUX.2 pays more attention to what comes first, so lead with the main subject and its key action, then style, then context, then secondary detail.
- Natural language, not keywords. Full descriptive phrases beat comma-separated tags.
- Start short, add only what changes the image. The model handles very long prompts, but more words do not mean better results; specific beats long, and filler hurts.
- Do not contradict or bury. Conflicting cues ("bright sunny day with moody dark shadows") confuse it, and critical details placed last get less weight.
- It is multilingual. Prompting in the content's native language (French for a Parisian cafe, Japanese for anime) yields more culturally authentic results.
- Hosted models can upsample a terse prompt into a fuller one; klein does not, so write the full prompt yourself for klein.
- It is grounded in real-world knowledge (lighting, materials, spatial logic), so plausible scenes hold together. [max] extends this with live grounding search.

## Prompt structure

<rules id="structure">

- Order the prompt: Subject + Action first, then Style, then Context (setting, lighting, mood), then Technical (camera, lens, composition).
- The fuller build order, used only as needed: image type, subject, location, style, camera, lighting, colors, effect, additional elements. It is a menu, not a checklist; include only slots that change the image.
- Be concrete: "a woman in her mid-30s with shoulder-length auburn hair" outperforms "a person". Name the action and state, not just the noun.
- If the framing pulls too wide, name the subject first and push the environment later.

</rules>

<template id="general">

{subject with attributes} {action}, {style or medium}, {setting}, {lighting}, {camera and lens}, {one or two effects}

</template>

<example use_case="directed-photoreal">

```text
A golden retriever mid-leap chasing a tennis ball across a sunlit hardwood floor in a cozy living room, muddy paw prints trailing behind, warm afternoon light through sheer curtains, candid pet photography, 35mm lens, shallow depth of field
```

*Why: subject and action first, then a concrete setting, lighting, and lens, the directed register FLUX rewards over a bare "a dog in a room".*

</example>

## Style and camera

<rules id="style">

- Name the style early and keep it concrete: photographic, illustrative, cinematic, painterly, or a specific medium (oil painting, watercolor, charcoal sketch, isometric 3D render). To pin a look, name both the art form and the style.
- Simulate a camera with model, lens, and settings: "shot on Kodak Portra 400, natural grain" or "Hasselblad X2D, 80mm, f/2.8" beats "professional photo".
- Era looks: "early digital camera, slight noise, flash, 2000s digicam style"; "film grain, warm cast, soft focus, 80s vintage photo"; "shot on Sony A7IV, clean sharp, high dynamic range".
- Use one or two strong effects (film grain, bokeh, motion blur, double exposure), not a pile. Name a reference artist or film when you want a specific signature.

</rules>

<example use_case="film-still">

```text
A lighthouse keeper standing on a cliff in a storm, old film still, shot on Kodak Portra 400 with natural grain, overcast stormy light, muted cool tones, dramatic contrast, cinematic detail
```

*Why: a single style anchor (old film still) plus a named film stock and concrete light, rather than stacked quality tags.*

</example>

## Text rendering

Legible in-image text is a FLUX.2 strength (posters, infographics, UI, packaging); [flex] is the typography specialist.

<rules id="text">

- Quote the exact words, then state where they go, the font, the size, and the capitalization. "At the top, the text 'SUMMER SALE' in large bold block letters; below it, '50% OFF' in smaller italic" beats just mentioning the words.
- Give each text block its own role and placement when there are several (headline, subtitle, label).
- For brand text, set the color with a hex code ("the logo text 'ACME' in color #FF5733").

</rules>

<example use_case="product-typography">

```text
A Samsung Galaxy phone product advertisement. The headline "Ultra-strong titanium" in bold white sans-serif across the top; smaller subtext "Shielded in a strong titanium frame" beneath it. Close-up of the phone edge showing the titanium frame, dark gradient background, clean minimalist tech aesthetic, professional product photography
```

*Why: each text block is quoted with its own weight and placement, and the layout and aesthetic are named, so the typography and image resolve together.*

</example>

## Color and hex control

<rules id="color">

- FLUX.2 matches exact colors from hex codes. Always attach the hex to a specific object: "the sofa in deep teal #1B6B6F" works; "use #1B6B6F somewhere" does not.
- Signal a hex with the word "color" or "hex" before the code.
- For a gradient, give the start and end colors (and the direction or zones if it matters).

</rules>

<example use_case="hex-interior">

```text
A modern living room with warm terracotta walls in hex #C4725A, a large L-shaped sectional sofa in deep teal #1B6B6F, and golden amber #E8A847 accent pillows, natural daylight casting soft shadows, interior photography
```

*Why: every hex is bound to a named object (walls, sofa, pillows), the documented condition for reliable color matching.*

</example>

## JSON structured prompts

FLUX.2 reads structured JSON directly, which is useful for multi-subject scenes, brand work, and automation. Paste the JSON as the prompt, or flatten it to natural language; the model reads both. Start simple and add fields as needed.

<template id="json">

```json
{
  "scene": "overall scene description",
  "subjects": [
    { "description": "detailed subject with explicit color", "position": "where in frame", "action": "what it is doing" }
  ],
  "style": "artistic style",
  "color_palette": ["#hex1", "#hex2"],
  "lighting": "lighting description",
  "mood": "emotional tone",
  "composition": "framing and layout",
  "camera": { "angle": "camera angle", "lens": "lens type", "depth_of_field": "focus behavior" }
}
```

</template>

<example use_case="json-product">

```json
{
  "scene": "Studio product shot of a ceramic coffee mug on a marble surface",
  "subjects": [
    { "type": "mug", "description": "matte black finish, gold interior, steam rising, strictly in color #1A1A1A", "position": "center foreground", "color_match": "exact" }
  ],
  "style": "lifestyle product photography",
  "color_palette": ["#1A1A1A", "#C9A227", "#FFFFFF"],
  "lighting": "soft morning light from the left"
}
```

*Why: each element gets its own field, and per-part color is pinned with an exact hex and color_match, which is how JSON buys precise control for brand and product work.*

</example>

## Image editing

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Replace, Redraw, Restore) or the constraint (Keep), but the opening clause must instruct rather than describe. A declarative setup such as "Image 1 provides the foundation, Image 2 provides the face" states the plan instead of issuing it and pushes the real instruction back by a sentence or two.
- Describe the transformation, not the whole scene. "Change the dress color to red" or "add warm sunset lighting" beats re-describing everything; the model preserves what you do not mention.
- Name explicit replacements: "replace the blue shirt with a red leather jacket". Then name what to keep ("maintaining the same pose and lighting", "keeping the rest of the room unchanged").
- For a style transfer, name the target style and pin the composition: "turn this photo into an oil painting in Monet's style, keeping the original composition".

</rules>

<example use_case="edit-transformation">

```text
Change the weather to a warm sunny day with a clear blue sky and add a flock of birds flying over the treetops
```

*Why: names only the deltas (weather, sky, birds) and never re-describes the forest that stays constant, the transformation-focused habit.*

</example>

<example use_case="style-transfer">

```text
Redraw the photograph in image 1 in the impressionist oil-painting style of image 2, keeping image 1's composition and subjects unchanged
```

*Why: a pure style transfer, the look is taken only from image 2 while image 1's content and composition stay locked.*

</example>

<example use_case="style-transfer-plus-edit">

```text
Redraw the living room from image 1 in the watercolor style of image 2, and add the floor lamp from image 3 beside the sofa, keeping image 1's layout and furniture placement
```

*Why: takes content from one image and the style from another while folding in an object from a third, pinning the layout so only the look and the added lamp change.*

</example>

## Multiple reference images

FLUX.2 composes across several reference images in one model: pull a subject, a material, a background, or a style from each.

<rules id="multi-image">

- Name each input positionally (image 1, image 2, or first image, second image) in upload order, and refer to it that way.
- Weld every borrowed element to its source and give each input one role: "the subject from image 1", "the jacket from image 2", "the background from image 3", "the style of image 1". Read the instruction as an assignment list, one role per input.
- Name what moves, pin what stays: state what to take from each image, and what to hold constant (proportions, identity, composition).

</rules>

<example use_case="multi-ref-simple">

```text
The subject from image 1 wearing the jacket from image 2, photographed in the environment from image 3, keeping the subject's face and the jacket's color unchanged
```

*Why: three inputs in three roles (subject, garment, setting), each welded to its source, with identity and the jacket color pinned so only the placement changes.*

</example>

<example use_case="multi-ref-flagship">

```text
Create a house for the chickens from image 1 using materials from images 2, 3, 4, and 5. Use the wood from image 5 for the base, the materials from images 2 and 4 for the walls and floor, and the material from image 3 for a small pillow nest. Place the chickens from image 1 in their new home, sitting on the pillow nest. Next to them, include the eggs from image 6. Apply the style of image 1 to the entire new scene
```

*Why: a long, fully specified multi-reference build that assigns every numbered image a distinct role (subject, four material sources, props) and designates one image as the style source for the whole composite.*

</example>

## Per-variant notes

The scheme is shared; these are the only prompting-relevant differences.

<rules id="variants">

- klein (4B and 9B): no prompt upsampling, so write the full, self-contained prompt across subject, environment, style, and technical; do not rely on the model to fill gaps. Keep it focused (klein gets confused past roughly a hundred words). It has no weight syntax, so signal emphasis in words ("prominently featuring", "with particular attention to"). Some hosts expose a negative field for klein; if so, target subject-specific failure modes rather than generic quality terms.
- max: adds grounding search. It can pull live, real-world information (current events, trending products, the weather in a city right now, a recent match) to ground the image, so you can reference current or real subjects without supplying reference material. It also has the strongest prompt following; for competing styles, weight them in words ("dominant: neon-lit rainy streets; secondary: ukiyo-e line work").
- flex: the typography and fine-detail specialist; reach for it on text-heavy work.
- pro: the production default; dev: the open 32B model for local use and fine-tuning.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Keyword soup: rewrite disconnected tags as a descriptive phrase, subject first.
- Burying the subject: do not place the main subject or critical detail at the end; FLUX weights the front.
- Stacked quality tags: "8K, ultra-detailed, masterpiece, best quality" adds little; one or two concrete realism cues suffice.
- Too many effects: one or two strong effects read as intentional; more reads as noise.
- Contradictions: do not combine cues that fight ("photorealistic portrait" plus "watercolor painting style").
- Expecting negatives to work: there is no core negative prompt; describe the desired state instead.
- Re-describing the whole scene when editing: state only the change and what to keep.
- Under-specifying klein: with no upsampler, a vague klein prompt underperforms; write the full stack.
- Floating hex codes: attach every hex to a named object.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. Two notes from reconciling sources: [max]'s grounding search (live web information) is documented on BFL's own [max] model page, though provider guides do not all expose it; and FLUX.2 has no negative prompt in the core scheme per BFL, while some hosts add one for klein.

- Official (Black Forest Labs): [FLUX.2 prompting guide](https://docs.bfl.ai/guides/prompting_guide_flux2), [building a good prompt](https://docs.bfl.ai/guides/prompting_unified_building), [FLUX.2 image editing](https://docs.bfl.ai/flux_2/flux2_image_editing), [FLUX.2 max model page](https://bfl.ai/models/flux-2-max), [FLUX.2 announcement](https://bfl.ai/blog/flux-2).
- Provider: [fal FLUX.2 prompt guide](https://fal.ai/learn/devs/flux-2-prompt-guide), [fal FLUX.2 klein prompt guide](https://fal.ai/learn/devs/flux-2-klein-prompt-guide), [fal FLUX.2 max prompt guide](https://fal.ai/learn/devs/flux-2-max-prompt-guide).

Coverage note: re-checked 2026-08-07 against the FLUX 3 release. The owner's image prompting guide still scopes itself to FLUX.1, FLUX.1 Kontext, and FLUX.2, and FLUX 3 Image remains announced but unreleased, so nothing in this guide changed. Only the FLUX 3 Video cross-reference was added.

Last verified: 2026-08-09.
