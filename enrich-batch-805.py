#!/usr/bin/env python3
"""Enrichment batch 805: 5 West Virginia Republican state delegates (WV bottom-of-alphabet).

Primary archetype_curated federal bucket is fully exhausted; this batch deepens
evidence_curated profiles for WV Republican state delegates, covering rubric
categories not yet in their existing 2-claim records.

Targets:
  William Anderson  (WV-R, State Delegate Dist. 8)  — biblical_marriage[2], election_integrity[0]
  Wayne Clark       (WV-R, State Delegate Dist. 99) — biblical_marriage[2], election_integrity[0]
  Vernon Criss      (WV-R, State Delegate Dist. 12) — biblical_marriage[2], election_integrity[0]
  Tresa Howell      (WV-R, State Delegate Dist. 53) — biblical_marriage[2], election_integrity[0]
  Stanley Adkins    (WV-R, State Delegate Dist. 50) — biblical_marriage[2], election_integrity[0]

Key West Virginia 2025 Regular Session bills used:
  SB 456 (Riley Gaines Act): defines male/female by biological sex, signed Mar 12, 2025
  HB 3016: strict photo voter ID requirement, signed May 1, 2025

Sources: wvlegislature.gov, governor.wv.gov, wvpublic.org, westvirginiawatch.com

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep the
master under GitHub's 50MB warning.
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
    # ------------ William Anderson (WV-R, State Delegate District 8) ------------
    ("william-anderson", "WV", "Delegate", [
        claim("wa-b805-1", "william-anderson", "biblical_marriage", 2, True,
              "Anderson voted for West Virginia Senate Bill 456 — the Riley Gaines Act — "
              "which the House of Delegates passed on March 7, 2025 and Gov. Patrick Morrisey "
              "signed into law on March 12, 2025 in the legislature's first ceremonial signing. "
              "The law defines 'male' and 'female' in West Virginia state code by biological "
              "sex — a male as one born capable of producing sperm, a female as one born "
              "capable of producing ova — and preserves single-sex spaces (restrooms, "
              "changing rooms, sleeping quarters) in public schools, state higher education "
              "institutions, correctional facilities, and domestic violence shelters on the "
              "basis of biological sex. Anderson's vote with the Republican House majority "
              "to codify biological sex in state law documents his rejection of transgender "
              "ideology as a framework for West Virginia public policy.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb456+sub1.htm&yr=2025&sesstype=RS&i=456",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-riley-gaines-act-law",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("wa-b805-2", "william-anderson", "election_integrity", 0, True,
              "Anderson voted for House Bill 3016 — West Virginia's stricter photo voter ID "
              "law — which the House of Delegates passed on March 28, 2025 and Gov. Patrick "
              "Morrisey signed on May 1, 2025. The law requires every in-person voter to "
              "present a government-issued photo ID (driver's license, passport, or resident "
              "ID card) and eliminates eleven previously accepted non-photo identity documents "
              "such as Medicaid cards and utility bills. The Senate passed the measure 32-2, "
              "with only the two Democratic senators opposed. Anderson's vote for the "
              "Republican-sponsored measure reflects support for verified photo identification "
              "as a baseline requirement for in-person voting in West Virginia elections.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_history.cfm?INPUT=3016&year=2025&sessiontype=RS",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/"]),
    ]),

    # ------------ Wayne Clark (WV-R, State Delegate District 99) ------------
    ("wayne-clark", "WV", "Delegate", [
        claim("wc-b805-1", "wayne-clark", "biblical_marriage", 2, True,
              "Clark voted for West Virginia SB 456 — the Riley Gaines Act — passed by the "
              "House of Delegates on March 7, 2025 and signed by Gov. Patrick Morrisey on "
              "March 12, 2025. The law encodes in West Virginia statute that 'male' means a "
              "person whose biological sex is male (capable of producing sperm) and 'female' "
              "means a person whose biological sex is female (capable of producing ova), and "
              "restricts access to single-sex restrooms, changing facilities, and overnight "
              "accommodations in public schools, colleges, prisons, and domestic violence "
              "shelters to persons of the corresponding biological sex. Clark's affirmative "
              "vote with the Republican majority marks alignment with the principle that "
              "biological sex — not self-identified gender — determines access to "
              "sex-designated spaces in West Virginia public institutions.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb456+sub1.htm&yr=2025&sesstype=RS&i=456",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-riley-gaines-act-law",
               "https://blog.wvlegislature.gov/house-floor-session/2025/03/07/house-passes-defining-biological-sex-bill-parents-bill-of-rights/"]),
        claim("wc-b805-2", "wayne-clark", "election_integrity", 0, True,
              "Clark voted for HB 3016 — the West Virginia photo voter ID bill — passed by "
              "the House on March 28, 2025 and signed into law by Gov. Morrisey on May 1, "
              "2025. The law requires all in-person voters to show a government-issued photo "
              "ID at the polls, eliminating eleven alternative identity documents (including "
              "Medicaid cards and utility bills) that had previously been accepted. Only the "
              "Senate's two Democratic members voted against the measure in that chamber (32-2). "
              "Clark's vote to tighten voter ID requirements reflects consistent support for "
              "identity-verified elections in West Virginia.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_history.cfm?INPUT=3016&year=2025&sessiontype=RS",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/"]),
    ]),

    # ------------ Vernon Criss (WV-R, State Delegate District 12) ------------
    ("vernon-criss", "WV", "Delegate", [
        claim("vc-b805-1", "vernon-criss", "biblical_marriage", 2, True,
              "Criss voted for SB 456 — the Riley Gaines Act — signed by West Virginia Gov. "
              "Patrick Morrisey on March 12, 2025 in the legislature's first ceremonial "
              "signing event of the Morrisey administration. The law adds statutory definitions "
              "of 'male' and 'female' based on biological sex to West Virginia code, and "
              "designates single-sex restrooms, locker rooms, and overnight sleeping areas "
              "in public schools, state universities, correctional institutions, and domestic "
              "violence shelters as accessible only to persons of the corresponding biological "
              "sex. Criss, who began representing House District 12 in December 2022, voted "
              "with the overwhelming Republican House majority to codify biological sex "
              "distinctions in state law, rejecting the premise that gender identity supersedes "
              "biological sex for purposes of West Virginia public facilities law.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb456+sub1.htm&yr=2025&sesstype=RS&i=456",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-riley-gaines-act-law",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/",
               "https://ballotpedia.org/Vernon_Criss"]),
        claim("vc-b805-2", "vernon-criss", "election_integrity", 0, True,
              "Criss voted for HB 3016, West Virginia's photo voter ID bill passed by the "
              "House on March 28, 2025 and signed by Gov. Morrisey on May 1, 2025. The law "
              "requires every in-person voter to present a government-issued photo ID such "
              "as a driver's license, passport, or state resident ID card, removing eleven "
              "non-photo alternatives that had previously qualified. The Senate adopted the "
              "measure 32-2 — only the chamber's two Democrats voted no. Criss's vote for "
              "HB 3016 demonstrates support for photo-identification-based election integrity "
              "in West Virginia, consistent with his Republican caucus's priority of ensuring "
              "only eligible citizens participate in the state's elections.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_history.cfm?INPUT=3016&year=2025&sessiontype=RS",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/",
               "https://ballotpedia.org/Vernon_Criss"]),
    ]),

    # ------------ Tresa Howell (WV-R, State Delegate District 53) ------------
    ("tresa-howell", "WV", "Delegate", [
        claim("th-b805-1", "tresa-howell", "biblical_marriage", 2, True,
              "Howell voted for West Virginia SB 456 — the Riley Gaines Act — passed by the "
              "House on March 7, 2025 and signed by Gov. Patrick Morrisey on March 12, 2025. "
              "The law defines 'male' and 'female' in West Virginia state code according to "
              "biological sex observable at birth, and restricts single-sex restrooms, "
              "changing rooms, and overnight sleeping quarters in public schools, state "
              "colleges, prisons, and domestic violence shelters to persons of the matching "
              "biological sex. The bill's ceremonial signing featured former collegiate "
              "swimmer Riley Gaines. Howell's vote with the Republican House majority to "
              "codify biological sex definitions in state law reflects her rejection of "
              "gender ideology as a governing principle for West Virginia institutions.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb456+sub1.htm&yr=2025&sesstype=RS&i=456",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-riley-gaines-act-law",
               "https://blog.wvlegislature.gov/house-floor-session/2025/03/07/house-passes-defining-biological-sex-bill-parents-bill-of-rights/"]),
        claim("th-b805-2", "tresa-howell", "election_integrity", 0, True,
              "Howell voted for HB 3016, requiring photo identification for all in-person "
              "voters in West Virginia. The House passed the bill on March 28, 2025, and "
              "Gov. Patrick Morrisey signed it on May 1, 2025. Under the law, acceptable "
              "IDs are limited to government-issued photo credentials — driver's license, "
              "passport, or resident ID card — eliminating eleven alternatives such as "
              "Medicaid cards and utility bills that had previously been accepted. The Senate "
              "passed the bill 32-2, with opposition confined to the chamber's two Democratic "
              "members. Howell's support for HB 3016 demonstrates commitment to voter "
              "identity verification as a foundational election integrity requirement.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_history.cfm?INPUT=3016&year=2025&sessiontype=RS",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/"]),
    ]),

    # ------------ Stanley Adkins (WV-R, State Delegate District 50) ------------
    ("stanley-adkins", "WV", "Delegate", [
        claim("sa-b805-1", "stanley-adkins", "biblical_marriage", 2, True,
              "Adkins voted for SB 456 — the Riley Gaines Act — enacted March 12, 2025, "
              "the first ceremonial bill signing of Gov. Patrick Morrisey's administration. "
              "The law adds definitions of 'male' and 'female' based on biological sex to "
              "West Virginia state code and restricts single-sex restrooms, changing "
              "facilities, and overnight accommodations in public schools, state universities, "
              "prisons, and domestic violence shelters to persons of the matching biological "
              "sex. Adkins, representing House District 50, voted with the Republican caucus "
              "to codify biological sex as the standard governing sex-designated public spaces "
              "in West Virginia — directly rejecting the premise that transgender identity "
              "supersedes biological sex in state law.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb456+sub1.htm&yr=2025&sesstype=RS&i=456",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-riley-gaines-act-law",
               "https://wvpublic.org/riley-gaines-signed-into-law-a-bill-that-defines-men-and-women/"]),
        claim("sa-b805-2", "stanley-adkins", "election_integrity", 0, True,
              "Adkins voted for HB 3016, West Virginia's photo voter ID law passed by the "
              "House on March 28, 2025 and signed by Gov. Morrisey on May 1, 2025. The law "
              "mandates that all in-person voters present a government-issued photo ID "
              "before casting a ballot, eliminating the eleven alternative non-photo "
              "documents (including Medicaid cards, utility bills, and bank statements) that "
              "had previously been accepted. The Senate passed the companion measure 32-2, "
              "with only the body's two Democratic members voting against. Adkins's "
              "affirmative vote reflects support for photo-identity-verified elections as "
              "the standard for West Virginia in-person voting.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_history.cfm?INPUT=3016&year=2025&sessiontype=RS",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law",
               "https://westvirginiawatch.com/2025/03/28/west-virginia-house-passes-stricter-voter-photo-id-law/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
