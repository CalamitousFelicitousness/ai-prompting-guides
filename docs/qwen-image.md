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
  # open weights (run locally). Qwen-Image and its YYMM releases are Apache 2.0; Qwen-Image-2.1 ships under the
  # Qwen Research License. The YYMM suffix IS part of the name and identifies the release: 2512 is December 2025,
  # 2511 November, 2509 September. An unsuffixed name is the original August 2025 release. Qwen-Image-2.1 leaves
  # that scheme for a version number and is NOT a YYMM release; it is the September 2026 unified model.
  - { id: "Qwen-Image-2.1",       access: "open-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-edit, text-rendering, transparency], best_for: "current open model, and the only one that generates and edits in a single checkpoint; native transparent (RGBA) output, several reference images in one edit, and region marks drawn on the input image. Ships with its own prompt-rewriting models, whose published spec is the owner's clearest statement of what a good Qwen prompt looks like" }
  - { id: "Qwen-Image-2512",      access: "open-weights", tier: "base",   caps: [text-to-image], best_for: "the previous open text-to-image foundation; text-to-image only, and still the reference point for the Qwen 1328 resolution set" }
  - { id: "Qwen-Image-Edit-2511", access: "open-weights", tier: "std",    caps: [image-edit, multi-image-edit], best_for: "current open editor; its pipeline takes several reference images in one edit" }
  - { id: "Qwen-Image-Layered",   access: "open-weights", tier: "std",    caps: [image-edit, layer-separation], best_for: "decomposes a scene into separately editable layers; a finetune of Qwen-Image" }
  - { id: "Qwen-Image",           access: "open-weights", tier: "legacy", caps: [text-to-image], best_for: "the original open release; superseded by Qwen-Image-2512" }
  - { id: "Qwen-Image-Edit-2509", access: "open-weights", tier: "legacy", caps: [image-edit, multi-image-edit], best_for: "previous open editor" }
  - { id: "Qwen-Image-Edit",      access: "open-weights", tier: "legacy", caps: [image-edit], best_for: "the first open editor; one reference image only" }
capabilities: [text-to-image, image-edit, multi-image-edit, text-rendering, dense-layout, ui-simulation, formula-rendering, layer-separation, transparency]
prompt:
  languages: ["en", "zh", "ja", "ko", "es", "mixed"]
  literal_text: "wrap the exact words in double quotes; quote each text element separately with its own style"
  length_strategy: "rewards long, detailed, multi-sentence descriptions; on the 3.0 tier write a full multi-section brief and specify every panel rather than splitting a layout across several calls"
  auto_expand_behavior: "some hosts auto-expand short prompts; write a complete detailed prompt when you need tight control. For 2.1 the owner ships the expander itself, as two prompt-rewriting models (PE-T2I for generation, PE-I2I for editing) that turn a brief into the long form the model wants. Running them is optional; writing what they would have written is not"
  transparency: "QWEN-IMAGE-2.1 ONLY. Transparency is chosen by the prompt, not by a setting. The owner's recommended form opens 'This is an RGBA image with transparency.' and closes 'The image has alpha channel and the background is transparent.', with the description in between"
  negatives: "SPLIT BY ACCESS. The open checkpoints expose a real negative prompt field, and the owner's reference pipeline passes an empty string by default, so reach for it only to remove a specific artifact you can see. On the hosted line, describe the artifact to exclude, and where a host exposes no negative field fold the exclusion into the positive prompt"
  quality_suffix: "THE PRE-2.1 OPEN CHECKPOINTS ONLY. Their reference pipeline appends ', Ultra HD, 4K, cinematic composition.' to an English prompt, and the Chinese equivalent to a Chinese one. It does NOT transfer to the hosted line, and it is reversed on 2.1, whose own rewriter bans boosters outright and treats 2K, 4K and 8K as words that never belong in the prompt"
  references: "SPLITS BY MODEL. On the dedicated editors (Edit, Edit-2509, Edit-2511) name each input as Image 1, Image 2, Image 3 and phrase each as 'the X from Image N'. On 2.1 the owner's form is the angle-bracket tag <image1>, <image2>, mandatory once there are two or more inputs and left off entirely for a single one, where the image is referred to in plain words. Never mix the two"
  aspect_ratio: "KEEP IT OUT OF THE PROMPT ON 2.1. Both of the owner's rewriters forbid a ratio, a resolution or a pixel count anywhere in the prompt text and carry it in a separate field instead, which also covers the words 2K, 4K and 8K"
  world_knowledge: "draws on built-in knowledge of interfaces, public figures, and domain conventions, but does not retrieve live facts; state any current or verifiable detail in the prompt text"
sources:
  official: ["https://qwen.ai/blog?id=qwen-image-2.1", "https://huggingface.co/Qwen/Qwen-Image-2.1", "https://github.com/QwenLM/Qwen-Image-2.1", "https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I", "https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I", "https://qwen.ai/blog?id=qwen-image-3.0", "https://help.aliyun.com/en/model-studio/qwen-image-3-0-pro", "https://help.aliyun.com/en/model-studio/qwen-image-3-0", "https://qwen.ai/blog?id=qwen-image-2.0", "https://www.alibabacloud.com/help/en/model-studio/qwen-image-api", "https://www.alibabacloud.com/help/en/model-studio/qwen-image-edit-api", "https://github.com/QwenLM/Qwen-Image", "https://huggingface.co/Qwen/Qwen-Image", "https://huggingface.co/Qwen/Qwen-Image-2512", "https://huggingface.co/Qwen/Qwen-Image-Edit-2511", "https://huggingface.co/Qwen/Qwen-Image-Layered"]
  provider: ["https://fal.ai/learn/tools/how-to-use-qwen-image-2"]
  community: ["https://qwenimage-2.com/blog/qwen-image-prompting-guide", "https://wavespeed.ai/blog/posts/blog-how-to-use-qwen-image-2-0-text-to-image-editing/", "https://inference.sh/blog/guides/qwen-image-2-generation"]
last_verified: "2026-09-21"
---

# Qwen-Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- Write prompts as one continuous natural-language description, not comma-separated tags. Qwen rewards complete, detailed scenes over keyword lists.
- Put intent into the words (subject, setting, style, lighting, composition) rather than relying on numeric knobs.
- Qwen's defining strength is legible in-image text. When any words must appear in the image, follow the Text rendering rules.
- The 3.0 tier is prompted the same way as 2.0, just at greater length. Every rule here holds across both generations; the 3.0 sections add reach, they do not replace anything.
- Qwen-Image-2.1 is the open line's current model and the one place in this family where rules are REVERSED rather than extended. Quality boosters are out, the aspect ratio leaves the prompt, and multi-image edits use a different token form. Each section below says where 2.1 differs; obey those notes over the general rule.
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

Open weights, to run locally:

- `Qwen-Image-2.1` is the current one and does generation and editing in a single checkpoint, so there is no longer a separate editor to load. It adds transparent (RGBA) output chosen by the prompt, several reference images in one edit, and region marks drawn onto the input image. It also ships with the owner's own prompt-rewriting models, which is where most of the craft below comes from.
- `Qwen-Image-2512` and `Qwen-Image-Edit-2511` are the previous generation-and-editor pair, and `Qwen-Image-Layered` separates a scene into editable layers. The older `Qwen-Image`, `Qwen-Image-Edit` and `Qwen-Image-Edit-2509` releases are superseded.
- Licensing differs inside the open line: the earlier releases are Apache 2.0 and 2.1 is under the Qwen Research License. That is a distribution question rather than a prompting one, but it is the sort of thing that decides which checkpoint a project can use.

A prompt written for one variant transfers to the others, with 2.1's reversals as the exception. Pick the variant by the look you want, then keep the prompt the same. The one asymmetry runs upward: a brief written for 3.0 can be too long for a 2.0 variant to hold, so when moving a dense layout down a generation, split it into fewer regions rather than trimming detail evenly.

## How the model reads prompts

- Natural language wins, structure helps. Qwen reads full descriptive sentences better than tag lists, but ordering the description (subject, then setting, then style, then camera and lighting) improves control.
- It rewards detail. Long, specific, multi-sentence prompts produce better results than short ones. Spend the words.
- Some hosts auto-expand a short prompt before generation. This adds variety but takes control away from you. When the output must match the prompt, write the full detailed prompt yourself so there is nothing left to expand.
- On 2.1 the owner published the expander, and with it the answer to what it expands INTO. Two rewriting models ship beside the checkpoint, one for generation and one for editing, each with its instructions in the open. A brief becomes roughly twenty sentences and four to five hundred words of description, whatever its starting length: a three-word request and a three-hundred-word request both arrive at the same size, so a thin brief buys an invented frame rather than a shorter prompt. Write that yourself, or run the rewriter; either way, that is the shape the model was tuned on.
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

### The observer form, on Qwen-Image-2.1

The owner's generation rewriter publishes its own instructions, so for 2.1 there is a documented answer to what a good prompt looks like: one long paragraph describing the finished image as though you were looking at it. It is a different register from the formula above, not a longer version of it, and it is what the model was tuned on.

<rules id="observer-2.1">

- Describe, do not instruct. Present tense, third person, declarative, written by an observer reporting what is in the frame. No "you", no "create", no "make sure", nothing addressed to the model.
- An instruction about the job is not content. "Use double quotes", "4K, no noise", "make the text sharp" are obeyed silently and never appear in the description.
- Write about twenty sentences and four to five hundred words, at roughly twenty-five words a sentence. A dense frame runs longer and a single quiet subject shorter, but a thin brief never buys a thin description.
- Open with one sentence of about twenty words naming the medium, the style, the subject and the background or palette, usually the orientation too. The medium noun (photograph, poster, illustration, infographic, card, logo) is the one part never left out, and the style word is named here once.
- Put the background and the surface it sits on immediately after that opening, not at the end.
- Then walk the frame in a fixed order. A divided frame (poster, page, interface, wide scene) goes top band, then left, centre and right with a sentence or two each, then bottom band. A single subject goes background falloff, pose and placement, head and face, body and each garment, what is held, then whatever is left at the edges.
- Reach the whole frame with eight to fourteen positional phrases, and open about a third of the sentences on the position itself ("In the upper-left corner, ...", "Across the lower third, ..."). Phrases that all cluster in the middle leave the corners to chance.
- Keep it to one paragraph. Break only when the image is genuinely stacked regions (panels, cards, slides), and then write one paragraph per region, each opening on where that region sits.
- Set each text string after its surroundings are placed: where it sits, what it looks like, and what it says, in straight double quotes and its own script, with weight, colour, case and relative size. Write a line break as a second line rather than a newline inside the string.
- Anything not meant to be read is called blurred, indistinct or too small to read. Never invent letters for it. A chart's axes, tick labels, legend entries and cell values ARE text and get written out.
- Skip the text step entirely when nothing in the image is meant to be read. Inventing signage for an image that has none is a failure, not a bonus.
- Give the lighting its own sentence: the source, its direction, its quality, and the shadows and highlights it leaves.
- Close with exactly one sentence that steps back ("The overall composition is ..."), covering balance, palette, style and mood. One only, never a second summary.
- Hedge what an observer could not be sure of. "Appears to be", "likely", "suggesting", or an honest pair ("a notebook or a tablet"). Be flatly definite only about what the brief fixed.
- Give colours a modifier, almost never bare: deep navy, muted olive, pale cream, off-white, blue-grey. Give the material, not just the noun: brushed metal, coarse linen, weathered wood, frosted glass.
- Enumerate, never summarise. "Several items" and "various decorations" describe nothing. Write small counts as words, and when something is partly hidden say so and describe the visible part.
- Describe people by their observable surface: build, posture, where they are looking, expression, hair, skin tone, and each garment with its colour and material. Age is a life stage or a decade, never a number of years. A face turned away or cropped is stated as such rather than described.
- Name objects by class, not by brand, unless the brief named one. Photographic and design vocabulary (shallow depth of field, bokeh, backlit, negative space, drop shadow) is welcome.
- Keep the frame physically coherent: shadows fall away from the light, reflections match what faces the surface, and neighbouring objects stay in scale. An impossible request is described as the image shows it, with everything around it still coherent.
- No quality boosters on 2.1. Masterpiece, 8K, highly detailed and award-winning are out, and so are ratio, resolution and pixel counts, which belong to the request rather than the description.
- The description is English whatever language the brief arrived in; only the text shown inside the image keeps its own script. Editing reverses part of this, so see "Image editing".

</rules>

<template id="observer-2.1">

The image is a {orientation} {style} {medium noun} of {subject}, {background and palette}. {The background and the surface it sits on}. {Top band, or the subject's pose and placement}. {Left, centre and right of the frame, one or two sentences each}. {Lower edge}. {Each text string: where it sits, how it is set, and "the exact words"}. The lighting is {source, direction, quality, and the shadows it leaves}. The overall composition {balance, palette, style, mood}.

</template>

<example use_case="observer-paragraph-21">

```text
The image is a wide realistic photograph of a small neighbourhood bicycle repair shop seen from the pavement, set against a muted brick and slate palette. The background is a terrace of weathered red brick with pale chalky mortar, a rolled steel shutter half raised on the right. In the upper-left of the frame a hand-painted wooden sign in deep navy reads "HALF-LINK CYCLES" in worn cream capitals, with a second line beneath in smaller letters reading "repairs while you wait". Across the top edge a string of small pennants in faded orange and teal sags between two hooks. In the centre of the frame a man in his forties crouches beside an upturned touring bike, back slightly rounded, gaze fixed on the rear derailleur. He wears a charcoal canvas apron over a heather-grey shirt with the sleeves pushed past the elbow, and his hands, dark with grease, hold a small hex key that appears to be steel. To his left a steel workstand carries a second frame in matte olive, its paint chipped along the down tube. Along the lower edge three chainrings, a coiled inner tube and a chipped enamel mug sit on a flattened strip of cardboard. On the far right, tucked into the corner, a child's bike in pale pink leans against the shutter with its stabilisers still attached. Beside the doorway a small chalkboard lists four prices in uneven white handwriting, the top line reading "puncture 8", the rest too small to read. A tabby cat, or possibly a young fox, sits half in shadow at the foot of the doorway, only its outline visible. The lighting is soft overcast daylight from the left, leaving weak shadows under the workstand and a dull sheen along the bike's top tube. The overall composition is asymmetric and calm, built from muted earth tones with two saturated accents, quiet and documentary in mood.
```

*Why: the register the 2.1 rewriter produces. It opens on medium, style, subject and palette, takes the background next, then walks upper-left, top edge, centre, left, lower edge, far right and doorway with a dozen positional phrases; the legible strings are quoted and the illegible ones are called too small to read; the ambiguous shape is hedged as a pair; and it ends on one stepping-back sentence with no boosters anywhere*

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

### Transparent assets

Qwen-Image-2.1 only, and the one capability here that the prompt switches on by itself: the same checkpoint returns either an ordinary image or one with an alpha channel, decided by the words. The dedicated `Qwen-Image-Layered` still separates an existing scene into layers; 2.1 makes the transparent asset in the first place.

<rules id="transparency">

- Use the owner's sandwich. Open with "This is an RGBA image with transparency.", describe the subject in between, and close with "The image has alpha channel and the background is transparent." Both ends carry weight; the phrasing is the owner's recommended form.
- Describe the subject as a cutout asset, not as a scene. There is no environment to place it in, so the words that would have set a background go to the subject's own edges, outline and interior instead.
- Do not describe a checkerboard, a white background or a "removed" background. Transparency is stated, not drawn, and describing a backdrop is how you end up with one painted in.
- Several elements can share one transparent image. Arrange them by position as usual, and keep the space between them part of the transparency rather than filling it.
- An edit keeps the alpha. Editing a transparent image (changing an expression, swapping the text inside it) preserves the transparent background without being asked, so pin the alpha only if something in the instruction might imply a new backdrop.
- To get a cutout from an ordinary photograph, ask for the subject as an RGBA layer with the background transparent. This is extraction, so name what to keep rather than describing it afresh.

</rules>

<template id="transparency">

This is an RGBA image with transparency. {subject as a cutout, with its outline, materials and interior detail}. The image has alpha channel and the background is transparent.

</template>

<example use_case="transparent-asset">

```text
This is an RGBA image with transparency. A cartoon dragon sticker in a flat illustration style, curled around itself with its tail wrapping to the front, scales in two tones of jade green with a pale cream belly, small amber eyes and a thin white outline running around the whole silhouette. The image has alpha channel and the background is transparent.
```

*Why: the owner's opening and closing sentences with the asset between them, described by its silhouette, palette and edge treatment, and with no backdrop mentioned anywhere*

</example>

<example use_case="transparent-extraction">

```text
This is an RGBA image with transparency. Extract the ceramic vase and the dried stems in it from this photograph as a single cutout, keeping the glaze texture, the chipped rim and the exact arrangement of the stems, with a clean edge and no shadow carried over from the table. The image has alpha channel and the background is transparent.
```

*Why: extraction rather than generation, so it names what survives the cut and explicitly leaves the original surface's shadow behind, which is the part that otherwise comes along as a grey smear*

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

The editing rewriter that ships with 2.1 publishes its instructions too, and they are the sharpest statement of edit craft the family has. They hold for the older editors as well; only the token form and the language rule below are version-specific.

<rules id="edit-2.1">

- Decide first which kind of job it is, because they want opposite amounts of writing. Changing THIS picture (a local object or attribute, a text or interface edit, a restyle, a canvas transform) wants clarifying and constraining: say exactly what changes and let everything else stand. Making a NEW picture of this subject (placing it in a new scene, compositing across images, building a shoot or a poster from a reference) wants constructing: design the scene, the lighting and the layout to a finished standard.
- Edit exactly the attributes you named, push each to an unmistakable degree, and hold everything else at the input. The two failure modes are symmetric: LEAKAGE, where a sharpen also re-grades colour or an outfit swap quietly drops an accessory, and UNDER-EDITING, where the result could be mistaken for the untouched input.
- Preservation locks content, never edit strength. Recognisability is bought by naming what stays fixed, not by asking for the change more faintly.
- Say what stays without repainting it. Name untargeted content by type, position and role, and prefer one blanket preservation clause to walking the frame. A preservation description reads to the model as a generation instruction, so the more concretely you describe something you meant to keep, the more likely it drifts. Spend concrete description only on what is changing, or on telling two similar objects apart.
- Identity is the hardest invariant. A person's face and the accessories that make them recognisable, a product's exact design, markings and count, and the input's medium (photograph, anime, illustration, sketch, 3D render, painting) all survive every edit unless you target them.
- When identity comes from a reference image, POINT at the image instead of describing the features. Verbal description makes the model regenerate the face, and a regenerated face is a degraded likeness.
- Do only what was asked. Do not add operations, and do not tidy defects, overlays or clutter you were not asked about, however prominent they look.
- When an edit removes, moves or reveals something, say enough about the newly exposed area for the result to hold together physically.
- Commit to text exactly. Any readable string in the output is quoted in full, never summarised or abbreviated; a string you cannot commit to should not be added at all. Match the typography and language the input already establishes unless you are changing them.
- Name outpainting as outpainting when the canvas grows outward, rather than describing a wider scene and hoping.
- State requirements affirmatively: "keep the background exactly as in the input" rather than "do not change the background". The ordinary "keep X unchanged" form is affirmative enough.
- Do not hedge in an edit. The observer paragraph hedges; an instruction commits. Resolve alternatives and vague degrees before you write, and state your reading as a decision.
- Keep ratio, resolution and 2K / 4K / 8K words out of the instruction on 2.1, exactly as in generation.

</rules>

<rules id="edit-language-2.1">

- Two language decisions run in parallel on an edit, and conflating them is the usual mistake.
- The prose of the instruction, everything outside the quotes, follows the language you write in: Chinese instruction, Chinese prose; English instruction, English prose; any other language, English prose.
- The text rendered INTO the image, everything inside the quotes, follows its own order of precedence: the exact words or the target language you name; failing that, the dominant language of text already in the image; failing that, the language of your instruction.
- So an English instruction that asks for a new title on a mostly Thai sign gets Thai in the quotes and English around them.
- Keep each rendered string monolingual. No mixed scripts inside one string, no bilingual pairs, no parenthetical translations, unless you asked for them. Units and proper nouns may stay Latin.
- A genre never overrides the language. A spec-sheet, technical or storyboard look is achieved with layout and typography; the labels stay in the language the image and the instruction settled on.

</rules>

### Marking the region on the image

Qwen-Image-2.1 only. Where an instruction alone cannot say which part of a picture you mean, 2.1 takes the answer drawn onto the image: circles, painted areas, or a separate mask.

<rules id="region-marks">

- Draw the mark, then refer to it in words. The mark says where; the instruction still says what to do.
- Circles in different colours address several regions in one pass. Name the colour in each clause, and give each region its own change.
- A painted area works the same way: name the colour of the paint and say what should occupy that area.
- Circles and paint cover the pixels underneath them. When what is under the mark has to survive, pass the original image and a separate mask as two inputs instead, and say which is which.
- A mask is a location, not a description. Say what goes in the masked area and how it should meet the surrounding image.
- Sequential edits hold the rest of the frame still, so a series of marked edits on the same base can be assembled into frames of an animation.

</rules>

<example use_case="circle-marked-multi-region">

```text
Remove the metal watch in the blue circle, change the hair in the red circle to black, and replace the area in the green circle with gray short-sleeved linen pajamas.
```

*Why: the owner's own marked-region prompt. Three regions in one instruction, each addressed by the colour of its circle and given exactly one operation, with no preservation clause needed because the marks scope the edits*

</example>

<example use_case="mask-as-second-input">

```text
Using the second image as the mask, paint a cowboy on horseback into the masked area of the first image, matching its dusk light and the dust haze along the horizon, and keep everything outside the mask exactly as it is.
```

*Why: the two-input form, for when a drawn circle would have covered detail that matters. The mask carries the where, the instruction carries the what, and the lighting match is stated so the addition sits in the scene rather than on top of it*

</example>

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

- Name each input by its position, in upload order, and refer to it exactly that way. The base subject you are editing is usually the first one.
- THE TOKEN FORM SPLITS BY MODEL. The dedicated editors (Edit, Edit-2509, Edit-2511) use `Image 1`, `Image 2`, `Image 3`. Qwen-Image-2.1 uses `<image1>`, `<image2>`, and its owner calls the tags mandatory once two or more images are attached, ruling out "the first image", "image A" and their Chinese equivalents. With a single input, 2.1 takes no tag at all and wants the image referred to in plain words. Never mix the two conventions in one prompt.
- On 2.1, give every image its role in the sentence: which one is the canvas whose composition and untargeted content survive, which ones supply material, and what is taken from each. A composite inherits the canvas image's framing, so which image is the canvas decides the shape of the result.
- Describe each image individually. Never compress several into a range or a group ("the three portraits") to save writing them out, because each one needs its own role.
- Some jobs have no canvas at all. In a group portrait built from separate headshots, every input is an identity source and the composition is yours to specify; the owner's own example prompt for that case is a plain sentence about what the characters are doing together.
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

<example use_case="tagged-composite-21">

```text
Place the woman from <image1> onto the velvet bench on the left of the hotel lobby in <image2>, wearing the emerald wool coat from <image3>. <image2> is the canvas: keep its composition, framing and lighting direction, and leave everything outside the bench exactly as it is. Keep her face and hair as they are in <image1>, and take only the coat from <image3>, matching its collar shape and the sheen of the fabric.
```

*Why: the 2.1 tag form, with one role per image and the canvas named outright so the result inherits that image's framing. Identity is pinned by pointing at the image rather than describing her face, which is what keeps the likeness, and the borrowed garment is scoped to the two properties that have to survive*

</example>

<example use_case="untagged-same-role-21">

```text
These three characters are sitting around a campfire in a forest
```

*Why: the owner's own quick-start prompt for several references, and the one case where the tags come off: every input holds the same role, one character each, and nothing needs telling apart. The moment the images take different jobs, the owner's rewriting spec makes the `<image1>` tags mandatory*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Describe specific artifacts to exclude rather than generic terms. "blurry text, warped letters, extra fingers" beats "bad quality".
- Reach for exclusions only when a specific artifact keeps appearing. A detailed positive prompt usually produces clean results on its own, and over-constraining reduces variety.
- Where a host exposes no separate negative field, fold the exclusion into the positive prompt by describing the desired opposite, for example "clean sharp text" instead of listing "no blurry text".
- On 2.1 the owner's rewriters phrase everything affirmatively, including preservation: "keep the background exactly as in the input" rather than "do not change the background". Where you need an exclusion in the prompt text, write it as the state you want instead.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Tag soup: a list of disconnected keywords. Rewrite as one descriptive scene.
- Unquoted text: any words meant to appear in the image must be in double quotes, or they get read as scene description.
- Overlong single strings: long rendered text degrades. Split it into shorter labeled blocks with explicit positions.
- Over-stacked quality tags: piling on "8K, ultra HD, masterpiece, best quality" adds little. Spend words on subject, material, and light. On 2.1 this hardens into a ban: the owner's rewriter forbids boosters outright, and the quality suffix the pre-2.1 reference pipeline appended does not belong there.
- Writing the frame into a 2.1 prompt: a ratio, a resolution or a "4K" belongs to the request, not the description. Both of the owner's rewriters strip them out.
- Mixing the two reference conventions: `Image 1` belongs to the dedicated editors, `<image1>` to 2.1, and a single image on 2.1 takes no tag at all.
- Describing a face you meant to keep: on an edit, pointing at the reference image preserves a likeness and describing it regenerates one. The same holds for any identity you are carrying across.
- Describing what stays in detail: a concrete description of untargeted content reads as an instruction to generate it, so name it by type and position and leave the appearance alone.
- Asking for an edit faintly to protect the rest of the image: preservation is bought by naming what stays, not by weakening the change, and a change that lands faintly is the second way an edit fails.
- Painting a transparent background: on 2.1, say the image has an alpha channel and a transparent background. Describing a checkerboard or a white backdrop gets you one, rendered.
- Instructing the model inside an observer paragraph: "make sure the text is sharp" and "use double quotes" are notes about the job. Apply them silently; the description says only what is in the frame.
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
- Official (open weights), Qwen-Image-2.1: [Qwen-Image-2.1 blog](https://qwen.ai/blog?id=qwen-image-2.1), [Qwen-Image-2.1 model card](https://huggingface.co/Qwen/Qwen-Image-2.1), [Qwen-Image-2.1 on GitHub](https://github.com/QwenLM/Qwen-Image-2.1), [Qwen-Image-2.1-PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I), [Qwen-Image-2.1-PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I). The two PE repositories ship a `system_prompt.txt` carrying the owner's full rewriting spec; the observer form, the edit rules and the language rules here are read from those two files.
- Provider: [fal.ai how-to for Qwen Image 2](https://fal.ai/learn/tools/how-to-use-qwen-image-2).
- Community (illustrative only): [qwenimage-2.com prompting guide](https://qwenimage-2.com/blog/qwen-image-prompting-guide), [wavespeed.ai usage guide](https://wavespeed.ai/blog/posts/blog-how-to-use-qwen-image-2-0-text-to-image-editing/), [inference.sh generation guide](https://inference.sh/blog/guides/qwen-image-2-generation).

Coverage note: Qwen-Image-2.1's craft comes from the system prompts of the two rewriting models rather than from the model card, which carries a quick start and little else. Those files are owner-written instructions to an owner-trained rewriter, which puts them above any sample prompt, and they overturn two things the rest of this guide teaches: the appended quality suffix, which they forbid, and writing the aspect ratio into the prompt, which they move to a separate field. Both reversals are scoped to 2.1 here. One owner-versus-owner conflict is left standing: the 2.1 repository's multi-reference quick start passes three images with an untagged sentence, while the editing rewriter calls `<image1>` tags mandatory for two or more inputs. The guide follows the rewriter and records the untagged form as the same-role case the quick start demonstrates. The resolution table and the step count live in `guides/model-specs.md`; the cap on how many reference images one request takes is provider surface and is deliberately absent. See also `sources/qwen-image/qwen-image-2.1-notation-resolution.md`. Qwen-Image-3.0 shipped without weights, a model card, or a prompt guide, and its launch blog contains no example prompts. The 3.0 craft here is derived from the owner's worked examples and the two Model Studio model references; neither approved provider had published 3.0 prompt guidance at the time of writing. The owner's own surfaces conflict on live knowledge retrieval, resolved on the API reference; see `sources/qwen-image-3.0/qwen-image-3.0-notation-resolution.md`.

Last verified: 2026-09-21.
