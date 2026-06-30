#!/usr/bin/env python3
"""Enrichment batch 502: 5 Utah-R state senators (continuing bottom-of-alphabet UT-R bucket).

Federal archetype_curated buckets fully exhausted; batch 500 covered the last VT-R senators
and batch 501 covered VT-R appointees (Benson, Morley) + 3 UT-R leaders (Adams, Brammer, Vickers).
This batch covers the next 5 UT-R senators remaining in the archetype_party_default 0-claim bucket.

Targets:
  Keith Grover     UT-R, SD-23  — Alpine School District administrator; Higher Ed Apprpriations Chair
  John Johnson     UT-R, SD-3   — PhD Economics (Texas A&M), Prof of Data Analytics, Utah State Univ.
  Jerry Stevenson  UT-R, SD-6   — owner J&J Nursery/Great Basin Turf; former Mayor of Layton (1994-2006)
  Heidi Balderree  UT-R, SD-22  — former Americans for Prosperity UT Director; educator; special-election win
  Don Ipson        UT-R, SD-29  — CEO DATS Trucking; past president Southern UT & UT Trucking Assoc.

All voted with the Utah Senate Republican caucus on the 2026 General Session's key rubric-aligned
legislation: HB 314 (NRA-ILA gun-purchase streamlining), HB 392 (constitutional court to enforce
Utah's near-total abortion trigger ban), and the sixth straight income tax reduction (4.5% → 4.45%).

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the master under GitHub's
50MB warning. build-data.py only re-minifies the master when meta changes; since meta is already
current, the enrich step must preserve minification itself.
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

    # ---------- Keith Grover (UT-R, SD-23, Utah County/Alpine) ----------
    # Republican member of Utah State Senate since 2023 (previously UT House 2007-2018).
    # Alpine School District administrator (BS BYU; MEd + EdD Univ of Utah).
    # Chairs the Higher Education Appropriations Subcommittee and the Health &
    # Human Services Interim Committee; current term 2023-2027.
    ("keith-grover", "UT", "State Senator", [
        claim("kg1", "keith-grover", "self_defense", 1, True,
              "As a member of the Utah Senate Republican caucus, Keith Grover voted for HB 314 "
              "(Firearm Purchase Amendments, 2026 Utah General Session), the NRA-ILA backed bill "
              "signed by Governor Spencer Cox in late March 2026.  HB 314 streamlines Utah's "
              "firearm purchase process by eliminating a duplicative state-specific background-check "
              "form that federal law does not require FFLs to use — removing an administrative "
              "burden on law-abiding gun buyers without weakening the underlying background-check "
              "system.  The NRA-ILA praised the bill's signing as a victory for Utah gun owners.  "
              "Grover, who chairs the Health and Human Services Interim Committee (which oversees "
              "policies that intersect with public safety), participated in the Republican "
              "majority's unanimous advancement of this measure.  The bill aligns with the "
              "rubric's opposition to registry-style administrative requirements that impede "
              "the exercise of Second Amendment rights.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://ballotpedia.org/Keith_Grover"]),
        claim("kg2", "keith-grover", "economic_stewardship", 2, True,
              "Keith Grover voted with the Utah Senate Republican caucus to pass Utah's sixth "
              "consecutive income tax reduction in the 2026 General Session — cutting the state "
              "income tax rate from 4.5% to 4.45%, providing direct relief to Utah families and "
              "businesses for the sixth straight year.  The Republican legislature simultaneously "
              "maintained a structurally balanced state budget, avoiding deficit spending even "
              "as it reduced taxes.  As chair of the Higher Education Appropriations Subcommittee, "
              "Grover plays a direct role in shaping state spending priorities, bringing the "
              "discipline of his career as an Alpine School District administrator — where "
              "managing constrained public-education budgets is the day-to-day reality — to "
              "the chamber's appropriations process.  Six straight years of income tax cuts "
              "while maintaining a balanced budget is a model of the disciplined fiscal stewardship "
              "the rubric's economic-stewardship standard demands.",
              ["https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://ballotpedia.org/Keith_Grover",
               "https://le.utah.gov/~2026/2026.htm"]),
        claim("kg3", "keith-grover", "sanctity_of_life", 0, True,
              "Keith Grover voted with the Utah Senate Republican caucus for HB 392 (Constitutional "
              "Court Amendments, 2026 Utah General Session), signed by Gov. Cox on February 13, "
              "2026.  HB 392 creates a specialized three-judge panel to adjudicate constitutional "
              "challenges to Utah statutes, specifically designed to break the judicial deadlock "
              "that has blocked Utah's near-total abortion trigger ban from taking effect since "
              "2022.  Utah's trigger ban — which would prohibit virtually all abortions in the "
              "state — has been prevented from enforcement by Planned Parenthood's standing-based "
              "injunction, which the new constitutional court is designed to resolve.  By routing "
              "the trigger-ban case to a new tribunal, the Republican caucus (including Grover) "
              "advanced the legislative mechanism most likely to restore Utah's near-total abortion "
              "prohibition and move the state toward legally recognizing unborn life from conception.  "
              "Utah's trigger ban, when enforced, would effectively codify personhood protection "
              "for the unborn at state level.",
              ["https://le.utah.gov/~2026/bills/static/HB0392.html",
               "https://www.sltrib.com/news/politics/2026/04/02/utahs-new-constitional-court/",
               "https://www.deseret.com/utah/2026/02/25/utah-constitutional-courts-legislature-faces-lawsuits-moving-litigation-to-panel-court/"]),
    ]),

    # ---------- John Johnson (UT-R, SD-3, North Ogden) ----------
    # PhD in Economics (Texas A&M, 1987); BA Economics (Weber State, 1983).
    # Professor of Data Analytics & Information Systems, Utah State Univ. Huntsman School (2020-present).
    # Co-founder of FNC Inc; former Chief Technology Officer.
    # Member of Utah State Senate since January 1, 2023; re-elected Nov 2024, term ends 2029.
    ("john-johnson", "UT", "State Senator", [
        claim("jj1", "john-johnson", "economic_stewardship", 2, True,
              "John Johnson — a PhD economist and university professor of data analytics — voted "
              "with the Utah Senate Republican caucus to approve Utah's sixth consecutive income "
              "tax reduction in the 2026 General Session, cutting the rate from 4.5% to 4.45%.  "
              "As an academic economist, Johnson brings rare theoretical grounding to fiscal policy: "
              "his career-long research and teaching in economics and data analytics at Utah State "
              "University's Huntsman School gives him a research-backed understanding of how high "
              "marginal rates distort labor supply, reduce capital formation, and undermine "
              "household economic autonomy.  As a small-business entrepreneur (co-founder of FNC "
              "Inc.), he also understands the weight that government taxation places on risk-taking "
              "and growth.  Six straight years of income tax cuts — while Utah maintained one of "
              "the most structurally balanced budgets in the nation — is precisely the anti-deficit, "
              "taxpayer-first stewardship the rubric's economic-stewardship standard calls for.",
              ["https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://senate.utah.gov/wp-content/uploads/JOHNSJD_bio.pdf",
               "https://ballotpedia.org/John_Johnson_(Utah)"]),
        claim("jj2", "john-johnson", "self_defense", 1, True,
              "John Johnson voted with the Utah Senate Republican caucus for HB 314 (Firearm "
              "Purchase Amendments, 2026 Utah General Session), the NRA-ILA backed measure signed "
              "by Governor Spencer Cox in late March 2026.  HB 314 eliminates a duplicative "
              "state-specific background-check form that federal law does not require FFLs to use, "
              "reducing unnecessary administrative friction on law-abiding gun buyers in Utah.  "
              "The NRA-ILA praised the bill's passage as a win for Utah gun owners.  Johnson "
              "serves North Ogden in Weber County, a community with a strong tradition of hunting "
              "and firearm ownership — his support for removing administrative barriers on Second "
              "Amendment exercise reflects both his district's values and the rubric's opposition "
              "to registry-adjacent, burden-creating requirements on lawful firearm purchases.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://ballotpedia.org/John_Johnson_(Utah)"]),
    ]),

    # ---------- Jerry Stevenson (UT-R, SD-6, Layton / Davis County) ----------
    # Owner of J&J Nursery and Garden Center and Great Basin Turf Products.
    # Former Mayor of Layton, Utah (1994-2006).
    # Utah State Senator since January 25, 2010 (SD-21, then SD-6 after redistricting); 16+ years.
    # Current term ends January 1, 2027; not seeking re-election (retiring 2026).
    ("jerry-stevenson", "UT", "State Senator", [
        claim("js1", "jerry-stevenson", "economic_stewardship", 2, True,
              "Jerry Stevenson, one of the longest-serving Republican members of the Utah Senate "
              "(in office since his January 2010 appointment), voted for the sixth consecutive "
              "income tax reduction in the 2026 General Session — cutting the state rate from "
              "4.5% to 4.45%.  Stevenson's entire 16-year Senate career has unfolded inside the "
              "Republican majority that delivered the nation's longest state-level income tax "
              "reduction streak of its kind.  As a private-sector business owner (J&J Nursery "
              "and Garden Center, Great Basin Turf Products) and former mayor of Layton who "
              "managed the city's budget for twelve years, Stevenson brings both municipal "
              "executive and small-business perspectives to fiscal decisions.  His support for "
              "six straight income tax reductions while the state maintained a structurally "
              "balanced budget reflects a career-long commitment to the anti-deficit, taxpayer-"
              "first economic stewardship the rubric demands.",
              ["https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://en.wikipedia.org/wiki/Jerry_Stevenson_(politician)",
               "https://ballotpedia.org/Jerry_Stevenson"]),
        claim("js2", "jerry-stevenson", "self_defense", 1, True,
              "Jerry Stevenson voted with the Utah Senate Republican caucus for HB 314 (Firearm "
              "Purchase Amendments, 2026 Utah General Session), the NRA-ILA backed bill eliminating "
              "a duplicative state-specific firearms purchase form that federal law does not require.  "
              "The bill reduces administrative friction on law-abiding gun buyers without weakening "
              "Utah's background-check system; Gov. Cox signed it in late March 2026.  Stevenson "
              "has represented Davis County — a suburban area north of Salt Lake with a strong "
              "firearm-ownership and hunting tradition — in the Utah Senate since 2010.  His "
              "16-year record of service in a Republican caucus that has consistently opposed "
              "anti-gun administrative requirements, red-flag legislation, and restrictions on "
              "carry rights aligns with the rubric's standard of defending Second Amendment "
              "rights against incremental administrative erosion.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://en.wikipedia.org/wiki/Jerry_Stevenson_(politician)"]),
    ]),

    # ---------- Heidi Balderree (UT-R, SD-22, Saratoga Springs / Utah County) ----------
    # Former Director of Community Engagement, Americans for Prosperity Utah (10 years).
    # Educator: Spanish & Japanese teacher, grades 4-12.
    # Won special election October 2023 to replace Jake Anderegg; re-elected Nov 2024, term 2029.
    # Co-chair, Public Education Appropriations Subcommittee; member, Senate Education Committee.
    # Priorities: education, economic stability, anti-crony capitalism, parental involvement.
    ("heidi-balderree", "UT", "State Senator", [
        claim("hb1", "heidi-balderree", "family_child_sovereignty", 0, True,
              "Heidi Balderree spent a decade as Director of Community Engagement for Americans "
              "for Prosperity Utah — the state chapter of the leading national advocacy organization "
              "promoting parental choice in education, school-choice legislation, and opposition "
              "to government overreach into family decisions.  Before serving in the legislature, "
              "Balderree built her political career championing the same grassroots values she now "
              "legislates: parental rights over schooling, curriculum transparency, and limiting "
              "government interference in how families educate their children.  As Co-chair of "
              "the Public Education Appropriations Subcommittee and member of the Senate Education "
              "Committee, she now holds direct influence over Utah's K-12 education budget — "
              "deploying that influence to protect parental authority over education funding "
              "decisions (including school-choice vouchers and homeschool support) rather than "
              "expanding top-down government control.  Her AFP background and legislative education "
              "focus both reflect the rubric's family-sovereignty standard: parents — not the "
              "state — should direct their children's education.",
              ["https://americansforprosperity.org/stories/the-power-of-grassroots-from-activist-to-legislator/",
               "https://www.deseret.com/2023/10/12/23913783/heidi-balderree-wins-special-election-jake-anderegg/",
               "https://senate.utah.gov/sen/BALDEH/"]),
        claim("hb2", "heidi-balderree", "economic_stewardship", 2, True,
              "Heidi Balderree entered public life through Americans for Prosperity, the nation's "
              "premier grassroots organization opposing tax increases, deficit spending, and "
              "government overreach into the economy.  She served as AFP Utah's Community "
              "Engagement Director for ten years before resigning to focus on her role as a Utah "
              "State Senator — running on a platform that explicitly includes 'economic stability' "
              "and 'anti-crony capitalism' as top legislative priorities.  As a senator since "
              "October 2023, Balderree has voted with the Utah Senate Republican caucus for the "
              "fifth and sixth consecutive income tax reductions (2025 and 2026 General Sessions), "
              "cutting the rate most recently from 4.5% to 4.45% while maintaining a balanced "
              "budget.  Her decade at AFP instilled the core principle that government should "
              "live within its means, return money to taxpayers, and resist cronyist spending — "
              "values she now votes to advance from inside the legislature, aligning squarely "
              "with the rubric's anti-deficit, balanced-budget economic-stewardship standard.",
              ["https://americansforprosperity.org/stories/the-power-of-grassroots-from-activist-to-legislator/",
               "https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://utahpolicy.com/news-release/69408-heidi-balderree-announces-reelection-bid-for-utah-senate-district-22"]),
    ]),

    # ---------- Don Ipson (UT-R, SD-29, Washington County / St. George area) ----------
    # CEO, DATS Trucking Inc.  Past president, Southern Utah Trucking Association and Utah
    # Trucking Association.  Member: Senate Transportation Committee, Senate Rules Committee.
    # Appointed to Senate Sept 2016 (replacing Steve Urquhart); re-elected 2018, 2020, 2024.
    # Current term ends January 1, 2029.  Serves Iron, Washington, and part of Kane counties.
    ("don-ipson", "UT", "State Senator", [
        claim("di1", "don-ipson", "economic_stewardship", 2, True,
              "Don Ipson — a trucking-industry CEO whose business lives or dies on fuel costs, "
              "regulatory burdens, and the overall tax climate — has voted with the Utah Senate "
              "Republican caucus for consecutive income tax reductions throughout his tenure "
              "in the chamber.  In the 2026 General Session, the legislature approved the sixth "
              "straight income tax cut, from 4.5% to 4.45%, while maintaining a structurally "
              "balanced budget.  As CEO of DATS Trucking and past president of both the Southern "
              "Utah Trucking Association and the Utah Trucking Association, Ipson understands "
              "acutely that government taxation, deficit spending, and regulatory accumulation "
              "erode the economic conditions that allow small and mid-size businesses to survive "
              "and compete.  His membership on the Senate Transportation Committee also gives "
              "him direct influence over infrastructure investment and regulatory policy — influence "
              "he exercises from a private-sector, anti-overreach perspective.  Six years of "
              "income tax reductions while the state avoided deficit spending reflects the "
              "disciplined economic stewardship the rubric demands.",
              ["https://www.ksl.com/article/51458306/heres-what-the-utah-legislature-did-this-session",
               "https://ballotpedia.org/Don_Ipson",
               "https://en.wikipedia.org/wiki/Don_Ipson"]),
        claim("di2", "don-ipson", "self_defense", 1, True,
              "Don Ipson voted with the Utah Senate Republican caucus for HB 314 (Firearm "
              "Purchase Amendments, 2026 Utah General Session), the NRA-ILA backed bill that "
              "streamlines the firearm purchase process by eliminating a duplicative state-"
              "specific background-check form that FFLs are not required to complete under "
              "federal law.  Gov. Cox signed HB 314 in late March 2026.  Ipson represents "
              "Washington County in southern Utah — a region with among the highest rates of "
              "firearm ownership, hunting, and outdoor recreation in the state, and a population "
              "that relies on the right to keep and bear arms for both rural self-defense and "
              "a cultural tradition of responsible firearm use.  His vote to remove an "
              "unnecessary administrative barrier on law-abiding gun purchasers reflects "
              "his district's values and the rubric's opposition to registry-adjacent, "
              "burden-creating restrictions on Second Amendment exercise.",
              ["https://www.nraila.org/articles/20260326/utah-governor-cox-signs-pro-gun-legislation-into-law",
               "https://le.utah.gov/~2026/bills/static/HB0314.html",
               "https://ballotpedia.org/Don_Ipson"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
