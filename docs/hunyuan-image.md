---
guide: "HunyuanImage (family)"
prompt_scheme: "hunyuan-image"
models:
  - { id: "hunyuan-image-3.0-instruct", access: "open-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, structured-layout, reasoning], best_for: "editing, multi-image fusion, and briefs you want the model to reason about and expand before it draws" }
  - { id: "hunyuan-image-3.0-instruct-distil", access: "open-weights", tier: "distilled", caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, structured-layout, reasoning], best_for: "the same instruction and editing behavior at lower cost; reach for it to iterate, then finish on the flagship" }
  - { id: "hunyuan-image-3.0", access: "open-weights", tier: "base", caps: [text-to-image, text-rendering, structured-layout], best_for: "text-to-image only, with your words used exactly as written and no rewriting stage in the way" }
capabilities: [text-to-image, image-edit, multi-image-fusion, text-rendering, structured-layout, reasoning]
prompt:
  languages: ["en", "zh", "mixed"]
  formula: "main subject and scene, then image quality and style, then composition and perspective, then lighting and atmosphere, then technical parameters; extra keywords may sit before or after that spine"
  length_strategy: "long and specific wins. The owner's own reference prompts run several hundred words across four or five paragraphs, one axis per paragraph, closing on a single sentence that names the overall style"
  literal_text: "quote the exact words, name the surface they sit on, describe the type treatment, and say which language the text is in; short strings render far better than paragraphs"
  auto_expand_behavior: "the instruct models can think about a prompt and rewrite it before drawing, so a sparse brief is expanded for you; when your wording is already exact, use the host path that draws directly instead of the rewriting one"
  references: "address inputs by ordinal position, Image 1 and Image 2, and weld each borrowed element to its source; no at-sign and no brackets"
  negatives: "no negative prompt field; state the desired condition in the positive prompt instead"
sources:
  official: ["https://github.com/Tencent-Hunyuan/HunyuanImage-3.0", "https://github.com/Tencent-Hunyuan/HunyuanImage-3.0/blob/main/Hunyuan-Image3.md", "https://huggingface.co/tencent/HunyuanImage-3.0-Instruct", "https://huggingface.co/tencent/HunyuanImage-3.0"]
  provider: ["https://wavespeed.ai/blog/posts/hunyuan-image-3-0-complete-guide-2026/"]
  community: []
last_verified: "2026-08-07"
---

# HunyuanImage: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution options, input counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the HunyuanImage 3.0 family: the base text-to-image checkpoint, the Instruct checkpoint, and the distilled Instruct checkpoint. They share one prompt grammar; the Instruct checkpoints add reasoning, self-rewriting, editing, and fusion on top of it.
- The owner writes the name closed up as HunyuanImage-3.0. The spaced form "Hunyuan Image 3.0" appears widely and means the same model.
- Write long. This model is built to read several hundred words of prose and use nearly all of it, which is the opposite of the brevity that suits most video models. Detail here is control, not decoration.
- Write flowing prose in paragraphs, not comma-separated tag lists.

</rules>

## TL;DR

<template id="quickstart">

{shot type} of {main subject and what it is doing} in {scene}, {composition and perspective}, {lighting and atmosphere}, {lens or camera detail}. The overall image presents a {style} style.

</template>

## Models and when to use which

All three take the same prompt. What differs is what happens to it before the image is drawn.

- **Instruct**: the flagship. It can reason about a brief, rewrite it into a fuller description, and then draw. It is also the only line that edits an existing image or fuses several inputs.
- **Instruct-Distil**: the same instruction behavior with fewer sampling steps. Use it to explore composition and wording, then finish on the flagship.
- **Base**: text-to-image only, and it does not rewrite anything. Your prompt is what the model sees.

<rules id="model-choice">

- Choose Base when your prompt is already fully specified and you want it honored literally. Nothing stands between your words and the image.
- Choose Instruct when the brief is sparse, when you want the model to resolve the ambiguity for you, or when the task is editing or fusion.
- A fully written prompt sent to Instruct on its rewriting path can come back reinterpreted. If you have spent effort on exact wording, use the host's direct-generation path so the rewrite stage does not restate your prompt in its own terms.
- Editing and multi-image fusion do not exist on Base. A prompt written against an input image has nothing to attach to there.

</rules>

## How the model reads prompts

<rules id="reading">

- Describe the main subject and its action first, then the environment, then the style. Content priority is the owner's stated rule and it holds across every example.
- Long prompts are the intended input, not an edge case. Several hundred words across several paragraphs is normal, and the model uses the fine detail rather than averaging it away.
- Give each paragraph one job: overall shot and mood, then subject, then environment, then lighting. Mixing all four into one block is what makes long prompts turn to mush.
- Close on a style sentence. Every reference prompt the owner publishes ends by naming the overall look in one line, such as "The overall image presents a cinematic, photorealistic photography style". It reads as a summary and acts as a global instruction.
- The instruct models may think about the prompt and rewrite it before drawing. That is why a two-line brief still produces a detailed image, and why exact wording can drift if you did not want the expansion.
- Where the output shape is not fixed by the host, the model infers it from the prompt. Naming the artifact, a magazine cover, a poster, a nine-panel tutorial sheet, steers the proportions as well as the content.
- Both Chinese and English are first-class. Chinese can carry Chinese cultural subject matter more precisely; otherwise write in whichever language your text strings need.

</rules>

## Prompt structure

The owner gives two formulas: a universal one for a simple prompt, and a longer spine for a fully specified one. Both are defaults rather than cages, and extra keywords may sit before or after either.

<rules id="structure">

- The universal formula is subject, action, scene. Avoid tag-form prompts entirely and describe the imagined scene in natural language; that instruction is the first line of the owner's handbook.
- The full spine extends it: main subject and scene, then image quality and style, then composition and perspective, then lighting and atmosphere, then technical parameters.
- Close on a style sentence. The owner states this as its own step, to re-emphasize the style and strengthen the overall style response, and every published reference prompt ends that way.
- Technical parameters means camera language, and the owner's photography examples spend it freely: focal length and lens type (85mm portrait lens, 100mm macro), aperture (f/1.8 wide open), shutter speed for frozen motion (1/4000s), camera format (medium format), and technique (focus stacking, a polarizing filter to cut reflections). Naming where focus falls, such as on the subject's eye, is part of it.
- Name materials and textures explicitly. Velvet, stucco, brushed titanium and matte plaster all render distinctly, and texture words carry more weight than quality adjectives.
- State the palette as an interplay rather than a list: "a balanced interplay of deep teal and rich red" does more than naming two colors.
- Keep one idea per sentence. Long prompts survive on sentence discipline, not on commas.

</rules>

<template id="general">

{shot type} captures {main subject} in {setting}, creating {mood}.

{The subject in detail: posture, wardrobe, materials, expression, and how light falls on them.}

{The environment: what is behind the subject, how sharply it is rendered, and the palette.}

{The lighting: key source and direction, shadow character, contrast, and what stays visible in the dark areas.}

The overall image presents a {style} style.

</template>

<example use_case="flagship-long-form">

```text
A cinematic medium shot captures a young woman seated on an ornate vintage armchair within a dimly lit room, creating an intimate and theatrical atmosphere.

She sits in a relaxed yet elegant posture, her gaze directed slightly away from the camera, wearing a simple dress in a dark teal hue whose fine-woven texture catches the light. The armchair is upholstered in deep red velvet, the fabric showing intricate texture and slight signs of wear. Her skin has a soft, matte quality, and the light delicately models the contours of her face and arms.

Behind her, partially blurred by a shallow depth of field consistent with an f/2.8 aperture, the wall carries a subtle damask-patterned wallpaper. The palette is a carefully balanced interplay of deep teal and rich red.

A single key light positioned off-camera projects gobo patterns across the woman and the back wall, casting intricate shapes of light and shadow. Some shadows are deep and defined, others soft, wrapping around the subject without losing detail in the darker areas.

The overall image presents a cinematic, photorealistic photography style.
```

*Why: the house long-form pattern. One paragraph per axis, camera language stated as an aperture rather than as "blurry background", and a closing sentence that fixes the style globally.*

</example>

<example use_case="compact-five-part">

```text
A low-angle wide shot of a lone lighthouse on a basalt headland, rendered in a high-detail realistic style. The tower sits slightly right of center with the horizon low in the frame. Cold blue pre-dawn light rakes in from the left, the beam cutting through thin sea mist. Shot on a 24mm lens with deep focus. The overall image presents a restrained, naturalistic landscape photography style.
```

*Why: the full five-part spine in five sentences. Useful when you want the structure without the length, and a good starting point to expand paragraph by paragraph.*

</example>

<example use_case="sparse-brief-for-rewriting">

```text
A rainy Tokyo alley at night, neon signs, a single figure with an umbrella.
```

*Why: deliberately underspecified, and only worth sending to an instruct checkpoint on its rewriting path, where the missing composition, lighting and lens get filled in for you. The same line on the base checkpoint produces a much thinner image, because nothing stands between it and the renderer.*

</example>

## Photorealism and style

<rules id="style">

- Name the medium and the era rather than stacking quality words. "Post-impressionist oil painting with heavy impasto" beats "beautiful, masterpiece, highly detailed".
- For photographic looks, spend words on light behavior: hard or soft key, direction, contrast ratio, whether shadows retain detail. That is what separates a photograph from a render.
- Chiaroscuro, gobo patterns, rim light and ambient occlusion are all understood as named techniques.
- One style per image. A conflicting pair such as "photorealistic anime" makes the model pick or blend badly.
- The closing style sentence is where a style belongs. Scattering style words through the description competes with the subject.
- Named styles the owner demonstrates directly: cartoon, old photograph, black-and-white manga, American comic, Japanese manga, steampunk, pixel art, 3D render, cyberpunk, post-apocalyptic wasteland, graffiti, ink wash, oil painting and watercolor. Naming one of these does more than describing it loosely.
- Material is a style axis of its own, and works especially well on lettering. Clay, plush, felt, transparent, frosted, gel, lava, flocked, stone, metal, glass, cloud, sand, wool, vinyl, foam, acrylic, plastic and tulle are all demonstrated.

</rules>

<template id="material-lettering">

A front-facing composition. The word "{text}" rendered in 3D as {material}, forming the absolute central subject of the frame, against a plain {color} background.

</template>

<example use_case="material-study-grid">

```text
A two-by-two grid in a product visualization style, showing the same rabbit model rendered in four materials. The rabbit sits upright with ears raised, facing forward, in an identical pose in every cell, against a uniform neutral dark grey background.

Top left: matte white plaster, smooth and non-reflective, with soft ambient occlusion gathering where the ears meet the head and the limbs meet the body.

Top right: flawless clear glass, showing believable refraction so the background distorts through the body, with crisp specular highlights running along the contours.

Bottom left: brushed titanium, with anisotropic reflections, a cool grey metallic sheen, and sharp highlights against deep shadow that define the solid form.

Bottom right: dense soft grey fur, individual strands visible, light catching the tips to form a gentle halo while the interior shadow stays deep and soft.

The whole grid is lit by soft, even studio light from several directions so every material reads clearly, with no blown highlights. The overall image presents a highly realistic 3D rendering style.
```

*Why: one pinned variable (the pose) and one varying axis (the material), with each cell given its own paragraph. Naming the grid shape in the first line also steers the output proportions.*

</example>

## Text rendering

Text is one of this family's strengths in both Chinese and English, and it responds to the same specificity as everything else.

<rules id="text">

- Put the exact words in quotes, and say what language they are in when the prompt is mixed.
- Name the surface the text sits on: a poster, a shop sign, a book cover, a UI panel.
- Describe the type treatment: weight, case, serif or sans, color, and alignment. "A line of large black bold sans-serif type, centered" is actionable; "nice typography" is not.
- Place text explicitly in the frame, and state its position relative to the subject.
- Sequence multiple strings rather than listing them: "at the bottom center, bold text reads {A}, followed by {B} below it".
- For a bilingual layout, give each string its own sentence with its own treatment rather than describing both at once. The same prompt written in Chinese or in English produces equivalent results, so choose the language your strings need.

</rules>

### Long text

Long passages are a supported capability here rather than a limitation, and they have their own technique.

<rules id="long-text">

- Split a long passage into several sentences, each with its own quoted string. One giant quoted block is where accuracy falls apart; several short quoted strings hold.
- Label the position of each string before you quote it. "The first line reads {A}. The second line reads {B}." is the documented form, and works the same way for "on the left", "on the top", "at the bottom".
- Structure a document-like image the same way: name the title, then each paragraph, then each bullet, quoting every one and saying where it sits.
- If the text comes out wrong, the layout is the lever, not the wording. Change the aspect ratio, or reorganize the arrangement, for instance from a side-by-side layout to a stacked one, and generate again.
- Ask for the writing implement and surface when it matters: handwriting on paper, marker on a glass whiteboard, and printed type all render differently.

</rules>

<example use_case="bilingual-poster">

```text
A modern graphic design poster, simple and centered. The subject is a rounded 3D cartoon penguin standing in the middle of the frame, its body glossy black with a pure white belly, a small yellow beak, yellow feet, and a red scarf tied neatly at its neck with a soft cloth texture.

The background is a smooth gradient from pale blue at the top to white at the bottom, with a few faint out-of-focus light discs and soft abstract beams behind the penguin.

Text sits in the lower area, centered. The upper line reads "HunyuanImage 3.0" in large black bold sans-serif type. Below it, a smaller line in dark grey bold sans-serif reads "Native Multimodal Model". Both lines are clean and highly legible.

Lighting is bright and even with no strong shadows. The overall image presents a modern, minimal graphic design poster style.
```

*Why: two strings, each quoted with its own weight, color and size, placed in a named region. The subject and background are settled before the type is introduced, so the layout does not fight the illustration.*

</example>

<example use_case="signage-in-scene">

```text
A street-level photograph of a narrow bakery frontage at dawn. A hand-painted wooden sign above the door reads "MORNING LOAF" in cream serif capitals with slight brush texture, slightly weathered. Warm interior light spills through the window onto wet cobbles. Shot on a 35mm lens at a shallow depth of field. The overall image presents a warm documentary photography style.
```

*Why: a short string bound to a physical object and a material, which is far more reliable than asking for text in the abstract.*

</example>

<example use_case="long-text-per-line">

```text
A blank sheet of A4 paper, with a poem written on it in handwritten script.

The first line reads "Quan Shan Yue", then "Li Bai".
The second line reads "The bright moon rises over the Tian Shan, amid a vast sea of clouds".
The third line reads "The long wind blows ten thousand miles, past the Jade Gate Pass".
The fourth line reads "The Han armies march down the Baideng road, the Hu peer at Qinghai Bay".

The paper is lit evenly from the front with a soft shadow at its edge. The overall image presents a clean, high-detail photographic style.
```

*Why: the owner's long-text pattern. Every line is quoted separately and prefixed with its position, which is what keeps a multi-line passage accurate where one long quoted block would not.*

</example>

<example use_case="long-text-document">

```text
A wide photograph of a glass whiteboard in a room overlooking a city skyline, with a person pointing at the handwriting on it. The handwriting is in marker and slightly messy.

At the top, the title reads "HunyuanImage 3.0", followed by two paragraphs. The first paragraph reads "HunyuanImage 3.0 is an open-source model that generates images from complex text with superior quality." The second paragraph reads "It leverages world knowledge and advanced reasoning to help creators produce professional visuals efficiently."

At the bottom there is a section that says "Key Features", followed by four points. The first is "Native Multimodal Large Language Model". The second is "The Largest Text-to-Image MoE Model". The third is "Prompt-Following and Concept Generalization". The fourth is "Native Thinking and Recaption".

The overall image presents a natural, documentary photography style.
```

*Why: a whole document laid out by naming each element and its position before quoting it, title then paragraphs then bullets. The writing implement and surface are stated, which is what makes the handwriting read as marker on glass rather than as printed type.*

</example>

## Structured layouts

Position labels are the unifying technique across every structured format this model handles. Panels, grid cells and lines of text all work the same way: say where the thing sits, then say what it is.

<rules id="layout">

- Declare the format and the style in the opening sentence, before any cell content: how many rows and columns, and what the overall look is.
- Walk the cells in reading order, each with its own position label. Row by row for a grid ("the first row, first cell ...; the second row, left cell ..., middle cell ..., right cell ..."), or panel by panel for a strip ("panel one ..., panel two ...").
- Pin what stays identical across cells explicitly, or the model will vary it.
- For numbered sequences, say the numeral appears and where it sits in each frame.
- Keep the background and lighting uniform across cells unless variation is the point; a shared background is what makes a grid read as one image.
- Repeat the style at the end. On multi-cell work the owner treats the closing style line as load-bearing, because it is what pulls independently described cells into one coherent image.
- If a cell needs a caption, say so as its own clause: "below it there is text reading {word}".
- Expand the detail rather than leaving cells terse. The owner's advice on both comic and sticker layouts is that filling in more of the imagined detail improves the result.

</rules>

<template id="panels">

{A statement of the format and overall style}. Panel one, {beat}. Panel two, {beat}. Panel three, {beat}. Panel four, {beat}. The overall visual presents a {style} style.

</template>

<example use_case="four-panel-comic">

```text
A black-and-white four-panel comic in a clean line-art style.

Panel one, a small round robot waves at the reader, and a speech bubble above it reads "Hello, I am HunyuanImage 3.0".

Panel two, the robot holds up a glowing stylus and points at a floating outline of a cat, with a speech bubble reading "An AI image model".

Panel three, the robot stands proudly beside a finished oil painting of the cat on an easel, and a speech bubble reads "It turns your words into pictures".

Panel four, the robot throws both arms up with stars in its eyes as confetti falls around it.

The overall visual presents a crisp black-and-white manga style.
```

*Why: the format is declared first, each panel gets one beat and one quoted line, and the closing sentence restates the style so four separately described panels read as one strip.*

</example>

<example use_case="sticker-grid">

```text
An image presented in a pixel art style, the overall composition a standard nine-cell grid of three rows by three columns, showing nine independent penguin stickers on a plain light background.

The first row, first cell, the penguin shows a happy expression; middle cell, it looks sad; right cell, it looks angry.

The second row, left cell, the penguin looks shocked; middle cell, it wears sunglasses and looks cool; right cell, it is crying loudly.

The third row, left cell, the penguin looks shy; middle cell, it is thinking with a hand to its chin; right cell, it waves goodnight with eyes closed.

Below each penguin there is a short caption naming its mood. The overall visual presents a pixel art style.
```

*Why: nine cells addressed by row and position, one emotion each, a single caption rule stated once, and the style named at both ends. This is the same position-label discipline as the long-text pattern, applied to a grid.*

</example>

<example use_case="numbered-tutorial-sheet">

```text
An eye-level view of a nine-panel tutorial sheet showing how to draw a parrot in pencil. Nine equally sized square frames sit in three rows of three, evenly spaced on a light grey background.

The first row covers the opening steps. Frame one blocks in the basic geometry with simple pencil lines: a circle for the head and a larger oval for the body, with a small sans-serif numeral "1" in its upper right corner. Frame two adds a triangular beak outline and a long curved line for the tail, numbered "2". Frame three refines the silhouette, adding the crest and the circular outline of the eye, numbered "3".

The second row adds structure. Frame four adds the wing shape and a horizontal branch beneath the bird, numbered "4". Frame five separates the feather groups on the wing and tail with short strokes and draws the claws gripping the branch, numbered "5". Frame six introduces cross-hatched shading under the wing and along the belly, numbered "6".

The third row completes the drawing. Frame seven deepens the hatching and adds feather texture and a highlight in the eye, numbered "7". Frame eight develops the branch with bark texture and knots, numbered "8". Frame nine is the finished study with refined lines and strong tonal contrast, numbered "9".

The lighting is even and bright with no directional source, keeping every step legible. The overall image presents a clean, orderly digital illustration tutorial style.
```

*Why: rows grouped into stages, each frame given one instruction plus its numeral, and a stated flat lighting scheme so nothing in the sheet reads as a lit scene.*

</example>

## Image editing

Editing is an Instruct capability. The prompt is an instruction against the supplied image.

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Remove, Replace, Restyle) or the constraint (Keep), but the opening clause must instruct rather than describe.
- NAME WHAT MOVES, PIN WHAT STAYS. State the change, then name what has to survive it: subject identity, pose, background, lighting, framing.
- Scope the change. Say whether it applies to one element or the whole frame; an unscoped instruction gets applied unevenly.
- Describe the target state, not the editing operation. "The wall is bare grey concrete" lands better than "remove the clutter from the wall".
- Because the instruct path may reason about the edit before performing it, a clear statement of intent helps more than a list of micro-adjustments. Say what the finished image should be.

</rules>

<example use_case="style-transfer">

```text
Restyle the entire photograph as a post-impressionist oil painting with heavy impasto, visible directional brushstrokes, and a warm ochre and deep blue palette. Keep the composition, the subject's pose and proportions, and the direction of the light exactly as they are in the original.
```

*Why: pure style transfer. The restyle is scoped to the whole frame, the target medium is named concretely, and the closing sentence pins the three things a restyle most often drags along with it.*

</example>

<example use_case="style-transfer-plus-edit">

```text
Restyle the photograph as a 1950s comic-book illustration with bold ink outlines, halftone shading, and flat spot colors, and replace the plain background wall with a rain-streaked city street at night. Keep the man's face, posture, and the position of his hands unchanged, and keep the light on him coming from the upper left as it does now.
```

*Why: a global restyle and a scoped replacement in one instruction, each naming its own extent, with identity, posture and light direction pinned so the second change cannot disturb the subject.*

</example>

<example use_case="targeted-removal">

```text
Remove the parked scooter from the foreground and leave the pavement beneath it as clean wet asphalt continuous with the rest of the street. Keep everything else in the frame identical, including the reflections in the shop window and the people in the background.
```

*Why: names the target state of the vacated area rather than only the removal, which is what stops the model inventing something new in the gap.*

</example>

## Multi-image fusion

Fusion combines several supplied images into one coherent result. It is an Instruct capability.

<rules id="fusion">

- Address inputs by ordinal position: Image 1, Image 2, Image 3, numbered in the order you supply them. There is no at-sign and no bracket in this family's notation.
- ONE ROLE PER INPUT. Weld each borrowed element to its source: "the logo from Image 1", "the material from Image 2", "the setting from Image 3". An unattached noun is ambiguous the moment there is more than one input.
- Say what the finished object is, not just what to take. The owner's own example ends by naming the artifact to produce, which gives the borrowed parts something to assemble into.
- Give each input a different kind of job where you can. Identity, material, and setting compose cleanly; two inputs both claiming the subject's face do not.
- Pin the attributes that must survive from a given input, especially shape, proportion, and any lettering.

</rules>

<template id="fusion">

Using {the element} from Image 1 and {the element} from Image 2, create {the finished artifact}. Keep {what must survive} exactly as it appears in {its source}.

</template>

<example use_case="fusion-two-source">

```text
Using the logo from Image 1 and the material and finish of the fridge magnet in Image 2, create a new fridge magnet. Keep the logo's shape, proportions, and lettering exactly as they are in Image 1, and apply the glossy moulded plastic surface, rounded bevel, and soft edge highlight from Image 2.
```

*Why: two inputs, two distinct jobs, and the invariant spelled out. The instruction ends by naming the object to be produced, so the borrowed graphic and the borrowed material have a defined thing to become.*

</example>

<example use_case="fusion-three-source">

```text
Using the woman from Image 1, the embroidered jacket from Image 2, and the rain-slicked night market from Image 3, create a single photograph of her wearing the jacket while walking through that market. Keep her face and hair exactly as they appear in Image 1 and keep the jacket's embroidery pattern and color unchanged from Image 2. Light her with the market's warm stall lighting so she belongs to the scene rather than being placed on top of it.
```

*Why: three inputs in three roles, identity and pattern pinned to their own sources, and a final sentence that reconciles the lighting so the composite reads as one photograph.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative prompt field in this family, so every exclusion belongs in the positive prompt.
- State the condition you want instead of the one you are avoiding. "The sky is a clear unbroken blue" removes the clouds more reliably than forbidding them.
- Where a plain exclusion is genuinely the clearest phrasing, keep it short, concrete, and grouped at the end rather than scattered.
- Do not paste a stock defect list from a tag-driven model. Long boilerplate exclusions dilute a prompt this model was built to read closely.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Conflicting instructions: "photorealistic anime" forces the model to pick or to blend badly. Choose one style and commit.
- Quality-word stacking: "masterpiece, best quality, ultra detailed" adds nothing here. Spend those words on materials, light behavior, and lens.
- Tag lists: this is a prose model. Comma-separated keyword piles underperform the same content written as sentences.
- One giant paragraph: long prompts need one axis per paragraph. Mixing subject, environment and lighting into a single block is where long prompts lose coherence.
- Missing style sentence: without the closing line naming the overall look, style is left to be inferred from scattered adjectives.
- Impossible physics: descriptions that violate how light or materials behave produce strange results rather than surreal ones. Ask for surrealism explicitly if that is the intent.
- Too many competing subjects: several elements each demanding to be the focus flattens all of them. Name the hierarchy.
- Expecting exact wording on a rewriting path: if the model is set to expand your prompt, it will restate it. Use the direct path when your phrasing is deliberate.
- Editing or fusion prompts aimed at the base checkpoint: it is text-to-image only, and an instruction about an input image has nothing to attach to.
- Bare references in fusion: "the jacket" with three inputs supplied is ambiguous. Always say which image it comes from.

</rules>

## Sources

Trust order is official first, then provider, then community; the owner wins on any conflict.

- Official (Tencent Hunyuan): [HunyuanImage-3.0 repository](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0), [the repository's own prompt guide](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0/blob/main/Hunyuan-Image3.md), [the Prompt Handbook](https://docs.qq.com/doc/DUVVadmhCdG9qRXBU), [Instruct model card](https://huggingface.co/tencent/HunyuanImage-3.0-Instruct), [base model card](https://huggingface.co/tencent/HunyuanImage-3.0).
- Provider: [WaveSpeed HunyuanImage 3.0 guide](https://wavespeed.ai/blog/posts/hunyuan-image-3-0-complete-guide-2026/).

Coverage note: the Prompt Handbook is the richest owner source and is written in Chinese. The universal subject-action-scene formula, the position-label technique for long text and grids, the panel and sticker templates, the material list and the instruction to close on a style sentence all come from it. The five-part spine and the content-priority rule are corroborated by the repository guide. Long text is a documented capability with its own technique here, which is why this guide does not carry the common advice to keep rendered strings short; that advice came from a provider and the owner demonstrates the opposite.

The fusion notation is taken from the owner's documented editing example, which is written in Chinese and addresses inputs by ordinal position; the English rendering as Image 1 and Image 2 follows that pattern and is worth re-checking when an English example is published.

Last verified: 2026-08-07.
