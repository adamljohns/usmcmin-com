#!/usr/bin/env python3
"""Enrichment batch 631: hand-curated claims for 4 Utah State Representatives.

Targets archetype_party_default UT state reps with 0 claims (bottom of alphabet).
Federal archetype_curated senator/rep buckets are now fully drained.

Reps: Rex Shipp (UT-71), Stephanie Gricius (UT-50),
      R. Neil Walter (UT-74), Raymond P. Ward (UT-19).
Each claim cites reliable sources and reflects 2021-2026 voting record /
public positions.
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


TARGETS = [
    # --- Rex Shipp (UT HD-71, State Representative, R) ---
    ("rex-shipp", "UT", "State Representative", [
        claim("rs1", "rex-shipp", "self_defense", 0, True,
              "Shipp was a named co-sponsor of Utah HB60 (2021), the 'Conceal Carry Firearms Amendments' (constitutional carry) bill eliminating the permit requirement for adults 21+ to carry a concealed firearm; it passed the Utah House 54-19 on January 26, 2021, passed the Senate, and was signed by Gov. Spencer Cox, taking effect May 5, 2021.",
              ["https://le.utah.gov/~2021/bills/static/HB0060.html",
               "https://www.nraila.org/articles/20210505/utah-permitless-carry-goes-into-effect"]),
        claim("rs2", "rex-shipp", "biblical_marriage", 2, True,
              "Shipp sponsored HB174 (2026), 'Sex Characteristic Change Treatment Amendments,' permanently banning puberty blockers and cross-sex hormones for transgender minors in Utah; the bill passed the Utah House 54-15 and the Senate by supermajority, and was signed into law by Gov. Spencer Cox on March 18, 2026.",
              ["https://utahnewsdispatch.com/2026/02/05/utah-house-passes-ban-transgender-treatments-for-minors/",
               "https://universe.byu.edu/metro/utah-enacts-law-to-permanently-ban-transgender-treatment-for-minors"]),
    ]),

    # --- Stephanie Gricius (UT HD-50, State Representative, R) ---
    ("stephanie-gricius", "UT", "State Representative", [
        claim("sg1", "stephanie-gricius", "sanctity_of_life", 0, True,
              "Gricius sponsored HB256 (2023) to allow pregnant drivers to use the HOV lane, grounding the bill in Utah's existing legal recognition of unborn children as separate persons; she stated: 'Utah has recognized an unborn child as a separate person. We've done that with our abortion laws, we've done that with our homicide laws.' The bill passed the Utah House 49-23.",
              ["https://www.deseret.com/utah/2023/1/30/23572820/pregnant-women-able-use-hov-lane-carpool-lane-utah/",
               "https://www.ksl.com/article/50568659"]),
        claim("sg2", "stephanie-gricius", "family_child_sovereignty", 0, True,
              "Gricius sponsored HB200 (2024), 'Order for Life Sustaining Treatment Amendments,' requiring healthcare providers (physicians, nurses, physician assistants) to obtain a parent or guardian signature before designating a minor child as 'do not resuscitate'; the bill amends professional-conduct standards and took effect May 1, 2024.",
              ["https://le.utah.gov/~2024/bills/static/HB0200.html",
               "https://www.billtrack50.com/billdetail/1662446"]),
    ]),

    # --- R. Neil Walter (UT HD-74, State Representative, R) ---
    ("r-neil-walter", "UT", "State Representative", [
        claim("nw1", "r-neil-walter", "industry_capture", 3, True,
              "Walter sponsored HB138 (2025), 'Food Labeling Amendments,' requiring cultivated (lab-grown), plant-based, and insect-based meat substitutes to carry clear consumer labels, protecting Utah's traditional agriculture and livestock market from deceptive industry competition; the bill received bipartisan support and took effect May 7, 2025.",
              ["https://www.upr.org/utah-news/2025-02-18/utah-bill-would-require-more-labeling-for-cultivated-meat-products",
               "https://le.utah.gov/~2025/bills/static/HB0138.html"]),
        claim("nw2", "r-neil-walter", "family_child_sovereignty", 0, True,
              "Walter publicly opposes 'CRT and other ideologies that label children, ignore parent input, and attempt to re-educate the community,' has served on charter school boards for 11 years, and as Chair of the Utah House Education Committee (2025-2026) has advanced parent-driven education legislation, including homeschool-freedom bills that passed the House unanimously.",
              ["https://www.rneilwalter.com/",
               "https://le.utah.gov/~2025/bills/static/HB0209.html"]),
    ]),

    # --- Raymond P. Ward (UT HD-19, State Representative, R) ---
    ("raymond-p-ward", "UT", "State Representative", [
        claim("rpw1", "raymond-p-ward", "sanctity_of_life", 1, False,
              "Ward stated in 2024: 'I support the trigger law as written. It outlaws elective abortions, but has important exceptions for the life and health of the mother, and in cases of rape and incest, and when the fetus is found to have a fatal anomaly.' He also stated he would not support a six-week abortion ban, endorsing restrictions-with-exceptions rather than full abolition.",
              ["https://www.sltrib.com/news/politics/2024/10/17/utah-house-district-19-election/",
               "https://www.sltrib.com/news/politics/2024/06/08/incumbent-ray-ward-faces-gop/"]),
        claim("rpw2", "raymond-p-ward", "sanctity_of_life", 2, False,
              "When asked in his 2024 campaign about restricting in vitro fertilization, Ward answered 'No' and stated 'In vitro fertilization is an important way that people can have children,' explicitly opposing any limits on IVF despite the routine creation and discard of embryos the practice involves.",
              ["https://www.sltrib.com/news/politics/2024/10/17/utah-house-district-19-election/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
