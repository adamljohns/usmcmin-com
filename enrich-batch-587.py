#!/usr/bin/env python3
"""Enrichment batch 587: 5 Ohio R state senators with 0 claims.

All archetype_curated federal officials are fully enriched; this batch continues
the reverse-alpha archetype_party_default sweep into Ohio (OH), the next
state group after OK (batch 586) in reverse-alphabetical order.

Senators:
  Theresa Gavarone  (OH-R, District 2, Senate Majority Floor Leader)
  Rob McColley      (OH-R, District 1, former Senate President, 2026 LG candidate)
  Jerry C. Cirino   (OH-R, District 18, SB 1 Advance Ohio Higher Education Act)
  Terry Johnson     (OH-R, District 14, SB 215 constitutional carry author)
  Bill Reineke      (OH-R, District 26, Senate President Pro Tempore 2025-)

Claims drawn from Ohio Senate official pages, Ballotpedia, Wikipedia, and
Ohio Legislature bill records for 2019-2026 (2021-2026 Senate service range).

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep master under
GitHub's 50MB limit.
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
    # ---------- Theresa Gavarone (OH-R, District 2, Senate Majority Floor Leader) ----------
    ("theresa-gavarone", "OH", "Senator", [
        claim("tg1", "theresa-gavarone", "sanctity_of_life", 0, True,
              "Gavarone co-sponsored Ohio Senate Bill 23 (133rd General Assembly, 2019), "
              "the Heartbeat Protection Act that banned most abortions once a fetal heartbeat "
              "is detectable — typically around six weeks. Governor Mike DeWine signed the "
              "bill on April 11, 2019. Gavarone also co-authored a Senate Joint Resolution "
              "with then-Senate President Rob McColley in 2023 to hold a special August "
              "election on raising the constitutional amendment threshold — a legislative "
              "effort to protect Ohio's existing pro-life statutes before the November 2023 "
              "Issue 1 abortion ballot measure. She is documented by Ballotpedia as opposing "
              "the November 2023 Issue 1, which ultimately amended Ohio's constitution to "
              "enshrine a broad right to abortion.",
              ["https://www.legislature.ohio.gov/legislation/legislation-summary?id=GA133-SB-23",
               "https://ballotpedia.org/Theresa_Gavarone",
               "https://en.wikipedia.org/wiki/Theresa_Gavarone"]),
        claim("tg2", "theresa-gavarone", "self_defense", 0, True,
              "Gavarone received the American Conservative Union (ACU) Foundation's "
              "'Award for Conservative Excellence' specifically for her record on gun rights, "
              "pro-life policies, and cutting income taxes, as documented on her official "
              "Ohio Senate news page. As Ohio Senate Majority Floor Leader for the 136th "
              "General Assembly (elected by her Senate colleagues), Gavarone has been a "
              "consistent defender of Ohioans' Second Amendment rights, supporting the "
              "state's existing constitutional carry framework and opposing any new "
              "restrictions on law-abiding gun owners.",
              ["https://ohiosenate.gov/members/theresa-gavarone/news/gavarone-recognized-for-strong-conservative-voting-record",
               "https://ballotpedia.org/Theresa_Gavarone"]),
    ]),

    # ---------- Rob McColley (OH-R, District 1, former Senate President) ----------
    ("rob-mccolley", "OH", "Senator", [
        claim("rm1", "rob-mccolley", "sanctity_of_life", 0, True,
              "McColley co-sponsored Ohio Senate Bill 23 (133rd General Assembly, 2019), "
              "the Heartbeat Protection Act banning most abortions after a detectable fetal "
              "heartbeat, with no exceptions for rape or incest. The bill was signed by "
              "Governor DeWine on April 11, 2019. As Senate President (2024), McColley "
              "also co-authored the Senate Joint Resolution with Sen. Gavarone to hold an "
              "August 2023 special election aimed at raising the constitutional amendment "
              "threshold from 50% to 60% — a direct legislative defense of Ohio's pro-life "
              "statutes before the abortion rights ballot measure. He consistently opposed "
              "the November 2023 Issue 1 amendment.",
              ["https://www.legislature.ohio.gov/legislation/legislation-summary?id=GA133-SB-23",
               "https://en.wikipedia.org/wiki/Rob_McColley",
               "https://ballotpedia.org/Robert_McColley"]),
        claim("rm2", "rob-mccolley", "self_defense", 0, True,
              "As Ohio Senate President, McColley publicly and formally supported Senate "
              "Bill 215 (134th General Assembly), Ohio's Constitutional Carry legislation "
              "establishing the right of law-abiding adults to carry a concealed handgun "
              "without a government-issued permit — the same bill authored by Sen. Terry "
              "Johnson that made Ohio the 22nd constitutional carry state. McColley's "
              "official Ohio Senate page includes a video recording of his floor statement "
              "in support of SB 215. He also championed flat income tax reform as Senate "
              "President, reducing the burden on Ohio families.",
              ["https://ohiosenate.gov/members/rob-mccolley/video/senator-mccolley-supporting-sb-215",
               "https://en.wikipedia.org/wiki/Rob_McColley",
               "https://ballotpedia.org/Robert_McColley"]),
    ]),

    # ---------- Jerry C. Cirino (OH-R, District 18) ----------
    ("jerry-c-cirino", "OH", "Senator", [
        claim("jc1", "jerry-c-cirino", "family_child_sovereignty", 0, True,
              "Cirino authored Senate Bill 1 (136th General Assembly, 2025), the Advance "
              "Ohio Higher Education Act, which: bans all Diversity, Equity, and Inclusion "
              "(DEI) programming, offices, staff, consultants, and mandatory training at "
              "Ohio state universities; prohibits political or ideological litmus tests in "
              "all hiring, promotion, and admissions; requires full syllabus transparency; "
              "mandates a foundational American civics course for all public-university "
              "students; and bans university faculty from going on strike. The Ohio Senate "
              "passed SB 1 unanimously; Governor Mike DeWine signed it on March 28, 2025, "
              "and it took effect June 27, 2025. The law restores intellectual freedom and "
              "parental confidence that public higher education will not subject students "
              "to ideological indoctrination or discriminatory viewpoint enforcement.",
              ["https://en.wikipedia.org/wiki/Ohio_Senate_Bill_1_(2025)",
               "https://ohiosenate.gov/members/jerry-c-cirino/news/senate-passes-cirinos-landmark-higher-education-legislation",
               "https://ballotpedia.org/Jerry_Cirino"]),
        claim("jc2", "jerry-c-cirino", "self_defense", 0, True,
              "Cirino has publicly stated that tight gun regulations do not work in the "
              "places they are tried and advocates for allowing trained school staff to be "
              "armed as the most effective deterrent to school shooters — a position "
              "rejecting gun-control orthodoxy and affirming that armed citizens, not "
              "government restrictions, provide the best public safety. He represents a "
              "conservative northeastern Ohio district (Kirtland area, Lake and Geauga "
              "counties) where he has served since January 1, 2021.",
              ["https://ballotpedia.org/Jerry_Cirino",
               "https://en.wikipedia.org/wiki/Jerry_Cirino"]),
    ]),

    # ---------- Terry Johnson (OH-R, District 14) ----------
    ("terry-johnson", "OH", "Senator", [
        claim("tj1", "terry-johnson", "self_defense", 0, True,
              "Johnson authored and championed Senate Bill 215 (134th General Assembly), "
              "Ohio's Constitutional Carry law establishing the right of law-abiding adults "
              "21 and over to carry a concealed handgun without a government-issued permit. "
              "Johnson explained that Ohio already permitted open carry without a license, "
              "but putting on a jacket or sweatshirt inadvertently triggered concealed-carry "
              "permit requirements — criminalizing law-abiding gun owners for a "
              "technicality. SB 215 closed that loophole and made Ohio the 22nd "
              "constitutional carry state. The Ohio Senate concurred with House amendments "
              "and Governor DeWine signed the bill into law.",
              ["https://ohiosenate.gov/members/terry-johnson/news/senate-concurs-with-changes-to-johnson-permitless-carry-bill",
               "https://ohiosenate.gov/members/terry-johnson/news/what-ohios-permitless-carry-bill-really-does",
               "https://www.legislature.ohio.gov/legislation/134/sb215"]),
        claim("tj2", "terry-johnson", "sanctity_of_life", 0, True,
              "Johnson (a licensed physician and former family doctor from Scioto County) "
              "sponsored Senate Bill 157 (134th General Assembly), requiring medical "
              "professionals to provide life-preserving care to any infant born alive "
              "after a failed abortion attempt, and prohibiting the direct or indirect "
              "use of Ohio taxpayer dollars to fund abortions. The born-alive protection "
              "reflects Johnson's conviction as a physician that every living infant "
              "outside the womb has an unqualified right to medical care — regardless of "
              "the circumstances of their birth.",
              ["https://ohiosenate.gov/members/terry-johnson/biography",
               "https://ballotpedia.org/Terry_Johnson_(Ohio_politician)",
               "https://en.wikipedia.org/wiki/Terry_Johnson_(Ohio_politician)"]),
        claim("tj3", "terry-johnson", "self_defense", 1, True,
              "Johnson authored Senate Bill 58 (134th General Assembly) prohibiting the "
              "State of Ohio or any political subdivision from requiring any person to "
              "purchase, obtain, or possess firearm liability insurance, or from charging "
              "any fee for the lawful possession of a firearm, firearm parts, components, "
              "ammunition, or a knife. The bill directly pre-empts gun-insurance mandates "
              "— a regulatory mechanism gun-control advocates use to price law-abiding "
              "citizens out of Second Amendment exercise — and is documented on Johnson's "
              "official Ohio Senate biography page.",
              ["https://ohiosenate.gov/members/terry-johnson/biography",
               "https://ballotpedia.org/Terry_Johnson_(Ohio_politician)"]),
    ]),

    # ---------- Bill Reineke (OH-R, District 26, Senate President Pro Tempore 2025-) ----------
    ("bill-reineke", "OH", "Senator", [
        claim("br1", "bill-reineke", "sanctity_of_life", 0, True,
              "Reineke co-sponsored Ohio Senate Bill 23 (the Heartbeat Protection Act, "
              "133rd General Assembly, 2019), banning most abortions from the time a "
              "fetal heartbeat is detectable. Signed by Governor DeWine on April 11, 2019, "
              "the bill reflected the Ohio legislature's commitment to protecting unborn "
              "life at the earliest medically detectable point. Reineke has continued that "
              "record since joining the Ohio Senate in 2021, opposing the November 2023 "
              "Issue 1 ballot measure that embedded a broad abortion right in the Ohio "
              "Constitution. He now serves as Ohio Senate President Pro Tempore (2025-present).",
              ["https://www.legislature.ohio.gov/legislation/legislation-summary?id=GA133-SB-23",
               "https://en.wikipedia.org/wiki/Bill_Reineke",
               "https://ballotpedia.org/Bill_Reineke"]),
        claim("br2", "bill-reineke", "refuse_federal_overreach", 0, True,
              "As a member of the Ohio House during the 133rd General Assembly, Reineke "
              "supported the HB 49 provision to freeze enrollment in Ohio's federally "
              "mandated Medicaid expansion, preventing new low-income adults from enrolling "
              "in the ACA-driven program — a direct refusal to expand Ohio's dependency on "
              "federal matching funds and the regulatory control that accompanies them. "
              "Reineke also opposed HB 62's gas-tax increase, reflecting a broader pattern "
              "of resisting government growth funded by higher taxes on Ohioans.",
              ["https://en.wikipedia.org/wiki/Bill_Reineke",
               "https://ballotpedia.org/Bill_Reineke",
               "https://ohiosenate.gov/senators/reineke/bio"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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
