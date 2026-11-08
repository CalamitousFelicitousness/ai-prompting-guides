# Seedream: 5.0 Flash and provisional 5.5 pass, source notes

Not a scrape. Hand-authored 2026-11-08 from the sibling scrapes in this folder. The earlier passes
(2026-05-31 family guide, 2026-07-13 5.0 Pro merge) left no note here; their decisions live in project
memory. This note records what the November pass settled.

## 1. Seedream 5.5 is not owner-released; added as provisional at the user's request

Evidence gathered 2026-11-08:

- ByteDance Seed: no 5.5 page (`seed.bytedance.com/en/seedream5_5` is a 404); the homepage blog list
  ends at the 5.0 Pro launch for Seedream.
- BytePlus ModelArk model release announcements (last updated 2026-10-26): no 5.5 entry. Docs nav still
  lists only "Seedream 5.0 pro / flash tutorial" and "... interactive editing guide".
- BytePlus Lumina (ByteDance's own creative product): two SEO pages. One expects "late October 2026,
  subject to change"; the other says "currently a preview build ... has not announced a release date,
  pricing, API access, or public availability".
- WaveSpeed (approved provider): live `bytedance/seedream-v5.5` text-to-image, edit, and
  layer-decomposition pages. Atlas Cloud (not approved) also hosts it. apixo (not approved) says "Not
  yet" as of its November page.

The user chose "Flash plus provisional 5.5". So 5.5 is in the guide with a YAML comment, a "provisional"
best_for, a dedicated "Seedream 5.5: provisional notes" section, and a pitfall. Tier `flagship`
(BytePlus Lumina calls it "the official successor to Seedream 5.0 Pro"; WaveSpeed calls 5.0 Pro "the
previous Pro model"), while 5.0 Pro stays `flagship` as the documented top tier. Caps exclude
`grounded-edit` and `reasoning` because no 5.5 source mentions marks, coordinates, or a planning step.
`transparency` reuses the existing cap name.

What was taught from 5.5 sources, all marked provisional:
- "no new prompt syntax to learn" (Lumina) -> write 5.5 prompts like 5.0 Pro.
- Transparency is a request field (`background: transparent` on WaveSpeed); the prompt-side craft is
  WaveSpeed's tip "ask for the subject on its own in the prompt" plus its "isolated" example prompts.
- Multi-round edit stability (WaveSpeed, Lumina) -> edit in small rounds.
- Layer decomposition as a separate endpoint with optional prompt (WaveSpeed) -> same as 5.0 mode.
- Small text and languages (Lumina preview: Thai, Japanese, Russian named) -> proofread anyway.

Kept out: resolution tiers (1k/1.5k/2k/3k), reference count (10), `max_images` billing, pricing,
Lumina's "80+ rounds" and Atlas Cloud's "100+ rounds" claims (unverifiable marketing numbers).

Re-verify when ByteDance publishes: tier, caps (marks? coordinates? reasoning?), whether 5.0 Pro moves
to legacy, and any owner prompt guide.

## 2. Seedream 5.0 Flash joins the scheme

`dola-seedream-5-0-flash-260915`, ModelArk release 2026-09 ("same capabilities as Seedream 5.0 pro,
including interactive editing, layer decomposition, and native multilingual generation ... faster and
costs less"). The tutorial's capability table ticks every feature for both; differences are image
quality ("Pro: higher image quality") and a parameter (Pro also offers a fast prompt-optimization mode).
Merged, tier `distilled` (vendor flash tier), same caps as Pro. The distillation cost recorded is the
owner's own: highest image quality is reserved for Pro.

Naming: BytePlus prefixes both with "Dola" and date-suffixes the IDs (YYMMDD). Recorded in a YAML
comment and a Naming paragraph; the guide's short IDs (`seedream-5.0-pro`) stay.

## 3. Coordinate tags (new owner prompt notation)

The "Seedream 5.0 pro / flash interactive editing guide" documents `<point>x y</point>` and
`<bbox>x1 y1 x2 y2</bbox>` written into the prompt, normalized per image to 0-999 with 0,0 top-left
(`x = round(x_px / width * 1000)`). This is prompt grammar the model reads on every host, so it is in
scope, unlike the frontend canvas code around it. Owner tips taught verbatim in substance: name the
target when a box holds several subjects; box what must stay and say "keep unchanged".

Guide-added rule: never estimate coordinates. The guide's reader is an agent writing prompts, usually
without measured coordinates; a guessed box is the failure mode the owner docs do not need to warn a
UI developer about.

## 4. Owner vs owner: layer separation form

- July (Seed launch blog): plain-text request inside a normal generation, "Separate this poster into
  independent editable layers: ... Inpaint the background where the subject was covering it".
- November (BytePlus API tutorial): a dedicated `layer_decomposition` mode; prompt optional; returns
  a base image plus layers with position, stacking order and descriptions. Prompt tips: omit for
  automatic split, name elements ("Decompose the person, title text, and decorative icon in the
  lower-right corner."), mark them with doodles, or give `<bbox>` regions.

Resolution: API reference governs. Taught the mode's prompt forms as canonical and kept the blog's
plain-text request as the tolerated form for hosts without the mode. The old example (with the inpaint
clause, which the mode makes redundant because it returns a base image) was replaced by the two owner
forms.

## 5. Smaller changes

- Mark removal: the owner's freeform-marking example says "Remove all sketch lines"; the guide had no
  such rule. Added as a rule, a pitfall, and the owner example. Same lesson as gemini-image and
  gpt-image markup.
- Languages: the tutorial lists the 14 additional languages explicitly (Russian, Arabic, Filipino,
  Thai, Turkish, Korean, Malay, Spanish, Portuguese, Indonesian, French, German, Vietnamese,
  Japanese). This settles the July provider disagreement on the count; the guide lists them by name.

## 6. Kept out

Resolution tiers, the 16-layer cap, input size and pixel limits, IPM rate limits, prompt optimization
mode names, `layer_decomposition` and other request fields, SDK version notes, the TouchEdit demo.
