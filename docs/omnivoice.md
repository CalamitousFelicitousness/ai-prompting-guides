---
guide: "OmniVoice"
prompt_scheme: "omnivoice"
models:
  - { id: "omnivoice", access: "open-weights", tier: "std", caps: [text-to-speech, voice-clone, voice-design, cross-lingual, pronunciation-override, non-verbal-tags], best_for: "zero-shot speech in over 600 languages, which is the widest coverage of any model in this set. Cloning is the stable path; voice design works but was trained on Chinese and English only" }
capabilities: [text-to-speech, voice-clone, voice-design, cross-lingual, pronunciation-override, non-verbal-tags]
prompt:
  languages: ["en", "zh", "yue", "600+"]
  script: "the prompt is the text to be spoken. Direction does not go in it; the voice comes from either a reference clip or an attribute string, and only three inline forms are parsed out of the script itself"
  direction_syntax: "voice design uses a CLOSED comma-separated attribute vocabulary in a separate field, one attribute per category, freely combined across categories. Inside the script, [laughter] marks a non-verbal, bracketed ARPAbet such as [B EY1 S] fixes a pronunciation, and pinyin tone markers do the same for Chinese"
  voices: "two routes and they behave differently. A reference clip clones a voice and is the mode the model was primarily trained on; an attribute string designs one from nothing and is less stable, especially outside Chinese and English"
  length_strategy: "write the script as it should be read. There is no documented length strategy, and text normalisation is applied automatically for numbers and symbols"
  auto_expand_behavior: "none for the script. The instruct string is normalised rather than expanded, and a reference transcript can be filled in automatically by speech recognition when omitted"
  negatives: "no negative field. An unwanted voice is a casting problem, fixed by changing the reference clip or the attribute string"
sources:
  official: ["https://github.com/k2-fsa/OmniVoice", "https://github.com/k2-fsa/OmniVoice/blob/main/docs/voice-design.md", "https://huggingface.co/k2-fsa/OmniVoice", "https://arxiv.org/abs/2604.00688"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# OmniVoice: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers OmniVoice from the k2-fsa team, a zero-shot text-to-speech model published under Apache 2.0 with a single released checkpoint.
- THE PROMPT IS THE SCRIPT. What you write is spoken. Direction is not written in prose anywhere; it lives in the voice you supply and in three inline notations.
- Voice comes from one of two places: a reference recording to clone, or a closed set of attributes to design from. These are different modes with different reliability, not two ways of saying the same thing.
- The design vocabulary is CLOSED and enumerable. This is unusual: most models here take free-form voice descriptions, and OmniVoice does not.
- Over 600 languages for cloning, but voice design was trained on Chinese and English only. Coverage is not uniform across the two modes.
- Write the script in the language it should be spoken. The instruct string may be written in English or Chinese either way.

</rules>

## TL;DR

<template id="quickstart">

Script: {the words to be spoken, in their own language}

Voice, one of:
  a reference clip of the voice to clone
  an attribute string: {gender}, {age}, {pitch}{, accent or dialect}

</template>

## Models and when to use which

One published checkpoint, so the choice is not which model but which mode.

- Voice cloning from a reference clip is the primary mode. The owner states the model was trained mainly on this task and that it is the most stable, so reach for it whenever a reference is available.
- Voice design from attributes needs no audio at all, which makes it the right choice for a character that does not exist yet. It is explicitly the weaker mode, and it degrades on low-resource languages because its training data was Chinese and English.
- A reference clip can be encoded once and reused. Where a character recurs across many lines, build the reference once and keep it rather than re-supplying the clip, which keeps the voice stable and avoids repeated work.

## How the model reads prompts

- The script is spoken literally. There is no rewriting and no interpretation of intent, so anything not meant to be heard must not be in the text.
- Three inline notations are parsed out of it, and everything else is speech.
- Text normalisation is automatic. Numbers and symbols are expanded before synthesis, with different machinery for Chinese and English than for other languages, so a written number generally does not need spelling out.
- The voice carries identity, accent and default manner. There is no emotion control and no style field beyond the design attributes, which makes casting the main lever.
- Cross-lingual cloning carries an accent. If the reference clip is in a different language from the script, the output speaks the script with the reference language's accent. That is sometimes exactly what you want and is otherwise a reason to match languages.
- A reference transcript helps but is optional. Supplying the words spoken in the reference clip improves the clone; omit it and speech recognition fills it in.

## Prompt structure

<rules id="structure">

- Write the script as it should be heard, punctuated for the ear.
- Do not write stage directions. There is no channel for them and no rewriting stage to strip them, so they are read aloud.
- Match the reference clip's language to the script unless you want an accent. This is the single most common source of an unexpected result.
- Give a reference transcript when you have one, and expect slightly weaker cloning when you do not.
- For a recurring character, build the voice once and reuse it rather than re-cloning per line, which keeps identity stable across a long piece.
- Choose the mode before writing anything: a clip if the voice exists, attributes if it does not.

</rules>

## Voice design attributes

The design field takes a comma-separated attribute string. Categories are exclusive within themselves and free to combine across.

<rules id="design">

- One attribute per category, any number of categories. Two pitches or two ages in one string is not a richer description, it is a malformed one.
- The categories are gender, age, pitch, style, English accent, and Chinese dialect.
- Gender is male or female. Age runs child, teenager, young adult, middle-aged, elderly. Pitch runs very low, low, moderate, high, very high.
- Style has exactly one value, whisper. There is no other style attribute, so any other manner has to come from a reference clip instead.
- An English accent only applies when the script is English, and a Chinese dialect only when the script is Chinese. Supplying the wrong pairing does nothing.
- Attributes may be written in English or Chinese, and the two may be mixed; the model detects and normalises the instruct language itself.
- Separators are forgiving. Half-width and full-width commas are both accepted and mismatches are corrected.
- Do not write prose here. This field is not a description of a person the way some other models accept; an adjective outside the vocabulary is not understood.

</rules>

<example use_case="designed voice from attributes">

```text
female, young adult, high pitch, british accent
```

*Why: the owner's own example, and one attribute from each of four categories. Every term is drawn from the closed vocabulary, which is what makes it work; "bubbly" or "posh" would not be understood however natural they sound.*

</example>

<example use_case="whispered elderly voice">

```text
male, elderly, low pitch, whisper
```

*Why: whisper is the only style value there is, so a hushed delivery has to be requested here rather than described in the script. Pairing it with a low pitch and an age does the rest of the characterisation.*

</example>

## Inline notation

Three forms are parsed out of the script. Everything else is spoken.

<rules id="notation">

- NON-VERBAL: `[laughter]` and similar bracketed markers place a non-speech sound in the line.
- PRONUNCIATION, ENGLISH: bracketed ARPAbet phonemes with stress digits fix a word's reading, written as `[B EY1 S]`.
- PRONUNCIATION, CHINESE: pinyin tone markers do the same job for Chinese characters.
- The notation survives text normalisation. Numbers and symbols around it are rewritten automatically, and these forms are preserved rather than mangled.
- Keep brackets for notation only. An unrecognised bracketed word is not a recognised marker and not valid ARPAbet, so it risks being read out.
- ARPAbet is per phoneme and space-separated, with the stress digit attached to the vowel. It is not a spelling hint.

</rules>

<example use_case="pronunciation and a non-verbal in one line">

```text
The word is spelled bass but pronounced [B EY1 S] when you mean the guitar. [laughter] Everyone gets that one wrong.
```

*Why: the phoneme string sits where the spoken word belongs rather than after it, because ARPAbet replaces the reading rather than annotating it. The non-verbal sits between sentences, where a real laugh would fall.*

</example>

## By use-case

- A character that already has a voice: clone from a clip, match the clip's language to the script, and supply the transcript.
- A character invented from nothing: design from attributes, and accept that Chinese or English will be more reliable than a low-resource language.
- A deliberate foreign accent: clone from a reference in the accent's language and write the script in the target language. This is the documented behaviour rather than a trick.
- A long piece with a recurring speaker: build the voice once and reuse the encoded reference across every line.
- A language outside Chinese and English: prefer cloning. Design coverage does not match the model's cloning coverage.

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field and nothing to exclude against. The script is read as written.
- An unwanted voice quality is a casting problem. Change the reference clip, or change an attribute in the design string.
- An unwanted accent usually means a language mismatch between reference and script rather than anything in the text.
- An unwanted reading of a word is fixed with the pronunciation notation, not by rephrasing around it.
- Do not write exclusions into the script. They will be spoken.

</rules>

## Pitfalls and anti-patterns

- Writing stage directions in the script: there is no direction channel, so they are read aloud.
- Writing prose into the design field: the vocabulary is closed, and an adjective outside it is not understood rather than approximated.
- Two attributes from one category: one pitch, one age, one gender. A second value in the same category is malformed, not more specific.
- Expecting an accent attribute to work on the wrong script language: English accents apply to English text and Chinese dialects to Chinese text.
- Expecting a style beyond whisper: there is exactly one style value. Any other manner has to come from a reference clip.
- Mismatching reference and script language by accident: the result speaks with the reference language's accent, which is a documented behaviour and surprises people who did not intend it.
- Assuming design coverage matches cloning coverage: cloning spans over 600 languages, design was trained on two.
- Treating design as the default: the owner states cloning is the mode the model was primarily trained on and the more stable one.
- Writing ARPAbet as a spelling hint: it is space-separated phonemes with a stress digit on the vowel, and it replaces the word's reading.
- Re-cloning the same character per line: encode the reference once and reuse it, or identity drifts across a long piece.
- Omitting the reference transcript when you have it: cloning quality is better with it.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (k2-fsa): the [OmniVoice repository](https://github.com/k2-fsa/OmniVoice) for the two voice modes, the cloning workflow, cross-lingual accent behaviour, automatic text normalisation and the inline control syntax; the [voice design reference](https://github.com/k2-fsa/OmniVoice/blob/main/docs/voice-design.md) for the closed attribute vocabulary, its per-category exclusivity, the accent and dialect language conditions, and the example strings; the [model card](https://huggingface.co/k2-fsa/OmniVoice); the [technical report](https://arxiv.org/abs/2604.00688).

Coverage note: there is a naming collision worth knowing about. This guide covers the k2-fsa research model; a commercial product at omnivoice.app shares the name and is unrelated, and it dominates search results for the term. Nothing here comes from that product. The owner's statement that voice design was trained on Chinese and English only, while cloning spans the full language set, is recorded prominently because the headline figure of 600-plus languages is easily read as applying to both modes.

Last verified: 2026-08-29.
