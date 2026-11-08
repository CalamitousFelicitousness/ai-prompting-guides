---
guide: "Pruna Video (P-Video)"
prompt_scheme: "pruna-video"
# Pruna's own video models. Pruna also sells MiniMax H3 as P-Video-2-Pro and P-Video-2-Pro-Reference (see the MiniMax H3 guide); P-Video-2-Pro-Avatar is built on H3 but has its own fields and is covered here.
models:
  - { id: "p-video-2",             access: "closed-weights", tier: "flagship", caps: [text-to-video, image-to-video, first-last-frame, native-audio, dialogue, singing, audio-to-video, text-rendering], best_for: "Pruna's quality text- and image-to-video: native speech with lip-sync, sung lyrics, sharper close-ups and identity hold, with a voice, music and SFX mix written into the prompt" }
  - { id: "p-video",               access: "closed-weights", tier: "budget",   caps: [text-to-video, image-to-video, native-audio, dialogue, audio-to-video], best_for: "the fastest and cheapest drafts and social clips; same prompt formula as P-Video-2 but weaker lip-sync, close-ups and identity hold, and its prompt is used as written unless the host turns rewriting on" }
  - { id: "p-video-edit",          access: "closed-weights", tier: "std",      caps: [video-edit, reference-image], best_for: "one principal change to existing footage: color, material, product, environment, relighting, object removal, or an object added from a reference still" }
  - { id: "p-video-replace",       access: "closed-weights", tier: "std",      caps: [character-replace, reference-image, lip-sync], best_for: "swapping who appears in a clip while the camera, blocking and background stay; best on normal, controlled motion" }
  - { id: "p-video-2-pro-replace", access: "closed-weights", tier: "std",      caps: [character-replace, lip-sync], best_for: "putting one or two photographed people into a source clip, including fast action; the source soundtrack and voice stay" }
  - { id: "p-video-animate",       access: "closed-weights", tier: "std",      caps: [motion-control, lip-sync], best_for: "making one still move with a driver clip's acting, timing and camera when the still defines the look of the world" }
  - { id: "p-video-avatar",        access: "closed-weights", tier: "std",      caps: [speech-to-video, lip-sync, dialogue], best_for: "spokesperson-style talking video from one portrait and a script or recording, in several languages, voice only" }
  - { id: "p-video-2-pro-avatar",  access: "closed-weights", tier: "std",      caps: [speech-to-video, lip-sync, dialogue, singing], best_for: "talking or singing video from one portrait, painting or character, built on MiniMax H3 but prompted with plain sentences in separate picture and voice fields" }
capabilities: [text-to-video, image-to-video, first-last-frame, native-audio, dialogue, singing, audio-to-video, text-rendering, video-edit, reference-image, character-replace, lip-sync, motion-control, speech-to-video]
prompt:
  languages: ["en"]
  speech_languages: "spoken and sung lines are written in the language they should be heard in; the avatar models take the script in the target language and a delivery note that names the language and accent. Pruna publishes no list for the generation models"
  formula: "Subject, Action, Scene, then optional Camera, Lighting, Style and Audio, in that order. Pruna calls the short version a 'fast pass' (subject, action, scene) and the full version 'locked-in'"
  length_strategy: "short. One or two sentences for a fast pass or a chained segment; a locked-in prompt adds one clause per optional slot and an 'Audio:' sentence. One hero action per clip"
  auto_expand_behavior: "host prompt upsampling. Off by default on P-Video, on by default on P-Video-2, P-Video-Edit and the Pro avatar, where it rewrites the prompt before generation. Turn it off when a prompt must run exactly as written"
  negatives: "no negative field on the generation, edit, replace or animate models; write exclusions inline as short plain statements ('No objects fall or move off the table.', 'No music, no voice.'). P-Video-Avatar alone has an experimental negative field, for burned-in captions"
  dialogue: "speaker, delivery, colon, then the line in double quotes ('She speaks confidently: \"...\"'). Two speakers are labelled by position or number. Sung lyrics go in a 'Lyrics she sings (original): \"...\"' clause, and the Audio sentence points back to 'the lyrics above'"
  references: "edit and replace prompts name stills in words: 'shown in the reference image' (Edit), 'reference image 1' (Replace), 'image 1' or 'the person in the image' (Pro-Replace). No @ tokens"
  avatar_fields: "three free-text fields: the script (the words, in the target language), the voice prompt (how it is said, never spoken) and the picture prompt (on-camera motion and what stays still). Never paste the script into the other two"
sources:
  official: ["https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-2.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-edit.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-replace.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-2-pro-replace.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-animate.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-avatar.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-2-pro-avatar.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/cheatsheet.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/video_generation/advanced.html", "https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/workflows/scene_chaining.html"]
  provider: ["https://wavespeed.ai/models/pruna-ai/p-video-2/text-to-video", "https://wavespeed.ai/models/pruna-ai/p-video-2/image-to-video"]
  community: []
last_verified: "2026-11-08"
---

# Pruna Video (P-Video): prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers Pruna's own video models: P-Video and P-Video-2 for generation, and P-Video-Edit, P-Video-Replace, P-Video-2-Pro-Replace, P-Video-Animate, P-Video-Avatar and P-Video-2-Pro-Avatar for work on existing footage or portraits. Pruna does not name a base model for any of them except P-Video-2-Pro-Avatar.
- P-Video-2-Pro and P-Video-2-Pro-Reference are MiniMax H3 under Pruna's name. Prompt them with the MiniMax H3 guide, not this one.
- Write plain natural language: short clauses or sentences in the formula order. There is no JSON prompt form, no @ token grammar and no bracket tag set.
- Know which free-text field you are filling. Generation and edit models read one prompt; Replace and Animate read an optional instruction; the avatar models read three separate fields with separate jobs.
- Pruna's general video prompting guide was illustrated with WAN 2.2 models, not P-Video. Where it and a P-Video model page differ, follow the model page.

</rules>

## Model names and aliases

Pruna names its products by tier and job, and the names do not say what is underneath. Route by the table, not by the name.

| Pruna name | What it is | Guide |
| --- | --- | --- |
| P-Video | Fast, cheap generation (Pruna's own) | This guide |
| P-Video-2 | Quality generation with native speech (Pruna's own) | This guide |
| P-Video-Edit | Instruction edit of existing footage | This guide |
| P-Video-Replace, P-Video-2-Pro-Replace | Swap people in existing footage | This guide |
| P-Video-Animate | Move one still with a driver clip | This guide |
| P-Video-Avatar, P-Video-2-Pro-Avatar | Talking or singing video from a portrait | This guide |
| P-Video-2-Pro, P-Video-2-Pro-Reference | MiniMax H3 | MiniMax H3 guide |
| P-Image-Ideogram | Ideogram 4.0 caption schema | Ideogram 4 guide |

<rules id="naming">

- "Pro" in a P-Video-2-Pro name means the MiniMax H3 line, not a higher tier of P-Video-2. P-Video-2-Pro generates from text and keyframes; P-Video-2 is a different model.
- P-Video-2-Pro-Avatar is built on H3 but is prompted with this guide's three avatar fields in plain sentences. Do not apply the H3 structured form to it.
- P-Video-Replace and P-Video-Avatar are the faster, cheaper versions of the two Pro task models; the prompts differ, so check which one you are writing for.

</rules>

## TL;DR

<template id="quickstart">

{subject with key attributes}, {action}, {scene}. {camera move or "Static camera"}, {lighting}, {style}. {Speaker} {delivery verb}: "{line}". Audio: {music bed}, {voice quality}, {ambience or SFX}.

</template>

## Models and when to use which

All of them read natural language; what changes is the job and which fields exist. Pruna's own decision guide:

- P-Video-2: "Need the highest generation quality, lip-sync, or audio-conditioned output". Its stated gain over P-Video is "native-speech lip-sync (pause / line / rest), sharper close-ups, and identity lock".
- P-Video: "Need the fastest / cheapest generation iteration". Same formula, but weaker at exactly what P-Video-2 adds, so keep lines short and close-ups few. It uses the prompt as written unless the host turns upsampling on, and some hosts only return its sound when asked to.
- P-Video-Edit: "Footage exists and you need a color, product, environment, object, or text edit". It is "not a character-swap model".
- P-Video-2-Pro-Replace, or the cheaper P-Video-Replace: "Footage exists and you need different people in the same shot".
- P-Video-Animate: "Footage exists and the hero still should move like the driver". Pruna's rule between the two: "Choose Animate when the still defines the world; choose P-Video-2-Pro-Replace when the clip defines the world."
- P-Video-2-Pro-Avatar, or the voice-only P-Video-Avatar: a talking or singing clip from one still.
- Draft modes on P-Video, P-Video-2 and Edit are "a preview: faster and cheaper, lower quality". Iterate there, then rerun the same wording at full quality: "same wording every rerun".

## How the model reads prompts

- THE FORMULA IS A SLOT ORDER, NOT SYNTAX. Subject, Action and Scene carry the clip; Camera, Lighting, Style and Audio are optional enhancements added in that order. Commas or short sentences both work.
- PRUNA SEPARATES A FAST PASS FROM A LOCKED-IN PROMPT. Fast pass: "subject, action, scene. Enough for first looks." Locked-in: "Subject + action + scene + camera, lighting, style, audio; same wording every rerun." Explore with the first, ship with the second.
- UPSAMPLING DECIDES WHETHER YOUR WORDS RUN AS WRITTEN. It rewrites the prompt before generation and is on by default on P-Video-2, Edit and the Pro avatar ("leave true for production"), off on P-Video ("full user control"). Turn it off "when you need a literal, test-only prompt", for chained segments, and on the Pro avatar when the picture must follow your prompt: "When true, the picture prompt is rewritten from the portrait."
- DESCRIBE, DO NOT COMMAND, IN GENERATION PROMPTS. Pruna's motion rules: "Use descriptive, direct language", "Focus on motion and action", "Use dynamic verbs", and not "command-style instructions 'Please create a video of a lake at sunset'". Edit, Replace and Animate are the exception: their prompts are instructions.
- LENGTH CAN COME FROM THE PROMPT on P-Video-2. Where the host leaves duration unset, "the model chooses length from the prompt". An imported track sets the length instead.

## Prompt structure

<rules id="structure">

- Lead with the subject and its key attributes, then one action, then the scene. Pruna: "One hero action per clip."
- Sequence actions with "then" when a clip needs more than one: "wakes up, then puts on glasses, then drinks coffee".
- Add camera, lighting and style as short clauses. A camera path can run start to end: "camera starting in front, then circling and ending behind the character".
- Close with an "Audio:" sentence that names the music bed, the voice quality and the ambience or SFX.
- Keep prompts short. Pruna's chaining workflow keeps each segment to one or two sentences "for better model control".
- For a silent clip, say so: "No audio." or "No music, no voice."

</rules>

<template id="general">

{Subject with attributes}, {action}, {scene}. {Camera}. {Lighting}. {Style}. {Speaker} {delivery}: "{line}". Audio: {music}, {voice quality}, {ambience}, {SFX}.

</template>

<example use_case="flagship-lyric-visualizer">

```text
Fictional Black rapper in oversized hoodie performs in a parking garage at night, purple LED tubes, light fog, camera slow orbit at chest height, confident hand gestures on beat. On-screen graffiti-style text overlay: "MIDNIGHT DROP". Lyrics he raps (original): "Midnight drop, yeah we run the block. Neon signs and the bass won't stop. Started from the bottom of the parking lot, now every speaker hit every spot. Yeah! Let's go!" Audio: trap beat with heavy 808s, rapper delivers the lyrics above with clear enunciation, ad-libs on the last line.
```

*Why: Pruna's P-Video-2 rap example (one dash made plain). Subject, scene, light and camera come first, the on-screen text is quoted, the lyrics sit in their own labelled clause, and the Audio sentence ties the beat, the delivery and the ad-libs back to "the lyrics above"*

</example>

<example use_case="formula-locked-in">

```text
Knitted purple prune character, reading a book, eyes look at book then at camera, cozy room, camera slowly zooming in, warm natural light, documentary style, character reading aloud: "P-Video generates state-of-the-art AI video in seconds. Ten seconds of video in ten seconds for only ten cents. With draft mode for rapid iteration, custom or built-in audio generation, and lip sync."
```

*Why: Pruna's locked-in formula example, one slot per clause in order (subject, action with a small beat, scene, camera, lighting, style), ending with a spoken line in the reading-aloud form*

</example>

<example use_case="silent-product">

```text
Matte black air fryer on white quartz kitchen counter, morning side light, no people. Lid opens slowly revealing golden fries inside, subtle steam. Static camera, Apple-style product cleanliness. No music, no voice.
```

*Why: Pruna's silent product example. One object, one slow action, a static camera, and the silence stated outright, since the model otherwise adds sound*

</example>

## Dialogue, singing and sound

<rules id="dialogue">

- Write who speaks, how, a colon, then the line in double quotes: "She speaks confidently: "We're shipping the integration this quarter."" The P-Video form is `character reading aloud: "..."`.
- Keep the speaker in a stable framing while they talk: "static phone-camera framing", "Static camera, realistic podcast studio".
- Two speakers: label them by position or number and give each line its label: `Man 1 (on the left) "..." Man 2 (on the right) "..."`, or `Dialogue - Man 1: "..." Man 2: "..."`. Pruna warns: "Above two speakers, speaker separation can degrade."
- Name the spoken language and accent in the subject clause when it is not obvious: "Two French men speaking English".
- Let the model voice the line for the best lip-sync. With native speech, "it pauses, delivers the line, then rests, and the mouth follows". Use an imported track only when that exact recording must play.
- For singing, "paste full lyrics" in a labelled clause, "Lyrics she sings (original): "..."", ask for "natural lip sync" or "accurate lip sync", and in the Audio sentence point back to the words: "female vocal singing the lyrics above clearly".
- Mix the audio in words. Pruna's dialogue examples keep a bed under the voice and say so: "her voice clear and close-mic, very light bathroom room tone, never voice-only".
- On-screen text goes in quotes with its placement: "Large clean white text overlay centered: "SHIP 10x FASTER"", "Clean lower-third text overlay".

</rules>

<example use_case="two-speaker-podcast">

```text
Two fictional French men speaking English with a clearly noticeable French accent, natural conversational tone, relaxed pacing, discussing a new AI video generation model, intelligent but casual tech founders vibe. They remain seated on a podcast sofa, facing slightly toward each other. Subtle conversational movement only: light head nods, very small hand movements, natural breathing. Static camera, realistic podcast studio, documentary realism. Dialogue - Man 1: "Have you tested P-Video-2 yet? The speed-to-quality cost ratio is impressive." Man 2: "I did! I made a ten-second video in ten seconds for only ten cents. I really love it." Audio: warm podcast studio room tone, faint lo-fi intro music bed under the conversation at low volume, natural dialogue levels, not dry voice-only.
```

*Why: Pruna's P-Video-2 two-speaker example (dashes made plain). Language and accent are set once for both men, movement is kept small so the lips read, each line carries its speaker label, and the Audio sentence places the music under the voices*

</example>

<example use_case="singing-from-a-still">

```text
Intimate live session: she strums acoustic guitar and sings with accurate lip sync, minimal body sway, static camera, warm film grain. Lyrics she sings (original): "City lights are fading slow, I packed my bags and let you go. Every street remembers us, but I'm not asking for your trust." Audio: fingerpicked acoustic guitar plus her voice singing the lyrics above, warm studio room tone, no backing track.
```

*Why: Pruna's image-to-video singing example. The still supplies the singer, the prompt adds only the performance, the full lyrics are pasted, and the Audio sentence rules out a backing track*

</example>

## Image-to-video, last frames and chaining

<rules id="i2v">

- Let the still carry the look and write the motion. "Keep motion subtle and aligned with the reference frame." Refer to the subject by role ("The woman", "the golem") rather than re-describing it.
- Add keep lines for what must not drift: "warm bathroom background unchanged", "sneaker stays sharp and centered".
- Start from a clean, well-lit still. Pruna's retail advice: "start from a clean product or on-model still."
- P-Video-2 also takes a last frame for "end-frame control"; describe the motion that gets there.
- To chain clips, use the last frame of one clip as the first image of the next and write a short prompt for the new action: "The character approaching and entering a magical doorway". Pruna's chaining workflow keeps segments to one or two sentences and turns upsampling off so each runs as written.

</rules>

<example use_case="i2v-dialogue-with-mix">

```text
The woman holds the serum bottle toward camera and speaks enthusiastically: "Okay this serum actually fixed my dry patches in one week." Subtle head movement, natural blinking, static phone-camera framing, warm bathroom background unchanged. Audio: soft trending lo-fi hip-hop beat playing under her voice, her voice clear and close-mic, very light bathroom room tone, never voice-only.
```

*Why: Pruna's UGC image-to-video example (one dash made plain). The still is "the woman", the prompt adds one gesture, one line and small natural motion, pins the background, and mixes music under the voice*

</example>

<example use_case="i2v-product-turntable">

```text
Slow 15-degree product rotation on invisible turntable, sneaker stays sharp and centered, static camera, premium SNKRS-style product video, no hands, no text.
```

*Why: Pruna's silent product loop from a still. The motion is small and exact, the subject is pinned in place, and the two likely intruders, hands and text, are excluded in plain words*

</example>

## Editing footage (P-Video-Edit)

<rules id="edit">

- "Use one principal change per run. Describe the desired final state, then name what must remain unchanged."
- Fast pass: "one line: change only X to Y". Locked-in adds "Change + preserve lines: geometry, motion, camera, lighting, and anything that must not move."
- Name a reference still in words: "the roof cargo box shown in the reference image". Say what to match: shape, material, proportions.
- For a change that must hold through cuts, say so: "persistently from the first frame to the last", "Apply this environment after every cut and camera transition."
- "Stacking unrelated edits in one prompt reduces reliability." Two related color changes can share a run when each is named exactly.
- Edit is "not a character-swap model". Use a Replace model for people.

</rules>

<example use_case="edit-attribute">

```text
Change only the SUV body paint to deep metallic red. Preserve the vehicle geometry, glass, trim, headlights, tires, reflections and shadows. Keep the environment, lighting and camera movement unchanged.
```

*Why: Pruna's attribute edit. "Change only" names the single target and end state, then two preserve lines cover the object's own parts and everything around it*

</example>

<example use_case="edit-from-reference">

```text
Add the roof cargo box shown in the reference image to the SUV. Match its shape, matte-black material and proportions. Keep it rigidly attached and correctly aligned to the vehicle roof throughout the camera movement. Preserve the vehicle body, windows, trim, wheels, pedestrian, environment and lighting.
```

*Why: Pruna's reference-guided addition. The reference is named in words, the properties to copy are listed, the new object is pinned to its anchor through the camera move, and the rest is preserved*

</example>

<example use_case="edit-environment-restyle">

```text
Change the entire game environment into a colorful candy world, persistently from the first frame to the last. Replace the gray city with candy towers, lollipops, gumdrops and cotton-candy clouds. Turn the white rooftops into smooth wafer-and-frosting tracks, the cyan water into glossy pink syrup, red brick walls into chocolate-bar walls, and gray obstacles into large candy blocks. Apply this environment after every cut and camera transition. Preserve the exact orange runner, rivals, colored ladder rungs, gameplay mechanics, course layout, camera, actions, speed and timing. Change nothing else.
```

*Why: Pruna's long restyle. Each old element is mapped to its new one, persistence across cuts is stated twice, and a full preserve list protects the gameplay that the restyle must not touch*

</example>

## Replacing people (P-Video-Replace and P-Video-2-Pro-Replace)

<rules id="replace">

- The clip keeps its camera, blocking, background, timing and audio; the instruction only says who becomes whom. On P-Video-2-Pro-Replace "the voice stays the voice of the source", so pick a photo that fits that voice.
- P-Video-Replace: "Keep it to one short sentence plus a keep line (motion, audio, camera; add lip sync for dialogue drivers)." Template: "Replace the person in the source video with {character label} from reference image 1. Keep motion, audio, and camera from the source video."
- When identity drifts on P-Video-Replace, add guard lines from Pruna's examples: "The output character must be the woman from reference image 1.", "Reference image 1 is identity only.", and for props "Do not invent a new bottle."
- P-Video-2-Pro-Replace: leave the instruction empty "when one person is on screen, or when two photos should map left to right". Otherwise map by position or appearance: "Replace the woman on the left with the woman from image 2, and the man on the right with the man from image 1."
- In a group, name the one person to change and what stays: "Replace only the barista standing behind the counter with the person in the image. Keep the customers in the foreground unchanged."
- Pruna says P-Video-Replace is "strong on normal movement and slow, controlled action"; very fast action, heavy occlusion or extreme camera motion "may reduce consistency". Use the Pro model for fast action.

</rules>

<example use_case="replace-with-guards">

```text
Replace the red-haired woman in the bedroom source video with the Filipina woman in rust orange linen robe from reference image 1. The output character must be the Filipina woman from reference image 1. Reference image 1 is identity only. The amber glass serum dropper bottle in the output must be the exact original bottle from the source video and reference image 2, same glass shape, amber color, cap, label, grip, and lift toward camera around 2 seconds. Do not invent a new bottle. Keep the bedroom background, lip sync, motion, audio, and camera from the source video.
```

*Why: Pruna's two-reference P-Video-Replace instruction (one dash made plain). Each still has one job (identity, prop), the prop's details and its timed gesture are pinned, and the keep line carries lip sync because the driver speaks*

</example>

## Animating a still (P-Video-Animate)

<rules id="animate">

- The still sets the look; the driver clip sets acting, timing and camera. The instruction is "usually left empty" on a first pass.
- Add one when identity drifts or lip sync needs tightening: "Subject + motion beats + sync line; call out hands, props, and match lip sync and audio from the source video."
- Pattern: "Animate the {subject and wardrobe} using the source video: {beat}, {beat}, and {beat}. Match lip sync and audio from the source video." For a driver with no speech, end with "Match audio from the source video."
- Lock props and hands that tend to wander: "keeps both hands on the shaker bottle at his chest throughout", "Front paws stay hidden under the desk."
- Animate does not write a new script; the words come from the driver.

</rules>

<example use_case="animate-non-human">

```text
Animate the photorealistic golden retriever in the emerald blazer behind the desk using the source video: its mouth and jaw follow the driver's speech with accurate lip sync throughout, speaking the line with the same timing and emphasis as the human founder. Front paws stay hidden under the desk. Small head nod and serious half-smile. Match lip sync and audio from the source video exactly.
```

*Why: Pruna's Animate example for a non-human still. The subject is named with its wardrobe, the speech is mapped from the human driver to the dog's mouth, the paws are locked out of frame, and the sync line closes it*

</example>

## Talking avatars (P-Video-Avatar and P-Video-2-Pro-Avatar)

The avatar models split the prompt into three fields. The script is what is said, the voice prompt is how it is said, and the picture prompt (called the video prompt on P-Video-Avatar) is what the camera sees. On the Pro model, "prompt directs the picture; voice_prompt directs delivery and is not spoken."

<rules id="avatar">

- SCRIPT: "Short lines, one beat per sentence, target language." Write it for the ear and "rewrite per locale (do not ship English in a foreign voice)". Pruna's own scripts spell numbers out ("Three point two").
- VOICE PROMPT: "How it is said: tone, pace, energy, role, not the words of the script." Name the register, what to avoid ("hype, theatrical") and the accent, and keep it in line with the face in the still. "Do not paste the script here."
- PICTURE PROMPT: "On-camera motion: face, shoulders, hands; background behavior; usually fixed camera for stable lip sync." "Avoid re-stating the script."
- On the Pro model, keep to one take: "One continuous shot. No second scene, no cut, no on-screen words." "Name the gesture and what stays still. Do not ask for a new location halfway through." Long clips are stitched, and "a change of room, or a wide static background, can show a seam."
- Match the voice to the person in the still: gender, age, language and accent.
- For strict cadence or pronunciation, "prefer uploaded audio over generated TTS". With an uploaded song on the Pro model, tell the picture when to sing and what is not the song: "sing the words from the first frame. The piano keys are not the song."
- P-Video-Avatar has an experimental negative field, "useful for reducing burned-in subtitles or overlays from a source frame". Start low; higher strength "can affect identity, motion, or background".

</rules>

<example use_case="avatar-three-fields">

```text
voice_script: Hey, we finally shipped the thing I kept talking about. One portrait, your audio or a script, and you get the talking video back.
voice_prompt: Natural conversational tone, relaxed pacing, real pauses, honest not salesy.
prompt: Medium close-up, she speaks to the lens. A small nod on the last line. The camera stays put. The background stays the same room. Mouth clearly visible. No captions, no cut.
```

*Why: Pruna's P-Video-2-Pro-Avatar example (one dash made plain). Words, delivery and picture each sit in their own field, the picture prompt names one gesture and what stays still, and nothing from the script is repeated outside it*

</example>

<example use_case="avatar-localized">

```text
voice_script: Bienvenue sur SuiteLodge. En quelques minutes vous branchez votre première propriété, le tableau d'occupation s'affiche en direct.
voice_prompt: Professional French onboarding, clear articulation, approachable manager tone.
video_prompt: Fixed camera, centered; light hand motion, stable vertical crop.
```

*Why: Pruna's P-Video-Avatar French example (one dash made plain). The script is written natively in French rather than translated on the fly, the voice prompt names the language and role in English, and the picture stays fixed for clean lip sync*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- The generation, edit, replace and animate models have no negative field. Exclude in the prompt as short plain statements of the wanted condition: "No objects fall or move off the table.", "no readable brand logos", "no hands, no text".
- Silence and voicelessness are exclusions too, and the model adds sound unless told: "No audio.", "No music, no voice.", "no voiceover".
- Keep each exclusion tied to a failure the clip invites. Pruna's prompts carry one or two, not a list.
- P-Video-Avatar's negative field is for burned-in captions or overlays from the source still; use it at low strength.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Using this guide for P-Video-2-Pro or P-Video-2-Pro-Reference: they are MiniMax H3; use that guide.
- Applying MiniMax H3's structured tags to P-Video-2-Pro-Avatar: it takes plain sentences in its three fields.
- Command-style generation prompts ("Please create a video of..."): describe the scene and the motion instead.
- Several hero actions in one short clip: keep one, or sequence two with "then".
- More than two speakers: separation degrades; split the scene or cut to two.
- A dialogue clip with a busy camera: keep the speaker framed and the camera static or slow.
- Lyrics left for the model to invent: paste the full words in a labelled clause.
- Re-describing a supplied still: refer to the subject by role and spend the words on motion.
- Several unrelated edits in one P-Video-Edit run: one principal change per run.
- Asking P-Video-Edit to swap a person: use a Replace model.
- Expecting a new voice from P-Video-2-Pro-Replace: the source voice stays; choose a matching photo.
- Pasting the script into the avatar's voice or picture prompt: each field has one job.
- A room change or new location mid-avatar clip: it shows as a seam; keep one take.
- Leaving upsampling on when the prompt must run exactly as written: turn it off for tests, chains and locked finals.
- Following Pruna's general WAN-illustrated video guide over a model page: the model page wins.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. The owner is Pruna AI. Its model pages carry the model-specific craft; its general video prompting guide and cheatsheet supply the shared vocabulary, but their examples were made with Pruna-optimized WAN 2.2 models, so where they differ from a model page this guide follows the model page. Pruna's own pages disagree on whether P-Video needs an input image (one says it "requires an input image", the comparison table lists the image as optional); this guide treats it as optional, as the formula examples do. The adjudications are recorded in `sources/pruna/pruna-notation-resolution.md`.

- Official (Pruna AI): [P-Video](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video.html), [P-Video-2](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-2.html), [P-Video-Edit](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-edit.html), [P-Video-Replace](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-replace.html), [P-Video-2-Pro-Replace](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-2-pro-replace.html), [P-Video-Animate](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-animate.html), [P-Video-Avatar](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-avatar.html), [P-Video-2-Pro-Avatar](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/p-video-2-pro-avatar.html), the [prompting cheatsheet](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/cheatsheet.html), the [video generation guide](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/video_generation/advanced.html), and the [scene chaining workflow](https://docs.pruna.ai/en/stable/docs_pruna_endpoints/performance_models/workflows/scene_chaining.html).
- Provider: WaveSpeed's P-Video-2 [text-to-video](https://wavespeed.ai/models/pruna-ai/p-video-2/text-to-video) and [image-to-video](https://wavespeed.ai/models/pruna-ai/p-video-2/image-to-video) pages.

Last verified: 2026-11-08.
