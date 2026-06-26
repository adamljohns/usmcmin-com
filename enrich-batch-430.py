#!/usr/bin/env python3
"""Enrichment batch 430: Wisconsin State Assembly Republicans (bottom of alphabet).

archetype_curated federal bucket fully exhausted; continuing with
Wisconsin (WI) state assembly members from the bottom of the reverse-alpha list
with 0 claims.

Targets:
  Robin Vos       (WI-R, State Assembly District 33, Assembly Speaker)
  Tyler August    (WI-R, State Assembly District 31, Majority Leader, NRA Life Member)
  Shae Sortwell   (WI-R, State Assembly District 2, pro-life / 2A)
  Ron Tusler      (WI-R, State Assembly District 3, election integrity / pro-life)
  Scott Allen     (WI-R, State Assembly District 82, pro-life legislator)

Each claim cites >=1 reliable source reflecting documented voting records
or official public positions. Sources: ballotpedia.org, en.wikipedia.org,
legis.wisconsin.gov, docs.legis.wisconsin.gov, nraila.org, ivoterguide.com.

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
    # -------------- Robin Vos (WI-R, State Assembly District 33, Speaker) ----------
    ("robin-vos-wi-33", "WI", "Assembly", [
        claim("rv1", "robin-vos-wi-33", "sanctity_of_life", 0, True,
              "Publicly stated 'I believe life begins at conception' (September 2024, UW-Madison) and stated he ran for office 'to protect the lives of unborn children.' Signed four anti-abortion bills as Assembly Speaker in June 2019, including measures restricting abortion access — reflecting a consistent public pro-life posture.",
              ["https://www.dailycardinal.com/article/2024/09/vos-says-hes-open-to-finding-consensus-on-abortion-at-uw-madison-visit",
               "https://ballotpedia.org/Robin_Vos"]),
        claim("rv2", "robin-vos-wi-33", "self_defense", 1, True,
              "As Assembly Speaker, pledged Republicans will 'fight for and protect your freedom, from unnecessary red flag gun laws' and expressed openness to arming teachers and armed security personnel in schools — taking a pro-Second-Amendment posture against restrictive gun-control measures.",
              ["https://www.lacrossetribune.com/news/state-and-regional/govt-and-politics/wisconsin-assembly-speaker-robin-vos-open-to-arming-teachers-in-schools/article_b6e67610-e698-5c98-9092-6a17f256f5bc.html",
               "https://ballotpedia.org/Robin_Vos"]),
    ]),

    # -------------- Tyler August (WI-R, State Assembly District 31, Majority Leader) --
    ("tyler-august-wi-31", "WI", "Assembly", [
        claim("ta1", "tyler-august-wi-31", "sanctity_of_life", 0, True,
              "In June 2022, when Governor Tony Evers called a special legislative session to legalize abortion following the Dobbs decision, August and fellow Republicans immediately gaveled the session in and out — preventing any vote and preserving Wisconsin's 1849 abortion ban that protects unborn life from conception.",
              ["https://en.wikipedia.org/wiki/Tyler_August",
               "https://ballotpedia.org/Tyler_August"]),
        claim("ta2", "tyler-august-wi-31", "self_defense", 0, True,
              "NRA Life Member who voted in favor of Wisconsin's concealed carry legislation during his first term in the State Assembly, stating he 'supports the concept of concealed carry' — backing lawful armed self-defense as a constitutional right.",
              ["https://ballotpedia.org/Tyler_August",
               "https://legis.wisconsin.gov/assembly/31/august/"]),
    ]),

    # -------------- Shae Sortwell (WI-R, State Assembly District 2) ----------------
    ("shae-sortwell-wi-2", "WI", "Assembly", [
        claim("ss1", "shae-sortwell-wi-2", "sanctity_of_life", 4, True,
              "Believes abortion providers, including Planned Parenthood, should not receive funds from federal, state, or local governments — opposing taxpayer subsidization of the abortion industry. Sponsored 2023 Assembly Bill 975 placing a 14-week gestational limit on abortion procedures.",
              ["https://ballotpedia.org/Shae_Sortwell",
               "https://ivoterguide.com/candidate/25188/race/1430/election/985"]),
        claim("ss2", "shae-sortwell-wi-2", "self_defense", 1, True,
              "NRA-PVF endorsed for 'proven record of fighting to protect Second Amendment rights'; sponsored 2023 Assembly Bill 801 allowing persons licensed for concealed carry to possess firearms in places of worship located on private school grounds — directly opposing gun-free zone mandates that restrict lawful carry.",
              ["https://www.nraila.org/email/alerts/2022/wisconsin/general/vote-shae-sortwell-to-protect-the-second-amendment/",
               "https://ballotpedia.org/Shae_Sortwell"]),
    ]),

    # -------------- Ron Tusler (WI-R, State Assembly District 3) -------------------
    ("ron-tusler-wi-3", "WI", "Assembly", [
        claim("rt1", "ron-tusler-wi-3", "sanctity_of_life", 0, True,
              "Self-described 'proudly pro-life' legislator who testified against Medical Assistance funding for abortion providers (AB 183, May 2019) and has authored multiple pro-life bills including measures designating an unborn child as a dependent for Wisconsin income tax purposes and grant programs supporting Choose Life Wisconsin and financial assistance for adoption.",
              ["https://docs.legis.wisconsin.gov/misc/lc/hearing_testimony_and_materials/2019/ab183/ab0183_2019_05_07.pdf",
               "https://ballotpedia.org/Ron_Tusler"]),
        claim("rt2", "ron-tusler-wi-3", "election_integrity", 0, True,
              "Authored 2023 Wisconsin Assembly Bill 93 (verifying citizenship of individuals on the official voter registration list) and Assembly Bill 21 (removing ineligible voters from the official voter registration list); also co-sponsored Senate Bill 88 (whistleblower protection for municipal clerks who witness and report election fraud or irregularities) — a multi-bill election-integrity enforcement posture.",
              ["https://ballotpedia.org/Ron_Tusler",
               "https://docs.legis.wisconsin.gov/2023/legislators/assembly/2528"]),
    ]),

    # -------------- Scott Allen (WI-R, State Assembly District 82) -----------------
    ("scott-allen-wi-82", "WI", "Assembly", [
        claim("sa1", "scott-allen-wi-82", "sanctity_of_life", 0, True,
              "Consistent pro-life legislative record including bills restricting use of fetal body parts, protecting children born alive following abortion attempts, and establishing legal definitions protecting unborn life — reflecting a sustained commitment to protecting life from conception throughout his tenure in the Wisconsin State Assembly.",
              ["https://ballotpedia.org/Scott_Allen_(Wisconsin)",
               "https://docs.legis.wisconsin.gov/2023/legislators/assembly/2441"]),
        claim("sa2", "scott-allen-wi-82", "self_defense", 0, True,
              "Supported legislation allowing persons licensed for concealed carry to possess firearms in places of worship, expanding lawful carry rights for law-abiding citizens into venues previously restricted — consistent with constitutional carry principles protecting armed self-defense.",
              ["https://ballotpedia.org/Scott_Allen_(Wisconsin)",
               "https://docs.legis.wisconsin.gov/document/legislator/2025/2872"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug/wrong-state collisions."""
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
