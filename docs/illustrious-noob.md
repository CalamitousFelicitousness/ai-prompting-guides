---
guide: "Illustrious and NoobAI"
prompt_scheme: "illustrious-noob"
models:
  - { id: "illustrious-xl-v2.0", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "latest stable Illustrious; the strongest natural-language plus Danbooru-tag mix and high-resolution illustration" }
  - { id: "illustrious-xl-v1.0", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "widely finetuned Illustrious base; Danbooru tags with solid natural-language support" }
  - { id: "illustrious-xl-v0.1", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "the original research base; the ancestor most anime SDXL finetunes and LoRAs (and NoobAI) are built on" }
  - { id: "noobai-xl-1.1", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "NoobAI eps-prediction; full Danbooru plus e621 knowledge with a documented quality, aesthetic, and date-tag system" }
  - { id: "noobai-xl-vpred-1.0", access: "open-weights", tier: "base", caps: [text-to-image], best_for: "NoobAI v-prediction; richer contrast and color range, but must run in a v-prediction-aware host" }
capabilities: [text-to-image]
prompt:
  languages: ["en"]
  literal_text: "not a strength; these are SDXL anime models, not text-rendering models, and there is no quoting convention; avoid in-image text and add any words in an editor afterward"
  length_strategy: "native interface is a comma-separated Danbooru (and e621, on NoobAI) tag list in a fixed section order; lead with tags and support them with natural language (Illustrious v1.0+ and NoobAI read sentences too); quality, aesthetic, and date tags steer fidelity, and a strong negative prompt is part of every prompt"
  negatives: "essential and recommended (these are CFG-guided SDXL models): both families ship a recommended negative; NoobAI's adds e621-suppression tags (mammal, anthro, furry, ambiguous form, feral, semi-anthro) to keep output in anime form"
  auto_expand_behavior: "none in the weights; Illustrious's own platform offers optional Tag Booster (TIPO) and Mood Enhancer (natural-language expansion) as host features, so write the full prompt yourself unless a host expands it"
sources:
  official: ["https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0", "https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.0", "https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0", "https://www.illustrious-xl.ai/updates/21", "https://www.illustrious-xl.ai/updates/20", "https://huggingface.co/Laxhar/noobai-XL-1.1", "https://huggingface.co/Laxhar/noobai-XL-Vpred-1.0"]
  provider: []
  community: []
last_verified: "2026-06-21"
---

# Illustrious and NoobAI: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For samplers, steps, CFG, resolutions, and v-prediction setup, consult each model card; those are runtime settings and out of scope here.
- It covers two SDXL booru-tag families that share one prompt scheme: Illustrious-XL (OnomaAI, trained on Danbooru) and NoobAI-XL, also written NoobXL (Laxhar, trained on Danbooru plus e621). NoobAI is a finetune of Illustrious-XL v0.1, so a prompt written for one transfers to the other.
- The native interface is a comma-separated Danbooru tag list in a fixed section order, not a sentence. Natural language is supported (Illustrious v1.0 and later, and NoobAI) and can be mixed with tags, but tags lead.
- These are anime and illustration models. They are not realism models, and they are not text-rendering models.
- They are text-to-image with no input image, so there is no editing or multi-image section; those are N/A and omitted.
- Negative prompts are essential here (CFG-guided SDXL); both families ship a recommended negative, and a prompt without one underperforms.
- The two families differ in capability, not grammar. NoobAI adds e621 knowledge (more characters and artists, plus furry and anthro content) and a documented quality, aesthetic, and date-tag system; Illustrious leans on aesthetic tags. These differences are called out inline below.

</rules>

## TL;DR

<template id="quickstart">

Positive: masterpiece, best quality, newest, safe, {1girl/1boy/count}, {character} \({series}\), {artist:name}, {appearance and clothing}, {expression}, {pose}, {setting}, {a few general or meta tags}

Negative: worst quality, low quality, lowres, bad anatomy, bad hands, signature, jpeg artifacts {on NoobAI, also add nsfw, mammal, anthro, furry, feral to keep it pure anime}

</template>

## Models and when to use which

- Illustrious lineage (Danbooru only): `v0.1` is the original untuned research base and the ancestor of most anime SDXL finetunes and of NoobAI. `v1.0` and `v1.1` add high-resolution illustration and stronger natural-language support. `v2.0` is the latest stable checkpoint with the best natural-language alignment. `v3.0` and `v3.5` add eps and v-prediction variants with better color control, rolling out over time.
- NoobAI lineage (Danbooru plus e621): built on Illustrious v0.1. The eps-prediction models (`1.0`, `1.1`) are the default. `Vpred-1.0` is the v-prediction model with richer contrast and color, but it must run in a v-prediction-aware host or it renders wrong.
- Pick Illustrious for clean anime and illustration and the broadest LoRA ecosystem. Pick NoobAI when you want e621 breadth (more characters and artists, or deliberate furry and anthro) or its documented tag system. The prompt grammar is identical across all of them, including eps versus v-prediction.
- All of these are untuned base models with no default style. Quality, aesthetic, and artist tags are what give an image its look; without them the output is plain by design.

## How the models read prompts

- Tags are primary. Write them in lowercase and comma-separated. Spaces and underscores both work for multi-word tags; for artist handles, match the Danbooru or e621 spelling, which is usually underscored (`artist:john_kafka`).
- Earlier tags carry more weight, so lead with the tags that matter most. Within a tag section the order is flexible.
- Use Danbooru and e621 parenthetical disambiguation: a character with its series (`arlecchino (genshin impact)`), or an ambiguous word with its sense (`horror (theme)`, `graphite (medium)`). In hosts that read parentheses as emphasis (A1111, Comfy, reForge), escape literal parentheses as `\(` and `\)`.
- Standard SDXL emphasis works to push or pull a tag (`(detailed background:1.2)`); unlike some Danbooru models these do not need unusually high weights.
- Artists: NoobAI documents the `artist:name` form and stacking several blends their styles; Illustrious also takes plain Danbooru artist names. More artists means more blending and less consistency, so start with one or two.
- Natural language is supported alongside tags on Illustrious v1.0 and later and on NoobAI (v2.0 improved it). Lead with tags, then add a sentence or two for scene and mood. Name a character, then describe their appearance, especially with multiple characters, or the model mixes them up.
- Quality, aesthetic, and date tags are levers, not decoration; see the vocabulary below.
- Some hosts expand prompts for you (Illustrious's platform has a TIPO-based Tag Booster and a natural-language Mood Enhancer). That is a host feature, not part of the weights; write a full prompt unless you are relying on it.

## Prompt structure

<rules id="structure">

- Order the prompt as a prefix of fidelity tags, then the subject block: quality tags, aesthetic tags, date tag, meta tags, and rating, then the count (1girl, 1boy, 1other, 2girls), then character, then series, then artist, then the general tags.
- Lead with a quality prefix. NoobAI's documented prefix is "masterpiece, best quality, newest, absurdres, highres, safe,"; Illustrious uses the same quality words and adds aesthetic tags like "very aesthetic" or "extremely aesthetic".
- Set a rating tag (safe, sensitive, nsfw, explicit) in the positive prompt and put the ones you want suppressed in the negative.
- Add a date tag to steer the era of the art style: a year (`year 2024`) or a period word (newest, recent, mid, early, old).
- Keep composition tags deliberate. Use one clear framing tag (upper body, cowboy shot, portrait, full body) and do not stack conflicting ones (close-up, upside-down, cowboy shot together), which confuses the model.
- Always pair the positive prompt with a negative; on these models the negative does as much work as the positive.

</rules>

<template id="general">

{quality tags}, {aesthetic tags}, {date tag}, {meta tags}, {rating}, {count}, {character} \({series}\), {artist:name(s)}, {hair and eyes}, {clothing and accessories}, {expression}, {pose and framing}, {setting and background}, {extra general tags}

</template>

<example use_case="single-character-full-tags">

```text
Positive: 1boy, holding knife, blue eyes, jewelry, jacket, shirt, open mouth, hand up, simple background, hair between eyes, vest, knife, tongue, holding weapon, grey vest, upper body, necktie, solo, looking at viewer, smile, pink blood, weapon, dagger, open clothes, collared shirt, blood on face, tongue out, blonde hair, holding dagger, red necktie, white shirt, blood, short hair, holding, earrings, long sleeves, black jacket, dark theme
Negative: worst quality, comic, multiple views, bad quality, low quality, lowres, displeasing, very displeasing, bad anatomy, bad hands, scan artifacts, monochrome, greyscale, signature, twitter username, jpeg artifacts, 2koma, 4koma, guro, extra digits, fewer digits
```

*Why: the documented Illustrious tag order in practice, count first then a free-order pile of subject, clothing, and action tags (a quality word like "masterpiece" can lead or trail), with a heavy negative carrying the quality floor and artifact suppression these SDXL models depend on*

</example>

## Tag vocabulary

<rules id="vocab">

- Quality tags (shared word ladder): masterpiece, best quality, good quality, normal quality, low quality, worst quality. Illustrious also recognizes "average quality", "bad quality", and the disambiguated "masterpiece (quality)". NoobAI maps these to image-popularity percentiles (masterpiece is the top 5%, worst quality the bottom 30%), so they track recent user preference rather than raw skill.
- Aesthetic tags: Illustrious uses "very aesthetic", "extremely aesthetic", and color cues like "very vibrant colors". NoobAI adds its own waifu-scorer aesthetic tags, led by "very awa" (the top 5% aesthetic) and "worst aesthetic" (the bottom 5%).
- Date tags: a specific year (`year 2024`) or a period word. NoobAI's documented period mapping is old (2005-2010), early (2011-2014), mid (2014-2017), recent (2018-2020), newest (2021-2024). Newer periods skew toward current rendering and shading.
- Rating tags: safe, sensitive, nsfw, explicit. Set the one you want and suppress the rest in the negative.
- Meta tags: highres, absurdres, lowres, official art, and similar format and fidelity tags.
- Artist tags: `artist:name` (NoobAI) or the plain Danbooru artist handle; stack a few to blend styles, knowing more artists drift the result.
- These are not Pony models: do not use the `score_9, score_8, ...` aesthetic ladder here. Use the word-quality and aesthetic tags above.
- NoobAI e621 layer: NoobAI also knows e621 tags, e621 artists, and furry and anthro forms. To keep output in human anime form, keep the anti-furry tags (mammal, anthro, furry, ambiguous form, feral, semi-anthro) in the negative; to draw furry or anthro on purpose, drop them and add the e621 species and form tags you want.

</rules>

## By use-case

<example use_case="noobai-multi-artist-style">

```text
Positive: masterpiece, best quality, artist:john_kafka, artist:nixeu, artist:quasarcake, chromatic aberration, film grain, horror \(theme\), limited palette, x-shaped pupils, high contrast, color contrast, cold colors, arlecchino \(genshin impact\), black theme, gritty, graphite \(medium\)
Negative: nsfw, worst quality, old, early, low quality, lowres, signature, username, logo, bad hands, mutated hands, mammal, anthro, furry, ambiguous form, feral, semi-anthro
```

*Why: NoobAI's style comes from stacked `artist:` tags, here three blended; the character carries its series in escaped parentheses, and medium and theme tags (`graphite (medium)`, `horror (theme)`) use the same disambiguation, all over the standard NoobAI negative*

</example>

<example use_case="natural-language-plus-tags">

```text
masterpiece, best quality, very aesthetic, newest, safe, 1girl, solo, long silver hair, blue eyes, white dress, standing on a cliff overlooking the sea at sunset. Wind moves through her hair and the tall grass, warm golden light catches the dress, distant sailboats sit on the horizon. wide shot, scenery, detailed background
```

*Why: tags carry quality, aesthetic, date, rating, and the core subject, then a natural-language sentence adds the scene and atmosphere; Illustrious v1.0 and later and NoobAI both read this tag-plus-sentence hybrid*

</example>

<example use_case="noobai-e621-suppression">

```text
Positive: masterpiece, best quality, newest, absurdres, highres, safe, 1girl, solo, fox ears, fox tail, orange hair, kimono, holding a paper fan, cherry blossoms, looking at viewer, upper body
Negative: nsfw, worst quality, old, early, low quality, lowres, signature, username, logo, bad hands, mutated hands, mammal, anthro, furry, ambiguous form, feral, semi-anthro
```

*Why: NoobAI's e621 training can pull "fox ears" toward a full anthro fox; the anti-furry negative (mammal, anthro, furry, feral, semi-anthro) holds the fox-eared girl in human anime form, which Illustrious does not need*

</example>

## Text rendering

<rules id="text">

- In-image text is not a strength of either family; these SDXL anime models were not trained to render legible words, and there is no quoting convention.
- Do not rely on them for signs, titles, or captions. If a short word slips in, treat it as decorative, not dependable.
- For real typography, leave space and add the text in an editor after generation.

</rules>

## Negative prompts and exclusions

<rules id="negatives">

- Treat the negative as half the prompt. A documented Illustrious negative is "worst quality, comic, multiple views, bad quality, low quality, lowres, displeasing, very displeasing, bad anatomy, bad hands, scan artifacts, monochrome, greyscale, signature, twitter username, jpeg artifacts, 2koma, 4koma, guro, extra digits, fewer digits".
- NoobAI's recommended negative is "nsfw, worst quality, old, early, low quality, lowres, signature, username, logo, bad hands, mutated hands, mammal, anthro, furry, ambiguous form, feral, semi-anthro". The trailing furry and anthro tags are the e621 suppressors; keep them for pure anime, drop them when you want furry or anthro.
- Mirror your rating: if the positive is "safe", put "nsfw, explicit" in the negative. The quality floor ("worst quality, low quality, lowres") and artifact tags ("jpeg artifacts, signature, username") belong in almost every negative.
- Add the specific artifacts you actually see ("bad hands, extra digits") rather than piling on generic words.

</rules>

## Pitfalls and anti-patterns

<rules id="avoid">

- Skipping the negative: these models lean on it; an empty negative gives soft, low-quality output. Always include a quality-floor negative.
- Expecting realism: both families are anime and illustration only; use a different model for photoreal.
- Wrong quality system: do not use Pony `score_9` tags here; use the word-quality and aesthetic tags (masterpiece, very aesthetic, very awa).
- Unescaped parentheses: in emphasis-parsing hosts, literal parens in tags must be `\(` and `\)`, or `(series)` is read as emphasis.
- Conflicting composition tags: stacking close-up, upside-down, and cowboy shot confuses framing; pick one.
- NoobAI furry bleed: animal-ear or tail tags can drift to full anthro; keep the anti-furry negative unless you want it.
- v-prediction in the wrong host: NoobAI Vpred and the Illustrious v-pred variants need a v-prediction-aware host or they render washed out; the prompt grammar is unchanged, only the runtime is.
- Naming characters without describing them: give hair, eyes, and outfit too, especially with multiple characters, or the model conflates them.
- No-style flatness: that is the untuned base; add quality, aesthetic, and artist tags to give it a look.

</rules>

## Sources

Trust order: official beats provider beats community, and official wins on any conflict. Both families are owner-published and non-commercially licensed, and neither is hosted by an approved provider, so the rules come from the owners' own materials. Illustrious and NoobAI agree on the shared grammar; where they differ it is NoobAI's e621 layer and quality and aesthetic vocabulary, noted inline above.

- Official (OnomaAI, Illustrious): [Illustrious-XL-v2.0](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v2.0), [Illustrious-XL-v1.0](https://huggingface.co/OnomaAIResearch/Illustrious-XL-v1.0), [Illustrious-XL v0.1](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0), [ILXL image generation user guide](https://www.illustrious-xl.ai/updates/21), [ILXL model series](https://www.illustrious-xl.ai/updates/20).
- Official (Laxhar, NoobAI): [NoobAI-XL 1.1](https://huggingface.co/Laxhar/noobai-XL-1.1), [NoobAI-XL V-Pred 1.0](https://huggingface.co/Laxhar/noobai-XL-Vpred-1.0).

Last verified: 2026-06-21.
