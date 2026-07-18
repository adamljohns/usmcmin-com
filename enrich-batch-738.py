#!/usr/bin/env python3
"""Enrichment batch 738: hand-curated claims for 4 NJ Republican state senators.

archetype_curated federal pool fully exhausted; moving to archetype_party_default
R state senators from the bottom of the alphabet. NJ is the next available state
after WY/WV/WI/WA/VA/VT/TX/TN are all evidence_curated.

Targets (reverse-alpha by name within NJ):
  Parker Space (NJ-24), Mike Testa (NJ-01),
  Vincent J. Polistina (NJ-02), Joseph Pennacchio (NJ-26).

Sources: insidernj.com, njleg.state.nj.us, pub.njleg.state.nj.us,
newjerseymonitor.com, nj.gov, ballotpedia.org, ballotready.org,
senatenj.com, ivoterguide.com.
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
    # ---------------- Parker Space (NJ-24, State Senator) ----------------
    ("parker-space", "NJ", "Senator", [
        claim("ps1", "parker-space", "sanctity_of_life", 0, True,
              "New Jersey Right to Life PAC-endorsed senator who, as a state assemblyman, introduced the Pain-Capable Unborn Child Protection Act (banning abortion from 20 weeks of fertilization), the Born-Alive Abortion Survivors Protection Act, and a parental-notification bill — placing him firmly in the pro-life, personhood-aligned wing of the NJ GOP. Planned Parenthood endorsed his Democratic opponent for his Senate seat, confirming his anti-abortion-industry standing.",
              ["https://www.insidernj.com/press-release/new-jersey-right-to-life-state-pac-endorses-parker-space-for-senate-and-dawn-fantasia-mike-inganamort-for-assembly/",
               "https://njrtl.org/"]),
        claim("ps2", "parker-space", "sanctity_of_life", 3, True,
              "Opposed physician-assisted suicide legislation in the New Jersey Assembly — extending his sanctity-of-life position from abortion to euthanasia, consistent with the rubric's opposition to state-facilitated killing at either end of life.",
              ["https://www.insidernj.com/press-release/new-jersey-right-to-life-state-pac-endorses-parker-space-for-senate-and-dawn-fantasia-mike-inganamort-for-assembly/"]),
        claim("ps3", "parker-space", "self_defense", 1, True,
              "Introduced S3972 (March 2026) to remove New Jersey's magazine-capacity limits, directly challenging one of the state's most restrictive gun laws and defending the right of law-abiding owners to possess standard-capacity firearms.",
              ["https://pub.njleg.state.nj.us/Bills/2026/S4000/3972_I1.HTM",
               "https://legiscan.com/NJ/people/parker-space/id/15979"]),
    ]),

    # ---------------- Mike Testa (NJ-01, State Senator) ----------------
    ("mike-testa", "NJ", "Senator", [
        claim("mt1", "mike-testa", "self_defense", 1, True,
              "Self-described 'unapologetic pro-gun, pro-taxpayer, conservative Republican' who publicly opposed Gov. Murphy's COVID-era emergency closure of gun stores, defending firearms retailers and Second Amendment rights against executive overreach.",
              ["https://en.wikipedia.org/wiki/Mike_Testa",
               "https://ballotpedia.org/Mike_Testa_Jr."]),
        claim("mt2", "mike-testa", "economic_stewardship", 2, True,
              "Sponsors legislation requiring a two-thirds legislative supermajority before any New Jersey state tax may be raised — a structural guard against deficit spending and casual tax increases in what is routinely ranked the nation's highest-taxed state.",
              ["https://www.ballotready.org/people/mike-testa",
               "https://ballotpedia.org/Mike_Testa_Jr."]),
    ]),

    # ---------------- Vincent J. Polistina (NJ-02, State Senator) ----------------
    ("vincent-j-polistina", "NJ", "Senator", [
        claim("vp1", "vincent-j-polistina", "economic_stewardship", 2, True,
              "Introduced legislation to exempt tips from New Jersey's gross income tax, arguing 'taxing tips is like taking credit for someone else's hard work' — part of a broader tax-relief agenda in one of the nation's highest-taxed states.",
              ["https://www.senatenj.com/m/newsflash/Home/Detail/455",
               "https://www.roi-nj.com/2024/03/27/politics/different-vision-polistina-questions-high-costs-of-housing-education-clean-energy-and-health-care/"]),
        claim("vp2", "vincent-j-polistina", "sanctity_of_life", 0, True,
              "Voted no on NJ S49 (Freedom of Reproductive Choice Act, January 2022), opposing the codification of abortion-on-demand into state law — one of all 15 Republican senators who voted against the bill, which removed remaining statutory protections for unborn children.",
              ["https://newjerseymonitor.com/2022/01/13/murphy-signs-law-solidifying-abortion-rights-in-new-jersey/",
               "https://www.nj.gov/health/news/2022/approved/20220113a.shtml"]),
    ]),

    # ---------------- Joseph Pennacchio (NJ-26, State Senator) ----------------
    ("joseph-pennacchio", "NJ", "Senator", [
        claim("jp1", "joseph-pennacchio", "sanctity_of_life", 0, True,
              "Voted no on NJ S49 (Freedom of Reproductive Choice Act, January 2022), joining all 15 Senate Republicans in opposing the bill that codified abortion-on-demand into state law; also received recognition from the New Jersey Family Policy Council for a consistently pro-family, pro-life legislative record.",
              ["https://www.insidernj.com/press-release/senate-approves-weinberg-greenstein-sweeney-freedom-reproductive-choice-act/",
               "https://justfacts.votesmart.org/candidate/55025/joseph-pennacchio"]),
        claim("jp2", "joseph-pennacchio", "sanctity_of_life", 4, True,
              "Publicly stated that Planned Parenthood and other abortion providers should not receive funds from federal, state, or local governments (including Title X grants) — an anti-abortion-funding position that reflects never taking financial support from PP, NARAL, or EMILY's List.",
              ["https://ivoterguide.com/candidate/58240/race/18530/election/1048",
               "https://ballotpedia.org/Joseph_Pennacchio"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions."""
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
