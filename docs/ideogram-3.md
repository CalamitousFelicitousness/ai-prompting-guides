---
guide: "Ideogram 3.0 (image)"
prompt_scheme: "ideogram-3"
models:
  - { id: "ideogram-3", access: "closed-weights", tier: "std", caps: [text-to-image, image-edit, masked-edit, outpainting, style-transfer, subject-control, text-rendering, color-control, transparency], best_for: "the only Ideogram model with style presets, style codes, style reference images, a negative prompt and a color palette, which makes it the pick for logos, brand graphics and matching a set look; also a saved-character mode, inpainting, remix, reframing and background replacement. Its transparent variant draws on no background for stickers, icons and print" }
  # legacy; Ideogram's docs say they may still appear in the picker and point new work to Ideogram 4.5 or 4.0
  - { id: "ideogram-2a", access: "closed-weights", tier: "legacy", caps: [text-to-image], best_for: "a fast, lower-cost earlier model; plain prompt, a broad style type, no negative prompt or style references" }
  - { id: "ideogram-2", access: "closed-weights", tier: "legacy", caps: [text-to-image], best_for: "the earlier generation; kept for existing workflows only" }
capabilities: [text-to-image, image-edit, masked-edit, outpainting, style-transfer, subject-control, text-rendering, color-control, transparency]
prompt:
  languages: ["en"]
  literal_text: "put the exact words in straight double quotes with the spelling and capitals you want, mention the text early in the prompt, say where it appears, and keep each string short; describe the lettering's weight, shape and mood rather than naming a font file"
  length_strategy: "full sentences, main idea first; short prompts leave room for the model's own choices, longer ones give control. Ideogram says 3.0 may weaken or ignore words past about 150 words, so keep the most important content well inside that"
  auto_expand_behavior: "Magic Prompt (on by default) rewrites and expands the prompt and can translate it into English; it adds detail and items you did not ask for and often turns a negative into a positive. Turn it off to test your own wording, and when a style preset or style references should carry the look"
  negatives: "a negative-prompt field exists on 3.0 generation, character and remix: list items separated by commas; the main prompt takes precedence over it, so never contradict the prompt, and prefer a positive description of what should be visible. Inpainting has no negative field. In the main prompt, describe the absence instead of writing 'no' or 'without'"
sources:
  official: ["https://docs.ideogram.ai/prompting/prompting", "https://docs.ideogram.ai/prompting/prompt-structure", "https://docs.ideogram.ai/prompting/text-in-images", "https://docs.ideogram.ai/prompting/refine-and-iterate", "https://docs.ideogram.ai/prompting/fix-common-problems", "https://docs.ideogram.ai/create/image-settings", "https://docs.ideogram.ai/create/models", "https://docs.ideogram.ai/edit/remix", "https://docs.ideogram.ai/organize-and-share/characters", "https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-3", "https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-3-character", "https://developer.ideogram.ai/v2/api-reference/images/remix/ideogram-3", "https://developer.ideogram.ai/v2/api-reference/images/inpaint/ideogram-3", "https://developer.ideogram.ai/v2/api-reference/images/replace-background/ideogram-3", "https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-2a"]
  provider: ["https://fal.ai/models/fal-ai/ideogram/v3/edit/api"]
  community: []
last_verified: "2026-11-08"
---

# Ideogram 3.0: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers Ideogram 3.0, its transparent-background variant, and the legacy Ideogram 2a and 2.0. Ideogram 4 and 4.5 take a structured JSON caption and have their own guide; do not carry their caption or edit-instruction forms over here.
- Write plain-language prompts in full sentences. 3.0 has no JSON caption, and weight syntax or flags (`::1`, `(important)`, `--ar`, `--style`) are read as words, not commands.
- Style is a setting, not only words: a style type, presets, style codes, style reference images, and a color palette sit beside the prompt. When one of them carries the look, keep style words out of the prompt.
- Editing on 3.0 is descriptive: an inpaint, remix, or background prompt describes the finished result, not the change. That is the opposite of Ideogram 4.5's edit instructions.

</rules>

## TL;DR

<template id="quickstart">

{image type} of {main subject}, {action or placement}, {setting}, {lighting}, {style}. The {object} reads "{exact words}" in {lettering description}.

</template>

## Models and when to use which

- `ideogram-3`: the model to reach for when the look must be steered by settings: a style preset, a style code, your own style reference images, a color palette, or a negative prompt. Ideogram's docs single it out for logos, brand graphics, and matching a set style. It also powers the saved-character mode, inpainting, remix, reframing, and background replacement, and most custom models are trained on it.
- Ideogram 3.0 Transparent: the same prompting, drawn with no background, for stickers, t-shirt and print designs, icons, and clip art.
- `ideogram-2a` and `ideogram-2`: legacy. Ideogram says they may still appear in the picker and points new work to 4.5 or 4.0. They take the same plain prompt with a broad style type, and have no negative prompt, style references, or palette.
- For open layout control with bounding boxes and hex palettes per element, or for multi-turn instruction editing, use the Ideogram 4 and 4.5 guide instead.

## How the model reads prompts

- Words near the start carry more weight. Put the main idea first.
- Full sentences tell it how things relate; tag lists do not.
- Describe what can be seen. An abstract idea lands when it is shown through something visible.
- If you describe something, it tries to show it, even when that breaks the framing. Leave out what you do not want in the picture.
- English is the most reliable, above all for in-image text. Magic Prompt can translate a prompt into English.
- Writing "16:9" or "transparent PNG" in the prompt does not change the output settings.
- It has a practical length ceiling: Ideogram says 3.0 may weaken or ignore words past about 150 words.

## Prompt structure

<rules id="structure">

- Short form: image type, main subject, action or placement, setting, lighting, style, then any text that reads "exact words". Drop any part that does not matter for the task.
- Long form, in order: a one-sentence summary (if you write only one sentence, make it this one), subject details with any quoted text, pose or action, secondary elements, setting, lighting and atmosphere, framing, and finish.
- Literal, visually grounded wording gives the most consistent results and the best layout control, which matters most when the image includes text. Abstract wording works when it carries a few concrete anchors.
- Keep one idea per prompt. Too many unrelated ideas confuse the model.
- To give something more weight, move it earlier, repeat it, or describe it more fully (size, color, texture, where it sits).

</rules>

<template id="general">

{One-sentence summary: image type and main subject}. {Subject details, with "exact words" for any text}. {Pose or action}. {Secondary elements}. {Setting}. {Lighting and atmosphere}. {Framing}. {Finish or medium}.

</template>

<example use_case="flagship-product">

```text
A product photo of a men's perfume bottle named "Nightlife for men" in a sleek studio setup. The bottle is tall and rectangular with dark glass, a matte black cap, and silver lettering. The text "Nightlife for men" appears on the label in bold, modern font. The bottle stands upright with a slight reflection on the surface below. A wristwatch and a pair of sunglasses sit nearby. The scene is set on a smooth black surface with blurred city lights in the background. Lighting is moody and cool, with soft blue highlights and deep shadows. The bottle is centered in the frame, captured at eye level. A shallow depth of field gives the image a polished, professional look.
```

*Why: Ideogram's own long-form prompt, one part per sentence in its documented order: summary, subject details with the quoted label, placement, secondary objects, setting, light, framing, finish*

</example>

<example use_case="illustration-long-form">

```text
A whimsical watercolor painting of a little girl playing with her bunny in a flower-filled field. The girl has short brown hair, a yellow dress, and rosy cheeks. She holds a fluffy white bunny in her arms, and both are smiling. The bunny is leaning into her, with its ears flopping gently. Wildflowers, butterflies, and a toy picnic basket surround them. They are outdoors in a grassy meadow, under a wide blue sky. The light is soft and sunny, with warm pastel tones and a dreamy atmosphere. The girl and bunny are slightly off-center, framed from a gentle downward angle. The brush strokes are loose and textured, with light color bleeds.
```

*Why: the same long-form order applied to illustration; the medium leads the summary and returns at the end as brushwork, so the style is stated twice*

</example>

## Text rendering

<rules id="text">

- Quote the exact words. Anything inside quotation marks is text to render; keep the spelling and capitals you want.
- Mention the text early. Text named near the start renders more reliably than text added at the end.
- Say where it appears ("painted across the mural behind the artist", "curving along the bottom").
- Keep it short, and keep the scene simple; each extra word raises the odds of a typo, and a busy scene leaves less room for clean lettering.
- Describe the lettering's weight, shape, and mood rather than relying on a font name. Leave the style out and the model, or Magic Prompt, picks one.
- For several blocks, give each its own words, style, and place, in reading order from the top down.
- Long passages and non-Latin or accented text are the weak spots; keep non-Latin text to a word or two.
- To fix a misspelling, regenerate, then try shorter words, then correct it in an editor rather than prompting harder.

</rules>

<example use_case="lettering-style">

```text
The word "Welcome" written in bold sans-serif typeface, in deep forest green on a warm cream background.
```

*Why: Ideogram's lettering example: the word is quoted, then its typeface is described by weight and family, and its color and ground are named*

</example>

<example use_case="multi-block-poster">

```text
A vintage jazz poster. At the top, the headline "BLUE NOTE SESSIONS" in large gold serif capitals. Below the trumpeter, "Live jazz every Saturday night" in off-white italic serif. At the bottom, "THE VELVET ROOM" in small gold sans-serif capitals.
```

*Why: Ideogram's multi-block example: three strings, each with its own place, size, color, and lettering, described from the top down*

</example>

<example use_case="text-on-surface">

```text
A risograph poster pasted on a sunlit brick wall with text that reads: "Everything you can imagine is real. - Pablo Picasso"
```

*Why: Ideogram's opening text example: the medium and the surface the poster sits on are named before the quoted line, so the lettering belongs to the scene*

</example>

## Style controls

<rules id="style">

- The style type sets the broad look: Auto picks one from the prompt, General suits most uses including art and abstract work, Realistic gives lifelike photos, and Design gives clean, vector-like images such as logos and posters.
- A style preset is a prescriptive aesthetic that defines the look even with a short prompt. Style reference images copy the look of your own images; pick images that share a look for a steady style, or mix different ones to see what blends. A preset and style references are alternatives, and both work only with the Auto or General style type.
- Style codes are short hexadecimal codes that each represent a style; like style references, they cannot be combined with a preset.
- When a preset or style references carry the look, turn Magic Prompt off and keep style words out of the prompt. Short, content-only prompts let the style come through.
- The color palette is a direction, not an exact match; it works best alongside color words in the prompt.
- Without a style setting, name the exact medium or technique ("impasto oil painting", "risograph print") rather than "beautiful" or "modern".

</rules>

<example use_case="content-only-for-style-reference">

```text
A fox curled up in snow under a pine tree.
```

*Why: guide-built from Ideogram's fox example with its medium removed: when a preset or style references set the look, the prompt carries only the content, so the two do not compete*

</example>

## Magic Prompt

<rules id="magic-prompt">

- Magic Prompt rewrites and expands the prompt before generation, and can translate it into English. It is on by default.
- It adds detail and items you did not ask for; Ideogram's example turned "Photo of cupcake and strawberries" into a scene with frosting, sprinkles, and a sunlit rustic background.
- It often turns a negative into a positive, so an exclusion written into the prompt can come back as an inclusion.
- Turn it off to test your own wording, to change one thing at a time, and whenever a preset or style references should set the look.

</rules>

## Editing: inpaint, remix, background and character

<rules id="edit">

- Inpainting: the mask marks the region to repaint, and the prompt describes the repainted result: what should be in that region, not an instruction to change it.
- Remix: one source image plus a prompt that describes the complete image you want. A higher image strength keeps more of the source. For one small, bounded change, inpainting suits better than remixing the whole image.
- Background replacement: the prompt is a plain description of the new background only.
- Saved character: one centered, front-facing image of the character against a simple background makes the best reference. The prompt then describes the new scene; the reference carries the character, so do not spend words re-describing the face.
- Reframing extends the image outward from the source and takes no prompt; the style controls still apply to the new area.

</rules>

<example use_case="remix-restyle-product">

```text
A studio photograph of the same ceramic mug on a pale blue table, soft side lighting, simple background.
```

*Why: Ideogram's remix example: the prompt describes the whole finished image, using "the same" to tie the subject to the source*

</example>

<example use_case="remix-pure-style-transfer">

```text
A loose watercolor painting of the same lighthouse on the same rocky point at dusk, soft washes bleeding into each other, visible paper texture, muted blue and peach palette.
```

*Why: guide-built to the remix rule: a pure restyle written as a description of the finished painting, with "the same" holding the subject and setting to the source*

</example>

<example use_case="remix-style-plus-edit">

```text
A 1950s travel poster in flat gouache of the same harbor town, the red boat now moored in the foreground, and a banner across the top reading "VISIT PORT ELLIS" in bold cream capitals.
```

*Why: guide-built: the style change and the added banner are both written as parts of the finished image, with the new words quoted and placed, because 3.0 remix reads a description, not a list of changes*

</example>

<example use_case="inpaint-describe-result">

```text
A black leather tote bag with brass buckles resting on the wooden bench.
```

*Why: guide-built to the inpaint field's own wording, "the prompt describing the repainted result": it states what the masked region should contain and how it sits in the scene*

</example>

<example use_case="character-new-scene">

```text
Standing on a rainy city crosswalk at night under a clear umbrella, neon shop signs reflected in the wet street, cinematic photograph.
```

*Why: guide-built to Ideogram's character guidance: the saved reference supplies the person, so the prompt is entirely the new scene, light, and medium*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- 3.0 has a negative prompt for generation, character, and remix. List the items separated by commas, such as "green, green candies".
- The main prompt takes precedence. Never put something in the negative that the prompt asks for: a classical guitar keeps its strings even when "strings" is in the negative.
- A positive description of what should be visible often works better than a negative.
- In the main prompt, describe the absence instead of writing "no", "without", or "not"; models latch onto the word that follows. Write "an empty room with chairs neatly arranged", not "no people in the room", and "a robot with a smooth, featureless face", not "a robot with no eyes".
- Inpainting, 2a, and 2.0 have no negative field; describe the desired state.

</rules>

<example use_case="describe-the-absence">

```text
An empty street at dawn, wet cobblestones, shuttered shopfronts, soft blue light.
```

*Why: built on Ideogram's own "An empty street" rule: the absence of people is stated as a visible quality of the scene, so there is no "no people" for the model to latch onto*

</example>

## Pitfalls and anti-patterns

<rules id="avoid">

- Tag lists or weight syntax: write full sentences; `::1` and `--ar` are read as words.
- Prompts past about 150 words: words near the end may be weakened or ignored; cut or move the important content forward.
- Style words fighting a preset or style references: keep the prompt content-only and Magic Prompt off.
- Negative that contradicts the prompt: the prompt wins; rewrite the positive side instead.
- "No" in the main prompt: describe the absence as something visible.
- Edit instructions on 3.0: inpaint and remix prompts describe the finished image; "change the bag to black" belongs to Ideogram 4.5, not here.
- Re-describing a saved character's face: describe the new scene and let the reference carry the person.
- JSON captions: 3.0 is plain text only; the caption form belongs to Ideogram 4 and 4.5.
- Ignored details: move them earlier or repeat them; contradictory details: pick one direction.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. The owner is Ideogram; its prompting pages cover 4.5, 4.0, and 3.0 together, and only the rules that apply to 3.0 are taught here. The API reference governs field behaviour, such as the negative prompt's lower precedence and the inpaint prompt describing the repainted result.

- Official (Ideogram): [Prompting basics](https://docs.ideogram.ai/prompting/prompting), [Prompt structure](https://docs.ideogram.ai/prompting/prompt-structure), [Text in images](https://docs.ideogram.ai/prompting/text-in-images), [Refine and iterate](https://docs.ideogram.ai/prompting/refine-and-iterate), [Fix common problems](https://docs.ideogram.ai/prompting/fix-common-problems), [Image settings](https://docs.ideogram.ai/create/image-settings), [Models](https://docs.ideogram.ai/create/models), [Remix](https://docs.ideogram.ai/edit/remix), [Characters](https://docs.ideogram.ai/organize-and-share/characters), API reference for 3.0 [generate](https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-3), [character](https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-3-character), [remix](https://developer.ideogram.ai/v2/api-reference/images/remix/ideogram-3), [inpaint](https://developer.ideogram.ai/v2/api-reference/images/inpaint/ideogram-3), [replace background](https://developer.ideogram.ai/v2/api-reference/images/replace-background/ideogram-3), and [2a generate](https://developer.ideogram.ai/v2/api-reference/images/generate/ideogram-2a).
- Provider: [fal Ideogram V3 Edit](https://fal.ai/models/fal-ai/ideogram/v3/edit/api).

Last verified: 2026-11-08.
