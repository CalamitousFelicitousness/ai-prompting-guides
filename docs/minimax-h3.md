---
guide: "MiniMax H3"
prompt_scheme: "minimax-h3"
models:
  - { id: "h3-base-fl2va", access: "open-weights", tier: "base", caps: [text-to-video, image-to-video, keyframe-interpolation, native-audio, dialogue, text-rendering], best_for: "text-only generation and keyframe work; the four modes T2VA, I2VA, FL2VA, and L2VA, covering pure text, a first frame, a first and last frame pair, or a last frame alone" }
  - { id: "h3-base-ref2va", access: "open-weights", tier: "std", caps: [reference-to-video, video-editing, video-continuation, native-audio, dialogue, text-rendering], best_for: "omni-reference work; identity and style locking, motion transfer, voice-timbre reference, video editing, and continuation, mixing image, video, and audio references in one request" }
capabilities: [text-to-video, image-to-video, keyframe-interpolation, reference-to-video, video-editing, video-continuation, native-audio, dialogue, text-rendering]
prompt:
  languages: ["en"]
  dialogue_languages: ["ar", "zh", "en", "fr", "de", "it", "ja", "ko", "pt", "ru", "es"]
  form: "two layers; hosted surfaces accept free-form prose and rewrite it, while the model itself consumes a structured field format, so write prose for exploration and the structured form when the rewrite must stop guessing"
  formula: "base modes use an optional keyframe-alignment line, then integrated_multimodal_description, overall_soundscape, and non_diegetic_music in that order; full-reference mode uses subject_definitions, summary, retention_analysis, detailed_description, overall_soundscape, and non_diegetic_music"
  literal_text: "put any words visible on screen in straight double quotes and preserve the original language and punctuation verbatim, never translated"
  length_strategy: "write the body long and shot by shot; the owner's own target for a full-reference body is roughly 350 to 500 English words, and dialogue-heavy work should fit the complete spoken timeline rather than hit a word count"
  auto_expand_behavior: "a preprocessing stage rewrites free-form input into the structured representation before generation, and it will invent whatever you left unspecified; write the structured form yourself to take that decision back"
  negatives: "no negative field; write exclusions as ordinary prose sentences inside the prompt, which the model follows unusually well"
  references: "label every input and give each one exactly one job; the structured form uses <Picture N>, <Video N>, <Audio N>, and <Subject N>, and the labels keep the same meaning in every section"
  dialogue: "wrap spoken and sung lines in <d>[Language] ...</d>, keep everything outside the tag (speaker, action, delivery) in English, and give each vocal source a stable (S1), (S2) ID"
sources:
  official: ["https://github.com/MiniMax-AI/MiniMax-H3", "https://huggingface.co/MiniMaxAI/MiniMax-H3", "https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md", "https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md"]
  provider: ["https://fal.ai/learn/devs/minimax-h3-prompting-guide", "https://fal.ai/minimax-h3", "https://wavespeed.ai/blog/video-model-access/minimax-h3-api-guide/"]
  community: []
last_verified: "2026-08-06"
---

# MiniMax H3: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- H3 generates video and audio together from one prompt. Sound is not an afterthought here: two of the required fields are audio fields, and leaving them empty hands the whole soundtrack to the model.
- Write the prompt body in English. The only text that keeps its original language is dialogue and lyrics inside `<d>`, and words that are visibly on screen.
- Two prompt forms are valid, and they are layers of one pipeline, not rivals. See "Two ways to prompt H3" before choosing.
- Every input you attach gets a label and exactly one job. ONE ROLE PER INPUT.

</rules>

## TL;DR

<template id="quickstart">

```text
integrated_multimodal_description: [Shot 1] {style}, {shot size} of {subject with appearance}, {setting}. The camera {motion type} {amplitude} {speed} as {action}. {Speaker description} (S1) says: <d>[{Language}] {exact line}</d> [Shot 2] At {MM:SS.mmm}, the camera cuts to {new shot and what changed}.

overall_soundscape: {ambient sound}, {physical action sounds}, {non-verbal human sounds}.

non_diegetic_music: {instrumentation}, {tempo}, {how it develops or fades}.
```

</template>

## Models and when to use which

H3 ships as two checkpoints covering five modes. They share one prompt grammar: shots, camera language, speakers, dialogue, and the two audio fields are written identically in both. What changes is the field layout of the wrapper and the labels available.

- `h3-base-fl2va`: text and keyframe work, covering four modes. **T2VA** builds the whole audiovisual timeline from text alone. **I2VA** starts from a supplied first frame and develops forward. **FL2VA** describes the continuous path between a supplied first and last frame. **L2VA** infers a plausible opening and converges on a supplied final frame.
- `h3-base-ref2va`: omni-reference work. Takes image, video, and audio references together and covers identity locking, style and motion transfer, voice-timbre reference, editing an existing video, and continuing from one.

Pick by what you are holding. No media means T2VA. An image that literally is the first or last frame of the shot means a keyframe mode. Anything you are treating as a reference rather than a frame, a face to preserve, a clip to match, a track to sing along to, or footage to edit, means Ref2VA.

## Two ways to prompt H3

This is the thing to understand before writing anything. H3 generates from a structured representation, not from your prose. A preprocessing stage sits in front of the model, reads whatever you sent, and rewrites it into that representation. So there are two places to stand.

<rules id="layers">

- Free-form prose is the working default on hosted surfaces. Write ordinary paragraphs, attach your references, and let the rewrite build the structure. Good for exploration and for prompts you would otherwise never finish.
- The structured form is what the model actually consumes. Write it yourself when the rewrite keeps inventing details you did not ask for, when timing must be exact, when dialogue must be word-perfect, or when you are driving the base model directly.
- The rewrite fills gaps. Anything you leave unspecified, it will decide: shot count, cut times, camera moves, ambience, whether there is music at all. That is convenience when you are exploring and a liability when you are not.
- The two forms are not rivals, so do not mix them halfway. Either write clean prose and let the rewrite work, or write the full structured form with its fields in order.
- The structured tags are real parsed tokens, not documentation shorthand. `<d>` is registered in the model's tokenizer, so spell the tags exactly as written here.

</rules>

## How the model reads prompts

- It reads cinematography vocabulary directly. Lens choice, movement, exposure behavior, and film-stock character all translate, so use the real words rather than describing the effect you hope they produce.
- It reads a timeline, not a mood. The body is written shot by shot in playback order, and every detail should correspond to something visible or audible at a specific moment.
- It follows negative direction unusually well. There is no negative field, so exclusions are ordinary sentences in the prompt, and they work.
- It treats audio as a first-class output. Ambience, physical sound, dialogue, and score are separate concerns written in separate places.
- Long is normal. A full shot list with sound design belongs in one prompt, and a single shot does not justify a thin description.
- Multi-beat prompts drift into a slideshow when the timing is vague. Timed shots are the fix.

## Prompt structure: base modes

Base-mode prompts are an optional alignment line, then three fields in a fixed order.

<rules id="structure">

- If you supplied a keyframe, the alignment instruction is the first line of the prompt, followed by one blank line before the fields.
- Then `integrated_multimodal_description`, then `overall_soundscape`, then `non_diegetic_music`, in that order. Keep the field names exactly.
- `integrated_multimodal_description` carries visuals, actions, shots, speakers, dialogue, and sound tied to a moment. It is the main body.
- `overall_soundscape` summarizes ambience, physical action sound, and non-verbal human sound across the whole video.
- `non_diegetic_music` describes score the characters cannot hear. Use `N/A` when there is none.
- T2VA has no alignment line and starts directly at the first field.

</rules>

<template id="alignment">

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

</template>

*The I2VA form. For FL2VA and L2VA, use: `How the reference pictures align with the target video - <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video`, where `N` is the actual final shot and `S.SS` is the effective duration to exactly two decimals. Owner examples print this label both with and without the angle brackets; both are accepted.*

## Shots, cuts, and timing

<rules id="shots">

- Open with `[Shot 1]` and give it no timestamp. Every later shot gets a strictly increasing cut time inside the video's duration: `[Shot 2] At 00:03.500, ...`.
- State the overall style and the initial composition at the start of `[Shot 1]`. Common anchors: `Cinematic`, `live-action`, `2D-animated`, `3D CG`, `claymation`, `watercolor`, `vintage film`. Derive it from the reference image for keyframe modes, from the text for T2VA.
- Phrase cuts as `the camera cuts to`, `the shot cuts to`, `the shot transitions to`, `the shot changes to`, or `the shot switches to`. Cross-dissolve, fade, and wipe are for when the user asked for them.
- A cut must introduce new information: a new subject, space, state, viewpoint, or time. If only the distance or angle changes slightly, move the camera instead of cutting.
- Describe an unusual transition as a physical event rather than naming an effect. Written-out actions land better than effect names.

</rules>

## Camera motion

Write camera motion as natural English inside the shot, never as labels stacked at the end of a sentence. A complete expression has three dimensions: motion type, amplitude, and speed. Add amplitude and speed only when they matter, since medium amplitude at normal speed is the assumed default.

| Dimension | Expression |
| --- | --- |
| Motion type | `Zoom In / Zoom Out` (focal length changes, body still) |
| Motion type | `Push In / Pull Out` (camera moves forward or back) |
| Motion type | `Pan Left / Pan Right` (pivots horizontally in place) |
| Motion type | `Truck Left / Truck Right` (translates horizontally) |
| Motion type | `Tilt Up / Tilt Down` (pivots vertically in place) |
| Motion type | `Pedestal Up / Pedestal Down` (whole camera rises or drops) |
| Motion type | `Arc Shot` (moves in an arc around the subject) |
| Motion type | `Tracking Shot` (follows a moving subject) |
| Motion type | `Static Shot` (position and lens hold) |
| Motion type | `Shake Slightly / Shake Strongly` |
| Motion type | `POV` (the subject's point of view) |
| Motion type | `Roll Clockwise / Roll Counterclockwise` |
| Amplitude | `with small amplitude`, `with large amplitude` |
| Speed | `at slow speed`, `at fast speed` |

<example use_case="camera-phrasing">

```text
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

*Why: each move is a verb inside the action rather than a label appended to it, and amplitude and speed appear only where they change the read*

</example>

## Speakers, dialogue, and singing

This is the most exacting part of the format, and the part that pays off most, because H3 lip-syncs and voices what you write.

<rules id="dialogue">

- Give every vocal source a stable ID: `(S1)`, `(S2)`, and so on. An ID belongs to a speaker for the whole video. Characters who never vocalize get no ID.
- When several already-numbered speakers vocalize together, use a compound ID such as `(S1,S2)`.
- On a speaker's first appearance, establish a stable identity: character type, age, gender, whether they are on screen, pitch, timbre, speaking rate, accent.
- Keep the speaker phrase, the ID, the action, and the delivery OUTSIDE `<d>`. Inside `<d>`, put only the language tag and the literal spoken words.
- Preserve every original word and punctuation mark inside `<d>` verbatim. Do not translate or rewrite. Write `[unclear]` for spans you genuinely cannot make out rather than guessing.
- For voiceover use the exact phrase `says in an off-screen voiceover`, and immediately after the `<d>` block state that the on-screen character's lips stay closed.
- When one line crosses a cut, mark `<scenetrans>` at the connecting point in both parts and say the audio continues across the cut. Use `<cutoff>` when the video ends mid-speech.

</rules>

<example use_case="dialogue-basic">

```text
The young woman with a quiet, breathy voice (S1) says: <d>[English] I get off at the next station.</d>
The two children (S1,S2) shout together, <d>[English] Wait for us!</d>
```

*Why: identity, ID, and delivery sit outside the tag while the tag holds only the language and the exact words, which is what keeps the spoken line from being paraphrased*

</example>

<example use_case="voiceover">

```text
The man (S1) says in an off-screen voiceover: <d>[English] I still remember that road.</d> while his lips remain completely closed.
```

*Why: the fixed voiceover phrase plus the explicit closed-lips note stops the model from animating a mouth to match narration that is not being spoken on camera*

</example>

## On-screen text

<rules id="text">

- Put any banner, sign, label, subtitle, or neon text that is actually visible in straight double quotes.
- Preserve the original text and punctuation verbatim, without translation, exactly as with dialogue.

</rules>

<example use_case="on-screen-sign">

```text
A red neon sign reading "营业中" glows above the doorway.
```

*Why: the quoted string is reproduced as-is in its own script rather than translated into the English body around it*

</example>

## The two audio fields

<rules id="audio">

- `overall_soundscape`: one continuous paragraph of one to four English sentences covering ambience, physical action sound, and non-verbal human sound across the whole video. Wind, rain, traffic, footsteps, fabric, impacts, breathing, laughter, panting.
- Do not repeat dialogue, singing, or diegetic music here. Those live in the body, tied to their moment. Use `N/A` only when the user explicitly asked for total silence.
- `non_diegetic_music`: one to three sentences on score only the audience hears. Name instrumentation, tempo, rhythm, and how the dynamics change.
- Do not write mood words or explain what the music is doing emotionally. Describe the music itself.
- Sound a character can hear, singing, a radio, a television, a phone, is diegetic and belongs in the body, not here. Use `N/A` when there is no score.

</rules>

<example use_case="audio-fields">

```text
overall_soundscape: Steady rain taps against the cafe windows while low room ambience continues underneath. The entrance bell rings once, followed by wet footsteps and the soft scrape of a chair.

non_diegetic_music: Sparse piano notes at a slow tempo, joined by sustained low strings that gradually increase in volume before fading out.
```

*Why: the soundscape lists physical sources rather than an atmosphere, and the score is described by instrument, tempo, and dynamic movement instead of by the feeling it is supposed to create*

</example>

## By mode

### T2VA, text only

<example use_case="t2va">

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium-wide shot frames a baker opening the shutters of a small street bakery before sunrise. The camera pushes in with small amplitude at slow speed as the middle-aged baker with a calm, slightly raspy voice (S1) places a fresh loaf on the wooden counter and says: <d>[English] First batch of the morning.</d> [Shot 2] At 00:05.000, the camera cuts to a close-up of steam rising from the sliced bread while the baker's final words carry over from the previous shot.

overall_soundscape: Wooden shutters scrape open over a quiet street as trays clink softly inside the bakery. The doorbell rings once, followed by light footsteps and the crisp sound of bread being sliced.

non_diegetic_music: A soft acoustic-guitar pattern at a moderate tempo, joined by sparse upright-bass notes and a gentle fade at the end.
```

*Why: style and shot size open the body, one speaker is established with a voice description before speaking, the second shot carries a real cut time, and the dialogue is explicitly held across the cut*

</example>

### I2VA, develop forward from a first frame

`<Picture 1>` is the actual first frame at 0.00 seconds and belongs to `[Shot 1]`. Establish the style, subjects, composition, and scene anchors from the image first, then describe the next action. Identity, clothing, colors, key objects, and spatial relationships stay consistent. Shape: **first-frame anchor, action onset, continuous development, result or reaction**.

<example use_case="i2va">

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, the young woman shown in <Picture 1> remains beside the rain-covered train window, preserving her appearance, clothing, seat position, and the carriage layout. The camera trucks right with small amplitude at slow speed as she lifts her gaze from the folded letter toward the passing city lights. Her reflection moves across the glass while the quiet, breathy young woman (S1) says: <d>[English] I get off at the next station.</d> She folds the letter along its existing crease.

overall_soundscape: The train wheels produce a steady metallic rhythm beneath a low ventilation hum. Rain ticks against the window while paper rustles softly in her hands.

non_diegetic_music: Sustained cello notes at a slow tempo with widely spaced piano tones, gradually decreasing in volume.
```

*Why: the alignment line pins the image to time zero, the body names what carries over from it explicitly before moving, and only then does the action start*

</example>

### FL2VA, the path between two frames

Picture 1 is the opening and Picture 2 is the ending. Do not restate two static images; supply the motion that connects them. Favor a single shot so the model can interpolate continuously, and use multiple shots only when asked. The last frame must be reached at the end of the final shot. Shape: **first-frame state, observable intermediate changes, progressively narrowing differences, last-frame state**.

<example use_case="fl2va">

```text
How the reference pictures align with the target video - Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a rain-soaked cyclist begins in the position and framing established by Picture 1, holding a closed black umbrella beside a silver bicycle. The camera pulls out with small amplitude at slow speed as she releases the bicycle handle, raises the umbrella above her shoulder, and presses the runner upward until the canopy opens. Water rolls from the expanding fabric while she steps beneath it, rotates the handle into the final angle, and settles into the pose, spacing, and composition established by Picture 2 at the end of the shot.

overall_soundscape: Rain falls steadily on the pavement, followed by the metallic click of the umbrella runner and the soft snap of the canopy opening. Water drips from the bicycle frame as distant traffic passes.

non_diegetic_music: N/A
```

*Why: one continuous shot describing a single mechanical action from start state to end state, with the final clause landing explicitly on Picture 2's composition, and N/A used rather than inventing a score*

</example>

### L2VA, converge on a final frame

`<Picture 1>` is the final frame and belongs to the last `[Shot N]`, not to Shot 1. Infer a plausible earlier state from the user's intent and the image, then describe how characters, objects, camera, and scene approach it. Shape: **plausible preceding state, explicit action and transition path, gradual convergence, last-frame landing**.

<example use_case="l2va">

```text
How the reference pictures align with the target video - <Picture 1> (from [Shot 1]) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a close shot begins with an intact drinking glass near the edge of a dark wooden table, while the same hand and sleeve visible in <Picture 1> approach from the right. The camera pushes in with small amplitude at slow speed as the fingertips strike the rim. The glass tips, falls, and hits the floor with a sharp impact; cracks spread through it as fragments slide outward. Toward the end, the moving pieces lose momentum and settle into the exact broken arrangement, hand position, camera angle, lighting, and final composition established by <Picture 1>.

overall_soundscape: Fingertips tap the glass before it scrapes across the tabletop, falls, and breaks with a sharp crash. Small fragments scatter and gradually stop sliding across the floor.

non_diegetic_music: A low electronic pulse at a slow tempo, ending immediately after the glass breaks.
```

*Why: the shot runs an irreversible physical process forward and lets it come to rest exactly on the supplied end state, which is what makes a last-frame anchor land instead of jump-cutting to it*

</example>

## Full-reference mode

Ref2VA replaces the three fields with six sections, in this order. Everything above about shots, camera, speakers, dialogue, and the two audio fields still applies unchanged.

| Section | Purpose |
| --- | --- |
| `subject_definitions` | Defines referenced content and its labels |
| `summary` | Task type, target video, main reference relationships |
| `retention_analysis` | How each reference is preserved, transferred, or reused |
| `detailed_description` | Visuals, actions, shots, sound, dialogue in playback order |
| `overall_soundscape` | Ambience and physical sound |
| `non_diegetic_music` | Audience-only score |

### Labels

<rules id="labels">

- `<Subject N>`: visible content that gets reused or modified. People, animals, objects, scenes, backgrounds, clothing, props, interfaces, effects, styles, actions, expressions, poses. It is a content unit, not a file.
- `<Picture N>`: an image used as a concrete frame or a shot-planning anchor.
- `<Video N>`: a video providing an editing source, a continuation start, or whole-video structure such as camera movement, cuts, or rhythm.
- `<Audio N>`: an audio signal that is copied or referenced.
- A label keeps the same meaning in every section once assigned. Never redefine it, never introduce a new one in `summary`.
- If an image only defines a character, scene, costume, or style, do NOT give it a standalone `<Picture N>` entry. Cite it inside that `<Subject N>` definition instead.
- One subject may draw on several assets, and one asset may supply several subjects. Say which asset provides what.
- Video and audio labels are numbered independently, so `<Video 1>` and `<Audio 2>` can be the same source file. A reference video does not automatically create an `<Audio N>` just because it has sound.

</rules>

<example use_case="subject-definitions">

```text
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose walking motion comes from <Video 1>.
<Picture 3> is a storyboard reference for [Shot 1] and [Shot 2], defining their viewpoint, subject placement, and shot order.
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

*Why: one subject is welded to two different assets with each contributing a named property, the storyboard image declares which shots it governs, and the audio label reuses the speaker ID rather than minting a new one*

</example>

### Task type and retention

<rules id="retention">

- `summary` opens with a square-bracketed task-type prefix. Combine types with ` + ` and never repeat one: `[video editing + audio reuse]`, `[video continuation + keyframe completion]`.
- Types: `keyframe completion` (an image is a concrete frame anchor), `reference generation` (guidance for character, scene, style, action, camera, storyboard), `video editing` (a source video is directly modified), `video continuation` (new content extends an existing video), `audio reuse` (the same signal is reused), `audio reference` (only style, timbre, content, texture, beat, or continuity is referenced).
- The mere presence of a video or audio file does not create its task type. A video that only supplies camera movement or rhythm is `reference generation`.
- For an edit, begin the summary after the prefix with: `The target video is an edited version of <Video 1>.`
- `retention_analysis` gives one line per label with a fixed marker. Visible content uses `fully_preserved`, `partially_preserved`, `attribute_transfer`, or `weak_reference`. Audio uses `fully_copy`, `partially_copy`, `reference`, or `weak_reference`.
- Choose a marker only within the role you already gave that label. New actions or backgrounds added to the target are not losses of fidelity.
- Do not write speaker IDs in `retention_analysis`.

</rules>

### Writing the body

<rules id="ref-body">

- Establish style in one or two English sentences BEFORE `[Shot 1]`, unlike base modes where it opens the first shot.
- Aim for roughly 350 to 500 English words for a generation task. Dialogue-heavy work should fit the complete spoken timeline instead of chasing a count. Editing descriptions scale with the source video.
- At a subject's first clear appearance, describe its referenced characteristics, its position in frame, and its current action. Reuse the label afterward without redefining it.
- Anchor frames with natural phrasing: `the shot begins from <Picture 1>`, `the shot's keyframe corresponds to <Picture 2>`, `the shot ends on <Picture 3>`.
- When a referenced subject speaks, keep both labels: `<Subject 2> (S1)`. The subject label says who it is; the speaker ID says who is talking.
- Assign speaker IDs once, in the order vocal events actually happen in the target video.
- When a voice exists only inside reused music, cite `<Audio N>` as the source and do not invent a speaker ID. A real person, character, or narrator gets an ID.
- Do not reduce the body to a plot summary or a list of reference relationships. It has to describe what is on screen.

</rules>

<example use_case="ref2va-flagship">

```text
subject_definitions:
<Subject 1> is the coffee-shop environment in <Picture 1>, featuring an exposed brick wall, an orange tufted sofa with patterned pillows, a neon sign, and a wooden coffee table.
<Subject 2> is the fluffy white Samoyed in <Picture 2>, <Picture 3>, and <Picture 4>, with thick white fur, pointed ears, a dark nose, and a curved tail.
<Subject 3> is the young blonde woman in <Video 1>, with long blonde hair and a light-pink button-down shirt with rolled-up sleeves.
<Subject 4> is the young man in <Video 2>, with short wavy brown hair and a dark-grey hoodie with drawstrings.
<Audio 1> is the voice-timbre reference for <Subject 3> (S1), containing a spoken English vocal layer.

summary:
[reference generation + audio reference] The target video shows <Subject 3> eating a cookie in <Subject 1>. <Subject 4> enters with <Subject 2>, which lunges toward the cookie. The three-shot exchange uses <Audio 1> as the voice-timbre reference for <Subject 3> and ends with a canned audience laugh.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table are retained.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the Samoyed's thick white fur, pointed ears, dark nose, and curved tail are retained.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the blonde woman's identity, long hair, and light-pink shirt are retained.
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the young man's short wavy brown hair and dark-grey hoodie are retained.
<Audio 1>: reference - its vocal timbre guides the dialogue delivery of <Subject 3> without copying the original signal.

detailed_description:
The target video uses a realistic multi-camera sitcom style with warm indoor lighting.
[Shot 1] A medium shot establishes <Subject 1>, the coffee shop with its exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table. <Subject 3> (S1), the young woman with long blonde hair and a light-pink button-down shirt with rolled-up sleeves, sits on the sofa holding a chocolate-chip cookie. From the left, <Subject 4>, the young man with short wavy brown hair and a dark-grey hoodie with drawstrings, enters holding the leash of <Subject 2>, the thick-furred white Samoyed with pointed ears, a dark nose, and a curved tail. The dog lunges toward the cookie and pulls the leash taut. <Subject 3> (S1) jerks her hand back and, using the clear youthful voice timbre referenced from <Audio 1>, exclaims with light annoyance, <d>[English] Hey! Watch your dog!</d> She closes her lips and guards the cookie while <Subject 4> pulls the dog back.
[Shot 2] At 00:03.000, the shot cuts to a close-up of <Subject 4> (S2), the young man in the dark-grey hoodie from Shot 1, sitting beside <Subject 3> on the sofa and holding <Subject 2> securely in his arms. <Subject 4> (S2) says in a casual young male voice with a playful tone and an easy conversational pace, <d>[English] He just likes cookies more than me.</d> He closes his mouth into an apologetic smile and strokes the dog's thick white fur.
[Shot 3] At 00:05.000, the shot cuts to a close-up of <Subject 3> (S1), the blonde woman in the light-pink shirt from Shot 1. Her annoyance softens as she looks toward the Samoyed. <Subject 3> (S1) replies in the same clear youthful voice referenced from <Audio 1> with an amused cadence, <d>[English] Well, he has good taste at least.</d> She smiles and raises the cookie in a small toast-like gesture. A classic canned audience laugh begins immediately after the line and continues through the final frame.

overall_soundscape:
Soft indoor coffee-shop room tone continues throughout the scene.

non_diegetic_music:
N/A
```

*Why: the long flagship for the format, six inputs each welded to one job across four subjects and one audio reference, every label defined once and reused unchanged through all six sections, two speakers assigned in the order they actually speak, and the audio marked `reference` rather than `fully_copy` because only its timbre is borrowed*

</example>

## Free-form prompting

When you are working through a hosted surface that rewrites for you, plain prose is the normal way in. It is also how most published example prompts for this model are written. The structure below is what makes prose survive the rewrite intact.

<rules id="freeform">

- Assign a job to every reference, in the prompt text. This is the single highest-value habit, and it works across modalities. NAME WHAT MOVES, PIN WHAT STAYS.
- Order the paragraphs: reference jobs, then story and action, then style and visual language, then audio direction, then exclusions.
- Write a timed shot list for anything longer than one beat, or the result drifts into a slideshow.
- Direct the audio as specifically as the picture. Itemize sound sources; for music, name instrumentation and place events on the clock.
- Lock identity by enumerating features, not adjectives. A list of concrete attributes gives the model something to hold; "beautiful" does not. The same works for products, sets, and typography.
- For edits, pair every change with what must stay stable, in the same breath. That is what makes it a local edit rather than a regenerated shot.
- Put duration and aspect ratio in the prompt text.
- State what you do not want, in prose. Exclusions are unusually effective on this model.

</rules>

<example use_case="freeform-reference-jobs">

```text
Match the Hitchcock-style camera move in Video 1. Make the subject in Video 2 sing, using Video 3 as the reference for both the vocal performance and physical delivery.
```

*Why: three video inputs and three disjoint jobs, camera from one, identity from another, performance from a third, so nothing is left for the rewrite to assign arbitrarily; ONE ROLE PER INPUT in its shortest possible form*

</example>

<example use_case="freeform-selective-edit">

```text
Preserve the buildings, pedestrians, and overall environment in Video 1 as photoreal live action. Transform only the trees and cars into 3D pixel-art or voxel-block objects in the style of Minecraft, using Image 1 as the visual reference. Keep their motion physically correct, and preserve the real environment's shadows and transmitted light.
```

*Why: the preserve list comes first and the word "only" scopes the transformation, then the physics and lighting continuity clauses stop the changed objects from detaching from the plate*

</example>

<example use_case="freeform-substitution-list">

```text
In the reference video: replace the newspaper with a green hardcover book; replace the chair with a red sofa; remove the subject's sunglasses and reveal a clear face; remove the burning-car effect and restore the vehicle to normal; replace the photograph taken from the coat with a small black notebook; and add a tree on the left side of frame.
```

*Why: six edits as one semicolon-chained substitution list, each naming its target concretely, which reads as a work order rather than a new scene description*

</example>

<example use_case="freeform-timed-shot-list">

```text
Use Image 1 for the character and Image 2 for the UI style.

[0-2 seconds] High-angle overhead shot. The character sits on a vivid, highly saturated purple floor, looks up at camera, and matches Image 1. A game menu appears on the right: START NEW GAME, CONTINUE (highlighted), SETTINGS, EXIT GAME. Player profile MINIMAX appears top left. The cursor selects CONTINUE.

[2-4 seconds] Smoothly push in to her right arm. A RIGHT ARM EQUIPMENT panel slides in from the right. PHANTOM GRIP is selected, then the selection moves to CHRONOS CLAW. Her mechanical hand reconfigures: fingers separate, new claw-like joints lock into place, and cyan LEDs flare brighter.

[4-7 seconds] Arc smoothly to her left. An ARMAMENT CUSTOMIZATION grid slides in, showing hand, forearm, elbow, and upper-arm components. The selector cycles rapidly. Her left arm disassembles section by section: the forearm plate releases, new armor slides in, the elbow joint swaps, and the hand reconfigures, with exposed wiring and pistons visible during the change.

[7-8.5 seconds] Pull back to a medium shot. CONFIRM CONFIG flashes; click it. All UI panels collapse inward and vanish. She uncrosses her legs and settles into a relaxed seated pose with one knee raised, lifting the prosthetic hand for a subtle post-configuration movement.
```

*Why: reference jobs first, then every beat pinned to its own time window with a camera move and a concrete state change, which is what stops a long multi-beat prompt from collapsing into a slideshow*

</example>

<example use_case="freeform-audio-direction">

```text
BGM: an original 15-second title cue, 60% suspense and 40% jazz. Use a low drone, tense string pizzicato, cool synth pulses, low kick, sparse brushwork, fragments of walking bass, short baritone-sax phrases, and clipped brass accents. Build suspense with low frequencies and hi-hat in the first 2 seconds; bring in the low beat at 3 seconds, jazz-bass movement at 6 seconds, and a short sax/brass riff at 10 seconds. Freeze the final 2 seconds on a tense chord and drum hit. Keep it mysterious and criminally cool, never upbeat, and do not imitate an existing melody.
```

*Why: the score is specified as instrumentation plus a timeline of events on the clock rather than as a mood, and it closes with two exclusions that keep it from drifting upbeat or derivative*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field. Write exclusions as ordinary sentences in the prompt, and expect them to be followed.
- Name the specific drift you are guarding against rather than generic quality words. "No subtitles, on-screen text, or watermarks" and "no sci-fi, period costume, or animation styling" both work; "bad quality" does not.
- Genre drift is the most common thing worth excluding on a stylized prompt, because a strong style pulls the whole scene toward its usual genre.
- In the structured form, exclusions still go in the body as prose. They do not get a field.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Half-structured prompts: field names with prose thrown in between, or tags in an otherwise free-form paragraph. Commit to one form.
- Leaving the audio fields empty: the model still generates sound, it just picks it for you. Write both fields or set `N/A` deliberately.
- Mood words in `non_diegetic_music`: describe instrumentation, tempo, and dynamics; "tense and emotional" gives the model nothing to play.
- Repeating dialogue in the soundscape: spoken and sung lines live in the body only, tied to their moment.
- Slideshow drift: a multi-beat prompt without timing becomes a series of stills. Give every beat after the first a cut time.
- Cutting when you meant to move: if only distance or angle changes, use camera motion. A cut should carry new information.
- Translating what must stay verbatim: dialogue inside `<d>` and on-screen text keep their original language and punctuation. Everything else is English.
- Renumbering speakers: an ID belongs to a source for the whole video, and IDs are assigned in the order vocal events occur. Never mint a new one for the same voice.
- Giving an image a `<Picture N>` entry when it only defines a character or style: cite it inside that subject's definition instead.
- Confusing subject and speaker labels: `<Subject 2> (S1)` means the referenced subject who is also the first speaker. Keep both.
- Plot-summary bodies: "they argue and then make up" describes a story, not a shot. Describe what is visible and audible.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

The owner and the providers appear to disagree, and the disagreement resolves rather than needing a ruling: they describe two layers of one pipeline. The owner's guides document the structured representation the model consumes, while provider examples are free-form prose that a preprocessing stage rewrites into that representation. Both are valid inputs at different points, so this guide teaches both and keeps owner notation canonical for the structured layer. Provider label styles such as plain "Image 1" are recorded as free-form conventions, not as structured syntax. Where a provider's endpoint layout offers fewer modes than the owner documents, this guide follows the owner, since endpoint availability is a provider fact while the prompt shape is not. The full adjudication is in `sources/minimax-h3/minimax-h3-notation-resolution.md`.

- Official (MiniMax): [MiniMax-H3 on GitHub](https://github.com/MiniMax-AI/MiniMax-H3), [MiniMax-H3 on HuggingFace](https://huggingface.co/MiniMaxAI/MiniMax-H3), [base prompt writing guide (T2VA, I2VA, FL2VA, L2VA)](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md), [full-reference prompt writing guide (Ref2VA)](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md).
- Provider: [fal MiniMax H3 prompting guide](https://fal.ai/learn/devs/minimax-h3-prompting-guide), [fal MiniMax H3 overview](https://fal.ai/minimax-h3), [WaveSpeed MiniMax H3 guide](https://wavespeed.ai/blog/video-model-access/minimax-h3-api-guide/).

Last verified: 2026-08-06.
