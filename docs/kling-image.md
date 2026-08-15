---
guide: "Kling Image"
prompt_scheme: "kling-image"
models:
  - { id: "kling-v3", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, style-transfer, multi-image-reference, marked-input-editing, text-rendering, subject-control, outpainting], best_for: "the mainline image flagship. Strongest feature retention, free multi-reference, the full edit handbook and the marked-input channel. The default choice" }
  - { id: "kling-v3-omni", access: "closed-weights", tier: "flagship", caps: [text-to-image, image-edit, style-transfer, multi-image-reference, series-generation, marked-input-editing, text-rendering, subject-control, outpainting], best_for: "the only model that generates a SERIES of related images in one pass, plus the strongest cinematic-narrative single images. Reach for it for storyboards, ad sets and pre-visualization" }
  - { id: "kling-image-o1", access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, style-transfer, multi-image-reference, marked-input-editing, text-rendering, subject-control, outpainting], best_for: "calls itself Omni Image 1.0 in its own docs. Same prompt grammar as kling-v3 (their guides are the same document re-skinned); prefer kling-v3" }
  - { id: "kling-v2-1", access: "closed-weights", tier: "legacy", caps: [text-to-image, image-edit, multi-image-reference, subject-control, text-rendering], best_for: "prompt adherence and reliable output. Carries dedicated character and face feature reference, which the 3.0 series folds into subject control" }
  - { id: "kling-v2-new", access: "closed-weights", tier: "legacy", caps: [image-edit, style-transfer], best_for: "the style model. Image-to-image with a large built-in style bank and style training; it does not do plain text-to-image" }
capabilities: [text-to-image, image-edit, style-transfer, multi-image-reference, series-generation, marked-input-editing, text-rendering, subject-control, outpainting]
prompt:
  languages: ["en", "zh"]
  formula: "the owner publishes several and reconciles none. The general one is 5W1H: Who (subject), What (subject description), When (time), Where (environment), Why (what it is doing), How (composition, perspective, style, tone, lighting, texture). The owner's own caveat is that it is reference only, you need not fill every slot, and stacking elements blindly HURTS output quality"
  register: "chosen by TASK, not by input presence, and this is where the image line differs from the video line. An atomic EDIT is imperative ('Make the cat smaller.'). A whole-image RE-RENDER is descriptive ('The flowerpot in the foreground blooms.'). Both take inputs. The owner mixes both registers inside one prompt"
  length_strategy: "no owner guidance on any surface. Measured across the owner's examples, length tracks the NUMBER OF INDEPENDENT CONSTRAINTS rather than any stated preference: atomic edits run a handful of words, single-subject re-renders 25 to 60, multi-image or full commercial scenes 90 to 160"
  literal_text: "NAME THE SURFACE that carries the text, then the exact words in double quotes. Quoting alone does NOT mark text as literal: the owner also quotes pose nicknames and style tags, so the surface noun is what disambiguates"
  auto_expand_behavior: "none documented. Kling does not claim to rewrite or expand a terse prompt"
  negatives: "no negative-prompt field or technique is documented. Exclusion is done INLINE and positively: a terse 'No X.' clause, or an imperative 'Remove X from the image'. The strongest owner form pairs the negation with its replacement in one clause"
  structured_json: "none. Kling Image is natural language only"
  references: "TWO systems, split by whether the input has a name. A raw uploaded image gets a plain English ordinal in prose ('the shirt from Image 3'); indices bind explicitly, are NOT positional, and need not be contiguous. A SAVED ELEMENT gets a bracketed name token ('[@Korean Girl]'). They compose in one sentence"
  marked_inputs: "arrows, selections and doodles drawn ON the input image are referred to in the prompt in plain English ('the arrow', 'the selected areas', 'the doodle'). This channel has no video-line equivalent"
sources:
  official: ["https://kling.ai/document-api/guides/capability-map/image", "https://kling.ai/document-api/api/image/3-0-omni", "https://kling.ai/document-api/api/image/o1", "https://kling.ai/document-api/api/image/common", "https://kling.ai/quickstart/ai-image-prompt-formula", "https://kling.ai/quickstart/how-to-generate-text-in-images", "https://kling.ai/quickstart/klingai-element-library-3-user-guide", "https://kling.ai/quickstart/klingai-image-3-model-user-guide", "https://kling.ai/quickstart/klingai-image-3-omni-user-guide", "https://kling.ai/quickstart/klingai-image-o1-user-guide"]
last_verified: "2026-07-16"
---

# Kling Image: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- This guide is IMAGE only. Kling's video line is a separate scheme with a separate guide, and the two REUSE MODEL IDS: `kling-v3` and `kling-v3-omni` each name both an image model and a video model, told apart only by which endpoint you call. A bare model id is ambiguous.
- Write natural language. There is no JSON prompt form. Raw uploaded images are pointed at with plain ordinals in prose; saved elements are pointed at by name in a bracketed token.
- REGISTER FOLLOWS THE TASK, not the input. An atomic edit is an imperative; a whole-image re-render is a description; both take input images and the owner freely mixes them in one prompt. Do not import the video line's rule that an input flips the prompt into instruction mode.
- Kling Image and Kling Video are prompted DIFFERENTLY at every layer that matters: different formula, different referent grammar, no shot syntax, and an extra marked-input channel. Do not transplant rules between them.

</rules>

## TL;DR

<template id="quickstart">

{subject with appearance, clothing and posture} {what it is doing} in {environment} at {time or season}, {composition and perspective}, {art style}, {colour tone}, {lighting}, {texture}.

</template>

## Models and when to use which

The prompt grammar is shared, so a prompt written once transfers. Pick on capability.

- `kling-v3` is the default and carries the full edit handbook. `kling-image-o1` shares its grammar exactly: the two user guides are the same document re-skinned, down to identical prompt templates and an identical typo, so anything here for one holds for the other. Prefer `kling-v3`.
- `kling-v3-omni` is the one to reach for when you want a SET of related images rather than one. It is the only model that generates a coherent series in a single pass, and its single-image work leans hardest into cinematic narrative.
- `kling-v2-1` carries dedicated character and face feature reference. `kling-v2-new` is the style model: image-to-image with a large built-in style bank and style training, and no plain text-to-image.
- Older image ids (`kling-v1`, `kling-v1-5`, `kling-v2`) remain callable but are not part of the current line. Note there is no image `kling-v1-6`; the video line has one and the image line does not, so the two lines' version numbers do not correspond.
- The owner's published image capability table is internally contradictory (it denies Image 3.0 the multi-reference feature that its own description in the same table advertises). Do not plan around it; test the capability.

## How the model reads prompts

- Nothing is auto-expanded. Detail is your only lever, and the owner's framing is that the model is like a student given homework: "The more specific the prompt description, the more accurate and stable the generated image will be."
- But specificity is not stacking. The owner's own caveat on its formula: "it is not necessary to include all the elements every time you write a prompt... avoid blindly stacking elements, which may affect the quality of the output image."
- The model is pitched as reading natural language AND images together as one interface, under a concept the owner calls Multi-modal Visual Language. In practice that means a reference image is read as part of the prompt, not as a separate channel, which is why references are pointed at in ordinary prose.
- It reasons about scenes rather than just rendering them. The owner demonstrates prompts that require inference: deriving an overhead view from a straight-on photo, predicting how a person will look in ten years, generating a landmark from a marked map.
- Aspect ratio is read from the prompt text. The owner writes it bare, as "3:4." or "3:2 ratio."

## Prompt structure

The owner's general formula is 5W1H. Treat the slots as a checklist and the ordering as loose; the examples reorder freely and the owner explicitly calls the formula reference-only.

<rules id="structure">

- WHO: the main subject. A person, animal, plant, food, building or object.
- WHAT: the subject described. Appearance, posture, clothing, distinguishing features.
- WHEN: the time. A time of day, a season, or a historical period. Nothing in the video line has this slot.
- WHERE: the environment the subject sits in.
- WHY: what the subject is doing, and the emotion behind it. Actions, interactions, expressions.
- HOW: the picture as a picture. Composition, perspective, art style, colour tone, lighting, texture, and the small details.
- Fill the slots that serve the image and drop the rest. Stacking every slot every time is a stated cause of worse output, not better.
- Replace abstract nouns with the visible thing. "Magic" gives the model nothing; "swirling blue energy particles with an ethereal glow" gives it a target.

</rules>

<template id="general">

{art style}. {subject: age, appearance, clothing, props} {posture and expression}, {what it is doing}. {environment}, {time or season}. {lighting: direction, quality, colour}. {composition and shot size}, {perspective}. {colour palette}. {texture and film character}. {mood}.

</template>

<example use_case="t2i-5w1h-compact">

```text
An old painter wearing a beret stands in front of an easel and paints intently in the garden at dusk, with an impressionist style, soft lighting, close-up
```

*Why: the owner's own 5W1H demonstration, and the whole formula in one line. Who and What (an old painter, beret), Why (paints intently), Where (the garden), When (at dusk), How (impressionist, soft lighting, close-up). Nothing is stacked and nothing is padded*

</example>

<example use_case="t2i-flagship-cinematic">

```text
The image features two men and a red convertible, styled in a western crime film manner. The man on the left wears a black jacket and pants, with a relaxed posture; the man on the right is in a dark gray hoodie and jeans, with a tense stance. The red Ford convertible has a vintage look, fitting the desert standoff vibe. The two men face each other on opposite sides of the car, with the left man raising his hands in a deceptive gesture, and the right man with hands in his pockets, slightly turned in vigilance. The setting is a desert with red-brown rock hills, sparse vegetation, and a pale blue sky. The lighting is strong midday sunlight, creating sharp contrasts and shadows, emphasizing texture and a sense of tension. The composition centers the car, with the men on either side, framed by desert hills in the background. The color scheme contrasts vibrant red with subdued desert tones. The shot is at eye level, with a medium depth of field, while the distant hills blur naturally. The film quality has a cinematic grain, evoking tension, testing, and isolation.
```

*Why: the owner's own flagship, and the house pattern for long-form work. It walks a fixed order (subject and wardrobe, then posture, then setting, then lighting, then composition, then palette, then shot size and angle, then depth of field, then grain, then mood) and spends every word on staging rather than on quality boosters*

</example>

## Composition and camera vocabulary

The owner ships these as enumerated vocabularies, and all of them land as written.

- Framing: centered, rule of thirds, golden ratio, triadic, foreground, negative space, diagonal, symmetrical, leading lines, frame-in-frame.
- Shot size: establishing shot, long shot, full shot, medium long shot, medium shot, medium close-up, close-up, extreme close-up.
- Angle and height: top-down, high-angle, low-angle, eye-level, worm's eye, bird's-eye, fisheye, over-the-shoulder, frontal, three-quarter view, profile, rear view.
- Focal length: ultra-wide, wide, standard, telephoto. The owner also accepts it stated bluntly, as "Set to 35mm".
- Aperture and tone: wide or narrow aperture; low-key, mid-key, high-key.
- Lighting: top, back, soft, hard, side, front, backlight, stage, colourful, cool-toned.
- Colour tone: cool, warm, bright, dark, low contrast, high contrast, high saturation, black and white.

## Text rendering

Thin but real. The owner's two surfaces use different shapes, and what they share is the important part.

<rules id="text">

- NAME THE SURFACE that carries the text, then give the exact words in double quotes. The surface is what makes the words land: a sign, a nameplate, a wall projection, a magazine cover layout, a balloon.
- Two attested shapes. Woven into the sentence: `a sign that says "I want to eat fish"`, or `with "Kuaishou" written on it`. Or as a labelled slot: `Wall projection: "2026" & "Love the world with you."`
- QUOTING ALONE DOES NOT MARK LITERAL TEXT. The owner also puts pose nicknames, style tags and theme lines in the same double quotes. The surface noun is the disambiguator, so never rely on the quotes by themselves.
- Keep each string short. Long strings are where lettering degrades.
- Chinese and English both render, and the owner claims they render together in one image.
- Typography, size, weight and colour are not documented, and neither is spatial placement beyond naming the surface. Ask for them and you are past what the owner supports.
- To suppress text, say so: `No text.`

</rules>

<example use_case="literal-text-on-a-surface">

```text
A little white cat is holding up a sign that says "I want to eat fish"
```

*Why: the owner's own text-rendering demonstration. The surface is named first and carries the words, so the model has somewhere to put them; the exact string is quoted and short*

</example>

## Image editing

<rules id="edit">

- PIN FIRST, THEN CHANGE. The owner's canonical formula opens with the preservation clause: "Keep everything else unchanged, modify [ ] to [ ]." This is the most repeated device in the whole corpus and effectively every editing example carries one.
- THE WIDTH OF THE KEEP CLAUSE DECIDES WHAT YOU MUST DESCRIBE. This is NAME WHAT MOVES, PIN WHAT STAYS, encoded in the owner's own formula. Widen it ("Keep the female figure in Image 1 along with her clothing and hairstyle") and the prompt stops describing those things. Narrow it ("Keep the person's facial features") and the prompt must describe everything else in full.
- Two shapes for the clause, both attested: the catch-all ("Keep everything else unchanged", "leaving everything else untouched") and the enumerated ("keeping all facial features, poses, and lighting the same"). Prefer the catch-all unless you need to pin something specific.
- Scope the target by naming it, not by locating it. A definite noun phrase does the work, sharpened where needed by an attribute ("the blue cup"), a depth cue ("the flowerpot in the foreground") or a possessor ("the cup in a girl's hand").
- NAME THE END STATE, NOT THE OPERATION. This is the owner's only stated failure. "Switch the boy's head and feet direction" is called out as unclear and prone to wrong output; "Rotate the boy in the image so that his head is facing downward" is the fix. A relational operation leaves the result ambiguous; an absolute end state does not.
- Chain several edits with semicolons and give the whole chain one trailing keep clause.
- Precise values are accepted where you have them: a hex colour lands.
- An edit is imperative. A re-render is descriptive. Both are correct, both take inputs, and the owner mixes them inside one prompt.

</rules>

<example use_case="edit-with-preservation">

```text
Change the wall color to #F5D76E while keeping the character unchanged.
```

*Why: the owner's own. A precise value for the one thing that moves, and a catch-all pin for everything that does not. The clause costs four words and removes every question about drift*

</example>

<example use_case="edit-compound-chain">

```text
Change the background to the inside of a spaceship, with the table turning into a control desk. The kitten is wearing a spacesuit, and remove the flowerpot and books, leaving only the cup and small biscuit bowl.
```

*Why: four edits in one prompt (background, material, wardrobe, removal) closed by a residual pin. "leaving only the cup and small biscuit bowl" is the keep clause inverted: instead of naming what stays put, it names what survives a deletion*

</example>

### Marked inputs: arrows, selections and doodles

Kling lets you draw on the input image and then point at your own marks in the prompt. This channel has no equivalent on the video line and it is the cleanest way to say WHERE.

<rules id="marked">

- Refer to your marks in plain English: "the arrow", "the selected objects", "the selected area", "the doodle". There is no token.
- An arrow carries more than a location. The owner uses one arrow to supply a camera position ("Shoot according to arrow perspective") and another to supply BOTH the hue and the angle of a light ("Light according to the arrow's color and direction").
- A selection scopes an otherwise-ambiguous edit: "Change clothing in selected area to red".
- A doodle carries shape and placement: a stick figure sets a pose, a rough sketch sets a background layout, a blob sets where a hat goes.
- MARKS AND REFERENCES COMPOSE. A reference image says WHAT, a mark says WHERE, in one sentence.

</rules>

<example use_case="marked-input-composed-with-reference">

```text
Add flowers from Image 2 to all selected areas
```

*Why: the owner's own, and the two pointing systems welded in one line. Image 2 supplies what the flowers look like, the drawn selection supplies where they go, and neither has to describe the other*

</example>

## Style transfer

Two mechanisms, and they are not interchangeable.

<rules id="style">

- BORROW a style from a reference image when you have one: "Change the style of Image 1 to that of Image 2." Name no style adjective at all; the reference carries it. The owner states the model reads brush strokes, colour combinations and composition logic off the reference.
- NAME a style when you do not: "Convert the image to [Ghibli] style." The owner ships a large style bank as first-class vocabulary, including Pixar, Ghibli, JOJO, The Simpsons, Rick and Morty, Family Guy, Detective Conan, My Little Pony, Barbie, Powerpuff Girls, Disney 2D animation, chibi anime 3D, 2D chibi, plush toy, cotton doll, building blocks, crayon drawing, colored pencil illustration, watercolour illustration, children's picture book, vintage comic, American comic, vintage propaganda poster, calendar poster, sketch, pixel art, perler bead, ultra-flat, horror, steampunk, mecha, post-apocalyptic sci-fi, soulslike game, hero concept art, 3D clay Polaroid, snow globe, acrylic keychain, lacquer painting, gongbi painting, and Wu Guanzhong style.
- Materials are a parallel bank and work the same way: embroidery, yarn, gummy, paper-cut, plush, ultra-light clay, linen, glass, denim, wood, cotton, building block, bamboo weaving, oil painting, pearl shell, lace, silk, balloon, ceramic, plaster, down jacket.
- When you borrow a style AND change something else, name the borrowed axis CONCRETELY rather than saying "style". The owner's own combined example asks to replicate "the texture and tone" of a specific image.
- Pin what must survive the restyle. A restyle with no keep clause takes the subject with it.

</rules>

<example use_case="style-transfer-pure">

```text
Change the style of Image 1 to that of Image 2
```

*Why: the owner's own, and it is the whole prompt. No style adjective, no scene description, nothing but the two roles: Image 1 is the content, Image 2 is the style. ONE ROLE PER INPUT with nothing else in the way*

</example>

<example use_case="style-transfer-plus-edit">

```text
Create a fantasy movie still based on the goddess's look in the reference image, replicating the texture and tone of image 2. In a magical jungle, the goddess reaches for a ripe red peach, her expression focused and curious. The shot is a bird's-eye view with a dense peach orchard, framed by branches and leaves. Soft, diffused light creates dappled shadows, with the focus on the peach and her hand, and a blurred background for a cinematic, grainy feel.
```

*Why: the owner's own, and the harder case. Identity comes from one reference, style from another, and everything else (scene, pose, camera, lighting) is new. Each borrowed thing is welded to its source, and the borrowed style is named as "texture and tone" rather than left as a vague "style"*

</example>

## Multi-image and references

ONE ROLE PER INPUT. On the image line this is done in plain prose, and the welding device is a prepositional phrase attached to every borrowed element.

<rules id="reference">

- TWO POINTING SYSTEMS, AND WHICH ONE YOU USE DEPENDS ON WHETHER THE INPUT HAS A NAME. A raw uploaded image has no name, so point at it with a plain ordinal in prose: "the shirt from Image 3", "the background being image 4". A saved element HAS a name, so point at it by that name in a bracketed token: `[@Butterfly Perfume]`, `[@Korean Girl]`. Both appear in image prompts and they compose in one sentence.
- The bracketed form also wraps plain images on the owner's web surface (`[@Image]`, `[@image 1]`), so a token is not proof you are looking at an element. What makes it an element is that the name resolves to a saved asset.
- WELD EVERY BORROWED ELEMENT TO ITS SOURCE, one phrase per element. An element with no source phrase is unowned and the model will guess.
- INDICES ARE EXPLICIT, NOT POSITIONAL. The owner's examples list sources out of order and skip indices entirely, which only works because each element names its own index. Never let sentence order imply a mapping.
- Declare a base when one image is the foundation: "Use Image 1 as the base." Then dress it from the others.
- RE-ANCHOR A SOURCE when you need it twice. The owner names image 1 once as the environment and again as the surface a character sits on.
- Assert identity when it must be exact: "The smartphone must be identical to Image 2's."
- Close a composite with the global render intent: the photographic style, the lighting, the quality bar.
- Case and phrasing drift in the owner's own material ("Image 1" and "image 1"; "Dress the model from Image 2" and "have the person in image 1 wear"). Nothing suggests it matters. Pick one and hold it.

</rules>

<example use_case="multi-source-three-inputs">

```text
Take Image 3, replace the dog with the man from Image 1, and replace the cat with the lady from Image 2.
```

*Why: the owner's own, and the cleanest possible ONE ROLE PER INPUT. Image 3 donates the scene and composition, Image 1 and Image 2 each donate one person, and every swap names both what it replaces and where the replacement comes from*

</example>

<example use_case="multi-source-wardrobe">

```text
With the car from image 1 as the environmental subject, the character from image 2 is wearing the top from image 4 and the pants from image 5, with shoes from image 7 and a hat from image 8, and glasses from image 9. The character is sitting on the hood of the car from image 1, while the dog from image 3 stands at the character's feet. Generate a fashion photography shot with high-end, fashionable lighting, ensuring the image is clear and realistic.
```

*Why: the owner's own, and eight sources welded without a single ambiguity. Every borrowed item carries its own "from image N", image 1 is re-anchored for a spatial relation, image 6 is skipped entirely because indices are explicit rather than positional, and the closing sentence supplies the render intent for the whole composite*

</example>

## Series and storyboards

`kling-v3-omni` only. It generates a set of related images from one prompt.

<rules id="series">

- DO NOT USE THE VIDEO LINE'S SHOT SYNTAX. There is no `shot n, m, words;` here. On the image line "Shot 1" labels an output, not an input.
- Close the prompt with a bare noun phrase declaring the artifact: "Storyboard sequence.", "TVC storyboard.", "5-panel storyboard.", "Ad series." This terminator is the most consistent convention in the owner's series material.
- Bind each reference to a role at the head of the prompt with a parenthetical: "Huang (Ref 1) vs Chen (Ref 2), Setting (Ref 3)."
- Pin what must hold across the set with a bare constraint clause: "Consistent car/cast.", "Consistent bottle shape."
- Length is optional and can be stated several ways: spell it in words ("generate six storyboard frames"), hyphenate it ("5-panel storyboard"), enumerate the beats, or omit it and let the model choose.
- To enumerate beats, the owner's one attested form is a compact per-beat list: "S1: Driving. S2: Man driving POV. S3: Woman at villa checking watch." Fragments, no durations, no camera grammar inside the beat.
- The whole brief can be a theme line rather than a subject: a quoted line of copy plus a panel count is a complete series prompt.
- Prepare the references for their roles: an environment reference should be an empty scene, a character reference a plain background, a pose reference just the action lines.

</rules>

<example use_case="series-with-role-bound-refs">

```text
Huang (Ref 1) vs Chen (Ref 2), Setting (Ref 3). Escort vs Bandits: Rival leaders clash, brutal melee, Escorts win. Storyboard sequence.
```

*Why: the owner's canonical series prompt. Three references bound to named roles at the head, then a telegraphic plot line, then the terminator that declares what artifact to make. The model is left to break the plot into panels*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative-prompt technique documented, and no negative field is discussed on any surface. Exclusion happens inside the positive prompt.
- Two attested forms: a terse "No X." clause ("No text.", "No clutter.", "No grain.", "no posing"), or an imperative removal ("Remove the flowerpot and books", "Delete the selected objects").
- THE STRONGEST FORM PAIRS THE NEGATION WITH ITS REPLACEMENT. The owner's own: "No harsh contrast, only smooth tonal transitions." and "No heavy shadows, only gentle, diffused light." Saying what should be there instead gives the model somewhere to go.
- When removing from an existing image, name the residue: "remove the flowerpot and books, leaving only the cup and small biscuit bowl."

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Naming an operation instead of an end state: "Switch the boy's head and feet direction" is the owner's own failure case. Say "Rotate the boy in the image so that his head is facing downward."
- An edit with no keep clause: pin what stays, or accept drift. The preservation clause is the first thing in the owner's formula, not the last.
- Stacking every formula slot: stated to HURT quality, not help it. Fill what serves the image.
- Abstract nouns: "magic" renders nothing. Describe what it looks like.
- Importing the video line's rules: no shot syntax, no input-flips-the-register rule, and no id-bound token. Different scheme, same vendor. The bracketed token that DOES exist here binds an element's NAME, not a caller-assigned id.
- Giving a raw uploaded image a name token, or a saved element an ordinal: the two pointing systems are not interchangeable. Names for elements, indices for uploads.
- Assuming index order from sentence order: indices bind explicitly. The owner's own examples skip and reorder them.
- Leaving a borrowed element unwelded in a multi-image prompt: every element needs its own source phrase or the model guesses.
- Relying on quotes to mark literal text: the owner quotes pose nicknames and style tags too. Name the surface.
- Asking for typography: font, weight, size and kerning are undocumented. Name the surface and keep the string short.
- Specifying a count you need honored: the models are stated to be insensitive to numbers. Describe the group.
- Quality-booster tails: the owner's own examples are littered with "8k", "64K", "High res" and "peak detail". This is residue, never endorsed in prose, and it buys nothing. Spend the words on the picture.
- A restyle with no pin: the style change takes the subject with it unless you keep something.

</rules>

## Sources

Trust order is official > provider > community; official wins on any conflict. Kling's own surfaces disagree with each other more than they disagree with anyone else, so where the API reference and a web-app guide differ, this guide follows the API reference, because prompts written from here are sent through providers and proxies that wrap the API rather than the web app. The adjudications are recorded in `sources/kling/kling-notation-resolution.md`.

- Official (Kuaishou / Kling AI): the [image capability map](https://kling.ai/document-api/guides/capability-map/image) and the [3.0 Omni](https://kling.ai/document-api/api/image/3-0-omni), [O1](https://kling.ai/document-api/api/image/o1) and [common](https://kling.ai/document-api/api/image/common) image API references; the [IMAGE 3.0](https://kling.ai/quickstart/klingai-image-3-model-user-guide), [IMAGE 3.0 Omni](https://kling.ai/quickstart/klingai-image-3-omni-user-guide) and [IMAGE O1](https://kling.ai/quickstart/klingai-image-o1-user-guide) user guides; and the unlinked prompt-teaching quickstarts for the [5W1H image formula](https://kling.ai/quickstart/ai-image-prompt-formula) and [text in images](https://kling.ai/quickstart/how-to-generate-text-in-images).

Last verified: 2026-07-16.

Coverage notes. Kling states NO prompt-length guidance and NO negative-prompt technique on any image surface; both are characterized here from the owner's own examples and labelled as such. Text rendering is the thinnest area of the corpus: it rests on one dedicated quickstart from a batch that predates the current models, plus two incidental captions in the 3.0 Omni guide, and the owner documents no typography or placement vocabulary at all. The IMAGE O1 and IMAGE 3.0 user guides are the same document re-skinned, character-identical through the entire prompt handbook, which is why they share a scheme here; the 3.0 Omni guide shares no prompt-handbook surface with either and contributes the series layer alone. The owner never states the Image O1 to Image 3.0 Omni lineage that the video line states for its own O1, so no lineage claim is made here. The published image capability table contradicts itself and is not relied on. The Element Library, outpainting, and style training are out of scope: the first two are product surfaces with no prompt-text grammar documented, and the third is a training flow rather than a prompt.
