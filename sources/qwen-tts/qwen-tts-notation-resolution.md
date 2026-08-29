# Qwen TTS source decisions

Not a scrape. A hand-authored record of the merge decision and the source access situation for
`qwen-tts`. Written 2026-08-29.

## The merge was verified, not assumed

Planning called for merging Qwen3-TTS (open weights) with Qwen-Audio-3.0-TTS (hosted) under the rule
that access is not a scheme split. That rule alone would not have been enough here, because the two
are separate releases from different points in time with confusingly adjacent names, and a different
control scheme would have forced a split regardless of access.

The evidence that they share a scheme comes from Alibaba's Model Studio speech synthesis page, which
documents both lines side by side on one API surface:

- `qwen-audio-3.0-tts-flash` and `qwen-audio-3.0-tts-plus` take direction through an `instruction`
  parameter.
- `qwen3-tts-instruct-flash-realtime` takes direction through an `instructions` parameter, and its
  sibling `qwen3-tts-flash-realtime` has no such field.

Both are natural-language delivery direction in a field separate from the spoken text, which is the
same shape the open repository documents as `instruct`. **Merged, on evidence.**

## Instruction control is a capability, not a flag

The single most useful thing in this guide, and the easiest to get wrong:

| Checkpoint | Instruction control |
| --- | --- |
| `Qwen3-TTS-12Hz-1.7B-CustomVoice` | yes |
| `Qwen3-TTS-12Hz-1.7B-VoiceDesign` | yes |
| `Qwen3-TTS-12Hz-1.7B-Base` | no |
| `Qwen3-TTS-12Hz-0.6B-CustomVoice` | NO |
| `Qwen3-TTS-12Hz-0.6B-Base` | no |
| `qwen3-tts-instruct-flash-realtime` | yes |
| `qwen3-tts-flash-realtime` | NO |

The 0.6B CustomVoice looks like a cheaper 1.7B CustomVoice and carries the same nine timbres, and it
silently has no direction field. On the hosted side the same distinction is carried entirely by the
model id. Both are recorded in the guide's model rows and its pitfalls.

## Access notes

- The open repository README and the Model Studio speech synthesis page are both server-rendered and
  fetch cleanly.
- The hosted line's dedicated pages do not. `alibabacloud.com/help/en/model-studio/qwen-audio-tts`
  returned 10 bytes of text and the Chinese equivalent returned 587; both render client-side. The
  Alibaba Cloud blog announcing the model returned nothing either. Only the general speech synthesis
  page at `/help/en/model-studio/text-to-speech` is readable, and it happens to carry everything
  needed. Anyone re-verifying should go there rather than to the per-model pages.
- The output sample rate is not stated in the README or on the model cards. It is taken from
  `config.json` in the owner's own tokenizer repository, which gives `output_sample_rate: 24000`,
  `audio_channels: 1` and a 12.5 Hz frame rate. That is an owner artefact in an owner repository, so
  it is recorded unmarked in the spec table rather than as unpublished.

## Naming hazard

`Qwen3-TTS` is the Apache-2.0 open series from the Qwen team. `Qwen-Audio-3.0-TTS` is a hosted,
closed product released about four months later. The names are one token apart and the access is
completely different, so a search for open Qwen TTS weights lands on the hosted product routinely.
Stated in the guide's model section and its pitfalls.
