# Stable Audio source conflicts and their resolution

Not a scrape. This is a hand-authored adjudication of conflicts between Stability AI's own surfaces
and between those surfaces and the secondary coverage of them. Evidence pulled from the sibling files
in this folder and from the Hugging Face cards, which are read through the authenticated HF tools
rather than scraped. Written 2026-08-29.

## Which model line is current. RESOLVED, and it was nearly got wrong.

The guide was originally scoped as "Stable Audio 2.5 plus Open and Open Small". That scope was a year
stale. **Stable Audio 3.0 shipped 2026-05-20** and is the current family; 2.5 is superseded, and the
2.5 launch post is still the most visible Stable Audio page in search results, which is how the stale
scope arose in the first place. A DAW plugin and a rebuilt web app followed on 2026-08-18.

Anyone re-verifying should start from `github.com/Stability-AI/stable-audio-3` and the model table in
its README, not from stability.ai news posts.

## The naming trap. RECORDED IN THE GUIDE.

Two distinct things both read as "open Stable Audio":

| Name | What it is |
| --- | --- |
| `stable-audio-open-1.0`, `stable-audio-open-small` | the 2024 line, superseded |
| `stable-audio-3-small-music`, `-small-sfx`, `-medium` | the current family, also openly published |

"Stable Audio Open" is a product name belonging to the old line, not a description of the new one.
`stable-audio-open-small` and `stable-audio-3-small-music` are two generations apart. The guide's
Models section states this explicitly because the failure is silent: both download and run, and the
older one is simply worse at music without saying so.

## Conflict 1: parameter count of the small models. RESOLVED on owner authority.

Secondary coverage of the 3.0 launch reports the small models at 459M parameters. The model table in
the owner's own repository README says 433M. **The owner governs**; the spec table carries 433M and
nothing here is sourced from the launch coverage. Recorded because 459M appears in several places and
will look like the better-attested number to anyone who checks the news rather than the repo.

## Conflict 2: sampling steps for Stable Audio Open 1.0. RECORDED IN THE CELL.

The `stable-audio-open-1.0` card contains two usage snippets that disagree with each other. The
`stable-audio-tools` snippet passes `steps=100`; the `diffusers` snippet immediately below it passes
`num_inference_steps=200`. Same card, same model, no explanation. The spec table carries both with
attribution to the snippet each came from rather than picking one.

## Not a conflict, but the subtlest thing in the guide: guidance and negatives.

Stable Audio 3 ships with guidance at 1.0 by default, and the inference doc suggests 7.0 "for stronger
prompt adherence". A negative-prompt field exists and is documented. These three facts together mean
something the docs never say outright: **at the shipped default, the negative prompt is close to
inert**, because guidance is the mechanism a negative acts through. Raising guidance strengthens the
positive prompt and the negative together; they are not independent controls.

This is the distillation-cost rule with a twist. The usual pattern is that a few-step checkpoint runs
at zero guidance and exclusions are permanently dead, as on ACE-Step turbo and z-image-turbo. Here the
post-trained checkpoints still accept guidance, so the cost is recoverable rather than structural. The
guide's negatives section states it in those terms, since "this model has a negative prompt" on its own
would be true and misleading.

## Conflict 3: whether small-music and small-sfx are a size ladder. RESOLVED.

They are not. The prompt guide's model compatibility table marks small-music as covering music and
stems but NOT samples or SFX, and small-sfx as covering samples and SFX but NOT music or stems. They
are same-size specialists (both 433M), not a large and a small. This matters more than a capability
footnote usually would, because the natural assumption is that a smaller model does everything worse
rather than that it does some things not at all.

Corroborated on a second, independent owner surface. The Hugging Face card metadata carries `music` on
small-music, `sound-effects` on small-sfx, and both on medium. That is a different surface from the
prompt guide's compatibility table and it partitions the family the same way, which is the strongest
form this claim can take short of measurement.

## Surface access notes

- `platform.stability.ai/docs/api-reference` renders client-side and returns about 1.6 KB of shell to
  both curl and WebFetch. Firecrawl would render it but was out of credits on the day. Nothing in the
  guide is sourced from it, which costs nothing: it is an API reference and this repo's scope excludes
  API surface anyway. The Stable Audio 3 Large row is therefore built from the repository model table,
  which is the only owner surface that describes it, and no card is published for it.
- The gated cards (`stable-audio-3-medium`, `-small-music`, `-small-sfx`, and the two legacy Open
  models) each carry their own gate. Accepting the gate on one does not grant the others. The base
  checkpoints are ungated and carry the same model description, which is what made the family
  documentable before the gated cards were opened.

  The gated cards were read afterwards and changed nothing. They repeat the same model description
  verbatim, carry `base_model:` fields confirming each post-trained checkpoint's pairing with its base,
  and show the expected split in their usage snippets: the base cards pass roughly 50 steps at guidance
  7.0 explicitly, while the post-trained cards omit both and take the low-step, low-guidance defaults.
  Recorded because a guide built from sibling checkpoints is a weaker claim than one built from the
  cards themselves, and that weakness no longer applies.

## What the guide takes from where

- Generation modes, the model compatibility table, the metadata tag vocabulary, the per-mode element
  checklists, every verbatim example prompt, and the audio-to-audio and inpainting technique including
  the context-beats-prompt rule: all from `docs/guides/prompting.md`.
- Family line-up, parameter counts, maximum lengths, hardware and VRAM: from the repository README's
  model and performance tables.
- Sample rate: from the README's SAME autoencoder description, not carried across from Open 1.0.
- Defaults for steps, guidance and duration, and the existence of the negative-prompt field: from
  `docs/workflows/inference.md`.
- English-only, the inability to produce intelligible vocals, and the legacy line's music weakness:
  from the Stable Audio Open cards, whose Limitations sections are the most explicit statement of
  those constraints the owner publishes.
