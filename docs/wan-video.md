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
  - { id: "wan3.0-video", access: "closed-weights", caps: [text-to-video, image-to-video, first-last-frame, reference-to-video, document-to-video, video-edit, video-extend, native-audio], tier: "flagship", best_for: "one All-in-One model covering text, first-frame, first-and-last-frame and reference modes at once, plus documents and web pages as input, plus editing and extending a clip you already have, over durations long enough to carry a whole story rather than a beat. Audio is ON by default and there is still no negative field" }
  - { id: "wan3.0-video-prime", access: "closed-weights", caps: [text-to-video, image-to-video, first-last-frame, reference-to-video, document-to-video, video-edit, video-extend, native-audio], tier: "distilled", best_for: "the speed tier of 3.0, taking the same prompt through the same modes and returning it sooner. The owner states its capabilities are aligned with the standard model and publishes no quality comparison, so write the prompt exactly as for wan3.0-video and treat any difference between them as unmeasured rather than absent" }
  - { id: "wan2.7-t2v", access: "closed-weights", caps: [text-to-video], tier: "std", best_for: "highest-fidelity cinematic text-to-video with advanced camera control; prompt-faithful motion and shot direction" }
  - { id: "wan2.7-i2v", access: "closed-weights", caps: [image-to-video], tier: "std", best_for: "cinematic animation from a first frame; also covers first-and-last-frame and continuation in one model" }
  - { id: "wan2.7-r2v", access: "closed-weights", caps: [reference-to-video], tier: "std", best_for: "consistent multi-character scenes from mixed image and video references, with per-character voice timbre" }
  - { id: "wan2.7-videoedit", access: "closed-weights", caps: [video-edit], tier: "std", best_for: "instruction-based editing of an existing video: add, change or remove elements, or restyle the environment. Wants an IMPERATIVE instruction, never a scene description. Uses the @Video token form, which 3.0 does not" }
  - { id: "wan2.6-t2v", access: "closed-weights", caps: [text-to-video], tier: "std", best_for: "multi-shot storytelling with synchronized audio; the everyday narrative workhorse" }
  - { id: "wan2.6-i2v", access: "closed-weights", caps: [image-to-video], tier: "std", best_for: "multi-shot animation from a first-frame image with synchronized audio" }
  - { id: "wan2.6-r2v", access: "closed-weights", caps: [reference-to-video], tier: "std", best_for: "single or multi-role reference-to-video that keeps a character's identity across the clip" }
  - { id: "wan2.5-t2v-preview", access: "closed-weights", caps: [text-to-video], tier: "std", best_for: "audio-synced single-shot video when you need native sound but not multi-shot cuts" }
  - { id: "wan2.2-t2v-plus", access: "closed-weights", caps: [text-to-video], tier: "budget", best_for: "silent video with a stable success rate; use when audio is not needed" }
  - { id: "wan2.2-kf2v", access: "closed-weights", caps: [first-last-frame], tier: "budget", best_for: "silent interpolation between a start and an end frame" }
  - { id: "wan2.2-animate-move", access: "closed-weights", caps: [character-animation], tier: "std", best_for: "driving a character image with the motion of a reference video; takes no text prompt" }
  - { id: "wan2.2-animate-mix", access: "closed-weights", caps: [character-animation], tier: "std", best_for: "replacing the character in a video with one from an image; takes no text prompt" }
capabilities: [text-to-video, image-to-video, first-last-frame, reference-to-video, document-to-video, video-edit, video-extend, speech-to-video, character-animation, control-to-video, motion-control, music-to-dance, multi-shot, native-audio]
prompt:
  languages: ["en", "zh", "mixed"]
  formula: "Subject + Scene + Motion + Aesthetic control + Stylization; add Sound (hosted 2.5+) and timed Shots (hosted 2.6+) as needed. Unchanged on 3.0, where a supplied document or web page carries the CONTENT and the prompt carries the TREATMENT"
  structured_request: "WAN 3.0. The owner's own request formatter organizes a generation prompt into labelled sections: [Core Task], [Plot Summary], [Audio Style], [Camera & Core Constraints], [Negative Prompts]. Core Task and Plot Summary are always present; the rest appear only when there is something to say. Edit instructions stay bare and do not use it"
  dialogue_and_text: "put spoken lines in quotes inside the sound description; on-screen written text renders only approximately, so do not rely on exact wording. The owner names on-screen text accuracy as a known weak point on 3.0, so this holds on the newest model too. On 3.0 name the speaker and the language of every line, and keep each quoted line in the language it is spoken in"
  length_strategy: "rewards complete, multi-dimension descriptions; terse prompts underperform"
  clip_length: "CHANGED ON 3.0. Earlier models take a duration you pick and the prompt has to fill it. On 3.0 a smart-duration mode reads the prompt and picks the length itself, so write the story you actually want and let the length follow. Do not pad a prompt to fill a slot there. The owner's formatter treats total length and frame shape as settings kept out of the prompt, while its sample prompts state them inline; timestamps on beats are content either way"
  auto_expand_behavior: "INVERTED BY ACCESS. Hosted models rewrite a terse prompt by default, 3.0 included, where the owner documents the rewrite as on unless you turn it off. Open-weights models do not expand anything unless prompt extension is switched on, so a terse local prompt stays terse and underperforms. Locally: either turn extension on or write the fully expanded prompt yourself. Some hosts add their own enhancer on top, and a deliberate deep-thinking mode for prompts that carry several references"
  negatives: "open-weights models take a real negative prompt and ship a canonical default defect bank; much of the hosted line exposes no negative field, so fold exclusions into the positive prompt there. 3.0 has NO negative field. The owner's examples fold an exclusion into the positive text, and its request formatter closes the prompt with a labelled [Negative Prompts] list, but only of exclusions actually wanted, never a generic quality or defect pack"
  references: "three different token conventions depending on mode (character1 / Image 1 / @Video). VACE uses no tokens at all. 3.0 keeps the Image 1 / Video 1 form, also accepts Img 1 and the closed-up Image1, and adds Audio 1 for referenced audio; Chinese prompts use 图1 / 视频1 / 音频1. See 'Naming references' and never mix them."
sources:
  official: ["https://github.com/Wan-Video/Wan2.1", "https://github.com/Wan-Video/Wan2.2", "https://github.com/ali-vilab/VACE/blob/main/UserGuide.md", "https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y", "https://github.com/aigc-apps/VideoX-Fun", "https://github.com/ali-vilab/Wan-Move", "https://github.com/ali-vilab/UniAnimate-DiT", "https://huggingface.co/Wan-AI/Wan-Dancer-14B", "https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt", "https://www.alibabacloud.com/blog/model-studio-wan-video-generation-prompts-recipe_602777", "https://www.alibabacloud.com/blog/602776", "https://www.alibabacloud.com/help/en/model-studio/use-video-generation", "https://www.alibabacloud.com/help/en/model-studio/image-to-video-first-and-last-frames-guide", "https://help.aliyun.com/en/model-studio/wan3-video-generation-api-reference", "https://help.aliyun.com/zh/model-studio/wan3-0-video", "https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452", "https://help.aliyun.com/zh/model-studio/wan3-video-generation-guide", "https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-guide"]
  provider: ["https://fal.ai/learn/devs/wan-2-6-prompt-guide-mastering-all-three-generation-modes", "https://fal.ai/learn/devs/wan-26-developer-guide-mastering-next-generation-video-generation", "https://wavespeed.ai/models/alibaba/wan-3.0/reference-to-video"]
last_verified: "2026-09-16"
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

- All-in-one: `wan3.0-video` is a single model covering text-to-video, first-frame, first-and-last-frame and reference modes, and it is the only one that reads a document or a web page as input. `wan3.0-video-prime` is the same model on a speed tier and takes an identical prompt. Neither is gated.
- Text-to-video: `wan2.7-t2v` is the practical default for prompt-faithful motion and camera control; `wan2.6-t2v` is the multi-shot plus audio workhorse; `wan2.5-t2v-preview` gives audio without multi-shot; `wan2.2-t2v-plus` is the silent budget option.
- Image-to-video: `wan2.7-i2v` animates a first frame and also handles first-and-last-frame and continuation; `wan2.6-i2v` adds multi-shot and audio from a single image.
- Reference-to-video: `wan2.7-r2v` carries subjects from several mixed image and video references with per-character voice; `wan2.6-r2v` keeps one or more characters consistent across a clip.
- Video editing: `wan2.7-videoedit` and `wan3.0-video` both take an existing video and an instruction, but they address it differently, and only 3.0 also extends a clip, before its start, after its end or both.

Capability gates run through the family. Native synchronized audio generated from your prompt arrives at hosted Wan 2.5 and is standard above it. Multi-shot narrative arrives at hosted Wan 2.6. Reference-to-video arrives at hosted Wan 2.6. Documents and web pages as input arrive at hosted Wan 3.0 and exist nowhere else. Instruction editing arrives at hosted Wan 2.7 and carries on to 3.0; extending a clip you already have is hosted 3.0 only, though VACE has always done it on the open-weights side. Everything on the open-weights line is silent and single-shot; the open models reach audio only through speech-to-video, where you hand the model an audio file rather than describe one.

Wan 3.0 is close to a superset, but it is not one. It gains the long single generation, the document input, referenced audio, smart duration, instruction editing and clip extension. What it still does not have is the negative-prompt field the rest of the family exposes. It also cannot combine a pinned first or last frame with references, a document or a link: those are alternatives, not layers. The nearest substitute inside reference mode is to ask for a reference image as the opening, a key moment or the closing frame in words, which places it without the pixel-exact hold a pinned frame gives. Check the mode you need before assuming the newest model covers it.

## How the model reads prompts

- It is formula-driven. The model reads named components (subject, scene, motion, aesthetic control, stylization) better than a loose description. A weak prompt that skips aesthetic control and stylization tends to produce a static camera in an undefined space.
- It rewards detail. Complete, multi-dimension prompts produce better results than short ones. Alibaba's own evaluation of the open models found that results from expanded prompts beat both open and closed competitors; the expansion is doing real work, not decoration.
- Prompt expansion behaves in opposite ways on the two access lines, and this is the single most consequential difference between them. Hosted models rewrite a terse prompt by default, which adds variety but takes control away; write the full structured prompt yourself when the output must match your intent. Open-weights models expand nothing unless you switch extension on, so a terse local prompt is passed through as-is and underperforms. Locally you must either enable extension or supply the fully expanded prompt yourself. There is no default that saves you. Wan 3.0 sits on the hosted side of this: the rewrite is on unless you turn it off, so the warning above applies to it in full. Some hosts add their own enhancer, and at least one adds a deliberate deep-thinking mode worth switching on when a prompt carries several references at once.
- Clip length is chosen differently on Wan 3.0. Everywhere else you pick a duration and the prompt has to fill it, which is why padding a thin prompt into a long slot produces a model rushing or stalling. Wan 3.0 adds a smart-duration mode that reads the prompt and picks the length itself, so a one-line beat stays short and a real narrative gets room. Write the story you want and let the length follow; do not pad to fill a slot there.
- Camera moves carry meaning. Push-in reads as intimacy or tension, pull-out as scale or isolation, tracking as moving alongside the subject, orbit as the subject being central, a fixed camera as stillness and focus. Choose the move for the feeling, then state it.
- One clip is one continuous shot. A single-shot prompt cannot cut between unrelated scenes; cuts only happen between shots in a multi-shot prompt. Keep a single shot to one continuous action. Wan 3.0 stretches this: a take declared as continuous ("one continuous take, no cuts") can carry several timestamped beats, because the owner's own long takes are paced that way.
- Wan 3.0 reads long, sectioned prompts. The owner's 30-second samples run to several hundred words and are laid out like a treatment: a synopsis, the visual style and palette, the characters, the camera style, then shot by shot. Short bracketed labels ("[Voice and dialogue]", "[Lighting and scene]") and field names inside a beat ("Camera:", "Scene:", "Action:") keep that length parseable. The owner's request formatter goes one step further, into fixed labelled sections; see "Structured requests on Wan 3.0".
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

### Structured requests on Wan 3.0

Hosted, Wan 3.0 only. The owner publishes a prompt-formatting skill alongside its 3.0 guide, and it organizes every generation request into the same labelled sections before the owner's prompt rewrite sees it. That makes the layout the owner's own answer to how a 3.0 request should be shaped, and it is the most useful shape once references, dialogue and timed shots pile up in one prompt.

<rules id="structured-request">

- Use five labelled sections, in order: [Core Task], [Plot Summary], [Audio Style], [Camera & Core Constraints], [Negative Prompts]. The Chinese labels are 【核心任务】【情节概要】【音频风格】【运镜与核心约束】【负面提示词】.
- [Core Task] is one or two sentences: what kind of video, what it shows, every reference with what it lends, and the global style. Voice references are declared here too ("the host's timbre references Audio 1").
- [Plot Summary] is numbered beats, each saying who does what. Bind every quoted line to its speaker. When you have timestamps, open the beat with them ("Shot 1 0-5 sec:"); when you do not, number the beats and nothing more.
- [Audio Style] covers the dialogue language and texture, live sound, and the mood and rhythm of the music. [Camera & Core Constraints] covers camera style, movement, cutting rhythm and any hard rules. Either one shrinks to a line or drops out when there is nothing to say.
- [Negative Prompts] is a comma-separated list of things you actually want kept out, and it appears only when there are some. Never paste a generic quality or defect pack into it.
- [Core Task] and [Plot Summary] are always present. A simple request can stop after them.
- Keep total length, frame shape, resolution and frame rate out of the sections. The formatter treats them as settings and uses the length only to judge how many events fit. Timestamps on beats are content and stay.
- Write only what you want. The formatter adds no plot, quality boosters, watermark or subtitle rules the request did not ask for, and its output goes on into the owner's prompt rewrite, which is on by default.
- Keep the request in one language, the language of your main instruction. Quoted dialogue, lyrics and on-screen text stay in the language they are delivered in.
- Do not use this layout for an edit. The formatter passes edit instructions through untouched, so write those as the bare commands in "Video editing".

</rules>

<template id="structured-request">

[Core Task]
Generate a {genre or type} {what the video shows}, referencing the {what is adopted} of {subject} in {Image N / Video N / Audio N}. The {character}'s timbre references Audio N. The entire film adopts {global style}.

[Plot Summary]
1. {Shot 1 0-N sec: if timed} {who does what}.
2. {who does what}; using the timbre of Audio N, says: "{line}".

[Audio Style]
{dialogue language and texture}, {live sound}, {music mood and rhythm}.

[Camera & Core Constraints]
{camera style and movement}, {cutting rhythm}, {hard rules}.

[Negative Prompts]
{only exclusions you actually want}

</template>

<example use_case="structured-request-four-references">

```text
[Core Task]
Generate a quiet late-night drama scene in a small radio station, referencing the host's face, hairstyle and clothing in Image 1, the structure and finish of the vintage ribbon microphone in Image 2, and the slow handheld drift of the camera in Video 1. The host's timbre references Audio 1. The entire film adopts a warm, low-key 1970s film look with soft grain.

[Plot Summary]
1. Shot 1 0-5 sec: Wide shot of the empty studio at night; the host sits alone at the desk, the microphone from Image 2 lit by a single desk lamp.
2. Shot 2 5-11 sec: Medium close-up; the host leans toward the microphone and, using the timbre of Audio 1, says in English: "If you're still awake, this one's for you."
3. Shot 3 11-16 sec: Close-up of the host's hand sliding a fader up as a record starts to turn.

[Audio Style]
Soft English speech close to the microphone, the hum of old equipment, and a record crackle leading into a mellow jazz ballad that rises under the last shot.

[Camera & Core Constraints]
Slow handheld drift throughout, following the movement in Video 1; gentle cuts between shots, no fast moves.

[Negative Prompts]
on-screen text, extra people in the studio, modern computer screens
```

*Why: the flagship for the layout. Four references, each lending one named thing; the voice declared once in Core Task and used at the line that needs it; timed beats sized to a few seconds each; the spoken language named; and a negative list holding three specific exclusions rather than a defect pack*

</example>

<example use_case="structured-request-owner-short">

```text
[Core Task]
Generate a hands-on restoration video of an old wooden chair, referencing the woodworker's appearance in Image1 and the old wooden chair's look in Image2, and referencing the hand movements of applying glue and pressing in Video1. The entire film adopts a plain and natural lifestyle documentary style.

[Plot Summary]
1. The woodworker inspects the loose backrest joint.
2. The woodworker applies wood glue following the technique in Video1 and presses the backrest back into position to secure it.
3. The woodworker releases both hands; the backrest remains sturdy.

[Audio Style]
Only retain live sounds such as wood friction and light tool clicks; the person remains naturally silent.
```

*Why: the owner's own filled-in example, and the short end of the layout. No timestamps, so the beats are only numbered; camera and exclusions were never asked for, so those sections are gone; and silence is written as "remains naturally silent" plus the sounds that stay*

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
- Wan 3.0 accepts more than one spelling of the same token. The owner documents `Image 1` and the short `Img 1`, its request formatter writes them closed up (`Image1`, `Video1`, `Audio1`), and Chinese prompts use `图1` (or `图片1`), `视频1`, `音频1`. None of them takes an `@`. Pick one spelling and hold it for the whole prompt.
- On Wan 3.0 a token can stand in the sentence as the subject or the object itself, with no noun around it: "Video 1 holds Image 3, sitting on the chair in Image 4".
- Hosted video editing on Wan 2.7: label inputs `@Video` and `@Image1`, written with a space on both sides, and bind each token to the noun it owns ("the sweater in @Image1", "the rider in @Video"). A token can also stand in for the object itself ("a giant @Image1 floats on the sea").
- Open-weights VACE: there are no tokens. Weld each reference to the scene by re-describing its attributes in prose and giving it its own clause and its own role. Do not write "image 1" at VACE; it has no such grammar.
- Some providers expose their own form (for example `@Video1`). Where a host documents a convention, follow the host's. Unofficial Wan 3.0 pages also teach `@Image1` and `@Audio1`; the owner documents no `@` form for 3.0.
- ONE ROLE PER INPUT. Whatever the convention, every reference gets exactly one job in the sentence, and every action, line, and borrowed object is bound to the input it came from. With three or more inputs an unattached action is ambiguous, so state the spatial relationship too.

</rules>

## By mode

### Text-to-video

Available on both access lines.

<rules id="t2v">

- Build the prompt from the advanced formula: aesthetic stack first, then subject and motion in the scene.
- Keep the action simple and short enough to read in one continuous shot. Long, multi-step choreography in a single shot fails.
- Wan 3.0 is the exception for long takes. Its clips run long enough to hold a sequence of beats in one shot, and the owner's samples do it: declare the take ("single shot", "one continuous take, no cuts"), then give each beat its own timestamp or its own sentence so the model paces them rather than rushing them together.

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
- On Wan 3.0 a pinned first frame is reproduced exactly and is only the opening of a clip that can run far past it, so the describe-only-motion rule above is for short clips. The owner's 3.0 first-frame prompts are timed scripts: they name the frame as `Image 1`, set the opening scene from it once, direct every later beat in full, and tell the model to hold the frame's look throughout ("maintain the ink-wash painting style of Image 1").
- Choose between a pinned frame and a reference on Wan 3.0 by what must be exact. A pinned first or last frame is held exactly; a reference image carries identity, product or style into shots of its own. The two cannot be combined in one request.

</rules>

<example use_case="i2v-landscape">

```text
Gentle camera push toward the mountain peak as clouds drift overhead and the light shifts from morning to golden hour. Serene, cinematic movement.
```

*Why: adds only temporal change (camera path, cloud motion, light shift) and never re-describes the static landscape*

</example>

#### First-and-last-frame

Available on both access lines. Silent on the open-weights models and on `wan2.2-kf2v`; `wan2.7-i2v` and Wan 3.0 generate sound here.

<rules id="first-last">

- The two inputs are the first (start) frame and the last (end) frame. You do not tag them; you describe the motion and camera that carry the first into the last.
- Both frames already carry all appearance. Do not re-describe the contents of either one. Describe the path between them: the prompt's only job is to control the transition.
- Wan 3.0 changes the scale of that path, not the job. With seconds of footage between the frames, the owner's own first-and-last prompt opens with a bracketed statement of the take ("[One continuous take, slow aesthetic camera movement, no cuts]"), sets a global look and the subject once, writes the sound with its entry times, then paces the journey in timestamped beats that end on the last frame's composition.
- Write the camera as a three-beat arc: where it starts, how it moves, where it lands on the final frame.
- Name the subject once so identity holds across the interpolation, then spend the rest of the prompt on motion and camera.
- On the open-weights `wan2.1-flf2v-14b`, prefer a Chinese prompt. The model was trained mainly on Chinese text-video pairs and the owner recommends Chinese for best results.
- Drop the sound layer on the silent models: the open weights and `wan2.2-kf2v`. On `wan2.7-i2v` and Wan 3.0, write it as in any other mode.

</rules>

<example use_case="first-last-frame">

```text
Realistic style. A curious black kitten looks up at the sky. The camera starts at eye level and gradually rises until it captures the kitten's upturned gaze from above.
```

*Why: leads with a style token, names the subject once, gives one motion beat, then a camera trajectory that resolves on the last frame's top-down composition*

</example>

<example use_case="first-last-frame-long-take-30">

```text
[One continuous take, no cuts, slow rising camera, soft watercolor texture throughout.] A lighthouse keeper in a yellow oilskin coat on a rocky island at dawn. Audio: waves breaking on the rocks and gulls throughout; at second 6 a foghorn sounds once, far off; no dialogue, the keeper remains naturally silent.
[0-4s: The watch] The keeper stands at the foot of the lighthouse looking out to sea, coat flapping in the wind, the camera low behind him.
[4-8s: The climb] He climbs the spiral stairs and the camera rises with him past salt-stained windows, the sky outside turning from grey to pale gold.
[8-12s: The view] He steps out onto the gallery at the top and the camera lifts over his shoulder, settling on the wide sunrise over the water that the last frame holds.
```

*Why: Wan 3.0 only, in the shape of the owner's long-take sample: the take declared in brackets, the subject and look set once, sound written with an entry time and an explicit silence, and three timed beats whose camera path ends on the last frame*

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
- On Wan 3.0 a third reference kind joins the set: audio. Choose the kind by the job it has to do. The owner assigns images to a character's appearance and clothing, a product's structure and material, props, scene layout, lighting and style; video to action, camera movement, rhythm and timeline; audio to a speaker's timbre and lines, ambient sound, effects and music, including music or voice that a dance or lip-sync should follow.
- Say in the prompt how each reference should shape the result. An attached asset with no stated job is a hint; an asset named in a clause is an instruction.
- On Wan 3.0 state the adoption scope as well as the job, and what to leave behind: "Scene A references Image 4, adopting spatial layout, architecture and lighting; the person in the image is ignored." Without the exclusion, whatever else is in the picture is a candidate for the shot.
- One entry per subject. Bind each character, prop and scene to its reference separately rather than listing several subjects against one image. A single character sheet defines one character.
- When several references show the same subject, say which view or attribute each one supplies and that together they define ONE entity. Otherwise the model can put two of it in the frame.
- A reference can also become part of the finished clip on Wan 3.0. State where it goes and how the new footage joins it: an image as the opening, a key moment or the closing frame; a video as the opening, middle or closing segment; an audio clip across the whole film or over one stretch. For a grid image, describe the panels in reading order and refer to the whole grid by its one number.
- Write a swap as who does what. The owner's sample says "Seamlessly replace the male character from Image 1 into Video 1's female role", and its formatter restates any replace or substitute request as a performer and an action: "the character from Image 1 performs the action from Video 1".
- To give a character a referenced voice on Wan 3.0, declare it once and use it at the line: "the host's timbre references Audio 1", then "using the timbre of Audio 1, says: ..." The owner's sample form is equally valid: "Extract the voice characteristics from Audio 1, and have the character say the following lines: ..."
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

<example use_case="r2v-tokens-as-subjects-30">

```text
Video 1 holds Image 3, sitting on the chair in Image 4, playing a soothing country folk song, and says: "The sunshine is so nice today." Image 1 holds Image 2 in hand, walks past Video 1, places Image 2 on the table next to Video 1, and says: "That sounds great, can you sing it again?"
```

*Why: the owner's own five-input prompt. The tokens are the nouns, so a person, an instrument, a chair and a handed-over prop each resolve to one input; the handoff of Image 2 is spelled out step by step, and each line belongs to one token*

</example>

<example use_case="r2v-swap-with-voice-30">

```text
Seamlessly replace the male character from Image 1 into Video 1's female role. The character sits by the window, holding a phone to the ear.
[Voice and dialogue] Extract the voice characteristics from Audio 1, and have the character say the following lines: "Really? That sounds great! When are you coming back? I miss you so much."
[Lip-sync and expressions] The generated voice must precisely drive the character's lip movements with natural opening and closing. While speaking, include natural blinking, slight head nodding, and a sense of breathing.
[Lighting and scene] The character's face must naturally receive mixed lighting from warm indoor light and cool neon light from outside the window. Raindrops continuously slide slowly down the window in the background. The character blends naturally with the scene edges, with no cutout artifacts.
[Camera and quality] Long take, camera pushes forward extremely slowly, extremely stable frame, cinematic lighting.
```

*Why: the owner's image-video-audio prompt, trimmed, with its resolution and duration words among the cuts. One kind each doing one job (identity, the role and its action, the voice), then bracketed sections that keep lip sync, lighting integration and camera from blurring into one paragraph*

</example>

### Document and web-page to video

Hosted, Wan 3.0 only. Hand the model a document, a deck, a spreadsheet or a public web page and it reads the contents and builds video from them. This is the one mode where the prompt is not carrying the facts.

<rules id="doc2v">

- Split the labour: the file carries the CONTENT, the prompt carries the TREATMENT. Do not retype the document's facts into the prompt, and do not expect the file to imply a look.
- Data is the exception. When the video must show exact figures from a spreadsheet, the owner's own prompt addresses the cells by coordinate, restates the values it wants plotted ("the B7 cell value $1,580 (January GMV)"), and says outright that labels must match the cells. Tie each chart to its rows, and state what the chart must NOT carry ("labels show only dollar values, no percentages").
- A document can share the request with reference images, which carry the visual style the file cannot. The owner's spreadsheet prompt pairs each segment with its own style source ("visual reference: trend line chart style from reference image 2").
- Name the artifact you want out. "Brand TVC", "video courseware", "narrated video briefing", "animated data chart" each set a different pace, voice and grade, and the model has no other way to know which one the deck is for.
- Pitch the prompt at the level of control you actually want. The owner publishes both extremes: a one-line creative brief, and a full shot-by-shot direction naming the palette, the opening frame, the camera moves and the closing beat. Longer wins where the output matters, which is the same rule as everywhere else in this guide.
- The aesthetic formula still applies. Stylization, light, shot size and camera movement work exactly as they do in text-to-video; you are directing footage whose script came from elsewhere.
- The owner's prompt rewrite cannot be switched off in this mode, so whatever you write is rewritten before generation. Make the treatment explicit enough to survive that: name the artifact, the palette and the pacing rather than leaving them to be inferred.
- One source per generation, and a link only works on a page that is public and needs no login. A file and a link cannot both be attached.
- A document cannot be combined with a pinned first or last frame. If you need an exact opening image, that is a different mode.
- Do not lean on the video to reproduce text from the document. On-screen text accuracy is a weakness the owner names on this model; state facts in the narration instead, where the audio carries them.

</rules>

<example use_case="doc2v-directed">

```text
A high-end smart glasses product advertisement, with an overall minimalist, futuristic, fashion-forward style, restrained lighting, a palette of black, silver-gray, and ice-blue as main tones, with localized soft white light accents and parameter UI graphics. Opening on a pure black background, a pair of smart glasses slowly emerges from the darkness, with refined highlights gliding along the temple edges, the frame silhouette outlined under cold edge lighting. The camera passes in extreme close-up over the lenses, nose pads, hinges, temples, and material details, showcasing the delicate texture of metal and high-performance composite materials. The product then slowly rotates in midair, with minimalist motion graphics displaying core parameter information in sync. The camera then quickly converges, all components precisely returning to assemble into the complete product. It transitions to a young model wearing the glasses, naturally turning their head, raising their hand, walking, and smiling in a minimalist space and urban lighting environment. The ending features the product floating and frozen against a solid-color background, with the camera slowly pushing in toward the brand logo and core slogan. The overall music is minimalist electronic ambiance with precise beats, clean and powerful rhythm.
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
- On Wan 3.0 size each shot at about four to six seconds, the owner's stated storyboard grain, and let a long clip have more shots rather than longer ones.
- The owner's 3.0 samples use several timestamp spellings: `Shot 1 [0-3s]`, `(0:00 - 0:03) Camera: ... Scene: ... Action: ...`, `[0-3s: A water drop]`, `0s - 8s: Prologue`, and plain `Segment 1:`. Any of them works; pick one and hold it for the whole prompt.
- Inside a long beat, name its parts. "Camera:", "Scene:", "Action:", "Detail:" and "Atmosphere:" keep a dense beat from reading as one run-on sentence.
- For a 30-second story on Wan 3.0, write it the way the owner does: a short synopsis, the visual style and palette, the characters, the camera style, then the shot-by-shot. The shared sections are what keep grade and identity steady across a dozen cuts.
- Timestamps do not have to mean cuts on Wan 3.0. Declare "one continuous take, no cuts" first and the same timed beats pace a single shot instead.

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

Hosted, `wan2.7-videoedit` and `wan3.0-video`. This mode takes an IMPERATIVE INSTRUCTION. Do not write a scene description here; that is VACE's grammar, and the two are not interchangeable.

The two versions address the clip differently. 2.7 binds every element with the `@Video` and `@Image1` tokens. 3.0 takes the instruction bare when a single video is attached, and uses its own `Video 1` form only when another input has to be told apart, so the tokens below belong to 2.7 alone.

On 3.0 the words also pick the mode. An attached video is a reference until the prompt says otherwise, so an edit must carry an editing verb: "edit the video", "remove", "replace", "change to", "convert". Leave the verb out and the clip is borrowed from rather than changed.

<rules id="videoedit">

- Write what to change, as a command. On 2.7 bind every element to its input with the `@Video` and `@Image1` tokens; on 3.0 address the attached clip directly.
- NAME WHAT MOVES, PIN WHAT STAYS. State the change, then state what must not change.
- Use a preservation clause for global edits (color grade, weather, season, background swap) and for removals, because those touch the whole frame: "keep everything else unchanged".
- Omit the preservation clause for a small local add or swap; "Change the cat to a dog" needs no pin.
- Stack a specific pin on top of the generic one. On a global edit, pin the subject's motion explicitly ("the character's movements do not change") as well as adding the catch-all. The catch-all alone will not hold a moving subject still.
- Name both endpoints of a change, not just the target: "from cool tones to warm yellow tones", not "make it warm".
- Chain several operations in one instruction with a comma.
- Evidenced edit types: add, change and remove elements; the same with one or more reference images supplying the new elements; changing the environment (season, weather, lighting) or the whole scene; converting the whole clip to another style; and, on 3.0, rewriting what a character says. The owner also lists lighting editing on 3.0 with no worked example. Camera editing has no owner example on either version, so treat it as untested.
- To change dialogue on 3.0, quote the new line in full and name who says it: "Edit the video, change the man's dialogue to: ...". The rest of the clip stays as it was.
- With several reference images on 3.0, weld each borrowed item to the person in `Video 1` who receives it, one sentence per item, and say how it should sit ("naturally fitting her head shape").

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

<example use_case="videoedit-restyle-30">

```text
Convert the entire scene to clay style
```

*Why: the owner's whole 3.0 edit prompt, and worth seeing at full length: one clip attached, one imperative, no token and no preservation clause, because a total restyle has nothing left to hold back*

</example>

<example use_case="videoedit-dialogue-30">

```text
Edit the video, change the man's dialogue to: "The deal is done. Now... we disappear."
```

*Why: the owner's 3.0 dialogue edit. The editing verb selects the mode, the speaker is named, and the replacement line is quoted whole rather than described*

</example>

<example use_case="videoedit-reference-multi-30">

```text
Edit the video: the woman in Video 1 puts on the hat from Image 1, naturally fitting her head shape. The man in Video 1 puts on the hat from Image 2, naturally fitting his head shape. The man's russet-brown shirt is replaced with the blue washed loose denim shirt from Image 3, with the collar open and sleeves rolled up to the forearms. The movements, other clothing, and the rest of the scene remain unchanged.
```

*Why: the owner's four-input 3.0 edit. Each borrowed item gets its own sentence welded to one person in Video 1, the shirt change names both endpoints, and the closing pin holds motion and everything else in place*

</example>

### Video extension

Hosted, Wan 3.0. Hand the model a clip and it generates new footage after its end, before its start, or on both sides at once. VACE has done clip extension on the open-weights side all along; this is the hosted line's version, and the prompt is what selects it.

<rules id="videoextend">

- Say that you are extending. The mode is chosen by the words, not by the attachment: without an extension word ("extend", "continue") the clip is read as a reference for a new video instead.
- Name the source as `Video 1` and give the direction in the owner's words, knowing what they mean. "Extend backward" continues AFTER the last frame. "Extend forward" builds what comes BEFORE the first frame and ends on it. That is the owner's Chinese sense (向后延长, 向前延长) carried into its English docs, and it is the opposite of how an English reader takes "forward".
- In an English prompt, add a clause that fixes the side so neither reading can win: "extend Video 1 backward, continuing after its last frame", or "extend Video 1 forward, leading up to its first frame". In a Chinese prompt the direction words are unambiguous on their own.
- To extend both ways, treat the clip as the middle segment and write each side as its own clause with its own content: "Using the video as the middle segment, extend forward by two seconds: ...; using the video as the middle segment, extend backward by three seconds: ...".
- Then direct the new footage like any other shot: what the subject does, where the camera goes, and how the stretch ends, or for a forward extension how it arrives at the clip's opening.
- When several people carry across the join, define them once by label and appearance ("Character A is a male with short dark brown hair wearing a black tailcoat") and direct them by label after that. The owner's forward extension does exactly this.
- Continue the action, do not restate it. The model already holds the clip; spend the prompt on what has not happened yet.
- Let the framing come from the source. An extension inherits the clip's shape, so asking for a different one fights the input instead of reframing it.
- Motivate the camera if you want it to leave the original frame. "The camera follows him to the oven behind" earns the move; a cut with no reason behind it tends to arrive as a jump.
- The clip you attach spends part of the length budget, so plan the extension against what is left rather than against a full-length clip.

</rules>

<template id="videoextend">

Extend Video 1 {backward, continuing after its last frame | forward, leading up to its first frame}, {what the subject does in the new stretch}, {camera behaviour that motivates the move}, {closing beat, or how it meets the clip}.

</template>

<example use_case="videoextend-backward">

```text
Extend Video 1 backward, the baker brings up the brushed bread, puts the brush aside, the camera follows the baker to the oven behind for baking
```

*Why: the owner's own extension prompt, verbatim, and the case the English trap bites: "backward" here means the footage that comes next. The intent verb leads and names the clip, the continuation reads as ordinary shot direction, and the camera move is motivated by the baker's walk*

</example>

<example use_case="videoextend-both-sides">

```text
Using the video as the middle segment, extend forward by two seconds: the camera smoothly follows as the girl slowly walks toward the camera, stops, gently lifts her head, takes a deep breath in the cold air with lips slightly parted; using the video as the middle segment, extend backward by three seconds: the girl finishes rubbing her hands, looks directly at the camera, and breaks into a warm, radiant smile. She slowly raises a gloved hand to catch a gently falling snowflake. The camera slowly pulls back to a medium-long shot, revealing a sunny snowy forest path, golden hour backlighting, lens flare, shallow depth of field, warm and healing atmosphere.
```

*Why: the owner's bidirectional prompt. Each side restates "middle segment" and carries its own length and action; the forward side walks the girl INTO the clip's opening, the backward side carries her on past its end and closes with the look of the whole piece*

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

<rules id="sound-30">

- Wan 3.0. Name the language of every voice, not only its tone: "a young English-speaking villain voice throughout", "Voiceover: English male or female voice, bright and confident". Keep each quoted line in the language it is spoken in, even when the rest of the prompt is in another.
- Time a voice to the second when its entry matters: "Starting at second 8, an ethereal, gentle female voice slowly recites: ...". Pace narration by rate when a voiceover has to fit its segment ("speaking at approximately 2.5 words per second").
- Mix the layers in words. Say whether music runs the whole film and where it sits against the voice ("when voiceover appears, the music does not disappear, volume just slightly lower than the voice"), and tie each sound effect to the on-screen event that triggers it ("a crisp ding when key data pops up").
- Write an ending silence in when you want one: "leaving 1 second of silence after speaking".
- For a clip with people but no speech, say so and say what remains: "the person remains naturally silent", then the sound sources you want kept. That is the owner formatter's wording for a silent performer, and it names what stays as well as what goes.
- A referenced voice is declared once and used at the line; see "Reference-to-video". A referenced music or voice track is also what the owner points to for a dance or lip sync that follows the beat or the speech.

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
- For a longer list of exclusions on Wan 3.0, close the prompt with a labelled section the way the owner's request formatter does: "[Negative Prompts]" followed by a comma-separated list. List only what this video must not contain ("slow motion, tripod shots, lyrical music"). Plain negatives inside a section also work there ("No slow motion, no unnecessary transition effects").
- Do not carry the default defect bank onto Wan 3.0. It has nowhere to go, and pasting it into the positive prompt spends the model's attention describing artifacts you are trying to avoid. The owner's formatter says the same from the other side: it never adds a generic quality or negative pack that the request did not ask for.

</rules>

<template id="negative-default">

Bright tones, overexposed, static, blurred details, subtitles, style, works, paintings, images, static, overall gray, worst quality, low quality, JPEG compression residue, ugly, incomplete, extra fingers, poorly drawn hands, poorly drawn faces, deformed, disfigured, misshapen limbs, fused fingers, still picture, messy background, three legs, many people in the background, walking backwards

</template>

## Pitfalls and anti-patterns

<rules id="avoid">

- Writing an instruction at VACE: it wants a caption of the finished video. Rewrite "remove the man and make it snowy" as a description of the scene as it should end up.
- Writing a description at Wan 2.7 video editing: it wants a command. Rewrite "a cat sits on the sofa in a warm-toned room" as "change the dog to a cat, change the grade from cool to warm, keep everything else unchanged".
- Describing only the change in VACE repainting: the retained region must be described too, or the model loses the frame around your edit.
- Mixing reference-token conventions: `character1`, `Image 1`, and `@Image1` belong to different modes, and VACE has none of them. On Wan 3.0, `Image 1`, `Img 1` and `Image1` are spellings of one convention; choose one per prompt.
- Numbering Wan 3.0 references across kinds: an image attached after a video is still `Image 1`. Counting the whole set in one sequence mislabels every token after the first.
- Assuming Wan 3.0 is a superset: it still has no negative field, and it cannot combine a pinned first or last frame with references, a document or a link. Inside reference mode, ask for a reference image as the opening or closing frame in words instead.
- Carrying the 2.7 `@Video` token into a 3.0 edit, or writing `@Image1` and `@Audio1` in any 3.0 prompt: 3.0 names inputs `Image 1`, `Video 1` and `Audio 1`, so the `@` form belongs to 2.7 editing alone.
- Attaching a clip to Wan 3.0 without an intent word: with no editing verb and no extension word, the clip is read as a reference for a new video. Say "edit the video" to change it, or "extend Video 1 backward" to continue it.
- Reading "extend forward" as English on Wan 3.0: it builds footage BEFORE the clip and ends on its first frame; "extend backward" continues after the last frame. Add a clause naming the side.
- Retyping a prose document into a Wan 3.0 prompt: the file already carries the facts. Spend the prompt on treatment. Spreadsheet data headed for a chart is the exception; there, name the cells and the values to show.
- Borrowing Wan 3.0 features from unofficial guides: saved character profiles called by name and "1080P" as a quality switch in the prompt appear on no owner surface. Carry identity with a reference image, and set resolution where the request sets it.
- Using the 3.0 structured request for an edit: the owner's formatter passes edit instructions through untouched. Write edits as bare commands.
- Padding a Wan 3.0 prompt to fill a long clip: on smart duration the prompt sets the length, so padding buys a longer, thinner video rather than a fuller one.
- Shipping Wan 3.0 audio unheard: it arrives by default and the owner calls its texture a work in progress. Listen before delivering, or switch it off.
- Writing a sound description for an open-weights model: they are silent. Sound only exists on hosted 2.5 and above, or through speech-to-video where you supply the file.
- Writing a prompt for character animation: those models take no text at all.
- Describing what a control input already covers: with a pose or depth video, drop the motion and the camera; with a camera trajectory, drop the camera; with an audio or music track, drop the sound. The control signal wins and the words are wasted, or worse, they fight it.
- Leaving a terse prompt to a local model: nothing will expand it. Either turn extension on or write the full prompt yourself.
- Re-describing the image in image-to-video: state only motion and camera, never the static content.
- Rapid scene changes inside one shot: a single shot is one continuous take; use a multi-shot prompt for cuts, which means a hosted 2.6 model or above.
- Counting on legible on-screen text: video text renders approximately; if exact words must appear, generate them as a still in Wan image or Qwen-Image and animate or composite separately.
- Long, complex action choreography in one shot: break it into shorter shots or simpler motion. On Wan 3.0 a declared continuous take with timestamped beats is the alternative.
- Lip-syncing to exact words: precise lip sync to specific words is unreliable outside speech-to-video; write dialogue for tone and timing, not frame-accurate mouth shapes. Wan 3.0 adds one more route the owner demonstrates, a voice referenced as `Audio 1` driving the speaking character, with no published measure of how exact it is.
- Leaving the spoken language implicit on Wan 3.0: name it for every voice, and keep quoted lines in the language they are delivered in.
- Naming specific real people: usually rejected or inconsistent; describe the appearance instead.
- Tag soup: rewrite disconnected keywords as a structured description with named components.

</rules>

## Sources

Trust order: official beats provider beats community. Official wins on any conflict.

- Official (Wan, Alibaba), open weights: [Wan2.1 repository](https://github.com/Wan-Video/Wan2.1), [Wan2.2 repository](https://github.com/Wan-Video/Wan2.2), [VACE user guide](https://github.com/ali-vilab/VACE/blob/main/UserGuide.md).
- Official (Alibaba), offshoots: [VideoX-Fun, the Fun family pipeline from Alibaba Cloud PAI](https://github.com/aigc-apps/VideoX-Fun), [Wan-Move](https://github.com/ali-vilab/Wan-Move), [UniAnimate-DiT](https://github.com/ali-vilab/UniAnimate-DiT), [Wan-Dancer](https://huggingface.co/Wan-AI/Wan-Dancer-14B). The Fun prompt conventions are read from the shipped inference scripts under `examples/wan2.2_fun/`, because the model cards do not state them.
- Official (Wan, Alibaba), hosted: [Wan 2.7 AI video creation guide](https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aZxe5myC99MelA2WgN7R35y), [text-to-video prompt guide](https://www.alibabacloud.com/help/en/model-studio/text-to-video-prompt), [Wan video prompts recipe](https://www.alibabacloud.com/blog/model-studio-wan-video-generation-prompts-recipe_602777), [Wan 2.6 and 2.5 prompt guide](https://www.alibabacloud.com/blog/602776), [video model comparison](https://www.alibabacloud.com/help/en/model-studio/use-video-generation), [first-and-last-frame guide](https://www.alibabacloud.com/help/en/model-studio/image-to-video-first-and-last-frames-guide).
- Official (Wan, Alibaba), Wan 3.0: [Wan3.0 video generation API reference, Chinese](https://help.aliyun.com/zh/model-studio/wan3-video-generation-api-reference), [the same reference in English](https://help.aliyun.com/en/model-studio/wan3-video-generation-api-reference), [wan3.0-video model card](https://help.aliyun.com/zh/model-studio/wan3-0-video), [wan3.0-video-prime model card](https://help.aliyun.com/zh/model-studio/wan3-0-video-prime), [Wan3.0 launch article](https://www.alibabacloud.com/blog/wan3-0-30-second-ai-video-generation-from-any-input_603452), [Wan3.0 video generation guide, Chinese](https://help.aliyun.com/zh/model-studio/wan3-video-generation-guide), [the same guide in English](https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-guide). The guide links the owner's `wan3-pe` prompt-formatting skill as a download, in a Chinese and an English edition with the same content; the structured-request rules come from it.
- Provider: [fal Wan 2.6 prompt guide (three modes)](https://fal.ai/learn/devs/wan-2-6-prompt-guide-mastering-all-three-generation-modes), [fal Wan 2.6 developer guide](https://fal.ai/learn/devs/wan-26-developer-guide-mastering-next-generation-video-generation), [WaveSpeed Wan 3.0 reference-to-video](https://wavespeed.ai/models/alibaba/wan-3.0/reference-to-video).

Coverage note: the Wan 2.7 creation guide is a single-page app whose Storyboard Control, Character Control and Prompt Recipe sections did not render when scraped. Storyboard control appears to be a multi-panel image input rather than a prompt-text construct, and remains a gap to close rather than a capability to assume. A video-side thinking mode now does exist, exposed by a provider on Wan 3.0 and recommended there for prompts carrying several references; the owner still documents none, on 3.0 or anywhere else in its video docs. Wan 3.0 has left invitational testing, and its reference now documents instruction editing and clip extension beside the original three modes. The launch article said the 2.7 editing capability would carry forward; the reference has since caught up with it, so the earlier reading of that claim as marketing was premature rather than wrong. The Chinese and English references drifted apart for a few weeks and are back in step: both now carry the Prime model, editing, extension and the prompt-rewrite switch. Where they diverge again this guide follows the Chinese one. Two owner surfaces disagree on one point: the `wan3-pe` formatter keeps total length and frame shape out of the prompt as settings, while the usage guide's sample prompts write both inline. The guide teaches the formatter's explicit rule and treats the inline form as tolerated. The extension direction words follow the Chinese meaning in both languages, so English "forward" means before the clip. Unofficial Wan 3.0 prompt guides circulate with invented syntax (an `@Image1` token form, saved character profiles, a "1080P" prompt switch); none of it appears on an owner surface. Reference and asset counts, durations, resolutions, file size and page limits are provider surface and are deliberately absent.

Last verified: 2026-09-16.
