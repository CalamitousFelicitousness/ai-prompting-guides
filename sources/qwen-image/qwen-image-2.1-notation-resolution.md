# Qwen-Image-2.1: structure decision and source notes

Not a scrape. Hand-authored 2026-09-21 from the owner surfaces released with the model on 2026-09-20:
the launch blog (`qwen-blog-image-2.1.md`), the `Qwen/Qwen-Image-2.1` card, the `QwenLM/Qwen-Image-2.1`
GitHub README, and the two prompt-rewriting repositories `Qwen-Image-2.1-PE-T2I` and
`Qwen-Image-2.1-PE-I2I`, each of which ships a `system_prompt.txt`. Cards and system prompts were read
through the authenticated HF tools and saved under `hf-qwen-image-2.1*/`.

## 1. Merge into `qwen-image`, no new scheme

Qwen-Image-2.1 joins `guides/qwen-image.md`. Same family, same quoted-text grammar, same
subject-setting-style ordering underneath. What 2.1 changes is the register and three specific rules,
which is the version-conditioned case the guide already handles for the 3.0 tier.

It is the first model in this guide that REVERSES family rules rather than extending them, so the global
rules block now says so outright and every affected section carries a 2.1 note.

## 2. The craft lives in the rewriters' system prompts, not the model card

The card is a quick start: install, three snippets, an aspect-ratio table, a showcase. The two PE
repositories carry the real guidance, 10 KB and 18 KB of it, written by the owner to steer an
owner-trained rewriter whose output feeds this model. That is stronger evidence than a sample prompt,
because a sample shows one output while the spec states the rule the outputs were drawn from.

The T2I file gives an eight-step procedure and a long "Throughout" section: the observer register, the
size target (about twenty sentences, 400 to 500 words, regardless of brief length), the opening-sentence
shape, the region walk order, eight to fourteen positional phrases with a third of sentences opening on
one, the text step with its skip condition, the lighting sentence, exactly one closing sentence, hedging,
colour modifiers, materials, enumeration, people described by observable surface with age as a life
stage, objects by class not brand, and physical coherence.

The I2I file gives the edit craft: the intent branch (clarify a change to THIS picture versus construct a
NEW picture of this subject), attribute disentanglement with leakage and under-editing as symmetric
failures, "preservation locks content, never edit strength", "say what stays without repainting it",
identity as the hardest invariant with the instruction to POINT at a reference image rather than describe
a face, affirmative phrasing, no hedging, literal text, and explicit outpainting.

LESSON, and this is the fourth time in a month after GPT Image 2.5, Anima and Wan 3.0: the prompting
guidance is not where the last pass looked. Here it was inside two sibling repositories, in a file that
is not the README. When a model ships with a rewriter, prompt enhancer or formatter, read that thing's
instructions: it is the owner telling you what the model wants.

## 3. Reversal one: the quality suffix is banned on 2.1

The guide carries a `quality_suffix` key because the pre-2.1 open reference pipeline appends
", Ultra HD, 4K, cinematic composition." to an English prompt. It was recorded as the one place in this
whole guide set where a 4K-style booster is owner-recommended rather than an anti-pattern.

The 2.1 T2I spec says: "No quality boosters - no 'masterpiece', '8K', 'highly detailed',
'award-winning'." The I2I spec adds that 2K, 4K and 8K are quality words that must never appear in the
prompt and must not be read as aspect-ratio hints.

Resolved by scoping rather than deletion: the key now reads THE PRE-2.1 OPEN CHECKPOINTS ONLY and states
the reversal. The older pipelines still append it, so the fact is not wrong, it is bounded.

## 4. Reversal two: the aspect ratio leaves the prompt

House scope treats aspect ratio as prompt content, because most models here read "16:9" in the text. Both
2.1 rewriters forbid it: "The ratio lives only in the `wh_ratio` field. Never write a ratio, a resolution,
or a pixel count into the description itself", and on the edit side "Never include any resolution or
aspect ratio information in `rewritten_prompt`".

Recorded as a model-scoped `aspect_ratio` key plus rules in both the observer and edit sections. Same
shape as the wan3-pe finding five days ago, and the second owner in a week to separate frame from
description; worth watching as a trend rather than treating as a quirk.

## 5. Notation: three forms in one guide, and one conflict left standing

- Dedicated editors (Edit, Edit-2509, Edit-2511): `Image 1`, `Image 2`.
- 2.1 with two or more inputs: `<image1>`, `<image2>`. The I2I spec calls this "mandatory and
  non-negotiable" and explicitly rules out "图1", "第一张图", "the first image" and "image A".
- 2.1 with one input: no tag at all, "refer to the image naturally".

CONFLICT: the GitHub README's multi-reference quick start passes three images with an untagged sentence,
"These three characters are sitting around a campfire in a forest". The rewriter spec says tags are
mandatory at N >= 2.

Resolved in favour of the spec, on the rule that an explicit instruction outranks a demonstration. The
untagged form is taught as the same-role case the quick start actually shows: three inputs, one role
each, nothing to tell apart. Both appear as examples so the difference is visible rather than asserted.

## 6. Two language decisions on an edit, and only one on generation

T2I: "The description is always in English, whatever language the request arrives in. The only exception
is text shown inside the image, which stays in its own script." That corroborates the lorebook's
always-on language rule, which already says the prompt is English while in-image text keeps its script.

I2I splits it in two, and opens by warning against conflating them. Decision (A), the prose outside the
quotes: Chinese in, Chinese out; English in, English out; any other language in, English out. Decision
(B), the text rendered into the image: the words or language the user names, else the dominant language
of text already in the image, else the language of the instruction. Plus: rendered strings stay
monolingual, and a "technical" or "spec sheet" genre never licenses switching labels to English.

Taught as its own `edit-language-2.1` rules block, because the worked example the owner gives (English
instruction, Thai sign, Thai stays in the quotes) is not something a reader would derive.

## 7. Licensing and naming

Qwen-Image-2.1 is under the Qwen Research License, not Apache 2.0, unlike every earlier open release in
this guide. `access` stays `open-weights`, which records only whether downloadable weights exist; the
frontmatter comment and the Models section carry the split, since it decides what a project may use.

The name also leaves the YYMM scheme (2509, 2511, 2512) for a version number. The comment says so, because
a reader who learned the suffix rule from this guide would otherwise expect a 2609-style name.

## 8. Tiering

2.1 is `flagship` on the open line: newest, and the only checkpoint doing generation and editing at once.
It is smaller than Qwen-Image (7B visual generation component against 20B), so "largest" and "best" part
company here; the vocabulary's "largest OR best in the family" covers it, and best is the useful reading.

2512 moves from "current open text-to-image foundation" to "the previous" one, and the Edit-2511 spec-row
note now says it is the last of the dedicated editors. Neither is retiered to `legacy`: the owner has not
withdrawn them, and 2512 remains the reference point for the Qwen 1328 resolution set.

## 9. Kept out of the guide

Ten reference images per request, the seven-entry resolution table, 40 steps, the 2K default, and the
architecture numbers are request and weight surface. The resolutions, steps, sampler and architecture went
into `guides/model-specs.md`; the reference cap is provider surface and is recorded nowhere.

Published CFG: none. The card and README give steps and sizes but no guidance value, and the scheduler is
named only as flow matching with Euler discrete and dynamic shifting. An SGLang example runs
`--guidance-scale 1`, but SGLang is not an approved provider here, so the cell reads `not published`
rather than carrying a third-party number.
