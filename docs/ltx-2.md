---
guide: "LTX (family)"
prompt_scheme: "ltx-2"
models:
  - { id: "ltx-2-5-pro", access: "closed-weights", tier: "flagship", caps: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, native-audio, dialogue, singing, control-adapters, multi-shot], best_for: "final renders on the current generation. Native multi-shot, strongest prompt adherence, best faces and on-screen text. Does NOT do retake, extend or reframe" }
  - { id: "ltx-2-5-fast", access: "closed-weights", tier: "distilled", caps: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, native-audio, dialogue, singing, control-adapters, multi-shot], best_for: "iteration on the current generation, and the only tier that reaches the highest resolutions. Unlike 2.3 Fast it also takes audio-to-video" }
  - { id: "ltx-2.5-22b", access: "open-weights", tier: "flagship", caps: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, native-audio, dialogue, singing, control-adapters, multi-shot], best_for: "the current generation run locally, in dev and distilled checkpoints. Most 2.3 LoRAs and IC-LoRAs load unchanged; the owner advises validating adapters before production" }
  - { id: "ltx-2-3-pro", access: "closed-weights", tier: "std", caps: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, video-extend, native-audio, dialogue, singing, control-adapters], best_for: "still the ONLY path to retake, extend and reframe, which 2.5 does not have. Reach for it when a shot needs continuation or reframing rather than fresh generation" }
  - { id: "ltx-2-3-fast", access: "closed-weights", tier: "distilled", caps: [text-to-video, image-to-video, keyframe-interpolation, video-edit, native-audio, dialogue, singing, control-adapters], best_for: "previous-generation iteration tier. No audio-to-video; 2.5 Fast added it" }
  - { id: "ltx-2.3-22b", access: "open-weights", tier: "std", caps: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, video-extend, native-audio, dialogue, singing, control-adapters], best_for: "previous open generation, and still the host of every released IC-LoRA checkpoint and the spatial upscaler the 2.5 pipeline calls" }
  - { id: "ltx-2", access: "open-weights", tier: "legacy", caps: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, video-extend, native-audio, dialogue, singing, control-adapters], best_for: "the original generation. Same prompt grammar; later releases improved adherence, audio and detail rather than syntax. Its hosted tiers are retired, so prefer 2.5" }
capabilities: [text-to-video, image-to-video, audio-to-video, keyframe-interpolation, video-edit, video-extend, native-audio, dialogue, singing, control-adapters, multi-shot]
prompt:
  languages: ["en"]
  multilingual_speech: "characters can talk and sing in multiple languages. The 2.5 model card declares nine (en, de, es, fr, ja, ko, zh, it, pt); the Dub-It adapter validates five (en, fr, es, de, ru). Those are different claims about different things, so treat any other language as supported but unverified"
  formula: "Shot + Scene + Action + Character + Camera + Audio, written as one flowing paragraph in present tense"
  length_strategy: "CHANGED BY GENERATION. On 2.5, match length to COMPLEXITY, not to duration: roughly 4-8 sentences for a single shot, longer for a screenplay or multi-shot scene, provided every sentence adds concrete detail. On 2.3 and earlier, length scales with DURATION and a short prompt for a long shot makes the model rush. Never pad to fill a slot on 2.5"
  dialogue_and_text: "put spoken lines in quotation marks; segment long speech into short quoted phrases with acting directions between them. On-screen written text improved on 2.5 but exact spelling is still not guaranteed: keep strings short and prominent, and add critical titles in post"
  auto_expand_behavior: "the owner SHIPS a prompt enhancer with 2.5 as a separate small model, and hosts expose it as a toggle. It expands a short prompt into richer cinematic instruction. Write the full prompt yourself when you need exact wording; reach for the enhancer only from a deliberately sparse brief"
  negatives: "the owner's prompting guidance uses NO negative prompts at all. Steer positively: describe what you want and stay internally consistent. Where a negative field exists, note that the distilled checkpoint runs at guidance 1.0, where it cannot bite"
  structured_json: "none. LTX is natural language only, and numeric or parametric direction is explicitly called a mistake. Do not write JSON prompts for it"
  multi_shot: "2.5 ONLY. Several shots joined by explicit cuts inside one prompt, written as one chronological paragraph. Never a shot list or numbered beats. Earlier generations produce a single continuous take"
  references: "each conditioning input owns a dimension and the prompt covers the complement; see 'Conditioning inputs and what the prompt keeps'"
sources:
  official: ["https://ltx.io/blog/ltx-2-5-prompt-guide", "https://docs.ltx.io/open-source-model/usage-guides/prompting-guide", "https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide", "https://docs.ltx.io/models", "https://docs.ltx.io/open-source-model/usage-guides/text-to-video", "https://docs.ltx.io/open-source-model/usage-guides/image-to-video", "https://docs.ltx.io/open-source-model/usage-guides/ic-lo-ra", "https://docs.ltx.io/open-source-model/integration-tools/ic-lo-ra-adapters", "https://docs.ltx.io/api-documentation/api-reference/video-generation/extend", "https://ltx.io/blog/ltx-2-3-prompt-guide", "https://github.com/Lightricks/LTX-2", "https://huggingface.co/Lightricks/LTX-2.5", "https://huggingface.co/Lightricks/LTX-2.3"]
last_verified: "2026-08-12"
---

# LTX: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- LTX generates video WITH SYNCHRONIZED AUDIO from a single prompt. There is no still-image output; images are only ever an input. So there is no image half to this guide, and no image guide to cross-reference.
- Audio is generated jointly with the picture and is ON by default. Some hosts expose a silent-video switch, but unless you throw it, every prompt is an audio prompt whether you wrote one or not. A prompt with no sound described still produces sound, just sound you did not choose.
- Write as one flowing paragraph in present tense. For dialogue-heavy scenes, switch to screenplay beats (see "Screenplay form"), which is LTX's native idiom and is what the owner's own flagship examples use.
- Natural language only. There is no JSON prompt form, and numeric or parametric direction ("pans right at 2 degrees per second") is explicitly listed by the owner as a mistake.
- TWO GENERATIONS ARE CURRENT and they differ on two rules that matter. Multi-shot is 2.5 only, and prompt length is judged differently (see "Prompt length"). Everything else in this guide holds for both.

</rules>

## TL;DR

<template id="quickstart">

{shot scale and genre}. {scene: lighting, color palette, texture, atmosphere}. {character with age, hair, clothing, distinguishing features} {action in present tense}. {camera move, and how the subject appears once it lands}. {ambient sound and music}; the character says "{line}".

</template>

## Models and when to use which

The prompt grammar is identical across every model and both access paths, so a prompt written once transfers everywhere. Pick on capability, not on how to phrase things.

- Fast is for exploring, Pro for the final render. The owner's advice is to compose on Fast and re-render the keeper on Pro. This holds in both generations.
- The open weights are the same production model as the API, so nothing in this guide changes when you move between them. The LoRA and IC-LoRA ecosystem attaches to the open weights.
- THE NEWEST MODEL IS NOT A SUPERSET. 2.5 adds native multi-shot and gives its Fast tier audio-to-video, which 2.3 Fast never had. It also drops retake, extend and reframe, which remain 2.3 Pro only. If a shot needs continuing or reframing rather than generating, you are on 2.3 whether or not you wanted to be.
- Every released IC-LoRA is still a 2.3-generation checkpoint. The owner reports that most load on 2.5 unchanged and advises validating an adapter before you rely on it.
- LTX-2 is the original generation and its hosted tiers are retired. Nothing about prompt SYNTAX changed across the line; later releases improved adherence, audio quality and detail.

## How the model reads prompts

- Prompt length is the one rule that changed between generations, and it is the rule most likely to make a 2.3 habit misfire on 2.5. It has its own section below; read it before writing anything long.
- It is genuinely a cinematographer's model. Terms like "macro lens", "tracking shot", "shallow depth of field", "golden hour" and "low angle" directly change the output. Write a shot description, not a wish.
- It reads screenplays. Sluglines, character cues with parenthetical acting directions, quoted dialogue and beat markers all work, and the owner's flagship examples are written that way. No other major video model's official guidance does this.
- Emotion belongs in the body, not the label, with one exception. "He is sad" is a wasted word; "his eyes widen momentarily" and "he lowers his head" are direction. The exception is the audio layer, where an emotion word is a legitimate voice-delivery descriptor: "speaks in a sad, slow-paced voice" is good writing, not a banned label.
- Camera moves need a destination. Do not just name the move; say how the subject appears once the move lands. The model uses that to complete the motion.
- It rejects numbers. Natural language beats parametric direction, and the owner calls out "exactly 3 birds at 45 degrees" as an anti-pattern.

## Prompt length

The rule inverted between generations. Both versions are correct for their own model, and the owner scoped the older claim itself, writing that longer prompts outperform short ones "on 2.3".

<rules id="length">

- ON 2.5: match length to COMPLEXITY, not to duration. Roughly four to eight sentences for a single shot; a screenplay or multi-shot scene runs longer, but only while every sentence adds concrete visual or audio detail. Do not pad to fill a duration.
- ON 2.3 AND EARLIER: match length to DURATION. A short prompt for a long shot makes the model rush through the action, racing the beats to fill time you under-wrote. Here length is word count and complexity is scene load, and the target is a LONG prompt describing a SIMPLE scene.
- Both generations agree on the underlying quality bar: every sentence must carry concrete detail. What changed is whether an extra sentence with nothing new in it still helps. On 2.3 padding bought you pacing; on 2.5 it buys you nothing.
- The mechanism behind the change is worth knowing, because it tells you which way to err. On 2.5 the model can pick the clip length from the prompt itself: a one-line action stays short, a multi-shot sequence runs long. Length is an OUTPUT of what you describe, not an input you tune to a slot.
- KEEP THE SCENE FOCUSED on either generation. A few clear characters and actions beat a crowded frame, and one coherent light logic per shot beats mixed sources.

</rules>

## Prompt structure

The owner's six named elements, in order.

<rules id="structure">

- Establish the shot: cinematography terms matching the intended genre, plus shot scale.
- Set the scene: lighting conditions, color palette, surface textures, atmosphere.
- Describe the action: the core action as a natural sequence, flowing from beginning to end.
- Define the characters: age, hairstyle, clothing, distinguishing features. Express emotion through physical cues, never abstract labels.
- Identify the camera movement: how and when the camera moves, AND how the subjects appear after the move lands.
- Describe the audio: ambient sound, music, speech or singing. Spoken dialogue in quotation marks. Name the language and accent if it matters.

</rules>

<rules id="craft">

- One flowing paragraph, present tense.
- Match the level of detail to the shot scale. A close-up needs more detail than a wide shot.
- Describe camera movement relative to the subject.
- Four to eight descriptive sentences is the working range for a single shot. See "Prompt length" for what makes it grow, which differs by generation.

</rules>

<template id="general">

{genre and shot scale}, {lighting and color palette}, {texture and atmosphere}. {character: age, hair, clothing, distinguishing features} {action, present tense, as a sequence}. {camera movement} {how the subject appears once the move lands}. {ambient sound}, {music}. {character} says "{line}".

</template>

<example use_case="vague-to-specific">

```text
A young woman in a red coat walking briskly through a rain-soaked Tokyo street at night, neon reflections on wet pavement, handheld camera following from behind.
```

*Why: the owner's own rewrite of the anti-pattern "a person walking"; every added clause removes a choice the model would otherwise have made arbitrarily*

</example>

## Screenplay form

This is LTX's signature and the thing to reach for whenever anyone speaks. The owner's flagship examples are screenplays, not paragraphs.

<rules id="screenplay">

- Open with a slugline when the scene needs establishing: interior or exterior, location, time of day, and the kind of shot.
- Give each speaker a character cue with a parenthetical acting direction, then the quoted line: `Reporter (grinning): "..."`.
- Use beat markers as timing tokens. "A beat of silence", "Beat.", "A pause." all read as pauses.
- Establish ambience before the action starts, so the sound bed is running when the first thing happens.
- Let dialogue drive the camera. If a character says "if my cameraman can pan over", then say the camera pans right. The model connects them.
- Close a camera move by stating the framing it lands on.

</rules>

<example use_case="flagship-screenplay-with-audio">

```text
EXT. SMALL TOWN STREET - MORNING - LIVE NEWS BROADCAST
The shot opens on a news reporter standing in front of a row of cordoned-off cars, yellow caution tape fluttering behind him. The light is warm, early sun reflecting off the camera lens. The faint hum of chatter and distant drilling fills the air.
The reporter, composed but visibly excited, looks directly into the camera, microphone in hand.
Reporter (live): "Thank you, Sylvia. And yes, this is a sentence I never thought I would say on live television, but this morning, here in the quiet town of New Castle, Vermont... black gold has been found!"
He gestures slightly toward the field behind him.
Reporter (grinning): "If my cameraman can pan over, you will see what all the excitement is about."
The camera pans right, slowly revealing a construction site surrounded by workers in hard hats. A beat of silence, then, with a sudden roar, a geyser of oil erupts from the ground, blasting upward in a violent plume.
Workers cheer and scramble, the black stream glistening in the morning light. The camera shakes slightly, trying to stay focused through the chaos.
Reporter (off-screen, shouting over the noise): "There it is, folks, the moment New Castle will never forget!"
The camera catches the sunlight gleaming off the oil mist before pulling back, revealing the entire scene, the small-town skyline silhouetted against the wild fountain of oil.
```

*Why: the flagship. Slugline, ambience established before the action, character cues with parenthetical direction, dialogue that cues its own camera move, an explicit beat of silence before the event, an off-screen line with a volume direction, and a pull-back that states the framing it lands on*

</example>

<example use_case="multi-speaker-call-and-response">

```text
The camera opens in a calm, sunlit frog yoga studio. Warm morning light washes over the wooden floor as incense smoke drifts lazily in the air. The senior frog instructor sits cross-legged at the center, eyes closed, voice deep and calm. "We are one with the pond." All the frogs answer softly: "Ommm..." "We are one with the mud." "Ommm..." He smiles faintly. "We are one with the flies." A pause.
The camera pans to the side towards one frog who twitches, eyes darting. Suddenly its tongue snaps out, catching a fly mid-air and pulling it into its mouth.
The master exhales slowly, still serene. "But we do not chase the flies..." Beat. "Not during class."
The guilty frog lowers its head in shame, folding its hands back into a meditative pose. The other frogs resume their chant: "Ommm..." Camera holds for a moment on the embarrassed frog, eyes closed too tightly, pretending nothing happened.
```

*Why: a group responder ("all the frogs answer softly"), voice quality given without a speaker tag, "A pause." and "Beat." as timing tokens, a pan that changes subject mid-shot, and every emotion carried by a physical cue rather than a label*

</example>

## Multi-shot scenes

2.5 ONLY. Several distinct shots joined by explicit cuts inside one prompt. Earlier generations render one continuous take, so the same prompt there has no cut mechanism to drive and collapses into a single shot.

<rules id="multishot">

- Write the whole scene as ONE CHRONOLOGICAL PARAGRAPH. No shot lists, no numbered beats, no sluglines, unless you also describe the cut in prose. The cut has to be a sentence, not a layout.
- Two to four shots per generation. More cuts than that need shorter, clearer beats in each one.
- NAME THE TRANSITION in natural language: "a hard cut transitions to", "the view cuts to a close-up of", "a match cut connects", "the image dissolves into".
- RE-ESTABLISH THE NEW SHOT after every cut: shot scale, camera angle, who or what is in frame, and the lighting if it changed. The cut resets the frame, so nothing carries over unless you say it does.
- KEEP IDENTITY CONSISTENT by reusing the same visual identifiers for anyone who reappears: "the woman in the red coat, earlier at the table, now...". This is NAME WHAT MOVES, PIN WHAT STAYS applied across a cut instead of across an input.
- STATE AUDIO CONTINUITY at every cut. Say whether music, dialogue and ambience continue or change: "the piano score continues across the cut", "the dialogue drops, only wind remains". A cut you leave silent about sound is a cut the model resolves for you.
- Give each shot a clear job: establish, then detail, then reaction; or wide, then medium, then close-up.
- Keep the action chronological, and let connectives carry the order: "initially", "a moment later", "simultaneously".
- Do not change geography or costume between cuts without saying so. Unexplained changes read as errors, not as edits.
- Everything from single-shot still applies: present tense, physical emotion cues, quoted dialogue, concrete camera language.

</rules>

<template id="multishot">

{shot scale} {scene, lighting, palette}. {character with distinguishing features} {action, present tense}. {ambient sound and music}. {named transition} to {new shot scale and angle} of {who or what is in frame}; {what happens to the sound across the cut}. {action, present tense}. {named transition} to {new shot scale} of {re-identified subject, repeating the same visual identifiers}; {audio change}. {closing action}.

</template>

<rules id="when-single-shot">

- Stay on a single continuous take for unbroken camera motion, intimate performance, or dialogue that has to stay lip-synced in one framing.
- For image-to-video from a first frame, prefer a single take. A cut throws away the framing your input image just established, so only cut if you mean to leave that image behind and say so.

</rules>

<example use_case="multishot-three-cuts">

```text
A wide shot frames a rainy city intersection at dusk, neon signs reflecting on wet asphalt. A young woman in a yellow raincoat walks toward camera, gripping a folded newspaper, while cars hiss past behind her. Soft synth music and distant traffic fill the air. A hard cut transitions to a medium close-up of her face under the hood, raindrops catching the neon as she looks off-screen left; the synth score continues across the cut, traffic muffled. She whispers, "He's late." Another hard cut jumps to a low-angle shot of a man's scuffed boots stepping into a puddle at the curb; the music drops to a low drone. He lifts his head into frame, short dark hair, soaked jacket, and smiles toward her off-screen as a bus rumbles past.
```

*Why: the owner's own multi-shot demonstration. Three shots, each cut named, each new framing re-established, the score tracked across both cuts ("continues", then "drops to a low drone"), and the second subject introduced by appearance at the moment he enters frame rather than in advance*

</example>

<example use_case="multishot-identity-across-a-time-jump">

```text
An establishing wide shot looks down a sunlit hospital corridor, pale green walls and polished floor, a nurse in navy scrubs with cropped grey hair pushing an empty gurney away from camera. Fluorescent hum and distant intercom chatter fill the space. A match cut connects the gurney's wheels to a close-up of a suitcase's wheels rolling across the same polished floor, now dimmed to evening amber; the intercom is gone and only the wheels remain. The camera tilts up to a medium shot of the same nurse in navy scrubs and cropped grey hair, coat over one arm, walking toward the exit, her shoulders lowered. She says quietly, "That's enough for today." A soft piano line fades in beneath her voice and carries to the end.
```

*Why: shows the two rules that are easy to drop. Identity is re-pinned by repeating "navy scrubs and cropped grey hair" rather than saying "the same nurse", and every cut states what happens to the sound, including a deliberate removal ("the intercom is gone") and a late addition. The lighting change is named, so the time jump reads as intended rather than as drift*

</example>

## Audio and dialogue

Audio is written into the same paragraph as the picture, never a separate field. There are three things to describe and a fourth worth adding.

<rules id="audio">

- Acoustic environment, voice qualities, and ambient sounds. Name all three when they matter.
- A short audio-mix line at the end earns its place: "the audio is crisp with faint room tone".
- Ambience examples that work: the sound of rain on pavement, soft ambient music, a crowd cheering in the distance.
- Speech is the model's strong path. The owner notes that audio WITHOUT speech may come out lower quality, so a silent-but-for-ambience shot is the harder ask, not the easier one.

</rules>

<rules id="dialogue">

- Put every spoken line in quotation marks. Name the language and accent when they matter.
- SEGMENT LONG SPEECH. Break a long sentence into short quoted phrases with acting directions between them. This is how you get pacing, emotion and physical acting under control beat by beat.
- Direct the acting at the granular level and expect it to land: "he pauses, looks to the side, then continues speaking with a cracking voice".
- Trailing dots inside a quoted phrase read as a pause.
- Characters can sing, and multi-speaker call-and-response works.

</rules>

<example use_case="dialogue-segmentation">

```text
A middle-aged man with greying hair speaks in a sad, slow-paced voice, "I remember after you kids came along..." He pauses and looks to the side, then continues, "your mom..." His eyes widen momentarily. He finishes with a cracking voice, "said something to me I never quite understood." The camera slowly zooms into his face. The audio is crisp with faint room tone.
```

*Why: the clearest demo of the LTX difference. Quoted phrase, acting direction, quoted phrase, physical cue, voice-quality direction, quoted phrase, then the camera move and an audio-mix line. Written as one long quoted sentence it would have been delivered flat*

</example>

## Cinematic vocabulary

Terms the model recognizes. Mix freely; you do not need one from every group.

- Camera language: follows, tracks, pans across, circles around, tilts upward, pushes in, pulls back, overhead view, handheld movement, over-the-shoulder, wide establishing shot, static frame. Explicit forms like "slow dolly in" and "handheld tracking" are what the owner recommends.
- Pacing and time: slow motion, time-lapse, rapid cuts, lingering shot, continuous shot, freeze-frame, fade in, fade out, seamless transition, sudden stop.
- Film characteristics: film grain, lens flares, pixelated edges, jittery stop-motion.
- Scale: expansive, epic, intimate, claustrophobic.
- Visual effects: particle systems, motion blur, depth of field.
- Lighting: flickering candles, neon glow, natural sunlight, dramatic shadows.
- Texture: rough stone, smooth metal, worn fabric, glossy surfaces.
- Color palette: vibrant, muted, monochromatic, high contrast.
- Atmosphere: fog, rain, dust, smoke, particles.
- Genre, cinematic: period drama, film noir, fantasy, epic space opera, thriller, modern romance, experimental film, arthouse, documentary.
- Genre, animation: stop-motion, 2D and 3D animation, claymation, hand-drawn.
- Genre, stylized: comic book, cyberpunk, 8-bit pixel, surreal, minimalist, painterly, illustrated.
- Ambient sound: coffeeshop noise, wind and rain, forest ambience with birds.
- Dialogue style: energetic announcer, resonant voice with gravitas, distorted radio-style, robotic monotone, childlike curiosity.
- Volume: whisper, mutter, shout, scream.

## Conditioning inputs and what the prompt keeps

ONE ROLE PER INPUT. Every conditioning input owns a dimension of the output, and the prompt's job is to cover the complement. The catch, and the thing most likely to trip you if you come to LTX from another model family, is that WHICH dimension gets taken varies by input, so the prompt's residue moves with it.

<rules id="conditioning">

- An input image owns appearance. The prompt keeps motion, camera, and the sound that emerges. NAME WHAT MOVES, PIN WHAT STAYS: do not re-describe what is already visible in the frame.
- An input audio track owns the temporal structure. The prompt keeps the visual interpretation: what scenes, subjects and camera work should accompany that soundtrack.
- A control signal (depth, pose, canny, motion track) owns structure and motion. The prompt keeps style, materials, lighting, atmosphere and identity.
- For control signals the rule is ALIGN, NOT OMIT, and this is where LTX differs from model families that simply subtract. You never name the control artifact itself ("the depth map shows...") and you describe visual style instead. But you DO keep the prompt aligned with the reference's motion and composition, and you must not contradict its structure. Going silent on motion is not the instruction; contradicting it is the failure.
- A source video in a video-to-video edit owns everything you are not changing. The prompt describes the new content for the region you are changing.

</rules>

## By mode

### Text-to-video

<rules id="t2v">

- The prompt is the only source of truth, so detail is your only lever. Cover all six elements.
- This is where prompt length matters most, because no conditioning input is filling the time for you. On 2.3 that means writing to the duration; on 2.5 it means the duration can follow what you wrote.

</rules>

### Image-to-video

<rules id="i2v">

- The image is the first frame and already fixes the scene. Describe what happens NEXT: how the subject moves, how the camera follows, what sounds emerge.
- Do not re-describe the static elements already visible in the image. Describe the transition from stillness to motion.
- Audio is still generated from nothing, so the sound layer is as much your job here as in text-to-video. This is the part people forget.

</rules>

<example use_case="i2v-motion-and-sound-only">

```text
The woman turns to face the camera and smiles, a warm breeze moving through her hair. Soft piano music plays in the background.
```

*Why: the owner's own example. Not one word about what she looks like or where she is, because the image said that; only the motion, and the sound that emerges*

</example>

### Audio-to-video

You SUPPLY an audio file; the model does not invent the sound in this mode. On 2.3 this is Pro only; on 2.5 both tiers take it.

<rules id="a2v">

- The audio anchors the temporal structure: pacing, beats, and the shape of the cut.
- Use the prompt to describe the VISUAL interpretation of that audio: what scenes, subjects, and camera work should accompany the soundtrack.
- Do not describe the sound. It is already in the room.

</rules>

### Keyframe interpolation

<rules id="keyframe">

- Supply a first frame and a last frame. Both already carry appearance, so the prompt controls the path between them.
- Describe the motion and the camera trajectory that carries the first into the last.

</rules>

### Retake

2.3 Pro only, and absent from 2.5. Regenerate a chosen time region of an existing video.

<rules id="retake">

- The prompt describes the NEW content for the region being regenerated, not the whole clip.
- Lead with a register token ("live-action cinematic", "live-action horror") so the regenerated region matches the surrounding footage.
- Camera movement still belongs in the prompt here; a retake is a fresh generation of that region, not a control-signal edit.

</rules>

<example use_case="retake-region">

```text
A live-action horror style, thick black oily tentacles slither across the floor and furniture of a living room. Dark, glowing eyes peer through a heavy mist, creating an atmosphere of eerie supernatural dread.
```

*Why: the owner's own retake example. A register token first so it cuts against the original footage, then the new content for that region only, with the camera and atmosphere still described*

</example>

### Extend

2.3 Pro only, and absent from 2.5. Generate additional footage onto an existing video.

<rules id="extend">

- The prompt covers ONLY the new footage. The existing video owns everything already on screen, so do not re-describe it. This is the same displacement as image-to-video, with a video tail in place of a still frame.
- The prompt is OPTIONAL in this mode. The tail of the input already carries appearance and motion, so the prompt is a steer rather than a specification. Supply one when you want the continuation to go somewhere it would not drift on its own; omit it when a plain seamless continuation is what you want.
- Extend runs in two directions, and the direction changes what you write. Extending forward, the prompt continues the action past the last frame. Extending BACKWARD, the prompt describes what leads INTO the existing footage and must arrive at its opening state; write it as a lead-in, not a continuation.
- Audio continues if the input video has audio, so the sound layer is not yours to write from nothing here the way it is in text-to-video.
- Whether the length-scales-with-duration rule applies here is NOT documented. The input tail supplies context that a text-to-video prompt has to supply in words, so a terse prompt may be correct in this mode alone. Treat prompt length as an open question and test it rather than assuming the text-to-video rule carries over.

</rules>

## LoRAs and control adapters

Two different things, and they stack.

<rules id="adapters">

- A plain LoRA takes a text prompt only and shifts style globally.
- An IC-LoRA (in-context LoRA) takes a text prompt PLUS a reference input, and does targeted, reference-driven work at the frame level while preserving the scene's identity.
- Control-type IC-LoRAs (union control, motion track) need an extracted signal: a depth map, pose skeleton, edge map, or motion trajectory. Union control is canny, depth and pose in one adapter.
- Everything else in the family (colorization, deblur, day-to-night, water simulation, upscaling and so on) conditions directly on a reference video clip with no signal extraction at all.
- With any control adapter: describe visual style, not the control type. Write "ornate architecture", never "the depth map shows ornate architecture".

</rules>

<rules id="triggers">

- SOME adapters require a trigger phrase, written in capitals and PREPENDED before any scene description. Published examples include DEBLUR, COLORIZE, ADD WATER, ENHANCE QUALITY and REMOVEBEARD.
- The owner does not publish a trigger-to-adapter mapping anywhere in the docs; it lives in each adapter's own model card. Read the card. Do not guess a trigger from the adapter's name, because a wrong or missing trigger silently produces a normal generation with none of the adapter's effect.
- The control adapters (union, pose, depth, canny, motion track) and the camera-control LoRAs have no documented trigger.

</rules>

### Camera-control LoRAs

There is one adapter per move: dolly in, dolly out, dolly left, dolly right, jib up, jib down, static.

<rules id="camera-lora">

- Loading the adapter IS the camera instruction. The move is baked in.
- Describe the DESTINATION of the movement, not the movement. This is the owner's stated recommendation, and it is the same rule as the base guide's "state how the subject appears after the camera lands", just with the move itself removed.

</rules>

### Video-to-video edits

A family of adapters that re-render an existing clip with one thing changed: colorization, deblur, decompression, day-to-night, clean plate, instant shave, water simulation, in-outpainting. They share one prompt shape.

<rules id="video-edit">

- ONE CONCRETE INSTRUCTION per generation. Name what changes and what stays, and phrase it additively as the thing you want present rather than as a removal or a prohibition.
- The source clip owns geometry, motion and everything you do not mention. As with image-to-video, do not re-describe what is already on screen.
- Several of these need a trigger phrase; see the trigger rule above, and read the adapter's own card.

</rules>

### Dub-It (speech replacement)

Replace the speech in an existing video. The source clip owns the speaker, the scene and the camera; the prompt owns only the words and the delivery. The owner previously shipped this as LipDub, so treat that name as the same tool when you meet it in older material.

<template id="dub-it">

{speaker} is speaking {language or accent}, saying: "{full dialogue}"

</template>

<rules id="dub-it">

- Provide the FULL dialogue text. The model follows the content of the prompt and will not translate for you.
- Write the dialogue in the target language's native script: Cyrillic for Russian, Chinese characters for Mandarin.
- Validated languages are English, French, Spanish, German and Russian. Others may work and are not attested.
- One speaker only; the beta cannot tell two apart.
- MATCH THE SYLLABLE LENGTH of the original dialogue. This is the sharpest rule in the whole LTX surface, because it makes prompt length a literal timing instrument: too long and the model skips words, too short and the delivery drags. Slightly longer beats too short.
- Emotion and delivery notes can be added to the prompt.
- Works for dubbing into another language and for rephrasing in the original one.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- LTX's official prompting guidance does not use negative prompts at all. There is no negative-prompt technique to teach, and none is implied by the guide's silence: the owner steers positively throughout.
- Steer by describing what you want and staying internally consistent. "A still, peaceful lake with dramatic waves crashing" fails not because it lacks a negative prompt but because it contradicts itself.
- Where a host exposes a negative field anyway, treat it as a quality guard, not a steering tool.
- ON THE DISTILLED CHECKPOINT A NEGATIVE PROMPT CANNOT BITE, whatever you write in it. Distilled runs at guidance 1.0, and at that setting there is no unguided branch for an exclusion to push against. The owner's own local pipeline both ships a default negative string and runs at guidance 1.0, which is exactly how you end up with a negative prompt in your code that provably does nothing. The dev checkpoint is the trainable one and its recommended guidance is not published, so treat the field as responsive only there and verify before relying on it.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Too vague: "a nice video of nature" leaves the model to pick arbitrarily. Name what is in the frame.
- Over-constrained: "exactly 3 birds flying left to right at 45 degrees while the camera pans at 2 degrees per second" is worse than prose. LTX wants natural language, not numbers.
- Mismatched duration on 2.3: a ten-word prompt for a ten-second shot makes the model rush the action. On that generation, long videos need long prompts.
- Padding on 2.5: adding sentences that carry no new detail, to fill a duration. That was the 2.3 fix and it is not the 2.5 one; here length follows what you describe.
- Assuming the newest model does everything: retake, extend and reframe exist only on 2.3 Pro. Writing an extend prompt for 2.5 targets a mode it does not have.
- Conflicting directions: contradictions inside one prompt (a still lake with crashing waves, or two incompatible light sources) confuse the scene. Be internally consistent.
- Emotion labels instead of cues: "sad" and "confused" are not directions. Give the physical cue. The exception is voice delivery, where "in a sad, slow-paced voice" is correct.
- Overloaded scenes: too many characters or simultaneous actions reduce clarity. Keep the scene focused whichever generation you are on.
- Multi-shot written as a layout: a numbered shot list or bare sluglines gives the model no cut to perform. Describe each cut in prose, inside one paragraph.
- Silent cuts: changing shot without saying what happens to the music, dialogue and ambience. The model will decide for you, and it will not decide consistently.
- On-screen text and logos: 2.5 renders short text better than earlier versions, but exact spelling and frame-to-frame consistency are still not guaranteed. Keep any string short and prominent, check it across the whole clip, and add critical titles in post.
- Complex physics: chaotic motion introduces artifacts. Dancing is fine; shattering, splashing crowds of debris are not.
- Re-describing the image in image-to-video: state only motion, camera and sound.
- Forgetting the audio: LTX always generates sound. If you did not describe it, you still got it, and you did not choose it.
- Writing a JSON or parameter-style prompt: there is no structured-prompt form for LTX.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict. Every source below is from Lightricks.

- Official (Lightricks): [LTX-2.5 prompt guide](https://ltx.io/blog/ltx-2-5-prompt-guide), [open-source prompting guide](https://docs.ltx.io/open-source-model/usage-guides/prompting-guide), [API prompting guide](https://docs.ltx.io/api-documentation/implementation-guides/prompting-guide), [models and tiers](https://docs.ltx.io/models), [text-to-video usage guide](https://docs.ltx.io/open-source-model/usage-guides/text-to-video), [image-to-video usage guide](https://docs.ltx.io/open-source-model/usage-guides/image-to-video), [IC-LoRA usage guide](https://docs.ltx.io/open-source-model/usage-guides/ic-lo-ra), [IC-LoRA adapter list](https://docs.ltx.io/open-source-model/integration-tools/ic-lo-ra-adapters), [LTX-2.3 prompt guide](https://ltx.io/blog/ltx-2-3-prompt-guide), [LTX-2 repository](https://github.com/Lightricks/LTX-2), [LTX-2.5 model card](https://huggingface.co/Lightricks/LTX-2.5), [LTX-2.3 model card](https://huggingface.co/Lightricks/LTX-2.3).

Coverage notes. The prompt-length rule genuinely changed between generations and is taught here as version-conditioned rather than corrected: the 2.3 guidance ties length to duration, and the owner scoped that claim itself with the words "on 2.3", while the 2.5 guidance ties length to complexity. Automatic duration is the mechanism behind the change, since the model can now derive clip length from the prompt instead of the writer padding to fill a fixed slot. The video-to-video edit rule is stated only in the 2.5 guide's summary, which names a "Video Editing" IC-LoRA, promises a section on it, and then ships neither that section nor an adapter of that name; the rule is taught here scoped to the released edit adapters it plainly describes. The extend mode appears nowhere in the owner's prompting guidance; its rules here come from the endpoint reference's own description of the prompt field, which is the only place the technique is stated. That source yields the scope, the optionality and the direction rule, but no worked example, so none is given: the one extend prompt the owner publishes is placeholder text in a request sample and is not guidance. Per-adapter trigger phrases live on the individual adapter model cards, several of which are access-gated; this guide teaches the trigger rule and deliberately ships no trigger table. The owner's docs moved from docs.ltx.video to docs.ltx.io during this pass and the links above follow the new host.

Last verified: 2026-08-12.
