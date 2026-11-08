# Krea 3: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08. Sources in this folder: Krea's API overview and user-guide pages (curl of
the Mintlify `.md` twins), the launch post and technical report (firecrawl), Krea's Notion prompting guide for
reference-driven editing (firecrawl; the page renders without sign-in), the Krea docs model overview and
text-to-image examples, and fal's landing, edit, edit API, text-to-image, realtime and prompting-guide pages.

## 1. Own scheme, not part of `krea-2`

Krea 3 starts from the Krea 2 pretrain, but its prompt surface differs on every axis that decides a split: a VLM
text encoder that sees the references, an always-on expansion step with thinking levels instead of the creativity
control, a negative-prompt field, box labels referenced as `@label`, and content references instead of weighted
style references. Krea's own Krea 3 page routes aesthetic exploration to Krea 2. One model row; "Krea 3 Ultra" is
`thinking_mode: ultra` on the same endpoint, so it is described in Models, not given a row.

## 2. Owner-vs-owner: ordering of change and preservation

- API overview (governs): "Lead with the change. Add only the details that help to execute it. Close with one
  preservation sentence ... Do not list everything that should stay the same."
- Launch post: "Start with what stays ... Then describe the change." Two Notion showcase prompts (kettle, soda can)
  also open with the preservation clause.
- Notion "When writing your own": change first, then what should stay; its shortened prompts follow that order.

Taught: the API order. The launch-post order is recorded in Sources as a tolerated variant; the kettle prompt is
kept as an example because it is an owner restage, and its why-line attributes the pinning, not the order.

## 3. Reference naming

API overview: "refer to each image by what it shows". Launch post, Notion and technical report: "image 1", "images
2 to 4", "the person from image 1, wearing the jacket from image 2". fal's prompt field: "Refer to images as
<image-1>, <image-2>, ... and regions as @label", and fal's returned expanded prompts use `<image-1>`. Taught: number
plus content, which satisfies both owner forms; fal's tag form recorded as host-documented. `@label` is common to
Krea's API (`regions[].label`, default `@1`, `@2`) and fal.

## 4. Thinking levels and legacy names

Krea API: `fast` (default), `high`, `ultra`. The Notion examples record "medium thinking", and fal's enum is
`medium, high, ultra` with `medium` default: the pre-rename name of the default level (changelog 2026-10-15,
"renamed thinking modes (fast and high)"; legacy names sunset 2026-10-30). The guide names no level values.

## 5. Examples

Owner verbatim: mug, strap, copper ornaments, translate (technical report and API); atrium and watch (Notion
shortened prompts); woodblock, couture side profile, office close-up, kettle (Notion); seating swap (launch post,
marked "Prompt shortened" there). Provider: the two expanded prompts fal returns on its edit and text-to-image pages.
Guide-built to owner rules: pure style transfer, style transfer plus text edit, labeled boxes, and the Night Shift
to Day Break text swap (the technical report shows that pair but not its instruction). Not used: the soda-can
prompt (owner, but it carries ratio and percentage layout figures), the full atrium and watch prompts (the
shortened owner versions teach the same), Runware's and eachlabs' pages (not approved sources).

## 6. Kept out

Prices, latency, resolutions and the 4K tier, reference-count limits (launch post says 6, API and fal say 8),
reference resizing figures, region count limit, coordinate fields, ZDR rules, error codes, plan gating details,
fal's realtime frame size.
