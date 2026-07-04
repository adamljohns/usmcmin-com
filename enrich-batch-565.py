#!/usr/bin/env python3
"""Enrichment batch 565: 4 WI Republican State Assembly Members, 8 claims.

All archetype_curated federal and state slots from the bottom of the alphabet
(WY, WV) are exhausted. This batch takes the next available bottom-of-alphabet
targets: Wisconsin Republican Assembly Members with 0 claims.

Candidates (all WI, R, 'State Assembly Member'):
  Chanz Green      (District 74 — Duluth/Superior border region)
  Amanda Nedweski  (District 32 — Pleasant Prairie/Kenosha County)
  Alex Dallman     (District 39 — Green Lake/Marquette County)
  Adam Neylon      (District 15 — Pewaukee/Waukesha County)

Rubric categories covered:
  Green     — self_defense[0], sanctity_of_life[0]
  Nedweski  — family_child_sovereignty[0], biblical_marriage[2]
  Dallman   — sanctity_of_life[0], economic_stewardship[2]
  Neylon    — biblical_marriage[2], election_integrity[0]
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
    # -------- Chanz Green (WI-74, R, State Assembly Member) --------
    ("chanz-green-wi-74", "WI", "Assembly Member", [
        claim("cg1", "chanz-green-wi-74", "self_defense", 0, True,
              "Led introduction of 2025 Wisconsin Assembly Bill 609 (October 29, 2025), which would eliminate Wisconsin's permit requirement for concealed carry and affirm the right of every law-abiding adult to carry concealed without a government license — making Wisconsin a constitutional-carry state. Green stated: 'As a gun owner and a proud advocate for the Second Amendment, I don't feel that me having to get a permit to conceal and carry is necessary.' The bill received an NRA-supported public hearing before the Assembly Committee on State Affairs in January 2026.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab609",
               "https://www.nraila.org/articles/20260105/wisconsin-committee-to-hear-permitless-carry-legislation"]),
        claim("cg2", "chanz-green-wi-74", "sanctity_of_life", 0, True,
              "Cosponsored 2025 Wisconsin Assembly Bill 382 (introduced July 31, 2025), which requires health care providers present at the delivery of a child born alive following an abortion or attempted abortion to render the same degree of professional medical care as would be provided to any other newborn at the same gestational age — and makes intentional killing of such a child a felony carrying life imprisonment, the same penalty as first-degree intentional homicide. The bill recognizes the personhood and full legal protection of every child born alive.",
              ["https://legiscan.com/WI/bill/AB382/2025",
               "https://docs.legis.wisconsin.gov/2025/proposals/ab382"]),
    ]),

    # -------- Amanda Nedweski (WI-32, R, State Assembly Member) --------
    ("amanda-nedweski-wi-32", "WI", "Assembly Member", [
        claim("amn1", "amanda-nedweski-wi-32", "family_child_sovereignty", 0, True,
              "Primary author of 2025 Wisconsin Assembly Bill 677, creating a new felony crime of 'grooming a child for sexual activity.' The bill arose from the Kenosha educator scandal and passed the Assembly 93–6 with overwhelming bipartisan support. It was signed into law as 2025 Wisconsin Act 88 on March 6, 2026, making Wisconsin one of the first states with an explicit anti-grooming criminal statute protecting children from predatory adults in positions of trust.",
              ["https://docs.legis.wisconsin.gov/2025/proposals/ab677",
               "https://kenoshacountyeye.com/2026/03/06/new-wisconsin-law-criminalizing-child-grooming-signed-reform-fueled-by-kenosha-scandal-first-exposed-by-kenosha-county-eye/",
               "https://www.wispolitics.com/2026/rep-nedweski-anti-grooming-bill-passes-assembly-with-overwhelming-support/"]),
        claim("amn2", "amanda-nedweski-wi-32", "biblical_marriage", 2, True,
              "Cosponsored and championed 2025 Wisconsin Assembly Bill 104 ('Help Not Harm Act'), which prohibits licensed health care providers from performing gender-transition medical interventions — including puberty blockers, cross-sex hormones, and surgical procedures — on any individual under 18 years of age. The Assembly passed it 50–43 on March 20, 2025; the Senate concurred 18–15 on February 11, 2026; enacted into law February 16, 2026. Nedweski declared: 'Protect kids, not profits.'",
              ["https://legiscan.com/WI/bill/AB104/2025",
               "https://docs.legis.wisconsin.gov/2025/related/enrolled/ab104.pdf",
               "https://www.wispolitics.com/2026/rep-nedweski-protect-kids-not-profits-nedweski-urges-action-after-medical-industry-reversal/"]),
    ]),

    # -------- Alex Dallman (WI-39, R, State Assembly Member) --------
    ("alex-dallman-wi-39", "WI", "Assembly Member", [
        claim("ald1", "alex-dallman-wi-39", "sanctity_of_life", 0, True,
              "Co-introduced 2023–2024 Wisconsin Assembly Bill 975 (January 19, 2024), which would have prohibited abortion after 14 weeks post-fertilization, with limited medical emergency exceptions, conditioned on a public referendum — affirming the state's interest in protecting unborn human life. The Assembly passed AB 975 on April 15, 2024. Dallman joined dozens of Assembly Republicans in recognizing the humanity of the unborn from early development.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/reg/asm/bill/ab975",
               "https://legiscan.com/WI/rollcall/AB975/id/1369066"]),
        claim("ald2", "alex-dallman-wi-39", "economic_stewardship", 2, True,
              "As a member of Wisconsin's Joint Committee on Finance (JFC), co-led the removal of over 600 of Governor Evers' proposed spending increases and regulatory expansions from the 2025–27 biennial state budget, returning it to base funding levels. The resulting budget delivered a $1.5 billion income tax cut by expanding the 4.4% bracket. Dallman stated: 'Today, the Joint Committee on Finance returned to our state's base budget by removing over 600 of the Governor's proposals that would have massively increased spending and taxes.'",
              ["https://www.wispolitics.com/2025/rep-dallman-dallman-and-the-joint-committee-on-finance-return-to-base-budget/",
               "https://www.riponpress.com/news/dallman-state-budget-delivers-results-for-wisconsin/article_b25c5077-a9d5-4d3c-936e-f90bb564bbf0.html"]),
    ]),

    # -------- Adam Neylon (WI-15, R, State Assembly Member) --------
    ("adam-neylon-wi-15", "WI", "Assembly Member", [
        claim("adn1", "adam-neylon-wi-15", "biblical_marriage", 2, True,
              "Cosponsored 2025 Wisconsin Assembly Bill 104 ('Help Not Harm Act'), prohibiting licensed health care providers from performing gender-transition medical interventions — puberty blockers, cross-sex hormones, or surgical procedures — on individuals under 18. Passed Assembly 50–43 (March 20, 2025) and Senate 18–15 (February 11, 2026); enacted into law February 16, 2026. As Co-Chairman of the Joint Committee for Review of Administrative Rules, Neylon also oversees compliance of state health agency rules with this prohibition.",
              ["https://legiscan.com/WI/bill/AB104/2025",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab104.pdf"]),
        claim("adn2", "adam-neylon-wi-15", "election_integrity", 0, True,
              "As Co-Chairman of Wisconsin's Joint Committee for Review of Administrative Rules (JCRAR), publicly challenged the Wisconsin Elections Commission for unilaterally drafting election observer rules without adequate legislative input, stating 'I feel a little bit like you didn't even try here' and calling the Commission's exclusion of legislators 'insulting.' He also co-authored 2025 Assembly Bill 268, which broadens complainants' right to appeal Wisconsin Elections Commission decisions regarding election officials' conduct.",
              ["https://www.wispolitics.com/2025/jcrar-co-chair-knocks-elections-commission-for-not-getting-more-lawmaker-input-on-observer-rules/",
               "https://legiscan.com/WI/bill/AB268/2025",
               "https://docs.legis.wisconsin.gov/2025/related/proposals/ab268"]),
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
