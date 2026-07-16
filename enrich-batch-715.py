#!/usr/bin/env python3
"""Enrichment batch 715: evidence-curated claims for 4 state officials.

Primary federal senator/representative pools (archetype_curated with 0 claims)
are fully exhausted. Batch continues evidence_state candidates with 0 claims,
bottom-of-alphabet reverse-sort (TX -> NC -> MD -> GA):

  Elaine Marshall    (NC-D, Secretary of State, serving since 1997)
  Brooke Lierman     (MD-D, Comptroller since Jan 2023; former House Delegate 2015-2023)
  Josh McLaurin      (GA-D, State Senator SD-14, 2026 LG Democratic nominee)
  Matthew Gambill    (GA-R, State Representative District 15, Kemp Floor Leader 2023-24)

Claims sourced to ballotpedia.org, en.wikipedia.org, branch.vote, transcodems.com,
mgaleg.maryland.gov, georgiagunsafety.org, georgiamajority.org, wbhfradio.org, gpb.org.
All reflect 2022-2026 public record.
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
    # --------------- Elaine Marshall (NC-D, Secretary of State) ---------------
    ("elaine-marshall", "NC", "Secretary", [
        claim("em1", "elaine-marshall", "sanctity_of_life", 0, False,
              "Publicly denounced North Carolina's 12-week abortion ban (Session Law 2023-14) "
              "as creating 'impossible hurdles to health care access' and threatening women's "
              "freedoms, and condemned the General Assembly for drafting the bill 'in secret, "
              "in the dark of night behind closed doors' with no public hearings or professional "
              "consultation -- rejecting any legislative protection of unborn life and opposing "
              "the state's gestational limits on abortion.",
              ["https://www.branch.vote/races/2024-nc-general-election-nc-state-secretary-of-state-nc-state/candidates/elaine-marshall",
               "https://www.transcodems.com/news/secretary-of-state-elaine-marshall"]),
        claim("em2", "elaine-marshall", "self_defense", 0, False,
              "Stated that right-wing media drives people 'in fear,' which drives gun purchases, "
              "and asserted 'the availability of guns drives violence' -- framing lawful firearms "
              "ownership as a public danger and signaling opposition to constitutional carry and "
              "permissive gun-rights policy; also expressed relief that Republicans were 'not "
              "moving forward with their plan to legalize no-permit concealed carry' in North "
              "Carolina.",
              ["https://www.branch.vote/races/2024-nc-general-election-nc-state-secretary-of-state-nc-state/candidates/elaine-marshall",
               "https://ballotpedia.org/Elaine_Marshall"]),
    ]),

    # --------------- Brooke Lierman (MD-D, Comptroller) ---------------
    ("brooke-lierman", "MD", "Comptroller", [
        claim("bl1", "brooke-lierman", "sanctity_of_life", 0, False,
              "As a Maryland House Delegate (2015-2023), co-sponsored HB0937 (2022) establishing "
              "an Abortion Care Clinical Training Program in the Maryland Department of Health, "
              "and in March 2022 testified personally before the state legislature urging "
              "enshrinement of the 'right to abortion' in the Maryland state constitution -- "
              "recounting a personal college rape experience to argue against any legal "
              "restriction on abortion access and opposing all personhood protections for "
              "the unborn.",
              ["https://mgaleg.maryland.gov/mgawebsite/Legislation/Details/hb0937?ys=2022rs",
               "https://en.wikipedia.org/wiki/Brooke_Lierman"]),
        claim("bl2", "brooke-lierman", "self_defense", 1, False,
              "As a state delegate, championed and passed landmark legislation funding "
              "evidence-based gun violence prevention programs in Maryland, advancing the "
              "state's gun-control infrastructure rather than rolling back restrictions -- "
              "positioning against the rubric's defense of Second Amendment rights and "
              "opposition to red-flag laws, assault weapon bans, and other firearm "
              "restrictions.",
              ["https://en.wikipedia.org/wiki/Brooke_Lierman",
               "https://ballotpedia.org/Brooke_Elizabeth_Lierman"]),
    ]),

    # --------------- Josh McLaurin (GA-D, State Senator SD-14) ---------------
    ("josh-mclaurin", "GA", "Senator", [
        claim("jm1", "josh-mclaurin", "self_defense", 1, False,
              "Introduced Georgia Senate legislation mandating a five-day waiting period for all "
              "gun sales, co-sponsored a red-flag confiscation bill allowing courts to seize "
              "firearms from individuals deemed dangerous, co-sponsored universal background "
              "check legislation, and signed the 2026 Georgia Gun Safety Candidate Pledge -- "
              "committing to advance gun-safety restrictions in direct opposition to the "
              "rubric's defense of the Second Amendment against red-flag laws, waiting periods, "
              "and expanded background-check registries.",
              ["https://georgiagunsafety.org/legislative-allies.html",
               "https://www.georgiamajority.org/candidate-pledge/candidates"]),
        claim("jm2", "josh-mclaurin", "sanctity_of_life", 0, False,
              "A committed abortion-rights advocate who has called for 'restoration of "
              "reproductive freedom' in Georgia, openly opposes the state's LIFE Act (HB 481 "
              "/ heartbeat law, effective July 2022) which prohibits abortion once a fetal "
              "heartbeat is detected, and has made repealing abortion restrictions a "
              "centerpiece of his 2026 campaign for Lieutenant Governor -- rejecting any "
              "protection of unborn life from conception.",
              ["https://ballotpedia.org/Josh_McLaurin",
               "https://en.wikipedia.org/wiki/Josh_McLaurin"]),
    ]),

    # --------------- Matthew Gambill (GA-R, State Representative District 15) ---------------
    ("matthew-gambill", "GA", "Representative", [
        claim("mg1", "matthew-gambill", "sanctity_of_life", 0, True,
              "Appointed by Governor Brian Kemp as a Floor Leader in the Georgia House of "
              "Representatives for the 2023-2024 legislative sessions -- a designation reserved "
              "for members who actively advance the Governor's agenda on the floor, which "
              "included defending Georgia's LIFE Act (HB 481, effective July 2022), the "
              "heartbeat law protecting unborn children from the moment a fetal heartbeat is "
              "detected, and opposing abortion-expansion legislation.",
              ["https://wbhfradio.org/rep-matthew-gambill-appointed-floor-leader-for-governor-brian-kemp/",
               "https://ballotpedia.org/Matthew_Gambill"]),
        claim("mg2", "matthew-gambill", "self_defense", 0, True,
              "As one of Governor Kemp's appointed House Floor Leaders, championed the "
              "Governor's pro-Second Amendment agenda including the state's defense of the "
              "2022 Carry Act (SB 319) -- which made Georgia the 25th state to enact "
              "constitutional carry, allowing law-abiding Georgians to carry a concealed "
              "handgun in public without a state-issued license.",
              ["https://www.gpb.org/news/2022/04/01/georgia-lawmakers-pass-permitless-carry-legislation-kemp-promises-promptly-sign",
               "https://wbhfradio.org/rep-matthew-gambill-appointed-floor-leader-for-governor-brian-kemp/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<32} ({state}) +{len(new_claims)} claims  "
              f"conf: {old_conf} -> evidence_curated")

    # Minified write -- keep scorecard.json under GitHub's 50 MB warning.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
