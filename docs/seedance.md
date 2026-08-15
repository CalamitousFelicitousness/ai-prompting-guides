---
guide: "Seedance (video)"
prompt_scheme: "seedance-v2"
models:
  - { id: "seedance-2.5",      access: "closed-weights", tier: "flagship",  caps: [text-to-video, image-to-video, reference-to-video, video-edit, video-extend, multi-shot, native-audio, structure-reference], best_for: "a complete story told in one pass, the heaviest multi-reference casts, structure references from untextured 3D, and timestamp-precise editing" }
  - { id: "seedance-2.0",      access: "closed-weights", tier: "std",       caps: [text-to-video, image-to-video, reference-to-video, video-edit, video-extend, multi-shot, native-audio], best_for: "cinematic renders with full director control of shots, camera, physics, and synchronized audio in one pass" }
  - { id: "seedance-2.0-fast", access: "closed-weights", tier: "distilled", caps: [text-to-video, image-to-video, reference-to-video, video-edit, video-extend, multi-shot, native-audio], best_for: "rapid iteration and high-volume work; less responsive to fine director controls (slow motion, multi-shot, dolly) on the first try" }
capabilities: [text-to-video, image-to-video, reference-to-video, video-edit, video-extend, multi-shot, native-audio, structure-reference]
prompt:
  languages: ["en", "zh", "mixed"]
  formula: "Subject + Action (the kinetic core), then Camera, then Scene, Style, and Lighting, then Audio, then Constraints; write it as a director's shot brief, not an image description"
  references: "cite every asset with an at-sign, its type, and its number in upload order, spaced as the owner writes it (@Image 1, @Video 1, @Audio 1, @Clay Render 1), on every host; the closed-up @Image1 in older provider examples is legacy, not a host requirement; a contiguous run is @Images 6 to 10; bind a named subject with Name@Image 1 and repeat the binding each time the subject is mentioned"
  structure_reference: "an untextured 3D pass (clay render, white model) carries blocking, camera path, pacing, and shot-size changes; pair it with an image that carries look, and say which asset owns which axis"
  audio: "native and synchronized in one pass; write dialogue in quotes with a voice and tone, name sound effects on cue, and call for ambient or music inline"
  multishot: "drive cuts with shot or scene labels (Shot 1, Scene 1) or time ranges (0-3s); give each shot one primary action and one camera move; on the flagship a single pass can carry a full setup, development, turn, and resolution"
  length_strategy: "short and structured beats long and poetic; a few sentences per shot; length must buy beats, references, or timed segments, never adjectives; iterate short, then extend in rounds"
  negatives: "pick the three to five exclusions that matter; one or two crisp must-nots beat a paragraph"
sources:
  official: ["https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5", "https://docs.byteplus.com/en/docs/ModelArk/2222480", "https://docs.byteplus.com/en/docs/ModelArk/2291680"]
  provider: ["https://fal.ai/models/bytedance/seedance-2.5/reference-to-video", "https://fal.ai/models/bytedance/seedance-2.5/image-to-video", "https://fal.ai/learn/tools/how-to-use-seedance-2-0", "https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/", "https://wavespeed.ai/blog/posts/seedance-2-0-complete-guide-multimodal-video-creation/"]
  community: []
last_verified: "2026-08-07"
---

# Seedance: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, input counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers the Seedance 2 series: seedance-2.5, seedance-2.0, and seedance-2.0-fast. They share one prompt grammar, so everything here applies to all three unless a rule is marked as flagship-only. Earlier versions (1.5-pro, 1.0-lite) prompt differently and have their own guides; this guide does not cover them.
- Seedance is a video model. ByteDance's image model is Seedream, which is out of scope here.
- Write a Seedance prompt as a director's shot brief: who does what, how the camera moves, what we hear, and how shots cut. It is not an image description, so describe motion, not a static frame.

</rules>

## TL;DR

<template id="quickstart">

{subject} {one primary action}, {one camera move}, {scene and lighting}, {style}. {a specific sound cue or a quoted line}. For an edited sequence, label shots: Shot 1 {beat}; Shot 2 {beat}.

</template>

## Models and when to use which

All three share one prompt scheme. Write the same brief for any of them; what changes is how much of it survives.

- `seedance-2.5`: the flagship, built on the same joint audio-video architecture as 2.0. Reach for it when the prompt is carrying a whole story rather than a moment, when the cast or asset library is large, when you want to steer blocking with an untextured 3D pass, or when you need to edit by timestamp after the fact.
- `seedance-2.0`: the previous flagship. Still the right choice for single scenes where camera direction, physics, cuts, and synchronized audio need to land, and its prompts port to 2.5 unchanged.
- `seedance-2.0-fast`: same features at lower cost and latency, for rapid iteration and volume. It is less responsive to fine director controls (slow motion, multi-shot, dolly moves) on the first try, so use it to explore, then move up to finish.

Earlier Seedance generations (1.5-pro, 1.0-lite) are separate models with their own prompt guides and lack the 2 series' multimodal references, native audio, and one-pass multi-shot.

<rules id="model-choice">

- Prompts written for 2.0 run on 2.5 as-is. Migrating is about spending the larger window, not rewording.
- The gains that change how you write are all on the flagship: a story arc in one pass, a much larger reference load, the untextured-3D structure channel, and timestamp-addressable edits.
- 2.0 is looser about stray subtitles and unrequested background music, so keep those exclusions in the prompt when targeting it.

</rules>

## How the model reads prompts

- It wants direction, not keywords. "Cinematic shot of a mountain, 4K, beautiful lighting" gives the model almost nothing to animate. State what moves, how it moves, and what the camera does while it happens.
- Subject and action are the core. Lead with who is doing what; that is the kinetic anchor the rest hangs on.
- One primary action and one camera move per shot. If a single shot tries to hold a run, a pan, a lightning strike, and a mood shift at once, the model picks one and drops the rest. For a compound move, write it as beats ("start with a slow dolly-in, then pan right for the final stretch").
- Short and structured beats long and poetic. A few tight sentences per shot outperform a paragraph. The model honors the earliest strong instruction, so if it is wrong, later lines will not save it.
- Audio is generated with the video in one pass, so sound is direction you write inline, not a later step.
- References anchor, text nudges. When you supply a strong reference, keep the text minimal and specific; the reference carries the look or motion.
- Quality drifts on long takes, and how far you get before it does is the main thing that separates the tiers. Break a long shot into beats or shorter shots when detail must hold, and on the older tiers assume the wobble starts early.
- A long window is an invitation to write a story, not a longer sentence. On the flagship, fill it with a setup, a development, a turn, and a resolution; padding one moment out to fill the time is how you get a slow shot rather than a good one.
- Length has to buy something. Beats, references, timed segments, and camera changes all earn their words. Adjectives never do, and a pile of them costs you the specifics you wrote elsewhere.

## Prompt structure

<rules id="structure">

- Order the prompt: Subject and Action first, then Camera (shot size, movement, angle), then Scene, Style, and Lighting, then Audio, then Constraints.
- Put the shot size up front so the model fixes the framing instead of re-centering mid-take.
- Use one clear style anchor rather than a pile of adjectives ("shot on Super 16, muted palette" beats "cinematic, epic, beautiful, moody").
- State constraints last as guardrails: what to keep fixed, what to exclude, and the timing or beat.

</rules>

<template id="general">

{subject with key attributes} {one primary action}, {shot size and camera movement}, {scene and lighting}, {one style anchor}. {sound cue or quoted line}. {constraints}.

</template>

<example use_case="t2v-single-shot">

```text
A golden retriever runs across a sandy beach at sunset, kicking up wet sand with each stride, the camera tracking alongside at ground level. Waves crash softly in the background
```

*Why: one subject, one active verb, one camera move (ground-level tracking), and one anchored ambient sound, in the subject, action, camera, sound order*

</example>

## Camera and motion

<rules id="camera">

- Use camera terms a cinematographer would recognize; the model treats them as literal instructions, not mood words. "Dynamic" means nothing to a lens; "slow dolly-in" does.
- Movement: dolly, tracking, crane, handheld, gimbal, pan, orbit, push-in, pull-back, tilt, whip pan, dolly zoom (Hitchcock zoom), POV, aerial. Handheld adds micro-shake; gimbal stays smooth.
- Shot size, stated up front: wide (establish space), medium (subject plus context), close-up, extreme close-up, over-the-shoulder.
- Angle with intent: eye level reads neutral, low angle adds presence, high angle adds vulnerability or overview.
- Lens as a feel, not exact numbers: wide, normal, or telephoto (telephoto keeps the background soft).
- Pace the move: slow, medium, or fast. One verb per shot; sequence compound moves as beats.

</rules>

## Multi-shot sequences

A single generation can be an edited sequence with natural cuts rather than one continuous take.

<rules id="multishot">

- Label the cuts, or you get a single take. Use "Shot 1:", "Shot 2:" or "Scene 1", "Scene 2", or time ranges ("0-3s", "3-6s"), or explicit cut language ("cut to a close-up of ...").
- Give each shot one action and one camera move, plus its own sound cue.
- Keep continuity across cuts: hold the lighting and palette steady and carry the same subject or wardrobe between shots.
- Give the sequence room. If the duration is too short for the shot count, the model compresses or drops shots.
- To force a single unbroken move instead, say so: "single continuous take, no cuts".

</rules>

<example use_case="multishot-commercial">

```text
A 15 second beverage commercial, warm cinematic grade held across every shot. Shot 1 [0-4s]: extreme close-up of condensation beading on a cold glass bottle, slow dolly-in, the crisp tick of ice settling. Shot 2 [4-8s]: the bottle rises from crushed ice as the camera tilts up slowly, bright backlight forming a halo, a soft whoosh under rising music. Shot 3 [8-12s]: a hand lifts the bottle against a sunset rooftop, gimbal-smooth tracking alongside, the city humming below and a single cork pop. Shot 4 [12-15s]: the label fills the frame and the text "Stay Cold" fades in at the lower center in clean white type as the music resolves
```

*Why: a detailed multi-shot sequence with time ranges, one action and one camera move per shot, a consistent grade carried across cuts for continuity, a distinct sound cue per beat, and synchronized on-screen text in the final shot*

</example>

## Long-form sequences and timed segments

On the flagship a single pass can carry a whole story rather than one moment. That is a writing change, not just a longer clip.

<rules id="longform">

- Structure the window as setup, development, turn, and resolution. A story that goes somewhere reads better than a single moment stretched to fill the time.
- Pin beats to explicit time ranges written into the prompt: `0-5s:`, `6-10s:`, `11-20s:`. Each segment gets its own action, camera behavior, and subject focus.
- Timed segments and cut labels are alternatives, not rivals. Use segments when you want continuous motion paced across the window, and cut labels when you want visible edits.
- For an unbroken move, say so up front and repeat it as a constraint: "single continuous take, smooth camera movement, no cuts".
- Open the prompt with the global settings that apply to every segment (framing, texture, take style, scene reference), then run the timeline. Anything you leave until segment three will not retroactively fix segment one.
- Build past the window in rounds rather than in one prompt. Extend the finished clip, restating the subjects, scene, style, and audio that must carry over.

</rules>

<template id="timed-segments">

{global framing, texture, and take style}. {scene reference}. 0-{X}s: {beat, camera behavior, subject focus}. {X}-{Y}s: {beat}. {Y}-{Z}s: {beat, and how it resolves}.

</template>

<example use_case="one-take-story-arc">

```text
One-take handheld gimbal tracking shot. The camera slowly pushes in through a gap in a heavy red curtain and enters a warm-toned backstage dressing room. A young female singer, with her back to the camera, is adjusting her earpiece as a staff member reminds her it's time to go on. She turns toward the camera and starts singing citypop. The camera pulls back and tracks her as she passes through the curtain into a dim backstage corridor, interacting naturally with her dancers along the way; one staff member hands her a microphone. She and the dancers then step onto the stage, and the camera arcs around to the back, gradually revealing the red-and-black stage design, LED screens, spotlights, haze, and reflective floor. The camera finally pulls out to a wide shot of the arena, showing the packed audience, light boards, glow sticks, and cheering crowd.
```

*Why: the flagship long-form pattern. One continuous camera carries four locations and a full arc, and every clause advances the subject or the camera rather than decorating the frame.*

</example>

<example use_case="timed-segments-multi-reference">

```text
16:9 widescreen, cinematic texture, single continuous take, smooth camera movement, no cuts. Scene reference: @Image 4. 0-5s: Open with a close-up of the Overlord from @Image 2. The camera slowly circles his upper body and transitions into a medium shot. The Overlord spins and turns, his body and back flags sweeping quickly past the lens to form a natural occlusion, and the camera follows through to Consort Yu's side in @Image 1. 6-10s: The camera steadily circles Consort Yu in a medium shot from @Image 1, following her water sleeves through the arc. She raises her arm, flicks her wrist, unfurls the sleeves, and half-turns, then holds the pose and looks sideways toward the Overlord. 11-20s: The male warrior from @Image 3 enters with an aerial flip. The Overlord takes center stage while the warrior advances and retreats on the opposite side in a combat exchange. The camera slowly pulls back from a medium-close shot to a full stage view, and all three strike a synchronized finale pose.
```

*Why: global settings first, then a timeline. Three characters each stay welded to their own image across segments, and the no-cuts constraint keeps the timing marks from being read as edit points.*

</example>

## Audio and dialogue

Seedance 2.0 generates synchronized audio alongside every frame in the same pass, so timing is locked. Direct it inline.

<rules id="audio">

- Be specific about what to hear. "A massive explosion that shakes the camera, debris clattering across concrete" gives the audio pass far more than "an explosion".
- Name sound effects on cue, and call for ambient sound and music by mood ("tense percussive score", "soft jazz in the background"). The model reads genre context.
- Write dialogue as a quoted line attached to a speaker, with a tone and voice ("a deep, serene male voice says: ..."). Lines in any language work inside quotes.
- Lip-synced dialogue works, but sound effects and ambient audio are the strongest; test dialogue before committing to a dialogue-heavy pipeline.
- To suppress audio elements, say so ("no dialogue", "no music").

</rules>

<example use_case="audio-forward">

```text
A vinyl record drops onto a turntable and the needle settles into the groove with a soft crackle. The camera slowly pushes toward the spinning label as warm analog music begins. Dust drifts in the beam of a desk lamp
```

*Why: layered, concrete sound cues (crackle into analog music) plus one camera move give the synchronized audio pass specific things to render*

</example>

## Reference inputs

Seedance combines a text prompt with reference images, video clips, audio, and untextured 3D passes. The citation convention is the load-bearing skill.

<rules id="references">

- Cite every asset with an at-sign, its type, and its number in upload order: `@Image 1`, `@Image 2`, `@Video 1`, `@Audio 1`. Never reference an asset by its raw asset ID.
- Use the owner's spaced form on every host. A citation is ordinary prompt text, not a host parameter: providers describe it as something you write "in your prompt", and the prompt reaches the same closed model whichever service you route through. The owner's spelling is the one that model's own documentation and demonstration prompts use, so it is the safest thing to send anywhere.
- You will meet `@Image1` closed up in two long-form provider walkthroughs, one at FAL and one at WaveSpeed, both from a period when the owner still wrote references bare. It is not house style at either company: their other Seedance pages use the bare form, and neither has published Seedance guidance since. Treat the closed-up spelling as legacy from two articles, not as a host requirement. If a binding genuinely fails on one host, its own spelling is a cheap thing to try, but it is not where to start.
- Stay consistent within a prompt. Mixing spellings across citations is how a binding gets missed.
- Cite a contiguous run in one phrase rather than listing it out: `@Images 6 to 10` for the rest of an orchestra, `@Images 15 to 18` for the audience. This is how a large cast stays readable.
- Bind a named subject to its asset with the closed form `Name@Image 1`, and repeat the binding every time that subject is mentioned. Use it whenever several people share a scene and a bare name would be ambiguous.
- Assign one role per asset by saying what to take from it: "the character from `@Image 1`", "the camera movement in `@Video 1`", "the background music from `@Audio 1`". This is the same habit as multi-image editing: one role per input, each element welded to its source.
- Say when a binding is strict. "The lead vocalist must strictly follow `@Image 5`" holds an identity harder than a bare citation, which is worth spending on the one or two subjects that matter most.
- What each type carries best: an image gives look, identity, wardrobe, or a first or last frame; a video gives motion, camera movement, shot language, VFX, or an editing rhythm; audio gives a voice timbre, music, or a beat to cut to.
- When references conflict, pick one to dominate (clean, short, unmistakable) and keep the text minimal. Competing look-versus-motion references blend into a muddy middle.
- You can scope a reference to one attribute ("appearance only") so it does not pull in pose or background.
- Upload assets in the order the prompt refers to them, since the number is the sort order.

</rules>

<example use_case="r2v-role-per-asset">

```text
Refer to the fight choreography and shot language in @Video 1 to stage a duel in the rain-soaked alley from @Image 3, with the swordsman from @Image 1 on the left and the masked fighter from @Image 2 on the right. Cut the action to the rhythm of @Audio 1, and add heavy rain, the ring of clashing steel, and a low percussive score
```

*Why: five assets in five distinct roles (@Video 1 the choreography and shot language, @Image 1 and @Image 2 the two fighters with positions, @Image 3 the setting, @Audio 1 the cut rhythm), each welded to its source, with layered sound called inline*

</example>

<example use_case="r2v-product-and-style">

```text
Place the perfume bottle from @Image 1 on a wet marble ledge, lit and color-graded like the mood board in @Image 2. Follow the slow push-in and rack focus from @Video 1 while a calm female voice delivers the line from @Audio 1, keeping the bottle's shape and label exact and unchanged
```

*Why: four assets in four roles (@Image 1 the hero product, @Image 2 the look reference, @Video 1 the camera move, @Audio 1 the voiceover), with the product pinned as the invariant so only the scene around it is built*

</example>

<example use_case="large-cast-with-ranges">

```text
A 30-second concert sequence in 16:9 landscape, with cinematic realism, authentic concert hall lighting, and the atmosphere of a formal classical concert. Use @Image 1 for the venue. Reference @Image 2 for the pianist. Reference @Image 3 for the cello. Reference @Image 4 for the violin. The lead vocalist must strictly follow @Image 5. Reference @Images 6 to 10 for the rest of the orchestra. Reference @Images 11 to 14 for the choir. Reference @Images 15 to 18 for the audience seating. Open with a high-angle wide shot of the full hall. The pianist strikes the keys and the lead vocalist steps into the spotlight and begins singing. The camera moves across the violin, cello, and orchestra as they perform, the violin bright and the cello warm. In the closing shot the camera pulls back, the singing ends, and the audience applauds.
```

*Why: a large cast stays readable because contiguous groups collapse into range citations, the one identity that matters most is bound with "must strictly follow", and the remaining words go to blocking and camera rather than to re-describing people the references already settled.*

</example>

## Structure references

An untextured 3D pass, called a clay render or white model, is a reference channel of its own. It carries geometry and motion with no look attached, which lets you separate blocking from styling instead of trying to get both out of one image.

<rules id="structure-reference">

- Cite it like any other asset: `@Clay Render 1`. It is a distinct type, so its numbering is its own.
- Take from it what it actually holds: camera movement, pacing, shot-size transitions, subject trajectory, blocking, spatial structure, character poses, and camera angles.
- Pair it with an image that carries the look, and say explicitly which asset owns which axis. This is ONE ROLE PER INPUT at its cleanest: structure from one, appearance from the other.
- Name the target style, since the render itself has none. "Render the white model as a dreamy, warm, 3D animated short" tells the model what to dress the geometry in.
- Lighting can be inherited from the geometry. Because the pass carries spatial information, asking for light source direction, color temperature, intensity, and shadow projection gives physically consistent results rather than painted-on light.
- Use it when composition and blocking are non-negotiable, such as a complex product or assembly shot, and when a text description of the camera path would be longer than the shot is worth.

</rules>

<template id="structure-reference">

Refer to @Clay Render 1 for {camera movement, pacing, blocking, trajectory}. Refer to @Image 1 for {materials, lighting, color, atmosphere}, and render the white model as {target style}.

</template>

<example use_case="clay-render-styled">

```text
Refer to @Clay Render 1 for camera movement, pacing, shot-size transitions, subject trajectory, and blocking. Refer to @Image 2 for character design, scene, materials, lighting, color, and fairy-tale atmosphere, and render the white model as a dreamy, warm, 3D animated short with a childlike fantasy feel. The story unfolds as follows: flight through a fantasy sky, then mythical beasts flying alongside through a sea of clouds, then a dive into the ocean, then weaving through the deep with manta rays, then passing through a mirrored rift in spacetime, then picking stars from the cosmos, then transforming back into the bedroom, then a father tucking in the blanket, and finally the picture book closing and holding on the last frame.
```

*Why: the two references are split cleanly along structure and look, neither is asked to do the other's job, and the beat list rides on top of a camera path that was already decided in 3D rather than described in words.*

</example>

## By mode

### Text-to-video

<rules id="t2v">

- The prompt drives everything: subject and action, camera, sound, and any cuts. Describe motion, not a still.

</rules>

### Image-to-video

<rules id="i2v">

- Provide a start image and describe the motion you want; the model preserves the image's content and adds the movement. Prompt for what changes (camera path, how elements move, light shifts), not the static appearance.
- For an exact A-to-B animation, supply a first and a last frame and describe the transition that carries one into the other.

</rules>

<example use_case="i2v-motion-only">

```text
Slow camera push toward the subject, soft wind moves the hair, the natural light shifts slightly warmer. A faint room tone underneath
```

*Why: describes only motion, camera, and a light shift, animating the supplied image rather than redrawing it*

</example>

### Reference-to-video

<rules id="r2v">

- The multimodal mode: combine images, videos, and audio with the text, naming each by type and number as in Reference inputs above.
- State the relationship between the generated scene and each reference explicitly, and let the dominant reference carry the look or motion while the text stays minimal.
- Set persistent directives once up front ("use the framing from @Video 1 throughout", "use @Audio 1 as the music for the whole clip"), then sequence the shots.

</rules>

<example use_case="r2v-full-multimodal-sequence">

```text
A vertical short-form cafe ad. Use the first-person, handheld feel from @Video 1 throughout, and use @Audio 1 as the background music for the whole clip. The opening frame is @Image 1. Shot 1 [0-3s]: a barista in the cafe from @Image 2 sets a tall glass on the counter, close-up, the clink of glass over soft ambient chatter. Shot 2 [3-7s]: she pours the iced tea from @Image 3 over the ice, the camera pushes in on the splash with a crisp pour-and-fizz sound. Shot 3 [7-11s]: she slides the drink forward and says, in a warm, upbeat female voice, "First sip is the best sip." Shot 4 [11-15s]: cut to a wide shot of the cafe, the logo from @Image 4 holds in the lower right, and the final frame freezes on @Image 5. Keep the logo and the glass design unchanged across every shot
```

*Why: a long, fully specified multimodal prompt that binds seven assets to distinct roles (@Video 1 the framing, @Audio 1 the music throughout, @Image 2 the setting, @Image 3 the drink, @Image 4 the logo, @Image 1 and @Image 5 the opening and frozen end frames), sequences time-ranged shots with one action, one camera move, and a synced sound per shot, places a single quoted line, and pins the logo and glass as invariants*

</example>

### Edit and extend video

<rules id="edit-extend">

- State only the change. The model preserves the parts you do not mention, so name what moves and pin what stays ("replace the cat in @Video 1 with the lion from @Image 1, keep the rest of the video unchanged").
- Scope an edit to a single axis when that is what you mean. "Adjust only the camera movement" plus an explicit list of what stays unchanged is far more reliable than describing the result you want and hoping the rest survives.
- Address edits by timestamp. Name the second and the region, then the change: at {time} in {clip}, {what to add, remove, or replace}. A timed edit plan can run several segments in one instruction.
- Extend forward or backward by describing the new content; to keep the original segment, say so, since extension may otherwise return only the new footage.
- On an extension, restate what must carry over. Subjects, scene, visual style, and sound effects all need naming, because the model is generating fresh footage rather than copying.
- Green-screen work is an editing mode: name what replaces the background and let the model resolve how the subject responds to the new environment, including cloth movement, hair, gait, and light interaction.
- To stitch clips into one coherent video, name them in order and describe the transition between each ("@Video 1, then a gust of wind leads into @Video 2").

</rules>

<template id="timed-edit">

Edit @Video 1. Keep {what stays} unchanged. Adjust only {the one axis}. 0-{X}s, {change}; {X}-{Y}s, {change}; {Y}-{Z}s, {change}.

</template>

<example use_case="edit-subject-swap">

```text
Replace the cat in @Video 1 with the lion from @Image 1. The lion lies across the girl's legs in the same spot, keep the rest of the video unchanged
```

*Why: names the single change and the source of the new subject, and pins everything else as unchanged*

</example>

<example use_case="edit-camera-only">

```text
Edit @Video 1. Keep the characters, actions, and visual style unchanged. Adjust only the camera movement. A 15-second segmented camera plan: 0-4s, a micro-FPV move skims tightly past the pan, then follows the popping toast and whip-pans to the coffee; 4-7s, push in and track laterally along the rim of the pan, following the fried egg as it flips up and lands back in place; 7-11s, rapidly rise to a top-down view, then descend at a steady pace, sweeping across the plate and keys; 11-15s, use a handheld close-up to follow the hands with a fast lateral whip, then push in on the breakfast and pull back to a medium two-shot. Keep the entire sequence smooth, continuous, and stable.
```

*Why: one axis is opened and everything else is nailed shut in the second sentence, so a four-segment camera rewrite lands without disturbing performance or grade.*

</example>

<example use_case="edit-green-screen-timed">

```text
Using @Video 1, render the green-screen background, obstacles, wardrobe, and supporting characters. 0-4s: outdoor training, replace the obstacles with rocks, bricks, tires, and wooden crates. 4-10s: locker room, friends offering encouragement. 10-15s: international match, replace the training poles with original defenders and a goalkeeper, and the protagonist scores. Overall photorealistic, cinematic quality.
```

*Why: one green-screen performance is re-set into three different environments on a timeline, with the subject left untouched so the model resolves how they react to each new space.*

</example>

<example use_case="extend-with-carryover">

```text
Extend the video. Continue from the visuals and subjects in @Video 1 and generate another clip, keeping the character subjects, scene, visual style, and sound effects consistent. The little boy runs along the train carriage holding a soccer ball. When the subway stops, the side door opens and he immediately dashes out, with the male lead chasing after him. The two run across the platform and out onto the street, startling passersby and vehicles along the way. The male lead finally catches up and grabs him. The boy looks up, aggrieved. The male lead's anger slowly fades; he pats the boy's head and shows a helpless smile.
```

*Why: the carryover list is explicit rather than assumed, and the new footage is written as its own small arc so the extension advances the story instead of idling.*

</example>

## On-screen text and subtitles

<rules id="text">

- Build a slogan from text, timing, position, entrance style, and visual attributes: a line that reads "{exact text}" appears {when} at the {position}, {how it animates}, in {color and font style}.
- Use common, high-frequency words and few special symbols; rare words and heavy punctuation hurt rendering.
- For dialogue captions, ask for subtitles synchronized to the audio ("subtitles at the bottom center, synchronized with the audio, appearing as each character speaks"). For comic framing, ask for speech bubbles around the speaker.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- Pick the three to five exclusions that matter for the shot; one or two crisp must-nots beat a paragraph, and too many negatives dull the result.
- Useful categories: visual noise (no text overlays, no watermarks), identity drift (no extra characters, no crowd), camera chaos (no snap zooms, no whip pans, no Dutch angles), body artifacts (no extra fingers, no warped hands), and grade (no heavy teal and orange).
- If artifacts persist after two tries, do not stack more negatives; adjust the subject wording or simplify the camera move instead.
- If you add a voiceover in post, ban auto captions.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Static image-style prompts: a still description gives no motion. Say what moves and what the camera does.
- Unlabeled multi-shot: without shot labels a longer prompt collapses into one continuous take.
- Overloaded shots: more than one action or camera move per shot makes the model choose and drop intent.
- Too little time for the shot count: the model compresses or skips shots; give the sequence room or cut the shot count.
- Vague audio: "add sound" yields generic noise; name the specific sounds.
- Reference confusion: cite each asset as @Type N, assign one role to each, and let one reference dominate when they compete.
- Copying the closed-up @Image1 from an older provider example: it predates the owner's own use of the notation. Write @Image 1 everywhere, and never mix the two spellings inside one prompt.
- Listing a crowd asset by asset: collapse contiguous groups into @Images 6 to 10 instead of ten separate clauses.
- A long window filled with one moment: the extra seconds are for a story arc, not for slowing a single action down.
- Structure reference asked to carry look: a clay render has no materials or palette, so pair it with an image and say which asset owns which axis.
- Unscoped edits: describing the finished result invites collateral change. Open one axis, then pin the rest.
- Long unbroken takes: expect drift past the first several seconds; break into beats or shorter shots when detail must hold.
- Real human faces: hosts restrict uploading reference images or video of real people; source character consistency from model-generated, preset, or authorized assets instead.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

- Official (ByteDance, BytePlus, Dreamina): [Seedance 2.5 announcement](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5), [Seedance 2 series prompt guide](https://docs.byteplus.com/en/docs/ModelArk/2222480), [Seedance 2 series tutorial](https://docs.byteplus.com/en/docs/ModelArk/2291680).
- Provider: [fal Seedance 2.5 reference-to-video](https://fal.ai/models/bytedance/seedance-2.5/reference-to-video), [fal Seedance 2.5 image-to-video](https://fal.ai/models/bytedance/seedance-2.5/image-to-video), [fal how to use Seedance 2.0](https://fal.ai/learn/tools/how-to-use-seedance-2-0), [WaveSpeed Seedance 2 prompt template](https://wavespeed.ai/blog/posts/blog-seedance-2-0-prompt-template/), [WaveSpeed Seedance 2 complete guide](https://wavespeed.ai/blog/posts/seedance-2-0-complete-guide-multimodal-video-creation/).

Coverage note: the reference citation form changed under this guide. An earlier pass recorded the bare "Image 1" as the owner form and the at-sign as a provider-only variant. Comparing the archived scrape of the owner's prompt guide against the current one shows that page carried no at-sign citations in May and carries twenty-seven now, revised on the day the flagship shipped, so the source changed rather than being misread. The at-sign is now common to the owner and both providers, but they space it differently, and the guide teaches the owner's spaced form for every host rather than switching per provider. The reasoning is that a citation is prompt text rather than a host parameter, so it reaches the same closed model either way, and the provider examples showing the closed-up spelling are dated two months before the owner adopted the notation at all. Neither provider has published Seedance guidance since. The flagship's own API reference has not published yet, so its rules here are drawn from the owner's announcement prompts and from the live provider endpoints; expect to re-verify the flagship sections when the reference lands.

Last verified: 2026-08-07.
