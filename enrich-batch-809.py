#!/usr/bin/env python3
"""Enrichment batch 809: 5 Utah State Representatives (Republican, archetype_party_default).

Federal archetype_curated bucket is fully exhausted; this batch moves to the next
available bottom-of-alphabet tier — UT state representatives reverse-sorted by name.
Targets: Jason B. Kyle (D-8), James A. Dunnigan (D-36), Jake Sawyer (D-9),
Douglas R. Welton (D-65), Doug Fiefia (D-48).

MINIFIED write preserved — separators=(",",":") — keeps scorecard.json ~35-36MB.
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
    # ---------------- Jason B. Kyle (UT-8, State Rep) ----------------
    ("jason-b-kyle", "UT", "Representative", [
        claim("jk1", "jason-b-kyle", "sanctity_of_life", 0, True,
              "States on his campaign website: 'The proper role of government includes protecting life, especially life that cannot defend itself. I will defend the most vulnerable.' He affirms life from conception and represents a Republican caucus that passed HB 467 (2023, banned abortion clinics, 56–14) and HB 560 (2024, tightened Utah's near-total abortion trigger law, 59–10).",
              ["https://www.jasonbkyle.com/",
               "https://ballotpedia.org/Jason_Kyle",
               "https://www.deseret.com/utah/2023/2/15/23601210/abortion-clinic-ban-bill-planned-parenthood-utah/"]),
        claim("jk2", "jason-b-kyle", "self_defense", 0, True,
              "Chief sponsor of HB 103 (2023 General Session), 'Weapon Possession Revisions,' clarifying that lawful use of a controlled substance under a valid prescription does not disqualify a person from possessing or carrying a firearm — closing an ambiguity that had been used to restrict gun rights. The bill passed the House 74–0 and Senate 26–0 before being signed into law, with backing from the Utah Shooting Sports Council.",
              ["https://le.utah.gov/~2023/bills/hbillint/HB0103S02.htm",
               "https://www.standard.net/news/government/2023/feb/14/utah-rep-jason-kyle-new-in-office-on-track-to-notch-first-legislative-triumph/",
               "https://utahshootingsportscouncil.org/legislation-2023-bills/"]),
        claim("jk3", "jason-b-kyle", "border_immigration", 3, True,
              "Publicly backed Utah's 2025 E-Verify expansion bill on the House floor, stating 'Federal lawmakers should take action to combat illegal immigration, but us doing what we can do here is important.' He was an active floor proponent of requiring more employers to verify workers' immigration status, supporting mandatory E-Verify enforcement at the state level.",
              ["https://www.ksl.com/article/51450379/utah-lawmakers-advance-bill-to-boost-number-of-firms-checking-workers-migratory-status",
               "https://utahnewsdispatch.com/2025/01/06/utah-crime-immigration-public-safety-bills-2025-legislative-session/"]),
    ]),

    # ---------------- James A. Dunnigan (UT-36, Speaker pro tempore) ----------------
    ("james-a-dunnigan", "UT", "Representative", [
        claim("jd1", "james-a-dunnigan", "self_defense", 0, False,
              "Voted against HB 60 (2021 General Session), Utah's landmark Constitutional Carry bill eliminating the permit requirement for concealed carry — one of only two Republicans in the entire chamber to vote no (bill passed 54–19). The Utah Shooting Sports Council and national gun-rights advocates considered this the most significant Second Amendment expansion in Utah in years; Dunnigan's dissent placed him outside the Republican caucus consensus on permitless carry.",
              ["https://www.ksl.com/article/50095109/utah-moves-to-drop-concealed-carry-gun-permit-requirement-with-house-ok-of-bill",
               "https://www.deseret.com/utah/2021/1/26/22250768/state-house-passes-bill-to-drop-concealed-carry-gun-permit-requirement-legislature-second-amendment/"]),
        claim("jd2", "james-a-dunnigan", "self_defense", 1, False,
              "Chief sponsor of HB 425 (2025), 'Department of Public Safety Fee Amendments,' which raised concealed firearm permit fees for out-of-state applicants and granted the Bureau of Criminal Identification (BCI) unilateral authority to set future permit fees without specific legislative approval. The Utah Shooting Sports Council opposed the bill, arguing it would burden lawful permit-seekers and give an executive agency unchecked power over Second Amendment permit costs.",
              ["https://le.utah.gov/Session/2025/bills/enrolled/HB0425.pdf",
               "https://utahshootingsportscouncil.org/legislation-2025-bills/"]),
        claim("jd3", "james-a-dunnigan", "economic_stewardship", 2, True,
              "As Speaker pro tempore and senior House Republican, Dunnigan has been part of the majority that passed income tax cuts for six consecutive years, reducing Utah's rate from 4.85% to 4.50% (2025) and delivering an estimated $1.5 billion in cumulative tax relief for families. He also sponsored HB 13 (2025), creating market-driven housing infrastructure financing districts to increase supply without government subsidies.",
              ["https://house.utleg.gov/utahs-tax-cut-streak-six-years-and-1-5-billion/",
               "https://utahnewsdispatch.com/2025/03/06/utah-legislature-approves-another-tax-cut/"]),
    ]),

    # ---------------- Jake Sawyer (UT-9, State Rep) ----------------
    ("jake-sawyer", "UT", "Representative", [
        claim("js1", "jake-sawyer", "self_defense", 0, True,
              "Voted YES on HB 133 (2025 General Session), 'Dangerous Weapons Amendments,' which lowered the legal open-carry age from 21 to 18, allowed 18–20-year-olds to carry concealed without a permit, and removed criminal penalties for carrying a loaded firearm in a vehicle — a significant expansion of constitutional carry rights. NRA-ILA supported legislation; passed the House 56–13 (failed in Senate committee).",
              ["https://le.utah.gov/~2025/bills/static/HB0133.html",
               "https://www.nraila.org/articles/20250206/utah-pro-gun-bill-passes-house-advances-to-senate"]),
        claim("js2", "jake-sawyer", "family_child_sovereignty", 0, True,
              "Voted YES on HB 233 (2025), 'School Curriculum Amendments,' banning organizations that perform elective abortions — including Planned Parenthood — from providing health instruction or materials in Utah public schools. The bill passed the House 51–14 and was signed into law (effective July 1, 2025), protecting schoolchildren from abortion-provider influence in public school curricula.",
              ["https://le.utah.gov/~2025/bills/static/HB0233.html",
               "https://utahnewsdispatch.com/2025/02/21/utah-house-passes-bill-ban-planned-parenthood-educators-from-schools/"]),
    ]),

    # ---------------- Douglas R. Welton (UT-65, State Rep) ----------------
    ("douglas-r-welton", "UT", "Representative", [
        claim("dw1", "douglas-r-welton", "christian_liberty", 0, True,
              "Chief sponsor of HB 381 (2025), 'Civics Education Amendments,' requiring all Utah high school students to complete a mandatory yearlong course in U.S. constitutional government and citizenship as a graduation requirement, developed in partnership with Utah Valley University's Civic Thought and Leadership Initiative. Signed by Governor Cox. Welton stated his goal was to get students 'back to the core of who we are as Americans,' grounding civic identity in founding constitutional principles.",
              ["https://le.utah.gov/~2025/bills/static/HB0381.html",
               "https://www.deseret.com/utah/2025/02/04/legislature-education-high-school-civics-voters-graduation-requirements-government-bill/",
               "https://www.nas.org/press-release/utah-adopts-legislation-inspired-by-the-general-education-act/"]),
        claim("dw2", "douglas-r-welton", "self_defense", 0, True,
              "Voted YES on HB 133 (2025 General Session), 'Dangerous Weapons Amendments,' expanding constitutional carry rights by lowering the open-carry age to 18, permitting concealed carry without a permit for 18–20-year-olds, and decriminalizing loaded-firearm transport — NRA-ILA-supported legislation that passed the House 56–13.",
              ["https://le.utah.gov/~2025/bills/static/HB0133.html",
               "https://www.nraila.org/articles/20250206/utah-pro-gun-bill-passes-house-advances-to-senate"]),
        claim("dw3", "douglas-r-welton", "family_child_sovereignty", 0, True,
              "Voted YES on HB 215 (2023), the 'Utah Fits All' scholarship program, providing up to $8,000 per student in public funding for private school tuition, transportation, and educational materials — the largest school-choice expansion in Utah history, passed the House 54–20. Despite publicly expressing reservations about bill design, Welton supported the core parental-rights principle of giving families freedom over their children's education.",
              ["https://le.utah.gov/~2023/bills/static/HB0215.html",
               "https://www.sltrib.com/news/education/2023/01/26/controversial-utah-voucher-bill/"]),
    ]),

    # ---------------- Doug Fiefia (UT-48, State Rep) ----------------
    ("doug-fiefia", "UT", "Representative", [
        claim("df1", "doug-fiefia", "sanctity_of_life", 0, True,
              "States on his campaign Key Issues page: 'I am committed to protecting the unborn, empowering women, and fostering a society that cherishes every life' and 'believes in the sanctity of human life.' He voted with the Republican caucus majority for HB 233 (2025), banning Planned Parenthood educators from Utah public schools (passed 51–14), and aligns with the pro-life Republican legislative caucus.",
              ["https://dougfiefia.com/key-issues/",
               "https://utahnewsdispatch.com/2025/02/21/utah-house-passes-bill-ban-planned-parenthood-educators-from-schools/"]),
        claim("df2", "doug-fiefia", "family_child_sovereignty", 0, True,
              "Sponsored HB 418 (2025), the 'Digital Choice Act,' signed into law April 4, 2025, requiring Big Tech platforms to provide full data portability, deletion rights, and interoperability to give families and individuals control over their data. Also sponsored HB 286 (2026), the 'AI Transparency Act,' requiring AI companies to publish child safety plans and prevent chatbots from inappropriate conversations with minors — advanced against Trump administration opposition.",
              ["https://www.deseret.com/utah/2025/05/28/he-once-worked-for-big-tech-now-this-utah-lawmaker-is-leading-efforts-to-regulate-it/",
               "https://www.kuer.org/politics-government/2026-04-19/trump-doesnt-want-states-regulating-ai-utah-rep-doug-fiefia-isnt-listening",
               "https://utahnewsdispatch.com/2026/01/27/utah-bill-requires-ai-companies-safety-plans-for-children/"]),
        claim("df3", "doug-fiefia", "economic_stewardship", 2, True,
              "Voted YES on HB 267 (2025), prohibiting public-sector unions in Utah from collectively bargaining — a limited-government, pro-taxpayer vote giving elected officials direct control over public compensation rather than union negotiation. (The bill was later repealed by voter referendum in December 2025, but Fiefia voted for it on original passage.)",
              ["https://www.kuer.org/politics-government/2025-01-27/utah-house-passes-bill-to-block-public-sector-unions-from-collective-bargaining"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
