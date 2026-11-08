# Gemini Image: Nano Banana 2.1 pass and source notes

Not a scrape. Hand-authored 2026-11-08 from the sibling scrapes in this folder. The earlier passes
(2026-05-31 family guide, 2026-08-07 Flash Lite merge) left no note; their decisions live in the guide.
This one records what the 2.1 pass settled so it is not re-derived.

## 1. Nano Banana 2.1 joins the scheme, no split

`gemini-nano-banana-2.1` went GA on 2026-10-06 (Gemini API changelog). The owner calls it "an update to
Nano Banana 2" and its image-generation page keeps one prompt guide for every model. The prompting
section, best practices and limitations text are unchanged from the August snapshot apart from model
names. Same grammar, capability difference only: merged.

Tiers: 2.1 is `distilled` (the Flash workhorse), `gemini-3.1-flash-image` moves to `legacy` (the
changelog deprecates it, "no shutdown date announced", and the docs call it "previous-generation").
Pro stays `flagship` (largest, Pro line).

## 2. Naming: the nickname became the official name

The API page title is "Gemini Nano Banana 2.1", the ID is `gemini-nano-banana-2.1`, Vertex uses the
same. There is no "Gemini 3.x Flash Image" name for it. The DeepMind model card says "based on Gemini
3.6 Flash"; no `gemini-3.6-flash-image` ID appears on any Google surface, so the guide warns against
constructing one.

The house rule "prefer the Gemini name, translate the nickname" still holds for the older four; the
naming section now says the pattern broke at 2.1 and to read the table. User preference for Gemini
naming is met by using Google's own official string, which contains "Nano Banana".

The `-preview` rule was stale: the preview IDs were deprecated 2026-05-28 (shutdown 2026-06-25 on the
Gemini API) and the Vertex 3.1 Flash Image page now lists the plain `gemini-3.1-flash-image`, GA. The
rule was rewritten in both Gemini guides, which carry the section verbatim.

## 3. Owner vs owner: is Pro still the strongest?

- API docs: Pro is "the premium choice for complex visual tasks"; 2.1 "serves as the more efficient
  counterpart to Gemini 3 Pro Image".
- DeepMind 2.1 model card: 2.1 (Thinking) scores above Pro on every listed measure (overall preference,
  infographic design and factuality, general editing, character and product consistency, mask/ink
  editing, stylization, multi-reference editing).

Resolution: both are owner surfaces and they disagree in framing (product positioning) more than
substance. Kept Pro as the higher tier because it is the Pro line and the docs still position it there,
and it is the only model with a listed style-reference role. Dropped the old "Pro is still the strongest
model" sentence and told the reader to start on 2.1, attributing the ranking to the model card. No
benchmark figures in the guide.

## 4. Flash Lite reasoning and video: the August guide was wrong or is now stale

August guide: Lite "has no reasoning step" and only 3.1 Flash took video. Current owner surfaces: the
Lite model page lists Thinking as supported, the thinking-level table lists Lite (minimal default,
high available), and video-to-image now names 2.1, 3.1 Flash and 3.1 Flash Lite. The DeepMind Lite page
scraped in August already benchmarked "Nano Banana 2 Lite Thinking On", so the August claim was likely
wrong at the time. Corrected to "reasons only when the level is raised". Lite still has no search
grounding of either kind (model page: Search grounding not supported).

Thinking defaults taught in words, not enum names: 2.1 middle setting by default, 3.1 Flash and Lite
only when raised, Pro by default.

## 5. Mask-based editing

Three surfaces, consistent once read together:

- DeepMind 2.1 page headline: "better visual design, mask-based editing, subject consistency". The page
  is a carousel whose section headings scrape after their slides; the mask slide's prompt is "mask the
  object inside the sketch and place in a completely different environment but don't change the size
  and position of the object itself, create 5 of these each 16:9, each it's own server call, one at a
  time" (an app/agent prompt; the tail is app plumbing and was not taught).
- Model card: evaluates "Ink (doodle) based Editing" and "Mask/Ink-Based Editing"; known limitations
  include "Partial instruction following and ink persistence in masked/doodle based editing".
- fal landing page: "No separate mask parameter: the marked image is the input"; draw a coloured box,
  "say in the prompt to edit only inside the mark and remove the mark"; "The rest of the frame is
  regenerated rather than copied bit for bit".

Taught as a new "Marked-region edits" section with two directions (mark selects the change, mark
protects the subject). The old edit rule "no masks or brushes" became "no mask field; draw it on the
input or define it in words". `marked-input-editing` cap on 2.1 only: the model card benchmarks Pro and
3.1 Flash on the same task, so they accept marked images, but only 2.1 carries the owner capability
claim. Same cap name as gpt-image.

Both marked-edit examples are guide-built. fal's balloon demo publishes images, not its prompt, and the
DeepMind prompt is app-flavoured; the second example reuses its "same size and position" clause.

## 6. DeepMind Gemini Image prompt guide (never scraped before)

`deepmind.google/models/gemini-image/prompt-guide/` is a Gemini-app surface (its AI Studio link still
points at a preview ID). Taught only where additive and not contradicted by the API docs:

- "assign a distinct name to each character or object in your prompt" -> named-character rule and the
  six-reference example.
- "Ask for multiple images at once" -> compare-options rule, paired with the API limitation that the
  count is not guaranteed.
- "provide the exact translated text in quote marks" -> localization rule.

Not taught: "Look for the in-product resolution dropdowns" (app UI).

## 7. Model-card limitations turned into craft

- Small text blurry at the smallest size -> text rule and pitfall, worded without the resolution enum.
- Persistent subject pose in edits -> pose rule and pitfall.
- Left/right confusion -> anchor-positions rule and pitfall.
- Thinking vs no-thinking gap largest on infographic factuality -> keep reasoning on for diagrams.

## 8. Smaller fixes and stale owner text

- Languages: the owner list has `ua-UA` in both the August and November snapshots; the guide had
  dropped it. Added as `uk-UA`.
- Panoramic ratios (1:4, 4:1, 1:8, 8:1): aspect ratio is prompt text, so in scope. The guide's advice
  to lay content along the long axis is guide-built from the owner's "fixed tiling artifacts on wide
  and panoramic aspect ratios".
- Stale owner text, not acted on: the sequential-art note still says "best with Gemini 3 Pro and Gemini
  3.1 Flash Image"; the DeepMind `/flash/` page header still reads "Nano Banana 2" with a preview link.

## 9. Kept out

Resolution tiers (and that 2.1 drops the 512px size), reference counts (14 total, 4 characters, 10
objects; Pro 5 and 6 plus 3 style), token limits and per-image token figures, pricing, thinking-level
enum strings, the Interactions API move, fal's per-token billing and video/PDF size caps.
