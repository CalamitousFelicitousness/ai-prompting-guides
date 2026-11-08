---
guide: "Seedream (image)"
prompt_scheme: "seedream"
models:
  # seedream-5.5 is PROVISIONAL: hosted by WaveSpeed, described by BytePlus Lumina preview pages, not yet documented by ByteDance or BytePlus ModelArk.
  - { id: "seedream-5.5",       access: "closed-weights", tier: "flagship",  caps: [text-to-image, image-edit, multi-image-reference, text-rendering, layer-separation, transparency], best_for: "provisional: the announced successor to 5.0 Pro, aimed at photographic realism, cut-out subjects on transparent backgrounds, and edits that hold steady over many rounds; whether it reads marks or coordinate tags is undocumented" }
  # BytePlus lists the 5.0 tiers as Dola Seedream 5.0 pro / flash (dola-seedream-5-0-pro-260628, dola-seedream-5-0-flash-260915); the YYMMDD suffix is part of the id there.
  - { id: "seedream-5.0-pro",   access: "closed-weights", tier: "flagship",  caps: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit, layer-separation], best_for: "high-density infographics and dense multi-block text, grounded editing driven by marks drawn on the input image or coordinate tags in the prompt, layer separation into editable assets, native multilingual text, and the most photoreal lighting, material, and skin rendering in the documented family" }
  - { id: "seedream-5.0-flash", access: "closed-weights", tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit, layer-separation], best_for: "the 5.0 Pro feature set (marks, coordinate tags, layer separation, multilingual text) faster and cheaper, for latency- and cost-sensitive work; the owner reserves the highest image quality for Pro" }
  - { id: "seedream-5.0-lite",  access: "closed-weights", tier: "budget",    caps: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning], best_for: "reasoning-aware and knowledge-driven images (diagrams, charts, multi-subject scenes it plans), plus current-events and real-world-referential content via online search" }
  - { id: "seedream-4.5",       access: "closed-weights", tier: "std",       caps: [text-to-image, image-edit, multi-image-reference, text-rendering], best_for: "designer-grade typography and posters, dense legible text, and faithful deep editing that tracks every reference detail" }
  - { id: "seedream-4.0",       access: "closed-weights", tier: "base",      caps: [text-to-image, image-edit, multi-image-reference, text-rendering], best_for: "fast, layout-aware generation and multi-panel series when speed matters more than ultimate polish" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit, layer-separation, transparency]
prompt:
  languages: ["en", "zh", "ru", "ar", "fil", "th", "tr", "ko", "ms", "es", "pt", "id", "fr", "de", "vi", "ja", "mixed"]
  formula: "Subject + Action + Environment, plus optional Style, Color, Lighting, Composition; order the description Subject, Setting, Style, Lighting, Technical"
  literal_text: "wrap the exact in-image words in double quotes, give them a surface and a described style; short display text is reliable on every tier, and 5.0 Pro is the tier that holds dense multi-block text"
  length_strategy: "on 4.5 and 5.0-lite, concise and precise beats ornate, and over-long prompts get details dropped or contradicted; 5.0 Pro inverts this for information design, absorbing long structured art direction because it plans the layout before it draws"
  auto_expand_behavior: "prompt optimization is on by default on many hosts; write the full prompt yourself when you need tight control"
  negatives: "generate first, then add exclusions only to fix an artifact you actually see; where a host exposes no negative field, fold the exclusion into the positive prompt"
  references: "name multiple inputs positionally as Image 1, Image 2, and so on (some hosts use Figure 1, Figure 2); say what to take from which; a single reference can be named descriptively"
  annotations: "5.0 Pro and Flash read marks drawn on the input image; address each marked region by the color of its box or lasso as a bulleted list (for example 'Red frame: ...'), write each bullet as content rather than a command, ask for the marks to be removed, and close with an explicit line holding everything else unchanged"
  coordinates: "5.0 Pro and Flash read <point>x y</point> and <bbox>x1 y1 x2 y2</bbox> in the prompt, on a 0-999 grid per image with 0 0 at the top-left; name the image beside each tag and the target inside each box, and never guess coordinates you have not measured"
  transparency: "5.5 (provisional): a transparent background is a host request setting, not prompt text; in the prompt, describe the subject on its own ('isolated') and nothing behind it"
sources:
  official: ["https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro", "https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro-editing-guide", "https://docs.byteplus.com/en/docs/modelark/model-release-announcement", "https://seed.bytedance.com/en/seedream5_0_pro", "https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro", "https://docs.byteplus.com/en/docs/ModelArk/1829186", "https://docs.byteplus.com/en/docs/ModelArk/1824121", "https://seed.bytedance.com/en/seedream5_0_lite", "https://seed.bytedance.com/en/seedream4_5", "https://ai.byteplus.com/lumina/en/image/what-is-seedream-5-5"]
  provider: ["https://wavespeed.ai/models/bytedance/seedream-v5.5", "https://wavespeed.ai/models/bytedance/seedream-v5.5/edit", "https://wavespeed.ai/models/bytedance/seedream-v5.5/layer-decomposition", "https://fal.ai/seedream-5.0", "https://fal.ai/models/bytedance/seedream/v5/pro/edit", "https://fal.ai/learn/devs/seedream-v4-5-prompt-guide", "https://blog.fal.ai/seedream-5-0-lite-prompting-guide/", "https://fal.ai/learn/tools/how-to-use-seedream-5-lite", "https://wavespeed.ai/blog/posts/seedream-4-0-to-5-0-complete-tutorial-image-generation-editing/"]
  community: []
last_verified: "2026-11-08"
---

# Seedream: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution limits, image counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the Seedream image family: seedream-5.0-pro, seedream-5.0-flash, seedream-5.0-lite, and seedream-4.5, which share one prompt scheme (seedream-4.0 is the predecessor and prompts the same way), plus provisional notes on seedream-5.5. A prompt written for one tier transfers to the others: 5.0 Pro and Flash add capability, not new syntax.
- Seedream is an image model. For video, ByteDance's separate model is Seedance, which is out of scope here.
- Write prompts as coherent natural language, not comma-separated tags. Seedream reads intent, and since 4.5 it gets the intended image with less description, so be concise and precise rather than ornate.
- Three things are reachable only on 5.0 Pro and 5.0 Flash, and only if you write for them: grounded editing (marks drawn on the input image, or coordinate tags in the prompt), layer separation, and native prompting in languages beyond English and Chinese. On the older tiers, describe the region in words instead.

</rules>

## TL;DR

<template id="quickstart">

{subject with key attributes and action}, {setting}, {style}, {lighting}, {a few technical or composition cues}. For in-image words, add: a {sign, title, or label} that reads "{exact text}" in {described typography}.

</template>

## Models and when to use which

All of them share one prompt scheme; a prompt written for one transfers to the others. Pick by the job.

- `seedream-5.5` (provisional): the announced successor to 5.0 Pro. WaveSpeed hosts it, but ByteDance has not documented it, and BytePlus's own Lumina pages still describe it as a preview. BytePlus says prompts carry over from 5.0 Pro unchanged. Its stated aims are photographic realism, subjects cut out onto transparent backgrounds, and edits that hold steady over many rounds. Until ByteDance documents it, use 5.0 Pro or Flash for anything that relies on marks, coordinate tags, or a documented behavior (see Seedream 5.5: provisional notes).
- `seedream-5.0-pro`: the documented flagship. It plans the layout before it renders, which makes it the tier for high-density infographics, dense multi-block text, posters, and UI mockups. With 5.0 Flash, it is one of two tiers that read marks drawn on the input image and coordinate tags in the prompt, separate an image into editable layers, and prompt natively in languages beyond English and Chinese. Its lighting, material, and skin rendering are the most photoreal in the documented family.
- `seedream-5.0-flash`: the same feature set as 5.0 Pro (marks, coordinate tags, layer separation, multilingual text) at higher speed and lower cost. The owner reserves the highest image quality for Pro, so move to Pro for the densest information design or the most demanding photoreal finish; prompts transfer unchanged in either direction.
- `seedream-5.0-lite`: reasons about the scene before it renders, so it plans multi-subject composition, spatial relations, and physical plausibility, and it can pull on real-world knowledge and online search. Use it for knowledge-driven and reasoning-heavy images (diagrams, charts, multi-subject scenes with per-subject attributes) and for current or real-world-referential content.
- `seedream-4.5`: the typography and deep-editing workhorse. Strongest at legible dense text, posters, logos, and faithful editing that tracks every detail across reference images. Prefer it when visual polish and text fidelity matter most.
- `seedream-4.0`: the predecessor, fast and layout-aware. Use it for quick multi-panel series and social assets when speed outweighs ultimate quality.

Rule of thumb: for dense information design, annotation-driven editing, multilingual text, or maximum photoreal polish, reach for 5.0 Pro, or 5.0 Flash when speed and cost matter more than the last step of quality. For knowledge-driven or topical work where online search earns its keep, reach for 5.0-lite. 4.5 remains a strong typography and deep-editing workhorse.

Naming: BytePlus lists the 5.0 tiers as Dola Seedream 5.0 pro and Dola Seedream 5.0 flash, with date-suffixed IDs (`dola-seedream-5-0-pro-260628`, `dola-seedream-5-0-flash-260915`). Dola is the BytePlus product prefix; it is the same model as Seedream 5.0 Pro or Flash on any other host.

## How the model reads prompts

- Natural language wins. Coherent sentences that state intent beat keyword lists. "A girl in a lavish dress walking under a parasol along a tree-lined path, in the style of a Monet oil painting" beats "girl, umbrella, tree-lined street, oil painting texture".
- Concise and precise beats ornate. Since 4.5 the model needs less description and no longer washes colors out, so stacking flowery vocabulary hurts more than it helps. Spend words on substance.
- Front-load what matters. Earlier words carry more weight, so lead with the subject and the elements you care most about.
- It rewards the right length. A few focused sentences is the sweet spot. Very long prompts scatter the model's attention and start to contradict themselves, so it drops or fumbles details.
- 5.0 Pro (and Flash, which shares its feature set) is the exception to that length rule, but only for information design. It parses intent and plans the layout before it draws, so long, structured art direction that enumerates every panel of an infographic or UI holds together instead of scattering. Keep prompts tight on the older tiers; spend the words on 5.0 Pro when the image is information-dense.
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

5.0 Pro and 5.0 Flash generate text natively in Russian, Arabic, Filipino, Thai, Turkish, Korean, Malay, Spanish, Portuguese, Indonesian, French, German, Vietnamese, and Japanese alongside Chinese and English, and render each script by its own typographic rules. Earlier tiers are effectively English and Chinese only.

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

Language is good at saying what to generate and bad at saying where to edit. On 5.0 Pro and 5.0 Flash you stop describing the location in words and point at it instead, in one of two forms: a mark drawn on the input image (point, box, and lasso selections, freehand doodles, handwritten annotations) named in the prompt, or a coordinate tag written into the prompt itself. Both turn into deterministic local edits. This is the biggest prompt-craft change the 5.0 tiers bring, and it is the one thing that does not degrade gracefully onto 4.5 or 5.0-lite.

<rules id="grounded-edit">

- Mark the region on the input image, then address it by the color of its mark. Draw colored boxes or lassoes and write one bullet per region ("Red frame: ...", "Green frame: ..."). Each element stays inside its own boundary and stays independent of the others.
- Write each bullet as the content you want there, not as a command. "Red frame: oversized blue cat head gazing at bubbles, no body" beats "put a cat in the red box". Fold any exclusion into the same bullet.
- Ask for the marks to be removed. The owner's own sketch edit says "Remove all sketch lines"; without it, drawn lines can survive into the result.
- Close with an explicit hold line. End the instruction with "Keep everything else the exact same". This is NAME WHAT MOVES, PIN WHAT STAYS applied to a marked-up image.
- Point at the marks rather than transcribing them when the image already carries handwriting: "Perform precise edits based on the 6 purple boxes and handwritten annotations in the original image."
- A rough sketch is a valid control signal. Hand the model a crude layout of blocks and lines, tell it to render the finished piece, and tell it to preserve the sketch's layout structure.
- Trust it to find blank space. Instructions like "complete all the questions above and write out the calculation steps" work because the model locates each answer's slot on its own.
- For color, give a hex code or point at a swatch in another image, and pair it with a material to swap surface and color in one instruction.

</rules>

<example use_case="freeform-sketch-marks">

```text
Edit the image based on the hand-drawn sketch. Add a stack of realistic magazines or art books in the marked area at the lower left, and add a ceramic cup of coffee with a saucer in the marked area on the right. Remove all sketch lines. Keep the composition unchanged. Let the newly added objects blend naturally into the original scene.
```

*Why: the owner's freeform-marking example. Each addition is welded to a marked area by its position, the sketch lines are removed explicitly, and the composition is pinned*

</example>

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

### Coordinate tags

The second form puts the location in the prompt as text. Coordinates are normalized per image on a 0-999 grid: the top-left corner is 0 0 and the bottom-right is 999 999, whatever the image's pixel size. Scale a pixel position by 1000 over the image's width (for x) or height (for y) and round.

<rules id="coordinates">

- `<point>x y</point>` marks a spot and lets the model decide how far the edit extends. `<bbox>x1 y1 x2 y2</bbox>` gives the top-left and bottom-right corners and fixes the size of the edit area.
- Put the image name beside every tag ("in Image 1 <bbox>...</bbox>"). For a cross-image move, give one box in the source image and one in the target.
- When a box covers several subjects, name the one to edit ("the person on the left", "the cat wearing a hat").
- Box what must not change, too, and say so ("keep the area ... unchanged"). A held box is a stronger pin than a closing sentence alone.
- Only use coordinates you have actually measured, from a user's selection in an editing UI or a vision model's detection. Never estimate them from a description; without real coordinates, describe the location in words or use a drawn mark.

</rules>

<example use_case="point-and-box-edits">

```text
Replace the person on the left in Image 1 <bbox>120 180 640 760</bbox> with a robot, replace the object at <point>520 460</point> in Image 1 with a crown, and keep the area Image 1 <bbox>700 120 920 360</bbox> unchanged.
```

*Why: assembled from the owner's coordinate examples. The box names its target because it may hold more than one person, the point leaves the extent to the model, and a second box pins the area that must not move*

</example>

<example use_case="cross-image-placement">

```text
Place the subject from Image 1 <bbox>179 283 796 986</bbox> at the position in Image 2 <bbox>118 331 933 871</bbox>.
```

*Why: the owner's cross-image example. One box selects what to take, the other says where it lands, and each tag sits beside the name of its image, ONE ROLE PER INPUT expressed as coordinates*

</example>

### Layer separation

5.0 Pro and Flash split one image into a base image plus separate transparent layers. On the BytePlus API this is its own request mode, and the prompt in that mode is optional: without one, the model picks out the main subjects, text, background, and decorations itself. Where a host has no separate mode, the launch blog's plain-text request ("Separate this poster into independent editable layers: ...") is the tolerated form.

<rules id="layers">

- To control the split, name the elements to separate in plain language and say where they are when that disambiguates.
- Alternatively, mark the elements on the input with doodles or selections, or give each region as a `<bbox>` tag.
- Layers come back as separate images, so edit one afterwards with an ordinary edit prompt on that layer alone.

</rules>

<example use_case="layer-separation-named">

```text
Decompose the person, title text, and decorative icon in the lower-right corner.
```

*Why: the owner's named-element form. It lists only what to lift into layers and gives a location for the one element that might be ambiguous*

</example>

<example use_case="layer-separation-regions">

```text
Perform precise layer separation on the image. The text regions to separate are at <bbox>180 64 812 198</bbox>, <bbox>757 210 939 280</bbox>, and <bbox>178 714 826 810</bbox>; the parrot is at <bbox>347 305 642 997</bbox>.
```

*Why: the owner's coordinate form, shortened. Each region gets its own box and the subject is named beside its box, so the split follows the measured regions instead of the model's guess*

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

## Seedream 5.5: provisional notes

Everything in this section comes from WaveSpeed's hosted model pages and BytePlus's Lumina preview pages, not from ByteDance documentation. Treat it as provisional and re-verify once ByteDance documents the model.

<rules id="seedream-5-5">

- Write 5.5 prompts the same way as 5.0 Pro prompts. BytePlus says the structure that works on 5.0 Pro applies directly, with no new prompt syntax.
- For a cut-out subject on a transparent background, the transparency itself is a request setting on the host, not prompt text. In the prompt, describe the subject on its own ("isolated") and leave out any scene behind it, or a background may be painted in.
- Edit in small rounds. 5.5 is built to keep unedited areas steady across many rounds, so refine with one change per turn instead of regenerating. Still say what changes and what stays in every edit.
- Hosts can run layer separation as its own request; its optional prompt names the layers, objects, or grouping to split, as on 5.0 Pro.
- BytePlus's preview pages target small text and broader language coverage, naming Thai, Japanese, and Russian. Proofread small type anyway.
- Nothing yet documents whether 5.5 reads drawn marks or coordinate tags. Route marked and coordinate edits to 5.0 Pro or Flash until it does.

</rules>

<example use_case="transparent-sticker">

```text
A cute cartoon fox mascot sticker waving, thick white outline, flat vector style, isolated
```

*Why: a WaveSpeed 5.5 example for transparent output. The subject stands alone with no scene described, so nothing competes with the cut-out once the host's transparent-background setting is on*

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
- Assuming 5.0 behavior on the older tiers: annotation-driven editing, coordinate tags, layer separation, and non-English prompting are 5.0 Pro and Flash capabilities. On 4.5 and 5.0-lite, describe the region in words instead of marking it.
- Expecting pixel-perfect output from 5.0 Pro or Flash: the owner states that fine-grained text rendering and pixel-level editing consistency are still imperfect. Proofread dense small type and inspect the seams of a local edit.
- Marking regions but not pinning the rest: an annotated edit without a closing "keep everything else the exact same" invites drift outside the marked areas.
- Leaving the marks in: ask for sketch lines, boxes, and doodles to be removed, or they can survive into the result.
- Guessed coordinates: write a `<point>` or `<bbox>` only from a measured selection; an estimated box edits the wrong region with full confidence.
- Treating 5.5 as documented: its notes here are provider-sourced, so keep marked and coordinate edits on 5.0 Pro or Flash until ByteDance documents 5.5.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. Seedream 5.0 Pro shipped on 2026-07-08 and 5.0 Flash on 2026-09-15; 5.0-lite remains the separate reasoning and online-search tier. The BytePlus 5.0 tutorial now lists the languages 5.0 Pro and Flash render natively, which settles the earlier provider disagreement over the count. That tutorial runs layer separation as its own request mode with an optional prompt, and the launch blog's plain-text request is kept as a tolerated form for hosts without that mode. Seedream 5.5 is provider-sourced: WaveSpeed hosts it, while ByteDance Seed has no page for it, the ModelArk release list does not include it, and BytePlus Lumina describes it as a preview. The 5.5 notes are provisional until ByteDance documents the model. WaveSpeed's 5.0 Pro page is autogenerated boilerplate that omits the Pro capabilities entirely; it is not a source of model-specific prompt craft.

- Official (ByteDance, BytePlus): [Seedream 5.0 pro / flash tutorial](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro), [Seedream 5.0 pro / flash interactive editing guide](https://docs.byteplus.com/en/docs/modelark/seedream-5-0-pro-editing-guide), [ModelArk model release announcements](https://docs.byteplus.com/en/docs/modelark/model-release-announcement), [Seedream 5.0 Pro model page](https://seed.bytedance.com/en/seedream5_0_pro), [Seedream 5.0 Pro launch blog](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro), [Seedream 4.0-4.5 prompt guide](https://docs.byteplus.com/en/docs/ModelArk/1829186), [Seedream 4.0-5.0 tutorial](https://docs.byteplus.com/en/docs/ModelArk/1824121), [Seedream 5.0-lite model page](https://seed.bytedance.com/en/seedream5_0_lite), [Seedream 4.5 model page](https://seed.bytedance.com/en/seedream4_5), [BytePlus Lumina: what is Seedream 5.5](https://ai.byteplus.com/lumina/en/image/what-is-seedream-5-5) (preview).
- Provider: [WaveSpeed Seedream 5.5](https://wavespeed.ai/models/bytedance/seedream-v5.5), [WaveSpeed Seedream 5.5 edit](https://wavespeed.ai/models/bytedance/seedream-v5.5/edit), [WaveSpeed Seedream 5.5 layer decomposition](https://wavespeed.ai/models/bytedance/seedream-v5.5/layer-decomposition), [fal Seedream 5.0 overview](https://fal.ai/seedream-5.0), [fal Seedream 5.0 Pro edit](https://fal.ai/models/bytedance/seedream/v5/pro/edit), [fal Seedream 4.5 prompt guide](https://fal.ai/learn/devs/seedream-v4-5-prompt-guide), [fal Seedream 5.0-lite prompting guide](https://blog.fal.ai/seedream-5-0-lite-prompting-guide/), [fal how to use Seedream 5.0-lite](https://fal.ai/learn/tools/how-to-use-seedream-5-lite), [WaveSpeed Seedream 4.0 to 5.0 tutorial](https://wavespeed.ai/blog/posts/seedream-4-0-to-5-0-complete-tutorial-image-generation-editing/).

Last verified: 2026-11-08.
