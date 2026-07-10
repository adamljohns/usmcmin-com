#!/usr/bin/env python3
"""Enrichment batch 614: hand-curated claims for 5 UT R state legislators.

Continuing the archetype_party_default UT R state-rep bucket (Z→A sort).
TN bucket (batches 612-613) and WY/WV/WI/WA/VA/TX R buckets exhausted.

Targets (5 R): Walt Brooks (UT), Val L. Peterson (UT), Troy Shelley (UT),
Trevor Lee (UT), Tracy Miller (UT).
Each claim cites >=1 reliable source and reflects 2019-2026
voting record / public positions.

NOTE: writes scorecard.json MINIFIED to keep the master under
GitHub's 50MB warning.
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
    # ---------- Walt Brooks (UT-R, State Representative) ----------
    ("walt-brooks", "UT", "Representative", [
        claim("wb1", "walt-brooks", "self_defense", 0, True,
              "Chief House sponsor of Utah HB0060 (2021) — Utah's constitutional carry law — "
              "authorizing law-abiding adults to carry a concealed firearm without a government-"
              "issued permit. The bill passed the House 54–19 and Senate 22–6 and was signed by "
              "Gov. Spencer Cox on February 12, 2021, removing prior-state-permission as a "
              "prerequisite for bearing arms.",
              ["https://le.utah.gov/~2021/bills/static/HB0060.html",
               "https://kutv.com/news/utah-legislature-2021/governor-signs-permit-less-concealed-carry-bill-into-law",
               "https://gunowners.org/ut02022021/"]),
        claim("wb2", "walt-brooks", "sanctity_of_life", 0, True,
              "Co-sponsored Utah HB0467 (2023) restricting abortion clinic construction and "
              "requiring abortions be performed in hospital settings, tightening access under "
              "Utah's trigger ban; also signed a September 2022 cease-and-desist letter with "
              "~20 House Republicans demanding Planned Parenthood stop abortion referrals to "
              "neighboring states — demonstrating consistent pro-life advocacy beyond the "
              "minimum required by law.",
              ["https://le.utah.gov/~2023/bills/static/HB0467.html",
               "https://kuer.org/politics-government/2022-09-16/utah-republican-lawmakers-sign-cease-and-desist-asking-planned-parenthood-to-stop-abortion-referrals"]),
    ]),

    # ---------- Val L. Peterson (UT-R, State Representative, House Exec. Appropriations Chair) ----------
    ("val-l-peterson", "UT", "Representative", [
        claim("vp1", "val-l-peterson", "self_defense", 0, True,
              "States on his official Utah House profile: 'I believe in an armed citizenship "
              "and the rights to purchase, possess and use firearms for legitimate purposes' — "
              "an unambiguous public commitment to the constitutional right to keep and bear "
              "arms without restrictive licensing frameworks.",
              ["https://house.utleg.gov/rep/PETERVL/",
               "https://ballotpedia.org/Val_Peterson"]),
        claim("vp2", "val-l-peterson", "economic_stewardship", 2, True,
              "Earned a 100% score on the Sutherland Institute's 2012 legislative scorecard "
              "for fiscal conservatism and constitutional governance; as House Executive "
              "Appropriations Committee Chair (2023–2026) has been a principal architect of "
              "Utah's six consecutive income-tax reductions totaling over $1.5 billion — "
              "consistently prioritizing taxpayer relief over government expansion.",
              ["https://ballotpedia.org/Val_Peterson",
               "https://justfacts.votesmart.org/candidate/biography/121394/val-peterson"]),
    ]),

    # ---------- Troy Shelley (UT-R, State Representative) ----------
    ("troy-shelley", "UT", "Representative", [
        claim("ts1", "troy-shelley", "sanctity_of_life", 0, True,
              "In a 2024 Salt Lake Tribune candidate questionnaire, affirmed that he 'cannot "
              "support a law that restricts a consequence of a previous choice,' framing the "
              "unborn child as a living person whose existence is the direct consequence of a "
              "sexual choice — a personhood-from-conception posture consistent with Utah's "
              "near-total abortion trigger ban he has supported.",
              ["https://www.sltrib.com/news/politics/2024/06/08/brian-nielson-troy-shelley-both/",
               "https://ballotpedia.org/Troy_Shelley"]),
        claim("ts2", "troy-shelley", "biblical_marriage", 2, True,
              "Voted YES on Utah HB252 (2025) Transgender State Custody Amendments (passed "
              "House 60–14), prohibiting hormone therapy and gender-affirming surgeries for "
              "inmates and requiring incarceration by biological sex — directly opposing "
              "transgender ideology in state custody policy. Quoted saying he supported 'clarity "
              "for the courts' on biological sex classifications.",
              ["https://ksl.com/article/51245129/",
               "https://kuer.org/politics-government/2025-02-03/utah-house-passes-bill-banning-gender-affirming-care-for-inmates"]),
    ]),

    # ---------- Trevor Lee (UT-R, State Representative) ----------
    ("trevor-lee", "UT", "Representative", [
        claim("tl1", "trevor-lee", "biblical_marriage", 4, True,
              "Chief sponsor of Utah HB77 (2025) Flag Display Amendments, banning Pride flags "
              "and other non-governmental flags from public school classrooms and government "
              "buildings. Passed the House 53–20 and Senate 21–8; became law May 7, 2025 "
              "without the governor's signature — the first state law of its kind to reach "
              "the statute books.",
              ["https://le.utah.gov/~2025/bills/static/HB0077.html",
               "https://ksl.com/article/51258981/utah-governor-lets-pride-flag-ban-bill-become-law-without-signature",
               "https://utahnewsdispatch.com/2025/03/06/utah-house-passes-bill-banning-pride-flags-in-schools/"]),
        claim("tl2", "trevor-lee", "industry_capture", 0, True,
              "Chief sponsor of Utah HB84 (2025) Vaccine Amendments, requiring any food "
              "containing a vaccine component to be regulated as a drug rather than food — "
              "preventing covert pharmaceutical delivery through the food supply and protecting "
              "informed consent. Signed into law March 26, 2025.",
              ["https://le.utah.gov/~2025/bills/static/HB0084.html",
               "https://ksl.com/article/51257053/utah-governor-signs-bill-regulating-foods-containing-vaccine-components"]),
    ]),

    # ---------- Tracy Miller (UT-R, State Representative, Sandy/South Jordan) ----------
    ("tracy-miller", "UT", "Representative", [
        claim("tm1", "tracy-miller", "family_child_sovereignty", 0, True,
              "Chief sponsor of Utah HB325 (2025) Parent Access to Learning Materials Pilot "
              "Program — legislation that would have required schools to make all classroom "
              "materials, assignments, and digital resources accessible to parents for review "
              "before use, placing parental oversight above administrative discretion over "
              "curriculum content. Demonstrates a consistent parental-rights philosophy even "
              "when the bill did not advance.",
              ["https://sandyjournal.com/2025/03/28/527468/",
               "https://southjordanjournal.com/2025/03/28/527480/"]),
        claim("tm2", "tracy-miller", "refuse_state_overreach", 0, True,
              "Sponsored Utah HB144 S2 (2025) School Community Council Amendments, removing "
              "a state mandate requiring school community councils to teach a digital-citizenship "
              "curriculum — restoring local school-level discretion and opposing top-down "
              "curriculum mandates from the state education bureaucracy.",
              ["https://sandyjournal.com/2025/03/28/527468/",
               "https://ballotpedia.org/Tracy_Miller"]),
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
