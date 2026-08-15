# FLUX 3: structure decision and notation adjudication

Not a scrape. Hand-authored, written 2026-08-07 from the sibling scrapes in this folder. Records why
FLUX 3 became a new video-only guide rather than an update to `flux-2.md`, and the notation calls made
while writing it.

## 1. Why a new guide, and why video only

FLUX 3 was announced 2026-07-23 as a single multimodal flow model covering video, audio, images, and
robot action prediction. That breadth is misleading for this repo's purposes, because the capabilities
ship separately and only one of them has arrived.

The owner's own launch plan lists four staged releases: FLUX 3 Video (video and audio generation and
editing), FLUX-mimic and FLUX 3 Action (partners only), FLUX 3 Image, and FLUX 3 Dev (open weights).
The FLUX 3 announcement says image early access comes "in the following weeks", and the FLUX 3 Video
post confirms the roadmap "further includes FLUX 3 Image for image generation and editing, and FLUX 3
Dev as an open-weight variant."

Two independent checks confirm the image half is not documented:

1. `docs.bfl.ai` ships five video prompting pages (overview, text-to-video, audio and speech,
   image-to-video, camera terms) and no FLUX 3 image prompting page.
2. The FLUX Prompting Guide index page states it "covers prompting for the entire FLUX model family -
   FLUX.1, FLUX.1 Kontext and FLUX.2". FLUX 3 appears in that index only as a link to the video guides.

So there is no FLUX 3 image prompt scheme to write down yet. The guide is `flux-3-video.md`, scheme
`flux-3-video`, and `flux-2.md` keeps the image half unchanged.

The video layer is its own scheme by the repo's usual test. It has modes (`t2v`, `i2v`, `v2v`), a camera
and motion grammar, a four-layer audio and dialogue system, multi-shot cut markers, and keyframe
ordering, none of which exist in the FLUX.2 image scheme. This is the Wan image-versus-video precedent:
a modality that adds a large prompt layer gets its own guide. It also partly inverts FLUX.2 habits, which
is the other half of that test: FLUX.2 teaches hex color pinning and JSON-structured prompts, and neither
is documented for FLUX 3 video. The guide states that explicitly so an agent does not carry them across.

When FLUX 3 Image ships, re-run this decision. It may merge into `flux-2.md`, or need a third guide, and
nothing published so far settles it.

## 2. Owner notation kept, with one ASCII substitution

The owner's timestep format prints en-dashes in both the range and the separator, for example
`0.0–1.5s — locked wide of a still harbor at dawn`. The repo requires ASCII-clean guides, so the guide
prints ASCII hyphens throughout: `0.0-1.5s - locked wide of a still harbor at dawn`.

This is safe. The separator sits in prose consumed by a language model, and nothing else in the format is
load-bearing punctuation. The same substitution was applied to a dash inside the owner's jazz-club audio
example. Every other owner literal is ASCII already, including the shot labels (`SHOT ONE`), the cut
marker (`HARD CUT`), the schema field names, and the bracketed shot timings (`[0.0s-3.5s]`).

Owner forms kept verbatim: the six schema element names (core summary, scene, subject description,
dynamic narrative, audio, style and color), the labeled-field names, `HARD CUT`, and the recurring
guardrail clauses (`no on-screen text, no subtitles`, `no announcer delivery`, `no other speech`).

## 3. Duration and aspect ratio

The owner's camera reference appends `10 seconds, 16:9` to nearly every example phrase, so both appear in
prompt text rather than only in the request body.

Aspect ratio is in scope by the repo's standing rule, since the model reads it from the prompt. Clip
length is treated the same way and for the same reason: the guide says to state it when pacing depends on
it, and reproduces it inside example prompts, but never prints the supported range or ceiling. The
owner's "up to 20 seconds" and the parameter's 5-to-20 range are capability limits, out of scope, and the
first of them would trip the repo's own scope-leak grep.

Everything else in the parameter table is out of scope and absent from the guide: mode names as literal
values, resolution tiers, the audio toggle, safety tolerance, and the draft cache. The draft *workflow*
(preview cheaply, then re-render the approved take at full quality with the same subjects, composition,
and motion) is portable technique and is kept as prose.

## 4. The "quoted line becomes on-screen text" rule is owner-documented

Worth flagging because it reads like an inference and is not one. The audio guide states it directly: "A
quoted line without a visible speaker or a voiceover cue may be treated as text that belongs in the
frame." That is why `no on-screen text, no subtitles` appears in almost every owner dialogue example, and
why the guide carries the rule in three places (the dialogue rules, the typography rules, and the
pitfalls list) rather than once.

## 5. fal is used for craft only, not for facts

fal is an approved provider, and its FLUX 3 article contributes four genuine prompt-craft observations:
naming the format is the highest-leverage word in the prompt; naming a work or idea and stopping often
beats adding detail; a long clip can carry a beginning, a turn, and an end without being asked for a
sequence; and the model's recall of real dates and sequences is reliable enough to lean on.

Its factual claims are stale and were not used. The article was written before general availability
("FLUX 3 is coming soon to fal", "pricing has not been announced") and states 480p and 720p resolutions,
while the owner ships HD and Full HD. Resolution is out of scope anyway, but the staleness is recorded
here so the article is not mistaken for a current reference.

No fal FLUX 3 prompting guide exists under `fal.ai/learn/devs/` as of 2026-08-07; a web search summary
implied one, and both candidate URLs returned 404. WaveSpeed had published nothing on FLUX 3. Re-check
both providers later.

## 6. World knowledge: opposite conclusion from Qwen-Image-3.0

Noted because the two adjudications landed days apart and reach opposite rules, which is correct rather
than inconsistent.

Qwen-Image-3.0's API model cards list Web Search as unsupported, so that guide tells the writer to put
every current fact into the prompt. FLUX 3 Video's owner documentation says the opposite in its own
voice: it "combines world knowledge acquired in pretraining with real-time grounding, making it a
powerful tool for documentaries, and short-form educational content, just from as little as a handful of
words in a short prompt." fal's independent testing corroborates it. So this guide tells the writer to
name the work or era and stop.

Same question, different models, different answers, both taken from the owner's API-facing surface.
