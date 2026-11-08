---
guide: "Ideogram 4 and 4.5 (image)"
prompt_scheme: "ideogram-4"
models:
  # Ideogram 4 is one model: the open weights (nf4 and fp8 builds) and the hosted "Ideogram 4.0" on Ideogram's API take the same caption.
  - { id: "ideogram-4", access: "open-weights", tier: "base", caps: [text-to-image, text-rendering, layout-control, color-control], best_for: "typography and graphic design (posters, logos, signage, packaging), precise layout, and in-image text; strong photoreal and illustration as well. Ideogram also serves it as Ideogram 4.0, with remix and a transparent-background variant on its own service" }
  - { id: "ideogram-4.5", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, masked-edit, text-rendering, layout-control, color-control, transparency], best_for: "the same JSON caption for generation, plus instruction editing that leaves the rest of the image intact over many turns: product colorways and restaging, interior and architecture swaps, text edits and translation inside a design, photo restoration, and a consistent character from reference images" }
capabilities: [text-to-image, image-edit, multi-image-reference, masked-edit, text-rendering, layout-control, color-control, transparency]
prompt:
  format: "structured JSON caption (high_level_description, style_description, compositional_deconstruction), shared by every Ideogram 4.x surface. SPLIT BY ACCESS: on the open weights the caption is required, and plain text sent raw does not work and trips the safety filter, so plain text must go through magic prompt first; Ideogram's own app and API accept plain language and convert it into the caption themselves. Ideogram 4.5 edits take a plain-language instruction"
  languages: ["en", "multilingual"]
  literal_text: "in a caption, put the exact words in a text element's `text` field and its styling in `desc`; one text element per block; use \\n for line breaks. In plain language and in edit instructions, put the exact words in straight double quotes, name the text early, and say where it sits; English and short strings render most reliably"
  length_strategy: "exhaustive and relationship-dense; name and describe every object and every text block; the model was trained on captions that describe everything in the image. Edit instructions are the opposite: one change per turn, plus the details that must stay"
  auto_expand_behavior: "SPLIT BY ACCESS. Open weights: magic prompt (an LLM) expands plain text into a full caption and is on by default in the reference pipeline; without it, write the caption yourself. Ideogram's service: Magic Prompt on rewrites and expands the prompt (and rewrites pasted JSON too); off keeps your wording and only converts it into a caption; valid JSON skips it unless it is on. Ideogram 4.5 edits are always converted into a structured edit prompt, and Magic Prompt does not apply to them"
  negatives: "no negative field on any 4.x surface; describe the desired state and omit what you do not want; the caption is additive. Ideogram's docs say models latch onto the word after 'no', 'without' or 'not', so describe the absence instead ('an empty street'). In 4.5 edits, exclusions take the form of a keep sentence"
sources:
  official: ["https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md", "https://huggingface.co/ideogram-ai/ideogram-4-fp8", "https://ideogram.ai/blog/ideogram-4.0/", "https://github.com/ideogram-oss/ideogram4", "https://docs.ideogram.ai/prompting/prompting", "https://docs.ideogram.ai/prompting/prompt-structure", "https://docs.ideogram.ai/prompting/text-in-images", "https://docs.ideogram.ai/prompting/json-prompting", "https://docs.ideogram.ai/prompting/fix-common-problems", "https://docs.ideogram.ai/create/reference-images", "https://docs.ideogram.ai/edit/masks-and-inpainting", "https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-4-5", "https://developer.ideogram.ai/v2/api-reference/images/precise-edit/ideogram-4-5", "https://ideogram.ai/models/4.5/", "https://ideogram.ai/blog/ideogram-4-5-product-photo-editing/", "https://ideogram.ai/blog/ideogram-4-json-prompting/"]
  provider: ["https://fal.ai/models/ideogram/v4", "https://fal.ai/models/ideogram/v4.5/edit"]
  community: []
last_verified: "2026-11-08"
---

# Ideogram 4 and 4.5: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the open-weight Ideogram 4 release (its nf4 and fp8 builds are quantizations of one model and take the same prompts), the same model served by Ideogram as Ideogram 4.0, and the API-only Ideogram 4.5, which takes the same caption and adds editing.
- The native prompt is a structured JSON caption. Ideogram 4 was trained exclusively on it, and Ideogram's docs state that 4.5 and 4.0 use the same format. On the open weights it is required: plain text sent raw does not work and trips the safety filter, so run it through magic prompt or write the caption. Ideogram's own service accepts plain language and converts it.
- Editing, reference images, and masks belong to Ideogram 4.5. The open release is text-to-image only.
- Pin every relationship. The model was trained on captions that name and describe every object and text block, so the surest way to get everything rendered is to enumerate it.
- Ideogram 3.0 is prompted differently (plain text with a negative prompt and style presets) and has its own guide.

</rules>

## TL;DR

Write a JSON caption. The minimal valid form is a high-level summary plus a `compositional_deconstruction` that names the background and every element:

<template id="quickstart">

```json
{
  "high_level_description": "one or two sentence summary of the whole image",
  "compositional_deconstruction": {
    "background": "the setting or environment",
    "elements": [
      {"type": "obj", "desc": "a subject, described in detail"},
      {"type": "text", "text": "exact words to render", "desc": "font, color, placement"}
    ]
  }
}
```

</template>

For an Ideogram 4.5 edit, write one instruction instead:

<template id="edit-quickstart">

{The one change, with its target named precisely}. Keep {the fragile details that must survive, such as labels, logos, faces} and everything else exactly the same.

</template>

## Models and when to use which

- `ideogram-4` (open weights): one model in nf4 and fp8 quantizations that prompt identically; pick a build for speed or memory, not for prompting. Strongest at typography and graphic design (posters, logos, signage, packaging, multi-line and multi-font text) and at precise layout; a capable photoreal and illustration model across styles. Text-to-image only.
- Ideogram 4.0 on Ideogram's service: the same model and caption. Ideogram adds a remix mode (one source image plus a prompt) and a transparent-background variant, and takes no reference images. Ideogram's docs point to it for very wide formats.
- `ideogram-4.5` (API only): Ideogram's newest model. It generates from the same caption or from plain language, and it edits: an instruction, optional reference images, and an optional mask. Its precise-edit mode copies every pixel the edit did not need to change, so an image survives many rounds of edits without the drift that whole-image re-rendering builds up.
- Pruna sells P-Image-Ideogram, "built in collaboration with Ideogram", and states it "uses the same Ideogram 4.0 structured-caption schema"; prompt it with this guide. It adds thinking levels on Pruna's side, and Pruna's advice is to match the level to the prompt: higher levels suit detailed prompts and "on vague prompts, High can add unrequested detail", while lower levels suit simple ones. Its prompt upsampling is the magic-prompt step described below; Pruna says to switch it off "when the spec is final".

## How the model reads prompts

- It reads structured JSON captions natively. Each training caption exhaustively describes everything in the image, so the model expects the same exhaustive, relationship-dense input.
- How plain text is handled depends on where the model runs. On the open weights, write the caption yourself or let magic prompt expand plain text into one; bare plain text does not work. On Ideogram's service, plain language is converted into a caption for you, with or without Magic Prompt's expansion.
- It is literal. Ideogram's own advice for 4.0 is to trade mood words ("moody", "vibrant", "nice lighting") for concrete ones: "warm directional light from the upper left", a named medium, specific colors.
- It rewards naming everything. One element per object or text block, each with its own description, is how every requested thing gets rendered.
- It honors structure. Color comes from a hex palette, placement from bounding boxes, and in-image text from typed text elements, rather than from adjectives buried in a sentence.
- Aspect ratio and global intent go in `high_level_description` as plain words ("a square 1:1 poster", "16:9 framing"). Weight syntax and flags (`::1`, `(important)`, `--ar`) are read as words, not commands.

## The JSON caption schema

<rules id="schema">

- Three top-level fields, in this order: `high_level_description` (a one or two sentence summary that reads like a natural prompt), `style_description` (optional), and `compositional_deconstruction` (required).
- Always include `high_level_description`. The open schema calls it optional but strongly recommended; Ideogram's service reads a caption without it as plain text.
- `compositional_deconstruction` must contain `background` (a string, first) then `elements` (a list), both required.
- Key order is strict. The model was trained on a fixed key order, and the open pipeline's caption verifier warns on unknown, missing, or out-of-order keys. Ideogram's service reorders keys inside each block for you, but the strict form works everywhere, so write it.
- Hex colors are uppercase `#RRGGBB` (`#1B1B2F`, not `#1b1b2f` or `#fff`). Ideogram's service also accepts lowercase; the open schema does not.
- Serialize compactly (no superfluous whitespace) and keep non-ASCII characters literal rather than as escape sequences. In Ideogram's app, paste the JSON without Markdown code fences.
- On 4.5, a very long caption can lose its last elements, so list the most important elements first.

</rules>

<template id="caption">

```json
{
  "high_level_description": "one or two sentence summary of the whole image",
  "style_description": {
    "aesthetics": "mood and aesthetic keywords",
    "lighting": "lighting description",
    "photo": "camera and lens, for photos; use photo OR art_style, not both",
    "medium": "photograph",
    "color_palette": ["#1B1B2F", "#E43F5A"]
  },
  "compositional_deconstruction": {
    "background": "the background and environment",
    "elements": [
      {"type": "obj", "bbox": [120, 80, 540, 620], "desc": "a subject described in detail"},
      {"type": "text", "bbox": [600, 100, 700, 900], "text": "EXACT WORDS", "desc": "font, weight, color, placement"}
    ]
  }
}
```

</template>

<example use_case="full-caption-photo">

```json
{
  "high_level_description": "A golden retriever riding a skateboard down a sunny sidewalk.",
  "style_description": {
    "aesthetics": "warm, playful, vibrant",
    "lighting": "bright afternoon sunlight, long soft shadows",
    "photo": "shallow depth of field, eye-level, 85mm lens",
    "medium": "photograph",
    "color_palette": ["#F5C542", "#87CEEB", "#4A4A4A", "#FFFFFF", "#2E8B57"]
  },
  "compositional_deconstruction": {
    "background": "A sun-drenched suburban sidewalk lined with green hedges and a white picket fence. Dappled light filters through overhead trees.",
    "elements": [
      {"type": "obj", "bbox": [200, 300, 800, 900], "desc": "A golden retriever with a fluffy coat, standing on a red skateboard with all four paws. Its tongue is out and ears are flapping in the wind."},
      {"type": "obj", "bbox": [250, 750, 750, 950], "desc": "A worn red skateboard with black wheels rolling along the concrete sidewalk."}
    ]
  }
}
```

*Why: the canonical full caption: a summary, a photographic style block with a palette, then a background and two boxed elements, each named and described*

</example>

## Style: the style_description block

<rules id="style">

- `style_description` controls aesthetics, lighting, medium, and color. It is optional; for photoreal work you can omit it and fold film stock, grain, and white balance into the prose instead. Ideogram's own advice is that a missing or thin style block is the usual cause of a generic look, because the model has no default style.
- It must contain exactly one of `photo` (for photographs, paired with `medium: "photograph"`) or `art_style` (for illustration, painting, 3D render, vector, and the like). Use one, never both.
- When present, `aesthetics`, `lighting`, and `medium` are required by the open schema; `color_palette` is optional and always comes last.
- Key order depends on the type. Photo: `aesthetics`, `lighting`, `photo`, `medium`, `color_palette`. Non-photo: `aesthetics`, `lighting`, `medium`, `art_style`, `color_palette`.
- `medium` is a short label: `photograph`, `illustration`, `3d_render`, `painting`, `graphic_design`, and so on. `lighting` can be `n/a` for flat illustration.

</rules>

## Composition and bounding-box layout

<rules id="layout">

- `compositional_deconstruction` carries the layout: a `background` string, then an `elements` list. Each element is an object (`type: "obj"`) or a text block (`type: "text"`).
- Element key order: `obj` is `type`, `bbox`, `desc`, `color_palette`; `text` is `type`, `bbox`, `text`, `desc`, `color_palette`. `bbox` and `color_palette` are optional but must keep these positions when present.
- A `bbox` is `[y_min, x_min, y_max, x_max]` in normalized 0 to 1000 coordinates with the origin at the top-left. Note the order is Y first, then X. Keep the lower coordinate before the upper one on each axis.
- Boxing is optional and selective. Box the elements whose placement matters and leave the rest unboxed; or skip boxes entirely and state position in prose ("in the upper third", "on the rule-of-thirds line", "lower-left foreground"). Both work.
- Give each object and text block its own element. One element per thing, each welded to its own description and, if used, its own box. Leave room for each text block and avoid overlapping boxes.

</rules>

<example use_case="selective-boxing-and-palette">

```json
{
  "high_level_description": "A lone sailboat on calm water at sunset.",
  "style_description": {
    "aesthetics": "serene, warm, golden hour",
    "lighting": "golden hour backlighting, warm atmospheric haze",
    "photo": "wide angle, f/8, long exposure",
    "medium": "photograph",
    "color_palette": ["#FF6B35", "#F7C59F", "#004E89", "#1A659E", "#2B2D42"]
  },
  "compositional_deconstruction": {
    "background": "A calm ocean stretching to a low horizon, sky washed in orange and pink with thin wisps of cloud.",
    "elements": [
      {"type": "obj", "desc": "A single sailboat with a white triangular sail, silhouetted against the setting sun."}
    ]
  }
}
```

*Why: the subject carries no bbox, its place is set in prose; layout is only as explicit as you need, and the palette steers the whole image to sunset tones*

</example>

## Text rendering

In-image text is the family's headline strength: clean signage, logos, captions, watermarks, and dense multi-line, multi-font layouts.

<rules id="text">

- Use a `text` element per text block. Put the exact words in `text` and the styling (font, weight, case, color, treatment, placement) in `desc`. The split between the literal string and its visual description is the mechanism behind reliable typography.
- Line breaks go inside the string as `\n` (for example `"text": "MANGO\nSAGO\nSOCIAL"`).
- For multiple fonts or styles, give each word or block its own `text` element with its own `desc`; the model renders each in its own lettering.
- Set type scale by description ("the largest type on the page", "smaller than the title but larger than the footer") or pin it exactly with a `bbox`.
- Describe lettering by weight, width, case, shape, and mood (bold, hairline, condensed, all caps, serif, script, pixel, distressed, drop shadow) rather than by a font name; the model draws letters, it does not load font files.
- In plain language, put the exact words in straight double quotes, keeping the spelling and capitals you want, mention the text early, say where it sits, and keep each string short. For several blocks, give each its own words, style, and place, in reading order from the top down.
- English and short strings are the most reliable. Ideogram's docs list long passages and non-Latin or accented text as the weak spots; keep non-Latin text to a word or two.
- Text elements also handle incidental in-scene text: a product label, a book spine, a sign within a photograph.

</rules>

<example use_case="design-and-typography">

```json
{
  "high_level_description": "A clean, modern business card layout for a tech company.",
  "style_description": {
    "aesthetics": "minimal, professional, geometric",
    "lighting": "even, diffuse studio lighting",
    "medium": "graphic_design",
    "art_style": "flat vector design, generous whitespace, sans-serif typography",
    "color_palette": ["#FFFFFF", "#F0F0F0", "#333333", "#0066FF", "#00CC88"]
  },
  "compositional_deconstruction": {
    "background": "A solid off-white card surface with subtle paper texture.",
    "elements": [
      {"type": "text", "text": "ACME TECH", "desc": "Bold dark grey sans-serif company name across the upper third of the card."},
      {"type": "text", "text": "hello@acme.tech", "desc": "Small blue sans-serif contact email near the bottom of the card."}
    ]
  }
}
```

*Why: a non-photo caption (note the art_style key order) with two text elements, each pairing the literal string with its own styling and placement, the core typography pattern*

</example>

<example use_case="plain-language-text-blocks">

```text
Vintage naturalist collector card, "MANTIS SHRIMP" in bold display serif at top, "Odontodactylus scyllarus" in green italic below the illustration, "Possesses the most complex eyes in the animal kingdom." in smaller roman, "8 of 50" bottom right, "OCEAN MARVELS" in banner at bottom
```

*Why: Ideogram's own plain-language text example for 4.0 on its service: every string is quoted in full with its own lettering and position, which is what turns described text into rendered text*

</example>

## Color palette control

<rules id="color">

- A `color_palette` array of `#RRGGBB` hex steers the image's dominant colors directly, rather than through adjectives. Put it last in `style_description` for the whole image, and optionally a smaller palette inside an element for that element alone.
- Treat it as strong steering, not a pixel lock. Include the colors you actually want present, background included; if you want a dark backdrop, put the dark hex in the palette.
- Include contrast pairs, both a highlight and a shadow color, for more controlled lighting.
- Swapping only the palette on an otherwise fixed caption re-tints the same scene, which is a clean way to explore brand variants.
- You can also name colors inline in a `desc` or `background` (named or hex); the structured palette and inline color both work and combine.

</rules>

## Plain text and magic prompt

<rules id="plaintext">

- Open weights: plain text sent straight to the model does not work and is likely to trip the safety filter. Run it through magic prompt (on by default in the reference pipeline) or write the caption.
- Ideogram's service: plain language is accepted. With Magic Prompt on, an LLM rewrites and expands it and builds the caption; with it off, your wording is kept and only converted into the caption. Valid JSON is used as written unless Magic Prompt is on, which rewrites JSON too, so turn it off when a hand-written caption must be used exactly.
- Magic prompt is opinionated. Ideogram lists what it does: it populates sparse scenes with secondary elements you did not ask for, upgrades vague references to specific ones, strips hedging ("could include", "or similar"), drops render details like bokeh and film grain unless you name them, and picks one value when you offer two. Fine for exploring; for a brand deliverable with fixed colors and text placement, write the caption.
- Plain language follows the same craft as the caption: full sentences rather than tags, the main idea first (words near the start carry more weight), what can be seen rather than abstractions, and exact text in quotes. Ideogram's order is image type, main subject, action or placement, setting, lighting, style, then the quoted text.

</rules>

<example use_case="plain-language-product">

```text
A product photo of a green glass bottle, centered on a cream pedestal, soft window light, a minimal studio setting. The label reads "NORTHWIND" in bold dark letters.
```

*Why: Ideogram's own starting prompt in its documented order (image type, subject, placement, light, setting), with the label text quoted and given its own sentence*

</example>

## Image editing (Ideogram 4.5)

Ideogram 4.5 edits an existing image from a plain-language instruction. Its precise-edit mode copies every pixel the edit did not need to change, which is what lets an image take edit after edit without drift.

<rules id="edit">

- State the one change first, then what must survive: "Keep everything else exactly the same." Name the fragile details rather than trusting "keep the product" to cover them: labels, logos, keycap legends, a face, the framing.
- Identify the target by what it is now: "the orange keycaps", "the white midsole", "the abstract print inside the black frame". That scopes the change better than "make the keyboard teal".
- One change per turn. For a sequence, the accepted result becomes the next input, and later instructions restate the approved details while pointing at something new ("The toaster keeps its exact shape, cherry-red finish, chrome details and position").
- Branch for alternatives. For colorways or competing directions, edit from the shared approved source rather than recoloring the last variant, and go back to the last good version instead of repairing several accumulated changes in one prompt.
- A mask marks where to edit; the prompt still has to say what goes there. With a mask, describe the area's new content ("mustard yellow velvet upholstery"). Reach for a mask when a part is hard to name in words, or when an earlier instruction changed too much.
- Light changes how color reads. A relight also warms or cools the product, so keep a neutral version for color reference.
- A new viewpoint asks the model to invent what the camera never saw, so treat it as its own branch and check it against the real product.
- Text: quote the new words and say the lettering stays ("change the sign to read ..."). 4.5 can also translate text in place while keeping the design.
- Magic Prompt does not apply to edits; the service turns every edit instruction into a structured edit prompt itself.

</rules>

<example use_case="edit-background-name-fragile-details">

```text
Turn this into a clean e-commerce packshot: rebuild the ENTIRE background edge to edge as one seamless pure white studio sweep with a soft natural contact shadow, no frame, border or tone step anywhere. Keep the product exactly as it is: shape, materials, lighting and every logo, label and letter on it unchanged, and fully in frame. Keep every keycap legend and colour exactly as they are.
```

*Why: Ideogram's saved keyboard edit (its dashes made ASCII): the change comes first and is fully specified, and the keep sentences name the small details (legends, logos) most likely to drift*

</example>

<example use_case="edit-target-by-current-color">

```text
Change the orange keycaps to a deep teal, keeping every cream keycap, every legend and the white case. Keep everything else in the image exactly the same, including every logo and all text on the product.
```

*Why: Ideogram's second keyboard edit: "the orange keycaps" picks out a set of objects by their current color, and the keep clause separates them from the cream keys and the case*

</example>

<example use_case="edit-colorway-keep-clause">

```text
Change the product's colour and finish to slate-blue knit. The product keeps its exact shape, size, proportions, details and position; the camera, framing and everything not mentioned stay exactly the same.
```

*Why: the keep clause Ideogram reuses across its product sequences; it pins the product's geometry and the camera so only the color and finish move*

</example>

<example use_case="edit-sequence-restate-approved">

```text
Change the blueberries in the bowl to fresh ripe strawberries, some halved, filling the same bowl. The toaster keeps its exact shape, cherry-red finish, chrome details and position; the camera, framing and everything not mentioned stay exactly the same.
```

*Why: a later turn in Ideogram's toaster sequence: it names the container the new fruit fills and restates the finish approved in the previous turn*

</example>

<example use_case="edit-relight-keep-objects">

```text
Make it evening: dusky blue light through the window, and the table lamp switched on. Keep every object exactly where it is.
```

*Why: the third turn of Ideogram's living-room sequence; a global light change is safe to chain when the keep sentence fixes every object's position*

</example>

<example use_case="edit-restoration">

```text
Restore this old photograph: remove every scratch, dust speck, stain, crease, tear and film blemish, even out the faded tones and recover the detail. Keep it black and white and keep every person and letter exactly as it is.
```

*Why: Ideogram's restoration prompt: it lists each defect to remove, then pins the medium (black and white), the people, and any lettering*

</example>

## Reference images (Ideogram 4.5)

<rules id="references">

- With reference images attached, the prompt works as an edit instruction: say what should change and keep the rest of the prompt short.
- Give each reference one role, and say what comes from it. Weld each borrowed element to its source.
- In Ideogram's app, type `@` and pick each image so it drops in as a pill such as `@img_1`; the labels can differ, so insert the real pills rather than typing a guessed name. You do not have to mention every attached image.
- Through the API there is no documented tag: the first image is the one edited and the others are references, and in precise edit the references are never edited themselves. Name each reference by what it shows.
- Crop a reference down to the thing it supplies, and say which part of the product should use it ("the upper panels only"). Check that its lighting or background has not leaked into the scene.
- For a consistent character, use clear shots of the face from a few angles, describe the new scene, and refer to the character by its tag. Reuse the same references each time.
- A reference can also carry a look: name what to take from it (palette, brushwork, texture) and pin the composition.

</rules>

<example use_case="product-into-scene">

```text
Place the bottle from @img_1 on the table in @img_2. Keep the bottle label visible. Use the lighting and camera angle of the scene.
```

*Why: Ideogram's own two-reference example: each image gets one role, the label is protected, and the instruction says which image the light and camera come from*

</example>

<example use_case="character-from-references">

```text
@img_1 sitting at a café table, reading a newspaper, morning light
```

*Why: Ideogram's character example: the reference tag stands in for the person, so the prompt spends its words on the new scene and light*

</example>

<example use_case="three-reference-composite">

```text
Put the woman from @img_1 in the linen jacket from @img_2, standing in the courtyard from @img_3. Keep her face and hairstyle exactly as in @img_1 and the jacket's colour and buttons exactly as in @img_2. Use the courtyard's afternoon light on all of it.
```

*Why: guide-built to Ideogram's rules: three references with one role each, every kept detail welded to its source, and one image named as the light source*

</example>

<example use_case="pure-style-transfer">

```text
Restyle @img_1 in the style of @img_2: flat gouache shapes, visible brush texture and the same muted palette. Keep the composition, the people and their poses exactly the same.
```

*Why: guide-built: the style reference's contribution is named in concrete terms, and the keep sentence fixes everything except the rendering*

</example>

<example use_case="style-transfer-plus-edit">

```text
Restyle @img_1 as a two-colour risograph print in pink and teal ink, and change the shop sign to read "OPEN LATE". Keep the street layout and the cyclist exactly where they are.
```

*Why: guide-built: the style change and the text edit share one turn because both touch the whole image, the new words are quoted, and the keep sentence names what both must leave alone*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field on any 4.x surface. Describe the desired state instead of listing what to avoid.
- The caption is additive: only what you name tends to appear, so to exclude something, leave it out and describe the alternative ("a clear blue sky" rather than "no clouds").
- In plain language, Ideogram's docs say models latch onto the word after "no", "without", or "not"; write "an empty street" rather than "a street with no people". Magic Prompt often turns a negative into a positive. Short trailing exclusions such as "no text, no logos" do appear in Ideogram's own prompts; keep them brief.
- In an edit, the keep sentence does the excluding: name what must not change.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Bare plain text on the open weights: it does not work and trips the safety filter; write a caption or let magic prompt build one.
- Hand-written caption with Magic Prompt on: the service rewrites your JSON; turn it off to use the caption as written.
- Caption without `high_level_description` on Ideogram's service: it is read as plain text.
- Under-describing: name and describe every object and text block; a sparse caption leaves elements to chance.
- Mood words instead of visible ones: "nice lighting" leaves the choice to the model; name the light's source and direction.
- Field name: it is `color_palette` (American spelling). Some summary docs write `colour_palette`, but the schema and verifier expect `color_palette`.
- Key order: keep the schema's key order; out-of-order keys degrade quality on the open weights and warn in the verifier.
- Hex shorthand or lowercase: write uppercase `#RRGGBB`, not `#fff` or `#1b1b2f`.
- bbox axis order: it is `[y_min, x_min, y_max, x_max]` with Y first; swapping to X-first misplaces everything.
- photo and art_style together: pick one; they are mutually exclusive inside `style_description`.
- Several changes in one edit turn: split them, one change per turn, and keep each accepted result.
- Recoloring the last variant for a new colorway: branch from the approved source instead.
- Typed reference labels in the app: insert the real `@` pills; a guessed label is not a reference.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. The owner is Ideogram (ideogram.ai). The open release's prompting reference governs the caption itself; where Ideogram's service is more lenient (key order, lowercase hex, plain-text conversion), the guide teaches the strict form and notes the leniency. Where the summary model cards and the prompting reference disagree on a field name (`colour_palette` vs `color_palette`), this guide follows the prompting reference and its caption verifier.

- Official (Ideogram), open release: [prompting guide (docs/prompting.md)](https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md), [HF model card](https://huggingface.co/ideogram-ai/ideogram-4-fp8), [Ideogram 4.0 blog](https://ideogram.ai/blog/ideogram-4.0/), [GitHub repo](https://github.com/ideogram-oss/ideogram4).
- Official (Ideogram), service and 4.5: [Prompting basics](https://docs.ideogram.ai/prompting/prompting), [Prompt structure](https://docs.ideogram.ai/prompting/prompt-structure), [Text in images](https://docs.ideogram.ai/prompting/text-in-images), [JSON prompting](https://docs.ideogram.ai/prompting/json-prompting), [Fix common problems](https://docs.ideogram.ai/prompting/fix-common-problems), [Reference images](https://docs.ideogram.ai/create/reference-images), [Masks and inpainting](https://docs.ideogram.ai/edit/masks-and-inpainting), [4.5 generate API](https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-4-5), [4.5 precise edit API](https://developer.ideogram.ai/v2/api-reference/images/precise-edit/ideogram-4-5), [Ideogram 4.5 page](https://ideogram.ai/models/4.5/), [4.5 product photo editing guide](https://ideogram.ai/blog/ideogram-4-5-product-photo-editing/), [Ideogram 4 JSON prompting guide](https://ideogram.ai/blog/ideogram-4-json-prompting/).
- Provider: [fal Ideogram V4](https://fal.ai/models/ideogram/v4), [fal Ideogram V4.5 Edit](https://fal.ai/models/ideogram/v4.5/edit).
- Hosted under another name: Pruna's [P-Image-Ideogram](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-image-ideogram.html) page, which states the shared Ideogram 4.0 caption schema.

Last verified: 2026-11-08.
