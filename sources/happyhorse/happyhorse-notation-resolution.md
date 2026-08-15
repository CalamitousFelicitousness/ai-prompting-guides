# HappyHorse: structure decision and source notes

Not a scrape. Hand-authored 2026-08-07 from the sibling scrapes in this folder. Longer than most of these
because HappyHorse has the worst signal-to-noise ratio of any release covered so far: the authoritative
surface is small and the impersonation layer around it is enormous.

## 1. Its own scheme, not merged into wan-video

`guides/happyhorse.md`, scheme `happyhorse`, covering the 1.1 and 1.0 generations across text-to-video,
image-to-video, reference-to-video, and video editing.

Alibaba now ships two unrelated video lines, and the temptation is to file the second one under the first.
The owner's own "Video generation and editing" overview settles it by listing them side by side as
alternatives for every task, never as tiers of one family. The prompt-relevant differences are structural,
not capability:

| Axis | HappyHorse | Wan |
| --- | --- | --- |
| Negative prompt field | none, on any surface checked | present |
| Audio | always generated, no toggle | toggleable, plus reference audio |
| Frame pinning | first frame only | first frame and first/last frame |
| Reference citation | bracketed `[Image N]` | ImageN/VideoN form |
| Non-image reference input | none | documents, web links |

The negative-prompt row alone is disqualifying. `guides/wan-video.md` teaches a negative-prompt strategy
and a prompt-extension behavior that have nothing to attach to on HappyHorse, and a guide that taught both
schemes would have to contradict itself in its own rules block. That is the repo's split criterion, and it
is the same call already made for Wan image versus Wan video.

Team lineage is consistent with the split but was not used as evidence: HappyHorse comes from the Taotian
Future Life Lab under Alibaba Token Hub, not from the Tongyi group that ships Wan.

## 2. 1.0 and 1.1 merge, with one exception worth stating

Same API shape, same prompt field, same bracketed citation notation, same four modes. The 1.1 release
improved motion dynamics, subject consistency, instruction following, and visual quality. That is capability,
not grammar, so it merges under the Seedream precedent.

The exception the guide states explicitly: **video editing never got a 1.1 model**. The edit model is
`happyhorse-1.0-video-edit`, and the owner still recommends it in the 1.1 era. "Always use 1.1" is therefore
wrong for one of the four modes, which is exactly the kind of thing an agent would otherwise assume from a
version number.

## 3. Owner-versus-provider on prompt length, resolved without overriding the owner

This is the substantive conflict in this release.

fal's benched guide is emphatic that HappyHorse rewards brevity: roughly twenty words, one cinematography
cue, no tag piles, and a measured claim that padding degrades human motion (shorter strides, flatter gait,
hands losing geometry). The owner's showcase blog, meanwhile, prints a text-to-video prompt that ends in
eleven stacked style tags: "Cinematic wide-angle composition, warm golden hour lighting, shallow depth of
field, film grain texture, muted vintage color palette ... 35mm film look."

Resolved as an owner-versus-OWNER question rather than owner-versus-provider, which is what it actually is.
The repo's rule ranks owner surfaces, and the API reference governs. The API reference's own text-to-video
example is short prose with no tag stack at all, and the WaveSpeed and fal examples agree with it. So two of
three owner surfaces and both providers point the same way, and the blog is the outlier.

The blog is a product demonstration, so its trailing tag stack is recorded here as a tolerated variant and
is not taught. What the blog uniquely contributes and IS taught: dialogue written inline in double quotes
with a named delivery, multi-beat prompts separated by semicolons, and the camera cue placed last. Those are
corroborated by the owner's own reference-to-video API example, which is likewise multi-shot.

Consequence for the house rule requiring a long flagship prompt: the flagship here is long because it
carries three quoted lines, an ambience statement, and a camera move, not because it is decorated. The
guide says so in the rationale so the example is not read as licence to pad.

## 4. Notation: bracketed `[Image N]` is canonical

The reference-to-video API reference is explicit, and is the only surface that specifies the notation:

> In the prompt, use "**[Image 1]**" and "**[Image 2]**" to refer to the corresponding reference image in
> the `media` array. The order must be consistent with the order in the `media` array. When using a
> reference, specify the object in the image, such as "the woman in a red qipao in [Image 1]".

Two drifts recorded, neither taught:

- The showcase blog writes it unbracketed as "Image 1" in a video-editing prompt.
- The video-editing API reference's own example avoids the notation entirely and addresses the reference in
  plain language: "the striped sweater **from the image**".

The guide teaches the bracketed form everywhere and notes the unbracketed variant, because a citation that
survives across all four modes is worth more to an agent than per-mode notation trivia. Note that the
second sentence of the owner's rule is the repo's ONE ROLE PER INPUT principle stated by the vendor itself,
which is the first time an owner has spelled it out rather than the guides inferring it.

Mode naming also drifts between owner surfaces: the blog calls the modes T2V, I2V, S2V, V2V, and SV2V, while
the API reference calls them text-to-video, image-to-video, reference-to-video, and video editing. API
reference governs; "subject-to-video" is not used in the guide.

## 5. Language support versus language performance

Not a contradiction, and recorded so it is not later read as one.

The owner's prompt field says input in any language is supported. fal's bench reports that Mandarin
underperformed the same content written as an English sentence. Those are different claims: one is about
what parses, the other about what scores. The guide states both in their own terms, keeps "any input
language is accepted" as the owner fact, and notes English prose benched strongest for the picture while
dialogue should be written in the language you want spoken.

The dialogue carve-out matters because lip-sync covers Mandarin, Cantonese, English, Japanese, Korean,
German, and French. Reading fal's note as "write everything in English" would break lip-sync on purpose.

## 6. The impersonation layer, and why the source bar did the work here

Searching this model returns far more squatter and SEO content than authority. Domains encountered that are
NOT the owner and were not used: happyhorses.io, happy-horse.art, happyhourse.com, happyhorse10.net,
happyhorse-turbo.org, happyhorsemodel.ai, happyhorse.app, plus prompt-guide listicles on imagine.art,
glbgpt.com, cuty.ai, jxp.com, xmk.com and explainx.ai. Several of these present themselves as the official
site or as an official prompt guide.

Two concrete falsehoods in that layer, worth naming because they are the kind of thing that would be
laundered into a guide by a careless pass:

- **"Open source."** At least two of those domains bill HappyHorse as an open-source model. fal, an official
  API partner, states the opposite without hedging: "we can confirm that HappyHorse-1.0 will be closed
  source. It will not be licensable or open source."
- **The official site.** The owner's own announcement links happyhorse.com. None of the hyphenated or
  pluralized lookalikes are it.

Nothing from that layer is cited. This is the clearest case so far of the source-quality bar earning its
place: a community-tier sweep would have produced a guide full of confident invention.

Also discarded: the Qwen Cloud model page for `happyhorse-1.1-t2v` lists "Prefix Completion", "Function
Calling", "Context Cache", "Structured Outputs" and "Web Search" under Features. Those are text-model
template boilerplate rendered onto a video model's page. Treat that page as an availability signal only.

## 7. The Wan misfiling trap was checked and did not fire

Project memory records this trap firing twice: Alibaba files generically titled prompt guides under
`model-studio/` that actually belong to Wan, and links them from unrelated model pages. The video-side
equivalent is `model-studio/text-to-video-prompt`, which a search summary surfaced while looking for
HappyHorse prompt guidance.

Checked before filing: its own title carries the suffix "| Wan video generation". It is Wan's guide, it is
not a HappyHorse source, and it was not scraped into this folder. Each of the four API references in this
folder was separately verified to name its own HappyHorse model in the request body.

Standing conclusion, unchanged: check a Model Studio doc's own "Applies to" or title attribution BEFORE
filing anything from that tree.

## 8. Scope: what was dropped

Out of scope in full, per the standing rule: resolution tiers, duration ranges, frame rate, reference-image
counts, character limits, the watermark and seed parameters, region and endpoint routing, and pricing.

Two judgment calls worth recording:

- **Aspect ratio stayed out**, which departs from the usual treatment. The house rule keeps aspect ratio in
  because most models read "16:9" from the prompt text. HappyHorse takes it as a parameter enum on every
  surface checked, so writing a ratio into the prompt is not a technique here. The guide instead tells the
  agent to spend prompt words on shot size and camera movement, and says the frame shape is chosen
  host-side.
- **Timecodes stayed in.** "Shot 2 (mid tracking, 1-4s)" is literal prompt text that the model parses, so it
  is craft, not a limit, in the same way aspect ratio is craft for models that read it from the prompt.

The prompt-enhancer toggle seen on WaveSpeed is stated as portable technique with no parameter name, and is
given a reason specific to this model: it reinflates prompts that were deliberately trimmed.
