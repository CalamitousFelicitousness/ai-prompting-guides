"""Build the SillyTavern prompting-guides lorebook from guides/*.md.

Writes the canonical file that ST imports, plus a dated copy under archive/.

The canonical filename never changes on purpose. ST takes the world name from
the filename, and character cards link a lorebook by world name, so a versioned
filename would break every card link on each import. The build identifies itself
from inside instead: the [Meta] Version entry's memo shows it in ST's entry list,
and the always-loaded manifest lets the model report it on request.

The build number only advances when the guide content actually changes, so
re-running on an unchanged set is a no-op.

Content rule for a guide entry, verified byte-for-byte against the hand-made
export this replaced: <promptgen_SCHEME> wrapping the guide body with the YAML
frontmatter stripped, from the H1 through the end of Pitfalls, Sources dropped.

    python3 build-lorebook.py                      # dry run, reports what would change
    python3 build-lorebook.py --write              # write the files ST imports
    python3 build-lorebook.py --write --publish    # and refresh the tracked repo copies
"""
import copy
import json
import re
import shutil
import sys
from pathlib import Path

GUIDES = Path(__file__).parent / "guides"
LOREBOOK = Path("/mnt/c/Users/ohiom/Downloads/[Instructions] Prompting guides.json")
ARCHIVE = LOREBOOK.parent / "archive"

# The published copies. guides/ is a symlink into the OneDrive vault and git stores
# a symlinked directory as a link blob rather than as files, so the tracked copy has
# to be a real directory that --publish refreshes.
DOCS = Path(__file__).parent / "docs"
REPO_LOREBOOK = Path(__file__).parent / "lorebook" / LOREBOOK.name
MODALITY = {"IMG": "image", "VID": "video"}

# uid -> (scheme, modality, display name, match keys). uids are identity and must
# stay stable across rebuilds; displayIndex below is what controls list order.
CATALOG = {
    "2":  ("anima", "IMG", "Anima", ["anima"]),
    "3":  ("flux-2", "IMG", "FLUX.2",
           ["flux", "flux.2", "flux 2", "flux2", "bfl", "black forest labs"]),
    "4":  ("gemini-image", "IMG", "Gemini Image (Nano Banana)",
           ["gemini-image", "gemini image", "nano banana", "nano-banana", "nanobanana",
            "nano banana pro", "gemini 3 pro image", "gemini 3.1 flash image"]),
    "20": ("gpt-image", "IMG", "GPT Image",
           ["gpt-image", "gpt image", "gpt-image-2", "gpt image 2", "gptimage"]),
    "28": ("grok-imagine-image", "IMG", "Grok Imagine Image",
           ["grok", "grok imagine", "grok-imagine", "grok imagine image",
            "grok-imagine-image", "grok image", "grok imagine 2", "xai"]),
    "5":  ("hidream-o1", "IMG", "HiDream-O1", ["hidream", "hidream-o1", "hidream o1"]),
    "26": ("hunyuan-image", "IMG", "HunyuanImage",
           ["hunyuan", "hunyuanimage", "hunyuan image", "hunyuan-image",
            "hunyuan image 3", "hunyuan image 3.0", "hunyuanimage-3.0"]),
    "6":  ("ideogram-4", "IMG", "Ideogram 4", ["ideogram", "ideogram 4", "ideogram4"]),
    "7":  ("illustrious-noob", "IMG", "Illustrious / NoobAI",
           ["illustrious", "illustrious xl", "noobai", "noob-ai", "noobxl", "noob xl"]),
    "8":  ("kling-image", "IMG", "Kling Image", ["kling-image", "kling image"]),
    "9":  ("krea-2", "IMG", "Krea 2", ["krea", "krea 2", "krea2"]),
    "10": ("qwen-image", "IMG", "Qwen-Image",
           ["qwen", "qwen-image", "qwen image", "qwen image 2.0", "qwen-image 2.0",
            "qwen image 3.0", "qwen-image 3.0"]),
    "11": ("seedream", "IMG", "Seedream",
           ["seedream", "seedream 5", "seedream 5.0", "seedream 4.5"]),
    "12": ("wan-image", "IMG", "Wan Image",
           ["wan-image", "wan image", "wan-image-v2", "wan t2i",
            "wan text to image", "wan text-to-image", "wan image pro",
            "wan 2.7 image", "wan2.7 image", "wan 2.6 image", "wan2.6 image",
            "wan 2.7", "wan2.7", "wan-2.7", "wan 2.6", "wan2.6", "wan-2.6"]),
    "13": ("z-image", "IMG", "Z-Image", ["z-image", "z image", "zimage", "z-image turbo"]),
    "21": ("flux-3-video", "VID", "FLUX 3 Video",
           ["flux 3", "flux-3", "flux3", "flux 3 video", "flux-3-video"]),
    "22": ("gemini-omni", "VID", "Gemini Omni",
           ["gemini-omni", "gemini omni", "gemini-omni-flash", "gemini omni flash"]),
    "23": ("happyhorse", "VID", "HappyHorse", ["happyhorse", "happy horse", "happy-horse"]),
    "14": ("kling-video", "VID", "Kling Video", ["kling-video", "kling video"]),
    "15": ("ltx-2", "VID", "LTX",
           ["ltx", "ltx-2", "ltx 2", "ltx-2.3", "ltx 2.3", "ltx-2.5", "ltx 2.5",
            "ltxv", "lightricks"]),
    "16": ("minimax-h3", "VID", "MiniMax H3",
           ["minimax", "minimax h3", "minimax-h3", "h3", "hailuo"]),
    "17": ("seedance", "VID", "Seedance",
           ["seedance", "seedance 2", "seedance 2.0", "seedance 2.5"]),
    "18": ("wan-video", "VID", "Wan Video",
           ["wan-video", "wan video", "wan-video-v2", "wan video edit", "wan videoedit",
            "wan 3.0", "wan3.0", "wan-3.0", "wan 3", "wan3",
            "wan3.0-video", "wan 3.0 video",
            "wan 2.7", "wan2.7", "wan-2.7", "wan 2.6", "wan2.6", "wan-2.6",
            "wan 2.5", "wan2.5", "wan-2.5", "wan 2.2", "wan2.2", "wan-2.2",
            "wan 2.1", "wan2.1", "wan-2.1",
            "wan t2v", "wan i2v", "wan r2v", "wan s2v", "wan ti2v", "wan kf2v",
            "wan flf2v", "flf2v", "wan vace", "vace", "unianimate",
            "wan animate", "wan fun", "wan move", "wan dancer"]),
}

MANIFEST_UID = "24"
PHRASING_UID = "25"
ROUTER_UID = "1"
FORMAT_UID = "0"
SPECS_UID = "27"

# The spec table is not a guide. It has no prompt_scheme, so it stays out of
# CATALOG and out of the guide count, and it keys on the QUESTION rather than on
# a model name so it can load next to whichever guide is already in context.
# Bare "steps" is deliberately absent: it matches "step by step" far too often to
# be worth the tokens.
SPECS_KEYS = ["resolution", "native resolution", "recommended resolution",
              "what resolution", "which resolution", "inference steps",
              "sampling steps", "how many steps", "step count", "cfg", "cfg scale",
              "guidance scale", "sampler", "scheduler", "fps", "frame rate",
              "framerate", "model specs", "generation settings",
              "recommended settings", "vram"]

# Always-on output-format rule. It owns uid 0 so the wording is version-controlled
# here instead of living only inside the exported JSON. The language half is scoped
# deliberately: a blanket "prompts are English" would contradict z-image (in-image
# text is rendered in whatever script you type, never translated), minimax-h3 and
# ltx-2 (spoken lines carry their delivered language) and wan2.1-flf2v-14b (the
# owner recommends Chinese). Hence the three carve-outs and the yields-to-guide line.
FORMAT = """<prompt_generation_output>

Whenever writing image or video generation prompts wrap them in code blocks and present individual prompts separately.

The prompt inside the block is written in English, whatever language we are speaking. If the conversation is in Polish, the reply is Polish and the prompt is still English: the conversation language is yours, the prompt language is the model's. Narration, in-character dialogue and everything outside the block are unaffected.

Three things inside a prompt are not description, and they keep their own language:

- Literal text meant to appear in the image. The model draws the characters it is given and does not translate them, so words that should read as Polish are written in Polish inside the quotes.
- Spoken or sung lines. The delivered language is the content: keep the line itself in that language and leave the direction around it in English.
- A prompt for a model whose own guide prefers another language, the way wan2.1-flf2v-14b prefers Chinese.

Everything else in the block, subject, scene, camera, lighting and style, stays English. A loaded guide overrides this entry.

</prompt_generation_output>"""

# Always-on prompt-craft default. Deliberately a default and not a ban: the guides
# genuinely disagree about exclusions (gpt-image says plain negatives work as
# written, illustrious-noob treats the negative as half the prompt, wan-video ships
# a defect bank), so this yields to whichever guide is loaded.
PHRASING = """<promptgen_phrasing>

Write what should be true, not what should be absent. Text encoders tend to bind a named token regardless of the negation wrapped around it, so the negation is what gets dropped and "no clutter" becomes a reliable way to get clutter.

- Prefer the positive that displaces the problem. "Bare concrete walls" beats "no clutter", "hands at her sides" beats "no gesturing", "flat overcast light" beats "no harsh shadows".
- Where an exclusion is genuinely needed, keep it short, concrete, and grouped in one place rather than scattered through the prompt.
- This is a default, not a ban. Several models here do take real exclusions, and some expose a dedicated negative field or a canonical defect block. When a model's guide is loaded, its negatives section overrides this entry.

</promptgen_phrasing>"""

ROUTER = """<promptgen_model_index>

Prompting guides available here. Naming a model loads its full guide.

IMAGE: Anima, FLUX.2, Gemini Image (Nano Banana), GPT Image, Grok Imagine Image, HiDream-O1, HunyuanImage, Ideogram 4, Illustrious / NoobAI, Kling Image, Krea 2, Qwen-Image, Seedream, Wan Image, Z-Image
VIDEO: FLUX 3 Video, Gemini Omni, HappyHorse, Kling Video, LTX, MiniMax H3, Seedance, Wan Video

Several vendors ship more than one guide, so name the model and the modality:
- Alibaba has four. Qwen-Image and Wan Image are image; Wan Video and HappyHorse are video. Wan Video and HappyHorse are two separate video lines, not versions of each other, and they are prompted differently.
- Black Forest Labs has two: FLUX.2 for image, FLUX 3 Video for video. FLUX.2 conventions do not transfer to FLUX 3.
- Google has two: Gemini Image for image, Gemini Omni for video.
- Kuaishou has two: Kling Image and Kling Video.

Each guide is authoritative for its own model. These models are prompted in genuinely different ways, so never carry a convention from one model's guide to another: if the guide for the named model is not loaded, ask for it rather than guessing from a different model's rules.

Reference notation is the classic case, and it is NOT shared. Seedance writes @Image 1, HappyHorse writes [Image 1], Grok Imagine Image writes <IMAGE_0> and counts from ZERO, Gemini Omni uses its own angle-bracket tags, Wan uses one form for reference-to-video and a different one for video editing, and several models write Image 1 with no sigil at all. Two models reaching for angle brackets does not make them the same notation, and one of them starts at 0 while nearly everything else starts at 1. Vendor and modality predict nothing here. Take the form from the loaded guide, and do not assume a model numbers its inputs at all.

</promptgen_model_index>"""


def guide_text(scheme):
    return (GUIDES / f"{scheme}.md").read_text(encoding="utf-8")


def verified(scheme):
    m = re.search(r'^last_verified:\s*"?([\d-]+)"?', guide_text(scheme), re.M)
    return m.group(1) if m else "unknown"


def body(scheme):
    text = re.sub(r"\A---\n.*?\n---\n", "", guide_text(scheme), flags=re.DOTALL)
    text = text[text.index("# "):]
    cut = text.find("\n## Sources")
    if cut != -1:
        text = text[:cut]
    return text.strip()


def wrap(scheme):
    tag = "promptgen_" + re.sub(r"[-.]", "_", scheme)
    return f"<{tag}>\n\n{body(scheme)}\n\n</{tag}>"


def manifest_rows():
    rows = {"IMG": [], "VID": []}
    for scheme, modality, _, _ in CATALOG.values():
        rows[modality].append(f"{scheme} {verified(scheme)}")
    return (f"IMAGE: {' | '.join(sorted(rows['IMG']))}\n"
            f"VIDEO: {' | '.join(sorted(rows['VID']))}")


def manifest(build, date, rows, specs_date):
    return (
        "<promptgen_manifest>\n\n"
        f"Prompting guide set v{build}, exported {date}, {len(CATALOG)} guides. "
        "Each date is when that guide was last verified against its sources.\n\n"
        f"{rows}\n\n"
        "This is the complete set. If asked about a model that is not listed, say its guide "
        "is not loaded and ask for it, rather than answering from a different model's rules.\n\n"
        f"A separate open-weights spec table (verified {specs_date}) carries native and "
        "recommended resolutions, step counts, CFG, samplers, frame rates and durations. It is "
        "not a guide and loads only on request. If asked for any of those and the table is not "
        "loaded, say so and ask for it rather than answering from memory.\n\n"
        "</promptgen_manifest>"
    )


def index_table(build, date, specs_date):
    rows = sorted(
        ((name, scheme, MODALITY[modality], verified(scheme))
         for scheme, modality, name, _ in CATALOG.values()),
        key=lambda r: (r[2], r[0].lower()),
    )
    lines = [
        "# Guide index",
        "",
        f"Set v{build}, exported {date}. Generated by `build-lorebook.py --publish`; edit that, not this.",
        "",
        "| Guide | File | Modality | Last verified |",
        "| --- | --- | --- | --- |",
    ]
    lines += [f"| {name} | [`{scheme}.md`]({scheme}.md) | {mod} | {dt} |"
              for name, scheme, mod, dt in rows]
    lines += [
        f"| Model specs (reference, not a guide) | [`model-specs.md`](model-specs.md) | open weights | {specs_date} |",
        "",
    ]
    return "\n".join(lines)


def publish(blob, build, date, specs_date):
    """Refresh the tracked copies: guide bodies into docs/, the lorebook into lorebook/.

    Only *.md is copied, because the vault also holds exported archives.
    """
    DOCS.mkdir(exist_ok=True)
    REPO_LOREBOOK.parent.mkdir(exist_ok=True)
    names = {p.name for p in GUIDES.glob("*.md")}
    for src in sorted(GUIDES.glob("*.md")):
        shutil.copyfile(src, DOCS / src.name)
    stale = sorted(p.name for p in DOCS.glob("*.md")
                   if p.name not in names and p.name != "INDEX.md")
    for name in stale:
        (DOCS / name).unlink()
    (DOCS / "INDEX.md").write_text(index_table(build, date, specs_date) + "\n", encoding="utf-8")
    REPO_LOREBOOK.write_text(blob, encoding="utf-8")
    return len(names), stale


book = json.loads(LOREBOOK.read_text(encoding="utf-8"))
entries = book["entries"]
guide_template = copy.deepcopy(entries["17"])
const_template = copy.deepcopy(entries[ROUTER_UID])

added, updated, rekeyed = [], [], []

for uid, (scheme, modality, name, keys) in CATALOG.items():
    content = wrap(scheme)
    if uid in entries:
        if entries[uid]["content"] != content:
            updated.append(name)
        if entries[uid]["key"] != keys:
            gained = [k for k in keys if k not in entries[uid]["key"]]
            lost = [k for k in entries[uid]["key"] if k not in keys]
            rekeyed.append(f"{name} (+{gained or 0} -{lost or 0})")
        entries[uid]["content"] = content
        entries[uid]["key"] = keys
    else:
        e = copy.deepcopy(guide_template)
        e.update({"uid": int(uid), "key": keys, "content": content,
                  "comment": f"[Promptgen][{modality}] {name}"})
        entries[uid] = e
        added.append(name)

if entries[FORMAT_UID]["content"] != FORMAT:
    entries[FORMAT_UID]["content"] = FORMAT
    updated.append("Output format")

if entries[ROUTER_UID]["content"] != ROUTER:
    entries[ROUTER_UID]["content"] = ROUTER
    updated.append("Model index")

# Sibling of the Output format entry: same system-at-depth-0 injection point,
# cloned from it so the placement fields cannot drift apart.
if PHRASING_UID in entries:
    if entries[PHRASING_UID]["content"] != PHRASING:
        entries[PHRASING_UID]["content"] = PHRASING
        updated.append("Prompt phrasing")
else:
    e = copy.deepcopy(entries[FORMAT_UID])
    e.update({"uid": int(PHRASING_UID), "key": [], "content": PHRASING, "order": 99,
              "comment": "[Promptgen] Prompt phrasing"})
    entries[PHRASING_UID] = e
    added.append("Prompt phrasing")

# The spec table reuses the guide entry template because it wants the same
# keyword-triggered placement, but it is keyed on the question rather than the
# model, so it can load alongside whichever guide is already in context.
specs_content = wrap("model-specs")
if SPECS_UID in entries:
    if entries[SPECS_UID]["content"] != specs_content:
        updated.append("Model specs")
    if entries[SPECS_UID]["key"] != SPECS_KEYS:
        rekeyed.append("Model specs")
    entries[SPECS_UID]["content"] = specs_content
    entries[SPECS_UID]["key"] = SPECS_KEYS
else:
    e = copy.deepcopy(guide_template)
    e.update({"uid": int(SPECS_UID), "key": SPECS_KEYS, "content": specs_content,
              "comment": "[Promptgen][REF] Open-weights model specs"})
    entries[SPECS_UID] = e
    added.append("Model specs")

# Advance the build number when guide content, routing, keys, or any guide's
# verification date moved. Dates live in frontmatter, which is stripped from the
# entry bodies, so they have to be checked separately or a re-verification pass
# would ship silently under the old build number.
prior = entries.get(MANIFEST_UID, {}).get("content", "")
m = re.search(r"guide set v(\d+)", prior, re.I)
build = int(m.group(1)) if m else 0

rows = manifest_rows()
specs_date = verified("model-specs")
if prior and (rows not in prior or f"verified {specs_date}" not in prior):
    updated.append("verification dates")
if added or updated or rekeyed or not prior:
    build += 1

date = max([verified(s) for s, _, _, _ in CATALOG.values()] + [specs_date])
content = manifest(build, date, rows, specs_date)

if MANIFEST_UID in entries:
    entries[MANIFEST_UID]["content"] = content
else:
    e = copy.deepcopy(const_template)
    e.update({"uid": int(MANIFEST_UID), "key": [], "content": content, "order": 98,
              "comment": f"[Meta] Version - v{build} | {date} | {len(CATALOG)} guides"})
    entries[MANIFEST_UID] = e
    added.append("Version manifest")
entries[MANIFEST_UID]["comment"] = f"[Meta] Version - v{build} | {date} | {len(CATALOG)} guides"

# Reflow display order. The version entry sits first so opening the world in ST
# answers "which build is this?" without scrolling or opening anything.
order = [MANIFEST_UID, FORMAT_UID, PHRASING_UID, ROUTER_UID, SPECS_UID]
order += sorted((u for u in CATALOG if CATALOG[u][1] == "IMG"), key=lambda u: CATALOG[u][2].lower())
order += sorted((u for u in CATALOG if CATALOG[u][1] == "VID"), key=lambda u: CATALOG[u][2].lower())
order += [u for u in entries if u not in order]
for i, uid in enumerate(order):
    entries[uid]["displayIndex"] = i

dated = ARCHIVE / f"{LOREBOOK.stem} v{build} {date}.json"
blob = json.dumps(book, ensure_ascii=False, separators=(",", ":"))

print(f"build v{build}  date {date}  entries {len(entries)}  guides {len(CATALOG)}")
print(f"added:   {added or 'none'}")
print(f"updated: {updated or 'none'}")
print(f"rekeyed: {rekeyed or 'none'}")

write = "--write" in sys.argv
do_publish = "--publish" in sys.argv

if not write and not do_publish:
    print(f"\nDRY RUN. would write:\n  {LOREBOOK}\n  {dated}")
    print(f"  --publish would also refresh {DOCS}/ and {REPO_LOREBOOK}")
    sys.exit(0)

if write:
    ARCHIVE.mkdir(exist_ok=True)
    LOREBOOK.write_text(blob, encoding="utf-8")
    dated.write_text(blob, encoding="utf-8")
    print(f"\nimport into ST: {LOREBOOK}")
    print(f"archived copy:  {dated}")

if do_publish:
    count, stale = publish(blob, build, date, specs_date)
    print(f"\npublished:      {count} guides + INDEX.md -> {DOCS}")
    print(f"                {REPO_LOREBOOK}")
    if stale:
        print(f"removed stale:  {', '.join(stale)}")
