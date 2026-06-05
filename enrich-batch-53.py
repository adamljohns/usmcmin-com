#!/usr/bin/env python3
"""Enrichment batch 53: 5 archetype_curated federal candidates with 0 claims.

Targets pulled from the BOTTOM of the alphabet bucket (OH, KS, IL states).
Mix: Alea Nadeem (OH-09 R), Anthony Campbell (OH-09 R), Prasanth Reddy
(KS-03 R), Robert Crandall (IL Senate R), Joshua Loyd (IL-13 R).
Sources: iVoterGuide, Ohio Capital Journal debate 2026-04-20, KCUR 2024
debate, KSN News, IPM Newsroom / WCIA, Ballotpedia IL R primary 2026.
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
    # ---------- Alea Nadeem (OH-09 R, Air Force Lt. Col.) ----------
    ("alea-nadeem", "OH", "representative", [
        claim("an1", "alea-nadeem", "sanctity_of_life", 0, True,
              "Publicly supported the Ohio Heartbeat Bill and holds a consistent pro-life record from her Ohio House service; named one of the top 10 'Arch Conservatives' by the Columbus Dispatch in 2013 partly on the strength of her anti-abortion votes.",
              ["https://ivoterguide.com/candidate?elecK=400&raceK=2190&primarypartyk=R&canK=4002",
               "https://ballotpedia.org/Alea_Nadeem"]),
        claim("an2", "alea-nadeem", "self_defense", 0, True,
              "Holds a pro-Second Amendment record from Ohio House service; iVoterGuide 2026 profile rates her as supportive of constitutional carry and gun rights.",
              ["https://ivoterguide.com/candidate?elecK=400&raceK=2190&primarypartyk=R&canK=4002",
               "https://ballotpedia.org/Alea_Nadeem"]),
        claim("an3", "alea-nadeem", "border_immigration", 2, True,
              "As an Ohio state representative, voted against issuing drivers licenses to illegal immigrants and opposed using Ohio taxpayer dollars for college tuition subsidies for illegal immigrants — opposing state-level sanctuary benefits.",
              ["https://ivoterguide.com/candidate?elecK=400&raceK=2190&primarypartyk=R&canK=4002"]),
    ]),

    # ---------- Anthony Campbell (OH-09 R, healthcare data exec) ----------
    ("anthony-campbell-oh-09", "OH", "representative", [
        claim("ac1", "anthony-campbell-oh-09", "foreign_policy_restraint", 0, True,
              "At the April 2026 OH-09 Republican primary debate, stated: 'The constitution is abundantly clear — it's the sole duty of Congress to debate and declare war, while the President must be able to rapidly respond to immediate attacks.' Explicitly opposed endless undeclared wars.",
              ["https://ohiocapitaljournal.com/2026/04/20/all-five-republican-candidates-running-for-ohios-9th-congressional-district-debate-before-primary/"]),
        claim("ac2", "anthony-campbell-oh-09", "biblical_marriage", 2, True,
              "At the April 2026 OH-09 primary debate, joined all Republican candidates in opposing transgender athletes competing in women's sports — consistent with rejecting transgender ideology in athletics policy.",
              ["https://ohiocapitaljournal.com/2026/04/20/all-five-republican-candidates-running-for-ohios-9th-congressional-district-debate-before-primary/"]),
        claim("ac3", "anthony-campbell-oh-09", "border_immigration", 1, True,
              "At the April 2026 OH-09 primary debate, stated Congress does not need an amnesty bill for illegal immigrants — opposing any legislative pathway to amnesty.",
              ["https://ohiocapitaljournal.com/2026/04/20/all-five-republican-candidates-running-for-ohios-9th-congressional-district-debate-before-primary/"]),
    ]),

    # ---------- Prasanth Reddy (KS-03 R, oncologist) ----------
    ("prasanth-reddy", "KS", "representative", [
        claim("pr1", "prasanth-reddy", "sanctity_of_life", 0, False,
              "Describes himself as 'personally pro-life' but publicly stated any abortion restrictions must include exceptions for rape, incest, danger to the health of the mother, and fetal abnormalities — falling short of an unconditional life-at-conception personhood position.",
              ["https://www.kcur.org/politics-elections-and-government/2024-10-25/sharice-davids-prasanth-reddy-kansas-us-house-3rd-district-debate",
               "https://kansasreflector.com/2024/10/18/kansas-congressional-rivals-sharice-davids-prasanth-reddy-elevate-feud-on-abortion-rights/"]),
        claim("pr2", "prasanth-reddy", "border_immigration", 0, True,
              "Calls the southern border situation 'an economic, public health, and national security crisis' and pledged it would be his top priority in Congress; as a legal immigrant himself, says 'if you can't secure the border, you can't secure the American Dream.'",
              ["https://www.ksn.com/news/your-local-election-hq/candidates/prasanth-reddy-republican-for-us-house-district-3/",
               "https://www.kcur.org/politics-elections-and-government/2024-10-25/sharice-davids-prasanth-reddy-kansas-us-house-3rd-district-debate"]),
        claim("pr3", "prasanth-reddy", "self_defense", 0, True,
              "Supports Second Amendment gun rights; contrasted with opponent Sharice Davids on firearms policy in their October 2024 debate, backing gun rights against Democratic calls for stricter gun control.",
              ["https://www.kcur.org/politics-elections-and-government/2024-10-25/sharice-davids-prasanth-reddy-kansas-us-house-3rd-district-debate"]),
    ]),

    # ---------- Robert Crandall (IL Senate R, businessman) ----------
    ("robert-crandall-il-senate", "IL", "senate", [
        claim("rc1", "robert-crandall-il-senate", "border_immigration", 3, True,
              "Advocates for an 'Americans First native-born labor sourcing pipeline' that mandates American workers be prioritized in hiring before any immigrant labor is considered — a policy equivalent to mandatory E-Verify enforcement — and treats immigration as a workforce 'last resort' only.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Illinois,_2026_(March_17_Republican_primary)"]),
        claim("rc2", "robert-crandall-il-senate", "economic_stewardship", 4, True,
              "Campaigns on reversing 40 years of globalist economic policy by restoring the 50,000 factories and 8 million jobs exported overseas, framing the re-industrialization of America as an explicit rejection of the WEF/Davos offshore-everything economic model.",
              ["https://ballotpedia.org/United_States_Senate_election_in_Illinois,_2026_(March_17_Republican_primary)"]),
    ]),

    # ---------- Joshua Loyd (IL-13 R, Army veteran / businessman) ----------
    ("joshua-loyd", "IL", "representative", [
        claim("jl1", "joshua-loyd", "border_immigration", 0, True,
              "Stated he wants to tighten immigration policies along the southern border as a core campaign priority in the Illinois 13th Congressional District 2026 race.",
              ["https://ipmnewsroom.org/meet-joshua-loyd-and-jeff-wilson-the-republican-candidates-for-illinois-13th-congressional-district/",
               "https://www.wcia.com/news/your-local-election-hq/two-republican-candidates-pushing-for-spot-in-illinois-13th-congressional-district/"]),
        claim("jl2", "joshua-loyd", "foreign_policy_restraint", 0, False,
              "Expressed support for the United States' current involvement in Middle East conflicts — a hawkish posture that does not require a formal Article I Congressional declaration of war.",
              ["https://ipmnewsroom.org/meet-joshua-loyd-and-jeff-wilson-the-republican-candidates-for-illinois-13th-congressional-district/"]),
        claim("jl3", "joshua-loyd", "industry_capture", 0, True,
              "Stated the ACA creates 'artificial inflation' in healthcare costs and advocates for market-based reform that allows free-market competition to drive down premiums — opposing the federal mandate structure underlying ACA's government-industry entanglement.",
              ["https://ipmnewsroom.org/meet-joshua-loyd-and-jeff-wilson-the-republican-candidates-for-illinois-13th-congressional-district/"]),
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
