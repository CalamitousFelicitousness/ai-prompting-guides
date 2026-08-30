# ACE-Step source conflicts and their resolution

Not a scrape. This is a hand-authored adjudication of conflicts BETWEEN ACE-Step's own surfaces,
written because the repo's source bar resolves owner-vs-provider on owner authority but has no rule
for owner-vs-owner. Evidence pulled from the sibling files in this folder. Written 2026-08-29.

ACE-Step is unusual for this repo in that there is no provider or community tier worth consulting:
the owner ships a full prompting tutorial in its own repository, and every rule in the guide traces
to it. The conflicts are all internal to the owner's own documentation set.

## Which repository is canonical. RESOLVED.

There are two. `ace-step/ACE-Step` is the v1 repository and `ace-step/ACE-Step-1.5` is the current
one; the citation block on the v1.5 model card points at the latter. The v1 README is partly stale
in a way that is easy to misread: its News section announces the 2026-01-28 v1.5 release while its
Roadmap still carries an unchecked `[ ] Train and Release ACE-Step V1.5` a few sections below. The
v1 README also documents a Gradio UI whose tab layout no longer matches the current one.

**`ace-step/ACE-Step-1.5` governs.** Nothing in the guide is sourced from the v1 README. Anyone
re-verifying this guide should start from the 1.5 repository and treat the v1 one as historical.

## Conflict 1: which checkpoints respond to guidance. UNRESOLVED, recorded as such.

Two owner surfaces disagree, and both are current:

| Surface | Claim |
| --- | --- |
| Model-zoo table, in both the 1.5 README and the Hugging Face card | base and sft have a CFG column marked yes; turbo marked no |
| Hyperparameter table, `docs/en/Tutorial.md` | `guidance_scale` is annotated "Only Base model effective" |

The two agree that turbo has no classifier-free guidance, and that fact is stated consistently in
every surface including the prose description of the turbo line. It is the only guidance claim the
guide relies on, and it is load-bearing: it is what makes exclusions inert on the default checkpoint.

The disagreement is confined to sft. The model-zoo table is a capability matrix and the hyperparameter
table is operational guidance, so neither is obviously the API-reference-equivalent that the
owner-vs-owner rule would rank first. Rather than pick, the guide's sft model row and the spec table
both state that the model-zoo tables mark it as supporting guidance while the tutorial says otherwise.

This is deliberately not smoothed over. A reader tuning guidance on sft needs to know the owner has
said both things, because the failure mode is silent: guidance that does nothing looks identical to
guidance that is doing something subtle.

## Conflict 2: how many distilled checkpoints exist. NOTED, no craft impact.

`docs/en/Tutorial.md` states "We've open-sourced 4 Turbo models" and names `turbo`, `turbo-shift1`,
`turbo-shift3` and `turbo-continuous`, distinguished by the shift schedule used during distillation.
The model-zoo tables in the README and on the model card publish one turbo row per decoder size.

No resolution needed for prompting purposes: the tutorial is explicit that the four differ only in a
denoising hyperparameter and take an identical prompt. The guide therefore names the variants without
counting them, and the spec table carries one row per published checkpoint. Revisit only if a variant
ever acquires its own prompt behaviour.

## Conflict 3: step count for the base checkpoint. RECORDED IN THE CELL.

The model-zoo tables give base 50 steps. The tutorial's hyperparameter table says "Turbo uses 8, Base
uses 32-100". These are not really contradictory, since 50 sits inside 32-100, but a single number and
a range are different kinds of claim. The spec table carries both with attribution rather than
collapsing them to 50.

## Non-conflict worth recording: the owner cites a competitor's tutorial.

The caption section of `docs/en/Tutorial.md` closes by linking a third-party Notion guide to prompting
Suno, describing the ideas as universal. It is a community source under this repo's trust order and
nothing in the guide comes from it. Recorded here only so a future pass does not mistake the owner's
link for an owner statement and promote it.

## Conflict: 19 languages or 50-plus. RESOLVED, they are different models.

The `ace-step/ACE-Step` README and the project page at `ace-step.github.io` both advertise 19
languages with a well-performing top ten of English, Chinese, Russian, Spanish, Japanese, German,
French, Portuguese, Italian and Korean. The 1.5 README, the 1.5 project page and the 1.5 tech report
all say 50-plus. The two numbers sit on surfaces that look interchangeable and are not.

Checked by following what each surface points at. The root project page links to exactly three
things: `ACE-Step-v1-3.5B`, `github.com/ace-step/ACE-Step`, and arXiv 2506.00045. The 1.5 line has
its own page at `ace-step.github.io/ace-step-v1.5.github.io/`, its own paper at arXiv 2602.00744,
and its own checkpoints. So the 19 is v1's and the 50-plus is 1.5's, and the guide covers 1.5.

The owner also states the direction of travel. The 1.5 page carries a list of what v1 lacked, one
entry of which is "Multilingual Lyrics Compliance: Improved support for lyrics in multiple
languages, enhancing accuracy and naturalness." The jump is intended, not a stale number.

Worth knowing how thin the 50-plus is, though. For the generator it rests on one sentence in the
tech report abstract, reproduced verbatim on the 1.5 README and the 1.5 project page, plus one
feature bullet. No generator surface enumerates it.

The only enumeration the owner publishes anywhere in this family is on `acestep-transcriber`, the
annotation model that labelled 1.5's training data. That card claims the same 50-plus and names 26
by region, "including but not limited to": Chinese, Japanese, Korean, Vietnamese, Thai, Indonesian,
Malay, Filipino, Hindi, Bengali, Tamil, Urdu, English, German, French, Spanish, Italian, Portuguese,
Russian, Polish, Dutch, Greek, Turkish, Arabic, Hebrew and Persian. The guide carries those 26 as
the well-covered core, attributed to the transcriber rather than to the generator, because the
generator's lyric coverage is bounded by what its labeller could read. The matching 50-plus on both
models is consistent with the generator's figure being inherited from the annotation pipeline; the
owner never says so, so the guide does not either.

The tutorial's vocal-language control is documented as usually auto-detected from the lyrics, which
is the craft-relevant half and is what the guide carries.

## What the guide takes from where

- Caption dimensions, the seven caption principles, the structure-tag vocabulary, the tag-combining
  and tag-stacking rules, the caption-lyrics consistency checklist, syllable counts, uppercase and
  parenthesis conventions, vowel extension being unstable, and the AI-flavoured-lyrics red flags:
  all from `docs/en/Tutorial.md`.
- The checkpoint line-up, per-model capabilities, and the quality and diversity ratings: from the
  model-zoo tables, which appear identically in the 1.5 README and on the Hugging Face card.
- Sample rate, duration bounds and default hyperparameters: from `docs/en/INFERENCE.md` and
  `docs/en/API.md`.
- The two-stage planner-plus-diffusion architecture and default-on rewriting: from the abstract and
  the LM hyperparameter table, which agree.

- The 50-plus language claim and the automatic vocal-language detection: the 1.5 repository README
  and the prompting tutorial. The 26 named languages: the transcriber model card.
