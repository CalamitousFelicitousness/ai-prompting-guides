---
guide: "Kling 4.0"
prompt_scheme: "kling-video-4"
models:
  - { id: "kling-4.0", access: "closed-weights", tier: "flagship", caps: [text-to-video, image-to-video, first-last-frame, multi-keyframe, multi-shot, native-audio, dialogue, elements, reference-image, reference-video, voice-reference, video-edit, text-rendering], best_for: "one model for every Kling 4.0 job: long narrative takes from a one-line idea or a full shot plan, keyframed sequences, mixed image, video and voice references, and editing an existing video. Its prompt grammar is not the 3.0 grammar" }
capabilities: [text-to-video, image-to-video, first-last-frame, multi-keyframe, multi-shot, native-audio, dialogue, elements, reference-image, reference-video, voice-reference, video-edit, text-rendering]
prompt:
  languages: ["en", "zh"]
  speech_languages: "nine named: Chinese, English, Japanese, Korean, Spanish, Portuguese, German, French, Hindi. Named Chinese dialects and accents: Sichuanese, Cantonese, Beijing, Northeastern, Taiwanese Mandarin. Named English accents: American, British, Indian. One owner table writes Indonesian where every other surface writes Hindi. What happens to a language outside the set is not documented for 4.0"
  formula: "four blocks: Asset Roles, Overall Settings, Sequence of Events (time-ranged beats), Audio. A blog gives the slot list Subject + Action + Setting + Camera + Lighting + Pacing + Sound. Same content; teach the blocks"
  length_strategy: "both ends work. A one-line prompt is expanded by the model; a clear, detailed prompt is followed as written. The owner's advice: start with one sentence covering subject, scene, action and emotion, then add only the details that change the result, such as camera work, timing, audio and preservation. The owner's showcase prompts run from one line to well over a thousand words"
  multi_shot: "on by default; the model splits shots by itself. Steer it in prose: declare the shot regime ('Six shots with hard cuts', 'One uninterrupted 15-second shot. No cuts') and give time-ranged beats. The 3.0 'shot n, m, words;' form is not documented for 4.0"
  dialogue: "prose attribution, not bracket labels: who speaks, in which language, with what delivery, then the line in double quotes in that language's own script. Turns are kept apart by timing and an explicit one-speaker-at-a-time rule"
  auto_expand_behavior: "YES, model-side and owner-stated. A short prompt is expanded with storyline, scene blocking and camera movement; a sufficiently clear prompt is followed faithfully. No switch is documented"
  negatives: "minimize them. The owner names two exclusions as necessary because the model adds both by default: no subtitles and no background music. Scoped exclusions on references and styles are also asked for. Otherwise state the wanted condition positively"
  structured_json: "none. Natural language, with soft section labels as an optional structuring device"
  references: "@ plus the input's id, with the input's ROLE stated in the same sentence. The id comes from the host: caller-assigned on the owner API (@image_1), positional on FAL and in the owner's web app (@Image1)"
sources:
  official: ["https://kling.ai/quickstart/kling-4-model-user-guide", "https://kling.ai/document-api/api/video/4-0/text-to-video", "https://kling.ai/document-api/api/video/4-0/image-to-video", "https://kling.ai/document-api/api/video/4-0/video-omni", "https://kling.ai/document-api/guides/capability-map/video", "https://kling.ai/document-api/updates/api", "https://kling.ai/dev/model-release/kling-4", "https://kling.ai/blog/kling40-kling-visual-realism-creative-control-introducing-storytelling", "https://kling.ai/blog/kling-4-ai-video-model", "https://kling.ai/blog/kling-4-multiple-keyframes-guide", "https://kling.ai/blog/kling-4-vs-3"]
  provider: ["https://fal.ai/models/kling/v4/text-to-video", "https://fal.ai/models/kling/v4/image-to-video", "https://fal.ai/models/kling/v4/reference-to-video"]
last_verified: "2026-10-25"
---

# Kling 4.0: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- This guide is Kling 4.0 only. Kling 3.0, 3.0 Omni, 3.0 Turbo, O1, 2.6 and 2.5 Turbo are covered by the separate Kling Video guide and use a DIFFERENT grammar. Do not carry it across: no `<<<image_1>>>` tokens, no `shot n, m, words;` shot lists, no `[Speaker, voice]:` dialogue labels.
- This guide is VIDEO only. Kling's image models are a separate scheme.
- Write natural language. There is no JSON prompt form. Soft section labels ("Audio:", "CAMERA:") are an optional structuring device, not syntax.
- Kling 4.0 is ONE model reached through several modes: text only, keyframes, mixed references, and editing. The grammar is the same in all of them; what changes is which inputs are present and how the prompt names them.
- THE PROMPT MODE FLIPS ON THE WORD "Edit". To change an existing video, open with "Edit @Video1" and instruct. Without it the prompt describes a new video, and "Reference @Video1" is read as borrowing from the video, not editing it.

</rules>

## TL;DR

<template id="quickstart">

{@id} defines {role}; preserve its {properties}. (one line per input; omit when there are none)
Scene and texture: {...}; visual style: {...}; camera tone: {...}.
0-{X}s: {visuals + action + emotion}. {X}-{Y}s: {camera movement + detail}. {Y}s-end: {closing shot}.
Audio: {speaker} says in {language}, {delivery}: "{line}". {ambience}. {sound effects}. {music, or "No background music."} {"No subtitles." unless you want them}

</template>

## Models and when to use which

- `kling-4.0` is the one API model. It covers text-to-video, image-to-video with any number of keyframes, generation from mixed image, video, element and voice references, and editing. Unlike 3.0 there is no separate Omni model: in 4.0 "Omni" names a mode of the same model.
- Kling 4.0 Flash is a faster mode on the owner's web app, "ideal for rapid creative iteration and short-form video creation". The owner states it "does not currently support start-and-last frames or multiple keyframes", and publishes no API id for it. The prompt grammar is the same; drop keyframe instructions when writing for it.
- The owner's own steer between generations: "Kling 3.0 remains useful for shorter generations, prompt-led scenes, Multi-Shot content, native audio". If you choose 3.0, switch to the Kling Video guide; prompts do not transfer in either direction.

## How the model reads prompts

- SHORT PROMPTS ARE EXPANDED, CLEAR PROMPTS ARE FOLLOWED. Stated: "the model will automatically expand simple prompts by filling in the storyline, scene blocking, and camera movements. When the description is already sufficiently clear, the model follows it faithfully without adding its own interpretation." Use a one-liner to explore an idea and a full plan to control one. No switch for the expansion is documented.
- AN INPUT WITHOUT A ROLE IS GUESSED AT. "If you provide only asset IDs without specifying their roles, the model will infer their intended use, making the results less predictable." Every referenced input gets a job in the same sentence.
- CONCRETE BEATS ABSTRACT. "Describe visual details as explicitly as possible to reduce the need for the model to infer or guess." The owner's own replacements: "Premium look" becomes "Side backlighting outlines the object's edges, the background is blurred, and fine matte grain is visible on the surface"; "Vintage feel" becomes "Yellowed walls, worn furniture edges, and warm incandescent lighting".
- DURATION AND ASPECT RATIO WRITTEN IN THE PROMPT ARE READ. Where the host leaves them unset, "the model detects and follows the duration intent in the Prompt, for example, "Generate a 15-second video."" The owner documents the same for aspect ratio in the reference mode ("Generate a 9:16 vertical video."). A value the host sets wins over the text.
- SHOTS AND SOUND ARE ALWAYS ON. "Audio-visual synchronization and Smart Storyboard are enabled by default and have no separate toggles." A prompt with no sound written into it still gets sound, and a prompt with no shot plan still gets cut into shots where the model sees fit.
- THE MODEL ADDS SUBTITLES AND BACKGROUND MUSIC BY DEFAULT. Exclude them when you do not want them; these are the two negatives the owner calls necessary.
- Write the prompt in English or Chinese. Write each spoken line in the language it should be heard in.
- TERM TRAP: the owner's 4.0 user guide often uses "element" to mean the SUBJECT of a shot ("Describe the element and what you want to happen"), not a saved library Element. Read which is meant before copying a sentence.

## Prompt structure

<rules id="structure">

- The owner's template has four blocks in this order: ASSET ROLES, OVERALL SETTINGS, SEQUENCE OF EVENTS, AUDIO. Skip Asset Roles when there are no inputs; keep the other three.
- Start small and add what changes the result: "Start with one sentence that clearly describes the element, scene, action, and emotion. Then add only the details that meaningfully affect the result, such as camera work, timing, audio, and preservation requirements. This is more effective than piling on adjectives."
- PACING is a slot of its own in 4.0. The owner's slot list is "Subject + Action + Setting + Camera + Lighting + Pacing + Sound".
- Put the time into the Sequence of Events as ranges: "0-X s" for visuals, action and emotion, "X-Y s" for camera movement and further detail, "Y s-end" for the closing shot.
- State the duration in the prompt when it matters ("15 seconds", "A continuous 7-second shot"), and the aspect ratio when the host does not set it.
- Replace every abstract quality word with what the camera would see: lighting, materials, composition.

</rules>

<template id="general">

[Asset Roles]
@Image1 defines {role}; preserve its {properties}.
@Image2 defines {role}; preserve its {properties}. Reference the {property} of @Video1.
[Overall Settings]
Scene and texture: {...}; visual style: {...}; camera tone: {...}.
[Sequence of Events]
0-{X}s: {visuals + action + emotion}
{X}-{Y}s: {camera movement + additional details}
{Y}s-end: {closing shot}
[Audio]
{dialogue or voiceover} + {ambient sounds} + {music} + {sound effects}

</template>

<example use_case="role-assignment-minimal">

```text
@Image1 defines the scene. Preserve its spatial layout, furnishings, and lighting.

@Image2 defines the female protagonist. Preserve her facial features, hairstyle, and clothing.

The female protagonist walks toward the window, stops, and looks back.
```

*Why: the owner's own minimal example. One sentence gives each input its job and names what to preserve, then a plain action line. Nothing is left for the model to guess*

</example>

<example use_case="t2v-short-direction">

```text
A continuous 7-second shot set in the UK. Two friends who have not seen each other for a long time meet at the corner of a quiet street at dusk, surrounded by a diverse crowd going about their daily lives. They smile, walk quickly toward each other, and share a warm embrace. Their facial expressions and body movements are natural. A handheld camera follows them with subtle camera shake. Soft, warm lighting with a nostalgic cinematic film look. Include natural footsteps, street ambience, background music, and English dialogue.
```

*Why: the owner's own text-to-video example. Duration and shot regime first, then scene, action, camera, light and sound in one paragraph. "English dialogue" with no lines written hands the words to the model, which is the expansion behavior at work*

</example>

<example use_case="four-block-flagship">

```text
[Asset Roles]
@Image1 defines the lighthouse keeper; preserve her face, grey braid, oilskin coat and knitted gloves.
@Image2 defines the lantern room; preserve its brass lamp housing, curved glass panes and iron railing.
[Overall Settings]
15 seconds, one hard cut at 13 seconds. Scene and texture: salt-crusted glass, wet iron, a thin haze of lamp-oil smoke; visual style: realistic, muted blue-grey palette with warm lamp light; camera tone: steady and close.
[Sequence of Events]
0-4s: Storm at dusk. Wide shot from outside the glass, rain streaking the panes as the keeper climbs the last steps into the lantern room, breathing hard, determined.
4-9s: The camera slowly pushes in as she strikes a match and lifts it to the wick. Her hands shake from the cold, then steady.
9-13s: The lamp catches. Close-up of her face lit gold from below, relief breaking into a tired smile.
13s-end: Hard cut to an extreme wide shot from the sea. The beam sweeps across black water toward a small fishing boat.
[Audio]
She whispers in English, low and hoarse: "Come on, come on." Wind against the glass and rain on iron. The match scrapes and the wick catches with a soft "whump". No music for the first 9 seconds, then a low cello note swells as the beam sweeps. No subtitles.
```

*Why: built to the owner's four-block template. Each input has one job with its preserved traits, the duration and cut point are stated once, every beat carries visuals, action and emotion, the camera gets one move per beat, and the audio block names all four layers plus the subtitle exclusion*

</example>

## References and the @ grammar

ONE ROLE PER INPUT. In 4.0 that is the stated rule, not just good practice: "Specify the purpose and scope of each reference."

<rules id="references">

- The token is `@` followed by the input's id, written with no space: `@image_1`, `@Video1`. The owner's examples sometimes drift to "@Video 1"; do not copy the space.
- THE ID COMES FROM THE HOST. On the owner's API you assign each input an id and write it after the `@` ("set "id": "image_1" on a refer_image object, then reference it as @image_1"). FAL and the owner's web app number inputs for you by type and order: `@Image1`, `@Video1`, `@Element1`. The examples in this guide keep the owner's `@Image1` numbering; where you assign ids, either assign matching ones or rewrite the tokens.
- GIVE EVERY INPUT ITS ROLE IN THE SAME SENTENCE: "@Image1: preserve the character's appearance", "@Video1: reference the action pacing". A bare token is the documented way to get an unpredictable result.
- SCOPE THE ROLE AND EXCLUDE WHAT MUST NOT CARRY OVER. "When multiple assets provide different types of information, specify the scope of each asset's role and explicitly exclude elements that should not be carried over." The owner's API example: "Follow the movement rhythm in @video_1 without using its background."
- Match the role to the input type. The owner's list: character reference for "Face, clothing, identity"; product reference for "Shape, color, logo"; scene reference for "Layout and atmosphere"; style reference for "Lighting, color, visual treatment"; video reference for "Motion, camera movement, pacing".
- Images can be more than likenesses: three-view sheets, image grids, infographics, wireframes, composition plates and storyboards all work as references. A video can be a depth-map or untextured "white-model" render that carries only motion and space.
- A storyboard reference must be told not to appear: "Do not render the storyboard itself." The owner adds the sketch artefacts to keep out.
- NAME WHAT MOVES, PIN WHAT STAYS. References say what stays consistent; the prompt says what happens. "Rather than using one prompt to describe everything, creators can give each reference a specific role across identity, movement, camera direction, pacing, and visual style."
- With many inputs, "prioritize those that have the greatest impact on the visuals and pacing", and "verify that each @ reference points to the correct asset".
- A reference and a keyframe that disagree about something meant to persist (an outfit, a logo) force the model to choose. "When something is supposed to remain consistent, use the same reference logic throughout the sequence."

</rules>

<example use_case="multi-reference-six-images">

```text
Reference the facial features of the characters in @Image1, @Image2, and @Image3, keeping them strictly consistent. Reference the design of the blue motorcycle in @Image4 and keep it strictly consistent. Reference the design of the red sports car in @Image5 and keep it strictly consistent. Reference the filming equipment in @Image6 and keep it strictly consistent.
```

*Why: the owner's own six-input example. Every token is welded to exactly one property (faces, motorcycle design, car design, equipment) and every one carries the same pin, "keep it strictly consistent"*

</example>

<example use_case="motion-donor-plus-characters">

```text
Reference the fighting movements and attack rhythm from @video_1, and use @image_1 and @image_2 for the character designs.
```

*Why: the owner's API example, with caller-assigned ids. The video donates motion and rhythm only, the two images donate appearance only, and the sentence says so, so the video's people and setting are not copied*

</example>

<example use_case="camera-donor-with-replacement">

```text
Reference the camera path and pacing of @Video1. Replace the element with the car in @Image1 and the background with @Image2.
```

*Why: the owner's camera-reference example, which also shows creative recreation: borrow the path and pacing, swap the subject and the background. "Element" here means the video's subject, not a library Element*

</example>

<example use_case="storyboard-reference">

```text
Reference the character design in @Image1 and use the storyboard in @Image2 as the director-approved sequence of shots, framing, camera paths, screen direction, and emotional progression for this scene. Recreate the finished stop-motion-style frames described in each storyboard panel. Do not render the storyboard itself. Avoid pencil-sketch textures, grids, title bars, Chinese annotations, and director's notes.
```

*Why: the owner's storyboard example. The storyboard is given its full job (order, framing, paths, emotion) and then explicitly kept out of the picture, with its sketch artefacts named, so the panels are filmed instead of reproduced*

</example>

## Sequence of events, shots and camera

<rules id="sequence">

- Write the video as a timeline. "For longer videos, it can help to write the prompt around the progression of the timeline." Each range carries what is seen, what happens and how it feels.
- Make the ranges end at the stated duration. The owner never states this as a rule, but every one of its timelines does it.
- DECLARE THE SHOT REGIME in words, because the model splits shots on its own otherwise. Either a count with its cuts ("Six shots with hard cuts", "Hard cuts at 3.0, 5.0, 8.0, 10.0, and 11.0 seconds") or one take ("The entire video must be one continuous master shot with no visible cuts").
- Name the transitions you want and ban the ones you do not. The owner's vocabulary: match cuts on a sound, an action or a movement; wipes motivated by something passing the lens ("Cuts are motivated by wing wipes, smoke wipes and close architectural passes"); occlusion transitions; "Gentle Fade to Black". And "No fades or dissolves" when cuts must stay hard.
- Give relative pacing in words: "The first four shots are brief and punchy. Let the final shot run slightly longer".
- Camera: push-ins, pull-outs, pans, tracking shots and orbits are the owner's named moves. Give each beat one move; a long take can chain moves in sequence ("first bobs alongside him..., then dives into the hole with him, tilts upward..., and finally rises to an extreme long shot").
- 4.0 is pitched at bigger motion than earlier Kling: "Instead of reducing movement to keep the shot stable, creators can push character movement and camera direction further". Plan ambitious action, but keep it in the timeline so each beat has one job.
- The owner's long examples pin counts with a header line, "SCENE CONTEXT EXACT 1 CHARACTER - NO DUPLICATES", and give camera direction in physical terms (lens length, distance, a percentage of push-in). Both are demonstrated rather than stated.

</rules>

<example use_case="timeline-product-story">

```text
0-5s: Establish a modern kitchen at sunrise. A woman enters the frame and walks toward the counter.
5-12s: She notices the product, picks it up, and examines it while the camera slowly moves closer.
12-20s: She begins using the product. Keep the movement natural and maintain the same character and product appearance.
20-27s: Shift to a closer angle as she reacts positively to the result.
27-30s: End on a clean product hero shot with soft lighting.
```

*Why: the owner's timeline example from the keyframes guide, with its bold labels and dashes made plain. One job per range, the camera written into the beat it belongs to, a continuity pin in the middle, and a closing shot that lands exactly on the total*

</example>

## Keyframes

Keyframes say WHEN something must be seen; references say WHAT stays consistent. "Keyframes show the important moments. The prompt explains how the video moves between them."

<rules id="keyframes">

- Four shapes, each with the owner's own phrasing:
- First frame: "Use @Image1 as the first frame, then describe what happens next."
- Last frame alone (new in 4.0): "Use @Image1 as the last frame, then describe what happens before it."
- First and last: "Use @Image1 as the first frame and @Image2 as the last frame, then describe the [process] in between." Best for transformations, craftsmanship and before-and-after.
- Middle frames: "Add a description to each keyframe, specifying what appears at that point and how the camera reaches that position", in the form `X-Y sec | Keyframe 1: [Describe what happens]`.
- Write each keyframe's time into the prompt. The owner's control table is all timestamps: "Raise a hand at 3 seconds, turn around at 7 seconds"; "Character B enters through the door at 6 seconds"; "The sky darkens at 5 seconds; it starts raining at 10 seconds".
- Add a keyframe only where something changes. Each one "should answer a simple question: What must the viewer see at this point in the video?" More keyframes do not mean more control.
- One change per keyframe. One that "changes the character, environment, product, camera angle, lighting, and visual style at the same time can create an unnecessarily difficult transition."
- Make the prompt's timeline match the keyframes. "Plan the timeline first, then make sure the prompt follows the same sequence."
- A keyframe can double as an identity reference: "Begin with the female model in @image_1, preserving her facial features, hairstyle, clothing, and accessories."
- Keyframes do not need to be new shots. They can mark a change inside one concept: a costume change, day into night, a product moving from box to use, a style shift.
- Flash takes no first-and-last pair and no middle frames.

</rules>

<example use_case="first-last-process">

```text
Use @Image1 as the first frame (a piece of raw iron) and @Image2 as the last frame (a finished knife). Generate a 15-second video showing the process of forging a knife, in a realistic documentary style.
```

*Why: the owner's first-and-last example. Each frame is named with what it shows, and the prompt spends its words on the process between them plus duration and style. The owner's original says "sword" for the generated object and "knife" for the last frame; it is aligned here so the prompt does not contradict its own end frame*

</example>

<example use_case="first-last-locked-camera">

```text
Use @Image1 as the first frame and @Image2 as the last frame. The entire video should be one continuous lateral tracking shot from the side, with no cuts, angle changes, or scene changes.
```

*Why: the owner's second first-and-last example. When the frames already carry the content, the prompt's job is the path between them: one camera move, and the shot regime fixed explicitly*

</example>

<example use_case="three-keyframes">

```text
A cinematic, photorealistic fashion video. Begin with the female model in @image_1, preserving her facial features, hairstyle, clothing, and accessories. She moves naturally and gracefully, transitioning smoothly into the pose and composition shown in @image_2. Continue the motion toward the final pose and scene shown in @image_3. Ensure seamless transitions between all three keyframes, with realistic body movements, natural facial expressions, consistent character identity, and coherent lighting. Smooth camera movement, premium fashion commercial aesthetic. Avoid abrupt cuts, distorted anatomy, and unnatural motion.
```

*Why: the owner's API example with a first, a middle and a last frame. The first frame also pins identity, each later frame is reached in order by token, and the prompt describes the motion between them. Its closing negative line is the owner's own; the owner's user guide would trim it to what the model actually tends to add*

</example>

## Audio and dialogue

Sound is always generated, in stereo. The prompt's Audio block chooses it: "Dialogue/voiceover + ambient sounds + music + sound effects". Audio inputs are voices only; "Background music and sound effects are generated by the model based on the visuals."

<rules id="dialogue">

- WRITE THE LINE IN ITS LANGUAGE, IN QUOTES. "To generate speech in a specific language, write the dialogue in that language inside quotation marks." Name the language in the attribution too: "speaks in natural, clear, slightly slow Spanish:".
- Attribute in prose, not with bracket labels: who speaks, in which language, with what delivery, then a colon and the quoted line.
- DESCRIBE THE VOICE when no voice is supplied: "describe the speaker's age, vocal tone, speaking speed, and emotion."
- Direct the delivery inside the line's sentence, including which words carry the weight: "Begin with warm appreciation, emphasize "love" and "confident," then finish with an audible smile."
- Tie the words to the performance: "describe the character's expression, movement, and tone to help connect the words with the performance."
- ONE SPEAKER AT A TIME, stated: "When one person is speaking, the others remain silent. No interruptions or overlapping dialogue." Time the hand-offs: "After she finishes speaking, pause for approximately 0.5 seconds." Give everyone "a distinct voice".
- With several languages, lock each speaker to theirs ("The Spanish tourist speaks only Spanish.") and guard the accent ("without English-accented pronunciation").
- Keep the speaker visible when the line must be lip-synced on screen: "The entire line must be delivered while the director is on screen."
- A SUPPLIED VOICE IS WELDED AT THE LINE. Where the voice is its own input with an id, put its token in the attribution: `says in English using @1: "Excuse me."`. Where a host attaches the voice to an element instead, the element speaks with it; write the delivery, not the timbre.
- Dialects and accents can be named: Sichuanese, Cantonese, a Beijing, Northeastern or Taiwanese Mandarin accent; American, British or Indian English.

</rules>

<rules id="sound">

- Name all four layers you care about. A layer you leave out is chosen for you.
- Set the mix in words: "Music ducks beneath every spoken line"; "Ambient sounds must not overpower the dialogue"; "Roar, wings and fire remain louder than the music."
- Keep the bed continuous across cuts when it should be: "The ambience never resets at the cuts."
- Time the music like any other event: "No music for the first 12 seconds. During the final three seconds, a cheerful tuba and ukulele duet plays."
- To have no music, say so; the model adds background music by default. The owner's long examples write it emphatically: "SFX only, no music, no score, no song, no soundtrack."
- Onomatopoeia goes in quotes: springy "boing-whoing" sounds, a rubbery "pop".
- Stereo is the output format, not a prompt technique. No panning phrasing is documented; spatial words ("closer", "more distant", "centred") appear in the owner's examples only.

</rules>

<example use_case="single-line-language">

```text
A Spanish female tourist looks at the interpreter in the middle and raises the map in her hand. She speaks in natural, clear, slightly slow Spanish: "¿Dónde está la estación de metro más cercana?"
```

*Why: the owner's language example. An action anchors the speaker, the attribution names language, clarity and pace, and the line is written in Spanish so it is spoken in Spanish*

</example>

<example use_case="voice-token-in-a-scene">

```text
Use @image_1 as the character reference. A girl sits by the window on a moving train, quietly gazing outside with a melancholic expression. After a few moments, the camera slowly pulls back, revealing more of the train carriage and other passengers. The girl stands up from her seat and carefully walks down the aisle. As she passes another passenger, she turns slightly and politely says in English using @1: "Excuse me." Natural body movements, realistic facial expressions, accurate lip synchronization, cinematic lighting, continuous camera movement.
```

*Why: the owner's API voice example. The image gets its role first, the scene runs in order with one camera move, and the supplied voice (id "1") is welded at the exact line it speaks, beside the language and the manner*

</example>

<example use_case="trilingual-three-speaker-dialogue">

```text
SCENE CONTEXT EXACT 3 UNIQUE HUMAN CHARACTERS ACROSS THE VIDEO: Three people are in a bright, clean, fictional city tourist information center. Maintain consistent color tones throughout. The tourist stands on the left, the interpreter stands in the middle, and the tourism staff member stands on the right. A city map and route diagram are placed on the information desk. Background text and map labels must be blurred and unreadable. No real brands, organization names, logos, or watermarks may appear.
ACTION TIMING:
0-3 seconds: Medium shot of all three people. The Spanish female tourist looks at the interpreter in the middle, raises the map in her hand, and speaks in natural, clear, slightly slow Spanish: "¿Dónde está la estación de metro más cercana?" After she finishes speaking, pause for approximately 0.5 seconds. The interpreter turns to the tourism staff member and translates into Chinese: "她想知道最近的地铁站在哪里。"
3-7 seconds: Cut to the interpreter and the tourism staff member. The tourism staff member looks at the map and answers in natural, clear Chinese: "沿这条路直走，步行大约五分钟就能到。" After the staff member finishes speaking, pause for approximately 0.5 seconds. The interpreter confirms understanding and turns toward the tourist.
7-11 seconds: The interpreter translates the staff member's answer into natural, clear, slightly slow Spanish: "La estación de metro está a unos cinco minutos a pie. Siga recto por esta calle." While speaking, the interpreter points to the route on the map, and the tourist studies it attentively.
11-15 seconds: Return to a medium shot of all three people. After understanding the directions, the Spanish tourist smiles, nods, and says in Spanish: "Muchas gracias." All three maintain a natural service interaction as the scene ends.
AUDIO:
- The Spanish tourist speaks only Spanish.
- The Chinese tourism staff member speaks only Chinese.
- The Chinese interpreter speaks Chinese first, then Spanish.
- Each person has a distinct voice.
- When one person is speaking, the others remain silent. No interruptions or overlapping dialogue.
- All dialogue must have clear vocals, with lip movements synchronized to the corresponding language.
- Spanish pronunciation must be natural and standard, without English-accented pronunciation.
- Speech should be slightly slow, with natural pauses between sentences.
- Retain subtle ambient sounds from a tourist information center. Do not add background music. Ambient sounds must not overpower the dialogue.
CAMERA: Begin with a medium shot of all three people to establish their relationships. When the tourist speaks, cut to a two-shot of the tourist and interpreter. When the interpreter relays the question, cut to the interpreter and staff member. During the staff member's response, include a close-up of the map route. When the interpreter translates into Spanish, return to a two-shot of the interpreter and tourist. End with a medium shot of all three people. Maintain consistent character positions, eyelines, and clothing throughout. Do not abruptly replace characters or change their spatial relationships.
STYLE: Realistic, natural, professional travel-service documentary style. Bright, clean lighting, natural facial expressions, and restrained movements. The scene should resemble an authentic interaction at an airport or city tourist information center.
```

*Why: the owner's flagship dialogue sample, with one parenthetical removed because it forbade the map close-up that its own CAMERA block asks for. Positions are pinned, every line is in its own language and script with a timed pause after it, the AUDIO block states the one-speaker rule and the per-speaker language locks, the music exclusion is explicit, and incidental text is blurred*

</example>

## Text and subtitles

<rules id="text">

- Subtitles can be written into the prompt. "For best results, specify the font size, alignment, display duration, and whether the subtitles should be synchronized with the dialogue."
- Give each subtitle its words in quotes and its time range.
- For exact on-screen text, spell it out in quotes or backticks, name the case, and pin it: "Fix a clear, stable, readable sign with the exact uppercase text `KLING AI OPEN 24 hours`" and "The text must remain correctly spelled, undistorted, and free of flickering throughout the video."
- Suppress text you did not ask for: "Background text and map labels must be blurred and unreadable."
- If you want no subtitles at all, say "No subtitles"; the model may add them by default.

</rules>

<example use_case="timed-burned-in-subtitles">

```text
Subtitles: Burn in English subtitles, bottom-center within the title-safe area, positioned 10% above the bottom edge of the frame. Use no more than one or two lines. Rounded cream-colored felt subtitle panels with bold, dark chocolate-brown text, high contrast, and stable positioning. Each subtitle appears and disappears in sync with the corresponding voiceover: 0.78-1.38 sec: "ONE." 1.98-3.84 sec: "ONE MEANS JUST ONE." 4.16-4.66 sec: "TWO." 4.86-6.82 sec: "TWO MEANS ONE AND ONE TOGETHER." 7.26-7.78 sec: "THREE." 8.04-10.16 sec: "THREE MEANS TWO AND ONE MORE." 10.32-10.80 sec: "FOUR." 11.06-13.08 sec: "FOUR MEANS THREE AND ONE MORE." 13.32-14.24 sec: "ONE, TWO, THREE, FOUR." 14.40-15.00 sec: "GREAT JOB!"
```

*Why: the owner's subtitle example. Placement, line count, panel style, contrast and sync are all specified, then every caption gets its exact words and its time range*

</example>

## Editing a video

With "Edit @Video1" the prompt stops describing and starts instructing.

<rules id="edit">

- OPEN WITH "Edit @Video1", THEN SAY WHAT CHANGES AND HOW. The owner's warning: "Simply writing "Reference @Video1" may be interpreted as reference-based generation instead of editing." Some of the owner's own short examples drop the prefix; keep it.
- ADD A PRESERVATION CLAUSE. "If other elements must remain unchanged, add "Keep everything else unchanged." ... Without specifying what to preserve, other visual elements may also change." Spell out the list when it matters: "including the background, other subjects, camera movement, lighting, composition, and video duration".
- Preserve the soundtrack explicitly if it must not change: "Keep the audio exactly identical to the original video. Do not add any new sounds."
- Editable: expressions, body movement, characters and objects, backgrounds, camera position, camera movement, style, weather, colors and materials, and spoken lines ("Replace the final line "..." with "..."").
- Replacing several people: take them in the order they appear and give each its own image token plus a description of the new look.
- Removing something: ask for the hole to be filled: "Seamlessly reconstruct the areas previously obscured by the person".
- Restyling part of a frame: say which part changes and that the rest stays as it was ("Only the Corgi should be transformed into a blocky style. The wooden porch, snowy ground ... must remain completely realistic").
- Creative recreation is the reference-mode cousin of editing: "Borrow its narrative pacing, shot composition, or presentation style, then replace the characters, products, and scenes with your own. Clearly specify what to borrow and what to replace in your prompt." It works best when the source clip and your content are close in pacing and shot structure.

</rules>

<example use_case="remove-with-fill">

```text
Edit @Video1 to remove the foreground person. Keep everything else unchanged, including the background, other subjects, camera movement, lighting, composition, and video duration. Seamlessly reconstruct the areas previously obscured by the person, ensuring natural, consistent details with no visible artifacts.
```

*Why: the owner's removal sample (its token spacing tidied). Edit prefix, one target, a spelled-out preservation list, and an instruction for what fills the space the person leaves*

</example>

<example use_case="add-element-and-replace-line">

```text
Edit @video_1. When the box is opened again at the end of the video, @element_1 is sleeping inside. Replace the final line "Ah, it's all old stuff." with "Why is there a pig here?"
```

*Why: the owner's API edit example. The edit names the moment the new element appears, places it by token, and swaps one spoken line by quoting old and new. Add a preservation clause when the rest of the video must hold still*

</example>

<example use_case="pure-style-transfer">

```text
Edit @Video1. Replace the video's style with the felt style of @Image1. Preserve the original composition, shots, and actions. Change only the style; do not alter the characters' clothing designs, motorcycle design, scene elements, or event sequence.
```

*Why: the owner's style-transfer example. The image donates style and nothing else, and the prompt lists what must survive the restyle, so the felt look does not redesign the costumes or the bike*

</example>

<example use_case="style-transfer-plus-weather-edit">

```text
Edit @Video1. Replace the video's style with the felt style of @Image1, and change the weather from bright sunshine to light, steady snowfall. Preserve the original composition, shots, character actions and timing. Do not alter the characters' clothing designs or the event sequence. Keep the audio exactly identical to the original video.
```

*Why: built from the owner's style-transfer example plus weather, which the owner lists as an editable target. Two changes in one instruction, each named once, then the preservation list and the soundtrack pin*

</example>

<example use_case="replace-three-people">

```text
Edit @Video1. Replace the three people who walk out of the convenience store one after another with the following characters: First character: use the identity, face, dark curly hair, white sun hat, white short-sleeved shirt with a black-and-white striped inner top, green apron, loose light gray jeans, and dark sneakers of the man in @Image1. Second character: use the identity, short light blonde hair, red sweatshirt, green apron, white knee-high socks, and red shoes of the woman in @Image2. Third character: use the identity, short light blonde hair, white chef hat, black-framed glasses, blue-green-and-black patterned knit outfit, green apron, white shoes, and the same off-white plush sheep held in his arms as the man in @Image3. The order in which the three characters appear, their movements from inside the store to the doorway, their pauses to pose, and their approach toward the camera and exit through the foreground should follow the actions and camera timing of @Video1: the first character slightly lifts the brim of his sun hat before approaching the camera; the second character naturally adjusts her apron and gives a slight wave at the doorway before approaching the camera; the third character holds the plush sheep, adjusts his glasses, then approaches the camera and slightly raises the plush sheep as he gets closer. Fix a clear, stable, readable sign with the exact uppercase text `KLING AI OPEN 24 hours` in the middle of the convenience store's right-side glass window. The text must remain correctly spelled, undistorted, and free of flickering throughout the video. Keep the sign fixed to the inside of the glass window without obstructing any characters. Keep everything else unchanged: preserve the green convenience store doorframe, doorway composition, interior shelves, fluorescent lights, glass reflections, daylight, camera position, walking direction, duration, pacing, and aspect ratio of @Video1. Do not add any characters, change the store structure or camera movement, or introduce subtitles, logos, watermarks, or extra text.
```

*Why: the owner's four-input edit. Each new person is welded to one image in order of appearance with the traits to take, the video keeps its motion and timing, a sign is added with exact text, and the preservation list closes the edit*

</example>

## Style

<rules id="style">

- Style covers more than a label: "Style control extends to materials, lighting, and the overall atmosphere of the scene."
- For animation, exclude photorealism: "When specifying an animation style, explicitly exclude photorealism to avoid inconsistent results that mix the two styles."
- "When specifying a style, combining positive descriptions with explicit exclusions produces more consistent results". This is one of the places the owner asks for a negative.
- Styles the owner names for 4.0: cinematic, retro DV, animation, pixel art, felt, clay, glitch art, fantasy, cyberpunk, vlog, realistic documentary.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- Minimize negatives. "Negative prompts can increase the likelihood of errors." Say what you want to see: the owner rewrites "Don't show the element's face while they're on the phone" as "The element is shown in profile while talking on the phone."
- TWO EXCLUSIONS ARE NECESSARY, per the owner, because the model adds both by default: "no subtitles and no background music". Write them whenever you do not want them.
- Scoped exclusions are positive tools, not noise: keep a reference's background out ("without using its background"), keep photorealism out of an animation, keep a storyboard's own drawing out of the frame.
- The owner's API takes exclusions inside the prompt text ("The prompt can include positive and negative descriptions"); there is no separate negative field to rely on.
- The owner's long showcase prompts end with constraint sections ("Negative Constraints:", or a list of failures that "equals a failed shot"). That style is demonstrated, not recommended; the stated guidance is the minimal one above.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Carrying 3.0 grammar into 4.0: `<<<image_1>>>` tokens, `shot n, m, words;` lists and `[Speaker, voice]:` labels belong to the older models. Use @ tokens, timelines and prose attribution.
- A bare token with no job: the model guesses its role. Say what each input defines and what to preserve.
- "Reference @Video1" when you mean to edit it: that borrows from the video instead. Write "Edit @Video1".
- An edit with no preservation clause: other things change too. Add "Keep everything else unchanged" and list what matters.
- Abstract quality words ("premium look", "cinematic feel", "premium fashion commercial aesthetic"): the owner's own FAQ says to replace them with lighting, materials and composition.
- A prompt full of "don't": rewrite as the wanted state, except for the two default additions.
- Unwanted subtitles or background music: the model adds them unless told not to.
- Keyframes everywhere: add one only where something must be seen at that moment.
- One keyframe that changes character, place, light and style at once: split the change.
- A prompt timeline that disagrees with the keyframes, or a reference and a keyframe that disagree on what should persist: plan the timeline once and keep every input to the same logic.
- Overlapping dialogue: state the one-speaker rule and time a pause after each line.
- A line written in one language and expected in another: write it in the language it should be spoken in, inside quotes.
- An animation style with no photorealism exclusion: the two styles mix.
- A storyboard reference with no "do not render the storyboard": the panels themselves can appear.
- A space inside a token ("@Video 1") or a token that points at the wrong input: write the id exactly and check each one.
- Reading "element" in the owner's sentences as a library Element when it means the shot's subject.
- Keyframe instructions for Flash: it takes no first-and-last pair and no middle frames.

</rules>

## Sources

Trust order is official > provider > community; official wins on any conflict. Where the API reference and the web-app user guide or a blog differ, this guide follows the API reference, because prompts written from here are sent through providers and proxies that wrap the API rather than the web app. The adjudications are recorded in `sources/kling/kling-notation-resolution.md`.

- Official (Kuaishou / Kling AI): the [Kling 4.0 user guide](https://kling.ai/quickstart/kling-4-model-user-guide), the [text-to-video](https://kling.ai/document-api/api/video/4-0/text-to-video), [image-to-video](https://kling.ai/document-api/api/video/4-0/image-to-video) and [omni video](https://kling.ai/document-api/api/video/4-0/video-omni) API references, the [video capability map](https://kling.ai/document-api/guides/capability-map/video), the [API changelog](https://kling.ai/document-api/updates/api), the [developer release note](https://kling.ai/dev/model-release/kling-4), and the [launch](https://kling.ai/blog/kling40-kling-visual-realism-creative-control-introducing-storytelling), [complete guide](https://kling.ai/blog/kling-4-ai-video-model), [multiple keyframes](https://kling.ai/blog/kling-4-multiple-keyframes-guide) and [4.0 versus 3.0](https://kling.ai/blog/kling-4-vs-3) blog posts.
- Provider: FAL's Kling 4.0 [text-to-video](https://fal.ai/models/kling/v4/text-to-video), [image-to-video](https://fal.ai/models/kling/v4/image-to-video) and [reference-to-video](https://fal.ai/models/kling/v4/reference-to-video) model pages, for its positional token naming.

Last verified: 2026-10-25.

Coverage notes. The 4.0 API reference was marked as a preview when this was written. The owner states the expansion behavior, the role rule, the edit prefix, the preservation clause, the minimal-negatives rule with its two necessary exclusions, the subtitle specification and the keyframe phrasings; these are taught as rules. The four-block template is the user guide's, and the API defers to that guide for prompt organization. The owner's long showcase prompts use a capitalised multi-section scaffold (scene context, active references, format mode, optics, action timing, audio, positive constraints) that no surface recommends; its idioms are cited where useful but it is not taught as a template. The 3.0 shot-list form, bracket speaker labels and do-not-restate voice rule do not appear on any 4.0 surface and are not carried over. Only one owner example shows a voice token, and the web-app guide shows none, so the voice rule rests on that API example. Speech languages are taken from the user guide and the launch post; one release-note table lists Indonesian in place of Hindi. Silent translation of out-of-set languages is documented for 3.0 and not for 4.0, so it is not asserted here. Video extension is announced as coming soon and has no prompt grammar yet. Flash's limits beyond its missing keyframe modes are host and plan facts and are left out.
