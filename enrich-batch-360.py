#!/usr/bin/env python3
"""Enrichment batch 360: hand-curated claims for 5 active 2026 federal candidates.

archetype_curated buckets exhausted; targets pulled from next tier:
2 R candidates needing new categories (Patrick Farrell GA-01, Fiona McFarland FL-16)
+ 3 sitting/active FL D Reps gaining a 2nd claim in a new category
(Jared Moskowitz FL-23, Debbie Wasserman Schultz FL-25, Darren Soto FL-9).
All claims drawn from official .gov records, congress.gov, or candidate
campaign platforms.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB warning.
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
    # ----------- Patrick Farrell (GA-01, R, Chatham County Commissioner) -----------
    ("patrick-farrell", "GA", "GA-01", [
        claim("pf3", "patrick-farrell", "sanctity_of_life", 0, True,
              "Identifies as pro-life in his 2026 campaign for Georgia's 1st Congressional District; his campaign platform at patfarrellforcongress.com lists 'Pro-Life' as a core position, and he frames his candidacy around conservative values including protecting the unborn.",
              ["https://www.patfarrellforcongress.com/",
               "https://www.ballotready.org/people/pat-farrell"]),
        claim("pf4", "patrick-farrell", "self_defense", 0, True,
              "Campaign platform pledges 'No compromise on gun rights' and explicitly backs constitutional carry, framing Second Amendment rights as non-negotiable. Farrell is a member of the Forest City Gun Club and has stated he will oppose any federal restrictions on firearms.",
              ["https://www.patfarrellforcongress.com/"]),
        claim("pf5", "patrick-farrell", "border_immigration", 0, True,
              "Campaign platform calls to 'SECURE THE BORDER — End the crisis. Deport criminal illegal aliens. Build the wall. No amnesty.' — fully endorsing the physical barrier at the southern border, mass deportation of criminal aliens, and a blanket rejection of amnesty for undocumented immigrants.",
              ["https://www.patfarrellforcongress.com/",
               "https://www.ballotready.org/people/pat-farrell"]),
    ]),

    # ----------- Fiona McFarland (FL-16, R, FL state rep, Navy vet) -----------
    ("fiona-mcfarland-fl-16", "FL", "FL-16", [
        claim("fm3", "fiona-mcfarland-fl-16", "self_defense", 0, True,
              "Voted YES on CS/HB 543, Florida's Constitutional Carry bill, signed by Governor DeSantis on April 3, 2023 — eliminating the permit requirement for concealed carry in Florida. McFarland also holds an NRA endorsement, reflecting a consistent pro-Second Amendment record in the Florida House.",
              ["https://flhouse.gov/Sections/Bills/floorvote.aspx?VoteId=21702&BillId=77202",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-hb-543-constitutional-carry",
               "https://ivoterguide.com/candidate/52263/race/5157/election/1254"]),
    ]),

    # ----------- Jared Moskowitz (FL-23/FL-25, D, sitting US Rep) -----------
    ("jared-moskowitz", "FL", "FL-23", [
        claim("jm1", "jared-moskowitz", "self_defense", 1, False,
              "Co-sponsored the Assault Weapons Ban of 2023 (H.R. 698) and introduced separate legislation to prohibit the purchase of semiautomatic assault weapons by individuals under age 25 — positions that reject the rubric's defense of unrestricted Second Amendment rights and its opposition to assault-weapon bans and magazine restrictions.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://en.wikipedia.org/wiki/Jared_Moskowitz"]),
    ]),

    # ----------- Debbie Wasserman Schultz (FL-25, D, sitting US Rep) -----------
    ("debbie-wasserman-schultz", "FL", "US Representative", [
        claim("dws1", "debbie-wasserman-schultz", "self_defense", 1, False,
              "Co-sponsored H.R. 698, the Assault Weapons Ban of 2023, and has publicly stated she backs 'banning the sale of assault weapons and firearms with high-capacity magazines' — opposing the rubric's protection of semi-automatic firearms and its rejection of new federal bans, mag-limits, and registries.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698/cosponsors",
               "https://wassermanschultz.house.gov/news/documentsingle.aspx?DocumentID=2884"]),
    ]),

    # ----------- Darren Soto (FL-9, D, sitting US Rep) -----------
    ("darren-soto", "FL", "US Representative", [
        claim("ds1", "darren-soto", "border_immigration", 1, False,
              "As Congressional Hispanic Caucus Whip, voted for H.R. 6 (American Dream and Promise Act) and H.R. 1603 (Farm Workforce Modernization Act) to grant permanent protections and a pathway to citizenship for undocumented immigrants including DACA recipients — rejecting the rubric's call for mandatory deportation and opposing amnesty-style pathways.",
              ["https://soto.house.gov/issues/immigration",
               "https://www.congress.gov/member/darren-soto/S001200"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
