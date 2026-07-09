#!/usr/bin/env python3
"""Enrichment batch 590: hand-curated claims for 4 SC Republican state senators.

Targets archetype_party_default state senators from South Carolina (bottom of
alphabet — WY/WV/WI/WA/VA already exhausted by prior batches).

Candidates:
  Josh Kimbrell (SC-R) — District 11, Spartanburg County
  Harvey S. Peeler Jr. (SC-R) — District 14, Finance Committee Chairman
  George E. Campsen III (SC-R) — District 43, Religious Liberty Caucus Chair
  Greg Hembree (SC-R) — District 28, Senate Education Committee Chairman

Each claim cites >=1 reliable source (scstatehouse.gov, ballotpedia.org,
official campaign sites, news) and reflects 2020-2025 voting record /
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
    # ---------------- Josh Kimbrell (SC-R, State Senator District 11) ----------------
    ("josh-kimbrell", "SC", "Senator", [
        claim("jk1", "josh-kimbrell", "sanctity_of_life", 0, True,
              "Co-sponsored SC Senate Bill 474, the 'Fetal Heartbeat and Protection from Abortion Act' (2023), banning most abortions after detection of a fetal heartbeat (~6 weeks). The bill passed the SC Senate 27-19 on May 23, 2023, and was signed into law by Governor McMaster on May 25, 2023.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/474.htm",
               "https://scdailygazette.com/2026/04/22/question-about-a-no-exception-abortion-ban-splits-sc-republicans-wanting-to-be-governor/"]),
        claim("jk2", "josh-kimbrell", "self_defense", 0, True,
              "Co-sponsored SC Senate Bill 109, the Constitutional Carry companion bill. The House version (H.3594) passed the Senate in February 2024 and was signed into law by Governor McMaster on March 7, 2024, making South Carolina the 29th permitless-carry state. Kimbrell cited passage of constitutional carry as a top legislative accomplishment in his 2026 governor's race platform.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/109.htm",
               "https://www.live5news.com/2024/03/07/mcmaster-signs-constitutional-carry-bill/",
               "https://www.foxcarolina.com/2025/06/23/sc-senator-josh-kimbrell-announces-run-governor/"]),
        claim("jk3", "josh-kimbrell", "election_integrity", 0, True,
              "Lead Senate sponsor of a joint resolution to amend the SC Constitution so that only U.S. citizens may vote, replacing 'every' with 'only a' in the citizenship-voting clause. Placed on the November 2024 ballot, the amendment was approved by South Carolina voters with 86 percent support.",
              ["https://abcnews4.com/news/local/amendment-to-change-a-single-word-in-south-carolinas-constitution-sparks-debate-voting-early-voting-rep-seth-rose-sen-josh-kimbrel-eligibility",
               "https://www.fairus.org/legislation/state-and-local/eight-states-approve-constitutional-amendments-banning-noncitizen"]),
    ]),

    # ---------------- Harvey S. Peeler Jr. (SC-R, State Senator District 14) ----------------
    ("harvey-s-peeler-jr", "SC", "Senator", [
        claim("hp1", "harvey-s-peeler-jr", "sanctity_of_life", 0, True,
              "Supported the SC Fetal Heartbeat and Protection from Abortion Act (SB 474, signed May 25, 2023), framing his pro-life position in explicitly religious terms: 'Senator Peeler believes that life is a gift from God and must be protected, which is why he strives to protect the unborn and supported the Heartbeat bill — the most pro-life legislation ever passed in the history of South Carolina.'",
              ["https://www.harveypeeler.com/platform",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/474.htm"]),
        claim("hp2", "harvey-s-peeler-jr", "self_defense", 0, True,
              "NRA 'A'-rated senator who voted for South Carolina's Constitutional Carry Act (H.3594, signed March 7, 2024), open carry legislation, and designation of SC as a 'protected Second Amendment state.' His campaign website calls him a 'Second Amendment Champion.'",
              ["https://www.harveypeeler.com/2a",
               "https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/"]),
        claim("hp3", "harvey-s-peeler-jr", "economic_stewardship", 2, True,
              "As Senate Finance Committee Chairman, authored S.1087 (Comprehensive Tax Cut Act of 2022), the largest tax cut and rebate in South Carolina history — over $2 billion in relief. The bill cut the top income tax rate from 7% to 6.5% immediately, phasing to 6%, and passed both chambers unanimously (Senate 42-0, House 110-0). Signed by the governor June 28, 2022.",
              ["https://www.fitsnews.com/2022/02/17/harvey-peeler-unveils-south-carolina-senates-income-tax-cut/",
               "https://www.scstatehouse.gov/sess124_2021-2022/bills/1087.htm"]),
    ]),

    # ---------------- George E. Campsen III (SC-R, State Senator District 43) ----------------
    ("george-e-campsen-iii", "SC", "Senator", [
        claim("gc1", "george-e-campsen-iii", "sanctity_of_life", 0, True,
              "Co-sponsored SC Senate Bill 1, the original 'SC Fetal Heartbeat and Protection from Abortion Act' in January 2021, which passed the Senate 30-13 and was signed into law February 18, 2021. Also participated in floor debate on successor legislation S.474 in 2023 after the SC Supreme Court struck down the first law.",
              ["https://www.scstatehouse.gov/sess124_2021-2022/bills/1.htm",
               "https://www.scsenategop.com/2021/01/29/senate-republicans-pass-fetal-heartbeat-bill/"]),
        claim("gc2", "george-e-campsen-iii", "election_integrity", 0, True,
              "Primary sponsor of SC Senate Bill 108 (2022 Election Integrity Act), which passed both chambers unanimously and was signed by Governor McMaster on May 13, 2022. The bill enacted nearly 20 reforms: required voter ID on absentee ballot applications, banned ballot harvesting, banned unsolicited mailing of absentee applications, banned private funding of election administration ('Zuckerbucks'), required annual voter-roll maintenance, and mandated post-election risk-limiting audits. Campsen's quote: 'Our election reform bill makes it easier to vote, and harder to cheat.'",
              ["https://www.scstatehouse.gov/sess124_2021-2022/bills/108.htm",
               "https://thefga.org/blog/sen-chip-campsen-elections-bill-20-new-reforms-south-carolina-elections/",
               "https://votecampsen.com/sen-chip-campsens-elections-bill-brings-nearly-20-new-reforms-to-south-carolina-elections/"]),
        claim("gc3", "george-e-campsen-iii", "christian_liberty", 0, True,
              "Chairman of the South Carolina Senate Religious Liberty Caucus. Recipient of the William Wilberforce Award for Defense of Religious Liberty from the Palmetto Family Council. In 2025 sponsored S.333, a concurrent resolution designating March 1 as 'South Carolina First in Religious Liberty Day' commemorating the inaugural SC Religious Liberty Conference.",
              ["https://justfacts.votesmart.org/candidate/biography/11920/chip-campsen-iii",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/333.htm"]),
    ]),

    # ---------------- Luke A. Rankin (SC-R, State Senator District 33) ----------------
    ("luke-a-rankin", "SC", "Senator", [
        claim("lr1", "luke-a-rankin", "self_defense", 0, False,
              "The only Republican SC state senator to vote NO on the Constitutional Carry Act (H.3594) when it passed 28-15 in February 2024. Delivered a 40-minute floor speech opposing the bill, citing police chiefs from Myrtle Beach, Conway, Columbia, and Anderson who testified against it. Has repeatedly used his Senate Judiciary Committee chairmanship to bottle up or kill pro-gun bills: removed an open carry bill from the committee agenda in 2018; held constitutional carry bills H3094 and H3096 in committee without hearings in 2021. The National Association for Gun Rights rated him the worst state senator in America on Second Amendment issues.",
              ["https://www.grandstranddaily.com/rankin-only-republican-senator-to-vote-against-constitutional-carry-bill/",
               "https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.ammoland.com/2021/04/south-carolina-constitutional-and-open-carry-bills-in-hands-of-luke-rankin-in-senate/"]),
        claim("lr2", "luke-a-rankin", "self_defense", 1, False,
              "Sponsored SC Senate Bill 638 (2023–2024 session) to create a 'South Carolina Voluntary Do-Not-Sell Firearms List' maintained by SLED; violations by firearm sellers would be a felony carrying up to $2,000 fine or 5 years imprisonment. The bill was opposed by the NRA and Palmetto Gun Rights and was blocked in subcommittee.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/638.htm",
               "https://myrtlebeachsc.com/horry-county-s-c-senator-luke-rankin-ranks-worst-in-america-by-gun-owners/"]),
        claim("lr3", "luke-a-rankin", "family_child_sovereignty", 0, True,
              "Voted YES (one of 29-13 Senate majority) on SB 62 (April 2025), restoring and expanding SC's Education Scholarship Trust Fund for private school and homeschool choice after the SC Supreme Court struck down the prior version. Also co-sponsored H.3011 (Parental Rights in Education Act, 2025) giving parents legal standing to direct their children's education, health care, and upbringing, and co-sponsored H.3118 (Parental Bill of Rights, 2025).",
              ["https://palmettopromise.org/house-and-senate-reach-school-choice-agreement-in-magic-amendment/",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/62.htm",
               "https://www.scstatehouse.gov/sess126_2025-2026/bills/3011.htm"]),
    ]),

    # ---------------- Greg Hembree (SC-R, State Senator District 28) ----------------
    ("greg-hembree", "SC", "Senator", [
        claim("gh1", "greg-hembree", "sanctity_of_life", 0, True,
              "Co-sponsored SC Senate Bill 1, the 'SC Fetal Heartbeat and Protection from Abortion Act' in 2021, which passed the Senate 30-13 and was signed into law February 18, 2021. A longtime pro-life legislator who has stated he has debated abortion '11 of his 13 years' in the SC Senate chamber.",
              ["https://www.scstatehouse.gov/sess124_2021-2022/bills/1.htm",
               "https://www.wmbfnews.com/2023/05/08/sc-lawmakers-still-havent-agreed-abortion-would-they-let-voters-decide/"]),
        claim("gh2", "greg-hembree", "self_defense", 0, True,
              "Voted YES on SC's Constitutional Carry Act (H.3594) when the Senate passed it 28-15 in February 2024. Stated his reasoning: 'I think this fear that's always up in this debate, the facts don't back it up. I've changed my position, I've come to believe this is just not the big problem.' Bill was signed into law March 7, 2024 by Governor McMaster.",
              ["https://scdailygazette.com/2024/02/02/sc-senate-approves-permit-less-carry-with-a-training-incentive-twist/",
               "https://www.live5news.com/2024/03/07/mcmaster-signs-constitutional-carry-bill/"]),
        claim("gh3", "greg-hembree", "family_child_sovereignty", 0, True,
              "As Senate Education Committee Chairman, authored the Academic Choice in Education (ACE) Act enabling nonprofit scholarship organizations to fund private school and homeschool tuition, and authored SB 62 (2025) to restore school choice after the SC Supreme Court struck down the Education Scholarship Trust Fund in September 2024. His quote: 'Senate Bill 62 puts students and their parents back in the driver's seat and empowers them with choice in education.'",
              ["https://www.federationforchildren.org/afc-congratulates-south-carolinas-senate-on-passing-historic-school-choice-bill/",
               "https://readlion.com/south-carolina-senate-votes-to-restore-school-choice-house-likely-to-approve/"]),
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
