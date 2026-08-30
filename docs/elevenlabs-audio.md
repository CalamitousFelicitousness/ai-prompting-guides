---
guide: "ElevenLabs Music and Sound Effects"
prompt_scheme: "elevenlabs-audio"
models:
  - { id: "music_v2", access: "closed-weights", tier: "flagship", caps: [text-to-music, lyrics-to-song, instrumental, composition-plan, music-inpaint, audio-reference, stems], best_for: "full songs from a plain description, or from a structured composition plan when the arrangement has to be controlled section by section. Also the tier that edits an existing song in place" }
  - { id: "music_v1", access: "closed-weights", tier: "legacy", caps: [text-to-music, lyrics-to-song, instrumental], best_for: "the previous music generation, superseded and without the plan and editing surface" }
  - { id: "eleven_text_to_sound_v2", access: "closed-weights", tier: "std", caps: [text-to-sfx, ambience, one-shot, loop, musical-elements], best_for: "short sound effects, ambiences, one-shots and loops from a description. It also generates musical fragments such as drum loops and stabs, which is where it overlaps the music model" }
capabilities: [text-to-music, lyrics-to-song, instrumental, composition-plan, music-inpaint, audio-reference, stems, text-to-sfx, ambience, one-shot, loop, musical-elements]
prompt:
  languages: ["en", "multilingual"]
  lyric_languages: "multilingual, but the owner publishes NO list for music. It names English, Spanish, German and Japanese as examples and stops there. Styles stay English whatever the lyrics are"
  description: "one natural-language field answering five questions: genre, mood, instrumentation, tempo and production era. Anything left open is filled with the most statistically average choice, which is the owner's own framing"
  lyrics: "optional and inline. Lyrics are written into the description or into a plan's text field; by default the model writes its own, and instrumental has to be asked for explicitly"
  composition_plan: "an ordered list of sections, each with its own text, duration, and separate positive and negative style lists. The first section's styles set the tone for the whole song, so they carry the most weight"
  plan_notation: "inside a section's text, THREE bracket families do different jobs: [Section Name] labels the part, (parentheses) hold phonetic vocal sounds such as (ooh), and {curly braces} hold short inline directions such as {guitar solo}. Broader characteristics belong in the style list instead"
  length_strategy: "detail buys control and costs surprise. The owner notes that short evocative prompts give more creative results and that prompt length does not always correlate with quality, so choose deliberately rather than always maximising"
  auto_expand_behavior: "a plan can be generated from a plain prompt and then edited by hand, which is the documented route to a structured prompt without writing one from scratch. Nothing rewrites a plain description"
  negatives: "REAL and recommended. The composition plan has a dedicated negative style list per section and the owner says to use it liberally, and for loops the owner treats exclusion as the main technique rather than a fallback"
sources:
  official: ["https://elevenlabs.io/docs/overview/capabilities/music/best-practices", "https://elevenlabs.io/docs/overview/capabilities/music", "https://elevenlabs.io/docs/overview/capabilities/sound-effects", "https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans", "https://elevenlabs.io/docs/overview/models"]
  provider: []
  community: []
last_verified: "2026-08-30"
---

# ElevenLabs Music and Sound Effects: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers Eleven Music and the sound-effects model together, because both take a describe-the-sound prompt and their coverage overlaps: the effects model generates musical fragments and the music model does sound design.
- ElevenLabs speech is a DIFFERENT scheme with its own guide. Audio tags from a speech transcript do not belong here, and voice-only rules do not apply.
- Answer five questions in a music prompt: genre, mood, instrumentation, tempo and production era. Whatever you leave open gets the most average answer available.
- Studio vocabulary is functional, not decorative. Words like sidechained, close-mic'd, bone-dry and plate reverb move real levers.
- Exclusions are a first-class technique here, unlike most models in this set. Say what must not be there.
- Two registers exist: a plain description, and a structured composition plan for section-by-section control.
- No language list is published for music. The owner says multilingual and names English, Spanish, German and Japanese, so anything further is untested rather than supported. The speech guide's per-model lists do not help here, because they describe different models.

</rules>

## TL;DR

<template id="quickstart">

{genre}, {tempo} BPM{, key}, {two or three instruments with their character}, {mood or setting}, {production era or treatment}

</template>

## Models and when to use which

- `music_v2`: the current music model. Plain prompts, structured composition plans, editing an existing song in place, and conditioning on a reference recording.
- `music_v1`: superseded; no reason to prefer it.
- `eleven_text_to_sound_v2`: short sound effects, ambiences, one-shots and loops. It also makes drum loops, stabs and pads, so a short musical fragment can come from either model.
- Choose by length and structure, not by category. Something short and self-contained belongs to the effects model; anything with sections, vocals or an arrangement belongs to the music model.

## How the model reads prompts

- Unanswered questions get average answers. This is the owner's central framing: a prompt is answering genre, mood, instrumentation, tempo and era whether you meant it to or not, and silence is a choice for the most likely option.
- Studio language works. Production terms change the mix audibly, and where the vocabulary is missing, describing the room works instead: asking for something that sounds like it was recorded in a stairwell gets a stairwell.
- Era is a dial and it can move mid-song. Naming a period sets the whole production character, and narrating a change of era across the track produces a coherent transition.
- Tempo and key are held precisely. They are stated to be reliable enough to layer a generation against other material, which makes them worth specifying whenever the output has to fit something else.
- The model follows instructions about time. Narrating an arrangement in order works, and the small words carry it.
- More detail is not always better. The owner notes that short evocative prompts produce more creative results, so detail is a control-versus-surprise trade rather than a quality ladder.
- Vocals are the default. A track without singing has to ask for instrumental explicitly.

## Prompt structure

<rules id="structure">

- Settle the five questions before writing: genre, mood, instrumentation, tempo, production era.
- Give each instrument a character rather than a name alone. "Filtered disco sample chops" and "sidechained bass" say more than "samples" and "bass".
- State tempo as a number with BPM, and state the key when the output has to sit alongside other material.
- Name the production treatment or the room. Where you lack the studio term, describe the space in plain words.
- Direct vocal delivery with expressive words: whispered, belted, conversational, deadpan, stacked harmonies. Multiple singers can be requested directly.
- Narrate arrangement in order and mark the silences. The load-bearing words are small ones: start with, just, then, bring in. Without "just", the model fills the space you meant to leave empty.
- Ask for instrumental explicitly when you do not want lyrics, and place vocals in time with timing cues when you do.
- For an isolated part, lead with "solo" for an instrument or "a cappella" for a vocal, and add key, tempo and tone.

</rules>

<example use_case="all five questions answered">

```text
French house, 122 BPM, filtered disco sample chops, sidechained bass, tight four-on-the-floor kick, rooftop-at-sunset mood, warm analog glue
```

*Why: the owner's own contrast against "upbeat electronic track". Genre, tempo, instrumentation, mood and production treatment are each decided by a person, so none of them is decided by the average of the training data.*

</example>

<example use_case="the same song in a different room">

```text
slow soul ballad, 68 BPM, female vocal - cavernous plate reverb, tape echo throws, gospel room
```

*Why: the owner's own demonstration that production words alone change the result. Genre, tempo and vocal are held constant; only the treatment moves, and the track moves with it.*

</example>

<example use_case="narrated arrangement">

```text
UK garage, 132 BPM - start with just a shuffled drum loop, add a warm sub bassline after four bars, then bring in chopped vocal stabs for the drop
```

*Why: the owner's example of time control. "Start with just" is what keeps the opening sparse; drop the "just" and the model fills the gap with material you never asked for.*

</example>

## Composition plans

The structured register. A plan is an ordered list of sections, each carrying its own text, length and style lists.

<rules id="plans">

- Each section has a text field, a duration, a list of styles to include and a list of styles to avoid, plus a setting for how closely it should follow its neighbours.
- The FIRST section's styles set the tone and genre for the whole song. Load them: half a dozen or so descriptors in the early sections until the direction is established.
- Generic quality descriptors are reasonable filler at the end of a style list rather than something to avoid.
- Inside a section's text, three bracket families do three different jobs. `[Section Name]` labels the part, `(parentheses)` carry phonetic vocal sounds such as `(ooh)` or `(hmmm hmmm)`, and `{curly braces}` carry short inline directions such as `{guitar solo}` or `{instrumental break}`.
- Keep the braces for short cues only. Anything describing the whole section, such as genre, instrumentation or overall vocal style, belongs in the style list instead.
- Do not put a broad characteristic in parentheses. Writing `(soft female vocals)` in the text is the owner's own example of the wrong place; that belongs in the styles.
- Styles are written in English even when the lyrics are not.
- A plan can be generated from a plain prompt and then edited, which is usually easier than authoring one from nothing.
- Sections can reference audio from an existing song, which is how a part is kept unchanged while its neighbours are regenerated.

</rules>

<example use_case="section text with all three bracket families">

```text
[Verse]
I've been waiting
{instrumental break}
for you
```

*Why: the owner's corrected example. The section label is bracketed, the short cue is in braces, and the vocal characterisation that a beginner would put in parentheses here has been moved out to the section's style list where it governs the whole part.*

</example>

## Sound effects and loops

<rules id="sfx">

- Describe simple effects plainly: the object, the action and the surface are usually enough.
- For a sequence, describe the events in order in one prompt rather than generating and splicing.
- The model also makes musical fragments, so a drum loop, a brass stab or a synth pad can be asked for here with a tempo and a key.
- Use the trade vocabulary. Impact, whoosh, ambience, one-shot, loop, stem, braam, glitch and drone are all understood and each names a shape rather than a source.
- Keep the requested length short. Effects are brief, and asking for a long one produces padding.
- A loop is an exercise in exclusion. State the bars, the tempo and the key, then state what must not be there.
- For sequences needing exact timing, generate the parts separately and assemble them, which is the owner's own advice.

</rules>

<example use_case="sequence in one prompt">

```text
Footsteps on gravel, then a metallic door opens
```

*Why: the owner's example of a multi-part effect. The word "then" is doing the sequencing, which is enough for two events; a longer chain is better generated in pieces and layered.*

</example>

<example use_case="loop defined by what it excludes">

```text
boom bap drum break, 90 BPM, dusty and swung, four bars, no melody - just drums
```

*Why: the owner's own example, and the clearest case in this whole guide set where a negative is the right tool. "No melody, just drums" is what keeps a drum break a drum break; phrased positively it would drift into a beat with a tune on top.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Exclusions are supported and encouraged here, which makes this scheme an exception among the audio models in this set.
- A composition plan gives each section its own list of styles to avoid, and the owner's advice is to use it liberally to prevent unwanted sounds.
- In a plain prompt, write the exclusion in words. "No melody", "instrumental only", "no drums until the second half" all do real work.
- For loops, exclusion is the primary technique rather than a fallback. The owner's framing is that the negative space IS the prompt.
- Exclusion also controls time: "instrumental only after 1:45" removes vocals from a span rather than from the whole track.
- The general positive-phrasing default does not apply here. Where a loaded guide and a general rule disagree, this guide governs.

</rules>

## Pitfalls and anti-patterns

- Leaving the five questions open: an unanswered question is answered for you with the most average option available.
- Naming instruments without character: a list of instruments produces a generic arrangement. Say how each one sounds.
- Omitting "just" when narrating an arrangement: without it the model fills the silence you meant to leave.
- Expecting an instrumental by default: vocals are the default, and instrumental must be requested.
- Putting a whole-section characteristic in parentheses inside plan text: parentheses are for phonetic vocal sounds, braces are for short cues, and broad description belongs in the style list.
- Using braces for something long: they are inline cues, not a second description field.
- Underloading the first section of a plan: its styles set the tone for everything after it, so a thin first section weakens the whole song.
- Writing styles in another language: styles are English even when the lyrics are not.
- Carrying speech audio tags into a music prompt: they are a different scheme, and voice-only tag rules do not apply here.
- Avoiding negatives out of habit: this is the one audio scheme in the set where exclusion is a documented primary technique.
- Maximising prompt length by reflex: short evocative prompts are documented to give more creative results, so length is a choice about control rather than quality.
- Asking for a long sound effect: effects are short by design, and a long request pads rather than extends.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (ElevenLabs): the [music best practices guide](https://elevenlabs.io/docs/overview/capabilities/music/best-practices), which is the source of the five questions, the production vocabulary material, the era and arrangement techniques, the loop-by-exclusion framing, the timing cues and the isolation prefixes, together with every verbatim music example here; the [composition plans guide](https://elevenlabs.io/docs/eleven-api/guides/how-to/music/composition-plans) for the section structure, the three bracket families and the corrected text example; the [Eleven Music overview](https://elevenlabs.io/docs/overview/capabilities/music) for audio reference and finetunes; the [sound effects guide](https://elevenlabs.io/docs/overview/capabilities/sound-effects) for the simple, sequence and musical-element patterns and the trade vocabulary; the [models overview](https://elevenlabs.io/docs/overview/models) for the line-up and the music model's language statement.

Coverage note: music and sound effects are merged into one guide because both take a describe-the-sound prompt and the two models overlap in practice, with the effects model generating musical fragments and the music model doing sound design. This is the same reasoning that keeps Stable Audio's music and effects in one guide. The negatives section is deliberately at odds with the general positive-phrasing preference that applies elsewhere in this set: this owner documents a dedicated negative field per section and treats exclusion as the primary technique for loops, so the guide governs.

Last verified: 2026-08-30.
