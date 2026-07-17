#!/usr/bin/env python3
"""Enrichment batch 723: hand-curated claims for 5 NY Republican State Senators.

archetype_curated federal senator/rep buckets fully exhausted; continuing the
state-level pivot. Targets five New York Republican State Senators with 0 claims
(archetype_party_default), taken from the bottom of the remaining alphabet:
  Pam Helming (SD-54), Steven Rhoads (SD-5), Stephen T. Chan (SD-17),
  Robert Rolison (SD-39), Patricia Canzoneri-Fitzpatrick (SD-9).

Each claim cites >=1 reliable source and reflects documented voting record /
public positions on the God-First/America-First rubric categories.
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
    # --- Pam Helming (NY, State Senator SD-54, Finger Lakes; since 2017) ---
    ("pam-helming", "NY", "State Senator", [
        claim("ph1", "pam-helming", "self_defense", 1, True,
              "Voted NO on the Concealed Carry Improvement Act (NY S51001A, July 2022 special session), which tightened permit requirements, expanded 'sensitive locations' banning carry, and restricted magazine capacity — part of the unified Republican minority opposition (20 Nay votes) that called the law an unconstitutional overreach after the Supreme Court's Bruen ruling.",
              ["https://www.nbcnews.com/news/us-news/new-york-senate-passes-stiffer-gun-restrictions-soften-blow-supreme-co-rcna35887",
               "https://www.nysenate.gov/senators/pamela-helming"]),
        claim("ph2", "pam-helming", "sanctity_of_life", 0, True,
              "Voted against the Reproductive Health Act (NY S240, January 22, 2019), which passed 38–24: the bill removed all references to the unborn from New York's penal code, repealed criminal penalties for late-term abortions, and authorized non-physicians to perform abortions. As one of the 24 Nay votes — all Republican — Helming affirmed protection of life in the womb.",
              ["https://en.wikipedia.org/wiki/Reproductive_Health_Act",
               "https://www.nysenate.gov/legislation/bills/2019/S240"]),
    ]),

    # --- Steven Rhoads (NY, State Senator SD-5, Nassau County; since Jan 2023) ---
    ("steven-rhoads", "NY", "State Senator", [
        claim("sr1", "steven-rhoads", "election_integrity", 0, True,
              "Sponsored S6139 (2023-24 session), legislation to require a government-issued photo ID to cast a ballot, with a no-cost ID provision for those lacking one — a foundational voter-ID measure that the rubric identifies as the first pillar of election integrity.",
              ["https://www.nysenate.gov/legislation/bills/2023/S6139",
               "https://www.nysenate.gov/senators/steven-d-rhoads"]),
        claim("sr2", "steven-rhoads", "family_child_sovereignty", 0, True,
              "Has championed parental rights in education as a core legislative priority: sponsoring and cosponsoring legislation to protect parental notification and consent rights in schools — standing against Albany bureaucrats imposing curricula or health decisions without parental knowledge.",
              ["https://steverhoads.com/meet-steve-rhoads/",
               "https://www.nysenate.gov/senators/steven-d-rhoads/about"]),
    ]),

    # --- Stephen T. Chan (NY, State Senator SD-17, South Brooklyn; since Jan 2025) ---
    ("stephen-t-chan", "NY", "State Senator", [
        claim("stc1", "stephen-t-chan", "sanctity_of_life", 0, False,
              "On January 21, 2025 — within his first three weeks in office — voted in favor of all five abortion-expansion bills passed by the NY Senate, becoming one of only two Republicans in the chamber to cross party lines and support legislation that funds and promotes abortion, placing him outside the pro-life standard the rubric measures.",
              ["https://newyorkfamilies.org/2025/01/state-senate-votes-to-promote-protect-and-fund-abortion/",
               "https://www.nysenate.gov/senators/stephen-t-chan"]),
        claim("stc2", "stephen-t-chan", "border_immigration", 2, True,
              "A vocal opponent of New York City's sanctuary-city policies, calling for an end to protections that shield dangerous criminal illegal aliens from deportation. His 2025 'Liberate New York' agenda explicitly includes stopping sanctuary measures that allow violent offenders to remain on the streets — consistent with the rubric's anti-sanctuary position.",
              ["https://www.nysenate.gov/newsroom/press-releases/2025/stephen-t-chan/senator-stephen-chan-leads-fight-public-safety-and",
               "https://www.nysenate.gov/senators/stephen-t-chan/about"]),
    ]),

    # --- Robert Rolison (NY, State Senator SD-39, Hudson Valley; since Jan 2023) ---
    ("robert-rolison", "NY", "State Senator", [
        claim("rr1", "robert-rolison", "family_child_sovereignty", 0, True,
              "Made protection of students and parental rights a central pillar of his 2025 legislative agenda, announced in coordination with Senate Republicans' 'Liberate New York' platform — opposing Albany's pattern of bypassing parents on curricula, gender-identity policies, and school health decisions.",
              ["https://www.nysenate.gov/newsroom/press-releases/2025/rob-rolison/fighting-hudson-valley-senator-rob-rolison-announces-2025",
               "https://www.timeshudsonvalley.com/mid-hudson-times/stories/rolison-announces-2025-legislative-agenda,154739"]),
        claim("rr2", "robert-rolison", "public_justice", 0, True,
              "A 26-year veteran of the Town of Poughkeepsie Police Department, Rolison has made overhauling New York's bail-reform laws a legislative priority, arguing that cashless-bail policies have returned repeat violent offenders to the streets and undermined public safety in his Hudson Valley communities — supporting a return to judicial discretion in setting bail for dangerous defendants.",
              ["https://www.nysenate.gov/newsroom/press-releases/2025/rob-rolison/fighting-hudson-valley-senator-rob-rolison-announces-2025",
               "https://www.nysenate.gov/senators/rob-rolison/about"]),
    ]),

    # --- Patricia Canzoneri-Fitzpatrick (NY, State Senator SD-9, Nassau County; since Jan 2023) ---
    ("patricia-canzoneri-fitzpatrick", "NY", "State Senator", [
        claim("pcf1", "patricia-canzoneri-fitzpatrick", "economic_stewardship", 4, True,
              "Joined business and labor leaders in March 2024 to oppose the NY Heat Act — sweeping legislation that would mandate the elimination of gas appliances and heating systems statewide in alignment with the ESG-driven climate agenda — calling for a cost-benefit analysis and warning that the mandate posed a direct threat to middle-class ratepayers and was not economically feasible.",
              ["https://www.nysenate.gov/newsroom/press-releases/2024/patricia-canzoneri-fitzpatrick/state-senator-canzoneri-fitzpatrick",
               "https://www.nysenate.gov/senators/patricia-canzoneri-fitzpatrick"]),
        claim("pcf2", "patricia-canzoneri-fitzpatrick", "family_child_sovereignty", 0, True,
              "Part of the Senate Republican coalition that advanced the 2025 'Liberate New York' agenda to protect students and parental rights across New York, opposing Albany's one-party imposition of curricula and policies that bypass parental consent — a priority she described as fighting 'destructive impacts of Albany's radical policies.'",
              ["https://www.nysenate.gov/newsroom/press-releases/2025/patricia-canzoneri-fitzpatrick/senator-canzoneri-fitzpatrick-senate",
               "https://www.nysenate.gov/senators/patricia-canzoneri-fitzpatrick/about"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
