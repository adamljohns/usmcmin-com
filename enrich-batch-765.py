#!/usr/bin/env python3
"""Enrichment batch 765: 5 Utah R State Representatives (bottom-of-alphabet targets).

Primary archetype_curated federal senator/rep buckets are exhausted; this batch
targets archetype_party_default UT R State Representatives — a heavily conservative
state with strong, verifiable voting records on life, family, and federalism.

Targets (reversed-alpha UT sweep):
  Mike Schultz (Speaker, HD-12)
  Karianne Lisonbee (HD-14)
  Ken Ivory (HD-39)
  Candice P. Pierucci (HD-49)
  Melissa G. Ballard (HD-20)

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Mike Schultz (UT, Speaker of the House / State Rep HD-12) ----------
    ("mike-schultz", "UT", "Representative", [
        claim("ms1", "mike-schultz", "sanctity_of_life", 0, True,
              "As Utah House Speaker, co-issued a joint statement with Senate President Stuart Adams calling the Utah Supreme Court's August 2024 ruling keeping the near-total abortion trigger ban blocked 'one of the worst outcomes we have ever seen from the Utah Supreme Court,' accusing the justices of undermining the Legislature's constitutional authority to protect the unborn following the Dobbs decision.",
              ["https://senate.utah.gov/president-adams-and-speaker-schultz-respond-to-utah-supreme-court-decision-2/",
               "https://en.wikipedia.org/wiki/Mike_Schultz_(politician)"]),
        claim("ms2", "mike-schultz", "biblical_marriage", 2, True,
              "Presided as Speaker over the Utah Legislature passing transgender sports restrictions for the third consecutive year in 2024, maintaining female-only athletic categories against male-born competitors — enacting the biological-sex distinctions the rubric's rejection of transgender ideology requires.",
              ["https://www.sltrib.com/news/politics/2024/03/02/utah-legisalture-passed-hundereds/",
               "https://ballotpedia.org/Mike_Schultz_(Utah)"]),
    ]),

    # ---------- Karianne Lisonbee (UT, State Rep HD-14 / Majority Whip) ----------
    ("karianne-lisonbee", "UT", "Representative", [
        claim("kl1", "karianne-lisonbee", "sanctity_of_life", 0, True,
              "Chief sponsor of H.B. 166, the Down Syndrome Nondiscrimination Abortion Act (2019), banning abortions performed solely because of a fetal Down syndrome diagnosis, signed into law with bipartisan House passage 54–15 and Senate 20–6. Lisonbee called the targeted practice 'eugenics' and built in state outreach to connect mothers with Down syndrome support resources.",
              ["https://le.utah.gov/~2019/bills/static/HB0166.html",
               "https://www.ksl.com/article/46501124/bill-outlawing-abortions-solely-for-down-syndrome-diagnosis-passes-utah-legislature"]),
        claim("kl2", "karianne-lisonbee", "sanctity_of_life", 1, True,
              "Primary sponsor of HB467 (2023), which stopped new abortion clinic licensing in Utah and prohibited all existing abortion clinic operations as of January 2024 — an effective end to elective abortion services in the state while the trigger ban remained blocked in court.",
              ["https://www.ksl.com/article/news/politics/utah-bill-to-close-abortion-clinics-passes-legislature/50591382",
               "https://le.utah.gov/~2023/bills/hbillint/HB0467S01.htm"]),
    ]),

    # ---------- Ken Ivory (UT, State Rep HD-39) ----------
    ("ken-ivory", "UT", "Representative", [
        claim("ki1", "ken-ivory", "refuse_federal_overreach", 0, True,
              "Sponsored HJR6 (2025), a resolution reaffirming Utah's sovereignty under the Ninth and Tenth Amendments and resisting federal jurisdictional overreach, and HB380 establishing a formal state mechanism to contest federal authority — arguing that 'for far too long, states have acted subservient' to Washington.",
              ["https://en.wikipedia.org/wiki/Ken_Ivory",
               "https://www.ksl.com/article/51246086/utah-lawmakers-address-federalism-while-working-to-balance-state-federal-jurisdiction"]),
        claim("ki2", "ken-ivory", "refuse_federal_overreach", 1, True,
              "Founded and serves as president of the American Lands Council, which drafted HB148 (Utah Transfer of Public Lands Act, 2012) demanding the federal government cede control of public lands to Utah — a sustained legislative and national campaign to restore state authority over land the Tenth Amendment framework holds belongs to the states, not Washington bureaucracies.",
              ["https://en.wikipedia.org/wiki/Ken_Ivory",
               "https://en.wikipedia.org/wiki/Utah_Transfer_of_Public_Lands_Act"]),
    ]),

    # ---------- Candice P. Pierucci (UT, State Rep HD-49) ----------
    ("candice-p-pierucci", "UT", "Representative", [
        claim("cp1", "candice-p-pierucci", "family_child_sovereignty", 0, True,
              "Chief sponsor of HB215 (2023), the Utah Fits All Scholarship Program, creating $8,000 education savings accounts for K-12 families to direct their children's education at private schools, homeschools, or learning pods. When a court struck it down, Pierucci called the ruling 'judicial activism' and cited the Utah Constitution's declaration that 'parents have the primary responsibility for the education of their children.'",
              ["https://le.utah.gov/~2023/bills/hbillint/HB0215S01.htm",
               "https://www.ksl.com/article/51297765/judge-strikes-down-utahs-school-choice-program-leaving-kids-in-limbo"]),
        claim("cp2", "candice-p-pierucci", "family_child_sovereignty", 1, True,
              "Sponsored HB529 (2024), amendments to strengthen the Utah Fits All Scholarship Program by tightening administration and residency standards while keeping funding flowing to families — continuing her sponsorship of parent-directed education over government-controlled schooling.",
              ["https://le.utah.gov/~2024/bills/hbillint/HB0529.htm",
               "https://www.ksl.com/article/51260952/changes-being-made-to-the-utah-fits-all-program"]),
    ]),

    # ---------- Melissa G. Ballard (UT, State Rep HD-20) ----------
    ("melissa-g-ballard", "UT", "Representative", [
        claim("mb1", "melissa-g-ballard", "biblical_marriage", 0, True,
              "Serves as Legislative Chair of the Utah Marriage Commission, the state body that promotes and strengthens the institution of marriage — consistent with the rubric's call for public policy support of marriage as the foundational covenantal union.",
              ["https://le.utah.gov/interim/2022/pdf/00003900.pdf",
               "https://www.utah.gov/pmn/sitemap/notice/989447.html"]),
        claim("mb2", "melissa-g-ballard", "family_child_sovereignty", 0, True,
              "A music educator and mother of six who champions parental voice in public education; sponsored legislation in 2019 to reform the Utah State Board of Education to a governor-appointed, Senate-ratified body with term limits and district representation, increasing public accountability over state education policy.",
              ["https://en.wikipedia.org/wiki/Melissa_Garff_Ballard",
               "https://ballotpedia.org/Melissa_Garff_Ballard"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
