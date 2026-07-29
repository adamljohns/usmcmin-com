#!/usr/bin/env python3
"""Enrichment batch 895: sitting U.S. Representatives — Texas (bottom-of-alphabet).

Adds 2 new claims per candidate from uncovered rubric categories. archetype_curated
federal senator/rep buckets are exhausted; targets are evidence_curated TX US Reps
with 5 existing claims and documented gaps in biblical_marriage, election_integrity,
and family_child_sovereignty.

Targets: Lance Gooden (TX-5-R), Brian Babin (TX-36-R), Michael Cloud (TX-27-R),
Keith Self (TX-3-R), August Pfluger (TX-11-R).

Sources: govtrack.us roll-call votes, congress.gov, official .house.gov press releases,
Texas Tribune news record, Wikipedia legislator pages.
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
    # ---------------- Lance Gooden (TX-5, R, US Representative) ----------------
    ("lance-gooden", "TX", "Representative", [
        claim("lg1", "lance-gooden", "biblical_marriage", 0, True,
              "Voted NAY on H.R. 8404 (Respect for Marriage Act) on July 19, 2022 (House Vote #373, 267-157), one of the near-unanimous Texas Republican delegation to oppose codifying same-sex marriage in federal law — only Rep. Tony Gonzales of the Texas GOP broke ranks to vote YEA.",
              ["https://www.texastribune.org/2022/07/19/congress-same-sex-marriage-texas/",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("lg2", "lance-gooden", "biblical_marriage", 2, True,
              "Co-sponsored legislation introduced by Rep. Marjorie Taylor Greene in August 2022 to criminalize gender-affirming healthcare for transgender minors and the medical providers who perform such procedures — directly rejecting the transgender ideology the rubric opposes in public policy.",
              ["https://en.wikipedia.org/wiki/Lance_Gooden"]),
    ]),

    # ---------------- Brian Babin (TX-36, R, US Representative) ----------------
    ("brian-babin", "TX", "Representative", [
        claim("bb1", "brian-babin", "biblical_marriage", 0, True,
              "Declared himself a 'strong supporter of traditional marriage' in his official congressional statement responding to the Supreme Court's 2015 Obergefell v. Hodges ruling, explicitly affirming the one-man-one-woman definition and raising concerns that the decision would threaten religious liberty for faith-based institutions.",
              ["https://babin.house.gov/news/documentsingle.aspx?DocumentID=300"]),
        claim("bb2", "brian-babin", "biblical_marriage", 4, True,
              "In 2016, introduced H.R. 5294 (Student Privacy Protection and Safety Act) to invalidate the Obama administration's 'Dear Colleague Letter on Transgender Students,' which had directed public schools to allow students to use bathrooms matching their gender identity rather than their biological sex — one of the earliest legislative efforts against LGBTQ-ideology mandates in public schools.",
              ["https://en.wikipedia.org/wiki/Brian_Babin"]),
    ]),

    # ---------------- Michael Cloud (TX-27, R, US Representative) ----------------
    ("michael-cloud", "TX", "Representative", [
        claim("mc1", "michael-cloud", "biblical_marriage", 0, True,
              "Voted NAY on H.R. 8404 (Respect for Marriage Act) on July 19, 2022 (House Vote #373, 267-157), part of the overwhelming Texas Republican House delegation that opposed codifying same-sex marriage in federal law — only Rep. Tony Gonzales of San Antonio voted YEA among Texas GOP members.",
              ["https://www.texastribune.org/2022/07/19/congress-same-sex-marriage-texas/",
               "https://www.govtrack.us/congress/votes/117-2022/h373"]),
        claim("mc2", "michael-cloud", "biblical_marriage", 2, True,
              "Voted YEA on H.R. 734 (Protection of Women and Girls in Sports Act), which passed the House 219-203 on April 20, 2023 (House Vote #192), prohibiting biological males from competing in female athletic programs receiving federal funding under Title IX — affirming biological sex as the basis of women's sports and rejecting transgender-ideology policy.",
              ["https://www.govtrack.us/congress/votes/118-2023/h192",
               "https://www.congress.gov/bill/118th-congress/house-bill/734"]),
    ]),

    # ---------------- Keith Self (TX-3, R, US Representative) ----------------
    ("keith-self", "TX", "Representative", [
        claim("ks1", "keith-self", "biblical_marriage", 2, True,
              "Co-sponsored H.R. 734 (Protection of Women and Girls in Sports Act) in the 118th Congress, which passed the House 219-203 on April 20, 2023 (House Vote #192), banning biological males from competing in women's or girls' athletic programs receiving federal funding — a direct legislative rejection of transgender ideology in sports and Title IX policy.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/734/all-info",
               "https://www.govtrack.us/congress/votes/118-2023/h192"]),
        claim("ks2", "keith-self", "family_child_sovereignty", 0, True,
              "Voted YEA on H.R. 5 (Parents' Bill of Rights Act), which passed the House 213-208 on March 24, 2023, requiring public schools to disclose curricula to parents, notify parents of events affecting their children's wellbeing, allow parents to review school library materials, and forbid withholding information about a child's welfare — affirming parental rights against government-school overreach.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5",
               "https://www.govtrack.us/congress/bills/118/hr5"]),
    ]),

    # ---------------- August Pfluger (TX-11, R, US Representative) ----------------
    ("august-pfluger", "TX", "Representative", [
        claim("ap1", "august-pfluger", "election_integrity", 0, True,
              "Voted YEA on H.R. 22 (SAVE Act / Safeguard American Voter Eligibility Act), which passed the House 218-213 on February 11, 2026, requiring documentary proof of U.S. citizenship when registering to vote in federal elections. Pfluger also formally demanded the Biden-Harris administration take action to prevent noncitizens from being placed on Texas voter rolls.",
              ["https://pfluger.house.gov/news/documentsingle.aspx?DocumentID=2173",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("ap2", "august-pfluger", "family_child_sovereignty", 0, True,
              "Voted YEA on H.R. 5 (Parents' Bill of Rights Act), which passed the House 213-208 on March 24, 2023, requiring public schools to disclose curricula, notify parents of events affecting children, allow parents to review library and instructional materials, and prohibit concealing information about a child's welfare from parents — a core parental-rights protection against school-government overreach.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/5",
               "https://www.govtrack.us/congress/bills/118/hr5"]),
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
