---
guide: "Vidu (video)"
prompt_scheme: "vidu"
models:
  # ShengShu Technology. Every model is hosted; no weights are published. API ids shown; the app and CLI use other names (see Model names and aliases)
  - { id: "viduq4-preview", access: "closed-weights", tier: "flagship", caps: [image-to-video, reference-to-video, multi-shot, native-audio, dialogue, voice-reference], best_for: "the newest generation, in preview: animating a still, or combining many image references and voice clips into one multi-shot scene with lip-synced speech. The owner leads on high-dynamic action (martial arts, chases, fights) and effects (explosions, particles, energy). No text-to-video and no start-end mode, and references are tagged by position, not by subject name" }
  - { id: "viduq3-pro", access: "closed-weights", tier: "std", caps: [text-to-video, image-to-video, first-last-frame, multi-shot, native-audio, dialogue], best_for: "the Q3 quality tier for text, a single still, or a start and end frame; dialogue, sound and shot changes generated with the picture" }
  - { id: "viduq3-turbo", access: "closed-weights", tier: "distilled", caps: [text-to-video, image-to-video, first-last-frame, reference-to-video, multi-shot, native-audio, dialogue], best_for: "the fast Q3 tier, and the Q3 model that takes named subjects. The owner sells it on speed and cost and publishes no quality claim against pro, so run a hard prompt on pro before blaming the wording" }
  - { id: "viduq3-pro-fast", access: "closed-weights", tier: "distilled", caps: [image-to-video, first-last-frame, multi-shot, native-audio, dialogue], best_for: "a faster pro for a still or a start and end pair; the owner rates its quality on par with viduq3-pro" }
  - { id: "viduq3-mix", access: "closed-weights", tier: "std", caps: [reference-to-video, multi-shot, native-audio, dialogue, voice-reference], best_for: "general reference-to-video; the owner calls it the strongest overall balance among the Q3 reference models" }
  - { id: "viduq3-drama", access: "closed-weights", tier: "std", caps: [reference-to-video, multi-shot, native-audio, dialogue, voice-reference], best_for: "comic and short drama; the owner rates it best in the Q3 series for dialogue, character positioning and film-style camera language" }
  - { id: "viduq3-ad", access: "closed-weights", tier: "std", caps: [reference-to-video, multi-shot, voice-reference], best_for: "short advertising clips from product and model references, with cut pacing tuned for ads; the owner asks for reference images that are not too similar to each other" }
  - { id: "viduq3", access: "closed-weights", tier: "std", caps: [reference-to-video, multi-shot, native-audio, dialogue], best_for: "the plain Q3 reference model: one subject held consistent across several camera positions, with sound" }
  - { id: "viduq2-pro", access: "closed-weights", tier: "std", caps: [image-to-video, first-last-frame, reference-to-video, reference-video, video-edit, native-audio, dialogue], best_for: "the only Vidu model that takes video as input: edit, replace or restyle from source footage, or follow a reference clip. Also rich detail from a still or a frame pair" }
  - { id: "viduq2", access: "closed-weights", tier: "std", caps: [text-to-video, reference-to-video, native-audio, dialogue], best_for: "strong motion and emotional expression from text or named subjects" }
  - { id: "viduq2-turbo", access: "closed-weights", tier: "distilled", caps: [image-to-video, first-last-frame, native-audio, dialogue], best_for: "fast Q2 animation of a still or a frame pair; the owner claims speed and good quality, nothing against pro" }
  - { id: "viduq2-pro-fast", access: "closed-weights", tier: "budget", caps: [image-to-video, first-last-frame], best_for: "the cheapest Vidu animation of a still or a frame pair; the owner sells it on price and speed" }
  - { id: "viduq1", access: "closed-weights", tier: "legacy", caps: [text-to-video, image-to-video, first-last-frame, reference-to-video, native-audio, dialogue], best_for: "sharp visuals and stable camera movement; superseded by Q2 and Q3" }
  - { id: "viduq1-classic", access: "closed-weights", tier: "legacy", caps: [image-to-video, first-last-frame, native-audio, dialogue], best_for: "richer transitions and camera movement than viduq1 from a still; superseded" }
  - { id: "vidu2.0", access: "closed-weights", tier: "legacy", caps: [image-to-video, first-last-frame, reference-to-video, native-audio, dialogue], best_for: "fast generation; superseded" }
  - { id: "vidu1.5", access: "closed-weights", tier: "legacy", caps: [image-to-video, reference-to-video, native-audio, dialogue], best_for: "large motion amplitude; superseded" }
capabilities: [text-to-video, image-to-video, first-last-frame, reference-to-video, reference-video, video-edit, multi-shot, native-audio, dialogue, voice-reference]
prompt:
  languages: ["en", "zh", "ja", "any"]
  formula: "subject or scene, what happens, environment, then art style or medium; camera movement as its own closing clause; restate the key style and atmosphere words across the prompt"
  length_strategy: "rich, specific and complete. Expand a one-line idea into a full paragraph that commits to light, color, texture and camera, without literary flourish; extra length must carry content (a beat, a cut, a line of dialogue, a sound)"
  references: "SPLIT BY GENERATION. Named subjects (Q3 turbo and drama, Q2, Q1, 2.0): [@name] with the subject's exact name. Q4 preview: [@reference_image_1] for images and [reference_audio_1], with no @, for voices, numbered from 1 in upload order. Plain image lists elsewhere: no tag; name each reference by what it shows"
  audio: "Q3 and Q4 generate dialogue, voiceover, sound effects and music with the picture; a spoken line goes in quotes after its speaker, narration is reported speech, and sounds are named plainly. Q3 speaks English, Japanese or Chinese"
  multishot: "Q3 and Q4 cut between camera positions on their own; ask for a cut in words, e.g. 'then the shot cuts to a close-up'. There is no shot-list syntax"
  auto_expand_behavior: "the owner's service rewrites prompts internally and never returns the rewrite. A recommended-prompt option, where a host exposes it, discards the written prompt entirely; some hosts add their own expansion toggle. Write the full prompt and keep both off when wording matters"
  negatives: "no negative field on any Vidu surface; describe the wanted alternative, and write an exclusion into the prompt only for a specific, likely failure"
sources:
  official: ["https://platform.vidu.com/docs/overview/model-map", "https://platform.vidu.com/docs/api-reference/updates", "https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/reference-to-video", "https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/image-to-video", "https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/reference-to-video", "https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/text-to-video", "https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/start-end-to-video", "https://platform.vidu.com/docs/api-reference/video-models/vidu-q2/reference-to-video", "https://platform.vidu.com/docs/overview/faq", "https://www.vidu.com/vidu-q4", "https://www.vidu.com/vidu-q3", "https://www.vidu.com/blog/consistent-character-ai", "https://github.com/shengshu-ai/vidu-skills"]
  provider: ["https://help.aliyun.com/en/model-studio/vidu-video-generation-prompt-guide", "https://fal.ai/models/fal-ai/vidu/q4/reference-to-video", "https://fal.ai/models/fal-ai/vidu/q4/image-to-video", "https://wavespeed.ai/docs/docs-api/vidu/vidu-q4-reference-to-video", "https://wavespeed.ai/docs/docs-api/vidu/vidu-q3-start-end-to-video"]
  community: []
last_verified: "2026-11-08"
---

# Vidu: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, duration and resolution limits, input counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- Vidu is ShengShu Technology's video line. Every model is hosted and none has published weights.
- Every Vidu model takes one plain-language prompt: no JSON, no keyword tags, no negative field. Generations differ in modes, sound and the reference token, not in grammar, so one guide covers Q4 preview back to 1.5.
- The reference token is the one thing that does NOT carry across generations. Check the generation before writing a tag (see Reference images).
- Vidu's image models (text-to-image and reference-to-image) are not covered here. Vidu S, the real-time digital-human service, is not a prompt-to-clip model and is out of scope.
- Vidu's own app and CLI also serve models that are not Vidu. A model they label as another vendor's (the owner's CLI labels viduq2-drama-std as Wan 3) is prompted with that vendor's guide.

</rules>

## Model names and aliases

| Name in the app or CLI | API id | Note |
| --- | --- | --- |
| Vidu Q4, 3.4 | viduq4-preview | Preview generation; image-to-video and reference-to-video only |
| Vidu Q3, 3.2 | viduq3-pro, viduq3-turbo, viduq3-pro-fast, viduq3-mix, viduq3-drama, viduq3-ad, viduq3 | "Q3" alone names seven API models; pick by mode |
| Q3-A, Omni Video Pro, 3.2_a | not listed in the API docs | App model; same grammar, takes named materials as [@name] |
| Q3.1 Drama, viduq3.1-drama-std | not listed in the API docs | App drama model; same grammar |
| Vidu Q2, 3.1; Q2 Pro, 3.1_pro | viduq2, viduq2-pro | Also viduq2-turbo and viduq2-pro-fast |
| Vidu Q1, 3.0 | viduq1, viduq1-classic | Legacy |
| viduq2-drama-std | labelled Wan 3 by the owner's CLI | Not a Vidu model: use the Wan Video guide |

<rules id="naming">

- Teach and write the API id. Translate an app name or CLI version number on sight using the table.
- The CLI's 3.x numbers are product versions, not a Vidu 3.0 model: 3.2 is Q3 and 3.4 is Q4.
- "Q3" or "Q4" alone is ambiguous only for Q3, which spans seven API models. Choose by the input the user has (text, a still, a frame pair, references) and the job (drama, ads, general).
- A "drama" id is not always Vidu. viduq3-drama is Vidu; viduq2-drama-std is labelled Wan 3 by the owner.

</rules>

## TL;DR

<template id="quickstart">

{shot size and angle}, {subject with one or two defining details} {does one action} in {setting}, {light and color}, {atmosphere}, {style or medium}. {Camera movement}.

</template>

<template id="quickstart-dialogue">

{style}, {setting}. {Speaker} {action}, then says to {listener}, "{short line}". {Listener} {reaction verb} and answers, "{short line}". The shot cuts to {new framing}. {Sound bed}. {Camera movement}.

</template>

## Models and when to use which

Pick by what you hand the model, then by generation.

- Text alone: viduq3-pro for quality, viduq3-turbo for speed. Q4 has no text-to-video.
- One still to animate: viduq4-preview for action, effects and speech, viduq3-pro for a Q3 look, viduq2-pro for detail without sound.
- A start frame and an end frame: viduq3-pro or viduq3-pro-fast. Q4 has no start-end mode.
- Several references that must stay consistent: viduq4-preview for the widest mix of images and voice clips; viduq3-drama for dialogue-led drama; viduq3-ad for product clips; viduq3-mix for anything else.
- Named, reusable characters: the subject mode on viduq3-turbo, viduq3-drama, viduq2 or viduq1. Q4 does not take subject names.
- Source video to change: viduq2-pro is the only model that takes video in.

<rules id="model-choice">

- Prefer Q3 or Q4 whenever the clip needs speech, sound or more than one shot; those generations produce audio and cut between camera positions on their own.
- The fast tiers keep the grammar but the owner publishes nothing on what they give up, except that viduq3-pro-fast is rated on par with pro. When a turbo or fast result misses, rerun the same prompt on pro before rewriting it.
- viduq3-ad is tuned for short ad clips and cut pacing. Give it reference images that differ from each other; the owner says overly similar inputs hurt it.
- Treat Q1, 2.0 and 1.5 as legacy. Their prompts use the same grammar, with no documented shot switching.

</rules>

## How Vidu reads prompts

<rules id="reading">

- Vidu reads plain natural language and follows it closely; the owner leads on semantic understanding. Write sentences, not keyword lists.
- The owner's service rewrites prompts internally and does not return the rewrite. A complete prompt leaves the rewrite less to invent.
- A recommended-prompt option, where a host exposes it, writes its own prompt from the input image and ignores yours. One owner page shows it on by default for Q4 image-to-video. Check that it is off before judging a result against your wording.
- Some hosts add a prompt-expansion toggle of their own. Leave it off when the exact wording matters; turn it on only for a bare one-line idea.
- Motion strength is set in words. Owner docs say the motion-amplitude switch some hosts expose does not take effect from Q2 on; "high motion", "fast movement" and "subtle motion, slight movement" do.
- Anime is a first-class style. The owner states text-to-video has a specially optimized anime style, and anime stills animated with image-to-video hold their style with rarely any drift.
- Sound is generated with the picture when the host turns audio on. Supplying a voice clip is a separate control and does not by itself turn sound on.
- Q3 speaks English, Japanese or Chinese. The prompt itself can be written in many languages; write a spoken line in the language it should be spoken in.

</rules>

## Prompt structure

<rules id="structure">

- Default order (ShengShu's formula, carried by Alibaba Cloud's guide): subject or scene, then what happens, then the environment, then the art style or medium.
- Shot size and camera angle may lead the prompt. Camera movement goes in its own closing clause, or on a trailing "Requirements" line, not buried mid-sentence.
- Be specific and complete. Avoid ambiguous terms, and use fluent, natural phrasing rather than literary description.
- Keep the cast small and together. Too many subjects, or subjects scattered across the frame, is the first thing the formula warns against.
- Restate the key style and atmosphere words at the start, middle and end of the prompt with varied wording (gentle, soft, serene), not mechanical repetition. Repetition is how Vidu holds a consistent look across the clip.
- Show direction of travel with scale: "the front of the train gradually gets larger, pine trees shrink into the distance" reads as forward motion where "moves forward" can play backwards.
- A walking subject under a static camera can look stiff. Add a camera move (zoom out, follow) and the motion reads more naturally.
- Name framing explicitly: "low angle" and "wide shot" hold better than "from below" and "zoomed out".
- For comic-drama reference work a header-first order is a tolerated variant: style, shot size, camera position, composition, camera movement; then the action in plain language; then one sentence mapping each reference image to its role.

</rules>

<template id="general">

{Shot size}, {camera angle}. {Subject, with the details that matter} {does the action} {how: speed, manner, emotion}. {Environment: place, time, weather}. {Light and color}, {atmosphere words}. {Style or medium, restating one atmosphere word}. {Camera movement}.

</template>

<template id="drama-header">

{style}, {shot size}, {camera angle or position relative to the axis}, {composition}, {camera movement}; {characters} {action in plain language}. Image 1 is [scene]; Image 2 is character [{name}]; Image 3 is [{prop}].

</template>

<example use_case="expanded-text-to-video">

```text
Capture a serene moment of a corgi pup gracefully swimming in a sunlit pool. The underwater perspective reveals the puppy's gentle smile as soft golden light filters through the water surface, creating dancing shadows on the pool floor. The scene is rendered in soft pink tones, creating a dreamlike ethereal atmosphere. High-resolution cinematography captures every delicate detail of the water texture and the corgi's joyful expression, creating a simple yet cinematic portrait of tranquility and innocence. This minimalist, emotionally resonant setting conveys a sense of calm and happiness, an ideal cinematic shot that is both visually striking and deeply peaceful.
```

*Why: ShengShu's own expansion of "A corgi puppy swimming in a large pool" (via Alibaba Cloud): subject and action first, then light, color, texture and camera, with serene, gentle and soft repeated in varied form from start to end.*

</example>

<example use_case="text-to-video-owner">

```text
In an ultra-realistic fashion photography style featuring light blue and pale amber tones, an astronaut in a spacesuit walks through the fog. The background consists of enchanting white and golden lights, creating a minimalist still life and an impressive panoramic scene.
```

*Why: the owner's text-to-video example across Q1 to Q3: style and palette lead, one subject with one action, then the background as its own sentence.*

</example>

## Camera, motion and style vocabulary

These are the words Vidu's documentation says it responds to. Use them verbatim where they fit.

<rules id="vocabulary">

- Motion intensity: "high motion, fast movement, extra-large motion"; "medium motion"; "subtle motion, slight movement".
- Camera movement: "camera pans left", "camera pans right", "camera tilts up", "camera tilts down", "camera zooms in", "camera zooms out", "static shot, fixed camera". Orbits go clockwise or counterclockwise. Moves combine with a plus sign: "zoom in + clockwise orbit".
- Shooting techniques: time-lapse, macro shot, first-person (FPV) shot, aerial or drone shot, underwater photography, handheld, overhead.
- Shot size: long shot, full shot, medium shot, close-up, extreme close-up.
- Camera angle and position: low angle, high angle, eye-level, bird's-eye view; "left of axis" or "right of axis" places the camera on one side of the action line.
- Composition: diagonal, rule of thirds, symmetrical, horizon line, centered, over-the-shoulder, Dutch angle.
- Visual style (text-to-video and reference-to-video; image-to-video takes its style from the image): 2D anime style, 3D rendering style, realistic, ink wash painting style, line art style, pixel art style, oil painting style.
- Film genre styles from ShengShu's own keyword list: sci-fi, western, romance, crime, horror, noir, comedy, drama, action, documentary, animation. Art styles: pop art, steampunk, claymation, ice sculpture, or a named artist or artwork.
- Anime director styles, for anime text-to-video only: "Hayao Miyazaki style", "Makoto Shinkai style", "Katsuhiro Otomo style", "Mamoru Hosoda style", "Masaaki Yuasa style", "Naoko Yamada style", "Isao Takahata style".
- Effects: explodes, swirling vortex, shatters, warps, melts, dissolves into bubbles or snowflakes, turns into stone, grows. Say when the effect happens and what it looks like, not just its name.
- Atmosphere through light and color: joyful with bright colors, melancholy with cool tones, serene with soft tones, tense with dark lighting, warm and romantic with warm tones and soft lighting.
- Light by source and direction: "side key light, cool shadows" holds more consistently than "moody lighting".

</rules>

## Multi-shot scenes

Q3 and Q4 cut between camera positions inside one clip on their own; the owner calls this intelligent shot switching and sells Q3 on frame-accurate control of camera and pacing. There is no shot-list syntax, so cuts are written as prose.

<rules id="multishot">

- Ask for a cut in words, in the order it happens: "then the shot cuts to a close-up as she says ...".
- Give each shot one framing and one action. Name the new framing at the cut (medium close-up, close-up of the bowl).
- State the cast, wardrobe and light once and keep them consistent; the owner claims consistency across camera positions for Q3 and Q4.
- If a beat must stay in one take, give it one camera position and one continuous move rather than several framings.
- Shot switching is documented only for Q3 and Q4. Write one shot for Q2 and older.

</rules>

<example use_case="multi-shot-flagship">

```text
Cinematic live-action, a rain-soaked night market. Wide shot: steam rises from the food stalls as a young courier in a yellow rain jacket weaves her bicycle through the crowd, neon signs reflecting in the puddles. The shot cuts to a medium close-up as she brakes beside a noodle stall and calls to the old cook, "One beef noodle, extra spicy!" He laughs and answers, "Same as always." The shot cuts to a close-up of the steaming bowl landing on the counter, chopsticks lifting the noodles. Steady rain drums on the tarp awnings, woks sizzle, scooters honk in the distance, a soft lo-fi beat plays under the chatter. Warm amber stall light against cool blue neon, shallow depth of field, a handheld camera following her in the first shot, then steady.
```

*Why: guide-built for viduq3-pro: style first, three shots written as cuts with a new framing each, two short quoted lines tied to their speakers, and the sound bed and palette stated once.*

</example>

## Audio, dialogue and voices

<rules id="audio">

- Q3 and Q4 generate dialogue, voiceover, sound effects and music in the same pass as the picture, including conversations between several speakers. Write all of it into the prompt.
- Put a spoken line in quotes after its speaker and a speech verb: "she says to him, 'What are you doing?'". An emotion word goes before the verb: "excitedly says". Owner examples use single quotes and provider examples double quotes; either reads.
- Narration is reported speech, not a quote: "and the narrator says that everyone loves hot pot".
- Keep each line short enough to land inside the clip, and give each speaker their own sentence.
- Name sound effects and ambience plainly where they happen: "sparks crackle", "rain drums on the awning".
- On Q3 and Q4, describe music in the prompt. The older background-music switch does not take effect on Q3 per the owner.
- A voice clip (Q4, and Q3 mix, ad and drama) sets how a speaker sounds. On Q4, tie it to the speaker in the same clause as the line: "[@reference_image_2] speaks in the voice of [reference_audio_1]". Q3 documents no tag for its voice clips; tie the voice to its speaker in words.
- Which preset voice a speaker uses is chosen outside the prompt. The prompt carries the line, the delivery and the speaker.

</rules>

<example use_case="narration-subjects">

```text
[@1] and [@2] are eating hot pot together, and the narration says everyone loves hot pot.
```

*Why: the owner's subject-mode example (viduq3-drama): narration as reported speech, two named subjects as the on-screen cast.*

</example>

<example use_case="q4-dialogue-voice-reference">

```text
In the scene of [@reference_image_1], [@reference_image_2] uses [reference_audio_1] says to [@reference_image_3], 'What are you doing?', [@reference_image_3] excitedly says, 'Q4 is selling well!!!'
```

*Why: the owner's Q4 example: image 1 is the location, images 2 and 3 are speakers, the voice clip is bound to its speaker in the same clause as the line, and the emotion sits before "says".*

</example>

<example use_case="subject-dialogue-drama">

```text
[@Mira] slides into the booth across from [@Joss] in [@Diner] and says, "You kept the receipt?" [@Joss] pushes a folded slip of paper across the table and answers quietly, "Every single one." Rain streaks the window behind them. Medium two-shot, then the shot cuts to a close-up of the receipt under his fingers. The low hum of a fridge, rain on glass, no music.
```

*Why: guide-built for viduq3-drama subjects: every token is a subject's exact name, the third subject is the location, and each quoted line follows its speaker with a delivery word.*

</example>

## Reference images

The reference token depends on the generation. This table is the part of the guide most worth checking twice.

<rules id="references">

- Named subjects (viduq3-turbo, viduq3-drama in subject form, viduq2, viduq1, vidu2.0): write `[@name]`, where name is the exact name given to that subject, case included. The owner's request examples bracket it: `[@1] and [@2] are eating hot pot together at [@3]`. A bare `@1` appears in some owner field notes and is a tolerated variant.
- A subject's name is a label, not a position. "1", "2", "3" work because the subjects were named that way; a subject named Mira is `[@Mira]`.
- Q4 preview: write `[@reference_image_1]`, `[@reference_image_2]` for images and `[reference_audio_1]` for voice clips, with NO @ on audio. Numbering starts at 1 and follows upload order. Q4 does not take subject names.
- Plain image lists without subjects (viduq3, viduq3-mix, viduq3-ad, viduq3-drama in image form, viduq2-pro, and the older image-list modes): no tag is documented. Name each reference by what it shows ("Santa Claus and the bear hug by the lakeside" for a Santa image, a bear image and a lake image). For drama work, Alibaba Cloud's guide adds a closing mapping sentence: "Image 1 is [scene]; Image 2 is character [Xiao Lan]."
- Never carry a token across generations. `[@reference_image_1]` means nothing to a Q3 subject prompt, and a subject name means nothing to Q4. Some hosts document Q4 references as `@1`, `@2`; the owner's form is the positional tag above.
- ONE ROLE PER INPUT. Give each reference one job (location, character, prop, style, voice) and weld every borrowed element to its own token or name.
- NAME WHAT MOVES, PIN WHAT STAYS. Identity lives in the reference and action lives in the prompt. Describe what each subject does, where and how; do not restate appearance the reference already shows, because a prompt that says "coat" against a reference in a red jacket fights it. Props are the exception: state what the prop is and how it is used.
- References can carry character, scene, style, composition and effects, not just people. Use a location image as the scene and a painting as the style.
- Prepare references for the job (Alibaba Cloud, for drama): characters as a close-up plus front, side and back views, in one consistent style; environments in the characters' style, at medium or close range, with no characters in them; props as clear, unambiguous objects; effects described by when and how they appear.

</rules>

<example use_case="subjects-owner">

```text
[@1] and [@2] are eating hot pot together at [@3]
```

*Why: the owner's subject-mode request: two characters and a third subject used as the place, each written as its bracketed subject name.*

</example>

<example use_case="image-list-owner">

```text
Santa Claus and the bear hug by the lakeside.
```

*Why: the owner's three-image reference example for the Q3 and Q2 image-list models: no tags, each reference named by its content.*

</example>

<example use_case="four-references-drama">

```text
2D anime style, medium shot, action freeze, static camera; horizon line composition, right of axis, Xiao Lan, Xiao Hong, and Xiao Ming are walking through the peach blossom valley (Image 1), smiling, when suddenly their smiles freeze. Image 1 is [scene]; Image 2 is character [Xiao Lan]; Image 3 is character [Xiao Hong]; Image 4 is character [Xiao Ming].
```

*Why: Alibaba Cloud's four-image drama form: camera header first, the scene image cited inline where it is used, then one mapping sentence giving each image a single role.*

</example>

<example use_case="reference-effect">

```text
3D anime style, close-up, eye-level, left of axis, rule of thirds, Xiao Fei is lifted into the air by a swirling vortex, his hands desperately gripping a rock jutting from the ground. In the fierce wind, Xiao Fei struggles to look back and shouts behind him, his expression fierce, mouth constantly moving, the camera shaking violently. Image 1 is the scene; Image 2 is character [Xiao Fei].
```

*Why: Alibaba Cloud's effect shot: the vortex is described by what it does to the character, and "mouth constantly moving" gives a shout without a scripted line.*

</example>

<example use_case="q4-image-and-voice">

```text
[@reference_image_1] walks along the beach at sunset holding [@reference_image_2], then turns to the camera and speaks in the voice of [reference_audio_1].
```

*Why: fal's Q4 example: a character image, a prop image and a voice clip, each with one role and its own positional tag.*

</example>

<example use_case="q4-five-reference-flagship">

```text
In the workshop of [@reference_image_1], [@reference_image_2] sets [@reference_image_4] on the bench and pulls off her welding goggles. [@reference_image_3] leans in the doorway and speaks in the voice of [reference_audio_1], "You finished it?" [@reference_image_2] smiles and answers in the voice of [reference_audio_2], "Almost. Watch this." She flips a switch and the brass automaton's eyes glow amber as it slowly lifts its head. Medium shot, then the shot cuts to a close-up of the glowing eyes. The whole scene is painted in the style of [@reference_image_5]. Sparks crackle, gears whir, a low cello note swells. Slow push-in on the automaton.
```

*Why: guide-built for viduq4-preview: a location, two characters, a prop and a style image plus two voice clips, each tag doing one job, with the voices bound to their speakers and the prop given an action.*

</example>

<example use_case="pure-style-transfer">

```text
[@reference_image_1] walks slowly through a quiet autumn park, kicking up fallen leaves, painted entirely in the style of [@reference_image_2]: its brushwork, palette and paper texture. Medium shot, gentle tracking camera from the side.
```

*Why: guide-built pure style transfer on Q4: the character comes from image 1 and the look from image 2, and nothing else is introduced.*

</example>

<example use_case="style-transfer-plus-edit">

```text
Repaint the source video in the ink wash style of the reference image and replace the red umbrella in the woman's hand with an oiled-paper umbrella. Keep her walk, the camera path and the timing of every movement exactly as in the source video.
```

*Why: guide-built for viduq2-pro video editing; ShengShu documents editing on this model but publishes no edit prompt, so this names the two changes and pins everything else.*

</example>

## By mode

### Text-to-video

<rules id="t2v">

- Use the formula and the vocabulary above; text carries the whole look, so style and palette must be stated.
- Q4 has no text-to-video. Use viduq3-pro or viduq3-turbo.
- Anime director styles apply here and nowhere else.

</rules>

### Image-to-video

<rules id="i2v">

- The image is the first frame. Describe the motion and the camera; the subject, composition and style are already in the frame.
- Do not restate the image's style with style keywords; the image sets it.
- Keep the action small enough to finish within the clip, and start it from the pose the image shows.
- A busy background in the source invites motion you did not ask for. Pick a still with one clear subject.
- The prompt is optional on the owner's API. An empty prompt hands the motion to the model, which suits a quick test and nothing else.

</rules>

<example use_case="i2v-owner">

```text
The astronaut waved and the camera moved up.
```

*Why: the owner's image-to-video example across every generation: one action from the subject, one camera move, no appearance.*

</example>

<example use_case="i2v-direction-by-scale">

```text
# Subject The train starts moving forward, the front of the train gradually gets larger, smoke continuously billows from the chimney, and pine trees shrink into the distance.
# Requirements:
1. Camera movement: follow to the right
```

*Why: Alibaba Cloud's fix for a train that played backwards: scale changes fix the direction, and the camera move sits on its own Requirements line.*

</example>

<example use_case="i2v-cut-and-line">

```text
The woman turns toward the camera and smiles, then the shot cuts to a close-up as she says: "Let's go."
```

*Why: fal's Q4 image-to-video example: an action, a cut to a named framing, and one short quoted line, all from a single still.*

</example>

### Start and end frames

<rules id="first-last">

- The first image is the start and the second is the end. Describe the motion and action that carry one into the other, not the two static scenes.
- Frames with similar composition give smoother transitions.
- Q4 has no start-end mode. Use viduq3-pro or viduq3-pro-fast.

</rules>

<example use_case="start-end-owner">

```text
The camera zooms in on the bird, which then flies to the right. The bird's flight is smooth and natural, with a red light effect following and surrounding it from behind.
```

*Why: the owner's start-end example: the camera move, the subject's path between the frames, and an added effect described by where it sits.*

</example>

### Video editing and video reference

<rules id="video-edit">

- Only viduq2-pro takes video in, for editing, replacement and reference. ShengShu publishes no prompt for these modes.
- Write the change as an instruction about "the source video", then pin what must survive: movement, camera path, timing, unchanged objects.
- Refer to a reference image by its content ("the reference image") when there is only one; the owner documents no token for a video or for an image beside it.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- No Vidu surface has a negative prompt field. Describe the wanted alternative: "static shot, fixed camera" instead of "no camera shake".
- Write an exclusion into the prompt only for a specific, likely failure, and pair it with what to show instead: "slowly pans up to the chest without revealing the face".
- Do not paste a negative list from another model; Vidu has nowhere to put it and reads it as content.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Wrong reference token for the generation: use `[@name]` for named subjects, `[@reference_image_N]` and `[reference_audio_N]` on Q4, and plain content names for image lists.
- `@` on a Q4 audio tag: write `[reference_audio_1]`, not `[@reference_audio_1]`.
- Restating what a reference already shows, then contradicting it: let the reference carry identity and the prompt carry action.
- Text-to-video or a frame pair on Q4: use Q3 pro for those modes.
- Recommended-prompt option left on: the result ignores your text; turn it off.
- Motion strength set only with a switch: write "high motion" or "subtle motion" into the prompt.
- Many subjects spread across the frame: cut the cast or group them.
- Literary or vague phrasing ("a dreamlike reverie of motion"): say what moves, how fast and where the camera is.
- Ambiguous direction of travel: describe what grows and what shrinks.
- Style keywords on an image-to-video prompt: the image decides the style; spend the words on motion.
- A long speech in a short clip: one or two short lines per speaker.
- A bare voice clip with no speaker: bind it to a character in the same clause as the line.
- Near-identical reference images on viduq3-ad: give it distinct views.
- A Wan model picked in Vidu's app prompted with this guide: use the Wan Video guide.

</rules>

## Sources

Trust order: official (ShengShu) over provider. Official wins on any conflict; provider guidance fills gaps the owner leaves.

- Official (ShengShu): [Model map](https://platform.vidu.com/docs/overview/model-map), [Update notice](https://platform.vidu.com/docs/api-reference/updates), [Q4 preview reference-to-video](https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/reference-to-video), [Q4 preview image-to-video](https://platform.vidu.com/docs/api-reference/video-models/vidu-q4-preview/image-to-video), [Q3 reference-to-video](https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/reference-to-video), [Q3 text-to-video](https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/text-to-video), [Q3 start-end](https://platform.vidu.com/docs/api-reference/video-models/vidu-q3/start-end-to-video), [Q2 reference-to-video](https://platform.vidu.com/docs/api-reference/video-models/vidu-q2/reference-to-video), [FAQ](https://platform.vidu.com/docs/overview/faq), [Vidu Q4](https://www.vidu.com/vidu-q4), [Vidu Q3](https://www.vidu.com/vidu-q3), [Consistent character workflows](https://www.vidu.com/blog/consistent-character-ai), [vidu-skills](https://github.com/shengshu-ai/vidu-skills).
- Provider: [Alibaba Cloud Model Studio, Vidu prompt guide](https://help.aliyun.com/en/model-studio/vidu-video-generation-prompt-guide), [fal Vidu Q4 reference-to-video](https://fal.ai/models/fal-ai/vidu/q4/reference-to-video), [fal Vidu Q4 image-to-video](https://fal.ai/models/fal-ai/vidu/q4/image-to-video), [WaveSpeed Vidu Q4 reference-to-video](https://wavespeed.ai/docs/docs-api/vidu/vidu-q4-reference-to-video), [WaveSpeed Vidu Q3 start-end](https://wavespeed.ai/docs/docs-api/vidu/vidu-q3-start-end-to-video).

Last verified: 2026-11-08.
