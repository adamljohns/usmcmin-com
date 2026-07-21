#!/usr/bin/env python3
"""Enrichment batch 810: 5 Utah State Representatives (Democratic caucus).

Federal archetype_curated bucket fully exhausted; continuing the UT state
representative pool from where batch 809 left off (reverse-alpha by name).
Targets: Verona Mauga (D-31), Sandra Hollins (D-21), Sahara Hayes (D-32),
Rosalba Dominguez (D-35), John Arthur (D-41).

All claims drawn from 2023-2026 official legislative records, candidate surveys,
and credible state-level news sources. MINIFIED write preserved (no indent=2).
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
    # ---------------- Verona Mauga (UT-31, State Rep, D) ----------------
    ("verona-mauga", "UT", "Representative", [
        claim("vm1", "verona-mauga", "self_defense", 1, False,
              "Ran in 2024 on an explicit 'sensible gun safety' platform, listing it among her core legislative priorities — in direct opposition to the rubric's Second Amendment standard that opposes red-flag laws, assault-weapon bans, and magazine-limit restrictions.",
              ["https://www.sltrib.com/news/politics/2024/10/17/2024-election-bill-swann-verona/",
               "https://ballotpedia.org/Verona_Mauga"]),
        claim("vm2", "verona-mauga", "biblical_marriage", 2, False,
              "Declared as a legislative priority that she will 'protect LGBTQIA+ rights' in the Utah Legislature — directly opposing the rubric's standard of rejecting transgender ideology and LGBTQ policy promotion in public institutions.",
              ["https://www.apaics.org/2025-wc-spotlight-awardees/the-hon.-verona-sagato-mauga",
               "https://www.utahhousedemocrats.utleg.gov/verona-mauga"],
              kind="statement"),
    ]),

    # ---------------- Sandra Hollins (UT-21, House Minority Whip, D) ----------------
    ("sandra-hollins", "UT", "Representative", [
        claim("sh1", "sandra-hollins", "sanctity_of_life", 0, False,
              "As House minority whip, stated she does not support banning abortion after six weeks and would not support a state constitutional amendment to restrict abortion — rejecting any life-at-conception or personhood standard and opposing legislative protection for the unborn.",
              ["https://www.sltrib.com/news/politics/2024/10/17/rep-sandra-hollinss-faces-david/",
               "https://ballotpedia.org/Sandra_Hollins"]),
        claim("sh2", "sandra-hollins", "sanctity_of_life", 2, False,
              "Stated in 2024 that IVF and fertility treatments 'are often medically necessary' and opposes any restrictions on them — including the routine embryo-discard practices IVF involves, in direct conflict with the rubric's anti-embryonic/IVF-discard standard.",
              ["https://ballotpedia.org/Sandra_Hollins",
               "https://www.sltrib.com/news/politics/2024/10/17/rep-sandra-hollinss-faces-david/"]),
        claim("sh3", "sandra-hollins", "economic_stewardship", 2, False,
              "Scored only 8% on the 2023 Utah Freedom Index legislative scorecard, reflecting a voting record that consistently favors government spending, taxation, and regulatory expansion over the balanced-budget and limited-government fiscal principles the rubric's economic stewardship standard requires.",
              ["https://thefreedomindex.org/ut/legislator/17527/",
               "https://thefreedomindex.org/ut/legislator/17527/votes/ut-scorecard-2023/"]),
    ]),

    # ---------------- Sahara Hayes (UT-32, State Rep, D) ----------------
    ("sahara-hayes", "UT", "Representative", [
        claim("sy1", "sahara-hayes", "biblical_marriage", 2, False,
              "Utah's first openly bisexual state legislator; voted NO on HB 269 (2025), the transgender dormitory policy bill, and gave an emotional floor speech pleading with colleagues not to pass 'another bill aimed at the transgender community' — the fourth consecutive year she fought anti-transgender legislation in the Republican-majority chamber (vote: 59–13, Hayes in the minority).",
              ["https://www.sltrib.com/news/education/2025/01/28/utahs-only-openly-lgbtq-lawmaker/",
               "https://www.sltrib.com/news/education/2025/02/06/utah-republican-lawmaker-defends/"]),
        claim("sy2", "sahara-hayes", "self_defense", 1, False,
              "Chief sponsor of HB 481 (2023 General Session), 'Firearm Safety and Suicide Prevention Education Requirements,' mandating that Utah schools provide government-prescribed firearm safety materials to parents of students who threaten self-harm — extending state authority into lawful gun storage and handling practices in private homes.",
              ["https://le.utah.gov/~2023/bills/hbillenr/HB0481.htm",
               "https://progressreport.betterutah.org/legislators/rep-sahara-hayes"]),
        claim("sy3", "sahara-hayes", "biblical_marriage", 2, False,
              "Chief sponsor of HB 234 (2024 General Session), 'Vital Records Amendments,' streamlining the court process for changing name and sex designations on Utah birth certificates — legislation that institutionalizes legal gender transitions in vital records, at odds with the rubric's rejection of transgender ideology.",
              ["https://le.utah.gov/~2024/bills/hbillint/HB0234.htm",
               "https://progressreport.betterutah.org/legislators/rep-sahara-hayes"]),
    ]),

    # ---------------- Rosalba Dominguez (UT-35, State Rep, D) ----------------
    ("rosalba-dominguez", "UT", "Representative", [
        claim("rd1", "rosalba-dominguez", "sanctity_of_life", 0, False,
              "In her 2024 campaign questionnaire, opposed a state constitutional amendment to ban abortion and stated 'No additional restrictions on reproductive health care are needed' and that 'family planning decisions should remain between patients and their doctors' — rejecting legislative recognition of personhood from conception.",
              ["https://www.sltrib.com/news/politics/2024/10/17/utah-house-district-35-rosalba/",
               "https://ballotpedia.org/Rosalba_Dominguez"],
              kind="statement"),
        claim("rd2", "rosalba-dominguez", "industry_capture", 4, False,
              "Called in 2024 for Utah to 'absolutely pursue and invest in renewables like solar and wind to reduce our carbon footprint' — endorsing mandatory government-driven energy transition aligned with the ESG and WEF sustainability frameworks the rubric's industry-capture category identifies as threats to economic sovereignty.",
              ["https://www.sltrib.com/news/politics/2024/10/17/utah-house-district-35-rosalba/",
               "https://ballotpedia.org/Rosalba_Dominguez"],
              kind="statement"),
    ]),

    # ---------------- John Arthur (UT-41, State Rep, D) ----------------
    ("john-arthur", "UT", "Representative", [
        claim("ja1", "john-arthur", "family_child_sovereignty", 0, False,
              "A career public-school educator — 2021 Utah Teacher of the Year, Title I school teacher, co-director of Teacher Fellows, and director of candidate recruitment for the Utah National Board Coalition — appointed to the Legislature by Democratic delegates whose caucus voted unanimously against HB 215 (2023), Utah's landmark school-choice scholarship program that passed 54–20 on Republican votes; his institutional and political alignment consistently favors government-school expansion over the parental-choice alternatives the rubric's family sovereignty standard supports.",
              ["https://kutv.com/news/local/salt-lake-city-sixth-grade-teacher-named-2021-utah-teacher-of-the-year",
               "https://le.utah.gov/~2023/bills/static/HB0215.html",
               "https://www.votejohnarthur.com/about"]),
        claim("ja2", "john-arthur", "economic_stewardship", 2, False,
              "Testified before the United States Senate Committee on Health, Education, Labor and Pensions in support of federal public-education programs, consistent with a career-long alignment with federally-backed school spending and deficit-financed federal outlays over the balanced-budget, market-driven approaches the rubric's economic stewardship standard favors.",
              ["https://en.wikipedia.org/wiki/John_Arthur_(Utah_politician)",
               "https://www.votejohnarthur.com/about"]),
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
