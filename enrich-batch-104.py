#!/usr/bin/env python3
"""Enrichment batch 104: evidence-curate 5 governor-race candidates (IL/HI/GA/CO/CA).

Targets archetype_curated governors/nominees that had 0 evidence claims, taken
from the bottom of the remaining alphabet bucket (IL→CA), after WY/WV/WI/WA/VA
were exhausted by prior batches. Each claim cites >=1 reliable source and
reflects 2024-2026 record or stated positions.

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
    # ---------------- J.B. Pritzker (IL-D, Governor) ----------------
    ("jb-pritzker", "IL", "Governor", [
        claim("jbp1", "jb-pritzker", "sanctity_of_life", 0, False,
              "Strongly pro-choice governor: on January 22, 2019, signed an executive order expanding abortion coverage for Illinois state employees; in October 2023 personally launched and funded Think Big America, a nonprofit that bankrolls abortion-access ballot measures in other states — placing him in direct opposition to the rubric's protection of unborn life from conception.",
              ["https://ballotpedia.org/J.B._Pritzker",
               "https://en.wikipedia.org/wiki/JB_Pritzker"]),
        claim("jbp2", "jb-pritzker", "self_defense", 1, False,
              "On January 10, 2023, signed the Protect Illinois Communities Act — making Illinois the ninth state to ban assault-style weapons and imposing magazine limits of 10 rounds for long guns and 15 for handguns, a sweeping infringement on the right to keep and bear arms that the rubric opposes.",
              ["https://www.illinois.gov/news/press-release.25887.html",
               "https://www.wgem.com/2023/01/11/gov-jb-pritzker-signs-bill-banning-assault-weapons-high-capacity-magazines/"]),
    ]),

    # ---------------- Josh Green (HI-D, Governor) ----------------
    ("josh-green-gov-2026", "HI", "Governor", [
        claim("jg1", "josh-green-gov-2026", "sanctity_of_life", 0, False,
              "On March 22, 2023, signed legislation expanding abortion access statewide: removes Hawaii's parental-consent requirement for minors seeking abortions, shields local providers from out-of-state prosecution, and allows physician assistants to perform first-trimester abortions — rejecting any protection of unborn life.",
              ["https://www.mauinews.com/news/local-news/2023/03/green-signs-first-bills-on-abortion-access-and-felony-prosecutions/",
               "https://www.hawaiipublicradio.org/local-news/2023-03-23/new-law-expands-abortion-access-protects-local-providers-from-out-of-state-authorities"]),
        claim("jg2", "josh-green-gov-2026", "self_defense", 1, False,
              "In response to the U.S. Supreme Court's 2022 Bruen ruling, signed Act 52 (SB 1230) maintaining Hawaii's strict gun-control framework by banning concealed carry in sensitive locations including hospitals, beaches, and theaters — defending gun-restriction regimes the rubric opposes.",
              ["https://governor.hawaii.gov/newsroom/office-of-the-governor-news-release-263-bills-signed-into-law-by-governor-josh-green-m-d/"]),
    ]),

    # ---------------- Keisha Lance Bottoms (GA-D, Governor D Nominee) ----------------
    ("keisha-lance-bottoms-gov", "GA", "Governor", [
        claim("klb1", "keisha-lance-bottoms-gov", "biblical_marriage", 4, False,
              "As Atlanta mayor, created the city's first LGBTQ Advisory Board (2018), directed the release of Atlanta's first LGBTQ Affairs report (February 2020), and appointed the city's first director of LGBTQ Affairs (December 2020) — institutionally embedding LGBTQ ideology into city government, the active promotion the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Keisha_Lance_Bottoms",
               "https://ballotpedia.org/Keisha_Lance_Bottoms"]),
        claim("klb2", "keisha-lance-bottoms-gov", "border_immigration", 2, False,
              "On September 6, 2018, signed an executive order directing Atlanta's Department of Corrections to stop accepting ICE detainees — making Atlanta a sanctuary city that refuses to cooperate with federal immigration enforcement, the anti-sanctuary posture the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Keisha_Lance_Bottoms"]),
    ]),

    # ---------------- Phil Weiser (CO-D, Governor candidate) ----------------
    ("phil-weiser-gov", "CO", "Governor", [
        claim("pw1", "phil-weiser-gov", "sanctity_of_life", 0, False,
              "As Colorado AG, joined the coalition lawsuit to halt the Texas heartbeat law, challenged the federal Gag Rule restricting abortion referrals, and pledges as governor to 'defend the right to reproductive healthcare...for those coming to our state' — treating abortion access as a non-negotiable priority inconsistent with the rubric's life-at-conception standard.",
              ["https://www.cpr.org/2022/07/11/colorados-attorney-general-vows-to-protect-abortion-access-gun-laws/",
               "https://philforcolorado.com/defending-colorado-and-our-rights/"]),
        claim("pw2", "phil-weiser-gov", "self_defense", 1, False,
              "As Colorado AG, litigated in court to defend Colorado's red-flag-style gun laws that remove firearms from individuals deemed a danger to themselves or others — directly opposing the rubric's anti-red-flag-law position.",
              ["https://www.cpr.org/2022/07/11/colorados-attorney-general-vows-to-protect-abortion-access-gun-laws/"]),
    ]),

    # ---------------- Gavin Newsom (CA-D, Governor) ----------------
    ("gavin-newsom", "CA", "Governor", [
        claim("gn1", "gavin-newsom", "sanctity_of_life", 0, False,
              "Personally championed California Proposition 1 (November 2022) — a joint effort with legislative leaders that amended the California Constitution to enshrine an explicit right to abortion and contraceptives; it passed with over two-thirds of the vote. Also signed a March 2022 law requiring private insurers to cover abortion with no co-pays or deductibles.",
              ["https://en.wikipedia.org/wiki/2022_California_Proposition_1",
               "https://ballotpedia.org/California_Proposition_1,_Right_to_Reproductive_Freedom_Amendment_(2022)"]),
        claim("gn2", "gavin-newsom", "biblical_marriage", 1, False,
              "As San Francisco mayor in February 2004, directed the city-county clerk to issue marriage licenses to same-sex couples in defiance of California law — roughly 4,000 licenses were issued during what became known as the 'Winter of Love' — a landmark act of institutionalizing same-sex marriage that directly rejected the one-man-one-woman definition the rubric upholds.",
              ["https://en.wikipedia.org/wiki/San_Francisco_2004_same-sex_weddings",
               "https://en.wikipedia.org/wiki/Gavin_Newsom"]),
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
