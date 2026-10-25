# MOSS-Image: structure decision and source notes

Not a scrape. Hand-authored 2026-10-25 from the owner surfaces in this folder.

- `hf-moss-image-{SFT,Base}-README.md`: Hugging Face model cards.
- `gh-*`: the OpenMOSS/MOSS-Image GitHub repository: README (EN/ZH), USERGUIDE (EN/ZH, titled "MOSS-Image-Base
  User Guide"), the prompt-enhancer skill with its layout reference and `compile_prompt.py`, the Gradio app and
  its `prompt_defaults.txt`, and `gh-examples/0NN.json`, the twenty showcase `parameters.json` files.
- `hf-pipeline_moss_image.py`: the custom Diffusers pipeline. The prompt is wrapped as one user message in the
  Qwen chat template with no system prompt; nothing rewrites it.
- `arxiv-2610.23374.md`: the technical report, with tables recovered from the LaTeX source.

No approved provider (FAL, WaveSpeed) lists the model, so the guide is owner-only.

## 1. Scope and scheme

One scheme, `moss-image`, for MOSS-Image-SFT (tier `std`) and MOSS-Image-Base (tier `base`). Same architecture,
pipeline and prompt forms; they differ in settings, which live in the spec table. Text-to-image only: the
report's Limitations section says the backbone "does not directly condition on reference images or support
image editing". Community distillations (lodestones DMD, akhaliq 4-step) and edit LoRAs are out of scope.

## 2. Layout coordinates: report against released surfaces. RESOLVED.

- Report, App. C.3: summary/items boxes were converted "to normalized [0,1000] yxyx coordinates". The
  scene/element branch sampled normalized, absolute and centre-relative coordinates 0.4/0.3/0.3. The report's
  own enhancer emitted normalized top-left boxes. App. K says zero-centred absolute boxes generalize better to
  unseen resolutions.
- User guide, model cards, enhancer skill and `compile_prompt.py`: `bbox_format: "yxyx"`,
  `bbox_coord_space: "abs_centralized"`, absolute pixels from the canvas centre.
- Showcase: all five JSON prompts (001, 002, 004, 011, 014) carry `abs_centralized` boxes; the summary/items ones
  also carry `yxyx`.

Resolved on the released usage surfaces, which describe the shipped checkpoints; the report describes the
pretraining run. Taught: centre-origin pixels with both markers present, compact one-line JSON as the compiler
emits it. The compiler floors top/left and ceils bottom/right before subtracting the centre; the guide's cup
example was produced by running it on the owner's draft.

## 3. Two layout schemas. RESOLVED.

- summary/items: user guide, cards, enhancer ("The public MOSS-Image Layout vocabulary is `summary` plus a flat
  `items` array. Use this one schema for new drafts."). Labels in the compiler: `object`, `character`, `text`.
- scene/element (`scene_type`, `gen_brief`, `elements` with `type`, `salience`, `identity`, `bbox`): report
  Figure 6a, and showcase 001 and 004. The report lists types `obj`/`text` and salience `primary`/`secondary`;
  the showcase adds `panel` and `background`.

Taught: summary/items only. scene/element is recorded, not taught. The showcase's extra labels (`panel`,
`subject`) are noted for `panel` only, since that is the one with a clear job (a full-frame background region).

## 4. Tag prompts. RESOLVED, with a caveat.

User guide: tag order "Quality -> Score -> Meta -> Year -> Character -> Series -> Artist -> General", artist as
`@foo bar`. Showcase 009 and 019 use tags. The report lists sixteen pretraining sources and none is a booru set,
and says nothing of tags. Taught as supported (the user guide is the usage surface), with prose as the primary
interface and the report's silence stated.

## 5. Negative prompts. RESOLVED.

User guide (Base): "nsfw, worst quality, bad anatomy, watermark, jpeg artifact". SFT card: "Negative prompt |
Empty". Gradio defaults: prefix "best quality, masterpiece", the same negative list. Showcase negatives vary per
image and are sometimes empty. The report: "Annotate rather than filter" (artifacts are described in captions),
which is why artifact words carry meaning. Taught: Base list, SFT empty by default, concrete artifact words only,
image-specific exclusions as a closing prompt sentence.

## 6. Text and line breaks

User guide: insert `\n` or real line breaks. Report: explicit breaks resolve row ambiguity during denoising
(App. J); long captions present text as "reads:" plus line-broken text; JSON carries escaped `\n`. Taught: real
breaks inside quotes in prose, `\n` in JSON. The guide's wording "reads exactly:" is the owner's showcase 018.

## 7. Example provenance and edits

- Fridge note: model card and user guide; the user guide's curly quotes made straight.
- Chalkboard: showcase 018; one em-dash made a comma.
- Convenience store: showcase 020, verbatim.
- MOSI whiteboard: user guide, verbatim.
- Tag order: user guide, verbatim. Rhodes Island tags: showcase 009, verbatim including "carring".
- EXPLORE poster: user guide, compacted to one line. Ceramic cup: enhancer `references/layout.md`, compiled.
