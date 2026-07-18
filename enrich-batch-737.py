#!/usr/bin/env python3
"""Enrichment batch 737: 3 federal candidates from bottom of alphabet (VA, SC, TN), 6 claims.

archetype_curated bucket exhausted; targets drawn from evidence_curated VA/SC/TN
candidates with 3 existing claims — fills distinct rubric-category gaps.
Bottom-of-alpha states (VA, SC, TN) per collision-avoidance protocol.

Targets:
  Tara Durant         (VA-07, R, state senator — suspended congressional bid May 2026)
  Mac Deford          (SC-01, D, 2026 D candidate — LOST June 23 runoff to Nancy Lacore)
  Joshua Sales        (TN-07, D, 2026 D primary candidate — Aug 6 primary)

Key sourced positions:
  Durant — voted YES on HJR3 (Jan 16, 2026) to repeal VA's one-man-one-woman
    constitutional marriage provision, one of 4 Republicans to cross party lines
    in the 26-13 Senate vote; campaign called for a Balanced Budget Amendment
    and pledged to "build the wall, end taxpayer-funded benefits for illegal
    immigrants" (taradurant.com).
  Deford — Post and Courier 2024 profile: "I don't think it's the government's
    role in our society to tell somebody who they are, who they should love";
    platform supports expanding ACA/Medicare/Medicaid and opposes spending cuts.
  Sales — campaign "The Sales Plan" proposes universal government healthcare
    ($50/mo replacing $600-$1,200 private premiums) funded by progressive
    taxation; lifts payroll cap to extend Social Security 75 years.
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


TARGETS = [
    # ------- Tara Durant (VA, R, State Senator SD-27 / suspended VA-07 congressional bid) -------
    ("tara-durant", "VA", "Senator", [
        claim("td3", "tara-durant", "biblical_marriage", 0, False,
              "On January 16, 2026, Durant voted YES on HJR3 in the Virginia Senate — a "
              "joint resolution placing a constitutional amendment on the November 2026 "
              "ballot that would repeal Virginia's existing constitutional provision "
              "defining marriage as solely the union of one man and one woman, replacing "
              "it with language recognizing marriages 'without regard to sex, gender, or "
              "race.' The Senate passed the measure 26-13; Durant was one of exactly four "
              "Republicans who crossed party lines to vote yes alongside Democrats, while "
              "the rest of the Republican caucus voted no. No public statement by Durant "
              "explaining her vote appeared in any indexed news source. Her yes vote is the "
              "operative record: she voted to remove Virginia's constitutional recognition "
              "of one-man-one-woman marriage from state law — the opposite of the rubric's "
              "standard.",
              ["https://en.wikipedia.org/wiki/2026_Virginia_Repeal_Same-Sex_Marriage_Ban_Amendment",
               "https://www.vpm.org/generalassembly/2026-01-16/senate-amendments-abortion-voting-rights-marriage-gerrymandering",
               "https://news.ballotpedia.org/2026/01/21/virginia-general-assembly-places-constitutional-amendments-on-same-sex-marriage-abortion-voting-rights-following-criminal-convictions-on-the-nov-2026-ballot/",
               "https://lis.virginia.gov/vote-details/HJ3/20261/2619794"]),
        claim("td4", "tara-durant", "economic_stewardship", 2, True,
              "Durant's 2025-2026 congressional campaign (she suspended the bid May 22, "
              "2026) explicitly committed to a Balanced Budget Amendment as a named "
              "federal legislative priority. Her campaign website (taradurant.com/meet-tara/) "
              "stated she would 'fight for pro-growth, America-first policies — including a "
              "Balanced Budget Amendment, permanent Trump tax cuts for American families, and "
              "ending taxes on tips, overtime, and Social Security.' Her June 18, 2025 launch "
              "statement, carried by Potomac Local, said: 'Now I'm running for Congress to take "
              "that same fight to Washington and work with President Trump to secure our border, "
              "fully fund our police, end the reckless spending, and restore common-sense "
              "leadership.' Her X announcement described partnering with Gov. Youngkin 'to cut "
              "taxes, back the blue, and grow our economy.' A named Balanced Budget Amendment "
              "commitment is the clearest possible alignment with the rubric's anti-deficit "
              "standard.",
              ["https://taradurant.com/meet-tara/",
               "https://www.potomaclocal.com/2025/06/20/tara-durant-launches-bid-to-unseat-eugene-vindman-in-virginias-7th-district/",
               "https://x.com/TaraDurantVA/status/1935305846767940020"]),
        claim("td5", "tara-durant", "border_immigration", 0, True,
              "Durant's congressional campaign website (taradurant.com/issues/) stated "
              "she would 'fight to keep poison out of our communities, build the wall, and "
              "end taxpayer-funded benefits for illegal immigrants,' and that 'Tara knows "
              "open borders bring crime, trafficking, and deadly drugs like fentanyl.' Her "
              "June 2025 campaign launch included a pledge to 'work with President Trump to "
              "secure our border, balance the budget, and put America first,' covered in the "
              "Fredericksburg Free Press and Potomac Local. The explicit border-wall pledge "
              "combined with ending taxpayer subsidies for illegal immigrants and invoking "
              "Trump's full border agenda places her squarely within the rubric's wall-and-"
              "enforcement standard.",
              ["https://taradurant.com/issues/",
               "https://www.fredericksburgfreepress.com/2025/06/19/state-sen-tara-durant-announces-her-intention-to-run-for-congress/",
               "https://www.potomaclocal.com/2025/06/20/tara-durant-launches-bid-to-unseat-eugene-vindman-in-virginias-7th-district/"]),
    ]),

    # ------- Mac Deford (SC-01, D, LOST June 23 runoff to Nancy Lacore 52-48) -------
    ("mac-deford", "SC", "Representative", [
        claim("md3", "mac-deford", "biblical_marriage", 0, False,
              "In a Post and Courier 'Meet the Candidates' profile (2024 cycle, same district "
              "and candidate), Deford stated: 'I believe in respecting the dignity of the "
              "individual. That means that I don't think it's the government's role in our "
              "society to tell somebody who they are, who they should love. That identity is "
              "unique to every individual.' He offered a mild softening on transgender athletes "
              "('there's room to discuss bathroom access and the role of transgender athletes "
              "in women's sports') but made no statement supporting government restriction on "
              "same-sex relationships. His framing — government has no role in defining who "
              "someone loves — is a direct rejection of the state's authority to recognize only "
              "one-man-one-woman unions, placing him against the rubric's biblical marriage "
              "standard.",
              ["https://www.postandcourier.com/moultrie-news/news/meet-the-candidates-mac-deford/article_38567654-0e0c-11ef-a1cd-03375193db09.html",
               "https://ballotpedia.org/Mac_Deford"]),
        claim("md4", "mac-deford", "economic_stewardship", 2, False,
              "Deford's 2026 campaign platform explicitly opposed cuts to Social Security, "
              "Medicare, and Medicaid; called for strengthening the ACA; supported Medicare "
              "negotiating prescription drug prices; and framed economic policy as: 'A revenue "
              "system should lift people up, not make life more expensive. My priority would be "
              "to craft revenue policy that strengthens the economy, supports families, and "
              "reflects responsible stewardship of public funds.' He also described tariffs as "
              "'reckless' and likened them to 'a hidden tax on working people.' In an ABC "
              "News4 profile, he prioritized 'lowering costs and restoring economic sanity' "
              "through program expansion rather than deficit reduction. This expansionary "
              "entitlement posture — protect and expand existing federal health and retirement "
              "programs, oppose spending restraint — directly opposes the rubric's "
              "anti-deficit/balanced-budget standard.",
              ["https://ballotpedia.org/Mac_Deford",
               "https://abcnews4.com/news/local/coast-guard-veteran-mac-deford-prioritizes-constituent-access-and-transparency-in-2026-run-south-carolina-1st-congressional-district-wciv-abc-news-4-10-2-2025"]),
    ]),

    # ------- Joshua Sales (TN-07, D, 2026 D primary candidate — Aug 6, 2026 primary) -------
    ("joshua-sales", "TN", "Representative", [
        claim("js4", "joshua-sales", "economic_stewardship", 2, False,
              "Sales's campaign platform ('The Sales Plan,' sales4congress.com) proposes a "
              "universal government-run healthcare system funded by a new progressive 'healthcare "
              "contribution' tax, replacing private insurance premiums — described as '$50/month "
              "for full coverage' replacing the current median '$600-$1,200 a month for coverage "
              "they're afraid to use.' He also supports lifting the Social Security payroll tax "
              "cap to generate approximately $401 billion per year to extend Social Security "
              "solvency for 75 years, framing it as closing 'a loophole' rather than a tax "
              "increase: 'Social Security is solvent for 75 years if everyone pays their share.' "
              "His macro-framing — 'Not Republican vs. Democrat. Billionaire vs. Working Class' "
              "— positions all of his proposals as redistributing from corporations and billionaires "
              "to working families, with 'none raise taxes on working families.' The creation of "
              "a new federal universal healthcare entitlement plus expanded Social Security "
              "spending funded by progressive taxation directly opposes the rubric's "
              "anti-deficit/balanced-budget standard, which rewards candidates who reduce the "
              "size and spending of the federal government.",
              ["https://sales4congress.com/the-sales-plan/",
               "https://sales4congress.com/platform/",
               "https://ballotpedia.org/Joshua_Sales"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~42MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
