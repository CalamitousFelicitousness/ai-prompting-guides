---
guide: "FIBO"
prompt_scheme: "fibo"
models:
  - { id: "Fibo-2.0-dev", access: "open-weights", tier: "flagship", caps: [text-to-image, image-edit, masked-edit, multi-image-reference, style-transfer, text-rendering, json-prompts], best_for: "the current full model: generation and editing in one set of weights, with guidance live. Best text, texture and anatomy in the family, the five photographic style modes, and the checkpoint to fine-tune" }
  - { id: "Fibo-2.0-edit-turbo", access: "open-weights", tier: "distilled", caps: [image-edit, masked-edit, multi-image-reference, style-transfer, text-rendering, json-prompts], best_for: "few-step editing only. Same edit grammar as Dev; no text-to-image, no styles, and no guidance, so a negative caption does nothing" }
  - { id: "Fibo-1.5", access: "open-weights", tier: "distilled", caps: [text-to-image, text-rendering, json-prompts], best_for: "few-step 1.x text-to-image. Guidance-free, so the negative has no effect; not for fine-tuning" }
  - { id: "Fibo-Edit-1.5-base", access: "open-weights", tier: "base", caps: [image-edit, masked-edit, multi-image-reference, style-transfer, json-prompts], best_for: "the undistilled 1.x editor with up to four reference images; the first reference sets the output's aspect ratio" }
  - { id: "Fibo-Edit-1.5-turbo", access: "open-weights", tier: "distilled", caps: [image-edit, masked-edit, multi-image-reference, style-transfer, json-prompts], best_for: "few-step version of Fibo-Edit-1.5-base, guidance-free" }
  - { id: "FIBO", access: "open-weights", tier: "legacy", caps: [text-to-image, text-rendering, json-prompts], best_for: "the original JSON-native model. Superseded by Fibo 2.0; its captions still render on 2.0 unchanged" }
  - { id: "Fibo-lite", access: "open-weights", tier: "distilled", caps: [text-to-image, text-rendering, json-prompts], best_for: "guidance-distilled FIBO for fast generation, with a stated slight quality loss against the full model" }
  - { id: "Fibo-Edit", access: "open-weights", tier: "legacy", caps: [image-edit, masked-edit, style-transfer, json-prompts], best_for: "the first FIBO editor: one image, optional mask. Superseded by Fibo-Edit-1.5 and Fibo 2.0" }
capabilities: [text-to-image, image-edit, masked-edit, multi-image-reference, style-transfer, text-rendering, json-prompts]
prompt:
  languages: ["en"]
  literal_text: "exact text in double quotes in a short prompt; in a VGL caption, each line or label is its own text_render entry with the exact string plus location, size, color and font. Fibo 2.0 is also shown each text_render string drawn as a small image, which helps it spell"
  length_strategy: "the model reads LONG structured captions; the owner's training captions averaged about 5,300 characters. Through a host that expands prompts, write a concrete one-paragraph brief and let the helper write the caption; written by hand, fill every field the image needs"
  auto_expand_behavior: "YES, host-side and by design. Bria's API, FAL and the owner's bria-vgl package pass a short prompt or edit instruction to a helper LLM that writes the full VGL caption, and return that caption. A host that accepts the caption directly skips the helper"
  negatives: "no negative input on the Fibo 2.0 hosts. Self-hosted, the negative is itself a VGL caption: Dev text-to-image uses a caption describing soft, plastic, artifact-laden images; edits use the empty caption; each style mode has its own; 1.x FIBO used a short VGL fragment for photographs. Distilled checkpoints ignore negatives"
  structured_json: "NATIVE. The model is trained on VGL: one JSON object with short_description, objects, background_setting, lighting, aesthetics, photographic_characteristics, style_medium, text_render, context, artistic_style, plus edit_instruction for edits. Every FIBO generation shares these fields"
  references: "in a multi-image edit, name the images <image_1> to <image_4> in the order they are passed, each exactly once, and say what each contributes. The first image is the one being edited"
sources:
  official: ["https://huggingface.co/briaai/Fibo-2.0-dev", "https://huggingface.co/briaai/Fibo-2.0-dev/blob/main/vgl/README.md", "https://huggingface.co/briaai/Fibo-2.0-edit-turbo", "https://github.com/Bria-AI/vgl", "https://docs.bria.ai/vgl", "https://docs.bria.ai/image-generation-best-practices", "https://docs.bria.ai/image-editing-best-practices", "https://docs.bria.ai/whats-new/fibo-2", "https://huggingface.co/briaai/FIBO", "https://huggingface.co/briaai/Fibo-lite", "https://huggingface.co/briaai/Fibo-1.5", "https://huggingface.co/briaai/Fibo-Edit", "https://huggingface.co/briaai/Fibo-Edit-1.5-base", "https://huggingface.co/briaai/Fibo-Edit-1.5-turbo", "https://huggingface.co/briaai/FIBO-gemini-prompt-to-JSON", "https://huggingface.co/briaai/FIBO-edit-gemini-prompt-to-JSON", "https://github.com/Bria-AI/FIBO", "https://github.com/Bria-AI/bria-skill"]
  provider: ["https://fal.ai/models/bria/fibo-2/generate", "https://fal.ai/models/bria/fibo-2/edit", "https://fal.ai/models/bria/fibo/generate", "https://fal.ai/models/bria/fibo-edit-1.5"]
last_verified: "2026-10-25"
---

# FIBO: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, step counts, resolution and code, consult the host's docs or the spec table; they are out of scope here.
- FIBO is prompted in VGL ("Visual GenAI Language"): one JSON object that describes the image field by field. Every FIBO generation, 1.x and 2.0, was trained on the same fields, so this is one guide.
- There are TWO WAYS IN, and the host decides which you write. Most hosts take a short prose prompt (or an edit instruction) and have a helper LLM write the VGL caption for you. Some also take the caption itself. Write a brief for the first, write VGL for the second.
- Every field except `edit_instruction` DESCRIBES the image. Instructions belong only in an edit instruction.
- Write in English. The helpers write English captions and the 1.x cards tag English only.
- Edit mode is a different input, not a different grammar: the same caption fields, describing the RESULT, plus one imperative instruction.

</rules>

## TL;DR

<template id="quickstart">

Short prompt (most hosts): {medium or "photograph"} of {subject with concrete appearance}, {environment}. {composition and framing, incl. negative space for copy}. {lighting: type and direction}. {materials and color}. {exact text in "double quotes" with placement and typeface}.

Edit instruction: {verb} {target, unambiguous} {to the new state}. Keep {invariants} unchanged. Match {shadows, perspective, scale, light}.

</template>

## Models and when to use which

- `Fibo-2.0-dev` is the one to use. Generation and editing share one set of weights, guidance is live, and it carries the best text, texture and anatomy in the family. `Fibo-2.0-edit-turbo` is its few-step editor: same edit grammar, no text-to-image.
- The 1.x line splits generation and editing across checkpoints: `FIBO` and its distillations `Fibo-lite` and `Fibo-1.5` generate; `Fibo-Edit` and the `Fibo-Edit-1.5` pair edit, with multiple references arriving in 1.5.
- Captions transfer forward. The owner states that FIBO and Fibo 1.5 captions "work with Fibo 2.0 as they are"; the only 1.x-only keys, two quality scores inside `aesthetics`, are dropped by the 2.0 pipeline.
- DISTILLED CHECKPOINTS (Lite, 1.5, both Turbos) run without guidance. A negative caption has nothing to push against there, and the owner says so: on 1.5 the negative "has no effect". What distillation costs in output quality is stated only for Lite, as a "slight quality degradation compared to the full model".
- `Fibo-Edit-RMBG` is a background-removal fine-tune driven by a fixed instruction. There is nothing to write for it, so it is not covered.

## How the model reads prompts

- THE CAPTION IS LONG BY DESIGN. FIBO was "trained on structured JSON captions of up to 1,000+ words that describe lighting, composition, color, camera and depth of field explicitly". One owner style prompt puts the training average at about 5,300 characters. A one-line prompt sent straight to the model is far outside that distribution; a host's helper exists to close the gap.
- THE HELPER FILLS GAPS. Given a short prompt, it invents the details you left out: framing, light, lens, background. So "the more concrete your input, the less the bridge has to guess, and the less you'll need to correct the JSON". Anything you care about, state.
- The helper defaults to a photograph and frames people closely. Name another medium if you want one, and ask for a wide scene if a person should be small in frame.
- FIELDS ARE DISENTANGLED. Lighting, camera, each object and the background are separate fields, so one can change without the rest drifting. This is why the owner's workflow is "generate once, then change one thing at a time" rather than rewriting the prompt.
- A plain sentence sent directly to the model also works, but "a full caption gives much more control".
- Hosts return the caption they generated. Keep it with its seed: sending both back reproduces the image, and adding a short change to them refines it.
- Fibo 2.0 sees each `text_render` string drawn as a small black-on-white image next to the caption, which is what makes its spelling reliable. This only happens for JSON captions; a prose prompt sent straight to the model gets no spelling aid.

## Writing a short prompt for a host

<rules id="brief">

- Write a "shot spec", the owner's term: SUBJECT, ENVIRONMENT, COMPOSITION, LIGHTING, STYLE OR MEDIUM, and CONSTRAINTS (what must stay, what to avoid, required text).
- Spend words on concrete visual controls, not superlatives. Asked whether "ultra, 8K, masterpiece" helps, the owner answers "Usually no."
- For photorealism name what a photographer would: the light's type and direction ("soft diffused key light from upper left"), the angle and placement ("3/4 angle, centered, negative space on right"), materials ("matte ceramic, crisp reflections"), the background ("white seamless, subtle shadow").
- Compose for the frame in words. Aspect ratio is set by the host, not the prompt, so write the placement it implies: "subject slightly left of center with negative space on the right for copy".
- A long brief can be organized the way the owner's own showcase prompt is: an opening sentence fixing era, genre, camera, lens, angle and light, then labeled paragraphs such as "Scene:", "Background:" and "Light and character:".
- Quote every piece of text exactly and give its placement, typeface and clarity: "Put the exact text verbatim in quotes and specify: Placement ... Typography expectations ... Clarity".
- Name public figures and protected brands and you may get a generic result; the owner warns these trigger an IP filter.

</rules>

<example use_case="shot-spec-product">

```text
Studio product photo of a matte black insulated travel mug on a white seamless background. 3/4 angle, centered subject with clean negative space on the right. Soft diffused key light from upper left, subtle shadow, crisp edges, realistic materials.
```

*Why: the owner's copy-ready product prompt. Subject and material, background, angle and placement with room for copy, then light with its direction, and no superlatives*

</example>

<example use_case="text-in-image-brief">

```text
Balloon lettering spelling exactly 'HAPPY NEW YEAR 2026', centered, high contrast on white background, soft studio lighting, crisp edges, realistic foil reflections.
```

*Why: the owner's text example. "Spelling exactly" plus the quoted string, then placement, contrast and edge clarity, which is the owner's three-part rule for text*

</example>

<example use_case="flagship-editorial-brief">

```text
An early-2000s fashion editorial photograph in the desert at dusk, shot on a digital camera with a wide-angle lens from a low angle, lit with a strong off-camera flash against the ambient sky.

Scene: a young woman with shoulder-length dark brown hair, windswept and flying, twists mid-motion, her body turning away while she looks back over her shoulder at the camera, lips slightly parted. She wears wraparound mirrored silver sport sunglasses, a heavy silver chain necklace, a fitted white ribbed tank top and loose light-grey cargo pants with large side pockets, sitting low on the hips. Her right arm swings out behind her, fingers spread. A burst of kicked-up sand billows around her legs and to the lower left, grains frozen in the air. She stands center-right, cropped mid-thigh at the bottom edge.

Background: flat scrubby desert with sparse dry bushes and footprints in the sand, low dark mountains along the horizon. Deep cobalt-blue sky with streaks of grey-violet clouds, a glowing orange and gold sunset band along the left horizon.

Light and character: hard flash from front-left lighting the subject brightly against the darker ambient sky, glossy highlights on skin, her long shadow cast across the sand to the right. Saturated blues and warm skin tones, high contrast, slightly underexposed background, crisp detail in the ribbed fabric, chain links and sand grains. Y2K action-editorial energy, dynamic and confident.
```

*Why: the owner's Fibo 2.0 API showcase prompt. One sentence fixes era, camera, lens, angle and light; then each paragraph maps onto caption fields (the subject's pose, clothing and placement; the background; lighting and aesthetics), so the helper has almost nothing to invent*

</example>

## Writing a VGL caption directly

Use this when the host takes a structured prompt, or when you refine a caption a host returned.

<rules id="vgl">

- One JSON object. Top-level keys, in the order the owner writes them: `short_description`, `objects`, `background_setting`, `lighting`, `aesthetics`, `photographic_characteristics`, `style_medium`, `text_render`, `context`, `artistic_style`; and for an edit, `edit_instruction` last.
- `short_description`: a summary of the whole image, 200 words at most.
- `objects`: the prominent subjects only, each "one object, or one group of similar objects". Each takes `description` (100 words at most), `location` in the frame ("center", "top-left", "bottom-right foreground"), `relationship` to the others, and optionally `relative_size` ("small", "medium", "large within frame"), `shape_and_color`, `texture`, `appearance_details`, `orientation` ("facing left", "lying on its side") and `number_of_objects` (an integer, for a group).
- People also take `pose`, `expression`, `clothing`, `action`, `gender` and `skin_tone_and_texture`. A person's left and right are their own: a raised left arm is their left even when it shows on the right of the frame.
- KEEP `objects` TO FIVE. The 1.x helpers cap it there and the 2.0 edit rules repeat it; everything else is background. "Background elements go in `background_setting`, not in `objects`."
- `background_setting`: the environment and every notable background element not listed as an object.
- `lighting`: `conditions` ("golden hour", "studio lighting"), `direction` ("side-lit from left", "backlit"), `shadows` ("long, soft shadows").
- `aesthetics`: `composition` ("rule of thirds", "close-up"), `color_scheme`, `mood_atmosphere`.
- `photographic_characteristics`: `depth_of_field`, `focus`, `camera_angle`, `lens_focal_length` ("portrait lens (e.g., 50mm-85mm)"). Keep it for non-photographs too when you want camera control.
- `style_medium`: the medium ("photograph", "oil painting", "3D render", "digital illustration"). `artistic_style`: three words at most ("realistic", "impressionistic, vibrant, textured"). Default to `photograph` and `realistic` unless you want something else.
- `context`: what kind of image this is ("a product shot for an e-commerce listing").
- TEXT: every piece of text in the image gets its own `text_render` entry, "one entry per line or label", with `text` (exact, never a placeholder), `location`, `size`, `color`, `font` ("bold sans-serif", "handwritten") and optionally `appearance_details` ("embossed on the leather"). List text even when the description also mentions it. Add none the user did not ask for, except text that belongs to an object, like STOP on a stop sign.
- DESCRIBE, DON'T INSTRUCT: "a sad woman", not "make the woman sad".
- KEEP FIELDS CONSISTENT. A snowy forest in the background means the description, the lighting and the mood all agree with snow. When you change one attribute by hand, change it in every field that mentions it; the owner's own one-word edits have left a stale color behind in a second field.
- Do not repeat a detail across fields; put each where it belongs.
- Leave out what does not apply. Empty values are dropped, so a missing key and an empty one are the same.
- Do not invent keys. The bounding boxes, RGB colors and other fields listed on Bria's VGL overview page are not in what Fibo 2.0 was trained on; the owner's caption guide says to use this format instead.
- 1.x captions from the owner's Gemini helper also carry `"preference_score": "very high"` and `"aesthetic_score": "very high"` inside `aesthetics`. Keep them for 1.x checkpoints; Fibo 2.0 drops them.

</rules>

<example use_case="vgl-complete-caption">

```json
{
  "short_description": "A red city bicycle with a wicker basket leans against a white brick wall on a quiet street on a sunny morning. A small wooden sign above it reads \"OPEN\".",
  "objects": [
    {
      "description": "A red city bicycle with a step-through frame, black tyres and a wicker basket on the handlebars.",
      "location": "center",
      "relationship": "Leaning against the wall, below the sign.",
      "relative_size": "large within frame",
      "shape_and_color": "Classic upright bicycle frame, glossy cherry red.",
      "texture": "glossy painted metal and woven wicker",
      "orientation": "side-on, facing left"
    }
  ],
  "background_setting": "A white-painted brick wall with a green wooden door on the right and a cobblestone pavement below.",
  "lighting": {
    "conditions": "bright morning sun",
    "direction": "side-lit from the right",
    "shadows": "crisp shadow of the bicycle cast on the wall to the left"
  },
  "aesthetics": {
    "composition": "centered, eye-level, with the bicycle filling the lower two thirds",
    "color_scheme": "red and green accents on white",
    "mood_atmosphere": "calm, cheerful"
  },
  "photographic_characteristics": {
    "depth_of_field": "deep",
    "focus": "sharp focus on the bicycle",
    "camera_angle": "eye-level",
    "lens_focal_length": "standard lens (e.g., 35mm-50mm)"
  },
  "style_medium": "photograph",
  "text_render": [
    {
      "text": "OPEN",
      "location": "top center, on a sign above the bicycle",
      "size": "medium",
      "color": "white",
      "font": "hand-painted serif",
      "appearance_details": "painted on a small dark wooden board"
    }
  ],
  "context": "A lifestyle street photograph for a café's social media post.",
  "artistic_style": "realistic"
}
```

*Why: the owner's complete caption from its caption guide. One prominent object with location, relationship and size, everything else in the background field, light with a direction and a matching shadow, and the sign's word in text_render even though the description already mentions it*

</example>

## Refining: change one thing

<rules id="refine">

- The owner's workflow: generate once, keep the returned caption and seed, then send the caption back with the same seed and a short change. The helper "rewrites only the fields the change touches and copies the rest".
- Write the change as a short phrase, one attribute at a time: "backlit", "85 mm", "warmer skin tones", "make it night", "Add sunlight".
- Lock the seed while you test a change; change the seed only once the caption is right.
- Editing the JSON yourself works the same way: change the field, keep the seed, regenerate. Change every field that mentions the attribute, not just the first.

</rules>

## Editing an image

The prompt for an edit is still a caption, but of the RESULT, plus `edit_instruction`. Hosts accept a plain-language instruction and write the caption for you.

<rules id="edit">

- Through a host, write the instruction as the owner's formula: TARGET + CHANGE + INVARIANTS + INTEGRATION CUES. Name what changes, what must stay unchanged, and what must match visually ("matching shadows, perspective, scale, and texture").
- Make the target unambiguous: left or right, front or back, color, size. Restate the invariants, such as camera angle, identity, label details, lighting and background; "repeatedly restating the invariants ... helps prevent drift."
- Full sentences are fine at the host. The helper rewrites them into the model's trained form.
- In a hand-written edit caption, `edit_instruction` is ONE IMPERATIVE COMMAND starting with a verb: Add, Change, Make, Move, Remove, Render, Turn, Zoom. A replacement is "Change the X to Y". Never mention "the original image" or "the reference image".
- Every other field DESCRIBES THE RESULT, copying everything the edit leaves alone (subjects, pose, composition, camera, style) word for word. Outside the instruction, avoid "changed", "added", "removed", "replaced", "now" and "originally": write "his hands are empty", not "the book was removed".
- A plain instruction string with no caption is also accepted by the Fibo 2.0 pipeline.
- To change text on a sign: `Change the text "Happy Anniversary" to "Hello".`

</rules>

<rules id="mask">

- With a mask, white marks the region to regenerate and everything else is kept. The region is regenerated, not retouched.
- Make the mask a little larger than the object, especially around hair, glass, fabric edges and contact points.
- Name "the masked region" in the instruction and describe what fills it in detail: material, size, how it meets the surface, a contact shadow. "Generate a white rose with a blue center in the masked region."
- Describe the content that fills the mask, never the mask itself.

</rules>

<rules id="multi-reference">

- The image being edited comes first; references follow. Name them `<image_1>`, `<image_2>`, up to `<image_4>`, in the order they are passed, each exactly once.
- Say what each reference contributes, not just that it exists: "the perfume bottle from <image_2>", "the warm side lighting ... from <image_2>".
- Each image is a separate source, not another view of the same scene.
- Bria's agent skill writes "image 1" in plain words instead and the host's helper accepts that, but `<image_1>` is the form the model is trained on and the form hosts return. Use it.
- On the 1.5 editor the first image also sets the output's aspect ratio.

</rules>

<example use_case="edit-with-invariants">

```text
Replace the bottle cap with brushed aluminum. Keep the bottle shape, label text, camera angle, and background unchanged. Match reflections and contact shadows to the original studio lighting.
```

*Why: the owner's formula in one go. Target and change in the first sentence, the invariants named in the second, and integration cues for the new material in the third*

</example>

<example use_case="multi-reference-three-images">

```text
Create a luxury fragrance poster by placing the perfume bottle from <image_2> upright on the grey boulder in the misty water from <image_3>, and add the minimalist typography from <image_1> in the upper sky.
```

*Why: the owner's poster edit as FAL documents it. Three inputs, each named once with the one thing it contributes (bottle, setting, typography) and where it goes*

</example>

<example use_case="multi-reference-four-images">

```text
Place the bottle from <image_2> in the woman's hand from <image_1> and the sunglasses from <image_4> on her face, make her wear the purple t-shirt from <image_3>, making sure the text on her shirt is visible.
```

*Why: a Fibo-Edit-1.5 instruction from FAL's page. The edited subject is <image_1> and each of three references donates exactly one item to a named place on her, with the text on the shirt protected*

</example>

<example use_case="restage-with-lighting-reference">

```text
Restage the serum bottle from <image_1> on a pale lavender stone plinth. Use <image_2> as a reference for the warm side lighting and peach background. Keep the bottle's shape, cap, label text, and colors consistent with <image_1>. Leave space to the right for campaign copy.
```

*Why: FAL's Fibo 2.0 edit example. One image supplies the product and the other only the light and backdrop, the product's invariants are listed, and the frame is composed for copy*

</example>

<example use_case="pure-style-transfer">

```text
Turn the image into the cartoon style.
```

*Why: the owner's edit_instruction for a style change. One imperative sentence; everything else in the caption keeps the source's subjects, pose and composition and only the medium and style fields change*

</example>

<example use_case="style-transfer-plus-edit">

```text
Turn the photo into a soft watercolor illustration and change the woman's coat to mustard yellow. Keep her pose, the street layout and the camera angle unchanged.
```

*Why: built to the owner's rules for a host instruction. The style change and the one content change are each named once, followed by the invariants; the helper turns it into one trained-form command plus a caption of the result*

</example>

<example use_case="masked-fill">

```text
Create the following background in the masked region: A vast ocean extending to horizon.
```

*Why: the owner's masked-edit instruction form. It names the masked region and describes what fills it, never the mask*

</example>

## Style modes (Fibo 2.0 Dev)

<rules id="styles">

- Five photographic looks ship with Dev: `boring_reality` (plain documentary photo, ordinary light and lens, real wear), `kodak_film` (1990s point-and-shoot film snapshot from a faded print), `hard_flash` (early-2000s compact-camera flash), `hazy_dreamy` (motion-blurred, faded 1960s editorial), `lens_distortion` (fisheye or ultra-wide portrait from very close).
- Each is a complete prompt pair for the helper plus its own negative caption. Text-to-image only; edits and refines keep their own prompts.
- ALWAYS USE THE STYLE'S OWN NEGATIVE. The default negative treats blur, haze and flare as defects, so it erases the film and hazy looks.
- Do not stack a style with a house-style preset; "the styles are whole prompts and were tested on their own".
- Through a host, the style is a separate choice and works with a plain text prompt only. Write the subject; do not try to describe the look as well.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- The Fibo 2.0 hosts take no negative. State exclusions in the brief's constraints instead ("no other elements or text").
- Self-hosted, a FIBO negative is a VGL caption, not a word list. For Dev text-to-image the owner's negative describes what to steer away from: smooth, featureless, plastic-like texture, waxy airbrushed skin, a blurred featureless backdrop, and an `aesthetics.artifacts` list of oversaturated colours, neon colour cast, overexposed highlights, lens flare, blur and haze.
- Edits use the empty caption the model was trained with: every key present, every value empty.
- For 1.x FIBO the owner applies a negative only when the caption is a photograph, and it is a VGL fragment: `{'style_medium':'digital illustration','artistic_style':'non-realistic'}`.
- On distilled checkpoints the negative does nothing.

</rules>

<example use_case="negative-caption-dev-t2i">

```json
{"short_description":"","objects":[{"description":"the main subject","texture":"smooth, featureless, plastic-like, airbrushed, no fine surface detail","appearance_details":"soft blurred edges, simplified shapes, no fine detail","skin_tone_and_texture":"waxy airbrushed skin, poreless, plastic smooth"}],"background_setting":"a plain seamless studio backdrop, perfectly smooth gradient, blurred and featureless, no visible texture","lighting":{},"aesthetics":{"artifacts":["oversaturated colours","neon colour cast","overexposed highlights","lens flare","slight blur","motion blur","haze"]},"photographic_characteristics":{"depth_of_field":"shallow, heavy bokeh obscuring most of the frame","focus":"soft, slightly out of focus, lacking fine texture"},"style_medium":"","context":"","artistic_style":""}
```

*Why: the owner's default Dev text-to-image negative. It is written in the same fields as a positive caption, describing the soft, generated look to avoid; do not use it with the film or hazy style modes*

</example>

## Pitfalls and anti-patterns

<rules id="avoid">

- A one-line prompt sent straight to the model: it was trained on long captions. Send a brief through a host's helper, or write the full caption.
- Superlatives ("ultra, 8K, masterpiece"): the owner says they usually do not help. Spend the words on light, angle, materials and placement.
- Instructions inside caption fields ("make the woman sad"): fields describe. Only `edit_instruction` commands.
- Edit-history words in an edit caption ("now", "replaced", "originally"): describe the result as if it always looked that way.
- An edit with no invariants: the rest can drift. Name what must stay.
- Mentioning "the original image" or "the reference image" in `edit_instruction`: name the image by `<image_N>` or by what it shows.
- An unnamed or doubly named reference in a multi-image edit: name every image once, in order, with its job.
- More than five objects: move the rest into `background_setting`.
- One-field changes in a hand edit: an attribute mentioned in three fields must change in all three.
- Placeholder or paraphrased text: write the exact string, one `text_render` entry per line.
- Inventing keys (bounding boxes, RGB arrays, `relative_distance`): not part of the trained format.
- The default negative with a film or hazy style: it removes the look. Use the style's own negative.
- Expecting a negative to work on Lite, 1.5 or a Turbo: they run without guidance.
- A tight mask: give the model a margin to blend.

</rules>

## Sources

Trust order is official > provider > community; official wins on any conflict. Bria publishes guidance on Hugging Face cards, in its open-source caption writer (`bria-vgl`), on docs.bria.ai and in an agent skill; where these differ, this guide follows the caption guide and the caption writer, because they describe the format the model was trained on and the one every host's helper produces. The adjudications are recorded in `sources/fibo/fibo-notation-resolution.md`.

- Official (Bria): the [Fibo 2.0 Dev](https://huggingface.co/briaai/Fibo-2.0-dev) card and its [VGL caption guide](https://huggingface.co/briaai/Fibo-2.0-dev/blob/main/vgl/README.md), the [Fibo 2.0 Edit Turbo](https://huggingface.co/briaai/Fibo-2.0-edit-turbo) card, the [`bria-vgl`](https://github.com/Bria-AI/vgl) caption writer, the [VGL overview](https://docs.bria.ai/vgl), the [generation](https://docs.bria.ai/image-generation-best-practices) and [editing](https://docs.bria.ai/image-editing-best-practices) best-practice pages, the [Fibo 2 release notes](https://docs.bria.ai/whats-new/fibo-2), the 1.x cards for [FIBO](https://huggingface.co/briaai/FIBO), [Fibo Lite](https://huggingface.co/briaai/Fibo-lite), [Fibo 1.5](https://huggingface.co/briaai/Fibo-1.5), [Fibo Edit](https://huggingface.co/briaai/Fibo-Edit), [Fibo Edit 1.5](https://huggingface.co/briaai/Fibo-Edit-1.5-base) and [Fibo Edit 1.5 Turbo](https://huggingface.co/briaai/Fibo-Edit-1.5-turbo), the 1.x [prompt-to-JSON](https://huggingface.co/briaai/FIBO-gemini-prompt-to-JSON) and [edit prompt-to-JSON](https://huggingface.co/briaai/FIBO-edit-gemini-prompt-to-JSON) helpers, the [FIBO repository](https://github.com/Bria-AI/FIBO), and the [Bria agent skill](https://github.com/Bria-AI/bria-skill).
- Provider: FAL's [Fibo 2 generate](https://fal.ai/models/bria/fibo-2/generate), [Fibo 2 edit](https://fal.ai/models/bria/fibo-2/edit), [FIBO generate](https://fal.ai/models/bria/fibo/generate) and [Fibo Edit 1.5](https://fal.ai/models/bria/fibo-edit-1.5) pages.

Last verified: 2026-10-25.

Coverage notes. The field rules come from the owner's caption guide and from the system prompts of its caption writers, which the caption guide says match how the training captions were written. The 1.x and 2.0 caption writers differ on two defaults: the 1.x writers cap objects at five and leave `text_render` empty unless the user gives exact text, while the 2.0 Generate writer has no object cap and lists text the scene implies; the guide teaches the five-object limit and the caption guide's text rule, which covers both. Bria's docs and its agent skill disagree on quality keywords and on how to name images in a multi-image edit; the guide follows the docs on the first and the caption guide on the second. Bria's VGL overview lists fields (bounding boxes, RGB colors, skin-tone scales, keypoints) that its own caption guide says Fibo 2.0 was not trained on; they are not taught. Step counts, guidance, resolution and the licence are in the spec table. The 1.x cards publish no prompt-length or language guidance beyond tagging English.
