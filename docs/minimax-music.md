---
guide: "MiniMax Music"
prompt_scheme: "minimax-music"
models:
  - { id: "music-3.0", access: "open-weights", tier: "flagship", caps: [text-to-music, lyrics-to-song, instrumental, structured-caption], best_for: "full songs up to five minutes with coherent structure and expressive vocals. Published as downloadable weights and also served hosted, and the weights are now the primary route because the paid music API closed to new users" }
  - { id: "music-cover", access: "closed-weights", tier: "std", caps: [music-cover, lyrics-extract, lyrics-to-song], best_for: "restyling an existing recording. Either pass the audio and let the lyrics be transcribed, or preprocess first to get editable structured lyrics back and change them before generating" }
  - { id: "music-2.6", access: "closed-weights", tier: "legacy", caps: [text-to-music, lyrics-to-song, instrumental], best_for: "the previous hosted generation, superseded by 3.0 on vocal quality and structural coherence" }
  - { id: "music-2.5", access: "closed-weights", tier: "legacy", caps: [text-to-music, lyrics-to-song, instrumental], best_for: "superseded. The tier that first unlocked instrumental-only generation" }
  - { id: "music-1.5", access: "closed-weights", tier: "legacy", caps: [text-to-music, lyrics-to-song], best_for: "superseded. The first tier to reach four-minute songs" }
capabilities: [text-to-music, lyrics-to-song, instrumental, structured-caption, music-cover, lyrics-extract]
prompt:
  languages: ["en", "zh", "more"]
  lyrics: "a SEPARATE field from the description, carrying the sung words with bracketed section tags on their own lines. Omit it for an instrumental, or leave it empty and let the model draft it from the description"
  description: "one field covering style, mood and scenario. It takes either a short comma-separated descriptor list or a three-section Structured Caption, and the owner recommends the structured form when precise control matters"
  structured_caption: "three labelled sections. Global Metadata carries genre, subgenre, tempo, key, scale, emotional progression, listening scenario and production profile; Vocal Details carries vocal gender, timbre, performance style, harmony, backing vocals and effects; Arrangement carries primary and secondary instruments, how instrumentation evolves by section, groove, bass, percussion, textures and spatial effects"
  length_strategy: "short descriptors work and the structured caption works better; the difference is control rather than quality. Write the structured form when the arrangement should evolve over the song, because that is the only form that can say when something changes"
  auto_expand_behavior: "optional and explicit. A caption-rewriter shipped with the open model expands a concise description into the structured form, and a lyrics optimizer will draft lyrics from the description when the lyrics field is left empty. Neither runs unless asked"
  negatives: "no negative field. Constraints are stated positively in the description, and an unwanted section is removed by editing the lyrics rather than by excluding it"
sources:
  official: ["https://platform.minimax.io/docs/guides/music-generation", "https://platform.minimax.io/docs/api-reference/music-generation", "https://huggingface.co/MiniMaxAI/MiniMax-Music3", "https://github.com/MiniMax-AI/MiniMax-Music3", "https://platform.minimax.io/docs/guides/local-deploy-music-3"]
  provider: []
  community: []
last_verified: "2026-08-29"
---

# MiniMax Music: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the MiniMax Music line, current model Music 3.0 plus the cover model and the superseded hosted tiers. They share one scheme.
- MiniMax ships three separate guides. This one is music. Speech is a different scheme where the prompt is the spoken script, and MiniMax H3 is video. Nothing transfers between them.
- A prompt here is TWO fields. The description covers the whole track; the lyrics field is a separate temporal script with its own section tags. Never merge them.
- The description has two registers: a short comma-separated descriptor list, or a three-section Structured Caption. Both work; the structured form is what the owner recommends for precise control.
- Music 3.0 has published weights. The hosted paid API closed to new users in August 2026, so self-hosting or a third-party host is the route for anyone starting now, and the prompt is identical either way.
- Write lyrics in the language they should be sung. The description stays in English.

</rules>

## TL;DR

<template id="quickstart">

Description: {genre}, {mood}, {two or three instruments}, {vocal type}, {scenario or setting}

Lyrics:
[Verse]
{four lines}

[Chorus]
{the hook}

[Outro]

</template>

## Models and when to use which

- `music-3.0`: the current model and the one to use. Full songs up to five minutes, holding theme, vocal identity and arrangement across the whole length. Its weights are published, which matters more than usual here because the hosted paid music API stopped accepting new users in August 2026. The prompt is the same whichever way you reach it.
- `music-cover`: for restyling an existing recording rather than writing a new song. Two workflows, covered below.
- `music-2.6`, `music-2.5` and `music-1.5`: superseded hosted tiers. 3.0's stated gains are in creative-intent understanding, mix quality and vocal naturalness, so there is no craft reason to prefer an older one.
- Access shapes the surface, not the grammar. Self-hosted, the description and lyrics arrive as two fields under different names than the hosted API uses. Same two inputs, same tags, same rules.

## How the model reads prompts

- Two inputs, two jobs. The description is the global portrait: style, instrumentation, vocal character, production. The lyrics field is the timeline: what is sung, in what section, in what order.
- The description has a low and a high gear. A comma-separated descriptor list is a valid prompt and the owner's own examples include one. A Structured Caption is the same field written in three labelled sections, and it is the only form that can express how the arrangement should change across the song.
- Structure comes from the lyrics field. Section tags are how the model is told where a chorus is, so an arrangement instruction with no corresponding tag has nothing to attach to.
- Nothing is rewritten unless asked. Expansion of a terse description into the structured form, and drafting of lyrics from the description, are both explicit opt-ins rather than defaults.
- Long-range coherence is the model's stated strength. It is built to hold a theme across a full song rather than to produce a loop, so describing a progression is a reasonable thing to do.
- Instrumental is a mode, not a prompt trick. Ask for it directly rather than writing lyrics that say there are no vocals.

## Prompt structure

<rules id="structure">

- Decide which register the description needs. Reach for the short descriptor list when exploring, and the Structured Caption when the arrangement should evolve or the vocal needs pinning down.
- In the short register, comma-separated descriptors are idiomatic: genre, mood, and a scenario. The owner's examples read like "Indie folk, melancholic, introspective, longing, solitary walk, coffee shop".
- In the structured register, write three labelled sections and keep each one to its own concern. Do not scatter instrument names through the vocal section or vice versa.
- Name a scenario or listening context, not only a genre. "Perfect for a rainy night" and "solitary walk, coffee shop" are the owner's own framings and they carry arrangement and energy information a genre label does not.
- Say when things change. Section-level instrument evolution is the thing the structured form exists for: which instruments enter at the chorus, what drops out for the bridge.
- Keep the description and the lyrics consistent. An instrument promised in one and contradicted in the other is a worse prompt than either alone.

</rules>

<template id="structured">

Genre: {genre and subgenre}. BPM: {tempo}. Key: {key and scale}. {Emotional progression across the song}. {Listening scenario}. {Production profile.}
Vocals: {gender and timbre}, {performance style}, {harmony and backing vocals}, {effects}.
Arrangement: {primary instruments}; {secondary instruments}; {what enters or leaves at which section}; {groove, bass and percussion}; {textures and space}.

</template>

<example use_case="structured caption">

```text
Genre: acoustic pop. BPM: 96. Key: C major. Warm and intimate, building gently into the chorus. Vocals: soft female lead, close and breathy, light stacked harmonies in the chorus. Arrangement: fingerpicked guitar and soft piano; brushed drums and upright bass enter in the chorus.
```

*Why: the owner's own example, and a compact demonstration of all three sections. Note that the only arrangement instruction with a time dimension, brushed drums and upright bass entering in the chorus, is the one that needs a matching chorus tag in the lyrics to land.*

</example>

<example use_case="short descriptor register">

```text
Indie folk, melancholic, introspective, longing, solitary walk, coffee shop
```

*Why: the owner's example of the low gear. Three mood words and two scenario words do more than a long paragraph of genre history would, and the model is free to make the arrangement decisions this leaves open.*

</example>

## Lyrics and song structure

<rules id="lyrics">

- Put each section tag on its own line, with the lines it governs beneath it.
- The documented tags are `[Intro]`, `[Verse]`, `[Pre Chorus]`, `[Chorus]`, `[Post Chorus]`, `[Interlude]`, `[Bridge]`, `[Hook]`, `[Build Up]`, `[Break]`, `[Transition]`, `[Inst]`, `[Solo]` and `[Outro]`.
- Two spellings circulate for the compound tags. The API reference writes `[Pre Chorus]` and `[Post Chorus]` with a space and abbreviates the instrumental passage to `[Inst]`; the model card writes `[Pre-Chorus]`, `[Post-Chorus]` and `[Instrumental]`. Match the surface you are prompting through, and prefer the API reference's forms when unsure.
- Tags are section labels, not performance direction. There is no documented way to qualify one the way some other music models allow, so how a section should be sung belongs in the description's vocal section.
- Put backing vocals and answering phrases in parentheses on the line they answer.
- Separate sections with a blank line so boundaries stay unambiguous.
- For an instrumental, use the instrumental mode rather than writing lyrics that describe silence.
- To have lyrics written for you, leave the field empty and turn on the optimizer; the description is what it writes from, so a vague description yields vague lyrics.

</rules>

<template id="lyrics">

[Intro]
{optional backing phrase} ({echo})

[Verse]
{four lines}

[Pre Chorus]
{two lines that lift}

[Chorus]
{hook line} ({answer})
{hook line}

[Verse]
{four lines matching the first verse's shape}

[Bridge]
{two lines of contrast}

[Chorus]
{hook}

[Outro]

</template>

<example use_case="song with sections and backing vocals">

```text
[Intro]
Streetlights fading (fading)

[Verse]
Streetlights flicker, the night breeze sighs
Shadows stretch as I walk alone
An old coat wraps my silent sorrow
Wandering, longing, where should I go

[Pre Chorus]
Every window holds a warmer room
Every door has closed before

[Chorus]
Pushing the wooden door, the aroma spreads (spreads)
In a familiar corner, a stranger gazes
And the night lets go of me

[Outro]
```

*Why: built out from the owner's example verse and chorus. Each tag sits on its own line, the sections are blank-line separated, and the parenthesised answers sit on the lines they answer. Pair it with a description naming an indie folk arrangement and a solitary scenario and the two fields agree.*

</example>

## Covers and restyling

<rules id="cover">

- Two workflows. Pass the recording with a style description and let the lyrics be transcribed automatically, or preprocess first to get structured lyrics back, edit them, then generate.
- Choose the two-step form whenever the words matter. The preprocessing step returns the lyrics already divided into tagged sections, which is an editable starting point rather than something you have to transcribe yourself.
- A cover description states the destination style, not the change. "Jazz, smooth, late night lounge, saxophone" is the owner's own example: it names where the track is going and says nothing about where it came from.
- Keep a cover description short. It is a style redirect, not a full song specification, and the field is bounded much more tightly than the ordinary description.
- The source supplies the structure and the melody. Anything you want preserved does not need describing; anything you want changed does.

</rules>

<example use_case="style redirect for a cover">

```text
Jazz, smooth, late night lounge, saxophone
```

*Why: the owner's example. Four descriptors, all destination. The melody, structure and lyrics come from the source recording, so spending words on them would be describing what is already fixed.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field. Nothing is subtracted from the result, so exclusions have no channel to act through.
- State the positive that displaces the problem. A named arrangement crowds out the one you did not want; "no drums" does not.
- Remove an unwanted section by editing the lyrics. Structure is controlled by which tags are present, so a bridge you do not want is a bridge you do not write.
- Silence an unwanted instrument by naming what plays instead. The arrangement section of a structured caption is the right place, because it is read as the full instrument list rather than as additions.
- For an unwanted vocal, use the instrumental mode rather than describing its absence.

</rules>

## Pitfalls and anti-patterns

- Merging the fields: putting section tags in the description or genre notes in the lyrics. Each field is read differently and neither does the other's job.
- Contradicting yourself across fields: an instrument named in the description and denied by the arrangement implied in the lyrics degrades the track rather than resolving.
- Mixing the two tag spellings: `[Pre Chorus]` and `[Pre-Chorus]` are documented on different owner surfaces. Pick the one your surface documents and stay consistent within a song.
- Qualifying a section tag: unlike some music models, there is no documented syntax for saying how a section is performed. That belongs in the description.
- Writing arrangement changes with no matching tag: "drums enter at the chorus" needs a chorus tag in the lyrics to attach to.
- Describing an instrumental instead of asking for one: there is a mode for it, and prose about the absence of vocals is not it.
- Expecting the description to be expanded automatically: rewriting into the structured form is an explicit step, not a default.
- Leaving the lyrics empty without turning on the optimizer: for a vocal track the words are required, and an empty field is not an instruction to invent them.
- Writing a long cover description: that field is bounded far more tightly than the ordinary one, and it only needs the destination style.
- Describing the source in a cover prompt: the melody and structure come from the audio. Words spent on them are words not spent on the change.
- Writing exclusions: there is no negative field. Name what should be there.
- Assuming the hosted API is available: it closed to new users in August 2026. The published weights are the current route.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (MiniMax): the [music generation guide](https://platform.minimax.io/docs/guides/music-generation) for the two-field workflow, the cover workflows and the 3.0 capability statement; the [music generation API reference](https://platform.minimax.io/docs/api-reference/music-generation), whose description and lyrics field documentation is the source of the structure-tag list, the per-mode field requirements and the short-register example; the [MiniMax Music 3 model card](https://huggingface.co/MiniMaxAI/MiniMax-Music3) for the Structured Caption's three sections, the structured example, and the model's own account of what it holds across a full song; the [self-hosting guide](https://platform.minimax.io/docs/guides/local-deploy-music-3) and the [GitHub repository](https://github.com/MiniMax-AI/MiniMax-Music3).

Coverage note: MiniMax's documentation renders client-side, and everything here comes from the markdown twin served at each page's path with a `.md` suffix, indexed at `/docs/llms.txt`. Two owner surfaces spell the compound section tags differently, the API reference using a space and the model card a hyphen, and the guide records both rather than picking, because the two surfaces correspond to the two ways the model is actually reached. The hosted paid music API closed to new users on 2026-08-20 with existing subscribers unaffected, which is why this guide treats the published weights as the primary route rather than the API.

Last verified: 2026-08-29.
