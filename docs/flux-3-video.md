---
guide: "FLUX 3 Video"
prompt_scheme: "flux-3-video"
models:
  - { id: "flux-3-video", access: "closed-weights", tier: "flagship", caps: [text-to-video, image-to-video, first-last-frame, keyframe-interpolation, video-continuation, native-audio, dialogue, multi-shot, text-rendering, grounding], best_for: "text, image, keyframe and continuation video with native synchronized audio; multi-shot sequences, multilingual on-camera dialogue, and in-scene typography in a single generation" }
  - { id: "flux-video-edit-fast", access: "closed-weights", tier: "distilled", caps: [video-edit], best_for: "instruction edits to a clip you already have: remove, add, replace, recolor, change text or dialogue, swap the setting, restyle, or turn a blockout into a finished shot. A separate FLUX Tools product, not a FLUX 3 mode; length, framing, camera, timing and audio all come from the source clip" }
capabilities: [text-to-video, image-to-video, first-last-frame, keyframe-interpolation, video-continuation, native-audio, dialogue, multi-shot, text-rendering, grounding, video-edit]
prompt:
  languages: ["en", "zh", "es", "fr", "de", "ja", "pt", "ru", "it", "id", "tr", "hi", "pa", "more"]
  formula: "Subject + Action, then Camera direction, then Scene and atmosphere, then Motion qualities, then Continuity constraints; direct a scene rather than describe a collection of objects"
  formats: "four interchangeable shapes for generation: natural-language one-liner (the default), labeled fields, a timestep timeline, and the six-element schema for multi-shot work. The edit tool takes a fifth, an instruction that names only the change and never re-describes the shot"
  length_strategy: "short prompts hand the model freedom and produce fresher results; long prompts buy precision. Start short, then lengthen only where control matters. Length alone is not the goal, and over-stuffing degrades motion coherence"
  literal_text: "quote the exact words; typography renders as part of the scene and holds through motion. A quoted line with no visible speaker and no voiceover cue may be rendered as on-screen text instead of spoken"
  audio: "native and synchronized in the same pass, never a second prompt. Four layers: speech, ambience, effects, music. Name sound sources rather than asking for silence"
  dialogue: "put the exact words in quotes and name who delivers them; mark off-screen lines as voiceover or narration; direct the voice with person, register, recording, delivery, and a guardrail"
  negatives: "no negative field in the core scheme; write guardrails into the prompt as plain clauses ('no on-screen text, no subtitles', 'no announcer delivery', 'no other speech')"
  references: "images enter as ordered frames: one pins the opening frame, two pin start and end, three or more become ordered waypoints the shot passes through; a video input is continued from its final frames. A clip sent to the edit tool is the thing being changed, and the owner demonstrates a reference-video input that carries a clip's cast into a new shot"
  world_knowledge: "combines pretraining knowledge with real-time grounding, so naming a real work, era, format, or event usually yields correct specifics without supplying them"
sources:
  official: ["https://docs.bfl.ai/guides/prompting_video_overview", "https://docs.bfl.ai/guides/prompting_video_text_to_video", "https://docs.bfl.ai/guides/prompting_video_audio", "https://docs.bfl.ai/guides/prompting_video_image_to_video", "https://docs.bfl.ai/guides/prompting_video_camera_terms", "https://docs.bfl.ai/flux_3/flux3_video", "https://bfl.ai/blog/flux-3-video", "https://bfl.ai/blog/flux-3", "https://docs.bfl.ai/guides/prompting_video_editing", "https://docs.bfl.ai/flux_tools/flux_video_edit", "https://docs.bfl.ai/cookbook/video_edit_recast_continue"]
  provider: ["https://fal.ai/learn/tools/flux-3-video-examples-prompts"]
  community: []
last_verified: "2026-10-15"
---

# FLUX 3 Video: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, input counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- FLUX 3 Video is a different prompt scheme from both image schemes, FLUX.2 and FLUX 3 Image. Do not carry their habits across: FLUX.2's JSON prompts and hex pinning, and FLUX 3 Image's bounding-box table and edit-only hex codes, are not documented for video.
- Picture and audio are generated together from one prompt. There is no second audio prompt, so the soundtrack is written into the same sentences as the shot.
- Direct a scene, do not describe a collection of objects. Say what happens, how subjects move, how the camera behaves, and what it sounds like.
- There is no negative field. Write exclusions into the prompt as plain clauses.
- This guide covers FLUX 3 Video and the separate FLUX Video Edit [fast] tool. FLUX 3 Image and the open-weights FLUX 3 Image Klein have their own guide; route FLUX 3 image work there. The announced open-weights FLUX 3 Dev has not shipped, and FLUX 3 Action is a robotics model that takes no video prompt.

</rules>

## Model names and aliases

| Name you may see | What it is | Guide |
| --- | --- | --- |
| FLUX 3 Image, `flux-3-image` | the full FLUX 3 image model, API only | FLUX 3 Image |
| FLUX 3 Image Klein, `flux-3-image-klein` | the 5.6B open-weights FLUX 3 image model, step-distilled; also on the API | FLUX 3 Image |
| FLUX 3 Image Klein Base, `flux-3-image-klein-base` | the undistilled Klein, open weights, for training and steering | FLUX 3 Image |
| FLUX 3 Video, `flux-3-video` | the FLUX 3 video model | FLUX 3 Video |
| FLUX Video Edit [fast] | a FLUX Tools video editor that takes a clip and an instruction | FLUX 3 Video |
| FLUX.2 [klein] 4B and 9B, `flux-2-klein-*` | the small open FLUX.2 models | FLUX.2 |
| FLUX.2 [pro], [flex], [max], [dev] | the other FLUX.2 models | FLUX.2 |
| FLUX 3 Dev | an announced open multimodal model that has not shipped | none |

<rules id="naming">

- "Klein" names two unrelated model lines. FLUX.2 [klein] and FLUX 3 Image Klein share a word and nothing else: different prompt schemes, different reference notation, and opposite defaults on prompt expansion. Resolve "klein" by the family number before applying any rule.
- FLUX 3 is not one prompt scheme. Its image models and its video model are documented and prompted separately; route by modality.
- FLUX 3 Dev was announced as an open multimodal model and has not been released. The open FLUX 3 releases are FLUX 3 Action, a robotics model that takes no image or video prompt, and FLUX 3 Image Klein.
- FLUX Video Edit [fast] is sold as a FLUX Tools product rather than under the FLUX 3 name. Its prompt rules sit in the FLUX 3 Video guide.

</rules>

## TL;DR

<template id="quickstart">

{camera} shot of {subject} {action} in {environment}. {supporting visual and motion detail}. {ambience and effects, or a quoted line with its speaker and delivery}.

</template>

## Models and modes

One model covers every generation workflow; what changes is which inputs you supply alongside the prompt. Editing a clip you already have is a separate tool, covered in its own section below.

- Text-to-video: prompt only. The model fills in framing, motion, and mood wherever you leave them open.
- Image-to-video: one image becomes the exact opening frame and the prompt drives the motion.
- Start and end frame: two images pin where the shot opens and where it lands, and the model generates the motion between them.
- Keyframes: three or more ordered stills become waypoints the shot passes through in turn, optionally pinned to times.
- Video continuation: an existing clip is carried forward from its final frames without a cut.

A draft workflow runs the same prompt as a fast cheap preview and then re-renders the approved take at full quality with the same subjects, composition, and motion. Iterate on drafts, not on full renders; the prompt is fixed at the draft stage, since the full render reproduces the approved take without re-reading it. Editing an existing clip has shipped as FLUX Video Edit [fast]. A reference-video input that carries a clip's cast into a new shot appears in the owner's cookbook, while the video overview still lists omni reference as coming; see "Reference video" below.

## How the model reads prompts

- Direct, do not list. Well-structured prompts with explicit motion, intentional shot language, and a clear narrative outperform piles of nouns.
- Short and long prompts are both valid, and they trade off. A short prompt hands the model framing, motion, and mood, which produces fresh and sometimes surprising results but leaves key details to chance. A long prompt buys precise control of scene, camera, pacing, and audio, at the risk that over-stuffing makes the motion less coherent.
- Start short to explore, then lengthen to lock in what matters. Add camera, motion, and atmosphere only where they improve control.
- Naming the format is the highest-leverage word in the prompt. "A 1987 local news report about teenagers at the mall" returns a news package; "teenagers at a 1980s mall" returns a shot. A format carries its own camera, lighting, and edit.
- It knows real subjects. Dates, construction sequences, publication years, and the order of events in a known work are often correct without being supplied, because pretraining knowledge is combined with real-time grounding. Name the work or the era and stop.
- Audio is generated with the picture, so scenes whose action implies sound give the audio more to work with. Footsteps, impacts, rain, engines, and crowds are easier than abstract visuals.
- Camera language is optional. Leave it out and the model infers a shot; add it when framing or motion behavior matters.
- The first prompt is a starting point, not the answer. Add context, remove ambiguity, or shift emphasis, and re-run.

## Prompt structure

<rules id="structure">

- Cover five things, in roughly this order: subject and action (who or what moves, and what exactly happens), camera direction (static, slow push-in, handheld follow, overhead drift, rapid pan), scene and atmosphere (environment, light, weather, time of day, mood), motion qualities (slow, abrupt, weightless, chaotic, precise, documentary), and continuity constraints (what must stay stable across the clip).
- Name each element with concrete nouns and verbs the camera can actually see. Vague adjectives leave the result to chance.
- Lead with subject and action, then wrap framing, movement, and style around it.
- State the aspect ratio in the prompt when the framing matters (16:9, vertical 9:16, 21:9), and say the clip length when pacing depends on it.
- To prevent unwanted cuts, say the shot is continuous and unbroken. The model will otherwise cut when it thinks a cut serves the scene.
- The owner's own long prompts put the one constraint that must hold in capitals ("ONE continuous unbroken real-time shot", "EXACTLY the same size") and close on a short stack of guardrails ("No on-screen text, no logos, no subtitles, no credits."). Reserve both for constraints the model keeps breaking.

</rules>

<template id="general">

{camera} shot of {subject} {action} in {environment}. {motion quality and supporting detail}. {lighting and atmosphere}. {audio}. {continuity constraints and guardrails}.

</template>

<example use_case="directed-one-liner">

```text
A low tracking shot of a fox sprinting through wet pine undergrowth at dawn. Mist drifts between the trees as the camera keeps pace beside it. Cool blue morning light, fast but controlled motion, cinematic naturalism.
```

*Why: subject and action first, then one framing term and one movement term, then light and motion quality, which is the shape the model reads most reliably*

</example>

## The four prompt formats

These are interchangeable shapes for the same content, not a quality ladder. Pick by how much control the shot needs.

<rules id="formats">

- One-liner: the default. A single flowing sentence with a consistent shape, so you can revise one part without touching the rest. Use it for quick ideas and B-roll.
- Labeled fields: break the prompt into named levers when you want to tune one in isolation without rewriting the sentence.
- Timestep: describe the shot as a short timeline when the action has to land on time. Keep each beat achievable, two or three for a short clip, and mark a hard cut where the angle changes.
- Schema: six elements (core summary, scene, subject description, dynamic narrative, audio, style and color) for work where a look and a story must hold across several shots. The subject description is held identically across shots, which is what keeps identity stable.
- Do not mix a timeline and a schema in one prompt. Pick the one that matches how the shot is actually organized.

</rules>

<template id="one-liner">

{camera} shot of {subject} {action} in {environment}. {supporting visual and motion details}

</template>

<template id="labeled-fields">

Camera shot: {framing and angle}
Subject + action: {who does what}
Depth of field: {shallow or deep, and what is sharp}
Lighting + palette: {light quality and color anchors}
Motion: {what moves in the frame}
Style: {overall look}

</template>

<example use_case="labeled-fields">

```text
Camera shot: wide shot, low angle
Subject + action: a lone rider crosses a shallow desert river
Depth of field: shallow (sharp on subject, blurred background)
Lighting + palette: warm backlight with soft rim, amber, cream, walnut
Motion: water splashes around the horse's legs, orange dust hangs in the light
Style: epic western realism
```

*Why: every lever is named and separable, so a single field can be changed between runs without disturbing the rest of the prompt*

</example>

<template id="timestep">

0.0-{t1}s - {opening framing and state}
{t1}-{t2}s - {the change that begins here}
{t2}-{end}s - {where the shot resolves}

</template>

<example use_case="timestep">

```text
0.0-1.5s - locked wide of a still harbor at dawn, boats motionless on glassy water
1.5-3.0s - a slow push-in begins as gulls lift off the water
3.0-5.0s - the sun breaks the horizon, warm light spreads and the camera settles
```

*Why: three achievable beats on an explicit clock, each naming both the camera state and what changes, so the action lands on time instead of drifting*

</example>

<template id="schema">

Core summary: {one line stating the whole sequence: who, where, and the arc}

Scene:
  Shot 1: {setting, light quality, depth of field}
  Shot 2: {setting, light quality, depth of field}

Subject description: {a fixed description repeated identically across every shot}

Dynamic narrative:
  Shot 1 [{start}s-{end}s]: {camera move and subject action}
  Shot 2 [{start}s-{end}s]: {camera move and subject action}

Audio:
  Shot 1: {soundscape}
  Shot 2: {soundscape}

Style and color: {global look, palette anchors, grain, dynamic range}

</template>

<example use_case="multi-shot-schema-flagship">

```text
Core summary: A three-shot sequence follows a lighthouse keeper through a night storm, from the lamp room to the gallery rail and back inside as the beam sweeps the water.

Scene:
  Shot 1: The lamp room interior, brass fittings and rain-streaked glass, the rotating lens throwing moving bars of light across the walls. Warm interior glow against black windows. Shallow depth of field.
  Shot 2: The exterior gallery, wind-driven rain slanting through the beam, black water heaving far below. Cold blue-grey light with a hard white core from the lamp. Deep depth of field.
  Shot 3: The lamp room again, calmer, condensation running down the glass. Warm low light, the storm now muffled. Shallow depth of field.

Subject description: A weathered keeper in his sixties, grey stubble, a heavy oiled canvas coat over a wool sweater, one hand permanently favoring a stiff shoulder.

Dynamic narrative:
  Shot 1 [0.0s-3.5s]: A slow dolly in past the rotating lens as he wipes the inner glass with a rag, his face lit in passing sweeps.
  Shot 2 [3.5s-7.0s]: Hard cut to a handheld shot on the gallery as he grips the rail, coat snapping in the wind, the beam raking across the rain behind him.
  Shot 3 [7.0s-10.0s]: Hard cut back inside. He pulls the door shut, leans against it, and the camera settles as the light continues its rotation.

Audio:
  Shot 1: Low mechanical hum of the lens gear, rain ticking on glass, the rag squeaking.
  Shot 2: Full storm roar, wind buffeting the microphone, waves booming against rock below.
  Shot 3: The door thuds closed, the storm drops to a muffled rumble, the gear hum returns, one long exhale.

Style and color: Realistic, high-fidelity cinematic sequence. Cold blue-grey exteriors against warm amber interiors, high dynamic range holding both the lamp's white core and deep shadow, fine grain throughout.
```

*Why: a long flagship that composes the full schema, holding one identical subject description across three shots so identity survives two hard cuts, giving every shot its own light, camera move, and soundscape, and tying it together with a single global palette*

</example>

## Camera and motion

<rules id="camera">

- Start with one framing term, one movement term, and one clear subject action. "A low tracking shot" is readable; "low aerial handheld orbit push-in" is not.
- Camera phrases are components, not prompts. Combine one with a subject, an environment, and a motion detail.
- Framing: macro, extreme close-up, close-up, medium shot, cowboy shot, full shot, two shot, wide shot, establishing shot.
- Angle: eye level, low angle, high angle, ground level, aerial, bird's eye, worm's eye, Dutch angle, over-the-shoulder, profile, POV, object POV.
- Composition: leading lines, center framing, rule of thirds, symmetry, negative space, frame within frame, foreground occlusion, silhouette, reflection framing, tableau.
- Movement: pan, tilt, dolly in, tracking, trucking, orbit, arc, crane or boom, pedestal, handheld, Steadicam follow, whip pan, dolly zoom, push through, locked-on.
- Focus and optics: shallow depth of field, deep focus, rack focus, split diopter, tilt shift, wide angle, telephoto compression, fisheye, macro, probe lens, anamorphic flares, halation, vignette.
- Time: slow motion, speed ramp, timelapse, fast motion, long exposure look, freeze frame, bullet time, cinemagraph.
- Lighting: rim light, chiaroscuro, golden hour, neon practicals, volumetric light, hard light, haze, spotlight, underwater caustics.
- Transitions between shots: match cut, whip transition, foreground wipe, jump cut, pass-through, quick cuts.
- Look and medium: stop motion, pixel art, kinetic typography, diorama, double exposure, datamosh, morphing, and named art directions such as dreamcore, dystopian, magical realism, maximalism.

</rules>

<example use_case="camera-led-shot">

```text
Steadicam follow shot tracking a chef weaving through a busy kitchen, flames flaring at the range as plates pass hand to hand, hard overhead light and steam catching in the air, ticket printer chattering and a dozen overlapping calls, 10 seconds, 16:9
```

*Why: one movement term drives the shot, the action supplies its own soundscape, and the framing and clip length are stated in the prompt text rather than assumed*

</example>

## Multi-shot sequences

<rules id="multishot">

- Label the shots and mark the cuts. "SHOT ONE ... HARD CUT. SHOT TWO ..." is enough to block several angles in one generation.
- Repeat the subject description identically in every shot. The model carries identity across a cut only if you restate it.
- Name one audio bed that runs across all shots, or each cut will bring its own soundscape.
- Give each shot one primary action and one camera move. Shots that try to do two things read as confusion, not coverage.
- For a single unbroken take, say so explicitly ("one continuous unbroken shot"). Without that, the model may insert a cut.
- Let the length carry the story. A longer clip is enough for a beginning, a turn, and an end without being asked for a sequence.

</rules>

<example use_case="hard-cut-sequence">

```text
SHOT ONE: wide aerial of a desert highway at dawn, a single red car speeding through. HARD CUT. SHOT TWO: interior close-up, the driver's hands drumming the wheel. HARD CUT. SHOT THREE: from the roadside, the car shrinks into the heat haze. One music bed across all three shots.
```

*Why: explicit shot labels and hard-cut markers block three angles in one generation, and naming a single music bed stops each cut from resetting the soundtrack*

</example>

## Audio, dialogue, and voice

Audio is generated in the same pass as the picture. A scene that clearly implies sound may be enough for a first pass; when the sound matters, write it into the shot.

<rules id="audio">

- Four layers are available and you rarely need all of them: speech (who speaks, the exact words, how they say it), ambience (the sound of the place), effects (sounds tied to visible actions), and music (style, pace, and where it sits in the mix).
- Name specific sources, not moods. "Distant traffic and rain ticking against a metal awning" gives the model more than "moody ambience".
- Name a quiet sound rather than asking for silence. "Rain against the window" or "a soft piano bed" works; "quiet room tone" can collapse into static or dead air.
- Tie effects to something visible in the frame or just outside it. That keeps the audio locked to the picture.
- When speech is the focus, keep other voices out of the background. Crowd conversation, a talking radio, or a second narrator competes with the line. Weather, machinery, footsteps, and traffic layer under speech cleanly because they add no words.
- Keep the mix to the one or two layers the scene actually needs.

</rules>

<template id="audio-layers">

{shot and action}.
Dialogue or voiceover: {speaker and exact words}.
Ambience: {place}.
Effects: {visible actions}.
Music: {style and role in the mix}.

</template>

<rules id="dialogue">

- Put the exact spoken words in quotation marks and say who delivers them.
- A visible speaker gives the model a face to lip-sync. An off-screen line needs an explicit "voiceover" or "narration" cue.
- A quoted line with neither a visible speaker nor a voiceover cue may be rendered as text in the frame instead of spoken. Make the distinction explicit, and add "no on-screen text, no subtitles" when the words must only be heard.
- Direct the voice with concrete anchors rather than praise words: person (age range and accent where they matter), register (low, bright, soft, rough), recording (close and dry, across a room, phone microphone, public address), delivery (hesitant, practical, lightly amused, talking to one friend), and a guardrail ("no announcer delivery", "no sales voice", "do not over-enunciate").
- Write lines a person would actually say. Use contractions, cut setup the viewer can already see, avoid ending every line on a slogan, and keep punctuation simple, since heavy punctuation turns into a sing-song rhythm.
- Leave room for the line. A short line in a longer clip is safer than copy written to fill every second; if the last word is clipped, shorten the line or give the shot more time.
- In an edit the clip cannot get longer, so a replacement line must fit the time the original speech took. Write it to that length; a longer one keeps its opening and loses the rest.
- Do not force several speakers, a long script, and multiple visual beats into one short clip. Split the scene when each part needs its own timing.

</rules>

<example use_case="on-camera-dialogue">

```text
Medium close-up of a tired station attendant behind the glass. She looks toward the stranded passenger and says, "The 6:10 is delayed again. They say ten minutes." Low, matter-of-fact delivery. Fluorescent room tone and rain against the platform roof. No on-screen text or subtitles.
```

*Why: a visible speaker gives the model a face to lip-sync, the line is quoted with its delivery, the ambience has two named sources, and the guardrail stops the words appearing as caption text*

</example>

<example use_case="voiceover">

```text
Locked shot of a studio microphone in a small treated booth. An off-screen voiceover says exactly once, "Most good tools have one thing in common. You stop noticing them." Close, dry recording. Rain against the window. No music, no second voice, no on-screen text or subtitles.
```

*Why: the off-screen cue is explicit so the line is not attached to a face, the recording character is named, and three separate guardrails keep the take clean*

</example>

<example use_case="dialogue-flagship">

```text
One continuous unbroken real-time ten-second cinematic shot inside a small dim basement jazz club, late set. A live trio (upright bass, brushed drums, and piano) plays a slow, smoky number continuously from the first frame to the last, never stopping. Slow dolly along the bar toward a bartender in a rolled-sleeve white shirt polishing a glass. Over the music, he leans toward a regular seated at the bar and says in a low, warm voice: "Last call was an hour ago. For you, the night is still young." The music keeps playing under and after his words. Audio: the jazz trio constant throughout, murmur of a few late patrons, the soft clink of the glass as he sets it down, and a faint espresso-machine hiss from the back. No on-screen text, no subtitles.
```

*Why: a long flagship that pins the take as unbroken, gives the camera one move, quotes the line with a register and a volume relationship to the music, and then names all four audio layers explicitly instead of leaving the mix to inference*

</example>

### Languages and accents

<rules id="languages">

- Name the language directly and place the label beside the line it belongs to. Supply the line in native script, in a romanized form, or as a plain-language instruction naming the language and meaning; quote the line when the exact words matter.
- For one speaker switching languages, label each line, put the lines in the intended order, say the same speaker continues across the switch, and keep each segment short enough for a natural pause.
- For several speakers, identify each by a visible role rather than a name ("the orange-suited astronaut"), then give each one a language, a line, and a delivery, and keep the turns separate with no overlap.
- Treat an accent as part of a character and a situation, not an isolated adjective. Pair it with pace, projection, emotion, and who the person is speaking to.
- Language, accent, line order, speaker attribution, and timing are directable targets, not exact controls. Judge each take by ear when the performance matters.
- Reusing the full voice direction across clips preserves the kind of voice but not a fixed performer. Treat the wording as casting direction and compare takes before cutting them together.

</rules>

<example use_case="two-speaker-multilingual">

```text
One continuous unbroken real-time ten-second cinematic shot inside an orbital greenhouse during a meteor shower. Medium two-shot: an astronaut in an orange work suit steadies a glowing irrigation valve on the left while an astronaut in a blue work suit reaches for the petal-shaped roof controls on the right. The orange-suited astronaut speaks first in Spanish, practical and excited: "Las raíces están listas." After she finishes, the blue-suited astronaut replies in French, smiling with quiet wonder: "Alors, ouvrons le ciel." Keep the speakers distinct, the turns short and separate, with no overlap and no other speech. Audio: soft ventilation, water moving through transparent pipes, roof servos, and distant muted meteor impacts; no music. No on-screen text, no subtitles.
```

*Why: each speaker is identified by a visible role rather than a name, each gets one language, one quoted line, and its own delivery, and the turns are explicitly ordered and non-overlapping*

</example>

## By mode

### Text-to-video

<example use_case="text-to-video">

```text
A cozy ramen shop on a rainy Tokyo night: steam rising from the broth, neon reflections in the window puddles, the cook working calmly. The camera drifts slowly past the counter. Rain patter and quiet kitchen sounds.
```

*Why: a complete scene in three clauses, one gentle camera move, and two named ambient sources, which is enough direction without over-constraining the motion*

</example>

### Image-to-video

The supplied image becomes the exact opening frame; the prompt supplies the motion only.

<rules id="i2v">

- Describe what happens next, not what the image already shows. Re-describing the frame wastes the prompt and can fight the pinned first frame.
- Name the motion and the camera behavior, since those are the only things the still cannot supply.
- Add the audio the motion implies, because the source image carries none.

</rules>

<example use_case="image-to-video">

```text
Push slowly forward between the trees as the mist thins ahead, branches drifting past the edges of frame and light strengthening toward the clearing. Wind in the canopy, distant birdsong, footfalls on wet leaves.
```

*Why: says only what changes from the pinned first frame, names one camera move and one atmospheric change, and supplies the soundscape the still cannot carry*

</example>

### Start and end frame

<rules id="first-last">

- Keep the two frames related, sharing a subject, scene, or camera setup, so the interpolation has a plausible path. The wider the gap, the more the model improvises.
- Write the prompt as the transformation between the two frames, naming the path rather than restating either frame.

</rules>

<example use_case="start-and-end-frame">

```text
A wide waterfront city skyline transitions from bright midday to glittering night: daylight fades through dusk to dark, thousands of lights switching on across the towers and shimmering on the water.
```

*Why: describes the journey between the two pinned frames as a continuous change, so the model has a route rather than two disconnected states*

</example>

### Keyframes

<rules id="keyframes">

- Order matters: the frames are read as a timeline from first to last. Space them so each transition is achievable.
- Keep the look consistent across frames so the result reads as one take rather than a series of cuts.
- Write one prompt that describes the whole arc through the waypoints, not one clause per frame.

</rules>

<example use_case="keyframes">

```text
A wide long-exposure night sky over snowy northern mountains: the aurora borealis sweeps and ripples, shifting from soft magenta and violet into teal and finally vivid green above the frozen horizon.
```

*Why: one continuous description that names the ordered colour states the pinned frames carry, so the interpolation reads as a single evolving shot*

</example>

### Video continuation

<rules id="continuation">

- The source clip sets the motion, subjects, and look. The prompt only says how the shot keeps unfolding.
- Write the continuation as an unbroken extension, not a new scene, unless a cut is what you want.
- Momentum carries across the seam, so name what the existing motion does next rather than restarting it.
- Name what the final frames show before saying where the shot goes: "Continue this video from its final frames: {what is on screen at the end}, then {what happens next}".
- Carry the established sounds through the seam unbroken before evolving them, then give each new event its own sound. Audio continuity is what makes an extension read as one shot rather than two clips joined.

</rules>

<example use_case="video-continuation">

```text
A herd of African elephants walks steadily toward the camera across a dry savanna beneath a huge hazy orange sunset, the animals growing larger in frame as the sun sinks lower behind them.
```

*Why: continues the existing motion in the same direction and names a slow change (scale, sun height) that gives the extension somewhere to go without breaking the seam*

</example>

### Reference video

Shown in the owner's cookbook on a preview surface; the video overview still lists omni reference as coming, so treat this as available where a host exposes it rather than as a guaranteed mode. A source clip supplies a cast and its motion, and the prompt decides how much of the source survives.

<rules id="reference-video">

- How much of the source you restate is the lever. Restate the staging and change only the medium, and you get the same shot recast. Re-list only the identity anchors and write a new scene around them, and you get the same character in a new shot.
- Give a clip you plan to reference three or four fixed visual anchors and one unmistakable motion, described the same way every time.
- Mechanical subjects drift toward smooth human movement unless the imperfection is written in: "stiff even steps, a faint mechanical tremor on each footfall", with the sound locked to the motion.
- The medium includes the sound. When you swap a medium, name the audio swap too, or a modern soundtrack stays under an old-looking picture. Add the medium's own guardrails ("no intertitle cards").

</rules>

<example use_case="reference-video-recast">

```text
The same brass wind-up tin robot from the source video, same red wind-up key turning in its back, same single amber eye, marches in the same straight line across the same watchmaker's bench, same tracking camera alongside it. The whole scene is now a scratched 1928 silent film print: soft black-and-white, heavy grain, flickering exposure, gate weave, dust and hairline scratches, a slightly sped-up hand-cranked judder. The sound is recast to the medium: the clockwork ticking is gone, replaced by a lively solo upright-piano march that hits in time with the robot's steps, under the soft clatter of a film projector running in a quiet room. No on-screen text, no intertitle cards.
```

*Why: the owner's recast. It repeats the staging and anchors word for word so the shot survives, changes only the medium, and recasts the sound along with the picture*

</example>

## Editing an existing clip

FLUX Video Edit [fast] takes a clip and an instruction. It is a separate FLUX Tools product rather than a FLUX 3 mode, and everything the prompt does not mention stays as filmed: length, framing, camera, timing and audio all come from the source.

<rules id="video-edit">

- Describe the change, not the shot. The shortest prompt that names the change is usually right; add detail only where the edit needs it. Never re-describe the whole scene.
- Write it as an instruction: Remove, Add, Replace, Make, Change, Restyle, Render, Say. A sentence describing a new event also works ("A gull swoops down and steals a fish from the crate.").
- Place what you add, and give it a size and a look, or the model chooses. "Add a lighthouse" lands small and far off; anchor it to things already in the shot ("on the end of the harbor wall to the right of the boats"). A pose works as a placement ("standing on the corner of the crate").
- There are no masks, so locate the target in words: by what it is, its color, or what it is next to.
- For a replaced person, say which wardrobe carries over ("wearing the same yellow apron and grey cap").
- For a new setting, name the surfaces the subject touches as well as the surroundings, so hands and feet have something to hold: "Add narrow metal window ledges at the climber's hand and foot contact points."
- For an effect such as weather, say where it lands on the scene's objects: "with flakes settling on the crate and the fish".
- For a text change, name the text object and its medium, then the new words: "Change the stencil on the crate to read DAILY CATCH."
- For dialogue, give the new line in quotes and write it to the length of the line it replaces; the clip cannot grow to fit more words. For a translation, ask for the same sentence and fence off the source language: "Say the same sentence entirely in German, with no English words."
- Audio is kept unless you ask for a dialogue or sound change, and a silent source returns a silent result. You cannot add speech or sound to a clip that has none.
- A stylization can be named in one line ("Make the whole clip a hand-drawn watercolour animation."). Converting an illustration to live action needs the new look described through materials and physical behaviour: fabric, seams, metal, reflections.
- To turn a blockout or previz into a finished shot, say what each placeholder becomes, then what must stay ("Same weave lines, same speeds, same camera overtake"), then the sound.
- Small local edits stack in one prompt as separate sentences. A global change (a new setting, a restyle, a time of day) goes in its own pass: feed the result back in and describe the next change, rather than combining both against the original.
- Recolor with a plain color name. No hex code appears in any owner video-edit example.
- Check the whole frame after an edit, not only the thing you changed. Untouched details can still drift.
- The tool cannot extend a clip, take an image or a style or motion reference, or edit audio alone. Extend with video continuation instead.

</rules>

<template id="video-edit">

{Operation} {the target, located in words} {into what, with placement, size and look}. {Any detail that must carry over}.

</template>

<example use_case="video-edit-add-with-placement">

```text
Add a tall white lighthouse with a red lantern room standing on the end of the harbor wall to the right of the boats.
```

*Why: the owner's placed addition. Appearance, size and an anchor to two things already in the shot, so it neither lands as a speck on the horizon nor drifts between frames*

</example>

<example use_case="video-edit-stacked-local">

```text
Remove the orange bucket. Make the apron red. Change the stencil on the crate to read DAILY CATCH. Add a seagull standing on the corner of the crate. Make it snow, with flakes settling on the crate and the fish.
```

*Why: the owner's stack of five small local edits, one sentence each, with the new object placed by pose and the weather told where to settle*

</example>

<example use_case="video-edit-dialogue">

```text
Make him say "Fresh mackerel, four for ten."
```

*Why: the owner's dialogue swap. The original line ran "Straight off the boat this morning, four for ten.", so the replacement is written to the same short length and nothing else is touched*

</example>

<example use_case="video-edit-setting">

```text
Replace the cliff with the reflective windows of a high-rise building. Add narrow metal window ledges at the climber's hand and foot contact points. Far below, traffic and illuminated buildings fill a dense city in blue-hour light.
```

*Why: the owner's setting swap. The new surroundings, the contact surfaces the climber's motion needs, and the light of the new place, with the climb itself left as filmed*

</example>

<example use_case="video-edit-restyle-to-live-action">

```text
Restyle this clip as live-action footage of a claw machine lifting a lavender octopus plush. Fine velour fibers and sewn seams replace the ink outlines. The plush compresses gently where the metal claw grips it. Soft arcade lights reflect in the glass.
```

*Why: the owner's illustration-to-live-action restyle, described through material, contact and reflection rather than a style name*

</example>

<example use_case="video-edit-blockout">

```text
Render this previz chase as a desert convoy pursuit at golden hour: the pillars become ruined highway columns in open dust, the lead car an armored pickup, the chaser a spiked buggy, both trailing dust plumes, heat shimmer. Same weave lines, same speeds, same camera overtake. V8 roar and wind.
```

*Why: the owner's blockout pass. Each placeholder is mapped to what it becomes, the motion that must survive is pinned in one line, and the sound is named. A second change, such as night, goes in a separate pass on this result*

</example>

## On-screen text and typography

<rules id="text">

- Quote the exact words and say where they sit. Typography renders as part of the scene, which covers titles, signage, and lower thirds.
- Say where the text sits and what it is made of, the same way you would describe any other object in the shot.
- Text can be the subject rather than an overlay: letters can assemble, stack, and move as scene elements.
- When a quoted line is meant to be spoken and not seen, add "no on-screen text, no subtitles". Without it, the model may render the words in frame.

</rules>

<example use_case="kinetic-title">

```text
Bold kinetic title card, the word "FLUX" assembling from streaks of light on a dark stage, letters settling into place as the last streak lands, low bass swell rising under the movement, 16:9
```

*Why: the exact word is quoted, the type is treated as the moving subject rather than an overlay, and the audio is tied to the moment the motion resolves*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- There is no negative field. Every exclusion goes into the prompt as a plain clause.
- Prefer describing the desired state. "Sharp focus throughout" beats asking for no blur.
- Keep the recurring guardrails short and specific: "no on-screen text, no subtitles" for spoken lines, "no announcer delivery" or "no sales voice" for reads, "no other speech" when a line must stay clear, "no music" when a bed would crowd the scene.
- Name the sound you want instead of asking for its absence, since a request for silence can produce dead air.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Spoken line appears as caption text: name a visible speaker or say voiceover, keep the exact line in quotes, and add "no on-screen text or subtitles".
- Read sounds like an advertisement: replace praise words with a person, a recording setup, and a social situation, then add "no announcer delivery".
- Sing-song cadence: simplify the punctuation, vary the sentence shapes, and ask for a relaxed conversational rhythm.
- Garbled words: remove competing speech such as crowd conversation, a talking radio, or a second voice.
- Last word clipped: shorten the line or give the shot more room rather than speeding up the delivery.
- Generic soundscape: name the source of each sound and tie every effect to a visible action.
- Camera word pile-up: stacking framing, rig, and movement terms in one phrase makes the shot less readable, not more controlled.
- Asking for silence: a request for a quiet room can collapse into static. Name a soft sound source instead.
- Over-stuffing: past a point, more description degrades motion coherence rather than improving control.
- Re-describing a pinned frame: in image-to-video, the still already carries the scene. Spend the prompt on what changes.
- Unrequested cuts: if the shot must be one take, say it is continuous and unbroken.
- Carrying image habits over: FLUX.2's JSON prompts and hex pinning, and FLUX 3 Image's bounding-box tables, are image-scheme features and are not documented for video.
- Re-describing the shot in an edit: the edit tool keeps everything the prompt does not mention. A full scene description invites it to change things you meant to keep.
- An unplaced addition in an edit: without a size and an anchor it lands small and far away.
- A replacement line longer than the original: the clip cannot grow, so the end of the line is lost. Write to the original's length.
- Asking for speech in a silent clip: the edit tool keeps the source's audio, and a silent source stays silent.
- Stacking a global change with other edits: do the restyle, setting or time-of-day change as its own pass and edit the result.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

- Official (Black Forest Labs): [video prompting overview](https://docs.bfl.ai/guides/prompting_video_overview), [text-to-video](https://docs.bfl.ai/guides/prompting_video_text_to_video), [audio and speech](https://docs.bfl.ai/guides/prompting_video_audio), [image-to-video](https://docs.bfl.ai/guides/prompting_video_image_to_video), [examples and cheatsheet](https://docs.bfl.ai/guides/prompting_video_camera_terms), [video editing](https://docs.bfl.ai/guides/prompting_video_editing), [FLUX 3 Video docs](https://docs.bfl.ai/flux_3/flux3_video), [FLUX Video Edit](https://docs.bfl.ai/flux_tools/flux_video_edit), [recast and continue video](https://docs.bfl.ai/cookbook/video_edit_recast_continue), [FLUX 3 Video announcement](https://bfl.ai/blog/flux-3-video), [FLUX 3 announcement](https://bfl.ai/blog/flux-3).
- Provider: [fal FLUX 3 examples and prompting notes](https://fal.ai/learn/tools/flux-3-video-examples-prompts).

Coverage note: re-checked 2026-10-15. FLUX 3 Image and FLUX 3 Image Klein have shipped with their own prompting docs and their own guide. FLUX Video Edit [fast] shipped as a separate FLUX Tools product and is covered here because its prompts are video prompts; its rules come from the owner's video editing guide and product page. The "recast and continue" cookbook, despite its address, runs on FLUX 3 Video's own reference-video and continuation inputs rather than on the edit tool, and its reference-video input is shown on a preview surface while the overview still lists omni reference as coming. The text-to-video, audio, image-to-video and camera pages carry no craft change since August. The fal article predates general availability and its stated resolutions and clip lengths are out of date; only its prompt-craft observations are used here. Structure and notation decisions are recorded in `sources/flux-3/flux-3-notation-resolution.md`.

Last verified: 2026-10-15.
