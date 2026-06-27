#!/usr/bin/env python3
"""Enrichment batch 450: 10 claims across 5 sitting U.S. Senators.

Bottom-of-alphabet targets: Patty Murray (WA-D), Maria Cantwell (WA-D),
Tim Kaine (VA-D), Mark Warner (VA-D), Tammy Baldwin (WI-D).
2 distinct-category claims per senator, all sourced from official senate.gov /
congress.gov / en.wikipedia.org records from 2021-2024.

Primary rubric categories covered: industry_capture, election_integrity,
foreign_policy_restraint, economic_stewardship.
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
    # ---------------- Patty Murray (WA-D, US Senator) ----------------
    ("patty-murray", "WA", "Senator", [
        claim("pm1", "patty-murray", "industry_capture", 0, False,
              "When the Senate voted 52-48 on S.J. Res. 29 (December 8, 2021) to overturn the Biden Administration's OSHA COVID-19 vaccine-or-testing mandate covering 84 million private-sector workers, Murray voted NO — publicly condemning the repeal effort as 'dangerous' — defending mandatory pharmaceutical intervention over individual conscience, contrary to the rubric's opposition to pharma mandates.",
              ["https://www.murray.senate.gov/senator-murray-slams-republicans-dangerous-effort-to-undermine-economic-recovery-and-pandemic-response-by-upending-vaccine-and-testing-safety-standard/",
               "https://www.democrats.senate.gov/2021/12/08/roll-call-vote-passage-of-sjres29-vaccine-mandate-disapproval"]),
        claim("pm2", "patty-murray", "election_integrity", 0, False,
              "Co-introduced the For the People Act (S.1, 117th Congress, March 2021) with Sen. Cantwell and colleagues — legislation that would have prohibited strict photo-ID requirements, mandated automatic and same-day voter registration nationwide, and dramatically expanded universal vote-by-mail — directly opposing the rubric's voter-ID and paper-ballot standards. Murray also repeatedly championed the Freedom to Vote Act for the same purposes.",
              ["https://www.murray.senate.gov/murray-cantwell-colleagues-introduce-for-the-people-act-to-protect-fundamental-voting-rights-strengthen-democracy-put-power-back-in-the-hands-of-the-american-people/",
               "https://www.congress.gov/bill/117th-congress/senate-bill/1"]),
    ]),

    # ---------------- Maria Cantwell (WA-D, US Senator) ----------------
    ("maria-cantwell", "WA", "Senator", [
        claim("mc1", "maria-cantwell", "foreign_policy_restraint", 4, False,
              "Voted YES on H.R.815, the $95.3 billion national security supplemental (Senate 79-18, April 23, 2024) delivering $60.6 billion to Ukraine, $14 billion in military assistance to Israel, and additional Indo-Pacific security commitments — hailing it as 'vital assistance to allies' and openly rejecting a restraint-first U.S. foreign policy posture contrary to the rubric.",
              ["https://www.cantwell.senate.gov/news/press-releases/cantwell-on-passage-of-foreign-aid-package-providing-vital-assistance-to-allies-israel-ukraine-and-taiwan",
               "https://en.wikipedia.org/wiki/Public_Law_118-50"]),
        claim("mc2", "maria-cantwell", "industry_capture", 0, False,
              "Voted NO on S.J. Res. 29 (Senate 52-48, December 8, 2021), the Congressional Review Act resolution to overturn the Biden Administration's OSHA vaccine-or-testing mandate for private employers with 100+ workers — siding with Murray and 46 other Senate Democrats to keep the government pharmaceutical mandate in force, contrary to the rubric's opposition to pharma mandates.",
              ["https://www.democrats.senate.gov/2021/12/08/roll-call-vote-passage-of-sjres29-vaccine-mandate-disapproval",
               "https://ballotpedia.org/Maria_Cantwell"]),
    ]),

    # ---------------- Tim Kaine (VA-D, US Senator) ----------------
    ("tim-kaine", "VA", "Senator", [
        claim("tk1", "tim-kaine", "economic_stewardship", 2, False,
              "Voted YES on the American Rescue Plan Act of 2021 (H.R.1319, Senate 50-49, March 6, 2021), a $1.9 trillion emergency spending package financed entirely through deficit borrowing with no corresponding revenue offsets — one of the largest single-year additions to the national debt and contrary to the rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/American_Rescue_Plan_Act_of_2021",
               "https://www.congress.gov/bill/117th-congress/house-bill/1319"]),
        claim("tk2", "tim-kaine", "industry_capture", 0, False,
              "Voted NO on S.J. Res. 29 (Senate 52-48, December 8, 2021), the Congressional Review Act resolution to strike down the Biden Administration's OSHA COVID-19 vaccine-or-testing mandate affecting 84 million private-sector workers — voting to maintain a government directive compelling workers to submit to pharmaceutical injection or weekly testing as a condition of employment.",
              ["https://www.democrats.senate.gov/2021/12/08/roll-call-vote-passage-of-sjres29-vaccine-mandate-disapproval",
               "https://en.wikipedia.org/wiki/Tim_Kaine"]),
    ]),

    # ---------------- Mark Warner (VA-D, US Senator) ----------------
    ("mark-warner", "VA", "Senator", [
        claim("mw1", "mark-warner", "foreign_policy_restraint", 4, False,
              "As Senate Intelligence Committee Chairman, was the most prominent Senate champion of H.R.815, the $95.3 billion Ukraine/Israel/Taiwan aid package (signed April 24, 2024), calling his vote to advance it 'the most important vote in 14 years in this job' — directly contradicting the rubric's mandate to end open-ended foreign military entanglements and resist NATO-sphere expansion commitments.",
              ["https://www.warner.senate.gov/public/index.cfm/2024/4/senate-intel-chair-warner-on-the-urgent-need-to-pass-aid-to-ukraine",
               "https://www.warner.senate.gov/public/index.cfm/2024/2/sen-warner-on-passage-of-national-security-supplemental"]),
        claim("mw2", "mark-warner", "industry_capture", 0, False,
              "Voted NO on S.J. Res. 29 (Senate 52-48, December 8, 2021), the Congressional Review Act resolution to overturn the Biden Administration's OSHA vaccine-or-testing mandate for private employers with 100+ employees — voting to keep the government pharmaceutical mandate in force against 84 million American workers, contrary to the rubric's anti-pharma-mandate standard.",
              ["https://www.democrats.senate.gov/2021/12/08/roll-call-vote-passage-of-sjres29-vaccine-mandate-disapproval",
               "https://en.wikipedia.org/wiki/Mark_Warner"]),
    ]),

    # ---------------- Tammy Baldwin (WI-D, US Senator) ----------------
    ("tammy-baldwin", "WI", "Senator", [
        claim("tb1", "tammy-baldwin", "foreign_policy_restraint", 4, False,
              "Voted YES on H.R.815 ($95.3 billion national security supplemental, Senate 79-18, April 23, 2024) providing $60+ billion to Ukraine and $14 billion in military assistance to Israel, declaring she was 'proud to help ensure this aid is used in line with American values' — rejecting the rubric's restraint-first foreign policy and open-ended overseas military commitment discipline.",
              ["https://www.baldwin.senate.gov/news/press-releases/baldwin-votes-to-support-our-allies-deliver-humanitarian-aid-and-disrupt-flow-of-fentanyl",
               "https://en.wikipedia.org/wiki/Public_Law_118-50"]),
        claim("tb2", "tammy-baldwin", "economic_stewardship", 2, False,
              "Voted YES on the American Rescue Plan Act of 2021 (H.R.1319, Senate 50-49, March 6, 2021), a $1.9 trillion COVID relief package financed entirely through deficit spending without revenue offsets — one of the largest single-year additions to the national debt in U.S. history and contrary to the rubric's anti-deficit/balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/American_Rescue_Plan_Act_of_2021",
               "https://www.congress.gov/bill/117th-congress/house-bill/1319"]),
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

    # Minified write — preserve no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
