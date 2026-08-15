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
