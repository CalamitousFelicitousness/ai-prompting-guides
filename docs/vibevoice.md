---
guide: "VibeVoice"
prompt_scheme: "vibevoice"
models:
  - { id: "VibeVoice-1.5B", access: "open-weights", tier: "std", caps: [text-to-speech, multi-speaker, long-form, voice-prompt], best_for: "long multi-speaker conversation from a labelled script, which is the model's whole reason to exist. Weights remain published; the owner withdrew its inference code, so running it is on you" }
  - { id: "VibeVoice-Realtime-0.5B", access: "open-weights", tier: "distilled", caps: [text-to-speech, streaming, long-form], best_for: "streaming single-speaker English narration. It is the SUPPORTED path, and it deliberately drops both multi-speaker and arbitrary voice prompts, so it does not take the labelled-script format at all" }
  - { id: "VibeVoice-Large", access: "closed-weights", tier: "flagship", caps: [text-to-speech, multi-speaker, long-form, voice-prompt], best_for: "the 7B tier evaluated in the technical report, where scaling gave richer timbre and better cross-lingual transfer. Never released: the owner's own table marks it Disabled, so it is documented but unobtainable" }
capabilities: [text-to-speech, multi-speaker, long-form, voice-prompt, streaming]
prompt:
  languages: ["en", "zh"]
  script: "a labelled transcript. The owner's technical report specifies the input as voice features and text both keyed by the same role identifiers, written Speaker 1:, Speaker 2: and so on, with each turn's text following its label"
  direction_syntax: "none. There is no tag vocabulary, no emotion field and no direction channel of any kind. Delivery comes from the voice prompt, from punctuation, and from what the words themselves imply"
  voices: "a voice prompt per speaker sets that role's timbre, and the same role identifier binds the voice to its turns. The realtime model instead ships fixed embedded voices, which the owner states is a deliberate choice to reduce deepfake risk"
  length_strategy: "budget roughly two speech tokens per text token. The owner reports a 2:1 speech-to-text ratio against a 64K context, which is what makes very long single-pass generation possible and is the number to reason about when a script may not fit"
  auto_expand_behavior: "none. Nothing is rewritten, and there is no planner in front of the model"
  negatives: "no negative field and no direction channel to negate. An unwanted delivery is a voice-prompt or punctuation problem"
sources:
  official: ["https://github.com/microsoft/VibeVoice", "https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-tts.md", "https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-realtime-0.5b.md", "https://huggingface.co/microsoft/VibeVoice-1.5B", "https://arxiv.org/abs/2508.19205"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# VibeVoice: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers Microsoft's VibeVoice text-to-speech line. VibeVoice-ASR is a speech recognition model on the same repository and is not a generation model, so it is out of scope here.
- READ THE AVAILABILITY SECTION FIRST. This is the only guide in this set covering a model whose owner withdrew its inference code, and what is documented does not match what is runnable.
- THE PROMPT IS A LABELLED SCRIPT. Each turn is prefixed with a role identifier, and the same identifier binds that speaker's voice to that speaker's lines.
- THERE IS NO DIRECTION CHANNEL. No audio tags, no emotion setting, no instruction field. Anything you write that is not a speaker label is spoken.
- Delivery therefore comes from three places only: the voice prompt for each role, the punctuation, and what the words themselves imply.
- English and Chinese are the trained languages. Other languages are documented as producing unpredictable output rather than an accent.

</rules>

## Availability

The line is not in the state its documentation implies, and this determines what is worth attempting.

- On 2025-09-05 the owner removed the VibeVoice-TTS inference code from the repository, stating that it had found uses inconsistent with the intent of the release. The repository's usage section and its multi-speaker example scripts went with it, and the model card's Installation section now points back to a README section that no longer exists.
- `VibeVoice-1.5B` weights remain published and downloadable. Running them is left to you.
- `VibeVoice-Large`, the 7B tier, was evaluated in the technical report but never released. The owner's own model table marks it Disabled.
- `VibeVoice-Realtime-0.5B` is the supported path: code, a demo and a notebook all ship. It is single-speaker and English-only, and it does not take the multi-speaker format at all.
- Do not confuse the two 7B models. `VibeVoice-Large` is the unreleased TTS tier; `VibeVoice-ASR-7B` is a released speech RECOGNITION model. Same repository, same number, different direction.
- The owner states the model is for research use and excludes voice impersonation without recorded consent, presenting synthetic audio as genuine recordings, and live voice conversion. Those exclusions are the reason the code was pulled, and they are worth reading before building on it.

## Models and when to use which

- `VibeVoice-Realtime-0.5B`: choose this unless you specifically need multiple speakers. It is supported, it streams, and its voices are fixed and embedded, which the owner says is deliberate rather than a limitation to work around.
- `VibeVoice-1.5B`: the multi-speaker long-form model, and the only released checkpoint that takes the labelled-script format. Weights only.
- `VibeVoice-Large`: documented for completeness. It is not obtainable.
- The realtime model is not a smaller version of the 1.5B. It drops the semantic tokenizer, takes only one speaker, and accepts only English, so it is a different job rather than a cheaper tier.

## How the model reads prompts

- Voice and text share one sequence. The technical report describes the input as voice features and text scripts concatenated together, both keyed by the same role identifiers, which is why the label is doing structural work rather than decorating the transcript.
- A language model reads the whole script before speaking any of it. That is what produces content-aware turn-taking rather than a run of separately synthesised lines glued together, and it is the reason to hand it the whole conversation at once rather than turn by turn.
- Length is budgeted in tokens, not minutes. The owner reports roughly two speech tokens per text token against a large context, so a very long script fits in one pass, and the failure mode when it does not is running out of context rather than degrading gradually.
- Nothing is rewritten. There is no planner, no expansion and no interpretation of intent, so the script is the entire specification.
- Background music appears on its own. The owner documents this as spontaneous and content-driven: a voice prompt containing music makes it more likely, and introductory phrasing such as a greeting can trigger it even from a clean prompt. It cannot be switched off.
- Punctuation is the main prosody control, and the owner recommends restricting it. For Chinese in particular it advises English punctuation and, preferably, only commas and full stops.

## Prompt structure

<rules id="structure">

- Prefix every turn with its role identifier followed by a colon: `Speaker 1:`, `Speaker 2:`. Keep the numbering consistent, because the label is what binds a turn to its voice.
- Give each speaker its own voice prompt, and keep the pairing stable across the whole script.
- Write turns in the order they should be heard. The model is reading a conversation, not assembling independent clips.
- Do not write stage directions, emotion notes or bracketed tags. There is no notation to consume them and they will be read out.
- Punctuate sparingly and conventionally. Commas and full stops carry the phrasing; exotic punctuation is a documented source of instability, especially in Chinese.
- Keep one language per script. English and Chinese are the trained pair, and mixing beyond that is where the model is documented to become unpredictable.
- If speech comes out too fast, split that speaker's long turn into several consecutive turns with the same label. This is the owner's own remedy and it is a formatting fix rather than a settings one.

</rules>

<template id="general">

Speaker 1: {first turn, punctuated plainly}

Speaker 2: {reply}

Speaker 1: {next turn; split a long one into consecutive same-label turns if it rushes}

Speaker 2: {closing turn}

</template>

<example use_case="two-speaker conversation">

```text
Speaker 1: So the archive finally got back to us this morning.

Speaker 2: And? Don't do the pause thing, just tell me.

Speaker 1: They found the second ledger. It was catalogued under the wrong year, which is why nobody had seen it since the seventies.
```

*Why: labels are consistent and numbered from one, each turn is a complete conversational move, and there is no direction anywhere. The delivery of "don't do the pause thing" comes from the words and the punctuation, because there is nowhere else to put it.*

</example>

<example use_case="pacing fix by splitting a turn">

```text
Speaker 1: I went back through the whole shipping register.

Speaker 1: Every entry, both columns, all the way to the end of the year.

Speaker 1: It took four days and I would do it again.
```

*Why: the owner's documented remedy for speech that runs too fast. One long paragraph becomes three consecutive turns under the same label, which gives the model natural breaks without inventing any notation to request them.*

</example>

## Voices

<rules id="voices">

- One voice prompt per role, bound by the role identifier. The report treats the voice features and the text as one interleaved sequence, so the binding is structural rather than a lookup.
- Keep a voice stable for the whole script. Changing the prompt for a role mid-conversation breaks the speaker consistency that is the model's main claim.
- A voice prompt containing background music makes background music in the output more likely. Choose clean prompts unless you want that.
- The realtime model does not take arbitrary voice prompts. Its speakers are embedded and selected by name, which the owner states is a deliberate measure against deepfake risk rather than an oversight.
- Cross-lingual use is a capability of the larger tier rather than of the line. The report attributes better cross-lingual transfer to scaling, and the released 1.5B is the smaller model.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- No negative field, and no direction channel to negate.
- Background music cannot be excluded. The owner states it is spontaneous and content-aware, so the levers are an instrumental-free voice prompt and avoiding introductory phrasing, not an instruction.
- An unwanted delivery is a voice-prompt problem. Change the prompt for that role rather than rewriting the line.
- Do not write exclusions into the script. Everything that is not a speaker label is spoken.
- Unwanted pace is fixed by splitting turns, not by asking for a slower reading.

</rules>

## Pitfalls and anti-patterns

- Expecting to run the 1.5B from the repository: the inference code was removed in September 2025 and the model card's installation link points at the gap it left.
- Confusing the two 7B models: `VibeVoice-Large` is unreleased TTS, `VibeVoice-ASR-7B` is released recognition.
- Sending the realtime model a multi-speaker script: it takes one speaker, and the labels are just text to it.
- Writing direction of any kind: there is no tag vocabulary and no instruction field, so a bracketed note or an adverbial aside is simply spoken.
- Inconsistent speaker labels: the identifier binds voice to turn, so renaming or renumbering mid-script produces a different speaker.
- Ornate punctuation, especially in Chinese: the owner recommends English punctuation and mostly commas and full stops, and says otherwise the output destabilises.
- Treating rushed speech as a settings problem: the documented fix is splitting a long turn into consecutive same-label turns.
- Expecting background music to be controllable: it is spontaneous, and the voice prompt influences it more than the script does.
- Prompting outside English and Chinese: the owner documents unpredictable output rather than an accented reading.
- Synthesising turns separately and concatenating: that discards the content-aware turn-taking the model exists to provide.
- Assuming a bracketed tag from another model works here: this scheme has no bracket notation at all.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (Microsoft): the [technical report](https://arxiv.org/abs/2508.19205), which is the source of the labelled-script input representation, the speech-to-text token ratio, the tokenizer frame rate and the scaling claims, and which remains the only owner surface still documenting the multi-speaker format; the [repository](https://github.com/microsoft/VibeVoice) and its [TTS documentation](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-tts.md) for the withdrawal notice, the model table, the punctuation and chunking remedies and the background-music behaviour; the [realtime model documentation](https://github.com/microsoft/VibeVoice/blob/main/docs/vibevoice-realtime-0.5b.md) for the single-speaker and embedded-voice constraints and their stated rationale; the [model card](https://huggingface.co/microsoft/VibeVoice-1.5B) for the tier table, the language pair and the responsible-use terms.

Coverage note: this guide had to be sourced unusually. The repository's usage section and its multi-speaker example scripts were removed on 2025-09-05 and the git history is truncated at that commit, so no earlier revision is retrievable; the model card's Installation section points at a README section that no longer exists; and the Hugging Face repository holds only weights. The labelled-script format is therefore taken from the technical report, which this project treats as an owner surface alongside the repository and the model card, rather than from any community fork. Nothing here comes from a fork or a mirror. The result is that the format is documented and the tooling to use it is not, which is stated plainly in the availability section rather than left for a reader to discover.

Last verified: 2026-08-29.
