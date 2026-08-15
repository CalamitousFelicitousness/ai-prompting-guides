---
guide: "Wan (image)"
prompt_scheme: "wan-image-v2"
models:
  - { id: "wan2.7-image-pro", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference], best_for: "interactive editing and precise prompt following; the current image flagship" }
  - { id: "wan2.6-image",     access: "closed-weights", tier: "std",      caps: [text-to-image, image-edit, multi-image-reference], best_for: "all-in-one generation and editing: multi-image input, subject-consistent generation, style transfer" }
  - { id: "wan-text-to-image-v2", access: "closed-weights", tier: "base", caps: [text-to-image], best_for: "plain text-to-image when you do not need editing or multi-image features" }
capabilities: [text-to-image, image-edit, multi-image-reference]
prompt:
  languages: ["en", "zh", "mixed"]
  formula: "Subject + Setting + Style (basic); + Camera + Atmosphere + Detail modifiers (advanced)"
  literal_text: "Wan's image docs define no quoting convention for in-image text and do not document reliable typography; for legible words in an image prefer Qwen-Image"
  length_strategy: "rewards complete prompts that build subject, setting, style, then camera, atmosphere, and detail"
  auto_expand_behavior: "prompt rewriting is on by default and usually best left on; write the full prompt yourself when you need tight control"
  negatives: "use the negative field to suppress defects (distorted limbs, malformed fingers, oversaturation, wax-like skin, chaotic composition, blurry text)"
  references: "for multi-image edits, name each input as image 1, image 2, image 3, and so on; phrase each as 'the X from image N' and combine several (for example, the style of image 1, the background of image 2, and the jacket from image 3)"
sources:
  official: ["https://www.alibabacloud.com/help/en/model-studio/text-to-image-prompt", "https://www.alibabacloud.com/help/en/model-studio/wan-image-generation-api-reference"]
  provider: []
  community: []
last_verified: "2026-05-31"
---

# Wan image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution limits, image counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- Wan is one model family that generates both stills and video. This guide is the image half; for motion, audio, and multi-shot see wan-video.md. The static-composition vocabulary (shot size, angle, lens, light, style) is shared between the two.
- Write the prompt as one continuous natural-language description built from named components, not a comma-separated tag list.
- Wan's image docs document no technique for words inside the image. Do not assume legible typography from these models. See Text in images below.

</rules>

## TL;DR

<template id="quickstart">

{subject with key attributes}, {setting}, {style}, {shot size and camera angle}, {lighting}, {atmosphere}, {a few detail modifiers}

</template>

## Models and when to use which

All three share one prompt scheme; pick by capability.

- `wan2.7-image-pro`: the current flagship, strongest at precise prompt following and interactive editing. Reach for it when prompt adherence matters most.
- `wan2.6-image`: the all-in-one workhorse for generation and editing, with multi-image input, subject-consistent generation, and style transfer.
- `wan-text-to-image-v2`: the plain text-to-image path when you only need an image from text and none of the editing or multi-image features.

A prompt written for one transfers to the others; pick by the capability you need, then keep the prompt the same.

## How the model reads prompts

- Natural language wins. The model reads full descriptive sentences better than tag lists, but ordering the description (subject, then setting, then style, then camera, atmosphere, and detail) improves control.
- It rewards detail. More complete and precise prompts produce higher-quality images.
- Prompt rewriting is on by default and usually best left on. A terse prompt is auto-elaborated, so do not pad the prompt with redundant detail unless you turn rewriting off. When editing, the rewriter expands the positive prompt only and leaves the negative untouched.
- It is bilingual. English, Chinese, and mixed-script prompts all work; the keyword vocabulary below is in English.

## Prompt structure

<rules id="structure">

- Basic (quick exploration): Subject + Setting + Style.
- Advanced (fine control): Subject + Setting + Style + Camera + Atmosphere + Detail modifiers.
- Lead with the subject and its key attributes, then the setting, then the style, then camera and lighting, then mood, then a few quality and detail modifiers.
- Keep the detail modifiers few. A short tail of quality cues helps; a long pile of them does not.

</rules>

<template id="general">

{subject with attributes and action}, {detailed setting}, {style}, {shot size and lens}, {lighting}, {atmosphere}, {a few detail modifiers}

</template>

<example use_case="photoreal-portrait">

```text
A 25-year-old woman with a round face looking at the camera, elegant ethnic dress, outdoors in soft daylight, commercial photography, half-body close-up, cinematic lighting, delicate light makeup, sharp focus
```

*Why: subject and attributes first, then setting, style, shot, and lighting, following the advanced formula without over-stacking quality tags*

</example>

## Visual vocabulary

Reference terms the model recognizes. Add the relevant ones; you do not need one from every group.

- Shot size: extreme close-up (facial detail and texture), close-up, medium shot, long shot (emphasize environment and scale).
- Camera angle: eye level, bird's eye, low angle, aerial.
- Lens: macro, ultra-wide angle, telephoto, fisheye.
- Style: realistic, watercolor, ink painting, Chinese ink, Gongbi, oil, 3D, C4D rendering, 3D cartoon, Pixar style, clay, ceramic, felt, origami, pointillism, surrealist, post-apocalyptic.
- Lighting: sunlight, moonlight, starlight, backlight, neon, ambient light.
- Composition and color are free text, not a fixed keyword set: describe them directly ("centered composition", "low saturation", "Morandi colors", "professional color grading").
- Atmosphere: dreamy, serene, lonely, majestic, dramatic, whimsical, childlike wonder.

## By use-case

### Photorealism

<rules id="photoreal">

- Lead with camera language: lens, shot size, and lighting. Name the material and texture you want rendered.
- Add realism cues sparingly (natural light, shallow depth of field, true-to-life color). Do not over-stack quality tags.

</rules>

<example use_case="product-shot">

```text
A macro shot of fresh cherries beside a glass of sparkling water, natural light, professional color grading, clean sharp focus, commercial product photography, true-to-life detail
```

*Why: a macro lens plus material and lighting cues drive photoreal texture without tag soup*

</example>

### Artistic styles

Wan's stylistic range is its strength. Name the style as a keyword and let it govern the rendering while the subject stays simple.

<rules id="styles">

- State the style explicitly and pair it with a clear subject and setting.
- Stacking a medium with a named tradition sharpens the look ("ink painting" plus "rice paper texture" plus "white space").

</rules>

<example use_case="ink-painting">

```text
A single orchid, ink painting, generous white space, artistic conception, delicate brushstrokes, the texture of rice paper
```

*Why: the style keyword leads, and the medium and texture cues pin a specific traditional look on a minimal subject*

</example>

<example use_case="felt-character">

```text
A panda made of wool felt wearing a wide-brimmed hat and a blue uniform vest, in a running pose, on an animal-kingdom city street at night, felt material, Pixar style, backlight, centered composition, adorable, 4K
```

*Why: a material-driven subject with a dense setting, then style, light, and composition trailing as the advanced formula prescribes*

</example>

<example use_case="detailed-cinematic-scene">

```text
A lone fisherman in a worn yellow raincoat stands at the end of a weathered wooden pier at dawn, casting a line into a calm grey sea. Thin mist hangs over the water and distant hills fade into soft layers behind him. Low golden light rakes across the wet planks, a few gulls scattered across the pale sky. Cinematic wide shot, slightly low angle, shallow depth of field, muted cool palette with a warm highlight on his face, fine detail in the rope and the wood grain
```

*Why: a long flagship that builds the full advanced formula, subject and action first, then a layered setting, then shot, angle, light, palette, and material detail, the dense but substantive register Wan rewards*

</example>

### Subject-consistent generation

<rules id="subject-consistency">

- To keep a character or object consistent across new images, supply reference images and describe the new scene or pose you want it placed in.
- Describe what should stay the same about the subject in words; the reference images carry the identity the prompt cannot fully specify.

</rules>

## Image editing

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Replace, Redraw, Restore) or the constraint (Keep), but the opening clause must instruct rather than describe. A declarative setup such as "Image 1 provides the foundation, Image 2 provides the face" states the plan instead of issuing it and pushes the real instruction back by a sentence or two.
- Editing is driven by a single natural-language instruction plus one or more reference images. There is no separate edit grammar; word the change plainly.
- Name each reference image by its position ("image 1", "image 2", in upload order), then say which attribute to take from which ("the style of image 1", "the background of image 2", "the subject of image 1"). You can combine several sources in one instruction (a garment onto a subject, a product onto a model, a subject into a new background).
- Weld every borrowed element to its source. With three or more inputs an unattached phrase like "the jacket" is ambiguous, so always write "the jacket from image 2"; read the instruction as one role per input.
- Name what moves, pin what stays. The model carries only what you name, so state each element you are changing and hold the rest constant ("keeping their face and pose unchanged"), or a transfer can drift the subject. There is no dedicated keep-unchanged control, so the words carry it.
- Each instruction is independent; there is no in-call conversation. Iterate by re-prompting with a refined instruction.
- For text edits, do not expect exact wording. See Text in images.

</rules>

<example use_case="multi-image-compose">

```text
Generate a plated tomato and egg stir-fry using the cooking style of image 1, the table background of image 2, and the ceramic bowl from image 3, matching the lighting across all three
```

*Why: assigns a distinct attribute to each of three inputs (style, background, object) by naming them in position, which is how Wan composes from several references at once*

</example>

<example use_case="restyle">

```text
Restyle the subject of image 1 as an oil painting with visible brushstrokes, keeping the pose and composition the same
```

*Why: states the target style and names the invariants in words, since there is no separate control to lock them*

</example>

<example use_case="clothing-transfer">

```text
Dress the person in image 1 in the jacket from image 2 and the wide-brimmed hat from image 3, keeping their face, hairstyle, and pose unchanged
```

*Why: takes two wardrobe pieces from two separate inputs onto the subject of image 1, naming each source and pinning identity so only the named items change*

</example>

<example use_case="subject-into-scene">

```text
Place the subject of image 1 into the background of image 2 and add the bicycle from image 3 beside them, matching the lighting and perspective across all three
```

*Why: composites a subject from one input into a scene from another and introduces an object from a third, with lighting and perspective named so the elements sit together*

</example>

<example use_case="product-on-model">

```text
Put the watch from image 2 on the wrist and the sunglasses from image 3 on the face of the model in image 1, keeping each product's shape and color exact and the model's identity unchanged
```

*Why: places products from two separate inputs onto one subject, naming each source and pinning product fidelity and identity*

</example>

<example use_case="style-transfer">

```text
Redraw the scene of image 1 in the ink-painting style of image 2, keeping image 1's composition and subject placement
```

*Why: a pure style transfer, the rendering comes from image 2 while the content and layout stay locked to image 1*

</example>

<example use_case="style-transfer-plus-edit">

```text
Render the portrait in image 1 in the oil-painting style of image 2 and change the background to a misty mountain valley, keeping the subject's face and pose unchanged
```

*Why: combines a style transfer from one reference with a background swap, pinning identity so only the look and the backdrop change*

</example>

## Text in images

<rules id="text">

- Wan's image prompt docs define no convention for words that must appear in the image: no quoting rule, no layout or font guidance, no multilingual text-rendering technique.
- Reliable typography is not a documented strength of `wan-text-to-image-v2` or `wan2.6-image`. The `wan2.7-image-pro` model page advertises long-text rendering, but the prompt docs do not substantiate how to drive it, so treat any in-image text on these models as approximate.
- When legible words in the image are the point (posters, titles, infographics, signage), use Qwen-Image, which documents an explicit quoting technique for in-image text. See qwen-image.md.
- "blurry or distorted text" is a listed defect to suppress with the negative field, which is a further sign that exact text is not a reliable target here.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- Use the negative field to suppress defects rather than over-stuffing the positive prompt. A practical bank: low quality, low resolution, distorted limbs, malformed or fused fingers, oversaturated colors, wax-like skin, no facial detail, chaotic composition, blurry or distorted text.
- Reach for exclusions when a specific artifact keeps appearing. A complete positive prompt usually produces clean results on its own.
- Where a host exposes no negative field, fold the exclusion into the positive prompt by describing the desired opposite ("clean even skin texture" rather than "no wax-like skin").

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Expecting legible in-image text: Wan image does not document it; switch to Qwen-Image when words must be readable.
- Tag soup: rewrite disconnected keywords as one descriptive scene with named components.
- Over-stacked quality tags: piling on "8K, ultra HD, masterpiece, best quality" adds little. Spend words on subject, material, and light.
- Fighting the rewriter: with prompt rewriting on, redundant detail is wasted; either trust the expansion or turn it off and write the full prompt.
- Vague editing instructions: name the reference images by position and say which attribute comes from which, or the compose step is left to guesswork.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

- Official (Alibaba, Wan): [text-to-image prompt guide (Wan text-to-image V2)](https://www.alibabacloud.com/help/en/model-studio/text-to-image-prompt), [Wan image generation and editing reference](https://www.alibabacloud.com/help/en/model-studio/wan-image-generation-api-reference).

Last verified: 2026-05-31.
