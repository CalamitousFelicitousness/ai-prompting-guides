---
guide: "ElevenLabs Speech"
prompt_scheme: "elevenlabs-speech"
models:
  - { id: "eleven_v3", access: "closed-weights", tier: "flagship", caps: [text-to-speech, audio-tags, multi-speaker, ipa-pronunciation], best_for: "expressive performance. The only tier with audio tags and inline IPA, and the one that does NOT accept break tags, so its pause control is punctuation and tags instead" }
  - { id: "eleven_v3_conversational", access: "closed-weights", tier: "std", caps: [text-to-speech, audio-tags, multi-speaker, ipa-pronunciation], best_for: "the same expressive scheme built for realtime turn-taking rather than rendered narration" }
  - { id: "eleven_multilingual_v2", access: "closed-weights", tier: "std", caps: [text-to-speech, break-tags, emotion-by-context], best_for: "lifelike delivery across a fixed language set. No audio tags, so direction comes from narrative context, punctuation and break tags" }
  - { id: "eleven_flash_v2_5", access: "closed-weights", tier: "distilled", caps: [text-to-speech, break-tags, emotion-by-context], best_for: "low-latency work across the multilingual set plus a few more. Same non-tag scheme as multilingual v2" }
  - { id: "eleven_flash_v2", access: "closed-weights", tier: "distilled", caps: [text-to-speech, break-tags, phoneme-tags, emotion-by-context], best_for: "English-only low latency, and the ONLY model that accepts SSML phoneme tags. If a pronunciation must be pinned with Arpabet rather than IPA, this is the one tier that can do it" }
  - { id: "eleven_ttv_v3", access: "closed-weights", tier: "std", caps: [voice-design], best_for: "designing a voice from a written description rather than choosing or cloning one" }
  - { id: "eleven_multilingual_ttv_v2", access: "closed-weights", tier: "legacy", caps: [voice-design], best_for: "the previous voice-design generation" }
  - { id: "eleven_multilingual_sts_v2", access: "closed-weights", tier: "std", caps: [speech-to-speech], best_for: "performing a line yourself and transferring it onto another voice, which keeps your delivery instead of describing it" }
  - { id: "eleven_english_sts_v2", access: "closed-weights", tier: "std", caps: [speech-to-speech], best_for: "the English-only voice changer" }
capabilities: [text-to-speech, audio-tags, multi-speaker, ipa-pronunciation, break-tags, phoneme-tags, voice-design, speech-to-speech, emotion-by-context]
prompt:
  languages: ["en", "multilingual"]
  script: "the prompt is the text to be spoken. Bracketed audio tags are performed rather than read, but ordinary narrative direction is NOT: a phrase like 'she said sadly' is part of the transcript and gets spoken"
  direction_syntax: "SPLIT BY MODEL GENERATION. v3 takes square-bracket audio tags such as [whispers] and inline IPA between forward slashes, and rejects break tags. The v2 family takes <break time=\"1.5s\" /> and, on one English tier only, SSML phoneme tags, and has no audio tags at all"
  audio_tags: "an OPEN vocabulary on v3, covering emotion, delivery and non-verbal sounds. Tags must describe something AUDIBLE and must apply to the voice only: the owner rules out [standing] or [grinning] as non-auditory and rules out music and sound-effect tags as out of scope for the voice"
  voices: "cast from the library, a clone, or a voice designed from a written description. The owner notes pacing is inherited from the audio a voice was built on, so a rushed voice is often a voice problem rather than a prompt problem"
  length_strategy: "write the script as it should be read. Emphasis comes from capitalisation, punctuation and ellipses rather than from length"
  auto_expand_behavior: "an opt-in Enhance step runs a language model over the transcript to insert audio tags. It is documented not to change a single word of the text, only to add tags and adjust emphasis punctuation"
  negatives: "no negative field. An unwanted delivery is fixed by recasting the voice, changing the tags, or rewriting the line"
sources:
  official: ["https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices", "https://elevenlabs.io/docs/overview/models", "https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-alpha"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# ElevenLabs Speech: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the ElevenLabs text-to-speech line. Eleven Music and Sound Effects are a different scheme with their own guide.
- THE PROMPT IS THE SCRIPT. Everything in it is spoken except the bracketed tags and markup described below.
- THE NOTATION SPLITS BY GENERATION and the two halves are mutually exclusive. v3 has audio tags and inline IPA and does NOT accept break tags. The v2 family has break tags and no audio tags. Writing v3 tags into a v2 model, or break tags into v3, silently fails.
- Narrative emotion cues are SPOKEN. Writing "she said, her voice trembling" does steer the delivery, and the model also reads the words aloud. The owner's advice is to remove them in post-production.
- Audio tags must be audible and about the voice. Not gestures, not music, not sound effects.
- Choose the voice for the job before writing tags. Pacing and character are inherited from the audio a voice was built on.

</rules>

## TL;DR

<template id="quickstart">

[{emotion or delivery}] {The line to be spoken.} [{non-verbal}] {The next line, with CAPITALS for emphasis and an ellipsis for hesitation...}

</template>

## Models and when to use which

The line splits on notation, not just on quality, so pick the model before writing the script.

- `eleven_v3`: the expressive flagship. Audio tags and inline IPA, no break tags. This is the default for performance work.
- `eleven_v3_conversational`: the same scheme tuned for realtime dialogue rather than rendered audio.
- `eleven_multilingual_v2`: lifelike but tag-free. Direction is narrative context, punctuation and break tags.
- `eleven_flash_v2_5` and `eleven_flash_v2`: the low-latency tiers, on the same tag-free scheme. Flash v2 is English only.
- `eleven_flash_v2` is the sole exception worth remembering for pronunciation: it is the only model that accepts SSML phoneme tags, so Arpabet is available there and nowhere else. On v3, use IPA instead.
- Text-to-voice models design a voice from a description; speech-to-speech models transfer your own recorded performance onto another voice.
- Speech-to-speech is the answer when direction keeps failing. Performing the line yourself and transferring it moves delivery out of the prompt entirely.

## How the model reads prompts

- Everything in the transcript is spoken unless it is recognised markup. Bracketed audio tags on v3 and break tags on v2 are consumed; ordinary prose is not.
- That includes emotional narration. The documented technique of writing dialogue tags works on delivery, and the words are still read out. This is the single most surprising behaviour in this scheme and it has no equivalent in models that separate direction positionally.
- Punctuation carries prosody. Ellipses produce hesitation, dashes produce short breaks, and both are documented as less consistent than explicit pauses.
- Capitalisation carries emphasis. The owner's own enhancement process adds capitals, question marks and exclamation marks to increase emphasis without changing words.
- The voice sets pacing. A voice built from short or clipped samples tends to rush, which is corrected by rebuilding or recasting the voice rather than by prompting harder.
- Tags act where they sit. Place a tag immediately before the segment it modifies, or immediately after, and it colours that segment.
- Text normalisation varies by model. Numbers, currency, dates and alphanumeric strings are not read identically across tiers, so anything whose reading matters should be written out or pinned.

## Prompt structure

<rules id="structure">

- Write the words as they should be heard, then add markup for what the words cannot carry.
- Keep emotional narration out unless you intend to hear it. If you use it deliberately, plan to cut it in post.
- Use capitals for emphasis and ellipses for hesitation rather than reaching for a tag every time.
- Spell out or pin anything whose reading is ambiguous: numbers, currency, dates, initialisms and abbreviations.
- Break long scripts into segments and assemble them, which is also the owner's advice for complex sequences.
- Match the script's register to the voice. A conversational voice reading formal copy fights itself.

</rules>

## Audio tags on v3

<rules id="tags">

- Tags are square-bracket modifiers inside the transcript, in three families: emotion such as `[curious]`, `[sad]` or `[mischievously]`; delivery such as `[whispers]` or `[shouts]`; and non-verbal sounds such as `[laughs]`, `[sighs]` or `[clears throat]`.
- The vocabulary is OPEN. The owner's own list is explicitly non-exhaustive and invites contextually similar tags.
- A tag must describe something AUDIBLE. The owner rules out `[standing]`, `[grinning]` and `[pacing]` because they are not sounds.
- A tag must be about the VOICE. Music and sound-effect tags are explicitly excluded; those belong to the separate sound-effects model, not to a speech transcript.
- Place a tag immediately before the segment it modifies, or immediately after it. `[annoyed] This is hard.` and `This is hard. [sighs]` are both correct placements.
- Tags combine for compound delivery, and combinations are worth experimenting with.
- Do not convert existing narration into a tag. The owner's rule is that tags are additions, so "He laughed loudly" becomes "He laughed loudly [chuckles]" rather than "[laughing loudly] He laughed".
- v3 has no break tags. Use `[short pause]`, `[long pause]`, or an ellipsis.

</rules>

<example use_case="tagged single-speaker line">

```text
[appalled] Are you serious? [sighs] I can't believe you did that!
```

*Why: the owner's own enhancement example. Each tag sits immediately before the clause it colours, both describe something audible, and neither replaces any of the original words.*

</example>

<example use_case="dialogue with interruption">

```text
Speaker 1: [starting to speak] So I was thinking we could-

Speaker 2: [jumping in] -test our new timing features?

Speaker 1: [surprised] Exactly! How did you-

Speaker 2: [overlapping] -know what you were thinking? Lucky guess!
```

*Why: adapted from the owner's timing example. Speaker labels bind the turns, trailing and leading dashes mark where a line is cut off, and the tags describe the manner of the interruption rather than narrating it in words that would be spoken.*

</example>

## Pauses and pronunciation

<rules id="notation">

- ON v3: pause with an ellipsis or a pause tag; there are no break tags. Pin a pronunciation by writing IPA between forward slashes directly in the text, which is supported natively across the model's language range.
- ON THE v2 FAMILY: pause with `<break time="1.5s" />`, up to about three seconds. Too many break tags in one generation destabilises the output, producing rushing or artefacts.
- Dashes and ellipses work on both as softer alternatives to an explicit pause, and are documented as less consistent.
- SSML phoneme tags exist only on the English Flash v2 tier. Arpabet is available there and nowhere else.
- Where a pronunciation is wrong and the model has no phonetic route, try alternate spellings. The owner recommends phonetic approximation as a legitimate fallback.
- For a name or term that recurs across a project, a pronunciation dictionary is the durable fix rather than repeating notation inline.

</rules>

<example use_case="pause and pronunciation on a v2 tier">

```text
"Hold on, let me think." <break time="1.5s" /> "Alright, I've got it."
```

*Why: the owner's own example. One break tag rather than several, placed between complete utterances; a run of them in a single generation is what causes the model to speed up or add artefacts.*

</example>

## Voices

<rules id="voices">

- Three routes: pick from the library, clone from a recording, or design a voice from a written description.
- Pacing is inherited from the audio a voice was built on. The owner recommends longer, continuous samples when creating a voice, because short clips produce unnaturally fast speech that no prompt fixes.
- Match the voice to the emotion you are asking for. A tag telling a bright voice to sound exhausted is fighting the casting.
- A separate speed control adjusts rate within a modest range, and extreme values degrade quality. Reach for it after casting and phrasing, not before.
- Where the performance matters more than the text, record it yourself and use speech-to-speech, which carries your delivery onto the target voice.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- No negative field. Nothing is subtracted from the audio.
- An unwanted delivery is a casting problem first, a tag problem second, and a wording problem third. Work in that order.
- Do not write an exclusion into the transcript. It is the spoken text and it will be read aloud, which is the same trap as narrative emotion cues.
- Where a tag is being ignored, try a different word rather than a stronger one. The vocabulary is open and the model is matching meaning, not looking up a table.
- Removing a competing tag often works better than adding a corrective one.

</rules>

## Pitfalls and anti-patterns

- Mixing the two notations: break tags do nothing on v3, and audio tags are not understood by the v2 family. Decide the model first.
- Forgetting that narrative emotion is spoken: "she whispered, terrified" changes the delivery AND is read aloud. Use a tag, or plan to cut the words.
- Writing a non-auditory tag: `[grinning]`, `[standing]` and `[pacing]` are not sounds and the owner rules them out.
- Writing music or sound-effect tags into a speech transcript: tags are voice-only. Sound effects are a separate model with its own guide.
- Converting narration into a tag: tags are additions, not a reformatting of the words already there.
- Stacking break tags: several in one generation destabilises the output and causes rushing or artefacts.
- Reaching for Arpabet on the wrong model: SSML phoneme tags work only on the English Flash v2 tier. Use IPA on v3.
- Blaming the prompt for a rushed voice: pacing comes from the samples the voice was built on.
- Leaving numbers and currency unnormalised: reading differs by model, so anything that matters should be written out.
- Assuming another vendor's tag vocabulary transfers: bracketed tags are model-specific, and several models in this set read an unrecognised bracket aloud.
- Treating the tag list as fixed: it is explicitly non-exhaustive, and sticking to the published examples leaves most of the control unused.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (ElevenLabs): the [text-to-speech best practices guide](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices), which is the source of the pause and pronunciation notation and its per-generation split, the emotion technique and the warning that its cues are spoken, the pacing and speed guidance, the text-normalisation material, and the v3 prompting section including the tag placement and content rules and the verbatim examples; the [models overview](https://elevenlabs.io/docs/overview/models) for the line-up and which capability each tier has; the [audio tags help-centre entry](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/how-do-audio-tags-work-with-eleven-v3-alpha) for the three tag families.

Coverage note: ElevenLabs' documentation site serves every page as markdown at the same path with a `.md` suffix, with a page index at `/docs/llms.txt` and a single-file dump at `/docs/llms-full.txt`. Everything here comes from those. Secondary coverage of Eleven v3 claims that inline sound-effect tags such as gunshots or explosions can be placed in a speech transcript; the owner's own tag specification rules that out explicitly, stating tags must not be used for anything other than the voice, so this guide follows the owner. The owner also publishes the full language-model prompt behind its Enhance button, which is the most precise statement of tag rules it makes anywhere, and several rules here are taken from it.

Last verified: 2026-08-29.
