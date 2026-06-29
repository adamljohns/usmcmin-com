#!/usr/bin/env python3
"""Enrichment batch 485: 5 Wisconsin State Assembly Republicans (archetype_party_default → evidence_curated).

Targets from the bottom of the alphabet (WI, archetype_party_default, 0 claims):
  Patrick Snyder (WI-85), Nancy VanderMeer (WI-70), Kevin Petersen (WI-57),
  John Spiros (WI-86), Lindee Brill (WI-27).

Sources: legis.wisconsin.gov, ballotpedia.org, docs.legis.wisconsin.gov,
  prolifewi.org, nrlc.org, wisbusiness.com, pbs.org, wsaw.com,
  wispolitics.com, wisconsinexaminer.com, wpr.org, americansforprosperity.org.
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
    # ------------- Patrick Snyder (WI-85, Marathon County / Wausau area) -------------
    ("patrick-snyder-wi-85", "WI", "Assembly", [
        claim("ps1", "patrick-snyder-wi-85", "sanctity_of_life", 0, True,
              "Co-authored SB 344 (2023), part of the 'Embrace Them Both' package, to extend Wisconsin's income-tax dependent exemption to preborn children whose fetal heartbeat has been detected — a legislative recognition of the humanity of the unborn before birth. Provided in-person testimony at the September 19, 2023 Senate Committee hearing in support, and the bill was championed by both Pro-Life Wisconsin and Wisconsin Family Action.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/sb344",
               "https://www.prolifewi.org/53023-prolife-wisconsin-supports-embrace-them-both-bill-package",
               "https://wifamilyaction.org/wisconsin-family-action-supports-embrace-them-both-bill-package/"]),
        claim("ps2", "patrick-snyder-wi-85", "election_integrity", 0, True,
              "Primary Assembly author of AJR 1 (2025), the constitutional amendment requiring photographic identification to vote in any Wisconsin election. Stated the bill would 'ensure that the people of Wisconsin have full confidence in the security and integrity of Wisconsin elections.' The Assembly passed it 54–45 (party-line) on January 14, 2025, and Wisconsin voters ratified it at the April 2025 election — voter ID is now embedded in the Wisconsin Constitution.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)"]),
        claim("ps3", "patrick-snyder-wi-85", "family_child_sovereignty", 0, True,
              "Voted YES on the Wisconsin Assembly 'Parental Bill of Rights' (January 2024, passed 62–35), establishing 16 enumerated parental rights including the right to determine a child's pronouns at school, opt out of classroom lessons conflicting with personal beliefs, and sue to enforce those rights. Also authored 2025 Wisconsin Act 48 ('Bradyn's Law') making sextortion of a minor a felony — further protecting children from predatory digital exploitation.",
              ["https://www.wsaw.com/2024/01/18/wisconsin-assembly-approves-bill-guaranteeing-parental-oversight-of-childrens-education/",
               "https://spectrumnews1.com/wi/milwaukee/news/2024/01/18/assembly-passes--parental-bill-of-rights-",
               "https://wisconsinexaminer.com/briefs/evers-signs-bills-that-make-sextortion-crime-extend-statute-of-limitations-for-hiding-a-corpse/"]),
    ]),

    # ------------- Nancy VanderMeer (WI-70, Monroe County / Tomah area) -------------
    ("nancy-vandermeer-wi-70", "WI", "Assembly", [
        claim("nv1", "nancy-vandermeer-wi-70", "election_integrity", 0, True,
              "Authored Wisconsin AB 570 (2023), an election integrity bill tightening absentee ballot certificate requirements, penalizing assistance in casting invalid ballots, and barring employees of political committees from serving as election officials. The bill passed the Republican-controlled legislature but was vetoed by Gov. Evers; the veto override failed May 15, 2024. VanderMeer is a consistent advocate for election security measures.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab570",
               "https://www.billtrack50.com/billdetail/1646206",
               "https://www.nancyforwisconsin.com/copy-of-legislation"]),
        claim("nv2", "nancy-vandermeer-wi-70", "sanctity_of_life", 0, True,
              "Voted YES on Wisconsin AB 975 (January 25, 2024, passed 53–46), the Assembly's most significant pro-life floor vote of the 2023–24 session, which would have banned abortion after 14 weeks postfertilization. VanderMeer is not among the 10 Republican dissenters, confirming her support for the restriction. She has maintained a consistent pro-life voting record across multiple sessions.",
              ["https://www.pbs.org/newshour/politics/wisconsin-republicans-approve-bill-banning-abortions-after-14-weeks-of-pregnancy",
               "https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://www.wispolitics.com/2024/divided-assembly-gop-passes-bill-to-put-14-week-abortion-ban-before-voters/"]),
        claim("nv3", "nancy-vandermeer-wi-70", "family_child_sovereignty", 0, True,
              "Named co-sponsor of Wisconsin AB 100 (2025), requiring public and private choice-program schools to designate athletic teams by biological sex at birth — protecting girls' sports from transgender competition. The Assembly passed it 51–43 on March 20, 2025. Also voted YES on the Parental Bill of Rights (January 2024, 62–35), enshrining 16 parental rights in Wisconsin law.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/reg/asm/bill/ab100",
               "https://wisconsinexaminer.com/2025/03/21/assembly-passes-bills-targeting-transgender-youth-in-school-and-their-medical-decisions/",
               "https://www.wsaw.com/2024/01/18/wisconsin-assembly-approves-bill-guaranteeing-parental-oversight-of-childrens-education/"]),
    ]),

    # ------------- Kevin Petersen (WI-57, Waupaca area) — Speaker Pro Tempore -------------
    ("kevin-petersen-wi-57", "WI", "Assembly", [
        claim("kp1", "kevin-petersen-wi-57", "election_integrity", 0, True,
              "Co-sponsored both of Wisconsin's landmark election integrity constitutional amendments: AJR 77 (2023, banning private 'Zuckerbucks' funding of elections, ratified by voters April 2, 2024) and AJR 1 (2025, requiring photographic voter ID, ratified by voters April 2025). Both are now permanently embedded in the Wisconsin Constitution. His campaign credits him with passing 'nearly two dozen election integrity reforms' during his career.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ajr77",
               "https://ballotpedia.org/Wisconsin_Question_1,_Ban_on_Private_and_Non-Governmental_Funding_of_Election_Administration_Amendment_(April_2024)",
               "https://docs.legis.wisconsin.gov/2025/proposals/ajr1"]),
        claim("kp2", "kevin-petersen-wi-57", "sanctity_of_life", 0, True,
              "Earned a 100% score from Wisconsin Family Action (2021–2022 scorecard) covering votes on life, marriage, family, and religious liberty. Co-introduced AB 1065 (2021, fetal heartbeat bill) and co-sponsored Born Alive legislation (AB 179) requiring medical care for infants surviving attempted abortion. A Catholic and NRA-member Navy veteran who describes himself as consistently pro-life.",
              ["https://wifamilyaction.org/wisconsin-family-action-releases-2021-2022-legislative-scorecard-2/",
               "https://docs.legis.wisconsin.gov/2021/related/proposals/ab1065",
               "https://docs.legis.wisconsin.gov/2019/related/proposals/ab179"]),
        claim("kp3", "kevin-petersen-wi-57", "economic_stewardship", 2, True,
              "As Assembly Speaker Pro Tempore (2023–2026) and 20-year Assembly Republican, Petersen highlights Wisconsin's fiscal turnaround as his signature accomplishment: from a $1.6 billion deficit and near-zero rainy-day fund when first elected in 2006 to a projected $2.5 billion surplus and a $2 billion rainy-day fund. Consistently earned the Wisconsin Manufacturers & Commerce 'Working for Wisconsin Award' for voting 96–100% in support of pro-growth, tax-cutting legislation.",
              ["https://legis.wisconsin.gov/assembly/57/petersen/about/",
               "https://www.wmc.org/press-releases/rep-kevin-petersen-awarded-for-job-creation-votes/",
               "https://www.wbay.com/2026/03/19/waupacas-kevin-petersen-not-running-re-election-assembly-after-20-years/"]),
    ]),

    # ------------- John Spiros (WI-86, Marshfield / Wood County area) -------------
    ("john-spiros-wi-86", "WI", "Assembly", [
        claim("js1", "john-spiros-wi-86", "sanctity_of_life", 0, True,
              "Named introducing co-sponsor of Wisconsin AB 975 (the 14-week abortion ban, January 2024, passed 53–46 in the Assembly). Also co-sponsored AB 6 (2021 Born Alive protection), AB 593 (2021 informed consent for abortion-inducing drugs), and AB 595 (2021 banning sex-selective abortions). Consistent multi-session pro-life sponsorship record as a Wisconsin Assembly member.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://ballotpedia.org/John_Spiros",
               "https://trackbill.com/legislator/wisconsin-representative-john-spiros/788-20976/"]),
        claim("js2", "john-spiros-wi-86", "election_integrity", 0, True,
              "Co-sponsored AJR 1 (2025), the constitutional amendment requiring photo ID to vote in any Wisconsin election, which Assembly passed 54–45 and voters ratified at the April 2025 election (61% in favor) — permanently enshrining voter ID in the Wisconsin Constitution. Also sponsored AB 595 (2025) requiring Help America Vote Act compliance and voter roll maintenance to remove ineligible voters.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ajr1",
               "https://www.wpr.org/news/april-2025-election-voter-id-requirement-passes-wisconsin-constitution",
               "https://wisconsinexaminer.com/2025/01/15/assembly-passes-voter-id-constitutional-amendment-proposal-now-it-goes-to-voters-in-april/"]),
        claim("js3", "john-spiros-wi-86", "self_defense", 1, True,
              "Chair of the Assembly Committee on Criminal Justice and Public Safety, overseeing all gun legislation in the Wisconsin Assembly. Sponsored AB 10 (2025, sales-tax exemption for gun safes, reducing costs for lawful gun owners) and earlier co-authored legislation allowing interstate long-gun purchases. Americans for Prosperity–Wisconsin endorsed Spiros multiple times, citing his consistent votes to 'lower taxes, cut red tape, and reform state government' including opposition to new firearms restrictions.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/reg/asm/bill/ab10",
               "https://americansforprosperity.org/press-release/americans-for-prosperity-backs-assemblyman-john-spiros/",
               "https://ballotpedia.org/John_Spiros"]),
    ]),

    # ------------- Lindee Brill (WI-27, Sheboygan County / Sheboygan Falls area) — new Jan 2025 -------------
    ("lindee-brill-wi-27", "WI", "Assembly", [
        claim("lb1", "lindee-brill-wi-27", "sanctity_of_life", 0, True,
              "Sponsored AB 382 (2025), Wisconsin's 'born alive' protection requiring physicians to provide the same standard of medical care to any infant surviving an attempted abortion as to any other newborn, treating the child as a patient with full legal protections. Also co-sponsored AB 407 (2025) requiring abortion providers to report the sex and any fetal anomaly of each aborted child to the state health department. Chairs the Speaker's Task Force on Protecting Kids and has stated she will 'infuse time-tested conservative philosophy and strong Christian values into my every action as an elected official.'",
              ["https://legis.wisconsin.gov/assembly/27/brill/",
               "https://ballotpedia.org/Lindee_Brill",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab407"]),
        claim("lb2", "lindee-brill-wi-27", "election_integrity", 0, True,
              "Primary Assembly author of AB 560 (2025), which would ban absentee ballot drop boxes statewide, requiring all absentee ballots to be returned by mail. Brill stated the bill is 'simple legislation to improve security for our elections and confidence from Wisconsin voters.' Co-authored with State Senator André Jacque; the bill received a public hearing before the Assembly Campaigns and Elections committee.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/reg/asm/bill/ab560",
               "https://www.wpr.org/news/gop-bill-ban-ballot-drop-boxes-wisconsin-intraparty-debate",
               "https://www.wispolitics.com/2025/rep-brill-stands-up-for-true-election-integrity/"]),
        claim("lb3", "lindee-brill-wi-27", "biblical_marriage", 2, True,
              "Co-sponsored AB 400 (2025) creating a civil cause of action allowing minors to sue health care providers who performed irreversible gender transition procedures on them. Also authored legislation introduced in January 2026 to prevent individuals from changing the biological sex on Wisconsin birth certificates, defining sex by chromosomes — a firm legislative rejection of transgender ideology as applied to children in law and medicine.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab400",
               "https://legis.wisconsin.gov/assembly/27/brill/",
               "https://ballotpedia.org/Lindee_Brill"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
