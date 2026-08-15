# HunyuanImage: structure decision and source notes

Not a scrape. Hand-authored 2026-08-07 from the sibling scrapes in this folder. First Tencent guide in the
set, and the first where the owner surface is a GitHub repo and a Hugging Face card rather than a docs site.

## 1. One guide for the family

`guides/hunyuan-image.md`, scheme `hunyuan-image`, covering `HunyuanImage-3.0` (base), the Instruct
checkpoint, and the distilled Instruct checkpoint.

All three are the same architecture: Hugging Face reports `hunyuan_image_3_moe` and the same parameter count
for every card. The owner's prompt guide gives one prompt spine and never splits it by checkpoint. The
differences are what happens around the prompt, not how it is written:

| | Base | Instruct / Distil |
| --- | --- | --- |
| Text-to-image | yes | yes |
| Prompt self-rewrite | no | yes |
| Reasoning before drawing | no | yes |
| Image editing | no | yes |
| Multi-image fusion | no | yes |

That is capability, so it merges, same as Seedream 4.5 plus 5.0-lite and the Qwen 3.0 pass. The guide marks
the editing and fusion sections as Instruct capabilities rather than splitting the file.

Named at family level, matching `gpt-image.md` and `gemini-image.md`.

## 2. The rewrite pipeline is the thing to teach, without naming the knob

The owner documents a staged pipeline: think, then recaption, then image. The base checkpoint has none of
it, which the prompt guide states in its first line: "The Pretrain Checkpoint does not automatically rewrite
or enhance input prompts, Instruct Checkpoint can rewrite or enhance input prompts with thinking."

The specific selectors are out of scope in full, as parameter names always are. What is kept is the portable
consequence, which is genuinely load-bearing here:

- A sparse brief is expanded for you on the instruct path, which is why a one-line prompt still yields a
  detailed image.
- A prompt you worded carefully can come back restated, so exact wording needs the direct path.

That is the same treatment given to Gemini's thinking level and Krea's creativity enum: state the behavior,
drop the enum. The guide's frontmatter carries it under `auto_expand_behavior`, which is what the house
template's slot is for.

Also dropped, deliberately: the repo ships two DeepSeek system prompts (`system_prompt_universal` and
`system_prompt_text_rendering`) for expanding prompts offline before sending them. Those are repo artifacts
and a second model's prompts, not this model's prompt craft. The fact they exist is evidence for the
"this model expects an expanded prompt" rule, which the guide states directly instead.

## 3. Long prompts, which inverts the most recent guide in the set

Worth flagging because it lands next to HappyHorse, where the rule is roughly twenty words.

The owner states it plainly: "Our model can effectively process very long text inputs, enabling users to
precisely control the finer details of generated images." Its eight published reference prompts run several
hundred words each. Both rules are correct for their own model and neither generalizes, which is now a
recurring finding in this repo rather than a surprise.

Two structural patterns were extracted from those reference prompts rather than from any prose rule, because
the owner demonstrates them without describing them:

- **One axis per paragraph.** Every English reference prompt runs overall shot and mood, then subject, then
  environment, then lighting, separated by blank lines.
- **A closing style sentence.** Every one ends on a single line naming the overall look, for example "The
  overall image presents a cinematic, photorealistic photography style." It is consistent enough across
  eight independent examples to teach as a rule.

## 4. Reference notation: inferred from a Chinese example, and flagged as such

The only documented multi-image instruction in the owner's material is in Chinese:

> 基于图一的logo，参考图二中冰箱贴的材质，制作一个新的冰箱贴

That addresses inputs by ordinal position (图一, 图二 = image one, image two), assigns one role to each, and
ends by naming the artifact to produce. The guide teaches the English equivalent as `Image 1` and `Image 2`,
bare, with no at-sign and no brackets.

**This is an inference, not a quoted English form, and the guide's coverage note says so.** Given that this
repo has now catalogued five different reference notations across the set, with Wan splitting by mode inside
a single model, an inferred notation is exactly the kind of claim that should carry its uncertainty in
public. Re-check when Tencent publishes an English multi-image example.

The ordinal-position form is at least consistent with the family it resembles most: Qwen, Seedream and
Kling Image all use bare `Image N`.

## 5. No negative prompt field

Checked across the owner repo, both model cards, and WaveSpeed's guide. Nothing exposes one, and WaveSpeed
hedges its own mention as "if supported by the API", which is a provider guessing rather than documenting.
Treated as absent, and the guide routes exclusions into the positive prompt, matching the FLUX.2, Gemini,
Krea and HappyHorse treatment.

## 6. Sources: an open-weights owner surface

New for this repo: the authoritative prompt guidance lives in the model's own GitHub repository
(`Hunyuan-Image3.md`) and its Hugging Face cards, not on a docs site. CLAUDE.md's source-quality bar has been
extended to say so, since the same will apply to any future open-weights release.

## 7. The Prompt Handbook, and how it was eventually read

`https://docs.qq.com/doc/DUVVadmhCdG9qRXBU`, linked from the repo guide, is the richest owner source and was
initially skipped as unreachable. It was recovered, and it changed the guide in three places. Recording the
route because the same obstacle will recur with any Tencent Docs or canvas-editor source.

What did NOT work:

- firecrawl: returns the shell only.
- DOM text: the document renders to five canvases; `document.body.innerText` is 366 characters of UI chrome.
- The network payload: content arrives over a websocket, not a fetchable JSON endpoint.
- Internal JS state: `openDocResponseText` holds only metadata; the editor model uses minified property
  names and a recursive walk of `pad.editor.root` found no text nodes.
- The printed PDF's text layer: 7,560 text operators but zero `/ToUnicode` maps and no embedded fonts, so
  the strings are raw glyph indices (`\x00`, `\x02`) with no route back to characters.

What DID work, in two stages:

1. **Playwright plus the accessibility toggle.** The page advertises `control + ~` for screen-reader support.
   Enabling it exposes the outline in the DOM, which gives the section list and the 12,369-word count, and
   the sidebar entries are clickable to jump section by section. Screenshots are then readable.
2. **Ghostscript on a print-to-PDF.** `gs -sDEVICE=png16m -r150` renders pages, then a 90-degree rotation
   with ImageMagick makes them upright. Neither poppler nor pdftotext was installed and neither was needed.
   Some pages are mangled where captions overprint each other, but the Chinese tables render cleanly.

Three changes to the guide came out of it:

- **A universal formula that is not the five-part spine.** The handbook opens with "avoid tag-form prompts,
  use natural language to describe the imagined scene", then gives subject plus action plus scene as the
  universal formula. The five-part spine appears one level down, as the technique line for the scenario
  playbooks. The guide now carries both and says which is which.
- **The closing style sentence is owner-STATED, not inferred.** Section 3 of this note previously recorded it
  as a pattern mined from examples. The sticker template states it as an explicit step: re-emphasize the
  style at the end to strengthen the overall style response. Upgraded from inference to documented rule.
- **Long text is a capability, not a limit.** The guide had carried WaveSpeed's advice to keep rendered
  strings short. The handbook has a whole `长文本渲染` section with its own tips block: split a long passage
  into multiple sentences with multiple quoted strings, prefix each with a position label ("the Nth line
  reads"), and if accuracy fails change the aspect ratio or reorganize the layout. Owner beats provider, so
  the short-strings advice was removed.

The unifying insight, which the handbook shows across three separate sections, is that position labels are
the mechanism for all structured output. Long text, comic panels and sticker grids are the same technique:
say where the element sits, then say what it is.

WaveSpeed is the only approved provider with substantive coverage, and it contributes the text-rendering
checklist (quote the exact string, describe the type treatment, name the surface, keep it short, state the
language) plus the conflicting-instruction pitfall ("photorealistic anime"). None of it contradicts the
owner. fal is listed as an inference provider on both Hugging Face cards but had no prompting article.
