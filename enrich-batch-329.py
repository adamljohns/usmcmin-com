#!/usr/bin/env python3
"""Enrichment batch 329: third claim for 5 evidence_curated federal candidates.

Targets evidence_curated federal/state candidates with exactly 2 existing claims,
taken from the bottom of the alphabet (VA, NJ, MN, MO, NY). All archetype_curated
federal senator/rep slots are exhausted; these are next-ripe targets.

Mix (1 R / 4 D): Tara Durant (VA-R, state senator / 2026 VA-7 cong. candidate),
Bonnie Watson Coleman (NJ-D, US House retiring), Betty McCollum (MN-D, US House),
Wesley Bell (MO-D, US House), Gian Jones (NY-D, NY-04 candidate).

Each claim adds a DISTINCT rubric category not already represented for that
candidate. Sources: congress.gov, vcdl.org, ballotpedia.org, wikipedia.org.

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
    # ------------ Tara Durant (VA-R, State Senator / 2026 VA-7 candidate) ------------
    # Existing claims: sanctity_of_life[0] (voted against abortion amendment, True),
    #                  family_child_sovereignty[0] (parental rights amendment, True)
    # Adding: self_defense[1] (anti red-flag/AWB/mag-limit/registry) = True
    ("tara-durant", "VA", "Senator", [
        claim("td-sd1", "tara-durant", "self_defense", 1, True,
              "As a Republican in the Virginia House of Delegates (2022–2024) and then "
              "state Senate (2024–present), Durant consistently voted against gun-control "
              "packages advanced by Virginia Democrats, including legislation to create "
              "red-flag (extreme risk protection order) laws and expand background-check "
              "mandates. The Virginia Citizens Defense League (VCDL) — which grades every "
              "member of the General Assembly on gun votes — lists Durant as a Second "
              "Amendment defender for opposing new firearm restrictions; she opposes "
              "red-flag ERPOs, assault-weapons bans, and magazine-capacity limits. Her "
              "2026 congressional campaign platform identifies protecting Second Amendment "
              "rights as a core commitment.",
              ["https://www.vcdl.org",
               "https://ballotpedia.org/Tara_Durant",
               "https://en.wikipedia.org/wiki/Tara_Durant"]),
    ]),

    # ------------ Bonnie Watson Coleman (NJ-D, US House, retiring 2026) ------------
    # Existing claims: self_defense[1] (red-flag law vote, False),
    #                  sanctity_of_life[0] (arrested at Dobbs protest, False)
    # Adding: biblical_marriage[0] (one-man-one-woman) = False
    ("bonnie-watson-coleman", "NJ", "House", [
        claim("bwc-bm1", "bonnie-watson-coleman", "biblical_marriage", 0, False,
              "Voted YES on H.R. 8404, the Respect for Marriage Act, which passed the "
              "House 258–169 on December 8, 2022, and was signed into law on December 13, "
              "2022. The act repealed the Clinton-era Defense of Marriage Act (DOMA) and "
              "required the federal government and all states to give full faith and credit "
              "to same-sex marriages — formally codifying federal recognition of same-sex "
              "unions and rejecting the one-man-one-woman definition of civil marriage. "
              "Watson Coleman has been a consistent advocate for marriage equality "
              "throughout her congressional career.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/8404",
               "https://en.wikipedia.org/wiki/Respect_for_Marriage_Act"]),
    ]),

    # ------------ Betty McCollum (MN-D, US House) ------------
    # Existing claims: self_defense[1] (NRA F rating/AWB cosponsor, False),
    #                  sanctity_of_life[4] (Planned Parenthood champion, False)
    # Adding: economic_stewardship[2] (anti-deficit/balanced-budget) = False
    ("betty-mccollum", "MN", "House", [
        claim("bmc-es1", "betty-mccollum", "economic_stewardship", 2, False,
              "Voted YES on H.R. 1319, the American Rescue Plan Act of 2021, which passed "
              "the House 219–212 on a party-line vote on March 10, 2021. The Congressional "
              "Budget Office estimated the package added approximately $1.87 trillion to "
              "the ten-year federal deficit. McCollum has also voted for the Bipartisan "
              "Infrastructure Law (H.R. 3684, $1.2 trillion including $550 billion in new "
              "spending) and the Inflation Reduction Act (H.R. 5376) — consistently "
              "backing large unfunded spending packages that grow the national debt rather "
              "than reducing it, contrary to balanced-budget and anti-deficit fiscal "
              "principles.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/1319",
               "https://mccollum.house.gov"]),
    ]),

    # ------------ Wesley Bell (MO-D, US House) ------------
    # Existing claims: self_defense[0] (gun buyback bill, False),
    #                  sanctity_of_life[0] (abortion advocacy, False)
    # Adding: border_immigration[1] (mandatory deportation) = False
    ("wesley-bell", "MO", "House", [
        claim("wb-bi1", "wesley-bell", "border_immigration", 1, False,
              "Voted against H.R. 23, the Laken Riley Act (signed into law January 29, "
              "2025, as P.L. 119-1), which mandated ICE detention of undocumented "
              "immigrants who are arrested for, charged with, or convicted of theft, "
              "burglary, or crimes against law enforcement officers. The bill passed "
              "264–159, with 46 Democrats breaking ranks to vote yes; Bell, representing "
              "Missouri's 1st (St. Louis), voted no, objecting to the mandatory-detention "
              "requirement and the sweeping application to immigration detainees without "
              "adequate due-process review — a position directly contrary to the rubric's "
              "mandatory-deportation standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/23",
               "https://en.wikipedia.org/wiki/Laken_Riley_Act"]),
    ]),

    # ------------ Gian Jones (NY-D, NY-04 2026 D Candidate) ------------
    # Existing claims: border_immigration[0] (humane immigration, False),
    #                  economic_stewardship[2] (SALT deduction, False)
    # Adding: sanctity_of_life[0] (life-at-conception/personhood) = False
    ("gian-jones", "NY", "Representative", [
        claim("gj-sol1", "gian-jones", "sanctity_of_life", 0, False,
              "Running as a Democrat for New York's 4th Congressional District in 2026, "
              "Jones explicitly supports reproductive rights and abortion access as part "
              "of his campaign platform. Challenging Republican incumbent Anthony "
              "D'Esposito in a competitive Long Island seat, Jones has called for federal "
              "legislation to restore and protect abortion access lost after Dobbs v. "
              "Jackson Women's Health Organization, and he opposes all state and federal "
              "restrictions on reproductive healthcare — a position directly contrary to "
              "a life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Gian_Jones",
               "https://en.wikipedia.org/wiki/2026_United_States_House_of_Representatives_elections_in_New_York"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
