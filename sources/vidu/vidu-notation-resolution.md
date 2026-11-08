# Vidu: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08. Sources: ShengShu's API docs (`docs-*.md`, curl of the `.md` twins listed in
`platform.vidu.com/docs/llms.txt` and the sitemap), the vidu.com Q3 and Q4 pages and owner-hosted blog posts, the
`shengshu-ai/vidu-skills` repo, Alibaba Cloud Model Studio's Vidu prompt guide, and the fal and WaveSpeed endpoint
pages (`providers/`). Two parallel digests read the API pages and the guide-type pages.

## 1. One scheme, no open weights

Every Vidu video model takes one plain-language prompt with no negative field. Generations differ in modes, audio and
the reference token, not in grammar, so Q4 preview through 1.5 share guide `vidu`. No checkpoint is published: no
ShengShu model on Hugging Face, and the `shengshu-ai` GitHub org holds CLI and agent tooling, robotics and
world-model research, and the Vidu S real-time digital-human README (papers and API links, no weights). Vidu S is an
interactive streaming service, not a prompt-to-clip model, and is out of scope. The image models (viduq2, viduq1
image) are out of scope for this pass.

## 2. Source tiers (user decision 2026-11-08)

The owner API docs carry notation, modes and audio but almost no craft. The craft doc is Alibaba Cloud Model Studio's
"Vidu Video Generation Prompt Guide" (help.aliyun.com, last modified 2026-10-10). It carries no ShengShu attribution,
but its formula, style-restatement rule and corgi expansion are a translation of ShengShu's 2024 Chinese prompting
guide (owner first-person text, vidu.studio era), which was reachable only as a WaytoAGI community repost
(`community-waytoagi-vidu-tool-tutorial.md`, provenance check only, not cited). The keyword table, the
"Image 1 is [scene]" mapping sentence and the comic-drama section exist only in Alibaba's version. The user chose to
admit Alibaba Cloud as a provider for this guide: its rules are taught as provider guidance, owner surfaces win on
conflict. The vidu.com blog posts are owner-hosted but generic SEO pieces (bylined, citing third parties); only
Vidu-specific claims were taken from them.

## 3. Reference notation (owner vs owner, owner vs provider)

- Subject mode (`subjects` with a `name`; Q3 turbo, Q3 drama, Q2, Q1, 2.0): every `name` field says "It can be used
  via [@name]" and every request example is bracketed (`[@1] and [@2] are eating hot pot together at [@3]`). Four of
  five prompt-field examples write bare `@1`. Taught: `[@name]` with brackets; bare `@name` recorded as a tolerated
  variant. The token is the subject's name, not a position; the examples only look positional because the subjects
  are named 1, 2 and 3. Name case varies between pages (`[@image1]`, `[@Image1]`); taught: match the name exactly.
- Image-list mode without subjects (viduq3, Q3 mix, ad, drama image form, Q2 pro, Q1, 2.0): no token documented;
  every owner example is untagged prose naming the contents ("Santa Claus and the bear hug by the lakeside."). Taught:
  name each reference by what it shows; Alibaba's trailing mapping sentence ("Image 1 is [scene]; Image 2 is character
  [Xiao Lan]") as the provider form for drama work.
- Q4 preview: no subject invocation ("viduq4-preview does not support the subject invocation method"). The prompt
  field repeats the generic `[@subjects_name]` note, but the only Q4-specific form is the request example:
  `[@reference_image_N]` for images, `[reference_audio_N]` for audio, with no `@` on audio. fal states the same rule.
  WaveSpeed documents `@1`, `@2` by array order; that conflicts with the owner and is recorded as a host variant, not
  taught.
- Audio references on Q3 mix, ad and drama: no in-prompt token documented. Not taught as `[reference_audio_N]`;
  the guide says tie the voice to its speaker in words.
- The owner-hosted Q1 anime blog writes `[@image 1]` (app chips with default names). Not taught; the API name rule
  covers it.

## 4. Structure order (owner vs provider)

Owner 2024 formula, via Alibaba: subject or scene, scene description, environment, art style or medium; restate the
style and atmosphere words across the prompt. Alibaba's comic-drama form leads with style, shot size, camera position,
composition and camera movement, then the action, then the image mapping. Alibaba's optimized examples move camera
movement into a trailing "Requirements" line. Taught: the prose formula as default, camera movement as its own closing
clause; the header-first drama form as a tolerated variant for reference-to-video work. Combined moves ("zoom in +
clockwise orbit") are allowed per Alibaba; the owner-hosted blog's one-move advice is generic and not taught as a rule.

## 5. Behaviour notes

- Prompt rewriting: the owner FAQ says the optimized prompt cannot be returned, so the service rewrites prompts and
  hides the result. The recommended-prompt option replaces the written prompt ("the model will ignore the prompt").
  The Q4 i2v page shows that option defaulting on, which may be a doc error; taught as "check it is off".
- Motion amplitude switch: owner docs say it does not take effect on Q2 and Q3. Motion strength is therefore taught
  as words (Alibaba's motion-intensity keywords).
- Background-music switch: owner docs say it does not take effect on Q3. Q3 generates dialogue, voiceover, sound
  effects and music with the picture (Q3 page), so music is taught as prompt text on Q3 and Q4.
- Spoken output: English, Japanese, Chinese (Q3 page). Nothing published for Q4.
- Voice-ID support is contradictory across owner pages (the subjects page says Q2 pro, Q3 and Q4 do not take voice
  IDs; the Q3 subject pages list the field). Voice choice is outside the prompt either way; not taught.
- The owner CLI labels `viduq2-drama-std` as Wan 3. Recorded as a routing note: a Wan model served in Vidu's app is
  prompted with the Wan Video guide.

## 6. Examples

Owner verbatim: the fog astronaut (t2v), the waving astronaut (i2v), the bird start-end prompt (response variant,
which drops a stray fragment from the request variant), the hot-pot subject prompts, the Santa and bear reference
prompt, and the Q4 dialogue prompt (stray space before a comma removed). Provider verbatim: Alibaba's corgi expansion
(em dash made ASCII), train and forest-walk optimizations, peach-blossom and vortex drama prompts; fal's Q4 cut-and-
dialogue and Q4 voice-reference prompts. Guide-built to owner and provider rules: the Q3 multi-shot flagship, the Q4
five-reference flagship, the subject dialogue scene, pure style transfer, style transfer plus a prop change, and the
Q2 pro video edit (the owner publishes no edit prompt).

## 7. Kept out

Prices, credit counts, durations and resolutions per model, reference and audio counts, character caps (they
disagree across pages: 1500, 2000, 5000, 20000), parameter names, off-peak mode, templates and effects, lip sync,
motion sync, smart multi-frame, extension and upscaling, the industry one-click products, Vidu S.
