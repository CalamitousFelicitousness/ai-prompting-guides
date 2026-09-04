---
guide: "Anima"
prompt_scheme: "anima"
models:
  - { id: "anima-base", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "maximum flexibility, style diversity across seeds, and strong tag adherence; a true base model whose plain neutral default relies on quality and artist tags to set an aesthetic. The tier LoRAs are trained against" }
  - { id: "anima-aesthetic", access: "open-weights", tier: "std", caps: [text-to-image], best_for: "a better default art style for less prompt work. Trained only on high-quality images with the quality tags STRIPPED from its captions, so it wants no score tags on either side of the prompt" }
  - { id: "anima-turbo", access: "open-weights", tier: "distilled", caps: [text-to-image], best_for: "fast iteration: 8 to 12 steps at CFG 1, and the owner's own recommended starting point. Distillation buys stability and a strong default style and costs diversity; at CFG 1 the negative prompt stops doing work" }
  - { id: "anima-2.9b", access: "open-weights", tier: "flagship", caps: [text-to-image], best_for: "the largest checkpoint on this scheme and the newest character knowledge, but a COMMUNITY layer expansion at preview stage rather than a CircleStone release. Take its card as authoritative for its own weights only, and fall back to the base rules wherever it is silent" }
capabilities: [text-to-image]
prompt:
  languages: ["en"]
  literal_text: "weak: it renders a single word and sometimes a short phrase, but not sentences; keep any in-image words to one short string welded to an object, and add longer text in an editor afterward"
  length_strategy: "native interface is a comma-separated Danbooru/Gelbooru tag list in a fixed section order; pure natural language also works (be descriptive, aim for at least two sentences, since very short prompts give unexpected results); tags and natural language mix in any order; trained with tag dropout, so you need not list every relevant tag"
  quality_tags: "THE RULE THAT MOVES BY TIER, and it fails silently. anima-base trained on them, so the human words and score_9 down to score_1 both work. anima-aesthetic had them stripped from its captions and the owner says NOT to use score_* on either side, because they push it toward slop. The 2.9B derivative also has no scores in its captions, though its untouched base layers still carry them"
  negatives: "SPLITS BY TIER. On anima-base they are real and recommended (it is CFG-guided): a quality and score negative plus the safety tags you want suppressed. On anima-aesthetic keep the shape but drop the score tags. On anima-turbo CFG is 1, so nothing is pushed away and the negative is decoration"
  auto_expand_behavior: "none built in; write the full tag list or description yourself"
sources:
  official: ["https://huggingface.co/circlestone-labs/Anima", "https://docs.comfy.org/tutorials/image/anima/anima", "https://civitai.com/models/2458426/anima"]
  provider: []
  community: ["https://huggingface.co/Gazingstars123/Anima-2.9B"]
last_verified: "2026-09-04"
---

# Anima: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, sampler and step settings, and code, consult the host's docs; they differ and are out of scope here.
- Anima is a booru-tag model. Its native interface is a comma-separated list of Danbooru/Gelbooru tags written in a fixed section order, not a natural-language sentence. This makes it prompt very differently from the natural-language models elsewhere in this set.
- It also understands natural language (a Qwen-3 0.6B text encoder gives good prompt adherence) and tag-plus-language hybrids. Tags are primary; reach for natural language to describe scenes, relationships, and anything without a clean tag.
- It is anime and illustration only, and is intentionally bad at realism. Do not prompt it for photographs.
- It is text-to-image with no input image, so there is no editing or multi-image section; those are N/A and omitted.
- It is CFG-guided, so negative prompts and quality tags are real, recommended levers (unlike the natural-language models elsewhere in this set). The Turbo tier is the exception and is covered below.
- FOUR checkpoints share this scheme and they are NOT interchangeable at the prompt. Base takes quality and score tags, Aesthetic wants no score tags at all, Turbo runs at CFG 1 where the negative stops working, and the community 2.9B has no scores in its captions. Check which one you are on before reusing a prompt.

</rules>

## TL;DR

<template id="quickstart">

masterpiece, best quality, score_7, safe, {1girl/1boy/count}, {character}, {series}, @{artist}, {hair, eyes, expression}, {clothing and accessories}, {pose or action}, {setting}, {a couple of meta or style tags}

</template>

That prefix is the anima-base default, and so is every example below. On anima-aesthetic drop the score tag; on anima-turbo drop the negative as well. See "Quality and score tags by tier".

## Models and when to use which

- `anima-base`: a compact 2B true base with no aesthetic tuning, so its default style is plain and neutral and quality plus artist tags do most of the work of giving it a look. In exchange you get the most flexibility, the most style diversity across seeds, and the strongest adherence to whatever tags you set. This is the tier to train LoRAs against.
- `anima-aesthetic`: the same model finetuned on high-quality images for a better default style and more consistency. It ships as v1.0, v1.0b and v1.1; the owner describes v1.0b as the aesthetics finetune alone, without the style-adjustment and stabilization LoRAs merged into v1.0, and prefers v1.0. Its captions had the quality tags stripped, which changes how you write the prompt.
- `anima-turbo`: the distilled tier, and the one the owner recommends starting with, on the grounds that it is only slightly worse than Aesthetic while being far faster to iterate with. Distillation also buys stability and a strong default style, and costs diversity. It ships as v1.0 and v1.1.
- `anima-2.9b`: a COMMUNITY derivative, not a CircleStone release. It expands anima-base from 28 transformer layers to 40 by deep-copying neighbouring blocks with their output projections zeroed, so it begins functionally identical to base and then continues training. Its knowledge cutoff is July 2026 against base's September 2025, so it knows newer characters and series. It is a preview, only its new layers are trained so far, and its card is authoritative for its own weights and nothing else.
- The prompt grammar is shared across all four. What moves between them is the quality-tag rule and whether the negative prompt does anything, both covered next.
- Because the base default is plain, always set a quality system and usually an artist tag on that tier. An anima-base prompt with no quality and no artist tags looks flat; that is the model working as designed, not a failure.
- An earlier `anima-preview` line also exists and is superseded.

## Quality and score tags by tier

<rules id="quality-tiers">

- ON `anima-base`: quality tags are trained and expected. Use the human words, the PonyV7 aesthetic scores (score_9 down to score_1), both, or neither; all combinations work.
- ON `anima-aesthetic`: the captions had every quality tag stripped, so you do not need them at all. Leaving "masterpiece, best quality" in is safe, but the owner asks directly for NO score_* tags in the positive OR the negative, because the tier is already tuned high and the scores push it into slop.
- ON `anima-turbo`: the quality question is secondary to the guidance one. At CFG 1 there is nothing to steer with, so treat both the quality prefix and the negative as far weaker levers than on base.
- ON `anima-2.9b`: its captions carry no scores either. Its author says you may still use them, and the untouched base layers do still carry the conditioning, so they weaken rather than break. Prefer the human quality words there and treat scores as optional.
- The mismatch fails SILENTLY in both directions. A base prompt carried onto Aesthetic brings score tags the owner warns against, and an Aesthetic prompt carried onto base drops a quality system that tier genuinely needs and comes out flat.

</rules>

## How the model reads prompts

- It was trained on three prompt forms: Danbooru-style tags, natural-language captions, and combinations of the two. All three work, and you can mix tags and sentences in any order.
- Write tags in lowercase with spaces, not underscores ("brown hair", not "brown_hair"). The one exception is score tags, which keep their underscores ("score_7").
- When a tag is spelled differently on Danbooru and Gelbooru, use the Gelbooru spelling.
- Prefix every artist tag with "@" ("@nnn yryr"). Without the "@" the artist effect is very weak.
- Character and series tags follow Danbooru romanization (for example "oomuro sakurako", "yuru yuri"); in natural language, follow normal English capitalization for character and series names.
- Prompt weighting works but needs higher weights than SDXL to bite. Use a stronger multiplier than you would there, for example "(chibi:2)".
- It was trained with random tag dropout, so you do not need every relevant tag; a focused set is fine.
- For pure natural language, be descriptive and aim for at least two sentences. Extremely short prompts give unexpected results and raise the chance of unwanted content.
- Name a character, then describe their appearance, rather than relying on the name alone. This matters most with multiple characters: a bare list of names with no descriptions confuses the model about who is who.
- Follow a character name with its series or copyright tag. The 2.9B author reports the model confusing characters without it, and the pairing is cheap insurance on every tier.
- On `anima-2.9b`, detail matters more than it does on base. Its author reports that a short prompt produces a bland, simple background and often misses the intent outright, so write the full tag list or a full description on that tier.

## Prompt structure

<rules id="structure">

- Follow the tag-section order: quality / meta / year / safety tags, then the subject count (1girl, 1boy, 1other, ...), then character, then series, then artist (@-prefixed), then general tags. Within any one section the order is free.
- Open with a quality system. The documented default prefix is "masterpiece, best quality, score_7, safe, "; lead with it unless you have a reason not to.
- Set a safety tag (safe, sensitive, nsfw, explicit) in the positive prompt, and the opposite ones in the negative, to keep content where you want it.
- Optionally pin a time period right after the quality block: a specific year ("year 2025") or an era word (newest, recent, mid, early, old).
- Add meta tags for format and fidelity (highres, absurdres, official art, anime screenshot, jpeg artifacts).
- Put the artist tag last before the general tags, always with "@". Start with one artist; stacking several blends styles but can get inconsistent.

</rules>

<template id="general">

{quality tags}, {year or era}, {meta tags}, {safety}, {count}, {character}, {series}, @{artist}, {hair, eyes, expression}, {clothing and accessories}, {pose or action}, {setting and background}, {extra style or meta tags}

</template>

<example use_case="single-character-full-tags">

```text
year 2025, newest, normal quality, score_5, highres, safe, 1girl, oomuro sakurako, yuru yuri, @nnn yryr, smile, brown hair, hat, solo, fur-trimmed gloves, open mouth, long hair, gift box, fang, skirt, red gloves, blunt bangs, gloves, one eye closed, shirt, brown eyes, santa costume, red hat, skin fang, twitter username, white background, holding bag, fur trim, simple background, brown skirt, bag, gift bag, looking at viewer, santa hat, ;d, red shirt, box, gift, fur-trimmed headwear, holding, red capelet, holding box, capelet
```

*Why: the documented tag-section order in practice, quality and year and safety first, then 1girl, the character, the series, the @-artist, then a free-order pile of appearance, clothing, and pose tags*

</example>

## Tag vocabulary

<rules id="vocab">

- Quality, human-score words: masterpiece, best quality, good quality, normal quality, low quality, worst quality.
- Quality, PonyV7 aesthetic scores: score_9 down to score_1 (these keep underscores). Use the human words, the scores, both, or neither; all combinations work.
- Safety: safe, sensitive, nsfw, explicit. Set the one you want in the positive and the rest in the negative.
- Time period: a specific year ("year 2025", "year 2024") or an era word (newest, recent, mid, early, old). Era words steer the art style toward that period of anime.
- Meta: highres, absurdres, official art, anime screenshot, jpeg artifacts, and similar format and source tags.
- Artist: always "@" plus the name ("@nnn yryr"); the effect is weak without the "@". One artist is the safe default.
- Subject count: 1girl, 1boy, 1other, 2girls, and so on, placed right after the quality block and before the character.
- Non-anime art: lead with a dataset tag on its own line, "ye-pop" or "deviantart", to pull from the model's non-anime training; an optional second line gives the alt-text (ye-pop) or work title (deviantart), then the description follows.

</rules>

## By use-case

<example use_case="natural-language-named-character">

```text
masterpiece, best quality, score_8, safe. Digital artwork of Fern from Sousou no Frieren, with long purple hair and purple eyes, wearing a black coat over a white dress with puffy sleeves. She stands in a sunlit forest clearing holding an open spellbook, soft warm light filtering through the leaves.
```

*Why: quality and safety tags can lead a natural-language prompt; the character is named and then described, so the model does not have to guess the appearance from the name alone*

</example>

<example use_case="tag-and-language-hybrid">

```text
masterpiece, best quality, score_8, newest, safe, 2girls, @nnn yryr. Two classmates share one umbrella on a rainy street at dusk, neon shop signs reflecting in the puddles. One has short black hair and a yellow raincoat; the other has long silver hair and a navy school uniform. wide shot, rain, city lights, looking at each other
```

*Why: tags carry the quality, count, era, safety, and artist, the sentence handles the scene and the relationship, and each of the two girls is described so the model keeps them distinct*

</example>

<example use_case="non-anime-dataset-tag">

```text
deviantart
Flame
Digital painting of a fiery dragon with glowing yellow eyes, black horns, and a long sinuous tail, perched on a glowing molten rock formation. The background is a gradient of dark purple to orange.
```

*Why: the "deviantart" dataset tag on its own line (with an optional title on the next) switches the model toward its non-anime art training; use "ye-pop" the same way for general illustration*

</example>

## Text rendering

<rules id="text">

- Text is a weak point. The model can usually render a single word, and sometimes a short phrase, but longer strings break down.
- Keep any in-image words to one short string. Quoting the word and welding it to an object (a sign, a badge) is fine, but do not expect pixel-exact multi-word text.
- For anything longer than a word or two, add the text in an editor after generation.

</rules>

<example use_case="single-word">

```text
masterpiece, best quality, score_8, safe, 1girl, holding a cardboard sign that says "HELLO", simple background, looking at viewer
```

*Why: a single short word is about the model's text ceiling; keep it to one word, welded to an object, and do not expect a clean longer phrase*

</example>

## Negative prompts and exclusions

<rules id="negatives">

- Negatives are real on `anima-base` and worth using; it runs with classifier-free guidance. The owner's default negative is "worst quality, low quality, score_1, score_2, score_3, artist name, blurry, jpeg artifacts, chromatic aberration".
- ON `anima-turbo` they are not. The distilled tier runs at CFG 1, and with no guidance there is nothing for an exclusion to push against, so the field is decoration. State the positive that displaces the unwanted element, or generate that image on base.
- ON `anima-aesthetic` keep the negative but drop the score tags out of it, the same as out of the positive.
- Mirror your safety intent: if the positive prompt is "safe", put "sensitive, nsfw, explicit" in the negative to hold content down. Short or vague prompts are the main cause of unwanted content, so combine safety negatives with a detailed positive.
- "artist name" in the negative suppresses signature and watermark text; keep it there for clean output.
- Add the specific artifacts you actually see ("extra fingers, bad hands, jpeg artifacts") rather than piling on generic words.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Missing @ on artists: an artist tag without "@" barely registers; always write "@artist name".
- Underscores in tags: use spaces ("blonde hair"), not underscores, except score tags ("score_7").
- SDXL-strength weights: weighting needs to be pushed harder than on SDXL; "(tag:1.1)" does little, try "(tag:2)".
- Too-short prompt: a bare one-line prompt invites unwanted or off-model content; add detail and safety tags.
- Expecting realism: Anima is anime and illustration only and will not do photographs; use a different model for photoreal.
- Long in-image text: only a word or two renders; do not ask for sentences, add them in an editor.
- Naming characters without describing them: list a character's hair, eyes, and outfit too, especially with multiple characters, or the model mixes them up.
- Plain, flat output: that is the base model with no quality or artist tags; add a quality system and an artist to give it a look.
- Carrying a base prompt onto Aesthetic unchanged: the score tags travel with it, and the owner warns they push that tier toward slop; strip score_* from both sides.
- Writing a negative prompt for Turbo: at CFG 1 nothing is pushed away, so displace the unwanted element with a positive or switch to base for that image.
- Treating the 2.9B as a CircleStone release: it is a community layer expansion at preview stage, and where its card is silent the base rules govern.

</rules>

## Sources

Trust order: official beats provider beats community, and official wins on any conflict. Anima has no approved-provider hosting (its license forbids paid API hosting), so the rules come from the owner's own materials, plus one community derivative recorded as such.

- Official (CircleStone Labs / Comfy Org): the [Anima model card](https://huggingface.co/circlestone-labs/Anima), which is the source of the tag-section order, the quality and safety vocabularies, the per-tier line-up and the Aesthetic score-tag warning, the Turbo settings and the default negative; the [ComfyUI Anima tutorial](https://docs.comfy.org/tutorials/image/anima/anima); [Anima on CivitAI](https://civitai.com/models/2458426/anima).
- Community: the [Anima-2.9B model card](https://huggingface.co/Gazingstars123/Anima-2.9B), the source of everything attributed to that derivative: the layer expansion, the absent score captions, the character-plus-series rule and the prompt-detail advice. It is authoritative for its own weights only and never overrides CircleStone on the rest of the line.

Last verified: 2026-09-04.
