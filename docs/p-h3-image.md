---
guide: "P-H3-Image"
prompt_scheme: "p-h3-image"
# Pruna AI's open-weights image model, a fine-tune of the MiniMax-H3 video model. Image only; MiniMax H3's video prompting is a different scheme with its own guide.
models:
  - { id: "P-H3-Image", access: "open-weights", tier: "distilled", caps: [text-to-image, image-edit, multi-image-reference, text-rendering], best_for: "documentary and editorial photography, portraits with real skin texture, film frames, TV-style anime, drawings, prints and flat graphic design with short quoted text; text-to-image and editing with several reference images. Step- and guidance-distilled, so there is no CFG and no negative prompt, and it is sensitive to how the prompt is written" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering]
prompt:
  languages: ["en"]
  formula: "open by saying what the image physically is (a photograph by a street photographer, a frame from an anime TV series, a two-color risograph print), then describe one scene: a viewpoint, one main subject caught in a moment, a few supporting elements, and light with a source and a direction"
  literal_text: "spell out every word in quotes, keep each string short, say where it sits, and end with 'There is no other text.' If you want no text, do not mention signs or labels at all"
  length_strategy: "a full, specific prompt of a few sentences to a few short paragraphs. Very short requests give weak results unless the bundled upsampler expands them; very long prompts make images worse"
  auto_expand_behavior: "YES by default. A bundled prompt upsampler rewrites every request into the full prompt the model renders best, for the requested aspect ratio, or into an edit brief. Remove or switch it off to render a prompt exactly as written"
  negatives: "none. The model is guidance-distilled: no negative prompt and no CFG. State the wanted image; for no text, leave signs and labels out of the prompt"
  references: "Picture 1 is the image to edit; references follow as Picture 2, Picture 3 and so on. A hand-written edit opens 'Edit <Picture 1>.' and names references as <Picture 2>; a short request to the upsampler can name them any way"
  edit_form: "Edit <Picture 1>. {the change, described as the finished result}. Keep {everything that must stay} exactly as it is."
sources:
  official: ["https://huggingface.co/PrunaAI/P-H3-Image", "https://huggingface.co/PrunaAI/P-H3-Image-Comfy", "https://www.pruna.ai/blog/oss-p-h3-image-launch", "https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/p_h3_image.md"]
  provider: []
  community: []
last_verified: "2026-11-08"
---

# P-H3-Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution limits, image counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- P-H3-Image is Pruna AI's open-weights image model, fine-tuned from the MiniMax-H3 video model. It makes single images, by text-to-image or by editing with reference pictures. It does not make video or audio, and MiniMax H3's video prompting guide does not apply to it.
- Write plain natural-language prose. There is no JSON prompt form, no weighting syntax and no tag list.
- A prompt upsampler ships with the model and rewrites every request by default. Decide first whether you are writing a short request for the upsampler or the full prompt the model renders; the rules below are for the full prompt, which is also what to write when the upsampler is switched off.
- There is no negative prompt and no guidance scale. Everything is said in the positive prompt.

</rules>

## TL;DR

<template id="quickstart">

A {what the image physically is: a photograph by..., a frame from..., a print of...}. {Viewpoint}, {one main subject caught in a moment}, {a few supporting elements}. {Light, with its source and direction}. {Each piece of text in quotes, with where it sits.} There is no other text.

</template>

## Models and when to use which

There is one model, shipped three ways that prompt identically: the diffusers pipeline, ComfyUI files in full, 8-bit and 4-bit precision, and a small LoRA that turns an existing MiniMax-H3 install into P-H3-Image. The 8-bit build stays very close to full precision; Pruna says the 4-bit build "keeps the quality but can change small details and sometimes the composition", so expect the same prompt to land slightly differently there.

It is step- and guidance-distilled from MiniMax-H3. Pruna reports that "for most prompts, the 8-step model matches the 50-step original", but distillation removes the guidance knob: there is no negative prompt to push against, and the prompt text is the only control. That is why the owner calls it "sensitive to prompting".

Pruna names its strengths as "documentary and editorial photography, portraits with real skin texture, film frames, TV-frame anime, ink and charcoal drawings, screen-printed posters and flat graphic design with short quoted text".

## How the model reads prompts

- IT RENDERS FULL PROMPTS, NOT REQUESTS. "P-H3-Image is sensitive to prompting and renders full, specific prompts much better than short requests." A one-line request is the upsampler's input, not the model's.
- THE FIRST SENTENCE SETS THE LOOK. Naming the real object the image is "sets the look more reliably than any style word".
- HYPE WORDS HURT. "Stunning, epic, cinematic, vibrant, hyper-detailed, 8k or masterpiece push P-H3-Image toward a glossy, oversaturated, airbrushed look."
- LENGTH CUTS BOTH WAYS. "Hype words and very long prompts make images worse, and very short prompts give weak results without the upsampler."
- UNQUOTED TEXT BECOMES PSEUDO-TEXT. "Text without its exact words turns into pseudo-text."
- WHAT YOU MENTION TENDS TO APPEAR. With no negative prompt, mentioning a sign, a label or a caption invites one. Leave out what you do not want.

## Prompt structure

<rules id="structure">

- Open with one sentence that says what the image is, as a real object: "a photograph by an experienced street photographer", "a frame from a Japanese anime TV series", "a two-color risograph print", "a flat scan of a handwritten recipe card".
- Describe one scene: "a viewpoint, one main subject caught in a moment, a few supporting elements, and light with a source and a direction".
- Give the light a source and a direction ("low winter sun from the left", "a single bare bulb overhead"), not a mood word.
- Name materials and physical details rather than quality adjectives.
- Keep the aspect ratio of the canvas in mind. The upsampler writes for the aspect ratio of the requested size, so a prompt written for a tall frame suits a tall canvas.

</rules>

<template id="general">

{A/An} {what the image is}{, framing or format}. {Viewpoint}. {Main subject} {caught in one moment}. {Two or three supporting elements, placed}. {Light: source, direction, quality}. {Texture or medium detail}. {Quoted text with placement, if any.} {"There is no other text." if text appears.}

</template>

<example use_case="flagship-handwritten-recipe-card">

```text
A flat photograph of a handwritten recipe card on warm cream index card stock with a slightly soft, uneven texture, shot straight down, filling the entire frame edge to edge. The card has faint blue ruled lines and a thin red top margin line. The handwriting is in blue ballpoint pen with a natural, slightly uneven hand, and a few small ink smudges.

At the top, in larger hand-lettered capitals with a little underline swoosh: "GRANDMA'S BANANA BREAD". Beneath it, in smaller script: "Makes one 9x5 inch loaf · 1 hour".

The left column is headed "INGREDIENTS" underlined twice, with a small hand-drawn banana doodle beside it. Items are listed with a short dash before each, in this order:
- "3 ripe bananas, mashed"
- "1/3 cup melted butter"
- "3/4 cup sugar"
- "1 egg, beaten"
- "1 tsp vanilla"
- "1 1/2 cups flour"
- "1 tsp baking soda"
- "pinch of salt"

The right side is headed "STEPS" with a small hand-drawn heart. Five numbered steps, each one line, written in the same pen:
1. "Preheat oven to 350°F and grease pan."
2. "Stir butter into mashed bananas."
3. "Mix in sugar, egg and vanilla."
4. "Add baking soda, salt and flour; stir gently."
5. "Bake 60 minutes until toothpick comes out clean."

A small coffee ring stain sits in one lower corner, and a tiny doodled smiley face and two hearts decorate the bottom margin. A faint pencil sketch of a loaf with a slice cut away sits in the empty lower-right area. There is no other text.
```

*Why: Pruna's own prompt from the model card. The first sentence says what the image is and how it was shot, every string that must appear is quoted with its place and order, the hand and pen are described once for all of it, and "There is no other text." closes the list. Pruna reports the handwriting follows the quoted text almost word for word*

</example>

<example use_case="painting-in-one-sentence">

```text
A German Expressionist oil painting of a Berlin street at night in the manner of Ernst Ludwig Kirchner, with gaunt figures hurrying past a glowing gas lamp.
```

*Why: Pruna's quickstart prompt. Even a single sentence follows the formula: what the image is (an oil painting in a named manner), one scene, one subject in motion, and a light source*

</example>

## Text rendering

<rules id="text">

- Put each piece of text in quotes, exactly as it should read, and say where it sits.
- Keep each string short. "Small or dense text, such as body copy or long code, turns into pseudo-text, and longer passages sometimes get single letters wrong. Short quoted strings render well."
- Give each text element its hand or typeface and size in words ("larger hand-lettered capitals", "smaller script").
- For lists, quote each item and state the order ("in this order:").
- End with "There is no other text." when text appears.
- If you want no text at all, do not mention signs, labels, captions or screens.

</rules>

<example use_case="graphic-print-short-text">

```text
A two-color risograph print in fluorescent pink and teal on off-white paper, with visible grain and slight misregistration between the two inks. A cyclist in a cap rides uphill out of the bottom-left corner, leaning into the pedals, a row of simple flat hills behind him and a large round sun in the upper right. Across the top, in bold condensed capitals: "TOUR DE BAKERY". In small type along the bottom edge: "SUNDAY 7 AM". There is no other text.
```

*Why: built to Pruna's four rules for one of its named strong styles. The medium is stated as a physical print with its inks and flaws, the scene has one subject in a moment, both strings are short, quoted and placed, and the closing line stops invented text*

</example>

## Image editing

Pass the image to edit as Picture 1, and any references after it. Pruna's warning: "As typed, P-H3-Image often redraws the whole scene. As an edit prompt, only the requested part changes."

<template id="edit">

Edit <Picture 1>. {The change, described as the finished result}. Keep {everything that must stay} exactly as it is.

</template>

<rules id="edit">

- Open with "Edit <Picture 1>." Without the upsampler, any other instruction gets that prefix added for you, so write the rest to read naturally after it.
- "Point to the exact thing. Name the object, person or text you mean and where it is, such as "the old man's faded blue cap" rather than "his hat"."
- "Describe the result, not the action. Say how the edited part looks in the finished image, and give new things a size next to something already there, such as "about the size of the cat's head"."
- "Say what stays. List what must not change, such as faces, poses, the background and the light. Without this list, P-H3-Image tends to redraw the whole image."
- "Quote new text exactly. Put new text in quotes and name the text around it that must stay."
- Keep a hand-written edit to one paragraph. The model expects either a single paragraph that starts "Edit <Picture 1>." and contains "Keep", or the upsampler's full brief.

</rules>

<example use_case="edit-named-target">

```text
Edit <Picture 1>. The old man in the rowing boat now wears a snug red knitted beanie in place of his faded blue cap, covering the top of his head down to just above his eyebrows. Keep his face, smile, white stubble, purple work jacket, hands on the oar, the boat, the harbor with its fishing boats, and the pink sunset light exactly as they are.
```

*Why: built from one of Pruna's edit requests ("give him a red beanie") in its hand-written form. The old hat is named exactly, the new one is described as it looks and where it sits, and the keep list covers the face, clothing, pose, setting and light*

</example>

<example use_case="edit-text-swap">

```text
Edit <Picture 1>. The chalkboard menu behind the counter now reads "SOUP OF THE DAY" on its top line in the same white chalk lettering, at the same size. Keep the line below it, "LENTIL 4.50", the barista, the counter, the coffee machine and the morning window light exactly as they are.
```

*Why: built to Pruna's text-edit rule. The new words are quoted, the surface and hand are pinned to the original, and the neighbouring text that must survive is quoted inside the keep list*

</example>

## Multiple reference images

<rules id="reference">

- Picture 1 is always the image being edited; the others are references, named "Picture 2, Picture 3 and so on". In a hand-written edit, name them with the same tags, `<Picture 2>`, so they match the labels the model sees in front of each image.
- Give each reference one job and weld it to its source: "the hat from <Picture 2>", "the dog from <Picture 3>".
- Say how big a borrowed object is against something in Picture 1, and where it goes.
- The model composes several references into one scene. Pruna's demonstrations include "eight public-domain portraits composed into one dinner party from a one-sentence request".
- NAME WHAT MOVES, PIN WHAT STAYS: list what must stay from Picture 1 as for any edit.

</rules>

<example use_case="multi-reference-edit">

```text
Edit <Picture 1>. The woman on the park bench now wears the wide-brimmed straw hat from <Picture 2>, tilted slightly back on her head, and the small brown dachshund from <Picture 3> sits on the bench beside her, about the size of her handbag. Keep the woman's face, hair, blue linen dress and pose, the bench, the trees behind her and the soft afternoon light exactly as they are.
```

*Why: built from Pruna's reference request ("give the woman in picture 1 the hat from picture 2") with a third input added. Each reference supplies one thing, the dog is sized against an object already in the scene, and the keep list holds the person and setting of Picture 1*

</example>

## Working with the prompt upsampler

The upsampler is a fine-tuned language model that runs before every render by default. "It thinks about the request first and then writes the prompt." Its output comes back with the image, so you can read what was rendered.

<rules id="upsampler">

- A short request is its intended input: "a red fox in fresh snow at first light" or, for an edit, "make the pickup truck red". Requests can name images any way ("the hat from the second photo").
- For text-to-image it writes "a detailed prompt for the aspect ratio" of the canvas. Its input pairs the request with that ratio, so keep the requested size and the ratio it was told the same.
- It decodes greedily, so the same request always gives the same prompt. To get a different composition, change the request or the seed, not the wording of a rerun.
- For an edit it writes either a one-paragraph "Edit <Picture 1>." prompt or a structured brief whose sections follow MiniMax-H3's reference form (subject definitions, a summary, a retention line per picture). Read that brief as the model's own edit format; for hand-written edits use the one-paragraph form instead.
- Turn the upsampler off to render a prompt exactly as written: when you have written a full prompt by these rules, when exact text must survive unchanged, or when you are comparing prompts. How to switch it off depends on the host.
- Keep it on for one-line ideas. Pruna says it "keeps prompts short and images natural rather than glossy".

</rules>

<example use_case="upsampler-request">

```text
a red fox in fresh snow at first light
```

*Why: Pruna's own request to the upsampler. With the upsampler on, a one-line idea is the right input; the upsampler supplies the medium, viewpoint and light. Without it, write the full prompt instead*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative prompt and no guidance scale. The model is guidance-distilled, so there is nothing for an exclusion field to push against.
- Describe the image you want. To keep something out, leave it out of the prompt rather than naming it.
- For text, close with "There is no other text."; for no text at all, do not mention any surface that could carry it.
- In edits, the keep list does the work exclusions would do elsewhere.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Hype words ("stunning", "epic", "cinematic", "8k", "masterpiece"): they make images glossy, oversaturated and airbrushed. Describe the medium and the light instead.
- A style word instead of a medium: open with the real object the image is.
- Very long prompts: they make images worse. Spend words on the scene, not on adjectives.
- Very short prompts with the upsampler off: write the full prompt or turn the upsampler on.
- Unquoted or long text: quote every word, keep strings short, and expect body copy to fail.
- Mentioning a sign or screen when you want no text: leave it out entirely.
- An edit typed as a bare request with the upsampler off: the model redraws the whole scene. Use the "Edit <Picture 1>. ... Keep ..." form.
- An edit with no keep list: list faces, poses, background and light.
- Pronouns in edits ("his hat"): name the exact object and where it is.
- Applying MiniMax H3's video prompt structure to text-to-image: this is a still-image model prompted in prose.
- Small faces and hands in the background: they break more easily, especially below the recommended resolution; make important people larger in frame.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. The owner is Pruna AI; its model cards, launch post and the diffusers pipeline it contributed are the sources. The launch post says edits take up to nine input images while the model cards say eight; image counts are out of scope here, and the spec table follows the model card. The edit forms (the one-paragraph prompt and the structured brief) are taken from the diffusers pipeline's own validation of what the model edits from. No approved provider hosts the model yet. Adjudications are recorded in `sources/p-h3-image/p-h3-image-notation-resolution.md`.

- Official (Pruna AI): [P-H3-Image model card](https://huggingface.co/PrunaAI/P-H3-Image), [P-H3-Image ComfyUI files](https://huggingface.co/PrunaAI/P-H3-Image-Comfy), [launch post](https://www.pruna.ai/blog/oss-p-h3-image-launch), [diffusers P-H3-Image docs](https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/pipelines/p_h3_image.md).

Last verified: 2026-11-08.
