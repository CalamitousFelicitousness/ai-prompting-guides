---
guide: "FLUX 3 Image"
prompt_scheme: "flux-3-image"
models:
  # hosted
  - { id: "flux-3-image", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, layout-control, grounding-search], best_for: "the full FLUX 3 image model: highest quality, and the only one that grounds a prompt in web search so real places, products and events come out right. It always expands the prompt before generating and cannot be told not to, so write short and spend words only on what you need to control" }
  # open weights (FLUX Kommunity License). Klein ships as a PAIR: a step-distilled checkpoint and an undistilled
  # base. They are different models with different settings, so never carry a step count or guidance across the pair.
  - { id: "flux-3-image-klein", access: "open-weights", tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, layout-control], best_for: "the fast open FLUX 3 image model, also served on the API. Step-distilled to run without guidance, so exclusions have nothing to push against and seeds converge; a prompt that fights the model's defaults needs the base checkpoint. Prompt length depends on whether the owner's upsampler runs in front of it: short with it, a full caption without it" }
  - { id: "flux-3-image-klein-base", access: "open-weights", tier: "base", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, layout-control], best_for: "the undistilled Klein: guidance is live and seeds stay diverse, so this is the checkpoint for LoRA training, fine-tuning, and any prompt that needs steering. Not on the API" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, layout-control, grounding-search]
prompt:
  languages: ["en"]
  formula: "medium and style first, then scene, lighting and camera, then each subject with its colors, materials, state and frame position; for an edit, the change as an instruction followed by one compact keep clause"
  length_strategy: "SPLIT BY WHAT SITS IN FRONT OF THE MODEL. Where an upsampler expands the prompt (flux-3-image always, Klein on the API, Klein in the reference CLI by default) write short and add detail only for what you must control. Where nothing expands it (Klein run directly, or with the upsampler skipped) write the full caption the upsampler would have written: about 100 to 350 words for an image, 50 to 150 for an edit. A short prompt to a bare model gives generic output"
  auto_expand_behavior: "ALWAYS ON for flux-3-image, with no off switch. On for Klein on the API. On by default in the owner's reference code for local Klein and skippable there; absent in a plain local pipeline unless you run the upsampler model yourself"
  literal_text: "quote the exact words in double quotes, in their own script, with line breaks written as \\n inside the quote; then give placement, weight, case, color and typeface character"
  references: "TWO NUMBERINGS. In a plain prompt, references count from ONE: 'image 1' (or 'the first image') is the first input. In a bounding-box record they count from ZERO: <ref_image_0> is that same first input. Never mix the forms in one prompt"
  layout: "optional bounding boxes: the caption, one space, then a JSON element table as the last thing in the prompt. Boxes are [y_min, x_min, y_max, x_max] integers on a 0-1000 grid with a top-left origin, y FIRST. Each row's id is cited in the caption as <id>. Boxes place and scale; they do not mask"
  edits: "write the change as an instruction (Remove..., Change the X to Y...), a whole-image change opens with its scope (Convert the entire image into...), and combining references is a generation request (Create a photograph of...). A one-line instruction is fine only where an upsampler expands it"
  color: "a hex code pins a target color in an edit, tied to one named object; outside edits, describe the palette in words"
  negatives: "no negative field on any surface. Describe the state you want ('an empty promenade', not 'no crowds'). On distilled Klein a negative would have nothing to push against anyway"
  world_knowledge: "flux-3-image searches the web by default, so naming a real place, product or event usually yields the real thing; Klein has no search, so describe what it must show"
sources:
  official: ["https://docs.bfl.ai/guides/prompting_summary", "https://docs.bfl.ai/guides/prompting_unified_basics", "https://docs.bfl.ai/guides/prompting_unified_building", "https://docs.bfl.ai/guides/prompting_unified_style", "https://docs.bfl.ai/guides/prompting_unified_technical", "https://docs.bfl.ai/guides/prompting_layout", "https://docs.bfl.ai/guides/prompting_unified_reference", "https://docs.bfl.ai/guides/prompting_editing_overview", "https://docs.bfl.ai/guides/prompting_editing_single_reference", "https://docs.bfl.ai/guides/prompting_editing_multi_reference", "https://docs.bfl.ai/flux_3/flux3_image_overview", "https://docs.bfl.ai/flux_3/flux3_image_generate", "https://docs.bfl.ai/flux_3/flux3_image_layout", "https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes", "https://docs.bfl.ai/flux_3/flux3_image_klein", "https://bfl.ai/blog/flux-3-image-klein", "https://huggingface.co/black-forest-labs/flux-3-image-klein", "https://huggingface.co/black-forest-labs/flux-3-image-klein-base", "https://huggingface.co/black-forest-labs/flux-3-image-klein-pup", "https://github.com/black-forest-labs/flux-3-image-klein"]
  provider: []
  community: []
last_verified: "2026-10-15"
---

# FLUX 3 Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and step limits, reference counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the FLUX 3 image models: the full `flux-3-image` on the API, and the open-weights `flux-3-image-klein` and `flux-3-image-klein-base`. They share one prompt scheme; what differs is whether something expands your prompt before the model sees it, and that difference decides how long to write.
- FLUX 3 Image is a different scheme from FLUX.2 and from FLUX 3 Video. Do not carry FLUX.2's whole-prompt JSON schema or its text-to-image hex pinning across, and do not carry video camera and audio grammar in from the video guide.
- One model does text-to-image, editing, multi-reference composition and bounding-box layout. The prompt alone says which job it is.
- Write the prose in English. Text that should appear in the image keeps its own script inside the quotes.
- References are numbered two ways. Plain prompts count from one ("image 1"); bounding-box records count from zero (`<ref_image_0>`). Both name the same first input.
- There is no negative field. Describe the state you want.

</rules>

## Model names and aliases

| Name you may see | What it is | Guide |
| --- | --- | --- |
| FLUX 3 Image, `flux-3-image` | the full FLUX 3 image model, API only | FLUX 3 Image |
| FLUX 3 Image Klein, `flux-3-image-klein` | the 5.6B open-weights FLUX 3 image model, step-distilled; also on the API | FLUX 3 Image |
| FLUX 3 Image Klein Base, `flux-3-image-klein-base` | the undistilled Klein, open weights, for training and steering | FLUX 3 Image |
| FLUX 3 Video, `flux-3-video` | the FLUX 3 video model | FLUX 3 Video |
| FLUX Video Edit [fast] | a FLUX Tools video editor that takes a clip and an instruction | FLUX 3 Video |
| FLUX.2 [klein] 4B and 9B, `flux-2-klein-*` | the small open FLUX.2 models | FLUX.2 |
| FLUX.2 [pro], [flex], [max], [dev] | the other FLUX.2 models | FLUX.2 |
| FLUX 3 Dev | an announced open multimodal model that has not shipped | none |

<rules id="naming">

- "Klein" names two unrelated model lines. FLUX.2 [klein] and FLUX 3 Image Klein share a word and nothing else: different prompt schemes, different reference notation, and opposite defaults on prompt expansion. Resolve "klein" by the family number before applying any rule.
- FLUX 3 is not one prompt scheme. Its image models and its video model are documented and prompted separately; route by modality.
- FLUX 3 Dev was announced as an open multimodal model and has not been released. The open FLUX 3 releases are FLUX 3 Action, a robotics model that takes no image or video prompt, and FLUX 3 Image Klein.
- FLUX Video Edit [fast] is sold as a FLUX Tools product rather than under the FLUX 3 name. Its prompt rules sit in the FLUX 3 Video guide.

</rules>

## TL;DR

<template id="quickstart">

Where an upsampler runs: {medium and style} of {subject} {doing what} in {setting}, {light}. Add only what you must control: "{exact text}" and where it sits, a position, a color.
Where nothing expands the prompt: write the full caption in "Prompt structure" below.

</template>

## Models and when to use which

All three share one scheme; pick by access and by how much the prompt must be steered.

- `flux-3-image` (API): the highest quality, and the only one with web grounding, so it is the right choice when the image must show a real thing correctly (a real landmark, product, poster or event). It always rewrites your prompt first, so a short prompt is the intended input.
- `flux-3-image-klein` (open weights, also on the API): the fast model. On the API it runs behind the owner's upsampler and an exact-restoration pass for unedited pixels, so it behaves much like the full model at lower cost. Locally it is a bare step-distilled model unless you put the upsampler in front.
- `flux-3-image-klein-base` (open weights): the undistilled Klein, slower but steerable. Use it for training and whenever a distilled result keeps ignoring an instruction.

The owner's prompt upsampler is a separate 9B model that ships alongside Klein. It turns a short request, the reference images and any boxes into the full prompt the model was tuned on, and its published instructions are the clearest statement of what that prompt looks like. Running it is optional; writing what it would have written is not, wherever it does not run.

## How the model reads prompts

- The caption controls composition. Reference images anchor content (what things look like) but do not lock structure (where things are); framing, pose and layout follow the words.
- Expansion decides length. Behind an upsampler, a short request is expanded into a long caption, so extra words only help where they fix something you care about: a position, an appearance, the light, a piece of text. A bare model takes what you type literally, so a short prompt yields a generic image and a one-line edit can reframe the whole shot.
- On the full model you can read what it actually used. The expanded prompt comes back with the result; check it when an output surprises you before rewriting your own.
- The full model looks things up. Naming a real event, product or place usually resolves to the real one. Klein has no search, so it can only use what it already knows or what you describe.
- Structure matters more than length. A clear order (medium, scene, light, subjects, positions) does more than extra adjectives, and a sentence that describes nothing visible is wasted.
- Distilled Klein runs with no guidance. That makes it fast and consistent, but it also means seeds converge and an instruction that fights the model's habits has little to push against. When that happens, the base checkpoint is the fix, not more emphatic wording.

## Prompt structure

These rules are the owner upsampler's own specification, and they describe the prompt every surface eventually hands the model. Write this way wherever nothing expands your prompt; behind an upsampler, write the short version and let it do the rest.

<rules id="structure">

- Lead with the medium and style in one opening sentence that sets the look: "High-angle black and white photograph with a grainy film texture." Then the scene, the lighting and the camera, then the subjects with concrete colors, materials and state.
- With no style requested, plan an actual photograph and open with the medium convention: "Full-color outdoor photograph, ...", "Full-color indoor photograph, ...", "Studio photograph, ...", "Close-up photograph, ...". Keep "photorealistic" for renders; a request for a "realistic" photo becomes the photograph convention.
- Give a photograph a few ordinary, non-ideal specifics drawn from the scene's own objects (a chipped rim, a crooked sign, a scuffed shoe) instead of the stock-photo ideal.
- Write one continuous prose block in the generative voice. Never "this image shows", "we can see" or "is visible".
- Be definite. Decide everything the request left open as one consistent plan; no hedging adverbs, no "or" between alternatives, no closing sentence about mood. This is the opposite of what some other models' rewriters ask for, so do not carry a hedging habit in.
- Turn a mood into what it looks like. "Lonely" is a single figure, an empty street and low light; write those.
- Give every person in focus an observable profile: ethnicity, gender, age range, skin tone ("fair skin", "brown skin"), hair and clothing.
- Make the layout reconstructable from the words: frame-relative positions (frame-left, frame-right, upper, lower, foreground, midground, background), sentence-initial anchors ("On the left, ...", "In the background, ..."), relations (holds, faces, behind) and a consistent order.
- Describe up to about ten instances one by one; beyond that give the exact count and the arrangement.
- Treat out-of-focus and distant planes as shapes, colors and silhouettes, never as identities or readable text. The background takes about a sixth of the caption.
- Add depth of field, bokeh or blur only when you want them. They change the picture, so do not add them by reflex.
- Do not invent names, brands, logos or celebrities; keep the ones the request named. Camera and film names used as style cues ("shot on Kodak Portra 400") are a different thing and are welcome.
- Drop appraisal and quality words: masterpiece, beautiful, iconic, highly detailed, ultrarealistic. Every phrase should name something you could point to in the frame.
- Time of day is lighting, not text. "At dusk" changes the light; it does not put the word on a sign.

</rules>

<template id="general">

{medium and style}, {framing and camera}, {light: source, direction, quality}. {Scene}. {Position anchor}, {subject with profile, colors, materials, state, action}. {Position anchor}, {second subject and its relation to the first}. {Supporting objects with positions}. {Background as shapes and colors}. {Each piece of text: "exact words" with placement and typography}.

</template>

<example use_case="short-prompt-behind-upsampler">

```text
Formula 1 cars race along a curved desert track at dusk, a packed grandstand on the right, the Sphinx and the pyramids of Giza rising through the haze behind them. Warm golden light, peach and lavender sky, high-angle shot, 1990s film photograph with fine grain.
```

*Why: the owner's own Klein prompt for the API, where an upsampler expands it. Two sentences fix only what matters (subject, the one position that matters, the landmark, the light, the medium) and leave the rest to the expansion*

</example>

<example use_case="full-caption-flagship">

```text
A restrained 1990s fashion editorial photograph in a warm beige studio. An adult woman with tousled shoulder-length brown hair sits barefoot on a large muted-green exercise ball. She wears a fitted rust-brown sleeveless crop top and matching high-waisted briefs. Her hands rest together in her lap; one leg extends diagonally toward the camera and the other bends beside the ball. Full-body framing with generous plain wall above her, soft directional daylight, gentle floor shadows, warm skin tones, slightly muted color print and fine film grain. The ribbed green ball remains fully readable beneath her.
```

*Why: an owner caption at full length. Medium and era open it, the subject's clothing and pose are concrete and positional, framing and light get their own clause, and nothing in it is a quality word*

</example>

<example use_case="photograph-convention-bare-model">

```text
Full-color outdoor photograph, eye-level medium shot in late afternoon sun, of a street vendor's fruit cart on a narrow cobbled lane. The low sun comes from frame-right and throws long shadows of the cart's wheels across the stones. In the center of the frame, a middle-aged South Asian man with brown skin, short grey hair and a trimmed beard stands behind the cart, wearing a faded blue cotton shirt with the sleeves rolled to the elbow and a canvas apron with a dark stain at the pocket. He holds a paper bag open with his left hand while weighing oranges on a dented brass scale with his right. On the cart in front of him sit three wooden crates of oranges, pomegranates and green limes, one crate's corner split and taped. On the left, a hand-lettered cardboard sign leans against the crates and reads "3 FOR 100" in thick black marker. In the background, the lane narrows between pale ochre walls, its far end a soft band of warm light and dark doorways.
```

*Why: the upsampler's form written by hand for a model with nothing in front of it. It opens on the photograph convention, gives the person a full observable profile, anchors every element to the frame, adds two ordinary flaws (the stain, the split crate), keeps the background to shapes and color, and quotes the one legible string*

</example>

## Style, light and camera

<rules id="style">

- Name a style concretely and early: a medium, an era, a film stock. "The grainy texture of mid-20th-century color film" tells the model more than "vintage".
- For an art style, name it and describe its visual traits (palette, stroke, texture, line weight). Describe the attributes rather than naming a specific artwork.
- For a photographic look, name the camera, lens or film stock and then say what that look does: "Shot on Fujifilm X-T5, 35mm f/1.4, visible grain, a warm color cast, slight chromatic aberration at the edges."
- For realism, describe what a real camera records: grain, chromatic aberration at the edges, an atmospheric blur in the foreground. One generic realism cue is enough; more add nothing.
- Name the light's source, direction and quality, then what it does in the scene: "soft window light from the left" rather than "good lighting"; "harsh, direct camera flash that casts sharp shadows against the background".
- Mixing styles works when the combination is coherent; hold it together with one shared palette.
- Use one or two strong effects. Several at once make an image feel unfocused.

</rules>

## Text rendering

<rules id="text">

- Put the exact words in double quotes, with the capitalization and punctuation you want, then say where they go and how they look: weight, case, color and the character of the typeface ("a bold, white sans-serif typeface reminiscent of Helvetica").
- Write a line break as `\n` inside the quote, so the break is part of the string: "OPEN\nLATE".
- Text in another script stays in that script inside the quotes while the rest of the prompt stays English: `The sign reads "東京".`
- Describe graphics that belong to a text (an arrow, an underline, a badge) together with that text, not elsewhere in the caption.
- Split long copy into blocks, each with its own placement. Name canonical structures exactly (a calendar month, a keyboard, a periodic table) and they come with their full layout.
- When the request needs text but supplies none, write concrete, domain-correct wording rather than leaving the model to invent filler.
- Proofread every quoted string before sending. The model renders what is between the quotes, typos included.
- Text in the background or out of focus should not be readable; describe it as shapes and color.

</rules>

<example use_case="short-text-poster">

```text
Art deco travel poster of a streamlined train crossing a coastal stone viaduct, bold text "RIVIERA EXPRESS", gold and navy geometric sunburst.
```

*Why: the owner's Klein poster prompt for an upsampled surface: one quoted string, a period style that implies its own lettering, and a two-color palette*

</example>

<example use_case="multi-line-text-bare-model">

```text
Studio photograph of a hand-painted wooden shop sign leaning against a white brick wall, lit by soft daylight from frame-left. The sign is a horizontal board of weathered teal paint with a thin cream border. Across its upper half, large cream serif capitals read "HARBOUR\nBAKERY" on two centered lines. Beneath them, smaller italic cream lettering reads "est. 1962". In the lower right corner, a painted loaf of bread in ochre and brown sits beside the text. Faint brush marks and two small paint chips show near the left edge.
```

*Why: two text blocks, each quoted with its own placement and typography, the line break written inside the quote, and the graphic that belongs to the sign described with it*

</example>

## Layout with bounding boxes

Boxes are optional. Use them when words cannot pin a position or a size: a specific arrangement, a poster grid, several similar objects, text at an exact spot.

<rules id="layout">

- Write the caption, then one space, then a JSON array of element rows. The array must be the last thing in the prompt.
- Each generation row has three keys, in this order: `"id"`, `"bbox"`, `"desc"`.
- A box is `[y_min, x_min, y_max, x_max]`: Y FIRST, then x. Integers from 0 to 1000, origin at the top-left. `[0, 0, 500, 500]` is the top-left quarter whatever the image's shape.
- The grid stretches with the frame, so equal units are not equal lengths on a non-square image. To keep an object's true shape, make its x-span roughly y-span times its width-to-height ratio times H/W. On a 2:3 portrait frame, a square object 100 units tall needs about 150 units of width.
- Design the boxes for the frame you will actually request; the same boxes on a different shape distort.
- Some tools take a box file in fractions from 0 to 1. Those convert to the 0-1000 grid before they reach the prompt. Never paste fractions into a prompt.
- Ids are a class noun plus an index: `person_1`, `dog_2`, `background_1`. Text blocks are a language code, `_Text_` and an index: `En_Text_1`, `Ja_Text_1`. Letters, digits and underscores only; no spaces or hyphens. Ids are case-sensitive and must be unique.
- Cite every row in the caption exactly once, as `<id>` right after the noun it names: "a wicker table <table_1> holding a tiered stand <stand_1>". Cite no id that has no row.
- The caption carries the scene, the light, the camera and the layout in words ("in the left foreground"); the desc carries the element's appearance. No coordinates in the caption.
- A desc opens with what the element is ("A black silhouette of a person...", never "The silhouette...") and gives shape, material, color, state and markings.
- A text row's desc quotes its full wording, with `\n` for line breaks, plus its typography. Leave a small margin around text boxes. The caption names the text block but does not repeat the words.
- One row per distinct object, person, animal, building, salient region or text block. No rows for style, light or atmosphere. More than about ten interchangeable items become one collection row with an exact count.
- Overlap boxes when things overlap: a dog in someone's lap sits inside their box. A background can span the frame, `[0, 0, 1000, 1000]`.
- Boxes set placement and scale, not a mask. An element can spill past its box, and a very small box may produce nothing at all; give new elements room.
- In the owner's reference code, a prompt whose every row is cited is sent as written, while an uncited row sends the prompt back through the upsampler, which keeps your boxes but rewrites your descriptions. Cite everything if you want your words to reach the model.

</rules>

<template id="layout">

{caption with medium, scene, light, camera, and each element named once with its <id> and a position in words} [{"id": "{class}_1", "bbox": [{y_min}, {x_min}, {y_max}, {x_max}], "desc": "{what it is: shape, material, color, state}"}, {"id": "En_Text_1", "bbox": [{y_min}, {x_min}, {y_max}, {x_max}], "desc": "The text \"{exact words}\" in {typography}"}]

</template>

<example use_case="layout-two-elements">

```text
Minimalist graphic illustration featuring a black silhouette of a person <silhouette_1> centered against a solid, vibrant chartreuse background <background_1>. The figure is captured in a dynamic, mid-stride running pose, facing toward the left side of the frame. The image relies entirely on the high-contrast relationship between the two colors, mimicking a digital recreation of a screen-printed or risograph aesthetic, with no discernible light source or shadow. [{"id":"background_1","bbox":[0,0,1000,1000],"desc":"A flat field of neon yellow-green possessing a subtle, tactile paper texture with fine, organic grain and slight variations in color saturation, giving the flat surface a sense of physical depth."},{"id":"silhouette_1","bbox":[150,150,850,850],"desc":"A black silhouette of a person in motion, composed of a dense, stippled texture that resembles physical ink on paper or a low-resolution digital dither. The leading edges, including the front of the head, chest, and forward leg, are relatively solid and opaque. The trailing edges, such as the back, outstretched rear arm, and lifted back leg, dissolve into a spray of coarse, square-shaped pixels and scattered dots. The black ink shows a slight textural irregularity, as if pressed onto a porous surface."}]
```

*Why: the owner's reference layout. Two rows, each cited once in the caption, the background spanning the whole grid, and the appearance detail living in the descs while the caption carries the pose and the overall look*

</example>

<example use_case="layout-poster-with-text">

```text
Vertical 35mm photograph with fine grain and slightly soft focus. Centered at the top is a cream-colored title <Fr_Text_1>. A hazy, pale grey and green overcast sky <sky_1> sits above dark, rolling mountains <mountains_1> and a distant coastal town <town_1> on the right. In the dark water <water_1> of a bay stands a massive, pale concrete parabolic dome <dome_1>. The dome's arched opening faces the shore, radiating a warm, golden-orange glow from its interior. A dark rectangular monolith <monolith_1> sits deep inside at water level. The golden light reflects on the rippling water, where scattered silhouettes of people <swimmers_1> wade. In the foreground, a pale, pebbly beach <beach_1> holds a large crowd of seated onlookers <crowd_1> in casual, light-colored clothing. Their backs are to the slightly elevated camera as they gaze at the structure under blue hour lighting. [{"id":"Fr_Text_1","bbox":[40,200,100,800],"desc":"\"LE FESTIVAL DU SOLEIL\" written in a thin, elegant, serif typeface in a light cream color"},{"id":"sky_1","bbox":[0,0,280,1000],"desc":"a hazy, overcast sky in muted tones of pale grey and muted green"},{"id":"mountains_1","bbox":[200,0,400,700],"desc":"dark, rolling mountains forming the backdrop along the coastline"},{"id":"town_1","bbox":[280,700,420,1000],"desc":"faint lights and small buildings of a coastal town at the foot of the hills"},{"id":"water_1","bbox":[380,0,750,1000],"desc":"dark bay water with a rippling surface"},{"id":"dome_1","bbox":[250,150,650,850],"desc":"a massive, smooth parabolic dome of pale concrete"},{"id":"monolith_1","bbox":[550,460,610,540],"desc":"a small, dark rectangular silhouette resembling a stage or monolith"},{"id":"swimmers_1","bbox":[580,200,720,800],"desc":"dozens of small, silhouetted figures scattered in the dark water, wading"},{"id":"beach_1","bbox":[720,0,1000,1000],"desc":"a pale, pebbly beach filling the foreground"},{"id":"crowd_1","bbox":[740,0,1000,1000],"desc":"a large crowd of people seated on the beach in casual, light-colored summer attire"}]
```

*Why: an owner poster layout for a 3:4 frame. The French title is its own text row with the wording only in its desc, crowds and swimmers are single collection rows, overlapping regions overlap their boxes, and every id is cited once*

</example>

## Image editing

The prompt alone says what to do with the attached images; there is no separate edit mode. Pick the voice by the shape of the task.

<rules id="edit">

- A bounded change to one image is an imperative instruction on it: "Remove the ...", "Change the ... to ...", "Zoom in on ...".
- A change to the whole image opens with its scope: "Convert the entire image into ...", "Apply a ... filter over the entire scene", "Shift the camera viewpoint to ..." followed by where the major elements now sit.
- Drawing references into a newly composed frame (combining subjects, a new scene, a garment or style donor) is a generation request: "Create a photograph of ...", "Generate a new image featuring ...", saying what comes from each image and what is new.
- NAME WHAT MOVES, PIN WHAT STAYS. Name the target precisely enough that only one thing matches (by position, size, color, or what it is next to), say what it becomes, then close with one compact clause naming what stays unchanged.
- Name the element as it is now and as it should be: "change the white car parked on the right to dark green".
- When a value matters, write the value: a hex code for a color, the exact words in quotes for text, a frame region for a position. "Pink" and "near the top" leave room.
- Tie each hex code to one named object: "change the color of only one bird in the middle to #e01075". A color name beside the code helps: "sky blue (#87CEEB)".
- Use "only" to scope a change ("Recolor only the fur"), and name an exclusion as the original state of the thing excluded ("the nose stays its original pale pink").
- State every end state concretely (which color, how large, which pose, which material) and give new content enough appearance to be generated.
- Cover the knock-on effects: shadows, reflections, occlusion, perspective, scale and lighting. When something is removed, say what fills the space.
- A zoom-in names what stays in frame and which neighbors are cut out. An outpainting continues the scene in the same medium.
- For a text edit, quote the new words exactly and match the original font, size and color unless you are changing them.
- Transferred people keep their identity, face and accessories unless you ask otherwise; say so when a change could pull on them.
- Directions are frame-relative. Use no quality words.
- Length follows the expansion rule. Behind an upsampler a short instruction is fine ("Make it a winter night: snow on the roof..."). On a bare model write 50 to 150 words of concrete instruction; a one-line edit there can reframe the shot.
- Unedited regions are only restored exactly on the API. On the open weights, pixels outside the change usually hold, but shadows, reflections and nearby light can shift, and content outside the region can change. Pin what matters by name.
- Writing the edit as a complete caption of the target image with the change folded in is also accepted by the open models, but the owner's own upsampler writes instructions, so treat the caption form as the alternative.

</rules>

<template id="edit">

{Operation verb} {the target, identified uniquely} {to its end state, with the exact value}, {knock-on effects}. Keep {the elements at risk, by name} and the rest of the image unchanged.

</template>

<example use_case="edit-short-behind-upsampler">

```text
Place the car on a coastal cliff road at sunset with the ocean below. Keep the car exactly identical, same angle and color.
```

*Why: the owner's Klein API edit. The change and the keep clause in two sentences, which is enough where the upsampler expands it*

</example>

<example use_case="edit-text-replacement">

```text
Change only the wording on the neon sign to the exact text "zum Schlappen". Keep the original sign's placement, mounting, glow color, perspective and the surrounding nighttime street scene. The new letters use continuous neon tubing and remain readable, with lowercase 'zum' and an uppercase 'S' in 'Schlappen'.
```

*Why: the owner's text edit. "Only" scopes it, the new words are quoted exactly, the keep clause names the sign's physical properties, and the case of each word is spelled out*

</example>

<example use_case="edit-hex-recolor-with-exclusions">

```text
Recolor only the white and black FUR of the cow. White fur becomes light muted green-teal #8bc4bb, and black fur patches become warm red-orange #de4528. Keep the exact patch shapes, fur texture, original shadows and grazing pose. The smooth bare nose and muzzle stay their ORIGINAL pale pink-beige color; exclude them completely from recoloring. Keep the dark eyes, nose openings, collar, yellow ear tag and hooves unchanged. Recolor the fur on the legs and ears only where it is white or black, not their bare skin. Preserve the entire pasture, tree line, sky, camera framing and lighting.
```

*Why: the owner's recolor, the long form for a precise job. Each source color is mapped to a named target with a hex code, the exclusion is stated as the excluded part's original state, and the keep list names the small details a recolor would otherwise sweep up*

</example>

<example use_case="edit-zoom-out">

```text
Use the white parakeet bathing in the puddle in the reference image as the subject. Zoom out to a wider view of the same outdoor scene, showing more of the grassy banks, shallow puddle and woodland beyond. Preserve the bird's appearance and bathing pose, the hovering butterfly, water splashes, golden lighting and low viewpoint. The bird occupies less of the wider frame while keeping the same scale relative to the puddle.
```

*Why: the owner's zoom-out. It names what the new frame reveals, what must survive, and the scale relationship that keeps the result from reading as a different photograph*

</example>

<example use_case="style-transfer-pure">

```text
Convert the entire photograph in image 1 into the painting style of image 2: thick, visible palette-knife strokes, a palette of ochre, cobalt blue and bone white, shadows flattened into single dark tones and edges softened where colors meet. Keep image 1's composition, the positions of the two figures on the bridge and the shape of the bridge exactly as they are.
```

*Why: a pure style transfer. The scope opener marks a whole-image change, the style is described by its attributes rather than by naming the painting, and the composition is pinned to the content image*

</example>

<example use_case="style-transfer-plus-edit">

```text
Convert the entire photograph in image 1 into the painting style of image 2: thick, visible palette-knife strokes, a palette of ochre, cobalt blue and bone white, and flattened shadows. In the same pass, replace the black umbrella held by the figure on the left with a red paper parasol, painted in that same style and casting a matching soft shadow on her shoulder. Keep image 1's composition, both figures' poses and the bridge unchanged.
```

*Why: the same transfer with one bounded change folded in. The new object is told to adopt the target style and its knock-on shadow is named, so it does not arrive looking pasted on*

</example>

### Multiple reference images

<rules id="multi-image">

- Refer to each input by its position, counting from one: "image 1" is the first, "image 2" the second. "The first image", "the second image" mean the same and are what the owner's upsampler writes. Pick one form and hold it for the whole prompt.
- ONE ROLE PER INPUT. Say what each image is for (subject, product, setting, style, garment) and weld every borrowed element to its source: "the bottle from image 3", never "the bottle".
- Say how the pieces relate: positions and interactions, not just the parts. "The woman in image 2 sits on the swing in image 1, with the cat from image 3 on her lap."
- Put the base image first. The first input sets the output's framing and shape, so the setting or photo being edited goes in that slot, and the prompt can name it as the base: "Use image 1 as the main image."
- An image can supply more than one thing (both the material and the background); name each role.
- Integrate an inserted object by naming its lighting, scale and contact with the scene: "lit by the window on the left", "make sure it blends naturally with the surroundings".
- A placement in words is a strong hint, not a hard position. When the exact spot matters, use box rows (below).
- Use every image you attach. An image with no stated job is left to the model to guess.

</rules>

<example use_case="multi-reference-three-inputs">

```text
Use image 1 as the main image. Insert the lake from image 2 on the left side of image 1, and make sure it blends naturally with the surroundings as if it is part of the garden view. Insert the ducks from image 3 into image 1, and make them appear as if they are near the lake on the grass
```

*Why: the owner's three-input composite. The base is named first, each insert is welded to its source image and given a position, and both inserts are told how to sit in the scene*

</example>

<example use_case="multi-reference-four-inputs-generation">

```text
Create a photograph of the woman from image 1 seated on the green wrought-iron bench from image 2, set in the autumn park from image 3, wearing the camel wool coat from image 4 buttoned over her own white shirt. She sits on the right half of the bench, facing frame-left, with fallen leaves around her shoes. Take her face, hair and earrings from image 1, the bench's shape and paint from image 2, the trees, path and soft overcast light from image 3, and only the coat from image 4. Keep her identity and accessories exactly as in image 1.
```

*Why: four inputs drawn into a new frame, so it is written as a generation request. Each image gets exactly one role, the borrowed parts are listed per image, and identity is pinned to its source*

</example>

<example use_case="multi-reference-pattern-transfer">

```text
Apply the exact colors and repeating pattern from image 2 to the glazed surface of the plate in image 1. Keep the plate's shape, rim, position, camera angle, table and lighting unchanged. The pattern follows the curved plate surface and appears fired into the ceramic glaze, with the existing glossy highlights remaining visible. Preserve the saturated burnt-orange, red-orange, ocher and near-black colors of image 2, especially away from reflected highlights.
```

*Why: the owner's material transfer. The donor supplies only pattern and color, the base keeps everything structural, and the physics of the new surface (following the curve, sitting under the glaze) is spelled out*

</example>

### Edits by box

When words cannot single out the target or place it, combine an instruction with box rows. Typical cases: one of several similar objects, an exact position or size, moving or resizing, removing one specific thing, holding specific elements in place.

<rules id="box-edit">

- In a box record, references count from ZERO: `<ref_image_0>` is the first input (the same image a plain prompt calls "image 1"), `<ref_image_1>` the second. This is the one place in the scheme that counts from zero.
- Open the instruction on the reference: "In <ref_image_0>, move ..." or "Modify <ref_image_0> by ...". When an element is taken from another reference, cite that reference too: "the lamp <lamp_1> from <ref_image_1>".
- Cite every involved element at its first mention with its `<id>`, every row exactly once, and no id without a row. End states (the new color, the new words in quotes, the pose) go in the instruction; the desc says what the element looks like.
- Edit rows have five keys: `"id"`, `"from"`, `"src_bbox"`, `"tgt_bbox"`, `"desc"`. `from` names the reference the element comes from (`"ref_image_0"`), or is `null` for new content. The owner's upsampler writes `"target"` for new content instead; read it the same way.
- Keep a thing in place: same box in `src_bbox` and `tgt_bbox`. Move or resize it: different boxes. Remove it: `tgt_bbox` null, and say in the instruction what to remove. Add, replace or recolor it: `from` null and `src_bbox` null, with its new look in `desc`.
- Add a keep row for each element that must not move. Unlisted areas usually hold, but an anchor makes it explicit.
- State additions and removals in the instruction as well as in the rows. The instruction and the table must agree.
- Close the instruction with one clause that everything else stays identical to the source.
- Do not carry box tokens into a plain edit. Without rows, write "image 1" and leave out every angle-bracket token.

</rules>

<template id="box-edit">

In <ref_image_0>, {operation} the {element} <{id}> {to its end state}. Keep the rest of the image completely unchanged, preserving the {element} <{id}>. [{"id": "{id}", "from": "ref_image_0", "src_bbox": [{y_min}, {x_min}, {y_max}, {x_max}], "tgt_bbox": [{new box, same box to keep, or null to remove}], "desc": "{what it looks like}"}]

</template>

<example use_case="box-edit-move">

```text
In <ref_image_0>, move the miniature grey amigurumi knight figure <knight_1> upwards and to the left along the yarn cliff <cliff_1>. Leave the polished steel tapestry needle <needle_1> in its original position in the air. Keep the rest of the image completely unchanged, preserving the blurred yarn backdrop <backdrop_1>, the large knitted dragon <dragon_1>, and the fiery orange thread <fire_1> suspended between them. [{"id":"knight_1","from":"ref_image_0","src_bbox":[500,150,850,350],"tgt_bbox":[194,55,544,255],"desc":"A miniature amigurumi knight figure crocheted from thick grey woolen yarn. It has visible, intricate stitches forming a rounded helmet shape and a cylindrical body, with tiny stubby arms reaching upwards against the cliff."},{"id":"backdrop_1","from":"ref_image_0","src_bbox":[0,0,1000,1000],"tgt_bbox":[0,0,1000,1000],"desc":"A soft, out-of-focus expanse of cream ivory and melange indigo knitted yarn, providing a blurred studio backdrop with tangible fiber fuzz catching the ambient light."},{"id":"cliff_1","from":"ref_image_0","src_bbox":[300,0,1000,450],"tgt_bbox":[300,0,1000,450],"desc":"A steep, uneven cliff face constructed from stacked, thick yarn skeins in rich shades of mustard yellow, terracotta, and melange indigo, featuring visible woven wool textures and loose, stray fiber strands."},{"id":"needle_1","from":"ref_image_0","src_bbox":[420,250,550,450],"tgt_bbox":[420,250,550,450],"desc":"A real, oversized polished steel tapestry needle, gleaming under the studio lighting. It features a blunt tip and an elongated eye, grasped like a weapon in the knight's yarn-stub hand."},{"id":"dragon_1","from":"ref_image_0","src_bbox":[100,600,950,1000],"tgt_bbox":[100,600,950,1000],"desc":"A large, fluffy knitted dragon made of highly textured, fuzzy yarn in terracotta and mustard yellow. It has a rounded snout, large crocheted eyes, and a wide-open mouth, with visible loose fibers creating a soft, tactile surface."},{"id":"fire_1","from":"ref_image_0","src_bbox":[350,400,650,650],"tgt_bbox":[350,400,650,650],"desc":"Curled, sculptural puffs of fiery orange angora thread, suspended in mid-air. The thread is highly textured, fuzzy, and chaotic, bursting from the dragon's mouth and stretching horizontally across the center."}]
```

*Why: the owner's move. Only the knight's two boxes differ; every other element has a keep row with matching boxes, every id is cited once, and the instruction says in words what the boxes say in numbers*

</example>

<example use_case="box-edit-remove">

```text
In <ref_image_0>, remove the orange tabby cat <cat_1> sitting on the folded blanket at the left of the fire, and fill its place with the continuation of the snow-block wall and the blanket's folds behind it. Keep the grey cat <cat_2> and the black cat <cat_3> exactly where they are, and keep the rest of the image completely unchanged. [{"id":"cat_1","from":"ref_image_0","src_bbox":[265,40,855,400],"tgt_bbox":null,"desc":"An orange tabby cat sitting on a folded blanket."},{"id":"cat_2","from":"ref_image_0","src_bbox":[300,420,820,640],"tgt_bbox":[300,420,820,640],"desc":"A grey short-haired cat lying curled beside the fire."},{"id":"cat_3","from":"ref_image_0","src_bbox":[280,680,840,960],"tgt_bbox":[280,680,840,960],"desc":"A black cat sitting upright with its tail wrapped around its paws."}]
```

*Why: a removal, built on the owner's remove row. The removed element has a null target box, the instruction says what fills the gap, and the two cats that must stay get keep rows so the removal cannot pull them along*

</example>

<example use_case="box-edit-from-second-reference">

```text
Modify <ref_image_0> by placing the ceramic table lamp <lamp_1> from <ref_image_1> on the left end of the oak sideboard <sideboard_1>. Keep the rest of the room exactly unchanged, preserving the framed print <print_1> above the sideboard. [{"id":"lamp_1","from":"ref_image_1","src_bbox":[80,250,950,750],"tgt_bbox":[300,120,560,280],"desc":"a ceramic table lamp with a linen shade"},{"id":"sideboard_1","from":"ref_image_0","src_bbox":[540,60,880,940],"tgt_bbox":[540,60,880,940],"desc":"an oak sideboard"},{"id":"print_1","from":"ref_image_0","src_bbox":[120,330,420,670],"tgt_bbox":[120,330,420,670],"desc":"a framed botanical print"}]
```

*Why: the owner's product placement with the source reference cited, as the upsampler spec asks. The lamp's from is ref_image_1, the SECOND input; its source box marks it in that image and its target box marks the spot in the first*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field on any FLUX 3 Image surface.
- Describe the state you want instead of the one you do not: "an empty promenade" rather than "no crowds"; "clean, unmarked surfaces" rather than "no text".
- If an unwanted element persists, put its replacement early, in the sentence that sets the scene, not in a trailing clause.
- A short plain negation is tolerated and appears in the owner's own prompts ("No text."), but it is the fallback, not the method.
- In an edit, removal is an instruction, not a negation: "Remove the cat from the sofa".
- On distilled Klein there is no guidance for a negative to push against, so positive description is the only lever. On Klein Base guidance is live, which is the place to try steering when wording alone fails.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Writing long behind an upsampler: on the full model the prompt is rewritten anyway, so extra prose only helps where it fixes something. Write short and read back the expanded prompt it returns.
- Writing short to a bare model: Klein run directly takes what you type, so a one-line prompt gives a generic image and a one-line edit can reframe the shot. Write the full caption or the full instruction.
- Off-by-one references: "image 1" and `<ref_image_0>` are the same picture. Converting between a plain edit and a box edit means renumbering every reference.
- Box tokens in a plain edit, or prose numbering in a box record: each form belongs to its own mode.
- x before y: boxes are `[y_min, x_min, y_max, x_max]`. Writing them x-first puts every element in the wrong place.
- Fractions in a prompt: box files for some tools use 0 to 1; the prompt grid is 0 to 1000 integers.
- An uncited row, or an id cited twice: every row is cited exactly once in the caption.
- Coordinates or appearance in the wrong place: positions go in the boxes and in words in the caption, appearance goes in the desc, no numbers in the caption.
- Boxes as masks: an element can spill out of its box, and a tiny box may come back empty.
- Carrying FLUX.2 habits in: there is no whole-prompt JSON schema here and no text-to-image hex pinning. Describe the palette in words; save hex codes for edits.
- Confusing the two Kleins: FLUX.2 [klein] never upsamples and uses its own reference rules; FLUX 3 Image Klein runs behind an upsampler on the API.
- Hedging: "a notebook or a tablet" and "appears to be" make the plan ambiguous. Decide.
- Naming an artwork for a style: describe its palette, stroke and texture instead.
- Expecting web grounding from Klein: only the full model searches. Describe real things Klein must get right.
- Expecting untouched pixels from a local edit: exact restoration of unedited regions happens on the API, not on the open weights.
- Quality boosters: masterpiece, 8K, highly detailed. They name nothing visible.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

- Official (Black Forest Labs), prompting guides: [FLUX prompting guide](https://docs.bfl.ai/guides/prompting_summary), [prompt basics](https://docs.bfl.ai/guides/prompting_unified_basics), [building a good prompt](https://docs.bfl.ai/guides/prompting_unified_building), [style, aesthetics and text](https://docs.bfl.ai/guides/prompting_unified_style), [technical parameters](https://docs.bfl.ai/guides/prompting_unified_technical), [layout prompts](https://docs.bfl.ai/guides/prompting_layout), [prompt reference](https://docs.bfl.ai/guides/prompting_unified_reference), [image editing](https://docs.bfl.ai/guides/prompting_editing_overview), [single-reference editing](https://docs.bfl.ai/guides/prompting_editing_single_reference), [multi-reference editing](https://docs.bfl.ai/guides/prompting_editing_multi_reference).
- Official (Black Forest Labs), FLUX 3 Image docs: [overview](https://docs.bfl.ai/flux_3/flux3_image_overview), [text to image](https://docs.bfl.ai/flux_3/flux3_image_generate), [image editing](https://docs.bfl.ai/flux_3/flux3_image_layout), [bounding boxes](https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes), [FLUX 3 Image Klein](https://docs.bfl.ai/flux_3/flux3_image_klein), [Klein launch post](https://bfl.ai/blog/flux-3-image-klein).
- Official (Black Forest Labs), open weights: [FLUX 3 Image Klein](https://huggingface.co/black-forest-labs/flux-3-image-klein), [Klein Base](https://huggingface.co/black-forest-labs/flux-3-image-klein-base), [Klein prompt upsampler](https://huggingface.co/black-forest-labs/flux-3-image-klein-pup), [reference inference code](https://github.com/black-forest-labs/flux-3-image-klein). The upsampler repository's `system_prompts.json` holds its four instructions (text-to-image, edit, and a box version of each); the caption, edit and box rules here are read from them and from the reference code's box handling.

Coverage note: the owner's surfaces disagree in several places, resolved in `sources/flux-3-image/flux-3-image-notation-resolution.md`. The two that matter most: the Klein model card asks for an edit written as a complete caption of the target, while the docs and the upsampler both write instructions (the guide teaches instructions and keeps the caption form as an alternative); and the card's "the n-th reference as <ref_image_n>" leaves the base open, while the box docs, the upsampler and the reference code all count from zero. The docs' advice to write short and their upsampler's 100 to 350 word captions are not in conflict once the access split is drawn: short is for a surface that expands, long for one that does not. The full model's own expander is not published; the Klein upsampler's instructions stand in for it, which the owner never claims. Several examples on the shared prompting pages were generated with FLUX.2 and are labelled as such there; only FLUX 3 examples are used here. The "Migrate from FLUX.2" page linked from the prompting guide redirects to the bounding-box page. Request fields, resolutions, reference counts and pricing are provider surface and are deliberately absent.

Last verified: 2026-10-15.
