---
guide: "Gemini TTS"
prompt_scheme: "gemini-tts"
models:
  - { id: "gemini-3.1-flash-tts-preview", access: "closed-weights", tier: "flagship", caps: [text-to-speech, multi-speaker, audio-tags, style-control, accent-control], best_for: "directed performance rather than plain narration. A language model drives the delivery, so it takes a scene, a persona and directorial notes as context and reads the transcript in character" }
capabilities: [text-to-speech, multi-speaker, audio-tags, style-control, accent-control]
prompt:
  languages: ["en", "multilingual"]
  script: "the transcript is one element of a larger prompt rather than the whole of it. Everything above it is direction and is never spoken, which is what makes this the most permissive speech scheme here"
  direction_syntax: "two layers. A structured context prompt in markdown headings carries the Audio Profile, Scene, Director's Notes and Sample Context; inline square-bracket audio tags such as [whispers] or [very slow] steer a specific span of the transcript"
  audio_tags: "an OPEN vocabulary, not a fixed list. Emotions, pace, and free inventions like [like dracula] all work, and the owner explicitly recommends experimenting. Write tags in English even when the transcript is not"
  voices: "one of thirty named voices, chosen to complement the direction rather than to contradict it; a breathy voice reinforces a tired note where a bright one fights it"
  length_strategy: "direct only what matters. The owner warns that over-specifying limits the model's creativity and can make the performance worse, so a short set of load-bearing notes beats an exhaustive rulebook"
  auto_expand_behavior: "none automatically. The owner suggests handing a blank outline of the prompt structure to a Gemini text model and having it draft the character, which is an explicit step rather than something the TTS model does"
  negatives: "no negative field. Direction is positive by construction: describe the performance you want and cast a voice that already leans that way"
sources:
  official: ["https://ai.google.dev/gemini-api/docs/speech-generation", "https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# Gemini TTS: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers Gemini TTS, Google's native audio text-to-speech model. Google's image and video models are separate schemes with their own guides; nothing transfers.
- THE TRANSCRIPT IS ONE PART OF THE PROMPT, not the whole of it. Everything written above it is direction and is not spoken. This is the opposite of most speech models here, where any stray instruction gets read aloud.
- The model is a language model that knows how to say things, not only what to say. Direct it the way you would direct an actor: give it a character, a place, and notes.
- Structure the direction with markdown headings. The owner's own prompts use headed sections, and that shape is part of the format.
- Audio tags are an OPEN vocabulary. There is no fixed list, invented tags work, and the owner recommends experimenting.
- Do not over-direct. The owner states explicitly that too many strict rules limit the model and can make the performance worse.
- Write audio tags in English even when the transcript is in another language.

</rules>

## Model names and aliases

Google ships every generative-media model under two names, and the nickname carries less information than the official name. Prefer the Gemini name and translate the nickname on sight.

| Gemini name (preferred) | Gemini API model ID | Nickname | Line | Role |
| --- | --- | --- | --- | --- |
| Gemini 3.1 Flash TTS | `gemini-3.1-flash-tts-preview` | none | Flash | Native audio text-to-speech; single and multi-speaker, directed by context prompt and audio tags |
| Gemini 3 Pro Image | `gemini-3-pro-image` | Nano Banana Pro | Pro | Image generation; a different prompt scheme with its own guide |
| Gemini 3.1 Flash Image | `gemini-3.1-flash-image` | Nano Banana 2 | Flash | Image generation; a different prompt scheme with its own guide |
| Gemini Omni Flash | `gemini-omni-flash-preview` | none | Omni | Video output with native audio; a different prompt scheme with its own guide |

<rules id="naming">

- Translate the nickname to the Gemini name before deciding anything. The Gemini name states the generation and the tier separately; the nickname collapses them and drops one.
- The TTS model has no nickname, so a Nano Banana name never refers to it. Those are image models.
- Cloud and Vertex surfaces append `-preview` to the same models. Same weights, different surface. The TTS model carries `-preview` in its base id already.
- Hosts invent tier labels that do not exist upstream. Names like Ultra or Multi on a hosted variant describe that host's packaging, not a Google model, and they change nothing about how the prompt is written.
- Gemini TTS, the Gemini image models and Gemini Omni are three different prompt schemes with three separate guides. Check which one you are in before applying a rule from memory.
- Imagen, Veo and Chirp are separate Google models on separate prompt schemes, and none belongs to this guide.

</rules>

## TL;DR

<template id="quickstart">

Say in {a manner}: "{the words to be spoken}"

</template>

For anything beyond one line, use the full structure below instead.

## How the model reads prompts

- Direction and transcript are separate by position, not by syntax. Everything before the transcript section is treated as instruction, so a note about pacing is never spoken.
- The model performs rather than reads. It infers delivery from the character, the place and the situation you describe, which is why a scene does real work even though nothing in it is spoken.
- Alignment matters. The owner recommends that the transcript's topic and writing style match the direction, so that who is speaking, what is said and how it is said agree. A formal script under a manic-DJ profile fights itself.
- Over-specification is a documented failure mode. Too many strict rules constrain the model and can produce a worse performance than fewer, better-chosen notes.
- The voice is part of the direction. Choosing a voice whose natural character already leans toward the note reinforces it; choosing one that leans away makes the model fight itself.
- Audio tags act on a span. A tag at the start of a line colours the whole line; tags placed mid-transcript switch delivery from that point.
- Tag vocabulary is open-ended and unlisted. The owner gives common examples but states there is no exhaustive list of what does and does not work.

## Prompt structure

The owner's format is six elements, written as markdown-headed sections in one prompt.

<rules id="structure">

- AUDIO PROFILE: name the character and give a role or archetype. Naming grounds the performance, and the name should be reused in the scene and context sections.
- SCENE: where this is happening and what it feels like. Physical details and situation, described as if writing a stage direction.
- DIRECTOR'S NOTES: the performance guidance. Style, pacing and accent are the usual three, but the model is not limited to them. This is the section to keep if you keep only one.
- SAMPLE CONTEXT: a sentence on what this voice is typically used for, so the performer enters the scene already oriented.
- TRANSCRIPT: the words to be spoken, and nothing else.
- AUDIO TAGS: inline square-bracket modifiers inside the transcript, for moments the notes cannot reach.
- Define only what matters. Leave out sections that carry nothing for this performance rather than filling them.
- Be descriptive rather than adjectival in the style note. The owner's own contrast is that "infectious enthusiasm, the listener should feel part of a massive community event" outperforms "energetic and enthusiastic".

</rules>

<template id="general">

# AUDIO PROFILE: {Character name}
## "{Archetype in a few words}"

## THE SCENE: {Place}
{Two or three sentences on the physical environment, what the character is doing, and the emotional temperature of the room.}

### DIRECTOR'S NOTES
Style: {descriptive, not adjectival; what the listener should feel}
Pace: {rate and cadence}
Accent: {specific region rather than a country}

### SAMPLE CONTEXT
{One sentence on what this voice is for.}

#### TRANSCRIPT
{The words to be spoken, with [tags] where a specific moment needs them.}

</template>

<example use_case="directed single-speaker performance">

```text
# AUDIO PROFILE: Maren H.
## "The Late-Night Archivist"

## THE SCENE: The Basement Stacks
It is past midnight in a university library annexe, three floors below ground. The air is dry and smells of old paper and warm dust. Maren is alone at a metal desk with one lamp on, turning the pages of a water-damaged ledger she has been trying to date for a week. She has just found the entry she was looking for.

### DIRECTOR'S NOTES
Style: Hushed and close, as though the listener is leaning in over the same page. Delight held under the surface rather than announced.
Pace: Unhurried, with real pauses where she is reading ahead before she speaks.
Accent: Educated Edinburgh, lightly worn.

### SAMPLE CONTEXT
Maren narrates archival documentaries and museum audio guides where the pleasure is in discovery rather than drama.

#### TRANSCRIPT
[whispers] Here. Third column, halfway down. The clerk has written the date twice, and the second time he has corrected himself.
[quietly delighted] Which means the shipment did not leave in the spring at all. It left in the autumn, and everything we thought we knew about that winter is wrong.
```

*Why: the scene is entirely unspoken and does most of the work; nothing in it appears in the transcript. The accent names a city rather than a country, the style note says what the listener should feel rather than listing adjectives, and the two tags mark a shift the notes could not place precisely.*

</example>

<example use_case="one-line style prefix">

```text
Say in a spooky whisper: "By the pricking of my thumbs... Something wicked this way comes"
```

*Why: the owner's own minimal form. For a single line the full structure is overkill, and a natural-language prefix plus the quoted text is enough.*

</example>

## Audio tags

<rules id="tags">

- Tags are square-bracket modifiers written inline in the transcript, such as `[whispers]`, `[laughs]`, `[sighs]`, `[gasp]` or `[cough]`.
- The vocabulary is open. Commonly used ones include amazed, crying, curious, excited, giggles, mischievously, panicked, sarcastic, serious, shouting, tired, trembling and whispers, but there is no exhaustive list and invention is encouraged.
- A tag at the start of a line sets the delivery for that line. Tags placed mid-transcript switch delivery from that point, so one line can move from whisper to shout and back.
- Tags cover pace as well as emotion: `[very fast]`, `[very slow]`.
- Tags can combine a manner with a pace in one bracket, as in `[sarcastically, one painfully slow word at a time]`.
- Similes work. `[like a cartoon dog]` and `[like dracula]` are the owner's own examples of how far the vocabulary stretches.
- Write tags in English even when the transcript is not. This is the owner's explicit recommendation.
- Use tags for moments and the Director's Notes for the whole performance. A tag repeated on every line is a note that belonged in the notes.

</rules>

<example use_case="delivery shifting within one line">

```text
[whispers] Hey there, I'm a new text to speech model, [shouting] and I can say things in many different ways. [whispers] How can I help you today
```

*Why: the owner's own example of span control. Each tag takes effect from where it sits, so a single sentence changes register twice without any of the tags being spoken.*

</example>

## Multi-speaker

<rules id="multispeaker">

- Label each line with a speaker name and give the model the transcript turn by turn.
- Direct the speakers individually in a line above the transcript, naming each one and the manner it should take.
- Keep speaker labels consistent. The label is how a turn is bound to a voice and a direction, so a renamed speaker mid-script is a new speaker.
- Cast contrasting voices for contrasting directions. The owner's example pairs a breathy voice with a tired note and an upbeat voice with an excited one, so the casting reinforces the direction rather than working against it.
- The full structured format extends to dialogue: give each speaker its own profile and notes, then a single transcript with labelled turns.

</rules>

<example use_case="two speakers with individual direction">

```text
Make Speaker1 sound tired and bored, and Speaker2 sound excited and happy:

Speaker1: So... what's on the agenda today?
Speaker2: You're never going to guess!
```

*Why: the owner's own example. One direction line covers both speakers, each turn is bound by its label, and the contrast is carried by the direction rather than by punctuation.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- No negative field, and no need for one. Direction is positive by construction, since you are describing a performance rather than filtering an output.
- An unwanted quality usually means a miscast voice. Change the voice before rewriting the notes.
- Where a note is being ignored, make it more specific rather than more forceful. "Do not rush" is weaker than a pacing note describing where the pauses fall.
- Cutting a note can help. Because over-specification degrades the performance, removing a competing instruction is a legitimate fix.
- Never write an exclusion into the transcript. It is the spoken text.

</rules>

## Pitfalls and anti-patterns

- Over-directing: the owner warns that too many strict rules limit the model and can make the result worse. This is the failure most people walk into, because more direction feels safer.
- Adjective-stacking the style note: "energetic and enthusiastic" underperforms a sentence describing what the listener should feel.
- Direction and transcript pulling apart: a formal script under a chaotic-DJ profile fights itself. Match the writing style to the direction.
- Naming a country as an accent: "British" spans more than the model can act on. Name a city or region.
- Repeating a tag on every line: that is a whole-performance note, and it belongs in the Director's Notes.
- Writing tags in the transcript's language: use English tags even for a non-English transcript.
- Assuming a fixed tag list: there is none, and treating the common examples as exhaustive leaves most of the control unused.
- Casting against the direction: a bright voice told to sound exhausted fights itself. Pick a voice that already leans the right way.
- Renaming a speaker mid-script: the label is the binding, so an inconsistent label is a new speaker.
- Carrying a tag vocabulary across vendors: bracketed tags are model-specific. What works here is not what works on another model, and several models here read an unrecognised bracket aloud.
- Applying an image-model rule from a Gemini image guide: three Gemini schemes, three guides.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (Google): the [speech generation documentation](https://ai.google.dev/gemini-api/docs/speech-generation), whose prompting guide section is the source of the six prompt elements, the directorial framing, the over-specification warning, the audio tag behaviour and vocabulary, the English-tags recommendation, the multi-speaker form and every verbatim example here; the [model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-tts-preview).

Coverage note: the model page itself renders client-side and returned only navigation, so nothing is sourced from it; the speech generation page is server-rendered and carries the full prompting guide. The Model names and aliases section is repeated across all Gemini guides in this set on purpose, because guides load independently and each has to stand alone.

Last verified: 2026-08-29.
