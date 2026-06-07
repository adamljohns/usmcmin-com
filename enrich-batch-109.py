#!/usr/bin/env python3
"""Enrichment batch 109: evidence-curate 4 state/statewide candidates (bottom-of-alphabet).

Targets: Kris Mayes (AZ-D AG), Katie Hobbs (AZ-D Gov), Adrian Fontes (AZ-D SoS),
Mark Totten (MI-D AG). All archetype_curated with 0 claims.
Each claim cites >=1 reliable source reflecting 2024-2026 public positions/actions.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------------- Kris Mayes (AZ-D, Attorney General) ----------------
    ("kris-mayes-ag", "AZ", "Attorney", [
        claim("km1", "kris-mayes-ag", "sanctity_of_life", 0, False,
              "On her first day as Arizona AG, Mayes established the state's first-ever Reproductive Rights Unit and actively litigated to block revival of Arizona's 1864 near-total abortion ban — a direct rejection of any life-at-conception personhood standard.",
              ["https://www.azag.gov/issues/reproductive-rights/ag-actions",
               "https://en.wikipedia.org/wiki/Kris_Mayes"]),
        claim("km2", "kris-mayes-ag", "biblical_marriage", 0, False,
              "Openly lesbian politician endorsed by the LGBTQ+ Victory Fund, explicitly rejecting the one-man-one-woman definition of marriage and making her identity a central element of her political platform.",
              ["https://victoryfund.org/candidate/kris-mayes/",
               "https://en.wikipedia.org/wiki/Kris_Mayes"]),
        claim("km3", "kris-mayes-ag", "border_immigration", 0, False,
              "Post-2024 election, Mayes announced plans to use the AG office to push back against Trump administration immigration enforcement — including opposing any DACA rollback — and filed dozens of lawsuits against federal immigration policies.",
              ["https://azmirror.com/2024/11/13/ag-kris-mayes-says-she-has-a-plan-to-protect-arizona-from-unacceptable-trump-policies/",
               "https://en.wikipedia.org/wiki/Kris_Mayes"]),
    ]),

    # ---------------- Katie Hobbs (AZ-D, Governor) ----------------
    ("katie-hobbs-gov-2026", "AZ", "Governor", [
        claim("kh1", "katie-hobbs-gov-2026", "sanctity_of_life", 0, False,
              "On taking office Hobbs signed an executive order barring state prosecutors from cooperating with out-of-state abortion investigations, and in 2024 signed the repeal of Arizona's 1864 near-total abortion ban — actively dismantling any legal protection for unborn life.",
              ["https://reprofreedomalliance.org/state-details/arizona/",
               "https://en.wikipedia.org/wiki/Katie_Hobbs"]),
        claim("kh2", "katie-hobbs-gov-2026", "border_immigration", 0, False,
              "Vetoed Republican-led state immigration enforcement measures and in her 2023 State of the State proposed expanding the Arizona Promise Scholarship to undocumented immigrant students at state universities — directly opposing mandatory deportation and strict border enforcement.",
              ["https://en.wikipedia.org/wiki/Katie_Hobbs",
               "https://azgovernor.gov/"]),
        claim("kh3", "katie-hobbs-gov-2026", "biblical_marriage", 4, False,
              "Shortly after taking office, signed an executive order titled 'Protecting Employment Opportunity' institutionalizing LGBTQ+ sexual-orientation and gender-identity protections into state government employment — promoting LGBTQ ideology through executive policy.",
              ["https://azgovernor.gov/",
               "https://en.wikipedia.org/wiki/Katie_Hobbs"]),
    ]),

    # ---------------- Adrian Fontes (AZ-D, Secretary of State) ----------------
    ("adrian-fontes", "AZ", "Secretary", [
        claim("af1", "adrian-fontes", "election_integrity", 0, False,
              "Publicly opposed measures to strengthen voter ID and restrict mass mail-in voting, stating he did not want legislation that would 'kill your ability to vote by mail' — rejecting the rubric's voter-ID and anti-mass-mail-in standards.",
              ["https://ktar.com/arizona-election-news/adrian-fontes-mail-in-voting/5824515/",
               "https://azsos.gov/adrian-fontes"]),
        claim("af2", "adrian-fontes", "border_immigration", 0, False,
              "Refused a DOJ request for Arizona's statewide voter rolls, blocking federal efforts to audit non-citizen voter data — prioritizing 'voter privacy' over federal law-enforcement cooperation on election and citizenship verification.",
              ["https://hoodline.com/2025/12/arizona-secretary-of-state-adrian-fontes-stands-firm-in-protecting-voter-privacy-against-doj-requests/",
               "https://azsos.gov/news/1026"]),
    ]),

    # ---------------- Mark Totten (MI-D, Attorney General candidate) ----------------
    ("mark-totten-ag", "MI", "Attorney", [
        claim("mt1", "mark-totten-ag", "sanctity_of_life", 0, False,
              "As Biden-era U.S. Attorney led Michigan's legal fight to protect abortion rights; his 2026 AG campaign pledges to 'fight back against efforts to roll back reproductive freedom' — opposing any recognition of life from conception.",
              ["https://www.michiganpublic.org/politics-government/2025-04-16/former-u-s-attorney-mark-totten-launches-campaign-for-michigan-attorney-general",
               "https://www.marktotten.com/priorities"]),
        claim("mt2", "mark-totten-ag", "self_defense", 1, False,
              "Campaign platform prioritizes 'reducing gun violence' by 'keeping guns out of dangerous hands' through expanded background checks and community-based interventions — supporting new gun-control measures inconsistent with the rubric's Second Amendment standards.",
              ["https://www.marktotten.com/priorities",
               "https://www.cbsnews.com/detroit/news/mark-totten-enters-race-for-michigan-attorney-general/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
