# MiniMax audio source conflicts and their resolution

Not a scrape. This is a hand-authored adjudication of conflicts between MiniMax's own surfaces,
written because the repo's source bar resolves owner-vs-provider on owner authority but has no rule
for owner-vs-owner. Evidence pulled from the sibling markdown files in this folder and from the
MiniMax Music 3 model card, read through the authenticated HF tools. Written 2026-08-29.

Covers both `minimax-speech` and `minimax-music`, since the conflicts arise from the same doc set.

## How these docs were read at all. METHOD, worth reusing.

`platform.minimax.io/docs` is a Mintlify site that renders client-side. An ordinary fetch of a guide
page returns about 90 KB of Next.js shell that strips to ZERO bytes of text, which is the failure mode
CLAUDE.md warns about: a large response that is not a page. Byte count alone said the page was fine.

Two things rescue it, and both should be tried on any vendor docs site before reaching for a renderer:

- **Every page is served as markdown at the same path plus `.md`.** This is the same trick that
  `docs.x.ai` supports, and it is a Mintlify feature rather than a MiniMax one, so expect it on any
  Mintlify-hosted vendor docs.
- **`/docs/llms.txt` is a complete page index** with one annotated line per page. It is the fastest way
  to find every audio-related page without crawling, and it is how the self-hosting page and the
  voice-design reference were found at all.

Not every path has a twin: `guides/t2a.md` returns four bytes while `guides/music-generation.md`
returns 13 KB. Take the paths from `llms.txt` rather than guessing them.

## Conflict 1: how the compound section tags are spelled. RECORDED BOTH WAYS.

| Surface | Pre-chorus | Post-chorus | Instrumental passage |
| --- | --- | --- | --- |
| Music generation API reference | `[Pre Chorus]` | `[Post Chorus]` | `[Inst]` |
| MiniMax Music 3 model card | `[Pre-Chorus]` | `[Post-Chorus]` | `[Instrumental]` |

Space against hyphen, and an abbreviation against a full word. Both are current and neither
acknowledges the other.

The usual rule here is that the API reference governs, because these guides serve agents prompting
through providers and proxies. **That rule does not cleanly apply this time**, because the two surfaces
describe the two genuinely different ways the model is reached: the hosted API on one side, and
self-hosted weights driven from the model card on the other. Neither is the wrapper of the other.

The guide therefore records both, tells the reader to match the surface they are prompting through,
and names the API reference's forms as the default when unsure. This is a deliberate departure from
the owner-vs-owner rule, and it is the first case in this repo where the two conflicting surfaces are
not two descriptions of one delivery path.

## Conflict 2: nothing. Speech 2.8 really did lose a capability.

Not a documentation conflict, but it reads like one and would be easy to "correct" away.

The emotion field supports `whisper` and `fluent` on `speech-2.6-turbo` and `speech-2.6-hd`, and the
same sentence states that `speech-2.8-hd` and `speech-2.8-turbo` do NOT support `whisper`. Meanwhile
2.8 is the only generation that supports interjection tags. So the newest tier is not a superset of
the one before it, in both directions.

This is stated exactly once, in the final clause of the emotion parameter's description. The release
notes announce 2.8 as an upgrade and mention no regression. The guide states it in the model rows, in
the model-selection section and in the pitfalls, because a script that needs whispering will otherwise
be sent to the newest model and quietly not whisper.

## The parenthesis collision in the speech script. NOT A CONFLICT, BUT THE MAIN HAZARD.

Three notations live inside the spoken script, and two of them share a delimiter:

- `<#x#>` for a timed pause. Unambiguous.
- `(phonetic)` for a pronunciation override, taking Pinyin with a tone digit, IPA, or Jyutping with a
  tone digit.
- `(laughs)` and eighteen other fixed words for non-verbal sounds, on the 2.8 tiers only.

The last two are both half-width parentheses, so the ONLY thing distinguishing an interjection from a
pronunciation override is whether the content is a recognised interjection or a parseable phonetic
string. Anything else in parentheses is neither, and the model reads it aloud.

That failure is silent and it is the most likely way a MiniMax speech prompt goes wrong, because
parentheses are the natural thing to reach for when writing an aside. The guide gives it its own rule
and its own pitfall entry.

## Access: the hosted music API is closing. RECORDED IN THE GUIDE.

The music generation guide carries a notice that from 2026-08-20 the paid Music Generation and Lyrics
Generation APIs are no longer available to new users, existing paying users continue, and the free
tiers are discontinued. It points new users at the consumer app or at the open-weights model.

This is access, not prompt craft, and normally out of scope. It is recorded because it changes which
surface a reader will actually be prompting through, and therefore which of the two tag spellings
above applies to them. The guide states it once, in the global rules and the model section, without
pricing detail.

`music-3.0` is treated as one model with published weights rather than as a hosted model and a
separate open one. The docs point at the Hugging Face model as the replacement for the API, which
makes them the same model on two delivery paths, and `access` records weight publication alone.

## Speech publishes 40 languages, music publishes none. NOT INTERCHANGEABLE.

The synchronous text-to-speech guide carries a supported-languages table of 40, and the API
reference's language-hint field accepts the same 40, so the two surfaces agree. The hint's
description adds one thing the table does not: the superseded 01 and 02 series do not support
Persian, Filipino or Tamil. That is a missing language rather than a weaker one, which makes it a
reason to pick a current tier rather than a quality trade-off.

Cantonese and Nynorsk appear as entries in their own right rather than inside Chinese and Norwegian.
That pairing is the case the hint exists to settle, and it matches the guide's existing account of
what the hint is for.

No equivalent list exists for the music model on any owner surface. The 40 belong to the speech
models, so `minimax-music` records its coverage as unpublished rather than inheriting them.

## What the guides take from where

- Pause, pronunciation and interjection notation, the interjection vocabulary, per-tier availability,
  the emotion set and its per-model support: all from the text field and emotion field descriptions in
  the speech API reference. This is the case CLAUDE.md describes, where an API reference page carries
  real prompt technique in its field descriptions; the surrounding schema is out of scope.
- Voice design's description-plus-preview pattern and its verbatim example: the voice design reference.
- The Structured Caption's three sections and the structured example prompt: the Music 3 model card.
- The section-tag list, the short-register example, and per-mode field requirements: the music
  generation API reference.
- The two cover workflows: the music generation guide.
- Sample rate, duration, architecture and VRAM for the spec table: the Music 3 model card.

- The forty-language list: the synchronous text-to-speech guide. The three languages the 01 and 02
  series lack: the API reference's language-hint field.
