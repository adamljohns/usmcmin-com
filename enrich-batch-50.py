#!/usr/bin/env python3
"""Enrichment batch 50: 5 federal House candidates (3R/2D) from the bottom
of the archetype_curated bucket with 0 claims.

Targets (bottom-of-alphabet pick):
  Ed Gallrein    (KY-04  R) — Trump-backed Navy SEAL, defeated Massie
  Kandiss Taylor (GA-01  R) — "Jesus, Guns & Babies"; GA GOP district chair
  Cait Conley    (NY-17  D) — Army vet, ex-NSC/CISA; LGBTQ+ Victory Fund
  Jack Schlossberg(NY-12 D) — JFK grandson; NYC Democrat primary
  Bridget Brink  (MI-07  D) — former US Ambassador to Ukraine

Each claim cites ≥1 reliable public source and reflects 2024-2026
voting record / public positions. Minified write preserves the ~35-36 MB
master (no indent=2 — see enrich-batch-4.py docstring).
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
    # ---------- Ed Gallrein (KY-04 R) ----------
    ("ed-gallrein", "KY", "Representative", [
        claim("eg1", "ed-gallrein", "sanctity_of_life", 0, True,
              "Recommended by Kentucky Right to Life (2026 PAC Alert); opposes abortion except when the pregnancy poses an immediate threat to the mother's life; explicitly opposes taxpayer funding for abortion providers including Planned Parenthood — a pro-life record consistent with the rubric's demand for life-at-conception protection.",
              ["https://kyrighttolife.org/wp-content/uploads/2026/04/KENTUCKY-RIGHT-TO-LIFE-VOTER-GUIDE-2026-PRIMARY-Election-PAC-ALERT.pdf",
               "https://en.wikipedia.org/wiki/Ed_Gallrein"]),
        claim("eg2", "ed-gallrein", "border_immigration", 0, True,
              "Supports completing the Mexico–United States border wall, fully funding U.S. Border Patrol and ICE, and ending the flow of fentanyl across the southern border — directly aligning with the rubric's call for a wall and military-backed border enforcement.",
              ["https://www.edgallrein.com/",
               "https://en.wikipedia.org/wiki/Ed_Gallrein"]),
        claim("eg3", "ed-gallrein", "self_defense", 1, False,
              "Drew backlash from gun-rights groups after pledging only to 'enforce the laws on the books' on firearms and declining to complete the National Association for Gun Rights candidate survey — language that Second Amendment advocates flag as typical of establishment Republicans who accept existing restrictions rather than demanding full rights restoration.",
              ["https://gunrights.org/ed-gallreins-gun-control-comments-spark-backlash-among-kentucky-gun-owners/",
               "https://bearingarms.com/kerry-slone/2026/05/18/gun-owners-key-role-ky4-n1232569"]),
    ]),

    # ---------- Kandiss Taylor (GA-01 R) ----------
    ("kandiss-taylor", "GA", "Representative", [
        claim("kt1", "kandiss-taylor", "sanctity_of_life", 0, True,
              "Believes life begins at conception and plans to criminalize abortion; supports enforcing the Comstock Act to block distribution of abortion-inducing drugs; opposes taxpayer funding for Planned Parenthood — fully consistent with the rubric's life-at-conception and abolition standard.",
              ["https://ballotpedia.org/Kandiss_Taylor",
               "https://ivoterguide.com/candidate/56793/race/26931/election/1409",
               "https://kandisstaylor.com/"]),
        claim("kt2", "kandiss-taylor", "election_integrity", 0, True,
              "Supports mandatory photo ID to vote, paper ballots, and removal of Dominion voting machines and ballot drop boxes — a hardline election-integrity stance matching the rubric's voter-ID / paper-ballot standard.",
              ["https://ballotpedia.org/Kandiss_Taylor",
               "https://ivoterguide.com/candidate/56793/race/26931/election/1409"]),
        claim("kt3", "kandiss-taylor", "self_defense", 0, True,
              "Runs on the 'Jesus, Guns & Babies' platform and affirms every Georgian's constitutional right to bear arms without qualification — consistent with the rubric's constitutional-carry ideal.",
              ["https://www.11alive.com/article/news/politics/kandiss-taylor-georgia-congress-campaign/85-2d8d3214-0251-48ca-a955-162a9ee57b93",
               "https://kandisstaylor.com/"]),
    ]),

    # ---------- Cait Conley (NY-17 D) ----------
    ("cait-conley", "NY", "Representative", [
        claim("cc1", "cait-conley", "sanctity_of_life", 0, False,
              "Supports unrestricted abortion rights; pledges to codify Roe v. Wade into federal law and lift abortion restrictions on military women if elected — rejecting any personhood-from-conception standard.",
              ["https://caitconley.com/",
               "https://ballotpedia.org/Cait_Conley"]),
        claim("cc2", "cait-conley", "sanctity_of_life", 4, False,
              "Pledges to restore federal Planned Parenthood funding; endorsed by the LGBTQ+ Victory Fund and Equality PAC, both of which require candidates to support abortion access as a condition of endorsement.",
              ["https://caitconley.com/",
               "https://victoryfund.org/news/lgbtq-victory-fund-endorses-cait-conley-for-ny-17/",
               "https://lgbtequalitypac.org/candidates/cait-conley/"]),
        claim("cc3", "cait-conley", "biblical_marriage", 2, False,
              "An openly LGBTQ+ candidate endorsed by the LGBTQ+ Victory Fund and Equality PAC; served in the Army under Don't Ask Don't Tell and frames that era as discrimination she opposed; committed to advancing LGBTQ+ equality and protections under federal law — rejecting the rubric's opposition to LGBTQ ideology in policy.",
              ["https://victoryfund.org/news/lgbtq-victory-fund-endorses-cait-conley-for-ny-17/",
               "https://lgbtequalitypac.org/candidates/cait-conley/",
               "https://ballotpedia.org/Cait_Conley"]),
    ]),

    # ---------- Jack Schlossberg (NY-12 D) ----------
    ("jack-schlossberg", "NY", "Representative", [
        claim("js1", "jack-schlossberg", "sanctity_of_life", 0, False,
              "Supports unrestricted access to reproductive care and abortion; as a member of the Harris-Walz Reproductive Rights Tour Bus, traveled the country advocating for abortion access, rejecting any personhood-from-conception framework.",
              ["https://ballotpedia.org/Jack_Schlossberg",
               "https://jimowles.org/news/candidate-answers-to-joldc-jack-schlossberg-for-us-congress-ny-12-2026"]),
        claim("js2", "jack-schlossberg", "biblical_marriage", 4, False,
              "Will not seek or accept endorsements from individuals who oppose LGBTQ+ rights; expressed openness to hosting Drag Story Hours; marched with the Lavender Green Alliance in the St. Patrick's Day Parade — endorsing LGBTQ+ ideology promotion in public life.",
              ["https://jimowles.org/news/candidate-answers-to-joldc-jack-schlossberg-for-us-congress-ny-12-2026",
               "https://ballotpedia.org/Jack_Schlossberg"]),
        claim("js3", "jack-schlossberg", "self_defense", 1, False,
              "Proposed the 'ricochet rule' specifically designed to restrict the flow of firearms into New York — backing new gun-control legislation contrary to the rubric's opposition to new restrictions on arms.",
              ["https://www.amny.com/news/jack-schlossberg-kennedy-heir-ny-12/",
               "https://ballotpedia.org/Jack_Schlossberg"]),
    ]),

    # ---------- Bridget Brink (MI-07 D) ----------
    ("bridget-brink", "MI", "Representative", [
        claim("bb1", "bridget-brink", "foreign_policy_restraint", 1, False,
              "As U.S. Ambassador to Ukraine (2022-2025), led the on-the-ground U.S. effort to supply military aid to Ukraine; resigned over President Trump's withdrawal of that support and built her congressional campaign on restoring it — directly opposing the rubric's call to end open-ended foreign military commitments.",
              ["https://michiganadvance.com/2025/06/18/bridget-brink-who-resigned-as-us-ambassador-to-ukraine-announces-michigan-congressional-run/",
               "https://emilyslist.org/candidate/bridget-brink/"]),
        claim("bb2", "bridget-brink", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List, the premier pro-abortion fundraising network, whose endorsement criteria requires candidates to support abortion rights — placing her squarely inside the abortion-industry money network.",
              ["https://emilyslist.org/news/emilys-list-endorses-bridget-brink-for-michigans-7th-congressional-district/",
               "https://michiganadvance.com/briefs/emilys-list-backs-brink-in-effort-to-unseat-barrett-in-competitive-7th-congressional-district/"]),
        claim("bb3", "bridget-brink", "sanctity_of_life", 0, False,
              "Opposes abortion restrictions; in her campaign launch statement explicitly framed restrictions on abortion rights as an attack on democracy alongside Russia's war on Ukraine — rejecting any legal limits on abortion access.",
              ["https://bridgetbrink.com/",
               "https://michiganadvance.com/2025/06/18/bridget-brink-who-resigned-as-us-ambassador-to-ukraine-announces-michigan-congressional-run/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
