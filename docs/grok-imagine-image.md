---
guide: "Grok Imagine Image (family)"
prompt_scheme: "grok-imagine-image"
models:
  - { id: "grok-imagine-image-2.0", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, reframe], best_for: "the default for new work. Designed around instruction fidelity and planned typography, so posters, infographics, UI mockups, tutorial sheets and any dense multi-element layout land on the first pass. Also the strongest at holding an input's identity across an edit" }
  - { id: "grok-imagine-image-quality", access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, multi-image-reference, style-transfer], best_for: "workflows already validated against it. It was the quality tier before 2.0 took that slot; prefer the flagship for anything new" }
  - { id: "grok-imagine-image", access: "closed-weights", tier: "budget", caps: [text-to-image, image-edit, multi-image-reference, style-transfer], best_for: "volume and speed on low-stakes work: ideation, thumbnails, draft variants, anything where a retry is cheaper than a better first pass" }
capabilities: [text-to-image, image-edit, multi-image-reference, text-rendering, style-transfer, reframe]
prompt:
  languages: ["en"]
  formula: "noun-phrase subject, then scene and action, then light, then medium or style as a trailing clause. Every prompt the owner publishes has this shape"
  literal_text: "wrap the exact words in double quotes and give each string its own typographic level (display, subhead, small print) plus a placement; the model plans type hierarchy before it renders, so an unstated hierarchy is one it invents"
  length_strategy: "write to the level of control you want, not to a word count. Anything you leave out is filled in by a rewriting LLM, so a short prompt is not a neutral prompt, it is a delegated one"
  auto_expand_behavior: "ALWAYS ON and not optional. Every request, generation and edit alike, passes through a prompt-rewriting (upsampler) LLM with its own reasoning budget before the image model sees a word. The owner API exposes no switch; some hosts surface one as a prompt enhancer. Write declarative facts that survive a paraphrase, and quote anything that must arrive verbatim"
  references: "with more than one input image, address them in the prompt as `<IMAGE_0>`, `<IMAGE_1>`, `<IMAGE_2>`, zero-indexed. Declare what each one is before issuing any instruction, then weld every borrowed element to its source"
  editing: "lead with an imperative naming the change, then pin what must not move. The owner's own edit examples are all plain imperatives"
  negatives: "there is no negative field on any surface, and no seed, guidance or style parameter either. Exclusions ride in the positive prompt, and the reliable form is naming what should be there instead of what should not"
sources:
  official: ["https://x.ai/news/grok-imagine-image-2", "https://docs.x.ai/developers/model-capabilities/imagine", "https://docs.x.ai/developers/model-capabilities/images/generation", "https://docs.x.ai/developers/model-capabilities/images/editing", "https://docs.x.ai/developers/model-capabilities/images/multi-image-editing", "https://docs.x.ai/developers/rest-api-reference/inference/images", "https://docs.x.ai/developers/tools/image-generation"]
  provider: ["https://fal.ai/models/xai/grok-imagine-image/api", "https://wavespeed.ai/models/x-ai/grok-imagine-image/edit"]
  community: []
last_verified: "2026-08-15"
---

# Grok Imagine Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and quality settings, reference counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the Grok Imagine IMAGE family. The Grok Imagine video models are a different scheme and are not covered here.
- A rewriting LLM stands between your text and the image model on every request. This is the single fact that shapes everything else below; read the next section before writing anything.
- Write natural-language sentences, not tag soup. Every prompt the owner publishes is a noun phrase describing a finished picture.
- Name the artifact you want (poster, infographic, product shot, title screen, editorial photo). This model was trained around usable design output, and stating the artifact sets both the layout logic and the level of polish.
- There is no negative field. Exclusions go in the prompt, phrased as what should be there.

</rules>

## TL;DR

<template id="quickstart">

{Subject as a noun phrase}, {what it is doing and where}. {Light: direction, quality, time of day}. {Medium or style as a trailing clause}. {Any literal words in double quotes, with their typographic level and placement}.

</template>

## Models and when to use which

All three share one prompt scheme and one reference notation. A prompt written for one transfers unchanged; pick by stakes and cost, not by grammar.

- `grok-imagine-image-2.0`: the default. Instruction fidelity and planned typography are the headline gains, so it is the one to reach for whenever a layout has more than one element or the image carries words.
- `grok-imagine-image-quality`: the previous quality tier, superseded when 2.0 became the quality path. Keep it only for workflows already validated against it.
- `grok-imagine-image`: the cheap fast path. Fine for ideation and drafts.

<rules id="model-choice">

- Do not reach for the top quality setting by reflex. In the owner's own launch leaderboard snapshot, 2.0 was entered at its LOWER quality setting and still placed above the previous quality model on both the text-to-image and image-edit boards. Raise the setting for dense small print and identity-sensitive edits; leave it down for everything else.
- `grok-imagine-image` is not a smaller 2.0. It is the older, cheaper line, so a prompt tuned against 2.0's instruction following will lose detail on it rather than merely lose polish.

</rules>

## How the model reads prompts

Your prompt is not what the image model sees. On both generation and editing, the request first passes through a prompt-rewriting (upsampler) LLM that has its own reasoning budget, and the image model is conditioned on that LLM's rewritten output. The owner documents this in its own token accounting; one approved provider returns the rewritten text as an enhanced prompt, and another exposes the rewriter as a toggle. Through the owner's own API there is no way to switch it off.

Everything below follows from that.

<rules id="rewriter">

- Write declarative facts about a finished picture, not instructions to a system. "A rain-slicked street at dusk" survives a paraphrase; "make sure you really emphasise the rain" is advice to a reader who will not be there.
- Quote anything that must arrive intact. Literal words, proper nouns, and specific model or product names go in double quotes so the rewriter carries them through rather than paraphrasing them.
- Do not use weighting syntax, parenthetical emphasis, token repetition, or any other diffusion-era trick. There is no field for them and a language model normalizes them away. Emphasis comes from being specific and from word order.
- Short prompts are not neutral prompts. Whatever you leave unstated is invented by the rewriter, consistently and confidently. If you care about the lens, the palette, or the time of day, say so.
- Long prompts are safe here in a way they are not everywhere. The rewriter is a language model, so it holds a paragraph together; the failure mode of a long prompt is contradiction, not truncation. Say each thing once.
- Never contradict yourself across a prompt. "Minimalist" early and "richly detailed background" late does not average out; the rewriter picks one and commits.
- If output ignores a detail you stated, restate it as a concrete visual fact rather than louder. "No text" becomes "a blank unmarked wall".

</rules>

## Prompt structure

<rules id="structure">

- Lead with the subject as a noun phrase. Drop the instruction verb: the owner's own tool shows Grok rewriting a user's "Generate an image of a corgi surfing a big wave, in the style of a Japanese woodblock print" into the prompt "A corgi surfing a big wave, Japanese woodblock print style". That compressed form is the target shape.
- Put style last, as a trailing clause. "in the style of a X" compresses to "X style" in the owner's own normalization.
- Order the middle: subject, then what it is doing, then the setting, then the light, then the medium. Front-loaded words carry the composition; trailing words carry the treatment.
- Give light a direction and a quality, not just a time. "Late afternoon sun raking from the left, long shadows" beats "golden hour".
- Name the medium concretely. "Four-ink screen print with visible halftone and slight registration offset" is a target; "beautiful artwork" is not.
- State the frame when it matters. The model reads "portrait", "16:9", "square crop" in the prompt text, and will otherwise pick a frame that suits the described scene.
- Skip quality boosters. "8K", "masterpiece", "highly detailed", "award-winning" spend words without adding a visual target, and the rewriter will replace them with something specific anyway. Describe the finish you want instead.

</rules>

<template id="general">

{Subject as a noun phrase}, {action}, {setting}. {Light: direction, quality, time}. {Foreground and background detail that must be present}. {Medium, palette, and surface treatment}. {Literal text in double quotes with its level and placement}. {Frame}.

</template>

<example use_case="flagship-editorial-poster">

```text
A vintage travel poster for the Amalfi Coast, portrait orientation. A terraced cliff town in warm ochre and coral stacks above a deep teal bay, with a single white ferry cutting a wake toward the harbor. Late afternoon sun rakes across the buildings from the left, throwing long shadows down the staircases and lighting a lemon grove in the foreground. Flat screen-printed color in four inks, heavy paper grain, thin registration offsets at the edge of each shape. The headline "AMALFI" runs across the lower third in a condensed sans serif, letter-spaced wide. Beneath it, smaller and centered, the line "SAIL THE COAST BY SEA". A thin rule separates the two.
```

*Why: the full formula at scale, with the two text strings quoted and each assigned its own level and placement, so the type hierarchy is specified rather than invented*

</example>

## Text in images

Typography is this family's headline strength on 2.0: the owner's claim is that it plans the type hierarchy and the layout before rendering, which is why dense sheets hold together and small print stays legible. Prompt it accordingly. An unstated hierarchy is not an absent one, it is one the model chooses.

<rules id="text">

- Put the exact words in double quotes. Everything inside the quotes is what gets rendered; everything outside describes how.
- Give every string a level and a placement. Display, subhead, and small print are different jobs, and the owner's own text example names two of them at once ("bold retro typography, sharp small print").
- Describe the typeface by shape, not by name. "Condensed sans serif, letter-spaced wide", "bold slab serif", "chrome-beveled display face" are directions; a font name may or may not be known.
- Keep each string short. Long paragraphs of body copy degrade into texture in every model, this one included; render the headline and the labels, and leave real body copy to layout software.
- Spell out anything unusual. Invented band names, product names, and acronyms should appear exactly once, in quotes, with no competing spelling elsewhere in the prompt.
- State what carries no text. A layout that should have a clean area is more reliable when you say "the lower third is empty sky" than when you say nothing.

</rules>

<example use_case="concert-poster">

```text
A concert poster for a synthwave band. A chrome sports car races toward a neon grid horizon under a vast setting sun, cyan and magenta gradients, heavy scanlines and slight chromatic aberration. The band name "NIGHTDRIVE" fills the top third in a wide chrome-beveled display face with a hard specular highlight. Along the bottom edge, in small clean uppercase with generous letter spacing, the sharp print reads "FRIDAY 12 SEPT / THE UNION HALL / DOORS 8PM / 18+". Portrait poster proportions.
```

*Why: two strings, two levels, two placements, with the small print explicitly called sharp, which is the exact capability the model was built around*

</example>

## Structured visuals

Infographics, tutorial sheets, UI mockups, and title screens are the case this family was tuned for, and they are also where vague prompts fail most visibly. Describe the layout as a grid or a flow before describing any cell's contents.

<rules id="structured">

- State the layout skeleton first: how many cells, arranged how. "Four numbered steps in a two by two grid" gives the planner something to plan.
- Label the cells in order, in quotes. Numbering them inside the quoted strings keeps the sequence from being shuffled.
- Say what connects the parts: arrows, rules, connecting lines, a title bar, a legend. Otherwise you get panels rather than a diagram.
- Pin the visual constants across cells: one line weight, one palette, one drawing style. Without it each cell drifts toward its own illustration.
- For UI, name placement explicitly rather than leaving it to inference. A control gets a label and a position: a button labeled "Continue" in the bottom right.

</rules>

<example use_case="infographic">

```text
An illustrated infographic explaining how a French press works, four numbered steps in a two by two grid on cream paper. Each cell holds a simple line drawing of the press at that stage with a short caption beneath it: "1. COARSE GRIND", "2. BLOOM 30S", "3. STEEP 4 MIN", "4. PRESS SLOW". A title bar across the top reads "FRENCH PRESS". Muted olive and rust palette, one consistent thin line weight throughout, generous white space, small hand-lettered annotations with thin arrows pointing to the plunger and the filter screen.
```

*Why: skeleton before contents, captions numbered inside the quotes so the order holds, and the line weight and palette pinned once for all four cells*

</example>

## Image editing

Editing is a first-class capability here rather than a bolted-on mode, and the owner's own edit prompts are plain imperatives.

<rules id="edit">

- Lead with an imperative naming the change: Replace, Add, Remove, Render, Restore, Recolor. The owner's published edit prompts all take this form.
- Separate the change from the preserve. Name the one thing that moves, then name what must stay identical.
- Pin the things that drift silently: face, hairstyle, proportions, logo, label text, palette, contrast, framing, camera angle, and the position of everything you did not mention.
- Make one change per turn. Chaining short edits, each output feeding the next, is the owner's documented refinement path and it beats one instruction carrying three changes.
- Repeat the preserve list on every iteration. Dropping it once is enough to start identity drift, and in a chain that drift compounds.
- Ask for integration when you insert something: match the light direction, the color temperature, the shadow behavior, and the grain, or the addition reads as pasted.
- WaveSpeed recommends phrasing the edit as the desired outcome rather than the process ("the man wearing a red shirt" rather than "change the shirt color to red"). The owner's own examples do the opposite and work, so treat this as a second thing to try when an imperative is being over-applied, not as the house form.

</rules>

<example use_case="scoped-edit">

```text
Replace the plain blue backdrop behind the woman with a softly blurred bookshelf interior lit by warm tungsten light. Keep her face, hair, glasses, posture, and the exact color and weave of her jacket identical. Keep the existing key light on her face and the current framing unchanged. Relight only the edge of her hair and shoulders to match the warmer background so the cutout does not read as pasted.
```

*Why: one change, an explicit preserve list covering the things that shift silently, and a scoped relight that fuses the composite without licensing a re-render of the subject*

</example>

### Style transfer

The family covers a wide stylistic range, from photographic through anime, painting, and pencil. The risk in a style transfer is not the style, it is that the model redraws the scene while it changes the medium.

<example use_case="style-transfer">

```text
Render this as a loose graphite pencil sketch with detailed cross-hatched shading, visible paper tooth, and no color. Keep the composition, the pose, and the proportions of every subject exactly as they are.
```

*Why: the medium is described by its marks rather than named, and the geometry is pinned so the restyle does not become a redraw*

</example>

<example use_case="style-transfer-plus-edit">

```text
Render this as a 1950s screen-printed advertisement in four flat inks with visible halftone dots and slight registration offset. Keep the product, its label text, and the arrangement of the objects on the table exactly as they are. Change the background from the grey studio sweep to a warm mustard field, and add the line "FRESHLY GROUND" in a bold condensed serif across the top edge.
```

*Why: a restyle, a background swap, and a text addition in one pass, held together by an explicit preserve list that protects the one thing a screen-print treatment would otherwise dissolve, the label*

</example>

### Reframing an existing image

The owner ships recomposition as a feature: take one finished image and refill it into a different frame rather than cropping it. Prompt-side, the useful part is saying what must survive the move.

<rules id="reframe">

- Name what must stay in frame and roughly where. A recompose invents new edges, and anything you did not protect can be cropped out to make room.
- Say what the new space should contain. Moving a landscape image into a tall frame creates sky or foreground that did not exist; describe it or it gets invented.
- Keep the style contract in the reframe prompt. Restating the palette and medium stops the extended area from drifting away from the original's treatment.

</rules>

## Multiple reference images

With more than one input, the prompt gains the family's one piece of real notation. Inputs are addressed as `<IMAGE_0>`, `<IMAGE_1>`, `<IMAGE_2>`, zero-indexed, in the order sent. Use it: an unnumbered "the first image" is a description the rewriter can paraphrase, while the token is a handle.

<rules id="references">

- Declare every input before instructing. Give each one a line saying what it is, then issue the instruction. A manifest first, a plan second.
- ONE ROLE PER INPUT. Each image does exactly one job, and every borrowed element is welded to the source it came from.
- NAME WHAT MOVES, PIN WHAT STAYS. Say which element comes from which input, then say what must remain identical about it, per source.
- Address inputs by token and by description together: "`<IMAGE_1>` is a tan leather satchel". The token prevents a swap; the description survives the rewrite.
- State how the inputs interact, in one sentence, using the tokens on both sides.
- Ask for integration explicitly. Match light direction, color temperature, shadow behavior, scale, and perspective so the result reads as one photograph rather than a collage.
- Single-image edits take no token. The notation only applies once there is more than one input, so do not write `<IMAGE_0>` into a one-image edit.

</rules>

<template id="multiref">

`<IMAGE_0>` is {what it is}. `<IMAGE_1>` is {what it is}. `<IMAGE_2>` is {what it is}.
{Imperative combining them, naming each borrowed element and its source token}. Keep {invariant} from `<IMAGE_0>` exactly. Keep {invariant} from `<IMAGE_1>` exactly. {Integration instruction referencing the destination}.

</template>

<example use_case="three-source-composite">

```text
<IMAGE_0> is a studio photo of a woman in a grey knit sweater. <IMAGE_1> is a tan leather satchel on a white background. <IMAGE_2> is a rain-slicked city street at dusk with neon shopfronts.
Place the woman from <IMAGE_0> on the street from <IMAGE_2>, carrying the satchel from <IMAGE_1> over her right shoulder. Keep her face, hair, and the sweater's texture and color exactly as in <IMAGE_0>. Keep the satchel's leather grain, hardware, and strap width exactly as in <IMAGE_1>. Relight her to the street's ambient neon, match shadow direction and color temperature to <IMAGE_2>, and add faint wet reflections beneath her feet so she sits in the scene rather than on top of it.
```

*Why: three inputs declared as a manifest before any instruction, each welded to one role by token, invariants named per source, and an explicit relight plus ground contact so the composite fuses*

</example>

## Character and world consistency

The owner's own demonstration of consistency is a set of separately generated images, a character, her locations, and her props, that hold one look across the set. Nothing in the API carries state between requests, so the consistency is something the prompt does.

<rules id="consistency">

- Write a style contract once: palette, light, medium, surface treatment, lens character. Reuse it verbatim in every prompt in the set. Rewording it is what makes a set drift.
- Describe a character by fixed, nameable attributes rather than by impression: hair color and length, eye color, build, scars, the specific garment and its material. Impressions get re-imagined each time; attributes get carried.
- Keep the contract and the character block in the same position in every prompt. Position is part of what the rewriter is reading.
- Once you have one image you like, switch from describing to referencing: feed it as an input and edit from it. Reference beats description for identity, every time.
- Generate the props and locations against the same contract, not against the character image, or they inherit the character's framing and light.

</rules>

<example use_case="world-set">

```text
A snowbound Norse war camp of hide tents and timber watchtowers under heavy snowfall, seen from a low rise at blue hour. Flat overcast light, desaturated palette of bone white, charcoal, and weathered oak, with a single warm ember glow from a central fire. Painterly matte-illustration style, soft edges, visible brush texture, no lens effects. 16:9.
```

*Why: the second half is a style contract meant to be pasted unchanged into every other prompt in the set, which is what holds a separately generated world together*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field. Not on the owner's API, not on the approved providers. There is also no seed, no guidance control, and no style parameter, so the prompt text is the entire surface you have.
- Write the exclusion as a positive fact. "A blank unmarked wall" is a target the model can render; "no text on the wall" is a target only if the rewriter preserves the negation, and it is one clause among many.
- Where you must state a bare exclusion, keep it short, concrete, and at the end: "no watermark, no extra text, no logos". Name the specific artifact, never a mood.
- Do not build a stock defect block. Some models in this set reward a canonical bank of negative terms; this one has nowhere to put it, and pushing it into the positive prompt spends the rewriter's attention describing things you do not want.
- In editing, the preserve list is the real negative. "Keep her face and jacket identical" excludes far more, far more reliably, than any list of things to avoid.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Tag soup: comma-separated keyword lists get rewritten into prose anyway, and you lose control of the ordering. Write the sentence yourself.
- Weighted or parenthesized emphasis: no field parses it, and the rewriter strips it. Be specific instead.
- Assuming the prompt reaches the model: it does not, and this is the most common source of surprise here. A detail that must survive belongs in quotes or in a plain declarative clause.
- Quality boosters: "8K", "masterpiece", "ultra detailed", "award-winning" add no visual target. Describe the finish.
- Instruction verbs in a generation prompt: "Generate an image of ..." is stripped by the owner's own normalization. Start at the subject.
- Contradiction across a long prompt: "minimalist" plus "richly detailed background" resolves to one of the two, unpredictably.
- Body copy as rendered text: headlines and labels render, paragraphs degrade. Leave real copy to layout tools.
- Unnumbered references in a multi-image edit: "the first image" is paraphrasable, `<IMAGE_0>` is not.
- Using `<IMAGE_0>` on a single-image edit: the notation belongs to the multi-input path only.
- Dropping the preserve list mid-chain: identity drift compounds across a multi-turn edit and is usually noticed several steps too late.
- Reaching for maximum quality by reflex: the owner's own leaderboard entry used the lower setting. Spend the setting on small print and identity, not on everything.

</rules>

## Sources

Trust order is official over provider over community; official wins on any conflict.

- Official (xAI): [Imagine Image 2.0 announcement](https://x.ai/news/grok-imagine-image-2), [Imagine overview](https://docs.x.ai/developers/model-capabilities/imagine), [image generation](https://docs.x.ai/developers/model-capabilities/images/generation), [image editing](https://docs.x.ai/developers/model-capabilities/images/editing), [multi-image editing](https://docs.x.ai/developers/model-capabilities/images/multi-image-editing), [REST images reference](https://docs.x.ai/developers/rest-api-reference/inference/images), [image generation tool](https://docs.x.ai/developers/tools/image-generation).
- Provider: [FAL grok-imagine-image](https://fal.ai/models/xai/grok-imagine-image/api), [WaveSpeed grok-imagine-image edit](https://wavespeed.ai/models/x-ai/grok-imagine-image/edit).

Coverage notes. The rewriting-LLM behavior is documented only in the token-accounting fields of the REST reference, not in prose anywhere; the rendered reference page hides those fields behind a control, so the markdown variant is the citable form. The reference-token notation comes from the same field list. Language support is not published: every prompt and every in-image text example the owner ships is English, so `languages` records `en` alone and non-Latin in-image text should be treated as untested rather than unsupported. The owner's blog and its API docs disagree on how many reference images an edit accepts; that number is provider surface and is deliberately absent here. The edit-phrasing note is attributed to WaveSpeed because it contradicts the owner's own examples.

Last verified: 2026-08-15.
