#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = [
    "SKILL.md",
    "references/00-operating-principles.md",
    "references/01-studio-inventory.md",
    "references/02-capability-modes.md",
    "references/10-genre-router.md",
]


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9+#/.-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def hit(text: str, patterns) -> bool:
    return any(re.search(p, text) for p in patterns)


# Specific rules first. Up to two explicit genre DNAs may be loaded for hybrids.
GENRE_RULES = [
    ([r"\bmelodic dubstep\b", r"\bfuture dubstep\b", r"\bmelodic dub\b"], "references/genres/melodic-dubstep.md"),
    ([r"\bliquid (?:dnb|d b|drum(?: and)? bass)\b", r"\bliquid drum\b"], "references/genres/liquid-dnb.md"),
    ([r"\bminimal (?:dnb|d b|drum(?: and)? bass)\b", r"\bdeep (?:dnb|d b|drum(?: and)? bass)\b"], "references/genres/minimal-deep-dnb.md"),
    ([r"\bafro house\b", r"\bafro tech\b"], "references/genres/afro-house.md"),
    ([r"\btech house\b"], "references/genres/tech-house.md"),
    ([r"\bbass house\b"], "references/genres/bass-house.md"),
    ([r"\bmelodic house\b", r"\bmelodic techno\b"], "references/genres/melodic-house-techno.md"),
    ([r"\bdeep tech\b", r"\bminimal house\b", r"\bminimal tech\b"], "references/genres/minimal-deep-tech.md"),
    ([r"\btechno\b"], "references/genres/techno.md"),
    ([r"\bhouse\b"], "references/genres/house.md"),
]

TOPICS = [
    ([r"\bstutter\b", r"\bslic(?:e|ing)\b", r"\bsampl(?:e|er|ing)\b", r"\bsimpler\b", r"\bgranular\b", r"\bspectral\b", r"\bresampl\w*\b"], "references/33-sampling-stutter-engine.md"),
    ([r"\brobotic\b", r"\brobotique\b", r"\bvocoder\b", r"\bovox\b", r"\bvocal bender\b", r"\btune real[- ]time\b", r"\bvocal tuner\b", r"\btalking bass\b", r"\bformant\w*\b"], "references/34-robotic-bass-vocoder-vocal-engine.md"),
    ([r"\bdubstep\b", r"\bgrowl\w*\b", r"\bhypergrowl\b", r"\briddim\b"], "references/35-dubstep-bass-engine.md"),
    ([r"\bdrum(?: and)? bass\b", r"\bdnb\b", r"\bd b\b", r"\bjungle\b", r"\bcalibre\b", r"\balix perez\b", r"\bskeptical\b", r"\bjustin hawkes\b", r"\bkumarion\b", r"\breaper\b"], "references/36-dnb-engine.md"),
    ([r"\bsnare\b", r"\bkick design\b", r"\bdrum design\b", r"\btransient design\b", r"\brim ?shot\b", r"\belectronic percussion\b", r"\bglitch percussion\b"], "references/37-drum-transient-design.md"),
    ([r"\briser\b", r"\bimpact\b", r"\bdownlifter\b", r"\buplifter\b", r"\btransition fx\b", r"\batmospher\w*\b", r"\batmos\b", r"\bfx transition\b"], "references/38-fx-atmos-transitions.md"),
    ([r"\breverse (?:bass|cymba(?:l|le|n)|crash|reverb|vocal|kick|snare|impact|fx)\b", r"\b(?:bass|cymbale|reverb|vocal|kick|snare|impact) invers\w*\b", r"\bsuck-?back\b", r"\bpre[- ]fx\b"], "references/39-reverse-pre-fx-engine.md"),
    ([r"\bbreak\b", r"\bpont\b", r"\bdrop\b", r"\barrang\w*\b", r"\bbuild(?:up)?\b"], "references/20-arrangement-engine.md"),
    ([r"\bkick\b", r"\bbass\b", r"\bsub\b", r"\bsidechain\b", r"\bphase\b", r"\blow[- ]end\b"], "references/30-low-end-engine.md"),
    ([r"\bgroove\b", r"\bdrum\w*\b", r"\bperc(?:ussion)?s?\b", r"\bhat\b", r"\bshaker\b", r"\bconga\w*\b"], "references/31-groove-drums-engine.md"),
    ([r"\bserum\b", r"\bsound design\b", r"\bsynth\w*\b", r"\bwavetable\b", r"\bfm\b"], "references/32-sound-design-engine.md"),
    ([r"\bmix(?:ing|age)?\b", r"\beq\b", r"\bcompress\w*\b", r"\bsoothe\w*\b", r"\bstereo\b", r"\breverb\b", r"\bsatur\w*\b", r"\bclip(?:per|ping)?\b"], "references/40-mix-engine.md"),
    ([r"\bpan(?:ning|oram\w*)?\b", r"\bspatial\w*\b", r"\bstereo (?:width|field|image|placement)\b", r"\bchamp stereo\b", r"\bimage stereo\b", r"\bplacement stereo\b", r"\bsub mono\b", r"\bwidth\b", r"\bdepth\b", r"\bmid/side\b", r"\bm/s\b", r"\bcorrelation\b", r"\bmono compat\w*\b", r"\bbass mono\b"], "references/41-spatial-spectrum-stereo-engine.md"),
    ([r"\bmaster(?:ing)?\b", r"\blufs\b", r"\btrue peak\b", r"\bl4\b", r"\blimiter\b", r"\bbeatport\b", r"\bstream(?:ing)?\b"], "references/50-mastering-engine.md"),
    ([r"\bapc ?64\b", r"\bmaschine\b", r"\bmk3\b", r"\ba49\b", r"\bkomplete\b", r"\bnks\b", r"\bableton\b"], "references/60-ableton-hardware-workflow.md"),
    ([r"\blom\b", r"\blive object model\b", r"\bdeviceparameter\b", r"\bparameter mapping\b", r"\bautomation state\b", r"\bmacro mapping\b", r"\bableton bridge\b", r"\bai bridge\b", r"\bbridge ia\b"], "references/61-ableton-lom-bridge.md"),
    ([r"\breference\b", r"\breference track\b", r"\banalys\w*\b", r"\bproducer\b"], "references/70-reference-analysis-protocol.md"),
    ([r"\blabel[- ]ready\b", r"\brelease[- ]ready\b", r"\blivrable\b", r"\bpour label\b", r"\bexport\b", r"\bstems?\b", r"\bdeliver\w*\b", r"\bdither\b", r"\bsample licen[cs]\w*\b", r"\bsample provenance\b"], "references/65-label-ready-qc-export.md"),
    ([r"\bde a a z\b", r"\ba to z\b", r"\bfrom scratch\b", r"\bstart to finish\b", r"\btrack complete\b", r"\bmorceau complet\b", r"\bmorceau livrable\b", r"\bproduction complete\b", r"\bfinish(?:ing)? the track\b"], "references/03-end-to-end-production-lifecycle.md"),
    ([r"\bcpu\b", r"\blatency\b", r"\bfreeze\b", r"\bflatten\b", r"\bcommit\b", r"\bperformance mode\b"], "references/66-project-performance-freeze-resample.md"),
]

ADVANCED_REFS = {
    "references/33-sampling-stutter-engine.md",
    "references/34-robotic-bass-vocoder-vocal-engine.md",
    "references/35-dubstep-bass-engine.md",
    "references/36-dnb-engine.md",
    "references/37-drum-transient-design.md",
    "references/38-fx-atmos-transitions.md",
    "references/39-reverse-pre-fx-engine.md",
}


def select_refs(prompt: str, load_all: bool = False):
    if load_all:
        return sorted(str(p.relative_to(ROOT)) for p in (ROOT / "references").rglob("*.md"))

    low = norm(prompt)
    chosen = list(CORE)

    genre_matches = []
    for patterns, path in GENRE_RULES:
        if hit(low, patterns):
            genre_matches.append(path)

    # "minimal" alone is genre-like only with clear music context.
    if re.search(r"\bminimal\b", low) and hit(low, [r"\b(track|morceau|groove|bassline|house|tech|techno|dnb|drum|producer|mix|drop|break)\b"]):
        p = "references/genres/minimal-deep-tech.md"
        if p not in genre_matches and not re.search(r"\bminimal (?:dnb|d b|drum)", low):
            genre_matches.append(p)

    # Keep up to two explicit DNAs for hybrids; preserve specificity/order.
    for path in genre_matches[:2]:
        if path not in chosen:
            chosen.append(path)

    for patterns, path in TOPICS:
        if hit(low, patterns) and path not in chosen:
            chosen.append(path)

    # Bridge is ambiguous: without technical bridge cues, treat it as musical arrangement.
    if re.search(r"\bbridge\b", low) and not hit(low, [r"\blom\b", r"\bableton bridge\b", r"\bai bridge\b", r"\bbridge ia\b", r"\blive object model\b"]):
        path = "references/20-arrangement-engine.md"
        if path not in chosen:
            chosen.append(path)

    if ADVANCED_REFS.intersection(chosen) and "references/83-advanced-sound-design-video-notes.md" not in chosen:
        chosen.append("references/83-advanced-sound-design-video-notes.md")

    if "references/61-ableton-lom-bridge.md" in chosen:
        for extra in (
            "references/62-semantic-mapping-contract.md",
            "references/63-write-safety-and-automation.md",
            "references/64-plugin-profile-strategy.md",
        ):
            if extra not in chosen:
                chosen.append(extra)

    if "references/65-label-ready-qc-export.md" in chosen:
        for extra in (
            "references/66-project-performance-freeze-resample.md",
            "references/03-end-to-end-production-lifecycle.md",
            "references/41-spatial-spectrum-stereo-engine.md",
        ):
            if extra not in chosen:
                chosen.append(extra)

    if "references/03-end-to-end-production-lifecycle.md" in chosen:
        for extra in (
            "references/41-spatial-spectrum-stereo-engine.md",
            "references/65-label-ready-qc-export.md",
            "references/66-project-performance-freeze-resample.md",
        ):
            if extra not in chosen:
                chosen.append(extra)

    # v1.5.0 docs ride along with the references they complement.
    for trigger, extra in (
        ("references/61-ableton-lom-bridge.md", "docs/bridge-safety-and-semantics.md"),
        ("references/03-end-to-end-production-lifecycle.md", "docs/production-workflow.md"),
        ("references/60-ableton-hardware-workflow.md", "docs/user-setup-and-control-surfaces.md"),
    ):
        if trigger in chosen and extra not in chosen:
            chosen.append(extra)

    if "references/41-spatial-spectrum-stereo-engine.md" in chosen and "references/40-mix-engine.md" not in chosen:
        chosen.append("references/40-mix-engine.md")

    if "references/80-evidence-policy.md" not in chosen:
        chosen.append("references/80-evidence-policy.md")
    return chosen


def read_context(paths, max_chars: int | None = None):
    parts = []
    used = 0
    included = []
    for rel in paths:
        p = ROOT / rel
        if not p.exists():
            continue
        block = f"\n\n===== {rel} =====\n{p.read_text(encoding='utf-8')}"
        if max_chars and used + len(block) > max_chars and rel not in CORE:
            continue
        parts.append(block)
        included.append(rel)
        used += len(block)
    return "".join(parts), included


def main():
    ap = argparse.ArgumentParser(description="Run the Electronic Production Engineer skill through local Ollama.")
    ap.add_argument("prompt", nargs="+")
    ap.add_argument("--model", default=os.environ.get("OLLAMA_MODEL", "qwen3:8b"))
    ap.add_argument("--all", action="store_true", help="Load all reference files (uses more context).")
    ap.add_argument("--host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    ap.add_argument("--think", action="store_true", help="Request thinking mode on models that support it.")
    ap.add_argument("--show-refs", action="store_true", help="Print selected reference files before the answer.")
    ap.add_argument("--dry-run", action="store_true", help="Select references and exit without calling Ollama.")
    ap.add_argument("--max-context-chars", type=int, default=int(os.environ.get("EPE_MAX_CONTEXT_CHARS", "70000")))
    args = ap.parse_args()

    prompt = " ".join(args.prompt)
    refs = select_refs(prompt, args.all)
    context, included = read_context(refs, None if args.all else args.max_context_chars)

    if args.show_refs or args.dry_run:
        print(json.dumps({"selected_refs": refs, "included_refs": included, "context_chars": len(context)}, indent=2, ensure_ascii=False))
        if args.dry_run:
            return

    system = (
        "Follow the canonical Electronic Production Engineer skill below. "
        "Use only relevant sections; identify capability mode before claiming measurements or execution; "
        "distinguish measured facts from inference; prefer root-cause fixes over plugin stacking.\n" + context
    )

    payload = {
        "model": args.model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
    }
    if args.think:
        payload["think"] = True

    req = urllib.request.Request(
        args.host.rstrip("/") + "/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            data = json.load(r)
    except Exception as e:
        print(f"Ollama call failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(data.get("message", {}).get("content", ""))


if __name__ == "__main__":
    main()
