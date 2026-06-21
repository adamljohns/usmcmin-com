#!/usr/bin/env python3
"""Enrichment batch 332: 14 claims across 5 sitting U.S. Senators.

Targets: Catherine Cortez Masto (NV-D), Martin Heinrich (NM-D),
Ben Ray Luján (NM-D), Andy Kim (NJ-D), Jeanne Shaheen (NH-D).
All evidence_curated with 3 existing claims; adds 2-3 claims each
covering distinct rubric categories not yet represented per candidate.

Sourced from ballotpedia.org, en.wikipedia.org, official *.senate.gov,
congress.gov, govtrack.us.
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
    # ---------- Catherine Cortez Masto (NV-D, US Senator) ----------
    ("catherine-cortez-masto", "NV", "Senator", [
        claim("ccm4", "catherine-cortez-masto", "border_immigration", 1, False,
              "Opposes mandatory deportation enforcement; in March 2025 co-led a letter with 39 Democratic colleagues to DHS Secretary Noem and USCIS Director Edlow demanding DHS maintain DACA renewal processing. Previously sponsored the Protect Vulnerable Immigrant Youth Act (S.1885, 2023) and the Fairness for Immigrant Families Act (S.819, 2023), both prioritizing pathways to legal status over removal.",
              ["https://ballotpedia.org/Catherine_Cortez_Masto",
               "https://www.cortezmasto.senate.gov/"]),
        claim("ccm5", "catherine-cortez-masto", "foreign_policy_restraint", 1, False,
              "Voted for the April 2024 $95B bipartisan national security supplemental (P.L.118-50) providing military aid to Ukraine, Israel, and Taiwan; also introduced an amendment to exempt those allies from Trump-era tariffs — consistently supporting open-ended U.S. overseas military commitments rather than the drawdown the rubric calls for.",
              ["https://www.cortezmasto.senate.gov/news/press-releases/new-cortez-masto-votes-to-pass-bipartisan-national-security-package/",
               "https://en.wikipedia.org/wiki/Catherine_Cortez_Masto"]),
        claim("ccm6", "catherine-cortez-masto", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan Act (March 2021, $1.9 trillion in deficit-financed spending) and the Inflation Reduction Act (August 2022); as Senate Democratic Outreach Vice Chair championed major spending legislation without accompanying budget-neutral offsets — at odds with the rubric's balanced-budget and anti-deficit standard.",
              ["https://www.govtrack.us/congress/members/catherine_cortez_masto/412681",
               "https://en.wikipedia.org/wiki/Catherine_Cortez_Masto"]),
    ]),

    # ---------- Martin Heinrich (NM-D, US Senator) ----------
    ("martin-heinrich", "NM", "Senator", [
        claim("mh4", "martin-heinrich", "biblical_marriage", 0, False,
              "Cosponsored the Respect for Marriage Act and issued a press release upon its December 2022 signing celebrating it as 'Love is Love is now the Law of the Land' — rejecting the one-man-one-woman marriage definition the rubric upholds.",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/heinrich-on-historic-respect-for-marriage-act-love-is-love-is-now-the-law-of-the-land",
               "https://en.wikipedia.org/wiki/Martin_Heinrich"]),
        claim("mh5", "martin-heinrich", "foreign_policy_restraint", 1, False,
              "Voted for the April 2024 $95B national security supplemental providing military assistance to Ukraine, Israel, and Taiwan; has consistently supported U.S. military engagement abroad and U.S. security commitments rather than repealing AUMFs or winding down foreign entanglements.",
              ["https://www.govtrack.us/congress/members/martin_heinrich/412281",
               "https://en.wikipedia.org/wiki/Martin_Heinrich"]),
        claim("mh6", "martin-heinrich", "economic_stewardship", 2, False,
              "Voted for the Inflation Reduction Act (2022) and the Infrastructure Investment and Jobs Act (2021), large spending packages adding hundreds of billions to the federal debt; as JEC Chairman called publicly for Federal Reserve rate cuts to stimulate further economic activity rather than restraining federal borrowing.",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/heinrich-votes-for-historic-inflation-reduction-act-to-lower-costs-for-americans-invest-in-health-care-and-climate-action",
               "https://www.jec.senate.gov/public/index.cfm/democrats/2024/6/jec-chairman-heinrich-it-s-time-for-the-fed-to-lower-interest-rates"]),
    ]),

    # ---------- Ben Ray Luján (NM-D, US Senator) ----------
    ("ben-ray-lujan", "NM", "Senator", [
        claim("brl4", "ben-ray-lujan", "border_immigration", 0, False,
              "Opposes border wall construction and enforcement-first immigration approaches; his Senate immigration page advocates for comprehensive reform including DACA protections. When voting for the 2024 national security supplemental that included immigration enforcement provisions, he stated he found those provisions 'far from perfect' and had 'consistently voiced concern over the lack of input from Hispanic and border-state lawmakers.'",
              ["https://www.lujan.senate.gov/about/issues/immigration/",
               "https://www.lujan.senate.gov/newsroom/press-releases/lujan-statement-on-national-security-supplemental-vote/"]),
        claim("brl5", "ben-ray-lujan", "foreign_policy_restraint", 1, False,
              "Voted to advance the April 2024 $95B bipartisan national security supplemental providing aid to Ukraine, Israel, and Taiwan, stating it was 'necessary for Congress to address the situation'; consistently supports U.S. overseas military commitments.",
              ["https://www.lujan.senate.gov/newsroom/press-releases/lujan-statement-on-national-security-supplemental-vote/",
               "https://en.wikipedia.org/wiki/Ben_Ray_Luj%C3%A1n"]),
        claim("brl6", "ben-ray-lujan", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan ($1.9T, 2021), the Inflation Reduction Act (2022), the CHIPS and Science Act (2022), and the Infrastructure Investment and Jobs Act (2021) — large deficit-financed federal spending bills contrary to the rubric's balanced-budget standard.",
              ["https://www.govtrack.us/congress/members/ben_lujan/412293",
               "https://en.wikipedia.org/wiki/Ben_Ray_Luj%C3%A1n"]),
    ]),

    # ---------- Andy Kim (NJ-D, US Senator) ----------
    ("andy-kim", "NJ", "Senator", [
        claim("ak4", "andy-kim", "border_immigration", 1, False,
              "Voted against the Laken Riley Act (S.5, January 2025), which would have required mandatory ICE detention for undocumented immigrants arrested for theft, burglary, or violent crimes; released a statement citing 'constitutional concerns' with the bill's due-process provisions, instead calling for more immigration judges to establish an orderly asylum adjudication process.",
              ["https://www.kim.senate.gov/senator-kim-statement-on-the-constitutional-problems-of-s-5-immigration-bill/",
               "https://en.wikipedia.org/wiki/Andy_Kim_(politician)"]),
        claim("ak5", "andy-kim", "economic_stewardship", 2, False,
              "As a House member (2019–2024), voted for the American Rescue Plan ($1.9T, 2021) and the Inflation Reduction Act (2022); since entering the Senate in December 2024, has supported continued federal spending programs without offsetting revenue — contrary to the rubric's balanced-budget standard.",
              ["https://www.govtrack.us/congress/members/andy_kim/412797",
               "https://en.wikipedia.org/wiki/Andy_Kim_(politician)"]),
    ]),

    # ---------- Jeanne Shaheen (NH-D, US Senator) ----------
    ("jeanne-shaheen", "NH", "Senator", [
        claim("js4", "jeanne-shaheen", "border_immigration", 1, True,
              "Broke with most Senate Democrats to vote for the Laken Riley Act (S.5, 2025), which mandates ICE detention for undocumented immigrants arrested for theft, burglary, or violent crimes — making her one of only 12 Senate Democrats to vote for the bipartisan enforcement measure, partially aligning with the rubric's mandatory-detention standard.",
              ["https://ballotpedia.org/Jeanne_Shaheen",
               "https://en.wikipedia.org/wiki/Jeanne_Shaheen"]),
        claim("js5", "jeanne-shaheen", "biblical_marriage", 0, False,
              "Sponsored the Respect for Marriage Act (2022), which federally codified same-sex and interracial marriage and repealed DOMA; released a statement calling the legislation's Senate advancement 'crucial' — directly rejecting the one-man-one-woman definition the rubric upholds.",
              ["https://www.shaheen.senate.gov/news/press/shaheen-statement-on-advancement-of-crucial-marriage-equality-legislation",
               "https://en.wikipedia.org/wiki/Jeanne_Shaheen"]),
        claim("js6", "jeanne-shaheen", "economic_stewardship", 2, False,
              "Voted for the American Rescue Plan (2021, $1.9T) and the Inflation Reduction Act (2022), both adding to the federal debt; while she has publicly expressed concern about the $1 trillion annual federal interest payment and co-introduced a Bipartisan Fiscal Commission Act, her overall voting record reflects consistent support for large deficit-financed spending packages.",
              ["https://www.shaheen.senate.gov/about/priorities/fiscal-responsibility",
               "https://ballotpedia.org/Jeanne_Shaheen"]),
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
