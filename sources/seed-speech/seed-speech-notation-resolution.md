# Seed Speech: structure decision and source notes

Not a scrape. Hand-authored 2026-10-15 from the owner surfaces in this folder.

- `volc/`: Volcengine documentation (library 6561, 豆包语音), fetched as markdown through the docs site's own
  JSON endpoint, `https://www.volcengine.com/api/doc/getDocDetail?DocumentID=<id>&LibraryID=6561&type=online`.
  The `MDContent` field is the rendered markdown; `Content` is a rich-text delta for newer pages. The page list
  comes from `https://www.volcengine.com/api/doc/getDocList?LibraryID=6561`. Each file opens with a comment
  carrying the title, the page's `UpdatedTime` and its canonical URL. This endpoint is why the guide was writable
  at all: the rendered docs are client-side and returned an empty shell to every earlier fetch.
- `byteplus-*.md`: BytePlus (international) docs and launch post, firecrawl with `--wait-for 9000`.
- `fal-seed-speech-tts-v2-llms.txt`: FAL's wrapper, approved provider.

## 1. Scope and scheme

One scheme, `seed-speech`, covering the owner's text-to-speech line: `seed-tts-2.0` (preset 2.0 voices),
`seed-icl-2.0` (cloned voices, and the voices produced by the voice-design model), and `seed-tts-1.0` as legacy.
They share the script field and differ in which direction channel they accept.

Out of scope, each a different grammar or a non-generation surface:

- Seed Audio (豆包音频生成模型, `seed-audio-1.0`): one prompt describing dialogue, score and foley with `@音频N`
  references. A separate scheme; a future `seed-audio` guide.
- The S2S realtime models (全双工, O2.0, SC2.0) and the podcast model: agent and dialogue-generation surfaces.
- ASR, simultaneous interpretation, voice conversion.

## 2. One slot, two uses: instruction or preceding line

The API has a single context slot (`context_texts` on the owner API, a list of which "only the first value is
effective"). The console exposes it as a dropdown with two modes, 语音指令 (voice instruction) and 引入上文
(quote the preceding text), feeding the same slot (console GIFs on 6561/1871062, verified frame by frame).
So an instruction and a preceding line cannot be sent together. The guide teaches one or the other per request.

The model is described as Query-Response (BytePlus TTS 2.0 overview; Volcengine 1871062 "传统TTS，模型只能看到
response文本"). Every owner instruction example is addressed to the speaker, either as a request ("你可以说慢一点吗？",
"Could you speak a bit slower?") or as a director's line ("用低沉沙哑的语气、带着沧桑与绝望地说"). Taught as: write
the slot as something said TO the speaker.

FAL names the field `voice_instruction` and documents only the instruction use. Owner semantics govern: the same
slot carries a preceding line. Recorded as a host label, not a narrower capability.

Per-voice mode: the foreign-voice table on 6561/1257544 gives each voice a 推荐推理模式 (recommended inference
mode), QA or Context, with matching 支持能力 (指令遵循 or 上下文遵循). Every row of the Chinese 2.0 table is marked
指令遵循. Taught: check the voice's mode before choosing what goes in the slot.

## 3. Instructions on cloned and designed voices: owner against owner

- Current API references (2528925 HTTP, 2534913 and 2532486 WebSocket, all updated 2026-09-28/29): the `model`
  field is needed only for cloned voices, "且指定后不支持使用语音指令context_texts".
- Model list (2499930, 2026-09-29): 语音指令 row is a check for TTS 2.0 and a dash for ICL 2.0 (icons decoded).
- Historical V3 references (1598757, 1719100, 1329505, 2026-05-25): clones take `seed-tts-2.0-standard`
  (default, "不支持语音指令QA和语音标签Cot能力。如果传入QA或Cot参数，接口会过滤掉") or `seed-tts-2.0-expressive`
  (supports both, "存在效果抽卡的情况").
- Clone best practice (2298705, 2026-09-29): demonstrates `context_texts: ["用最悲伤的语气演绎下面这句话："]` on a
  clone to recover the reference's emotion.
- Quickstart (2119699, 2025-12-09): the console lets clones use instructions and quoted context.

Resolved on the API reference, which governs: do not rely on the slot for a cloned or designed voice. The
historical text explains the demonstrations: they ran on the expressive variant, and the standard default drops
the slot silently. The guide says the slot may be filtered without an error and moves delivery into the
reference recording, the design description and the words. Designed voices count as clones: the voice-design
page (2277844) says the designed voice id is used through the clone synthesis path.

## 4. Inline sentence tags

- Historical V3 references: `<cot text=急促难耐>...</cot>` with a parser switch, "仅适用于“豆包声音复刻大模型
  2.0”的表现力增强版本", a single sentence of about 64 characters including the tag, scoped to that sentence.
- BytePlus TTS 2.0 overview: "Emotion Tag. You can enter emotion tag to control sentence level emotion."
- Console (screenshots on 2119699): "在任意句前添加[心理活动、细腻表情、肢体动作等描述]，可增强表现力", marked 抢先体验
  (early access), with a 【】 shortcut and the example "[声音结结巴巴，但努力想表现出强硬]".
- Current API references: no inline tag at all, and a field that strips parenthesised text only when a host
  enables it, otherwise "括号内内容会被正常朗读".

Resolved: no current API surface documents an inline direction tag for the preset voices. The console bracket form
is a UI early-access feature and is recorded as such, not taught as API syntax. `<cot>` is recorded as the
historical expressive-clone form. The guide's rule is that brackets in the script are spoken unless a host says
otherwise. The "括号指令" wording on third-party pages (ai-bot.cn) was traced and has no owner source.

## 5. SSML on 2.0 voices

- TTS product intro (1257543, 2026-07-10) and the historical references: 2.0 voices and ICL 2.0 voices "暂不支持".
- SSML page (1330194, 2026-09-10): Mandarin voices only; voices whose id ends `_saturn_bigtts` excluded; not on
  bidirectional streaming; keep SSML input short including tags; `<soundEvent>` not on 2.0 or ICL 2.0 voices.
- Current HTTP reference (2026-09-29): SSML supported for Chinese and English voices only.
- Model list: SSML row reads 仅支持标签 for both TTS 2.0 and ICL 2.0.

Resolved on the newest API reference: SSML works on 2.0 voices for Chinese and English, minus the `_saturn_`
voices, with the SSML page's short-input and no-bidirectional cautions kept. The language scope is the reference's
(Chinese and English) rather than the SSML page's (Mandarin only), because it is newer.

## 6. Clone reference length

Clone best practice: 14 to 30 seconds, wav, single speaker, mono, steady emotion. Product intro (163032): "建议使用
10-15 秒" and "最短录制5s音频即可启动复刻". BytePlus voice replication 2.0: same 14 to 30 as the best practice.
Taught as the dedicated best-practice page's window, since BytePlus repeats it.

## 7. Markdown and emoji are read by default

The markdown filter field defaults to off, and the reference's own example says off reads " **你好** " as
"星星你好星星". The emoji filter also defaults to off. Taught as a pitfall: strip markdown and emoji from LLM
output before it becomes a script.

## 8. Languages

TTS 2.0 language table (2499930): zh, en, ja, ko, es-MX, pt-BR, id, ms, th, vi, fil, de, fr, es-ES, ru, ar;
European Portuguese for ICL 2.0 only. The explicit-language field lists 31 codes; the extra Northern European and
other languages work only on the multilingual `zh_..._uranus_bigtts` voices. Auto-detection reads the first
sentence. `zh-cn` is "中文为主，支持中英混读". Dialects (Cantonese, Shanghainese, Beijing, Tianjin, Sichuan,
Shaanxi, Henan, Dongbei) need a dialect-capable voice; 1871062 also lists dialect as something an instruction
controls.

## 9. Provenance of examples

Owner examples are verbatim from 1871062 (instruction and context libraries), 2298705 (clone emotion and the
assistant-reply context), 2277844 and 163032 (voice design), 1330194 (SSML), 2528925 (pronunciation rules) and the
BytePlus API reference (English instructions). Chinese ellipses are kept as written. The guide's English scripts,
dialogue chain, design description and SSML sample are built to those rules and say so in their Why lines.
