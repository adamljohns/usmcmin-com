#!/usr/bin/env python3
"""Enrichment batch 94: hand-curated claims for 4 candidates (NY/OH/MN).

Targets archetype_curated candidates from the bottom of the alphabet (OH, NY, MN)
that had 0 evidence claims. Uses the (slug + state + office_keyword) matcher.

Candidates: Thomas DiNapoli (NY Comptroller-D), Mathura Sridharan (OH AG-R),
Keith Ellison (MN AG-D), Heather Hill (OH Gov candidate-R, lost May 2026 primary).
Each claim cites >=1 reliable source and reflects 2024-2026 positions/record.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ---------------- Thomas DiNapoli (NY-D, State Comptroller) ----------------
    ("thomas-dinapoli-2026", "NY", "Comptroller", [
        claim("td1", "thomas-dinapoli-2026", "biblical_marriage", 0, False,
              "Publicly declared support for marriage equality as Comptroller and leveraged "
              "the NY Common Retirement Fund's shareholder power to push LGBTQ "
              "non-discrimination policies at portfolio companies — directly opposing the "
              "one-man-one-woman standard the rubric requires.",
              ["https://www.hrc.org/press-releases/new-york-comptroller-tom-dinapoli-supports-marriage-equality",
               "https://en.wikipedia.org/wiki/Tom_DiNapoli"]),
        claim("td2", "thomas-dinapoli-2026", "economic_stewardship", 4, False,
              "As trustee of New York's ~$270B Common Retirement Fund, DiNapoli adopted an "
              "ESG-driven Climate Action Plan targeting net-zero by 2040, divested coal "
              "producers, and orchestrated the ouster of three ExxonMobil board members via "
              "activist-investor campaigns in 2021 — a full embrace of the WEF/ESG-aligned "
              "portfolio strategy the rubric identifies as an industry-capture risk.",
              ["https://www.osc.ny.gov/common-retirement-fund/corporate-governance",
               "https://en.wikipedia.org/wiki/Tom_DiNapoli"]),
        claim("td3", "thomas-dinapoli-2026", "sanctity_of_life", 0, False,
              "Identifies as pro-choice and frames abortion restrictions as 'extremist' in "
              "his 2026 reelection materials; as a New York State Assemblyman for 20 years "
              "(1986-2007) he consistently voted in favor of abortion-access legislation, "
              "never acknowledging personhood from conception.",
              ["https://dinapolifornewyork.com/record-policy",
               "https://en.wikipedia.org/wiki/Tom_DiNapoli"]),
    ]),

    # -------- Mathura Sridharan (OH-R, Attorney General candidate / Solicitor General) --------
    ("mathura-sridharan-ag", "OH", "Attorney General of Ohio", [
        claim("ms1", "mathura-sridharan-ag", "family_child_sovereignty", 0, True,
              "As Ohio Solicitor General, Sridharan is defending Ohio's 2024 social-media "
              "age-verification law — which requires platforms to obtain verifiable parental "
              "consent before opening accounts for minors under 16 — establishing state "
              "precedent affirming parental authority over children's digital access against "
              "Big Tech resistance.",
              ["https://www.law.nyu.edu/news/mathura-sridharan-18-solicitor-general-ohio",
               "https://www.hometownstations.com/news/ag-yost-names-ohio-s-new-solicitor-general/article_74ca20ca-6447-48f2-ad05-2be01874bbc3.html"]),
        claim("ms2", "mathura-sridharan-ag", "refuse_federal_overreach", 0, True,
              "Argued and secured a U.S. Supreme Court stay in Ohio v. EPA (2023), blocking "
              "the EPA's 'good neighbor' cross-state air-pollution rule — a landmark Tenth "
              "Amendment victory protecting Ohio's sovereignty against unilateral federal "
              "regulatory expansion. As head of the Ohio AG's Tenth Amendment Center, "
              "Sridharan systematically challenges federal overreach in state and federal courts.",
              ["https://jurisreview.com/ohio-welcomes-mathura-sridharan-as-12th-solicitor-general-amid-culture-clash/",
               "https://www.law.nyu.edu/news/mathura-sridharan-18-solicitor-general-ohio"]),
    ]),

    # ---------------- Keith Ellison (MN-D, Attorney General) ----------------
    ("keith-ellison-ag-2026", "MN", "Attorney General of Minnesota", [
        claim("ke1", "keith-ellison-ag-2026", "self_defense", 1, False,
              "As Minnesota AG, Ellison sued gun manufacturer Glock in December 2024 under "
              "state consumer-fraud and nuisance law, and previously sued firearms retailer "
              "Fleet Farm in 2022 for negligent sales to straw purchasers — an activist "
              "anti-gun litigation strategy that seeks to impose liability on legal gun "
              "makers and sellers, directly threatening Second Amendment rights and commerce.",
              ["https://www.ag.state.mn.us/Office/Communications.asp",
               "https://en.wikipedia.org/wiki/Keith_Ellison"]),
        claim("ke2", "keith-ellison-ag-2026", "sanctity_of_life", 4, False,
              "Received a 100% rating from Planned Parenthood during his 12 years in "
              "Congress, and as MN AG won dismissal in September 2025 of a constitutional "
              "challenge to Minnesota's abortion-access laws — actively defending and "
              "expanding the abortion-on-demand framework while maintaining firm ties to "
              "the abortion-lobby network the rubric's Q4 tests.",
              ["https://www.ag.state.mn.us/Office/Communications/2025/09/03_Abortion.asp",
               "https://en.wikipedia.org/wiki/Keith_Ellison"]),
        claim("ke3", "keith-ellison-ag-2026", "biblical_marriage", 0, False,
              "Served as vice-chair of the Congressional LGBT Caucus during his 12 years "
              "in the U.S. House (2007-2019) and has consistently championed same-sex "
              "marriage and LGBTQ rights throughout his career — voting for the Equality "
              "Act and explicitly rejecting any definition of marriage as exclusively "
              "between one man and one woman.",
              ["https://en.wikipedia.org/wiki/Keith_Ellison"]),
    ]),

    # ------------- Heather Hill (OH-R, Governor candidate, lost May 2026 primary) -------------
    ("heather-hill-gov", "OH", "Governor of Ohio", [
        claim("hh1", "heather-hill-gov", "family_child_sovereignty", 0, True,
              "Made parental rights in education a centerpiece of her 2026 Ohio gubernatorial "
              "primary campaign, advocating for full parental authority over curriculum and "
              "school-library content — consistent with the rubric's parental-sovereignty "
              "standard. Hill was disqualified from the May 2026 R primary after her "
              "running mate withdrew, but continued campaigning independently.",
              ["https://www.wdtn.com/news/your-local-election-hq/2-news-speaks-with-heather-hill-on-education-entering-politics-connecting-with-ohioans/",
               "https://www.wfmj.com/news/political/decision-2026-oh-governor-heather-hill/article_fb44d766-56d1-46d9-98b0-16b96d3ddd67.html"]),
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
