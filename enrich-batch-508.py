#!/usr/bin/env python3
"""Enrichment batch 508: 5 Wisconsin Republican State Assembly Members with 0 claims.

archetype_party_default state legislators (WI — bottom of alphabet), continuing
from batch 507. All five are sitting Assembly Republicans with 0 prior claims.

Targets:
  Duke Tucker     (duke-tucker-wi-75)     — WI AD-75 Burnett County; elected Nov 2024;
                                            U.S. Air Force veteran (Desert Storm/Shield);
                                            NRA member; operations manager, Grantsburg Telcom
  Dean Kaufert    (dean-kaufert-wi-53)    — WI AD-53 Neenah; former Mayor of Neenah 2014-2022;
                                            prior Assembly service 1991-2015 (AD-55, ACU 96.43%);
                                            returned to Assembly Jan 2025; retiring 2026
  David Steffen   (david-steffen-wi-4)   — WI AD-4 Howard/Brown County; in office since 2015;
                                            author of AB386 ($2.9B tax cut, 2023); AB382 introducer
  David Murphy    (david-murphy-wi-56)   — WI AD-56; introducer of AB382 (born alive, 2025);
                                            cosponsor of AJR78 (voter photo ID, 2023)
  David Armstrong (david-armstrong-wi-67) — WI AD-67 Rice Lake/Barron County; formerly AD-75
                                            (2021-2025); co-author of multiple housing/childcare
                                            tax bills; elected to AD-67 Nov 2024

Key WI bills referenced:
  AB975  (2023) — 14-week abortion referendum; passed Assembly 53-46, Jan 25, 2024; vetoed by Gov. Evers
  AJR78  (2023) — Voter photo ID const. amendment (Assembly companion to SJR73); passed 62-35 Nov 2023
  SJR2   (2025) — Voter photo ID const. amendment (second consideration); passed Assembly 54-45 Jan 2025;
                   approved by WI voters April 2025 (now in WI Constitution)
  AB382  (2025) — Born alive infant protection; introduced July 31, 2025
  AB609  (2025) — Constitutional carry / concealed carry reform
  AJR112 (2025) — Right to keep and bear arms as fundamental right, subject to strict scrutiny
  AB74   (2025) — Parental notification of sexual misconduct by school staff
  AB448  (2011) — Partial-birth abortion ban
  AB100  (2025) — Sex-based athletic teams (K-12); prohibits males from competing on female teams

NOTE: writes scorecard.json MINIFIED to keep file ~35-36 MB under GitHub 50 MB cap.
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
    # ---- Duke Tucker (WI AD-75, Burnett County; since Jan 2025) ----
    ("duke-tucker-wi-75", "WI", "Assembly", [
        claim("dt1", "duke-tucker-wi-75", "self_defense", 0, True,
              "Duke Tucker (R, WI AD-75) is a confirmed cosponsor of 2025 Wisconsin Assembly Bill 609, legislation to reform Wisconsin's concealed carry law toward constitutional carry — allowing law-abiding citizens to carry a concealed firearm without the current permit requirement. Tucker is an NRA member and U.S. Air Force veteran (Desert Storm/Shield) who describes himself as 'a staunch supporter of the 2nd Amendment ... committed to responsible gun ownership and the right to defend yourself and your family.' His cosponsorship of AB609 reflects that commitment in the 2025-26 legislative session.",
              ["https://legiscan.com/WI/research/AB609",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab609",
               "https://ballotpedia.org/Duke_Tucker"]),
        claim("dt2", "duke-tucker-wi-75", "election_integrity", 0, True,
              "Duke Tucker was a cosponsor of 2025 Senate Joint Resolution 2 (SJR2/AJR1), the second-consideration voter photo ID constitutional amendment, introduced January 6, 2025. The Assembly passed SJR2 54-45 on January 14, 2025, and Wisconsin voters approved the amendment at the April 1, 2025 statewide referendum — permanently enshrining a photo identification requirement to vote in any Wisconsin election in the state constitution.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/sjr2",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("dt3", "duke-tucker-wi-75", "self_defense", 1, True,
              "Duke Tucker was a co-introducing representative of 2025 Wisconsin Assembly Joint Resolution 112 (AJR112), introduced October 29, 2025, which would amend the Wisconsin Constitution to designate the right to keep and bear arms as a 'fundamental individual right' subject to strict scrutiny — the highest standard of judicial review, which defeats nearly all gun-control restrictions including red-flag laws, assault-weapon bans, and magazine limits. Tucker's role as an introducer places him among the leading pro-2A legislators in the 2025-26 session.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr112",
               "https://www.nraila.org/articles/20251226/wisconsin-strict-scrutiny-resolution-scheduled-for-committee-hearing"]),
    ]),

    # ---- Dean Kaufert (WI AD-53, Neenah; since Jan 2025) ----
    ("dean-kaufert-wi-53", "WI", "Assembly", [
        claim("dk1", "dean-kaufert-wi-53", "election_integrity", 0, True,
              "Dean Kaufert is a confirmed co-introducing representative of 2025 Assembly Joint Resolution 1 (AJR1) and its Senate companion SJR2, the second-consideration voter photo ID constitutional amendment, introduced January 6, 2025. The amendment passed the Assembly 54-45 and was approved by Wisconsin voters at the April 1, 2025 statewide referendum, permanently enshrining a photo identification requirement to vote in any Wisconsin election in the state constitution. Kaufert serves as Vice Chair of the Assembly Committee on Ways and Means.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://legiscan.com/WI/bill/SJR2/2025",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("dk2", "dean-kaufert-wi-53", "family_child_sovereignty", 0, True,
              "Dean Kaufert was a co-introducing representative of 2025 Wisconsin Assembly Bill 74, introduced February 28, 2025, which requires school boards to notify parents or guardians by end of day when a credible report alleges sexual misconduct by a school staff member against their child. Kaufert's co-introduction of AB74 affirms a commitment to parental rights and school transparency; the bill was signed into law in 2025.",
              ["https://docs.legis.wisconsin.gov/2025/related/proposals/ab74",
               "https://legiscan.com/WI/bill/AB74/2025"]),
        claim("dk3", "dean-kaufert-wi-53", "sanctity_of_life", 0, True,
              "During his prior Assembly tenure representing District 55 (1991-2015), Dean Kaufert was a named introducing representative of 2011 Wisconsin Assembly Bill 448, legislation prohibiting partial-birth abortions with a criminal penalty — one of the most direct pro-life legislative positions a legislator can take. Kaufert earned a 96.43% lifetime rating from the American Conservative Union across 24 years of prior Assembly service, reflecting a consistent pro-life and socially conservative voting record.",
              ["https://docs.legis.wisconsin.gov/2011/related/proposals/ab448",
               "https://justfacts.votesmart.org/candidate/3507/dean-kaufert",
               "https://ballotpedia.org/Dean_Kaufert"]),
    ]),

    # ---- David Steffen (WI AD-4, Howard/Brown County; since Jan 2015) ----
    ("david-steffen-wi-4", "WI", "Assembly", [
        claim("ds1", "david-steffen-wi-4", "sanctity_of_life", 0, True,
              "David Steffen (R, WI AD-4) is a primary introducing representative of 2025 Wisconsin Assembly Bill 382, introduced July 31, 2025, requiring health care providers present at a birth following an abortion or attempted abortion to exercise the same professional standard of care for that infant as for any other child born alive at the same gestational age, and to immediately transfer the infant to a hospital. Steffen has cosponsored born-alive legislation in consecutive sessions — SB16 in 2021 and AB382 in 2025 — reflecting a sustained commitment to infant personhood from the moment of live birth.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://docs.legis.wisconsin.gov/2021/related/proposals/sb16"]),
        claim("ds2", "david-steffen-wi-4", "election_integrity", 0, True,
              "David Steffen is a confirmed cosponsor of 2023 Wisconsin Assembly Joint Resolution 78 (AJR78), the Assembly companion to SJR73 — the voter photo ID constitutional amendment (first consideration), which passed the Assembly 62-35 on November 9, 2023. In January 2025 Steffen joined Assembly Republicans at a press conference announcing the second-consideration resolution (SJR2/AJR1), which passed 54-45 and was approved by Wisconsin voters at the April 1, 2025 referendum, permanently requiring photo ID to vote in the Wisconsin Constitution.",
              ["https://www.billsponsor.com/bills/491164/wisconsin-senate-joint-resolution-73-session-2023",
               "https://www.wispolitics.com/2025/rep-steffen-joins-assembly-republicans-in-announcing-voter-id-constitutional-amendment/",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("ds3", "david-steffen-wi-4", "biblical_marriage", 0, True,
              "David Steffen has stated on the public VoteSmart/iVoterGuide voter survey: 'Governments should define marriage as between one man and one woman; no other definition of marriage should be legalized or supported with taxpayer or public funds.' He has also stated: 'Judeo-Christian values established a framework of morality which permitted our system of limited government,' reflecting a worldview grounding his policy positions in biblical marriage and religious tradition.",
              ["https://justfacts.votesmart.org/candidate/51859/david-steffen",
               "https://ballotpedia.org/David_Steffen"]),
    ]),

    # ---- David Murphy (WI AD-56; current session) ----
    ("david-murphy-wi-56", "WI", "Assembly", [
        claim("dm1", "david-murphy-wi-56", "sanctity_of_life", 0, True,
              "David Murphy (R, WI AD-56) is a confirmed introducing representative of 2025 Wisconsin Assembly Bill 382, introduced July 31, 2025, requiring health care providers present at a birth resulting from an abortion or attempted abortion to exercise the same professional standard of care for that infant as for any other child born alive at the same gestational age and to immediately transfer the infant to a hospital. Murphy's co-introduction of AB382 affirms his position that legal personhood and medical obligations extend to every child the moment of live birth.",
              ["https://legiscan.com/WI/research/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab382",
               "https://wifamilycouncil.org/radio/wi-reps-reintroduce-born-alive-bill/"]),
        claim("dm2", "david-murphy-wi-56", "election_integrity", 0, True,
              "David Murphy is a confirmed cosponsor of 2023 Wisconsin Assembly Joint Resolution 78 (AJR78), the Assembly companion to Senate Joint Resolution 73 — the voter photo ID constitutional amendment (first consideration). AJR78 passed the Assembly 62-35 on November 9, 2023. Murphy stated on passage of the second-consideration resolution (SJR2/AJR1) in January 2025: 'Putting Voter ID in our constitution will permanently protect election integrity in Wisconsin.' Voters approved the amendment at the April 1, 2025 referendum.",
              ["https://www.billsponsor.com/bills/491164/wisconsin-senate-joint-resolution-73-session-2023",
               "https://www.wispolitics.com/2025/rep-murphy-statement-on-passage-of-voter-id-constitutional-amendment/",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("dm3", "david-murphy-wi-56", "christian_liberty", 0, True,
              "David Murphy authored 2023 Wisconsin Assembly Joint Resolution 60 (AJR60), a constitutional amendment to Article I, Section 18 of the Wisconsin Constitution prohibiting any state or local agency from ordering a house of worship to close or limiting its gathering size during any emergency — including public health emergencies — in direct response to Gov. Evers's COVID-19 church-closure orders. The Senate passed AJR60 21-10 in November 2023. Murphy reintroduced the second-consideration resolution as AJR10 (2025); it passed the Assembly 56-43 and Senate 18-15 and is on the November 2026 statewide ballot.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ajr60",
               "https://www.wsaw.com/2023/11/07/wisconsin-senate-vote-amendment-blocking-church-closures-during-public-state-emergencies",
               "https://ballotpedia.org/Wisconsin_Prohibit_Government_Closure_of_Places_of_Worship_During_Emergencies_Amendment_(2026)"]),
    ]),

    # ---- David Armstrong (WI AD-67, Rice Lake/Barron County; formerly AD-75, since 2021) ----
    ("david-armstrong-wi-67", "WI", "Assembly", [
        claim("da1", "david-armstrong-wi-67", "sanctity_of_life", 0, True,
              "David Armstrong (R, WI AD-67, formerly AD-75 2021-2025) was a co-introducing representative of 2023-24 Wisconsin Assembly Bill 975, legislation introduced January 19, 2024 that would have placed a 14-week abortion restriction on the Wisconsin ballot as a public referendum. The bill passed the Assembly 53-46 on January 25, 2024, before being vetoed by Governor Evers. Armstrong's position as a primary introducer placed him among the legislators leading the pro-life coalition advancing the measure.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab975",
               "https://www.pbs.org/newshour/politics/wisconsin-republicans-approve-bill-banning-abortions-after-14-weeks-of-pregnancy"]),
        claim("da2", "david-armstrong-wi-67", "election_integrity", 0, True,
              "David Armstrong is a confirmed cosponsor of 2023 Wisconsin Assembly Joint Resolution 78 (AJR78), the Assembly companion to SJR73 — the voter photo ID constitutional amendment (first consideration). He also cosponsored the second-consideration resolution (SJR2/AJR1) in January 2025. Both passed the Assembly; the amendment was approved by Wisconsin voters at the April 1, 2025 referendum, permanently enshrining a photo ID voting requirement in the Wisconsin Constitution.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ajr78",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ajr1",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("da3", "david-armstrong-wi-67", "biblical_marriage", 2, True,
              "David Armstrong was a co-introducing representative of 2025 Wisconsin Assembly Bill 100, introduced March 3, 2025, which designates school athletic teams by the biological sex of participants, defines 'sex' as determined by a physician at birth and reflected on the birth certificate, prohibits males from competing on female teams in public and choice-program schools, and provides a private cause of action for female students denied athletic opportunities. Armstrong's co-introduction of AB100 reflects his rejection of transgender ideology in K-12 public school sports.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab100",
               "https://legiscan.com/WI/bill/AB100/2025"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36 MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
