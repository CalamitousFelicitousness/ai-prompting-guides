# FLUX 3 Image: structure decision and source notes

Not a scrape. Hand-authored 2026-10-15 from the owner surfaces in this folder: the Klein and Klein Base
model cards, the prompt upsampler card and its `system_prompts.json` (keys `t2i`, `i2i`, `t2i_bbox`,
`i2i_bbox`), the reference repository README and its `bbox.py`, `pup.py` and `generate.py`, the Klein
launch post, and the `.md` twins of the BFL docs pages for FLUX 3 Image and the shared prompting guides.
`*.clean.md` copies have the Mintlify `export const` blocks stripped; worked examples live in those blocks,
so read the raw file for examples.

## 1. A new scheme, `flux-3-image`

FLUX 3 Image gets its own guide rather than joining `flux-2` or `flux-3-video`.

- Against `flux-2`: FLUX.2 has a whole-prompt JSON schema and documents hex codes in text-to-image; FLUX 3
  Image has neither (its only JSON is the bounding-box element table, and hex appears only in edits). The
  reference notation differs, and so does the expansion default: FLUX.2 [klein] never upsamples, while
  FLUX 3 Image always does on the API. One guide would contradict itself on four rules.
- Against `flux-3-video`: the modality split, the same call as Wan image versus Wan video. The video guide's
  camera, motion and audio grammar has no image counterpart.

The FLUX.2 guide's "Model names and aliases" section is repeated verbatim in this guide, because "klein"
now names models in two unrelated families.

## 2. The lineup

- `flux-3-image`: API only, no published size, steps or guidance. Always expands the prompt ("FLUX 3 Image
  expands it before generating"), with no `prompt_upsampling` field, and searches the web by default.
  Returns the expanded prompt with the result.
- `flux-3-image-klein`: 5.6B, open weights, step-distilled, 16 steps, CFG 1 ("none" on the card). On the
  API it runs "with prompt upsampling and pixel restoration, which preserves unedited regions of an image
  exactly" (launch post). Locally it is bare unless the upsampler runs; the reference CLI runs it by
  default (`--no-pup` skips it); Diffusers needs it called separately.
- `flux-3-image-klein-base`: same 5.6B, undistilled, 50 steps, CFG 3.5. Hugging Face only.
- `flux-3-image-klein-pup`: a 9B Qwen3.5 fine-tune that writes the prompt. Not an image model, so not a
  model row. Trained on Klein only ("no other image model was part of training"), preference-tuned on
  Klein renders of its own prompts.

FLUX 3 Dev, announced in the FLUX 3 launch post as an open multimodal backbone, appears nowhere in the
current docs. The Klein post calls Klein "the second open weights release from the FLUX 3 family,
following FLUX 3 Action". Recorded as unshipped, not as renamed: nothing says Klein is Dev, and Dev was
announced as multimodal while Klein is image-only.

## 3. Length: three owner statements, one rule

- Docs: "A short prompt works. FLUX 3 Image expands it into a detailed description before it generates."
- Klein card: "Write full scene captions ... A short prompt gives generic output".
- Upsampler `t2i`: "Typical length is 100 to 350 words".

Not a conflict once the access split is drawn: the docs describe a surface that expands, the card
describes a model that may not, and the upsampler describes what the expansion produces. Taught as
`length_strategy: SPLIT BY WHAT SITS IN FRONT OF THE MODEL`, the same shape as Wan's access-inverted
expansion rule. The card's own example prompts are long; the docs' Klein examples are one or two
sentences, consistent with the docs assuming the API.

## 4. Edit register: caption or instruction

- Klein card: "For edits, describe the target image as a complete caption of the reference with the edit
  folded in", with a caption-register example ("The same lone American bison ... now at night").
- Docs (overview, single-reference, image editing, Klein page): "Write the change as an instruction."
- Upsampler `i2i`: picks the voice by task shape; imperative for bounded changes, a scope opener for whole-
  image changes, a "Create a photograph of ..." generation request for composites. "Describe the change,
  not the whole scene", 50 to 150 words, one compact keep clause.

Resolved for the instruction. Every docs page and the upsampler agree, and the upsampler was preference-
tuned on rendered results, which is the closest thing to evidence of what the model responds to. The
card's caption form is recorded as an accepted alternative. Both agree on the actual failure: a one-line
instruction to a model with nothing in front of it.

Keep-list length is a smaller version of the same split. The single-reference page's records name every
major element; the upsampler asks for "one compact clause". Taught as one compact clause that names the
elements actually at risk, which is what the owner's FLUX 3 examples (cow, neon sign, zoom) do.

## 5. Two reference numberings

- Plain prompts count from one. Multi-reference page: "'Image 1' is the first entry in `images`, 'image 2'
  the second". The upsampler writes ordinals ("the first image, the second image").
- Box records count from zero. Bounding-box page: "`ref_image_0` is the first image in `images`; the
  second is `ref_image_1`." Upsampler `i2i_bbox`: "attached in order as ref_image_0, ref_image_1, ...".
  `pup.py`: "Reference images follow in attachment order: ref_image_0, ref_image_1, ...". README:
  `"from": "ref_image_0" | "target"`.
- The only worked example with a non-zero token (multi-reference page, lamp on a sideboard) passes
  `images: [room, lamp]` and takes the lamp `from: "ref_image_1"`. Zero-based, settled.
- The Klein card's "refer to the n-th reference as `<ref_image_n>`" is correct only if n counts from zero.
  Read as English ordinal it is off by one; the guide does not reuse that wording.

Single-reference page: "For a plain written edit ... leave out the tokens." The `i2i` upsampler bans
angle-bracket tokens outright. So the two forms do not mix. The image-editing quickstart's `<owl_subject>`
with no rows is read as expanded output (that page says the expander "adds a box" for many edits), not as
a pattern to teach.

## 6. Box format

- Coordinate order: every source agrees on `[y_min, x_min, y_max, x_max]`, integers 0-1000, top-left
  origin. The reference code rejects boxes whose maximum is at most 1 ("max <= 1 means 0-1 coordinates").
- The CLI's `--boxes` file takes 0-1 fractions in the same order and converts them. Taught as a tool
  format never to paste into a prompt.
- Aspect correction, from `t2i_bbox`: "an element of physical width-to-height ratio a gets an x-span of
  about y-span x a x H/W"; the layout page gives the 2:3 worked case (150 wide per 100 tall).
- New content: the docs use `"from": null` in about thirty rows and never `"target"`; `i2i_bbox` and the
  README use `"target"`. The code passes user-supplied rows through unchanged and requires `"target"` only
  on rows the upsampler adds. Taught as `null` with `"target"` read the same way.
- Recolor rows: the launch tiger edit writes `"desc": "Make both pink."`, an instruction inside a desc.
  `i2i_bbox` puts end states in the paragraph and appearance in the desc, and the bounding-box format table
  defines desc as "What it should look like after the edit". Taught as appearance in the desc; the tiger
  row is an outlier.
- Citation: `i2i_bbox` requires every row cited exactly once. The bounding-box tutorial's move instruction
  omits `<needle_1>` while carrying its keep row; the launch version of the same edit cites it. In the
  reference code an uncited id sends the prompt back through the upsampler, which keeps boxes but adopts
  its own descs (`generate.py`, `reconcile`). Taught: cite everything.
- Ids: "Use lowercase names with a number" (bounding-box page) against owner text ids `En_Text_1`,
  `Ja_Text_1` and unindexed ids like `purple_fabric` in image-editing examples. The code accepts
  `[A-Za-z][A-Za-z0-9_]*`, case-sensitive. Taught: lowercase class noun plus index, with the
  language-code text form as written in the owner data.
- Positions in descs: `t2i_bbox` says "but no position"; several launch descs carry one ("filling the
  foreground"). Taught as the spec says; the launch descs are tolerated.
- `src_bbox_1stage` and `tgt_bbox_1stage` appear only in `i2i_bbox`, in no docs example, and are dropped by
  the reference code before the model. Not taught.
- Citing the source reference token: `i2i_bbox` asks for "the cup <cup_1> from <ref_image_1>"; the owner's
  lamp example omits it. The guide's version of the lamp example adds it and says so in its Why.

## 7. Voice

The upsampler forbids hedging, "this image shows", "is visible", quality and emotion judgments, and a
closing mood sentence. Owner captions on the docs pages break several of these ("A faint haze or smoke
drifts", "partially visible", "The overall mood is one of quiet observation"), and "building a good
prompt" recommends mood words. Taught as the upsampler states it, since it is the specification of what
the model receives on every expanded surface, with the docs' looser captions read as tolerated.

This register is close to the opposite of Qwen-Image-2.1's rewriter, which asks for hedging and a closing
composition sentence. The guide says so in its structure rules, because an agent writing for both will
carry the habit across.

Brands: the upsampler says "Do not invent names, brands, logos or celebrities"; the style page recommends
camera names ("Shot on Fujifilm X-T5"). Read as different things: depicted content versus a style cue.

## 8. Smaller conflicts

- Negatives: the technical page's positive-description rule against owner prompts ending "No text." and
  "no glossy surfaces". Taught positive-first, with a short negation as the tolerated fallback.
- Aspect ratio: `t2i` never mentions the canvas; the full model's API reference says "a ratio the prompt
  asks for wins" under `auto`; owner poster prompts open "Create a finished 1:1 graphic design artwork".
  The ratio is request surface; the guide teaches only that the caption should suit the frame.
- Line breaks: `\n` inside the quote on the style page and in every upsampler prompt; "slashes indicate
  line breaks" in the generate-page posters. Taught `\n`.
- Hex: the reference page says "Use a hex code to specify a target color" without scope; every FLUX 3
  demonstration is an edit, and the only text-to-image hex example on the use-case page is FLUX.2 output.
  Taught for edits only.

## 9. Provenance of examples

The shared pages ("style, aesthetics and text", the use-case page, parts of multi-reference) still show
images generated with FLUX.2 and say so. Only examples labelled or evidently FLUX 3 are used. Owner
strings were normalised to ASCII (the image-editing quickstart and bounding-box prose carry U+2014 and
U+2013). The guide's own examples (photograph convention, multi-line sign, style transfers, four-input
generation, removal) are built to the upsampler's rules and say so in their Why lines.

The "Migrate from FLUX.2" page linked from the prompting summary returns a 307 to the bounding-box page.

## 10. Effects on other guides

- `flux-3-video`: its rule that FLUX 3 Image is unreleased is false; corrected in the same pass.
- `flux-2`: it cited `prompting_unified_building`, which now carries FLUX 3 content; the citation moved to
  the prompt reference's FLUX.2 sections and the FLUX.2 prompting guide. Its FLUX 3 rule was rewritten.
- Lorebook: the generic keys `flux 3`, `flux-3`, `flux3` moved from the video entry to the image entry, and
  the video entry is now keyed on video-specific names. A bare "FLUX 3" loads the image guide.
