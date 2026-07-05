#!/usr/bin/env python3
"""merge-scorecard-local.py — turn local-extractor findings into a refine-records.py dossier.

The civic twin of merge-pastor-enrichments.js. Reads local-politician-extract.py output and
emits a dossier keyed by slug@STATE that refine-records.py applies — reusing the hardened
engine (slug@STATE disambiguation, tier validation, per-answer footnotes). Only VERIFIED
findings become scores; held items are dropped. Additive by default (reset_unspecified=False):
fills/updates the verbatim-verified cells and never wipes existing evidence.

Usage: merge-scorecard-local.py EXTRACT_OUT.json DOSSIER_OUT.json [--reset]
"""
import json, sys, time

CONF = {"federal": "evidence_federal", "state": "evidence_state", "local": "evidence_local"}


def main():
    src, out = sys.argv[1], sys.argv[2]
    reset = "--reset" in sys.argv
    data = json.load(open(src))
    today = time.strftime("%Y-%m-%d")
    records = {}
    for r in data.get("candidates", []):
        findings = r.get("findings") or []
        if not findings:
            continue
        st = (r.get("state") or "").upper()
        key = f"{r['slug']}@{st}" if st else r["slug"]
        evidence, srcs = {}, []
        for f in findings:
            cat, qi = f["category"], str(f["question_idx"])
            evidence.setdefault(cat, {})[qi] = {
                "v": bool(f["score_impact"]),
                "src": [f["source_url"]] if f.get("source_url") else [],
                "note": (f.get("claim_text") or f.get("quote") or "")[:400],
            }
            if f.get("source_url"):
                srcs.append(f["source_url"])
        records[key] = {
            "profile": {
                "confidence": CONF.get(r.get("level"), "evidence_state"),
                "confidence_note": f"Local-grind (Qwen finds + Gemma cross-check, verbatim-verified) {today}",
                "last_refined": today,
            },
            "evidence": evidence,
            "sources_add": sorted(set(srcs)),
            "notes_append": f"Local-grind evidence pass {today}: {len(findings)} verbatim-verified position(s).",
        }
    dossier = {
        "_meta": {"author": "local-grind", "date": today,
                  "note": "local-politician-extract findings (verbatim + Gemma cross-check)"},
        "reset_unspecified": reset,
        "records": records,
    }
    json.dump(dossier, open(out, "w"), indent=1)
    cats = sum(len(v["evidence"]) for v in records.values())
    cells = sum(len(qs) for v in records.values() for qs in v["evidence"].values())
    print(f"wrote {out}: {len(records)} candidate(s), {cats} categories, {cells} scored cells"
          + (" [RESET mode]" if reset else " [additive]"))


if __name__ == "__main__":
    main()
