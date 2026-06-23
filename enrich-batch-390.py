#!/usr/bin/env python3
"""Enrichment batch 390: hand-curated claims for 5 WA Democratic State Senators.

Continuing archetype_party_default WA state-senator enrichment from the
bottom of the alphabet (next block after batch 389 which covered WA Republicans).

Senators: Victoria Hunt (WA-SD5), Vandana Slatter (WA-SD48),
Tina Orwall (WA-SD33), T'wina Nobles (WA-SD28),
Steve Conway (WA-SD29).

2 distinct-category claims per senator (10 total).

Each claim cites >=1 reliable source and reflects verified 2023-2025 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Victoria Hunt (WA-SD5, D, State Senator) ----------------
    ("victoria-hunt", "WA", "Senator", [
        claim("vh1", "victoria-hunt", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Alliance Advocates and self-identifies as a champion of 'reproductive healthcare rights,' affirming a pro-choice position that rejects any legal protection for the unborn from conception.",
              ["https://victoriahunt.com/",
               "https://progressivevotersguide.com/washington/2024/general/victoria-hunt"]),
        claim("vh2", "victoria-hunt", "self_defense", 1, False,
              "Voted YES on Washington HB 1163 (April 2025), a permit-to-purchase requirement mandating that residents obtain a government-issued five-year permit from the Washington State Patrol before buying any firearm; the bill passed the Senate 29-19 on a strict party-line vote — every Democratic senator voted yes, every Republican no — imposing a new bureaucratic barrier on law-abiding gun owners.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate"]),
    ]),

    # ---------------- Vandana Slatter (WA-SD48, D, State Senator) ----------------
    ("vandana-slatter", "WA", "Senator", [
        claim("vs1", "vandana-slatter", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Alliance Advocates as a 'proven champion to protect reproductive rights and freedoms in Washington'; sponsored the My Health My Data Act (2023), which created broad privacy protections for patients seeking abortion and reproductive services in Washington following the Dobbs decision — affirming a pro-choice stance that rejects any legal protection for the unborn from conception.",
              ["https://www.plannedparenthoodaction.org/planned-parenthood-alliance-advocates/press-releases/planned-parenthood-alliance-advocates-endorses-slate-of-washington-reproductive-rights-champions",
               "https://vandanaslatter.com/endorsements/"]),
        claim("vs2", "vandana-slatter", "self_defense", 1, False,
              "Voted YES on Washington HB 1163 (April 2025), which requires all Washington residents to obtain a government-issued permit before purchasing a firearm; the bill passed the Senate 29-19 on a strict party-line vote with all Democrats voting yes — imposing new government gatekeeping on the exercise of Second Amendment rights by law-abiding citizens.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://www.nraila.org/articles/20250415/washington-permit-to-purchase-bill-passes-senate"]),
    ]),

    # ---------------- Tina Orwall (WA-SD33, D, State Senator) ----------------
    ("tina-orwall", "WA", "Senator", [
        claim("to1", "tina-orwall", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Alliance Advocates of Washington and Pro-Choice Washington throughout her legislative career, identifying as a pro-choice legislator who opposes any restrictions on abortion access — a position that rejects legal recognition of the unborn from conception.",
              ["https://www.electtinaorwall.com/accomplishments/",
               "https://progressivevotersguide.com/index.php/washington/2024/general/tina-orwall"]),
        claim("to2", "tina-orwall", "self_defense", 1, False,
              "Voted YES on Washington HB 1163 (April 2025), the permit-to-purchase firearms bill requiring a government-issued permit before any firearm may be purchased in Washington; the measure passed 29-19 on a strict party-line Senate vote with all Democrats in support — endorsed by the Alliance for Gun Responsibility, Orwall has consistently backed gun-control measures throughout her tenure.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://gunresponsibility.org/endorsements/"]),
    ]),

    # ---------------- T'wina Nobles (WA-SD28, D, State Senator) ----------------
    ("twina-nobles", "WA", "Senator", [
        claim("tn1", "twina-nobles", "sanctity_of_life", 0, False,
              "Endorsed by Planned Parenthood Votes Northwest and Hawaii; sponsored Washington SB 5826 (2025), which would require public colleges and universities to provide students with access to medication abortion through campus health centers — actively advancing institutional access to abortion and rejecting any legal protection for unborn life from conception.",
              ["https://legiscan.com/WA/bill/SB5826/2025",
               "https://prochoicewashington.org/2020/11/10/for-immediate-release-twina-nobles-unseats-anti-choice-incumbent/"]),
        claim("tn2", "twina-nobles", "family_child_sovereignty", 0, False,
              "Voted YES on Washington ESSB 5599 (2023), which allows licensed youth shelters to withhold the location of a runaway minor from parents when the child is seeking gender-affirming care or reproductive services; the bill passed on a party-line vote 29-20 with all Democrats supporting it — removing a parental-notification requirement and giving state agencies authority to harbor children from parents over medical decisions.",
              ["https://komonews.com/news/local/senate-bill-5599-washington-state-transgender-trans-at-risk-youth-gender-affirming-reproductive-care-without-parental-consent-governor-jay-inslee-family-foster-homeless-children-families-minors-law-legislation",
               "https://www.spokesman.com/stories/2023/apr/19/washington-senate-passes-bill-to-protect-transgend/"]),
    ]),

    # ---------------- Steve Conway (WA-SD29, D, State Senator) ----------------
    ("steve-conway", "WA", "Senator", [
        claim("sc1", "steve-conway", "self_defense", 1, False,
              "Voted YES on Washington HB 1163 (April 2025), the permit-to-purchase firearms bill mandating a government-issued permit from the Washington State Patrol before any firearm purchase; the bill passed the Senate 29-19 on a strict party-line vote with all Democrats — including Conway, who serves as Senate President Pro Tempore — voting in favor, imposing a new licensing barrier on law-abiding gun buyers.",
              ["https://washingtonstatestandard.com/2025/03/08/controversial-permit-to-purchase-gun-bill-clears-washington-senate/",
               "https://mynorthwest.com/mynorthwest-politics/bill-requiring-permits-for-gun-purchases-passes-house-on-party-line-vote/4059942"]),
        claim("sc2", "steve-conway", "family_child_sovereignty", 0, False,
              "Voted YES on Washington ESSB 5599 (2023), allowing licensed youth shelters to withhold the location of a runaway minor from parents when the child is seeking gender-affirming care or reproductive services; the bill passed 29-20 on a party-line vote with all Democrats in support — substituting state discretion for parents' right to know where their child is and what medical decisions are being made.",
              ["https://komonews.com/news/local/senate-bill-5599-washington-state-transgender-trans-at-risk-youth-gender-affirming-reproductive-care-without-parental-consent-governor-jay-inslee-family-foster-homeless-children-families-minors-law-legislation",
               "https://www.spokesman.com/stories/2023/apr/19/washington-senate-passes-bill-to-protect-transgend/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
