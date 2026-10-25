# FIBO: structure decision and source notes

Not a scrape. Hand-authored 2026-10-25 from the owner surfaces in this folder.

- `hf/<repo>/README.md`: every briaai FIBO card, gated ones included (fetched with the authenticated `hf` CLI).
- `hf/Fibo-2.0-dev/vgl/README.md`: the owner's VGL caption guide. `hf/Fibo-2.0-dev/styles/`: the five style modes.
- `bria-vgl-0.10.0/`: the owner's caption writer from PyPI, dialect `thales` (Fibo 2.0): schemas and system prompts.
- `hf-code/`: the 1.x prompt-to-JSON helpers, which hold the 1.x system prompts and field descriptions.
- `docs/`, `github/`, `fal/`: docs.bria.ai `.md` pages and OpenAPI bundles, the FIBO / vgl / bria-skill repos, FAL llms.txt.

## 1. One scheme for 1.x and 2.0. RESOLVED: merge.

The 1.x Gemini helper's output schema and the thales output schema have the same top-level keys and the same
nested fields (compared key by key). 2.0 edits add `edit_instruction`; 1.x Gemini captions add
`aesthetics.preference_score` and `aesthetics.aesthetic_score`, which the 2.0 pipeline drops. The caption guide:
"FIBO and Fibo 1.5 used the same fields ... Their captions work with Fibo 2.0 as they are". The architectures
differ (1.x: SmolLM3-3B + Wan 2.2 VAE; 2.0: Qwen3-VL-4B + FLUX.2 VAE) but the prompt grammar does not, so per
the merge rule this is one guide with per-generation notes. `fibo-scene-analyzer` emits a different
SceneDescription format (boxes, colour tokens, keypoints) and is not a prompt surface for these models.
`Fibo-Edit-RMBG` is driven by a fixed instruction and is not covered.

## 2. Image naming in multi-image edits. RESOLVED: `<image_N>`.

- bria-vgl best practices, the caption guide, the Fibo 2.0 card and FAL fibo-2/edit: `<image_1>` to `<image_4>`
  in input order; FAL returns VGL with the tags kept. The 1.x Gemini edit helper requires every image referenced
  exactly once by `<image_N>`, in edit_instruction only.
- bria-skill (agent skill): plain "image 1", "No brackets, tags, or markup".
- Bria docs' own multi-reference example names no numbers and describes each source by content.

The tag is what the model is trained on and what the helpers emit; the skill's plain form is input to a helper
that rewrites it. Taught: `<image_N>`, with the plain form noted as tolerated by host helpers.

## 3. Object cap and text default. RESOLVED.

- 1.x helpers: at most 5 objects; `text_render` empty unless the user gives exact text.
- thales Generate: no object cap; lists text quoted or implied by the scene. Inspire, edits, Caption, Refine and
  `boring_reality` keep the restrictive text rule; edits keep the 5-object cap.
- Caption guide: "Keep `objects` to 5 at most" (under Edits); "Every text goes in `text_render`" ... "Don't add
  text the user didn't ask for, except text that is part of an object".

Taught: the caption guide's text rule and a five-object limit for hand-written captions, which is safe on every
generation.

## 4. Quality keywords. RESOLVED.

docs.bria.ai best practices: "ultra, 8K, masterpiece" ... "Usually no." bria-skill: "Quality keywords: high
quality, professional, commercial grade, 4K, sharp focus". Taught: the docs' answer; the skill is an agent
helper, the docs page is the prompt guidance.

## 5. VGL overview fields not in training. RESOLVED.

docs.bria.ai/vgl lists bounding boxes, RGB colour arrays, skin-tone scales and keypoints. The caption guide: "Fibo
2.0 was not trained on those. Use the format in this guide." Every example and schema in use carries plain
strings. Not taught.

## 6. Negatives. RESOLVED.

Fibo 2.0 hosts (Bria API, FAL fibo-2) expose no negative. Self-hosted Dev: a JSON caption (`NEGATIVE_T2I`) for
text-to-image, the empty caption for edits, a per-style negative for style modes (never the default with
kodak_film or hazy_dreamy). 1.x FIBO: a VGL fragment for photographs only, written as a single-quoted Python-dict
string in the owner's code. Distilled checkpoints: no effect (stated on Lite, 1.5, both Turbos). The pipeline
default when no negative is passed is the empty edit caption even for text-to-image, so self-hosted text-to-image
should pass the card's negative explicitly; recorded here, not taught, as it is pipeline behaviour.

## 7. Settings conflicts (spec table only)

- Fibo-2.0-dev: card 50 steps / CFG 5; the diffusers pipeline defaults to 30. Card used.
- Fibo-Edit: card guidance 5; the diffusers docstring says 3.5. Card used.
- Fibo-lite: "~10x Faster" and "(2x faster!)" on the same card; speed is not in the spec table.

## 8. Example provenance

- Travel mug, HAPPY NEW YEAR balloons, bottle-cap edit: docs.bria.ai best-practice pages, verbatim.
- Desert editorial: docs.bria.ai OpenAPI bundle example "Generate a new image using a textual prompt", verbatim.
- Bicycle caption: the caption guide, verbatim. Dev negative: the Fibo-2.0-dev card, verbatim.
- Fragrance poster: FAL fibo-2/edit llms.txt. Restage serum bottle: FAL fibo-2/edit page. Four-image try-on:
  FAL fibo-edit-1.5 page. "Turn the image into the cartoon style." and the masked ocean: bria-skill / caption
  guide rewrite tables.
- Watercolor plus mustard coat: built to the owner's rules; labelled as such in its Why line.
