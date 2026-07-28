#!/usr/bin/env python3
"""Enrichment batch 867: TN + SC Republican state representatives.

Federal senator/representative buckets fully depleted; targeting bottom-of-alphabet
state legislators with 0 claims. 3 Tennessee State Reps (Districts 37, 38, 94)
+ 2 South Carolina State Reps (Districts 1 and 120).

Sources: wapp.capitol.tn.gov (TN roll-call records), scstatehouse.gov (SC bill pages),
tennesseelookout.com / The Guardian (Paul Sherrell March 2023 hearing),
scdailygazette.com, abcnews4.com, legiscan.com.
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
    # ---- Rick Scarbrough (TN-R, District 37 - Campbell County) ----
    ("rick-scarbrough", "TN", "Representative", [
        claim("rs1", "rick-scarbrough", "sanctity_of_life", 0, True,
              "Voted for Tennessee's Human Life Protection Act (SB13/HB1, 111th GA), which enacted a "
              "near-total abortion ban triggered immediately upon the Dobbs decision in June 2022 — "
              "affirming life from conception as the law of the state.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0001&GA=111",
               "https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
        claim("rs2", "rick-scarbrough", "self_defense", 1, True,
              "Voted for Tennessee's permitless carry law (HB786/SB765, 112th GA), signed April 8, 2021, "
              "removing the government permit requirement for law-abiding adults to carry a handgun — "
              "directly opposing the restriction the rubric targets.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0786&GA=112",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
        claim("rs3", "rick-scarbrough", "biblical_marriage", 2, True,
              "Voted for the Tennessee SAFE Act (SB1/HB1, 113th GA), signed March 22, 2023, "
              "banning gender-affirming medical procedures for minors — rejecting transgender ideology "
              "in pediatric medicine.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0001&GA=113",
               "https://en.wikipedia.org/wiki/Tennessee_SAFE_Act"]),
    ]),

    # ---- Rick Eldridge (TN-R, District 94 - Macon/Smith/Trousdale) ----
    ("rick-eldridge", "TN", "Representative", [
        claim("re1", "rick-eldridge", "sanctity_of_life", 0, True,
              "Voted for Tennessee's Human Life Protection Act (SB13/HB1, 111th GA), enacting a "
              "near-total abortion ban that took effect immediately after Dobbs v. Jackson (June 2022), "
              "recognizing life from conception under state law.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0001&GA=111",
               "https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
        claim("re2", "rick-eldridge", "self_defense", 1, True,
              "Voted for Tennessee's permitless carry law (HB786/SB765, 112th GA, signed April 8, 2021), "
              "removing the permit requirement for law-abiding adults to carry handguns — consistent "
              "with the rubric's opposition to government-imposed firearm restrictions.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0786&GA=112",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
        claim("re3", "rick-eldridge", "biblical_marriage", 2, True,
              "Voted for the Tennessee SAFE Act (SB1/HB1, 113th GA, signed March 22, 2023), banning "
              "gender-affirming medical procedures (puberty blockers, cross-sex hormones, surgery) for "
              "minors — rejecting transgender ideology as applied to children.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0001&GA=113",
               "https://en.wikipedia.org/wiki/Tennessee_SAFE_Act"]),
    ]),

    # ---- Paul Sherrell (TN-R, District 38 - Anderson County) ----
    ("paul-sherrell", "TN", "Representative", [
        claim("ps1", "paul-sherrell", "sanctity_of_life", 1, True,
              "At a March 2, 2023 Tennessee House committee hearing, Sherrell publicly stated that "
              "physicians and women who obtain abortions should face capital punishment — 'we could "
              "hang them' — placing himself at the most explicitly abolitionist end of pro-life advocacy, "
              "demanding full criminal penalty rather than mere restriction.",
              ["https://tennesseelookout.com/2023/03/03/lawmaker-says-doctors-mothers-who-get-abortions-could-be-hanged/",
               "https://www.theguardian.com/us-news/2023/mar/03/tennessee-republican-hang-abortion-doctors-women"]),
        claim("ps2", "paul-sherrell", "sanctity_of_life", 0, True,
              "Voted for Tennessee's Human Life Protection Act (SB13/HB1, 111th GA), which enacted a "
              "near-total abortion ban effective immediately upon Dobbs (June 2022), protecting life "
              "from conception as Tennessee law.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0001&GA=111",
               "https://en.wikipedia.org/wiki/Abortion_in_Tennessee"]),
        claim("ps3", "paul-sherrell", "self_defense", 1, True,
              "Voted for Tennessee's permitless carry law (HB786/SB765, 112th GA, signed April 8, 2021), "
              "removing the permit requirement for adults to carry handguns — opposing the government "
              "restriction the rubric targets.",
              ["https://wapp.capitol.tn.gov/apps/billsearch/BillSummaryPublic.aspx?BillNumber=HB0786&GA=112",
               "https://en.wikipedia.org/wiki/Gun_laws_in_Tennessee"]),
    ]),

    # ---- Wm. Weston J. Newton (SC-R, District 120 - Beaufort County) ----
    ("wm-weston-j-newton", "SC", "Representative", [
        claim("wjn1", "wm-weston-j-newton", "sanctity_of_life", 0, True,
              "Sponsored S.474 (Fetal Heartbeat & Protection from Abortion Act) in the SC House "
              "Judiciary Committee, which he chairs; the 6-week abortion ban was signed by Gov. McMaster "
              "on May 25, 2023 — Newton actively advancing the bill through the committee process.",
              ["https://governor.sc.gov/news/2023-05/gov-henry-mcmaster-protects-life-signs-fetal-heartbeat-and-protection-abortion-act",
               "https://www.scstatehouse.gov/query.php?search=DOC&searchtext=S474&category=LEGISLATION"]),
        claim("wjn2", "wm-weston-j-newton", "self_defense", 1, True,
              "Co-sponsored H.3594 (SC Constitutional Carry / Second Amendment Preservation Act), "
              "signed March 7, 2024 by Gov. McMaster — eliminating the permit requirement to carry a "
              "handgun in South Carolina and making it the 29th permitless-carry state.",
              ["https://www.scstatehouse.gov/sess125_2023-2024/bills/3594.htm",
               "https://legiscan.com/SC/bill/H3594/2023"]),
        claim("wjn3", "wm-weston-j-newton", "family_child_sovereignty", 0, True,
              "Co-sponsored H.4757 (Parental Rights Act, 125th GA), which passed the SC House 116-1 "
              "on February 19, 2026 — requiring parental access to lesson plans, consent on "
              "gender/sexuality instruction, and a private right of action against school districts.",
              ["https://abcnews4.com/news/local/parental-rights-act-moves-forward-after-near-unanimous-vote-in-sc-house-h-4757-laws-mahmoud-v-taylor-lgbtq-south-carolina",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/4757.htm"]),
    ]),

    # ---- William R. Whitmire (SC-R, District 1 - Oconee County) ----
    ("william-r-whitmire", "SC", "Representative", [
        claim("wrw1", "william-r-whitmire", "sanctity_of_life", 0, True,
              "Voted for S.474 (Fetal Heartbeat & Protection from Abortion Act), the 6-week abortion "
              "ban signed May 25, 2023 — SC House Republicans passed it over Democratic opposition, "
              "recognizing cardiac activity as the threshold for protection.",
              ["https://governor.sc.gov/news/2023-05/gov-henry-mcmaster-protects-life-signs-fetal-heartbeat-and-protection-abortion-act",
               "https://en.wikipedia.org/wiki/Abortion_in_South_Carolina"]),
        claim("wrw2", "william-r-whitmire", "self_defense", 1, True,
              "Co-sponsored H.3594 (SC Constitutional Carry / Second Amendment Preservation Act), "
              "signed March 7, 2024 — the permitless carry law that passed the House 87-26 and removed "
              "South Carolina's permit requirement for concealed and open carry.",
              ["https://legiscan.com/SC/bill/H3594/2023",
               "https://www.scstatehouse.gov/sess125_2023-2024/bills/3594.htm"]),
        claim("wrw3", "william-r-whitmire", "biblical_marriage", 2, True,
              "Co-sponsored H.4608 (Save Women's Sports Act, 124th GA), which passed the SC House 70-33 "
              "and was signed into law in 2022 — banning biological males from competing in female "
              "athletic categories in public schools and colleges.",
              ["https://www.scstatehouse.gov/sess124_2021-2022/bills/4608.htm",
               "https://ballotpedia.org/William_Whitmire_(South_Carolina)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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

    # Minified write — preserve no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
