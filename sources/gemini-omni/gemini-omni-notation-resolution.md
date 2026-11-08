# Gemini Omni: split decision and notation adjudication

Not a scrape. Hand-authored 2026-08-07 from the sibling scrapes in this folder. Records why Gemini Omni
Flash became its own guide instead of joining `gemini-image.md`, which tag notation is canonical, and
what the sibling Nano Banana 2 Lite release does to the image guide.

## 1. Separate guide, and this is the clearest split in the set

Gemini Omni Flash (`gemini-omni-flash-preview`) shares a vendor and a conversational philosophy with the
Gemini Image family, which makes a merge tempting. It fails on the repo's actual test, and not marginally:
four documented rules directly contradict `gemini-image.md`, on top of a full video layer.

| Question | `gemini-image` | `gemini-omni` |
| --- | --- | --- |
| Negatives | No negative field; use semantic negatives, describe the absence positively ("an empty street with no traffic") | Plain negatives work and are the documented advice: "No dialogue", "No embellishments", "Don't add text" |
| Reference notation | Positional natural language ("the dress in the first image") | Angle-bracket role tags, `<FIRST_FRAME>` and `<IMAGE_REF_N>`, plus an explicit declaration block |
| Editing verbosity | Detailed instruction with invariants pinned | "Simple prompts work best. Overly descriptive prompts can lead to unintended changes." The owner shows verbose prompts as the Avoid case |
| Languages | 14 named, multilingual text rendering is a headline strength | "English (EN) is fully supported, but other languages have not been evaluated" |

The negatives row alone is disqualifying. An agent carrying the image guide's rule across would rewrite
"No dialogue" into a positive description and lose a control the video model actually honours. The
notation row is the same problem in reverse.

On top of that sits everything a video modality brings and the image scheme has no equivalent for:
timecode syntax, event-triggered edits, audio direction, shot-cut control, and a default that produces
multiple shots unless told otherwise.

This is the Wan and FLUX 3 precedent applied a third time. Same vendor, same conversational instinct,
different scheme.

Guide is `guides/gemini-omni.md`, scheme `gemini-omni`, named at the family level ("Gemini Omni") rather
than after the single current release, matching how `gemini-image.md` is family-level. Omni Flash is the
first release of an any-to-any line announced at Google I/O 2026, so more members are expected.

## 2. Two tag families in owner material; the API docs win

The API documentation formally defines two role tags: `<FIRST_FRAME>` to pin a starting frame and
`<IMAGE_REF_N>` (zero-indexed) to bind a reference, plus an explicit declaration form
`[# Sources <FIRST_FRAME>@Image1] [# References <IMAGE_REF_0>@Image2]` with natural-language guiding
instructions appended at the end of the prompt.

The DeepMind showcase page uses a different, looser family in its example prompts: bare `<image>`,
`<video>`, and `<object>` as inline placeholders, for example `Change spaceship to <object>` and
`When the finger in <video> touches the animal toy play the sound the animal makes`.

Resolved on the repo's owner-vs-owner rule: the API reference governs, because these guides serve agents
prompting through providers and proxies that wrap the API. `<FIRST_FRAME>` and `<IMAGE_REF_N>` are taught
as canonical. The showcase forms are recorded here as tolerated variants and are not taught, since
nothing in the API documentation defines them and a proxy has no reason to accept them.

Note the docs' own recommendation ranks the simple tags above the explicit declarations, so the guide
teaches simple tags first and the declaration block as the multi-role fallback.

**Rendering hazard:** every one of these tags must live inside a code fence or backticks in the guide.
Bare in Markdown prose they are raw HTML and vanish on render. This is the same defect caught in the
MiniMax H3 draft, and the repo's awk lint does not detect it; the angle-bracket check does.

## 3. Event-triggered editing is the distinctive capability

Worth naming because it does not appear in any other guide in the set. The owner's showcase prompts bind
a change to a moment in the source clip rather than to a timestamp:

- `When the person touches the mirror, the entire environment turns into 3d voxel art`
- `When the hand opens, reveal a physical photorealistic flying machine based on this sketch, floating above the hand, propeller spinning. No music, just realistic sound.`
- `Add harp sounds synchronized to when I touch each fern leaf`
- `The lights of the apartments start turning on in sync with the music.`

Google's own framing for this is "text and action synchronization". It coexists with, and is separate
from, the clock-based forms the API docs document (natural-language timing such as "After 3 seconds, a
woman enters the scene", and the bracketed `[0-3s]` timecode syntax). The guide teaches both and
distinguishes them: clock timing for choreography, event triggers for reactions in supplied footage.

## 4. Documented non-capabilities are kept, as prompt hazards

The docs list several things the model will not do, and they are in scope because writing a prompt that
asks for them wastes a generation: no video extension, no interpolation between a first and last frame,
no reasoning across multiple videos, no voice editing, and no audio reference uploads. The guide states
these as "do not prompt for" rather than as a capability table.

Precedent for keeping this class of fact: `gemini-image.md` already carries "transparent backgrounds are
unsupported, so ask for a white background".

## 5. Duration and aspect ratio

Aspect ratio is a request parameter here rather than something the model reads from the prompt, which
differs from most guides in the set. The owner's own showcase prompts nonetheless append both, for
example `Cinematic, 16:9.` and `10s.`, so writing them into the prompt text is attested owner practice
and is kept. The guide notes that the reliable control is host-side and moves on, per the standing rule
for host-specific knobs.

The blog's "10-second video generations currently, with longer durations coming soon" is a capability
limit and is not printed.

## 6. Sibling release: Nano Banana 2 Lite merges into the image guide

The same announcement introduced Nano Banana 2 Lite (`gemini-3.1-flash-lite-image`), which is a Gemini
Image family member, not an Omni one. It merges into `gemini-image.md` as a capability tier: the owner
describes it as "the control and accuracy you expect from Nano Banana, accelerated", retaining "reliable
prompt adherence, strong character consistency and legible in-image text rendering". No new grammar.

The same announcement demotes the original Nano Banana (`gemini-2.5-flash-image`) to legacy, with an
explicit recommendation to swap to Lite. The guide records that, since it changes which variant an agent
should reach for, and the model entry is kept rather than deleted because hosts still serve it.

## 7. Provider status

fal serves Gemini Omni and describes it accurately ("like Nano Banana for video", multi-turn edits with
consistency held on unmentioned elements), but publishes no prompting guide, only endpoint copy. It is
cited as a provider source for the conversational-editing framing only. WaveSpeed had an availability
post and no prompt guidance. Re-check both later.

## 8. Gemini Omni 1.1 and 1.2 (2026-11-08)

Timeline, from the AI Studio changelog and model page: `gemini-omni-flash-preview` (this guide's original
subject) was followed by `gemini-omni-1.1-flash`, GA on 2026-08-27, which added video extension, first and
last frame interpolation and resolution control. The preview shut down on 2026-09-30. `gemini-omni-1.2-flash`
went GA on 2026-11-05, and `gemini-omni-1.1-flash` routes to it from 2026-12-03. This repo missed the 1.1
release; the 1.2 pass covers both.

Same scheme, no split. The API guide's prompt section carries over unchanged apart from the removed tag
section and new extension tips. Tiers: 1.2 is `distilled` on the same Flash mapping the preview had, 1.1 is
`legacy`, and the preview row is dropped.

### Section 2 is reversed: the tags are deprecated

The 1.2 API guide says: "Do not include control strings (such as `<FIRST_FRAME>`, `<LAST_FRAME>`,
`<IMAGE_REF_0>`, or `<VIDEO_REF_0>`) in your text prompts. These tags are deprecated and unsupported in
future models. Describe how each image or video should be used in natural language instead." Its "Using
tags in prompts to set image roles" section is gone. The surface that section 2 ruled canonical has
withdrawn the notation, so the guide now teaches plain-language roles, and the simple-tag template, the
explicit-declaration block and the six-reference timeline example are removed.

- fal's 1.1 guide still teaches `<IMAGE_REF_0>` and `<VIDEO_REF_0>`. Owner wins. fal's prompts are reused
  with the tags replaced by plain names, and each Why line says so.
- The lowercase `<image>`, `<video>`, `<object>` and `<audio>` placeholders are still on the DeepMind
  showcase and on the DeepMind prompt guide, both app surfaces (Gemini app, Flow). Still recorded, still not
  taught.
- Google's 1.1 blog names inputs by filename ("The dog character dog.png should do the classical dance from
  dance3.mp4"). That only works if the host passes filenames to the model, which no source confirms. Not
  taught.
- The owner's own 1.2 reference example ("A cat playfully batting at a ball of yarn.", given a cat image and
  a yarn image) names neither image, which is why the guide says a plain description suffices when the
  subjects are obvious.

### Section 4 is reversed: extension and first-and-last frame now work

Both are documented and demonstrated since 1.1. The "do not prompt for" list is rewritten to the 1.2
limitations: extension appends only; uploaded clips with speech cannot be extended with more dialogue;
reference clips only for new generations; no voice editing (the model card adds that changing what someone
says is restricted); no API audio input.

### Owner-internal tensions, and how each was settled

- Several reference videos against "Referencing or reasoning across multiple videos is not supported". The
  docs allow several short reference clips and the 1.1 launch demo maps three dance clips to three
  characters, yet the limitations list warns against multi-video prompting. Taught as: tie each clip to one
  character or one job, and expect reliability to drop as clips are added.
- Dialogue quotes. The API guide, the DeepMind prompt guide and the 1.1 blog all quote spoken lines. The
  Vertex video best-practice page, which covers Omni and Veo together, says to use a colon and no quotes so
  the line is not rendered as text. The Omni-specific surfaces govern for the default; the Vertex form is
  taught as the fix when lines bleed into captions.
- "Focus short videos on a single scene" (Vertex, shared with Veo) says to split A-then-B-then-C into
  separate clips. The Omni API guide teaches timecoded multi-beat sequences and a multi-shot default, and
  extension is its documented way to lengthen a story. Not taught as a rule.
- Image-to-video. Vertex says to prompt for motion only and not re-describe the image; the DeepMind prompt
  guide and both owner first-and-last-frame examples re-describe the endpoints. Different modes, and both
  are taught under their own mode.
- Audio references. The API guide says audio inputs and references are unsupported in the current API; the
  Cloud GA post says they are "gated behind allowlisting"; the model card and DeepMind pages list audio input
  and show sampled voices. Taught as: describe voices and sound in words.
- Extension totals. The DeepMind prompt guide still says "10 second intervals, up to 40 seconds total" and
  "Omni 1.1"; the API guide says 3 to 10 seconds per turn and 30 seconds total. Numbers are out of scope; the
  prompt-guide page is stale on this.
- Duration in the prompt. The API guide says a duration set on the request replaces any length in the
  prompt, so section 5's "stating them costs nothing" becomes: the prompt length is read when the request
  sets none.

### Provider points

fal's 1.1 guide is the richest prompting source after the API guide. Taken from it: the two-speaker
flagship, the three-input reference prompt (tags replaced), the product edit with a preserve list, the
regrade-plus-hat edit (used as the style-plus-edit example with a note that it carries two changes), the
advice to make a last frame by editing the first, and the motion-only image pins. Not taken: fal's statement
that Google's prompt guide for the model breaks a prompt into components "and starts with the subject" with
a link to the 1.1 blog; the blog contains no such breakdown.

Kept out as limits or provider surface: resolution values, clip lengths, reference counts (images per
character, number and length of clips), the extension lookback in seconds, pricing, the seed parameter, and
regional rules beyond a one-line pointer.
