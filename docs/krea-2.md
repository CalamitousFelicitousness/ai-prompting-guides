---
guide: "Krea 2"
prompt_scheme: "krea-2"
models:
  # cloud only
  - { id: "krea-2-medium", access: "closed-weights", tier: "std", caps: [text-to-image, style-transfer, text-rendering], best_for: "the stable, consistent default; strongest on illustration, anime, painting, concept art, and expressive artistic styles, with repeatable results across seeds" }
  - { id: "krea-2-large", access: "closed-weights", tier: "flagship", caps: [text-to-image, style-transfer, text-rendering], best_for: "the rawer, more textured, more flexible model; photorealism and raw aesthetics (motion blur, film grain, low dynamic range) and the richest surface texture, looser and less predictable" }
  - { id: "krea-2-medium-turbo", access: "closed-weights", tier: "distilled", caps: [text-to-image, style-transfer, text-rendering], best_for: "a fast, distilled Medium for quick iteration; same prompt grammar, and it favors shorter, cleaner prompts" }
  # open weights. The released model carries NO size suffix: medium and large are cloud-only product
  # sizes, while the open checkpoints are distinguished by Raw versus Turbo instead. Raw is the base
  # model despite the name, and Turbo is its distilled derivative.
  - { id: "Krea-2-Raw", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "control and LoRA training: 52 steps at CFG 3.5, so guidance is live and seeds stay varied. The owner calls it a finetuning base and not recommended for inference, which is a steer toward Turbo rather than a defect; it is still the checkpoint to reach for when you need guidance response or off-distribution range" }
  - { id: "Krea-2-Turbo", access: "open-weights", tier: "distilled", caps: [text-to-image], best_for: "speed and polish: 8 steps at CFG 0.0. Distillation buys the step count and a clean look, and costs guidance response and seed diversity, so it is the default for finished-looking output and the wrong tool for wrestling a stubborn prompt. Target for LoRAs trained on Raw" }
capabilities: [text-to-image, style-transfer, text-rendering]
prompt:
  languages: ["en"]
  literal_text: "for in-image words (word marks), wrap the exact words in straight double quotes and bind them to a typographic treatment and print medium (for example hand-lettered sans-serif typography reading the quoted phrase); keep strings short, it is built for word marks, not paragraphs"
  length_strategy: "scale prose to ambition: terse one-liners work for a clean concept or named-style shot, and long multi-sentence paragraphs that enumerate subject, material, lighting, palette, background, and render technique work for complex scenes; both are first-class. Pair prompt detail with the creativity control, detailed prompt with a literal setting, short prompt with a loose one"
  negatives: "SPLIT BY CHECKPOINT. The cloud models expose no negative-prompt field, and Turbo is run at CFG 0.0 so classifier-free guidance is off and an exclusion has nothing to push against there either: on both, describe the desired state and phrase suppression as a positive instruction (for example 'no smoothing, no retouching' to force raw skin texture), and for tighter fidelity to exactly what you wrote lower the creativity control rather than reaching for a negative. Raw is run at CFG 3.5, so guidance is live and it is the only checkpoint where steering against something can work at all"
  auto_expand_behavior: "a built-in creativity control decides how far the model invents beyond your words; at its most literal it renders only what you wrote, at its loosest it fills in style, composition, camera, and palette; turn it down for art-directed prompts, up for short open-ended ones"
sources:
  official: ["https://docs.krea.ai/developers/krea-2/overview", "https://www.krea.ai/blog/krea-2-image-model", "https://www.krea.ai/blog/krea-2-turbo", "https://huggingface.co/krea/Krea-2-Raw", "https://huggingface.co/krea/Krea-2-Turbo"]
  provider: ["https://fal.ai/learn/tools/krea-2-prompting-guide", "https://fal.ai/models/krea/v2/large/text-to-image", "https://fal.ai/models/krea/v2/medium/text-to-image", "https://wavespeed.ai/models/wavespeed-ai/krea-v2-medium-turbo/text-to-image"]
  community: []
last_verified: "2026-08-09"
---

# Krea 2: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, resolution, and pricing, consult the host's docs; they differ and are out of scope here.
- It covers the Krea 2 family, Krea's first from-scratch foundation image model: Krea 2 Medium, Krea 2 Large, and the fast Krea 2 Medium Turbo. They share one prompt scheme, so a prompt written for one transfers to the others; they differ in aesthetic character and speed, not grammar.
- Write natural-language prompts: lead with the subject, then stack comma-separated render clauses (material, surface, lighting, palette, background, medium, camera). Full sentences and terse one-liners both work. No JSON and no tag-soup.
- It is aesthetic-first. Krea 2 is built to render a chosen LOOK, not just place a subject, so describe the RENDER (material, surface quality, lighting, medium, grain), not only the subject. Naming a medium, art movement, era, print process, or director lands.
- Style is a separable axis here: a creativity control sets how literally it follows you, and style references transfer a look from one or more images. Both are covered below.
- It is text-to-image. Reference images supply STYLE (style transfer and moodboards), not content edits, so there is no instruction-editing section; the references section covers image inputs.
- There is no negative-prompt field; describe the desired state and phrase exclusions positively.

</rules>

## TL;DR

<template id="quickstart">

{subject and key action}, {pose and framing}, {lighting}, {color palette}, {background or backdrop}, {material and surface qualities}, {named medium or art style}, {camera or lens}. For a specific look, add one or more style reference images and let them carry the style while the prompt carries the content.

</template>

## Models and when to use which

- `krea-2-medium`: the default. Heavy post-training makes it stable and consistent across seeds. Strongest on illustration, anime, painting, concept art, and expressive artistic styles. Reach for it for repeatable, art-directed work.
- `krea-2-large`: more than twice Medium's size with a softer post-training profile, so it is rawer, more textured, and more flexible. Strongest on photorealism and raw aesthetics (motion blur, film grain, low dynamic range) and the richest surface texture. Looser and less predictable; at its best it produces results Medium cannot match.
- `krea-2-medium-turbo`: a fast, distilled variant of Medium for quick iteration. Same prompt grammar, and it favors shorter, cleaner prompts.
- Pick by look, not syntax: the grammar is identical across all three. Route stable illustration and anime to Medium, raw photoreal and heavy texture to Large, and fast exploration to Turbo.

## How the model reads prompts

- Describe the render, not just the subject. "a photo of a frog" gives a generic result; name the material, surface, lighting, and framing instead: "frontal macro portrait, vibrant orange sticky toes gripping a dark leaf, pitch black background, sharp facial focus, dramatic lighting". The more specific the visual language, the more precise the output.
- Treat surface and material as the subject. Concrete surface words land hard: "matte, powdery", "unglazed ceramic", "hyper-reflective liquid metal", "glassy iridescent gloss", "heavy ink texture", "coarse film grain". When texture is the point, say so ("skin texture is the subject", "no smoothing, no retouching").
- Camera vocabulary sets composition, for photos and illustration alike: "low-angle", "wide angle", "close-up macro", "contrapposto pose", "shallow depth of field", "wide cinematic shot".
- Name the medium or style explicitly. Krea 2 honors named print processes, art movements, eras, and directors: "risograph poster", "ukiyo-e woodblock print", "pointillist painting", "flat 2d vector illustration", "vintage 1950s Technicolor", "in the style of Tim Walker", "in the style of Zhang Yimou".
- Give lighting, palette, and background their own clauses. Named flat backdrops are reliably honored ("pitch black background", "solid bright chroma green background", "seamless white backdrop"); name the palette outright ("minimalist two-tone palette of pure black and blood red").
- Scale prose to ambition. A one-liner is enough for a clean named-style shot; a long paragraph that enumerates every material, light, and surface is rewarded for a complex scene.
- It resists the polished AI look, but you must ask for the alternative. To get raw, state the rawness ("grain", "low dynamic range", "no retouching"); to get clean, state the cleanliness ("high-key studio lighting", "seamless white backdrop").

## Prompt structure

<rules id="structure">

- Lead with the subject and its action, then stack render clauses in roughly this order: pose and framing, lighting, palette, background, material and surface, named medium or style, camera.
- Put each rendering decision in its own comma-separated clause rather than burying it; the model reads "grainy risograph texture" or "shallow depth of field" as discrete instructions.
- Name one clear medium or style and commit. You can blend looks, but a single named medium reads most cleanly.
- Decide how literal you want the render and set the creativity control to match: a fully specified brief wants a literal setting, an open prompt wants a loose one.

</rules>

<template id="general">

{subject and action}, {pose and framing}, {lighting}, {color palette}, {background or backdrop}, {material and surface qualities}, {named medium or art style}, {camera or lens}, {grain and dynamic-range notes for raw looks}

</template>

<example use_case="render-language-flagship">

```text
A vase of oranges and two pomegranates rendered in a retro-futuristic Y2K cyber-aesthetic, characterized by hyper-reflective liquid metal and heavy airbrush textures. The central vase is constructed from elongated, razor-sharp tribal chrome tendrils and fluid, spiky cyber-sigilism shapes that interlock and sweep outward into sharp points. Nestled within the jagged metallic thorns are smooth, highly polished metallic orange spheres and two deep ruby-magenta pomegranate forms, all coated in a glassy, iridescent gloss. Blinding, multi-point white starburst lens flares erupt from the intense specular highlights. The vessel sits against a smooth gradient backdrop transitioning from deep cobalt blue at the top to a hazy neon cyan and magenta at the base. The rendering technique mimics early 2000s vintage 3D CGI artwork, saturated with a coarse, heavy film grain and a distinct digital noise texture overlaying the entire composition.
```

*Why: the full render-language formula at scale, every surface, reflection, light, palette, backdrop, and the named CGI era and film grain stated as discrete clauses, which is how Krea 2 hits a precise, textured look rather than a polished default*

</example>

## By use-case

<example use_case="photoreal-wildlife">

```text
resting cheetah in close-up profile facing right, golden fur with dense black spots, distinctive black tear marks, sharp focus on amber eye and textured fur, paws on flat reddish-brown stone, blurry spotted fur in lower right, shallow depth of field, soft dark green blurred background, warm natural daylight, wildlife photography
```

*Why: a clean photoreal brief, named subject features, the focus point, depth of field, light, and "wildlife photography" as the render; both variants handle this, and Large gives the rawest fur texture*

</example>

<example use_case="texture-as-subject">

```text
close-up macro photograph of a lower eyelid and cheek, extreme proximity revealing every pore and fine vellus hair on pale skin flushed with a soft mauve-pink bloom. Skin texture is the subject: matte, powdery in quality, like the surface of a peach or unglazed ceramic. The blush diffuses at its edges like watercolor into wet paper. No smoothing, no retouching, every micro-texture intact.
```

*Why: texture is the explicit subject; concrete surface similes ("matte, powdery, like unglazed ceramic") and "no smoothing, no retouching" push Krea 2 off its polished default into raw skin*

</example>

<example use_case="illustration-risograph">

```text
a low-angle, tightly cropped shot of a quirky, minimalist horse character straddling a simplified astronaut, depicted in a naive flat illustration style with a grainy risograph texture, using bold black outlines and a vibrant, awkward color palette of teal, orange, and yellow against the astronaut's white suit.
```

*Why: an illustration brief that names the style (naive flat illustration, grainy risograph), the linework (bold black outlines), and a deliberately "awkward" palette, the expressive direction Medium is built for*

</example>

<example use_case="named-style-one-liner">

```text
an ukiyo-e woodblock print of traffic including a cybertruck on the golden gate bridge.
```

*Why: a terse prompt leaning on a named medium; with the creativity control loose, Krea 2 fills in the rest of the woodblock look from a couple of words of style*

</example>

<example use_case="retro-technicolor">

```text
two dancers in a dramatic dip, woman in an emerald gown leaning against an art-deco lamppost supported by a man in a white tuxedo, artificial studio-set desert with painted dunes and purple cacti, theatrical painted sunset backdrop, vintage 1950s Technicolor film style, wide cinematic shot, highly saturated colors
```

*Why: a period-render brief; naming "vintage 1950s Technicolor film style" plus "wide cinematic shot" and "highly saturated colors" sets era, format, and palette at once*

</example>

## Creativity and expansion

<rules id="creativity">

- Krea 2 has a creativity control that decides how far it invents beyond your words. When a prompt is short or vague, it fills in style, composition, camera, and palette; this control sets how much liberty it takes.
- At its most literal, it renders only what you wrote. Use that for tightly art-directed prompts where every detail is already specified.
- At its loosest, it takes meaningful creative liberty with style and mood. Use that for short, open-ended prompts where you want the model to surprise you.
- Pair the control with the prompt: a detailed brief wants the literal end for fidelity; a sparse brief wants the loose end so the model supplies the missing aesthetics. A long, fully specified prompt at a loose setting will drift.
- The literal end is your "stay on brief" tool, and it stands in for the negative prompt the model does not have.

</rules>

## Style transfer, references, and moodboards

<rules id="reference">

- Content in the prompt, style in the reference. The text names what is in the scene and its composition; the reference images carry how it looks. The same subject prompt against two different references yields two different looks.
- One role per reference. Give each reference a job and set its influence: a high-strength reference governs the look, a low-strength one only tints it.
- Blend multiple references as a moodboard. Several references fuse into one combined aesthetic, so say what each contributes (one for palette, one for texture, one for composition) to keep the blend intentional.
- A moodboard sets overall direction. Passing many images steers palette, texture, mood, and composition at once, without writing a long style prompt.
- Some hosts also expose trained custom styles and generative sliders (intensity, complexity, movement) to steer a look without rewriting the prompt; treat those as host features layered on the same prompt grammar.

</rules>

<example use_case="multi-reference-style-blend">

```text
people running. extremely exaggerated wide camera angle, exaggerated shapes. risograph poster. graphic illustration. dynamic composition.
```

*Why: the prompt carries only content and composition (people running, an exaggerated angle), while several blended style references supply the risograph look, one role per reference, which is how Krea 2 separates what is in the image from how it looks*

</example>

## Text rendering

<rules id="text">

- Put the exact in-image words in straight double quotes and bind them to a typographic treatment and print medium ("hand-lettered sans-serif typography reading ...").
- Name the lettering style so the type matches the art (hand-lettered, sans-serif, the print process); the word mark then renders as part of the composition, not pasted on.
- Keep it short. Krea 2 is built for word marks and short phrases, not paragraphs; for long copy, leave space and set the type in an editor.

</rules>

<example use_case="word-mark-poster">

```text
bold graphic poster illustration, stylized horse with an elongated fluid body and wavy serpentine tail, primitive folk art style, heavy ink texture, hand-lettered sans-serif typography reading "run wild", off-white textured paper background, risograph or linocut print aesthetic, vintage graphic design, flat 2d shapes, matte finish, high contrast, organic wobbly edges, abstract composition
```

*Why: the word mark is quoted and welded to its typographic treatment (hand-lettered sans-serif) inside a fully described print-poster render, so the lettering is generated in the same ink-textured style as the art*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Krea 2 has no negative-prompt field. State the desired state instead of forbidding its opposite: "matte finish" rather than "not glossy", "seamless white backdrop" rather than "no clutter".
- Phrase suppression as a positive instruction. "No smoothing, no retouching" works because it tells the model to keep texture, not because it is a negative field.
- For fidelity to exactly what you wrote, lower the creativity control rather than reaching for a negative; that is the model's real "stay on brief" lever.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Vague subject, generic result: name the render (material, surface, lighting, framing), not just the noun.
- Style as a bare prompt word: for a specific look, use a named style or a style reference; an adjective like "beautiful" gets the polished default.
- Fighting the AI look without specifying the alternative: to get raw, ask for grain, low dynamic range, and "no retouching"; the model will not add rawness you did not request.
- Wrong variant: route stable illustration and anime to Medium, raw photoreal and heavy texture to Large, fast iteration to Turbo.
- High creativity on a fully specified prompt: it drifts; lower the control when the brief is already complete.
- Expecting content editing: references transfer STYLE, not content; Krea 2 is text-to-image, not an instruction editor.
- Long in-image text: only short word marks render cleanly; quote them and keep them short.
- Loose multi-reference blends: when stacking references, say what each contributes, or the blend muddies.

</rules>

## Sources

Trust order: official beats provider beats community, and official wins on any conflict. The owner (Krea) and the providers (FAL, WaveSpeed) agree on the prompt grammar; the providers add worked examples that the guide draws on.

- Official (Krea): [Krea 2 API overview](https://docs.krea.ai/developers/krea-2/overview), [Introducing Krea 2 blog](https://www.krea.ai/blog/krea-2-image-model).
- Provider: [FAL Krea 2 prompting guide](https://fal.ai/learn/tools/krea-2-prompting-guide), [FAL Krea 2 Large](https://fal.ai/models/krea/v2/large/text-to-image), [FAL Krea 2 Medium](https://fal.ai/models/krea/v2/medium/text-to-image), [WaveSpeed Krea 2 Medium Turbo](https://wavespeed.ai/models/wavespeed-ai/krea-v2-medium-turbo/text-to-image).

Last verified: 2026-08-09.
