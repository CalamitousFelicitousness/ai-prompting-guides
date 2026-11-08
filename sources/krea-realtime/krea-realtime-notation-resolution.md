# Krea Realtime 14B: routing decision and source notes

Not a scrape. Hand-authored 2026-11-08. Sources: the HF model card `krea/krea-realtime-video` (read through the HF
tools), Krea's technical post (`krea-blog-krea-realtime-14b.md`), and Krea's Realtime app guide
(`krea-docs-realtime-user-guide.md`, which describes the app surface and its model picker, not this checkpoint).

## 1. A row in `wan-video`, not its own guide

The card's `base_model` is Wan-AI/Wan2.1-T2V-14B, `base_model_relation: finetune`; Krea calls it a Self-Forcing
distillation. It keeps Wan 2.1's text encoder and caption style (the setup downloads the Wan2.1-T2V-1.3B folder,
the examples are short English captions, and a Wan 2.1 LoRA loads with its trigger word). What it adds is a
streaming layer: prompt changes mid-generation and video-to-video restyling. That is a handful of rules, not a
grammar, so it joins the Wan Video offshoots as an open-weights row with a short subsection, which also gives
it the required spec row. Tier `distilled`.

## 2. Prompt craft taken from the technical post

- "trained on detailed prompts and performs best with long, detailed captions with explicit descriptions of
  motion. Simpler captions tend to produce more static outputs."
- "our model struggles to generate complex camera motions", attributed to DMD mode collapse.
- Repetitive motion on a long single-prompt stream; fixed by interpolating between variations of the prompt.
- On diverse transitions ("a woman" to "a bird") the model "prioritizes consistency over prompt adherence"; Krea's
  fix is a KV-cache attention bias, a pipeline setting. The guide teaches stepping through intermediate prompts.

## 3. Numbers

Card prose says 4 inference steps (11 fps on a B200); the card's diffusers examples pass 6. Both recorded in the
spec row. Frame rate 24 is from `export_to_video(..., fps=24)` in the owner's examples; resolution and duration are
not published. Timestep shift 5.0 is the owner's training choice. CFG is not stated and the video table has no CFG
column.

## 4. Example

Guide-built, from the card's v2v caption "A car racing down a snowy mountain road", expanded to the post's advice
(explicit motion in every clause, one simple camera move).
