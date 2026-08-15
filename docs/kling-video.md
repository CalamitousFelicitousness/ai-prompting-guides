---
guide: "Kling"
prompt_scheme: "kling-video"
models:
  - { id: "kling-v3", access: "closed-weights", tier: "flagship", caps: [text-to-video, image-to-video, first-last-frame, multi-shot, native-audio, dialogue, singing, rap, elements, motion-control], best_for: "the mainline flagship. Native audio, multi-shot storytelling, five speech languages, strongest element consistency. The default choice" }
  - { id: "kling-v3-omni", access: "closed-weights", tier: "flagship", caps: [text-to-video, image-to-video, first-last-frame, video-edit, shot-extension, multi-shot, native-audio, dialogue, singing, rap, elements, reference-video, motion-control], best_for: "everything kling-v3 does PLUS video input: editing, restyling, shot extension, video elements with bound voice. Reach for it when a video is an input, not just an output" }
  - { id: "kling-3.0-turbo", access: "closed-weights", tier: "distilled", caps: [text-to-video, image-to-video, first-last-frame, multi-shot, native-audio, dialogue, singing, rap, motion-control], best_for: "the cheap seat for 3.0-era work. Text and image in only, no video input, no element control. Compose here, re-render the keeper on kling-v3" }
  - { id: "kling-video-o1", access: "closed-weights", tier: "legacy", caps: [text-to-video, image-to-video, first-last-frame, video-edit, shot-extension, elements, reference-video, motion-control], best_for: "3.0 Omni's predecessor and the origin of the edit grammar. Video input and editing, but NO multi-shot and NO audio. Prefer kling-v3-omni" }
  - { id: "kling-v2-6", access: "closed-weights", tier: "legacy", caps: [text-to-video, image-to-video, first-last-frame, native-audio, dialogue, motion-control], best_for: "the first Kling model with native audio, and the only one whose docs state the dialogue rules outright. Two speech languages, no multi-shot" }
  - { id: "kling-v2-5-turbo", access: "closed-weights", tier: "legacy", caps: [text-to-video, image-to-video, first-last-frame, motion-control], best_for: "silent video only. No audio layer exists here at all, so every sound, dialogue and voice rule in this guide is inert" }
capabilities: [text-to-video, image-to-video, first-last-frame, video-edit, shot-extension, multi-shot, native-audio, dialogue, singing, rap, elements, reference-video, motion-control]
prompt:
  languages: ["en", "zh"]
  speech_languages: "NOT the same as prompt language, and it MOVES BY VERSION. The 3.0 series speaks five: Chinese, English, Japanese, Korean, Spanish. Kling 2.6 speaks two: Chinese and English. Kling 2.5 Turbo speaks none. An out-of-set language FAILS SILENTLY: it is translated to English and voiced in English, with no error"
  formula: "the owner publishes SIX variants across six surfaces and never reconciles them. The canonical one, from the dedicated text-to-video prompt guide, is Subject (subject description) + Subject Movement + Scene (scene description) + (Camera Language + Lighting + Atmosphere). The others rename or re-slice the same parts, so treat the slots as the formula and the ordering as loose; Kling's own newest surface declines to call it a formula at all. The exception is the image-to-video formula, which is genuinely different and drops the scene slot entirely; see 'By mode'"
  length_strategy: "no owner guidance of any kind, on any surface. Measured across the owner's own examples the range is roughly 35 to 115 words, clustering near 55 to 75. Do NOT assume the length-scales-with-duration rule from other families; Kling never states it. Duration is stated IN the prompt text instead"
  multi_shot: "in-prompt shot syntax; canonical form is 'shot n, m, words;' with semicolons. Availability is 3.0-series only; O1, 2.6 and 2.5 Turbo are single-shot"
  dialogue: "canonical form is a bracketed speaker label carrying a voice descriptor, then the line in double quotes. Turns MUST be separated by an explicit temporal connective or the model runs them together as one speaker"
  auto_expand_behavior: "none documented on any surface. Kling does not claim to rewrite or expand a terse prompt; what you write is what is read"
  negatives: "no owner guidance on any surface. There is no negative-prompt technique to teach. Kling's demonstrated house style is to state the desired positive condition instead"
  structured_json: "none. Kling is natural language only. The multi-shot and referent grammars are inline text conventions, not JSON"
  references: "a token bound to the caller-assigned input id, written inline in the prompt. OPTIONAL: use it only to disambiguate when two inputs could fill one role"
sources:
  official: ["https://kling.ai/document-api/guides/capability-map/video", "https://kling.ai/document-api/apiReference/model/textToVideo", "https://kling.ai/document-api/apiReference/model/imageToVideo", "https://kling.ai/document-api/api/video/o1", "https://kling.ai/document-api/updates/api", "https://kling.ai/quickstart/klingai-video-3-model-user-guide", "https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide", "https://kling.ai/quickstart/klingai-video-o1-user-guide", "https://kling.ai/quickstart/klingai-video-26-audio-user-guide", "https://kling.ai/blog/kling-ai-prompt-guide", "https://kling.ai/blog/kling-ai-camera-control-video-guide", "https://kling.ai/blog/kling-ai-motion-prompts-guide", "https://kling.ai/blog/kling-3-subject-binding-character-consistency", "https://kling.ai/quickstart/text-to-video-prompt-guide", "https://kling.ai/quickstart/image-to-video-guide"]
last_verified: "2026-07-16"
---

# Kling: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- This guide is VIDEO only. Kling also has a full image line whose models reuse the same ids (`kling-v3` and `kling-v3-omni` each name both a video model and an image model, told apart only by endpoint). The image line is a separate scheme and is not covered here.
- Write natural language. There is no JSON prompt form. The two inline conventions that ARE syntax, the multi-shot form and the referent token, are described in their own sections.
- Kling is TWO MODEL LINES, not one ladder, and the version numbers hide it. The owner states: "the Kling VIDEO 2.6 model has been upgraded to VIDEO 3.0, and the Kling VIDEO O1 model has been upgraded to VIDEO 3.0 Omni". O1 is NOT older than 2.6; it is 3.0 Omni's predecessor on a parallel line. Do not read the numbers as a ranking.
- THE PROMPT MODE INVERTS WITH THE INPUT, inside a single model. With no video input, the prompt DESCRIBES the finished shot. With a video input, the prompt INSTRUCTS an editor ("Remove the bystanders"). Get this backwards and the model does nothing useful. See "By mode".
- Audio is a mode, never a keyword. No phrase in the prompt turns sound on. Where a host exposes the toggle and it is off, every sound and dialogue word you wrote is inert; where it is on, the sound you did not describe is still generated, just not chosen by you.

</rules>

## TL;DR

<template id="quickstart">

{subject with the traits that matter} {action in present tense}. {scene: location, lighting, atmosphere}. {ONE camera move, with its destination}. {[Speaker, voice descriptor]: "{line}"}. {ambient sound and music}.

</template>

## Models and when to use which

The prompt grammar is shared across the family, so a prompt written once mostly transfers. What changes is which layers EXIST, and a layer that does not exist fails silently rather than erroring.

- `kling-v3` is the default. `kling-v3-omni` is the same thing plus video input, so pick it when a video is an input rather than only an output. `kling-3.0-turbo` is the cheap seat: text and image only, no element control.
- `kling-video-o1` is where the edit grammar came from and still works, but it has neither multi-shot nor audio. Prefer `kling-v3-omni` for anything new.
- THREE HARD FORKS inside this family, in descending order of how badly they bite:
- Audio does not exist below `kling-v2-6`. The owner is blunt about it: "Previously, KLING's video models could only generate 'silent visuals'." Every dialogue, sound and voice rule in this guide is inert on `kling-v2-5-turbo`, and inert on `kling-video-o1`, whose docs never mention sound at all.
- Multi-shot is 3.0-series only. Shot syntax sent to O1, 2.6 or 2.5 Turbo is just words in a prompt.
- Voice binding CHANGED GRAMMAR between versions. On `kling-v2-6` you bind a voice inline in the prompt text. On the 3.0 series the voice is bound to an element out of band and you are told not to restate it. These are opposite instructions; check which model you are writing for.

## How the model reads prompts

- Nothing is auto-expanded. No Kling surface documents prompt rewriting or enhancement, so a terse prompt stays terse. Detail is your only lever: the owner's own line is "the level of details in the prompt determines the richness of content in the generated video".
- Prompt language and SPEECH language are different things. Write the prompt in English or Chinese; write each spoken line in the language you want heard, in that language's own script.
- Camera, motion and localized effects are PROSE, not tool panels. This is recent and deliberate. The owner now teaches camera as text ("In AI video, the motion is described through text") and explicitly steers away from the old widgets: describe movement "instead of treating the model as a separate director feature", and write localized motion "rather than as a tool command". Older Kling material that reaches for a camera-control setting or a motion brush describes a superseded workflow.
- The model reads cinematic vocabulary directly. Shot sizes, angles, and named moves all land as written.

## Prompt structure

Kling publishes four formulas across four surfaces and reconciles none of them. They are variations on one slot set, so learn the slots and hold the ordering loosely. The newest surface declines to call it a formula at all: prompts are "built from clear scene direction rather than secret formulas".

<rules id="structure">

- Cover the slots that matter for the shot: SUBJECT, ACTION, SCENE, CAMERA, LIGHTING AND MOOD, and SOUND where audio exists. Not every slot every time; a slot that does not serve the shot is padding.
- Lead with whatever anchors the shot. The owner's examples variously open with style ("American cartoon style animation"), with the camera ("A smooth and deliberate dolly-in tracking shot approaching..."), or with the scene. All three work.
- ENVIRONMENTAL MOTION is a slot Kling treats as first-class and most families ignore: what the world does in response to the subject. Leaves pulled by wind, dust rising after a step, water spreading from a landing, cloth lifting, hair trailing. The owner's motion formula puts it between the action and the camera.
- State duration IN the prompt when pacing matters. This is prompt text, not a parameter, and the owner's own examples do it: "a 4-second duration", "A smooth and deliberate 5-second dolly-in".
- Describe only what a viewer could SEE or HEAR. The owner's recurring rule: "Visible motion language is safer and clearer than internal technical claims."

</rules>

<template id="general">

{style or register}. {subject with the traits that matter} {action, in visible stages}. {scene, lighting, atmosphere}. {environmental response to the action}. {one camera move, with its destination}. {sound: ambience, music, and any dialogue}.

</template>

## Cinematic vocabulary

The owner's canonical camera list, complete: push in, pull back, pan left, pan right, tilt up, tilt down, track forward, orbit slowly, static camera. Also used freely in examples: dolly in, tracking shot, and the framing terms extreme close-up, medium close-up, medium shot, medium-wide, full body shot, wide shot, establishing wide shot, low angle, and shallow depth of field. Composition terms Kling names: centered, rule of thirds, off center.

<rules id="camera">

- ONE MAIN CAMERA MOVE PER SHOT. This is stated: "A common mistake is asking for too many movements at once." A secondary move is tolerated only if you mark it subtle or gentle and it serves the same reveal, which is exactly what the owner's own compound example does.
- NAME THE DESTINATION, not just the direction. The owner teaches this as a pattern: "Start with [close/wide view], then [camera movement] to reveal [final view]." A pull-back needs both a clear starting subject and a clear revealed environment, or "the model may not know what to reveal".
- Weld the camera to the subject's action. "camera slowly pushes in on the character's face as she turns toward the window" beats "cinematic camera movement", because the model gets both halves.
- Prepositions carry meaning and the owner is consistent: push and dolly take "toward" or "on"; pull back and tilt take "from X to Y" or "from X to reveal Y"; pan takes "across" or "from left to right".
- Express speed as adverbs, not magnitudes. Slow, gradually, smooth, steady, no sudden motion. The owner never writes numeric camera speeds.
- Match the move to the scene. A product detail wants a slow push-in; a landscape wants a pull-back; a runner wants a tracking shot. "Random movement can make the clip harder to read."

</rules>

## Motion

<rules id="motion">

- Move past the bare verb. "A man running." is the owner's own named anti-pattern; the fix is visible speed, effort, posture, surface contact and camera relationship.
- Build the action in three visible stages: PREPARATION, MAIN ACTION, FOLLOW-THROUGH. For a jump that is the crouch, the arc, the landing. For a run it is the forward lean, the arm drive, the foot contact.
- The owner's motion checklist, to spend words on: posture, speed, direction, ground contact, camera relationship, clothing motion, environmental response, emotional intent.
- Reduce competing actions before adding style. "When anatomy or timing feels wrong, simplify the scene before adding style."

</rules>

<example use_case="motion-with-environmental-response">

```text
A full body shot of a man sprinting through a neon-lit city street, steam rising from the pavement, tracking shot following the athlete, cinematic depth of field, 4-second duration
```

*Why: the owner's own before-and-after fix for "A man running." Subject, then action, then the environment's response to it, then the camera, then style and duration, all in the motion formula's order*

</example>

## Multi-shot and storyboards

Available on the 3.0 series only. The shot list goes in the prompt text.

<rules id="multishot">

- The canonical form is `shot n, m, words;` with standard semicolons between shots: n is the shot number in sequence, m is that shot's duration in seconds, words is that shot's prompt.
- EVERY SHOT'S DURATION MUST SUM TO THE TOTAL. This is the one hard arithmetic rule in Kling's prompt grammar. Each shot also needs a floor of at least a second.
- Give each shot ONE JOB. The owner's own framing: a wide establishing shot, then a push-in, then a tilt to a detail, then a pull-back to close. "This structure works better than putting every instruction into one long paragraph."
- Write cross-shot continuity into the text. Nothing carries lighting or time of day between shots for you; the owner's example says so explicitly in prose ("Golden hour lighting and long shadows remain perfectly consistent with Shot 1").
- Where a host exposes a multi-shot toggle and it is OFF, shot syntax is ignored and you get a single shot. Where it is on but the scene suits one shot, the model may collapse to one anyway: automatic shot planning "will generally follow the prompts" but flexes. Only an explicit shot list is honored strictly.
- Subjects do NOT reliably carry between shots by pronoun. Name the subject again, or bind it to an element.
- The owner demonstrates several other shot notations on its web-app surfaces (a parenthesized-duration form, a timecode-block form, a bracketed-label form). Those are product-surface demonstrations. Nothing states they parse identically through an API, so prefer the semicolon form above when writing through one.

</rules>

<example use_case="multi-shot-with-durations">

```text
shot 1, 3, wide establishing shot of a rain-soaked Tokyo alley at night, neon signs bleeding red and cyan into standing water, static camera; shot 2, 4, medium shot, a courier in a dripping yellow jacket stops and looks up at a doorway, the camera slowly pushes in on her face; shot 3, 3, close-up of her hand pulling a soaked envelope from inside the jacket, water running off the paper; shot 4, 5, low-angle wide shot as she steps through the doorway and the alley light falls away behind her, the camera pulls back to reveal the empty street, neon and rain consistent with shot 1
```

*Why: four shots numbered in sequence, durations summing to the total, one camera job per shot, and cross-shot continuity ("consistent with shot 1") stated in the text because nothing carries it automatically*

</example>

## Audio and dialogue

Native audio exists from `kling-v2-6` upward, and not at all below it. Audio is generated jointly with the picture from the same prompt, so a prompt with no sound written into it still produces sound, just sound you did not choose.

### Dialogue

Kling's surfaces show several dialogue conventions, but only one is ever stated as a RULE with named failure modes, and only one is valid across the whole family. Use it.

<rules id="dialogue">

- The canonical form is a bracketed speaker label carrying a voice descriptor, then the line in double quotes: `[Detective, raspy deep voice]: "Don't move."` A speech verb outside the bracket is optional and the owner uses both forms.
- GIVE EVERY SPEAKER A UNIQUE, CONSISTENT LABEL, and reuse that exact string at every mention. Pronouns and synonyms break it: the owner's named failure is `[Agent] says... Then, he says...`.
- GIVE EVERY SPEAKER A DISTINCT VOICE DESCRIPTOR. `[Man] says... [Woman] says...` is called out by name: "The voice characteristics are too vague and can confuse the model."
- ANCHOR THE LINE TO AN ACTION FIRST. Describe what the speaker does, then give the line, or "the model won't know who slammed the table".
- SEPARATE TURNS WITH AN EXPLICIT TEMPORAL CONNECTIVE. This is the highest-value rule in the whole Kling corpus and the failure is loud: run two turns together and "the model may generate a continuous speech from one character". Use "Immediately,", "Then,", "After a brief pause,", or the literal marker "this is when the speaker switches". The owner's house idiom silences the other party explicitly: `During this, [X] remains silent.`
- Put the emotion, pace, accent and language in the label alongside the voice. `[Female tourist, slightly slow, clumsy accent, in Spanish]`.
- Write each spoken line in the target language's own script. An out-of-set language does NOT error; it is silently translated to English and voiced in English. The 3.0 series speaks five languages, `kling-v2-6` speaks two.
- When English is spoken, lowercase the words; reserve uppercase for acronyms and proper nouns.
- Speech and singing need the longer duration tier to land whole; short clips truncate or destabilize the audio.

</rules>

<example use_case="multi-character-dialogue">

```text
Visual: A dimly lit casino VIP room, a green-felt poker table at the center, warm wall lamps casting silhouetted glows through drifting smoke. Dialog: [Man in suit, leaning forward on his elbows, deep male voice]: "Three rounds to decide. Win, and the chips are yours." During this, [Woman with curly hair] remains silent. Immediately, [Woman with curly hair, fingers tracing the table edge, cool glamorous female voice]: "I don't care about the chips." Background: low room tone and the click of chips.
```

*Why: unique non-pronominal labels reused verbatim, a distinct voice descriptor each, the action packed in before each line, and the turn boundary marked twice over by the silence clause and "Immediately," so the two voices do not merge into one*

</example>

### Sound effects, ambience and music

<rules id="sound">

- Weld a sound effect to the action that makes it, in the same clause, parenthetically: `extends her energy wings (with a loud alarm sound)`, `gently sweeps a brush across the cover (with a subtle brushing sound)`.
- Ambience gets a scene, its sound elements, and a spatial quality: rain, insects, crowd murmur, traffic; echo in an open hall, small room acoustics. The reverb slot is real and most families have no equivalent.
- Music takes instrumentation, genre and emotion: "Piano performance + jazz + melancholy". BGM is live owner vocabulary, written as `Background: soft beauty BGM playing.`
- Lyrics and rap bars go in double quotes exactly like dialogue, with a style and an accompaniment description. Rap bars are expected to carry real rhyme and meter.
- Quotation marks mark SOUND CONTENT generally, not only speech. Onomatopoeia takes them too: `producing a "shh-shh" sound`.
- The soft labels `Visual:`, `Dialog:`, `Background:` and `Sound Effects:` are an available structuring device, used in roughly half the owner's examples and required by none.
- ONE CORE AUDIO THEME PER GENERATION. Stacking several ambiences plus complex speech is a stated cause of unstable output.

</rules>

### Voice binding

<rules id="voice">

- On the 3.0 series a voice is bound to an ELEMENT out of band, and once bound you should NOT name the tone again: "it's not recommended to set the tone again in the prompt". This is the only do-not-restate rule the owner states anywhere.
- On `kling-v2-6` the binding is INLINE in the prompt instead, attached immediately after the character name. Two different grammars for the same idea; check your model.
- Never bind a voice to something that cannot speak. Binding one to a visual action, a prop, a siren, or a character who has no line is a stated error class.
- Never bind two speakers to the same voice, and never let a voice descriptor contradict the character you can see. `[A tall man, sharp high-pitched female child voice]` is a stated failure.
- Delivery and manner are always yours to write, bound voice or not: "says with a barely contained smile" is performance, not timbre.

</rules>

## Conditioning inputs and the referent grammar

ONE ROLE PER INPUT. Kling gives this a literal syntax: a token, written inline in the prompt, that binds to the id the caller assigned an input.

<rules id="referents">

- The token IS the id. An input given the id `element_1` is referred to as `<<<element_1>>>` in the prompt text; the same holds for `image_1`, `video_1`, `voice_1`. It is not positional and not automatic.
- THE TOKEN IS OPTIONAL, and the owner's own example prompts mostly omit it. Use it only to DISAMBIGUATE, when more than one input could fill a role and you must weld a specific element to a specific slot. With one image and one obvious job, plain English is what the owner writes: "Change the color of the parrot's feathers to match the reference image."
- A token stands in for the object itself and takes any sentence slot, including possessives. Keep the sentence around it ordinary: "Simpler grammar is better."
- The owner's web app spells the same mechanism `@Name`, keyed on an element's name rather than an id, because the UI has names where the API has ids. Same idea, different surface.
- An element owns APPEARANCE and, if one is bound, VOICE. Name it and spend your words on what it DOES.
- A reference video used as a property donor needs the borrowed property NAMED, so it reads as a donor and not as a base to edit: "following the camera movement of the video", "with the same motion as the character in the video".

</rules>

## By mode

### Text-to-video

<rules id="t2v">

- The prompt is the only source of truth, so detail is the only lever. Cover the slots. Unlike image-to-video, text-to-video "necessitates scene description": nothing supplies the scene but you.
- Pure description. No imperative, no referents, nothing to point at.
- Use simple words and simple sentence structures. The owner asks for this on both prompt-teaching surfaces; detail means more specifics, not more elaborate language.
- Keep the visual content simple enough to complete in the shot. A scene that needs a minute of screen time will be rushed into ten seconds.
- COUNTS ARE UNRELIABLE. Stated outright: the models are "not sensitive to numbers, making it difficult to maintain consistency in counts, such as '10 puppies on the beach'". Do not specify quantities you need honored; describe "a litter of puppies" instead.
- Complex physics is still hard: a bouncing ball, the trajectory of a high-altitude throw. Choose motion the model can carry.
- Split screen has a documented in-prompt form: name the panel count and what each panel holds, as in "4 camera angles, representing spring, summer, autumn, and winter".
- Cultural register responds to explicit naming: words like "Oriental mood", "China" and "Asia" are called out by the owner as reliably steering both style and casting.

</rules>

<example use_case="t2v-flagship">

```text
American cartoon style animation. On a sunny summer afternoon, wildflowers bloom across a wide green hillside under a blue sky with floating clouds. Two boys aged eight to ten, in casual T-shirts, shorts and baseball caps, chase butterflies across the hill. A wide-angle shot first shows them running over the rolling grass, then a low-angle close-up captures their determined, exaggerated expressions as they swing their nets. One boy jumps to catch a butterfly while the other points excitedly. A car appears on the road in the background; the camera follows it approaching and the boys stop, holding their nets, watching curiously. The car stops nearby, kicking up light dust, the boys still in a curious stance. Bright and colorful lighting, full of summer adventure joy.
```

*Why: the owner's own flagship. Style first, then scene, then subject, then a sequenced beat list with the shot changes written in prose, closing on lighting and mood. Nothing points at an input because there is no input*

</example>

### Image-to-video

<rules id="i2v">

- The image supplies the scene, so the prompt does not have to. Stated: "In contrast to Text-to-Video, which necessitates scene description, Image-to-Video is already provided with a scene. Thus, it only requires the depiction of the subjects in the image and the intended movement for these subjects."
- The image-to-video formula is its own: SUBJECT + MOVEMENT, then optionally BACKGROUND + MOVEMENT. Subject and movement are the two load-bearing halves; drop either and it fails.
- NAME THE SUBJECT. Never send a bare instruction. This is Kling's sharpest documented failure and it explains why photographs so often produce static video: handed "Put on sunglasses" over a painting, the model decides it is looking at a painting and pans across it like an exhibit rather than animating anyone. Naming the subject gives the motion something to attach to.
- Several subjects: list them in sequence, each with its own movement.
- Keep the movement physically plausible AND likely for that specific image. A description that deviates far from the image buys you a camera cut or a transition instead of the motion you asked for.
- Use simple words and simple sentence structures. This is the one place in Kling where the owner asks for less language rather than more.
- The rule above is stated on an older surface, and the 3.0-era examples do not follow it consistently: one flagship 3.0 image-to-video prompt re-describes an entire street scene down to a grey hoodie and the clerk's white hair. Re-describing is not punished. Treat subject-plus-movement as the floor that always works, not as a ceiling.
- Audio is still generated from nothing here, so the sound layer is as much your job as in text-to-video.

</rules>

<example use_case="i2v-name-the-subject">

```text
Mona Lisa puts on sunglasses with her hand, and a ray of light appears in the background
```

*Why: the owner's own before-and-after. "Put on sunglasses" alone fails, because with no subject named the model reads the painting as an object and pans across it. Naming the subject welds the movement to something in the frame, and the second clause adds background motion in the same subject-plus-movement shape. No scene description, because the image already is the scene*

</example>

### First and last frame

<rules id="keyframe">

- Supply both frames and describe the CHANGE between them, not the contents of either.
- An end frame requires a start frame; an end frame alone is not supported.

</rules>

### Reference and elements

<rules id="reference">

- Elements lock a character, prop or scene across camera moves and cuts. Name the element, then describe what it does.
- Reference workflows are "most useful when the prompt keeps the character, product, or prop description steady while the scene, camera angle, or action changes". NAME WHAT MOVES, PIN WHAT STAYS.
- If a reference image and your text disagree, you have given the model conflicting information. The owner's fix is to align them, not to arbitrate: do not describe outdoor camping over an indoor reference photo.

</rules>

### Editing a video

Omni line only (`kling-v3-omni` and `kling-video-o1`). THIS IS WHERE THE PROMPT MODE FLIPS.

<rules id="edit">

- With a video input, the prompt is an INSTRUCTION, not a description. Write the imperative verb first: Add, Remove, Change, Generate. The owner's framing is "post-production is as simple as having a conversation" and "Your prompts become the most efficient editing tool".
- Name the TARGET and the CHANGE, and scope the target in prose: "Change the man in the grey coat to a woman in a red coat."
- Weld a borrowed attribute to its donor with a prepositional tail: `from the image`, `with the image`, `to the style of the image`. This is ONE ROLE PER INPUT as sentence grammar.
- ADD AN EXPLICIT PRESERVATION CLAUSE. The owner's own API example does: "Keep all other elements of the video unchanged." Its UI templates mostly rely on implicit preservation and never promise that unnamed content holds still, so the clause costs a few words and buys a guarantee the docs decline to make.
- Task composition works: one prompt can add a subject AND change the background, or restyle AND use an element. The owner asserts this but never demonstrates the composed syntax, so keep composed edits short and ordered.
- Do not describe the finished video here. A caption is not an edit.

</rules>

<example use_case="edit-with-preservation">

```text
Change the color of the parrot's feathers to match the reference image. Keep all other elements of the video unchanged.
```

*Why: the owner's own API example. Imperative first, target scoped, the borrowed attribute welded to its donor in plain English with no token needed because only one image is supplied, and an explicit preservation clause*

</example>

### Shot extension

Omni line only. Generate the shot before or after an existing one.

<rules id="extend">

- Prefix with the direction, then DESCRIBE the new shot in full: "Based on the video, generate the next shot: ..." or "... generate the previous shot: ...".
- This is the one hybrid: the prefix is an instruction, everything after the colon is a description. Give the new shot its own camera, blocking, lighting and grade.
- Multi-shot on the Omni line can also be built by CHAINING: feed each output back as the next input. Consistency across the chain comes from elements, not from the prompt.

</rules>

<example use_case="extend-next-shot">

```text
Based on the video, generate the next shot: from the back seat, show a medium shot of a middle-aged man and a young man in front. They angle slightly apart, forming a tense, restrained opposition as they turn to look out their windows. The background is blurred, and soft natural light creates muted olive-green and brown tones with light film grain.
```

*Why: the owner's own example. An imperative prefix names the direction, then the new shot is described as fully as a fresh generation would be, down to the grade and the grain*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Kling publishes NO negative-prompt guidance on any surface. There is no technique here to teach, and the owner's silence is total rather than implied.
- Where a host exposes a negative field, the owner's own recommendation is to skip it: supplement the negative "via negative sentences within positive prompts".
- The demonstrated house style is to state the desired positive condition instead: "one continuous long take without any cuts" rather than a list of forbidden tokens.
- Unwanted output is fixed by ADDING specificity or REMOVING competing actions, not by exclusion. "Simplify the scene before adding style."

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Reading the version numbers as a ranking: O1 is 3.0 Omni's predecessor, not a model older than 2.5. Two parallel lines.
- Describing the finished video when a video is an input: with a video in, the prompt instructs. Write the imperative.
- Instructing when there is no video: with no video in, the prompt describes. A bare command has nothing to act on.
- Writing dialogue for `kling-v2-5-turbo`, or any sound at all: no audio layer exists there. It is silently ignored.
- Writing shot syntax for anything outside the 3.0 series: single-shot models read it as words.
- Two dialogue turns with no connective between them: the model merges them into one speaker. Add "Immediately," or silence the other party explicitly.
- Pronouns for a speaker after the label: "[Agent] says... Then, he says..." breaks the binding. Reuse the exact label.
- Vague speaker labels: `[Man]` and `[Woman]` are too thin to voice apart. Give each a distinct descriptor.
- Restating a bound voice tone on the 3.0 series: it is already bound to the element, and the owner says not to.
- Stacking camera moves: "Push in, pan left, tilt up, rotate, zoom, and follow the subject" destabilizes. One main move.
- Contradicting yourself: "Static camera with fast push-in and orbit movement" gives mixed signals. Choose one.
- Vague camera direction: "Make it cinematic" and "cinematic camera movement" are named anti-patterns. Name the move and its destination.
- A bare motion verb: "A man running." Add posture, speed, surface contact and the camera relationship.
- A bare instruction in image-to-video: "Put on sunglasses" names no subject, so the model films the image instead of animating it. This is why photographs generate static video. Name the subject and weld the movement to it.
- An image-to-video movement that the image cannot plausibly support: you get a camera cut or a transition, not the motion. Keep the action likely for that frame.
- Shot durations that do not sum to the total: this is arithmetic, not a suggestion.
- Specifying a count you need honored: "10 puppies on the beach" will not give you ten. The models are stated to be insensitive to numbers. Describe the group, not the arithmetic.
- Stacking audio: several ambiences plus complex speech in one prompt is a stated cause of instability. One core audio theme.
- Speech in an unsupported language: it does not error, it comes out English. Check the language set for your model.
- Quality-booster tails: the owner's own examples end with "8K detail, masterpiece cinematography" and "High consistency, cinematic lighting, 4K". This is example residue, never endorsed in prose, and it buys nothing. Spend the words on the shot.

</rules>

## Sources

Trust order is official > provider > community; official wins on any conflict. Kling's own surfaces disagree with each other more than they disagree with anyone else, so where the API reference and a web-app guide or blog differ, this guide follows the API reference, because prompts written from here are sent through providers and proxies that wrap the API rather than the web app. The adjudications are recorded in `sources/kling/kling-notation-resolution.md`.

- Official (Kuaishou / Kling AI): the [video capability map](https://kling.ai/document-api/guides/capability-map/video), the [text-to-video](https://kling.ai/document-api/apiReference/model/textToVideo), [image-to-video](https://kling.ai/document-api/apiReference/model/imageToVideo) and [O1](https://kling.ai/document-api/api/video/o1) API references, the [API changelog](https://kling.ai/document-api/updates/api), the [VIDEO 3.0](https://kling.ai/quickstart/klingai-video-3-model-user-guide), [VIDEO 3.0 Omni](https://kling.ai/quickstart/klingai-video-3-omni-model-user-guide), [VIDEO O1](https://kling.ai/quickstart/klingai-video-o1-user-guide) and [VIDEO 2.6 audio](https://kling.ai/quickstart/klingai-video-26-audio-user-guide) user guides, and the [prompt](https://kling.ai/blog/kling-ai-prompt-guide), [camera control](https://kling.ai/blog/kling-ai-camera-control-video-guide), [motion](https://kling.ai/blog/kling-ai-motion-prompts-guide) and [subject binding](https://kling.ai/blog/kling-3-subject-binding-character-consistency) blog guides, plus the unlinked prompt-teaching quickstarts for [text-to-video](https://kling.ai/quickstart/text-to-video-prompt-guide) and [image-to-video](https://kling.ai/quickstart/image-to-video-guide).

Last verified: 2026-07-16.

Coverage notes. Kling states NO prompt-length guidance on any surface; the word range in the frontmatter is measured from the owner's own examples, not stated by it, and the length-scales-with-duration rule from other families is absent here and has not been assumed. The image-to-video rule IS stated, but only on the dedicated image-to-video quickstart, which none of the model guides or prompt blogs links or repeats; the 3.0-era examples do not follow it consistently, so it is given as a floor rather than a prohibition. Kling states NO negative-prompt technique. The formula appears in six framings across six surfaces, so the slots are taught and the ordering is not; the text-to-video prompt guide's version is treated as canonical because it is the only surface whose whole purpose is the formula. The four prompt-teaching quickstarts that carry the formulas, the image-to-video rule and the count and split-screen guidance all date from a single batch that predates the 3.0 series; their structural rules are corroborated by newer surfaces and their capability claims are not relied on here. Multi-shot appears in seven notations across owner surfaces; the API's semicolon form is taught and the web-app forms are noted as demonstrations, because nothing states they parse identically through an API. The video-effects template library, the Avatar, Lip Sync and text-to-audio layers, and the legacy camera-control, motion-brush and video-extension features are out of scope here: the first is a set of preset ids, the second is a separate modality, and the third no longer exists on the current API.
