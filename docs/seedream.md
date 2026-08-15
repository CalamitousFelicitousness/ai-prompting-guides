---
guide: "Seedream (image)"
prompt_scheme: "seedream"
models:
  - { id: "seedream-5.0-pro",  access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit, layer-separation], best_for: "high-density infographics and dense multi-block text, grounded editing driven by marks drawn on the input image, layer separation into editable assets, native multilingual text, and the most photoreal lighting, material, and skin rendering in the family" }
  - { id: "seedream-5.0-lite", access: "closed-weights", tier: "budget",   caps: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning], best_for: "reasoning-aware and knowledge-driven images (diagrams, charts, multi-subject scenes it plans), plus current-events and real-world-referential content via online search" }
  - { id: "seedream-4.5",      access: "closed-weights", tier: "std",      caps: [text-to-image, image-edit, multi-image-reference, text-rendering], best_for: "designer-grade typography and posters, dense legible text, and faithful deep editing that tracks every reference detail" }
  - { id: "seedream-4.0",      access: "closed-weights", tier: "base",     caps: [text-to-image, image-edit, multi-image-reference, text-rendering], best_for: "fast, layout-aware generation and multi-panel series when speed matters more than ultimate polish" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit, layer-separation]
prompt:
  languages: ["en", "zh", "fr", "de", "ru", "ja", "ko", "es", "ar", "mixed"]
  formula: "Subject + Action + Environment, plus optional Style, Color, Lighting, Composition; order the description Subject, Setting, Style, Lighting, Technical"
  literal_text: "wrap the exact in-image words in double quotes, give them a surface and a described style; short display text is reliable on every tier, and 5.0 Pro is the tier that holds dense multi-block text"
  length_strategy: "on 4.5 and 5.0-lite, concise and precise beats ornate, and over-long prompts get details dropped or contradicted; 5.0 Pro inverts this for information design, absorbing long structured art direction because it plans the layout before it draws"
  auto_expand_behavior: "prompt optimization is on by default on many hosts; write the full prompt yourself when you need tight control"
  negatives: "generate first, then add exclusions only to fix an artifact you actually see; where a host exposes no negative field, fold the exclusion into the positive prompt"
  references: "name multiple inputs positionally as Image 1, Image 2, and so on (some hosts use Figure 1, Figure 2); say what to take from which; a single reference can be named descriptively"
  annotations: "5.0 Pro reads marks drawn on the input image; address each marked region by the color of its box or lasso as a bulleted list (for example 'Red frame: ...'), write each bullet as content rather than a command, and close with an explicit line holding everything else unchanged"
sources:
  official: ["https://seed.bytedance.com/en/seedream5_0_pro", "https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro", "https://docs.byteplus.com/en/docs/ModelArk/1829186", "https://docs.byteplus.com/en/docs/ModelArk/1824121", "https://seed.bytedance.com/en/seedream5_0_lite", "https://seed.bytedance.com/en/seedream4_5"]
  provider: ["https://fal.ai/seedream-5.0", "https://fal.ai/models/bytedance/seedream/v5/pro/edit", "https://fal.ai/learn/devs/seedream-v4-5-prompt-guide", "https://blog.fal.ai/seedream-5-0-lite-prompting-guide/", "https://fal.ai/learn/tools/how-to-use-seedream-5-lite", "https://wavespeed.ai/blog/posts/seedream-4-0-to-5-0-complete-tutorial-image-generation-editing/"]
  community: []
last_verified: "2026-07-13"
---

# Seedream: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution limits, image counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the Seedream image family: seedream-5.0-pro, seedream-5.0-lite, and seedream-4.5, which share one prompt scheme (seedream-4.0 is the predecessor and prompts the same way). A prompt written for one tier transfers to the others: 5.0 Pro adds capability, not new syntax.
- Seedream is an image model. For video, ByteDance's separate model is Seedance, which is out of scope here.
- Write prompts as coherent natural language, not comma-separated tags. Seedream reads intent, and since 4.5 it gets the intended image with less description, so be concise and precise rather than ornate.
- Three things are reachable only on 5.0 Pro, and only if you write for them: marks drawn on the input image (grounded editing), layer separation, and native prompting in languages beyond English and Chinese. On the older tiers, describe the region in words instead.

</rules>

## TL;DR

<template id="quickstart">

{subject with key attributes and action}, {setting}, {style}, {lighting}, {a few technical or composition cues}. For in-image words, add: a {sign, title, or label} that reads "{exact text}" in {described typography}.

</template>

## Models and when to use which

All four share one prompt scheme; a prompt written for one transfers to the others. Pick by the job.

- `seedream-5.0-pro`: the flagship. It plans the layout before it renders, which makes it the tier for high-density infographics, dense multi-block text, posters, and UI mockups. It is also the only tier that reads marks drawn on the input image, separates an image into editable layers, and prompts natively in languages beyond English and Chinese. Its lighting, material, and skin rendering are the most photoreal in the family.
- `seedream-5.0-lite`: reasons about the scene before it renders, so it plans multi-subject composition, spatial relations, and physical plausibility, and it can pull on real-world knowledge and online search. Use it for knowledge-driven and reasoning-heavy images (diagrams, charts, multi-subject scenes with per-subject attributes) and for current or real-world-referential content.
- `seedream-4.5`: the typography and deep-editing workhorse. Strongest at legible dense text, posters, logos, and faithful editing that tracks every detail across reference images. Prefer it when visual polish and text fidelity matter most.
- `seedream-4.0`: the predecessor, fast and layout-aware. Use it for quick multi-panel series and social assets when speed outweighs ultimate quality.

Rule of thumb: for dense information design, annotation-driven editing, multilingual text, or maximum photoreal polish, reach for 5.0 Pro. For knowledge-driven or topical work where online search earns its keep, reach for 5.0-lite. 4.5 remains a strong typography and deep-editing workhorse.

## How the model reads prompts

- Natural language wins. Coherent sentences that state intent beat keyword lists. "A girl in a lavish dress walking under a parasol along a tree-lined path, in the style of a Monet oil painting" beats "girl, umbrella, tree-lined street, oil painting texture".
- Concise and precise beats ornate. Since 4.5 the model needs less description and no longer washes colors out, so stacking flowery vocabulary hurts more than it helps. Spend words on substance.
- Front-load what matters. Earlier words carry more weight, so lead with the subject and the elements you care most about.
- It rewards the right length. A few focused sentences is the sweet spot. Very long prompts scatter the model's attention and start to contradict themselves, so it drops or fumbles details.
- 5.0 Pro is the exception to that length rule, but only for information design. It parses intent and plans the layout before it draws, so long, structured art direction that enumerates every panel of an infographic or UI holds together instead of scattering. Keep prompts tight on the older tiers; spend the words on 5.0 Pro when the image is information-dense.
- 5.0-lite reasons before it draws. It evaluates the whole scene first, so you can assign attributes per subject and trust it to plan the layout (see the reasoning layer below).
- It is bilingual, and language sets culture. English, Chinese, and mixed prompts all work. Writing the prompt in a scene's native language shifts the whole atmosphere (architecture, light, mood) to match that culture, not just the words.
- Prompt optimization is on by default. A terse prompt is auto-expanded, which adds variety but takes control away. Write the full prompt when the output must match your intent.

## Prompt structure

<rules id="structure">

- Official formula: Subject + Action + Environment, then optional Style, Color, Lighting, Composition.
- A fuller ordering that works well: Subject, then Setting, then Style, then Lighting, then technical or camera cues. Each added clause removes one decision from the model and hands it to you.
- State the purpose and type when there is one ("design a logo for a gaming company", "an educational infographic"), not just the contents.
- Swap vague adjectives for concrete detail: instead of "beautiful sunset", name the coast, the cloud type, the color, and the light direction.

</rules>

<template id="general">

{subject with attributes and action}, {detailed setting}, {style or medium}, {lighting direction and quality}, {camera or composition cues}

</template>

<example use_case="photoreal-portrait">

```text
Professional headshot of a female CEO with short blonde hair, confident expression, wearing a navy suit, neutral office background, soft studio lighting, shallow depth of field, 85mm lens, high-end corporate photography
```

*Why: subject and wardrobe first, then setting, lighting, and technical cues, concise but fully specified, the register Seedream prefers*

</example>

## What 5.0-lite's reasoning adds

Seedream 5.0-lite runs a reasoning pass over the prompt before it generates. This does not change how you write a prompt; it changes what the same prompt reliably delivers.

<rules id="reasoning">

- Pile on per-subject attributes and trust the plan. "The woman on the left is tall in a red jacket; the man in the middle is shorter in a denim shirt; the woman on the right has silver hair and a black turtleneck" holds together, because the model assigns and tracks attributes across the scene.
- Ask for structured and technical content and expect coherence: labeled diagrams, charts with real axes, scientific cross-sections, formulas. Name the format precisely.
- Use real-world and current references. Name a specific building, brand, regional style, or recent topic and the model has something concrete to ground on through its world knowledge and online search.
- Drop quality-booster noise. Tokens like "masterpiece, best quality, 8K, ultra-detailed" distract the reasoning pass; describe the actual image instead.

</rules>

<example use_case="reasoning-infographic">

```text
A clean infographic of the water cycle, with labeled arrows for evaporation, condensation, precipitation, and collection, earth tones with blue water elements, white background, educational illustration style
```

*Why: leans on the reasoning pass to arrange the stages in a scientifically coherent layout rather than as decorative icons*

</example>

## Text rendering

Legible in-image text is a Seedream strength, and 4.5's typography is its headline feature.

<rules id="text">

- Wrap the exact words in double quotes. Unquoted text is read as scene description, so "a poster titled "Seedream 4.5"" renders the literal title while "a poster titled Seedream 4.5" may not.
- Give the text a surface and a style: a neon sign, a chalkboard, an engraved plate; "bold sans-serif", "elegant script", "hand-painted".
- State placement: title top-center, subtitle below, label bottom-right.
- Keep each rendered string short. Single words and short phrases render cleanly; dense small text and long paragraphs drift. 4.5 holds small text better than 5.0-lite, but short is safer on both.
- For non-Latin or mixed scripts, name the language; the model renders multiple scripts together.

</rules>

<example use_case="poster-typography">

```text
A dark-navy tech-conference poster. The all-caps title reads "AI SUMMIT 2026" in bold sans-serif, centered; the subtitle "San Francisco, June 15 to 17" sits below in light gray. A holographic shape glows in the center, generous whitespace around it
```

*Why: each text element is quoted, placed, and given a weight, and the layout is described, so the typography resolves cleanly*

</example>

## Multilingual prompting and text

5.0 Pro takes prompts natively in a wide set of languages, French, German, Russian, Japanese, Korean, Spanish, and Arabic alongside Chinese and English, and renders each script by its own typographic rules. Earlier tiers are effectively English and Chinese only.

<rules id="multilingual">

- Write the prompt in the target language to get a culturally native image, not merely translated text. The model aligns architecture, faces, and clothing to that language's cultural context, so the whole scene shifts, not just the glyphs.
- Name the script when it must be rendered, and expect the model to apply that language's rules: right-to-left cursive for Arabic, accent marks for Spanish.
- Multi-language layouts work. Ask for the same copy side by side in several named languages and it sets each block correctly.
- For a translation edit, pin the design and move only the words: hold the palette, icons, imagery, and module structure, translate the text, and call out the one structural change the target script actually forces, such as flipping the layout to right-to-left.

</rules>

<example use_case="layout-preserving-translation">

```text
Keep the medical poster's color palette, icons, doctor photo, module structure, and overall layout unchanged. Only translate all English text into Arabic and adjust the layout to right-to-left reading
```

*Why: a translation edit that pins every design invariant and moves only the language, while naming the single structural change the target script genuinely requires*

</example>

<example use_case="multi-language-poster">

```text
A subway station public safety notice poster, vertical 4:5, modern public transit wayfinding style, white background, yellow warning color, black icons. The text content is displayed side by side in four languages: English, Chinese, Japanese, and Korean
```

*Why: naming each language and asking for them side by side lets the model set four scripts in one layout, each following its own typographic rules*

</example>

## Spatial and composition control

<rules id="spatial">

- With more than one subject, explicit positions are essential, or placement becomes a coin flip. Name where each subject sits.
- Positional vocabulary: on the left, on the right, in the center, in the foreground, in the background. Relational: between them, behind, above, below, beside. Scale: towering over, dwarfed by, filling the frame. Frame regions: lower right third, upper left corner, dead center.
- Describe negative space on purpose. The model fills the frame by default, so to leave it empty say so ("enormous negative space above and to the left", "positioned in the lower right third").

</rules>

<example use_case="multi-subject-spatial">

```text
On the left side of a small marble cafe table, a man in a rust linen shirt. On the right, a woman in an oversized cream sweater, laughing. Two steaming cappuccinos between them. Warm window light, shallow depth of field
```

*Why: every subject is pinned to a position and the props are placed relationally, so the composition is not left to chance*

</example>

<example use_case="multi-subject-reasoning-scene">

```text
A rooftop bar at golden hour, four friends posing for a group photo. On the far left, a tall woman with short silver hair in a red leather jacket raises a glass. Next to her, a shorter man in a blue denim shirt with rolled sleeves laughs. To his right, a woman in a flowing white sundress holds a small camera. On the far right, a bearded man in a charcoal suit leans on the railing. Warm backlight from the setting sun, the city skyline soft behind them, a small neon sign on the wall reads "SKYLINE". Editorial photography, shallow depth of field
```

*Why: a long flagship that leans on 5.0-lite's reasoning, four subjects each with distinct attributes pinned to explicit left-to-right positions, plus lighting, background, and one quoted sign, so the model plans the composition instead of blending the people*

</example>

## By use-case

### Photorealism

<rules id="photoreal">

- Lead with camera language (lens, shot size, depth of field) and name the light direction and quality. Name materials and textures you want rendered.
- Use real camera and film cues when you want their look: "85mm", "shallow depth of field", "golden hour", "rim lighting". Material words ("matte white", "brushed steel") beat "shiny".
- 5.0 Pro executes advanced camera technique if you name each motion layer separately. Say which parts stay sharp and which blur, and how, rather than asking for "motion blur" and hoping.
- For skin, ask for the texture you want and forbid the smoothing you do not: name pores, lines, and matte falloff, and say "avoid excessive skin smoothing" when retouching.

</rules>

<example use_case="product-shot">

```text
A modern smartphone floating against a dark background with a subtle blue gradient, product photography, soft studio lighting raking across the glossy screen, ultra-detailed, commercial quality
```

*Why: one clear subject with directed lighting and material cues, no tag soup*

</example>

<example use_case="panning-motion">

```text
A panning shot of a cyclist. The rider and the bicycle are clear and sharp, the background street is stretched into horizontal motion blur, and the wheel spokes have rotational blur to convey a sense of speed
```

*Why: each motion layer is named on its own (sharp subject, horizontal background blur, rotational wheel blur), which is what produces a true panning shot instead of a uniformly smeared frame*

</example>

### Posters and typography

<template id="poster">

A {style} poster for {subject}. The title reads "{headline}" in {typography} at the {position}; the subtitle "{subtitle}" in {typography} below. {color palette}, {composition and whitespace}.

</template>

### Diagrams and infographics

<rules id="diagram">

- Name the format explicitly (mind map, Venn diagram, flowchart, cross-section, labeled chart) and the surface (on a blackboard, on a white background).
- Use precise technical terminology so the concept is represented accurately, and quote any labels that must read exactly. 5.0-lite's reasoning makes structured layouts hold together.
- On 5.0 Pro, dense information design is the headline capability, so spend the words. Anchor one subject at the center, then enumerate every surrounding panel by its exact chart type, and name the palette and the layout discipline. The model plans the hierarchy before it draws.
- Name chart types precisely. "A bar chart comparing the sizes of five research stations" gives it a layout to compute; "some charts" does not.

</rules>

<example use_case="equation-blackboard">

```text
A blackboard showing the system of equations "5x + 2y = 26" and "2x - y = 5" with the solution steps written out beneath in neat chalk
```

*Why: precise content, an explicit surface, and quoted strings, the recipe for educational output*

</example>

<example use_case="high-density-infographic">

```text
A visual infographic chronicling scientific research at Antarctica's Qinling Station. Place the main Qinling Station building at the center. Surround it with a timeline of research station development, a bar chart comparing the sizes of five research stations, a pie chart of the station's energy sources, and a line chart of monthly sunshine. Supplement this with realistic photos of research equipment, a summer weather panel, a seven-step fieldwork flowchart, and on-site sampling photography to showcase China's Antarctic research in a comprehensive way
```

*Why: the long flagship for 5.0 Pro, and the pattern to copy, one anchor subject fixed at the center and then every surrounding panel named by its exact chart type, so the model has a concrete hierarchy to plan rather than a vague request for an infographic*

</example>

### Artistic styles

<rules id="styles">

- Name the medium or movement as a style anchor ("watercolor illustration", "oil painting", "isometric 3D render", "concept art", "film noir"), or the output drifts.
- Reinforce a look with a few related cues rather than one vague word, and name a reference artist or film when you want a specific signature.

</rules>

## Image editing

<rules id="edit">

- Describe the end state, not the process. "Change the background to a sunset beach, keep the person and their clothing exactly the same" works; "make it better" does not.
- Name what moves, pin what stays. Every edit should state the change and the invariants ("keep the same road, tree, and composition"); the model keeps the geometry and rebuilds the rest, so name what must survive.
- The four operations are addition, deletion, replacement, and modification. Name the target element precisely and avoid vague pronouns ("change it").
- Use spatial words to scope a change (the tallest one, the item on the left, the red area).
- When words are not enough, mark the source image with arrows, boxes, or doodles and refer to them by color or shape ("insert a sofa where the blue area is marked", "enlarge the title to match the red box").
- For a bigger change, describe the target's characteristics (brushstrokes, palette, visible pixels), not just "make it a painting".

</rules>

<example use_case="background-swap">

```text
Change the background to a sunset beach, keep the person and their clothing exactly the same, and match the lighting and shadows to the new scene
```

*Why: names the change, pins the subject as invariant, and asks for relighting so the composite holds together*

</example>

<example use_case="scoped-material-edit">

```text
Keep the model's pose and the shape of the dress unchanged. Change the dress material from silver metal to clear water, so the skin shows through, and shift the lighting from reflection to refraction
```

*Why: fixes the invariants first, then scopes a single material change and its physical consequence, leaving no ambiguity*

</example>

## Interactive precision editing

Language is good at saying what to generate and bad at saying where to edit. On 5.0 Pro you stop describing the location in words and mark it on the image instead: the model reads point, box, and lasso selections, freehand doodles, and handwritten annotations, and turns them into deterministic local edits. This is the biggest prompt-craft change the Pro tier brings, and it is the one thing that does not degrade gracefully onto 4.5 or 5.0-lite.

<rules id="grounded-edit">

- Mark the region on the input image, then address it by the color of its mark. Draw colored boxes or lassoes and write one bullet per region ("Red frame: ...", "Green frame: ..."). Each element stays inside its own boundary and stays independent of the others.
- Write each bullet as the content you want there, not as a command. "Red frame: oversized blue cat head gazing at bubbles, no body" beats "put a cat in the red box". Fold any exclusion into the same bullet.
- Close with an explicit hold line. End the instruction with "Keep everything else the exact same". This is NAME WHAT MOVES, PIN WHAT STAYS applied to a marked-up image.
- Point at the marks rather than transcribing them when the image already carries handwriting: "Perform precise edits based on the 6 purple boxes and handwritten annotations in the original image."
- A rough sketch is a valid control signal. Hand the model a crude layout of blocks and lines, tell it to render the finished piece, and tell it to preserve the sketch's layout structure.
- Trust it to find blank space. Instructions like "complete all the questions above and write out the calculation steps" work because the model locates each answer's slot on its own.
- For color, give a hex code or point at a swatch in another image, and pair it with a material to swap surface and color in one instruction.
- Ask for layer separation in plain text. Name the layers you expect back and ask for the background to be restored where the subject was covering it, which is what makes the layers usable as assets.

</rules>

<example use_case="colored-frame-regions">

```text
- Red frame: oversized blue cat head gazing at bubbles, no body
- Green frame: transparent bubble with indoor light reflections
- Yellow frame: big warm beige wool ball
- Purple frame: grass-green blanket draped on the sofa

Keep everything else the exact same
```

*Why: one bullet per marked region, each written as content rather than a command, each pinned to its own colored boundary, and one closing line that holds the rest of the frame constant*

</example>

<example use_case="sketch-to-render">

```text
Transform this annotated hand-drawn sketch into a publishable premium SaaS website hero section, strictly preserving the layout structure of the sketch. Generate a clear English headline in the red-box title area that reads "Orchestrate AI Workflows at Scale", with a short subtitle beneath it
```

*Why: the sketch carries the layout and the prompt carries the finish, and the quoted headline is welded to a specific marked box so the type lands where it was drawn*

</example>

<example use_case="color-and-material-swap">

```text
Change the pumpkins to an alternating pattern of dark green (#3E4A2E) and turmeric yellow (#DB973E), and give the background typography an embroidered texture
```

*Why: two scoped edits in one instruction, each welded to a named element, with the colors pinned by hex and paired with a color name so they land exactly*

</example>

<example use_case="material-and-swatch-from-references">

```text
Using the material from Image 1 and the color swatch from Image 2, modify the sofa in Image 3
```

*Why: three inputs each doing exactly one job, the edit target welded to Image 3 and the two borrowed properties welded to their own sources, ONE ROLE PER INPUT*

</example>

<example use_case="layer-separation">

```text
Separate this poster into independent editable layers: the text, the main subject, the background, and the environmental decorations. Inpaint the background where the subject was covering it, and keep each layer transparent where nothing sits
```

*Why: layers are requested in plain language, each expected layer is named, and asking for the occluded background to be restored is what turns the output into reusable assets rather than flat cutouts*

</example>

## Multiple reference images

Seedream takes several reference images and composes across them: swap a subject, transfer a style, dress a character, match a palette.

<rules id="multi-image">

- Name each input positionally: Image 1, Image 2, Image 3, in upload order (some hosts use Figure 1, Figure 2). A single reference can instead be named descriptively ("the character in the reference image").
- Weld every borrowed element to its source. With three or more inputs an unattached phrase like "the outfit" is ambiguous, so write "the outfit from Image 2", "the style of Image 3". Read the instruction as one role per input.
- Split a reference prompt into two parts: the reference target (what to take from each image, such as a character, a product's material, a style) and the generated-scene description (the output you want).
- Name what moves, pin what stays, the same as in single-image editing: state the elements you are taking and hold identity, pose, or composition constant.

</rules>

<example use_case="character-swap-plus-style">

```text
Replace the character in Image 2 with the character from Image 1, and render the result in the style of Image 3, keeping Image 2's pose and composition
```

*Why: three inputs, each assigned one role (subject, target scene, style), every element welded to its source and the invariants pinned*

</example>

<example use_case="makeup-and-outfit-transfer">

```text
Transfer the makeup from Image 2 onto the person in Image 1 and dress them in the outfit from Image 3, keeping the person's face shape and hairstyle unchanged
```

*Why: two borrowed elements from two sources onto the base subject in Image 1, each named, with identity pinned*

</example>

<example use_case="style-transfer">

```text
Redraw the scene from Image 1 in the watercolor style of Image 2, keeping Image 1's subjects and composition unchanged
```

*Why: a pure style transfer, taking only the look from Image 2 while the content stays locked to Image 1*

</example>

<example use_case="reasoned-multi-image">

```text
Classify the flowers in Image 1 by variety, then arrange one of each into the three vases in Image 2, matching the lighting of Image 2
```

*Why: combines reasoning (classify and sort) with a positional multi-image instruction, a 5.0-lite strength*

</example>

<example use_case="multi-person-fusion">

```text
Combine the people from Image 2 to Image 6 into a group photo referencing the positioning in Image 1. The people should have happy expressions, with trees and a cafe storefront in the background
```

*Why: one input carries composition rather than content, serving purely as a positioning template while the others supply the subjects, and the fused group still resolves to one consistent background and lighting*

</example>

## Advanced control

<rules id="advanced">

- HEX colors: drop a hex code in the prompt for accurate color, and pair it with a name ("#FF006E hot pink") for best results. It works best on large areas and gradients (give the start and end colors), which is useful for brand consistency.
- Language as art direction: write the prompt in a scene's native language to pull its cultural look, and mix a native scene description with English technical terms when you want both.
- Series and sets: trigger a consistent multi-image set by asking for "a series", "a set", or a count, and number the frames ("Image 1: ...; Image 2: ..."), keeping style and palette consistent across them.

</rules>

## JSON structured prompts

Seedream reads a JSON object as the prompt: give each element its own description, position, and color, and the fields become the layout. Reach for it when you have several subjects to place, per-element color to lock, or commercial art direction to spell out; keep plain prose for single-subject or creative work where model freedom helps. Mix the two, JSON for structure and natural language inside the fields. The format suits 5.0-lite especially, since it reasons over the listed parts before it composes them.

<template id="json">

```json
{
  "scene": "the overall scene in one line",
  "subjects": [
    { "description": "subject with attributes", "position": "where in frame", "color": "#hex or named color" }
  ],
  "style": "medium or art direction",
  "color_palette": ["#hex1", "#hex2"],
  "lighting": "direction and quality",
  "camera": { "angle": "camera angle", "lens": "lens", "depth_of_field": "focus behavior" }
}
```

</template>

<example use_case="json-multi-subject">

```json
{
  "scene": "Overhead flat lay breakfast spread on a marble surface",
  "subjects": [
    { "description": "Acai smoothie bowl with banana, granola, and chia seeds", "position": "upper left", "color": "deep purple #6B2FA0" },
    { "description": "Black coffee in a white ceramic cup", "position": "upper right", "color": "dark brown #3E1F00" },
    { "description": "Sourdough toast with avocado", "position": "lower left", "color": "green #568203" },
    { "description": "Glass of fresh orange juice", "position": "lower right", "color": "bright orange #FF8C00" },
    { "description": "Bowl of mixed berries", "position": "center" }
  ],
  "style": "editorial food photography, flat lay",
  "lighting": "soft natural window light from the top",
  "camera": { "angle": "directly overhead", "lens": "35mm wide" }
}
```

*Why: in prose these five dishes would bleed into one another, but one object each, with a position and a per-item hex, pins every subject and its color, which is exactly when JSON earns its place over a sentence*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Do not pre-load negatives. Generate first, then add an exclusion only to fix an artifact you actually see.
- Some 5.0-lite text-to-image endpoints expose no negative field. Where there is none, fold the exclusion into the positive prompt by describing the desired opposite ("clean even skin" rather than "no blemishes").
- When a negative field exists, keep it short and specific (for example: blurry, low quality, distorted, watermark, text overlay, cropped).

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Keyword soup: rewrite disconnected tags as one descriptive scene.
- Quality-booster stacking: "masterpiece, best quality, 8K" adds nothing and distracts 5.0-lite's reasoning; describe the image instead.
- Over-long prompts: past a few dense sentences the model drops details or contradicts itself (two subjects in one spot, conflicting light). Keep it focused.
- Conflicting instructions: "photorealistic cartoon" and similar contradictions confuse the model.
- Unquoted in-image text: words that must appear must be in double quotes, or they get read as scene description.
- Dense tiny text: split long or small text into short labeled strings; expect display-size text, not paragraphs.
- Vague edits: name the target element and avoid pronouns; state what stays unchanged.
- Multi-subject without positions: assign each subject a place, or the model guesses.
- Assuming Pro behavior on the older tiers: annotation-driven editing, layer separation, and non-English prompting are 5.0 Pro capabilities. On 4.5 and 5.0-lite, describe the region in words instead of marking it.
- Expecting pixel-perfect output from 5.0 Pro: the owner states that fine-grained text rendering and pixel-level editing consistency are still imperfect. Proofread dense small type and inspect the seams of a local edit.
- Marking regions but not pinning the rest: an annotated edit without a closing "keep everything else the exact same" invites drift outside the marked areas.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. Seedream 5.0 Pro shipped on 2026-07-08, which settles the earlier owner-versus-provider question about the full 5.0: it is released, and 5.0-lite remains the separate reasoning and online-search tier. Providers disagree with each other on how many languages 5.0 Pro speaks (claims range from "over ten" to "a dozen" to "14"), so this guide names the attested languages and prints no count. WaveSpeed's 5.0 Pro page is autogenerated boilerplate that omits the Pro capabilities entirely; it is not a source of model-specific prompt craft.

- Official (ByteDance, BytePlus): [Seedream 5.0 Pro model page](https://seed.bytedance.com/en/seedream5_0_pro), [Seedream 5.0 Pro launch blog](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro), [Seedream 4.0-4.5 prompt guide](https://docs.byteplus.com/en/docs/ModelArk/1829186), [Seedream 4.0-5.0 tutorial](https://docs.byteplus.com/en/docs/ModelArk/1824121), [Seedream 5.0-lite model page](https://seed.bytedance.com/en/seedream5_0_lite), [Seedream 4.5 model page](https://seed.bytedance.com/en/seedream4_5).
- Provider: [fal Seedream 5.0 overview](https://fal.ai/seedream-5.0), [fal Seedream 5.0 Pro edit](https://fal.ai/models/bytedance/seedream/v5/pro/edit), [fal Seedream 4.5 prompt guide](https://fal.ai/learn/devs/seedream-v4-5-prompt-guide), [fal Seedream 5.0-lite prompting guide](https://blog.fal.ai/seedream-5-0-lite-prompting-guide/), [fal how to use Seedream 5.0-lite](https://fal.ai/learn/tools/how-to-use-seedream-5-lite), [WaveSpeed Seedream 4.0 to 5.0 tutorial](https://wavespeed.ai/blog/posts/seedream-4-0-to-5-0-complete-tutorial-image-generation-editing/).

Last verified: 2026-07-13.
