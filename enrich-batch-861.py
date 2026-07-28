#!/usr/bin/env python3
"""Enrichment batch 861: +1 self_defense claim for 5 Wyoming House Republicans.

The archetype_curated federal pool is fully exhausted. This batch continues
the bottom-of-alphabet, 2-claim → 3-claim strategy for WY evidence_curated
state representatives.

All 5 targets voted Aye on HB0130 (2026), Wyoming's amendment to the Second
Amendment Protection Act, which passed the House 49–12 on February 21, 2026.
HB0130 would have prohibited state and local authorities from using personnel
or funds to enforce any federal law, order, or regulation that unconstitutionally
infringes on Second Amendment rights. Governor Gordon vetoed the bill on
March 11, 2026, but the floor votes document each rep's clear, on-record
commitment to refusing cooperation with unconstitutional federal firearms mandates.

Targets (all R, WY, 'State Representative'):
  Laurie Bratten   — adding self_defense[1]
  Landon Brown     — adding self_defense[1]
  Ken Clouston     — adding self_defense[1]
  Julie Jarvis     — adding self_defense[1]
  Joseph Webb      — adding self_defense[1]

Minified write preserved — see enrich-batch-4.py docstring.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, name_slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{name_slug}-{category}-{q_idx}-{cid}",
        "category": category,
        "question_idx": q_idx,
        "score_impact": score_impact,
        "kind": kind,
        "text": text,
        "sources": sources,
        "verified": True,
        "verified_date": TODAY,
        "disputed": False,
        "confidence": "high",
    }


_HB0130_TEXT = (
    "Voted Aye on HB0130 (2026), Wyoming's amendment to the Second Amendment "
    "Protection Act. The bill — which passed the Wyoming House 49–12 on "
    "February 21, 2026 — would have added civil-penalty enforcement mechanisms "
    "to prohibit state and local authorities from using personnel or funds to "
    "enforce any federal law, executive order, or regulation that "
    "unconstitutionally infringes on the Second Amendment rights of law-abiding "
    "citizens. Governor Gordon vetoed the bill on March 11, 2026, but the "
    "floor vote documents a clear, on-record commitment to refusing cooperation "
    "with unconstitutional federal firearms mandates."
)
_HB0130_SOURCES = [
    "https://www.wyoleg.gov/Legislation/2026/HB0130",
    "https://oilcity.news/wyoming/legislature/2026/03/11/governor-gordon-vetoes-second-amendment-protection-act/",
    "https://bearingarms.com/camedwards/2026/03/11/wyoming-governor-vetoes-second-amendment-protection-act-n1231830",
]

TARGETS = [
    # ---------------- Laurie Bratten (WY-R) ----------------
    ("laurie-bratten", "WY", "Representative", [
        claim("lb3", "laurie-bratten", "self_defense", 1, True,
              _HB0130_TEXT, _HB0130_SOURCES),
    ]),

    # ---------------- Landon Brown (WY-R) ----------------
    ("landon-brown", "WY", "Representative", [
        claim("lbr3", "landon-brown", "self_defense", 1, True,
              _HB0130_TEXT, _HB0130_SOURCES),
    ]),

    # ---------------- Ken Clouston (WY-R) ----------------
    ("ken-clouston", "WY", "Representative", [
        claim("kc3", "ken-clouston", "self_defense", 1, True,
              _HB0130_TEXT, _HB0130_SOURCES),
    ]),

    # ---------------- Julie Jarvis (WY-R) ----------------
    ("julie-jarvis", "WY", "Representative", [
        claim("jj3", "julie-jarvis", "self_defense", 1, True,
              _HB0130_TEXT, _HB0130_SOURCES),
    ]),

    # ---------------- Joseph Webb (WY-R) ----------------
    ("joseph-webb", "WY", "Representative", [
        claim("jw3", "joseph-webb", "self_defense", 1, True,
              _HB0130_TEXT, _HB0130_SOURCES),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        office = (c.get("office") or "")
        if office_keyword.lower() not in office.lower():
            continue
        return c
    return None


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, state, office_keyword, claims in TARGETS:
        m = find_candidate(scorecard, slug, state, office_keyword)
        if not m:
            print(f"  ✗ NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see enrich-batch-4.py docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
