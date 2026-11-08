---
guide: "GPT Image (family)"
prompt_scheme: "gpt-image"
models:
  - { id: "gpt-image-2.6-sunburst", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge, marked-input-editing, animated-gif, vector-output], best_for: "the detail and precision pick and the owner's base model: images that must meet demanding requirements for detail, layout or edit accuracy, with the owner claiming greater consistency across edits at medium or high quality. Adds the planning setting, markup-guided edits, and animated GIF and SVG output. Slower per image than Flare" }
  - { id: "gpt-image-2.6-flare",    access: "closed-weights", tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge, marked-input-editing, animated-gif, vector-output], best_for: "the speed pick and the owner's smaller model: workflows where response time matters most, with layout gains the owner names for posters, product imagery and other professional visuals. Same new features as Sunburst. It buys latency, not a guaranteed lower price" }
  - { id: "gpt-image-2.5-sunburst", access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge], best_for: "the previous quality pick; the owner moves its workflows to 2.6 Sunburst first" }
  - { id: "gpt-image-2.5-flare",    access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge], best_for: "the previous speed pick; the owner moves its workflows to 2.6 Flare first" }
  - { id: "gpt-image-2",      access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge], best_for: "existing validated workflows; the owner files it under earlier models, and it is the baseline to test the 2.6 models against" }
  - { id: "gpt-image-1.5",    access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge], best_for: "existing workflows only; deprecated and scheduled for shutdown" }
  - { id: "gpt-image-1-mini", access: "closed-weights", tier: "budget", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge], best_for: "cost and throughput on low-stakes work: large batch variants, rapid ideation, previews, draft assets. A mini of generation 1, deprecated and scheduled for shutdown" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, world-knowledge, marked-input-editing, animated-gif, vector-output]
prompt:
  languages: ["en", "multilingual"]
  formula: "Scene, then Subject, then Important details, then Use case, then Constraints; short labeled segments with line breaks beat one long paragraph"
  literal_text: "wrap the exact words in quotes or ALL CAPS and give typography as a constraint (font style, size, color, placement); spell tricky words letter by letter"
  length_strategy: "long prompts work, but start from a clean base and refine with small single-change follow-ups; debugging a short prompt is far easier than debugging a long one"
  format_freedom: "prose, labeled segments, JSON-like structures, instruction style and tag lists all parse; pick the one that is easiest to maintain, and give every style word a visual target"
  photorealism: "say 'photorealistic' explicitly, it engages a distinct mode; camera and lens language shapes the look but is not simulated exactly, and polish must be suppressed on purpose"
  negatives: "plain negatives work and go in the prompt ('no watermark', 'no extra text', 'no logos'); there is no separate negative field"
  references: "reference each input by index AND description ('Image 1: product photo, Image 2: style reference'), then state how they interact"
  editing: "'change only X' plus 'keep everything else the same', and repeat the preserve list on every iteration or the edit drifts; a preserve list cannot promise pixel-identical regions, so composite the approved edit into the original when an area must not move at all"
  quality_setting: "a request setting, never words in the prompt; the owner says to set parameters separately from the prompt. Raise it for small or dense text, detailed infographics, close-up portraits, and identity-sensitive edits, and leave it low for high-volume work. The same setting name does not give the same quality on different models"
  transparency: "ask for an isolated subject in the prompt AND set transparency on the request; a checkerboard drawn into the image is not an alpha channel, and the owner's cutout prompt forbids a backdrop, checkerboard, scenery and shadow outright"
  planning_setting: "2.6 models only, a request setting the owner calls complexity, never words in the prompt. It sets how much the model plans the scene before rendering: more helps an open prompt or a crowded scene and adds little to a fully specified design; start focused edits low, since more planning can bring unwanted changes. Fix layout with planning and small-text legibility with quality"
  markup: "2.6 models, on hosts that take a drawn annotation layer: mark the target on the layer, name the mark in the prompt ('the vase inside the red circle'), state the change and what stays, and ask for the mark to be removed from the finished image"
  animation: "for a looping GIF from a 2.6 model, describe the subject, the motion as a few beats, a starting pose it returns to, and whether the camera moves, then ask for a smooth loop; output format and frame settings belong on the request"
  vector_output: "for an SVG from a 2.6 model, prompt exactly as for a raster logo (vector-like shapes, strong silhouette, balanced negative space, flat design, minimal strokes, no gradients unless essential); the format is a request setting"
sources:
  official: ["https://developers.openai.com/api/docs/guides/image-prompting", "https://developers.openai.com/api/docs/guides/image-generation", "https://openai.com/index/introducing-images-2-6/", "https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst", "https://developers.openai.com/api/docs/models/gpt-image-2.6-flare", "https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst", "https://developers.openai.com/api/docs/models/gpt-image-2.5-flare", "https://developers.openai.com/api/docs/models/gpt-image-2", "https://developers.openai.com/api/docs/deprecations", "https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide"]
  provider: ["https://fal.ai/gpt-image-2.6", "https://fal.ai/learn/tools/prompting-gpt-image-2", "https://fal.ai/gpt-image-2.5", "https://wavespeed.ai/blog/ai-models/gpt-image-2-5-flare-and-sunburst-now-on-wavespeedai/"]
  community: []
last_verified: "2026-11-08"
---

# GPT Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, quality and fidelity settings, resolution limits, reference counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the whole GPT Image family, GPT Image 2.6 and 2.5 Sunburst and Flare included. They share one prompt scheme; a prompt written for one transfers to the others, and the owner's migration advice is to keep the prompt, references, size, quality and output format unchanged for the first comparison, leave the planning setting at its default, and retune one setting at a time only after comparing real output. The same prompt still renders differently on each model.
- Keep request settings out of the prompt. Quality, planning depth, output size, output format (SVG and animated GIF included) and background transparency are set on the request, not asked for in words; the owner says to set fields in the request and use the prompt to describe the image. Aspect ratio and placement still belong in the prompt text.
- Write in a consistent order and label the segments. This model rewards a skimmable structure more than it rewards clever phrasing.
- Name the artifact you want (ad, UI mock, infographic, editorial photo). Stating the intended use sets the mode and the level of polish.
- Say what must not change. Constraints and preserve lists are load-bearing here, not decoration, and are where most weak prompts fail silently.
- Plain negatives work. Write them into the prompt; there is no separate negative field.

</rules>

## TL;DR

<template id="quickstart">

{scene and environment}. {Subject and what it is doing}. {Materials, lighting, framing, mood}. {The artifact this is: editorial photo, product mockup, poster, UI screen, infographic}. {What must not appear or must not change}.

</template>

## Models and when to use which

All seven share one prompt scheme; pick by quality requirement, latency and migration state rather than by grammar. The 2.6 models add four things the earlier ones lack: a planning setting, markup-guided edits, animated GIF output and SVG output.

- `gpt-image-2.6-sunburst`: the detail and precision pick, and the owner's base model. Start here when the image must meet demanding requirements for detail, layout, or edit accuracy. The owner's launch post credits it with greater consistency across edits at medium or high quality.
- `gpt-image-2.6-flare`: the speed pick, and the owner's smaller model. Start here when response time matters most. The launch post credits it with better layout quality for posters, product imagery and other professional visuals.
- `gpt-image-2.5-sunburst` and `gpt-image-2.5-flare`: the previous generation. Each moves to its 2.6 counterpart first, Flare to Flare and Sunburst to Sunburst.
- `gpt-image-2`: filed by the owner under earlier models. Keep it for workflows already validated against it, and use it as the baseline when testing the 2.6 models.
- `gpt-image-1.5`: deprecated and scheduled for shutdown. Existing workflows only.
- `gpt-image-1-mini`: the cost and throughput option for large batches, ideation, previews, and draft assets. Deprecated and scheduled for shutdown.
- `gpt-image-1` is shut down. Prompts written for it are a starting point on the current models.

<rules id="model-choice">

- For new work, start on 2.6 Flare when response time matters most and on 2.6 Sunburst when detail, layout or edit accuracy must meet a demanding bar.
- Moving a 2.5 workflow: test the matching 2.6 model first.
- Moving a gpt-image-2 workflow that already meets its quality bar: test 2.6 Flare first. Moving a task where gpt-image-2 falls short: start on 2.6 Sunburst and confirm it clears the bar.
- Once Sunburst meets the bar, try Flare with the same prompts, references, size and quality setting, and switch only if Flare also passes.
- Compare models with the prompt, references, output size, quality setting and output format held fixed, and the planning setting left at its default. The same quality setting name does not produce the same image quality on different models, so a matched label is where a comparison starts rather than a guarantee.
- Retune settings before rewriting the prompt, and change one at a time: quality or planning, not both. The owner's order is to compare settings first.
- Flare is the latency option, not a guaranteed cost saving. The owner says to confirm current pricing rather than assume the faster model costs less.
- `gpt-image-1-mini` is a mini of generation 1, not of any later generation. Read as a list the ids invite the opposite assumption, and it is wrong.
- For cost-sensitive work, prefer a current model at a low quality setting over dropping to mini. The owner reported the low setting performing comparably on gpt-image-2, and it keeps you on a supported model.
- Raise the host's quality control for small or dense text, detailed infographics, close-up portraits, identity-sensitive edits, and large outputs. Leave it low for high-volume exploration.

</rules>

## How the model reads prompts

- Structure beats phrasing. Prompts written in a consistent order, with short labeled segments and line breaks once they run past a short paragraph, outperform the same content as one flowing block.
- It infers the mode from the artifact you name. Say "editorial photograph", "pitch-deck slide", or "mobile app UI mockup" and the model applies that genre's conventions, framing, and polish.
- Format is flexible, unusually so. Minimal prompts, descriptive paragraphs, JSON-like structures, instruction style, and tag lists all parse. The constraint is not syntax; it is that intent and limits must be explicit.
- Style words need visual targets. A pile of adjectives ("minimalist brutalist editorial luxury premium") gives the model nothing; naming a cream background, heavy black condensed sans serif, and generous negative space gives it something to draw.
- It over-polishes by default. Left alone it drifts toward advertising gloss, so believable images are bought partly by naming what to leave out.
- It has real world knowledge. Naming a verifiable time and place hands it the research: a crowd scene in Bethel, New York on August 16, 1969 comes back as Woodstock without the event being mentioned.
- It plans before drawing, and on the 2.6 models how much it plans is a request setting (see Planning depth). It holds identity well across edits, which is what makes multi-step and multi-image workflows practical.
- Iteration beats overloading. Long prompts work, but a clean base plus small single-change follow-ups is far easier to debug.

## Prompt structure

The canonical shape is five slots. Four of them describe the image; the fifth bounds it, and that is the one weak prompts omit.

<rules id="structure">

- Order the prompt scene, then subject, then important details, then use case, then constraints. Put each on its own labeled line once the prompt is more than a short paragraph.
- Scene sets where the image exists: location, time of day, background, environment.
- Subject is what the image is about, and what it is doing.
- Important details carry materials, clothing, texture, lighting, camera angle, lens feel, composition, and mood.
- Use case names the finished artifact. This is not a formality; it is what sets the genre and the polish level.
- Constraints state both exclusions and invariants: no watermark, no extra text, no logos, preserve the face, preserve the layout.
- Be concrete about materials, shapes, textures, and medium. Add quality levers (film grain, textured brushstrokes, macro detail) only where one is doing work.
- For people, describe scale, body framing, gaze, and object interaction: "full body visible, feet included", "child-sized relative to the table", "looking down at the open book, not at the camera", "hands naturally gripping the handlebars".
- For wide, cinematic, low-light, rain, or neon scenes, add extra detail on scale, atmosphere, and color, or the model trades mood for surface realism.

</rules>

<template id="general">

Scene:
{where this happens, time of day, background, environment}

Subject:
{who or what is the main focus, and what they are doing}

Important details:
{materials, clothing, texture, lighting, camera angle, lens feel, composition, mood}

Use case:
{editorial photo, product mockup, poster, UI screen, infographic, concept frame}

Constraints:
{no watermark, no logos, no extra text, preserve face, preserve layout}

</template>

<example use_case="five-slot-structure">

```text
Scene:
A quiet classical museum gallery in soft afternoon light.

Subject:
A woman in her 30s standing casually in front of a large oil painting.

Important details:
Natural smile, realistic skin texture, beige knit sweater, dark jeans, white sneakers, eye-level full-body framing, marble floor reflections, warm neutral color balance, shallow depth of field, believable indoor ambient light.

Use case:
Editorial lifestyle photograph.

Constraints:
No watermark, no logos, no extra people in the foreground, no heavy retouching.
```

*Why: every slot does one job, so any of them can be edited without rewriting the rest, and the constraint block rules out the three things this genre usually attracts*

</example>

## Planning depth

The 2.6 models take a planning setting on the request, which the owner calls complexity. It is separate from quality: quality sets how much visual detail the model can render, and planning sets how much it decides about the scene before rendering. It is not a prompt word, but it changes how much the prompt has to carry.

<rules id="planning">

- Leave the design open and plan more. When the prompt names the scene and the medium but leaves props, costumes and lettering to the model, more planning gives it room to compose.
- Specify fully and the setting matters less. When the prompt already sets the layout, the text and the style, the owner says higher planning may make little visible difference; the prompt has done the planning.
- Crowded scenes, dense text, complex layouts and relationships between objects are where the owner says more planning helps.
- Start focused edits low. More planning can bring changes you did not ask for, and the owner recommends low planning for most edits, paired with whatever quality the work needs. The owner's API defaults to the most planning, so a focused edit that keeps drifting may need the setting lowered, not a longer preserve list.
- Fix layout with planning and small text with quality. When labels land in the wrong place or connected objects come out wrong, compare planning levels with quality held fixed; when the layout is right but small text is hard to read, compare quality levels with planning held fixed.

</rules>

<example use_case="open-prompt-for-planning">

```text
A premium handcrafted layered paper-cut illustration of a football team celebrating a championship victory inside a packed stadium.
```

*Why: the owner's planning comparison prompt. It fixes the scene and the medium and leaves the trophy, the uniforms and the lettering open, and at each planning level the owner's outputs changed exactly those: the trophy decoration, the jerseys, and whether the "CHAMPIONS" sign sat in front of the team or in the stands*

</example>

## Photorealism

<rules id="photoreal">

- Say "photorealistic". The word engages a distinct mode rather than acting as a quality tag. Related levers work too: "real photograph", "taken on a real camera", "professional photography", "iPhone photo".
- Prompt as if a photo is being taken in the moment, not as if an image is being designed.
- Ask for real texture by name: pores, wrinkles, sun damage, fabric wear, chipped paint, scuffs, imperfections.
- Camera language shapes the look, it does not simulate optics. A lens, body, or film stock steers framing and character, but exact specs are interpreted loosely, so do not expect physical accuracy from them.
- Suppress polish explicitly. "No glamorization, no heavy retouching", "avoid cinematic lighting, dramatic color grading, or stylized composition", "not an overly enhanced movie-poster image". Without this the model drifts to advertising gloss.
- Avoid words that imply staging or studio production unless that is what you want.

</rules>

<example use_case="photoreal-flagship">

```text
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat. He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms. He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens. Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance. The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
```

*Why: a long flagship that leads with the mode word, names texture at the pore level, uses camera language for character rather than simulation, and closes by suppressing the polish the model would otherwise add*

</example>

<example use_case="world-knowledge">

```text
Create a realistic outdoor crowd scene in Bethel, New York on August 16, 1969. Photorealistic, period-accurate clothing, staging, and environment.
```

*Why: a verifiable date and place hands the model the research; it infers the event and supplies period detail that would take a paragraph to specify*

</example>

## Text in images

<rules id="text">

- Put literal text in quotes or ALL CAPS, and give typography as a constraint: font style, weight, size, color, placement.
- Say how many times the text should appear. "Render the tagline exactly once" prevents duplicate copies in the layout.
- For brand names and uncommon spellings, spell the word out letter by letter to improve character accuracy.
- Mark exactness when it matters: "EXACT, verbatim, no extra characters".
- Rule out stray lettering in the constraints, since layouts attract invented captions: "no extra text, no watermarks, no unrelated logos".
- Raise the host's quality control for small text, dense information panels, and multi-font layouts.

</rules>

<example use_case="marketing-text">

```text
Create a realistic billboard mockup of the shampoo bottle on a highway scene during sunset.
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
Typography: bold sans-serif, high contrast, centered, clean kerning.
Ensure text appears once and is perfectly legible.
No watermarks, no logos.
```

*Why: the copy is isolated on its own line under an exactness marker, typography is given as a constraint rather than a description, and the count is pinned so the phrase is not repeated across the board*

</example>

<example use_case="in-image-translation">

```text
Translate the text in the infographic to Spanish. Do not change any other aspect of the image.
```

*Why: localization works as a surgical edit, so the whole instruction is the change plus a total preserve clause; keeping typography, spacing, and hierarchy is left to the invariant rather than re-specified. Check the result for words left in the original language*

</example>

## Structured visuals

Infographics, slides, diagrams, and interface mockups are a strength. Name the artifact, then the audience, then the content, then the layout rules.

<rules id="structured">

- Name the artifact and the audience: "a biology diagram for high school students", "a Series A pitch-deck slide". Both shift the register.
- List the elements the image must contain as a bulleted or line-separated inventory rather than a sentence.
- Give real values. Believable specifics (figures, labels, footnotes) render better than placeholders and stop the model inventing filler. Then check every figure in the output: the owner warns its own slide example can come back with extra percentages nobody asked for.
- State the layout as constraints: background, typography family, spacing, where the logo or footnote sits.
- Rule out decoration explicitly. "Avoid clip art, stock photography, gradients, shadows, decorative elements" is what separates a usable slide from a generic one.
- For multi-panel work, label the panels and give each one its own line. For a comic strip, make each panel one clear visual beat, concrete and action-focused.
- Describe an interface as if the product already exists: layout, hierarchy, spacing and real interface elements. Concept-art language turns it back into a design sketch.
- Write educational visuals like an instructional design brief: the audience, the lesson objective, the components that must appear, and what to leave out.

</rules>

<example use_case="pitch-deck-slide">

```text
Create one pitch-deck slide titled "Market Opportunity" that feels like a real Series A fundraising slide from a YC-backed startup. Use a clean white background, modern sans-serif typography like Inter, and a crisp, minimal layout. The slide should include:
- A TAM/SAM/SOM concentric-circle diagram in muted blues and grays
- Market sizing figures: TAM $42B, SAM $8.7B, SOM $340M
- A clean bar chart below showing market growth from 2021 to 2026, with a subtle upward trend
- Small footnotes reading "AGI Research, 2024" and "Internal analysis"
- A company logo placeholder in the bottom-right corner
Highly readable text, clear data hierarchy, polished spacing. Avoid clip art, stock photography, gradients, shadows, or anything that feels generic.
```

*Why: names the genre precisely enough to import its visual language, gives every element real values instead of placeholders, and closes with an exclusion list that is what actually keeps the slide from looking generated*

</example>

<example use_case="labeled-diagram">

```text
Create a simple biology diagram titled "Cellular Respiration at a Glance" for high school students. Show how glucose turns into energy inside a cell, including glycolysis, the Krebs cycle, and the electron transport chain. Use arrows to connect the steps, and label the main molecules: glucose, pyruvate, ATP, NADH, FADH2, CO2, O2, and H2O. Make it look like a clean classroom handout, with a white background, simple icons, clear labels, and easy-to-read text. Avoid tiny text, extra decoration, or anything that makes the diagram hard to understand.
```

*Why: the audience sets the complexity level, every label is enumerated so none are invented, and the closing exclusion targets the specific failure mode of diagrams, which is unreadable small type*

</example>

<example use_case="ui-mockup">

```text
Create a realistic mobile app UI mockup for a local farmers market.
Show today's market with a simple header, a short list of vendors with small photos and categories, a small "Today's specials" section, and basic information for location and hours.
Design it to be practical, and easy to use. White background, subtle natural accent colors, clear typography, and minimal decoration.
It should look like a real, well-designed, beautiful app for a small local market.
Place the UI mockup in an iPhone frame.
```

*Why: names each screen region in reading order, quotes the one literal section heading, states the device frame, and asks for a real, shipped app rather than a concept, which keeps the result from reading as a design sketch*

</example>

## Logos and SVG output

<rules id="logo">

- Describe the brand, then the shapes that define the mark, and ask for a silhouette that stays recognizable on a small label and a large sign.
- Ask for vector construction in words: clean vector-like shapes, a strong silhouette, balanced negative space, flat design, minimal strokes, no gradients unless essential.
- Ask for an original, non-infringing mark.
- For a mark that will sit on other backgrounds, ask for a fully transparent background with clean edges and forbid the fakes (solid backdrop, scenery, checkerboard), and set transparency on the request as well.
- SVG is an output format set on the request, available from the 2.6 models when generating, not when editing. The prompt does not change for it: the owner sends the same logo prompt for SVG and for raster output.

</rules>

<example use_case="reusable-logo">

```text
Create an original, non-infringing logo for a company called Field & Flour, a local bakery.
The logo should feel warm, simple, and timeless. Use clean, vector-like shapes, a strong silhouette, and balanced negative space.
Favor simplicity over detail so it reads clearly at small and large sizes. Flat design, minimal strokes, no gradients unless essential.
Fully transparent background. Deliver a single centered logo with generous padding, clean alpha edges, and no solid backdrop, scenery, checkerboard, or watermark.
```

*Why: the owner's logo prompt, used unchanged for both its SVG and its transparent raster versions. Brand and mood come first, the construction is described in vector terms, the scale requirement is stated as a reason to stay simple, and the closing line names every fake substitute for transparency*

</example>

## Multiple reference images

<rules id="multi-image">

- Reference each input by index and description, not by index alone: "Image 1: product photo. Image 2: style reference." The description is what stops the roles being swapped.
- One role per input. Give each image exactly one job and weld every borrowed element to its source.
- State how the inputs interact: "apply Image 2's style to Image 1", "put the bird from Image 1 on the elephant in Image 2".
- Name what moves, pin what stays. Say which element comes from which image, then state what must remain identical, or identity, lighting, and background drift.
- Ask for integration explicitly: match lighting, shadow direction, color temperature, and perspective so the composite reads as one photograph.

</rules>

<example use_case="composite-two-inputs">

```text
Place the dog from the second image into the setting of image 1, right next to the woman, using the same style of lighting, composition, and background. Do not change anything else.
```

*Why: one role per input, the destination is stated precisely rather than left to the model, and the lighting match plus the blanket preserve keep the insertion from re-rendering the scene*

</example>

<example use_case="multi-source-composite">

```text
Image 1: a photo of a woman standing outdoors. Image 2: a green wool coat on a plain background. Image 3: a rainy city street at dusk.
Place the woman from Image 1 on the street from Image 3, wearing the coat from Image 2. Preserve her face, hairstyle, and body proportions exactly, and preserve the coat's color and weave. Relight her to match the street's ambient light and wet reflections, and match shadow direction and color temperature so the result reads as one photograph. No watermark, no extra people.
```

*Why: three inputs declared as an indexed manifest before any instruction, each welded to one role, with the invariants named per source and an explicit relight so the composite fuses instead of looking pasted*

</example>

## Image editing

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Replace, Redraw, Restore) or the constraint (Keep), but the opening clause must instruct rather than describe. A declarative setup such as "Image 1 provides the foundation, Image 2 provides the face" states the plan instead of issuing it and pushes the real instruction back by a sentence or two.
- Separate the change from the preserve. "Change only X" plus "keep everything else the same" is the core pattern.
- Repeat the preserve list on every iteration. Dropping it once is enough for the model to start drifting on faces, logos, or text.
- For surgical edits, extend the preserve list to the things that silently shift: saturation, contrast, layout, arrows, labels, camera angle, framing, and surrounding objects.
- Make one change per turn. A sequence of small edits outperforms one instruction carrying several.
- Name the outcome plainly. "Remove the flower from the man's hand" is enough; describing the removal procedure is not needed.
- For identity-sensitive work, list the identity attributes explicitly rather than saying "keep her the same".
- A preserve list cannot promise pixel-identical regions. Repeated edits can still move details you asked to keep, so when an area must not change at all, composite the approved edit back into the original instead.
- For a transparent cutout, ask for an isolated subject in the prompt and set transparency on the request as well. Forbid the fake versions outright (no backdrop, no checkerboard, no scenery, no shadow), and repeat the transparency requirement on every later edit.

</rules>

<example use_case="object-removal">

```text
Remove the flower from the man's hand. Do not change anything else.
```

*Why: the whole instruction is one change and one blanket invariant, which is the shortest form that still bounds the edit*

</example>

<example use_case="precision-swap">

```text
In this room photo, replace only the white chairs with chairs made of wood. Preserve camera angle, room lighting, floor shadows, and surrounding objects. Keep all other aspects of the image unchanged. Photorealistic contact shadows and fabric texture.
```

*Why: "replace only" scopes the swap, the preserve list names the four things that drift in interior edits specifically, and the closing texture note keeps the replacement physically grounded*

</example>

<example use_case="identity-preserving-edit">

```text
Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

*Why: the preserve list is enumerated attribute by attribute rather than summarized, which is what holds identity through a garment swap, and the integration clause stops the clothing reading as a cutout*

</example>

<example use_case="style-transfer">

```text
Use the same style from the input image and generate a man riding a motorcycle on a white background.
```

*Why: a pure style transfer takes only the look from the input and lets the subject be stated fresh, so nothing from the reference's content carries over*

</example>

<example use_case="style-transfer-plus-edit">

```text
Image 1: a photograph of a harbor at dawn. Image 2: a loose ink-and-wash painting.
Redraw Image 1 in the ink-and-wash style of Image 2, and add a small wooden fishing boat in the mid-ground rendered in that same style. Preserve Image 1's composition, horizon line, and the position of the existing buildings. No text, no watermark.
```

*Why: applies a style from one input to content from another while folding in a new element in the target style, with the composition pinned so only the look and the added boat change*

</example>

<example use_case="drawing-to-render">

```text
Turn this drawing into a photorealistic image. Preserve the exact layout, proportions, and perspective. Choose realistic materials and lighting consistent with the sketch intent. Do not add new elements or text.
```

*Why: names the target medium, pins the three geometric properties a render usually distorts, and delegates only material and lighting choice while forbidding invention*

</example>

<example use_case="transparent-cutout">

```text
Extract the product from the input image and isolate it on a fully transparent background.
Output: centered product, crisp silhouette, no halos/fringing.
Preserve product geometry and label legibility exactly.
Add only light polishing. Do not add a solid backdrop, checkerboard, scenery, or shadow.
Do not restyle the product; remove the background and preserve clean alpha transparency.
```

*Why: the owner's cutout prompt. It asks for isolation and names every fake substitute for transparency as an exclusion, because a drawn checkerboard or backdrop is the failure; it works only alongside transparency set on the request*

</example>

## Markup-guided edits

The 2.6 models can take a drawn annotation layer with an edit, on hosts that accept one. The drawing shows where the edit lands; the prompt says what changes.

<rules id="markup">

- Draw on the layer to point at the target: a circle around the object, a rough sketch of a shape. Keep the drawing on its own layer rather than painting it into the photo.
- Name the mark in the prompt by its color and shape, "the striped vase inside the red circle", so the words and the drawing point at the same thing.
- The mark locates the edit; it does not bound it. Still say what stays (the object's own shape, the things beside it, the rest of the scene), and compare the rest of the result with the original for changes you did not ask for.
- Ask for the mark to be removed from the finished image.
- The markup belongs to the first input image. Put the image being edited first; any further inputs are references.
- Use markup or a mask to locate an edit, not both. Where the host has no markup input, locate the edit in words, as in the rest of this guide.

</rules>

<example use_case="markup-edit">

```text
Recolor the striped vase inside the red circle to solid cobalt blue ceramic. Keep its shape, the dried stems, and the rest of the kitchen unchanged. Remove the red circle from the finished photo.
```

*Why: the owner's markup example. The target is named by the mark around it, the preserve clause covers the object's own shape as well as its surroundings, and the last sentence stops the circle being rendered into the result*

</example>

## Character consistency

<rules id="consistency">

- Establish the character once in a labeled block: appearance, clothing, palette, proportions, and personality.
- Reuse that block verbatim in every later prompt, under a "Character consistency" heading, and change only the scene.
- Feed prior outputs back in as reference images rather than relying on description alone.
- Re-specify any attribute that starts to drift instead of adding a general instruction to stay consistent.

</rules>

<example use_case="character-consistency">

```text
Continue the children's book story using the same character.

Scene:
The same young forest hero is gently helping a frightened squirrel out of a fallen tree after a winter storm. The character kneels beside the squirrel, offering reassurance.

Character consistency:
- Same green hooded tunic and soft brown boots
- Same facial features, proportions, and color palette
- Same gentle, heroic personality

Style:
Children's book illustration, hand-painted watercolor look, soft outlines, warm earthy colors.

Constraints:
Original character, no text, no watermarks.
```

*Why: the scene is the only slot that changed; the consistency block is carried across verbatim as an explicit checklist, which is what holds a character across a sequence*

</example>

## Animated GIFs

The 2.6 models can return a looping GIF. The output format and the frame settings are set on the request; the prompt describes the subject, the motion and the loop, which are the three things the owner names.

<rules id="animation">

- Write the motion as a short run of beats ("slowly lifts it, looks up and blinks, then lowers it"), and give the subject a starting pose to return to. Returning to the start is what closes the loop.
- Say whether the camera moves. The owner's loop keeps it still and says so.
- Pin what must hold across frames: props in hand, outfit, setting. "Keep the lantern in its hands."
- Ask for the loop in words: "Make the motion loop smoothly."
- Size the action to a short loop. The owner's example carries one gesture in a few beats, not a story.
- To animate an existing picture (a sketch, a mascot, a product shot), send it as the input image and describe the motion; the image carries the look.
- The launch post also shows a partner's sprite-sheet prompts: one still image holding a fixed grid of sequential frames, assembled into a GIF outside the model. That is a still-image technique. Use it only where the output is a still that something else will slice; on a host that returns a GIF, write the motion as above.

</rules>

<example use_case="looping-gif">

```text
A little monkey in an olive-green hooded coat stands in a snowy pine forest at dusk. A wooden cabin glows in the background. The monkey holds a glowing amber paper lantern at chest height, slowly lifts it, looks up and blinks, then lowers it back to its starting pose. Keep the lantern in its hands and the camera still. Make the motion loop smoothly.
```

*Why: the owner's GIF prompt. The scene is set once, the motion runs as three beats that end on the starting pose, the held prop and the camera are both pinned, and the loop is asked for by name*

</example>

<example use_case="sprite-sheet-variant">

```text
Create a single animation sprite sheet for a seamless looping GIF. A super-cute chibi adult office worker sits at a desk watching a computer monitor with a clearly plunging stock-market line chart. The sequence: hopeful expression, notices the chart falling, eyes widen, face crumples, large cartoon tears stream down both cheeks, then quietly wipes tears while still staring at the falling chart. Oversized round head, tiny body, big expressive eyes, soft rounded features, messy fluffy hair, white shirt and loosened tie. Exactly 6 sequential frames arranged in a precise 3-column by 2-row grid, read left-to-right then top-to-bottom. Every panel has identical dimensions. Fixed front three-quarter camera, same character, same desk, monitor, outfit, and cozy miniature office background. Clear incremental facial and tear motion; sixth frame transitions smoothly toward the first. Polished kawaii chibi 3D toy-like style, warm pastel lighting, funny and sympathetic mood. No captions, no words, no numbers, no logos, no speech bubbles, no panel labels, no borders, no gutters.
```

*Why: a partner prompt from the owner's launch post, and the still-image variant rather than the GIF form. It states the grid and the reading order, makes every panel the same size, fixes the camera and the character, has the last frame lead back to the first, and forbids the borders, gutters and labels that would break the slicing*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field. Plain negatives belong in the prompt and work as written.
- Keep them concrete and grouped in the constraints slot: "no watermark", "no extra text", "no logos or trademarks", "no extra people in the foreground", "no heavy retouching".
- Pair an exclusion with the invariant it protects when both matter: "do not add accessories, text, logos, or watermarks" alongside "preserve her exact likeness".
- Exclude the genre's usual failure, not generic badness. For slides that means clip art and gradients; for diagrams, tiny text; for photoreal, retouching and cinematic grading.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Vague praise: "stunning", "epic", "masterpiece", "insane detail" render as nothing. Replace with visual facts (overcast daylight, brushed aluminum, chipped paint, clean kerning).
- Bare style-tag piles: tags parse here, but a stack of adjectives with no visual target underperforms. Give every style word something concrete to point at.
- Omitting the constraints slot: this is the quiet failure. An unbounded description lets the model get inventive in directions you will regret.
- Dropping the preserve list mid-sequence: repeat it on every iteration or faces, logos, and text drift.
- Stacking edits: one instruction carrying several changes underperforms the same changes across several turns.
- Expecting camera specs to simulate optics: lens and body names steer the look, not the physics.
- Forgetting to suppress polish: photoreal prompts need explicit anti-retouching, or the output drifts to advertising gloss.
- Placeholder data in structured visuals: real, believable figures and labels render better than "Lorem" or "Value 1".
- Unspecified text count: say the copy appears once, or it may be repeated across the layout.
- Reaching for mini to save cost: it is a deprecated generation-1 model; prefer a current model at a low quality setting, which the owner reported performing comparably on gpt-image-2.
- Asking for settings in words: output size, quality and transparency are request settings, and writing them into the prompt does not set them.
- Painting transparency: a checkerboard in the image is not an alpha channel; ask for an isolated subject and set transparency on the request.
- Trusting a preserve list for pixel-exact regions: repeated edits still drift; composite the approved edit into the original instead.
- Judging models at a shared quality label: the same setting name is not the same quality on Flare, Sunburst and gpt-image-2; hold prompt, references and size fixed and compare the images.
- Fighting a drifting edit with words alone: on the 2.6 models, lower the planning setting first; more planning can bring changes nobody asked for.
- Raising planning to fix small text: planning moves layout, and small-text legibility is a quality question.
- Leaving the markup in: ask for the mark to be removed from the finished image.
- Sending a sprite-sheet prompt to a host that returns a GIF: describe the motion and the loop instead; the grid form is for still output that gets sliced afterwards.
- Trusting generated figures: check every number and label in a chart or slide, including ones the model added.

</rules>

## Sources

Trust order: official beats provider beats community. Official (OpenAI) wins on any conflict.

- Official (OpenAI): the [image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting), the owner's current prompting surface for the family, with tabs for 2.6 and 2.5, and the source of the Flare and Sunburst positioning, the model-selection and migration order, the settings-apart-from-the-prompt rule, the planning comparison, the markup, GIF and logo prompts, the interface, comic and educational techniques, the transparent-cutout prompt and the compositing advice for pixel-identical regions; the [image generation guide](https://developers.openai.com/api/docs/guides/image-generation) for what the planning setting changes, the markup layer rules and the SVG and GIF output notes; the [Images 2.6 launch post](https://openai.com/index/introducing-images-2-6/) for the planning advice on edits, the per-model claims and the partner sprite-sheet prompts; the model pages for [GPT Image 2.6 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.6-sunburst), [GPT Image 2.6 Flare](https://developers.openai.com/api/docs/models/gpt-image-2.6-flare), [GPT Image 2.5 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst), [GPT Image 2.5 Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) and [GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2); the [deprecations page](https://developers.openai.com/api/docs/deprecations) for the models scheduled for shutdown and the gpt-image-1 shutdown; the [GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide), which the owner pins as the GPT Image 2 notebook and which remains the source of the rules written against that generation.
- Provider: the [fal GPT Image 2.6 page](https://fal.ai/gpt-image-2.6), the [fal GPT Image 2 prompting guide](https://fal.ai/learn/tools/prompting-gpt-image-2), the [fal GPT Image 2.5 page](https://fal.ai/gpt-image-2.5), and the [WaveSpeed GPT Image 2.5 API guide](https://wavespeed.ai/blog/ai-models/gpt-image-2-5-flare-and-sunburst-now-on-wavespeedai/).

Coverage note: the owner's prompting guide is family-level and says it covers techniques shared across models, which is why each Sunburst and Flare generation joins this guide rather than getting its own. The providers agree with the owner on every prompting point but two. fal's GPT Image 2.6 examples pack several numbered changes into one edit, against the owner's one change per turn; this guide keeps the owner's rule. fal also labels the planning setting "reasoning effort" where the owner says complexity; it is the same control. Earlier, fal repeated a launch claim that 2.5 Flare beat gpt-image-2 on image quality where the owner's API guide said comparable, and this guide followed the API guide. fal's GPT Image 2 guide contributes the five-slot template used here, which makes the owner's "name the intended use" instruction a named slot. One rule inverts the rest of this guide set: tag-based prompts are explicitly accepted by the owner for this family, subject to every style word having a visual target. Structure and scope decisions are recorded in `sources/gpt-image-2/gpt-image-notation-resolution.md`.

Last verified: 2026-11-08.
