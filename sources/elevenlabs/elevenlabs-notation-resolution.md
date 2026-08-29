# ElevenLabs source conflicts and their resolution

Not a scrape. A hand-authored adjudication of conflicts between ElevenLabs' own surfaces and between
those surfaces and the secondary coverage of them. Written 2026-08-29. Covers both
`elevenlabs-speech` and `elevenlabs-audio`.

## Method: markdown twins and llms-full

`elevenlabs.io/docs` serves every page as markdown at the same path plus `.md`, publishes a page
index at `/docs/llms.txt`, and also publishes a single-file dump of the whole documentation set at
`/docs/llms-full.txt`. Everything in both guides comes from the markdown twins. No renderer needed.

## Conflict 1: can audio tags produce sound effects. RESOLVED on owner authority.

Secondary coverage of Eleven v3 states that inline sound-effect tags such as `[gunshot]`,
`[clapping]` and `[explosion]` can be placed directly in a speech transcript, describing it as a way
to place sound events at script-level timing without a separate step.

The owner's own tag specification says the opposite, twice:

- "DO NOT use tags such as [standing], [grinning], [pacing], [music]."
- "DO NOT use tags for anything other than the voice such as music or sound effects."

That specification is not marketing copy. It is the literal system prompt behind the Enhance button,
published verbatim in the best-practices page, which makes it the most precise statement of tag
semantics ElevenLabs makes anywhere.

**The owner governs.** The speech guide states that tags must be audible AND voice-only, and points
sound effects at the separate model. Recorded because the community claim is specific, plausible and
widely repeated, and someone re-verifying this guide will meet it before they meet the owner's rule.

## Conflict 2: nothing, but the notation genuinely splits by generation

Not a documentation conflict; a real product split that reads like one.

| | Audio tags | Break tags | Phonemes |
| --- | --- | --- | --- |
| `eleven_v3` | yes | NO | IPA inline, between forward slashes |
| `eleven_multilingual_v2`, `eleven_flash_v2_5` | no | yes | none |
| `eleven_flash_v2` | no | yes | SSML phoneme tags, Arpabet or IPA |

The two halves are mutually exclusive and both fail silently in the wrong place. The best-practices
page states plainly that "Eleven v3 does not support SSML break tags", and separately that phoneme
tags "are only compatible with the `eleven_flash_v2` model". So the single English low-latency tier
is the only place Arpabet works at all, which is an odd enough fact to be worth stating twice.

## The behaviour most likely to surprise: narrative emotion is spoken

The Emotion section recommends conveying emotion through narrative context or explicit dialogue tags,
and then says: "the model will still speak out the emotional delivery guides. These can be removed in
post-production using an audio editor if unwanted."

So the documented emotion technique produces audio containing the direction. This has no equivalent
in the other speech models in this set: Gemini separates direction positionally, MiniMax and Qwen
give it its own field, and OmniVoice has no prose direction at all. Only here does the recommended
technique require an editing pass afterwards.

The speech guide states it in the global rules, in the reading model and in the pitfalls, because it
is both counterintuitive and easy to not notice: the audio sounds right, and there is simply more of
it than you asked for.

## Why music and sound effects share one guide

The two models overlap in both directions rather than sitting on either side of a line:

- The sound-effects model's own prompting guide has a "Musical elements" section, with examples like
  "90s hip-hop drum loop, 90 BPM" and "Vintage brass stabs in F minor".
- The music best-practices guide has a "Sound Design" section covering non-musical audio, ambience
  and textures, prompted directly or inside a track.

Both take a describe-the-sound prompt and neither has a lyrics-style second field in its plain form.
This is the same reasoning that keeps Stable Audio's music and effects together, and it is why the
merge was chosen over the strict split at planning time.

## The negatives exception

`elevenlabs-audio` is the one audio guide in this set whose negatives section contradicts the
lorebook's always-on positive-phrasing default. Two owner statements drive it:

- Composition plans carry a `negative_styles` list per section, and the guidance is "Use negative
  styles liberally to prevent unwanted sounds."
- The loops section states that "a loop prompt is an exercise in exclusion" and that "for loops, the
  negative space is the prompt", with the worked example "no melody - just drums".

The always-on phrasing entry already yields to a loaded guide, and it has been updated to name this
as its counterexample rather than leaving the contradiction implicit.

## What the guides take from where

- Pause notation, IPA and phoneme rules, the emotion warning, pacing and speed, text normalisation,
  and the whole v3 prompting section including tag placement and content rules: the text-to-speech
  best-practices page.
- The three tag families: the audio-tags help-centre entry.
- Model line-up and per-tier capability: the models overview.
- The five questions, production vocabulary, era, arrangement narration, loops, timing cues and
  isolation prefixes: the music best-practices page.
- Section structure, the three bracket families and the corrected text example: the composition plans
  guide.
- Simple, sequence and musical-element patterns plus the trade vocabulary: the sound effects page.
