# Krea 2: structure decision and source notes

Not a scrape. Hand-authored 2026-11-08 at the recheck. Sources added this pass: Krea's repository for the open
release (`github-krea-2-readme.md`, `github-krea-2-prompting.md`, `github-krea-2-expansion.txt`), the current API
overview (`krea-docs-krea-2-overview-2026-11.md`), and the Krea 2 and Krea 2 Turbo user-guide pages. Krea's docs
moved from `docs.krea.ai` to `www.krea.ai/docs`; Mintlify serves a `.md` twin of every page, fetched with curl.

## 1. Krea 3 is a separate scheme

Krea 3 (2026-10-15) is initialised from the Krea 2 pretrain but is an instruction editor with a VLM text encoder,
a negative-prompt field, thinking modes instead of the creativity control, and box labels referenced as `@label`.
Krea's own Krea 3 page routes aesthetic exploration (style references, moodboards, LoRAs, sliders) to Krea 2 and
edits and consistency to Krea 3. Own guide, `krea-3`; this guide carries a routing line.

## 2. Open checkpoints in the body

The open rows were in frontmatter since August but the body described only the hosted models. Added: Raw and
Turbo bullets in Models, an access split on `auto_expand_behavior` (no creativity control or expansion when run
locally), the expansion contract from `expansion.txt`, and three verbatim owner samples (harvest mouse, analog
collage, cel anime) plus the minimal rocket-exhaust one. All owner samples were generated with Turbo at 2K.

## 3. Turbo naming

Krea's app and docs now call the hosted fast tier "Krea 2 Turbo"; WaveSpeed lists it as `krea-v2-medium-turbo`
and the row id stays `krea-2-medium-turbo`. The downloadable checkpoint is also named Krea-2-Turbo. The guide does
not claim the two are the same weights; it says a local run has none of the hosted controls.

## 4. Caps

`text-rendering` added to Krea-2-Turbo from the open-release prompting guide ("For text rendering, we recommend
putting quotes around the words to be rendered"), whose samples were all generated with Turbo. Raw left at
`text-to-image`: no owner statement about its text rendering. Spec row updated to match, plus the README's
resolution statements (Raw trained up to 1K; Turbo 1K to 2K).

## 5. Unchanged

The hosted API overview is the June text with new navigation chrome only: same creativity enum, same Medium and
Large endpoints, no negative field. No new open checkpoints on the `krea` HF org since June other than Turbo
style LoRAs.
