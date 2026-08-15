<!--
================================================================================
HOUSE TEMPLATE — AI image-model PROMPTING & USAGE guide
================================================================================
PURPOSE   One reusable schema for every "how to prompt model X" guide in this repo.
AUDIENCE  Primarily an LLM agent that will WRITE prompts for the model.
          Secondarily a human skimming for rules/examples. Optimise for the LLM:
          lead with imperative rules and concrete examples, keep prose minimal.

SCOPE — PROMPTING & USAGE ONLY  (read this twice)
          IN:  how to craft the prompt TEXT, what the model responds to, text-rendering
               technique, style/composition vocabulary, negative-prompt STRATEGY,
               prompt-length strategy, editing-instruction phrasing, use-case patterns,
               pitfalls. All of it portable across any provider/proxy that serves the model.
          OUT: API parameter names, numeric limits, resolution enums, image counts,
               endpoints, SDK/code samples, pricing. These are PROVIDER/PROXY-SPECIFIC
               (Alibaba vs FAL vs WaveSpeed vs a proxy all differ) and belong in the
               provider's own API docs — NOT here. Mention a behaviour (e.g. "some hosts
               auto-expand short prompts") only as portable technique, never as a named param.

ONE GUIDE PER prompt_scheme
          Models that share a prompt scheme (same prompt-writing rules) share ONE guide —
          list them all under `models`. A model prompted differently gets its OWN guide.
          (e.g. qwen-image-2.0 / -pro / -max / -plus share a scheme; the Wan series does
          NOT — it prompts differently — so Wan is a separate guide.)

ENCODING CONVENTIONS (use each where it is strongest)
          YAML frontmatter  → portable machine-readable FACTS (scheme, model line-up, langs).
          Markdown headings → the fixed section schema below. Keep order; drop a section
                              only when truly N/A (note the omission in <rules id="global">).
          <rules id="…">    → imperative, testable prompt-craft constraints the agent MUST obey.
          <template id="…"> → reusable prompt pattern with {slots} to fill.
          <example …>       → ONE concrete sample: the prompt in a ```text``` block, then a one-line *Why:* caption.
          ```text```        → literal prompt strings only (NOT API calls — those are out of scope).

          BLANK LINES       → REQUIRED inside every <rules>/<template>/<example>: one blank line after the
                              opening tag and before the closing tag (and between prompt: and why:). Without
                              them CommonMark/Obsidian treat the block as raw HTML and collapse the inner
                              list/text into one run-on paragraph.

HOW TO USE Copy this file to guides/<scheme>.md, fill every {{…}} and <!-- … -->,
          delete this comment block and any unused optional sections, set last_verified.
================================================================================
-->
---
guide: "{{Model family display name}}"
prompt_scheme: "{{scheme-key}}"          # cluster key — every model below obeys this guide
models:
  # variants that share this scheme; describe each by its CREATIVE strength (usage), not API limits
  - { id: "{{model-id}}", tier: "{{pro|std|max|plus|base}}", best_for: "{{e.g. dense text & posters}}" }
capabilities: [text-to-image, image-edit, text-rendering]   # trim to what is actually true
prompt:
  languages: ["{{en}}", "{{zh}}"]
  literal_text: "{{how in-image text is requested — e.g. wrap the exact words in double quotes}}"
  length_strategy: "{{e.g. rewards long, detailed, multi-sentence prompts}}"
  auto_expand_behavior: "{{e.g. short prompts may be auto-expanded by some hosts; write a full prompt for tight control | none}}"
  negatives: "{{strategy — e.g. describe what to exclude; where a host lacks a negative field, fold exclusions into the positive prompt}}"
sources:                                  # trust order: official > provider > community
  official: ["{{url}}"]
  provider: ["{{url}}"]
  community: ["{{url}}"]                   # lower trust; must never override official
last_verified: "{{YYYY-MM-DD}}"
---

# {{Model family}} — prompting & usage guide

<rules id="global">

- This guide covers PROMPT CRAFT only. For endpoints, parameters, limits, and code, consult the
  specific provider/proxy's API docs — they differ and are out of scope here.
- {{Always-applicable rule — e.g. write ONE continuous natural-language description, not comma-separated tags.}}
- {{Note any section below omitted as N/A for this model.}}

</rules>

## TL;DR

<template id="quickstart">

{{Minimal high-success prompt pattern with {subject}, {setting}, {style}, {detail} slots.}}

</template>

## Models & when to use which

<!-- For "which variant for which creative goal" — strengths only (e.g. -pro for dense typography,
     -max for photoreal portraits). NO resolution/count/limit details (provider-specific, out of scope). -->

## How the model reads prompts

<!-- Mechanism & behaviour that shapes prompt-writing: natural-language vs tags, how it rewards detail,
     auto-expansion behaviour and how to keep control, language handling, tokenisation quirks.
     Behaviour described portably — never as a named API parameter. -->

## Prompt structure

<rules id="structure">

- {{Ordering / composition — e.g. lead with subject, then setting, then style, then lighting/mood.}}

</rules>

<template id="general">

{{The canonical full-detail prompt skeleton with all slots.}}

</template>

## Text rendering

<rules id="text">

- {{e.g. Wrap the literal words to appear in the image in double quotes; name the language for non-Latin scripts; keep each string short; state typography & placement.}}

</rules>

<example use_case="{{poster}}">

```text
{{...}}
```

*Why: {{one line on what makes it work}}*

</example>

## By use-case

<!-- Repeat <template> + <example> per high-value use case: photorealism, posters, infographics,
     styles (anime/oil/3D/…), product shots, etc. One block each. -->

## Image editing

<rules id="edit">

- {{Editing instruction phrasing — what to hold constant, how to reference the source image in words,
     how to scope the change. (How an image is ATTACHED to a request is provider-specific → out of scope.)}}

</rules>

<example use_case="{{add-text}}">

```text
{{...}}
```

*Why: {{...}}*

</example>

## Negative prompts & exclusions

<rules id="negatives">

- {{Strategy: describe specific artifacts to avoid rather than generic terms; when to skip negatives.
     Where a provider exposes no negative field, fold the exclusion into the positive prompt instead.
     (Phrase as technique — do not document a specific provider's parameter.)}}

</rules>

## Pitfalls & anti-patterns

<rules id="avoid">

- {{Common failure → fix. e.g. tag-soup → rewrite as prose; over-long literal text → shorten.}}

</rules>

## Sources

<!-- List by trust tier (official / provider / community) with URLs and last-verified date.
     State the rule: official wins on conflicts; community is illustrative only. -->
