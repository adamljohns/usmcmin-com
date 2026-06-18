#!/usr/bin/env python3
"""Enrichment batch 278: hand-curated claims for 5 state officials (WY/WV/VA).

archetype_curated federal senators/reps bucket fully exhausted; targets drawn
from evidence_state candidates at the bottom of the alphabet (WY→WV→VA):
  Keith Kautz (WY AG-R), J.B. McCuskey (WV AG-R), Kris Warner (WV SoS-R),
  Tara Durant (VA State Senator D27-R), Todd Pillion (VA State Senator D6-R).

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # -------------- Keith Kautz (WY-R, Attorney General) --------------
    ("keith-kautz", "WY", "Attorney General", [
        claim("kk1", "keith-kautz", "sanctity_of_life", 0, True,
              "As Wyoming AG, Kautz's office petitioned the Wyoming Supreme Court to rehear its January 2026 ruling striking down Wyoming's near-total abortion bans, contending the court 'made numerous mistakes' — actively defending life-from-conception prohibitions through litigation.",
              ["https://www.wyomingpublicmedia.org/politics-government/2026-01-20/wyoming-petitions-state-supreme-court-to-rehear-abortion-case",
               "https://www.wyomingpublicmedia.org/politics-government/2026-01-06/wyoming-supreme-court-protects-abortion-access"]),
        claim("kk2", "keith-kautz", "sanctity_of_life", 1, True,
              "The Wyoming abortion statutes Kautz defends are near-total bans — not gestational-limit restrictions — reflecting an abolition-level posture. Governor Gordon specifically cited Kautz as someone who 'spoke out against abortion' when appointing him AG in July 2025, and Kautz had publicly joined Wyoming leaders praying 'for life' shortly before taking office.",
              ["https://ballotpedia.org/Keith_G._Kautz",
               "https://www.wyomingpublicmedia.org/politics-government/2025-04-17/recently-retired-state-supreme-court-justice-joined-wyoming-leaders-praying-for-life"]),
    ]),

    # -------------- J.B. McCuskey (WV-R, Attorney General) --------------
    ("jb-mccuskey", "WV", "Attorney General", [
        claim("jmc1", "jb-mccuskey", "sanctity_of_life", 0, True,
              "During his 2024 AG campaign, McCuskey pledged to support restrictions on abortion and protect the conservative values of West Virginians — a publicly stated pro-life, personhood-respecting commitment for the state's chief law-enforcement officer.",
              ["https://ballotpedia.org/John_B._McCuskey",
               "https://ballotpedia.org/West_Virginia_Attorney_General_election,_2024"]),
        claim("jmc2", "jb-mccuskey", "self_defense", 1, True,
              "McCuskey explicitly pledged to 'oppose restrictions on firearms' as a core commitment of his AG candidacy, aligning with the Second Amendment absolutist posture of refusing new gun control mandates.",
              ["https://ballotpedia.org/West_Virginia_Attorney_General_election,_2024",
               "https://en.wikipedia.org/wiki/JB_McCuskey"]),
        claim("jmc3", "jb-mccuskey", "refuse_federal_overreach", 0, True,
              "Committed to making multi-state lawsuits against federal government overreach a top priority, stating he would prioritize 'suing the federal government to overturn policies that challenged West Virginia values' — a posture of state sovereignty against federal encroachment.",
              ["https://ballotpedia.org/John_B._McCuskey",
               "https://ballotpedia.org/West_Virginia_Attorney_General_election,_2024"]),
    ]),

    # -------------- Kris Warner (WV-R, Secretary of State) --------------
    ("kris-warner", "WV", "Secretary of State", [
        claim("kw1", "kris-warner", "election_integrity", 0, True,
              "Championed a 2025 legislative package including HB 3016 (photo ID required for all in-person voting), SB 486 (expressly limiting voting to U.S. citizens only), and SB 490 (banning ranked-choice voting) — a comprehensive election-security agenda enacted in a single session.",
              ["https://sos.wv.gov/news/Pages/05-08-25-A.aspx",
               "https://ballotpedia.org/Kris_Warner"]),
        claim("kw2", "kris-warner", "refuse_federal_overreach", 0, True,
              "Publicly refused a U.S. Department of Justice request for protected personal voter information, declaring 'Turning it over to the federal government, which is contrary to State law, will simply not happen' — defending state authority over voter rolls against federal intrusion.",
              ["https://sos.wv.gov/article/wv-secretary-state-kris-warner-says-he-will-not-release-protected-personal-voter",
               "https://ballotpedia.org/Kris_Warner"]),
    ]),

    # -------------- Tara Durant (VA-R, State Senator District 27) --------------
    ("tara-durant", "VA", "State Senator", [
        claim("td1", "tara-durant", "sanctity_of_life", 0, True,
              "One of 19 VA Senate Republicans who voted against the all-trimester abortion constitutional amendment (SJ1, 2025 and 2026 sessions), unanimously opposing the Democratic majority's effort to enshrine unrestricted abortion through the third trimester into Virginia's constitution.",
              ["https://sbaprolife.org/newsroom/press-releases/va-senate-passes-all-trimester-abortion-amendment",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("td2", "tara-durant", "family_child_sovereignty", 0, True,
              "Introduced a floor amendment to the Virginia abortion constitutional amendment that would have added parental rights protections — requiring parental involvement in minors' abortion decisions — which Democrats voted down, demonstrating Durant's commitment to parental authority over children's medical decisions.",
              ["https://sbaprolife.org/newsroom/press-releases/va-senate-passes-all-trimester-abortion-amendment",
               "https://ballotpedia.org/Tara_Durant"]),
    ]),

    # -------------- Todd Pillion (VA-R, State Senator District 6) --------------
    ("todd-pillion", "VA", "State Senate", [
        claim("tp1", "todd-pillion", "sanctity_of_life", 0, True,
              "Voted against SB727 (April 22, 2026) — the Virginia Senate concurrence on the all-trimester abortion constitutional amendment — joining the unanimous Republican caucus in opposing unrestricted abortion access through the third trimester enshrined in the state constitution.",
              ["https://lis.virginia.gov/vote-details/SB727/20261/SV1580",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("tp2", "todd-pillion", "self_defense", 1, True,
              "NRA-evaluated Virginia Republican state senator (confirmed on Vote Smart) representing rural southwest Virginia Appalachian districts (Buchanan, Dickenson, Russell, Scott counties) with deep Second Amendment culture; votes consistently with the Republican caucus opposing gun control proposals advanced by Virginia's Democratic majority.",
              ["https://justfacts.votesmart.org/candidate/evaluations/155966/todd-pillion",
               "https://www.nrapvf.org/grades/virginia/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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
