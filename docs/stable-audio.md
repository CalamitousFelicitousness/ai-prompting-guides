---
guide: "Stable Audio"
prompt_scheme: "stable-audio"
models:
  - { id: "stable-audio-3-large", access: "closed-weights", tier: "flagship", caps: [text-to-music, text-to-sfx, stems, audio-to-audio, audio-inpaint, audio-continue], best_for: "the owner's highest-quality tier and the only one it does not publish weights for. Same prompt grammar as medium; reach for it through an API when quality matters more than running locally" }
  - { id: "stable-audio-3-medium", access: "open-weights", tier: "std", caps: [text-to-music, text-to-sfx, stems, audio-to-audio, audio-inpaint, audio-continue], best_for: "the only open checkpoint that does music, stems and sound effects all three. The default choice on a GPU, and the one to use when a prompt mixes musical and non-musical material" }
  - { id: "stable-audio-3-small-music", access: "open-weights", tier: "budget", caps: [text-to-music, stems, audio-to-audio, audio-inpaint, audio-continue], best_for: "music and isolated instruments on CPU. The owner marks it as not covering sound effects at all, so a foley prompt belongs on a different checkpoint rather than this one" }
  - { id: "stable-audio-3-small-sfx", access: "open-weights", tier: "budget", caps: [text-to-sfx, audio-to-audio, audio-inpaint, audio-continue], best_for: "sound effects, one-shots and samples on CPU. The owner marks it as covering neither music nor stems, so it is a specialist rather than a smaller generalist" }
  - { id: "stable-audio-3-medium-base", access: "open-weights", tier: "base", caps: [text-to-music, text-to-sfx, stems, audio-to-audio, audio-inpaint, audio-continue], best_for: "the pre-trained checkpoint behind medium, published for fine-tuning. It needs far more sampling steps and real guidance to reach usable output, so it is the wrong default for generating and the right one for training on your own library" }
  - { id: "stable-audio-3-small-music-base", access: "open-weights", tier: "base", caps: [text-to-music, stems, audio-to-audio, audio-inpaint, audio-continue], best_for: "the fine-tuning foundation for small-music" }
  - { id: "stable-audio-3-small-sfx-base", access: "open-weights", tier: "base", caps: [text-to-sfx, audio-to-audio, audio-inpaint, audio-continue], best_for: "the fine-tuning foundation for small-sfx" }
  - { id: "stable-audio-open-1.0", access: "open-weights", tier: "legacy", caps: [text-to-music, text-to-sfx], best_for: "the superseded 2024 line. Still widely deployed, but it predates the licensed music corpus and the owner states it is better at sound effects and field recordings than at music" }
  - { id: "stable-audio-open-small", access: "open-weights", tier: "legacy", caps: [text-to-music, text-to-sfx], best_for: "the superseded small model. Its diffusion transformer was trained on the sound-effects corpus alone, so its weakness at music is structural rather than a matter of quality" }
capabilities: [text-to-music, text-to-sfx, stems, audio-to-audio, audio-inpaint, audio-continue]
prompt:
  languages: ["en"]
  metadata_tags: "the model reads Key: Value tags inherited from its training metadata, written inline at the front of the prompt: TrackType (Music, Instrument or SFX), VocalType, Genre (repeatable), Instruments and Format. They steer the model toward a region of the training data rather than describing sound, so they are a complement to description, not a replacement for it"
  length_strategy: "one flowing descriptive paragraph, several sentences long, naming instruments individually and saying what each one does. The owner's own examples run 40 to 80 words; short prompts underperform and the model has no length penalty worth worrying about"
  auto_expand_behavior: "none by default. The reference UI offers an optional prompt assistant that drafts or expands a prompt before generation, but nothing rewrites your text unless you ask, so a terse prompt is taken as written and simply underspecifies"
  negatives: "a real negative-prompt field exists and takes plain descriptions of qualities to avoid. It only bites in proportion to guidance, and the shipped default guidance is low enough that both the positive prompt and the negative are held loosely; raise guidance when either needs to be enforced"
sources:
  official: ["https://github.com/Stability-AI/stable-audio-3", "https://github.com/Stability-AI/stable-audio-3/blob/main/docs/guides/prompting.md", "https://huggingface.co/stabilityai/stable-audio-3-medium", "https://huggingface.co/stabilityai/stable-audio-open-1.0", "https://stability.ai/stable-audio", "https://arxiv.org/abs/2605.17991"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# Stable Audio: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the Stable Audio 3 family from Stability AI (large, medium, small-music, small-sfx, plus their pre-trained base counterparts) and the superseded Stable Audio Open line. They share one prompt scheme.
- One field. Unlike a lyrics-bearing music model, everything goes in a single descriptive prompt; there is no separate lyrics or structure input.
- English only. The owner states the models were trained on English descriptions and will not perform as well in other languages.
- No usable vocals. The owner states the models cannot generate intelligible singing or speech, only occasional wordless vocal texture. Any track needing a sung or spoken line needs a different model.
- Write a paragraph, not a tag list. The model rewards several sentences that name each instrument and say what it is doing.
- Two vocabularies coexist: ordinary description, and Key: Value metadata tags carried over from the training data. Use both.
- Pick the checkpoint by material first. Music and sound effects are separate models at the small tier, and asking the wrong one is a bad prompt no wording can fix.

</rules>

## TL;DR

<template id="quickstart">

TrackType: {Music|Instrument|SFX}, {a sentence naming the genre or the sound source and its overall character}. {A sentence per element, saying what each instrument or layer does.} {A sentence on production, room and recording character.} {tempo} BPM

</template>

## Models and when to use which

The naming is a trap worth reading twice. "Stable Audio Open" is the superseded 2024 line; the current family is "Stable Audio 3", and most of it is also openly published. A model called `stable-audio-open-small` and a model called `stable-audio-3-small-music` are two generations apart, not two names for one thing.

- `stable-audio-3-medium`: the practical default and the only open checkpoint covering music, stems and sound effects together. Use it whenever a prompt mixes categories.
- `stable-audio-3-small-music` and `stable-audio-3-small-sfx`: a genuine split at the weights, not a size ladder. The owner's compatibility table marks small-music as not doing sound effects and small-sfx as doing neither music nor stems. These are specialists; route by material.
- `stable-audio-3-large`: the same grammar at the owner's top quality, available through an API rather than as weights.
- The `-base` checkpoints are pre-trained foundations published for fine-tuning. They are not tuned for direct generation, they need far more sampling steps and real guidance to produce usable audio, and the owner points anyone generating at the ordinary checkpoints instead.
- `stable-audio-open-1.0` and `stable-audio-open-small`: the legacy line. Both are weaker at music by construction, and Open Small more so, because its diffusion transformer was trained on the sound-effects corpus without the music archive at all. If music is the goal and you are on either of these, changing checkpoint beats improving the prompt.

## How the model reads prompts

- Prompt adherence tracks the training data. The owner's first tip is to think about what the model was trained on: a licensed production-music library and a large sound-effects collection, together with the text metadata attached to both. Prompts that read like that metadata land better than prompts that do not.
- That is why the tag vocabulary exists. `TrackType:`, `Genre:` and the rest are not a parser feature; they are the literal shape of the labels in the training set, so writing them puts the prompt in distribution.
- Text conditioning is a language model, and a recent one on the 3 family. Full sentences with relationships between elements are understood, so "flute glides over the beat adding an exciting texture" carries more than "flute".
- Nothing is rewritten unless you ask. There is no automatic expansion in the pipeline, so a three-word prompt is not elaborated, it just leaves everything unspecified.
- Duration is part of the conditioning, not a trim. The model composes to fit the length it is given, so a duration that suits the material produces better structure than generating long and cutting.
- Guidance is held low by default. The shipped configuration favours creative freedom over literal adherence; when the model is ignoring something you asked for, raising guidance is the lever, and it is also what makes a negative prompt do anything.
- Output varies run to run by design. Fix a seed to compare two prompts, or you are comparing noise.

## Prompt structure

<rules id="structure">

- Lead with the tags that place the material, then write description. `TrackType: Music, VocalType: Instrumental` at the front measurably steers toward coherent instrumental output.
- Name every instrument separately and give each one an action. The owner's examples do this consistently: what the kick does, what the bass does, what the piano does in the drop.
- Say how something sounds, not just what it is. Recording technique, room, microphone character and processing are all in the training metadata, so "close-mic'd electric piano" and "warm, textured analogue tape sound" are understood as production directions.
- Put the tempo in the prompt as a number followed by BPM. Both of the owner's canonical examples end that way.
- Reach for a scene or a feeling where a genre label runs out. "The vibe of a long car journey with friends" and "the last tune played in a DJ set" are the owner's own framings and they carry real information about arrangement and energy.
- Match the duration to what you are describing. A one-shot is not a track and the model composes into the length it is told.
- Do not translate. Write in English regardless of the conversation language.

</rules>

<template id="general">

TrackType: {Music|Instrument|SFX}{, VocalType: Instrumental}{, Genre: {genre}}{, Instruments: {list}}, {one sentence establishing style, era and overall feeling}. {One sentence per element naming the instrument and what it plays.} {One sentence on production character, room and recording style.} {tempo} BPM

</template>

## Metadata tags

The tag vocabulary comes from the labels on the licensed music library in the training set. Tags are written inline in the ordinary prompt, comma-separated, conventionally at the front.

<rules id="tags">

- `TrackType: Music` for a full arrangement, `TrackType: Instrument` for an isolated part, `TrackType: SFX` for a sound effect or one-shot. This is the single highest-value tag and the owner recommends it for all three cases.
- `VocalType: Instrumental` alongside `TrackType: Music` is the owner's recommendation for higher quality and more coherent output. Given the models cannot sing intelligibly, this is close to always correct for music.
- `Genre:` is repeatable. Write it once per genre (`Genre: Funk, Genre: Jazz`) rather than listing several after one key, and combining unrelated genres is explicitly supported.
- `Instruments:` takes a comma-separated list in one tag.
- `Format: Duo` and similar say how many parts are playing, which matters when asking for an isolated instrument and getting an ensemble.
- Tags position the prompt; they do not describe the sound. A prompt of nothing but tags underspecifies badly. Always follow them with real description.

</rules>

<example use_case="instrumental music with tags and description">

```text
TrackType: Music, VocalType: Instrumental, Genre: House, Genre: Tech House, A triumphant and stylish UK bass-flavoured tech-house tune that evokes feelings of the last tune played in a DJ set. The pumping four-to-the-floor kick is supported by an 808 bass that is syncopated. There are gliding emotional synth leads that build sections to their climax. Playful stabs and chops support the rhythm of the drums in sections. There is a beautiful gospel house piano that plays in the drop, giving the track a euphoric feeling. 128 BPM
```

*Why: the owner's own example, with the tag prefix added. Every element gets a named instrument and a verb, the emotional framing is a moment rather than an adjective, and the tempo closes the prompt.*

</example>

## By use-case

### Music

<rules id="music">

- Four things to settle before writing: genre, the instruments and how each sounds, the mood and energy, and the tempo.
- Write the emotional target as a situation rather than an adjective where you can. "Deeply nostalgic with a 90s internet aesthetic and a sense of something lost to time" outperforms "nostalgic".
- Say what happens in sections. Naming what plays in the drop, or what builds toward a climax, is how structure gets requested; there is no section-tag syntax to do it for you.
- Expect no intelligible singing. Wordless vocal texture sometimes appears and can be used deliberately, but a lyric cannot.

</rules>

<example use_case="music by scene rather than genre">

```text
TrackType: Music, VocalType: Instrumental, A quirky alternative pop ballad instrumental with the vibe of a long car journey with friends. The catchy synth bass is infectious, the tightly tuned acoustic drums add a classy flair, and the dreamy colourful synths bring a fuzzy old VHS tape atmosphere. At the same time, subtle guitars play indie rock-style motifs. The track is deeply nostalgic with a 90s internet aesthetic and a sense of something lost to time - brooding, bold, youthful, and melancholic.
```

*Why: the owner's example. It carries almost no genre vocabulary and works anyway, because the scene, the per-instrument actions and the closing mood stack do the specifying.*

</example>

### Stems and solo instruments

<rules id="stems">

- Open with `TrackType: Instrument` to maximise the chance of an isolated part rather than a full arrangement.
- Add `Format: Duo` or similar when you want more than one instrument but still not a band.
- Name the style the instrument is playing in, not just the instrument. A solo guitar in a genre sounds nothing like a solo guitar without one.
- Technique, recording environment and effects are all in the training vocabulary, so specify them.

</rules>

<example use_case="isolated instrument">

```text
TrackType: Instrument, a sombre solo acoustic guitar track with cavernous reverb and delicate finger picking.
```

*Why: the owner's example, and notably short. The tag does the heavy lifting of isolating the part, leaving the description free to spend its words on playing technique and room.*

</example>

### Sound effects and samples

<rules id="sfx">

- Three things to settle: the source (exactly what object or instrument makes the sound), the action (how it is triggered and how it decays), and the production (microphone, room, processing).
- Describe the envelope in words. "Fast decay", "zero ring", "grinds to a halt" and "massive suck-back followed by a supersonic crack" are how duration and shape get requested.
- Set a short duration. Most effects are brief, and asking for a long one produces padding.
- `TrackType: SFX` produces more semantically reasonable results, per the owner.
- Route to a checkpoint that does sound effects. On the small tier that means small-sfx specifically; small-music does not cover this at all.

</rules>

<example use_case="one-shot with a described envelope">

```text
TrackType: SFX, A blunt, powerful "thud" made by slamming a wooden desk drawer shut. It has a pronounced low-mid body, making it feel heavy, and is given a touch of analog distortion for aggressive character.
```

*Why: the owner's example, and a clean demonstration of the three elements. Source is a wooden desk drawer, action is slamming shut, production is the low-mid body plus analog distortion. Nothing is left to be guessed.*

</example>

<example use_case="sample with no real-world source">

```text
TrackType: SFX, A massive sub-bass note that mimics a vinyl record or tape machine being turned off. The pitch and speed drop simultaneously, causing the high-end harmonics to "smear" and thicken as the sound grinds to a halt at a sub-sonic frequency.
```

*Why: the owner's example for a sound with no literal source. It works by describing the physical process being imitated, which is how to request something that has no name.*

</example>

## Audio editing

Three modes take existing audio: audio-to-audio, which reworks a whole clip; inpainting, which regenerates a region in place; and continuation, which is inpainting past the end of the file.

<rules id="edit">

- Audio-to-audio starts generation from your clip instead of from noise, and a strength control decides how much survives. Turning it up filters away the low-level features first, so melody and rhythm go before timbre and tonality do.
- That ordering is the whole technique. A moderate setting changes the instrument while keeping the notes, which is timbre transfer; a higher setting keeps only the broad character and rewrites the material, which is style transfer.
- Inpainting preserves everything outside the marked region and generates inside it, using the surrounding audio to keep the transitions continuous.
- Continuation is the same operation with the region starting where the file ends and finishing at the new total length. A prompt is optional; without one the model extends what it hears.
- In these modes the audio context matters more than the prompt. Masking only a few seconds gives the model so much context that it reproduces something close to the original whatever you write, so start with a large region and shrink it on later passes.
- The prompt has to be plausible given what surrounds it. Asking a progressive house track for a dubstep drop works; asking it for a cat meow does not.
- Tag conventions still apply here. `TrackType: SFX` is still worth writing when inpainting an effect.

</rules>

<example use_case="timbre transfer over an existing recording">

```text
TrackType: Instrument, Heavy metal guitar, aggressively picked with high-gain saturation and tight palm muting
```

*Why: paired with a violin recording at a moderate strength setting, this keeps the played notes and swaps the instrument. The prompt describes only the destination timbre, because the melody is coming from the input rather than from the text.*

</example>

<example use_case="style transfer that rewrites the material">

```text
A cinematic outlaw country instrumental featuring blues pedal steel guitar, rustic mandolin, fiddle playing call and response, a tape-driven rattly drum-kit, an autoharp, and a soaring accordion solo.
```

*Why: the owner's example, applied over a trance track at a high strength setting. Because the source is being mostly discarded, the prompt has to fully specify the destination, so it names six instruments and what each contributes.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is a real negative-prompt field here, unlike most music models. It takes a plain description of qualities to avoid, and short quality words such as "poor quality" are the owner's own example.
- It works through guidance, so it is only as strong as guidance is. The shipped default is deliberately low, which means an exclusion written against defaults is close to inert.
- If an exclusion matters, raise guidance. The same move increases positive prompt adherence, so the two are not independent knobs; you are choosing how literally the model reads everything.
- The base checkpoints are the exception in the other direction: they are meant to run with real guidance, so exclusions carry there by default.
- Prefer the positive that displaces the problem even so. Naming the arrangement you want is more reliable than naming the one you do not, and it costs nothing.
- Keep negatives to broad qualities. They steer character, and are not a way to remove a named instrument from an arrangement you otherwise described.

</rules>

## Pitfalls and anti-patterns

- Asking the wrong specialist: a foley prompt on small-music, or a music prompt on small-sfx. The owner's compatibility table marks these as not covered at all, and no amount of rewording fixes a checkpoint that was not trained for the material.
- Confusing the generations: `stable-audio-open-small` is the superseded line, not the small member of Stable Audio 3. Check which family a checkpoint belongs to before blaming the prompt.
- Asking for vocals: the models cannot produce intelligible singing or speech. A lyric in the prompt yields wordless texture at best.
- Writing a tag list and stopping: tags position the prompt in the training distribution but describe nothing. They need real description after them.
- Writing description with no tags: it works, but leaves free quality on the table, particularly `TrackType:` and `VocalType: Instrumental`.
- Repeating a key instead of repeating the tag: write `Genre: Funk, Genre: Jazz`, which is the documented form.
- Naming instruments without actions: a list of six instruments gives the model an ensemble and no arrangement. Say what each one plays.
- Expecting a short prompt to be expanded: nothing rewrites it. A terse prompt is simply an underspecified one.
- Writing exclusions against default guidance and assuming they took: at the shipped setting the negative barely acts. Raise guidance or rephrase positively.
- Generating long and trimming: duration conditions the composition, so ask for the length you want.
- Masking a tiny region and expecting a big change: with that much surrounding context the model reproduces the original. Mask wide first.
- Prompting in another language: the owner states English only, and other languages degrade rather than translate.
- Comparing two prompts on different seeds: output varies by design, so fix the seed or you are measuring noise.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (Stability AI): the [stable-audio-3 repository](https://github.com/Stability-AI/stable-audio-3) and its [prompt guide](https://github.com/Stability-AI/stable-audio-3/blob/main/docs/guides/prompting.md), which is the owner's own prompting reference and the source of the generation modes, the model compatibility table, the metadata tag vocabulary, the per-mode element checklists, every verbatim example prompt here, and the audio-to-audio and inpainting technique; the [Stable Audio 3 Medium card](https://huggingface.co/stabilityai/stable-audio-3-medium) and its base and small siblings for the family line-up and training corpus; the [Stable Audio Open 1.0 card](https://huggingface.co/stabilityai/stable-audio-open-1.0) for the legacy line and its stated limitations; the [product page](https://stability.ai/stable-audio); the [technical report](https://arxiv.org/abs/2605.17991).

Coverage note: the Stable Audio 3 family superseded Stable Audio 2.5 in May 2026, and the 2.5 launch material still circulating describes a model line that is no longer current. Secondary coverage of the 3.0 release also reports a parameter count for the small models that the owner's own table contradicts, so the figures here come from the repository table rather than from the announcement. Stability's hosted API reference could not be read for this pass: it renders client-side and returned no content, so nothing in this guide is sourced from it, which is consistent with the guide being prompt-craft only. Stable Audio 3 Large is recorded from the owner's model table alone, since its card is not published.

Last verified: 2026-08-29.
