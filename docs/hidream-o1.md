---
guide: "HiDream-O1 (image)"
prompt_scheme: "hidream-o1"
models:
  - { id: "HiDream-O1-Image", access: "open-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, subject-personalization, text-rendering], best_for: "highest fidelity and the full task range: text-to-image, instruction editing, and subject-driven personalization (use this one for editing)" }
  - { id: "HiDream-O1-Image-Dev", access: "open-weights", tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, subject-personalization, text-rendering], best_for: "faster generation with prompt grammar identical to the full model. The grammar is identical; the responsiveness is not. Dev is run at guidance scale 0.0 against the full model's 5.0, so a steering cue has far less to push against and seeds vary less. Same words, less leverage" }
  - { id: "HiDream-O1-Image-Dev-2604", access: "open-weights", tier: "std", caps: [text-to-image, text-rendering], best_for: "leading text-to-image with the upgraded prompt refiner; text-to-image only, no editing or personalization" }
capabilities: [text-to-image, image-edit, multi-image-reference, subject-personalization, text-rendering]
prompt:
  languages: ["en", "zh", "mixed"]
  literal_text: "wrap the exact in-image words in straight double quotes and spell them out; state font, weight, case, color, and placement; for several text regions name each region with its content and position; do not name a work by title and expect its words, write the words"
  length_strategy: "rewards dense, fully specified prompts; enumerate subject attributes, objects, explicit spatial relations, and lighting; short or long both work, but detail is rewarded and ambiguity is best resolved by you rather than left to the model"
  auto_expand_behavior: "no host auto-expansion in the direct path; an optional Reasoning-Driven Prompt Agent can rewrite a short instruction into a dense prompt, but it is opt-in and not the default, so write the full prompt yourself for direct control"
  negatives: "no negative field in the core scheme; fold exclusions into the positive prompt as preservation clauses (keep X unchanged) or a short inline clause (no text, empty background)"
  references: "subject-driven: the reference images define and pin the subject(s); describe each subject or object by its distinguishing attributes in the prompt; do not index inputs as image 1 or image 2, the prompt carries scene, placement, and appearance while the references carry identity"
sources:
  official: ["https://github.com/HiDream-ai/HiDream-O1-Image", "https://huggingface.co/HiDream-ai/HiDream-O1-Image", "https://huggingface.co/HiDream-ai/HiDream-O1-Image-Dev-2604", "https://arxiv.org/abs/2605.11061"]
  provider: ["https://wavespeed.ai/blog/posts/hidream-o1-image-dev-pixel-unified-transformer/", "https://wavespeed.ai/models/wavespeed-ai/hidream-o1-image/text-to-image", "https://wavespeed.ai/models/wavespeed-ai/hidream-o1-image/edit", "https://fal.ai/models/fal-ai/hidream-o1-image"]
  community: []
last_verified: "2026-06-01"
---

# HiDream-O1: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the HiDream-O1-Image family: HiDream-O1-Image (full), HiDream-O1-Image-Dev (distilled), and HiDream-O1-Image-Dev-2604 (text-to-image). They share one prompt scheme, so a prompt written for one transfers to the others.
- HiDream-O1 is a unified image model: one model does text-to-image, instruction editing, and subject-driven personalization with the same prompt grammar. The task is set by whether you attach source or reference images, not by changing how you write.
- Write prompts as coherent natural-language description, not comma-separated tags. The model rewards dense, fully specified prose.
- The Reasoning-Driven Prompt Agent is OPTIONAL and not the default. The general case is writing a prompt straight to the model; when you do, spell out the detail the agent would otherwise resolve (see the prompt-agent section).

</rules>

## TL;DR

<template id="quickstart">

{shot and angle}. {subject with concrete attributes and action}, {setting with key objects placed by position}, {lighting and mood}. For in-image words, add: a {sign, title, or label} that reads "{exact text}" in {described type and placement}.

</template>

## Models and when to use which

All three share one prompt scheme; a prompt written for one works on the others. Pick by task and budget.

- `HiDream-O1-Image`: the highest-fidelity option and the one to use for instruction editing and subject-driven personalization. It handles every task.
- `HiDream-O1-Image-Dev`: faster, with prompt grammar identical to the full model. Write prompts exactly as you would for the full model.
- `HiDream-O1-Image-Dev-2604`: a text-to-image-focused checkpoint with an upgraded prompt refiner, strongest for text-to-image. It does not cover editing or personalization, so reach for the full model for those.

## How the model reads prompts

- Natural language wins. Coherent descriptive sentences beat keyword lists. The model is built to follow complex, multi-clause descriptions including style, mood, and on-image text.
- It rewards density. The strongest prompts enumerate every subject attribute, material, object, spatial relation, and the lighting, rather than leaving them implied. Specificity is the working register.
- Pixel-native, one token space. Pixels, text, and task conditions share a single token space (no separate text encoder, no latent compression), so in-image text and image content come from the same model. Naming a thing tends to anchor it where you place it, and rendered text holds together.
- It does not infer what you leave out. Without the optional agent, the model will not resolve implicit world knowledge for you; if a concept carries specific visual facts, state them.
- Bilingual. English and Chinese both work, including for in-image text; well-formed English is the most reliable form for intricate prompts, and you can mix a native-language scene description with English terms.
- The "O1" name points to the optional prompt-reasoning agent, not to in-model reasoning. The generator itself is a direct one-pass sampler, so what you write is what it renders.

## Prompt structure

<rules id="structure">

- Lead with framing when it matters: a short shot-and-angle fragment first (for example, "medium shot, eye-level, front view").
- Then a one-line scene summary (subject, setting, overall mood), then the subject's identity (skin, hair, eyes, expression), then wardrobe and worn objects, each with color, material, and detail.
- Place surrounding objects with explicit spatial anchors: to her left, upper center, in the background, at the bottom. The model honors stated positions.
- Put any literal text block next (quoted), and close with lighting and atmosphere.
- Each clause you add removes one decision from the model and hands it to you; resolve ambiguity yourself rather than leaving it open.

</rules>

<template id="general">

{shot, angle, view}. {one-line scene summary}. The subject is {identity: skin, hair, eyes, expression}, wearing {wardrobe with color and material}. {Objects placed with spatial anchors}. {Lighting direction and quality}.

</template>

<example use_case="photoreal-portrait-flagship">

```text
medium shot, eye-level, front view. A woman is seated in an ornate bedroom, illuminated by candlelight, with a calm and composed expression. The subject is a young woman with fair skin, light brown hair styled in an updo with loose tendrils framing her face, and blue eyes. She wears a cream-colored satin robe with delicate floral embroidery and lace trim along the neckline. Her ears are adorned with pearl drop earrings. She is seated on a bed with a dark, intricately carved wooden headboard. To her left, a wooden nightstand holds three lit white candles and a candelabra with multiple lit candles in the background. The bed is covered with patterned pillows and a dark, textured blanket. The walls are paneled with dark wood and feature a large, ornate tapestry with muted earth tones. The lighting creates soft highlights on her face and robe, with warm shadows cast across the room.
```

*Why: the full formula at scale, framing first, then subject and attributes, then objects pinned to positions, then lighting last, every detail stated rather than implied*

</example>

## Shots, camera, and composition

<rules id="camera">

- The model is tuned for explicit cinematic direction; name the shot, the angle, and the subject's orientation.
- Shot scales: extreme full shot, full shot, medium full shot, medium shot, medium close-up, close-up, extreme close-up.
- Camera angles: high angle, low angle, eye-level, bird's-eye view.
- Subject orientation: front view, side view, back view, three-quarter view.
- Composition and framing live in the prose (centered, lower-right third, generous negative space); the model does not need a ratio token to frame a shot.
- Multi-panel layouts work in one pass: describe both the overall arrangement and what differs in each panel.

</rules>

## Text rendering

Legible in-image text is a headline strength, including long passages and several text regions, in English and Chinese.

<rules id="text">

- Wrap the exact words in straight double quotes. Unquoted words are read as scene description.
- Spell the words out. Naming a work by its title (a poem, a slogan) does not reliably produce its words; write the words you want rendered.
- Give the text a place and a style: position, font, weight, case, color, and surface.
- For several text regions, name each region with its content and position; the model holds multi-region layouts when you describe them.
- State the language for non-Latin scripts; English and Chinese both render.

</rules>

<example use_case="text-sign">

```text
A dog holds a sign that says "HiDream-O1-Image release."
```

*Why: the literal words are quoted and bound to a surface, the minimal pattern for reliable in-image text*

</example>

<example use_case="poster-with-long-text">

```text
A vintage aviation poster depicting a bright red biplane cruising over rolling farmlands under a partly cloudy sky, with saturated colors and an aged paper texture. A red biplane with two sets of wings and a radial engine is positioned in the upper center of the image, flying toward the right. A pilot with light skin, wearing a brown flight helmet, goggles, and a brown jacket, is visible in the open cockpit. Below, the landscape consists of rolling fields in shades of green, yellow, and brown, divided by dirt roads and scattered with small houses, including a red barn. In the background, a line of green trees separates the fields from distant hills under a blue sky with white clouds. At the bottom, the text "ADVENTURE IN THE FRIENDLY SKIES" is displayed in large, bold, dark brown capital letters across two lines on a light beige background.
```

*Why: a text-heavy poster that pins layout with spatial anchors and specifies the quoted headline's case, weight, color, and placement, so typography and composition both resolve*

</example>

## By use-case

<example use_case="beauty-commercial">

```text
A luxury beauty portrait of an elegant young woman, flawless glowing skin, subtle natural makeup, holding a premium skincare bottle near her face, clean beige background, soft studio lighting, high-end commercial advertising style, close-up shot, refined composition, glossy skin texture, photorealistic, ultra-detailed, beauty campaign aesthetic
```

*Why: a commercial brief with one clear subject and product, directed light, and a stated style register, the kind of detailed prompt the model follows closely*

</example>

<example use_case="product-atmospheric">

```text
A poised individual gracefully cradling an elegantly designed glass bottle in their hands, with delicate tendrils of smoke curling sensuously around the vessel and catching the light, all set against an artistically generated dreamlike background that enhances the luxurious, evocative, and timeless atmosphere of the composition. No text involved.
```

*Why: an atmospheric product shot that closes with a plain-language exclusion ("No text involved.") instead of a negative field*

</example>

## Image editing

Attach a source image and describe the change. Use the full model for editing.

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Replace, Redraw, Restore) or the constraint (Keep), but the opening clause must instruct rather than describe. A declarative setup such as "Image 1 provides the foundation, Image 2 provides the face" states the plan instead of issuing it and pushes the real instruction back by a sentence or two.
- Name the change and pin what stays. State the edit and the invariants in the same prompt (keep the same person, pose, background, lighting); stating what must not change sharply improves identity preservation.
- Describe the end state, not the process, and keep the instruction a minimal delta: name only what changes, and everything unnamed is held.
- Reference the target element explicitly (the jacket, the text on the shirt, the person on the left); avoid vague pronouns.
- Edit operations: add, remove, replace, adjust, change background, restyle. Each names a target precisely.
- For several changes, prefer sequential single-purpose edits over one long compound instruction.
- NAME WHAT MOVES, PIN WHAT STAYS: every edit states the change and the elements that must stay identical.

</rules>

<example use_case="scoped-edit">

```text
Keep the same person and pose. Change the outfit to a light gray sweater and add gold thin-rimmed glasses. Keep the background and lighting unchanged.
```

*Why: names two scoped changes and pins the person, pose, background, and lighting as invariants, so the model edits rather than regenerates*

</example>

<example use_case="background-swap">

```text
Transform the background into a rainy neon city street at night, with wet asphalt reflections, blurred neon signs, and cinematic blue-magenta lighting. Preserve the same man, face, pose, outfit, expression, and framing. Add realistic rain atmosphere and reflections without changing the subject identity.
```

*Why: a full background replacement that pins the subject down to face and framing and folds the exclusion ("without changing the subject identity") into the positive instruction*

</example>

<example use_case="style-transfer">

```text
Restyle the image as a soft watercolor painting with visible brushstrokes and paper texture. Keep the same subject, pose, and composition unchanged.
```

*Why: a pure style transfer, taking only the medium while the content and composition stay locked, phrased in the name-the-change-pin-the-rest form*

</example>

<example use_case="style-transfer-plus-edit">

```text
Restyle the photo as a 1950s comic-book illustration with bold ink outlines and halftone shading, and change the background to a busy city street. Keep the person's face, pose, and outfit unchanged.
```

*Why: combines a style transfer with a second scoped change (the background) while pinning identity, the two-edit case kept explicit*

</example>

## Multiple reference images and subject-driven personalization

HiDream-O1 takes reference images that define a subject and places it in new scenes, and it composes a primary subject with several reference objects. Identity is carried by the references; the prompt carries the scene.

<rules id="multi-image">

- The references define and pin identity; the prompt describes the new scene, placement, and appearance, written like a fresh single-image prompt.
- Do NOT index inputs in words (no "image 1", "image 2"). HiDream binds references by what you describe, not by an image number, which is the main way its multi-reference grammar differs from index-based models.
- ONE ROLE PER INPUT: each reference is one subject or object; describe each by its distinguishing attributes (color, material, detail) so the model binds it to the right slot.
- NAME WHAT MOVES, PIN WHAT STAYS: name each subject or object you are placing into the scene, and ask for its identity or appearance to be preserved across the new context.
- When the references fully specify the subject (for example a try-on with pose and garment supplied), the prompt can be a short directive; when the scene is new, write a full descriptive paragraph.

</rules>

<example use_case="multi-reference-personalization">

```text
A young boy with blonde hair stands on steps wearing light blue jeans, a white t-shirt with logo, and blue and white sneakers. He wears a brown cord necklace with beads, a black wristwatch with digital display, and carries a yellow fanny pack with white zipper. In his hand is a red boxing glove with white top, a teal plastic toy car, and a plastic toy figure of Captain America. He wears a straw hat with cream band. Natural light illuminates the scene.
```

*Why: a multi-source brief that enumerates each reference object by its distinguishing attributes so every supplied item is welded to its slot, with the scene and light described as in a single-image prompt*

</example>

<example use_case="reference-try-on">

```text
Create a realistic try-on image of the person wearing the provided clothing.
```

*Why: when the references already carry the face, pose, and garment, the prompt can stay a short directive and let the inputs do the work*

</example>

## The Reasoning-Driven Prompt Agent (optional)

HiDream-O1 ships an optional prompt agent. It is a wrapper around the model, not part of it, and it is not the default path; routine prompts go straight to the model.

<rules id="agent">

- What it is: a separate "thinking" step that runs over your raw instruction before generation and rewrites it into a dense, self-contained English prompt. It is opt-in.
- What it resolves: spatial layout, subject attributes, physical logic, contextual relationships, text rendering, and implicit world knowledge (for example, expanding a historical reference into the specific dress and props it implies, or a poem named by title into its actual lines).
- When to reach for it: intricate, reasoning-heavy requests, several text regions, specific spatial relationships, or culturally specific subjects.
- The direct-path equivalent: write that resolution yourself. A complete manual prompt states the layout, the attributes, the literal text, and any world knowledge the model would otherwise have to guess. The long flagship prompts in this guide are the kind of output the agent produces, and you can author them directly.
- Where it runs and which backend it uses are host-specific and out of scope.

</rules>

<example use_case="agent-input-vs-direct">

```text
A vintage aviation poster featuring a bright red biplane cruising over rolling farmlands. Bold blocky text at the bottom promises adventure in the friendly skies.
```

*Why: a short intent like this is what the optional agent expands into the full biplane poster prompt above; with the agent off, write that fuller version yourself*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field in the core scheme. State exclusions inside the positive prompt.
- Pin invariants as preservation clauses: "keep the background and lighting unchanged", "without changing the subject identity".
- For a clean omission, add a short inline clause: "no text", "empty background", "no people".
- To remove something from an existing image, use a positive edit instruction ("remove the object on the table"), not a negative list.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Under-specifying: the model rewards density, so a sparse prompt forgoes its strength; enumerate subject, attributes, objects, spatial relations, and light.
- Naming instead of spelling: relying on a title or a concept to carry specific words or visual facts fails without the agent; write the literal text and the concrete details.
- Assuming the agent is on: it is opt-in, so a direct prompt must resolve its own layout, attributes, and text.
- Tag soup: rewrite disconnected tags as one coherent description.
- Compound edits: one long instruction with many changes drifts; split into sequential single-purpose edits.
- Vague edit targets: name the element to change and avoid pronouns; state what stays unchanged.
- Index-style references: do not write "image 1" or "image 2"; describe each reference by its attributes.
- Wrong variant for the task: the text-to-image checkpoint does not edit or personalize; use the full model for those.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. The model owner (HiDream.ai) and the providers agree on the essentials here: dense natural-language prompts, quoted literal text, and the prompt agent as an optional wrapper rather than the default path.

- Official (HiDream.ai): [GitHub README](https://github.com/HiDream-ai/HiDream-O1-Image), [HiDream-O1-Image model card](https://huggingface.co/HiDream-ai/HiDream-O1-Image), [HiDream-O1-Image-Dev-2604 model card](https://huggingface.co/HiDream-ai/HiDream-O1-Image-Dev-2604), [arXiv paper](https://arxiv.org/abs/2605.11061).
- Provider: [WaveSpeed dev blog](https://wavespeed.ai/blog/posts/hidream-o1-image-dev-pixel-unified-transformer/), [WaveSpeed text-to-image](https://wavespeed.ai/models/wavespeed-ai/hidream-o1-image/text-to-image), [WaveSpeed edit](https://wavespeed.ai/models/wavespeed-ai/hidream-o1-image/edit), [fal HiDream-O1-Image](https://fal.ai/models/fal-ai/hidream-o1-image).

Last verified: 2026-06-01.
