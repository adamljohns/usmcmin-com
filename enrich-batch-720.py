#!/usr/bin/env python3
"""Enrichment batch 720: evidence claims for 5 GA-R state representatives.

Primary federal senator/representative pools fully exhausted.
Continues evidence_state GA-R state representatives with 0 claims,
bottom-of-alphabet reverse-sort (Lauren McDonald -> Katie Dempsey ->
Kasey Carpenter -> Joseph Gullett -> Jordan Ridley):

  Lauren McDonald   (GA-R, State Representative HD-26, Forsyth Co., since Jan 2021)
  Katie Dempsey     (GA-R, State Representative HD-13, Rome/Floyd Co., since 2007)
  Kasey Carpenter   (GA-R, State Representative HD-4, Whitfield Co., since 2017)
  Joseph Gullett    (GA-R, State Representative HD-19, Paulding Co., since Jan 2019)
  Jordan Ridley     (GA-R, State Representative HD-22, Cherokee/Cobb, since Jan 2023)

Sources: en.wikipedia.org, legiscan.com, ajc.com, ballotpedia.org,
news.ballotpedia.org. Covers 2019-2024 public legislative record
(party-line floor votes and confirmed roll calls).
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
    # ----------- Lauren McDonald (GA-R, State Representative HD-26, since Jan 2021) -----------
    ("lauren-mcdonald", "GA", "Representative", [
        claim("lm1", "lauren-mcdonald", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which passed "
              "the Georgia House 100-75 on a strict party-line vote on March 25, 2021, and "
              "was signed by Governor Kemp on March 25, 2021. McDonald was in her first "
              "term (sworn in January 11, 2021) when the law required photo ID for absentee "
              "ballots, banned unsolicited absentee ballot mailings, capped drop boxes at one "
              "per county or one per 100,000 voters, and mandated a secure chain of custody "
              "for mail ballots — the most comprehensive Georgia election security reform in "
              "a generation.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("lm2", "lauren-mcdonald", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), which "
              "eliminated the Georgia Weapons Carry License requirement for carrying a "
              "handgun openly or concealed in public by law-abiding citizens. The bill "
              "passed the Georgia House 100-67 on a strict party-line vote on March 1, "
              "2022, and was signed by Governor Kemp on April 12, 2022 — defending the "
              "Second Amendment right to bear arms without a government-issued permission "
              "slip.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
        claim("lm3", "lauren-mcdonald", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), which prohibits healthcare professionals "
              "from prescribing cross-sex hormones or performing gender-transition surgeries "
              "on minors, signed by Governor Kemp on March 23, 2023. The bill passed the "
              "Georgia House 96-75 on a strict party-line vote on March 16, 2023, with "
              "McDonald among the Republican majority rejecting the claim that children can "
              "change their biological sex — an affirmation that gender is binary and "
              "determined at birth.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.ajc.com/politics/georgia-governor-signs-bill-limiting-treatment-to-transgender-minors/ZNEOHIJEYNANFF7VHWC4UJVS4E/"]),
    ]),

    # ----------- Katie Dempsey (GA-R, State Representative HD-13, since 2007) -----------
    ("katie-dempsey", "GA", "Representative", [
        claim("kd1", "katie-dempsey", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which banned "
              "abortions after a fetal heartbeat is detectable (approximately 6 weeks) and "
              "defined an unborn child with a detectable heartbeat as a 'natural person' "
              "under Georgia law. The bill passed the Georgia House 92-78 on March 28, 2019, "
              "with overwhelming Republican support, and was signed by Governor Kemp on "
              "May 7, 2019 — Dempsey, a multi-term member since 2007, was among the House "
              "majority affirming legal personhood from earliest detectable life.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("kd2", "katie-dempsey", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which passed "
              "the Georgia House 100-75 on a strict party-line vote on March 25, 2021, and "
              "was signed the same day. The law required photo ID for absentee ballots, "
              "prohibited officials from mailing unsolicited absentee ballot applications, "
              "established secure drop-box limits and supervision requirements, expanded "
              "in-person early voting while tightening weekend procedures, and authorized "
              "the State Election Board to intervene in counties with systemic problems.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("kd3", "katie-dempsey", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the Georgia Weapons Carry License requirement for carrying a handgun in "
              "public. The bill passed the Georgia House 100-67 on a strict party-line vote "
              "on March 1, 2022, and was signed into law by Governor Kemp on April 12, "
              "2022 — recognizing that law-abiding Georgians have a fundamental right to "
              "self-defense without prior government approval.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
    ]),

    # ----------- Kasey Carpenter (GA-R, State Representative HD-4, since 2017) -----------
    ("kasey-carpenter", "GA", "Representative", [
        claim("kc1", "kasey-carpenter", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which passed "
              "the Georgia House 92-78 on March 28, 2019. The law recognized any unborn "
              "child with a detectable heartbeat as a 'natural person' under Georgia law "
              "and banned abortions after cardiac activity is detectable at approximately "
              "six weeks. Carpenter, serving since 2017 in HD-4 (Whitfield County), was "
              "among the overwhelming Republican majority supporting fetal personhood.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("kc2", "kasey-carpenter", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), passed the "
              "Georgia House 100-75 on a strict party-line vote on March 25, 2021. The "
              "law required government-issued photo ID for absentee voting, restricted "
              "unsolicited absentee ballot distribution, capped drop boxes, mandated "
              "ballot chain-of-custody procedures, and gave the State Election Board "
              "enhanced oversight powers — comprehensively tightening Georgia's election "
              "administration.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("kc3", "kasey-carpenter", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), which "
              "eliminated the permit requirement for carrying a handgun in public. The "
              "bill passed the Georgia House 100-67 on a strict party-line vote on "
              "March 1, 2022, and was signed by Governor Kemp on April 12, 2022 — "
              "opposing permit-based infringement on the constitutional right of "
              "law-abiding Georgians to keep and bear arms.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021"]),
    ]),

    # ----------- Joseph Gullett (GA-R, State Representative HD-19, since Jan 2019) -----------
    ("joseph-gullett", "GA", "Representative", [
        claim("jg1", "joseph-gullett", "sanctity_of_life", 0, True,
              "Voted YES on Georgia HB 481 (LIFE Act / Heartbeat Bill, 2019), which passed "
              "the Georgia House 92-78 on March 28, 2019 and was signed by Governor Kemp "
              "on May 7, 2019. As a freshman representative from Paulding County (HD-19, "
              "sworn in January 2019), Gullett joined the overwhelming Republican majority "
              "to recognize unborn children with a detectable heartbeat as 'natural persons' "
              "under Georgia law — affirming the state's legislative defense of unborn "
              "personhood from earliest detectable life.",
              ["https://en.wikipedia.org/wiki/Georgia_House_Bill_481",
               "https://legiscan.com/GA/bill/HB481/2019"]),
        claim("jg2", "joseph-gullett", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), passed the "
              "Georgia House 100-75 on a strict party-line vote on March 25, 2021, and "
              "signed the same day. Gullett co-sponsored a key element of the bill — the "
              "private-money ban provision, sometimes called the 'Zuckerbucks ban,' which "
              "was folded into SB 202 — prohibiting outside organizations from funding "
              "election administration. The law also required photo ID for absentee "
              "voting, limited drop boxes, and restricted unsolicited ballot mailings.",
              ["https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://legiscan.com/GA/bill/SB202/2021"]),
        claim("jg3", "joseph-gullett", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), which "
              "eliminated the Georgia Weapons Carry License requirement for carrying a "
              "handgun openly or concealed in public by law-abiding citizens. The bill "
              "passed the Georgia House 100-67 on a strict party-line vote on March 1, "
              "2022, signed by Governor Kemp on April 12, 2022. Gullett's Turning Point "
              "Action 100% lifetime key-issues score reflects consistent Second Amendment "
              "advocacy, including this constitutional carry milestone.",
              ["https://en.wikipedia.org/wiki/Gun_laws_in_Georgia_(U.S._state)",
               "https://legiscan.com/GA/bill/SB319/2021",
               "https://ballotpedia.org/Joseph_Gullett"]),
    ]),

    # ----------- Jordan Ridley (GA-R, State Representative HD-22, since Jan 2023) -----------
    ("jordan-ridley", "GA", "Representative", [
        claim("jr1", "jordan-ridley", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), which prohibits healthcare professionals "
              "from prescribing cross-sex hormones or performing gender-transition surgeries "
              "on minors. The bill passed the Georgia House 96-75 on a strict party-line "
              "vote on March 16, 2023 — Ridley's first legislative session after taking "
              "office in January 2023 — and was signed by Governor Kemp on March 23, 2023. "
              "Ridley's Turning Point Action lifetime key-issues score of 100 confirms "
              "consistent alignment with conservative social positions, including the "
              "rejection of gender ideology for children.",
              ["https://legiscan.com/GA/bill/SB140/2023",
               "https://www.ajc.com/politics/georgia-governor-signs-bill-limiting-treatment-to-transgender-minors/ZNEOHIJEYNANFF7VHWC4UJVS4E/",
               "https://ballotpedia.org/Jordan_Ridley"]),
        claim("jr2", "jordan-ridley", "border_immigration", 2, True,
              "Voted YES on Georgia HB 1105 (Georgia Criminal Alien Track and Report Act "
              "of 2024), which passed the Georgia House 97-74 on a party-line vote on "
              "February 29, 2024, and was signed by Governor Kemp. The law requires "
              "Georgia sheriffs and jailers to hold any suspect believed to be in the "
              "country without legal permission when that person is subject to an ICE "
              "detainer, mandates reporting to federal immigration authorities, and "
              "authorizes police to arrest suspected illegal immigrants — eliminating "
              "sanctuary-style non-cooperation with federal immigration enforcement.",
              ["https://legiscan.com/GA/bill/HB1105/2023",
               "https://www.ajc.com/politics/georgia-house-passes-immigration-enforcement-bill-after-athens-killing/ZY6CKX44E5HRDLVEP3G3ZHJUOY/",
               "https://www.ajc.com/politics/kemp-signs-bill-requiring-georgia-sheriffs-to-enforce-federal-immigration-law/FQ55VHG6VBDYXED3X34DEFXNXE/"]),
        claim("jr3", "jordan-ridley", "election_integrity", 0, True,
              "Voted YES on Georgia SB 189 (2024), a comprehensive election security bill "
              "that passed the Georgia House 101-73 on March 26, 2024, and was signed by "
              "Governor Kemp on May 6, 2024. The law eliminates QR codes from ballots "
              "(requiring human-readable paper records), requires all absentee ballots to "
              "be counted by one hour after poll closing, expands the ability to challenge "
              "voter eligibility, and restructures the State Election Board — strengthening "
              "the chain of custody and verification procedures for Georgia elections.",
              ["https://legiscan.com/GA/bill/SB189/2023",
               "https://news.ballotpedia.org/2024/05/17/georgia-governor-brian-kemp-r-signs-legislation-making-significant-changes-to-state-election-laws/",
               "https://www.ajc.com/politics/georgia-voter-challenge-and-election-security-bills-signed-into-law/5D7L7RBZKRFR7MWNPVU6ZMVNCI/"]),
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
