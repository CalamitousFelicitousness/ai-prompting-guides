---
guide: "Gemini Image (Nano Banana)"
prompt_scheme: "gemini-image"
# Google's family name is "Gemini Image"; "Nano Banana" is the product nickname, and from 2.1 on it is also the official model name.
models:
  - { id: "gemini-3-pro-image",          name: "Gemini 3 Pro Image",          alias: "Nano Banana Pro",    access: "closed-weights", tier: "flagship",   caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding], best_for: "the premium tier Google points to for professional assets: print-ready posters, long multilingual text, logos, factual diagrams, brand consistency; reasons by default; the only model Google lists with a dedicated style-reference role" }
  - { id: "gemini-nano-banana-2.1",      name: "Gemini Nano Banana 2.1",      alias: "Nano Banana 2.1",    access: "closed-weights", tier: "distilled",  caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding, marked-input-editing], best_for: "the default for new work and high volume; reasons at a middle setting by default; strongest multi-character consistency and marked-region edits; clean ultra-wide and ultra-tall frames; image-search grounding and video references" }
  - { id: "gemini-3.1-flash-lite-image", name: "Gemini 3.1 Flash Lite Image", alias: "Nano Banana 2 Lite", access: "closed-weights", tier: "budget",     caps: [text-to-image, image-edit, text-rendering], best_for: "speed and scale at the lowest cost; keeps prompt adherence, character consistency and legible text; reasons only when the level is raised, no search grounding, not built for many references or long edit chains" }
  - { id: "gemini-3.1-flash-image",      name: "Gemini 3.1 Flash Image",      alias: "Nano Banana 2",      access: "closed-weights", tier: "legacy",     caps: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding], best_for: "the previous Flash default, now deprecated; Google recommends Gemini Nano Banana 2.1 for all new projects, and prompts transfer unchanged" }
  - { id: "gemini-2.5-flash-image",      name: "Gemini 2.5 Flash Image",      alias: "Nano Banana",        access: "closed-weights", tier: "legacy",     caps: [text-to-image, image-edit, multi-image-fusion, text-rendering], best_for: "the original model, now superseded; Google recommends moving to Gemini 3.1 Flash Lite Image" }
capabilities: [text-to-image, image-edit, multi-image-fusion, text-rendering, search-grounding, marked-input-editing]
prompt:
  languages: ["en", "zh-CN", "ja-JP", "ko-KR", "ar", "hi-IN", "es", "fr", "de", "pt-BR", "ru", "uk-UA", "vi-VN", "id-ID", "it-IT"]
  formula: "strong verb first (the operation), then Subject, Composition, Action, Location, Style; describe a scene in plain sentences, never a keyword list"
  literal_text: "put the exact words in quotes; give each text element its own font, size, and placement; for another language, quote the exact translated wording; for exact copy, settle the wording in conversation first, then ask for the image"
  length_strategy: "1-3 vivid sentences for a simple shot; longer with explicit layout for text-heavy posters and infographics; very long prompts make the model deprioritize some elements"
  auto_expand_behavior: "none; the models reason over the prompt (a thinking step) before drawing but do not silently rewrite it, so state the full intent yourself"
  negatives: "no negative field; use semantic negatives (describe the desired absence positively, e.g. 'an empty street with no traffic')"
  references: "name each input positionally (the dress in the first image, the woman in the second), give each one a single role, and give recurring characters a name you reuse every turn; weld every borrowed element to its source"
  markup: "no mask field; draw a box, outline or scribble on the input image in a color absent from the scene, name the mark in the prompt, say whether it selects what changes or what stays, and ask for the mark to be removed"
  grounding: "ask the model to 'use search' for real-time or factual content (weather, sports, recipes); Gemini Nano Banana 2.1 can also 'use image search' for visual references but cannot use images of real people; Flash Lite has neither"
sources:
  official: ["https://ai.google.dev/gemini-api/docs/image-generation", "https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1", "https://deepmind.google/models/gemini-image/flash/", "https://deepmind.google/models/model-cards/nano-banana-2-1/", "https://deepmind.google/models/gemini-image/prompt-guide/", "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/nano-banana-2-1", "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana", "https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/", "https://blog.google/technology/ai/nano-banana-pro/", "https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/", "https://deepmind.google/models/gemini-image/pro/", "https://deepmind.google/models/gemini-image/flash-lite/", "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/"]
  provider: ["https://fal.ai/nano-banana-2.1", "https://fal.ai/learn/tools/how-to-use-nano-banana-2", "https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026/"]
  community: []
last_verified: "2026-11-08"
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

Google ships most generative-media models under two names: an official Gemini name and a nickname that carries less information. Prefer the official name and translate the nickname on sight. From Nano Banana 2.1 on, the nickname is the official name, so read the table rather than assuming the pattern.

| Official name (preferred) | Gemini API model ID | Nickname | Line | Role |
| --- | --- | --- | --- | --- |
| Gemini 3 Pro Image | `gemini-3-pro-image` | Nano Banana Pro | Pro | Premium tier: world knowledge, brand consistency, precision control, style references |
| Gemini Nano Banana 2.1 | `gemini-nano-banana-2.1` | Nano Banana 2.1 | Flash | Default for new work; strongest multi-reference consistency and marked-region edits |
| Gemini 3.1 Flash Lite Image | `gemini-3.1-flash-lite-image` | Nano Banana 2 Lite | Flash Lite | Speed and scale; not built for many references or long edit chains |
| Gemini 3.1 Flash Image | `gemini-3.1-flash-image` | Nano Banana 2 | Flash (legacy) | Deprecated; Google recommends moving to Gemini Nano Banana 2.1 |
| Gemini 2.5 Flash Image | `gemini-2.5-flash-image` | Nano Banana | Flash (legacy) | Superseded; Google recommends moving to Gemini 3.1 Flash Lite Image |
| Gemini Omni 1.2 Flash | `gemini-omni-1.2-flash` | none | Omni | Video output with native audio; a different prompt scheme with its own guide |

<rules id="naming">

- Translate the nickname to the official name before deciding anything. For the older models the official name states the generation and the tier separately; the nickname collapses them and drops one.
- Gemini Nano Banana 2.1 (`gemini-nano-banana-2.1`) is the official name and ID; there is no "Gemini 3.x Flash Image" form of it. Its model card says it is built on Gemini 3.6 Flash, but no `gemini-3.6-flash-image` ID exists, so do not construct one.
- Nano Banana 2.1 succeeds Nano Banana 2 on the Flash line. Neither is the successor to Nano Banana Pro: the numbers count generations on the Flash line, and Pro is a separate, higher tier. Google still presents Pro as its premium image model, although its own 2.1 model card scores 2.1 ahead of Pro on overall preference and editing.
- The `-preview` IDs (`gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview`) were the pre-release forms of the same models. They are retired, and the plain IDs replaced them on both the Gemini API and Vertex.
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

All five share one prompt scheme; a prompt written for one transfers to the others. Pick by job.

- Gemini Nano Banana 2.1: the default for new work and high volume, and the model Google recommends for all new projects. It reasons at a middle setting by default and can be tuned either way, holds several characters and many objects consistent across references, confines an edit to a region drawn on the input image, renders clean ultra-wide and ultra-tall frames, and accepts image-search grounding and video references. Google's own model card scores it ahead of Gemini 3 Pro Image on overall preference, editing and infographics, so start here.
- Gemini 3 Pro Image: the premium tier Google points to for professional asset production: print-ready posters, long legible multilingual text, logos, factual diagrams, and brand work. It reasons by default, can use Google Search grounding, and is the one model Google lists with a dedicated style-reference role. Step up to it for a brand system or when separate style references matter.
- Gemini 3.1 Flash Lite Image: the speed and scale option, for near-real-time and high-throughput pipelines. It keeps prompt adherence, character consistency, and legible in-image text, but reasons only when the level is raised, has no search grounding of either kind, and is not optimized for many reference inputs or long multi-turn edit chains. Write self-contained prompts for it and keep edit sequences short.
- Gemini 3.1 Flash Image: the previous Flash default, now deprecated in favor of Gemini Nano Banana 2.1. Prompts written for it transfer unchanged; the one behavioral difference is that it reasons only when the level is raised, where 2.1 reasons by default.
- Gemini 2.5 Flash Image: the original model, now legacy. Google recommends moving to Gemini 3.1 Flash Lite Image, which is faster, cheaper, and better. Keep it only for existing pipelines pinned to it.

The one asymmetry worth planning around: a prompt built on reasoning, search grounding, or a long reference stack degrades on Flash Lite rather than failing loudly. When moving work down to Lite, drop the grounding instruction and cut the reference count rather than trimming the description.

## How the model reads prompts

It is a multimodal language model, not a keyword or CLIP matcher, so it understands creative intent holistically. Plain descriptive sentences win; tag lists, weighted token syntax, and quality-boosters do not help and sometimes hurt. It rewards detail and stated purpose: "a logo for a high-end, minimalist skincare brand" beats "a logo."

The model reasons before it draws, planning the composition (and on complex prompts sketching interim thought-images) rather than pattern-matching. Gemini 3 Pro Image reasons by default, Gemini Nano Banana 2.1 reasons at a middle setting by default, and Gemini 3.1 Flash Image and Flash Lite reason only when the level is raised. Combined with broad world knowledge and optional search grounding, this lets you hand it intent and facts, not just visual nouns.

The model is conversational by design. The most reliable workflow is to generate, then refine across turns, feeding prior outputs back in. It does not silently expand a short prompt, so write the full intent yourself.

## Prompt structure

<rules id="structure">

- Lead with the operation verb, then follow Google's element order: Subject, Composition, Action, Location, Style.
- Name materials and specifics, not generic nouns ("navy blue tweed", not "jacket"; "matte black ceramic mug", not "cup").
- Use photographic and cinematic language to control the look: lens (85mm, macro, wide-angle), angle (low-angle, aerial, eye-level), depth of field (shallow, f/1.8, bokeh), lighting (golden hour, three-point softbox, chiaroscuro), and film or camera character (1970s film stock, Fujifilm color, GoPro).
- Length: 1-3 vivid sentences for a simple shot; expand with explicit layout only for text-heavy or multi-element work. Very long prompts cause the model to deprioritize details, so spend words on what matters.
- State aspect ratio in plain words when it matters ("vertical 9:16 poster", "cinematic 21:9", "square image"). Gemini Nano Banana 2.1 also renders ultra-wide 4:1 and 8:1 banners and tall 1:4 and 1:8 strips; for those, lay the content out along the full length of the frame (a coastline, a skyline, a procession) rather than one centered subject.
- To compare options, ask for several in one prompt ("three distinct variations of this label", "four different color palettes for this poster"). Treat the count as a request; the model does not always return the exact number.

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

<example use_case="panoramic-banner">

```text
Create an ultra-wide 4:1 panoramic watercolor of the Amalfi Coast at golden hour. From left to right, pastel cliffside villages step down to a turquoise sea, a small white ferry crosses the bay, and the headland fades into warm haze at the far right. Loose wet-on-wet washes, visible cold-press paper texture, soft peach and teal palette. No text.
```

*Why: the ratio is stated in words, and the scene is laid out left to right so every part of the long frame carries content instead of one centered subject with filler on the flanks. The subject follows fal's panoramic launch example for 2.1.*

</example>

## Text rendering

<rules id="text">

- Put the literal words in quotes, exactly as they should appear: the text "GRAND OPENING".
- Give each distinct text element its own quoted string plus its own font, weight, size, and placement ("the title 'BERLIN' in bold blue serif at the top-center; the date in small text in the corner").
- Describe fonts in words (clean bold sans-serif, condensed serif, brush script); name a real typeface only as a style hint.
- Keep to a few short text elements; large, short text renders far more reliably than dense paragraphs or tiny captions, and small lettering blurs most at the smallest output size. For pixel-exact copy, generate the layout, then overlay the final text yourself.
- For exact wording, settle the copy in conversation first, then ask for the image that contains it.
- For another language, name the target language and any regional cues, and when the wording matters, quote the exact translated text rather than asking the model to translate it (the shop sign reads "Hecho a mano" in Spanish). The model renders many languages, including non-Latin scripts, and can translate text already inside an image.
- Suppress unwanted lettering with "No other text." Gemini Nano Banana 2.1 and Gemini 3 Pro Image are the strongest for long, legible, multilingual text and infographic layouts.

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

*Why: it leans on the model's world knowledge for a factual diagram, fixes the panel layout and caption font, and demands technical accuracy. Keep reasoning on for work like this, where Google's 2.1 model card shows it buying the most accuracy, and still verify the labels against a real source.*

</example>

## Image editing

<rules id="edit">

- Lead with an imperative verb. It can name the change (Add, Replace, Redraw, Restore) or the constraint (Keep), but the opening clause must instruct rather than describe. A declarative setup such as "Image 1 provides the foundation, Image 2 provides the face" states the plan instead of issuing it and pushes the real instruction back by a sentence or two.
- Open with the operation verb and name the change. There is no mask field: define the region in words, or draw it on the input image (see Marked-region edits).
- Refer to the source in words ("the provided photo", "this scene") and scope the change precisely.
- Define a region in language to edit only that area (semantic masking): "change only the blue sofa to brown leather; keep the rest of the room, the pillows, and the lighting unchanged."
- Always pin the invariants: state what must stay identical (face, pose, layout, colors, "everything else the same"). This is the difference between a clean edit and a full redraw.
- Make one change per turn for complex scenes. Stacking several edits in one prompt makes the model miss some of them.
- Edits inherit the source's lighting, perspective, and grain automatically; ask for natural integration ("match the existing window light", "follow the folds of the fabric").
- Studio-control edits work as plain instructions: relight ("turn this scene to night"), recolor, shift focus ("focus on the flowers"), change angle, or color-grade.
- To change a pose, say so explicitly and add a pose reference. Edits sometimes keep the input's pose and structure even when the prompt asks for a new one.
- Anchor positions to things in the scene ("the cup nearest the window", "her raised hand") rather than bare left and right, which the model sometimes swaps.

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

## Marked-region edits

Google ships mask-based editing as a headline feature of Gemini Nano Banana 2.1: you draw on the input image and the prompt refers to the drawing. There is no separate mask input; the marked image is the input. The older models accept marked images too, but Google scores them lower on this task.

<rules id="markup">

- Draw the mark on the image before sending it: a box, an outline, or a scribble, in a bright color that does not occur in the scene (magenta, lime). Use one mark per change.
- Name the mark by color and shape in the prompt ("inside the magenta box", "the object inside the white outline").
- Say which way the mark works. It can select what changes ("add a hot-air balloon inside the magenta box") or protect what stays ("keep the object inside the outline at the same size and position, and replace everything around it").
- Ask for the mark to be removed from the finished image. Google lists ink that persists into the output as a known limitation.
- Pin what stays outside the mark by name. The rest of the frame is regenerated rather than copied pixel for pixel, so expect a close match, not an identical one.
- Keep each marked edit to one change. Google also lists partial instruction-following on marked edits, so split multi-part changes across turns.

</rules>

<example use_case="mark-selects-change">

```text
In the provided photo, add a small striped hot-air balloon drifting inside the magenta box in the sky, lit by the same low sun as the rest of the scene. Change nothing outside the box: keep the model in the yellow gown, the teal car, and their reflections on the wet salt flat exactly where they are. Remove the magenta box from the finished image.
```

*Why: the mark selects the region, the prompt names it by color and shape, everything outside it is pinned by name because the rest of the frame is regenerated, and the closing instruction removes the box. The scene follows fal's 2.1 mask-editing demonstration, whose prompt is not published.*

</example>

<example use_case="mark-protects-subject">

```text
Keep the dandelion seed inside the white outline exactly as it is, at the same size and position in the frame, and place it in a completely different environment: resting on a mossy log in a dim forest after rain, with soft green bokeh behind it. Remove the white outline from the finished image. Horizontal 16:9.
```

*Why: here the mark protects the subject instead of selecting the change. "Same size and position" is the clause from Google's own mask-editing demonstration ("don't change the size and position of the object itself"), and the removal instruction guards against the outline persisting.*

</example>

## Multiple reference images

<rules id="reference">

- Refer to each input by position in words: "the dress in the first image", "the woman in the second image", "the background in the third image". Some hosts also let you number or @-mention inputs; the positional phrasing is the portable form.
- One role per input. Assign each reference a single job and weld every borrowed element to its source ("use the first image for the character, the second for the outfit, the third for the location"). Mixing roles across inputs is the main cause of blended, wrong-attribute results.
- Name what moves, pin what stays. Say exactly which element comes from which image and what must stay identical (face, logo shape, garment color), or the model will under-specify and drift.
- State how the elements combine and the final framing, and ask for the lighting and shadows to be adjusted so the composite reads as one photograph.
- Character consistency: keep the same reference across turns, give each recurring character or object a name in the prompt and reuse it every turn ("Mara, the woman in the first image"), command consistency explicitly ("the identity, hairstyle, and outfit of all three people must stay consistent, seen from new angles"), and feed prior outputs back in. For a specific pose, add a pose reference.
- Capacity varies by model. Gemini Nano Banana 2.1 and Gemini 3 Pro Image combine many references and hold several consistent characters, and Google's model card rates 2.1 strongest at multi-character consistency. Reserve the extra slots for objects rather than piling on conflicting references. Google lists a separate style-reference role only for Gemini 3 Pro Image. Gemini 3.1 Flash Lite Image and the legacy Gemini 2.5 Flash Image handle only a few, so consolidate roles before sending work to either.

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

<example use_case="named-cast-six-refs">

```text
Create a candid golden-hour picnic photo on a grassy hillside. Mara is the woman with auburn curls in the first image, and Biscuit is the golden retriever in the second. Park the sage-green Land Rover from the third image behind them. Mara sits on a plaid blanket wearing the straw sun hat from the fourth image, with the wicker basket from the fifth image open beside her, while Biscuit leaps after the striped kite from the sixth image. Keep Mara's face and curls, Biscuit's coat, and the car's color and shape exactly as in their references.
```

*Why: six inputs, one role each. The two characters are named once and then referred to by name, which is how Google's prompt guide suggests keeping subjects consistent; every borrowed object is welded to its image and the identities are pinned. The cast follows fal's six-reference 2.1 demonstration.*

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

- The models think before they draw. Gemini Nano Banana 2.1 reasons at a middle setting by default; lower it for quick drafts and raise it for complex, multi-element, multi-reference, or layout-critical prompts. Google's 2.1 model card shows reasoning lifting infographic accuracy and editing quality most, so keep it on for diagrams. Gemini 3.1 Flash Image and Flash Lite reason only when the level is raised. How you set the level is host-specific.
- Gemini 3.1 Flash Lite Image has no search grounding of either kind. Do not write "use search" or "use image search" instructions for it; supply the facts and the visual detail in the prompt instead.
- For real-world or time-sensitive content, tell the model to use search: "Use search to find {current fact} and visualize it as {description}." Good for weather, sports results, recent events, prices, and recipes.
- Pattern for data-driven images: ask it to retrieve the fact, then state the analytical task, then say how to visualize it.
- Gemini Nano Banana 2.1 (and the legacy Gemini 3.1 Flash Image) can also use image search ("use image search to find accurate references of {subject}") for visual grounding, but cannot use images of real people from search. To make the order explicit, tell it to search first and generate after.
- Gemini Nano Banana 2.1, Gemini 3.1 Flash Image, and Flash Lite accept a video as context; describe the still you want ("a poster capturing the key themes of this video"). Gemini 3 Pro Image takes images and text only.
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

*Why: image-search grounding pins species-accurate detail the model would otherwise approximate; it works for objects, animals, and places but not for specific people.*

</example>

<example use_case="search-then-generate">

```text
Create an image of Museum Clos Luce. In the style of a color chalk sketch, no text. Your plan is to first search for visual references, and generate after. Aspect ratio 16:9.
```

*Why: Google's own 2.1 demonstration. Stating the plan (search first, generate after) makes the grounding step explicit for a real building the model would otherwise approximate.*

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
- Dense or tiny text: keep to a few short, large quoted strings, since small lettering blurs most at the smallest output size; for exact copy, generate the layout and overlay the final text yourself.
- Stacked edits: make one change per turn rather than packing several into one prompt.
- Leaving the mark in: end every marked-region edit by asking for the box, outline, or scribble to be removed.
- Stuck pose: when an edit must change the pose, say so plainly and add a pose reference; otherwise the input's pose can carry through.
- Bare left and right: anchor positions to objects in the scene; the model sometimes swaps sides.
- Reasoning off for diagrams: keep reasoning on, or raise it, for infographics and data visuals.
- Conflicting styles: do not combine cues that fight, such as photoreal and cartoon in one prompt.
- Overloaded prompts: past a few hundred words the model deprioritizes elements; spend words on what matters.
- Expecting transparency: transparent backgrounds are unsupported, so ask for a white background.
- Naming real people: describe attributes instead of celebrities; image search cannot use images of people.
- Expecting one perfect output: the exact image count is not guaranteed, so iterate conversationally and run a few variations.
- Unverified facts: check the labels and figures in diagrams and infographics even when grounding is on.

</rules>

## Sources

Trust order: official beats provider beats community. Official (Google) wins on any conflict; provider guides are illustrative only. Notes from reconciling sources: Imagen and Veo are separate Google models on separate prompt schemes, not part of this family, so both are out of scope here; Gemini Omni Flash, though a Gemini generative-media model, is a video model on its own scheme with its own guide; the DeepMind prompt guide is written for the Gemini app, so its advice is taught here only where it adds to the API docs without contradicting them; and the Nano Banana 2.1 model card scores 2.1 above Gemini 3 Pro Image while the API docs still present Pro as the premium tier, so the guide starts work on 2.1 and keeps Pro as the higher tier.

- Official (Google): [Nano Banana image generation docs](https://ai.google.dev/gemini-api/docs/image-generation), [Gemini Nano Banana 2.1 model page](https://ai.google.dev/gemini-api/docs/models/gemini-nano-banana-2.1), [Nano Banana 2.1 on DeepMind](https://deepmind.google/models/gemini-image/flash/), [Nano Banana 2.1 model card](https://deepmind.google/models/model-cards/nano-banana-2-1/), [DeepMind Gemini Image prompt guide](https://deepmind.google/models/gemini-image/prompt-guide/), [Gemini Nano Banana 2.1 on Vertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/nano-banana-2-1), [the ultimate Nano Banana prompting guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana), [7 tips for Nano Banana Pro](https://blog.google/products-and-platforms/products/gemini/prompting-tips-nano-banana-pro/), [Introducing Nano Banana Pro](https://blog.google/technology/ai/nano-banana-pro/), [Introducing Gemini 2.5 Flash Image](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/), [Gemini 3 Pro Image model page](https://deepmind.google/models/gemini-image/pro/).
- Provider: [fal Nano Banana 2.1](https://fal.ai/nano-banana-2.1), [fal how to use Nano Banana 2](https://fal.ai/learn/tools/how-to-use-nano-banana-2), [WaveSpeed Nano Banana Pro guide](https://wavespeed.ai/blog/posts/google-nano-banana-pro-complete-guide-2026/).

Last verified: 2026-11-08.
