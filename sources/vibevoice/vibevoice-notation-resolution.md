# VibeVoice source recovery and its resolution

Not a scrape. A hand-authored record of how this guide was sourced, written because the normal
route failed and the fallback is worth documenting. Written 2026-08-29.

## The problem

VibeVoice's distinctive prompt grammar is the multi-speaker labelled script. On 2025-09-05 Microsoft
removed the VibeVoice-TTS inference code from the repository, stating it had found uses inconsistent
with the release's intent. That removal took the usage section and the multi-speaker example scripts
with it.

The result was that the grammar appeared undocumented on every live owner surface:

| Surface | State |
| --- | --- |
| `microsoft/VibeVoice` README | Installation and Usage section replaced by "Disabled due to widespread misuse" |
| `docs/vibevoice-tts.md` | model description and tips survive; no usage, no script format |
| `demo/text_examples/` | only the single-speaker file remains; every multi-speaker example returns 404 |
| `microsoft/VibeVoice-1.5B` card | Installation section points back to the GitHub README section that no longer exists |
| `microsoft/VibeVoice-1.5B` files | weights, config and one figure. No examples |

Git history does not help. Listing commits with `until=2025-09-06` returns exactly one, the removal
commit itself, so the branch was rewritten and no pre-removal revision is retrievable through the
API.

## The resolution: the technical report is an owner surface

The format is specified in the paper, in section 2.2's Input Representation:

> The model input X is formed by concatenating the voice font features and the text script
> embeddings, specified by users, interleaved with role identifiers (Speaker_k)

with the input written as `X = [Speaker_1: z_1, ..., Speaker_N: z_N] + [Speaker_1: T_1, ...,
Speaker_N: T_N]`, where the z terms are voice features and the T terms are text.

That gives the whole grammar: `Speaker N:` role identifiers, one per turn, with the SAME identifier
binding a speaker's voice to that speaker's text. This project's spec rules already name the
technical report as an owner surface alongside the repository and the model card, so nothing here
required relaxing the source bar.

**No fork, mirror or community reupload was used.** A duplicated repository preserving the original
README would have been a community source repeating owner text, which this project's rule says is
still not a source. The paper made that question moot.

The paper also supplied two things the live surfaces do not: the roughly 2:1 speech-to-text token
ratio, which is how a long script is budgeted against the context window, and the guidance scale and
denoising step count now in the spec table.

## Correction to an earlier reading

An earlier pass through this material concluded that "the 7B is the ASR model, not a TTS model".
That is half right and the half that is wrong matters. There are TWO 7B models:

- `VibeVoice-Large`, the 7B TTS tier. Evaluated in the technical report, where scaling from 1.5B to
  7B is credited with richer timbre and better cross-lingual transfer. Marked **Disabled** in the
  owner's model table and never released.
- `VibeVoice-ASR-7B`, a released speech RECOGNITION model on the same repository.

So a 7B TTS model exists in the literature and not on disk. The guide states both and warns against
conflating them, because the repository presents them side by side.

## What the guide deliberately does not do

The owner's stated out-of-scope uses include voice impersonation without recorded consent, presenting
synthetic audio as genuine recordings, and live voice conversion, and those exclusions are the
reason the code was withdrawn. The guide covers script formatting, speaker labelling, punctuation and
pacing. It does not offer guidance on cloning a specific person's voice, and it states the withdrawal
and the responsible-use position in its own section rather than burying them in a source note.

The realtime checkpoint is worth noting here as the owner's own answer to the same problem: its
voices are embedded rather than user-supplied, which the documentation says explicitly is to mitigate
deepfake risk. That is why the guide points readers at it as the supported path.
