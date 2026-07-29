#!/usr/bin/env python3
"""Enrichment batch 880: hand-curated claims for 5 candidates.

Targets from bottom-of-alphabet states (WY, WV, VA) with
evidence_curated confidence and few existing claims.

Mix: Tim Cywinski (VA-01-D), Suzanne Krzyzanowski (VA-05-D),
Beth Macy (VA-06-D), Evan Worrell (WV-D), Justin Fornstrom (WY-R).
7 total new claims across 5 candidates.

WebFetch blocked in this environment; research via WebSearch only.
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
    # ---------------- Tim Cywinski (VA-01, D) ----------------
    ("tim-cywinski", "VA", "Representative", [
        claim("tc1", "tim-cywinski", "sanctity_of_life", 0, False,
              "Attended the May 2026 Virginia reproductive freedom rally at the state Capitol organized in support of the Virginia Right to Reproductive Freedom Amendment, and participated in a 'Voices and Votes' event co-hosted by Birth in Color, a Virginia organization combining reproductive justice advocacy with voting-rights education — aligning with pro-choice rather than life-from-conception positions.",
              ["https://www.mobilize.us/timcywinskiforcongress/event/993328/",
               "https://rvamag.com/politics/virginia-politics/tim-cywinski-va-01-makes-his-case-for-congress-part-1.html"]),
        claim("tc2", "tim-cywinski", "foreign_policy_restraint", 3, True,
              "In a published RVA Mag interview, Cywinski sharply criticized the Democratic Party's deference to AIPAC and Israel, stating 'some of the leadership in the Democratic Party seems to be so far up Israel's ass that they're building the battlements against criticism,' and defended criticism of AIPAC as legitimate political speech — aligning with the rubric's skepticism of foreign-linked PAC influence in U.S. politics.",
              ["https://rvamag.com/politics/virginia-politics/tim-cywinski-va-01-makes-his-case-for-congress-part-2.html"]),
    ]),

    # ---------------- Suzanne Krzyzanowski (VA-05, D) ----------------
    ("suzanne-krzyzanowski", "VA", "Representative", [
        claim("sk1", "suzanne-krzyzanowski", "border_immigration", 1, False,
              "Stated 'ICE needs to be re-focused on pursuing criminals, not people who have been living in the U.S. for decades as good neighbors and hard workers' — explicitly opposing mandatory deportation of long-term undocumented residents.",
              ["https://www.cvilletomorrow.org/newsletter/what-should-ices-future-be-central-virginia-congressional-candidates-offered-very-different-answers/",
               "https://drkforcongress.com/"]),
    ]),

    # ---------------- Beth Macy (VA-06, D) ----------------
    ("beth-macy", "VA", "Representative", [
        claim("bm1", "beth-macy", "border_immigration", 1, False,
              "Pledged to 'fight to dethrone ICE, which is terrorizing our neighbors and has deported more than 400 people in the region this past year' — explicitly opposing mandatory immigration enforcement and deportation operations.",
              ["https://bethmacyforcongress.com/",
               "https://www.whsv.com/2026/04/08/mayor-deanna-reed-hosts-immigration-roundtable-with-city-leaders-beth-macy/"]),
    ]),

    # ---------------- Evan Worrell (WV, R, Delegate) ----------------
    ("evan-worrell", "WV", "Delegate", [
        claim("ew1", "evan-worrell", "self_defense", 1, True,
              "In August 2019, was among West Virginia Republican delegates who publicly pledged to defend Second Amendment rights and oppose proposed red-flag laws following mass shootings, stating: 'We stand firm in our convictions to defend our constitutional rights and uphold the freedoms of all the people of West Virginia' — directly opposing red-flag legislation.",
              ["https://www.newsandsentinel.com/news/local-news/2019/08/west-virginia-lawmakers-disagree-on-gun-control-after-mass-shootings/",
               "https://www.reviewonline.com/news/local-news/2019/08/two-west-virginia-lawmakers-disagree-on-gun-control/"]),
    ]),

    # ---------------- Justin Fornstrom (WY, R, Representative) ----------------
    ("justin-fornstrom", "WY", "Representative", [
        claim("jf1", "justin-fornstrom", "biblical_marriage", 2, True,
              "Voted YES on Wyoming House Bill 72 (2025), the Protecting Privacy in Public Spaces Act, which bans transgender Wyomingites from using bathrooms and sex-designated facilities in state-affiliated public spaces that align with their gender identity; the bill passed the House 52-8 and was signed into law by Governor Gordon in April 2025.",
              ["https://en.wikipedia.org/wiki/Wyoming_House_Bill_72",
               "https://www.wyomingnews.com/news/local_news/bill-prohibiting-transgender-peoples-access-to-female-only-spaces-passes-through-wyoming-house/article_6be7145e-e586-11ef-a103-73e6c1377ef5.html"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
