#!/usr/bin/env python3
"""Enrichment batch 145: hand-curated claims for 5 sitting U.S. Representatives.

All 5 are from Colorado — taken from the bottom of the evidence_federal
0-claim bucket (reverse-alphabetical collision-avoidance; top-of-alphabet
agent handles AK/AL/AR).

Mix (1R / 4D): Jeff Crank (CO-05-R), Diana DeGette (CO-01-D),
Jason Crow (CO-06-D), Brittany Pettersen (CO-07-D), Joe Neguse (CO-02-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Jeff Crank (CO-05-R, US Representative) ----------------
    ("jeff-crank", "CO", "Representative", [
        claim("jc1", "jeff-crank", "sanctity_of_life", 0, True,
              "Self-described 'proud pro-life advocate' who affirms protection of unborn life; assumed office January 3, 2025, and has maintained a consistent pro-life posture in the 119th Congress.",
              ["https://en.wikipedia.org/wiki/Jeff_Crank",
               "https://www.govtrack.us/congress/members/jeff_crank/456983"]),
        claim("jc2", "jeff-crank", "economic_stewardship", 0, True,
              "Cosponsor of H.R.1919, the Anti-CBDC Surveillance State Act, which passed the House on July 17, 2025 — prohibiting the Federal Reserve from issuing a central bank digital currency directly to individuals and banning its use as a monetary-policy tool.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/votes/119-2025/h201"]),
        claim("jc3", "jeff-crank", "self_defense", 0, True,
              "Self-described 'lifelong Second Amendment supporter and gun owner'; in May 2026 introduced H.R.8680, the Armed Forces Carry Rights Protection Act, to protect service members' constitutional carry rights — reinforcing a constitutional-carry posture.",
              ["https://www.govtrack.us/congress/members/jeff_crank/456983",
               "https://www.congress.gov/member/jeff-crank/C001137"]),
    ]),

    # ---------------- Diana DeGette (CO-01-D, US Representative) ----------------
    ("diana-degette", "CO", "Representative", [
        claim("dd1", "diana-degette", "sanctity_of_life", 0, False,
              "Co-chair of the House Pro-Choice Caucus since 1997; in 2025 sponsored H.Res.1285 reaffirming mifepristone as 'safe and effective' and demanding equitable policy access to medication abortion — categorically rejecting any personhood-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Diana_DeGette",
               "https://www.congress.gov/member/diana-degette/D000197"]),
        claim("dd2", "diana-degette", "sanctity_of_life", 4, False,
              "Consistently endorsed by and received support from NARAL Pro-Choice America (now Reproductive Freedom for All) and Planned Parenthood throughout her nearly three-decade congressional career — firmly embedded in the abortion-industry political-funding network.",
              ["https://ballotpedia.org/Diana_DeGette",
               "https://en.wikipedia.org/wiki/Diana_DeGette"]),
        claim("dd3", "diana-degette", "self_defense", 1, False,
              "Cosponsor of H.R.1307, the Office of Gun Violence Prevention Act of 2025, creating a new federal bureau to drive anti-gun-violence policy; has supported assault-weapons restrictions, expanded background checks, and magazine-capacity limits throughout her tenure.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1307/cosponsors",
               "https://en.wikipedia.org/wiki/Diana_DeGette"]),
    ]),

    # ---------------- Jason Crow (CO-06-D, US Representative) ----------------
    ("jason-crow", "CO", "Representative", [
        claim("jcrow1", "jason-crow", "sanctity_of_life", 0, False,
              "Pro-choice; cosponsored the Women's Health Protection Act to codify a federal right to abortion and preempt state pro-life laws; opposes any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Jason_Crow",
               "https://ballotpedia.org/Jason_Crow"]),
        claim("jcrow2", "jason-crow", "border_immigration", 0, False,
              "Voted NO on H.R.1 (One Big Beautiful Bill Act, roll call #190, July 3, 2025), which included $46.5B for border-wall construction and deployed National Guard/military to the southern border — opposing the wall-and-military border-enforcement priority.",
              ["https://www.govtrack.us/congress/votes/119-2025/h190",
               "https://en.wikipedia.org/wiki/One_Big_Beautiful_Bill_Act"]),
    ]),

    # ---------------- Brittany Pettersen (CO-07-D, US Representative) ----------------
    ("brittany-pettersen", "CO", "Representative", [
        claim("bp1", "brittany-pettersen", "sanctity_of_life", 0, False,
              "Cosponsor of the Women's Health Protection Act of 2025 (H.R.12) to federalize abortion access and preempt any state law protecting unborn life; has supported abortion access throughout her time in Congress and the Colorado legislature.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/12",
               "https://en.wikipedia.org/wiki/Brittany_Pettersen"]),
        claim("bp2", "brittany-pettersen", "self_defense", 1, False,
              "As a Colorado state legislator, championed HB 19-1177 — Colorado's red-flag law allowing courts to confiscate firearms without a criminal conviction — and has continued supporting gun-control measures in Congress, opposing constitutional-carry protections.",
              ["https://en.wikipedia.org/wiki/Brittany_Pettersen",
               "https://ballotpedia.org/Brittany_Pettersen"]),
    ]),

    # ---------------- Joe Neguse (CO-02-D, US Representative) ----------------
    ("joe-neguse", "CO", "Representative", [
        claim("jn1", "joe-neguse", "sanctity_of_life", 4, False,
              "Endorsed by and received campaign support from NARAL Pro-Choice Colorado and Planned Parenthood Action Fund; holds a 100% rating from Reproductive Freedom for All — placing him squarely inside the abortion-funding political network the rubric disqualifies.",
              ["https://votesmart.org/candidate/evaluations/151075/joseph-neguse",
               "https://en.wikipedia.org/wiki/Joe_Neguse"]),
        claim("jn2", "joe-neguse", "border_immigration", 1, False,
              "Supports a pathway to citizenship for undocumented immigrants and the DREAM Act; voted NO on H.R.1 (Big Beautiful Bill, July 3, 2025) which included mandatory deportation-detention expansion ($45B) and E-Verify mandates — opposing enforcement-first immigration policy.",
              ["https://en.wikipedia.org/wiki/Joe_Neguse",
               "https://www.govtrack.us/congress/votes/119-2025/h190"]),
        claim("jn3", "joe-neguse", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022) to codify federal recognition of same-sex marriage and repeal DOMA — rejecting the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Joe_Neguse",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
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
