# LTX-2.5: structure decision and source notes

Not a scrape. Hand-authored 2026-08-12 from the sibling scrapes in this folder plus the gated Hugging Face
card, read through the authenticated HF tools rather than firecrawl.

## 1. Merge into the existing `ltx-2` scheme

LTX-2.5 joins `guides/ltx-2.md`. Scheme, filename and lorebook uid all stay put. The evidence is unusually
direct for a merge call:

- The six named prompt elements are the same six, under the same headings, in the same order.
- The two Sample Prompts in the 2.5 docs (news reporter, frog yoga studio) are the SAME two prompts the 2.3
  guide published, and the same two already quoted in the guide. The owner reused its flagship examples
  verbatim for the new model.
- The "Additional Helpful Terms" vocabulary is carried over intact.
- The card states that "the large majority of LoRAs and IC-LoRAs trained on LTX-2.3 run on LTX-2.5 without
  changes", and every released IC-LoRA is still an `LTX-2.3-22b-*` checkpoint.

The differences are capability (native multishot, automatic duration) and degree (text rendering, prompt
adherence), which is the merge case exactly. Multi-shot looked like a candidate conflicting layer but is not:
the owner says to write it as "one chronological paragraph", explicitly forbids shot lists and numbered
beats, and states that "the same rules as single-shot apply". It extends the paragraph grammar rather than
replacing it.

The guide display name is de-versioned to `LTX (family)`, following the Seedance 2.5 pass, which dropped
"2.0" from the guide name while leaving `prompt_scheme` alone. The scheme is identity and the uid is
identity; the display name is not.

## 2. The length rule actually changed, and the owner version-scoped it first

This is the one real inversion, and it is the reason this note exists.

LTX-2.3 guidance, still live and archived in `sources/ltx/`:

> Match your prompt length to your video length - short prompts for long videos leave the model without
> enough direction to fill the duration.

> Longer, more descriptive prompts consistently outperform short ones **on 2.3**. If you're generating longer
> videos (8-10 seconds), make sure your prompt is detailed enough to fill the duration. A short prompt for a
> long video often results in the model rushing through the described action.

LTX-2.5 guidance:

> Match length to complexity rather than a fixed count. A simple single shot is often 4-8 sentences; a longer
> screenplay-style scene can run longer, provided every sentence adds concrete visual or audio detail.

The guide previously taught the 2.3 rule as the headline LTX differentiator ("LTX wants a LONG prompt
describing a SIMPLE scene"), separating length from complexity as independent axes. LTX-2.5 recouples them.

Two things make this safe to teach as a version-conditioned change rather than a silent overwrite:

- The owner scoped its own claim with the words "on 2.3". That is the vendor marking the rule as
  generation-specific before we did.
- There is a documented mechanism, not just new copy. Automatic duration lets the model derive clip length
  from the prompt ("a one-line action stays short, a multi-shot sequence runs longer"), so padding a prompt
  to fill a fixed slot is no longer the thing that works. The Gemma 4 12B text encoder is described as
  holding complex prompts together "instead of dropping details across a longer sequence", which is the other
  half of why the old advice was needed.

Recorded in the guide as an access-and-version-conditioned note, the same treatment `wan-video` gives
`auto_expand_behavior`.

## 3. Multishot is a model capability, not a prompting trick

Worth stating because a reader could otherwise assume 2.3 would take the same prompt. The card is explicit:

> Native multishot generation - generate connected scenes in a single pass: multiple shots that hold
> character identity, environment, lighting, voice, and visual style across cuts (previous versions produced
> a single continuous shot).

So the multi-shot section is marked 2.5-only. On earlier checkpoints the same prompt has no cut mechanism to
drive and degrades into one take.

## 4. The blog promises a Video Editing section it never delivers

`ltx.io/blog/ltx-2-5-prompt-guide` carries this in its Key Takeaways, and names it in the page subtitle:

> IC-LoRA tools (Dub-It, Video Editing) use their own formats: [...] Video Editing works best with one
> concrete, additive-phrased instruction naming what changes and what stays.

There is no Video Editing section in the body of either the blog or the docs prompting guide, and there is no
adapter called "Video Editing" in the released IC-LoRA list. The list does carry a family of video-to-video
edit adapters that the sentence plainly describes: Day to Night, Clean Plate, Colorization, Decompression,
Deblurring, Instant Shave, Water Simulation, In-Outpainting.

Resolution: teach the rule, attribute it to the takeaway, and scope it to that family rather than to a named
adapter that does not exist. The rule is worth keeping because it restates this repo's own NAME WHAT MOVES,
PIN WHAT STAYS principle in the owner's words, which is corroboration rather than a new claim. Flagged in the
guide's coverage note as owner-stated but undocumented in the body.

## 5. Dub-It is documented, and is a genuinely different prompt shape

Unlike the Video Editing case, Dub-It has a real template and real constraints:

> [Speaker] is speaking [Language/Accent], saying: "[Dialogue]"

Validated languages: English, French, Spanish, German, Russian. Requirements: supply the full dialogue text
because the model does not translate for you; write it in the target language's native script; single speaker
only in the beta. Best practice is to match the syllable length of the original, with slightly long beating
slightly short.

Note the mismatch to record: the Hugging Face card declares nine model languages (en, de, es, fr, ja, ko, zh,
it, pt) while Dub-It validates five. Those are different claims about different things (what the base model
speaks versus what the dubbing adapter was tested on) and the guide keeps them apart.

Both Dub-It and Relight are tagged "LTX-2.5 in development" in the adapter table, so they run on 2.3
checkpoints today.

## 6. Negatives: a field exists on the local path but cannot bite on the distilled checkpoint

The prompting guidance still uses no negative prompts anywhere, so the guide's positive-steering rule stands.
One refinement is now supported by the card: the Diffusers example imports `DEFAULT_NEGATIVE_PROMPT` and
passes it, while also running `guidance_scale=1.0`, and the distilled transformer is documented as "Fixed
8-step schedule, CFG=1". At guidance 1.0 the unconditional branch contributes nothing, so the negative prompt
is inert there regardless of what you write in it.

This is the distillation-cost note the house rules require: the syntax accepts a negative, the leverage is
absent. The dev transformer's recommended guidance is not published on the card, so the guide says the field
responds on the dev path without asserting a number.

## 7. Capability regression on 2.5, which is easy to miss

The endpoint compatibility table shows 2.5 gaining audio-to-video on the fast tier, which 2.3 fast lacked,
and losing three modes outright:

| Mode | ltx-2-5-fast | ltx-2-5-pro | ltx-2-3-fast | ltx-2-3-pro |
| --- | --- | --- | --- | --- |
| audio-to-video | yes | yes | no | yes |
| retake | no | no | no | yes |
| extend | no | no | no | yes |
| reframe | no | no | no | yes |

Retake, extend and reframe remain LTX-2.3 Pro only. The guide's model rows carry this, because a reader who
assumes the newest model is a superset would write an extend prompt for a checkpoint that has no extend.

## 8. Owner surface moved from docs.ltx.video to docs.ltx.io

The existing guide cited `docs.ltx.video`. The new card links `docs.ltx.io`, and the canonical
`docs.ltx.io/open-source-model/usage-guides/prompting-guide` serves the 2.5 content. Sources updated to the
`.io` host.

Scraping note for the next pass: the 2.5 docs were first reachable only through a Fern preview deployment
(`lightricks-preview-feature-ltx25-model-docs.docs.buildwithfern.com`), whose URL leaked into the blog's own
body copy. That preview host is NOT citable; it will disappear. It was used to find the content, then every
claim re-verified against the canonical host before it went into Sources.

Second scraping note: `ltx.io` is a Webflow site that returns only navigation chrome at the default wait.
`--only-main-content --wait-for 8000` yielded 3.6 KB of menus and an Optimizely block notice. Dropping
`--only-main-content` and raising the wait to 15000 yielded the full 57 KB page. If an LTX blog scrape comes
back small, it did not fail loudly, it just returned the shell.

## 9. Company naming

Press coverage of the release describes LTX as "the open world model company spun out of Lightricks", and the
model card headline calls LTX-2.5 "an open world model with open weights". The Hugging Face org is still
`Lightricks` and the GitHub org is still `Lightricks`. The guide keeps attributing the model to Lightricks,
since that is what every owner surface still says on the repo and card, and adds nothing about the corporate
structure, which is not prompt craft.
