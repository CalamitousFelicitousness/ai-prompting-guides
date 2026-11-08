# Pruna: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08 from the sibling scrapes in this folder. Pruna AI's docs are static
Sphinx/Furo pages at `docs.pruna.ai/en/stable/docs_pruna_endpoints/`; curl works. Tabbed example panels lose all
but the first tab under firecrawl, so the model pages were re-fetched as HTML and reduced to text with a small
html.parser script (the `html-*.txt` files hold every tab).

## 1. Routing: one Pruna brand, three schemes

Pruna's catalog mixes its own models with other vendors' models sold under Pruna names.

- P-Video-2-Pro and P-Video-2-Pro-Reference: "based on MiniMax H3" on their own pages and in the endpoint
  index. Routed to `minimax-h3.md` (a paragraph in its Models section, a Sources bullet, lorebook keys). Not
  covered by `pruna-video`.
- P-Video-2-Pro-Avatar: also "based on MiniMax H3", but a separate talking-video pipeline with three free-text
  fields and Gemini TTS for scripts. Prompted with plain sentences, never H3's structured form. Covered by
  `pruna-video`, with the H3 base stated.
- P-Image-Ideogram: "built in collaboration with Ideogram" and "uses the same Ideogram 4.0 structured-caption
  schema". Pruna does not say it is the open-weights checkpoint, and it adds five thinking levels the open
  release lacks. Routed to `ideogram-4.md` for prompt syntax, with Pruna's thinking-level advice attributed.
- P-Video, P-Video-2, P-Video-Edit, P-Video-Replace, P-Video-2-Pro-Replace, P-Video-Animate, P-Video-Avatar: no
  base model stated anywhere. Pruna is the owner of these names. New scheme `pruna-video`.
- P-Image, P-Image-Edit: Pruna's own image models, base not stated. No guide (user scoped this pass to video).
  Pruna's image prompting guide was illustrated with its compressed FLUX builds on Replicate and recommends
  quality boosters and long negative lists; treat it with care if an image guide is ever written.

## 2. One video guide, not several

P-Video and P-Video-2 share the formula (Subject, Action, Scene, then optional Camera, Lighting, Style, Audio)
and the knitted-prune example is reused almost verbatim. The task models (Edit, Replace, Animate, Avatar) share
Pruna's API, house vocabulary and plain-sentence style; each has its own field layout, taught in its own
section. Splitting them would give guides of a few rules each. Tiers: P-Video-2 flagship, P-Video budget (the
cost of it is recorded: weaker lip-sync, close-ups and identity hold, per Pruna's stated P-Video-2 gains), task
models std.

## 3. Owner-internal conflicts

- General video guide vs model pages: `video_generation/advanced` says "All example videos in this guide were
  generated using the Pruna-optimized WAN video models on Replicate", has a six-slot formula with no audio slot,
  and recommends quality boosters. Model pages govern; the general guide supplies vocabulary only.
- P-Video image requirement: the page says "P-Video requires an input image to work properly" while the
  comparison table lists "Text prompt (+ optional image / audio)" and the formula examples are text-only.
  Taught as optional.
- Upsampling defaults: off on P-Video ("full user control"), on for P-Video-2 and Edit ("leave true for
  production"), avatar pages say disable for strict control, the chaining notebook turns it off. Taught per
  model, with "turn it off when the prompt must run as written".
- Quote style: the formula bullets show curly single quotes inside the page's own quotes; every copyable prompt
  uses straight double quotes. Taught as double quotes.
- Reference labels differ by model: "shown in the reference image" (Edit), "reference image 1" (Replace),
  "image 1" / "the person in the image" (Pro-Replace). Each taught where it applies.
- Avatar picture field is `video_prompt` on P-Video-Avatar and `prompt` on Pro-Avatar; the guide says "picture
  prompt" and names both.
- Edit is "not a character-swap model" yet one API sample prompt says "Replace the person with the reference".
  Taught: use Replace for people.
- Pro-Avatar card prompts repeat with different trailing sentences (Louis XIV, Mona Lisa, Loft); they look
  caption-contaminated and were not used. The Integration and formula prompts were.

## 4. Provider divergence

WaveSpeed's P-Video-2 pages require a duration and say they do not support automatic duration, audio
conditioning or last-frame guidance. Pruna's "the model chooses length from the prompt" is therefore
host-dependent; the guide says "where the host leaves duration unset".

## 5. Examples

All examples are Pruna's own, with em dashes and the multiplication sign made ASCII. French avatar script keeps
its accents (spoken text). Not used: the WAN-era general-guide examples, the caption-contaminated Pro-Avatar
cards, and the two-men P-Video example with digits (the P-Video-2 version spells numbers out).

## 6. Kept out

Prices, generation speeds, durations and length caps, resolutions and fps, aspect enums, file formats and
sizes, reference-image counts, the voice roster and voice_language list, parameter names and defaults
(`save_audio`, `draft`, `ignore_audio`, `negative_prompt_strength`), rate limits, and workflow numbers.
