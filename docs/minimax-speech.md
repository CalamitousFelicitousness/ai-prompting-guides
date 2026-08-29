---
guide: "MiniMax Speech"
prompt_scheme: "minimax-speech"
models:
  - { id: "speech-2.8-hd", access: "closed-weights", tier: "flagship", caps: [text-to-speech, interjections, voice-clone, voice-design, pronunciation-override, emotion-control], best_for: "the highest audio quality and the only tier alongside 2.8-turbo that performs interjection tags. Note that it dropped the whispered delivery its 2.6 predecessor supports" }
  - { id: "speech-2.8-turbo", access: "closed-weights", tier: "distilled", caps: [text-to-speech, interjections, voice-clone, voice-design, pronunciation-override, emotion-control], best_for: "the fast tier of 2.8, with the same interjection vocabulary and the same missing whispered delivery" }
  - { id: "speech-2.6-hd", access: "closed-weights", tier: "std", caps: [text-to-speech, voice-clone, voice-design, pronunciation-override, emotion-control], best_for: "the previous generation, and the tier to fall back to when you need a whispered or deliberately fluent delivery, which 2.8 cannot produce. No interjection tags" }
  - { id: "speech-2.6-turbo", access: "closed-weights", tier: "distilled", caps: [text-to-speech, voice-clone, voice-design, pronunciation-override, emotion-control], best_for: "the fast tier of 2.6, and the other half of the whispered-delivery fallback" }
  - { id: "speech-02-hd", access: "closed-weights", tier: "legacy", caps: [text-to-speech, voice-clone, pronunciation-override, emotion-control], best_for: "superseded. Takes the base emotion set but neither interjections nor the fluent and whispered deliveries" }
  - { id: "speech-02-turbo", access: "closed-weights", tier: "legacy", caps: [text-to-speech, voice-clone, pronunciation-override, emotion-control], best_for: "superseded fast tier" }
  - { id: "speech-01-hd", access: "closed-weights", tier: "legacy", caps: [text-to-speech, voice-clone, pronunciation-override, emotion-control], best_for: "the oldest tier still accepting the emotion set" }
  - { id: "speech-01-turbo", access: "closed-weights", tier: "legacy", caps: [text-to-speech, voice-clone, pronunciation-override, emotion-control], best_for: "the oldest fast tier" }
capabilities: [text-to-speech, interjections, voice-clone, voice-design, pronunciation-override, emotion-control]
prompt:
  languages: ["en", "zh", "yue", "ja", "ko", "more"]
  script: "the prompt IS the words to be spoken, verbatim. Everything else is either inline notation inside that text or a separate control, so there is no place to write stage directions in prose: an unrecognised instruction gets read aloud"
  direction_syntax: "three inline forms, all embedded in the script. Pauses are <#x#> with x in seconds. Pronunciation overrides go in half-width parentheses as Pinyin with a tone digit, IPA, or Jyutping with a tone digit. Interjections are bracketed words in half-width parentheses such as (laughs) or (sighs), and exist only on the 2.8 tiers"
  voices: "cast from three sources: a system voice, a voice cloned from a recording, or a voice designed from a text description of how it should sound. The voice carries identity and baseline delivery; the script carries the performance"
  length_strategy: "write the script as it should be read, with paragraph breaks as real newlines. Length is a delivery decision rather than a quality one, and long scripts are handled by streaming rather than by shortening"
  auto_expand_behavior: "none. Nothing rewrites the script, which is what makes stray direction dangerous: text that is not recognised notation is simply spoken"
  negatives: "no negative field and no use for one. The script is read literally, so an unwanted delivery is fixed by changing the voice, the emotion setting, or the words themselves"
sources:
  official: ["https://platform.minimax.io/docs/guides/speech-t2a-websocket", "https://platform.minimax.io/docs/api-reference/speech-t2a-http", "https://platform.minimax.io/docs/guides/speech-voice-clone", "https://platform.minimax.io/docs/api-reference/voice-design-design", "https://platform.minimax.io/docs/release-notes/models"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# MiniMax Speech: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the MiniMax Speech text-to-speech line (2.8, 2.6, and the superseded 02 and 01 tiers). They share one scheme; what differs between them is which notation and which deliveries they support.
- MiniMax ships three separate guides. This one is speech. Music is a different scheme with a different grammar, and MiniMax H3 is video. Nothing transfers between them.
- THE PROMPT IS THE SCRIPT. What you write is what gets spoken, word for word. This inverts the usual rule: you are not describing a result, you are supplying it.
- Consequently there is nowhere to put a stage direction. Anything that is not recognised notation is read aloud, so "say this sadly" becomes four spoken words.
- Direction lives in three places instead: inline notation inside the script, the choice of voice, and a separate emotion setting.
- Write the script in the language it should be spoken. This is not a prompt to be translated into English.

</rules>

## TL;DR

<template id="quickstart">

{First sentence of the script.}<#0.5#>{Next sentence, with the pause sized to the beat you want.}

{New paragraph as a real newline.} {Any word needing a fixed pronunciation is followed by its phonetic form in parentheses.} {On a 2.8 tier, an interjection such as (sighs) can sit between sentences.}

</template>

## Models and when to use which

The generations are not a simple ladder: the newest tier gained a capability and lost one.

- `speech-2.8-hd` and `speech-2.8-turbo`: the current line, and the only tiers that perform interjection tags. HD is the quality option, turbo the fast one.
- `speech-2.6-hd` and `speech-2.6-turbo`: the previous line. They cannot do interjections, but they are the only tiers that support a whispered delivery and a deliberately fluent one. If a script needs whispering, 2.8 cannot do it and 2.6 is the answer.
- `speech-02` and `speech-01` tiers: superseded. They take the base emotion set and the pronunciation notation, but neither interjections nor the extended deliveries.
- The practical consequence: check which delivery a script needs before picking a tier, because the newest model is not a superset of the one before it.

## How the model reads prompts

- The script is read literally. There is no rewriting stage, no expansion, and no interpretation of intent, so anything you did not mean to be spoken must not be in the text.
- Notation is recognised by shape, not by meaning. Three forms are parsed out of the script; everything else is speech.
- Paragraph breaks are real newlines and they affect phrasing. Use them where you want the reader to take a breath and reset.
- Punctuation does most of the prosody. The model reads commas, full stops, question marks and ellipses as timing and intonation, so punctuating carefully is the cheapest control available.
- Emotion is chosen automatically from the text unless overridden. The owner recommends manual specification only when explicitly needed, which means writing emotionally unambiguous text usually beats forcing a setting.
- The voice carries identity and default character; the script carries the performance. Getting a delivery wrong is often a casting problem rather than a wording one.
- Language is set by the script, with a separate hint available for disambiguation. That hint matters most where a script could plausibly be read in more than one language or regional variety, Cantonese against Mandarin being the standard case.

## Prompt structure

<rules id="structure">

- Write the script exactly as it should be heard, including contractions, filler words and sentence fragments, because those are what make delivery sound spoken rather than read.
- Punctuate for the ear, not for the page. A comma is a short beat and a full stop is a longer one; a sentence that looks over-punctuated on paper often reads correctly aloud.
- Break paragraphs with real newlines wherever the delivery should reset.
- Do not write stage directions, speaker labels, or bracketed notes that are not recognised notation. All of them get spoken.
- Keep one voice per request. There is no speaker-turn syntax here, so a two-person dialogue is two requests with two voices, assembled afterwards.
- Spell out anything whose reading is ambiguous, or pin it with the pronunciation notation below. Numbers, dates, initialisms and units are the usual offenders.

</rules>

<template id="general">

{Opening line, punctuated as it should be spoken.}<#0.4#>{Follow-up clause after a deliberate beat.}

{Second paragraph, starting after a real newline.} {Ambiguous term}({phonetic form}) {continues the sentence.}

</template>

## Inline notation

Three forms are parsed out of the script. Everything else is spoken.

<rules id="notation">

- PAUSE: `<#x#>` inserts a silence of x seconds, written to at most two decimal places. It must sit between two speakable segments, and two pause markers cannot be placed back to back.
- PRONUNCIATION: put the phonetic form in half-width parentheses immediately after the word it fixes. Three notations are accepted: Mandarin Pinyin with a tone digit, IPA, and Cantonese Jyutping with a tone digit. Use it for homographs, polyphonic characters, loanwords and names.
- INTERJECTION: a small closed set of non-verbal sounds written in half-width parentheses, such as `(laughs)`, `(sighs)`, `(breath)`, `(gasps)`, `(coughs)`, `(chuckle)`, `(clear-throat)`, `(groans)`, `(pant)`, `(inhale)`, `(exhale)`, `(sniffs)`, `(snorts)`, `(burps)`, `(lip-smacking)`, `(humming)`, `(hissing)`, `(emm)` and `(sneezes)`. Available on the 2.8 tiers only.
- THE PARENTHESIS COLLISION IS REAL. Pronunciation overrides and interjections use the same delimiter, so what is inside the parentheses is the only thing distinguishing them. Keep parenthesised content to a recognised interjection or a valid phonetic string, and never use parentheses for an aside, a translation or a note.
- An unrecognised parenthesised word is the failure case to watch: it is neither an interjection nor a phonetic form, so it is read out as ordinary text.
- Interjections replace the words for the sound, they do not accompany them. Write `(laughs)`, not `he laughs (laughs)`.

</rules>

<example use_case="narration with pacing and a non-verbal beat">

```text
So there I was, three in the morning, staring at a server that had decided it no longer believed in DNS.<#0.8#>(sighs)

I tried the obvious thing first. Turned it off. Turned it on again.<#0.35#>Nothing.

By four I had a theory, and by five I had a theory and a headache.
```

*Why: pauses are sized differently on purpose, a long one to land the joke and a short one for the beat before "Nothing". The interjection sits on its own rather than being described in words, and the paragraph breaks give the delivery somewhere to reset.*

</example>

<example use_case="pronunciation control across languages">

```text
The word live is pronounced (lɪv) as a verb and (laɪv) as an adjective.

This is (he2)平, not (huo4)面.

去街市買啲(sung3)。
```

*Why: the owner's own three examples, one per notation. Each phonetic form sits immediately after the token it fixes, which is what binds them together; placed anywhere else it would be read as text.*

</example>

## Voices

<rules id="voices">

- Three sources of voice: the system voice library, a voice cloned from a reference recording, and a voice designed from a text description.
- Voice design takes two inputs: a description of how the voice should sound, and a sample line used to preview it. Write the description as a person plus a manner, not as an adjective list.
- Make the preview line exercise what you described. A voice described as fast-paced and high-energy should be previewed on a line that is actually fast-paced and high-energy, or the preview tells you nothing.
- The voice sets the baseline; the emotion control and the script move it from there. Casting an unsuitable voice and then fighting it with emotion settings is the wrong order.
- Cloned voices are transient unless used. A cloned voice that goes unused is cleaned up, so treat a clone as something to re-create rather than a permanent asset.

</rules>

<example use_case="voice design description and its preview line">

```text
Excited and enthusiastic male product reviewer (e.g., tech vlogger), fast-paced, high energy, and persuasive.
```

*Why: the owner's own example. It names a role first, which carries more than any adjective list would, then adds three delivery attributes. Its paired preview line is written in that same register rather than being neutral text.*

</example>

## Emotion and delivery

<rules id="emotion">

- A separate emotion control offers a fixed set: happy, sad, angry, fearful, disgusted, surprised, calm, plus fluent and whisper on the tiers that have them.
- It defaults to automatic. The model picks from the text, and the owner recommends overriding only when explicitly needed, so the first move is to make the script's emotional content unambiguous.
- `whisper` and `fluent` are 2.6-only. The 2.8 tiers do not support whispering, which is the single most likely reason to deliberately use an older model here.
- Emotion is set per request, not per sentence. A script that needs to move between emotional states has to be split into separate requests and assembled, the same as a multi-speaker dialogue.
- Where an emotion cannot be set, write it. Word choice, sentence length and punctuation carry more emotional signal than the control does, and they work on every tier.

</rules>

## Pitfalls and anti-patterns

- Writing stage directions: "excitedly", "he pauses", or a bracketed note all get read aloud. There is no prose direction channel.
- Using parentheses for an aside: they are reserved for pronunciation and interjections, and anything else in them is spoken.
- Writing an interjection alongside its description: `(laughs)` replaces "he laughs", it does not accompany it.
- Expecting interjections on a 2.6 or older tier: they are 2.8-only and are otherwise spoken as words.
- Expecting a whisper on 2.8: it was supported on 2.6 and is not on 2.8. The newest tier is not a superset.
- Stacking pause markers: two in a row are invalid. Use one marker with a longer value.
- Putting a pause at the very start or end: markers must sit between speakable segments.
- Placing a phonetic form away from its word: the binding is positional, so it has to sit immediately after the token it fixes.
- Writing a dialogue as one script: there is no speaker-turn syntax. Two voices means two requests.
- Changing emotion mid-script: the setting is per request. Split the script instead.
- Leaving ambiguous numbers and initialisms unspelled: they are a common source of a wrong reading, and pronunciation notation or plain spelling both fix it.
- Translating the script to English: unlike a prompt for an image model, the script's language IS the output language.
- Fighting a miscast voice with settings: change the voice first.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (MiniMax): the [synchronous text-to-speech guide](https://platform.minimax.io/docs/guides/speech-t2a-websocket) and the [text-to-speech API reference](https://platform.minimax.io/docs/api-reference/speech-t2a-http), whose script-field description is the source of the pause, pronunciation and interjection notation, the interjection vocabulary and the per-tier availability of each; the [emotion set and its per-model support](https://platform.minimax.io/docs/api-reference/speech-t2a-http); the [voice cloning guide](https://platform.minimax.io/docs/guides/speech-voice-clone); the [voice design reference](https://platform.minimax.io/docs/api-reference/voice-design-design) for the description-plus-preview pattern and its example; the [model release notes](https://platform.minimax.io/docs/release-notes/models) for the tier line-up.

Coverage note: MiniMax's documentation site renders client-side and returns an empty shell to an ordinary fetch, but every page is also served as markdown at the same path with a `.md` suffix, and a complete page index is published at `/docs/llms.txt`. Everything here comes from those markdown twins. The capability regression between 2.6 and 2.8 is stated only in a single sentence at the end of the emotion field's description, and is recorded here because nothing in the release notes mentions it.

Last verified: 2026-08-29.
