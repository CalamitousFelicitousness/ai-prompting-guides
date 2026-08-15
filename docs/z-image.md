---
guide: "Z-Image"
prompt_scheme: "z-image"
models:
  - { id: "z-image", access: "open-weights", tier: "base", caps: [text-to-image, text-rendering, bilingual], best_for: "maximum control and diversity: full CFG, negative prompts, and reference-image guidance, with varied identities, poses, and compositions across seeds" }
  - { id: "z-image-turbo", access: "open-weights", tier: "distilled", caps: [text-to-image, text-rendering, bilingual], best_for: "fast few-step generation; positive-only prompting (negatives are inert); deterministic, photoreal, with bilingual in-image text" }
capabilities: [text-to-image, text-rendering, bilingual]
prompt:
  languages: ["en", "zh"]
  literal_text: "wrap the exact words in straight double quotes and write them in the script you want rendered (the model does not translate them); weld the text to its surface and position; for posters, label each text block by role (headline, subtitle) with its position and font, then the quoted string"
  length_strategy: "describe what is literally visible in plain, concrete terms; it was trained on both short and long captions, so short and detailed prompts both work; do not pad with vague adjectives; a focused detailed prompt gives the most control, and Turbo infers sensible defaults from short prompts"
  negatives: "Base supports negative prompts (use them, paired with a positive counter-cue); Turbo runs without classifier-free guidance so negatives are ignored, fold every exclusion into the positive prompt"
  auto_expand_behavior: "an optional prompt enhancer (an LLM front-end) can expand a short or abstract prompt and inject world knowledge before generation; enhanced prompts are in-distribution; without it, name specific entities and details yourself"
sources:
  official: ["https://huggingface.co/Tongyi-MAI/Z-Image", "https://huggingface.co/Tongyi-MAI/Z-Image-Turbo", "https://github.com/Tongyi-MAI/Z-Image", "https://arxiv.org/abs/2511.22699"]
  provider: ["https://fal.ai/learn/devs/z-image-turbo-prompt-guide", "https://wavespeed.ai/blog/posts/blog-what-is-z-image-base/", "https://wavespeed.ai/blog/posts/blog-z-image-turbo-on-wavespeed/"]
  community: []
last_verified: "2026-06-06"
---

# Z-Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the Z-Image text-to-image family from Tongyi: Z-Image (the Base model) and Z-Image-Turbo (the distilled few-step model). They share one prompt scheme; a prompt written for one transfers to the other.
- Write prompts as plain, concrete natural-language description. The model rewards literal, factual detail over vague or flowery wording.
- One difference matters between the two: negative prompts work on Base but are ignored on Turbo (Turbo runs without classifier-free guidance), so on Turbo every exclusion must be phrased as a positive instruction.
- This release is text-to-image. Native editing is a separate model (Z-Image-Edit) that is not yet released, so this guide has no editing section; hosts that expose image-to-image and reference inputs are covered as a host feature below.

</rules>

## TL;DR

<template id="quickstart">

{subject with concrete attributes and action}, {setting and key objects}, {lighting described like a photographer}, {camera or lens for the effect}, {one or two style cues}. For in-image words, add: a {sign, label, or title} that reads "{exact text}" in {described type and position}.

</template>

## Models and when to use which

Both models share one prompt grammar; pick by the job.

- `z-image` (Base): the non-distilled model. It runs full classifier-free guidance, so it takes negative prompts and reference-image guidance and gives finer, more linear control. It also produces higher diversity across seeds (varied identities, poses, and compositions). Reach for it when you need control, negatives that stick, or variety.
- `z-image-turbo`: the distilled few-step model. Very fast and more deterministic (lower seed-to-seed variety), strong on photorealism and bilingual text. It runs without classifier-free guidance, so negative prompts do nothing here; put every constraint in the positive prompt.
- A common workflow is to explore quickly on Turbo, then switch to Base once a direction is worth refining.
- Native editing (Z-Image-Edit) and a combined generate-plus-edit model are separate and not yet released; do not expect the text-to-image checkpoints to edit an input image.

## How the model reads prompts

- Plain and factual wins. The model was trained on objective descriptions of what is literally visible, so concrete detail beats subjective words; "weathered hands pruning roses" guides it, "beautiful" does not.
- It is bilingual. English and Chinese are both first-class, and you can mix them in one prompt; write any in-image text in the script you want it rendered in, because the model renders the characters you give it rather than translating them.
- Length is flexible. It handles both short prompts and long detailed ones, so do not pad. A focused, detailed prompt gives the most control; Turbo in particular fills in sensible defaults from a short prompt, and over-stuffing it tends to add noise rather than detail.
- Lead with the subject. Earlier words steer the composition, so open with the main subject and its key attributes, then setting, then style and camera.
- A trailing tag tail is idiomatic. After the descriptive sentence, a short comma-separated list of style and camera cues works well ("..., shallow depth of field, shot on iPhone").
- The bare model has limited world knowledge. Name specific entities, brands, and landmarks explicitly (it renders named landmarks well), or run the prompt through the optional prompt enhancer, an LLM front-end that expands a terse or abstract prompt and injects world knowledge before generation. Enhanced prompts are in-distribution; without it, do that expansion yourself.

## Prompt structure

<rules id="structure">

- Order it subject, then attributes, then setting and location, then any in-image text, then lighting, then camera, then a short style-tag tail.
- Describe light like a photographer: "soft window light, 45 degree angle, gentle falloff" gives a clearer result than "cinematic lighting".
- Name a lens or film look only for the effect you want ("35mm, shallow depth of field", "realistic iPhone grain"); generic brand-dropping alone adds little.
- Be literal about layout: state composition and negative space ("centered subject, generous negative space, room for a headline at top").
- Put orientation in words ("vertical composition", "wide panoramic", "square"); the model reads it from the prompt.
- Keep style labels to about two; stacking many ("watercolor, oil, graphite, gouache, pastel") muddies the output.

</rules>

<template id="general">

{age and description of subject} with {distinctive features} wearing {clothing and accessories}, {expression or action}. {Setting and key objects}. The lighting is {direction and quality}. Shot on {camera} with {lens}, {time of day}. {One or two style cues}.

</template>

<example use_case="photoreal-flagship">

```text
A stylish young woman sits casually on an unmade bed bathed in soft daylight, wearing a pastel yellow oversized T-shirt with subtle white text and cozy light gray sweatpants. Her skin glows fresh beneath glossy deep lavender hydrogel under-eye patches, while her hair is tied back loosely with a scrunchie, complemented by delicate gold hoop earrings. Nearby, a tube of hand cream and an open laptop rest atop soft, slightly rumpled sheets. The natural window light gently illuminates her radiant skin and the subtle sheen of the hydrogel patches. Shot from a top-down selfie angle capturing her face, shoulders, and upper torso with realistic iPhone grain. Skincare selfie, shot on iPhone.
```

*Why: the full formula at scale, subject and wardrobe first, then props, then lighting and a top-down camera, closing with a short style-tag tail, all in plain factual language*

</example>

<example use_case="turbo-short">

```text
Street at dusk after rain, neon reflections, lone cyclist, motion blur gentle, wide angle, moody blue-magenta.
```

*Why: a terse fragment prompt, which Turbo handles well by inferring defaults; subject first, then setting, mood, camera, and palette as compact cues*

</example>

## Text rendering

Legible in-image text is a Z-Image strength, in English and Chinese, including multiple text regions in one image.

<rules id="text">

- Wrap the exact words in straight double quotes, and write them in the script you want rendered; the model renders the characters you give it and does not translate them.
- Weld the text to its surface and position: "a beanie embroidered with "...", "a sign on the wall that reads "...".
- For posters and layouts, label each text block by role and place it: give its position, font, weight, and color, then the quoted string. An explicit "Text control:" sentence that lists each line works well.
- Keep each rendered string deliberate. On Turbo, small or dense text can wobble; for pixel-exact small captions, leave space and add the type in an editor, or use Base.

</rules>

<example use_case="in-image-text">

```text
A candid mid-2010s-style snapshot of a pale young woman with icy platinum hair styled loose, seated on a metal bench inside a monochrome concept store. She wears a huge black hoodie, sheer tights, and maroon platform creepers, complemented by a beanie embroidered with "Z-Image Real & Fast". Her relaxed expression gazes off to the side. The lighting is cold and matte with soft shadows along a wooden floor, muted color saturation, cool bluish-gray shadows. The framing is slightly off-center and casually tilted, an informal snapshot aesthetic.
```

*Why: the literal words are quoted and welded to their surface (the beanie), inside an otherwise plain photoreal description*

</example>

<example use_case="poster-multi-text">

```text
A vertical movie poster, bold cinematic illustration. Text control: in the top center, in large white condensed sans-serif, the title reads "NIGHT TRAIN"; directly below, in a smaller gold serif, the tagline reads "Every stop is a choice"; in the bottom-left corner, in small white text, the credit reads "In theaters Spring 2026". A lone figure stands on an empty platform under a single sodium lamp, long shadows, deep teal and amber palette, heavy fog, dramatic low angle.
```

*Why: each text block is labeled by role, placed, and given a font and color before its quoted string, which is how multi-region typography stays organized*

</example>

## By use-case

<example use_case="product">

```text
A professional product photo of a brushed-steel wristwatch on a dark slate background. The textured dial, knurled crown, and sapphire crystal are clearly visible. Lit with soft directional studio light from the upper left, raking across the metal to catch the brushing. Shallow depth of field, sharp focus on the dial.
```

*Why: one clear product, its features named, with directed light and a stated focus, the concrete register the model rewards for commercial work*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- On Turbo there is no negative prompt; it runs without classifier-free guidance, so a negative field is ignored. Fold every exclusion into the positive prompt by stating the desired trait: write "sharp focus", "crisp edges", "matte surface", "soft even diffuse lighting" instead of "no blur" or "no glare".
- On Base, a negative prompt works and is worth using: list specific artifacts to suppress ("no lens flare, no glossy reflections, no tilted angles") and pair them with a positive counter-cue ("matte finish, level horizon").
- Either way, prefer naming the positive state; the model responds more reliably to what you want than to what you forbid.

</rules>

<example use_case="positive-only-exclusion">

```text
A clean studio product shot of a ceramic mug on a plain white background, sharp focus, crisp edges, matte glaze, soft even diffuse lighting, no harsh highlights expressed as a smooth low-glare surface.
```

*Why: a Turbo-safe prompt where every exclusion is rewritten as an inclusion ("matte glaze, soft even diffuse lighting" stands in for "no glare", "sharp focus, crisp edges" for "no blur")*

</example>

## Image-to-image and reference (host feature)

The text-to-image models do not take an input image, but hosts add image-to-image and reference-image guidance on top of them. The prompt-craft there is the same as elsewhere in the set.

<rules id="reference">

- Name what moves, pin what stays. State the single change and the elements to keep ("change the late-morning light to warm late-afternoon golden hour, keep the object placement and composition unchanged").
- One role per reference. When a host takes more than one reference, give each a distinct job (one for color or palette, one for layout or composition) and say which contributes what.
- Keep reference influence moderate. Strong influence clones or echoes the source; moderate influence keeps continuity while letting the prompt steer the rest.

</rules>

<example use_case="img2img-relight">

```text
Same scene, change the flat midday light to warm late-afternoon golden hour with long soft shadows. Keep the subject, object placement, and overall composition unchanged.
```

*Why: an image-to-image edit that names the one thing that moves (the lighting) and pins what stays, the reliable shape for "same scene, different mood"*

</example>

## Pitfalls and anti-patterns

<rules id="avoid">

- Turbo negatives: a negative prompt does nothing on Turbo; rewrite exclusions as positive traits in the main prompt.
- Vague adjectives: "beautiful", "nice", "good" give the model little to work with; name the concrete thing that makes the image work.
- Contradictions: conflicting directives like "photorealistic cartoon" send mixed signals; pick one register.
- Over-describing: padding a prompt with detail, especially on Turbo, adds noise rather than control; state the key elements and stop.
- Stacked style labels: more than about two media labels muddy the result; keep it to one or two.
- Mixed color temperature: warm and cool cues at once often read as muddy; pick one lane unless you want the tension.
- Wrong expectations of Turbo: it is more deterministic (less seed variety) and softer on tiny text and fine detail like intricate jewelry; use Base for diversity, and leave room to add small text later.
- Expecting the text-to-image models to edit: editing is the separate, unreleased Z-Image-Edit; the released checkpoints generate from text.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. Two conflicts were resolved on owner authority: Turbo's negative prompts are inert (the owner docs and FAL state Turbo runs without classifier-free guidance; a provider blog softened this to "sometimes ignored", which this guide does not follow), and the "solved hands" claim from community posts is omitted because the owner's materials do not make it.

- Official (Tongyi): [Z-Image model card](https://huggingface.co/Tongyi-MAI/Z-Image), [Z-Image-Turbo model card](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo), [GitHub repo](https://github.com/Tongyi-MAI/Z-Image), [tech report](https://arxiv.org/abs/2511.22699).
- Provider: [fal Z-Image Turbo prompt guide](https://fal.ai/learn/devs/z-image-turbo-prompt-guide), [WaveSpeed Z-Image Base](https://wavespeed.ai/blog/posts/blog-what-is-z-image-base/), [WaveSpeed Z-Image Turbo](https://wavespeed.ai/blog/posts/blog-z-image-turbo-on-wavespeed/).

Last verified: 2026-06-06.
