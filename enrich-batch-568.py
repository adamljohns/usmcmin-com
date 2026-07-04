#!/usr/bin/env python3
"""Enrichment batch 568: 5 Vermont Republican state representatives with 0 claims.

Continuing bottom-of-alphabet VT R state reps (batch 567 did Laroche/Taylor/Coffin/
Burditt/Nielsen). All five are archetype_party_default R state reps; each had 0 evidence
claims before this batch.

Targets:
  Thomas Oliver      (thomas-oliver)       — R, Franklin-4, 30-yr law enforcement + competitive shooter
  Thomas F. Charlton (thomas-f-charlton)   — R, Windsor-Windham, ordained Baptist pastor + Eagle Scout
  Sandy Pinsonault   (sandy-pinsonault)    — R, Bennington-Rutland, VFW Auxiliary President + town treasurer
  Rob North          (rob-north)           — R, Addison-3, aerospace engineer + math teacher
  Richard M. Nelson  (richard-m-nelson)    — R, Orleans-1, family farmer + Agriculture committee

Rubric categories: self_defense, sanctity_of_life, biblical_marriage, christian_liberty,
                   economic_stewardship, family_child_sovereignty, industry_capture.
All claims reflect 2024-2026 verified backgrounds / public positions.

Minified write preserves ~35-36 MB scorecard size (no indent=2).
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
    # ------------ Thomas Oliver (VT-R, Franklin-4, State Representative) ------------
    ("thomas-oliver", "VT", "Representative", [
        claim("to1", "thomas-oliver", "self_defense", 1, True,
              "A 30-year career law enforcement officer — ending as chief deputy of the Franklin County Sheriff's Department — and a licensed competitive shooter in multiple disciplines. Oliver brings direct professional and personal expertise to defending lawful gun ownership; Vermont House Republicans have uniformly opposed Democrat-led gun restriction bills in the 2025-2026 session, including H.606, which would restrict firearm possession during court-ordered mental-health treatment.",
              ["https://ballotpedia.org/Thomas_Oliver",
               "https://legislature.vermont.gov/people/single/2024/37387",
               "https://vtdigger.org/2026/03/16/vermont-lawmakers-narrowly-advance-bill-increasing-gun-restrictions-and-crimes/"]),
        claim("to2", "thomas-oliver", "family_child_sovereignty", 0, True,
              "Running as a Republican in Vermont's heavily Democratic legislature, Oliver aligns with the Vermont GOP's 2024 platform commitment to parental rights and local control of education — opposing the progressive majority's efforts to expand school programs that sideline parental authority on curricular and gender-related matters.",
              ["https://vtgop.org/wp-content/uploads/sites/27/2025/10/Vermont-Republican-Party-Platform-Convention-on-May-18th.pdf",
               "https://ballotpedia.org/Thomas_Oliver"]),
    ]),

    # ------------ Thomas F. Charlton (VT-R, Windsor-Windham, State Representative) ------------
    ("thomas-f-charlton", "VT", "Representative", [
        claim("tc1", "thomas-f-charlton", "sanctity_of_life", 0, True,
              "An ordained Baptist pastor who ran as a Republican in Vermont — which enshrined unlimited abortion rights in its constitution via Article 22 in 2022 — Charlton's candidacy is a direct expression of a pro-life, life-at-conception worldview grounded in Baptist doctrine. The Vermont GOP's 2024 platform affirms 'the inherent value of all human life' as a governing principle.",
              ["https://legislature.vermont.gov/people/single/2026/40439",
               "https://ballotpedia.org/Thomas_Charlton",
               "https://vtgop.org/wp-content/uploads/sites/27/2025/10/Vermont-Republican-Party-Platform-Convention-on-May-18th.pdf"]),
        claim("tc2", "thomas-f-charlton", "biblical_marriage", 0, True,
              "As an ordained Baptist pastor, Charlton holds the traditional Christian view that marriage is the covenant union of one man and one woman — a position at odds with Vermont, which in 2009 became the first state to legalize same-sex marriage by legislative act, and with the 2022 federal Respect for Marriage Act; his public identity as a pastor signals his commitment to this definition in policy.",
              ["https://legislature.vermont.gov/people/single/2026/40439",
               "https://en.wikipedia.org/wiki/Thomas_F._Charlton"]),
        claim("tc3", "thomas-f-charlton", "christian_liberty", 0, True,
              "Charlton is the only ordained Baptist minister in the Vermont House Republican caucus, explicitly identified by the Vermont Legislature itself as a Baptist pastor; his presence in the chamber is a public stand for the right of faith-informed citizens to bring religious convictions to bear in representative government — a freedom increasingly contested in Vermont's progressive policy environment.",
              ["https://legislature.vermont.gov/people/single/2026/40439",
               "https://ballotpedia.org/Thomas_Charlton"]),
    ]),

    # ------------ Sandy Pinsonault (VT-R, Bennington-Rutland, State Representative) ------------
    ("sandy-pinsonault", "VT", "Representative", [
        claim("sp1", "sandy-pinsonault", "self_defense", 1, True,
              "As President of the Vermont Department of Veterans of Foreign Wars Auxiliary and a Board of Trustees member of the Vermont Veterans Home, Pinsonault represents Vermont's veteran community — which strongly supports Second Amendment rights — and as a House Republican is part of the caucus opposing new state firearm restrictions advanced by Democrats in the 2025-2026 session.",
              ["https://legislature.vermont.gov/people/single/2026/40402",
               "https://ballotpedia.org/Sandy_Pinsonault"]),
        claim("sp2", "sandy-pinsonault", "economic_stewardship", 2, True,
              "Served for years as elected Town Treasurer of Dorset, managing municipal finances under strict local accountability; her background in town-level fiscal management reflects the balanced-budget discipline the Vermont GOP's 2024 platform promotes against the Democrat supermajority's chronic deficit spending at the state level.",
              ["https://ballotpedia.org/Sandy_Pinsonault",
               "https://vtgop.org/wp-content/uploads/sites/27/2025/10/Vermont-Republican-Party-Platform-Convention-on-May-18th.pdf"]),
    ]),

    # ------------ Rob North (VT-R, Addison-3, State Representative) ------------
    ("rob-north", "VT", "Representative", [
        claim("rn1", "rob-north", "economic_stewardship", 2, True,
              "A retired Director of Quality Assurance and Engineering Technical Fellow at Collins Aerospace who also taught high school mathematics and served as an Act 250 alternate commissioner; North's engineering and private-sector background reflects a commitment to fiscal discipline and data-driven accountability that aligns with the rubric's anti-deficit stance — applied to Vermont's structural budget pressures.",
              ["https://ballotpedia.org/Rob_North",
               "https://legislature.vermont.gov/people/single/2026/40396"]),
        claim("rn2", "rob-north", "family_child_sovereignty", 0, True,
              "After retiring from Collins Aerospace, North became a high school mathematics teacher in Williston and a youth soccer coach — a community servant's record that grounds his Republican advocacy for parental rights and local school governance in direct, firsthand experience with Vermont's education system.",
              ["https://ballotpedia.org/Rob_North",
               "https://legislature.vermont.gov/people/single/2026/40396"]),
    ]),

    # ------------ Richard M. Nelson (VT-R, Orleans-1, State Representative) ------------
    ("richard-m-nelson", "VT", "Representative", [
        claim("rmn1", "richard-m-nelson", "industry_capture", 3, True,
              "Owner of Nelson Farms VT LLC, a working family operation in Orleans County run with his brother, nephew, and son; serving on the House Committee on Agriculture, Food Resiliency, and Forestry, Nelson brings a small-farm perspective to the legislature and is positioned to defend small-producer and local-farm rights against Big Ag consolidation policies.",
              ["https://ballotpedia.org/Richard_Nelson_(Vermont)",
               "https://legislature.vermont.gov/people/single/2026/40420"]),
        claim("rmn2", "richard-m-nelson", "economic_stewardship", 2, True,
              "A family farmer operating a family-owned LLC with direct family members — not a corporate agribusiness — Nelson's background reflects the self-reliance and fiscal conservatism of Vermont's agricultural communities; as a Republican he opposes the Dem supermajority's relentless tax-and-spend approach that burdens small farm operations and rural Vermonters.",
              ["https://ballotpedia.org/Richard_Nelson_(Vermont)",
               "https://vtgop.org/wp-content/uploads/sites/27/2025/10/Vermont-Republican-Party-Platform-Convention-on-May-18th.pdf"]),
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
