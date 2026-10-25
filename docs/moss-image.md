---
guide: "MOSS-Image"
prompt_scheme: "moss-image"
models:
  - { id: "MOSS-Image-SFT", access: "open-weights", tier: "std", caps: [text-to-image, text-rendering, layout-control, json-prompts], best_for: "the default. A supervised fine-tune of Base on the same pipeline; the owner's comparison shows clearer text grouping and a more organized layout. Dense in-image text, posters, infographics and layout-controlled designs" }
  - { id: "MOSS-Image-Base", access: "open-weights", tier: "base", caps: [text-to-image, text-rendering, layout-control, json-prompts], best_for: "the pretrained checkpoint with no post-training or guidance distillation, kept for LoRA training. Guidance responds and needs tuning; every image in the owner's showcase was made with it" }
capabilities: [text-to-image, text-rendering, layout-control, json-prompts]
prompt:
  languages: ["en", "zh"]
  literal_text: "quote the exact words, in their own language and case, and put the intended line breaks into the text itself: real line breaks in a prose prompt, escaped \\n inside a JSON layout. Describe the typography and the surface the text sits on"
  length_strategy: "long and detailed. Training captions came at three lengths (a sentence, a paragraph, a full description of composition, subjects, scene and visible text), and in the owner's tests detailed prompts beat short ones by a wide margin, most of all on text. The owner's showcase prompts run from one line to several thousand characters"
  auto_expand_behavior: "none. The prompt reaches the text encoder as written, with no system prompt and no rewriting. The owner publishes a separate prompt-enhancer skill for an external LLM that writes the long caption or layout for you"
  negatives: "a short list of artifact words works, because the training captions describe artifacts (watermarks, blur, compression) rather than filtering them out. The owner's suggested list for Base is 'nsfw, worst quality, bad anatomy, watermark, jpeg artifact'; the SFT card's default negative is empty. Request-specific exclusions also work as a closing sentence in the prompt"
  structured_json: "YES, two ways besides prose. A JSON layout ('summary' plus a flat 'items' array with boxes) controls where text and objects go; Danbooru-style tag sequences are also accepted"
  layout_boxes: "[y_min, x_min, y_max, x_max] in whole pixels with the CANVAS CENTRE as origin, x rightward and y downward, declared with \"bbox_coord_space\": \"abs_centralized\" and \"bbox_format\": \"yxyx\". The boxes assume the exact width and height you generate at"
sources:
  official: ["https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT", "https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base", "https://github.com/OpenMOSS/MOSS-Image", "https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md", "https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE_ZH.md", "https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/SKILL.md", "https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/references/layout.md", "https://github.com/OpenMOSS/MOSS-Image/tree/main/assets/images", "https://arxiv.org/abs/2610.23374"]
last_verified: "2026-10-25"
---

# MOSS-Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and step settings, and code, consult the host's docs or the spec table; they are out of scope here.
- MOSS-Image is TEXT-TO-IMAGE ONLY. The owner states the model "does not directly condition on reference images or support image editing", so this guide has no editing or multi-image section. Third-party edit LoRAs exist and are not covered.
- Three prompt forms are native and share one text pathway: natural-language prose, Danbooru-style tag sequences, and a JSON layout with bounding boxes. Prose is the default; reach for a layout when exact placement matters.
- Write in English by default; it has the most training data. Chinese prompts work. Visible text stays in whatever language it should appear in.
- Nothing rewrites the prompt. What you write is what the model reads, so the detail has to be in it.
- MOSS-Image boxes are NOT the FLUX 3 Image convention. Both write y first, but MOSS-Image counts real pixels from the centre of the canvas. Never carry boxes between the two.

</rules>

## TL;DR

<template id="quickstart">

{medium and register}. {subject and action, with the appearance that matters}. {setting}. {camera and framing}. {lighting, materials, palette, mood}. {where the text sits and how it looks}, reading exactly:
"{line one}
{line two}"
{request-specific exclusion, if any}.

</template>

## Models and when to use which

- `MOSS-Image-SFT` is the one to run. It is fine-tuned from Base with "the same architecture and inference pipeline", and the owner's side-by-side shows it producing "clearer text grouping and a more organized whiteboard layout".
- `MOSS-Image-Base` is the raw pretrained checkpoint. The owner says it "has not undergone any post-training or distillation of inference parameters such as CFG", so guidance is live and needs tuning, which also makes it the checkpoint to train LoRAs on. Every showcase image in the owner's repository was made with Base, so its examples are Base prompts; they transfer to SFT unchanged.
- The prompt grammar is identical for both. Settings differ; see the spec table.

## How the model reads prompts

- The prompt goes to a Qwen3.5-9B text encoder as a single user message, with no system prompt. No enhancer runs inside the pipeline.
- TRAINING CAPTIONS CAME IN THREE LENGTHS: "a short sentence, a medium paragraph, or a detailed description of composition, subjects, scene attributes, and visible text". All three are in distribution, but detail wins. In the owner's tests short prompts scored about half what detailed ones did overall, and on text rendering 1.30 against 4.72 out of 5.
- Long prompts are normal here. Several of the owner's showcase prompts run past a thousand words, and its whole prompt-enhancer exists to produce them.
- The owner pairs short prompts with stronger guidance. If a one-line prompt is what you have, expect the host to need more guidance than the default.
- VISIBLE DEFECTS HAVE NAMES. The owner did not filter training images for watermarks, blur or compression; it described them in the captions instead ("Annotate rather than filter"). Words such as "watermark", "blurry" and "jpeg artifact" are therefore things the model recognizes, which is why they work in a negative prompt and as exclusions.
- English has the most training data; captions were "predominantly in English, without dedicated Chinese-caption annotation". Chinese prompts still work, as several owner showcase prompts are written entirely in Chinese, and Chinese in-image text renders well.

## Prompt structure

<rules id="structure">

- Describe visible choices. The owner's enhancer lists them: "subject and action, relevant appearance, setting, camera/framing, medium, lighting, materials, palette and mood". Put spatial relations in words ("occupies the right half of the frame").
- Write cohesive prose, in paragraphs if the image is complex. Do not sprinkle coordinates or JSON fields into a prose caption to make it look structured; use a real layout instead.
- Leave out what cannot be seen. The owner rules out "redundant quality tags, unrequested style changes, arbitrary word budgets and invisible process notes".
- For a designed image (poster, infographic, page), compose the words and the pictures together: "Establish reading order, relative prominence, coherent groups and readable text at the chosen pixels."
- Write the real copy. Never "headline here" or "some explanatory text"; the model renders what you write.
- Keep a minimalist brief minimalist and develop a rich one without forcing a generic title-hero-footer template on it.
- State request-specific exclusions as a closing sentence ("No prominent readable lettering, logos, or watermarks.").

</rules>

<template id="general">

{medium, register and overall look}. {subject: who or what, appearance, action}. {setting and background, with depth cues}. {camera: shot size, angle, lens feel, framing and where things sit}. {lighting, materials, palette, grade, mood}. {visible text: placement, typography, surface, then the exact words in quotes with their line breaks}. {exclusions specific to this image}.

</template>

<example use_case="photoreal-flagship">

```text
A cinematic, photorealistic nighttime scene of a small neighborhood convenience store on a quiet, rain-soaked street. The warmly illuminated storefront occupies the right half of the frame, while the street recedes into soft mist on the left. A lone young adult wearing a charcoal coat stands just outside the entrance beneath a transparent umbrella, seen in three-quarter rear view, gazing through the glass. Amber light reveals shelves inside and spills across the sidewalk, mingling with muted teal neon reflections in shallow puddles. Individual raindrops bead on the umbrella and catch the storefront light; fine streaks of rain remain visible against the darker street. A slightly weathered bicycle leans beside the entrance. Distant apartment windows and a few out-of-focus streetlights add depth without distracting from the figure. Eye-level wide shot, 35mm lens aesthetic, natural perspective, balanced negative space, restrained teal-and-amber color grading, realistic wet asphalt and glass textures, soft highlight bloom, subtle film grain, and gentle atmospheric depth. Quiet, intimate, and nostalgic rather than dramatic; believable lighting, with the figure clearly silhouetted against the warm window. No prominent readable lettering, logos, or watermarks.
```

*Why: an owner showcase prompt. Medium first, then the frame's halves in words, the subject, light and texture, a camera paragraph, a mood that says what it is not, and one closing exclusion aimed at this image's real risk: stray shop signage*

</example>

## Text rendering

The model's headline skill. The owner benchmarks pages of English and Chinese text and scores 96.3 percent coverage.

<rules id="text">

- QUOTE THE EXACT WORDS and keep them as they should appear: same language, case, punctuation. Do not translate or romanize them.
- PUT THE LINE BREAKS IN THE TEXT. "The model can render text and insert line breaks automatically, but the result may not always match your expectations." The owner's technical report shows explicit breaks fix ambiguous rows during denoising: "Text line breaks are also a form of layout." In prose, use real line breaks inside the quotes; in JSON, use escaped `\n`.
- Introduce a long passage with "reads exactly:" or "is handwritten in Chinese:" and then the quoted block. This mirrors how the long training captions present text.
- Say where the text is, on what surface, and how it looks: sticky note, chalkboard, glass panel, printed page; handwriting or typeset; color, weight, size relative to the rest.
- Ask for legibility in plain words when it matters ("Keep all text sharp, fully visible, and free of glare").
- Fit the text to its space. A short Chinese title needs a different footprint from a paragraph of Latin text; give long copy a surface large enough to hold it at a readable size.
- Very long Chinese passages are the weakest case in the owner's own benchmark. Break them into lines and, if exact placement matters, into separate layout items.
- Suppress text you did not ask for with an exclusion ("No prominent readable lettering, logos, or watermarks.").

</rules>

<example use_case="handwritten-note-multiline">

```text
A wide view of a refrigerator beside a kitchen counter with a fruit bowl. A small sticky note on the refrigerator door is handwritten in Chinese:
"记得买牛奶和鸡蛋！
牛奶两盒，鸡蛋一打。
顺便带一袋面包。"
```

*Why: the owner's model-card example, its curly quotes made straight. The scene is set in English, the note's surface and script are named, and each line of the note is its own line in the prompt so the breaks land where intended*

</example>

<example use_case="dense-text-chalkboard">

```text
A candid classroom photograph, slightly off-center, with a worn dark green chalkboard filling most of the frame. Uneven window light, soft shadows, chalk dust, eraser streaks, subtle camera grain. Visible board frame and chalk tray, a blurred desk corner in the foreground. Natural, slightly irregular white chalk handwriting, not polished typography or a flat blackboard graphic. Keep all text sharp, fully visible, and free of glare.

The chalkboard reads exactly:

"MOSS-Transcribe-Diarize is our flagship SOTA model family
for turning real-world long-form audio into structured,
speaker- aware transcripts in one pass. Instead of stitching
together separate ASR and diarization systems, these
models jointly perform speech transcription and speaker
diarization, producing time-aligned text with precise
timestamps and consistent speaker labels such as [S01], [S02], and beyond."
```

*Why: an owner showcase prompt (one dash made a comma). The surface gets a full photographic description, the handwriting style is pinned against the typeset look the model might default to, legibility is requested outright, and a seven-line paragraph is pre-broken into lines*

</example>

<example use_case="chinese-prompt-long-text">

```text
一个穿着"MOSI"标志的T恤的中国美女正拿着黑色的马克笔面向镜头微笑。她身后的玻璃板上手写体写着 "一、MOSS-Image的技术路线：5B 的单流 DiT 模型，基于 Muon 训练。二、MOSS-Image的模型特色：1、复杂文字渲染。支持中英渲染、自动布局； 2、使用 Layout 进行精准图像控制，支持文字编辑和物体增减等自由编辑。三、MOSS-Image的后续发展：探索 R2I 参考生图、助力生成式AI发展。"
```

*Why: the owner's user-guide example, written entirely in Chinese with mixed Chinese and English text to render. It relies on automatic line breaking; add explicit breaks inside the quotes when the line structure matters*

</example>

## Tag sequences

<rules id="tags">

- Tag prompts are accepted. The owner's recommended order is "Quality -> Score -> Meta -> Year -> Character -> Series -> Artist -> General".
- Write an artist as `@name` (the owner's placeholder is `@foo bar`). Write a character with its series in parentheses, as in `amiya (arknights)`.
- Tags and quoted text mix: a tag list can carry `with "Rhodes Island" on her clothes`.
- The owner's Gradio app prefills `best quality, masterpiece` as a prompt prefix, and its showcase uses `general` as a rating tag and `most attractive face` as a meta tag.
- Prose is still the stronger form for anything beyond character art. The owner's technical report lists no tag-captioned dataset in pretraining, so tag skill rests on later training the report does not describe; treat tags as a supported option, not the primary interface.

</rules>

<example use_case="tag-order">

```text
best quality, highres, hatsune miku, vocaloid, @foo bar, 1girl, blue hair
```

*Why: the owner's own tag-order example. Quality, then character, then series, then the artist written with an at-sign, then general tags. Replace `@foo bar` with a real artist name*

</example>

<example use_case="tags-with-rendered-text">

```text
general, 1girl, best quality, most attractive face, cosplay, amiya (arknights), with "Rhodes Island" on her clothes, carring a sword
```

*Why: an owner showcase prompt, kept as written including its typo. A rating tag, quality and meta tags, a character with series, and a short quoted phrase to render, all in one tag sequence*

</example>

## Layout prompts (JSON)

The owner marks layout control as experimental. It is still the model's strongest tool for placement: in the owner's tests JSON layouts outscored every prose strategy.

<rules id="layout">

- Use a layout when "specific text placement, a poster, several panels, or controlled object relationships would benefit from bounding boxes. A detailed image does not automatically need Layout."
- The whole prompt is one JSON object with a `summary`, a flat `items` array, and two markers: `"bbox_coord_space": "abs_centralized"` and `"bbox_format": "yxyx"`. Send it as the prompt, compact on one line, with non-ASCII text left unescaped.
- `summary.caption` (required) describes the whole image and its global treatment. Optional: `meta`, a list of medium or genre tags (`"poster"`, `"photograph"`); `canvas`, one of `single`, `multi_panel`, `collage`; `palette`, a list of colors.
- Each item has a `label`, a `caption` and a `bbox`. Labels: `object`, `character`, `text`. A `text` item also needs `text`, the exact characters with line breaks as `\n`. Optional `tags` and `palette` lists. The owner's own showcase also uses `panel` for a full-frame background region.
- An item's caption describes its appearance; for text, its typography and surface. Global style belongs in `summary.caption`, not repeated per item.
- BOXES: `[y_min, x_min, y_max, x_max]`, Y FIRST, in whole pixels, origin at the CENTRE of the canvas, x growing right and y growing down. A 1024x1024 canvas runs from -512 to 512 on both axes.
- To convert an ordinary top-left box `x1, y1, x2, y2` on a W x H canvas: `[y1 - H/2, x1 - W/2, y2 - H/2, x2 - W/2]`. Round the top and left edges down and the bottom and right edges up. Check every value: y within plus or minus H/2, x within plus or minus W/2, and each box with positive height and width.
- GENERATE AT THE SAME WIDTH AND HEIGHT the boxes were drawn for. The dimensions are not in the prompt, so a mismatch silently moves everything. The owner chose absolute pixels because they hold up better at unusual sizes than normalized boxes.
- A box is a placement, not an instruction to draw a frame, panel or sticker. Boxes may overlap where the picture overlaps. Split text into separate items only when the pieces need independent placement.
- Make the box fit the copy: check that the line breaks, text length and glyph size can fit at the resolution you will render.
- Do not invent fields. Extra keys such as `id`, `parent` or `children` are not part of the public format.
- EDIT BY REGENERATING. Change a text string, an item caption or a box and generate again; the owner swaps a poster title and rearranges infographic panels this way. Local details will vary between runs.
- The owner says natural language and structured input can be combined, but publishes no format for it. Put the prose in `summary.caption`.

</rules>

<template id="layout">

{"summary":{"meta":["{medium}"],"canvas":"single","caption":"{whole-image description and global style}"},"items":[{"label":"text","caption":"{typography and surface}","text":"{exact words, \n for breaks}","bbox":[{y_min},{x_min},{y_max},{x_max}]},{"label":"object","caption":"{appearance}","bbox":[{y_min},{x_min},{y_max},{x_max}]}],"bbox_coord_space":"abs_centralized","bbox_format":"yxyx"}

</template>

<example use_case="layout-poster-1024-square">

```text
{"summary":{"meta":["poster"],"canvas":"single","caption":"A minimalist travel poster with a cream background, a blue mountain illustration, and the title EXPLORE at the top."},"items":[{"label":"text","caption":"Large dark-blue uppercase title centered at the top.","text":"EXPLORE","bbox":[-416,-384,-288,384]},{"label":"object","caption":"A flat blue mountain illustration in the lower center.","bbox":[-192,-288,384,288]}],"bbox_coord_space":"abs_centralized","bbox_format":"yxyx"}
```

*Why: the owner's user-guide example, compacted to one line, for a 1024x1024 canvas. The title box runs from y -416 to -288 (96 to 224 pixels down from the top edge) and x -384 to 384 (centered); the mountain sits below it. Generate at exactly 1024x1024*

</example>

<example use_case="layout-product-campaign-1536x1024">

```text
{"summary":{"meta":["product campaign","studio photography"],"canvas":"single","caption":"A warm studio campaign for a handmade ceramic cup, with an ivory backdrop, soft side lighting and restrained dark-green typography. Keep the ceramic texture tactile and the composition calm."},"items":[{"label":"object","caption":"An ivory ceramic cup with a rounded handle, fine speckled glaze and a soft contact shadow, photographed at a three-quarter angle.","bbox":[-288,-592,352,32]},{"label":"text","caption":"Large dark-green Chinese title in crisp, moderately heavy lettering, with generous spacing and no backing panel.","text":"把日常，过成诗。","bbox":[-240,160,-64,640]},{"label":"text","caption":"Smaller dark-green Chinese supporting copy, comfortably legible on two lines.","text":"一杯温暖\n一刻从容","bbox":[0,160,144,608]}],"bbox_coord_space":"abs_centralized","bbox_format":"yxyx"}
```

*Why: the owner's layout reference example, compiled with the owner's own converter for a 1536x1024 canvas. The cup's top-left box (x 176 to 800, y 224 to 864) becomes [-288, -592, 352, 32] after subtracting 512 from y and 768 from x and putting y first. The two text items stay separate because they are placed independently, and the two-line copy carries its break as \n*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- For Base, the owner recommends "nsfw, worst quality, bad anatomy, watermark, jpeg artifact". Its showcase varies the list per image (adding "low quality", "blurry", "ugly face", "cropped") and sometimes leaves it empty.
- For SFT, the model card's default negative is empty. Start there and add artifact words only for a defect you actually see.
- Artifact words work because the training captions name artifacts instead of filtering them out. Keep the negative to such concrete defects; long negative essays have no support in the owner's material.
- Exclusions specific to one image go in the prompt as a closing sentence: "No prominent readable lettering, logos, or watermarks."
- In a layout, there is no exclusion field in the public format. Put the exclusion in `summary.caption`.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- A one-line prompt for a text-heavy image: short prompts are where the model fails on text. Write the full description and the exact copy.
- Text with no line breaks: the model guesses where lines break. Put the breaks in.
- Placeholder copy ("headline here"): it gets rendered. Write the real words.
- Translating the text you want shown: keep it in its own language and script.
- Boxes in x-first order or from the top-left corner: MOSS-Image boxes are y-first and centered. Convert, then check every value against plus or minus half the canvas.
- Boxes on a 0-1000 grid copied from another model: these are pixels, not a normalized grid.
- Generating a layout at a different size than it was drawn for: every element shifts. Use the exact width and height.
- Treating a box as a frame: a box marks where something goes; it does not draw a border.
- Inventing layout fields: stick to `summary`, `items`, `label`, `caption`, `text`, `bbox`, `tags`, `palette`, `meta`, `canvas` and the two markers.
- Coordinates or JSON fragments inside a prose caption: write positions in words, or write a full layout.
- Quality-tag padding in prose ("masterpiece, 8K, best quality" bolted onto a description): the owner's enhancer calls these redundant. Tags belong in tag-sequence prompts.
- Asking for an edit of an existing image or a reference likeness: the model has no image input.

</rules>

## Sources

Trust order is official > provider > community; official wins on any conflict. The owner's user guide, model cards and prompt-enhancer skill describe how the released checkpoints are prompted, so where they differ from the technical report, which describes the pretraining run, the guide follows them. The adjudications are recorded in `sources/moss-image/moss-image-notation-resolution.md`.

- Official (OpenMOSS / MOSI): the [MOSS-Image-SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT) and [MOSS-Image-Base](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base) model cards, the [GitHub repository](https://github.com/OpenMOSS/MOSS-Image) with its [user guide](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md) and [Chinese user guide](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE_ZH.md), the [prompt-enhancer skill](https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/SKILL.md) and its [layout reference](https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/references/layout.md), the [showcase prompts](https://github.com/OpenMOSS/MOSS-Image/tree/main/assets/images), and the [technical report](https://arxiv.org/abs/2610.23374).

Last verified: 2026-10-25.

Coverage notes. No approved provider (FAL, WaveSpeed) lists MOSS-Image, so every rule here is the owner's. The technical report documents only pretraining: it says nothing of SFT, tag prompts, negative prompts or recommended guidance, and it describes the summary/items layout as trained on a 0-1000 grid, while every released usage surface and every JSON prompt in the owner's showcase uses centre-origin pixels with explicit markers; the guide follows the released surfaces. The report also documents a second layout schema (`scene_type`, `gen_brief`, `elements` with `obj`/`text` types and a salience field) that several owner showcase prompts use; the owner's enhancer says to use summary/items for new drafts, so that schema is recorded but not taught. Tag-prompt rules come from the user guide alone. The format for mixing prose with item boxes is stated to exist and not published. Community few-step distillations and edit LoRAs are out of scope.
