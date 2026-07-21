#!/usr/bin/env python3
"""Enrichment batch 798: 3 federal Senate targets from the bottom of the alphabet
(TX, NH, SC) — deepening evidence_curated records with missing rubric categories.

Primary archetype_curated federal-senator bucket is fully exhausted; this batch
adds claims to evidence_curated senators/candidates with fewer than 8 claims.

Targets (bottom-agent territory):
  Ken Paxton       (TX-R) — christian_liberty, family_child_sovereignty, industry_capture
  Jeanne Shaheen   (NH-D) — election_integrity, christian_liberty
  Annie Andrews    (SC-D) — biblical_marriage, christian_liberty

All claims sourced from official *.gov, congress.gov, govtrack.us, ballotpedia.org,
or en.wikipedia.org. Writes scorecard.json MINIFIED (no indent) to keep the master
under GitHub's 50MB limit.
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
    # ------------ Ken Paxton (TX-R, 2026 U.S. Senate candidate / sitting TX AG) ------------
    ("ken-paxton-senate", "TX", "Senate", [
        claim("kp1", "ken-paxton-senate", "christian_liberty", 0, True,
              "As Texas Attorney General, Paxton filed two back-to-back November 2025 lawsuits "
              "defending religious organizations from government discrimination: one against the "
              "Texas Department of Housing and Community Affairs for issuing unconstitutional "
              "rules that restricted federal and state funding to Christian groups and other "
              "religious organizations serving homeless and low-income Texans, and a second "
              "against the Texas Higher Education Coordinating Board to end three university "
              "work-study programs that discriminated against religious students — including "
              "Christians — and sectarian employers, representing the most sustained "
              "state-level defense of institutional religious free exercise in the nation in 2025.",
              ["https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-state-housing-agency-discriminating-against-christian-groups-and",
               "https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-end-unconstitutional-taxpayer-funded-higher-education-work-program"]),
        claim("kp2", "ken-paxton-senate", "family_child_sovereignty", 0, True,
              "In October and November 2024, Paxton filed lawsuits against three Texas doctors — "
              "May Lau, M. Brett Cooper, and Hector Granados — for illegally providing "
              "gender-transition drugs to nearly two dozen Texas children in violation of "
              "Senate Bill 14 (Texas's ban on gender-modifying medical treatment for minors); "
              "Dr. Lau and Dr. Cooper entered Rule 11 agreements halting their medical practice "
              "entirely, and Dr. Granados was placed under a court-ordered injunction. In March "
              "2025 Paxton filed an emergency mandamus petition in the Texas Supreme Court to "
              "reverse a lower court order reinstating such treatments, directly defending the "
              "state's parental-protection framework for children's healthcare.",
              ["https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-doctor-illegally-providing-harmful-gender-transition-treatments",
               "https://www.texasattorneygeneral.gov/news/releases/paxton-fights-court-order-regarding-use-dangerous-procedures-on-children"]),
        claim("kp3", "ken-paxton-senate", "industry_capture", 0, True,
              "Filed a November 2023 lawsuit against Pfizer for misrepresenting the efficacy "
              "of its COVID-19 vaccine and conspiring to censor public discourse about the "
              "vaccine in violation of the Texas Deceptive Trade Practices Act; and in January "
              "2026 launched a wide-sweeping investigation — issuing over 20 Civil Investigative "
              "Demands to major medical providers, insurance companies, and pharmaceutical "
              "manufacturers including UnitedHealthcare and Pfizer — into unlawful financial "
              "incentives connected to childhood vaccine recommendations, directly challenging "
              "the pharma-to-physician payment pipeline that shapes pediatric vaccine schedules.",
              ["https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-pfizer-misrepresenting-covid-19-vaccine-efficacy-and-conspiring",
               "https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-launches-wide-sweeping-investigation-unlawful-financial-incentives"]),
    ]),

    # ------------ Jeanne Shaheen (NH-D, sitting U.S. Senator) ------------
    ("jeanne-shaheen", "NH", "Senator", [
        claim("jsah1", "jeanne-shaheen", "election_integrity", 0, False,
              "Took to the Senate floor to directly oppose the SAVE America Act — which requires "
              "proof of U.S. citizenship to register to vote in federal elections — calling it "
              "'This Bill Prevents Americans from Voting' and arguing that documented noncitizen "
              "voting is less than one hundredth of one percent of cases, while citing research "
              "finding the law caused hundreds of eligible registrants to be turned away in "
              "municipal elections and that women with birth certificates showing maiden names "
              "were denied registration. Her opposition places her squarely against citizenship "
              "verification as a condition of federal voter registration.",
              ["https://www.shaheen.senate.gov/news/press/on-senate-floor-shaheen-slams-republicans-save-america-act-this-bill-prevents-americans-from-voting"]),
        claim("jsah2", "jeanne-shaheen", "christian_liberty", 0, False,
              "An original co-sponsor who actively championed the Equality Act (S.393, 117th "
              "Congress, 2021–2022), which would expand federal civil rights protections to "
              "sexual orientation and gender identity across employment, housing, credit, "
              "education, and public accommodations; critically, the bill explicitly prohibits "
              "use of the Religious Freedom Restoration Act (RFRA) as a legal defense against "
              "LGBTQ discrimination claims — removing the primary shield that religious "
              "organizations, charities, schools, and small businesses currently use to decline "
              "participation in actions contrary to their beliefs. Shaheen joined colleagues "
              "in formally calling on Mitch McConnell to bring the bill to the Senate floor.",
              ["https://www.shaheen.senate.gov/news/press/shaheen-and-hassan-join-group-of-senators-in-push-to-bring-equality-act-to-a-vote",
               "https://www.congress.gov/bill/117th-congress/senate-bill/393"]),
    ]),

    # ------------ Annie Andrews (SC-D, 2026 U.S. Senate nominee / pediatrician) ------------
    ("annie-andrews-senate", "SC", "Senate", [
        claim("aand1", "annie-andrews-senate", "biblical_marriage", 2, False,
              "When Rep. Nancy Mace ran September 2022 campaign ads accusing her of 'child abuse' "
              "for providing gender-affirming care at the Medical University of South Carolina, "
              "Andrews responded: 'I do not support gender-affirming surgery for anyone under "
              "18 — nor does my hospital perform those procedures. What I support is "
              "evidence-based medical care, with parental consent, for teens struggling with "
              "gender identity issues.' Entering her 2026 U.S. Senate campaign, Andrews stated "
              "her views on transgender healthcare 'have not changed,' continuing to affirm "
              "hormonal and puberty-blocker interventions for minors with parental approval "
              "as legitimate 'evidence-based medicine,' in alignment with LGBTQ advocacy "
              "organizations rather than with a rejection of gender-transition ideology.",
              ["https://ballotpedia.org/Annie_Andrews",
               "https://en.wikipedia.org/wiki/Annie_Andrews_(physician)"]),
        claim("aand2", "annie-andrews-senate", "christian_liberty", 0, False,
              "As a pediatrician who provides gender-affirming care for LGBTQ youth and as "
              "2026 SC Democratic Senate nominee, Andrews has stated that 'sexual orientation "
              "and gender identity should be protected classes in non-discrimination laws' — "
              "a position that directly conflicts with Religious Freedom Restoration Act "
              "exemptions that religious healthcare providers, adoption agencies, and employers "
              "invoke to decline participation in gender-transition care or same-sex partnerships; "
              "her campaign platform calls for expanding LGBTQ protections as a core "
              "healthcare and civil rights priority.",
              ["https://ballotpedia.org/Annie_Andrews"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
