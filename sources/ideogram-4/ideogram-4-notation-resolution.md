# Ideogram 4 and 4.5: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08 at the recheck. New sources this pass: Ideogram's help docs
(`docs-*.md`, curl of the GitBook `.md` twins listed in `docs.ideogram.ai/llms.txt`), the v2 API reference
(`dev-*.md`, `.md` twins listed in `developer.ideogram.ai/v2/llms.txt`), the 4.5 model page, the 4.5 product-editing
and 4.0 JSON-prompting blog posts, fal's 4.5 pages, and the open repo's prompting guide as of its 2026-06-30 commit
(`github-ideogram4-prompting-guide-2026-06-30.md`). Two parallel digests read the docs and API pages.

## 1. One scheme for open Ideogram 4, hosted 4.0 and 4.5

Ideogram: "Ideogram 4.5 and 4.0 accept a plain-language prompt or a structured JSON prompt. Both models use the same
JSON format" (json-prompting), and the 4.5 API prompt field takes "a structured Ideogram 4.0 JSON prompt". The 4.5
edit is a different prompt role on the same model (an instruction, with references and masks), so it is a section
in this guide, not a second scheme. Hosted 4.0 is the open model on Ideogram's service: no row of its own, described
in Models. Ideogram 3.0, 2a and 2.0 are plain-text models with a negative prompt and style settings: separate
guide `ideogram-3`.

## 2. Owner correction to the open release (2026-06-30)

The repo's prompting guide changed from "You can pass in plain-text prompts directly to the model and it will work"
to "Passing in plain-text prompts directly to the model will not work and will likely trigger a safety warning.
Plain-text prompts should be run through a magic prompt". The schema note that "the model accepts any string" was
removed. The guide's earlier "plain text works but underperforms" is replaced with an access split.

## 3. Hosted leniency vs the open schema (owner vs owner)

The repo governs the caption, since it defines what the model was trained on; the hosted docs describe what
Ideogram's service tolerates. Taught: the strict form, which is valid everywhere, with hosted behaviour as notes.
- Key order: repo strict with a verifier; hosted docs "Ideogram puts the keys inside each block in the order the
  model expects, so you don't need to".
- Hex case: repo uppercase only; hosted "accepts uppercase or lowercase".
- `high_level_description`: repo optional but strongly recommended; hosted reads JSON without it as plain text.
  Taught: always include it.
- style subfields: repo requires aesthetics, lighting, medium when the block is present; hosted "Every field is
  optional". Taught: the repo rule.
- How much JSON matters: repo required; hosted "Plain language works well for most images" because the service
  converts it. Access split.

## 4. Reference notation for 4.5

The app inserts `@img_N` pills, and the docs warn "The labels shown in your prompt can differ; select the actual
pills rather than typing a guessed file name". The API documents no in-prompt tag, only order ("The first image is
the one being edited; any others are extra references"; precise-edit references "are never edited themselves").
Taught: pills in the app, name by content through the API. Examples keep the owner's `@img_N` form.

## 5. Examples

Owner verbatim: the keyboard edits 1 and 2 (em dashes made ASCII), the shoe colorway and toaster strawberries edits
(blog), the living-room relight and the restoration prompt (masks docs), the bottle-into-scene and cafe character
prompts (reference-images docs), the NORTHWIND starting prompt (prompt-structure docs), and the mantis shrimp card
(JSON prompting blog). Guide-built to owner rules: the three-reference composite, pure style transfer, and style
transfer plus a text edit (the owner lists "Style reference" as a 4.5 edit kind but publishes no prompt for it).
The open release's examples are unchanged.

## 6. Kept out

Prices, quality-mode names, reference and mask slot counts, palette color caps (16 global, 5 per element), the
10,000-character prompt cap, sizes and pixel budgets, context-window coordinates, and the 2K and 8K figures.
