---
guide: "Krea 3"
prompt_scheme: "krea-3"
models:
  # One model. "Krea 3 Ultra" in Krea's app is the top thinking level of the same model, not a separate checkpoint.
  - { id: "krea-3", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit], best_for: "fast instruction-following edits and reference-driven generation: restaging a product in a new scene, the same person or character across shots, precise swaps of an object, material, color or line of text, and turning sketches, line drawings and 3D blockouts into finished images" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, reasoning, grounded-edit]
prompt:
  languages: ["en"]
  literal_text: "quote every string the output must contain, in full, in straight double quotes; implied text ('a sign that describes rocket science') renders as garble, spelled-out text renders. For a text swap, quote the old words and the new ones"
  length_strategy: "for an edit, lead with the change and add only the detail that helps carry it out, then close with one preservation sentence; a short instruction is enough because a built-in expansion step turns it into a full edit recipe. Restages, multi-reference shots and new images reward a full paragraph of scene, light, material and camera, which is how Krea's own showcase prompts are written"
  auto_expand_behavior: "ALWAYS ON at the owner. A vision-language expansion step rewrites every prompt into a complete edit recipe before generation, and a thinking level, where the host exposes one, sets how much it plans: the default level for clear edits, a higher level for complex multi-reference edits or when the default missed, and a slow agentic top level for final edits. Some hosts let you switch expansion off; then write the full recipe yourself. Because expansion varies between runs, reusing a seed does not reproduce an image exactly"
  negatives: "a negative-prompt field exists on Krea's API and some hosts, but not at the top thinking level. The main levers are positive: the closing preservation sentence and 'only' for single-target edits. Krea's own prompts put exclusions inline as short 'no ...' clauses ('no added text', 'no extra props'); keep the negative field for a specific defect that keeps coming back"
sources:
  official: ["https://www.krea.ai/docs/developers/krea-3/overview", "https://www.krea.ai/docs/user-guide/features/krea-3", "https://www.krea.ai/blog/introducing-krea-3", "https://www.krea.ai/blog/krea-3-technical-report", "https://app.notion.com/p/krea-ai/Krea-prompting-guide-Reference-driven-image-editing-3f4805facfb7810d8e3ec81cb9be65e2", "https://www.krea.ai/docs/changelog"]
  provider: ["https://fal.ai/learn/tools/krea-3-prompting-guide", "https://fal.ai/krea-3", "https://fal.ai/models/krea/v3/edit", "https://fal.ai/models/krea/v3/text-to-image", "https://fal.ai/models/krea/v3/realtime"]
  community: []
last_verified: "2026-11-08"
---

# Krea 3: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, resolution, and pricing, consult the host's docs; they differ and are out of scope here.
- Krea 3 is Krea's instruction-following image editor, and it also generates from text alone. You say what should change and what should stay, and you give it reference images for CONTENT: the product, the person, the room, the material.
- Write plain-language instructions in full sentences. No JSON, no tag lists.
- Two principles run through every edit: NAME WHAT MOVES, PIN WHAT STAYS (state the change, then name what must stay identical), and ONE ROLE PER INPUT (say what each reference image contributes and weld each borrowed element to its source).
- For aesthetic exploration with weighted style references, moodboards, a creativity control, or LoRAs, use Krea 2, which has its own guide. Krea 3's reference images carry content, not a weighted style.

</rules>

## TL;DR

<template id="quickstart">

{The change, described as the finished result, with the target named precisely}. {Only the details that help carry it out: material, color, position, scale, light}. Keep {the one or two things that must not change, named concretely} exactly as they are.

</template>

## Models and when to use which

- `krea-3`: one model. Krea makes it the default image model in its app. Strongest on product restaging (the label and logo survive), the same person or character across new poses, places and light, precise local swaps, and sketches, line drawings, moodboards, and 3D blockouts turned into finished images. It keeps paintings, vector art, and ink drawings in their own medium.
- Krea 3 Ultra: the top thinking level of the same model, sold under its own name in Krea's app. It runs an agentic planning loop and is slow; use it for final, high-stakes edits.
- Krea 3 or Krea 2: Krea's own docs send fast instruction-following generation and editing, especially when a product or character must stay consistent, to Krea 3, and aesthetic exploration with style references, moodboards, and sliders to Krea 2.
- Some hosts also run Krea 3 as a live session that keeps editing one frame as you type: refer to the frame as the first image, and each new instruction edits the latest result.

## How the model reads prompts

- The text encoder is a vision-language model that sees the reference images together with your instruction, so you can point at things by what they look like: "the woman in the red coat", "the sneaker from the second image".
- Every prompt passes through an expansion step that rewrites it into a complete edit recipe: the finished scene, where every kept element sits, and every string of text in quotes. A short instruction is enough to start; what you write is the brief that recipe is built from, so every concrete detail you give survives into it.
- Krea trained it on long, complete edit recipes and found that spelled-out detail beats implied detail, most visibly for text: a quoted string renders, a described one ("a sign about rocket science") does not.
- Things you do not mention are expected to stay. A local edit should leave everything outside its target unchanged, and every line of text you do not name should survive.
- It inherits Krea 2's eye for style, so medium words still land: name the print process, the paint, the film stock, or the photographic genre when the result's look matters.
- Two owner-stated weak spots: extremely dense small text is imperfect, and identity is not perfectly preserved across edits.

## Prompt structure

<rules id="structure">

- Lead with the change. Describe it as the finished result, and for a restage describe it the way a photographer would: the scene, the light, the camera.
- Name the target precisely. "The large left-hand wall behind the staircase" is a clearer instruction than "redesign the room".
- Add only the details that help carry out the change: material, color, position, scale, light direction.
- Close with one preservation sentence that names the few things that matter, such as the label, the logo, the face, or the framing. Do not list everything in the image; unmentioned things are already expected to stay.
- Use "only" when the edit should touch one thing: "Remove only the woman in the red coat."
- When only part of an object should change, name the part: "the silver leaf handle ornaments", not "the handle".

</rules>

<template id="general">

{Change or finished result, target named precisely}. {Material, color, position, scale, or light details that carry it out}. {For a restage: scene, light source and direction, camera and lens, palette}. Keep {named elements that matter} exactly as they are.

</template>

<example use_case="minimal-edit">

```text
Change the mug to red, keeping everything else the same.
```

*Why: Krea's own canonical edit: the change leads, nothing is added that the edit does not need, and one closing clause pins the rest*

</example>

<example use_case="part-not-whole">

```text
Replace the blue nylon strap with a dark brown leather strap. Keep the hand, hair, shirt and framing exactly as they are.
```

*Why: from Krea's technical report: the target is one named part, and the preservation sentence names the nearby things most likely to be redrawn by mistake (the hand and hair touch the strap)*

</example>

## Image editing

<rules id="edit">

- Local edits (recolor or swap an object, add or remove an element, fix a detail, change the text on a sign): where the host offers a local-edit mode, use it. Only the region that needs to change is regenerated and the rest stays pixel-exact, which makes it safe to keep editing the latest output.
- Global edits (restyle, relight, change the season or time of day, reframe, combine several images into a new scene): leave the local mode off, since these must re-render the whole image. A whole-image edit of an earlier whole-image edit accumulates artifacts, so start each global edit from the original or an approved image rather than chaining.
- For the next shot of the same scene, upload the chosen result as the first image, then the original references it needs, and open with "Same scene, same {subject} as the first reference image, now ...".
- Sketches, line drawings, moodboards, and 3D blockouts: say what the input is, keep its composition and geometry, and add a line about materials and light. "Upgrade only materials, lighting and detail" keeps the layout fixed.
- Expanding an image: say the original stays intact and where it sits, describe what continues on each side, and restate the medium so the new area matches.
- Style changes: name the target medium and its marks (outlines, grain, brushwork), then pin the composition and the people. When a style change rides with another edit, give each its own sentence.

</rules>

<example use_case="material-swap">

```text
Replace only the large left-hand wall behind the staircase with warm walnut-grey vein-cut travertine, in large horizontal slabs with fine pores and recessed joints. Preserve the oval sunlight patch and the current exposure. Keep the stair pale and preserve its silhouette. Leave the camera, framing, furniture, occupants, ceiling, floor and glazing unchanged.
```

*Why: Krea's shortened prompt for this edit: "only" plus a precisely located target, the material described to the level of slab, pores and joints, then the light that must survive and a short list of what stays*

</example>

<example use_case="only-the-named-part">

```text
Change the silver leaf handle ornaments to polished copper finish.
```

*Why: from Krea's technical report, where the untrained model turned the whole handle copper; naming the part (the leaf ornaments) rather than the object is what scopes the change*

</example>

<example use_case="blockout-to-photo">

```text
Turn image 1, a 3D viewport render, into a finished photoreal product still life. Keep the camera, framing and each object's shape, scale and position. Upgrade only materials, lighting and detail. Give the watch brushed and polished steel surfaces, a cobalt dial and realistic reflections. Keep the stone matte and visibly textured. Use controlled studio lighting that separates metal from stone.
```

*Why: Krea's shortened blockout prompt: it says what the input is, fixes the geometry in one sentence, limits the change to materials and light, then gives each object its finish*

</example>

<example use_case="expand-illustration">

```text
Expand this woodblock print into a wide three-sheet triptych, keeping the original image intact as the center sheet. Continue the scene to the left with the open bay, a few sailboats with tan sails, and the distant hills of the city under the same orange-to-teal sunset gradient, and to the right with the forested headland, the winding coastal road carrying more cars, and a small white lighthouse on the point. Match the original exactly: flat bokashi color gradients, black keyblock outlines, visible wood grain and paper fibers, the same limited palette, and thin vertical seams between the three sheets.
```

*Why: Krea's own expansion prompt: the original is pinned as the center sheet, each side gets its own content, and the medium's marks are restated so the new sheets match*

</example>

<example use_case="pure-style-transfer">

```text
Repaint image 1 as a Japanese ukiyo-e woodblock print with flat bokashi color gradients, black keyblock outlines and visible wood grain in the paper. Keep the composition, the three people and their poses exactly as they are.
```

*Why: guide-built to Krea's rules: the target medium is named with its marks, and the preservation sentence pins composition and figures so only the rendering changes*

</example>

<example use_case="style-transfer-plus-edit">

```text
Repaint image 1 as a 1950s travel poster in flat gouache with a limited palette of teal, cream and coral. Change the sign above the door to read "OPEN LATE" in the same position. Keep the street layout and the cyclist's pose exactly as they are.
```

*Why: guide-built: the style change and the text edit each get their own sentence, the new words are quoted in full, and the preservation sentence names what both edits must leave alone*

</example>

## Multiple reference images

<rules id="multi-image">

- Say what each image is for: "image 1 is the room, image 2 is the sofa". One role per image, and weld each borrowed element to its source.
- Refer to each image by its number and by what it shows: "the person from image 1, wearing the jacket from image 2". Krea's API reference asks for references by content and its showcase prompts number them; combining both removes the ambiguity. Numbers follow upload order, so keep the order fixed for each shot.
- Some hosts document a tag form for references (fal writes `<image-1>`, `<image-2>`); use it where the host documents it.
- After naming a person's source image, list the identifying features in parentheses: "the woman from image 5 (exact face, slick center-part dark hair, ...)". Use "exact" for products, wardrobe, and jewelry that must match the reference.
- Fewer references keep more detail per reference. When fine detail matters (small text, logos, fabric, faces in a wide shot), send the sharpest original you have, do not upscale it first, and drop references the shot does not need.
- An image can also identify a target: "Refer to image 2 and remove the same woman from image 1."

</rules>

<example use_case="multi-reference-flagship">

```text
Refined, tasteful high-fashion editorial photograph, restrained and elegant. The woman from image 5 (exact face, slick center-part dark hair, bleached brows, sharp black winged liner, rosy cheeks, glossy nude lips) wears the exact black strapless column gown and long black satin opera gloves from image 1, the exact headpiece from image 2 and the exact pansy and black bead chandelier earrings from image 3. Backdrop is the chartreuse-to-amber gradient paper from image 4. Pure side profile, standing perfectly still, full-length, gloved hands relaxed at her sides, posture long and poised. One soft-edged directional light casts a clean elongated shadow of her profile and the headpiece onto the backdrop beside her. Generous negative space, calm, quiet and graceful, classic couture portraiture, fine film grain.
```

*Why: Krea's own five-reference prompt: the genre leads, every element is welded to its numbered source with "exact", the model's identity is spelled out in parentheses, and pose, light, and finish follow as a photographer's brief*

</example>

<example use_case="replace-with-references">

```text
Replace only the seating in image 1 with the sofa, chairs and table from images 2 to 4. Keep the rug, the room and the reading woman.
```

*Why: Krea's shortened launch prompt: one scene plus three product references, "only" scopes the swap, and the preservation sentence names the three things a full re-render would most likely disturb*

</example>

<example use_case="next-shot-continuity">

```text
Same scene, same woman and same outfit as the first reference image, now photographed from a different angle: front-facing close-up, chest-up framing, she faces the camera directly, face and shoulders square to the lens, candid neutral expression. Keep her identical (face from the portrait reference: brown eyes, ash-brown straight hair with wispy curtain bangs, mauve lips), the washed pink ringer tee with brown trims and small brown pixel-stitched bunny on the chest, the red crinkled leather shoulder bag strap over her shoulder with the bag partly visible. Background: the same dark polished mahogany panelled wall of the 1990s office, softly out of focus. Same warm soft directional light, 35mm film editorial look, fine grain, minimal.
```

*Why: Krea's follow-up shot: the previous result is uploaded first and named as the scene, the original portrait is named for the face, and only the camera angle and framing are new*

</example>

<example use_case="product-restage">

```text
Beautiful high-end product photograph of the exact yellow enamel kettle from the reference image, product unchanged (yellow enamel with small chips, black wooden handle and knob, black KREA print). It rests on a travertine counter in front of a sleek modern kitchen with fluted wood panels, styled with related tea items: a black cast-iron teapot, small handleless tea cups, a tin of loose-leaf tea with a wooden scoop, a jar of honey and a linen napkin. Warm diffused light, elegant, minimal, premium editorial photography.
```

*Why: Krea's product example: the product is pinned with "exact" and "unchanged" and its identifying marks (chips, handle, the printed word) are listed, then the new scene, props, and light are written as a full brief*

</example>

## Boxes and labels

<rules id="regions">

- Where the host lets you draw boxes on an input image, each box has a label, and the prompt refers to it as `@label`. Boxes without a label are `@1`, `@2`, and so on, in drawing order. Labels take no spaces.
- A box can carry its own note, a short instruction for that region, and a note can point at other boxes by label. When the notes carry the whole edit, the main prompt can be left empty.
- Reach for boxes when words cannot single out the target, such as one of several similar objects, and still say in words what should appear in the box.
- Box coordinates are a host parameter and out of scope here; this section covers only how the prompt refers to them.

</rules>

<example use_case="labeled-boxes">

```text
Replace the armchair in @1 with the oxblood velvet lounge chair from image 2, and put the brass floor lamp from image 3 in @lamp. Keep the rug, the window and the light in the room exactly as they are.
```

*Why: guide-built: one box is addressed by its default label and one by a custom label, each box gets one object welded to its source image, and the preservation sentence covers the rest*

</example>

## Text rendering

<rules id="text">

- Quote every string the output must contain, in full, in straight double quotes. Spell the words out; text that is only described comes out garbled.
- For a text swap, quote the old string and the new one, and say the typeface, color, and position stay.
- For a translation, name the target language and say all of the text should change, so no line is left in the source language.
- Lines you do not mention are expected to survive an edit. When no new text should appear, say "no added text".
- Dense small text is a known weak spot: keep strings short and large in the frame.

</rules>

<example use_case="text-swap">

```text
Change the headline "Night Shift" to "Day Break". Keep the layout, the typeface, the colors and every other line of text exactly as they are.
```

*Why: guide-built from the poster retitle in Krea's technical report: both strings are quoted, and the preservation sentence protects the other lines, which the model's training rewards it for keeping*

</example>

<example use_case="translate-all">

```text
Translate the text into English.
```

*Why: Krea's own instruction from its technical report; the whole poster is the target, so a short instruction is enough, and the expansion step lists each line to translate*

</example>

## Text-to-image

<rules id="t2i">

- With no input image, Krea 3 generates from the text alone. Write a full brief: the medium or photographic genre, the subject and its action, the setting, the light with its source and direction, the camera and lens, the composition, and the palette, with any text quoted.
- For open-ended aesthetic exploration, style references, or a creativity control, use Krea 2 instead.

</rules>

<example use_case="text-to-image-brief">

```text
An editorial photograph captured with a 50mm lens at a low angle features a single hand-thrown ceramic coffee cup with a textured cream-colored glaze. The cup sits in the lower-left quadrant of the frame, resting on a sunlit linen tablecloth with a heavy natural weave and soft creases. Beside the cup, a small matte silver spoon lies on the fabric, and thin wisps of steam rise vertically from the dark coffee inside. Bright, diffused morning light streams from a window on the far left, illuminating the rim of the cup and casting soft, elongated shadows to the right across the textured linen. The background consists of a softly blurred kitchen interior with a white wall and a wooden chair, rendered with a shallow depth of field that keeps only the cup and immediate surface in sharp focus. In the top right of the frame, the text "Your morning coffee" is printed in a clean, minimalist serif font. The composition is balanced and airy, emphasizing the tactile materials of the ceramic and linen.
```

*Why: the expanded prompt fal returns for its text-to-image sample, which shows the shape the expansion step aims for: genre and lens first, then subject, placement, light with direction, background, and the in-image text quoted with its typeface and position*

</example>

## Thinking level and expansion

<rules id="thinking">

- Expansion is always on at Krea; a thinking level, where the host exposes one, sets how much it plans before generating.
- Start at the default level for clear, single edits and everyday requests.
- Raise it for complex or multi-step edits, for several references to combine, or when the default result missed the request. Rewriting the prompt is the other fix; try the higher level first when the prompt is already clear.
- Keep the top, agentic level for final edits where quality matters more than time. It needs at least one input image and takes no negative prompt.
- Where a host lets you switch expansion off, write the full recipe yourself: describe the finished image completely, place each kept element, and quote every string of text.
- Reusing a seed does not reproduce an image exactly, because the expansion can differ between runs. To hold a result, keep the image and edit from it.

</rules>

<example use_case="what-expansion-writes">

```text
In the scene of <image-1>, the speckled tan coffee cup is replaced by a solid blue ceramic cup with a matte-glazed finish. The blue cup is filled with dark coffee, and delicate wisps of steam rise vertically from its surface. The cup rests on the textured beige linen tablecloth in the same position as the original, catching the bright, natural light from the window on the left and casting a soft shadow onto the fabric. The silver spoon remains on the table to the left of the cup exactly as in the original image. The text "Your morning coffee" remains in the top right corner of the frame in its white serif font. The background, including the window and the blurred kitchen interior, remains unchanged.
```

*Why: the expanded edit recipe fal returns for its cup-swap sample, in fal's `<image-1>` notation; it is the form to write by hand when expansion is off: the change, how it sits in the light, then each kept element and the kept text placed explicitly*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- The main levers are positive: the closing preservation sentence, and "only" for single-target edits.
- Put exclusions inline as short "no ..." clauses at the end of the brief, the way Krea's own prompts do: "no gradient, no added text", "no other marks on the dial, no extra props, no people".
- A negative-prompt field exists on Krea's API and on some hosts. Keep it for a specific defect that keeps coming back, not for things the preservation sentence already covers. It is not available at the top thinking level.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Listing everything that stays: name the few things that matter (label, face, framing); unmentioned things already stay.
- Vague target: name the exact object, part, or region, and use "only".
- Whole object changed when a part was meant: name the part ("the leaf ornaments", "the strap").
- Ambiguous references: give each image a number, say what it shows, and give it one role.
- Implied text: quote every string in full.
- Chaining global edits on the latest output: artifacts accumulate; use the local-edit mode for local changes and start global edits from the original or an approved image.
- Expecting weighted style references or a creativity control: those are Krea 2 tools.
- Expecting a seed to reproduce an image: the expansion varies; keep the image instead.
- Identity drift across shots: upload the clearest face reference, name it, and list the identifying features in parentheses.
- Upscaled or crowded references: send originals, and fewer of them when fine detail matters.

</rules>

## Sources

Trust order: official beats provider beats community, and official wins on any conflict. Krea's API reference governs where Krea's own surfaces differ; the launch post's "start with what stays" ordering is a tolerated variant. fal's prompting guide reproduces Krea's own example collection, and its endpoint pages supply the expanded-prompt samples and the `<image-N>` tag form.

- Official (Krea): [Krea 3 API overview](https://www.krea.ai/docs/developers/krea-3/overview), [Krea 3 user guide](https://www.krea.ai/docs/user-guide/features/krea-3), [Introducing Krea 3](https://www.krea.ai/blog/introducing-krea-3), [Krea 3 technical report](https://www.krea.ai/blog/krea-3-technical-report), [Krea prompting guide: reference-driven image editing](https://app.notion.com/p/krea-ai/Krea-prompting-guide-Reference-driven-image-editing-3f4805facfb7810d8e3ec81cb9be65e2), [Krea changelog](https://www.krea.ai/docs/changelog).
- Provider: [fal Krea 3 prompting guide](https://fal.ai/learn/tools/krea-3-prompting-guide), [fal Krea 3 overview](https://fal.ai/krea-3), [fal Krea 3 Edit](https://fal.ai/models/krea/v3/edit), [fal Krea 3 Text to Image](https://fal.ai/models/krea/v3/text-to-image), [fal Krea 3 Realtime](https://fal.ai/models/krea/v3/realtime).

Last verified: 2026-11-08.
