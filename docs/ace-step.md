---
guide: "ACE-Step"
prompt_scheme: "ace-step"
models:
  - { id: "acestep-v15-turbo", access: "open-weights", tier: "distilled", caps: [text-to-music, lyrics-to-song, music-cover, music-repaint, reference-audio], best_for: "the default for daily work and rapid iteration. The owner rates its audio quality above the undistilled checkpoints, but it runs without classifier-free guidance, so exclusions have nothing to push against and prompts that fight its defaults stop working" }
  - { id: "acestep-v15-sft", access: "open-weights", tier: "std", caps: [text-to-music, lyrics-to-song, music-cover, music-repaint, reference-audio], best_for: "detail and semantic parsing over raw clarity. The owner states it takes guidance and reads a prompt more closely, at the cost of some audio clarity against turbo" }
  - { id: "acestep-v15-base", access: "open-weights", tier: "base", caps: [text-to-music, lyrics-to-song, music-cover, music-repaint, stem-extract, track-add, accompaniment, reference-audio], best_for: "the only checkpoint that separates stems, adds a track to an existing one, or builds accompaniment under a bare vocal. Highest diversity across seeds and the most responsive to guidance, at lower rated quality" }
  - { id: "acestep-v15-xl-turbo", access: "open-weights", tier: "distilled", caps: [text-to-music, lyrics-to-song, music-cover, music-repaint, reference-audio], best_for: "turbo behaviour on the larger decoder; identical prompt grammar, higher audio quality" }
  - { id: "acestep-v15-xl-sft", access: "open-weights", tier: "std", caps: [text-to-music, lyrics-to-song, music-cover, music-repaint, reference-audio], best_for: "the owner's top quality rating; identical prompt grammar to the smaller sft" }
  - { id: "acestep-v15-xl-base", access: "open-weights", tier: "base", caps: [text-to-music, lyrics-to-song, music-cover, music-repaint, stem-extract, track-add, accompaniment, reference-audio], best_for: "the stem and track tasks at the larger decoder's quality" }
capabilities: [text-to-music, lyrics-to-song, music-cover, music-repaint, stem-extract, track-add, accompaniment, reference-audio]
prompt:
  languages: ["en", "zh", "ja", "ko", "more"]
  lyrics: "a SEPARATE field from the style description, carrying the sung words plus bracketed structure tags that mark each section and how it is performed; write [Instrumental] alone for music with no vocal"
  direction_syntax: "square-bracket tags inside the lyrics field, one per section, optionally qualified with a hyphen as [Chorus - anthemic]; UPPERCASE lyric lines for vocal intensity and (parentheses) for backing vocals"
  length_strategy: "the style description is format-agnostic, so bare style words, comma-separated tags and full natural-language description all work; combine several descriptive dimensions rather than lengthening one, because omitted dimensions are where the model improvises"
  auto_expand_behavior: "ON by default. A language-model planner rewrites the style description, infers tempo and key, and can draft lyrics from a one-line idea before the audio model ever sees it. Write the full prompt yourself to keep control, and expect a terse prompt to be elaborated rather than taken literally"
  negatives: "there is no acoustic negative field. The only exclusion channel is a negative prompt on the planner, which shapes what gets planned rather than what gets rendered, and turbo runs without guidance so exclusions cannot be enforced at generation time either. Phrase constraints positively and resolve conflicts by sequencing them in time"
sources:
  official: ["https://github.com/ace-step/ACE-Step-1.5", "https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/Tutorial.md", "https://huggingface.co/ACE-Step/Ace-Step1.5", "https://ace-step.github.io/ace-step-v1.5.github.io/", "https://arxiv.org/abs/2602.00744"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# ACE-Step: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the ACE-Step 1.5 music family from ACE Studio and StepFun: the 2B checkpoints (base, sft, turbo) and their XL 4B counterparts. All six share one prompt scheme; a prompt written for one transfers to the others.
- A prompt here is TWO fields, not one. The style description ("caption" in the owner's docs) covers the whole track: genre, instruments, mood, timbre, production. The lyrics field is a separate temporal script that says what happens when. Never merge them; collapsing the two loses the model's main control surface.
- The style description is the single largest influence on the result. Write it first and write it properly.
- The two fields must agree. The model is poor at resolving contradictions between them, so an instrument named in one and denied in the other degrades the whole track rather than picking a winner.
- A language-model planner sits in front of the audio model and rewrites terse input by default. Assume elaboration unless you write the prompt out in full.
- There is no negative-prompt field on the audio model itself, so exclusions are a planning-stage lever, not a rendering-stage one.

</rules>

## TL;DR

<template id="quickstart">

Style description: {genre}, {emotion or atmosphere}, {two or three instruments}, {timbre words}, {vocal type}, {tempo feel}

Lyrics:
[Intro - {instrument}]

[Verse]
{four lines, six to ten syllables each}

[Chorus - {performance word}]
{four lines, the hook}

[Outro - fade out]

</template>

## Models and when to use which

All six take the identical prompt. Pick by the job, not by the wording.

- `acestep-v15-turbo`: the owner's recommended default and the fastest. Rated highest for audio quality, but distilled to run without classifier-free guidance. That is the one difference that changes how you write: with no guidance there is nothing for an exclusion to push against, seeds converge, and a prompt that argues with the model's defaults simply loses. State what you want, positively.
- `acestep-v15-sft`: takes guidance and reads a prompt more closely. The owner describes its detail expression and semantic parsing as better than turbo's while conceding slightly lower audio clarity. Reach for it when a prompt is being partly ignored.
- `acestep-v15-base`: the undistilled foundation and the only checkpoint that can separate a stem, add a track over an existing one, or build accompaniment under a bare vocal. The owner rates its raw quality lowest of the three and its diversity across seeds highest, which makes it the one to use when everything is coming out the same.
- The `xl` row is the same three models on a larger decoder. The owner states they behave identically and differ only in audio quality, so nothing in this guide changes for them.
- The turbo line has several distillation variants that trade fine detail against structural clarity. The prompt is identical for all of them; the choice is a settings question, not a prompt-writing one.
- The planner is a separate, swappable model in three sizes. The largest is rated strongest at composition and at copying a melody from reference audio. A smaller planner does not change the prompt grammar, but it does weaken the rewriting and the inferred musical metadata, so a bigger planner rewards a terser prompt and a smaller one rewards writing more yourself.

## How the model reads prompts

- Two stages, not one. A language-model planner turns your input into a full song blueprint (elaborated style description, musical metadata, sometimes the lyrics themselves) and the diffusion model renders that blueprint. What you type is the planner's input, and the planner's output is what the audio model actually sees.
- Rewriting is on by default. The planner expands the style description, infers tempo, key and time signature, and detects the vocal language, all without being asked. This is genuinely useful for a one-line idea and genuinely in the way when you know what you want, so write in full when the details matter.
- The style description is format-agnostic. The owner trained it to accept bare style words, comma-separated tags and flowing natural language interchangeably, and states the format does not meaningfully change performance. Use whichever is easier to write; spend the effort on content, not on shape.
- Detail buys control and costs surprise. The owner is explicit that what you leave out is where the model plays. A sparse description yields variety, a dense one yields obedience, and neither is the right answer by default.
- Conflicting descriptors degrade rather than blend. Asking for classical strings and hardcore metal at once produces a bad fusion, not a choice. This gets worse with the planner engaged, because the planner generalises less well than the audio model.
- Over fifty languages for lyrics. Write the sung words in the language they should be heard in; the model is not translating them.

## Prompt structure

The style description covers the whole track at once. There is no ordering rule, so combine dimensions instead of ordering them.

<rules id="structure">

- Cover several dimensions rather than elaborating one. The owner's nine are style or genre, emotion or atmosphere, instruments, timbre texture, era reference, production style, vocal characteristics, tempo feel, and structural hints. Four or five well-chosen dimensions beat one long paragraph about genre.
- Be concrete. "Sad piano ballad with a breathy female vocal" is the owner's own contrast against "a sad song"; the second one is not a weaker prompt, it is a request for a random one.
- Texture adjectives do real work. Warm, crisp, airy, punchy, lush, raw and polished influence the mix and the timbre, not just the mood.
- Comparative references are efficient. Naming an era or a recognisable aesthetic carries more than a list of adjectives can.
- Name the vocal explicitly when you care: gender, and a delivery word such as breathy, powerful, falsetto or raspy. Leaving it out is a choice to let the planner cast it.
- Treat the description as a first draft. The owner's framing is that it is a starting point rather than a finished thing, so generate, listen, and adjust rather than trying to write it perfectly first.
- Do not resolve a style conflict by adding words. Either reinforce the side you want by repeating its terms, or convert the conflict into a sequence (see below), which is the only form the model handles cleanly.

</rules>

<template id="description">

{genre}, {emotion or atmosphere}, {lead instrument}, {supporting instruments}, {timbre words}, {vocal gender and delivery}, {era or production reference}, {tempo feel}

</template>

<example use_case="vocal pop">

```text
dream pop, wistful and weightless, chiming electric guitar, analog synth pads, brushed drums, warm and airy, female vocal with breathy delivery, 80s 4AD production, mid-tempo
```

*Why: eight dimensions in one line, each naming something audible; no adjective appears without a thing for it to attach to.*

</example>

<example use_case="style evolution instead of style conflict">

```text
starts as soft solo strings, builds into loud distorted metal in the middle, resolves into a sparse hip-hop outro, cinematic production, no vocal
```

*Why: strings against metal fuses badly when asked for at once, so the conflict is sequenced in time instead. The owner names this as the fix for incompatible styles.*

</example>

## Lyrics and song structure

The lyrics field is the temporal script. It carries four things beyond the words: what each section is, how it is performed, where the instrumental passages go, and how the energy moves.

<rules id="lyrics">

- Mark every section with a bracketed tag on its own line: `[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`, plus `[Build]`, `[Drop]` and `[Breakdown]` for dynamics and `[Instrumental]`, `[Guitar Solo]` or `[Piano Interlude]` for passages with no vocal.
- Qualify a tag with a hyphen to say how it is performed: `[Chorus - anthemic]`, `[Bridge - whispered]`. This is stronger than the bare tag, because it tells the model both what the section is and how to sing it.
- Keep tags short. Stacking qualifiers (`[Chorus - anthemic - stacked harmonies - high energy - epic]`) has two failure modes the owner names: the model may sing the tag as if it were a lyric, and the extra instructions confuse rather than refine. Complex style belongs in the style description, not in a tag.
- Separate sections with a blank line. Without it, section boundaries blur and content bleeds across them.
- Keep lines to roughly six to ten syllables, and keep the same position across sections to a similar count. The model aligns syllables to beats, so a six-syllable line followed by a fourteen-syllable one produces a lurching rhythm.
- Write a line in UPPERCASE for greater vocal intensity, and put backing vocals or answering phrases in (parentheses).
- Repeat vowels to extend a note if you want, but do not rely on it; the owner records the effect as unstable and sometimes mispronounced.
- For an instrumental track write `[Instrumental]` alone, or use section tags with no lyric lines under them to shape the arrangement over time.
- Every tag must be consistent with the style description. Check three pairings: instruments in the description against instrumental section tags, emotion against energy tags, and the vocal description against vocal tags.

</rules>

<template id="lyrics">

[Intro - {instrument}]

[Verse 1]
{line, six to ten syllables}
{line, similar count}
{line, similar count}
{line, similar count}

[Pre-Chorus]
{two lines that lift}

[Chorus - {performance word}]
{hook line} ({backing answer})
{hook line}

[Verse 2]
{four lines matching verse 1's shape}

[Bridge - {contrasting performance word}]
{two lines}

[Chorus - {performance word}]
{hook, with the final line in UPPERCASE for the lift}

[Outro - fade out]

</template>

<example use_case="full song with performance direction">

```text
[Intro - piano]

[Verse 1]
Rain on the kitchen glass
Your coat still on the chair
The kettle finds its voice
And fills the empty air

[Pre-Chorus]
I keep the small things close
They hold what you left here

[Chorus - anthemic]
So let the morning come (let it come)
I will not close the door
Some doors were never locked

[Verse 2]
The garden keeps your rows
The beans have climbed the string
I water them at six
And listen for the ring

[Bridge - whispered]
If you are not returning
Then let the rain say so

[Chorus - anthemic]
So let the morning come (let it come)
I will not close the door
SOME DOORS WERE NEVER LOCKED

[Outro - fade out]
```

*Why: every line sits in the six-to-ten range and matching positions match in length; the tags name a performance rather than stacking adjectives; the backing vocal answers rather than duplicating; the single uppercase line puts the intensity in one place instead of everywhere. Pair it with a description naming piano, strings and a female vocal, and the two fields agree.*

</example>

<example use_case="instrumental with an arrangement arc">

```text
[Intro - ambient]

[Main Theme - piano]

[Build]

[Climax - powerful]

[Breakdown]

[Outro - fade out]
```

*Why: no words at all, so the tags carry the entire structure. This is the form to use when the description sets the palette and the lyrics field only has to shape time.*

</example>

## By use-case

- Quick exploration: write three or four description dimensions, leave the lyrics empty or `[Instrumental]`, and let the planner draft. Use this to find a direction, not to finish a track.
- A specific song you can already hear: write both fields out in full and expect the planner's rewriting to be the thing standing between you and it.
- Covering or restyling an existing track: supply reference audio and describe the target style. The words for what should change go in the description; the structure stays with the source.
- Fixing one section: repaint that interval rather than regenerating, and keep both fields identical apart from the change you want.
- Building a track in layers: this is the undistilled base checkpoint's territory. Extract a stem, add a track over an existing one, or put accompaniment under a bare vocal.

## Editing and variation

<rules id="edit">

- Editing is task selection plus the same two fields, not a different prompt language. Write the description and lyrics for the result you want, not instructions about what to change.
- Reference audio steers timbre and style globally. Describe what should differ from it; anything you do not mention is inherited.
- Repainting rewrites a time interval in place. Keep the surrounding prompt identical, or the repainted region will not match its neighbours.
- Lyric editing works in small spans. The owner records that changing a large block at once distorts the result, and that several small sequential edits are the way to make a big change.
- Stem separation, adding a track and building accompaniment exist only on the base checkpoints. A prompt asking for them elsewhere does not fail loudly; it just generates a normal track.

</rules>

<example use_case="cover in a new style">

```text
same melody and lyrics, reimagined as a stripped acoustic folk arrangement, fingerpicked steel-string guitar, upright bass, brushed snare, close and dry recording, male vocal with a low warm delivery, slow tempo
```

*Why: it describes the destination rather than the edit. Naming the arrangement, the room and the vocal gives the model a full target; "make it more acoustic" would leave the other dimensions to the planner.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no acoustic negative field. Nothing you write is subtracted from the rendered audio, so exclusions do not work the way they do on an image model with a negative prompt.
- The one exclusion channel acts on the planner, shaping what gets planned rather than what gets rendered. It is a blunt instrument and it is upstream of the audio entirely.
- Turbo removes the other half. Running without classifier-free guidance means there is no mechanism for pushing away from a concept at generation time, so on the default checkpoint an exclusion has neither channel available.
- Phrase every constraint as the positive that displaces it. "Sparse arrangement, single guitar, long silences" gets you what "no drums, not busy" will not.
- Where two styles genuinely conflict, sequence them in time rather than excluding one. The owner names this as the fix, and it is the only form the model handles cleanly.
- Where one element keeps intruding, reinforce its replacement by repeating that element's terms in the description instead of naming the intruder.

</rules>

## Pitfalls and anti-patterns

- Merging the two fields: putting song structure in the style description, or genre and production notes in the lyrics field. Each field has its own job and the model reads them differently.
- Contradicting yourself across fields: a description naming a violin and a lyrics tag calling for a distorted electric guitar solo. The model does not choose, it degrades.
- Stacking qualifiers on a tag: `[Chorus - anthemic - epic - powerful - huge]` risks the model singing the words and confuses the direction. One qualifier.
- Uneven syllable counts: lines that swing between four and sixteen syllables produce a lurching vocal, because the model is aligning syllables to beats.
- Writing exclusions: there is no field that subtracts, and the default checkpoint has no guidance either. Say what should be there.
- Asking for incompatible styles at once: the result is a bad fusion, not a choice between them. Sequence them instead.
- Expecting a terse prompt to be taken literally: rewriting is on by default, so a one-line idea gets elaborated by the planner before the audio model sees it.
- Adjective-stacked lyrics: filling a section with vague imagery ("neon skies, electric hearts, endless dreams") is the owner's own first red flag for mechanical-sounding lyrics.
- Mixing metaphors across sections: water imagery in the first verse, fire in the second, flight in the third leaves nothing for a listener to hold. Pick one image and explore its facets.
- Lines too long to sing in a breath: if you cannot say it out loud comfortably, the vocal will not phrase it well either.
- Assuming the stem and track tasks work everywhere: they are base-checkpoint only, and asking for them elsewhere silently returns an ordinary track.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (ACE Studio and StepFun): the [ACE-Step 1.5 repository](https://github.com/ace-step/ACE-Step-1.5) and its [prompting tutorial](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/Tutorial.md), which is the owner's own prompt guide and the source of the caption dimensions, the structure-tag vocabulary, the syllable and consistency rules and the lyric red flags; the [Hugging Face model card](https://huggingface.co/ACE-Step/Ace-Step1.5) for the checkpoint line-up and the per-model capability and quality ratings; the [project page](https://ace-step.github.io/ace-step-v1.5.github.io/); the [technical report](https://arxiv.org/abs/2602.00744).

Coverage note: the owner's docs disagree with themselves about which checkpoints respond to guidance. The model-zoo tables in both the repository and the model card mark base and sft as supporting classifier-free guidance and turbo as not, while the tutorial's hyperparameter table states guidance is effective on base only. Turbo's exclusion from guidance is stated consistently everywhere and is the fact this guide relies on; the base-versus-sft question is recorded as unresolved rather than settled in either direction. The tutorial also names four distilled turbo variants where the model-zoo tables publish one per decoder size.

Last verified: 2026-08-29.
