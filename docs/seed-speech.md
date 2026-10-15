---
guide: "Seed Speech"
prompt_scheme: "seed-speech"
models:
  - { id: "seed-tts-2.0", access: "closed-weights", tier: "flagship", caps: [text-to-speech, instruction-control, emotion-by-context, built-in-voices, accent-control, pronunciation-override, break-tags, streaming], best_for: "the preset 2.0 voices, and the only model where the context slot reliably works. Reads the line it is answering, or a spoken-style request about how to deliver, and performs the script to match" }
  - { id: "seed-icl-2.0", access: "closed-weights", tier: "std", caps: [text-to-speech, voice-clone, voice-design, pronunciation-override, break-tags, streaming], best_for: "cloned voices and voices made by the voice-design model. Same script field, but the owner's API reference does not support the context slot here, so delivery has to come from the reference recording, the design description and the words" }
  - { id: "seed-tts-1.0", access: "closed-weights", tier: "legacy", caps: [text-to-speech, emotion-control, built-in-voices, streaming], best_for: "superseded. Its multi-emotion voices take a preset emotion label per request instead of an instruction, and only the labels listed for that voice" }
capabilities: [text-to-speech, instruction-control, emotion-by-context, built-in-voices, accent-control, pronunciation-override, break-tags, streaming, voice-clone, voice-design, emotion-control]
prompt:
  languages: ["zh", "en", "ja", "ko", "es", "pt", "id", "ms", "th", "vi", "fil", "de", "fr", "ru", "ar", "yue", "more"]
  speech_languages: "sixteen on 2.0: Chinese, English, Japanese, Korean, Mexican and Castilian Spanish, Brazilian Portuguese, Indonesian, Malay, Thai, Vietnamese, Filipino, German, French, Russian and Arabic, plus European Portuguese on cloned voices only. A further set of European languages and Hindi works only on the multilingual Chinese voices. Dialects (Cantonese, Shanghainese, Beijing, Tianjin, Sichuan, Shaanxi, Henan, Dongbei) need a voice that lists them"
  script: "the script field is the words to be spoken, verbatim. Direction does not go in it. Brackets, markdown and emoji in the script are read out unless a host strips them"
  direction_syntax: "one separate context slot that holds EITHER a delivery request addressed to the speaker OR the line the speaker is replying to, never both, because only its first entry is used. SSML is a separate opt-in markup for pauses and pronunciation on Chinese and English voices"
  voices: "three routes: a preset 2.0 voice, a voice cloned from a reference recording, or a voice designed from a short text description or a character image. Cloned and designed voices run on the clone model, which loses the context slot"
  length_strategy: "write the script as it should be heard. Length is not a quality lever. The context slot is where effort pays: a specific, emotionally loaded request or a real preceding line"
  auto_expand_behavior: "none. Nothing rewrites the script or the context slot"
  negatives: "no negative field. A wrong delivery is fixed by rewriting the request positively, quoting a different preceding line, or recasting the voice"
sources:
  official: ["https://www.volcengine.com/docs/6561/1871062", "https://www.volcengine.com/docs/6561/2528925", "https://www.volcengine.com/docs/6561/2499930", "https://www.volcengine.com/docs/6561/1257544", "https://www.volcengine.com/docs/6561/2298705", "https://www.volcengine.com/docs/6561/2277844", "https://www.volcengine.com/docs/6561/1330194", "https://docs.byteplus.com/en/docs/byteplusvoice/texttospeechv2", "https://docs.byteplus.com/en/docs/byteplusvoice/unidirectional_tts_http"]
  provider: ["https://fal.ai/models/fal-ai/bytedance/seed-speech/tts/v2/api"]
  community: []
last_verified: "2026-10-15"
---

# Seed Speech: prompting and usage guide

<rules id="global">

- This guide covers prompt craft only. For endpoints, parameters, limits, and code, consult the specific provider or proxy's API docs; they differ and are out of scope here.
- It covers ByteDance's text-to-speech line: the 2.0 model for preset voices, the 2.0 clone model for cloned and designed voices, and the superseded 1.0 model.
- ByteDance ships three guides here. Seedream is image, Seedance is video, and this one is speech. Seed Audio, the model that writes dialogue, score and sound effects from one descriptive prompt, is a different scheme and nothing below applies to it. The realtime voice-chat models are agents, not text-to-speech, and are out of scope too.
- THE SCRIPT IS SPOKEN AS WRITTEN. The script field holds the words to be heard and nothing else. A stage direction typed into it becomes spoken words.
- Direction has its own channel: one context slot beside the script. It takes either a request addressed to the speaker ("Could you speak a bit slower?") or the line the speaker is answering. Only one entry is used, so it is one or the other per request.
- The model is built for conversation. It reads the slot as what was just said to the speaker and shapes the reply's tone, pauses and emotion to fit. That is why every owner instruction is phrased as something said TO the speaker.
- Write the script in the language it should be spoken. This is not a prompt to be translated into English.

</rules>

## Model names and aliases

| Surface | Name used |
| --- | --- |
| Volcengine (China) docs and console | 豆包语音合成模型2.0, Doubao-TTS 2.0; clone model 豆包声音复刻模型2.0 |
| BytePlus (international) | Seed Speech, TTS 2.0, Voice Replication 2.0 |
| Owner API model ids | `seed-tts-2.0`, `seed-icl-2.0`, `seed-tts-1.0` |
| FAL | Bytedance Seed Speech Text to Speech, `seed-speech/tts/v2` |

<rules id="naming">

- Teach the owner ids. "Doubao TTS", "Seed Speech" and "Seed-TTS 2.0" all name the same 2.0 model; translate them on sight.
- "Seed Speech 2.0" on BytePlus is a platform bundle of TTS 2.0 and a speech recognizer. Only the TTS half is a prompting target.
- Seed Audio is NOT a newer Seed Speech. It is a separate model with a different prompt grammar.
- Hosts relabel the context slot. FAL calls it a voice instruction; the owner API calls it context texts. On every host it is the same slot and takes either use.
- ICL means the clone model ("in-context learning" from the reference clip). A request naming ICL 2.0 is a cloned or designed voice.

</rules>

## TL;DR

<template id="quickstart">

CONTEXT: {one line said TO the speaker: a delivery request such as "Could you say this like you are holding back tears?", OR the line the speaker is replying to}
SCRIPT: {the exact words to be spoken, punctuated for the ear, with no brackets, markdown or emoji}

</template>

`CONTEXT:` and `SCRIPT:` are labels in this guide marking which field a line goes in. Never send the labels themselves.

## Models and when to use which

- `seed-tts-2.0`: the default. Preset 2.0 voices, the full context slot, dialects on the voices that list them, and the voices tuned for many languages. Pick this whenever a preset voice will do.
- `seed-icl-2.0`: cloned voices and voices from the voice-design model. Pick it for a specific person's voice or a designed character. The owner's API reference says the context slot is not supported here; an older reference says the default clone tier drops it silently and only an expressive tier honours it. Plan for no slot: put the emotion in the reference recording, the design description and the words.
- `seed-tts-1.0`: superseded. Its multi-emotion voices take a preset emotion label instead of an instruction. Use it only when a voice exists nowhere else.

## How the model reads prompts

- Two inputs, read together. The script is the reply; the context slot is the turn before it. The owner's own comparison is the Beijing example below: the same script with no context reads as a flat statement, and with the question in the slot it gains the hesitations of someone thinking aloud.
- The model already infers emotion from the script's words. A script that is unambiguous on the page often needs no slot at all. Use the slot when the words alone could go two ways, or to push intensity.
- The slot is read as speech, not as a parameter. A request written the way a person would say it ("嗯，你的语气再欢乐一点") is the owner's form. A bare tag such as "happy" is the 1.0 emotion preset's form and does not belong here.
- Punctuation does the prosody. Ellipses, commas and question marks are read as hesitation, beats and rising pitch. The owner's scripts are punctuated heavily on purpose, often with an ellipsis mid-word for a stammer.
- Each voice has a recommended mode. Every preset Chinese 2.0 voice is marked for instruction following. In the foreign-language voice list each voice carries one: QA means it is tuned for a delivery request in the slot, Context means it is tuned for a preceding line. Match the slot to the voice.
- Global rate, volume and pitch are separate request settings. Use them for a whole-clip change; use the slot for the performance.

## Prompt structure

<rules id="structure">

- Write the script exactly as it should be heard: contractions, fillers ("嗯", "啊", "well"), false starts and fragments. They are what make it sound spoken.
- Punctuate for the ear. An ellipsis is a hesitation, a comma a short beat, a full stop a longer one, a question mark a rise. Use the full-width forms in a Chinese script.
- Keep direction out of the script. Bracketed notes, asterisk actions, speaker labels and parenthetical asides are all read aloud unless the host strips them.
- Strip markdown and emoji before a reply from a chat model becomes a script. By default the markup is kept, and the owner's example reads " **你好** " as "星星你好星星", the asterisks spoken as "star".
- One voice per request. There is no speaker-turn syntax. A dialogue is one request per line.
- Spell out what the reader could misread: unusual names, initialisms, units, mixed digits. Or pin them with a pronunciation rule (below).
- Math reads properly only when the host's LaTeX mode is on. Otherwise write the formula in words.

</rules>

<template id="general">

CONTEXT: {a delivery request in the speaker's own register, naming the emotion and, if needed, the pace, voice quality or dialect | OR the exact preceding line from the other party}
SCRIPT: {spoken words, with ellipses for hesitation and real punctuation for every beat}

</template>

## The context slot: delivery requests

<rules id="instruction">

- Address the speaker. Two owner forms work: a request ("你可以用特别特别痛心的语气说话吗？", "Could you speak in a very, very heartbroken tone?") and a director's line ("用低沉沙哑的语气、带着沧桑与绝望地说"). Both are said TO the voice.
- Name the emotion, then its texture. "带点害羞又藏着温柔期待" layers two feelings and a hidden one; the owner's multi-emotion examples all stack like this rather than naming one adjective.
- Voice quality goes in the request too: "低沉沙哑" (low and husky), "颤抖" (trembling), "哭腔" (on the edge of tears). These change the sound, not only the mood.
- The owner lists what a request can control: overall emotion (sad, angry), dialect (Sichuanese, Beijing), manner (coaxing, intimate, quarrelling, a cute high voice), pace and pitch. Volume is phrased as a request too: "你嗓门再小点" ("Lower your voice a bit").
- A whispered or ASMR delivery is a request, not a voice: "用asmr的语气来试试撩撩我".
- Push intensity with the words of the request. The owner doubles intensifiers on purpose ("特别特别痛心", "very, very heartbroken").
- One request per call. Only the first entry in the slot is used, so a second request is ignored.
- Write the request in the script's language. Every owner pairing matches, Chinese with Chinese and English with English; no owner surface shows them crossed.
- The slot is not spoken and is not billed. It costs nothing to make it specific.

</rules>

<example use_case="argument delivery from a request">

```text
CONTEXT: 你得跟我互怼！就是跟我用吵架的语气对话
SCRIPT: 那你另请高明啊，你找我干嘛！我告诉你，你也不是什么好东西！
```

*Why: the owner's example. The request sets up a fight as a relationship ("talk back at me"), not as a label, and the script supplies exclamation marks the delivery can lean on.*

</example>

<example use_case="layered emotion with hesitation">

```text
CONTEXT: 用试探性的犹豫、带点害羞又藏着温柔期待的语气说
SCRIPT: 哎，能…… 能一起撑伞不？这雨突然就大了！其实…… 我盼这场雨好久了，总觉得，这样的天气，能离你近一点 。
```

*Why: the owner's example. Three feelings stacked in one request, tentative, shy and hopeful, and a script that already stammers ("能…… 能") so the request has something to colour.*

</example>

<example use_case="voice quality and despair in a long monologue">

```text
CONTEXT: 用低沉沙哑的语气、带着沧桑与绝望地说
SCRIPT: 高兄，你看这烛火，要灭了…… 我这一生，像追着光跑的蛾，可光太暗，风太猛，到最后，连翅膀都烧没了。我多想再提剑走一趟大漠，再醉饮一回长安酒，可这副身子，这世道，连这点念想，都要碾碎了喂尘土……你说，下辈子，能不能让我生在一个，不用靠 "不一样"，就能活成自己的人间啊 。
```

*Why: the owner's long example. The request names a voice quality (low, husky) as well as two emotions, and the script's commas break every clause so the weariness has room. The owner's curly quotes around 不一样 are written straight here.*

</example>

<example use_case="with and without a request">

```text
CONTEXT: 用颤抖沙哑、带着崩溃与绝望的哭腔，夹杂着质问与心碎的语气说
SCRIPT: 我逆转时空九十九次救你，你却次次死于同一支暗箭。谢珩，原来不是天要亡你……是你宁死也不肯为我活下去。
```

*Why: the owner's A/B pair. Without the slot the line reads as narration; with it the same words become an accusation through tears. The request names the sound (trembling, husky, crying) and the stance (accusing, heartbroken), which is the full owner formula.*

</example>

<example use_case="English request in a natural register">

```text
CONTEXT: Could you speak in a very, very heartbroken tone?
SCRIPT: I kept the porch light on every night. I told myself you'd see it from the road... and you never came.
```

*Why: the request is the owner's English example, verbatim; the script is built for this guide. The request is phrased as a question to the speaker, the owner's form, and the ellipsis gives the break before the last clause.*

</example>

## The context slot: preceding lines

<rules id="context">

- Put the other party's last line in the slot, word for word, and the reply in the script. The slot is quoted, never spoken.
- Pick the line that sets the emotion. The owner's reunion examples quote "是… 是你吗？" so the reply comes out moved, without any instruction to be moved.
- After a chat model, send the user's last message. The owner's assistant example: in a conversation where the user says they were dumped and then that they are not sad at all, quote that last message so the cheerful reply sounds like a reaction to it.
- Use this mode for voices marked Context in the voice list, and on any voice when the scene already has dialogue. It carries tone more precisely than a description of the tone would.
- Within one conversation, keep each line's request in the same session if the host offers a session or section id. Otherwise the previous line in the slot is the only continuity there is.

</rules>

<example use_case="a question in the slot turns a statement into thinking aloud">

```text
CONTEXT: 你怎么评价北京这个城市？
SCRIPT: 北京…因为我来，这是第二次，上一次是在一…八年还是什么时候来过一次但是时间很短也没有时间去，真正的去游历，所以北京对我来说…只是…还存在一种想象之中啊，嗯没有太多的，直观的体验。
```

*Why: the owner's with-and-without comparison. The owner notes that without the question the model sees only the reply; with it the delivery picks up the pauses of someone answering on the spot. The script's own ellipses and filler ("嗯") supply the places to pause.*

</example>

<example use_case="assistant reply after a chat model">

```text
CONTEXT: 我才不难过呢，那个人太渣了。
SCRIPT: 哈哈，那就好，那你吃点好吃的好好庆祝一下。
```

*Why: the owner's assistant example. The slot holds the user's latest message, not the whole history and not a description, so the reply's laugh lands as relief at what the user just said.*

</example>

## Dialogue and multiple speakers

<rules id="dialogue">

- No speaker turns inside one script. A dialogue is a chain of requests, one per line, each with its own voice.
- Chain them through the slot: each line's request quotes the previous line. That is how the owner's two reunion examples are built, one answering the other.
- Cast each speaker once and keep the voice fixed across the chain.
- For a scripted scene on voices tuned for instructions, a request can stand in for the other speaker's line. You still get one or the other per request, never both.

</rules>

<example use_case="two-voice reunion chained through the slot">

```text
Line 1, voice A
CONTEXT: 是… 是你吗？怎么看着… 好像没怎么变啊？
SCRIPT: 你头发长了… 以前总说留不长，十年了… 你还好吗？

Line 2, voice B
CONTEXT: 挺好的… 就是去年整理旧书，翻到你给我写的毕业留言，还想… 什么时候能再见到你。
SCRIPT: 我也带着这个… 你看，当时在操场拍的，你笑起来眼睛都眯成缝了。
```

*Why: both pairs are the owner's, shown as two separate requests. Each slot quotes the other speaker, and the owner notes the model reads the reunion from the quoted line alone and answers in an excited tone.*

</example>

<example use_case="English scene built as a chain">

```text
Line 1, voice A (the mother)
CONTEXT: Mom, I got the job. The one in Singapore.
SCRIPT: Singapore? Oh... oh, honey, that's wonderful. That's so far. No, it's wonderful.

Line 2, voice B (the son)
CONTEXT: Singapore? Oh... oh, honey, that's wonderful. That's so far. No, it's wonderful.
SCRIPT: Hey. It's a fourteen-hour flight, not the moon. You'll visit. I'll make you.
```

*Why: built for this guide to the owner's chain pattern. Line 1's slot holds the son's announcement, line 2's slot holds the mother's reply verbatim, and each script carries its own hesitations ("Oh... oh") rather than asking for them.*

</example>

## Voices

<rules id="voices">

- Preset voices: each 2.0 voice id names its language, gender and character, and the owner's list marks which dialects and modes it supports. Casting comes first; a request moves a voice, it does not replace one.
- English on a Chinese voice works, but the owner recommends an English voice for English. The Chinese 2.0 voices the list marks for 30-plus-language recognition also read the extra languages, and only those voices reach the less common European languages and Hindi.
- Cloning: the reference recording IS the prompt. The owner asks for a clean single-speaker mono recording of about fourteen to thirty seconds with steady emotion, a register that fits the intended use, and both languages if the voice will mix Chinese and English. Noise, several speakers, heavy dialect and dramatic swings in the reference all carry over.
- A calm reference gives a stable clone; an emotional one varies from take to take. The owner recommends calm references for assistants and support lines.
- A clone follows the meaning of the text more than the emotion of the reference. Without the context slot, the script's words are what carry the emotion, so write them to.
- A host's fidelity mode, where offered, copies the reference's accent and emotion more closely, at the cost of speaking only the reference's language.
- Voice design: describe the voice in one line, or give a character image, and preview it on a sample line. The image wins when both are given.
- Write the description as a person plus delivery: gender and age, voice quality, accent, the role or scene, then pace, intonation and emotion. The owner's previews follow that order exactly.
- A designed voice runs on the clone model, so it inherits the missing context slot. Bake the intended emotion into the description and preview it on a line in that emotion.
- A designed voice is either Chinese or English, chosen when it is designed. Write the preview line in that language.

</rules>

<example use_case="voice design, the owner's short form">

```text
Description: 女性，语速中等偏快，语调低沉有力
Preview line: 夜色渐浓，城市的灯火次第亮起，每个人都在为自己的生活奔波，从未停歇。
```

*Why: the owner's request example. Three comma-separated attributes, gender, pace and intonation, are enough to design a voice; the preview line is calm narration that shows off the low, forceful intonation.*

</example>

<example use_case="voice design, the owner's full character form">

```text
星象师(男性中年40-50岁、沉稳有磁性带威严、普通话、庄重古典) 语速中等偏慢、语调起伏较大、愤怒痛心地质问道："我绘星象助你避灾，你却用星轨布杀阵！长公主，紫微垣的星光落进你眼里......怎么就化成了鸩毒？"
```

*Why: the owner's preview format: a role name, then a parenthesis of gender and age, voice quality, accent and style, then pace, intonation and emotion, then the line in quotes. Because the designed voice has no context slot, the anger goes into the design and the line together.*

</example>

<example use_case="English voice design for a narrator">

```text
Description: Female, about sixty, warm and slightly husky, soft Southern American accent, bedtime-story narrator; unhurried pace, gentle falling intonation, fond and amused
Preview line: Now, the fox had a plan, and like most of the fox's plans, it was clever, it was quick, and it was going to go terribly wrong.
```

*Why: built for this guide on the owner's character order, person first and delivery last. The preview line has the amused rhythm the description promises, so the preview actually tests it.*

</example>

<example use_case="recovering emotion on a clone">

```text
CONTEXT: 用最悲伤的语气演绎下面这句话：
SCRIPT: 引航者...你为什么说这些话...真的好过分啊！呜呜...你是不是在开玩笑，别吓我好不好，我不想失去你
```

*Why: the owner's clone best-practice example. It worked on the expressive clone tier, but the current API reference says the clone model does not take the slot, so treat this as host-dependent. The script's sobs and ellipses still carry the grief if the slot is dropped.*

</example>

## Pronunciation and pauses

<rules id="pronunciation">

- Two tools, never on the same words. A pronunciation dictionary rule and SSML on the same span cancel each other's effect; pick one.
- Dictionary rules, where a host exposes them, pair a word with a reading: `北京/(bei3)(jing1)` fixes a Pinyin reading with tone digits, and `omg/oh my god` rewrites the text before it is read. They work on Chinese and English 2.0 and clone voices.
- SSML is opt-in markup, sent instead of plain text, wrapped in one `<speak>` root. Without the root it is not parsed as SSML and the tags are spoken.
- Useful tags: `<break time="500ms"/>` for a timed pause (time only, no strength), `<phoneme alphabet="py" ph="xi1 xi1">茜茜</phoneme>` for Pinyin (`cmu` and `ipa` also exist), `<say-as interpret-as="...">` for how digits, dates and IDs are read, and `<sub alias="...">` to swap in spoken text.
- SSML works on Chinese and English 2.0 and clone voices, but not on voices whose id ends `_saturn_bigtts`, and not on bidirectional streaming. Keep SSML requests short, tags included; long ones fail more often. The prompt-tone sound tag does not work on 2.0 voices.
- Without SSML, punctuation is the pause control.

</rules>

<example use_case="SSML pause and polyphone fix">

```text
<speak>要一起去<phoneme alphabet="py" ph="chi1">吃</phoneme>饭吗<break time="600ms"/>我请客。</speak>
```

*Why: the phoneme tag is the owner's own example, with a pause added for this guide. One root, a short request, and a timed break where punctuation alone would give too short a beat.*

</example>

## Languages and dialects

<rules id="languages">

- The language follows the script. A host can pin it, or detect it automatically; automatic detection reads the FIRST sentence, so open in the target language.
- Chinese mode allows Chinese-English mixing. Other mixes are not covered: with a language pinned, text in other languages is skipped or fails.
- Portuguese and Spanish default to the Brazilian and Mexican variants. European Portuguese and Castilian Spanish need the language pinned explicitly.
- The Chinese-English voices and the voices for other languages are separate models underneath, each best in its own languages. Cast a native voice for a non-Chinese script.
- Dialect needs a voice that lists it. On those voices a dialect can be asked for in the slot ("用四川话说") or pinned by the host. A dialect-free voice will not produce one.

</rules>

## Legacy 1.0 emotion presets

<rules id="legacy">

- The 1.0 multi-emotion voices take an emotion label per request, not an instruction: Chinese voices use labels such as happy, sad, angry, surprised, fear, hate, excited, coldness, neutral, depressed, lovey-dovey and shy; English voices use neutral, happy, angry, sad, excited, chat, ASMR, warm, affectionate and authoritative.
- Each voice supports only its own subset of labels, listed per voice. A label outside it does nothing.
- Intensity steps are nonlinear; a middle and a high setting can sound alike.
- The label is per request. A script that changes emotion has to be split.
- Many 1.0 voices have a 2.0 counterpart under the same name. Moving to it trades the label for the context slot, which is the better control.

</rules>

## Pitfalls and anti-patterns

- Writing direction in the script: "(sighs)", "*laughs*", "[softly]" and "she whispers" are all spoken. Direction goes in the context slot.
- Sending markdown or emoji from a chat model: by default asterisks are read as "star" and emoji are kept. Strip them first.
- Putting a request and a preceding line in the slot together: only the first entry is used. Choose one.
- Writing the request as a tag: "sad" or "angry, fast" is the 1.0 label style. Phrase it as something said to the speaker.
- Relying on the slot for a cloned or designed voice: the API reference does not support it there, and the default clone tier drops it without an error. Write the emotion into the words, the reference or the design.
- Using a request on a voice tuned for context: voices marked Context in the voice list want the preceding line.
- Writing a whole dialogue as one script: there are no speaker turns. One request per line, chained through the slot.
- Expecting the console's bracket descriptions through the API: the console's early-access "[description] before a sentence" feature is a console form, and no current API reference documents it. Through an API, brackets are spoken.
- Forgetting the SSML root: without `<speak>` the tags are read out.
- Mixing a pronunciation rule and SSML on the same word: neither takes effect cleanly.
- Opening a foreign-language script with a Chinese or English sentence while relying on auto-detection: the first sentence sets the language.
- Asking for a dialect on a voice that does not list it: cast a dialect voice instead.
- Translating the script to English: the script's language IS the output language.

## Sources

Trust order is official, then provider, then community. Official wins on any conflict.

- Official (ByteDance, Volcengine): [voice instructions and quoted context](https://www.volcengine.com/docs/6561/1871062), the owner's example library for both uses of the slot; the current [HTTP synthesis reference](https://www.volcengine.com/docs/6561/2528925) and its WebSocket siblings, for the single-entry slot, the clone restriction, the markdown and emoji defaults, language and dialect behaviour and the pronunciation rule format; the [model list](https://www.volcengine.com/docs/6561/2499930) for the 2.0 against clone capability table and languages; the [voice list](https://www.volcengine.com/docs/6561/1257544) for per-voice modes, dialects and the 1.0 emotion labels; the [clone best practice](https://www.volcengine.com/docs/6561/2298705) for reference recordings and the assistant-reply example; [voice design](https://www.volcengine.com/docs/6561/2277844) with the product overview's character previews; [SSML](https://www.volcengine.com/docs/6561/1330194); the historical V3 references for the clone tiers and the old sentence tag.
- Official (ByteDance, BytePlus): the [TTS 2.0 overview](https://docs.byteplus.com/en/docs/byteplusvoice/texttospeechv2) for the query-response design, and the [unidirectional HTTP reference](https://docs.byteplus.com/en/docs/byteplusvoice/unidirectional_tts_http) for the English request examples.
- Provider (FAL): the [Seed Speech text-to-speech API](https://fal.ai/models/fal-ai/bytedance/seed-speech/tts/v2/api), which exposes the slot as a voice instruction.

Coverage note: Volcengine's documentation renders client-side, but its docs site serves every page as markdown through its own document-detail endpoint, which is where all of the Volcengine material here comes from. The owner's pages disagree on three things, recorded in `sources/seed-speech/seed-speech-notation-resolution.md`: whether cloned voices take the context slot (resolved on the current API reference: no), whether 2.0 voices take SSML (resolved on the newest reference: yes for Chinese and English), and whether an inline sentence tag exists (only in the console as an early-access feature, and in a superseded reference for the expressive clone tier).

Last verified: 2026-10-15.
