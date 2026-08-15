# Seedance 2.5: structure decision and source notes

Not a scrape. Hand-authored 2026-08-07 from the sibling scrapes in this folder. The notable outcome is
section 2: this release did not just add material, it overturned a citation rule the guide had been
teaching since May.

## 1. Merged into the existing guide, no split

`guides/seedance.md` now covers `seedance-2.5` alongside `seedance-2.0` and `seedance-2.0-fast`. Scheme
key stays `seedance-v2`, which still reads correctly since 2.5 is in the 2 series; renaming it would churn
CLAUDE.md, memory and the lorebook catalog for no gain.

The owner frames 2.5 as an extension of the same architecture in its own first paragraph: "Building on the
unified multimodal audio-video joint-generation architecture of Seedance 2.0". Everything that would force a
split is unchanged:

- Same director's-brief formula, subject and action first, camera next.
- Same citation notation, `@Type N` (see section 2).
- Same modes: text-to-video, image-to-video, reference-to-video, edit, extend.
- Same joint audio-video generation in one pass.

What 2.5 adds is capability that changes what you spend words on, not how you form them: a story arc in one
pass, a much larger reference load, an untextured-3D structure channel, and timestamp-addressable editing.
That is the merge criterion, same as Seedream 4.5 plus 5.0-lite and the Qwen 3.0 pass.

Guide display name went from "Seedance 2.0 (video)" to "Seedance (video)" and the H1 lost its version, per
the house title format and the precedent set when the Qwen guide stopped being named after one release.

## 2. The citation notation flipped, and the earlier call was not wrong

The guide previously taught:

> the official docs name assets by type and number ("Image 1", "Video 1", "Audio 1"), while FAL and
> WaveSpeed wrap the same reference as an @-mention ("@Image1"). This guide treats the official "Image 1"
> form as canonical and the @-form as a host variant of the same idea.

Every clause of that is now false. Re-scraping the owner's prompt guide shows it carries
`Last updated: July 31, 2026`, the same day the flagship shipped, and it now writes `@Image 1` throughout
(27 at-sign citations across Image, Video and Audio). The flagship announcement uses the at-sign form
exclusively and never uses a bare one.

**This is a source that changed under us, not a misreading, and the archived scrape proves it.** The May
scrape of that same page, kept at `sources/seedance/byteplus-seedance-2.0-prompt-guide.md`, contains ZERO
at-sign citations against 65 bare ones; the re-scrape of the same URL today contains 27. The page's own
"Last updated" stamp reads 2026-07-31. So the earlier adjudication was accurate when written. Recorded that
way in the guide's coverage note rather than as a correction, because "the owner changed its docs" and "we
got it wrong" call for different amounts of future suspicion.

This is also the first time keeping the raw scrapes paid off as an audit trail rather than as a digest
source. Keep them.

Three details the old text also got wrong, all now fixed:

- **The sigil is universal; the spacing is not.** Corrected 2026-08-07 after a portability question exposed
  an over-correction in the first version of this note. Counted across every scrape in this folder and its
  sibling:

  | Surface | `@Image 1` spaced | `@Image1` closed |
  | --- | --- | --- |
  | ByteDance 2.5 announcement | 18 | 0 |
  | BytePlus prompt guide (current) | 27 | 0 |
  | FAL how-to-use | 0 | 12 |
  | WaveSpeed complete guide | 0 | 42 |

  The owner spaces it; both approved providers close it up, in their own worked examples ("Replace the person
  in @Video1 with the girl in @Image1"). So the old guide text was RIGHT about the providers and wrong only
  about the owner.

  **Settled by dating the sources, after two wrong intermediate answers.** The first fix declared the space
  "not cosmetic", which would have sent an agent onto WaveSpeed writing a form WaveSpeed's docs never use.
  The second fix said "match the host", which assumed the provider spelling carried authority. Both were
  wrong for the same reason: neither asked what the spelling actually IS.

  It is prompt text. FAL's own wording is that you reference inputs "in your prompt using tags", and neither
  provider trained this model, so whichever service you route through, the same closed ByteDance model
  receives the literal string. There is no mechanism by which a host would prefer a different spelling unless
  it parsed the tag itself, and nothing in either provider's documentation describes parsing.

  The dates then decide it. WaveSpeed's guide is stamped 2026-05-29 and FAL's is from the same period, both
  two months BEFORE the owner adopted the notation on 2026-07-31, back when the owner still wrote references
  bare. Neither provider has published Seedance guidance since; WaveSpeed has no live 2.5 model page at all.
  So the closed-up form is not a host convention competing with the owner's, it is a pre-standardization
  convention that predates the owner having one, left unrevised.

  **Taught: the owner's spaced form on every host.** The closed-up spelling is recorded as legacy with a note
  that it is a cheap thing to try if a binding fails on one host, which is the honest limit of what is known
  without probing the live API.
- **Ranges exist.** `@Images 6 to 10`, `@Images 11 to 14`, `@Images 15 to 18` appear in the announcement's
  large-cast prompt. Without this, a big ensemble becomes a wall of one-asset clauses.
- **Subject binding is a documented form.** The owner's prompt guide specifies `<Subject_N>@<Image_N>`,
  example `Zhang San@Image 1`, and says to repeat the binding each time the subject is mentioned. This is
  the repo's ONE ROLE PER INPUT stated as syntax, and is the second time a vendor has spelled the principle
  out rather than the guides inferring it (the first was HappyHorse).

Mechanical follow-through: every bare citation already in the guide, in example prompts and in the `Why`
captions, was converted to the at-sign form, since leaving them would have contradicted the new rule inside
the same document.

## 3. Clay render and white model are the same thing

The announcement says "clay render" and cites `@Clay Render 1`. The owner's prompt guide says "white model".
Both mean an untextured 3D pass. The guide introduces the section with both names and cites with
`@Clay Render 1`, since that is the form that appears in an actual prompt.

Treated as a reference TYPE with its own numbering rather than as a kind of image, because the announcement
numbers it separately and because its role is categorically different: it carries geometry, blocking, camera
path and pacing with no look attached. That makes it the cleanest ONE ROLE PER INPUT example in the guide,
structure from one asset and appearance from another, and it is the reason the guide grew a dedicated
section instead of a bullet.

## 4. No flagship API reference exists yet

The owner's announcement says API access is "coming soon via BytePlus ModelArk", and the re-scrape confirms
it: the ModelArk prompt guide mentions Seedance 2.0 eighteen times and 2.5 zero times, despite having been
updated on launch day. Meanwhile fal already serves live 2.5 image-to-video and reference-to-video endpoints.

So for the flagship specifically, the standing owner-versus-owner rule (the API reference governs) has no
API reference to apply. The announcement is the only owner surface, and it is a showcase surface. Handled by
teaching its prompts, since there is nothing of higher rank to defer to, while stating the exposure in the
guide's coverage note and flagging the flagship sections for re-verification when the reference publishes.

The announcement's eight verbatim prompts are unusually good evidence for a marketing page: they are long,
specific, internally consistent, and they use the same notation the API-era 2.0 guide uses, which is what
makes them safe to teach.

## 5. Provider material: one source deliberately not used

fal's "What is Seedance 2.5" article was written BEFORE launch. Its text still says "Once Seedance 2.5
ships, fal is lined up to host it", it sources its specs to CNET rather than to ByteDance, and it hedges
with "reportedly". It is stale and community-derived despite sitting on an approved provider's domain.

Not cited as a craft source. The provider citations are fal's live 2.5 endpoint pages instead, which are
current and carry real prompt-field guidance ("Put spoken dialogue in double quotes for lip-synced audio",
and the i2v rule to describe what changes rather than what is already visible).

Related: the widely repeated 4K claim traces to CNET, and the owner's own announcement never mentions
resolution at all, saying only "notable gains in image, audio, and motion quality". Out of scope as a
resolution tier regardless, but worth recording that the owner did not make the claim.

Also noted, not taught: fal's playground says "Type # to reference inputs". That is a host UI affordance for
inserting an asset, not the in-prompt notation, and confusing the two would put a stray `#` into prompt text.

## 6. Scope: what was dropped and what was kept

Dropped in full: clip-length limits, reference counts per modality, resolution tiers, pricing, endpoint
paths, and the token arithmetic on fal's pricing block.

Kept, with the reasoning that keeps recurring:

- **Timecodes stayed in.** `0-5s:`, `11-20s:` are literal prompt text the model parses, so they are craft.
  Same treatment as the HappyHorse shot list.
- **Aspect ratio stayed in**, unlike the HappyHorse pass. The owner's prompts write "16:9 widescreen" and
  "in 16:9 landscape" directly into the prompt text, so here it is genuinely something the model reads.
- **Durations inside example prompts stayed** where the owner wrote them ("A 30-second concert sequence"),
  because that is prompt content setting pacing. No rule in the guide asserts a maximum length; the rules
  say "the window" and let the provider docs supply the number.
