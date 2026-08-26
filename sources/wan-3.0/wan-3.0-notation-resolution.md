# Wan 3.0: structure decision and source notes

Not a scrape. Hand-authored 2026-08-15 from the sibling scrapes in this folder: the Model Studio API
reference (English and Chinese), the `wan3.0-video` model card, the Alibaba Cloud launch article, and the
WaveSpeed provider pages.

## 1. Merge into `wan-video-v2`, no new scheme

Wan 3.0 joins `guides/wan-video.md`. Scheme, filename and lorebook uid all stay put.

- The prompt formula is unchanged. The owner's own text-to-video sample for 3.0 ("A kitten running on a
  rooftop under the moonlight, neon lights of the city flickering in the distance, cinematic quality,
  smooth camera movement.") is Subject + Scene + Motion + Aesthetic control + Stylization exactly as the
  guide already teaches it.
- The reference notation is the 2.7 notation. `Image 1`, `Video 1`, numbered in upload order, with
  dialogue attached to the named reference in quotes. The owner's 3.0 reference sample is structurally
  the same sentence as the 2.7 one.
- The differences are capability and two field removals, which is the merge case rather than the split
  case.

Video editing stays a 2.7 job (see 6), and the open-weights line is untouched.

## 2. The model is in invitational preview, not public beta

The `wan3.0-video` model card, updated 2026-08-06, ends its description with 该模型当前处于邀测阶段,
"this model is currently in the invitational testing stage". The English card says the same: "This model
is currently in invitational preview."

Press coverage and aggregator pages describe a public beta. The owner surface wins. This also explains
why `wan3.0-video` does NOT appear in the public video model comparison page: it has not been added
there yet, rather than removed. A future pass should not read that absence as a retirement.

Consequence for the guide: 3.0 is tiered `flagship` because tier records position on the capability
ladder, while the model row and the Models section both say plainly that 2.7 is the reachable default.
The 2.7 rows are demoted `flagship` to `std`, following the LTX 2.5 pass.

## 3. Audio references are new, and numbering runs within a kind

From the `media` array documentation on the create-task call:

> The 1st `reference_video` in the array corresponds to **Video 1**, the 2nd corresponds to **Video 2**,
> and so on.

> The 1st `reference_image` in the array corresponds to **Image 1**, the 2nd corresponds to **Image 2**,
> and so on.

> The 1st `reference_audio` in the array corresponds to **Audio 1**, the 2nd corresponds to **Audio 2**,
> and so on.

Plus, on the prompt field itself:

> In reference mode, you can use "Image 1", "Video 1", etc. in the prompt to refer to media assets in
> the corresponding order within the media array.

And, on ordering:

> Images and videos are counted separately, meaning Image 1 and Video 1 can coexist.

So `Audio 1` is genuinely new at 3.0, and the per-kind numbering rule that already applied to images and
videos now spans three kinds. That is the trap worth teaching: an image attached after a video is still
`Image 1`.

What a referenced audio clip is FOR is not stated by the owner. WaveSpeed's Pro Tips are the only
published answer ("Use reference audio when ambience, rhythm, voice style, or soundtrack direction
matters", against images for identity and style and video for motion, pacing, gesture and camera). Taught
in the guide with that attribution rather than as owner fact.

## 4. No negative prompt and no prompt-extension control

Both are absent from the 3.0 API reference. Verified by counting occurrences across the whole scraped
reference: `negative_prompt` 0, `prompt_extend` 0. The complete optional parameter set is `resolution`,
`ratio`, `duration`, `audio`, `seed`, `watermark`.

Both fields are all over the Wan 2.x surfaces in `sources/wan/`, and the guide teaches both: a canonical
default defect bank for the open line, and an access-inverted expansion rule. Neither carries to 3.0.

Two careful distinctions:

- Absence of a `prompt_extend` control is not proof that no rewriting happens. The guide says the control
  is not yours to hold on 3.0, not that expansion has stopped. WaveSpeed still ships a Prompt Enhancer on
  its 3.0 pages, which supports the weaker claim and not the stronger one.
- Absence of a negative field IS a hard fact about where exclusions can go, so that half is stated
  plainly. The owner demonstrates the workaround itself, closing its first-frame sample with "The audio
  of the video consists entirely of rap, with no other dialogue or noise." That is the shape the guide
  teaches: state the wanted content, then close the door in the same clause.

## 5. Clip length is chosen by the prompt now

`duration` defaults to 5 and takes 2 to 30, and:

> When set to `-1`: Smart duration mode, where the model automatically recommends a suitable duration
> based on the input prompt, content, and rich media.

The launch article gives the intent: "so a simple product beat doesn't get padded to 30 seconds and an
ambitious narrative isn't cut short."

This is the same inversion LTX 2.5 introduced, and it gets the same treatment: a version-conditioned
`clip_length` key plus a bullet in "How the model reads prompts", rather than an overwrite of the
existing length advice. Everywhere else in the family you still pick a duration and the prompt has to
fill it.

`ratio` has a matching `adaptive` default that "automatically recommends a suitable aspect ratio based on
the input media proportions and intent", which is the same idea applied to the frame.

## 6. The launch article claims an editing mode the API reference does not expose

The article states: "Video editing capabilities, first introduced in Wan2.7, carry forward into Wan3.0.
You can modify visuals, plot, and dialogue on generated videos."

The 3.0 API reference has no editing mode. The `media` types are `first_frame`, `last_frame`,
`reference_image`, `reference_video`, `reference_audio`, `file`, `link`, and none of them is a video to be
edited in place. Nor is there a separate `wan3.0-videoedit` model.

Resolved on the house rule that the API reference governs. The guide keeps editing on `wan2.7-videoedit`
and says so explicitly in the model row, the Models section and the pitfalls, because "the newest model
does everything" is exactly the assumption that wastes a generation here. Recheck when 3.0 leaves preview.

## 7. Two owner prompt shapes for document-to-video, both real

The launch article's showcase pairs a cafe brand document with a one-line brief:

> Turn this brand story into a warm-toned brand TVC. Make it emotionally resonant - the kind of film that
> makes people want to visit the cafe and stay a while.

The API reference pairs a `.pptx` with a full shot-by-shot direction naming palette, opening frame, camera
moves, and closing beat (the smart-glasses advert prompt).

These are not in conflict, they are two ends of a control range, so both are taught: the API reference
form as the one to reach for when output matters, the brief as the short form. The load-bearing rule is
the division of labour, which neither surface states outright but both demonstrate: the file carries the
CONTENT, the prompt carries the TREATMENT. The smart-glasses prompt never restates a spec from the deck.

## 8. Audio defaults ON

> **audio** `boolean` (Optional) Whether the output video contains audio. `true`: Default value, the output
> video contains audio.

So a 3.0 clip comes back with sound unless silence is requested, and disabling it does not change the
price. Recorded in the Sound section and in the model row, the same way the LTX pass recorded audio-on-by-
default there.

## 9. Owner-stated weaknesses, which is rare and worth keeping

> During internal testing, we identified areas where Wan3.0 still has room to grow: audio texture and
> on-screen text rendering accuracy are improving but not yet where we want them.

The on-screen text admission corroborates a claim the guide already made family-wide, so the guide now
says the rule holds on the newest model too rather than softening with age. The audio-texture admission is
new and pairs badly with audio-on-by-default, hence the pitfall about shipping 3.0 audio unheard.

## 10. Mutually exclusive input groups

> The `reference_xx`/`file`/`link` types and `first_frame`/`last_frame` types are mutually exclusive and
> cannot be used together in the same request.

Plus one file or one link, never both. This is a property of the model rather than of a host, so it is
admissible, but it is stated in the guide as a capability ("pinning an exact first or last frame and using
references or a document are alternatives, not layers") without naming fields or counts.

## 11. Provider coverage and the thinking mode

WaveSpeed carries Wan 3.0 as three endpoints (text-to-video, image-to-video, reference-to-video). FAL does
not appear to carry it yet.

WaveSpeed exposes `thinking_mode`, "deep-thinking mode for complex prompts and richer scene understanding",
default off, recommended "for prompts that combine multiple references or detailed scene requirements".

This partly closes a gap the guide's coverage note had flagged: it previously recorded that no video-side
thinking mode was documented anywhere and that the provider-described thinking mode belonged to Wan 2.7
Image. A video-side one now exists, on 3.0, in provider material only. The note is updated to say exactly
that rather than being deleted.

## 12. Scraping notes

`help.aliyun.com` and `alibabacloud.com` model pages (`wan3-0-video`) are roughly 90 percent navigation
chrome plus a pricing table; the substance is about 60 lines. The page that matters is
`wan3-video-generation-api-reference`, where the prompt field description, the media types and the
per-kind numbering all live. Both sites need `--wait-for 10000` or more.

The Chinese and English API references carry the same content. The Chinese model card was the faster route
to the preview status, since 邀测 is unambiguous where an English "preview" could mean several things.

## 13. Re-verification of 2026-08-26, and what it overturned

The Chinese API reference was updated 2026-08-25 (`更新时间：2026-08-25 18:17:27`). Four claims written on
2026-08-15 no longer hold, and one new mode appeared. Items 14 through 18 record each. The trigger was a
question about provider naming, not a scheduled re-check, which is the argument for re-scraping a
fast-moving owner surface before trusting a two-week-old reading of it.

## 14. wan3.0-video-prime is an owner model, not a provider label

The question was whether WaveSpeed's "Wan 3.0 Prime" was Alibaba's or WaveSpeed's. It is Alibaba's. The
Chinese API reference lists both values for the `model` field:

```text
wan3.0-video-prime：高速版，能力对齐标准版，端到端速度显著提升。
wan3.0-video：标准版。
```

There is an owner model card at `help.aliyun.com/zh/model-studio/wan3-0-video-prime`
(万相视频生成优速版模型) and an English one at `alibabacloud.com/help/en/model-studio/wan3-0-video-prime`
("the accelerated version of the Wan video generation model"). Recorded as `tier: "distilled"`, which is
where the closed vocabulary puts a vendor speed tier.

The owner's 能力对齐标准版 ("capabilities aligned with the standard version") is a vendor claim of no cost,
which the authoring rules say not to restate as fact. The model row therefore reports it as the owner's
statement and says any difference is unmeasured rather than absent. No steps, CFG or sampler are published
for either model, so there is no numeric tell of the kind that exposed HiDream-O1 Dev.

## 15. The Chinese and English references have diverged

Item 12 recorded that the two carried the same content. That is no longer true, and the divergence is
load-bearing rather than cosmetic. As of 2026-08-26 the Chinese reference carries the Prime model, the
video extension mode and the `prompt_extend` switch; the English one still describes the model field as a
fixed single value and has neither Prime nor extension, though it did gain `prompt_extend`.

The guide cited only the English reference. Reading it alone today yields the conclusion that Prime is
provider marketing, which is wrong. Both are now cited, and the guide states that the Chinese one governs
where they differ. The general lesson: for a vendor documenting in two languages, "the API reference
governs" is underspecified until you say which localization, and the vendor's home language leads.

## 16. Editing on 3.0: the launch article was early, not wrong

The 2026-08-15 pass found the launch article claiming 2.7's editing carries forward, found no editing mode
in the API reference, applied the house rule that the reference governs, and documented editing as a 2.7
job. The reference now lists 视频编辑 with a worked example, so the launch article was describing a
destination the reference had not yet reached.

The house rule still produced the right call at the time: on 2026-08-15 the guide would otherwise have
promised a mode that could not be called. Keep the rule; the correction is to re-scrape, not to start
trusting launch material. What changes is the note's tone, which now records the claim as premature rather
than as marketing.

## 17. Prompt extension exists on 3.0 after all

The guide said "the owner documents no expansion control at all" on 3.0 and treated expansion as not the
caller's to switch. `prompt_extend` is now documented in both references, defaulting to `true`. So 3.0 sits
on the ordinary hosted side of the guide's access-inverted expansion rule rather than being a third case,
and the frontmatter key and the prose both collapse back to it.

Worth noting how the earlier error was shaped: absence of evidence read as evidence of absence, on a page
that turned out to be incomplete. The same shape as the Grok `revised_prompt: ""` near-miss.

## 18. Invitational testing has ended, and video extension is new

The standard model card carried **该模型当前处于邀测阶段** on 2026-08-15 and no longer does, so the
INVITATIONAL PREVIEW marking is gone from the model row, from the all-in-one bullet, and from the 2.7
text-to-video row that called itself the default while 3.0 was invite-only.

视频延长 (video extension) is a new mode with real prompt craft attached: the reference says it is driven
by 含延长意图关键词的 prompt, a prompt carrying extension-intent keywords, so the mode is selected by the
words rather than by attaching a video. The owner's example names the clip as 视频1 and leads with the
intent verb. Extension is not new to the guide as a concept, since VACE has covered clip extension on the
open-weights side all along, but it is new to the hosted line.
