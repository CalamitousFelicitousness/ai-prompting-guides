---
guide: "Qwen-Image (family)"
prompt_scheme: "qwen-image"
models:
  # hosted
  - { id: "qwen-image-3.0-pro", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-edit, text-rendering, dense-layout, ui-simulation, formula-rendering], best_for: "information-dense layouts and micro-detail realism; longest briefs, smallest legible type, nested interfaces" }
  - { id: "qwen-image-3.0",     access: "closed-weights", tier: "std",      caps: [text-to-image, image-edit, multi-image-edit, text-rendering, dense-layout, ui-simulation, formula-rendering], best_for: "the same long-brief layout control for everyday volume; posters, web pages, UI screens" }
  - { id: "qwen-image-2.0-pro", access: "closed-weights", tier: "legacy",   caps: [text-to-image, image-edit, multi-image-edit, text-rendering, dense-layout], best_for: "dense typography, posters, infographics; strong text rendering and texture" }
  - { id: "qwen-image-2.0",     access: "closed-weights", tier: "legacy",   caps: [text-to-image, image-edit, multi-image-edit, text-rendering], best_for: "balanced quality and speed for general generation and editing" }
  - { id: "qwen-image-max",     access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-edit, text-rendering], best_for: "highest photoreal realism, fewest AI artifacts" }
  - { id: "qwen-image-plus",    access: "closed-weights", tier: "std",      caps: [text-to-image, image-edit, multi-image-edit, text-rendering], best_for: "diverse artistic styles plus solid text rendering" }
  # open weights (Apache 2.0; run locally). The YYMM suffix IS part of the name and identifies the release:
  # 2512 is December 2025, 2511 November, 2509 September. An unsuffixed name is the original August 2025 release.
  - { id: "Qwen-Image-2512",      access: "open-weights", tier: "base",   caps: [text-to-image], best_for: "current open text-to-image foundation; the usual local starting point" }
  - { id: "Qwen-Image-Edit-2511", access: "open-weights", tier: "std",    caps: [image-edit, multi-image-edit], best_for: "current open editor; its pipeline takes several reference images in one edit" }
  - { id: "Qwen-Image-Layered",   access: "open-weights", tier: "std",    caps: [image-edit, layer-separation], best_for: "decomposes a scene into separately editable layers; a finetune of Qwen-Image" }
  - { id: "Qwen-Image",           access: "open-weights", tier: "legacy", caps: [text-to-image], best_for: "the original open release; superseded by Qwen-Image-2512" }
  - { id: "Qwen-Image-Edit-2509", access: "open-weights", tier: "legacy", caps: [image-edit, multi-image-edit], best_for: "previous open editor" }
  - { id: "Qwen-Image-Edit",      access: "open-weights", tier: "legacy", caps: [image-edit], best_for: "the first open editor; one reference image only" }
capabilities: [text-to-image, image-edit, multi-image-edit, text-rendering, dense-layout, ui-simulation, formula-rendering, layer-separation]
prompt:
  languages: ["en", "zh", "ja", "ko", "es", "mixed"]
  literal_text: "wrap the exact words in double quotes; quote each text element separately with its own style"
  length_strategy: "rewards long, detailed, multi-sentence descriptions; on the 3.0 tier write a full multi-section brief and specify every panel rather than splitting a layout across several calls"
  auto_expand_behavior: "some hosts auto-expand short prompts; write a complete detailed prompt when you need tight control"
  negatives: "SPLIT BY ACCESS. The open checkpoints expose a real negative prompt field, and the owner's reference pipeline passes an empty string by default, so reach for it only to remove a specific artifact you can see. On the hosted line, describe the artifact to exclude, and where a host exposes no negative field fold the exclusion into the positive prompt"
  quality_suffix: "OPEN WEIGHTS ONLY. The owner's reference pipeline appends ', Ultra HD, 4K, cinematic composition.' to an English prompt, and the Chinese equivalent to a Chinese one. This is the one place in this set where a 4K-style quality booster is owner-recommended rather than an anti-pattern, and it does NOT transfer to the hosted line"
  references: "for multi-image edits, name each input as Image 1, Image 2, Image 3, and so on; phrase each as 'the X from Image N' and combine several in one instruction (for example, the person in Image 1 wearing the dress from Image 2 in the pose from Image 3)"
  world_knowledge: "draws on built-in knowledge of interfaces, public figures, and domain conventions, but does not retrieve live facts; state any current or verifiable detail in the prompt text"
sources:
  official: ["https://qwen.ai/blog?id=qwen-image-3.0", "https://help.aliyun.com/en/model-studio/qwen-image-3-0-pro", "https://help.aliyun.com/en/model-studio/qwen-image-3-0", "https://qwen.ai/blog?id=qwen-image-2.0", "https://www.alibabacloud.com/help/en/model-studio/qwen-image-api", "https://www.alibabacloud.com/help/en/model-studio/qwen-image-edit-api", "https://github.com/QwenLM/Qwen-Image", "https://huggingface.co/Qwen/Qwen-Image", "https://huggingface.co/Qwen/Qwen-Image-2512", "https://huggingface.co/Qwen/Qwen-Image-Edit-2511", "https://huggingface.co/Qwen/Qwen-Image-Layered"]
  provider: ["https://fal.ai/learn/tools/how-to-use-qwen-image-2"]
  community: ["https://qwenimage-2.com/blog/qwen-image-prompting-guide", "https://wavespeed.ai/blog/posts/blog-how-to-use-qwen-image-2-0-text-to-image-editing/", "https://inference.sh/blog/guides/qwen-image-2-generation"]
last_verified: "2026-08-09"
---

# Qwen-Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- Write prompts as one continuous natural-language description, not comma-separated tags. Qwen rewards complete, detailed scenes over keyword lists.
- Put intent into the words (subject, setting, style, lighting, composition) rather than relying on numeric knobs.
- Qwen's defining strength is legible in-image text. When any words must appear in the image, follow the Text rendering rules.
- The 3.0 tier is prompted the same way as 2.0, just at greater length. Every rule here holds across both generations; the 3.0 sections add reach, they do not replace anything.
- The model knows a great deal but looks nothing up. Write current, local, or checkable facts into the prompt instead of expecting the model to supply them.

</rules>

## TL;DR

<template id="quickstart">

{subject with key attributes}, {setting or environment}, {style}, {lighting}, {camera or shot}, {quality detail}. For any words that must appear in the image, add: a {sign, title, or label} that reads "{exact text}" in {typography}.

</template>

## Models and when to use which

All variants share one prompt scheme; they differ in rendering character and in how much instruction they can absorb, not in how you write the prompt.

Generation 3.0, for layout-heavy and detail-critical work:

- `qwen-image-3.0-pro`: the most instruction a single image can absorb, plus the finest micro-detail (micro-expressions, pores, individual hair strands). Use for newspapers, storyboards, menus, exam papers, nested interfaces, and any brief long enough to specify a dozen regions.
- `qwen-image-3.0`: the same long-brief layout control at everyday cost. Use for volume work such as posters, web page mockups, and UI screens.

Generation 2.0, still the right pick for shorter, single-subject prompts:

- `qwen-image-2.0-pro`: strong text rendering and material texture, good semantic adherence. Use for dense typography, posters, charts, infographics, and presentation slides.
- `qwen-image-2.0`: balances quality and speed for everyday generation and editing.
- `qwen-image-max`: highest realism and naturalness with the fewest generation artifacts. Use for photoreal portraits and product shots.
- `qwen-image-plus`: broadest stylistic range alongside reliable text rendering. Use when exploring varied artistic looks.

A prompt written for one variant transfers to the others. Pick the variant by the look you want, then keep the prompt the same. The one asymmetry runs upward: a brief written for 3.0 can be too long for a 2.0 variant to hold, so when moving a dense layout down a generation, split it into fewer regions rather than trimming detail evenly.

## How the model reads prompts

- Natural language wins, structure helps. Qwen reads full descriptive sentences better than tag lists, but ordering the description (subject, then setting, then style, then camera and lighting) improves control.
- It rewards detail. Long, specific, multi-sentence prompts produce better results than short ones. Spend the words.
- Some hosts auto-expand a short prompt before generation. This adds variety but takes control away from you. When the output must match the prompt, write the full detailed prompt yourself so there is nothing left to expand.
- Text rendering is the headline capability. Qwen renders accurate characters, handles long multi-line instructions, lays text out deliberately, places text on realistic materials, and aligns text to grids and tables.
- It is multilingual. English, Chinese, and mixed-script prompts all work, and the 3.0 tier natively renders further scripts including Japanese, Korean, and Spanish when you name the language.
- On the 3.0 tier the instruction budget stopped being the binding constraint. A brief long enough to describe every cell of a grid, every layer of a nested interface, and the exact copy in each is read and rendered in one pass. Write the whole thing rather than generating parts and compositing.
- Two distinct strengths sit behind that. Laying several concepts side by side without letting them bleed into each other is one; nesting a scene inside a scene inside a scene, each with its own consistent style, is the other. Prompt them differently: side-by-side wants a named grid, nested wants an explicit outer-to-inner order.
- Its world knowledge is broad and prompt-addressable. Naming a recognisable interface, a public figure, a document genre, or a domain convention gets you its real conventions without describing them. This is recall, not lookup, so anything time-sensitive or specific still has to be written out.

## Prompt structure

<rules id="structure">

- Quick exploration: Subject + Setting + Style.
- Fine control: Subject + Setting + Style + Camera + Atmosphere + Detail modifiers.
- Lead with the subject and its key attributes, then the environment, then the style, then camera and lighting, then mood and quality modifiers.
- Use concrete visual vocabulary: shot size (extreme close-up, close-up, medium shot, long shot), perspective (eye level, bird's eye, low angle, aerial), lens (macro, ultra-wide, telephoto, fisheye), lighting (natural, backlight, neon, ambient).

</rules>

<template id="general">

{subject with attributes and action}, {detailed setting}, {style}, {shot size and lens}, {lighting}, {atmosphere}, {quality and detail modifiers}

</template>

<example use_case="photoreal-portrait">

```text
A 25-year-old woman with a round face looking at the camera, elegant ethnic dress, outdoors at golden hour, commercial photography, half-body close-up, cinematic lighting, delicate light makeup, sharp detail
```

*Why: subject and attributes first, then setting, style, shot, and lighting, following the advanced formula*

</example>

## By use-case

### Photorealism

<rules id="photoreal">

- Lead with camera language: lens, shot size, aperture, lighting. Name the material and texture you want rendered.
- Add realism cues sparingly (natural light, shallow depth of field, true-to-life color). Do not over-stack quality tags.
- The Pro variant resolves micro-materials, so name them: individual hair strands, fabric weave, metallic reflections, subsurface scattering on skin. Specific surfaces render more texture than generic phrasing.

</rules>

<example use_case="product-shot">

```text
A macro shot of fresh cherries beside a glass of carbonated water, professional color grading, clean sharp focus, natural light, commercial product photography, hyper-realistic detail
```

*Why: macro lens plus material and lighting cues drive photoreal texture without tag soup*

</example>

### Posters and titled graphics

<template id="poster">

A {style} poster for {subject}. Headline "{headline}" in {typography} at the {position}; subtitle "{subtitle}" in {typography} below. {color palette}, {composition}.

</template>

<example use_case="event-poster">

```text
A healing-style hand-drawn poster of three puppies playing with a ball on green grass. The title "Come Play Ball!" in bold blue cartoon font at the top; the subtitle "Show Off Your Skills" in green below. Fresh green and blue palette with pink and yellow accents, cheerful childlike mood
```

*Why: each text element is quoted separately with its own font, color, and position, so the layout resolves correctly*

</example>

### Infographics, slides, and charts

<rules id="layout-text">

- State the overall layout first (columns, rows, panels, header), then quote each text block with its position in that layout.
- Keep each rendered string short. Split long paragraphs into labeled blocks.

</rules>

<example use_case="infographic">

```text
A three-column infographic on a light background. The header reads "Quarterly Results" in bold sans-serif. The left column is titled "Revenue", the center "Users", the right "Retention", each with a short caption beneath. Clean corporate style, blue and gray palette
```

*Why: the layout is named before the text, and each label is quoted in its column slot*

</example>

<example use_case="dense-scene-with-text">

```text
A top-down photograph of a developer's desk in warm afternoon light. A laptop screen shows green code on a dark editor; a white mug reading "DEBUG" in bold black letters sits beside it with steam rising; an open notebook shows a hand-drawn three-circle Venn diagram labeled "Speed", "Cost", and "Quality"; a sticky note reads "ship friday" in blue marker; a phone screen shows a single new-message badge. Shallow depth of field, the bookshelf behind softly blurred
```

*Why: a long flagship that exercises Qwen's text rendering at scale, each in-image string quoted separately with its own surface and style, plus a labeled diagram and a clear light direction, all held together as one coherent scene rather than tag soup*

</example>

### Information-dense layouts

The 3.0 tier reads a brief, not a caption. When the output is a document rather than a picture, stop describing a scene and start specifying an artifact region by region.

<rules id="dense-layout">

- Name the artifact first (a newspaper front page, a six-cell infographic, an exam paper, a storyboard), then its structure, then each region's content. The genre name alone buys you its real conventions.
- Declare the grid before you fill it. State the arrangement (three columns, a 2x3 grid, a header over two panels) and then address each cell by its position.
- Give every region a title and its content. An unnamed cell does not stay empty; it fills with plausible filler. If a region is meant to be blank, say so.
- Keep regions independent. State that cells do not bleed into each other when subjects are visually similar, or the model blends adjacent panels.
- For nesting, order the layers explicitly from outer to inner and give each its own style and light. Nesting is a different instruction from side-by-side layout and fails if you mix the two.
- Reserve small type deliberately. Name which blocks are body copy, captions, or footnotes, and keep the exact wording only for the strings that must be readable; let the rest be described as dense small print.
- Write the whole layout in one brief. Generating panels separately and compositing loses the shared grid, palette, and light.

</rules>

<template id="brief">

A {artifact type} on {surface or background}. {Grid or structure statement}. {Region 1 position}, titled "{title}", {contents}. {Region 2 position}, titled "{title}", {contents}. {Continue per region}. {Header or footer with exact copy and typography}. {Global style, palette, and lighting}.

</template>

<example use_case="grid-infographic">

```text
A 2x3 grid infographic poster on a warm off-white background, thin gray rules between cells, one subject per cell and no bleed between them. Top left, titled "Knife Grips", three hand diagrams with callout arrows. Top center, titled "Heat Zones", a pan seen from above with three shaded rings labeled "sear", "saute", and "hold". Top right, titled "Salt Timing", a simple timeline running from "before" to "during" to "rest". Bottom left, titled "Doneness", four steak cross-sections with a temperature label under each. Bottom center, titled "Resting", a cut of meat with dashed arrows showing juices redistributing. Bottom right, titled "Common Errors", four short lines in small type. A header across the top reads "Kitchen Fundamentals" in bold slab serif; a thin footer reads "one page, six ideas" in small caps.
```

*Why: a long flagship that names the grid before filling it, gives all six cells a quoted title and its own content so none of them invent filler, forbids bleed between visually similar cells, and spends small type on the one block that can afford it*

</example>

<example use_case="nested-interface">

```text
A laptop screen photographed straight on, showing a code editor in a dark theme. Inside the editor's preview pane, a browser window is open on a design portfolio with a white header and a three-column project grid. Inside the portfolio's hero image, a printed concert poster is visible, black ink on red, reading "NIGHT SHIFT" in condensed uppercase with "FRI 14 NOV" beneath it. Each layer keeps its own authentic styling and its own light: the editor's screen glow, the browser's flat white chrome, the poster's matte ink on paper.
```

*Why: orders the layers outer to inner one per sentence and gives each its own styling and light source, so the result reads as depth rather than three images collaged together*

</example>

<example use_case="newspaper-page">

```text
A broadsheet newspaper lying flat on a wooden table, shot from directly above in soft daylight. The masthead reads "THE HARBOUR REVIEW" in blackletter across the top. Below it a five-column front page: a lead story headlined "Ferry Terminal Reopens After Two Years" with a black-and-white photograph of a dock and a short italic caption beneath; a sidebar headlined "What Changes For Commuters" set in smaller type; a boxed weather strip along the bottom edge. Body copy is dense justified small print with visible column rules. Slightly uneven paper texture, one soft fold crease across the middle.
```

*Why: names the document genre so the model supplies newsprint conventions unprompted, quotes only the strings that must be legible, and lets the body copy be described as dense small print instead of spelled out*

</example>

### Multilingual text and formulas

<rules id="multilingual">

- Name the language of every string that is not in the prompt's own language, and quote the exact target-language text including its diacritics. Asking for a translation gives up control of both wording and layout.
- For a bilingual layout, say which language leads, where each sits, and whether the two share a baseline grid so the blocks align.
- Name a typeface family (serif, condensed sans, blackletter, gothic) rather than a specific font file.
- For mathematics, describe the notation structurally: the bounds of a summation, what sits in a numerator and denominator, which symbols are Greek, and what the lines align on. Describe the layout of the expression rather than pasting raw markup.
- Keep formulas and body text in separate named blocks. A displayed equation and the paragraph around it are two regions, not one.

</rules>

<example use_case="bilingual-label">

```text
A bilingual museum wall label, cream background, a thin gray rule down the middle. The left half is English: the title "Migration Patterns" in bold serif with a three-line description beneath. The right half is Spanish, titled "Patrones de Migración" in the same serif at the same size, with its own three-line description. Both halves sit on a shared baseline grid so the two blocks align line for line. A small catalogue number "1987.42" in gray sits at the bottom right.
```

*Why: names both languages, quotes each title in its own language rather than asking for a translation, and pins the shared baseline grid so the two columns line up*

</example>

<example use_case="typeset-mathematics">

```text
A single page from a mathematics textbook, white paper and black type, shot flat. A centered chapter heading reads "3.2 Convergence Tests". Below it two typeset theorem blocks in a serif academic face, each with a bold "Theorem" label and a number in the right margin. Between them a displayed equation running three lines aligned on the equals sign, with a summation over n from 1 to infinity, a fraction carrying a squared term in the denominator, and Greek letters in the exponent. Dense justified body text fills the rest of the page, with two inline formulas and a footnote rule at the bottom.
```

*Why: describes the notation structurally (summation bounds, what sits in the denominator, alignment on the equals sign) instead of pasting markup, and separates the displayed equation from the body text as its own region*

</example>

### Artistic styles

<rules id="styles">

- Name the style explicitly as a keyword. Qwen supports a wide range, including watercolor, oil, ink painting, 3D cartoon, Pixar style, clay, ceramic, origami, and pointillism.
- Pair a style keyword with a clear subject and setting; let the style govern rendering, not the subject.

</rules>

<example use_case="watercolor">

```text
A quiet cafe exterior on a bright white background, light watercolor style, soft dreamy washes, few details, Studio Ghibli feeling
```

*Why: the style keyword leads the rendering while the subject stays simple*

</example>

## Image editing

<rules id="edit">

- State the change as an instruction against the source image: what to add, remove, replace, or restyle, and what to keep unchanged.
- Lead with an imperative verb and name its target in the same clause: "Replace the face in Image 1 with ...", "Redraw the photo in Image 1 in the style of Image 2 ...". The leading verb can be the change or the constraint; "Keep the insect from this photograph exactly as it is and build a research figure around it" opens on a pin and is still an instruction.
- Pick a verb that IS the operation. Add, Remove, Replace, Restore, Redraw and Keep each tell the model what kind of change to make. A generic "Edit" only tells it that something changes, so it spends the strongest position in the prompt saying nothing.
- Do not open by describing what each input contributes. "Image 1 provides the foundation, Image 2 provides only the face" states the plan instead of issuing it, and delays the real instruction by a sentence or two. Weld each element to its source inside the instruction instead, the way the examples below do.
- Name what must stay constant (identity, pose, background, lighting) so the edit does not drift.
- Abstract quality assertions do nothing. "With zero drift", "perfectly", "seamlessly" have no visual target; the pinning is done by the list of elements you name, not by insisting on the outcome.
- For text edits, quote the exact new text and its placement, the same as in generation.
- Keep the instruction scoped to one clear change when precision matters; describe a single transformation rather than several at once.
- Editing inherits the generation strengths. The same tier that renders dense layouts will also add an annotation layer, repair damage, or build a labeled figure around an existing photograph, so specify those the way you would specify a layout: element by element, each with its position.
- When adding a layer over an existing image, pin the underlying image explicitly (printed text, paper texture, lighting) so the addition reads as applied on top rather than as a re-render of the whole frame.
- For repair work, name the damage you want gone and forbid invention. Restoration prompts fail by inventing new subject matter, not by under-repairing.

</rules>

<example use_case="add-text-to-photo">

```text
Add the text "OPEN" in bold red neon to the shop window in the upper left, keep the rest of the photo unchanged
```

*Why: names the new text, its style, and its location, and pins everything else as constant*

</example>

<example use_case="restyle">

```text
Restyle this portrait as an oil painting with visible brushstrokes, keep the subject's face, pose, and composition identical
```

*Why: states the target style and the invariants, so identity survives the restyle*

</example>

<example use_case="annotation-overlay">

```text
Add handwritten red pen annotations to this book page: underline the second sentence of the first paragraph, circle the word "entropy" where it appears, draw a curved arrow from that circle out to the right margin, and write "compare ch. 4" in the margin in the same hand. Keep the printed text, paper texture, and lighting unchanged.
```

*Why: names each mark, what it targets, and where it goes, then pins the underlying page so the result reads as ink added on top rather than a re-rendered page*

</example>

<example use_case="damage-restoration">

```text
Restore the damaged areas of this ink painting: fill the missing section in the lower left and remove the mold spotting across the upper half, matching the original brushwork, ink gradients, and paper tone. Do not add any new subject matter, and leave the existing composition, seals, and inscription untouched.
```

*Why: scopes the repair to named damage, ties the fill to the original technique, and forbids invention, which is the way restoration prompts usually fail*

</example>

<example use_case="photo-to-figure">

```text
Keep the insect from this photograph exactly as it is and build a research figure around it: add a thin leader line from each of four anatomical features to a small label beside it, a magnified inset of the wing venation in the top right corner with a hairline border, a scale bar with its measurement beneath the specimen, and a caption strip along the bottom reading "Fig. 3. Dorsal view." Keep the background clean and neutral.
```

*Why: pins the photographic subject first, then specifies every added element and its position, so the annotation layer is built around the original instead of replacing it*

</example>

### Multiple reference images

Qwen-Image editing can take more than one reference image in a single request, which is how you transfer or combine elements across photos: a garment, a face, a product, a background, or a style.

<rules id="multi-image">

- Name each input by its position (Image 1, Image 2, Image 3, in upload order) and refer to it exactly that way. The base subject you are editing is usually Image 1.
- Weld every borrowed element to its source. With three or more inputs an unattached phrase like "the dress" is ambiguous, so always write "the dress from Image 2", "the pose from Image 3". Read the finished instruction as an assignment list: one role per input.
- Name what moves, pin what stays. The model carries only what you name, so state each element you are changing and explicitly hold the rest constant ("keeping her face, hairstyle, and pose unchanged"); skipping the invariants lets a transfer drift the face or pose.
- Anything you do not name is ignored, so be explicit about every element you want carried over. The same pattern places a graphic such as a logo onto a named surface.

</rules>

<example use_case="clothing-and-accessory-transfer">

```text
The woman in Image 1 wears the red trench coat from Image 2 and carries the tan leather bag from Image 3, keeping her face, hairstyle, and pose unchanged
```

*Why: pulls two separate wardrobe elements from two different images onto the base subject in Image 1, names each source, and pins identity so only the named items transfer*

</example>

<example use_case="object-in-hand-and-pose">

```text
The woman in Image 1 holds the bouquet from Image 2 in her hands and takes the standing pose of the person in Image 3, keeping her face, hairstyle, and outfit unchanged
```

*Why: combines placing an object from Image 2 into the subject's hands with adopting a pose from Image 3, while pinning the subject's identity and clothing so only those two things change*

</example>

<example use_case="base-plus-background-plus-product">

```text
Keep the model from Image 1, place them against the studio background from Image 2, and add the wristwatch from Image 3 on their left wrist, matching lighting and perspective across all three
```

*Why: edits one base subject by swapping in a background from a second image and adding a product from a third, naming each source and the lighting match so the composite holds together*

</example>

<example use_case="two-person-composite">

```text
Combine the man from Image 1 and the woman from Image 2 into one natural photo standing side by side, using the garden background from Image 3, shot on a 50mm lens with matched lighting on both
```

*Why: merges two subjects from separate images and drops them into a background drawn from a third, with framing and lighting cues so it reads as a single photograph*

</example>

<example use_case="background-and-outfit-swap">

```text
Keep the person from Image 1, place them in the city street at dusk from Image 2, and change their jacket to the one from Image 3, relighting the subject to match the new scene
```

*Why: combines a background replacement from one image with a garment swap from another on the same base subject, with relighting so the edges blend*

</example>

<example use_case="style-transfer">

```text
Redraw the photo in Image 1 in the watercolor painting style of Image 2, keeping Image 1's composition, subjects, and layout unchanged
```

*Why: a pure style transfer, the look is taken only from Image 2 while the content and composition stay locked to Image 1*

</example>

<example use_case="style-transfer-plus-added-element">

```text
Redraw the scene from Image 1 in the brushstroke style of Image 2, and add the sailboat from Image 3 into the water rendered in that same style, keeping Image 1's composition
```

*Why: applies a style from one image to content from another while folding in an object from a third, unifying all of it in the target style*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Describe specific artifacts to exclude rather than generic terms. "blurry text, warped letters, extra fingers" beats "bad quality".
- Reach for exclusions only when a specific artifact keeps appearing. A detailed positive prompt usually produces clean results on its own, and over-constraining reduces variety.
- Where a host exposes no separate negative field, fold the exclusion into the positive prompt by describing the desired opposite, for example "clean sharp text" instead of listing "no blurry text".

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Tag soup: a list of disconnected keywords. Rewrite as one descriptive scene.
- Unquoted text: any words meant to appear in the image must be in double quotes, or they get read as scene description.
- Overlong single strings: long rendered text degrades. Split it into shorter labeled blocks with explicit positions.
- Over-stacked quality tags: piling on "8K, ultra HD, masterpiece, best quality" adds little. Spend words on subject, material, and light.
- Relying on auto-expansion for exact output: if the result must match the prompt, write the full prompt rather than a short one a host will expand.
- Expecting a lookup: the model recalls world knowledge, it does not retrieve it. Any date, price, score, or current event you need rendered has to be written into the prompt.
- Compositing a layout the model would render whole: on the 3.0 tier, generating panels separately and stitching them loses the shared grid, palette, and light. Describe the full layout in one brief.
- Leaving a region unnamed: an unspecified cell, panel, or margin fills with plausible filler rather than staying empty. Give every region content or declare it blank.
- Treating nesting as adjacency: layers inside layers need an explicit outer-to-inner order. Listing them side by side produces a collage instead of depth.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict; community entries are illustrative.

- Official (Alibaba, Qwen): [Qwen-Image-3.0 blog](https://qwen.ai/blog?id=qwen-image-3.0), [Model Studio qwen-image-3.0-pro model reference](https://help.aliyun.com/en/model-studio/qwen-image-3-0-pro), [Model Studio qwen-image-3.0 model reference](https://help.aliyun.com/en/model-studio/qwen-image-3-0), [Qwen-Image-2.0 blog](https://qwen.ai/blog?id=qwen-image-2.0), [Model Studio Qwen-Image API reference](https://www.alibabacloud.com/help/en/model-studio/qwen-image-api), [Model Studio Qwen image-edit API reference](https://www.alibabacloud.com/help/en/model-studio/qwen-image-edit-api).
- Official (open weights): [Qwen-Image on GitHub](https://github.com/QwenLM/Qwen-Image), [Qwen-Image](https://huggingface.co/Qwen/Qwen-Image), [Qwen-Image-2512](https://huggingface.co/Qwen/Qwen-Image-2512), [Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511), [Qwen-Image-Layered](https://huggingface.co/Qwen/Qwen-Image-Layered)
- Provider: [fal.ai how-to for Qwen Image 2](https://fal.ai/learn/tools/how-to-use-qwen-image-2).
- Community (illustrative only): [qwenimage-2.com prompting guide](https://qwenimage-2.com/blog/qwen-image-prompting-guide), [wavespeed.ai usage guide](https://wavespeed.ai/blog/posts/blog-how-to-use-qwen-image-2-0-text-to-image-editing/), [inference.sh generation guide](https://inference.sh/blog/guides/qwen-image-2-generation).

Coverage note: Qwen-Image-3.0 shipped without weights, a model card, or a prompt guide, and its launch blog contains no example prompts. The 3.0 craft here is derived from the owner's worked examples and the two Model Studio model references; neither approved provider had published 3.0 prompt guidance at the time of writing. The owner's own surfaces conflict on live knowledge retrieval, resolved on the API reference; see `sources/qwen-image-3.0/qwen-image-3.0-notation-resolution.md`.

Last verified: 2026-08-09.
