---
guide: "HappyHorse (video)"
prompt_scheme: "happyhorse"
models:
  - { id: "happyhorse-1.1-t2v", access: "closed-weights", tier: "flagship", caps: [text-to-video, multi-shot, native-audio, lip-sync], best_for: "cinematic text-to-video with synchronized audio; the default choice for a shot built from words alone" }
  - { id: "happyhorse-1.1-i2v", access: "closed-weights", tier: "flagship", caps: [image-to-video, multi-shot, native-audio, lip-sync], best_for: "animating a still into a shot; the image sets the look, the prompt names only what moves" }
  - { id: "happyhorse-1.1-r2v", access: "closed-weights", tier: "flagship", caps: [reference-to-video, multi-shot, native-audio, lip-sync], best_for: "carrying a character, garment, or prop from reference stills into a new scene with identity held" }
  - { id: "happyhorse-1.0-video-edit", access: "closed-weights", tier: "std", caps: [video-edit], best_for: "restyling or altering an existing clip while its motion and camera path stay locked; the only edit model in the family" }
  - { id: "happyhorse-1.0", access: "closed-weights", tier: "legacy", caps: [text-to-video, image-to-video, reference-to-video], best_for: "the earlier t2v, i2v, and r2v generation; same prompt grammar, weaker motion and consistency" }
capabilities: [text-to-video, image-to-video, reference-to-video, video-edit, multi-shot, native-audio, lip-sync]
prompt:
  languages: ["en", "zh", "ja", "ko", "de", "fr", "any"]
  formula: "subject, one action, setting, time of day, then ONE cinematography cue last; about twenty words unless extra length is carrying real content"
  length_strategy: "short by default; long prompts dilute rather than enrich. Spend words only on camera language, multiple beats, or multiple references, and switch to a timecoded shot list or headed sections when prose runs out of room"
  references: "number reference stills in upload order and cite them in the prompt as bracketed Image 1, Image 2, Image 3; name the object taken from each"
  audio: "generated jointly with the picture in one pass and never toggled off; dialogue in double quotes with speaker and delivery, sound effects named on cue, ambience stated inline"
  multishot: "label each beat and pin it to a time range; one primary action and one camera move per beat"
  negatives: "no host exposes a negative prompt field; fold exclusions into the positive prompt, and only for a risk that is actually likely"
sources:
  official: ["https://www.alibabacloud.com/help/en/model-studio/happyhorse-text-to-video-api-reference", "https://www.alibabacloud.com/help/en/model-studio/happyhorse-image-to-video-api-reference", "https://www.alibabacloud.com/help/en/model-studio/happyhorse-reference-to-video-api-reference", "https://www.alibabacloud.com/help/en/model-studio/happyhorse-video-edit-api-reference", "https://www.alibabacloud.com/blog/alibaba-rolls-out-happyhorse-1-0-in-limited-beta_603068"]
  provider: ["https://fal.ai/learn/tools/prompting-happy-horse", "https://fal.ai/happyhorse-1.0", "https://wavespeed.ai/models/alibaba/happyhorse-1.1/text-to-video"]
  community: []
last_verified: "2026-08-07"
---

# HappyHorse: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, resolution and duration limits, input counts, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- HappyHorse is a video model. There is no HappyHorse image model, so every prompt here describes motion over time, not a still frame.
- HappyHorse is Alibaba's second video line and is NOT Wan. It has no negative prompt field, no prompt-rewriting stage of its own, and no last-frame input. Carrying Wan habits across is the most common way to waste a prompt; Wan has its own guide.
- Write short. About twenty words is the working default, and extra length must be carrying content (a camera move, another beat, another reference), never decoration.
- HappyHorse 1.1 and 1.0 share one prompt grammar. The difference is motion quality, subject consistency, and instruction following, not syntax, so everything here applies to both.

</rules>

## TL;DR

<template id="quickstart">

{subject in one phrase} {does one action} in {setting}, {time of day}, {one atmosphere or camera cue}.

</template>

## Models and when to use which

Pick by what you are handing the model, not by version number. All four modes take the same kind of prompt text.

- Text alone: the t2v model. The whole shot is carried by the sentence.
- One still you want animated: the i2v model. It reads the still as the opening frame, so the prompt should name motion, not appearance.
- Stills whose subjects must survive into a new scene: the r2v model. This is the identity-preserving mode and the only one that uses bracketed image citations.
- An existing clip you want changed: the video-edit model. It preserves the source motion and camera path unless you say otherwise.

<rules id="model-choice">

- Prefer the 1.1 generation for anything motion-heavy or identity-sensitive; it was the release that improved motion dynamics, subject consistency, and instruction following.
- Video editing did not get a 1.1 model. The edit model is still a 1.0 model, so "always use 1.1" is wrong for that one mode; the prompt grammar is unchanged either way.
- Choose i2v over t2v whenever you already have the look you want in a still. Pinning the opening frame is far more reliable than describing the same appearance in words.
- Choose r2v over i2v when the subject must move through a scene you are inventing, rather than continue out of the frame you supplied.

</rules>

## How the model reads prompts

The model generates picture and sound together in a single pass, and it treats your prompt as one shared budget across everything it has to decide. That is the fact behind almost every rule in this guide.

<rules id="reading">

- Long prompts dilute. Padding a working shot with wardrobe, lens, and mood detail measurably degrades human motion: strides shorten, hands lose geometry, faces drift toward a generic average.
- Use exactly ONE strong cinematography cue: a lens, a lighting recipe, or a camera move. Stacking five mostly cancels them out.
- Stacked synonyms do not intensify anything. "Crimson, scarlet, ruby, deep red" is not redder than "crimson". Pick one and move on.
- Put the camera cue LAST. Position carries weight here, and the end of the prompt is where camera direction lands hardest.
- Write plain prose. Comma-separated keyword lists, JSON objects, and weighted parentheses all underperform the same content written as ordinary sentences.
- Any input language is accepted. English prose benchmarked strongest for the picture; write dialogue in whichever language you want spoken.
- A bare director or cinematographer name does almost nothing on its own. Translate the look into technique instead.
- Some hosts offer a prompt-enhancer or rewriter toggle that expands short prompts. Because this model rewards tight prompts, leave it off once you have tuned your wording, or it will reinflate exactly what you trimmed.

</rules>

## Prompt structure

<rules id="structure">

- Lead with the subject and the action. The first sentence does most of the work.
- Follow with setting and time of day, which are cheap and carry a lot of look.
- Close with one cue: atmosphere, lens, or camera move.
- Skip the wardrobe novel and the lighting recipe unless one of them is the point of the shot.
- Prefer concrete physical description over evaluative adjectives: "wet asphalt", "sodium vapor street lamps", "mid-afternoon sun on chrome" all earn their place; "stunning", "epic", "masterpiece" do not.

</rules>

<template id="general">

{subject and at most one wardrobe detail} {does one action} in {setting}, {time of day}. {camera move and lens}. {lighting cue}. {one mood word}.

</template>

<example use_case="twenty-word-default">

```text
A young woman in a red coat walks down a wet city street at night, neon reflections.
```

*Why: Subject, action, setting, time, one atmosphere cue, and then it stops. This is the length the model is happiest at.*

</example>

<example use_case="beat-with-camera">

```text
A 1965 cherry-red Mustang convertible drives along a winding California coastal highway at midday. Steady tracking shot from a parallel car, 35mm telephoto, shallow depth of field. Hard overhead sun flaring off the chrome.
```

*Why: The extra words all buy camera and light, which the model reads cleanly, and the camera cue sits where it gets the most weight.*

</example>

## Prompt length and the two long forms

Length is a decision, not a default. Prose stops scaling before the content does, and past that point you should change the shape of the prompt rather than keep adding sentences.

<rules id="length">

- Default to roughly twenty words. Go longer only when the shot leans on camera language, spans several beats, or cites several references.
- When you do go long, abandon plain prose. Extended paragraphs confuse the model in a way that structured text does not.
- For several beats in sequence, write a shot list and pin every beat to a time range.
- For one continuous take with many axes to specify, split the prompt into headed sections: Subject, Action, Setting, Camera, Lighting, Mood.
- Only use headed sections when you have real content for most of them. Empty headers hurt. With just a subject and a camera move, write twenty words and stop.
- If you are on the fifth or sixth generation of the same shot, the prompt is doing too much. Cut, do not add.

</rules>

<template id="shot-list">

Shot 1 ({framing}, 0-{X}s): {setup beat}
Shot 2 ({framing}, {X}-{Y}s): {action beat}
Shot 3 ({framing}, {Y}-{Z}s): {resolution beat}

</template>

<example use_case="multi-beat-shot-list">

```text
Shot 1 (wide establishing, 0-1s): The camera pulls into a rain-slicked Manhattan side street at night; neon storefront signs glow on both sides. Shallow puddles on the pavement. Empty.

Shot 2 (mid tracking, 1-4s): A young woman in a deep crimson wool peacoat enters frame from the right, hands in pockets, walking briskly away from camera. The camera tracks alongside her at her pace; warm amber backlight skims her shoulder, cool blue ambient fills the shadows.

Shot 3 (slow push-in close, 4-5s): A slow dolly-in onto her face. Her breath is visible in the cold air, calm expression, raindrops in her hair.
```

*Why: The flagship multi-beat form. Every beat is labeled with concrete framing and pinned to a window, so the camera moves land where they were asked for instead of blurring into one motion.*

</example>

<example use_case="continuous-take-sections">

```text
## Subject
A young woman in her late twenties wearing a deep crimson wool peacoat, hands tucked in the coat pockets, breath faintly visible in the cold air.

## Action
Walks briskly down a rain-slicked Manhattan side street at night, her boots clicking on wet asphalt, the camera tracking smoothly alongside her at her own pace.

## Setting
Rain-slicked Manhattan side street, night. Neon storefront signs, shallow puddles, scattered drifting steam from a manhole cover behind her.

## Camera
Steady tracking shot, 35mm telephoto, shallow depth of field, sharp on her face, soft bokeh background.

## Lighting
Warm amber backlight skimming her shoulder, cool blue ambient filling the shadows, neon pink and cyan reflections in the puddles.

## Mood
Cinematic, intimate, contemplative.
```

*Why: One continuous take with six axes specified. Roughly the same word count as a paragraph, but action stays out of the lighting and camera direction stays out of the wardrobe.*

</example>

## Camera and motion

Camera work is this model's strongest axis, and the one place where spending extra words reliably pays.

<rules id="camera">

- Write camera direction in plain English. Steadicam glides, slow dolly-ins, lateral orbits with parallax, helicopter aerials, and locked-off framing under wind all land.
- Keep it to two or three concrete cues even when you are spending words. A paragraph of camera decoration is worse than a clause.
- Name the framing in shot-list labels with standard terms: wide establishing, mid tracking, slow push-in close, low-angle wide, macro close-up.
- Framing is set by your words, but the frame shape is chosen host-side, so spend the prompt on shot size and movement rather than on writing a ratio into the text.
- Watch for camera and subject fighting: ask for an orbit or a rising camera over a fire and the framing pulls back, which reads as the flame shrinking. That is the move you asked for, not a failure of the model.
- Subjects that reward camera attention: vehicles and rigid metal, cloth and hair in wind, fire and embers, mirrors and reflections, and vast landscapes carried on framing alone.

</rules>

<example use_case="camera-led-shot">

```text
A lone hiker crosses a black volcanic ridge under low cloud. The camera orbits laterally around her at walking pace, holding her centered while the ridge line slides through the background with strong parallax.
```

*Why: The camera move is the subject of the shot, so it gets the last and largest share of the words, and the parallax cue tells the model what the move is for.*

</example>

<example use_case="atmospheric-establishing">

```text
A narrow alley at blue hour, thin mist pooling at street level, neon pink and cyan reflections breaking across shallow puddles.
```

*Why: No subject at all. For pure environment shots the atmosphere carries the frame, and adding a person would only split the budget.*

</example>

## Multi-shot sequences

<rules id="multishot">

- Multi-step action written as plain prose collapses. "First X, then Y, then Z" compresses into a single confused motion.
- Give each beat one primary action and one camera move. Two actions in one beat is how beats merge.
- Keep character description in the beat where the character first appears, then refer back plainly. Restating wardrobe every beat spends budget on nothing.
- The model holds character position and appearance across cuts, so you can cut freely rather than staging everything in one take.

</rules>

<example use_case="three-cut-narrative">

```text
Shot 1 (low-angle wide, 0-2s): An old fisherman pushes a wooden skiff off a shingle beach at dawn, mist on the water. The camera holds locked off as he wades in.

Shot 2 (mid, 2-4s): He swings a leg over the gunwale and settles onto the bench, oars rattling in the locks. The camera drifts with the boat.

Shot 3 (wide aerial, 4-6s): The skiff pulls clear of the shallows into flat grey open water. The camera rises steadily behind him.
```

*Why: Three beats, one action and one camera move each, and the fisherman is described once. The rising aerial in the last window reads as a deliberate cut, not a wander.*

</example>

## Audio, dialogue, and lip-sync

Sound is generated jointly with the picture in a single pass, and there is no switch to turn it off. Everything you want to hear has to be in the prompt text, and anything you leave unspecified is invented for you.

<rules id="audio">

- Write dialogue inside double quotes, attached to a named speaker and a delivery: voice low and steady, stuttering and mechanical, breathless.
- Lip-sync is supported for Mandarin, Cantonese, English, Japanese, Korean, German, and French. Write the line in the language you want spoken.
- Name sound effects on the cue that produces them rather than listing them at the end, so the sound lands with the picture that makes it.
- State the ambience once: room tone, weather, crowd, traffic. It is cheap and it stops the model choosing for you.
- Keep spoken lines short. A long speech has to fit the clip, and the model compresses delivery to make it, which flattens the performance.
- Emotion in the voice is directable. Ask for a stutter, a catch in the throat, or a flat affect and the vocal performance follows.

</rules>

<example use_case="dialogue-two-hander">

```text
A sun-drenched Parisian cafe, golden afternoon light spilling through arched windows. A sharp-dressed man in a tailored navy suit sits across from an elegant woman in a flowing crimson dress, half-empty coffee cups between them. He leans forward, voice low and steady: "You knew from the beginning, didn't you? That none of this was real." She holds his gaze without flinching, a ghost of a smile on her lips, slowly stirring her coffee: "Everything was real. That's exactly what makes it so dangerous." Faint clatter of cups and low room chatter under the exchange. Slow push-in across the table, shallow depth of field.
```

*Why: The long-form flagship. Two quoted lines with named delivery, one ambience statement, and a single camera cue at the end; the length is all content, and no adjective pile is doing the work.*

</example>

<example use_case="sound-on-cue">

```text
A blacksmith brings the hammer down on glowing steel, a sharp ringing clang on each strike, sparks scattering across the dark forge floor. Low roar of the coal fire behind him. Handheld medium shot.
```

*Why: The clang is named on the strike that causes it rather than appended as a sound list, so the sync lands.*

</example>

## Reference images

Reference-to-video is the identity-preserving mode, and it is the one place the model expects a specific citation notation.

<rules id="references">

- Number references in upload order and cite them in the prompt as bracketed `[Image 1]`, `[Image 2]`, `[Image 3]`. The numbering must match the order the stills were supplied in.
- ONE ROLE PER INPUT. Weld every borrowed element to its source: name the object you are taking and the image you are taking it from, as in "the woman in the red qipao in `[Image 1]`". A bare citation with no named object leaves the model guessing which part of the still you meant.
- Give each reference exactly one job. Two references competing for the same role, such as two faces for one character, is the fastest way to lose identity.
- Some owner showcase prompts write the citation unbracketed as Image 1. The bracketed form is what the API reference documents, so prefer it.
- Once an element is welded to its source, describe what it DOES rather than what it looks like. Re-describing the garment you already cited spends budget re-deciding something the reference had settled.

</rules>

<example use_case="three-source-reference">

```text
A woman in a red qipao from [Image 1] is first shown in a profile medium shot, highlighting the tailored cut and S-curve of the dress. The camera then switches to a low-angle shot, capturing her unfolding the fan from [Image 2] while the tassel earrings from [Image 3] sway with her head movement. The scene ends with a close-up of her face, focusing on the charm in her eyes as her fingertips touch the fan.
```

*Why: Three sources, three welded roles, and three framings in sequence. Every borrowed element names both the object and its image, and the prompt then spends its remaining words on motion.*

</example>

## By mode

### Text-to-video

<example use_case="text-to-video">

```text
A miniature city built from cardboard and bottle caps comes to life at night. A cardboard train slowly passes through, with small lights dotting the scene and illuminating the way ahead.
```

*Why: A whole world established in two sentences. The scale conceit does the aesthetic work, so no style vocabulary is needed at all.*

</example>

### Image-to-video

<rules id="i2v">

- The still is read as the opening frame, so do NOT re-describe what is already visible in it. Appearance is settled; the prompt is for motion.
- Name what moves, in what direction, and how the camera responds. That is the whole job of an i2v prompt.
- The prompt is optional in this mode, but an empty prompt hands the model the entire performance. Write one.
- Only the first frame is pinned. There is no last-frame input, so do not write a prompt that assumes you have specified where the shot ends.

</rules>

<example use_case="image-to-video">

```text
A boy and the rusty robot stand under the cool glow of the full moon, gently holding hands; a tight close-up captures the boy looking sincere, his lips moving softly to whisper, "we are friends"; the robot's luminous eyes flicker and pulse as it processes the message, responding in a stuttering, mechanical electronic voice, "we... are, we... are friends"; hearing this, the boy's expression lights up with joy, and he reaches out to pat the robot's weathered metal head; the camera pulls back to a wide shot.
```

*Why: Everything named is an event, not an attribute. Beats are separated by semicolons, the vocal performance is directed rather than described, and the camera move closes the prompt.*

</example>

### Reference-to-video

<example use_case="reference-to-video">

```text
The chef from [Image 1] plates the dish shown in [Image 2] onto the marble counter from [Image 3]. She sets the plate down, wipes her hands on her apron, and steps back out of frame. Handheld medium shot, warm window light from the left.
```

*Why: Person, object, and environment each come from a different still and each is welded to it, leaving the prompt free to spend its words on the action and the camera.*

</example>

### Video editing

<rules id="edit">

- NAME WHAT MOVES, PIN WHAT STAYS. State the change, then state explicitly what must survive it: the motion, the camera path, the timing, the unaffected regions.
- The mode preserves the source structure and motion by default, but saying so anyway is what stops an ambitious restyle from drifting.
- Say "the entire video" or "throughout" for global changes, and name the specific element for local ones. An unscoped instruction gets applied unevenly.
- Reference stills are cited the same bracketed way as in reference-to-video, and are how you supply a target style or a replacement garment.
- Editing runs on the 1.0 model. Nothing about the prompt grammar changes, but expect the motion quality of that generation.

</rules>

<example use_case="style-transfer">

```text
Transform the entire video into the Minecraft voxel style based on the visual aesthetic of [Image 1]. Convert all subjects, characters, and the environment into 3D blocks with low-resolution pixelated textures. Ensure the lighting and colors match the blocky world shown in [Image 1]. Throughout this transformation, the original movements, character actions, and camera tracking path must remain 100% unchanged.
```

*Why: Pure style transfer. The restyle is scoped to everything, the style source is cited, and the final sentence pins motion, action, and camera so the transformation cannot drag them along.*

</example>

<example use_case="style-transfer-plus-edit">

```text
Restyle the entire clip as a hand-painted watercolor animation with visible paper grain and soft bleeding edges, and replace the actor's grey hoodie with the embroidered denim jacket from [Image 1]. Keep his face, the handheld drift of the camera, and the timing of every step exactly as they are in the source video.
```

*Why: A global restyle and a targeted replacement in one instruction. Each change names its own scope, the replacement is welded to its reference, and one pin sentence protects identity, camera, and timing together.*

</example>

<example use_case="local-replacement">

```text
Make the horse-headed humanoid character in the video wear the striped sweater from [Image 1]. Leave the rest of the frame, the character's movement, and the camera untouched.
```

*Why: A local edit that names its target precisely rather than saying "the character", and closes by pinning everything outside the change.*

</example>

## On-screen text

<rules id="text">

- Wrap the exact words in double quotes and keep the string to a few words. Short signage, book titles, and simple labels render correctly.
- Long signage and dense paragraphs in frame still hallucinate. If the shot needs a wall of text, plan to compose it afterwards.
- State where the text sits and how it is rendered: embossed, painted, backlit, on a brass easel. Placement and material land more reliably than font names.
- Hold the camera relatively still across text. A fast move over lettering is where character shapes break down.

</rules>

<example use_case="on-screen-text">

```text
A slow dolly past a bookstore window at dusk. A single hardcover stands on a brass easel, its cover embossed in gold with the words "THE STARS BELOW".
```

*Why: A three-word string, quoted exactly, with its material and mount stated. The slow dolly keeps the lettering legible for the whole shot.*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- No host exposes a negative prompt field for this model, so every exclusion has to be written into the positive prompt.
- Most negatives are wasted words. This model does not add camera shake, lens flare, or on-screen text unless asked, so forbidding them spends budget defending against nothing.
- Write an exclusion only when the risk is concrete: "the street is empty, no people in frame" earns its keep because a street scene otherwise tends to populate itself.
- Prefer stating the positive that displaces the problem. "Bare concrete walls" removes the clutter more reliably than "no clutter".
- Never paste a stock negative list from another model. Long exclusion boilerplate is pure dilution here.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Quality-booster pile: "stunning, breathtaking, masterpiece, hyperrealistic, insane detail" drags output toward the model default and costs you the specifics you wrote elsewhere. Delete every one and spend the words on light or lens.
- Padding a working prompt: adding wardrobe, dust, and arm-swing notes to a clean action shot flattens the motion. If a twenty-word version works, stop there.
- Five cinematography cues at once: they cancel out. Pick one lens, one lighting recipe, or one camera move.
- Director name as a style: "Roger Deakins cinematography" alone barely registers. Write the technique instead, and if you keep the name, put the visual translation next to it.
- Multi-step action in plain prose: "first she lifts the kettle, then pours, then sets it down" becomes one confused motion. Move to a timecoded shot list.
- Extreme slow-motion requests: asking for very high frame-rate slow motion does not produce dramatic time dilation. Write it as a normal slow shot and accept what you get.
- Wardrobe detail under fast motion: specific garments drift toward generic ones once a subject starts running. Save wardrobe specifics for static or slow shots, or pin them with a reference image.
- Tag lists, JSON, and weighted parentheses: all underperform the same content as prose. This model is not a tag-driven image model.
- Stacked color synonyms: pick one color word.
- Bare reference citation: `[Image 1]` with no named object leaves the model to choose what to borrow. Always say what you are taking.
- Re-describing a pinned image in i2v: the opening frame already settled appearance, so words spent on it are words taken from motion.
- Wan habits carried over: negative prompt lists, last-frame instructions, and prompt-extension assumptions have nothing to attach to here.
- Empty section headers in the long form: a headed prompt with three blank axes parses worse than twenty words of prose.

</rules>

## Sources

Trust order is official first, then provider, then community; the owner's API reference wins on any conflict, and community material is illustrative only.

- Official (Alibaba): [text-to-video API reference](https://www.alibabacloud.com/help/en/model-studio/happyhorse-text-to-video-api-reference), [image-to-video API reference](https://www.alibabacloud.com/help/en/model-studio/happyhorse-image-to-video-api-reference), [reference-to-video API reference](https://www.alibabacloud.com/help/en/model-studio/happyhorse-reference-to-video-api-reference), [video editing API reference](https://www.alibabacloud.com/help/en/model-studio/happyhorse-video-edit-api-reference), [video generation and editing overview](https://www.alibabacloud.com/help/en/model-studio/video-editing-and-generation/), [HappyHorse 1.0 limited beta announcement](https://www.alibabacloud.com/blog/alibaba-rolls-out-happyhorse-1-0-in-limited-beta_603068).
- Provider: [fal prompting guide](https://fal.ai/learn/tools/prompting-happy-horse), [fal model overview](https://fal.ai/happyhorse-1.0), [WaveSpeed text-to-video model page](https://wavespeed.ai/models/alibaba/happyhorse-1.1/text-to-video).

Coverage note: the owner's API references document the modes, the bracketed image citation, and the mode-by-mode prompt field, but publish no prose prompting guide. The length, camera, and anti-pattern rules above come from fal's benched provider guide, which does not contradict the owner on any documented point. Where an owner showcase prompt ends in a long stack of style tags, that form is recorded as a tolerated variant and is not taught here, because the API reference's own examples and the provider bench agree on tight prose.

Last verified: 2026-08-07.
