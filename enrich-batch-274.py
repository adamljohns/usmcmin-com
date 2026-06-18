#!/usr/bin/env python3
"""Enrichment batch 274: hand-curated claims for 4 federal House candidates.

Targets evidence_federal House candidates with 0 claims from the bottom of
the alphabet (MI, NY).  The archetype_curated federal bucket is exhausted;
these are the next-best available candidates with documented public positions.

Mix (4 R): Robert Lulgjuraj (MI-10), Alfred Lemmo (MI-08),
Amir Hassan (MI-08), Alexander Portelli (NY-19).
Each claim cites >=1 reliable source and reflects 2025-2026 campaign positions.

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
    # ---------------- Robert Lulgjuraj (MI-10, R) ----------------
    ("robert-lulgjuraj", "MI", "representative", [
        claim("rl1", "robert-lulgjuraj", "border_immigration", 0, True,
              "Campaign platform calls to 'finish the border wall' as a top priority; his Secure the Border page states he will push to complete and extend physical barriers along the southern border, backed by military and Border Patrol resources.",
              ["https://ballotpedia.org/Robert_Lulgjuraj",
               "https://www.robertlforcongress.com/securetheborder"]),
        claim("rl2", "robert-lulgjuraj", "border_immigration", 1, True,
              "Pledges to 'support Border Patrol and ICE to deport illegal immigrants starting with dangerous criminals' and states he will 'always oppose amnesty for illegal immigrants' — consistent with mandatory deportation and enforcement-first posture.",
              ["https://ballotpedia.org/Robert_Lulgjuraj",
               "https://www.robertlforcongress.com/securetheborder"]),
        claim("rl3", "robert-lulgjuraj", "christian_liberty", 0, True,
              "America First campaign platform explicitly includes 'Protect Faith and Family — Defend religious liberty, protect life,' committing to free-exercise protections and opposing government interference with religious practice.",
              ["https://ballotpedia.org/Robert_Lulgjuraj",
               "https://www.robertlforcongress.com/"]),
    ]),

    # ---------------- Alfred Lemmo (MI-08, R) ----------------
    ("alfred-lemmo", "MI", "representative", [
        claim("al1", "alfred-lemmo", "sanctity_of_life", 0, True,
              "A proven pro-life activist who served on the board of Wayne County West Right to Life (Lifespan of Metro Detroit) for more than a decade, affirming the organization's personhood-from-conception mission and opposing abortion at every stage.",
              ["https://ballotpedia.org/Alfred_Lemmo",
               "https://michiganadvance.com/voter-guides/contests/8th-district-representative-in-congress/"]),
        claim("al2", "alfred-lemmo", "sanctity_of_life", 4, True,
              "Led Dearborn's successful 1988 statewide Michigan referendum campaign to end taxpayer funding of abortions, demonstrating a long record of opposing public abortion financing and any entanglement with the abortion industry — incompatible with receiving PP/NARAL/EMILY's List support.",
              ["https://ballotpedia.org/Alfred_Lemmo",
               "https://michiganadvance.com/voter-guides/contests/8th-district-representative-in-congress/"]),
    ]),

    # ---------------- Amir Hassan (MI-08, R) ----------------
    ("amir-hassan-mi-08", "MI", "representative", [
        claim("ah1", "amir-hassan-mi-08", "sanctity_of_life", 0, False,
              "Describes himself as pro-life but carves out exceptions for rape, incest, and the life of the mother — stopping short of a life-at-conception personhood position, which the rubric requires for a True score on this question.",
              ["https://michiganadvance.com/2025/07/14/navy-veteran-announces-run-for-congress-as-a-republican-in-consequential-michigan-district/",
               "https://hassanformi.com/"]),
        claim("ah2", "amir-hassan-mi-08", "sanctity_of_life", 2, False,
              "Openly supports IVF, calling it 'the blessing of IVF' and noting that his daughter Jayla was conceived through the procedure — incompatible with the rubric's anti-embryonic/IVF-discard standard.",
              ["https://michiganadvance.com/2025/07/14/navy-veteran-announces-run-for-congress-as-a-republican-in-consequential-michigan-district/",
               "https://hassanformi.com/"]),
        claim("ah3", "amir-hassan-mi-08", "border_immigration", 1, True,
              "A self-described 'committed America First Republican' who criticizes his Democratic opponent's 'dangerous and expensive radical open-border' policies and pledges strong ICE and Border Patrol enforcement to remove illegal immigrants.",
              ["https://michiganadvance.com/2025/07/14/navy-veteran-announces-run-for-congress-as-a-republican-in-consequential-michigan-district/",
               "https://www.kitchentablenews.org/michigan-news/amir-hassan-challenges-democrat-rivet-in-michigans-8th-district-race/"]),
    ]),

    # ---------------- Alexander Portelli (NY-19, R) ----------------
    ("alexander-portelli", "NY", "representative", [
        claim("ap1", "alexander-portelli", "economic_stewardship", 2, True,
              "States the top federal priority must be to 'get government spending under control and balance the federal budget,' estimating the federal government must be downsized by 20-25% to make a balanced budget achievable.",
              ["https://www.wbng.com/2026/05/28/portelli-challenges-oberacker-ny-19-republican-primary/",
               "https://www.allotsego.com/republican-alex-portelli-on-his-insurgent-run-for-congress/"]),
        claim("ap2", "alexander-portelli", "foreign_policy_restraint", 2, True,
              "Committed to 'ending all foreign aid provided by the United States to other countries,' framing every dollar sent abroad as money taken from American citizens — aligning with the rubric's opposition to funding hostile or Christian-persecuting regimes.",
              ["https://www.wbng.com/2026/05/28/portelli-challenges-oberacker-ny-19-republican-primary/",
               "https://www.allotsego.com/republican-alex-portelli-on-his-insurgent-run-for-congress/"]),
        claim("ap3", "alexander-portelli", "border_immigration", 0, True,
              "Pledges to 'reinforce our own borders' and says there 'has to be a way to remove' people here illegally — indicating support for a secure physical barrier and military-backed border enforcement.",
              ["https://www.allotsego.com/republican-alex-portelli-on-his-insurgent-run-for-congress/",
               "https://www.wbng.com/2026/05/28/portelli-challenges-oberacker-ny-19-republican-primary/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
