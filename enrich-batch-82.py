#!/usr/bin/env python3
"""Enrichment batch 82: hand-curated claims for 4 candidates from bottom of alphabet.

Targets archetype_curated candidates with 0 claims, taken from the BOTTOM of the
reverse-sorted bucket (WA, TX, TX, SC) to avoid collision with the top-of-alphabet
loop. Uses the (slug + state + office_keyword) matcher from earlier batches.

Mix (2 R / 2 D): Aaron Reitz (TX-R AG), Bruce Harrell (WA-D Mayor),
John Bash (TX-R AG withdrew), Mia McLeod (SC-D→Ind Gov).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions / record.

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
    # ---------------- Aaron Reitz (TX-R, AG candidate — lost R primary Mar 2026) ----------------
    ("aaron-reitz-ag", "TX", "Attorney", [
        claim("ar1", "aaron-reitz-ag", "sanctity_of_life", 0, True,
              "An unapologetic 100%-pro-life attorney who declares 'human life starts at conception, no exceptions.' As Texas Deputy AG for Legal Strategy, he coordinated lawsuits blocking the Biden administration's attempts to override Texas's Human Life Protection Act, and pledged as AG candidate to prosecute any violation of Texas's pro-life laws.",
              ["https://reitzfortexas.com/on-the-issues/",
               "https://reitzfortexas.com/meet-aaron-reitz/"]),
        claim("ar2", "aaron-reitz-ag", "self_defense", 1, True,
              "Pledged to fight any red-flag laws, assault-weapon bans, magazine-capacity limits, silencer or stabilizing-brace prohibitions, and gun-free-zone expansions, stating any such attempt 'will be met with forceful pushback from the state of Texas when I am Attorney General' — fully aligned with the rubric's opposition to all these restrictions.",
              ["https://reitzfortexas.com/on-the-issues/",
               "https://www.amarillopioneer.com/2026-primary-voter-guide/areitz"]),
        claim("ar3", "aaron-reitz-ag", "border_immigration", 0, True,
              "As Texas Deputy AG for Legal Strategy under Ken Paxton, Reitz led ('quarterbacked') the Texas v. Biden border-security litigation docket — lawsuits challenging Biden-era rollbacks of deportation, Title 42, and Remain-in-Mexico — earning Paxton's endorsement as the 'offensive coordinator' of Texas's border enforcement legal strategy.",
              ["https://reitzfortexas.com/meet-aaron-reitz/",
               "https://thetexan.news/elections/2026/paxton-cruz-alum-aaron-reitz-launches-bid-for-texas-attorney-general/article_68573b51-af41-4df0-a914-b41db195b1a9.html"]),
    ]),

    # ---------------- Bruce Harrell (WA-D, former Seattle Mayor — lost Nov 2025) ----------------
    ("bruce-harrell", "WA", "Mayor", [
        claim("bh1", "bruce-harrell", "biblical_marriage", 2, False,
              "As Seattle mayor, signed city legislation explicitly designed to protect residents seeking gender-affirming care in response to what he called Trump administration 'attacks on LGBTQ+ residents,' actively institutionalizing transgender ideology into municipal policy — contrary to the rubric's standard of rejecting it.",
              ["https://en.wikipedia.org/wiki/Bruce_Harrell",
               "https://harrell.seattle.gov/2025/09/23/mayor-harrell-announces-2026-budget-proposal-with-focus-on-affordability-public-safety-homelessness-and-protecting-local-priorities-from-federal-threats/"]),
        claim("bh2", "bruce-harrell", "border_immigration", 2, False,
              "Increased Seattle's Office of Immigrant and Refugee Affairs budget by 70% in his 2026 proposal to expand legal defense, 'Know Your Rights' trainings, and workforce services for undocumented immigrants — a sanctuary-adjacent posture that directly opposes the rubric's anti-sanctuary standard.",
              ["https://harrell.seattle.gov/2025/09/23/mayor-harrell-announces-2026-budget-proposal-with-focus-on-affordability-public-safety-homelessness-and-protecting-local-priorities-from-federal-threats/"]),
        claim("bh3", "bruce-harrell", "sanctity_of_life", 0, False,
              "Signed Seattle ordinances protecting access to abortion ('reproductive healthcare services'), framing the legislation as a local defense against federal restrictions and launching a lawsuit against the Trump administration over federal funding withheld in response — placing him in clear opposition to the rubric's life-from-conception standard.",
              ["https://en.wikipedia.org/wiki/Bruce_Harrell",
               "https://harrell.seattle.gov/2025/09/23/mayor-harrell-announces-2026-budget-proposal-with-focus-on-affordability-public-safety-homelessness-and-protecting-local-priorities-from-federal-threats/"]),
    ]),

    # ---------------- John Bash (TX-R, AG candidate — withdrew Apr 2025) ----------------
    ("john-bash-ag", "TX", "Attorney", [
        claim("jb1", "john-bash-ag", "border_immigration", 1, True,
              "As U.S. Attorney for the Western District of Texas under Trump's zero-tolerance policy, Bash's office processed and prosecuted over 208 criminal immigration cases in a single six-day window, enforcing mandatory criminal prosecution for every illegal-border-crossing referral — the strictest prosecution posture available under federal law.",
              ["https://www.justice.gov/usao-wdtx/pr/western-district-texas-us-attorneys-office-adds-208-immigration-cases-6-days-going",
               "https://en.wikipedia.org/wiki/John_Bash"]),
        claim("jb2", "john-bash-ag", "public_justice", 0, True,
              "Appointed by AG William Barr to lead the DOJ's 'Unmasking Investigation' — a probe into whether Obama-era intelligence officials abused NSA surveillance procedures to identify (unmask) Trump campaign associates in intelligence reports — demonstrating a record of examining potential civil-liberties violations by the federal security state.",
              ["https://en.wikipedia.org/wiki/John_Bash"]),
    ]),

    # ---------------- Mia McLeod (SC-D→Ind, Gov candidate 2022; state sen. through 2024) ----------------
    ("mia-mcleod-gov", "SC", "Governor", [
        claim("mm1", "mia-mcleod-gov", "sanctity_of_life", 0, False,
              "As an SC state senator, formed the bipartisan 'Sister Senators' coalition in 2023 that blocked a bill to ban all abortions in South Carolina, and publicly supports codifying Roe v. Wade into federal law — rejecting any life-from-conception standard.",
              ["https://ballotpedia.org/Mia_McLeod",
               "https://en.wikipedia.org/wiki/Mia_McLeod"]),
        claim("mm2", "mia-mcleod-gov", "self_defense", 1, False,
              "Advocates for 'common-sense gun reforms' in her state legislative record, placing her on the gun-control side of the debate and opposing the rubric's standard of blocking red-flag laws, assault-weapon bans, and magazine-capacity restrictions.",
              ["https://justfacts.votesmart.org/candidate/128282/mia-mcleod"]),
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
