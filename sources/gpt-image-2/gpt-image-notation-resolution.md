# GPT Image: structure decision and source notes

Not a scrape. Hand-authored 2026-08-07 from the sibling scrapes in this folder. Short, because unlike the
Qwen, FLUX and Gemini passes this release produced no owner-versus-owner conflict.

## 1. One guide for the family

`guides/gpt-image.md`, scheme `gpt-image`, covering `gpt-image-2`, `gpt-image-1.5`, `gpt-image-1`, and
`gpt-image-1-mini`.

The owner settles it directly. Its own document is titled "GPT Image Generation Models Prompting Guide"
(plural), presents one set of prompting fundamentals for all four, and its migration advice is "keep
prompts largely the same at first, then retune only after you have compared output quality, latency, and
retry rates on your real workload". Prompts transfer; the differences are quality, latency, and which
knobs a model exposes. That is the repo's merge criterion.

Named at family level rather than after the flagship, matching `gemini-image.md` and the owner's own
plural title.

## 2. Naming is clean, with one trap

No nickname layer here, so no Gemini-style alias matrix is needed. The ids read as written and the
marketing names are just their title-case form ("GPT Image 2" for `gpt-image-2`).

The one thing worth stating in the guide: **`gpt-image-1-mini` is a mini of generation 1, not of
generation 2.** Read as a list, `gpt-image-2 / gpt-image-1.5 / gpt-image-1 / gpt-image-1-mini` invites the
assumption that mini is the small sibling of the newest model, and it is not. The owner's own advice
reinforces the correction: for cost-sensitive work it recommends the flagship at a lower quality setting
over reaching for mini, saying the low setting "works just as well".

## 3. Provider agrees with owner; fal formalizes rather than competes

fal's guide (last updated the day of launch) contributes a five-slot template, Scene / Subject / Important
details / Use case / Constraints, and six "anti-slop" rules. None of it contradicts the owner. It is a
tighter formalization of the owner's own fundamentals, which state the order as "background/scene ->
subject -> key details -> constraints" and separately say to "include the intended use (ad, UI mock,
infographic) to set the mode".

The guide teaches the five-slot template as the canonical structure because it is the version that makes
the owner's "use case" instruction a named slot instead of an aside, and because both surfaces agree on
every element of it. fal's rules 4, 5 and 6 restate owner fundamentals almost verbatim (change plus
preserve with the list repeated each iteration; quotes or caps plus letter-by-letter spelling for hard
words; one revision per turn), which is corroboration rather than a second opinion.

## 4. Tags are accepted here, which inverts most of the guide set

Worth flagging because it contradicts a rule that is nearly universal elsewhere in this repo. Most guides
say never write tag lists. The owner says the opposite for this family: "Minimal prompts, descriptive
paragraphs, JSON-like structures, instruction-style prompts, and tag-based prompts can all work well as
long as the intent and constraints are clear."

Resolved by teaching the nuance rather than either extreme. Tags parse, but a bare style-tag pile
underperforms, which fal demonstrates with a weak-versus-usable pair: `minimalist brutalist editorial
luxury photoreal cinematic modern premium` against a description naming cream background, heavy black
condensed sans serif, asymmetrical type block, one hero object, generous negative space, studio tabletop
lighting. The rule the guide carries is that every style word needs a visual target, and that a skimmable
labeled template beats clever syntax. The owner says this too: "For production systems, prioritize a
skimmable template over clever prompt syntax."

## 5. Scope: quality and fidelity settings dropped, the technique kept

The owner's parameter table (`outputQuality`, `input_fidelity`, `size`, and the resolution constraint
arithmetic) is out of scope in full. What is kept is the portable technique underneath it: raise the
host's quality setting for small or dense text, detailed infographics, close-up portraits, and
identity-sensitive edits; a low setting is often enough for high-volume work. That follows the standing
treatment of host-specific knobs, the same as Gemini's thinking level.

`input_fidelity` is additionally moot on the flagship, which the owner's own table marks as "Disabled ...
because output is already high fidelity by default".

## 6. Distinctive craft, recorded so it is not mistaken for invention

Three patterns in the owner's examples are unusual enough to note their provenance.

**"Photorealistic" is a mode switch, not a quality tag.** The owner states that including the word
"photorealistic" directly "strongly engages the model's photorealistic mode", and lists "real photograph",
"taken on a real camera", "professional photography", and "iPhone photo" as similar levers. In the same
breath it warns that detailed camera specs "may be interpreted loosely", so lens and body names shape the
look rather than simulating optics. That combination inverts the FLUX.2 habit of naming a film stock and
lens for physical accuracy.

**Anti-polish instructions are load-bearing.** The owner's photoreal examples end with suppression, not
description: "No glamorization, no heavy retouching", "Avoid cinematic lighting, dramatic color grading,
or stylized composition", "not an overly enhanced or cinematic movie-poster image". The model over-styles
toward advertising polish by default, so believability is bought by naming what to leave out.

**Date and place trigger world knowledge.** The owner's example generates "a realistic outdoor crowd scene
in Bethel, New York on August 16, 1969" and notes the model infers Woodstock without being told. Naming a
verifiable time and place is a documented way to hand the model the research.
