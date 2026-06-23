#!/usr/bin/env python3
"""Enrichment batch 392: hand-curated claims for 3 federal candidates.

Targets active/recent U.S. federal candidates from bottom-of-alphabet states
(KY, IA) with 0 claims. Primary archetype_curated bucket is fully exhausted;
these candidates carry evidence_federal / archetype_party_default confidence
with verified public positions.

Candidates:
  - Pamela Stevenson (KY-D, 2026 Senate primary candidate; lost May 19 primary)
  - Christopher Campbell (KY-I, 2026 Senate general election independent)
  - Clint Twedt-Ball (IA-D, 2026 federal candidate)

Collision-avoidance: this agent takes bottom of alphabet (KY, IA).
Top-of-alphabet loop handles AK, AL, AR, etc.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---- Pamela Stevenson (KY-D, U.S. Senate primary candidate; lost May 19, 2026) ----
    ("pamela-stevenson", "KY", "Senate", [
        claim("ps1", "pamela-stevenson", "sanctity_of_life", 0, False,
              "Pro-choice Kentucky state legislator who ran for U.S. Senate pledging to protect abortion access. "
              "Endorsed by Reproductive Freedom for All (the NARAL successor organization); stated 'Women are able "
              "to make their own decisions about their healthcare' and 'The government has no business being in a "
              "doctor's room with a patient' — rejecting any fetal personhood or life-at-conception standard.",
              ["https://en.wikipedia.org/wiki/Pamela_Stevenson",
               "https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-in-kentucky-and-mississippi-attorney-general-races/"]),
        claim("ps2", "pamela-stevenson", "biblical_marriage", 2, False,
              "Gave a nationally viral March 2023 floor speech opposing Kentucky HB 470, which banned "
              "gender-affirming care for transgender youth and restricted classroom instruction on sexual "
              "orientation and gender identity. Declared: 'How dare you use my God for things against his "
              "people?' and led the chamber in a 'Me, free to be me' chant — directly opposing the rubric's "
              "rejection of transgender ideology in law and policy.",
              ["https://en.wikipedia.org/wiki/Pamela_Stevenson",
               "https://www.blackenterprise.com/rep-pamela-stevenson-gives-passionate-viral-speech-to-kentucky-leaders-against-anti-trans-bill/",
               "https://kentuckylantern.com/2023/03/16/kentucky-legislature-passes-anti-trans-bill/"]),
        claim("ps3", "pamela-stevenson", "border_immigration", 1, False,
              "At the March 17, 2026 Kentucky Democratic Senate primary debate, explicitly called for "
              "abolishing ICE: 'I'm for abolishing ICE because it's so broken that you can't return to sanity,' "
              "characterizing ICE agents as 'killing people at will' — the opposite of the rubric's mandatory "
              "deportation and border-enforcement standard.",
              ["https://www.lpm.org/news/2026-03-17/democratic-candidates-in-kentucky-senate-race-debate-ice-israel-and-affordability",
               "https://linknky.com/elections/2026/03/20/kentucky-democrats-senate-debate-2026-mcgrath-booker-romans-stevenson/"]),
    ]),

    # ---- Christopher Campbell (KY Independent, U.S. Senate general candidate) ----
    ("christopher-campbell-ky-senate", "KY", "Senator", [
        claim("cc1", "christopher-campbell-ky-senate", "foreign_policy_restraint", 1, True,
              "Campaign platform calls for an 'immediate moratorium on all military aid to foreign governments' "
              "and consolidation of the hundreds of globally deployed U.S.-funded military bases — aligning "
              "directly with the rubric's call to end forever wars and foreign military entanglements.",
              ["https://candidates.goodparty.org/campbell4congress2026",
               "https://linknky.com/press-releases/2025/11/05/press-release-campbell-declares-intent-to-run-for-senate/"]),
        claim("cc2", "christopher-campbell-ky-senate", "industry_capture", 4, True,
              "Running on an explicit 'Anti-Corruption, Anti-War, Pro-Kentucky' platform that targets 'waste, "
              "fraud, and abuse of the Military-Industrial Complex' and calls for a major reduction in "
              "defense-contractor spending — consistent with the rubric's call for Pentagon/defense-contractor "
              "audits.",
              ["https://candidates.goodparty.org/campbell4congress2026",
               "https://linknky.com/press-releases/2025/11/05/press-release-campbell-declares-intent-to-run-for-senate/",
               "https://www.forwardky.com/new-political-party-puts-forward-candidate-for-u-s-senate-seat/"]),
    ]),

    # ---- Clint Twedt-Ball (IA-D, 2026 federal candidate) ----
    ("clint-twedt-ball", "IA", "Senator", [
        claim("ctb1", "clint-twedt-ball", "sanctity_of_life", 0, False,
              "Spoke in support of 'removing restrictions on access to abortion' at the Iowa 2nd District "
              "Democratic primary debate (May 2026) — rejecting any recognition of fetal personhood or "
              "restriction on abortion access.",
              ["https://iowacapitaldispatch.com/2026/05/13/iowa-2nd-district-democratic-candidates-debate-healthcare-immigration/",
               "https://ballotpedia.org/Clint_Twedt-Ball"]),
        claim("ctb2", "clint-twedt-ball", "self_defense", 1, False,
              "Supports 'expanded background checks and red flag laws' for firearms — endorsing precisely the "
              "gun-control mechanisms (red-flag confiscation orders, universal background checks) that the "
              "rubric opposes as infringements on the right to keep and bear arms.",
              ["https://ballotpedia.org/Clint_Twedt-Ball",
               "https://www.clintforiowa.com/issues/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
    """
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
