---
guide: "Qwen TTS"
prompt_scheme: "qwen-tts"
models:
  - { id: "Qwen3-TTS-12Hz-1.7B-CustomVoice", access: "open-weights", tier: "std", caps: [text-to-speech, instruction-control, built-in-voices, streaming], best_for: "the built-in timbres with natural-language delivery direction on top. The default open checkpoint when you want a voice off the shelf and still want to direct it" }
  - { id: "Qwen3-TTS-12Hz-1.7B-VoiceDesign", access: "open-weights", tier: "std", caps: [text-to-speech, instruction-control, voice-design, streaming], best_for: "inventing a voice from a written description rather than choosing one. Takes prose, not an attribute list" }
  - { id: "Qwen3-TTS-12Hz-1.7B-Base", access: "open-weights", tier: "base", caps: [text-to-speech, voice-clone, streaming], best_for: "cloning from about three seconds of reference audio, and the checkpoint to fine-tune. No instruction control, so delivery comes from the reference alone" }
  - { id: "Qwen3-TTS-12Hz-0.6B-CustomVoice", access: "open-weights", tier: "budget", caps: [text-to-speech, built-in-voices, streaming], best_for: "the same built-in timbres at a smaller size. NO instruction control, which is the capability the 0.6B tier gives up" }
  - { id: "Qwen3-TTS-12Hz-0.6B-Base", access: "open-weights", tier: "budget", caps: [text-to-speech, voice-clone, streaming], best_for: "small-tier cloning and fine-tuning foundation. No instruction control" }
  - { id: "qwen-audio-3.0-tts-plus", access: "closed-weights", tier: "flagship", caps: [text-to-speech, instruction-control, built-in-voices, voice-clone, voice-design, inline-tags, streaming], best_for: "the hosted quality tier. Same instruction-driven scheme as the open line, plus inline emotion and sound tags embedded in the text" }
  - { id: "qwen-audio-3.0-tts-flash", access: "closed-weights", tier: "distilled", caps: [text-to-speech, instruction-control, built-in-voices, voice-clone, voice-design, inline-tags, streaming], best_for: "the hosted low-latency tier, same scheme" }
  - { id: "qwen3-tts-instruct-flash-realtime", access: "closed-weights", tier: "std", caps: [text-to-speech, instruction-control, built-in-voices, streaming], best_for: "the hosted streaming build of the open line WITH instruction control. Its plain sibling drops the instructions field, so the model id is what decides whether direction is available at all" }
  - { id: "qwen3-tts-flash-realtime", access: "closed-weights", tier: "distilled", caps: [text-to-speech, built-in-voices, streaming], best_for: "the hosted streaming build without instruction control; pick a voice and send text" }
capabilities: [text-to-speech, instruction-control, built-in-voices, voice-design, voice-clone, inline-tags, streaming]
prompt:
  languages: ["zh", "en", "ja", "ko", "de", "fr", "ru", "pt", "es", "it"]
  script: "the prompt is the text to be spoken. Delivery direction does NOT go in it; it goes in a separate instruction field, which is what keeps a direction from being read aloud"
  direction_syntax: "a natural-language instruction in its own field, written as prose. It directs delivery on the built-in-voice models and describes a whole persona on the voice-design model. Hosted tiers additionally accept emotion and sound tags embedded inline in the text"
  voices: "three routes: one of nine built-in timbres spanning gender, age, language and dialect; a voice designed from a prose description; or a clone from roughly three seconds of reference audio. Each built-in timbre has a native language that is its best-quality pairing, though any of them can speak any supported language"
  length_strategy: "no documented length strategy for the script. Effort belongs in the instruction, where a persona sentence carries more than a single adjective"
  auto_expand_behavior: "off by default and available on the hosted tiers, where an optimizer will rewrite a terse instruction before it is applied. The script itself is never rewritten"
  negatives: "no negative field. An unwanted delivery is corrected by rewriting the instruction positively, or by changing the voice"
sources:
  official: ["https://github.com/QwenLM/Qwen3-TTS", "https://huggingface.co/collections/Qwen/qwen3-tts", "https://www.alibabacloud.com/help/en/model-studio/text-to-speech"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# Qwen TTS: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers both of Alibaba's text-to-speech lines: the openly published Qwen3-TTS checkpoints and the hosted Qwen-Audio-3.0-TTS and Qwen3-TTS realtime tiers. They share one scheme, so a prompt written for one transfers.
- Alibaba ships several guides. This one is speech. Qwen-Image is image, Wan Image and Wan Video and HappyHorse are elsewhere; nothing transfers between them.
- TWO FIELDS, and the split is the whole point. The script is what gets spoken; the instruction is how it should be spoken. Because direction has its own field, it never risks being read aloud.
- The instruction is PROSE. Unlike models with a closed attribute vocabulary, this one wants a sentence describing a manner or a person.
- Instruction control is not universal across the family. The 0.6B checkpoints and one hosted realtime build do not have it, and on those the voice alone carries delivery.
- Write the script in the language it should be spoken. The instruction may be written in English or Chinese regardless.

</rules>

## TL;DR

<template id="quickstart">

Script: {the words to be spoken, in their own language}

Voice: {one of the built-in timbres, matched to the script's language where possible}

Instruction: {a sentence describing the manner, or the person speaking}

</template>

## Models and when to use which

Two published lines and one scheme. Pick on capability, not on wording.

- `Qwen3-TTS-12Hz-1.7B-CustomVoice`: built-in timbres plus instruction control. The default open choice.
- `Qwen3-TTS-12Hz-1.7B-VoiceDesign`: builds a voice from a written description instead of choosing one. Use it when the character does not exist yet.
- `Qwen3-TTS-12Hz-*-Base`: clones from a very short reference clip and is the fine-tuning foundation. No instruction control, so the reference carries the manner entirely.
- `Qwen3-TTS-12Hz-0.6B-CustomVoice`: the same timbres, smaller, and WITHOUT instruction control. This is the trap in the family: it looks like a cheaper version of the 1.7B and it silently lacks the direction field.
- Hosted `qwen-audio-3.0-tts-plus` and `-flash`: the quality and latency tiers of the newer hosted line, with the same instruction concept plus inline tags.
- Hosted `qwen3-tts-instruct-flash-realtime` versus `qwen3-tts-flash-realtime`: the same model with and without instruction control, distinguished only by the id. Getting the plain one and wondering why direction does nothing is the predictable mistake.
- The two lines are separate releases with adjacent names. Qwen3-TTS is the open, downloadable series; Qwen-Audio-3.0-TTS is a hosted product that shipped later. Searching for open Qwen TTS weights and landing on the hosted one is easy to do.

## How the model reads prompts

- Two channels, cleanly separated. Nothing you write as direction can be spoken by accident, because direction is not in the script. This is the opposite arrangement to models that embed direction inline, and it is the main reason prompts here are easy to get right.
- The instruction is understood as language, not matched against a list. A sentence like "speak in a particularly angry tone" works, and so does a paragraph describing a person's age, vocal range and habits.
- Semantics feed delivery. The owner states the model adapts tone, rhythm and emotion from the meaning of the text as well as from the instruction, so a well-written script does part of the work before any direction is added.
- The voice sets the baseline. Each built-in timbre has a native language, and the owner recommends matching them for best quality even though any voice can speak any supported language.
- Instruction control is a model capability, not a request option. Where the checkpoint lacks it, the field is simply absent rather than weak.
- On hosted tiers, an optional optimizer rewrites a terse instruction before applying it. It is off unless enabled, and the script is never touched.

## Prompt structure

<rules id="structure">

- Put the words in the script and everything else in the instruction. Never write "say this angrily" inside the script.
- Write the instruction as a sentence, not a tag list. "Very happy." works; a persona sentence works better.
- Name the person when you want a voice rather than a mood. Age, vocal range, and a behavioural detail characterise more sharply than an emotion word.
- Match the voice to the script's language where you can, and expect a slight quality cost when you deliberately do not.
- Keep one voice per request. There is no speaker-turn syntax, so a dialogue is several requests assembled afterwards.
- Where the checkpoint has no instruction control, move the characterisation into the voice choice, or switch to a checkpoint that has it.

</rules>

<template id="general">

Script: {the sentence or passage to be spoken}
Voice: {built-in timbre, or a reference clip, or a design description}
Instruction: {manner in one sentence} or {persona: age, range, and a habit}

</template>

<example use_case="short delivery direction">

```text
Speak quickly with a rising intonation, suitable for introducing fashion products.
```

*Why: the owner's own hosted example. It gives a rate, a contour and a context, and the context is what makes it usable: "quickly" alone leaves the register open, while naming the situation settles it.*

</example>

<example use_case="persona description for voice design">

```text
Male, 17 years old, tenor range, gaining confidence - deeper breath support now, though vowels still tighten when nervous
```

*Why: the owner's own voice-design example, and the best demonstration of what prose buys over an attribute list. Age and range would fit a closed vocabulary; "vowels still tighten when nervous" would not, and it is the detail that makes the voice a character rather than a preset.*

</example>

<example use_case="instruction in Chinese">

```text
用特别愤怒的语气说
```

*Why: the owner's example, and a reminder that the instruction's language is independent of the script's. Written direction in Chinese can steer an English script and vice versa.*

</example>

## Voices

<rules id="voices">

- Nine built-in timbres span gender, age, language and dialect, including regional Chinese voices such as a Beijing and a Sichuan timbre. Each has a native language.
- Match voice to script language for the best result. Any voice can speak any supported language, but the pairing is a documented quality factor.
- Cloning needs only a few seconds of reference audio plus its transcript. A mode exists that skips the transcript by using the speaker embedding alone, at a stated cost to cloning quality.
- Design a voice with prose when none exists, then clone that result if you need it repeatedly. The owner documents this explicitly: synthesise a short clip with the design model, then build a reusable reference from it.
- That design-then-clone route is the answer to character consistency. A prose description re-interpreted per request drifts; a reference built once does not.

</rules>

## Inline tags on hosted tiers

<rules id="tags">

- The hosted tiers accept emotion and sound tags embedded directly in the text, in addition to the instruction field. The open checkpoints direct through the instruction alone.
- This makes the hosted surface a hybrid: out-of-band direction for the whole utterance, inline tags for a specific moment.
- Prefer the instruction for anything spanning the utterance, and reserve inline tags for a single point in the line.
- Do not assume a tag written for another vendor's model works here. Bracketed tag vocabularies are model-specific and do not transfer.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- No negative field. Nothing is subtracted, and there is nothing to write an exclusion against.
- State the instruction positively. "Calm and measured, with long pauses" gets what "not excited" will not.
- An unwanted voice quality is a casting problem first. Change the timbre or the reference before rewriting the instruction.
- On a checkpoint without instruction control there is nothing to negate at all; the voice is the only lever.
- Never write an exclusion into the script. It is the spoken text and it will be read aloud.

</rules>

## Pitfalls and anti-patterns

- Writing direction into the script: it gets spoken. Direction has its own field precisely so this cannot happen, and putting it in the wrong place defeats that.
- Reaching for the 0.6B CustomVoice expecting a cheaper 1.7B: it has the same timbres and no instruction control.
- Using the plain hosted realtime build and wondering why instructions do nothing: instruction control is a different model id, not a flag.
- Writing the instruction as an attribute list: this model wants prose. A comma-separated list of adjectives underuses it, and it is not a closed vocabulary that would reward one.
- Confusing the two lines: Qwen3-TTS is the open series and Qwen-Audio-3.0-TTS is the later hosted product. The names are adjacent and the access is not.
- Mismatching voice and script language by default: any voice speaks any language, but the native pairing is the documented quality choice.
- Expecting a dialogue from one request: there is no speaker-turn syntax here.
- Re-describing a character every request: prose is re-interpreted each time, so a recurring voice should be designed once and then cloned.
- Skipping the reference transcript by habit: the transcript-free mode is documented as lower quality, not equivalent.
- Assuming inline tags work on the open checkpoints: they are a hosted-tier feature, and on an open checkpoint a bracketed tag is just text.
- Expecting the optimizer to be on: instruction rewriting is opt-in and hosted-only.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (Alibaba): the [Qwen3-TTS repository](https://github.com/QwenLM/Qwen3-TTS) for the released checkpoint table, which capability each tier has, the three generation modes, the built-in timbre list with native languages, the design-then-clone workflow and the verbatim instruction examples; the [Model Studio speech synthesis documentation](https://www.alibabacloud.com/help/en/model-studio/text-to-speech) for the hosted tiers, the instruction-control feature on both hosted lines, the optional instruction optimizer, and the inline emotion and sound tags.

Coverage note: the open and hosted lines are merged into one guide because both are directed the same way, by a natural-language instruction alongside the script, which the Model Studio documentation confirms for the hosted tiers and the repository confirms for the open ones. Access alone is not a scheme split. What differs is coverage rather than grammar: the hosted tiers add inline tags and an instruction optimizer, and two open checkpoints plus one hosted build have no instruction field at all. The hosted line's own product page could not be read for this pass, since it renders client-side and returned nothing; the Model Studio speech synthesis page is server-rendered and carries the same material.

Last verified: 2026-08-29.
