# Qwen-Image-3.0: source adjudication

Not a scrape. Hand-authored adjudication written 2026-08-07 from the sibling scrapes in this folder,
covering three questions the 3.0 release raised: whether it is a new prompt scheme, whether the model
can retrieve live knowledge, and which owner surface counts as a prompt guide.

## 1. Same prompt scheme, so no split

Qwen-Image-3.0 launched 2026-07-21 with two Model Studio model IDs, `qwen-image-3.0-pro` and
`qwen-image-3.0`. It folds into the existing guide rather than getting its own, because the difference
from 2.0 is capability, not syntax.

Everything new is reached through the grammar the guide already teaches. Longer briefs are more of the
same continuous natural-language description. Grid and nested layouts are ordinary spatial description
applied at greater length. Small text, formulas, and additional languages all still go through the
existing rule of quoting each literal string with its own style and placement. Reference handling is
unchanged. Nothing in 2.0's rule set becomes wrong on 3.0.

This is the Seedream 4.5 plus 5.0-lite precedent, not the Wan image-vs-video precedent. Wan split
because the video layer partly conflicts with the image rules; here there is no conflict to resolve.

## 2. Live world knowledge: the blog and the API model cards disagree

The owner blog demonstrates internet retrieval, generating "a weather forecast image for Hangzhou on
July 21" and stating the model "can also connect to the internet to retrieve the latest world
knowledge."

Both Model Studio model cards contradict this. `qwen-image-3.0-pro` and `qwen-image-3.0` each list
**Web Search: Unsupported** in their Model Capabilities table, alongside Function Calling: Unsupported.

Resolved on the repo's owner-vs-owner rule: the API reference governs, because these guides serve
agents prompting through providers and proxies that wrap the API and never the vendor's web app. The
blog demonstrations run inside Qwen Chat, a product surface that can orchestrate retrieval around the
model; the retrieval is the app's, not the model's. The distinction matters in practice, because a
prompt written on the assumption that the model will look something up produces confidently wrong
detail through an API.

The guide therefore teaches the opposite rule: state any current, local, or verifiable fact in the
prompt text. Built-in world knowledge (recognisable interfaces, named public figures, domain
conventions) is real and taught as such; live retrieval is not.

## 3. There is no owner prompt guide for 3.0

3.0 shipped without weights, a technical report, a model card, or benchmarks, a break from 1.0 and 2.0.
The launch blog is a capability showcase containing zero example prompts, and the Model Studio
`qwen-image-api` reference had not been updated to mention 3.0 as of 2026-08-07 (it carries the model
only as a navigation card).

One near miss is worth restating, because the 3.0 pass walked into it a second time. Model Studio's
[Text-to-image prompt guide](https://help.aliyun.com/en/model-studio/text-to-image-prompt) sits in the
same docs tree, is linked from the Qwen model-info pages' sidebar, and is easy to mistake for Qwen
guidance. It is not: its own "Applies to" block names Wanx Text-to-Image V2 and V1, and it was last
updated 2026-03-14, before 3.0 existed. This was already adjudicated on 2026-05-31, and the canonical
copy lives at `sources/wan/alibaba-text-to-image-v2-prompt-guide.md`, cited by `wan-image.md`. Do not
re-file it under a Qwen folder. The Basic and Advanced formulas it defines do transfer to Qwen and are
already in the guide; the document itself is not a Qwen source.

Neither approved provider had published 3.0 prompt guidance at the time of writing, which follows from
the API being invitation-only. The guide's 3.0 craft is therefore derived from the owner blog's own
worked examples and the two model-card descriptions, and should be revisited once WaveSpeed or FAL
publish.

## 4. Capability numbers dropped under the scope rule

The owner states several figures that are capability claims rather than prompt craft: a 4.5k token
instruction window, legible text down to 10px, 12 native languages, 20+ fonts, and 100+ artistic
styles. Per the repo scope rule the strategy is kept and the number dropped, so the guide says to write
a full multi-section brief and to specify small type deliberately, without printing the ceilings. The
token figure would also trip the repo's own scope-leak grep.

Languages are handled the way Seedream's were: name the ones the owner attests by example (English,
Chinese, Japanese, Korean, Spanish) rather than printing a count, since the count is unverifiable from
the published material and the names are what an agent actually writes into a prompt.

## 5. Tier split between the two 3.0 models

The two model-card descriptions divide cleanly and both are owner text.

| Model | Owner framing |
| --- | --- |
| `qwen-image-3.0-pro` | Micro-detail realism: micro-expressions, pores, individual hair strands, "approaching the quality of real photography". Images-within-images nesting. Newspapers, storyboards, menus, exam papers. |
| `qwen-image-3.0` | "Quality-speed balanced". Batch production of posters, web pages, and UI screens, framed around cost efficiency. |

Both carry the same long instruction window, small-text rendering, and language coverage, so the prompt
transfers between them unchanged. The guide records the split as a variant-choice note, consistent with
how the 2.0 tiers are already handled.
