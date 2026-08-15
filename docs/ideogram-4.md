---
guide: "Ideogram 4 (image)"
prompt_scheme: "ideogram-4"
models:
  - { id: "ideogram-4", access: "open-weights", tier: "base", caps: [text-to-image, text-rendering, layout-control, color-control], best_for: "typography and graphic design (posters, logos, signage, packaging), precise layout, and in-image text; strong photoreal and illustration as well" }
capabilities: [text-to-image, text-rendering, layout-control, color-control]
prompt:
  format: "structured JSON caption (high_level_description, style_description, compositional_deconstruction); the model was trained exclusively on this schema, so it is the native interface; plain text is accepted but underperforms"
  languages: ["en", "multilingual"]
  literal_text: "put the exact words in a text element's `text` field and its styling in `desc`; one text element per block; use \\n for line breaks; multilingual"
  length_strategy: "exhaustive and relationship-dense; name and describe every object and every text block; the model was trained on captions that describe everything in the image"
  auto_expand_behavior: "magic prompt (an LLM) can expand a plain-text prompt into a full JSON caption; it is on by default in the reference pipeline and on some hosts; write the caption yourself for full control"
  negatives: "no negative field; describe the desired state and omit what you do not want; the caption is additive"
sources:
  official: ["https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md", "https://huggingface.co/ideogram-ai/ideogram-4-fp8", "https://ideogram.ai/blog/ideogram-4.0/", "https://github.com/ideogram-oss/ideogram4"]
  provider: ["https://fal.ai/models/ideogram/v4"]
  community: []
last_verified: "2026-06-05"
---

# Ideogram 4: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the open-weight Ideogram 4 release. The nf4 and fp8 builds are quantizations of the same model and take the same prompts; treat them as one scheme.
- Ideogram 4 was trained exclusively on structured JSON captions. The caption is the native interface: the model accepts any string, but a caption that follows the schema gives markedly better control over layout, text, style, and color. Plain text works but underperforms.
- This release is text-to-image. Editing, remix, and character features belong to the hosted Ideogram product and are out of scope, so this guide has no image-editing or reference-image section.
- Pin every relationship. The model was trained on captions that name and describe every object and text block, so the surest way to get everything rendered is to enumerate it.

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

## Models and when to use which

There is one open-weight model, Ideogram 4, shipped in nf4 and fp8 quantizations that prompt identically; pick a build for speed or memory, not for prompting. It is strongest at typography and graphic design (posters, logos, signage, packaging, multi-line and multi-font text) and at precise layout, and it is a capable photoreal and illustration model across styles. The hosted Ideogram product adds editing and character tools that are not part of this release.

## How the model reads prompts

- It reads structured JSON captions natively. Training and inference share one format: each training caption exhaustively describes everything in the image, so the model expects the same exhaustive, relationship-dense input.
- Three ways to prompt, in order of control: write the JSON caption yourself (best); write plain text and let magic prompt expand it into a caption (casual input, near-caption quality); or pass bare plain text (works, but underperforms and trips the safety filter more often).
- It rewards naming everything. Because it was trained on captions that name every object explicitly, the reliable way to get every requested object and word rendered is to mirror that pattern: one element per object or text block, each with its own description.
- It honors structure. Color comes from a hex palette, placement comes from bounding boxes, and in-image text comes from typed text elements, rather than from adjectives buried in a sentence.
- Aspect ratio and global intent go in `high_level_description` as plain words ("a square 1:1 poster", "16:9 framing").

## The JSON caption schema

<rules id="schema">

- Three top-level fields, in this order: `high_level_description` (a one or two sentence summary, optional but strongly recommended), `style_description` (optional), and `compositional_deconstruction` (required).
- `compositional_deconstruction` must contain `background` (a string, first) then `elements` (a list), both required.
- Key order is strict. The model was trained on a fixed key order; keep it. A caption verifier warns on unknown, missing, or out-of-order keys.
- Hex colors are uppercase `#RRGGBB` only (`#1B1B2F`, not `#1b1b2f` or `#fff`).
- Serialize compactly (no superfluous whitespace) and keep non-ASCII characters literal rather than as escape sequences.

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

- `style_description` controls aesthetics, lighting, medium, and color. It is optional; for photoreal work you can omit it and fold film stock, grain, and white balance into the prose instead.
- It must contain exactly one of `photo` (for photographs, paired with `medium: "photograph"`) or `art_style` (for illustration, painting, 3D render, vector, and the like). Use one, never both.
- When present, `aesthetics`, `lighting`, and `medium` are required; `color_palette` is optional and always comes last.
- Key order depends on the type. Photo: `aesthetics`, `lighting`, `photo`, `medium`, `color_palette`. Non-photo: `aesthetics`, `lighting`, `medium`, `art_style`, `color_palette`.
- `medium` is a short label: `photograph`, `illustration`, `3d_render`, `painting`, `graphic_design`, and so on. `lighting` can be `n/a` for flat illustration.

</rules>

## Composition and bounding-box layout

<rules id="layout">

- `compositional_deconstruction` carries the layout: a `background` string, then an `elements` list. Each element is an object (`type: "obj"`) or a text block (`type: "text"`).
- Element key order: `obj` is `type`, `bbox`, `desc`, `color_palette`; `text` is `type`, `bbox`, `text`, `desc`, `color_palette`. `bbox` and `color_palette` are optional but must keep these positions when present.
- A `bbox` is `[y_min, x_min, y_max, x_max]` in normalized 0 to 1000 coordinates with the origin at the top-left. Note the order is Y first, then X.
- Boxing is optional and selective. Box the elements whose placement matters and leave the rest unboxed; or skip boxes entirely and state position in prose ("in the upper third", "on the rule-of-thirds line", "lower-left foreground"). Both work.
- Give each object and text block its own element. One element per thing, each welded to its own description and, if used, its own box.

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

In-image text is Ideogram 4's headline strength: clean signage, logos, captions, watermarks, and dense multi-line, multi-font layouts, in many languages.

<rules id="text">

- Use a `text` element per text block. Put the exact words in `text` and the styling (font, weight, case, color, treatment, placement) in `desc`. The split between the literal string and its visual description is the mechanism behind reliable typography.
- Line breaks go inside the string as `\n` (for example `"text": "MANGO\nSAGO\nSOCIAL"`).
- For multiple fonts or styles, give each word or block its own `text` element with its own `desc`; the model renders each in its own lettering.
- Set type scale by description ("the largest type on the page", "smaller than the title but larger than the footer") or pin it exactly with a `bbox`.
- Styling vocabulary the model reads in `desc`: weight (bold, hairline), width (condensed), case (all caps), family (sans-serif, serif, blackletter, script, pixel, marker), tracking, color (named plus hex), treatment (distressed, drop shadow, gradient fill), orientation, and the surface the text sits on.
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

## Color palette control

<rules id="color">

- A `color_palette` array of uppercase `#RRGGBB` hex steers the image's dominant colors directly, rather than through adjectives. Put it last in `style_description` for the whole image, and optionally a smaller palette inside an element for that element alone.
- Include the colors you actually want present, background included; if you want a dark backdrop, put the dark hex in the palette.
- Include contrast pairs, both a highlight and a shadow color, for more controlled lighting.
- Swapping only the palette on an otherwise fixed caption re-tints the same scene, which is a clean way to explore brand variants.
- You can also name colors inline in a `desc` or `background` (named or hex); the structured palette and inline color both work and combine.

</rules>

## Plain text and magic prompt

<rules id="plaintext">

- Plain text is accepted. A bare sentence renders, but with less control and lower fidelity than a caption, because the model only ever trained on structured captions.
- Magic prompt bridges the gap: an LLM expands a plain-text prompt into a full caption before generation, so a casual prompt gets near-caption quality. It is on by default in the reference pipeline and on some hosts; writing the caption yourself is how you take full control.
- The safety filter blocks unsafe prompts (returning a blocked-image placeholder), and it false-positives more often on bare plain text than on captions, another reason to prefer the structured form.

</rules>

<example use_case="plain-text-casual">

```text
a ginger cat wearing a tiny wizard hat reading a spellbook
```

*Why: plain text works for a quick, single-subject idea; magic prompt expands it into a caption, but for layout, exact text, or color control, write the JSON yourself*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field in the caption. Describe the desired state instead of listing what to avoid.
- The caption is additive: only what you name tends to appear, so to exclude something, simply leave it out and describe the alternative ("a clear blue sky" rather than "no clouds").

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Bare plain text: it underperforms and trips the safety filter more; write a caption, or let magic prompt build one.
- Under-describing: name and describe every object and text block; a sparse caption leaves elements to chance.
- Field name: it is `color_palette` (American spelling). Some summary docs write `colour_palette`, but the schema and verifier expect `color_palette`.
- Key order: keep the schema's key order; out-of-order keys degrade quality and warn in the verifier.
- Hex shorthand or lowercase: palettes must be uppercase `#RRGGBB`, not `#fff` or `#1b1b2f`.
- bbox axis order: it is `[y_min, x_min, y_max, x_max]` with Y first; swapping to X-first misplaces everything.
- photo and art_style together: pick one; they are mutually exclusive inside `style_description`.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. The owner is Ideogram (ideogram.ai); where the summary model cards and the prompting reference disagree on a field name (`colour_palette` vs `color_palette`), this guide follows the prompting reference and its caption verifier.

- Official (Ideogram): [prompting guide (docs/prompting.md)](https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md), [HF model card](https://huggingface.co/ideogram-ai/ideogram-4-fp8), [Ideogram 4.0 blog](https://ideogram.ai/blog/ideogram-4.0/), [GitHub repo](https://github.com/ideogram-oss/ideogram4).
- Provider: [fal Ideogram V4](https://fal.ai/models/ideogram/v4).

Last verified: 2026-06-05.
