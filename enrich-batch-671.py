#!/usr/bin/env python3
"""Enrichment batch 671: 5 TX Republican state officials — evidence_state → evidence_curated.

All five took office in 2023 or 2025 and therefore have NO votes on the 2021
landmark bills (SB 8 Heartbeat Act, HB 1927 Constitutional Carry, SB 1 Election
Integrity). Claims draw from their 88th/89th Legislature records, campaign-era
iVoterGuide questionnaires, and verified scorecard ratings.

Targets:
  Angelia Orr     (HD-13, Hillsboro area — took office Jan 2023)
  Andy Hopper     (HD-64, Wise/Denton counties — took office Jan 2025)
  Alan Schoolcraft (HD-44, Guadalupe/Gonzales counties — took office Jan 2025)
  Alan Blaylock   (HD-93 2026 R nominee, Fort Worth area — not yet in office)
  A.J. Louderback (HD-30, Gulf Coast six-county district — took office Jan 2025)
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
    # ---- Angelia Orr (TX, HD-13, Hill/Bosque/Falls/Limestone area) ----
    # First elected Nov 2022; sworn in Jan 10, 2023 (88th Legislature).
    # Did NOT serve during 87th Legislature — no SB 8, HB 1927, or SB 1 vote possible.
    ("angelia-orr", "TX", "Representative", [
        claim("ao1", "angelia-orr", "sanctity_of_life", 0, True,
              "Scored 96% on the Texas Alliance for Life 2025 Legislative Scorecard "
              "(89th Legislature), one of the highest ratings in the Texas House, "
              "reflecting consistent support for every major pro-life bill that session. "
              "Her 2022 iVoterGuide survey states: 'I am pro Life — and saving a life is "
              "saving a life,' and she identifies abortion as permissible only 'by the "
              "determination of her licensed medical doctor' when a mother's life is at risk. "
              "She also affirmed that abortion providers including Planned Parenthood should "
              "not receive taxpayer funding at any level of government.",
              ["https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ivoterguide.com/candidate/60263/race/15113/election/943",
               "https://ballotpedia.org/Angelia_Orr"]),
        claim("ao2", "angelia-orr", "family_child_sovereignty", 0, True,
              "Co-authored HB 3225 (89th Legislature, 2025), which requires municipal "
              "public libraries to move sexually explicit materials out of children's sections "
              "and prohibits minors from checking out such materials without explicit parental "
              "permission. The bill passed the Texas House 93-37 on May 9, 2025. Orr posted "
              "about it on her official website under the heading 'The Fight for Our Kids "
              "Isn't Over,' stating parents deserve the right to protect their children from "
              "inappropriate library content.",
              ["https://www.angeliaorr.com/post/the-fight-for-our-kids-isn-t-over",
               "https://www.texastribune.org/2025/05/09/texas-house-children-library-explicit-material/",
               "https://ballotpedia.org/Angelia_Orr"]),
        claim("ao3", "angelia-orr", "self_defense", 1, True,
              "In her 2022 iVoterGuide questionnaire, Orr stated: 'The Second Amendment is "
              "designed to keep the government in check from tyranny against our people. "
              "There should never, under any circumstances be any modification to the "
              "2nd amendment, NO red flag gun proposals or ANY idea that infringes or treads "
              "on the rights of citizens.' This categorical opposition to red-flag laws and "
              "all new firearm restrictions reflects the rubric's anti-red-flag position.",
              ["https://ivoterguide.com/candidate/60263/race/15113/election/943",
               "https://ballotpedia.org/Angelia_Orr"]),
    ]),

    # ---- Andy Hopper (TX, HD-64, Wise County/southern Denton County) ----
    # First elected Nov 2024; sworn in Jan 14, 2025 (89th Legislature).
    # Did NOT serve during 87th Legislature — no 2021-era votes possible.
    # Software engineer/defense industry veteran, TX State Guard Chief Warrant Officer.
    ("andy-hopper", "TX", "Representative", [
        claim("ah1", "andy-hopper", "sanctity_of_life", 1, True,
              "Signed the Abolish Abortion Texas Equal Protection Pledge, calling for "
              "total abolition of abortion rather than incremental regulation, and stated "
              "on his campaign website: 'Life begins at conception. Abortion is murder and "
              "must end in Texas.' He additionally stated: 'I believe that we should seize "
              "any opportunity that we have to end the practice of abortion, at whatever "
              "stage we can.' His 2025 legislative record reflects an 86% rating from both "
              "Texas Alliance for Life and Texas Right to Life (89th Legislature).",
              ["https://www.hopper4texas.com/platform/",
               "https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://texasrighttolife.com/pro-life-scorecards-and-highlights-89th-texas-legislature/"]),
        claim("ah2", "andy-hopper", "election_integrity", 0, True,
              "Ran on election integrity as a core platform plank, citing his software "
              "engineering background in national-defense systems: 'It is imperative that "
              "we move back to paper ballots that can be effectively recounted and protected.' "
              "In the 89th Legislature (2025) he authored a cluster of election-security bills "
              "— including HB 1001, HB 1002, HB 1004, HB 1007, HB 1009, and HB 1012 — each "
              "relating to the security of paper ballots and election record-keeping. He "
              "cited 'significant progress on Secure Texas Elections' in his end-of-session "
              "legislative-priority wrap-up.",
              ["https://www.hopper4texas.com/news/89th-legislative-priority-wrap-up/",
               "https://texasscorecard.com/state/meet-the-freshmen-andy-hopper/",
               "https://legiscan.com/TX/people/andy-hopper/id/25231"]),
        claim("ah3", "andy-hopper", "family_child_sovereignty", 0, True,
              "Voted YES on SB 12 (2025 'Parents Bill of Rights') — which bans Texas public "
              "schools from teaching sexual-orientation or gender-identity content PreK "
              "through 12th grade, requires parental consent for human sexuality instruction, "
              "and prohibits schools from helping students socially transition without parental "
              "knowledge. Also voted YES on SB 2 (2025 Education Savings Account program "
              "providing up to $10,900 per student annually for private school or homeschool "
              "expenses). Additionally co-authored HB 938 establishing civil liability for "
              "drag performers who perform lasciviously in the presence of minors.",
              ["https://legiscan.com/TX/bill/SB12/2025",
               "https://legiscan.com/TX/bill/SB2/2025",
               "https://www.kut.org/politics/2025-06-18/texas-legislator-andy-hopper-denton-representative-profile"]),
    ]),

    # ---- Alan Schoolcraft (TX, HD-44, Guadalupe/Gonzales counties) ----
    # First elected Nov 2024; sworn in Jan 14, 2025 (89th Legislature).
    # Attorney, Air Force veteran; previously served in Texas House 1981-1993.
    ("alan-schoolcraft", "TX", "Representative", [
        claim("as1", "alan-schoolcraft", "sanctity_of_life", 0, True,
              "Texas Right to Life PAC endorsed Schoolcraft with a 'bold Pro-Life leader' "
              "designation, citing his quote: 'Nothing is more important than protecting "
              "the lives of babies in the womb. God's sacred gift to us is life!' His "
              "iVoterGuide questionnaire states he is 'staunchly opposed to abortion and "
              "committed to upholding and promoting policies that protect the unborn,' and "
              "that abortion providers including Planned Parenthood should receive no taxpayer "
              "funds from any level of government. He scored 90% on the Texas Alliance for "
              "Life 89th Legislature (2025) scorecard.",
              ["https://www.texasrighttolifepac.com/elect-alan-schoolcraft-a-pro-life-leader/",
               "https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://ivoterguide.com/candidate/78072/race/6643/election/1214"]),
        claim("as2", "alan-schoolcraft", "self_defense", 0, True,
              "In campaign statements Schoolcraft declared: 'I am staunchly Pro-2nd "
              "Amendment! I take the \"shall not be infringed\" in the Constitution seriously,' "
              "and called for Texas to push back on ATF actions. He was endorsed by Gun "
              "Owners of America and Texas Gun Rights PAC in his 2024 campaign, both "
              "organizations that grade on absolute Second Amendment positions including "
              "constitutional carry and opposition to all new federal firearms regulations.",
              ["https://txgunrights.org/runoff-race-of-the-week-schoolcraft-vs-kuempel/",
               "https://texasscorecard.com/state/in-their-own-words-runoff-candidates-on-gun-rights/",
               "https://ballotpedia.org/Alan_Schoolcraft"]),
        claim("as3", "alan-schoolcraft", "family_child_sovereignty", 0, True,
              "Authored HB 117 (89th Legislature, 2025), establishing the Governor's Task "
              "Force on Governance of Early Childhood Education and Care to improve PreK "
              "standards and reduce bureaucratic fragmentation. Signed into law by Governor "
              "Abbott on June 20, 2025. Also authored HB 1279 — prohibiting Texas public "
              "schools from teaching 'hateful, divisive and discriminatory' ideological "
              "content based on race, sex, ethnicity, or religion — and HB 1280, banning "
              "DEI training mandates in governmental entities.",
              ["https://legiscan.com/TX/bill/HB117/2025",
               "https://gov.texas.gov/news/post/governor-abbott-launches-task-force-on-early-childhood-education-and-care",
               "https://house.texas.gov/members/4745/biography"]),
    ]),

    # ---- Alan Blaylock (TX, HD-93, Fort Worth / Tarrant County) ----
    # 2026 Republican nominee; NOT yet a sitting legislator.
    # Former Fort Worth City Council District 10 (since May 2023).
    # Won March 3, 2026 Republican primary with 87.4% of the vote.
    ("alan-blaylock", "TX", "District 93", [
        claim("ab1", "alan-blaylock", "sanctity_of_life", 0, True,
              "In his 2026 iVoterGuide candidate survey Blaylock stated: 'Elective abortion "
              "should never be allowed under any circumstances' and 'Life begins at conception, "
              "and every unborn child deserves full protection.' He indicated the Comstock Act "
              "(which bans interstate transportation of abortion-inducing drugs) should be "
              "enforced, and affirmed that abortion providers including Planned Parenthood "
              "should receive no government funding at any level. He additionally stated: "
              "'I am a devout Christian who believes in the Bible as the inspired Word of "
              "God...emphasizing personal responsibility, the sanctity of life, traditional "
              "family structures, and moral absolutes.'",
              ["https://ivoterguide.com/candidate/87281/race/23702/election/1343",
               "https://ballotpedia.org/Alan_Blaylock",
               "https://www.alanblaylock.com/"]),
        claim("ab2", "alan-blaylock", "family_child_sovereignty", 0, True,
              "Endorsed by the Texas Home School Coalition (THSC), which named him among 73 "
              "Texas House candidates in 2026 and stated he 'will be instrumental on matters "
              "of parental rights, education freedom, and limited government.' In his iVoterGuide "
              "survey he stated: 'Government should recognize and support the fundamental "
              "right and essential duty of parents to direct their child's health and "
              "educational well-being.' He also received the endorsement of For Liberty & "
              "Justice, Mercy Culture Church's political nonprofit, which focuses on Christian "
              "values in public policy.",
              ["https://thsc.org/2026-primary-results/",
               "https://ivoterguide.com/candidate/87281/race/23702/election/1343",
               "https://fortworthreport.org/2025/11/10/fort-worth-mercy-culture-trains-candidates-campaign-university/"]),
        claim("ab3", "alan-blaylock", "self_defense", 0, True,
              "In his 2026 iVoterGuide survey Blaylock stated: 'No restrictions on gun "
              "ownership are needed beyond basic background checks for felons and the "
              "mentally ill' and 'The Second Amendment guarantees the right to bear arms "
              "for self-defense.' He received the endorsement of Governor Greg Abbott, "
              "won the Republican primary with 87.4% of the vote against a challenger in "
              "a district that includes Fort Worth suburbs (Haslet, Saginaw, Keller, "
              "Lake Worth, Watauga).",
              ["https://ivoterguide.com/candidate/87281/race/23702/election/1343",
               "https://ballotpedia.org/Alan_Blaylock",
               "https://www.alanblaylock.com/"]),
    ]),

    # ---- A.J. Louderback (TX, HD-30, six-county Gulf Coast district) ----
    # First elected Nov 2024; sworn in Jan 14, 2025 (89th Legislature).
    # Jackson County Sheriff for five terms (40+ years in law enforcement, Air Force vet).
    # Founding member/Executive Director, Texas Regional Sheriff's Alliance.
    ("aj-louderback", "TX", "HD-30", [
        claim("ajl1", "aj-louderback", "border_immigration", 2, True,
              "As Jackson County Sheriff and founding director of the Texas Regional "
              "Sheriff's Alliance, Louderback was instrumental in expanding ICE's 287(g) "
              "immigration enforcement program to 16 Texas Gulf Coast counties. He testified "
              "before the U.S. House Judiciary Subcommittee on Immigration (February 15, 2018) "
              "that sanctuary city policies create 'a safe haven for criminality' and directly "
              "hamper law enforcement cooperation. In the 89th Legislature he co-sponsored a "
              "floor amendment strengthening SB 8 (2025) — the bill mandating that Texas "
              "county jails enter 287(g) ICE enforcement agreements — and spoke at the House "
              "podium in its support, drawing on his sheriff experience.",
              ["https://docs.house.gov/meetings/JU/JU01/20180215/106864/HHRG-115-JU01-Wstate-LouderbackA-20180215.pdf",
               "https://texaspolicyresearch.com/bills/89th-legislature-sb-8/",
               "https://ballotpedia.org/A.J._Louderback"]),
        claim("ajl2", "aj-louderback", "sanctity_of_life", 0, True,
              "Texas Right to Life PAC endorsed Louderback as '100% Pro-Life' and described "
              "him as 'disgusted by the vile, radical abortion policies...that allow for the "
              "barbaric mutilation and genocide of innocent infants up to birth,' adding that "
              "he 'will always defend the unborn.' He scored 93% on both the Texas Alliance "
              "for Life and Texas Right to Life 89th Legislature (2025) scorecards — the "
              "highest-tier rating for a freshman legislator.",
              ["https://www.texasrighttolifepac.com/coastal-bend-vote-aj-louderback/",
               "https://www.texasallianceforlife.org/89th-texas-lege-scorecard/",
               "https://texasrighttolife.com/pro-life-scorecards-and-highlights-89th-texas-legislature/"]),
        claim("ajl3", "aj-louderback", "self_defense", 0, True,
              "Authored HB 1487 (89th Legislature, 2025), which eliminates all License to "
              "Carry application, renewal, and related fees ($40 application, $40 renewal, "
              "$25 judicial-officer, $2 mental-health-check). The bill was signed into law "
              "effective September 1, 2025, making LTC permits free for all eligible Texans. "
              "NRA-ILA highlighted the bill. Louderback is a lifetime member of the NRA and "
              "Texas State Rifle Association, a licensed LTC instructor since 1995, and was "
              "endorsed by Gun Owners of America for his 2026 re-election campaign.",
              ["https://house.texas.gov/members/4620",
               "https://www.nraila.org/",
               "https://ballotpedia.org/A.J._Louderback"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
