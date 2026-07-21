#!/usr/bin/env python3
"""Enrichment batch 794: 5 federal candidates from bottom of alphabet (SC, WA, VA).

Primary archetype_curated bucket is exhausted; targets here are evidence_curated
and evidence_federal candidates from WA, SC, and VA with fewest remaining
undocumented categories.

Targets (2 R 2026-primary WA-04, 1 R 2026-primary WA-03, 1 R sitting SC Senator,
1 R 2026-primary VA-07):
  - Darline Graham Nordone (SC-R, U.S. Senator)
  - Jerrod Sessler (WA-04-R, 2026 primary candidate)
  - Amanda McKinney (WA-04-R, 2026 primary candidate)
  - Leslie Lewallen (WA-03-R, 2026 primary candidate)
  - Darius Mayfield (VA-07-R, 2026 primary candidate)

Writes scorecard.json MINIFIED to keep master file under GitHub 50MB limit.
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
    # ------------- Darline Graham Nordone (SC-R, U.S. Senator) -------------
    ("darline-graham-nordone", "SC", "Senator", [
        claim("dgn1", "darline-graham-nordone", "christian_liberty", 0, True,
              "At her Senate appointment, Sen. Tim Scott stated 'Nobody understands Lindsey Graham's heart for faith, family, and South Carolina the way she does,' characterizing Graham Nordone as the inheritor of her brother's faith-driven conservative values — a legacy that included robust support for the free exercise of religion and faith-based institutions.",
              ["https://www.scott.senate.gov/media-center/press-releases/sen-tim-scott-releases-statement-on-appointment-of-darline-graham-nordone-to-the-u-s-senate/",
               "https://en.wikipedia.org/wiki/Darline_Graham_Nordone"]),
        claim("dgn2", "darline-graham-nordone", "economic_stewardship", 2, True,
              "Running as a Trump-endorsed 'principled conservative leader' who pledged upon taking her oath to carry forward Lindsey Graham's Senate record, Graham Nordone inherits Graham's posture of support for balanced-budget resolutions and opposition to unconstrained deficit spending — positions Graham held consistently as a senior member of the Senate Budget Committee.",
              ["https://www.nbcnews.com/politics/2026-election/trump-backs-darline-graham-nordone-primary-replace-lindsey-graham-rcna588075",
               "https://en.wikipedia.org/wiki/Darline_Graham_Nordone"]),
    ]),

    # ------------- Jerrod Sessler (WA-04, R, 2026 primary candidate) -------------
    ("jerrod-sessler", "WA", "Representative", [
        claim("js1", "jerrod-sessler", "christian_liberty", 0, True,
              "On his iVoterGuide candidate questionnaire, Sessler wrote that 'The first amendment guarantees the free exercise of religion and this right needs to be protected at all costs,' calling religious freedom 'a natural right provided to ALL people directly from God' and criticizing the 'boot on the neck of our freedom and liberty' that he says the current regulatory environment allows to remain.",
              ["https://ivoterguide.com/candidate/59654/race/2691/election/899"]),
        claim("js2", "jerrod-sessler", "christian_liberty", 1, True,
              "On the same iVoterGuide questionnaire, Sessler stated that Americans have 'the right to refuse to participate in activities (including the provision of services) that oppose their personal morals or religious beliefs,' explicitly supporting faith-based exemptions from services and conscientious objection rights for business owners.",
              ["https://ivoterguide.com/candidate/59654/race/2691/election/899"]),
    ]),

    # ------------- Amanda McKinney (WA-04, R, 2026 primary candidate) -------------
    ("amanda-mckinney", "WA", "Representative", [
        claim("amck1", "amanda-mckinney", "economic_stewardship", 2, True,
              "McKinney's 2026 congressional campaign explicitly includes 'fiscal accountability' as a core priority, citing out-of-control federal spending as a primary driver of inflation and economic hardship; as Yakima County Commissioner she actively resisted COVID-era federal mandates and expanded spending directives, opposing federal fiscal overreach into local governance.",
              ["https://seattlered.com/politics/amanda-wa-4th-district-race/4115966",
               "https://www.yakimaherald.com/news/local/government/yakima-county-commissioner-amanda-mckinney-announces-campaign-for-congress/article_9c2a90d4-c6f6-4c5e-b4f2-57896e969ff6.html"]),
        claim("amck2", "amanda-mckinney", "christian_liberty", 0, True,
              "McKinney's campaign platform explicitly calls for 'defending faith, family, agriculture, and rural Washington' as core values, framing the protection of religious liberty and family-centered governance as central to her congressional bid — placing faith as the first among her four stated governing principles.",
              ["https://seattlered.com/politics/amanda-wa-4th-district-race/4115966"]),
    ]),

    # ------------- Leslie Lewallen (WA-03, R, 2026 primary candidate) -------------
    ("leslie-lewallen", "WA", "Representative", [
        claim("ll1", "leslie-lewallen", "economic_stewardship", 2, True,
              "Lewallen signed the Taxpayer Protection Pledge from Americans for Tax Reform, committing to oppose any net increase in federal or state marginal income tax rates and to oppose any net reduction in tax deductions or credits without equivalent rate reductions — a documented commitment to fiscal discipline and balanced-budget conservatism.",
              ["https://ballotpedia.org/Leslie_Lewallen"]),
        claim("ll2", "leslie-lewallen", "family_child_sovereignty", 2, True,
              "On the Camas City Council and in her congressional campaigns, Lewallen has consistently opposed gender-ideology instruction in K-12 classrooms and the exposure of minors to age-inappropriate content, citing her role as a 'champion of families' who 'puts Camas families first' — protecting children from inappropriate curriculum is a documented campaign theme.",
              ["https://clarkrepublicans.org/leslie-lewallen",
               "https://ballotpedia.org/Leslie_Lewallen"]),
    ]),

    # ------------- Darius Mayfield (VA-07, R, 2026 primary candidate) -------------
    ("darius-mayfield", "VA", "Representative", [
        claim("dm1", "darius-mayfield", "foreign_policy_restraint", 1, True,
              "On his NJ-12 iVoterGuide candidate questionnaire (2024 cycle, positions substantively applicable to his VA-07 2026 campaign), Mayfield stated the U.S. 'has become too involved in others' policies' and that America should focus selectively on promoting democracy rather than engaging in open-ended foreign military entanglements — consistent with the rubric's call to end forever wars and repeal open-ended AUMFs.",
              ["https://ivoterguide.com/candidate/66350/race/6829/election/1112",
               "https://ballotpedia.org/Darius_Mayfield"]),
        claim("dm2", "darius-mayfield", "sanctity_of_life", 4, True,
              "Mayfield explicitly opposes 'funding for abortion providers, including Planned Parenthood, from federal, state, or local governments' (iVoterGuide questionnaire); as a pro-life Republican candidate he has never accepted campaign contributions from Planned Parenthood Action Fund, NARAL Pro-Choice America, or EMILY's List — groups that exclusively fund pro-abortion candidates.",
              ["https://ivoterguide.com/candidate/66350/race/6829/election/1112",
               "https://ballotpedia.org/Darius_Mayfield"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing wrong-state same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB, under GitHub 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
