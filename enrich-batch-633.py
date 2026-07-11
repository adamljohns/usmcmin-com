#!/usr/bin/env python3
"""Enrichment batch 633: hand-curated claims for 2 Oklahoma State Senators.

Senators: Aaron Reinhardt (SD-37), Adam Pugh (SD-41).
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
    # --- Aaron Reinhardt (OK SD-37, State Senator — Jenks) ---
    ("aaron-reinhardt", "OK", "State Senator", [
        claim("ar1", "aaron-reinhardt", "self_defense", 0, True,
              "Reinhardt voted AYE on SB 500 (2025), the Firearm Industry Non-Discrimination Act, prohibiting Oklahoma public entities from contracting with businesses (10+ employees, contracts $100k+) that discriminate against the firearm industry; the Senate passed it 38-8 and Gov. Stitt signed it August 11, 2025.",
              ["https://www.nraila.org/articles/20250328/oklahoma-firearm-non-discrimination-bill-passes-senate",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB500_VOTES.HTM"]),
        claim("ar2", "aaron-reinhardt", "biblical_marriage", 2, True,
              "Reinhardt voted AYE on SB 904 (2026), prohibiting all Oklahoma public funds including Medicaid/SoonerCare from covering gender-transition procedures for minors or adults, and barring state property from being used for such procedures; the Senate passed it 39-8 and Gov. Stitt signed it May 14, 2026 with an emergency clause.",
              ["https://oksenate.gov/press-releases/senate-approves-gollihare-bill-prohibiting-medicaid-funding-gender-transition",
               "https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/SB904_VOTES.HTM"]),
        claim("ar3", "aaron-reinhardt", "family_child_sovereignty", 0, True,
              "Reinhardt voted AYE on HB 3705 (2026), expanding Oklahoma's Parental Choice Tax Credit cap from $250M to $275M and providing refundable tax credits of $5,000-$7,500 per student to families choosing private schools; the Senate passed it 39-9 on April 27, 2026, and Gov. Stitt signed it May 13, 2026.",
              ["https://oklahoma.gov/governor/newsroom/newsroom/2026/governor-stitt-signs-bill-delivering-more-education-freedom-for-oklahoma-families.html",
               "https://ocpathink.org/post/independent-journalism/stitt-signs-law-boosting-school-choice-opportunities"]),
    ]),

    # --- Adam Pugh (OK SD-41, State Senator — Edmond) ---
    ("adam-pugh", "OK", "State Senator", [
        claim("ap1", "adam-pugh", "sanctity_of_life", 0, True,
              "Pugh was the prime sponsor of SB 647 (2021), 'Lily's Law,' requiring all birthing centers and medical facilities to maintain a written policy allowing families to direct the disposition of remains of a stillborn or miscarried child, extending those protections to losses before 12 weeks gestation; Gov. Stitt signed it into law.",
              ["https://oksenate.gov/press-releases/senate-approves-lilys-law-protects-rights-grieving-families",
               "https://kfor.com/news/oklahoma-legislature/stitt-signs-lilys-law-to-protect-grieving-families/"]),
        claim("ap2", "adam-pugh", "self_defense", 0, True,
              "Pugh voted AYE on HB 2597 (2019), Oklahoma's constitutional carry bill establishing permitless concealed or open carry for Oklahomans 21+ (18+ for military); the Senate passed it 40-6 with all Republicans voting yes and Gov. Stitt signed it as his first bill on February 27, 2019, effective November 1, 2019.",
              ["https://oklahoma.gov/governor/newsroom/newsroom/2019/february/governor-kevin-stitt-signs-legislation-to-establish-constitution.html",
               "https://legiscan.com/OK/rollcall/HB2597/id/809860"]),
        claim("ap3", "adam-pugh", "family_child_sovereignty", 0, True,
              "Pugh voted YES on HB 1775 (2021), the Oklahoma Dignity in Education Act prohibiting public schools from requiring students to affirm race- or sex-based concepts such as collective guilt or inherent racial privilege; the Senate passed it 38-9 on strict party lines and Gov. Stitt signed it May 7, 2021.",
              ["https://legiscan.com/OK/bill/HB1775/2021",
               "http://webserver1.lsb.state.ok.us/cf/2021-22%20SUPPORT%20DOCUMENTS/votes/Senate/HB1775_VOTES.HTM"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
