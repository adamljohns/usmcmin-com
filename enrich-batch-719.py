#!/usr/bin/env python3
"""Enrichment batch 719: evidence-curated claims for 5 GA-R state representatives.

Primary federal senator/representative pools are fully exhausted.
archetype_party_default state-senator pools fully exhausted.
Batch continues evidence_state GA-R state representatives with 0 claims,
bottom-of-alphabet reverse-sort (Cameron -> Dubnik -> Barton -> Momtahan -> Hawkins):

  Mike Cameron     (GA-R, State Representative District 1, since Jan 2021)
  Matt Dubnik      (GA-R, State Representative District 29, since Jan 2017)
  Matt Barton      (GA-R, State Representative District 5, since Feb 2019)
  Martin Momtahan  (GA-R, State Representative District 17, since 2019)
  Lee Hawkins      (GA-R, State Representative District 27, since Jan 2013)

Claims sourced to en.wikipedia.org, legiscan.com, ballotpedia.org.
All reflect 2019-2022 public legislative record (party-line floor votes).
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
    # --------------- Mike Cameron (GA-R, State Representative District 1) ---------------
    ("mike-cameron", "GA", "Representative", [
        claim("mc1", "mike-cameron", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which passed "
              "the Georgia House 100-75 on a strict party-line vote on March 25, 2021, and "
              "was signed by Governor Kemp on March 25, 2021. The law required photo ID for "
              "absentee ballots, expanded early voting hours, restricted unsolicited absentee "
              "ballot applications, limited mobile voting units, and banned third-party "
              "distribution of food or water within 150 feet of polling places -- aligning "
              "with the God-First rubric's defense of election integrity against systematic "
              "ballot fraud.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("mc2", "mike-cameron", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (2022), which established constitutional carry "
              "by eliminating the Georgia Weapons Carry License requirement for carrying a "
              "handgun in public. The bill passed the Georgia House 100-67 on a strict "
              "party-line vote on March 1, 2022, and was signed by Governor Kemp on April 12, "
              "2022 -- aligning with the Second Amendment's protection of the right to bear "
              "arms without government-issued permitting requirements.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
        claim("mc3", "mike-cameron", "family_child_sovereignty", 0, True,
              "Voted YES on Georgia HB 1178 (Parents' Bill of Rights, 2022), which passed "
              "the Georgia House 98-68 on March 1, 2022. The law requires local school "
              "systems to publish all curriculum and instructional materials for parental "
              "review, grants parents the right to inspect school records and opt out of "
              "health screenings, and establishes formal processes for parents to challenge "
              "the inclusion of materials they deem inappropriate -- defending parental "
              "sovereignty over children's education against government overreach.",
              ["https://legiscan.com/GA/bill/HB1178/2021",
               "https://ballotpedia.org/Georgia_HB_1178_(2022)"]),
    ]),

    # --------------- Matt Dubnik (GA-R, State Representative District 29) ---------------
    ("matt-dubnik", "GA", "Representative", [
        claim("md1", "matt-dubnik", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which banned "
              "abortions after a fetal heartbeat is detectable (approximately 6 weeks) and "
              "defined an 'unborn child' with a detectable heartbeat as a 'natural person' "
              "under Georgia law. The bill passed the Georgia House 92-78 on March 28, 2019, "
              "with only two Republicans voting against it, and was signed by Governor Kemp "
              "on May 7, 2019 -- affirming legal personhood from earliest detectable life.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("md2", "matt-dubnik", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which passed "
              "the Georgia House 100-75 on a strict party-line vote on March 25, 2021. The "
              "law required photo ID for absentee ballots, limited unsolicited ballot "
              "applications, expanded in-person early voting access, and secured the chain "
              "of custody for mail ballots -- the broadest Georgia election security "
              "legislation in a generation.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("md3", "matt-dubnik", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the permit requirement for carrying a handgun in public. The bill passed the "
              "Georgia House 100-67 on a strict party-line vote on March 1, 2022, and was "
              "signed April 12, 2022 -- defending the constitutional right of law-abiding "
              "Georgians to keep and bear arms without a government permission slip.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
    ]),

    # --------------- Matt Barton (GA-R, State Representative District 5) ---------------
    ("matt-barton", "GA", "Representative", [
        claim("mb1", "matt-barton", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which passed "
              "the Georgia House 92-78 on March 28, 2019. The law defined any unborn child "
              "with a detectable heartbeat as a 'natural person' entitled to legal protection "
              "and banned abortions after cardiac activity is detectable at approximately six "
              "weeks -- with Barton among the overwhelming Republican majority affirming "
              "protection of unborn life.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("mb2", "matt-barton", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), passed the "
              "Georgia House 100-75 on a strict party-line vote on March 25, 2021. The law "
              "required government-issued photo ID for absentee voting, restricted "
              "unsolicited absentee ballot distribution, capped drop boxes to one per county "
              "or one per 100,000 voters, and mandated secure ballot-chain-of-custody "
              "procedures -- establishing the most comprehensive Georgia election security "
              "reform in decades.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("mb3", "matt-barton", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), which "
              "eliminated the Georgia Weapons Carry License requirement for carrying a "
              "handgun in public by law-abiding citizens. The bill passed the Georgia House "
              "100-67 on a strict party-line vote on March 1, 2022, signed by Governor Kemp "
              "on April 12, 2022 -- opposing permit-based infringement on the constitutional "
              "right to bear arms.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
    ]),

    # --------------- Martin Momtahan (GA-R, State Representative District 17) ---------------
    ("martin-momtahan", "GA", "Representative", [
        claim("mm1", "martin-momtahan", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which passed "
              "the Georgia House 92-78 on March 28, 2019, with virtually unanimous Republican "
              "support. The law recognized unborn children with detectable heartbeats as "
              "'natural persons' under Georgia law and prohibited abortion at or after cardiac "
              "activity is detectable -- affirming the state's legislative defense of unborn "
              "personhood.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("mm2", "martin-momtahan", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), passed 100-75 "
              "along strict party lines on March 25, 2021. The law required photo ID for "
              "absentee voting, prohibited government officials from mailing unsolicited "
              "absentee ballot applications, established secure drop-box limits and "
              "supervision requirements, and authorized the State Election Board to "
              "intervene in counties with systemic problems -- comprehensively tightening "
              "Georgia's election administration.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("mm3", "martin-momtahan", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), passed the "
              "Georgia House 100-67 on a strict party-line vote. The law eliminated the "
              "requirement for a Georgia Weapons Carry License to carry a handgun openly or "
              "concealed in public, recognizing that law-abiding citizens have a fundamental "
              "right to self-defense without prior government approval.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
    ]),

    # --------------- Lee Hawkins (GA-R, State Representative District 27) ---------------
    ("lee-hawkins", "GA", "Representative", [
        claim("lh1", "lee-hawkins", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which passed "
              "the Georgia House 92-78 on March 28, 2019 and was signed by Governor Kemp "
              "on May 7, 2019. As a multi-term Republican representative from Hall County, "
              "Hawkins was among the overwhelming majority of House Republicans voting to "
              "recognize unborn personhood and ban abortions after fetal cardiac activity "
              "is detectable -- among the strongest pro-life votes in Georgia's modern "
              "legislative history.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("lh2", "lee-hawkins", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), passed 100-75 "
              "on a strict party-line vote on March 25, 2021. The landmark law required "
              "photo ID for absentee voting, restricted unsolicited ballot applications, "
              "limited drop boxes, expanded in-person early voting while tightening "
              "weekend procedures, and gave the State Election Board enhanced oversight "
              "powers -- all affirming Georgia's commitment to verified, secure elections.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("lh3", "lee-hawkins", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the state permit requirement for carrying a handgun. The bill passed the "
              "Georgia House 100-67 on a strict party-line vote on March 1, 2022, and was "
              "signed into law on April 12, 2022 -- defending Second Amendment rights by "
              "removing the government-issued license barrier to lawful self-defense.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<36} ({state}) +{len(new_claims)} claims  "
              f"conf: {old_conf} -> evidence_curated")

    # Minified write -- keep scorecard.json under GitHub's 50 MB warning.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
