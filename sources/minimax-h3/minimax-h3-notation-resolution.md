# MiniMax H3: structured IR vs free-form prose, and the reference-label conflict

Not a scrape. Hand-authored adjudication of an apparent owner-vs-provider conflict, written 2026-08-06
from the sibling scrapes in this folder. The repo resolves owner-vs-provider on owner authority, but the
interesting result here is that the two surfaces are not actually in conflict once the pipeline is
understood, so the guide teaches both layers instead of discarding one.

## The apparent conflict

MiniMax's own prompt guides (`h3-prompt-guide-base-en.txt`, `h3-prompt-guide-ref-en.txt`, identical
byte-for-byte to the HuggingFace `docs/VIDEO_PROMPT_WRITING_GUIDE_*_en.md`) document a strict structured
format: named fields (`integrated_multimodal_description`, `overall_soundscape`, `non_diegetic_music`;
or the six-section Ref2VA layout), angle-bracket labels `<Picture N>` / `<Video N>` / `<Audio N>` /
`<Subject N>`, speaker IDs `(S1)`, dialogue wrapped in `<d>[Language] ...</d>`, `[Shot N]` markers, and
`At MM:SS.mmm,` cut times.

fal's prompting guide (`fal-minimax-h3-prompting-guide.md`, 44 example prompts) uses none of it. Every
example is free-form prose. Its labels are plain `Image 1`, `Video 1`, `Audio 1` (plus a single
inconsistent `@Image 1` in one of 44). Its timecodes are `[0-2 seconds]` ranges. Its dialogue is bare
quoted text. It never mentions the structured format, and never mentions H3-Context-IR.

## Resolution: these are two layers of one pipeline, not two competing specs

The owner README documents a three-module system. Free-form user input is consumed by **H3-Context-IR**,
which rewrites it into the **Context Intermediate Representation**, and that representation is what
**H3-Base** actually generates from. Verbatim from the README:

> H3-Context-IR: As inputs become increasingly complex, we build a dedicated system to deeply understand
> and refine the input multimodal instructions, then convert them into a form that H3 can readily
> understand - the Context Intermediate Representation - for generation. H3-Context-IR is critical to the
> quality of the final output, so we strongly recommend incorporating it into your generation pipeline or
> following the "Prompting Guidance" to build your own context-processing system.

Three independent pieces of evidence confirm the structured format is the model's literal input language,
not a documentation convention:

1. The README's own worked examples show the H3-Context-IR response body containing exactly
   `integrated_multimodal_description: [Shot 1] ...`, `overall_soundscape: ...`, `non_diegetic_music: ...`,
   and that string is then passed to H3-Base. The structured text is a pipeline artifact, not prose advice.
2. `<d>` is a registered special token. The README states: "We add several special tokens, such as `<d>`,
   to the tokenizer configuration. When using H3, the tokenizer and associated configuration files
   provided in the H3 repository are required." A tag in the tokenizer is parsed, not decorative.
3. The owner's Ref2VA worked example contains `<d>[English] Follow the wind, live free.</d>`, and fal's
   voice-clone example expresses the same line as bare prose: `The character says: "Follow the wind, live
   free. Leave worries behind, enjoy the moment." Match the voice in Audio 1.` Same content, two layers.

So: **fal's prose is valid input to a hosted endpoint that runs H3-Context-IR for you. The owner's
structured format is what H3-Base consumes.** Neither surface is wrong; they describe different points in
the same pipeline. fal is silent on Context-IR because from its callers' side the rewrite is invisible.

## What the guide does with this

- Teach both layers explicitly, labeled. Free-form prose is the default for hosted endpoints; the
  structured IR is what you write when you drive H3-Base directly, or when you want the rewrite to stop
  guessing.
- **Owner notation is canonical for the structured layer**: `<Picture N>`, `<Video N>`, `<Audio N>`,
  `<Subject N>`, `(S1)`, `<d>[Language] ...</d>`, `<scenetrans>`, `<cutoff>`, `[Shot N]`, `At MM:SS.mmm,`.
- fal's `Image 1` / `Video 1` / `Audio 1` are recorded as the free-form layer's ordinary convention, which
  is legitimate there because that text is going to be rewritten anyway. They are NOT taught as the
  structured layer's syntax.
- fal's single `@Image 1` example is discarded as a weak signal: it appears once in 44 examples and is
  inconsistent with fal's own other 43.
- fal's `[0-2 seconds]` range timecodes are recorded as a free-form convention only. The structured layer
  uses a single increasing cut time per shot, `At MM:SS.mmm,`, not ranges.

## Mode taxonomy divergence, also resolved on owner authority

The owner defines five modes across two checkpoints: T2VA, I2VA, FL2VA, L2VA on `H3-Base-FL2VA`, and
Ref2VA on `H3-Base-Ref2VA`. fal exposes three endpoint families and collapses I2VA and FL2VA into one
"First & Last Frame" surface, and offers no L2VA (last-frame-only) at all.

The guide follows the owner and documents all five modes, because L2VA has its own distinct prompt shape
(infer a plausible opening, converge on the supplied final frame) that the owner spells out and that is
simply unavailable through one provider's endpoint layout. Endpoint availability is a provider fact and
out of scope; the prompt shape is in scope.

## Two inconsistencies inside the owner's own base guide

Both are minor, both are recorded here so the guide's choices are not mistaken for transcription errors.

**1. The alignment-instruction template prints an em-dash.** The FL2VA and L2VA templates literally read
`How the reference pictures align with the target video - ...` with an em-dash before the clause. The repo
requires ASCII-clean guides, so the guide prints an ASCII hyphen. This is safe: the separator sits in a
prose instruction line consumed by a language model, and every load-bearing literal in the format (the
field names, `<d>`, `<Picture N>`, `[Shot N]`, `At MM:SS.mmm,`) is ASCII already.

**2. The FL2VA template drops the angle brackets the other two templates use.** Verbatim:

| Mode | Template form |
| --- | --- |
| I2VA | `... <Picture 1> (from [Shot 1]) is fully referenced.` |
| FL2VA | `... Picture 1 (from Shot 1) aligns with the 0.00-second mark ...` |
| L2VA | `... <Picture 1> (from [Shot N]) aligns with the S.SS-second mark ...` |

The FL2VA case example matches its own unbracketed template; the L2VA case example matches its bracketed
one. Since `ref-en.txt` defines `<Picture N>` as the canonical label form and two of three templates use
it, the guide teaches the bracketed form throughout and notes that the unbracketed spelling also appears
in owner examples and is accepted.

## Not a conflict, worth noting

fal's eight technique headings (assign a job to every reference; timed shot list; direct the audio; state
what you do not want; lock identity explicitly; name the change and the constraint together; use camera
and film language; describe transitions as events) do not contradict the owner spec at any point. They are
free-form-layer craft the owner guides do not cover, and two of them restate the repo's recurring named
principles (ONE ROLE PER INPUT, NAME WHAT MOVES PIN WHAT STAYS) in MiniMax's context.
