---
guide: "Wan (video)"
prompt_scheme: "wan-video-v2"
models:
  # open weights (Apache 2.0; run locally)
  - { id: "wan2.2-t2v-a14b", access: "open-weights", caps: [text-to-video], tier: "flagship", best_for: "strongest open text-to-video; trained on curated lighting, composition, contrast and color-tone labels, so it answers the full aesthetic stack" }
  - { id: "wan2.2-i2v-a14b", access: "open-weights", caps: [image-to-video], tier: "flagship", best_for: "animating a first frame locally with the same aesthetic control" }
  - { id: "wan2.2-ti2v-5b", access: "open-weights", caps: [text-to-video, image-to-video], tier: "std", best_for: "both modes in one model, small enough for a single consumer GPU; the usual local starting point" }
  - { id: "wan2.2-s2v-14b", access: "open-weights", caps: [speech-to-video], tier: "std", best_for: "lip-synced performance driven by an audio file you supply; the prompt describes visuals only" }
  - { id: "wan2.2-animate-14b", access: "open-weights", caps: [character-animation], tier: "std", best_for: "animating or replacing a character from a driving video; takes no text prompt at all" }
  - { id: "wan2.1-vace-14b", access: "open-weights", caps: [video-edit, reference-to-video], tier: "flagship", best_for: "the open all-in-one editor: masked repainting, outpainting, pose and depth control, reference composition. Wants a DESCRIPTIVE prompt, never an instruction" }
  - { id: "wan2.1-t2v-14b", access: "open-weights", caps: [text-to-video], tier: "base", best_for: "previous open text-to-video generation; silent and single-shot" }
  - { id: "wan2.1-t2v-1.3b", access: "open-weights", caps: [text-to-video], tier: "budget", best_for: "smallest open model; fits modest VRAM and is the common base for community finetunes and LoRAs" }
  - { id: "wan2.1-i2v-14b", access: "open-weights", caps: [image-to-video], tier: "base", best_for: "open image-to-video" }
  - { id: "wan2.1-flf2v-14b", access: "open-weights", caps: [first-last-frame], tier: "base", best_for: "open first-and-last-frame interpolation; trained mainly on Chinese text-video pairs, so prefer a Chinese prompt" }
  # open-weights offshoots (the Wan team, Alibaba Cloud PAI, and ali-vilab); the 2.1 and 5B siblings of each Fun variant follow the same rules
  - { id: "wan2.2-vace-fun-a14b", access: "open-weights", caps: [video-edit, reference-to-video], tier: "flagship", best_for: "the VACE scheme retrained on the Wan 2.2 base, so the open editor is no longer a generation behind. Same DESCRIPTIVE prompt rules as VACE" }
  - { id: "wan2.2-fun-a14b-control", access: "open-weights", caps: [control-to-video], tier: "std", best_for: "pose, depth, canny, MLSD or trajectory control from a control video; the prompt carries appearance ONLY" }
  - { id: "wan2.2-fun-a14b-control-camera", access: "open-weights", caps: [control-to-video], tier: "std", best_for: "camera movement supplied as a trajectory input; write NO camera language in the prompt" }
  - { id: "wan2.2-fun-a14b-inp", access: "open-weights", caps: [image-to-video, first-last-frame], tier: "std", best_for: "start-and-end frame prediction on the Fun pipeline" }
  - { id: "wan-move-14b", access: "open-weights", caps: [motion-control], tier: "std", best_for: "point-level object motion drawn as trajectories on the first frame; the prompt keeps appearance and camera but never the motion" }
  - { id: "wan-dancer-14b", access: "open-weights", caps: [music-to-dance], tier: "std", best_for: "long rhythm-locked dance video driven by a music track; the prompt's job is to name the dance style" }
  - { id: "unianimate-dit", access: "open-weights", caps: [character-animation], tier: "std", best_for: "human image animation from a pose sequence, shipped as a LoRA over Wan 2.1 image-to-video" }
  # hosted
  - { id: "wan3.0-video", access: "closed-weights", caps: [text-to-video, image-to-video, first-last-frame, reference-to-video, document-to-video, native-audio], tier: "flagship", best_for: "one All-in-One model covering text, first-frame, first-and-last-frame and reference modes at once, plus documents and web pages as input, over clips long enough to carry a whole story rather than a beat. Audio is ON by default and there is no negative field. INVITATIONAL PREVIEW, so 2.7 stays the reachable flagship for most work" }
  - { id: "wan2.7-t2v", access: "closed-weights", caps: [text-to-video], tier: "std", best_for: "highest-fidelity cinematic text-to-video with advanced camera control; prompt-faithful motion and shot direction. The practical default while 3.0 is invite-only" }
  - { id: "wan2.7-i2v", access: "closed-weights", caps: [image-to-video], tier: "std", best_for: "cinematic animation from a first frame; also covers first-and-last-frame and continuation in one model" }
  - { id: "wan2.7-r2v", access: "closed-weights", caps: [reference-to-video], tier: "std", best_for: "consistent multi-character scenes from mixed image and video references, with per-character voice timbre" }
  - { id: "wan2.7-videoedit", access: "closed-weights", caps: [video-edit], tier: "std", best_for: "instruction-based editing of an existing video: add, change or remove elements, or restyle the environment. Wants an IMPERATIVE instruction, never a scene description. Still the editing path; 3.0 does not expose one" }
  - { id: "wan2.6-t2v", access: "closed-weights", caps: [text-to-video], tier: "std", best_for: "multi-shot storytelling with synchronized audio; the everyday narrative workhorse" }
  - { id: "wan2.6-i2v", access: "closed-weights", caps: [image-to-video], tier: "std", best_for: "multi-shot animation from a first-frame image with synchronized audio" }
  - { id: "wan2.6-r2v", access: "closed-weights", caps: [reference-to-video], tier: "std", best_for: "single or multi-role reference-to-video that keeps a character's identity across the clip" }
  - { id: "wan2.5-t2v-preview", access: "closed-weights", caps: [text-to-video], tier: "std", best_for: "audio-synced single-shot video when you need native sound but not multi-shot cuts" }
  - { id: "wan2.2-t2v-plus", access: "closed-weights", caps: [text-to-video], tier: "budget", best_for: "silent video with a stable success rate; use when audio is not needed" }
  - { id: "wan2.2-kf2v", access: "closed-weights", caps: [first-last-frame], tier: "budget", best_for: "silent interpolation between a start and an end frame" }
  - { id: "wan2.2-animate-move", access: "closed-weights", caps: [character-animation], tier: "std", best_for: "driving a character image with the motion of a reference video; takes no text prompt" }
  - { id: "wan2.2-animate-mix", access: "closed-weights", caps: [character-animation], tier: "std", best_for: "replacing the character in a video with one from an image; takes no text prompt" }
capabilities: [text-to-video, image-to-video, first-last-frame, reference-to-video, document-to-video, video-edit, speech-to-video, character-animation, control-to-video, motion-control, music-to-dance, multi-shot, native-audio]
prompt:
  languages: ["en", "zh", "mixed"]
  formula: "Subject + Scene + Motion + Aesthetic control + Stylization; add Sound (hosted 2.5+) and timed Shots (hosted 2.6+) as needed. Unchanged on 3.0, where a supplied document or web page carries the CONTENT and the prompt carries the TREATMENT"
  dialogue_and_text: "put spoken lines in quotes inside the sound description; on-screen written text renders only approximately, so do not rely on exact wording. The owner names on-screen text accuracy as a known weak point on 3.0, so this holds on the newest model too"
  length_strategy: "rewards complete, multi-dimension descriptions; terse prompts underperform"
  clip_length: "CHANGED ON 3.0. Earlier models take a duration you pick and the prompt has to fill it. On 3.0 a smart-duration mode reads the prompt and picks the length itself, so write the story you actually want and let the length follow. Do not pad a prompt to fill a slot there"
  auto_expand_behavior: "INVERTED BY ACCESS, and changed again on 3.0. Hosted models rewrite a terse prompt by default. Open-weights models do not expand anything unless prompt extension is switched on, so a terse local prompt stays terse and underperforms. Locally: either turn extension on or write the fully expanded prompt yourself. On 3.0 the owner documents no expansion control at all, so treat expansion as not yours to switch; some hosts add their own enhancer and a deliberate deep-thinking mode for prompts that carry several references"
  negatives: "open-weights models take a real negative prompt and ship a canonical default defect bank; much of the hosted line exposes no negative field, so fold exclusions into the positive prompt there. 3.0 has NO negative field, and the owner's own examples fold the exclusion into the positive text"
  references: "three different token conventions depending on mode (character1 / Image 1 / @Video). VACE uses no tokens at all. 3.0 keeps the Image 1 / Video 1 form and adds Audio 1 for referenced audio. See 'Naming references' and never mix them."
sources:
  official: ["https://github.com/Wan-Video/Wan2.1", "https://github.com/Wan-Video/Wan2.2", "https://github.com/ali-vilab/VACE/blob/main/UserGuide.md", "https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y", "https://github.com/aigc-apps/VideoX-Fun", "https://github.com/ali-vilab/Wan-Move", "https://github.com/ali-vilab/UniAnimate-DiT", "https://huggingface.co/Wan-AI/Wan-Dancer-14B", "https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt", "https://www.alibabacloud.com/blog/model-studio-wan-video-generation-prompts-recipe_602777", "https://www.alibabacloud.com/blog/602776", "https://www.alibabacloud.com/help/en/model-studio/use-video-generation", "https://www.alibabacloud.com/help/en/model-studio/image-to-video-first-and-last-frames-guide", "https://help.aliyun.com/en/model-studio/wan3-video-generation-api-reference", "https://help.aliyun.com/zh/model-studio/wan3-0-video", "https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452"]
  provider: ["https://fal.ai/learn/devs/wan-2-6-prompt-guide-mastering-all-three-generation-modes", "https://fal.ai/learn/devs/wan-26-developer-guide-mastering-next-generation-video-generation", "https://wavespeed.ai/models/alibaba/wan-3.0/reference-to-video"]
last_verified: "2026-08-15"
---

# Wan video: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- Wan is one model family that generates both stills and video. This guide is the video half; for text-to-image and image editing see wan-image.md. The static-composition vocabulary (shot size, angle, lens, light, style) is shared between the two.
- Wan video comes in two access lines that share one grammar: the open-weights models (Wan 2.1 and 2.2, run locally) and the hosted models (Wan 2.2-plus through 3.0). The formula, the aesthetic vocabulary, and the camera language are identical across both. What differs is which modes exist and two defaults that invert. Every mode section below states its availability; obey it, because writing for a capability the model does not have is the most common way to waste a generation.
- Write a video prompt as one structured natural-language description built from named components, not a comma-separated tag list.
- On-screen written text renders only approximately. Do not rely on a video prompt to spell exact words on signs or titles.

</rules>

## TL;DR

<template id="quickstart">

{stylization}, {time and light}, {shot size and camera angle}, {camera movement}. {subject with key attributes} {motion described by speed and amplitude} in {scene}. For sound (hosted 2.5+), add: {ambient cue}; a character says "{line}" in a {tone} voice.

</template>

## Models and when to use which

Pick by access first (what can you actually run), then by mode, then by tier. A prompt written for one model in a mode transfers to the others in that mode on the same access line.

Open weights (Apache 2.0, run locally):

- Text-to-video and image-to-video: `wan2.2-ti2v-5b` does both and is small enough for a single consumer GPU, so it is the usual starting point. `wan2.2-t2v-a14b` and `wan2.2-i2v-a14b` are the stronger pair. The Wan 2.1 models are the previous generation and are the common base for community finetunes.
- First-and-last-frame: `wan2.1-flf2v-14b`. Prefer a Chinese prompt here; it was trained mainly on Chinese text-video pairs.
- Editing and control: `wan2.1-vace-14b` is the all-in-one open editor (masked repainting, outpainting, pose and depth control, reference composition). `wan2.2-vace-fun-a14b` retrains the same scheme on the Wan 2.2 base, so the open editor is no longer a generation behind.
- Audio-driven performance: `wan2.2-s2v-14b`. You supply the audio; the prompt describes only what is seen.
- Character animation: `wan2.2-animate-14b`. No text prompt.
- Control adapters and the rest of the offshoot line (Fun-Control, Fun-Control-Camera, Wan-Move, Wan-Dancer): see "Offshoots and control adapters" below. They all subtract from the prompt rather than change it.

Hosted:

- All-in-one: `wan3.0-video` is a single model covering text-to-video, first-frame, first-and-last-frame and reference modes, and it is the only one that reads a document or a web page as input. It is in invitational preview, so treat it as the ceiling rather than the default.
- Text-to-video: `wan2.7-t2v` is the practical default for prompt-faithful motion and camera control; `wan2.6-t2v` is the multi-shot plus audio workhorse; `wan2.5-t2v-preview` gives audio without multi-shot; `wan2.2-t2v-plus` is the silent budget option.
- Image-to-video: `wan2.7-i2v` animates a first frame and also handles first-and-last-frame and continuation; `wan2.6-i2v` adds multi-shot and audio from a single image.
- Reference-to-video: `wan2.7-r2v` carries subjects from several mixed image and video references with per-character voice; `wan2.6-r2v` keeps one or more characters consistent across a clip.
- Video editing: `wan2.7-videoedit` takes an existing video and an instruction. This stays a 2.7 job; 3.0 does not expose an editing mode, whatever the launch material implies.

Capability gates run through the family. Native synchronized audio generated from your prompt arrives at hosted Wan 2.5 and is standard above it. Multi-shot narrative arrives at hosted Wan 2.6. Reference-to-video arrives at hosted Wan 2.6. Documents and web pages as input arrive at hosted Wan 3.0 and exist nowhere else. Everything on the open-weights line is silent and single-shot; the open models reach audio only through speech-to-video, where you hand the model an audio file rather than describe one.

Wan 3.0 is not a superset. It gains the long single generation, the document input, referenced audio and smart duration, but it drops the negative-prompt field the rest of the family exposes, gives up the prompt-extension control, and has no editing mode. It also cannot combine a pinned first or last frame with references, a document or a link: those are alternatives, not layers. Check the mode you need before assuming the newest model covers it.

## How the model reads prompts

- It is formula-driven. The model reads named components (subject, scene, motion, aesthetic control, stylization) better than a loose description. A weak prompt that skips aesthetic control and stylization tends to produce a static camera in an undefined space.
- It rewards detail. Complete, multi-dimension prompts produce better results than short ones. Alibaba's own evaluation of the open models found that results from expanded prompts beat both open and closed competitors; the expansion is doing real work, not decoration.
- Prompt expansion behaves in opposite ways on the two access lines, and this is the single most consequential difference between them. Hosted models rewrite a terse prompt by default, which adds variety but takes control away; write the full structured prompt yourself when the output must match your intent. Open-weights models expand nothing unless you switch extension on, so a terse local prompt is passed through as-is and underperforms. Locally you must either enable extension or supply the fully expanded prompt yourself. There is no default that saves you. Wan 3.0 changes the picture again: the owner documents no expansion control on it at all, so expansion is not a lever you hold there. Some hosts add their own enhancer, and at least one adds a deliberate deep-thinking mode worth switching on when a prompt carries several references at once.
- Clip length is chosen differently on Wan 3.0. Everywhere else you pick a duration and the prompt has to fill it, which is why padding a thin prompt into a long slot produces a model rushing or stalling. Wan 3.0 adds a smart-duration mode that reads the prompt and picks the length itself, so a one-line beat stays short and a real narrative gets room. Write the story you want and let the length follow; do not pad to fill a slot there.
- Camera moves carry meaning. Push-in reads as intimacy or tension, pull-out as scale or isolation, tracking as moving alongside the subject, orbit as the subject being central, a fixed camera as stillness and focus. Choose the move for the feeling, then state it.
- One clip is one continuous shot. A single-shot prompt cannot cut between unrelated scenes; cuts only happen between shots in a multi-shot prompt. Keep a single shot to one continuous action.
- It is bilingual, but not symmetrically. English, Chinese, and mixed-script prompts all work. Chinese is the stronger native language on the open-weights line: every official VACE example prompt is Chinese, Wan 2.1 first-and-last-frame explicitly recommends Chinese, and the VACE guide singles out English users as the ones who need prompt expansion to compensate. Where your pipeline can carry a Chinese prompt, prefer one for the open models.

## Prompt structure

<rules id="structure">

- Basic (quick exploration): Subject + Scene + Motion.
- Advanced (full control): Subject description + Scene description + Motion description + Aesthetic control + Stylization.
- Describe motion by its amplitude, speed, and effect ("swaying violently", "drifting slowly", "shattering the glass"), not just the verb.
- Aesthetic control bundles light source, lighting environment, shot size, camera angle, lens, and camera movement. Lead the prompt with these so the model fixes the look before parsing action.
- State the stylization explicitly as a keyword (for example "cyberpunk", "claymation style", "line art illustration").
- Close on the camera. In the owner's own example corpus, effectively every prompt ends with a shot size, a camera move, or an explicit "fixed camera". Do this even when a control input already constrains the camera.

</rules>

<template id="general">

{stylization}, {time and light source}, {light quality and tone}, {shot size}, {camera angle}, {composition}, {camera movement}. {subject with appearance details} {motion with speed and amplitude} in {detailed scene}.

</template>

<example use_case="single-shot-cinematic">

```text
Backlight, medium shot, sunset, soft light, silhouette, centered composition, orbiting camera movement. A rugged cowboy grips his holster and turns slowly to face the horizon as the camera circles from behind him to the front, the low sun throwing a hard rim of light around his outline.
```

*Why: leads with the full aesthetic stack, names the camera move, then describes the move's arc in plain words so the orbit reveal lands*

</example>

## Cinematic vocabulary

Reference terms the model recognizes. Mix freely; you do not need one from every group.

- Camera movement: push in, pull out, pan left or right, tracking shot, orbiting movement (keep the arc under about 45 degrees to avoid distortion), crane or tilt up, fixed camera, compound movement (several moves in sequence).
- Shot size: extreme close-up, close-up, medium close-up, medium shot, medium full shot, full shot, wide shot, establishing shot.
- Camera angle: eye level, low angle, high angle, over the shoulder, top-down or aerial.
- Lens: wide-angle, ultra-wide fisheye, medium focal length, telephoto or long-focus, tilt-shift.
- Composition: centered, symmetrical, balanced, left-heavy or right-heavy, short-side.
- Light source: daylight, moonlight, firelight, neon, practical light, overcast, clear sky.
- Light quality: soft light, hard light, side light, rim light, backlight, top light, high or low contrast, silhouette.
- Time: dawn, sunrise, daytime, golden hour, sunset, dusk, night.
- Tone: warm tones, cool tones, high or low saturation, mixed tones.
- Stylization: cyberpunk, steampunk, wasteland, claymation, felt, 3D cartoon, pixel or 8-bit, puppet animation, line art illustration, documentary, surreal.

## Naming references

Wan has three different reference-token conventions plus one mode that has none. They are not interchangeable, and using the wrong one silently degrades the result into a guess about who does what.

<rules id="reference-tokens">

- Hosted reference-to-video on Wan 2.6: label roles `character1`, `character2`, matched to the ordinal of each reference input.
- Hosted reference-to-video on Wan 2.7 and 3.0: label inputs `Image 1`, `Video 1`, numbered in upload order.
- Hosted Wan 3.0 adds a third kind: `Audio 1`, `Audio 2` for referenced audio. Each kind is numbered independently, so `Image 1`, `Video 1` and `Audio 1` can all exist in one prompt and each points at a different asset. Count within the kind, never across the whole set.
- Hosted video editing on Wan 2.7: label inputs `@Video` and `@Image1`, written with a space on both sides, and bind each token to the noun it owns ("the sweater in @Image1", "the rider in @Video"). A token can also stand in for the object itself ("a giant @Image1 floats on the sea").
- Open-weights VACE: there are no tokens. Weld each reference to the scene by re-describing its attributes in prose and giving it its own clause and its own role. Do not write "image 1" at VACE; it has no such grammar.
- Some providers expose their own form (for example `@Video1`). Where a host documents a convention, follow the host's.
- ONE ROLE PER INPUT. Whatever the convention, every reference gets exactly one job in the sentence, and every action, line, and borrowed object is bound to the input it came from. With three or more inputs an unattached action is ambiguous, so state the spatial relationship too.

</rules>

## By mode

### Text-to-video

Available on both access lines.

<rules id="t2v">

- Build the prompt from the advanced formula: aesthetic stack first, then subject and motion in the scene.
- Keep the action simple and short enough to read in one continuous shot. Long, multi-step choreography in a single shot fails.

</rules>

<example use_case="t2v-action">

```text
Documentary style, daytime, hard side light, cool tones, full shot, low angle, tracking shot. A street dancer in a loose grey hoodie spins into a fast windmill on wet concrete, droplets flicking outward, the camera tracking low alongside the motion.
```

*Why: one clear continuous action, aesthetic control up front, motion described with speed and physical detail*

</example>

### Image-to-video

Available on both access lines.

<rules id="i2v">

- The one input acts as the first frame. You do not tag it; if useful, anchor the prompt with "continue from the first frame" before the motion description.
- The source image already fixes the subject, scene, and style. Describe only what changes over time: motion and camera movement. Do not re-describe what is already in the frame.
- Prefer motion that plausibly extends from the still (drifting clouds, flowing water, a gentle push toward a subject) over introducing brand-new elements.
- Phrase camera moves as paced trajectories with a clear stopping point ("slowly zooms in and stops on", "starts at eye level and gradually rises until").

</rules>

<example use_case="i2v-landscape">

```text
Gentle camera push toward the mountain peak as clouds drift overhead and the light shifts from morning to golden hour. Serene, cinematic movement.
```

*Why: adds only temporal change (camera path, cloud motion, light shift) and never re-describes the static landscape*

</example>

#### First-and-last-frame

Available on both access lines. Silent on every model that offers it.

<rules id="first-last">

- The two inputs are the first (start) frame and the last (end) frame. You do not tag them; you describe the motion and camera that carry the first into the last.
- Both frames already carry all appearance. Do not re-describe the contents of either one. Describe the path between them: the prompt's only job is to control the transition.
- Write the camera as a three-beat arc: where it starts, how it moves, where it lands on the final frame.
- Name the subject once so identity holds across the interpolation, then spend the rest of the prompt on motion and camera.
- On the open-weights `wan2.1-flf2v-14b`, prefer a Chinese prompt. The model was trained mainly on Chinese text-video pairs and the owner recommends Chinese for best results.
- Drop the sound layer entirely here; no first-and-last-frame model generates audio.

</rules>

<example use_case="first-last-frame">

```text
Realistic style. A curious black kitten looks up at the sky. The camera starts at eye level and gradually rises until it captures the kitten's upturned gaze from above.
```

*Why: leads with a style token, names the subject once, gives one motion beat, then a camera trajectory that resolves on the last frame's top-down composition*

</example>

### Reference-to-video

Hosted, Wan 2.6 and above. For the open-weights equivalent see VACE below, which is prompted differently.

<rules id="r2v">

- Reference-to-video carries a subject's identity (appearance, and on Wan 2.7 voice timbre) from one or more reference inputs into a new scene. Inputs can be images, videos, or a mix.
- Name each reference by the convention its version uses (see "Naming references") and stay consistent throughout the prompt.
- Each reference carries its own appearance and identity; do not re-describe how it looks. Name only what it does, what it holds, and where it is.
- To place one input's subject inside another input's setting, cross-reference them in one clause: "the cat in Image 1 plays in the room from Image 2".
- For dialogue, attach the quoted line to the named reference. Per-character voice timbre rides on a voice reference supplied alongside the input, not on words in the prompt; the prompt's job is only to say who speaks which line.
- Use clean, well-lit references. Performance drops with occlusion, clutter, or low-resolution inputs.
- On Wan 3.0 a third reference kind joins the set: audio. Choose the kind by the job it has to do. Images carry identity, product detail and visual style; video carries motion, pacing, gesture and camera behavior; audio carries ambience, rhythm, voice style and soundtrack direction. That split is WaveSpeed's guidance rather than the owner's, but it is the only published answer to what a referenced audio clip is for.
- Say in the prompt how each reference should shape the result. An attached asset with no stated job is a hint; an asset named in a clause is an instruction.
- Numbering runs within a kind, not across the set. The first image is Image 1 even when a video was attached before it, so count images among images and audio among audio.

</rules>

<example use_case="r2v-single-reference">

```text
Video 1 walks through a rain-slick neon street at night, collar turned up, glancing back once at the camera. Cinematic, shallow depth of field.
```

*Why: one reference named once, given a clear action and a new scene, so the model keeps Video 1's identity while relocating it*

</example>

<example use_case="r2v-three-subject-interaction">

```text
A dance battle between Video 1 and Video 2 in a neon-lit colosseum at night while Video 3 watches from a raised throne; Video 1 leads with a fast spin, Video 2 answers with a slow freeze, and Video 3 leans forward with interest. Dynamic camera, dramatic rim light.
```

*Why: three references, each given a distinct action and a stated spatial relationship, so the model places and animates all three without blending them*

</example>

<example use_case="r2v-cross-reference">

```text
The cat in Image 1 chases the red ball from Image 3 across the living room from Image 2, late-afternoon light through the window. Handheld camera following low.
```

*Why: draws a subject, a setting, and an object from three separate inputs and binds them in one clause by cross-referencing each by index*

</example>

<example use_case="r2v-multi-character-dialogue">

```text
character1 and character2 sit across a small table in a bright diner. character1 leans in and says to character2: "You actually remembered." Immediately character2 sets down the mug and replies: "Of course I did." Soft morning light, static medium two-shot.
```

*Why: the Wan 2.6 role tokens, each line anchored to a distinct action before the speech, and a linking word to keep the two lines from merging*

</example>

<example use_case="r2v-audio-reference">

```text
Video 1 performs on a small club stage, matching the rhythm and mood of Audio 1, while Image 1 watches from a corner booth holding Image 2. Warm stage wash, slow push-in, handheld camera. Video 1 finishes the last bar and says: "That one was for you."
```

*Why: Wan 3.0 only. Three reference kinds in one prompt, each numbered within its own kind and each given a stated job, with the audio reference told what it governs rather than just attached*

</example>

### Document and web-page to video

Hosted, Wan 3.0 only. Hand the model a document, a deck, a spreadsheet or a public web page and it reads the contents and builds video from them. This is the one mode where the prompt is not carrying the facts.

<rules id="doc2v">

- Split the labour: the file carries the CONTENT, the prompt carries the TREATMENT. Do not retype the document's facts into the prompt, and do not expect the file to imply a look.
- Name the artifact you want out. "Brand TVC", "video courseware", "narrated video briefing", "animated data chart" each set a different pace, voice and grade, and the model has no other way to know which one the deck is for.
- Pitch the prompt at the level of control you actually want. The owner publishes both extremes: a one-line creative brief, and a full shot-by-shot direction naming the palette, the opening frame, the camera moves and the closing beat. Longer wins where the output matters, which is the same rule as everywhere else in this guide.
- The aesthetic formula still applies. Stylization, light, shot size and camera movement work exactly as they do in text-to-video; you are directing footage whose script came from elsewhere.
- One source per generation, and a link only works on a page that is public and needs no login. A file and a link cannot both be attached.
- A document cannot be combined with a pinned first or last frame. If you need an exact opening image, that is a different mode.
- Do not lean on the video to reproduce text from the document. On-screen text accuracy is a weakness the owner names on this model; state facts in the narration instead, where the audio carries them.

</rules>

<example use_case="doc2v-directed">

```text
A high-end smart glasses product advertisement with a minimalist, futuristic, and fashionable style. The color palette features black, silver-gray, and ice-blue tones with subtle white light accents and parameter UI graphics. Opening in pure black background, a pair of smart glasses slowly emerges from darkness with refined highlights on the temple edges. The camera captures ultra-close details of lenses, nose pads, hinges, temples, and material textures, showcasing metal and high-performance composite materials. The product then rotates slowly in mid-air with minimalist motion graphics displaying core parameters. Then the camera pulls back as all parts precisely reassemble into the complete product, transitioning to a young model wearing demonstration in minimalist spaces and urban lighting environments.
```

*Why: the owner's own deck-to-advert prompt, and note what it does NOT do: it never restates a spec from the slides, it only directs how the slides should look on screen*

</example>

<example use_case="doc2v-brief">

```text
Turn this brand story into a warm-toned brand TVC. Make it emotionally resonant, the kind of film that makes people want to visit the cafe and stay a while.
```

*Why: the other end of the owner's range, useful when the document is already well structured and you want its own shape back; the two sentences still name an artifact and a grade rather than leaving both open*

</example>

### Multi-shot narratives

Hosted, Wan 2.6 and above. Not available on the open-weights line.

<rules id="multishot">

- Open with a one-line overall description of the theme, mood, or core event to set narrative direction.
- Number each shot and give it a bracketed timestamp, then describe its content: Shot 1 [0-3s], Shot 2 [3-6s], and so on.
- State transitions explicitly inside the shot content ("hard cut", "fixed camera") and keep key elements consistent across shots.
- To force a single shot instead, write "Generate single shot".
- A terse prompt will be elaborated into a multi-shot structure on its own. If you want the shot breakdown to be yours, be specific rather than brief.

</rules>

<template id="multishot">

{one-line overall description}. Shot 1 [0-3s] {scene, subject behavior, camera, light}. Shot 2 [3-6s] {transition cue, next scene, behavior}. Shot 3 [6-10s] {closing beat}.

</template>

<example use_case="multishot-cinematic-with-audio">

```text
A tense detective beat on a rainy night, cinematic and desaturated, the same cool grade held across every shot. Shot 1 [0-3s] Wide establishing shot of a neon-lit street in the rain, a detective in a black trench coat walks fast toward an old building, footsteps splashing and distant sirens. Shot 2 [3-7s] Hard cut to a medium tracking shot from behind as he pushes through the door, rain dripping from his collar, the heavy door creaking shut. Shot 3 [7-11s] Close-up, low-key side light on his face, he mutters in a low, gravelly voice: "Someone was here." Shot 4 [11-15s] Hard cut to an over-the-shoulder shot of a single muddy footprint under his flashlight, a low suspenseful score swelling underneath
```

*Why: the flagship, exercising camera, multi-shot and sound at once; an overall description then four timestamped shots, one camera move and one action each, a consistent grade for continuity, layered diegetic sound, and a single quoted line in Shot 3*

</example>

### Video editing, instruction style

Hosted, `wan2.7-videoedit`. This mode takes an IMPERATIVE INSTRUCTION. Do not write a scene description here; that is VACE's grammar, and the two are not interchangeable.

<rules id="videoedit">

- Write what to change, as a command. Bind every element to its input with the `@Video` and `@Image1` tokens.
- NAME WHAT MOVES, PIN WHAT STAYS. State the change, then state what must not change.
- Use a preservation clause for global edits (color grade, weather, season, background swap) and for removals, because those touch the whole frame: "keep everything else unchanged".
- Omit the preservation clause for a small local add or swap; "Change the cat to a dog" needs no pin.
- Stack a specific pin on top of the generic one. On a global edit, pin the subject's motion explicitly ("the character's movements do not change") as well as adding the catch-all. The catch-all alone will not hold a moving subject still.
- Name both endpoints of a change, not just the target: "from cool tones to warm yellow tones", not "make it warm".
- Chain several operations in one instruction with a comma.
- Evidenced edit types: add, change and remove elements; the same with a reference image supplying the new element; and changing the environment (season, weather, lighting) or the whole scene. The marketing material also claims style, camera and lip-sync editing, but the owner ships no worked examples for those, so treat them as untested.

</rules>

<template id="videoedit">

@Video {specific pin: what must not change}, {the change, stated as from-X to-Y}{, using the {element} in @Image1}, keep everything else unchanged.

</template>

<example use_case="videoedit-local-add">

```text
Add a square piece of dark chocolate to the cup in @Video.
```

*Why: a small local addition, so it needs no preservation clause at all; the token scopes the edit and the instruction stays a single command*

</example>

<example use_case="videoedit-reference-weld">

```text
Make the horse-man in @Video wear the striped sweater from @Image1.
```

*Why: the cleanest weld: each token is bound to the noun it owns, so the model knows which input supplies the subject and which supplies the garment*

</example>

<example use_case="videoedit-global-with-preservation">

```text
@Video The character's movements do not change. Change the overall lighting and color filter of the scene from cool tones to warm yellow tones, preserving the character's skin-tone detail so the character and background stay unified. Keep everything else unchanged.
```

*Why: a global grade change, so it carries the full pin stack: a specific motion pin, both endpoints of the change named, an intent clause explaining why the pin exists, and the generic catch-all*

</example>

### VACE, description style

Open weights, `wan2.1-vace-14b` and `-1.3b`. The open all-in-one editor. It covers reference-to-video, control-driven video-to-video (depth, pose, scribble, optical flow, layout, colorization), masked repainting (inpainting and outpainting), frame and clip extension, and compositions of those.

VACE inverts the editing grammar you would expect. Its owner states the rule outright: use a descriptive prompt, not an instruction.

<rules id="vace">

- DESCRIBE, DO NOT INSTRUCT. Caption the finished video as if it already exists. Never write "swap the rider", "remove the man", "make it cyberpunk".
- The prompt is always required; the control inputs (source video, mask, reference images) are all optional.
- Re-describe the retained content, not only the change. This is the opposite of an image-editing model's convention and it is the mistake most likely to cost you a generation. For masked repainting, describe the whole output frame: both the new content in the masked region and the untouched content around it.
- For control modes (depth, pose, scribble, flow, layout), the source video carries geometry and motion only. The prompt carries all appearance: subject, clothing, colors, background, style, lighting. Write it as though the control video did not exist, but keep the action you describe compatible with the motion the control signal encodes.
- Colorization is the exception among control modes. The grayscale source keeps structure and texture, so there the prompt re-describes the source scene and its real job is to name the colors.
- For reference modes, the reference carries the subject only; its background is stripped. The prompt must supply the entire scene, and must also re-describe the reference subject's salient attributes in words, because there is no token to point with.
- Close on a camera clause. Every official example does, even the control-driven ones where the source already fixes the camera.
- On failure, change the seed and adjust the prompt; that is the owner's stated remedy.

</rules>

<template id="vace">

{style}, {subject with appearance attributes}, {action}, {background and environment}, {light and atmosphere}, {shot size and camera movement}.

</template>

<example use_case="vace-repainting-retained-content">

```text
A vast golden phoenix soars over the city, its feathers blazing like flame, wings spread wide as it beats them slowly and gives off a soft radiance. Below, a bustling downtown at night, crowds looking up in astonishment, dense traffic, red and blue neon flickering against the dark. The camera looks down over the streets, capturing the whole spectacle in a mysterious, magnificent atmosphere.
```

*Why: the phoenix is the new masked content and the city below is retained from the source, yet both are described; an image-editing habit would have written only the phoenix and lost the frame*

</example>

<example use_case="vace-composition-flagship">

```text
Classical oil painting style, warm low sunlight, soft light and low contrast. A man dressed as a superhero stands confidently facing the camera, neatly cropped hair and a light beard, wearing the iconic blue and red suit with a yellow crest on the chest, his cape drifting behind him. On his shoulder perches a bright yellow plush duck with an orange beak and orange feet, wings slightly spread and feet planted apart for balance. His expression is serious and resolute. Pedestrians pass in the background of a broad riverside promenade. Eye-level camera, capturing his full upper body, even bright lighting, fixed camera.
```

*Why: the flagship for the open line; two references composed into one scene, each re-described by its own attributes and given its own clause and spatial role, with no token grammar available, then closed on the camera as every official VACE example is*

</example>

### Speech-to-video

Open weights, `wan2.2-s2v-14b`. The audio rule inverts here.

<rules id="s2v">

- You supply an audio file. The model does not generate sound from your words, so do not write a sound description, a quoted line, or a music cue into the prompt.
- The prompt describes only what is seen: the subject, the setting, the style. The supplied audio drives the performance and the lip sync.
- Keep it short. The reference image and the audio carry most of the information.
- A pose video can be supplied alongside to drive the body motion; where it is, do not describe body motion in the prompt either.

</rules>

<example use_case="s2v-visual-only">

```text
Summer beach vacation style, a white cat wearing sunglasses sits on a surfboard.
```

*Why: purely visual, with no sound or dialogue described, because the audio track supplies all of that; short because the reference image carries the rest*

</example>

### Character animation

Open weights `wan2.2-animate-14b`; hosted `wan2.2-animate-move` and `wan2.2-animate-mix`.

<rules id="animate">

- There is no prompt to write. These models take an image and a driving video; text is not an accepted input, and a prompt box exposed by a host is not reaching the model.
- Animation mode: the image carries the character's appearance and the static background; the driving video carries all the motion.
- Replacement mode: the driving video carries the motion and the background; the image carries only the replacement character's appearance.
- All creative control is in the choice of inputs. If the result is wrong, change the driving clip or the character image, not the words.

</rules>

## Offshoots and control adapters

Alibaba keeps extending the Wan 2.1 and 2.2 bases rather than replacing them. Three groups matter, and all
are open weights: the Wan team's own in-family models, Alibaba Cloud PAI's Fun family (shipped through the
VideoX-Fun pipeline), and ali-vilab's research models. Every one of them keeps the Wan grammar. What they
change is how much of it you are still responsible for.

<rules id="offshoots">

- CONTROL DISPLACES PROMPT. Each offshoot moves one dimension of control out of the prompt and into a control
  input: a pose video, a camera trajectory, a drawn point track, an audio file, a music track.
- When a control input covers X, stop describing X in the prompt. Drop exactly what the control covers, and
  nothing more. Words that duplicate a control signal are wasted at best and fight it at worst, and the
  control signal is the one that wins.
- What remains for the prompt is whatever no control input encodes, which is nearly always appearance and
  style.
- The negative-prompt defect bank does not change. The Fun family ships the same canonical string as base
  Wan, so the negative template above covers the whole open line.
- The offshoots are Chinese-first, more so than the base models. Every shipped example prompt in the Fun
  family, in VACE, and in Wan-Dancer's style files is Chinese.

</rules>

| Offshoot | Control input it adds | What the prompt still carries |
| --- | --- | --- |
| Fun-Control | a pose, depth, canny, MLSD or trajectory video | appearance only |
| Fun-Control-Camera | a camera trajectory | everything except the camera |
| Fun-InP | a start frame and an end frame | the scene |
| VACE-Fun | the VACE control stack, on the Wan 2.2 base | a full descriptive caption, per the VACE rules |
| Wan-Move | drawn point trajectories for object motion | appearance and camera, but never the motion |
| Wan-Dancer | a music track | the dance style |
| Animate, UniAnimate-DiT | a driving pose video | nothing |
| S2V | an audio file | the visuals only |

### The Fun family

Alibaba Cloud PAI ships `Wan2.1-Fun` and `Wan2.2-Fun` in InP, Control and Control-Camera variants, plus
`Wan2.2-VACE-Fun-A14B` and preference-tuned reward LoRAs. The prompt conventions below are read from the
shipped inference scripts, not from the model cards, which do not state them.

<rules id="fun">

- Fun-Control: the control video fixes both the motion and the framing, so write a pure appearance
  description. The shipped pose-driven example describes a woman's clothing, hair, expression and background
  and contains no verb of motion and no camera move at all.
- Fun-Control-Camera: the camera arrives as a trajectory. Write no camera vocabulary whatsoever. No push in,
  no pan, no tracking shot. The shipped example prompt contains none of it.
- Fun-Control with a reference image: the reference supplies identity, the control video supplies motion, and
  the prompt still carries appearance. Same rule.
- VACE-Fun is the VACE scheme retrained on the Wan 2.2 base, so it obeys the VACE rules: describe, do not
  instruct, and re-describe the retained content.

</rules>

<example use_case="fun-control-appearance-only">

```text
A young woman stands on a sunlit coastline in a dark blue vest over a crisp white shirt, a simple white apron stirring in the sea breeze. Her long violet hair lifts in the wind, a delicate black bow tied in it, set against the soft blue sky behind her. Her face is gentle and a little shy, her hands folded in front of her. Behind her the wide glittering sea catches the sun in a warm golden haze.
```

*Why: a pose video is supplying every movement and the framing, so the prompt spends all of itself on appearance and not one word on motion or camera*

</example>

### Wan-Move

Point-level object motion. You draw trajectories on the first frame and the model moves those points.

<rules id="wan-move">

- The trajectories carry the object motion. Do not describe motion in words.
- The camera is NOT controlled here, so the prompt keeps its camera clause. That is the difference from
  Fun-Control, where the control video fixes the framing too. Drop what the control covers, not more.
- The owner recommends turning prompt extension off when the prompt is already a full caption, since
  extension will rewrite it.

</rules>

<example use_case="wan-move-trajectory">

```text
A laptop is placed on a wooden table. The silver laptop is connected to a small grey external hard drive and transfers data through a white USB-C cable. The video is shot with a downward close-up lens.
```

*Why: the drawn trajectories move the cable and the drive, so the prompt names only what things look like and how they are shot, and never what moves*

</example>

### Wan-Dancer

Music-to-dance. A reference image plus a music track produces long, rhythm-locked dance video.

<rules id="wan-dancer">

- The music carries the rhythm and the choreography; the reference image carries appearance. The prompt's
  documented job is to name the dance style, and the owner ships canned style prompts (Chinese classical,
  K-pop, street, tap, Latin).
- Do not write choreography into the prompt. You will not beat the music track.

</rules>

## Sound and dialogue

Hosted, Wan 2.5 and above. On the open-weights line there is no sound generated from a prompt at all; the only audio path is speech-to-video, where you supply the audio file. Do not carry this section across to a local model.

On Wan 3.0 audio is ON by default: a clip comes back with a soundtrack whether or not you asked for one, and silence is something you switch off deliberately. Write the sound layer rather than leaving it, because an unwritten one is invented rather than absent. The owner also names audio texture as a known weak point on that model, so treat generated sound there as a draft rather than a deliverable.

<rules id="sound">

- Sound formula: Subject + Scene + Motion + Sound description, where sound is voice, sound effects, or background music.
- Voice: spoken line in quotes, plus emotion, tone, speed, timbre, and accent. Example phrasing: he says "love is not getting but giving" in a relaxed tone, at a moderate pace, in a clear American-English voice.
- Sound effect: source object, action, and ambient setting, woven inline. Example: a glass falls onto a wooden floor with a sharp "shatter" in a quiet room.
- Background music: name the music and its style ("suspenseful background music", "soft orchestral score").
- To suppress audio, write "No dialogue" or "No background music".

</rules>

<rules id="multi-voice">

- For two or more speakers in one clip, label each character uniquely and consistently; do not switch to pronouns or synonyms.
- Anchor each line to a unique action: describe the action first, then the speech.
- Give each character a distinct voice label (tone plus emotion).
- Use linking words to control order ("immediately", "then") so lines do not merge.

</rules>

<example use_case="dialogue-anchored">

```text
A dim interrogation room, cool light, medium two-shot. The agent slams a hand on the table. The agent, in a raspy low voice: "Where is the truth?" Immediately the assistant, calm and quiet: "Closer than you think."
```

*Why: each line is bound to a distinct action and a labeled voice, and the linking word keeps the two lines from blurring together*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- The open-weights models take a real negative prompt and ship a canonical default defect bank. Reuse it as a stable block rather than rewriting it per prompt.
- Much of the hosted line exposes no negative field. Where there is none, fold the most important exclusion into the positive prompt by describing the desired opposite ("smooth natural motion" rather than "no jitter").
- For video specifically, keep the motion-failure terms near the front. They suppress the frozen-frame result that ruins a clip, which is the failure a still-image defect bank will not catch.
- The VACE guide never mentions negative prompts. Do not assume one is wired up there.
- Wan 3.0 has no negative field at all, so every exclusion has to ride in the positive prompt. The owner's own example does exactly this for sound, closing a prompt by stating what the audio consists of entirely and naming what it therefore excludes. Copy that shape: describe the wanted state, then close the door on the alternative in the same clause.
- Do not carry the default defect bank onto Wan 3.0. It has nowhere to go, and pasting it into the positive prompt spends the model's attention describing artifacts you are trying to avoid.

</rules>

<template id="negative-default">

Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards

</template>

## Pitfalls and anti-patterns

<rules id="avoid">

- Writing an instruction at VACE: it wants a caption of the finished video. Rewrite "remove the man and make it snowy" as a description of the scene as it should end up.
- Writing a description at Wan 2.7 video editing: it wants a command. Rewrite "a cat sits on the sofa in a warm-toned room" as "change the dog to a cat, change the grade from cool to warm, keep everything else unchanged".
- Describing only the change in VACE repainting: the retained region must be described too, or the model loses the frame around your edit.
- Mixing reference-token conventions: `character1`, `Image 1`, and `@Image1` belong to different modes, and VACE has none of them.
- Numbering Wan 3.0 references across kinds: an image attached after a video is still `Image 1`. Counting the whole set in one sequence mislabels every token after the first.
- Assuming Wan 3.0 is a superset: it has no negative field, no prompt-extension control and no editing mode, and it cannot combine a pinned first or last frame with references, a document or a link. Editing is still a 2.7 job.
- Retyping a document's contents into a Wan 3.0 prompt: the file already carries the facts. Spend the prompt on treatment, and expect nothing from the prompt that the file states better.
- Padding a Wan 3.0 prompt to fill a long clip: on smart duration the prompt sets the length, so padding buys a longer, thinner video rather than a fuller one.
- Shipping Wan 3.0 audio unheard: it arrives by default and the owner calls its texture a work in progress. Listen before delivering, or switch it off.
- Writing a sound description for an open-weights model: they are silent. Sound only exists on hosted 2.5 and above, or through speech-to-video where you supply the file.
- Writing a prompt for character animation: those models take no text at all.
- Describing what a control input already covers: with a pose or depth video, drop the motion and the camera; with a camera trajectory, drop the camera; with an audio or music track, drop the sound. The control signal wins and the words are wasted, or worse, they fight it.
- Leaving a terse prompt to a local model: nothing will expand it. Either turn extension on or write the full prompt yourself.
- Re-describing the image in image-to-video: state only motion and camera, never the static content.
- Rapid scene changes inside one shot: a single shot is one continuous take; use a multi-shot prompt for cuts, which means a hosted 2.6 model or above.
- Counting on legible on-screen text: video text renders approximately; if exact words must appear, generate them as a still in Wan image or Qwen-Image and animate or composite separately.
- Long, complex action choreography in one shot: break it into shorter shots or simpler motion.
- Lip-syncing to exact words: precise lip sync to specific words is unreliable outside speech-to-video; write dialogue for tone and timing, not frame-accurate mouth shapes.
- Naming specific real people: usually rejected or inconsistent; describe the appearance instead.
- Tag soup: rewrite disconnected keywords as a structured description with named components.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

- Official (Wan, Alibaba), open weights: [Wan2.1 repository](https://github.com/Wan-Video/Wan2.1), [Wan2.2 repository](https://github.com/Wan-Video/Wan2.2), [VACE user guide](https://github.com/ali-vilab/VACE/blob/main/UserGuide.md).
- Official (Alibaba), offshoots: [VideoX-Fun, the Fun family pipeline from Alibaba Cloud PAI](https://github.com/aigc-apps/VideoX-Fun), [Wan-Move](https://github.com/ali-vilab/Wan-Move), [UniAnimate-DiT](https://github.com/ali-vilab/UniAnimate-DiT), [Wan-Dancer](https://huggingface.co/Wan-AI/Wan-Dancer-14B). The Fun prompt conventions are read from the shipped inference scripts under `examples/wan2.2_fun/`, because the model cards do not state them.
- Official (Wan, Alibaba), hosted: [Wan 2.7 AI video creation guide](https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y), [text-to-video prompt guide](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt), [Wan video prompts recipe](https://www.alibabacloud.com/blog/model-studio-wan-video-generation-prompts-recipe_602777), [Wan 2.6 and 2.5 prompt guide](https://www.alibabacloud.com/blog/602776), [video model comparison](https://www.alibabacloud.com/help/en/model-studio/use-video-generation), [first-and-last-frame guide](https://www.alibabacloud.com/help/en/model-studio/image-to-video-first-and-last-frames-guide).
- Official (Wan, Alibaba), Wan 3.0: [Wan3.0 video generation API reference](https://help.aliyun.com/en/model-studio/wan3-video-generation-api-reference), [wan3.0-video model card](https://help.aliyun.com/zh/model-studio/wan3-0-video), [Wan3.0 launch article](https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452).
- Provider: [fal Wan 2.6 prompt guide (three modes)](https://fal.ai/learn/devs/wan-2-6-prompt-guide-mastering-all-three-generation-modes), [fal Wan 2.6 developer guide](https://fal.ai/learn/devs/wan-26-developer-guide-mastering-next-generation-video-generation), [WaveSpeed Wan 3.0 reference-to-video](https://wavespeed.ai/models/alibaba/wan-3.0/reference-to-video).

Coverage note: the Wan 2.7 creation guide is a single-page app whose Storyboard Control, Character Control and Prompt Recipe sections did not render when scraped. Storyboard control appears to be a multi-panel image input rather than a prompt-text construct, and remains a gap to close rather than a capability to assume. A video-side thinking mode now does exist, exposed by a provider on Wan 3.0 and recommended there for prompts carrying several references; the owner still documents none, on 3.0 or anywhere else in its video docs. Wan 3.0 itself is in invitational preview, so its model card and API reference are the citable surfaces while the launch article describes the product; where the two differ, the reference is what this guide follows. The launch article says the 2.7 editing capability carries forward, but no editing mode appears in the 3.0 API reference, so editing is documented here as a 2.7 job. Reference and asset counts, durations, resolutions, file size and page limits are provider surface and are deliberately absent.

Last verified: 2026-08-15.
