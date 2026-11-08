# Ideogram 3.0: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08. The raw sources live beside the Ideogram 4 ones in `../ideogram-4/`
(`docs-prompting-*.md`, `docs-create-image-settings.md`, `docs-create-models.md`, `docs-edit-remix.md`,
`docs-organize-and-share-characters.md`, and the `dev-api-reference-images-*-ideogram-3*.md` and `-ideogram-2a.md`
API pages), fetched as GitBook and API `.md` twins in the same pass.

## 1. Own scheme

3.0 is plain text only ("Text" in the models table; the prompting pages say to start with plain language on 3.0),
has a negative prompt, style type, presets, style codes, style references and a palette that no 4.x model has
("Ideogram 3.0 is the only model with style presets, style reference images, negative prompts and color
palettes"), and its edit prompts are descriptive: inpaint "The prompt describing the repainted result", remix
"describe the complete image you want", replace background "Plain-language description of the desired new
background". Ideogram 4.5 edits are instructions. Splitting avoids a guide that teaches both edit grammars.

## 2. Shared craft, scoped

The docs.ideogram.ai prompting pages cover "Ideogram 4.5, Ideogram 4.0 and Ideogram 3.0" together. Rules without a
model attached are taught here (sentence form, main idea first, quoting text, describing lettering, describing the
absence, refine-and-iterate). Rules scoped to 4.x (JSON, bboxes, hex palettes per element) are not.

## 3. Length ceiling

prompt-structure: "keep plain-language prompts under about 150 words (roughly 200 tokens). It may weaken or ignore
words past that point" for 3.0. Kept as a craft rule with the figure, since it is the owner's statement of how the
model reads a prompt, not a host limit.

## 4. Legacy rows

2a and 2.0: "may still appear in the picker. For new work, use Ideogram 4.5 or 4.0." Rows with tier `legacy` and
caps `text-to-image` only; no owner text-rendering statement for them was in the fetched pages. 2a's API page shows
a plain prompt, style_type, no negative prompt, style references or palette.

## 5. Examples

Owner verbatim: the perfume and watercolor long-form prompts, the Welcome lettering line, the jazz poster, the
Picasso risograph poster (its en dash made ASCII), and the mug remix. Guide-built to owner rules: the content-only
fox for style references, the remix pure style transfer and style-plus-banner, the inpaint result description, the
character scene, and the empty-street absence. The 3.0 API pages carry placeholder prompts only.

## 6. Kept out

Preset counts and names, palette preset names and hex-count caps, style-reference counts, rendering speeds,
aspect-ratio lists, image strength scale, character mask mechanics, plan gating.
