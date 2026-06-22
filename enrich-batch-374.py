#!/usr/bin/env python3
"""Enrichment batch 374: hand-curated claims for 5 sitting U.S. Senators.

Targets federal-level senators with exactly 3 evidence claims, sorted from
the bottom of the alphabet (MT, MO, MS, NH, LA). Uses the
(slug + state + office_keyword) matcher from prior batches to avoid
same-slug name collisions.

Mix (4 R / 1 D): Steve Daines (MT-R), Eric Schmitt (MO-R),
Cindy Hyde-Smith (MS-R), John Kennedy (LA-R), Maggie Hassan (NH-D).
Each claim cites >=1 reliable source and reflects 2021-2026 voting
record / public positions across distinct rubric categories not
already covered by existing claims.

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
    # ---------------- Steve Daines (MT-R, US Senator) ----------------
    # Existing: sanctity_of_life/0 True, self_defense/1 True, border_immigration/0 True
    ("steve-daines", "MT", "Senator", [
        claim("sd4", "steve-daines", "economic_stewardship", 2, True,
              "A consistent fiscal hawk who has voted against multiple large deficit-spending packages from both parties. Reintroduced the Balanced Budget Accountability Act to withhold congressional pay unless the budget is balanced, stating 'If Congress can't do its job and pass a balanced budget, members shouldn't get paid.' In March 2024 he voted against a spending package he called 'out-of-control' because it contained $1.9 billion in earmarks without addressing the border crisis.",
              ["https://www.daines.senate.gov/meet-steve/legislative-issues/fiscal-responsibility/",
               "https://www.daines.senate.gov/2025/01/09/daines-if-members-of-congress-cant-balance-the-budget-they-shouldnt-get-paid/"]),
        claim("sd5", "steve-daines", "foreign_policy_restraint", 1, True,
              "Voted against the February 2024 $95 billion emergency supplemental providing aid to Ukraine, Israel, and Taiwan, stating: 'While I support providing lethal aid for Israel, Taiwan and Ukraine, I voted against the emergency supplemental spending bill today because securing our southern border should be our highest priority.' He also sought to carve Ukraine aid out of must-pass spending bills and require it to be funded with seized Russian assets rather than new U.S. appropriations.",
              ["https://www.tester.senate.gov/newsroom/news-coverage/billings-gazette-tester-backs-israel-ukraine-aid-daines-doesnt/",
               "https://en.wikipedia.org/wiki/Steve_Daines"]),
    ]),

    # ---------------- Eric Schmitt (MO-R, US Senator) ----------------
    # Existing: sanctity_of_life/0 True, self_defense/1 True, border_immigration/1 True
    ("eric-schmitt", "MO", "Senator", [
        claim("es1", "eric-schmitt", "christian_liberty", 0, True,
              "As Missouri Attorney General, Schmitt filed the landmark Missouri v. Biden lawsuit exposing the Biden administration's pressure campaign on Big Tech companies to censor speech on COVID, elections, and conservative viewpoints. As senator he introduced the COLLUDE Act to strip Section 230 immunity from platforms that censor speech at government direction, and chaired a Commerce Committee hearing on government censorship — directly defending free speech against government-industry collusion.",
              ["https://www.schmitt.senate.gov/media/press-releases/senator-schmitt-introduces-legislation-aimed-at-stopping-the-federal-governments-collusion-with-big-tech-to-censor-speech/",
               "https://en.wikipedia.org/wiki/Murthy_v._Missouri"]),
        claim("es2", "eric-schmitt", "industry_capture", 0, True,
              "As Missouri Attorney General, Schmitt filed multiple lawsuits against school districts and St. Louis County to halt COVID-19 mask mandates and public-health restrictions on indoor dining and gatherings, opposing government-medical-establishment capture of public policy. He was a leading opponent of government vaccine and mask mandates throughout the COVID-19 period, consistent with the rubric's concern about unelected pharmaceutical and regulatory capture.",
              ["https://en.wikipedia.org/wiki/Eric_Schmitt",
               "https://www.schmitt.senate.gov/about/"]),
    ]),

    # ---------------- Cindy Hyde-Smith (MS-R, US Senator) ----------------
    # Existing: sanctity_of_life/0 True, biblical_marriage/1 True, self_defense/1 True
    ("cindy-hyde-smith", "MS", "Senator", [
        claim("chs1", "cindy-hyde-smith", "election_integrity", 0, True,
              "One of only six senators to vote to object to Arizona's Electoral College certification on January 6, 2021, citing 'the erosion of integrity of the electoral process.' She also voted against certifying Pennsylvania's electoral votes, stating her constituents 'do not believe the presidential election was constitutional and cannot accept the Electoral College decision.' She later blocked Democrats' election-reform legislation as 'partisan political theater.'",
              ["https://www.hydesmith.senate.gov/hyde-smith-opposition-electoral-college-vote-certification",
               "https://en.wikipedia.org/wiki/Cindy_Hyde-Smith"]),
        claim("chs2", "cindy-hyde-smith", "border_immigration", 3, True,
              "A strong proponent of nationwide E-Verify implementation, supporting legislation to require employers to verify workers' legal status and deny American jobs to those in the country illegally. Hyde-Smith states that the federal government's first responsibility is defense of the American people, and she has introduced legislation to prevent those here illegally from improperly collecting government-funded tax credits.",
              ["https://www.hydesmith.senate.gov/issues/border-security",
               "https://en.wikipedia.org/wiki/Cindy_Hyde-Smith"]),
    ]),

    # ---------------- John Kennedy (LA-R, US Senator) ----------------
    # Existing: self_defense/1 True, sanctity_of_life/0 True, foreign_policy_restraint/1 False
    ("john-kennedy", "LA", "Senator", [
        claim("jk4", "john-kennedy", "economic_stewardship", 2, True,
              "Kennedy received an 'A+' rating from Susan B. Anthony Pro-Life America and consistently opposes deficit spending. He helped lead the effort to defund Planned Parenthood and has pushed to offset Ukraine aid with seized Russian assets rather than new U.S. appropriations. His fiscal priorities center on using existing resources responsibly rather than expanding government debt.",
              ["https://www.kennedy.senate.gov/public/2025/1/kennedy-receives-a-rating-from-susan-b-anthony-pro-life-america-for-standing-for-life",
               "https://en.wikipedia.org/wiki/John_Kennedy_(Louisiana_politician)"]),
        claim("jk5", "john-kennedy", "sanctity_of_life", 4, True,
              "Kennedy consistently votes to defund Planned Parenthood and cosponsored multiple bills prohibiting taxpayer dollars from going to Planned Parenthood. He also cosponsored the Born-Alive Abortion Survivors Protection Act and No Taxpayer Funding for Abortion Act, earning a record 'A+' rating from SBA Pro-Life America in both January 2024 and January 2025.",
              ["https://www.kennedy.senate.gov/public/2024/1/kennedy-receives-a-rating-for-championing-pro-life-values",
               "https://sbaprolife.org/senator/john-kennedy"]),
    ]),

    # ---------------- Maggie Hassan (NH-D, US Senator) ----------------
    # Existing: sanctity_of_life/0 False, self_defense/1 False, economic_stewardship/2 False
    ("maggie-hassan", "NH", "Senator", [
        claim("mh4", "maggie-hassan", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (2022), which federally codifies same-sex marriage and requires all states to recognize such unions, rejecting the one-man-one-woman definition. Hassan celebrated the bill's passage, stating it 'reaffirms freedom principles' and 'sends a message that love should not carry stigma or shame.' She holds a 100% rating from the Human Rights Campaign and as New Hampshire's state Senate majority leader helped make it the first state to legalize same-sex marriage legislatively.",
              ["https://www.hassan.senate.gov/news/press-releases/senator-hassan-statement-celebrating-senate-passage-of-marriage-equality-protections",
               "https://en.wikipedia.org/wiki/Maggie_Hassan"]),
        claim("mh5", "maggie-hassan", "sanctity_of_life", 4, False,
              "Met with Planned Parenthood of Northern New England leadership in April 2025 to discuss the impact of the Trump Administration's decision to pull Title X federal funding; cosponsored the EACH Act to guarantee abortion coverage for millions of Americans; and as governor worked to preserve state funding for Planned Parenthood — placing her squarely within the abortion-industry endorsement and funding network the rubric opposes.",
              ["https://www.hassan.senate.gov/news/press-releases/shaheen-hassan-help-reintroduce-each-act-to-guarantee-abortion-coverage-for-millions-of-americans",
               "https://en.wikipedia.org/wiki/Maggie_Hassan"]),
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
