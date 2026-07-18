#!/usr/bin/env python3
"""Enrichment batch 744: 5 Florida state senators — Tom Leek (SD-7),
Tom A. Wright (SD-8), Stan McClain (SD-9), Tracie Davis (SD-5),
Tina Scott Polsky (SD-30).

archetype_curated pool fully exhausted; continuing FL state-senator enrichment
from the evidence_state pool (32 FL state senators with 0 claims remaining as
of 2026-07-18).

Votes confirmed via Florida Politics, Wikipedia (Heartbeat Protection Act),
myfloridahouse.gov co-introducer records, and open.pluralpolicy.com:
- HB 543 (constitutional carry): House 76-32 (~Mar 29, 2023), Senate 27-13
  (Apr 3, 2023); signed Apr 3, 2023.
- SB 300 (6-week abortion ban): Senate 26-13, House 70-40 (Apr 13, 2023);
  signed Apr 13, 2023.
- FL Amendment 4 (right to abortion): voted down Nov 2024.

Sources: en.wikipedia.org, floridapolitics.com, flsenate.gov,
myfloridahouse.gov, ballotpedia.org, open.pluralpolicy.com.
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
    # -------- Tom Leek (FL SD-7, State Senator since Nov 2024; formerly FL House HD-25, 2016–2024) --------
    ("tom-leek", "FL", "Senator", [
        claim("tl1", "tom-leek", "self_defense", 0, True,
              "Co-introduced Florida HB 543 (2023) — the constitutional/permitless carry bill — and voted YES as it passed the Florida House 76–32 (~March 29, 2023), eliminating the permit requirement for law-eligible Floridians to carry concealed firearms in public. Governor DeSantis signed HB 543 into law April 3, 2023, making Florida the 26th constitutional-carry state. Leek's primary co-sponsorship signals full alignment with the rubric's constitutional carry standard.",
              ["https://www.myfloridahouse.gov/Sections/Bills/billsdetail.aspx?BillId=77202",
               "https://floridapolitics.com/archives/598200-house-passes-gun-bill-allowing-concealed-carry-without-a-permit/",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
        claim("tl2", "tom-leek", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (House passed 70–40, April 13, 2023), the 'Heartbeat Protection Act' banning abortion after approximately 6 weeks of pregnancy — the most restrictive abortion limit in Florida history at the time of passage — aligning with the rubric's protection of unborn life from earliest detectable heartbeat.",
              ["https://en.wikipedia.org/wiki/Heartbeat_Protection_Act",
               "https://floridapolitics.com/archives/600358-senate-passes-six-week-abortion-ban/"]),
    ]),

    # -------- Tom A. Wright (FL SD-8, State Senator since 2018) --------
    ("tom-a-wright", "FL", "Senator", [
        claim("taw1", "tom-a-wright", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (Senate passed 26–13, April 13, 2023), the 'Heartbeat Protection Act' banning abortion after approximately 6 weeks of pregnancy — the most restrictive abortion limit in Florida history at the time — aligning with the rubric's protection of unborn life from earliest detectable heartbeat.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://floridapolitics.com/archives/600358-senate-passes-six-week-abortion-ban/"]),
        claim("taw2", "tom-a-wright", "self_defense", 0, True,
              "Voted YES on Florida HB 543 (Senate passed 27–13, April 3, 2023), establishing constitutional/permitless carry — eliminating the state permit requirement for law-eligible citizens to carry concealed firearms in public. Governor DeSantis signed the bill the same day, making Florida the 26th constitutional-carry state — consistent with the rubric's support for constitutional carry rights.",
              ["https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/",
               "https://www.flsenate.gov/Session/Bill/2023/543"]),
        claim("taw3", "tom-a-wright", "border_immigration", 3, True,
              "Voted YES on Florida SB 1718 (passed Florida Senate April 28, 2023; signed May 10, 2023), requiring private employers with 25 or more workers to use the E-Verify system to confirm new hires' legal work authorization, with daily $1,000 fines and license suspension for non-compliant employers — part of what Governor DeSantis called 'the strongest anti-illegal immigration legislation in the country' — aligning with the rubric's support for mandatory E-Verify enforcement.",
              ["https://www.flsenate.gov/Session/Bill/2023/1718",
               "https://www.flgov.com/eog/news/press/2023/governor-ron-desantis-signs-strongest-anti-illegal-immigration-legislation-country",
               "https://www.npr.org/2023/05/30/1177657218/florida-anti-immigration-law-1718-desantis"]),
    ]),

    # -------- Stan McClain (FL SD-9, State Senator since Nov 2024; formerly FL House HD-23/27, 2016–2024) --------
    ("stan-mcclain", "FL", "Senator", [
        claim("sm1", "stan-mcclain", "self_defense", 0, True,
              "Co-introduced Florida HB 543 (2023) — the constitutional/permitless carry bill — and voted YES as it passed the Florida House 76–32 (~March 29, 2023), eliminating the state permit requirement for law-eligible Floridians to carry concealed firearms in public. Governor DeSantis signed HB 543 into law April 3, 2023. McClain's primary co-sponsorship of the flagship carry bill reflects strong first-order alignment with the rubric's constitutional carry standard.",
              ["https://www.myfloridahouse.gov/Sections/Bills/billsdetail.aspx?BillId=77202",
               "https://floridapolitics.com/archives/598200-house-passes-gun-bill-allowing-concealed-carry-without-a-permit/",
               "https://floridapolitics.com/archives/599712-legislature-passes-permitless-carry-bill/"]),
        claim("sm2", "stan-mcclain", "sanctity_of_life", 0, True,
              "Voted YES on Florida SB 300 (House passed 70–40, April 13, 2023), the 'Heartbeat Protection Act' banning abortion after approximately 6 weeks of pregnancy — Florida's most restrictive abortion limit at the time of passage — aligning with the rubric's protection of unborn life from earliest detectable heartbeat.",
              ["https://en.wikipedia.org/wiki/Heartbeat_Protection_Act",
               "https://floridapolitics.com/archives/600358-senate-passes-six-week-abortion-ban/"]),
    ]),

    # -------- Tracie Davis (FL SD-5, State Senator since 2022) --------
    ("tracie-davis", "FL", "Senator", [
        claim("td1", "tracie-davis", "sanctity_of_life", 0, False,
              "A consistent abortion-rights advocate: publicly endorsed Florida Amendment 4 (Right to Abortion Initiative, November 2024) which sought to embed a broad right to abortion in the Florida Constitution; and in the 2026 legislative session introduced SB 1308 'Reproductive Freedom' to expand abortion access in Florida (died in Health Policy, March 13, 2026). Both stances directly reject the rubric's protection of unborn life from conception.",
              ["https://ballotpedia.org/Florida_Amendment_4,_Right_to_Abortion_Initiative_(2024)",
               "https://www.flsenate.gov/Session/Bill/2026/1308"]),
        claim("td2", "tracie-davis", "self_defense", 1, False,
              "Sponsored SB 1336 'Firearm Hold Agreements' in the 2026 Florida legislative session — a measure establishing voluntary or court-ordered firearm surrender agreements — reflecting a regulatory approach to disarming citizens that contradicts the rubric's opposition to red-flag-style restrictions on the rights of law-abiding gun owners.",
              ["https://www.flsenate.gov/Session/Bill/2026/1336",
               "https://ballotpedia.org/Tracie_Davis"]),
    ]),

    # -------- Tina Scott Polsky (FL SD-30, State Senator since 2022) --------
    ("tina-scott-polsky", "FL", "Senator", [
        claim("tp1", "tina-scott-polsky", "sanctity_of_life", 0, False,
              "Voted NO on Florida SB 300 (Senate 26–13, April 13, 2023), the 'Heartbeat Protection Act' banning abortion after 6 weeks; publicly endorsed Florida Amendment 4 (Right to Abortion Initiative, November 2024); and previously sponsored SB 300 (2022) as a legislative counter-measure to abortion restrictions — a consistent multi-session record rejecting the rubric's protection of unborn life from conception.",
              ["https://open.pluralpolicy.com/vote/c902f7d8-6327-46a6-8b00-a20bf83fa512/",
               "https://ballotpedia.org/Florida_Amendment_4,_Right_to_Abortion_Initiative_(2024)",
               "https://en.wikipedia.org/wiki/Tina_Polsky"]),
        claim("tp2", "tina-scott-polsky", "biblical_marriage", 4, False,
              "Opposed Florida's 2022 repeal of the Reedy Creek Improvement District, publicly stating Disney was being 'attacked' for expressing support for its LGBTQ customers and employees and demanding whether the action was being taken 'based on spite' — a direct defense of corporate LGBTQ promotion that contradicts the rubric's opposition to advancing LGBTQ ideology in law and public life.",
              ["https://en.wikipedia.org/wiki/Tina_Polsky",
               "https://en.wikipedia.org/wiki/Disney_and_Florida%27s_Parental_Rights_in_Education_Act"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
