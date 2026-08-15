# AI prompting guides

Prompting guides for text-to-image and text-to-video models, one per prompt scheme. Written for an agent
that will write the prompts, and for a person skimming for rules and examples.

Each guide is built from the model owner's own documentation, and says which source it followed where they
disagree. Prompt craft only: no API parameters, limits or pricing, since those differ by provider.

## SillyTavern lorebook

[Download the lorebook](https://raw.githubusercontent.com/CalamitousFelicitousness/ai-prompting-guides/main/lorebook/%5BInstructions%5D%20Prompting%20guides.json)
(right click, Save link as) and import it under World Info. Naming a model in chat loads that model's guide.

Keep the filename as it is. SillyTavern takes the world name from the filename and character cards link a
lorebook by world name, so importing it under a different name creates a second world and leaves existing
card links pointing at the old one. The version lives inside the book instead, on the first entry.

## Guides

[docs/INDEX.md](docs/INDEX.md) lists them with verification dates.

[`docs/model-specs.md`](docs/model-specs.md) is a reference table rather than a guide: native resolutions,
step counts, CFG, samplers and frame rates for the open-weights models.

`TEMPLATE.md` is the house format, and `build-lorebook.py` compiles the guides into the lorebook.
