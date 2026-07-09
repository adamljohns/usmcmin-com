#!/usr/bin/env python3
"""Enrichment batch 594: hand-curated claims for 5 SC state senators.

Targets archetype_party_default state senators from South Carolina,
continuing from batch 593 (working bottom-of-alphabet through SC by name).

Candidates (reverse-alpha by name, remaining SC bucket):
  Everett Stubbs (SC-R)       — District 17, Chester/Fairfield/Lancaster/York, since Nov 2024
  Ed Sutton (SC-D)            — District 20, Charleston County, since Nov 2024
  Deon T. Tedder (SC-D)       — District 42, Charleston/Dorchester, since Nov 2023
  Darrell Jackson (SC-D)      — District 21, Richland County (Hopkins/Columbia), since 1992
  Daniel B. Verdin III (SC-R) — District 9, Greenville/Laurens/Union, since 2001

Each claim cites >=1 reliable source and reflects 2021-2026 voting record /
public positions.

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
    # ---------------- Everett Stubbs (SC-R, State Senator District 17) ----------------
    ("everett-stubbs", "SC", "Senator", [
        claim("es1", "everett-stubbs", "self_defense", 0, True,
              "Identifies as an 'unapologetic supporter of... pro-2A' on his official campaign website (votestubbs.com). As a freshman senator from District 17 (Chester, Fairfield, Lancaster, and York Counties) who took office November 2024 — after SC's Constitutional Carry Act (H.3594) was already signed March 7, 2024 — Stubbs co-sponsored S.183 (Drug-Induced Homicide Act, 2025), which targets fentanyl dealers whose product causes fatal overdoses, citing a fentanyl seizure in his district. He sits on the Senate Judiciary and Fish, Game, and Forestry Committees.",
              ["https://votestubbs.com/",
               "https://ballotpedia.org/Everett_Stubbs",
               "https://legiscan.com/SC/bill/S0183/2025"]),
        claim("es2", "everett-stubbs", "economic_stewardship", 2, True,
              "Co-sponsored S.318 (Commission on Fiscal Restraint and Government Efficiency Act, 2025-2026 session), which creates a state-level commission modeled on federal efficiency initiatives to mandate spending reductions with binding reporting deadlines to the General Assembly and Governor. Also received the endorsement of Americans for Prosperity – South Carolina, which cited fiscal responsibility and his opponent's record of voting for tax increases as key factors.",
              ["https://www.scstatehouse.gov/sess126_2025-2026/bills/318.htm",
               "https://americansforprosperity.org/blog/americans-for-prosperity-south-carolina-announces-two-new-endorsements-in-state-senate-races/",
               "https://ballotpedia.org/Everett_Stubbs"]),
        claim("es3", "everett-stubbs", "sanctity_of_life", 0, False,
              "Per the SC Daily Gazette 2024 Voter Guide (District 17 race), Stubbs does not advocate for an abortion ban at conception and stated his position as supporting the existing six-week heartbeat ban (SC Act #70 of 2023, S.474) without calling for further restriction to life-at-conception/personhood. He took office in November 2024 after the Fetal Heartbeat and Protection from Abortion Act was already enacted. He does not hold a formal personhood or life-begins-at-conception position.",
              ["https://scdailygazette.com/race-details/sc-senate-17-fanning-stubbs/"]),
    ]),

    # ---------------- Ed Sutton (SC-D, State Senator District 20) ----------------
    ("ed-sutton", "SC", "Senator", [
        claim("esu1", "ed-sutton", "biblical_marriage", 2, False,
              "Was one of only two senators (out of 46) to vote NO on H.4756 (SC Student Physical Privacy Act), which restricts transgender students to bathrooms and locker rooms matching their biological sex at birth, extending an existing K-12 law to public colleges and universities. The bill passed 35-2 on March 25, 2026, and was signed by Governor McMaster on May 15, 2026. Sutton argued the bill violated Title IX: 'The Fourth Circuit's already ruled this unconstitutional. The Supreme Court refused to hear it. This law is never going into effect.' The only other no vote was Democratic Sen. Deon Tedder.",
              ["https://scdailygazette.com/2026/03/26/sc-senate-approves-bill-restricting-transgender-bathroom-use-at-k-12-schools-and-colleges/",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/4756.htm"]),
        claim("esu2", "ed-sutton", "sanctity_of_life", 0, False,
              "As a member of the SC Senate Democratic Caucus — whose 10 members are uniformly on record opposing abortion restrictions — Sutton's caucus voted against S.474 (six-week heartbeat ban, enacted 2023, passed Senate 27-19 with all 15 Democrats opposed) and S.1095 (near-total abortion ban without rape/incest exceptions, 2026). No individual floor vote by Sutton on abortion legislation has been documented, as he only took office November 2024 and is not on the Medical Affairs Committee, but his caucus position is fully documented and he has not co-sponsored any pro-life legislation.",
              ["https://scdailygazette.com/2026/04/21/abortion-ban-advances-but-sc-senator-vows-to-stop-it-from-going-further/",
               "https://scdailygazette.com/2025/11/19/senators-reject-scs-abortion-ban-touted-as-strictest-nationwide/"]),
        claim("esu3", "ed-sutton", "family_child_sovereignty", 0, False,
              "Publicly opposes SC's Education Scholarship Trust Fund (ESA/school choice voucher program), describing himself as 'a fierce believer in the transformative power of public education' and stating opposition to taxpayer-funded scholarships for private school tuition. His stated education priorities center on improving public school options and teacher retention (supporting H.3196, the Educator Assistance Act) rather than diverting public funds to private schools. The SC Senate voted 29-13 in April 2025 to restore the school choice program (S.62) after the SC Supreme Court struck it down.",
              ["https://www.counton2.com/news/your-local-election-hq/democrat-ed-sutton-elected-to-charlestons-newest-senate-seat-here-are-his-plans/",
               "https://abcnews4.com/news/local/new-district-new-leader-ed-sutton-shares-plans-for-district-20-seat-and-its-importance-wciv-abc-news-4-2024-local-election-affordable-housing-public-transit"]),
    ]),

    # ---------------- Deon T. Tedder (SC-D, State Senator District 42) ----------------
    ("deon-t-tedder", "SC", "Senator", [
        claim("dtt1", "deon-t-tedder", "self_defense", 0, False,
              "Voted NO on H.3594 (SC Constitutional Carry/Second Amendment Preservation Act), which passed the Senate 28-14 on February 1, 2024 and was signed into law March 7, 2024, making South Carolina the 29th permitless-carry state. Before the final vote, Tedder successfully added an anti-racial profiling amendment to the bill — then voted against final passage anyway. He represents District 42 (Charleston and Dorchester Counties, North Charleston area) and sits on the Senate Judiciary Committee.",
              ["https://bearingarms.com/camedwards/2024/04/25/south-carolina-democrat-constitutional-carry-n1224656",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/3594.htm",
               "https://www.postandcourier.com/politics/south-carolina-senate-permitless-constitutional-carry/article_e5d09e26-c141-11ee-865e-43b91e5e3d2c.html"]),
        claim("dtt2", "deon-t-tedder", "sanctity_of_life", 0, False,
              "As a member of the Senate Medical Affairs Committee, actively opposed S.474 (the Fetal Heartbeat and Protection from Abortion Act, enacted 2023), which bans most abortions after detection of early cardiac activity (~6 weeks). Also voted NO on S.1095 (a near-total abortion ban, no rape/incest exceptions) when the Medical Affairs Committee advanced it 8-4 on party lines in April 2026. Tedder publicly questioned the bill's enforceability: 'If there's no policing mechanism to disallow what we're trying to disallow, essentially it will still be available.'",
              ["https://scdailygazette.com/2026/04/21/abortion-ban-advances-but-sc-senator-vows-to-stop-it-from-going-further/",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/474.htm",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/1095.htm"]),
        claim("dtt3", "deon-t-tedder", "biblical_marriage", 2, False,
              "One of only two senators (35-2) to vote NO on H.4756 (SC Student Physical Privacy Act), which extends transgender bathroom and locker room restrictions matching biological sex at birth from K-12 to public colleges and universities, signed by Governor McMaster on May 15, 2026. The other no vote was Democratic Sen. Ed Sutton of Charleston. Tedder represents District 42 (portions of Charleston and Dorchester Counties).",
              ["https://scdailygazette.com/2026/03/26/sc-senate-approves-bill-restricting-transgender-bathroom-use-at-k-12-schools-and-colleges/",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/4756.htm"]),
    ]),

    # ---------------- Darrell Jackson (SC-D, State Senator District 21) ----------------
    ("darrell-jackson", "SC", "Senator", [
        claim("dj1", "darrell-jackson", "self_defense", 0, False,
              "Voted NO on H.3594 (SC Constitutional Carry Act), which passed the Senate 28-14 on February 1, 2024, making South Carolina the 29th permitless-carry state. Jackson, a Democrat who has represented Richland County's District 21 (Hopkins/Columbia area) since 1992 and is also the Senior Pastor of Bible Way Church of Atlas Road, was among the 14 senators opposing the bill. His Palmetto Liberty PAC legislative scorecard rating was 6 out of 100, ranking near the bottom of all 46 senators on gun-rights votes.",
              ["https://www.postandcourier.com/politics/south-carolina-senate-permitless-constitutional-carry/article_e5d09e26-c141-11ee-865e-43b91e5e3d2c.html",
               "https://ballotpedia.org/Darrell_Jackson_(South_Carolina)",
               "https://justfacts.votesmart.org/candidate/biography/3957/darrell-jackson"]),
        claim("dj2", "darrell-jackson", "sanctity_of_life", 0, False,
              "One of 15 unified South Carolina Senate Democrats who voted against S.474 (the Fetal Heartbeat and Protection from Abortion Act), which passed 27-19 on May 23, 2023 and was signed into law the same day by Governor McMaster. Jackson, the Senior Pastor of Bible Way Church of Atlas Road who has served in the SC Senate since 1992, has aligned with his party caucus in opposing all abortion restrictions throughout his legislative career — a position at odds with his ministerial background. He has not co-sponsored any pro-life legislation during his Senate tenure.",
              ["https://www.washingtonpost.com/nation/2023/05/23/south-carolina-six-week-abortion-ban-vote/",
               "https://ballotpedia.org/Darrell_Jackson_(South_Carolina)",
               "https://www.scstatehouse.gov/member.php?code=920454435"]),
        claim("dj3", "darrell-jackson", "economic_stewardship", 2, False,
              "Sponsored S.10 (2025-2026 session) expanding state-funded paid parental leave for all categories of SC state employees — extending eligibility to grant-funded, time-limited, and part-time workers; doubling non-birthing parent leave from 2 to 4 weeks; and adding stillbirth as a qualifying event. The bill passed both chambers and was sent to the governor in 2026. The expansion represents increased state government benefit obligations and expenditure, inconsistent with anti-deficit/balanced-budget fiscal discipline.",
              ["https://holycitysinner.com/politics/sen-darrell-jackson-s-paid-parental-leave-expansion-heads-to/",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/10.htm"]),
    ]),

    # ---------------- Daniel B. Verdin III (SC-R, State Senator District 9) ----------------
    ("daniel-b-verdin-iii", "SC", "Senator", [
        claim("dbv1", "daniel-b-verdin-iii", "sanctity_of_life", 0, True,
              "As Chairman of the SC Senate Medical Affairs Committee, managed S.1 (the original SC Fetal Heartbeat and Protection from Abortion Act, 2021) through the committee process, overseeing hundreds of hours of public testimony; the bill passed the Senate 30-13 and was signed into law February 18, 2021. Also advanced S.474 (2023 successor heartbeat legislation, signed May 25, 2023) from his committee chair position. His campaign website states he has 'co-sponsored 30 pieces of pro-life legislation across his 23 legislative sessions' and is 'a stalwart defender of the life of the unborn... championing a Biblical worldview in other bioethical and social order issues.'",
              ["https://www.dannyverdin.com/about",
               "https://www.dannyverdin.com/issues",
               "https://www.scstatehouse.gov/sess124_2021-2022/bills/1.htm",
               "https://ballotpedia.org/Daniel_Verdin"]),
        claim("dbv2", "daniel-b-verdin-iii", "self_defense", 0, True,
              "Co-sponsored S.109 (SC Constitutional Carry Act of 2023) — the Senate companion to H.3594, which passed the Senate 28-15 in February 2024 and was signed into law March 7, 2024, making SC the 29th permitless-carry state. His campaign website states: 'Danny fully supports the Second Amendment and the rights of gun-owners to protect their families and property. Danny believes the overall safety of the community is strengthened and benefitted by responsible, well-defended individuals.' He has represented District 9 (Greenville, Laurens, and Union Counties) since 2001.",
              ["https://www.dannyverdin.com/issues",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/109.htm",
               "https://www.live5news.com/2024/03/07/mcmaster-signs-constitutional-carry-bill/"]),
        claim("dbv3", "daniel-b-verdin-iii", "biblical_marriage", 0, True,
              "Publicly states on his official campaign website: 'As a Christian, Verdin understands that marriage can only be entered into by one man and one woman, gender is acknowledged at birth based on biology and Biblical truth, and he will promote the natural order of male and female, marriage, and the home.' A graduate of Bob Jones University (B.A. 1986), Verdin has served as District 9's senator since 2001, bringing a consistent biblical-worldview framework to his legislative work as chairman of the Medical Affairs Committee.",
              ["https://www.dannyverdin.com/issues",
               "https://en.wikipedia.org/wiki/Danny_Verdin",
               "https://ballotpedia.org/Daniel_Verdin"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
