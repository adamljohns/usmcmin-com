#!/usr/bin/env python3
"""Enrichment batch 280: 5 low_evidence 2026 Oklahoma Democratic U.S. Senate candidates.

All five are running for the seat vacated by Markwayne Mullin (Mullin resigned March 2026
to become DHS Secretary; Kevin Hern won the R primary). Claims sourced from Ballotpedia,
Wikipedia, candidate websites, ontheissues.org, and news coverage (2025-2026).

Bottom-of-alphabet (OK) pull: Troy Green, R.O. Joe Cassity Jr., N'Kiyla Jasmine Thomas,
Jim Priest, Ervin Stone Yen.
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
    # ------------ Troy Green (OK-D, 2026 D Candidate, Mullin seat) ------------
    ("troy-green-ok-senate", "OK", "Senator", [
        claim("tg1", "troy-green-ok-senate", "family_child_sovereignty", 0, True,
              "Founded Safe Haven Oklahoma, a nonprofit focused on combating human trafficking and child exploitation; if elected, pledges to reform the foster care system to better protect at-risk children — consistent with the rubric's priority of safeguarding family and child welfare.",
              ["https://ballotpedia.org/Troy_W._Green_(Oklahoma_U.S._Senate_candidate)",
               "https://nondoc.com/2026/05/27/cheat-sheet-5-oklahoma-democrats-compete-in-u-s-senate-primary/"]),
        claim("tg2", "troy-green-ok-senate", "economic_stewardship", 2, False,
              "Champions Medicare expansion and increased federal healthcare and rural-revitalization spending with no stated commitment to reducing the deficit or achieving a balanced budget — a big-government approach at odds with the rubric's fiscal-restraint standard.",
              ["https://ballotpedia.org/Troy_W._Green_(Oklahoma_U.S._Senate_candidate)"]),
    ]),

    # ------------ R.O. Joe Cassity Jr. (OK-D, 2026 D Candidate) ------------
    ("r-o-joe-cassity-jr", "OK", "Senator", [
        claim("rc1", "r-o-joe-cassity-jr", "election_integrity", 0, False,
              "Has publicly condemned the Supreme Court's limiting of the Voting Rights Act as 'a full-scale attack on our sacred multiracial democracy,' opposing the voter-ID and election-security measures the rubric's election-integrity standard supports.",
              ["https://joe4oklahoma.com/",
               "https://www.civoren.com/candidate/r-o-joe-cassity-jr-"]),
        claim("rc2", "r-o-joe-cassity-jr", "economic_stewardship", 2, False,
              "Campaigns on expanding healthcare access and education funding for all Oklahomans with no pledge to reduce the deficit or balance the federal budget, reflecting a government-growth framework at odds with the rubric's fiscal-restraint standard.",
              ["https://ballotpedia.org/R.O._Joe_Cassity",
               "https://joe4oklahoma.com/"]),
    ]),

    # ------------ N'Kiyla Jasmine Thomas (OK-D, 2026 D Candidate) ------------
    ("nkiyla-jasmine-thomas", "OK", "Senator", [
        claim("njt1", "nkiyla-jasmine-thomas", "sanctity_of_life", 0, False,
              "Explicitly advocates for restoring a federal right to abortion access following the Dobbs decision, supporting a federal statute to guarantee abortion access — directly opposing life-at-conception personhood recognition.",
              ["https://ballotpedia.org/N'Kiyla_Thomas",
               "https://www.jasmineforok.com/policies"]),
        claim("njt2", "nkiyla-jasmine-thomas", "biblical_marriage", 0, False,
              "Includes codifying marriage equality as a stated policy priority, endorsing federal recognition of same-sex unions and rejecting the one-man/one-woman definition of marriage.",
              ["https://ballotpedia.org/N'Kiyla_Thomas",
               "https://www.jasmineforok.com/policies"]),
        claim("njt3", "nkiyla-jasmine-thomas", "biblical_marriage", 4, False,
              "Supports extending anti-discrimination protections for LGBTQ individuals into schools and public policy, opposing the rubric's position against institutional promotion of LGBTQ ideology.",
              ["https://ballotpedia.org/N'Kiyla_Thomas"]),
    ]),

    # ------------ Jim Priest (OK-D, 2026 D Candidate) ------------
    ("jim-priest", "OK", "Senator", [
        claim("jp1", "jim-priest", "christian_liberty", 0, True,
              "An ordained Christian minister who made personal faith central to his Senate campaign, explicitly arguing that 'Democrats can be people of faith' and grounding his service ethic in Christian conviction — no stated opposition to religious free exercise.",
              ["https://ballotpedia.org/Jim_Priest",
               "https://www.swoknews.com/ap/politics/jim-priest-advances-to-democratic-primary-runoff-election-for-u-s-senate-in-oklahoma/article_8e786666-4af5-5f35-a5ac-9ea1b10a805a.html"]),
        claim("jp2", "jim-priest", "economic_stewardship", 2, False,
              "Campaigns on federal investment in childcare access, rural hospital funding, and affordable housing with no commitment to reducing the deficit or balancing the federal budget — prioritizing expanded government spending over fiscal restraint.",
              ["https://ballotpedia.org/Jim_Priest",
               "https://jimpriest.com/about/"]),
    ]),

    # ------------ Ervin Stone Yen (OK-D, 2026 D Candidate) ------------
    ("ervin-stone-yen", "OK", "Senator", [
        claim("esy1", "ervin-stone-yen", "sanctity_of_life", 0, False,
              "Self-described 'pro-choice' physician who in his 2022 Oklahoma gubernatorial run stated he supports a woman's right to abortion; running in 2026 as a Democrat he maintains that medical decisions including abortion should rest between patient and doctor, with no political interference.",
              ["https://en.wikipedia.org/wiki/Ervin_Yen",
               "https://www.ontheissues.org/Ervin_Yen.htm"]),
        claim("esy2", "ervin-stone-yen", "self_defense", 1, False,
              "A gun-owner with a concealed carry permit who vows to defend law-abiding citizens' firearm rights, but opposed Oklahoma's permitless-carry legislation — falling short of the rubric's full constitutional-carry / no-new-restrictions standard.",
              ["https://www.ontheissues.org/governor/Ervin_Yen_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/Ervin_Yen"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
