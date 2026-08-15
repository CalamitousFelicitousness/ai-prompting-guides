# Kling notation conflicts and their resolution

Not a scrape. This is a hand-authored adjudication of conflicts BETWEEN Kling's own surfaces, written
because the repo's source bar resolves owner-vs-provider on owner authority but has no rule for
owner-vs-owner. Evidence pulled from the sibling scrapes in this folder. Written 2026-07-16.

Kling publishes prompt guidance across four surfaces that disagree: the API 2.0 reference, the legacy
API reference, the quickstart model user guides (a web-app product surface), and the blog. The user
guides describe the Kling web app, where shot counts and durations are set by widgets. The API
reference describes what an agent actually sends. This guide serves agents writing prompts through
providers and proxies, which wrap the API, never the web UI. **API surfaces therefore govern; user-guide
and blog forms are recorded as tolerated variants, not taught as canonical.**

## Conflict 1: the reference-token grammar. RESOLVED.

Four surface forms for one mechanism:

| Surface | Form |
| --- | --- |
| Legacy API reference | `<<<element_1>>>`, `<<<image_1>>>`, `<<<video_1>>>`, `<<<voice_1>>>` |
| VIDEO 3.0 Omni user guide | `@Grace`, `@Boxer A`, `@Image`, `@Element1` |
| VIDEO O1 user guide | `[@Video]`, `[@Image1]`, `[@Element]` (inside `Prompt Structure:` templates) |
| API 2.0 example prompts | plain English: "the reference image", "the video" |

**Resolution: they are one mechanism, and the token binds to the caller-assigned input id.**

The API 2.0 `contents` array gives every input an `id`. The owner's own example ids are, verbatim:

```text
"id": "image_1"      (5 occurrences)
"id": "image_2"      (3)
"id": "video_1"      (2)
"id": "element_1"    (2)
```

Those strings match the legacy page's documented tokens (`<<<image_1>>>`, `<<<video_1>>>`,
`<<<element_1>>>`) exactly. The token is not positional and not automatic: it is the id the caller
assigned. The web UI's `@Name` form is the same mechanism keyed on the element's name field instead,
because the UI has names where the API has ids. The O1 guide's `[@Video]` is a prose placeholder in a
fill-in-the-blank template, not a literal parsed syntax; its brackets are overloaded in the same
templates for writer-fill slots (`[describe content to add]`), which no parser could disambiguate.

**The token is OPTIONAL.** Both real example prompts in the API 2.0 reference omit it entirely:

```text
A girl sat on the train, looking out the window with a melancholic expression, her head swaying with the train.
```

(supplied with a first_frame, a last_frame AND an element carrying `"id": "element_1"`; the prompt
references none of them by token)

```text
Change the color of the parrot's feathers to match the reference image. Keep all other elements of the video unchanged.
```

(supplied with a base_video and a refer_image; refers to the reference image in plain English)

So: use a token when more than one input could fill a role and you must weld a specific element to a
specific slot. Skip it when the roles are unambiguous. This is ONE ROLE PER INPUT expressed as syntax.

The owner's only stated style rule on tokens, from the legacy page: "Simpler grammar is better. For
example: The man `<<<voice_1>>>` said, "Hello."."

## Conflict 2: multi-shot notation. RESOLVED.

Seven forms across surfaces:

| Surface | Form | Duration carried where |
| --- | --- | --- |
| API 2.0 text-to-video | `shot n, m, words; shot n, m, words;` | inline, in the prompt |
| Legacy API, customize | `multi_prompt` array of {index, prompt, duration} | a param, not prompt text |
| Legacy API, intelligence | "multi-shot scene descriptions in the prompt", syntax unspecified | not carried |
| VIDEO 3.0 user guide | `Shot 1, <words>. Shot 2, <words>.` | UI widget, out of band |
| VIDEO 3.0 Omni user guide | `Shot 1 (2s): <words>` (dominant, 5 of 9 examples) | inline, parenthesized |
| VIDEO 3.0 Omni user guide | `[00:00 - 00:02] <Framing>:` blocks with `Audio:` sub-lines | inline, as timecode ranges |
| Prompt-guide blog | `[Shot 1: Wide shot] <words>` | not carried |

**Resolution: `shot n, m, words;` is canonical.** It is the only form the API documents as prompt TEXT,
stated on the API 2.0 text-to-video page: "Multi-shot video format: "shot n, m, words; shot n, m,
words;" (separated by standard semicolons)". The legacy customize mode moves shots into a structured
array, which is a parameter and out of this guide's scope. Everything else is a web-UI or blog
demonstration.

Do NOT teach the UI forms as interchangeable. Nothing in the owner's material states that the web app's
`Shot 1 (2s):` or timecode-block forms are parsed identically when sent through the API, and asserting
it would be inference. Record them as forms the owner demonstrates on its product surface.

The `[00:00 - 00:02]` timecode form is the only one that carries a per-shot `Audio:` channel. That is a
real technique with no API-form equivalent, and the guide should say so rather than pretend the
semicolon form covers it.

## Conflict 3: the prompt formula. RESOLVED, with a caveat.

- VIDEO O1 user guide (Dec 15, 2025) states it verbatim: "**Prompt Structure**: Subject (subject
  description) + Movement + Scene (scene description) + (Cinematic Language + Lighting + Atmosphere)"
- Prompt-guide blog (Jul 3, 2026) softens it: "built from clear scene direction rather than secret
  formulas. A useful prompt usually defines the subject, action, setting, camera language, lighting,
  and atmosphere in plain, readable language."

Same six slots, different framing, seven months apart. The newer surface does not retract the formula;
it declines to call it a formula. **Teach the slots, and do not present them as a rigid ordering.**
Both surfaces agree on the content; only the prescriptiveness differs.

Note for future sessions: the formula circulating in community blogs ("Subject + Subject Movement +
Scene + (Camera Language + Lighting + Atmosphere)") is a real quote with drift. The owner writes
"Movement" not "Subject Movement", and "Cinematic Language" not "Camera Language". It is NOT a
community fabrication; it is owner-published on the older surface.

## The image-to-video rule: IT EXISTS. Earlier "no rule" finding was WRONG, corrected 2026-07-16.

An earlier pass through six owner surfaces (the VIDEO 3.0, 3.0 Omni and O1 user guides, plus the
prompt, motion and camera-control blogs) found no image-to-video rule and concluded the owner states
none. **That conclusion was wrong.** The rule lives on a seventh surface, a dedicated image-to-video
quickstart at `https://kling.ai/quickstart/image-to-video-guide` (Nov 24 2025), which none of the model
user guides and none of the prompt blogs links or repeats. Stated verbatim:

> In contrast to Text-to-Video, which necessitates scene description, Image-to-Video is already
> provided with a scene. Thus, it only requires the depiction of the subjects in the image and the
> intended movement for these subjects. Should there be several subjects with various movement, list
> them sequentially.

The formula, verbatim (a fifth Kling formula, and the only mode-specific one):

```text
Prompt = Subject + Movement, Background + Movement
```

**The rule is NOT the Wan/LTX omit-rule, and reading it as one loses the point.** Wan and LTX say the
image owns appearance so do not repeat it. Kling says the image owns the SCENE, and the prompt still
must NAME THE SUBJECT. Naming is mandatory; a bare instruction fails. The owner's worked failure is the
best diagnostic text in the whole corpus because it explains an effect users see constantly:

> If you want to have Mona Lisa in the painting wear sunglasses, when we simply input "wear sunglasses",
> the model may have difficulty understanding the instruction ... When "Kling" determines that it is a
> painting, it is more likely to generate a video with panning effects of the painting exhibition,
> **which is also the reason why photos are prone to generating static videos**.

So: no named subject -> the model films the image as an object -> a slow pan over a still. Fix by
welding the movement to a named subject: `Mona Lisa puts on sunglasses with her hand`, and for
background motion append the second half: `..., and a ray of light appears in the background`.

Stated tips from the same page, all portable:

- Simple words and simple sentence structures; avoid overly complex language. (The only place Kling
  asks for LESS language.)
- Movement must obey physics and should be movement plausible FOR THAT IMAGE.
- **A description that deviates far from the image causes a camera cut or transition**, not the motion.
- Complex physics (a bouncing ball, a high-altitude throw trajectory) is still hard.

**The caveat that must ship with the rule.** The page is dated Nov 24 2025 and describes the std/pro
mode era, and the 3.0-era examples do not obey it. This owner example supplies a first frame and
re-describes the entire scene including wardrobe and hair:

```text
Sunlight floods an old street in Madrid in front of a bakery where a female Chinese tourist and a male in a grey hoodie walk toward the clerk with polite smiles; the female tourist asks at a slightly slow pace with a clumsy accent in Spanish, "..."
```

while this one, also with a first frame, carries pure action and dialogue:

```text
Shot 1: The woman gazes into the distance and says, "..." Then she looks at the man and continues looking forward, saying, "..."
```

Re-describing is therefore not penalised. Teach subject-plus-movement as the FLOOR that always works
and the fix for static output, not as a prohibition on scene description.

**Method lesson, the third instance of the same error this project.** Kling's documentation has no
index and no cross-linking discipline: the i2v rule is absent from every guide and blog that discusses
i2v, and lives alone on a page none of them reference. "I checked N surfaces and found nothing" is NOT
evidence of absence for this vendor. Before declaring any Kling rule missing, enumerate the quickstart
namespace, not just the pages other pages happen to link.

The other stated do-not-restate rule is narrower and concerns voice, not appearance: where a voice tone
is bound to an element, "it's not recommended to set the tone again in the prompt".

## Conflict 4: preservation clauses in edits. UNRESOLVED, flagged.

- VIDEO O1 user guide: exactly one "keep" clause across roughly 20 edit templates, in the green-screen
  recipe only (`Change the background in [@Video] to a green screen, and keep [describe content to keep]`).
  Every other template relies on implicit preservation and the guide never warns that unnamed content
  may drift.
- API 2.0 O1 example: uses an explicit preservation clause unprompted: "Keep all other elements of the
  video unchanged."

The API example is the better model for an agent (an explicit clause costs little and the UI guide's
silence is not a claim that drift cannot happen), but the owner never states a rule either way. Ship
the explicit clause as the recommended technique and mark the owner as silent on whether it is required.
