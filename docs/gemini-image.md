---
guide: "Gemini Image (Nano Banana)"
prompt_scheme: "gemini-image"
# Google's family name is "Gemini Image"; "Nano Banana" is the widely used product nickname.
models:
  - { id: "gemini-3-pro-image",          name: "Gemini 3 Pro Image",          alias: "Nano Banana Pro",    access: "closed-weights", tier: "flagship",   caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding], best_for: "print-ready assets, long legible multilingual text and logos, factual diagrams, brand consistency; reasons by default; many references with several consistent characters" }
  - { id: "gemini-3.1-flash-image",      name: "Gemini 3.1 Flash Image",      alias: "Nano Banana 2",      access: "closed-weights", tier: "distilled",  caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding], best_for: "the generalist default for most work and high volume; tunable reasoning; strongest multi-reference handling; adds image-search grounding and video references" }
  - { id: "gemini-3.1-flash-lite-image", name: "Gemini 3.1 Flash Lite Image", alias: "Nano Banana 2 Lite", access: "closed-weights", tier: "budget",     caps: [text-to-image, image-edit, text-rendering], best_for: "speed and scale at the lowest cost; keeps prompt adherence, character consistency and legible text, but is not built for many references or long edit chains" }
  - { id: "gemini-2.5-flash-image",      name: "Gemini 2.5 Flash Image",      alias: "Nano Banana",        access: "closed-weights", tier: "legacy",     caps: [text-to-image, image-edit, multi-image-fusion, text-rendering], best_for: "the original model, now superseded; Google recommends moving to Gemini 3.1 Flash Lite Image" }
capabilities: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding]
prompt:
  languages: ["en", "zh-CN", "ja-JP", "ko-KR", "ar", "hi-IN", "es", "fr", "de", "pt-BR", "ru", "vi-VN", "id-ID", "it-IT"]
  formula: "strong verb first (the operation), then Subject, Composition, Action, Location, Style; describe a scene in plain sentences, never a keyword list"
  literal_text: "put the exact words in quotes; give each text element its own font, size, and placement; for exact copy, settle the wording in conversation first, then ask for the image"
  length_strategy: "1-3 vivid sentences for a simple shot; longer with explicit layout for text-heavy posters and infographics; very long prompts make the model deprioritize some elements"
  auto_expand_behavior: "none; the Gemini 3 image models reason over the prompt (a thinking step) before drawing but do not silently rewrite it, so state the full intent yourself"
  negatives: "no negative field; use semantic negatives (describe the desired absence positively, e.g. 'an empty street with no traffic')"
  references: "name each input positionally (the dress in the first image, the woman in the second) and give each one a single role; weld every borrowed element to its source"
  grounding: "ask the model to 'use search' for real-time or factual content (weather, sports, recipes); Gemini 3.1 Flash Image can also 'use image search' for visual references but cannot search for people; Flash Lite has neither"
sources:
  official: ["https://ai.google.dev/gemini-api/docs/image-generation", "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana", "https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/", "https://blog.google/technology/ai/nano-banana-pro/", "https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/", "https://deepmind.google/models/gemini-image/pro/", "https://deepmind.google/models/gemini-image/flash-lite/", "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/"]
  provider: ["https://fal.ai/learn/tools/how-to-use-nano-banana-2", "https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026/"]
  community: []
last_verified: "2026-08-07"
---

# Gemini Image (Nano Banana): prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and reference limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the whole Gemini Image family. They share one prompt scheme; the differences are capability, not grammar. See Model names and aliases below for the full line-up, and Models and when to use which for the choice between them.
- Write one continuous natural-language description that directs a scene. Do not list keywords, weighted tokens, or quality-boosters ("masterpiece, 8k, trending on ArtStation" do nothing here and can hurt).
- Start every prompt with a strong verb naming the operation: Create, Generate, Add, Remove, Replace, Transform, Translate, Relight, Focus on.
- There is no JSON or structured-field prompting in this scheme. Natural language is the whole interface.
- Iterate conversationally: make one change per follow-up turn and keep prior images in the thread to hold consistency.

</rules>

## Model names and aliases

Google ships every generative-media model under two names, and the nickname carries less information than the official name. Prefer the Gemini name and translate the nickname on sight.

| Gemini name (preferred) | Gemini API model ID | Nickname | Line | Role |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro Image | `gemini-3-pro-image` | Nano Banana Pro | Pro | Top tier: highest world knowledge, brand consistency, precision control |
| Gemini 3.1 Flash Image | `gemini-3.1-flash-image` | Nano Banana 2 | Flash | Generalist default; best multi-reference handling and consistency |
| Gemini 3.1 Flash Lite Image | `gemini-3.1-flash-lite-image` | Nano Banana 2 Lite | Flash Lite | Speed and scale; not built for many references or long edit chains |
| Gemini 2.5 Flash Image | `gemini-2.5-flash-image` | Nano Banana | Flash (legacy) | Superseded; Google recommends moving to Gemini 3.1 Flash Lite Image |
| Gemini Omni Flash | `gemini-omni-flash-preview` | none | Omni | Video output with native audio; a different prompt scheme with its own guide |

<rules id="naming">

- Translate the nickname to the Gemini name before deciding anything. The Gemini name states the generation and the tier separately; the nickname collapses them and drops one.
- "Nano Banana 2" is not the successor to "Nano Banana Pro". The 2 counts generations on the Flash line, so Nano Banana 2 is a newer generation than Nano Banana Pro while sitting below it in tier. Pro is still the strongest model.
- Cloud and Vertex surfaces append `-preview` to the same models (`gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview`). Same weights, different surface.
- Hosts invent tier labels that do not exist upstream. Names like Ultra or Multi on a hosted variant describe that host's packaging, not a Google model, and they change nothing about how the prompt is written.
- The same model often appears twice on one host, once under its nickname and once under its Gemini ID. Same weights.
- The image models and Gemini Omni are different prompt schemes with separate guides. Check which one you are in before applying a rule from memory.
- Imagen and Veo are separate Google models on separate prompt schemes, and neither belongs to this family.

</rules>

## TL;DR

<template id="quickstart">

{strong verb} a {subject with concrete attributes} {action or pose}, in {location and setting}, {composition and camera cue}, {lighting}, {style}. For in-image words: include the text "{exact words}" in a {font description} at {placement}. {Orientation or aspect ratio if it matters.}

</template>

## Models and when to use which

All four share one prompt scheme; a prompt written for one transfers to the others. Pick by job.

- Gemini 3 Pro Image: the flagship for finished, print-ready assets. Best-in-class legible long-form and multilingual text, logos, and factual diagrams. Reasons by default before drawing, can use Google Search grounding, and combines many references while keeping several characters consistent. Reach for it for posters, infographics, and brand work.
- Gemini 3.1 Flash Image: the generalist default for most work and high volume. Its reasoning effort is tunable, it handles multiple references and consistency best of the Flash line, and it uniquely accepts image-search grounding and video references (see Reasoning and grounding).
- Gemini 3.1 Flash Lite Image: the speed and scale option, for near-real-time and high-throughput pipelines. It keeps prompt adherence, character consistency, and legible in-image text, but has no reasoning step and no image search, and it is not optimized for many reference inputs or long multi-turn edit chains. Write self-contained prompts for it and keep edit sequences short.
- Gemini 2.5 Flash Image: the original model, now legacy. Google recommends moving to Gemini 3.1 Flash Lite Image, which is faster, cheaper, and better. Keep it only for existing pipelines pinned to it.

The one asymmetry worth planning around: a prompt built on reasoning, search grounding, or a long reference stack degrades on Flash Lite rather than failing loudly. When moving work down to Lite, drop the grounding instruction and cut the reference count rather than trimming the description.

## How the model reads prompts

It is a multimodal language model, not a keyword or CLIP matcher, so it understands creative intent holistically. Plain descriptive sentences win; tag lists, weighted token syntax, and quality-boosters do not help and sometimes hurt. It rewards detail and stated purpose: "a logo for a high-end, minimalist skincare brand" beats "a logo."

On the Gemini 3 image models the model reasons before it draws, planning the composition (and on complex prompts sketching interim thought-images) rather than pattern-matching. That reasoning is on by default for Gemini 3 Pro Image and tunable on Gemini 3.1 Flash Image; Gemini 3.1 Flash Lite Image has none. Combined with broad world knowledge and optional search grounding, this lets you hand it intent and facts, not just visual nouns.

The model is conversational by design. The most reliable workflow is to generate, then refine across turns, feeding prior outputs back in. It does not silently expand a short prompt, so write the full intent yourself.

## Prompt structure

<rules id="structure">

- Lead with the operation verb, then follow Google's element order: Subject, Composition, Action, Location, Style.
- Name materials and specifics, not generic nouns ("navy blue tweed", not "jacket"; "matte black ceramic mug", not "cup").
- Use photographic and cinematic language to control the look: lens (85mm, macro, wide-angle), angle (low-angle, aerial, eye-level), depth of field (shallow, f/1.8, bokeh), lighting (golden hour, three-point softbox, chiaroscuro), and film or camera character (1970s film stock, Fujifilm color, GoPro).
- Length: 1-3 vivid sentences for a simple shot; expand with explicit layout only for text-heavy or multi-element work. Very long prompts cause the model to deprioritize details, so spend words on what matters.
- State aspect ratio in plain words when it matters ("vertical 9:16 poster", "cinematic 21:9", "square image").

</rules>

<template id="general">

{Verb} a {style or medium} {shot type} of {subject with concrete attributes}, {action or expression}. Set in {location and time of day}, {key background elements}. {Composition, camera angle, lens, depth of field}. {Lighting and mood}. {Color or film character}. {In-image text, if any, quoted with font and placement.} {Orientation or aspect ratio.}

</template>

<example use_case="flagship-full-formula">

```text
Create a cinematic wide-angle photograph of an elderly Lisbon tram conductor leaning from the open door of a vintage yellow tram, mid-laugh, one hand resting on the brass rail. Set it on a steep cobbled street at golden hour, with pastel azulejo facades receding into soft bokeh behind him. Compose it as a low-angle three-quarter shot on an 85mm lens with shallow depth of field, warm rim light catching the steam from a paper coffee cup. Render it in the style of analog reportage photography on slightly grainy 1970s color film. On the tram's destination board, show the text "28 GRACA" in a worn cream serif. Horizontal 16:9.
```

*Why: it opens with a strong verb, then walks Subject, Action, Location, Composition and camera, then Style, names a film stock and lens instead of "vintage", and quotes the exact board text with a described font, so the whole intent arrives in one narrative pass.*

</example>

## Text rendering

<rules id="text">

- Put the literal words in quotes, exactly as they should appear: the text "GRAND OPENING".
- Give each distinct text element its own quoted string plus its own font, weight, size, and placement ("the title 'BERLIN' in bold blue serif at the top-center; the date in small text in the corner").
- Describe fonts in words (clean bold sans-serif, condensed serif, brush script); name a real typeface only as a style hint.
- Keep to a few short text elements; large, short text renders far more reliably than dense paragraphs or tiny captions. For pixel-exact copy, generate the layout, then overlay the final text yourself.
- For exact wording, settle the copy in conversation first, then ask for the image that contains it.
- For non-Latin scripts, name the language ("... in Korean"). The model renders many languages and can translate text already inside an image.
- Suppress unwanted lettering with "No other text." Gemini 3 Pro Image is the strongest for long, legible, multilingual text and logos.

</rules>

<example use_case="poster-typography">

```text
Generate a vertical 9:16 gig poster for a jazz night. Across the top, the words "MIDNIGHT BRASS" in a tall condensed serif, ink-black on warm cream. Centered below, a lone saxophonist silhouetted in an amber spotlight with drifting smoke. Near the bottom, "JUNE 14-16" in small caps and "BROOKLYN ARTS CENTER" in a thin sans-serif. Deep navy and gold palette, subtle film grain. No other text.
```

*Why: each text element is separately quoted with its own font, weight, and position, the layout is described top to bottom, and "No other text" stops the model inventing extra captions.*

</example>

<example use_case="in-image-translation">

```text
Using the provided product photo, translate all the English text on the three cans into Japanese, keeping the layout, colors, logo, and everything else exactly the same.
```

*Why: a localization edit that pins every invariant ("everything else exactly the same"), so only the language of the existing lettering changes.*

</example>

## By use-case

<template id="product">

A studio product photograph of a {material and color} {object} on a {surface}, {lighting setup}, shot from a {camera angle} on a {lens} with {focus or depth of field}, {background}. {Aspect ratio.}

</template>

<example use_case="product-mockup">

```text
A high-resolution studio product photograph of a matte black ceramic pour-over coffee dripper on a polished concrete slab. Three-point softbox lighting for soft, even highlights, shot from a slightly elevated 45-degree angle on a 50mm lens with sharp focus on the spout. Neutral background fading to charcoal. Square image.
```

*Why: it specifies material, lighting rig, angle, lens, and focus the way a product photographer would brief a shoot, which is what the model rewards for clean commercial output.*

</example>

<example use_case="sticker-icon">

```text
A kawaii die-cut sticker of a round red panda in a tiny chef's hat holding a dumpling, with bold clean outlines, simple cel-shading, and a vibrant palette, on a plain white background.
```

*Why: stickers and icons need an explicit white background because transparent backgrounds are not supported, and the style words (die-cut, cel-shading, bold outlines) pin the look.*

</example>

<example use_case="infographic-diagram">

```text
Create a clear, accurate infographic explaining how a four-stroke engine works, laid out as four labeled panels (intake, compression, power, exhaust), each with a simple cross-section diagram and a short caption beneath it in a clean sans-serif. Flat editorial illustration style, muted primary palette. Make the mechanical details and labels technically correct.
```

*Why: it leans on the model's world knowledge for a factual diagram, fixes the panel layout and caption font, and demands technical accuracy, which you should still verify against a real source.*

</example>

## Image editing

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Replace, Redraw, Restore) or the constraint (Keep), but the opening clause must instruct rather than describe. A declarative setup such as "Image 1 provides the foundation, Image 2 provides the face" states the plan instead of issuing it and pushes the real instruction back by a sentence or two.
- Open with the operation verb and name the change. The model edits conversationally, with no masks or brushes.
- Refer to the source in words ("the provided photo", "this scene") and scope the change precisely.
- Define a region in language to edit only that area (semantic masking): "change only the blue sofa to brown leather; keep the rest of the room, the pillows, and the lighting unchanged."
- Always pin the invariants: state what must stay identical (face, pose, layout, colors, "everything else the same"). This is the difference between a clean edit and a full redraw.
- Make one change per turn for complex scenes. Stacking several edits in one prompt makes the model miss some of them.
- Edits inherit the source's lighting, perspective, and grain automatically; ask for natural integration ("match the existing window light", "follow the folds of the fabric").
- Studio-control edits work as plain instructions: relight ("turn this scene to night"), recolor, shift focus ("focus on the flowers"), change angle, or color-grade.

</rules>

<example use_case="add-element">

```text
Using the provided photo of my cat, add a small knitted wizard hat on its head, sitting naturally and matching the soft window light. Keep the cat's pose, fur, and the background exactly as they are.
```

*Why: it names the addition, asks for lighting that matches the source, and pins the subject and background so nothing else shifts.*

</example>

<example use_case="semantic-mask-recolor">

```text
In the provided living-room photo, change only the blue sofa to a tan leather chesterfield. Keep the pillows, rug, wall art, and lighting exactly the same.
```

*Why: "change only ..." plus an explicit list of what to keep defines the edit region in language, so the recolor stays surgical instead of redrawing the room.*

</example>

<example use_case="style-transfer">

```text
Transform the provided street photo into the style of Van Gogh's "Starry Night", with swirling impasto brushstrokes and a deep blue and gold palette. Preserve the original composition and the positions of the buildings and cars.
```

*Why: it names the target style and explicitly preserves composition, so the scene is restyled rather than replaced.*

</example>

<example use_case="style-transfer-plus-edit">

```text
Restyle the provided portrait as a 1960s screen-print poster with bold flat colors and halftone shading, and add the text "LIVE AT THE FILLMORE" in a groovy psychedelic font across the bottom. Keep the subject's face, hairstyle, and pose unchanged.
```

*Why: it combines a style transfer with a text addition in one instruction while pinning the identity, so the restyle does not drift the likeness.*

</example>

## Multiple reference images

<rules id="reference">

- Refer to each input by position in words: "the dress in the first image", "the woman in the second image", "the background in the third image". Some hosts also let you number or @-mention inputs; the positional phrasing is the portable form.
- One role per input. Assign each reference a single job and weld every borrowed element to its source ("use the first image for the character, the second for the outfit, the third for the location"). Mixing roles across inputs is the main cause of blended, wrong-attribute results.
- Name what moves, pin what stays. Say exactly which element comes from which image and what must stay identical (face, logo shape, garment color), or the model will under-specify and drift.
- State how the elements combine and the final framing, and ask for the lighting and shadows to be adjusted so the composite reads as one photograph.
- Character consistency: keep the same reference across turns, command it explicitly ("the identity, hairstyle, and outfit of all three people must stay consistent, seen from new angles"), and feed prior outputs back in. For a specific pose, add a pose reference.
- Capacity varies by model. Gemini 3 Pro Image and Gemini 3.1 Flash Image combine many references and hold several consistent characters, so reserve the extra slots for objects and style rather than piling on conflicting references. Gemini 3.1 Flash Lite Image and the legacy Gemini 2.5 Flash Image handle only a few, so consolidate roles before sending work to either.

</rules>

<example use_case="multi-ref-composite">

```text
Create a professional e-commerce photo. Dress the woman from the first image in the green floral dress from the second image, and place her on the sunlit market street from the third image. Keep her face and hair unchanged and the dress's pattern and color exact, and adjust the lighting and shadows on both so they match the street scene. Full-body shot, natural perspective.
```

*Why: three inputs, one role each (person, garment, location), with the invariants on face and garment pinned and an explicit relight instruction so the pieces fuse into one believable photo.*

</example>

<example use_case="object-into-hand-plus-pose">

```text
Put the ceramic mug from the second image into the right hand of the woman in the first image, and change her pose to match the seated pose of the person in the third image. Keep the woman's face, hairstyle, and clothing from the first image unchanged, and keep the mug's shape and glaze exactly as in the second image.
```

*Why: each of the three inputs supplies exactly one thing (subject, object, pose); naming what moves (mug, pose) and pinning what stays (identity, clothing, glaze) stops the borrowed pose from dragging in the third person's face or outfit.*

</example>

<example use_case="style-transfer-reference">

```text
Redraw the photograph in the first image in the painterly watercolor style of the second image. Keep the first image's composition, subjects, and their positions unchanged, and borrow only the brushwork, palette, and texture from the second image.
```

*Why: a reference-based style transfer that welds content to the first image and style to the second, with "borrow only ..." stopping the style image's own subjects from leaking into the result.*

</example>

<example use_case="character-consistency">

```text
Put these three people and the dog into one award-winning fashion-editorial shot on a rain-slicked city street at night. Keep each person's identity, hairstyle, and outfit consistent with their reference photo, seen from natural angles and distances, and make the lighting fall believably on all of them.
```

*Why: it commands consistency explicitly for every referenced person while allowing new angles, which is how the model keeps a group coherent instead of averaging faces together.*

</example>

## Reasoning and grounding

<rules id="grounding">

- On the Gemini 3 image models the model thinks before it draws. On Gemini 3.1 Flash Image the reasoning effort is tunable (low by default); raise it for complex, multi-element, or layout-critical prompts and keep it low for simple shots. How you set that level is host-specific.
- Gemini 3.1 Flash Lite Image has no reasoning step and no search grounding of either kind. Do not write "use search" or "use image search" instructions for it; supply the facts and the visual detail in the prompt instead.
- For real-world or time-sensitive content, tell the model to use search: "Use search to find {current fact} and visualize it as {description}." Good for weather, sports results, recent events, prices, and recipes.
- Pattern for data-driven images: ask it to retrieve the fact, then state the analytical task, then say how to visualize it.
- Gemini 3.1 Flash Image can also use image search ("use image search to find accurate references of {subject}") for visual grounding, but it cannot search for people.
- Gemini 3.1 Flash Image additionally accepts a video as a reference; describe the still you want ("a poster capturing the key themes of this video").
- Always verify the facts, figures, and labels in a grounded diagram; reasoning lowers but does not remove the chance of confident errors.

</rules>

<example use_case="search-grounded-chart">

```text
Use search to find the five-day weather forecast for San Francisco, then visualize it as a clean modern weather chart with a day-by-day row, a clear icon and high and low temperature for each day, and a short note on what to wear. Friendly flat illustration style, legible sans-serif labels.
```

*Why: the retrieve, analyze, then visualize pattern hands the live-data task to search grounding while you keep control of the layout, style, and typography.*

</example>

<example use_case="image-search-grounded">

```text
Use image search to find accurate references of a resplendent quetzal, then create a 3:2 nature wallpaper of the bird on a mossy branch with a soft top-to-bottom gradient and a minimal composition.
```

*Why: image-search grounding pins species-accurate detail the model would otherwise approximate; it works for objects and animals but not for searching specific people.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative-prompt field in the core scheme; exclude things in positive language.
- Use semantic negatives: instead of "no cars", write "an empty, deserted street with no traffic"; instead of leaving text to chance, add "No other text." as a short closing instruction.
- Describe the desired state, not the forbidden one. The model follows affirmative descriptions far more reliably than prohibitions.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Keyword soup: rewrite tag lists and quality-boosters ("masterpiece, 8k, trending on ArtStation") as a narrative scene; they do nothing here.
- Negative phrasing: replace "no X" with a semantic negative that describes the desired absence positively.
- Dense or tiny text: keep to a few short, large quoted strings; for exact copy, generate the layout and overlay the final text yourself.
- Stacked edits: make one change per turn rather than packing several into one prompt.
- Conflicting styles: do not combine cues that fight, such as photoreal and cartoon in one prompt.
- Overloaded prompts: past a few hundred words the model deprioritizes elements; spend words on what matters.
- Expecting transparency: transparent backgrounds are unsupported, so ask for a white background.
- Naming real people: describe attributes instead of celebrities; image search cannot target people.
- Expecting one perfect output: the exact image count is not guaranteed, so iterate conversationally and run a few variations.
- Unverified facts: check the labels and figures in diagrams and infographics even when grounding is on.

</rules>

## Sources

Trust order: official beats provider beats community. Official (Google) wins on any conflict; provider guides are illustrative only. Two notes from reconciling sources: Imagen and Veo are separate Google models on separate prompt schemes, not part of this family, so both are out of scope here; and Gemini Omni Flash, though a Gemini generative-media model, is a video model on its own scheme with its own guide.

- Official (Google): [Nano Banana image generation docs](https://ai.google.dev/gemini-api/docs/image-generation), [the ultimate Nano Banana prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana), [7 tips for Nano Banana Pro](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/), [Introducing Nano Banana Pro](https://blog.google/technology/ai/nano-banana-pro/), [Introducing Gemini 2.5 Flash Image](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/), [Gemini 3 Pro Image model page](https://deepmind.google/models/gemini-image/pro/).
- Provider: [fal how to use Nano Banana 2](https://fal.ai/learn/tools/how-to-use-nano-banana-2), [WaveSpeed Nano Banana Pro guide](https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026/).

Last verified: 2026-08-07.
