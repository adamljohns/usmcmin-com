#!/usr/bin/env python3
"""Enrichment batch 275: evidence-curated R federal candidates with <3 claims,
reverse-alphabetical by state (WI → VA → MO → MI → IL).

Targets:
  Joe McGraw       (IL-17, R, 2 existing claims → +2)
  Douglas Ollivant (VA-07, R, 2 existing claims → +1)
  Alfred Lemmo     (MI-08, R, 2 existing claims → +1)
  Jim Ingram       (MO-06, R, 2 existing claims → +1)
  Casey Chlebek    (IL Senate, R, 0 existing claims → +3)

All claims cite >=1 reliable source; 2024-2026 positions/records only.

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
    # ---------------- Joe McGraw (IL-17, R) ----------------
    ("joe-mcgraw", "IL", "IL-17", [
        claim("jm3", "joe-mcgraw", "border_immigration", 0, True,
              "Made completing the southern border wall a central campaign promise in both his 2024 and 2026 runs for IL-17: called for 'a completed border wall' and expanded Border Patrol to end illegal crossings — a direct endorsement of the physical barrier and enforcement posture the rubric supports.",
              ["https://www.wsiu.org/state-of-illinois/2024-03-21/republican-joe-mcgraw-pushes-border-security-in-competitive-17th-congressional-district-race",
               "https://www.wglt.org/local-news/2024-03-21/republican-joe-mcgraw-pushes-border-security-in-competitive-17th-congressional-district-race"]),
        claim("jm4", "joe-mcgraw", "economic_stewardship", 2, True,
              "Stated that the 'best way to increase revenue is to lower taxes,' arguing that tax cuts paired with cutting waste and fraud are the route to federal deficit reduction — aligning with the rubric's preference for limited government and supply-side fiscal discipline over tax-and-spend approaches.",
              ["https://www.wglt.org/local-news/2024-10-31/in-contested-17th-district-democrat-eric-sorensen-and-gop-challenger-joe-mcgraw-have-different-approaches-to-federal-deficit",
               "https://www.wsiu.org/state-of-illinois/2024-10-31/mcgraw-sorensen-debate-federal-deficit-il-17"]),
    ]),

    # ---------------- Douglas Ollivant (VA-07, R) ----------------
    ("douglas-ollivant", "VA", "VA-07", [
        claim("do3", "douglas-ollivant", "foreign_policy_restraint", 1, False,
              "Career reflects sustained commitment to American military engagement abroad: served as NSC Director for Iraq under both Presidents Bush and Obama; is a Senior Fellow at the Foreign Policy Research Institute (FPRI); and founded Mantid International, a consulting firm with active offices in Baghdad and Beirut — squarely counter to the rubric's call to wind down foreign military entanglements.",
              ["https://en.wikipedia.org/wiki/Douglas_Ollivant",
               "https://www.fpri.org/contributor/douglas-a-ollivant/"]),
    ]),

    # ---------------- Alfred Lemmo (MI-08, R) ----------------
    ("alfred-lemmo", "MI", "MI-08", [
        claim("al3", "alfred-lemmo", "self_defense", 1, True,
              "Endorsed by Ted Nugent of the NRA, reflecting strong Second Amendment alignment; as a Catholic Republican engineer and longtime movement conservative who has run for Congress in Michigan, Lemmo supports the constitutional right to keep and bear arms — consistent with the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Alfred_Lemmo",
               "https://ivoterguide.com/candidate/51843/race/845/election/688"]),
    ]),

    # ---------------- Jim Ingram (MO-06, R) ----------------
    ("jim-ingram-mo-06", "MO", "MO-06", [
        claim("ji3", "jim-ingram-mo-06", "refuse_federal_overreach", 0, True,
              "In his 2025 Ballotpedia Candidate Connection survey, called for a Constitutional Convention to structurally restrain federal power, stating 'a career politician will not stand up and call for a Constitutional Convention because the political establishment will put up every road block possible' — advocating constitutional amendments for term limits, uniform election laws, and other limits on Washington's overreach.",
              ["https://ballotpedia.org/Jim_Ingram",
               "https://imforingram.com/the-candidate/"]),
    ]),

    # ---------------- Casey Chlebek (IL Senate, R) ----------------
    ("casey-chlebek", "IL", "Senator", [
        claim("cc1", "casey-chlebek", "foreign_policy_restraint", 1, True,
              "His MULA (Mavericks Under Liberty for America) foreign policy doctrine explicitly emphasizes 'avoiding needless interventions' and prioritizing American sovereignty over open-ended military commitments abroad — directly aligned with the rubric's call to end foreign military entanglements.",
              ["https://will.illinois.edu/21stshow/story/republican-u.s-senate-candidate-casey-chlebek",
               "https://caseyforsenate.com/"]),
        claim("cc2", "casey-chlebek", "sanctity_of_life", 4, True,
              "Explicitly opposes government funding for Planned Parenthood, affirming that no taxpayer money should flow to abortion providers — consistent with the rubric's rejection of using public funds to subsidize the abortion industry.",
              ["https://ivoterguide.com/candidate/48925/race/4665/election/890?culture=en-us",
               "https://will.illinois.edu/21stshow/story/republican-u.s-senate-candidate-casey-chlebek"]),
        claim("cc3", "casey-chlebek", "economic_stewardship", 2, True,
              "Proposes the MAGNA Agenda, including abolishing income taxes on retirement and Social Security income and restructuring the tax code to reduce the federal deficit without expanding spending — a limited-government fiscal posture aligned with the rubric's preference for sound money and fiscal restraint.",
              ["https://caseyforsenate.com/",
               "https://ivoterguide.com/candidate/48925/race/4665/election/890?culture=en-us"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
