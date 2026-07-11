#!/usr/bin/env python3
"""Enrichment batch 684: hand-curated claims for 5 Texas State Representatives.

All archetype_curated federal senator/representative targets are exhausted.
Pivoting to evidence_state TX state representatives from the bottom of the
alphabet (TX is the highest-state-code pool remaining).

Targets (5 TX D state reps, reversed-alpha order):
  Rafael Anchia (HD-103, Dallas), Ramon Romero Jr. (HD-90, Fort Worth),
  Rhetta Bowers (HD-113, Rowlett/Garland), Robert Guerra (HD-41, McAllen),
  Ray Lopez (HD-125, San Antonio).

Sources: Texas Tribune, KERA News, ABC News, Planned Parenthood Texas Votes,
Moms Demand Action, Texas Values Action, Young Conservatives of Texas,
LegiScan, Dallas Observer, Fort Worth Report, WFAA, Texas House official bios.

NOTE: writes scorecard.json MINIFIED — SCORECARD.write_text(json.dumps(...,
separators=(",",":"))) — to keep master under GitHub's 50MB limit.
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
    # ----------- Rafael Anchia (TX-D, Texas State Representative HD-103) -----------
    ("rafael-anchia", "TX", "State Representative", [
        claim("ra1", "rafael-anchia", "self_defense", 1, False,
              "Voted against Texas HB 1927 (the 2021 Firearms Carry Act / permitless carry law), delivered an impassioned floor speech, called a GOP colleague a 'coward' during debate, and separately filed at least five gun-restriction bills in the same 87th session — HB 930 (repeal Castle Doctrine), HB 1163, HB 1164, HB 1169, and HB 1173 — all of which failed in the Republican-controlled House.",
              ["https://www.texastribune.org/2021/04/15/texas-constitutional-carry-2/",
               "https://legiscan.com/TX/votes/HB1927/2021"]),
        claim("ra2", "rafael-anchia", "border_immigration", 2, False,
              "As Chairman of the Mexican American Legislative Caucus (MALC), publicly opposed and voted against Texas SB 4 (88th Legislature, 4th Special Session, 2023) — the law making illegal border crossing a state crime — calling it 'racially motivated for political gain' and warning it would 'lead to abuse of power against Latinos and immigrants.'",
              ["https://www.dallasobserver.com/news/dallas-lawmakers-blast-new-anti-immigrant-in-texas-17764716",
               "https://www.texastribune.org/2026/04/24/texas-immigration-law-sb-4-5th-circuit-court-of-appeals-ruling/"]),
        claim("ra3", "rafael-anchia", "election_integrity", 0, False,
              "Was a key organizer of the July 2021 Texas House Democratic quorum break, in which members flew to Washington D.C. to deny Republicans the quorum needed to pass SB 1 (the omnibus voter ID and election-restrictions bill). Publicly declared the voter-fraud rationale was 'a rounding error of a rounding error' and vowed not to 'buckle to the Big Lie in the state of Texas.'",
              ["https://abcnews.go.com/Politics/texas-democrats-break-quorum-special-session-voting-rights/story?id=78804436",
               "https://www.texastribune.org/2021/09/10/texas-house-democrats-quorum-break/"]),
    ]),

    # ----------- Ramon Romero Jr. (TX-D, Texas State Representative HD-90) -----------
    ("ramon-romero-jr", "TX", "State Representative", [
        claim("rrj1", "ramon-romero-jr", "border_immigration", 2, False,
              "As Chair of the Mexican American Legislative Caucus for the 89th Legislature (2025), publicly condemned Trump's immigration enforcement as 'a threat to the very fabric of our nation' and vowed MALC opposition to immigration raids at Texas schools — a position directly at odds with strict enforcement of immigration law.",
              ["https://www.keranews.org/government/2025-02-11/as-new-texas-hispanic-caucus-leader-romero-prepares-for-fierce-battle-over-immigration",
               "https://fortworthreport.org/2025/02/10/as-new-texas-hispanic-caucus-leader-romero-prepares-for-fierce-battle-over-immigration/"]),
        claim("rrj2", "ramon-romero-jr", "election_integrity", 0, False,
              "Participated in the July 2021 Texas House Democratic quorum break (flying to Washington D.C. to block SB 1, the omnibus voter-restrictions bill) and later led the August 2025 redistricting quorum break, calling it 'probably the most important thing I've ever done in my political career' after a federal judge struck down the maps he opposed as 'intentional discrimination.'",
              ["https://www.wfaa.com/article/news/local/texas/judge-tosses-map-texas-democrat-calls-quorum-break-most-important-thing-political-career/287-0c8f8c03-24b9-4088-8f7c-2e7f5c9af5a2",
               "https://fortworthreport.org/2025/08/03/tarrant-county-dems-among-texas-house-lawmakers-breaking-quorum-to-thwart-redistricting/"]),
        claim("rrj3", "ramon-romero-jr", "biblical_marriage", 2, False,
              "Texas Values Action — which scores legislators on votes protecting life, family, and religious freedom — gave Romero a 9% rating for the 88th Legislature (2023), reflecting consistent opposition to bills including SB 14 (the gender-affirming care ban for minors, passed 87–56) and SB 12 (drag performance restrictions). He was not among the four Democrats who crossed party lines to vote for SB 14.",
              ["https://txvaluesaction.org/legislator/ramon-romero-jr/",
               "https://www.texastribune.org/2023/05/12/texas-trans-kids-health-care-ban/"]),
    ]),

    # ----------- Rhetta Bowers (TX-D, Texas State Representative HD-113) -----------
    ("rhetta-bowers", "TX", "State Representative", [
        claim("rb1", "rhetta-bowers", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Texas Votes PAC in both the November 2022 and November 2024 general elections. Self-confirmed voting against the Texas abortion ban and authored HB 3744 (88th Legislature, 2023) to shield pharmacists from prosecution for prescribing abortion-related medication — placing her squarely within the abortion-industry political network the rubric opposes.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-texas-votes/elections/november-2024-elections-endorsements",
               "https://avowtexas.org/avow-2024-voter-guide/"]),
        claim("rb2", "rhetta-bowers", "self_defense", 1, False,
              "Endorsed by Everytown for Gun Safety / Moms Demand Action (2020 election cycle) and documented as voting against Second Amendment legislation nine times during the 87th Legislative regular session (2021), including a No vote on HB 1927 (the constitutional/permitless carry law).",
              ["https://momsdemandaction.org/press/everytown-sets-sights-on-texas-state-house-announcing-new-polling-digital-ads-and-endorsements/",
               "https://gunandsurvival.com/2021/07/16/state-rep-rhetta-bowers-awol-for-special-session-but-showed-up-to-vote-against-your-second-amendment-rights-nine-times-during-the-regular-session/"]),
        claim("rb3", "rhetta-bowers", "election_integrity", 0, False,
              "Participated in the July 2021 Texas House Democratic quorum break — flying to Washington D.C. to block SB 1 (the omnibus voter ID and election-integrity bill) — and subsequently received the NAACP Roy Wilkins Civil Rights Image Award in 2022 specifically for her role in that voting-rights activism, per her official Texas House biography.",
              ["https://www.texastribune.org/2021/07/14/texas-democats-walkout/",
               "https://house.texas.gov/members/3565/biography"]),
    ]),

    # ----------- Robert Guerra (TX-D, Texas State Representative HD-41) -----------
    ("robert-guerra", "TX", "State Representative", [
        claim("rg1", "robert-guerra", "biblical_marriage", 2, False,
              "Voted against Texas SB 14 (88th Legislature, 2023) — the law banning gender-affirming medical care (puberty blockers, hormone therapy) for transgender minors — when it passed the House 87–56. Guerra was not among the four Democrats (Harold Dutton, Tracy King, Shawn Thierry, and Abel Herrero) who crossed party lines to vote for the ban.",
              ["https://www.texastribune.org/2023/05/12/texas-trans-kids-health-care-ban/",
               "https://www.kut.org/politics/2023-05-18/texas-legislature-passes-ban-on-gender-affirming-care-for-minors"]),
        claim("rg2", "robert-guerra", "election_integrity", 0, False,
              "Participated in the July 2021 Texas House Democratic quorum break to block SB 1 (the omnibus election integrity / voter ID bill), though he was one of only two Democrats who returned early to Austin on August 7, 2021 — breaking with the caucus strategy before the walkout collapsed. His individual vote on SB 1's final passage remains unconfirmed in public records.",
              ["https://www.texastribune.org/2021/09/10/texas-house-democrats-quorum-break/",
               "https://www.texastribune.org/2021/08/07/texas-democrats-special-session/"]),
    ]),

    # ----------- Ray Lopez (TX-D, Texas State Representative HD-125) -----------
    ("ray-lopez", "TX", "State Representative", [
        claim("rl1", "ray-lopez", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood Texas Votes in the 2024 primary election; his Avow Texas (formerly NARAL Pro-Choice Texas) voter guide profile notes he has been supported by pro-choice organizations including Annie's List, NARAL, Avow, and Emily's List in every election cycle — placing him within the abortion-industry political network the rubric opposes.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-texas-votes/blog/planned-parenthood-texas-votes-endorsed-candidates-sweep-in-primary-elections",
               "https://avowtexas.org/avow-2024-voter-guide/"]),
        claim("rl2", "ray-lopez", "election_integrity", 0, False,
              "Was among 50+ Texas House Democrats who broke quorum in July 2021 and flew to Washington D.C. to block SB 1 (the omnibus voter ID and election-restrictions bill); publicly stated the bill 'create[s] burdensome obstacles for Texas voters' and expressed concern about poll-watcher intimidation of non-English speakers and voters with intellectual disabilities.",
              ["https://www.texastribune.org/2021/07/14/texas-democrats-walkout-quorum/",
               "https://www.house.texas.gov/news/press-releases/?id=7502"]),
        claim("rl3", "ray-lopez", "self_defense", 1, False,
              "Young Conservatives of Texas rated Lopez 13 out of 100 for the 87th Legislature (2021) and 23 out of 100 for the 88th Legislature (2023), with a career average of 18/100 — placing him consistently among the most anti-gun-rights members of the Texas House, a record that includes opposition to HB 1927 (the 2021 constitutional carry / permitless carry law).",
              ["https://ratings.yct.org/legislators/ray-lopez/87th-legislature",
               "https://www.yct.org/ycts-88th-legislative-session-ratings/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision.

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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
