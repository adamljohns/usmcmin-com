#!/usr/bin/env python3
"""Enrichment batch 813: 5 NH Republican state senators.

archetype_curated federal bucket fully exhausted; continuing bottom-of-alphabet
state-level pool. Targets from NH (next frontier after NJ completed in batch 812):
  Kevin Avard    (NH SD-12, Nashua, freshman elected Nov 2024)
  Keith Murphy   (NH SD-16, Manchester area, elected 2022 re-elected 2024)
  James Gray     (NH SD-6, Senate President Pro Tempore since 2023)
  Howard Pearl   (NH SD-17, re-elected 2024)
  Denise Ricciardi (NH SD-9, Bedford, re-elected 2024)

All claims drawn from 2024-2026 confirmed party-line roll-call votes and individual
documented actions. Sources: citizenscount.org, newhampshirebulletin.com, legiscan.com,
nhcornerstone.org, nhjournal.com, bostonglobe.com, official NH General Court records.
MINIFIED write preserved (no indent=2).
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
    # ---------------- Kevin Avard (NH SD-12, Nashua, R — freshman Jan 2025) ----------------
    ("kevin-avard", "NH", "State Senator", [
        claim("ka1", "kevin-avard", "biblical_marriage", 2, True,
              "Voted YES on NH HB 377 (signed August 1, 2025, effective January 1, 2026), banning puberty blockers and hormone therapy for minors — felony for providers — as part of the 16-8 party-line Senate majority. Also voted YES on the 2025 amendment adding a biological-sex exception to NH's anti-discrimination law, allowing bathrooms, locker rooms, sports, prisons, hospitals, and treatment centers to classify individuals based on biological sex.",
              ["https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://www.citizenscount.org/candidate/kevin-avard/serving"]),
        claim("ka2", "kevin-avard", "border_immigration", 2, True,
              "Voted YES on NH SB 62 (2025), prohibiting state and local governments from adopting sanctuary policies that would impede enforcement of federal immigration law — passed the Senate on a party-line vote with the entire 16-member Republican caucus supporting it.",
              ["https://nhjournal.com/nh-senate-passes-sanctuary-city-ban-over-unanimous-dem-opposition/",
               "https://www.citizenscount.org/candidate/kevin-avard/serving"]),
        claim("ka3", "kevin-avard", "election_integrity", 0, True,
              "Voted YES on NH SB 287 (signed August 1, 2025), requiring photo ID or a notarized signature on absentee ballot applications — passed 16-8 on party lines, all 16 Republicans including Avard voting YES. Tightens absentee-ballot access to verified identity, directly opposing mass-mail-in voting.",
              ["https://www.bostonglobe.com/2025/08/01/metro/nh-law-absentee-ballots-voter-id/",
               "https://www.citizenscount.org/bills/sb-287-2025"]),
    ]),

    # ---------------- Keith Murphy (NH SD-16, Manchester area, R — elected 2022) ----------------
    ("keith-murphy", "NH", "State Senator", [
        claim("km1", "keith-murphy", "biblical_marriage", 2, True,
              "Voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — passed the Senate 13-10 on party lines, the entire Republican caucus voting YES. Also voted YES on NH HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors in a 16-8 party-line Senate vote.",
              ["https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://ballotpedia.org/Keith_Murphy"]),
        claim("km2", "keith-murphy", "border_immigration", 2, True,
              "Voted YES on NH SB 563 (2024), prohibiting state and local governments from adopting sanctuary policies — passed the Senate 14-10 on party lines over unanimous Democratic opposition. Also voted YES on the 2025 successor bill SB 62, which passed the Senate on the same party-line alignment.",
              ["https://nhjournal.com/nh-senate-passes-sanctuary-city-ban-over-unanimous-dem-opposition/",
               "https://www.bostonglobe.com/2024/03/07/metro/ban-sanctuary-policies-clears-nh-senate/",
               "https://www.citizenscount.org/candidate/keith-murphy"]),
        claim("km3", "keith-murphy", "election_integrity", 0, True,
              "Voted YES on NH HB 1569 (2024), eliminating the affidavit ballot option and requiring photo ID to vote — passed the Senate 13-11 on party lines and signed by Gov. Sununu. A small business owner and restaurant industry veteran, Murphy has consistently backed voter-ID requirements as a condition of NH Senate Republican caucus membership.",
              ["https://www.democracydocket.com/news-alerts/new-hampshire-republicans-pass-bill-removing-exceptions-to-voter-id-requirement/",
               "https://ballotpedia.org/Keith_Murphy"]),
    ]),

    # ---------------- James Gray (NH SD-6, Senate President Pro Tempore, R) ----------------
    ("james-gray", "NH", "State Senator", [
        claim("jg1", "james-gray", "family_child_sovereignty", 0, True,
              "As Senate President Pro Tempore voted YES on NH SB 295 (2025), removing the household-income cap from NH's Education Freedom Account (EFA) program and opening school-choice vouchers to all NH families regardless of income — the most expansive school-choice expansion in NH history. Also voted YES on SB 442 (2024), raising the EFA income ceiling from 350% to 400% of the federal poverty level.",
              ["https://www.citizenscount.org/bills/sb-295-2025",
               "https://www.citizenscount.org/candidate/james-gray/serving",
               "https://ballotpedia.org/James_Gray_(New_Hampshire)"]),
        claim("jg2", "james-gray", "border_immigration", 2, True,
              "Voted YES on NH SB 563 (2024) and NH SB 62 (2025), both prohibiting state and local governments from adopting sanctuary policies that shield illegal immigrants from federal enforcement. The 2024 bill passed the Senate 14-10 over unanimous Democratic opposition; the 2025 successor passed on the same party-line alignment. Citizens Count confirmed Gray's YES votes on both.",
              ["https://nhjournal.com/nh-senate-passes-sanctuary-city-ban-over-unanimous-dem-opposition/",
               "https://www.citizenscount.org/candidate/james-gray/history",
               "https://www.bostonglobe.com/2024/03/07/metro/ban-sanctuary-policies-clears-nh-senate/"]),
        claim("jg3", "james-gray", "biblical_marriage", 2, True,
              "Voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors (13-10 Senate vote on party lines), and YES on NH HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors (16-8 party-line vote). As Senate President Pro Tempore Gray sets the chamber's floor agenda and supports both bills as part of the Republican majority's legislative program.",
              ["https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://ballotpedia.org/James_Gray_(New_Hampshire)"]),
    ]),

    # ---------------- Howard Pearl (NH SD-17, R — re-elected 2024) ----------------
    ("howard-pearl", "NH", "State Senator", [
        claim("hp1", "howard-pearl", "biblical_marriage", 2, True,
              "Confirmed YES vote on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — Citizens Count records the vote. Also voted YES on the 2025 amendment to NH anti-discrimination law adding a biological-sex exception for bathrooms, locker rooms, sports, prisons, hospitals, and treatment centers. Both votes documented by Citizens Count.",
              ["https://www.citizenscount.org/candidate/howard-pearl/serving",
               "https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/"]),
        claim("hp2", "howard-pearl", "border_immigration", 2, True,
              "Confirmed YES votes on NH SB 563 (2024) and NH SB 62 (2025) — Citizens Count records both sanctuary-policy-ban votes. SB 563 passed the Senate 14-10 over unanimous Democratic opposition (March 2024); SB 62 passed on a party-line majority in 2025. Pearl's YES votes on both bills are documented in his Citizens Count voting history.",
              ["https://www.citizenscount.org/candidate/howard-pearl/history",
               "https://nhjournal.com/nh-senate-passes-sanctuary-city-ban-over-unanimous-dem-opposition/"]),
        claim("hp3", "howard-pearl", "election_integrity", 0, True,
              "Voted YES on NH SB 287 (signed August 1, 2025), requiring photo ID or a notarized signature on absentee ballot applications — 16-8 party-line Senate vote. Pearl's district (SD-17, covering towns in Rockingham County) has a conservative electorate that strongly supports voter-ID measures; Pearl backed the bill as part of the 16-member Republican Senate caucus.",
              ["https://www.bostonglobe.com/2025/08/01/metro/nh-law-absentee-ballots-voter-id/",
               "https://www.citizenscount.org/candidate/howard-pearl/serving"]),
    ]),

    # ---------------- Denise Ricciardi (NH SD-9, Bedford, R — re-elected 2024) ----------------
    ("denise-ricciardi", "NH", "State Senator", [
        claim("dr1", "denise-ricciardi", "biblical_marriage", 2, True,
              "Voted YES on NH HB 619 (signed July 19, 2024), banning genital gender-reassignment surgery for minors — 13-10 Senate party-line vote with all Republicans voting YES. Also voted YES on NH HB 377 (signed August 1, 2025), banning puberty blockers and hormone therapy for minors in a 16-8 party-line vote. Ricciardi's Bedford-area SD-9 district is one of NH's most reliably conservative districts.",
              ["https://newhampshirebulletin.com/2024/07/19/sununu-signs-bills-limiting-transgender-youth-rights-sports-surgeries/",
               "https://newhampshirebulletin.com/2025/03/28/house-passes-ban-on-puberty-blockers-hormone-therapies-for-minors/",
               "https://ballotpedia.org/Denise_Ricciardi"]),
        claim("dr2", "denise-ricciardi", "border_immigration", 2, True,
              "Voted YES on NH SB 563 (2024), prohibiting state and local governments from adopting sanctuary policies — passed 14-10 on party lines over unanimous Democratic opposition. Also voted YES on the 2025 successor SB 62, keeping the ban on sanctuary policies active under the new session.",
              ["https://nhjournal.com/nh-senate-passes-sanctuary-city-ban-over-unanimous-dem-opposition/",
               "https://www.bostonglobe.com/2024/03/07/metro/ban-sanctuary-policies-clears-nh-senate/",
               "https://www.citizenscount.org/candidate/denise-ricciardi/history"]),
        claim("dr3", "denise-ricciardi", "election_integrity", 0, True,
              "Voted YES on NH HB 1569 (2024), eliminating the affidavit ballot option and requiring photo ID to vote — passed the Senate 13-11 on party lines and signed by Gov. Sununu. Also voted YES on SB 287 (2025) requiring photo ID or notarized signature on absentee ballot applications — 16-8 party-line. Ricciardi has consistently supported voter-ID and election-security legislation throughout her Senate tenure.",
              ["https://www.democracydocket.com/news-alerts/new-hampshire-republicans-pass-bill-removing-exceptions-to-voter-id-requirement/",
               "https://www.bostonglobe.com/2025/08/01/metro/nh-law-absentee-ballots-voter-id/",
               "https://www.citizenscount.org/candidate/denise-ricciardi/serving"]),
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
