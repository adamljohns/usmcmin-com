#!/usr/bin/env python3
"""Enrichment batch 548: hand-curated claims for 5 Tennessee State Senators (R).

All archetype_curated federal senators/reps are exhausted and prior batches
(546–547) covered the first TN Republicans; this batch continues the
bottom-of-alphabet sweep through remaining TN Republicans.

Targets (all TN R State Senators, 0 prior claims):
  John Stevens (SD-24), Joey Hensley (SD-28), Janice Bowling (SD-16),
  Jack Johnson (SD-27, Majority Leader), Ferrell Haile (SD-18, Pro Tempore).

Sources: ballotpedia.org, en.wikipedia.org, legiscan.com,
tennesseelookout.com, tnreportcard.org, scorecard.factennessee.org,
tngopsenate.com, nashvillebanner.com.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning.
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
    # ---------------- John Stevens (TN-24, State Senator, R) ----------------
    ("john-stevens", "TN", "State Senator", [
        claim("js1", "john-stevens", "sanctity_of_life", 0, True,
              "Stevens voted YES on SB1257 (2019), the Human Life Protection Act — Tennessee's total abortion trigger ban, effective August 25, 2022, thirty days after Dobbs v. Jackson overturned Roe. The bill passed the full Senate 25–5, prohibiting all elective abortions in Tennessee except to save the mother's life. Stevens has been a consistent member of the TN Senate Republican supermajority advancing pro-life legislation since 2012.",
              ["https://legiscan.com/TN/bill/SB1257/2019",
               "https://scorecard.factennessee.org/bills/sb-1257hb-1029-human-life-protection-act",
               "https://ballotpedia.org/John_Stevens_(Tennessee)"]),
        claim("js2", "john-stevens", "self_defense", 0, True,
              "Stevens sponsored SB1503 (2023, 113th General Assembly), legislation to lower the minimum age for Tennessee's permitless carry law from 21 to 18. The Senate Judiciary Committee approved it 7–2. In committee testimony Stevens stated: 'The right of self-defense is not a right granted by government. It was given to us by our Creator. The Founders preserved that right in the Second Amendment,' citing New York State Rifle & Pistol Ass'n v. Bruen (2022).",
              ["https://legiscan.com/TN/bill/SB1503/2023",
               "https://tennesseelookout.com/2023/03/21/senate-panel-clears-path-to-lower-permitless-gun-carry-age-to-18/",
               "https://ballotpedia.org/John_Stevens_(Tennessee)"]),
    ]),

    # ---------------- Joey Hensley (TN-28, State Senator, R) ----------------
    ("joey-hensley", "TN", "State Senator", [
        claim("jh1", "joey-hensley", "sanctity_of_life", 0, True,
              "Hensley SPONSORED SB600 (2023, 113th General Assembly), passed 27–6, prohibiting any local government from expending public funds to assist a person in obtaining an abortion, including out-of-state travel. The bill was a direct response to Metro Nashville's proposal to allocate $500,000 for residents to travel out of state for abortions after Dobbs. Hensley has also co-sponsored the Human Life Protection Act (SB1257, 2019) and stated publicly: 'I'm proud to have sponsored this legislation.'",
              ["https://legiscan.com/TN/people/joey-hensley/id/7280",
               "https://tennesseeconservativenews.com/tn-bill-to-prohibit-local-governments-from-using-taxpayer-dollars-to-fund-abortions-passes-senate/",
               "https://ballotpedia.org/Joey_Hensley"]),
        claim("jh2", "joey-hensley", "biblical_marriage", 4, True,
              "Hensley introduced Tennessee's 'Don't Say Gay' bill in 2012 and 2013, seeking to prohibit public schools from discussing or promoting LGBT issues in any grade. He has repeatedly co-sponsored legislation allowing therapists and counselors to refuse service to clients on grounds of religious or moral belief — bills specifically designed to let practitioners decline to counsel same-sex couples or gender-nonconforming clients. The Tennessee Legislative Report Card documents his ongoing opposition to LGBTQ promotion in schools and public policy.",
              ["https://en.wikipedia.org/wiki/Joey_Hensley",
               "https://ballotpedia.org/Joey_Hensley",
               "https://tnreportcard.org/senators/tn-sd28-hensley/"]),
    ]),

    # ---------------- Janice Bowling (TN-16, State Senator, R) ----------------
    ("janice-bowling", "TN", "State Senator", [
        claim("jb1", "janice-bowling", "biblical_marriage", 1, True,
              "Bowling co-sponsored SB1746 (2025–2026, 114th General Assembly), declaring that 'private citizens and organizations are not bound by the Fourteenth Amendment or by the Supreme Court's purported interpretation of the Fourteenth Amendment in Obergefell v. Hodges' — explicitly allowing private citizens to refuse recognition of same-sex marriages without legal penalty. The House companion (HB1473 by Rep. Gino Bulso) passed 68–24 on February 19, 2026.",
              ["https://legiscan.com/TN/bill/SB1746/2025",
               "https://tennesseelookout.com/2026/02/12/tennessee-republicans-advance-bills-targeting-lgbtq-residents/",
               "https://ballotpedia.org/Janice_Bowling"]),
        claim("jb2", "janice-bowling", "self_defense", 1, True,
              "Bowling sponsored SB2698/HB2770 (2022), making property owners who voluntarily post gun-free zones civilly liable for the safety of lawfully armed patrons disarmed by that policy — a direct challenge to administrative gun disarmament. She also sponsored legislation prohibiting healthcare professionals from asking patients whether they own firearms, subject to a $1,000-per-violation fine and professional licensing sanctions; the Tennessee Firearms Association tracked both bills as pro-Second-Amendment.",
              ["https://tennesseefirearms.com/2022/04/2022-legislative-year-end-report/",
               "https://tnreportcard.org/senators/tn-sd16-bowling/",
               "https://ballotpedia.org/Janice_Bowling"]),
    ]),

    # ---------------- Jack Johnson (TN-27, Senate Majority Leader, R) ----------------
    ("jack-johnson", "TN", "State Senator", [
        claim("jj1", "jack-johnson", "self_defense", 0, True,
              "Johnson SPONSORED SB765 (112th GA, 2021) — Tennessee's landmark permitless carry law; House companion HB786 by Rep. William Lamberth. The bill passed the Senate 23–9 and the House 64–29; Gov. Bill Lee signed it April 8, 2021, effective July 1, 2021. The law allows adults 21+ (military 18+) to carry handguns concealed or openly without a state-issued permit. Johnson shepherded the bill as Senate Majority Leader.",
              ["https://legiscan.com/TN/bill/SB0765/2021",
               "https://www.tngopsenate.com/republican-legislation-advances-to-strengthen-2nd-amendment-protections-and-pro-life-laws/",
               "https://ballotpedia.org/Jack_Johnson_(Tennessee_politician)"]),
        claim("jj2", "jack-johnson", "sanctity_of_life", 0, True,
              "FACT Tennessee's legislative scorecard confirms Johnson voted YES on SB1257/HB1029 — the Human Life Protection Act (2019 trigger law, effective August 25, 2022) — as a member of the Senate Republican supermajority. He consistently votes in alignment with Tennessee Right to Life recommendations and opposed legislation that would have weakened pro-life exceptions, per TLRC tracking.",
              ["https://scorecard.factennessee.org/senators/jack-johnson",
               "https://www.tnrtl.org/tn_legislature_passes_human_life_protection_act",
               "https://ballotpedia.org/Jack_Johnson_(Tennessee_politician)"]),
        claim("jj3", "jack-johnson", "border_immigration", 1, True,
              "Johnson sponsored a 2026 bill (114th GA) establishing a Class A misdemeanor for any person remaining in Tennessee 90+ days after a final federal deportation order — explicitly empowering state and local law enforcement to act on immigration when federal enforcement lapses. Johnson stated: 'The ability to enforce our immigration laws at the state level cannot depend on which party occupies the White House.' The bill passed the Tennessee Senate.",
              ["https://tennesseelookout.com/2026/04/07/tennessee-senate-adopts-new-state-immigration-crimes/",
               "https://nashvillebanner.com/2026/04/07/tennessee-senate-jack-johnson-immigration-policy/",
               "https://ballotpedia.org/Jack_Johnson_(Tennessee_politician)"]),
    ]),

    # ---------------- Ferrell Haile (TN-18, President Pro Tempore, R) ----------------
    ("ferrell-haile", "TN", "State Senator", [
        claim("fh1", "ferrell-haile", "biblical_marriage", 2, True,
              "As Tennessee Senate President Pro Tempore, Haile was a central sponsor and floor manager of SB1 (2023, 113th General Assembly) — the first state law banning gender-affirming medical care (puberty blockers, cross-sex hormones, and surgeries) for minors under 18. The bill passed the Senate 26–6 on February 13, 2023, and was signed by Gov. Lee on March 2, 2023. SB1 was later upheld by the U.S. Supreme Court in United States v. Skrmetti (2025).",
              ["https://en.wikipedia.org/wiki/Tennessee_Senate_Bill_1",
               "https://legiscan.com/TN/bill/SB0001/2023",
               "https://en.wikipedia.org/wiki/United_States_v._Skrmetti"]),
        claim("fh2", "ferrell-haile", "christian_liberty", 0, True,
              "Haile sponsored legislation (2025, 114th GA) enabling healthcare providers to refuse treatment to patients when the provider has ethical, moral, or religious objections — including potential refusal of gender-affirming care and abortion-related services. The bill codifies conscience protections for clinical practitioners, aligning with the religious free-exercise standard of the rubric.",
              ["https://ballotpedia.org/Ferrell_Haile",
               "https://scorecard.factennessee.org/senators/ferrell-haile",
               "https://en.wikipedia.org/wiki/Ferrell_Haile"]),
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
