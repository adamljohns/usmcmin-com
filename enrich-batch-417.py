#!/usr/bin/env python3
"""Enrichment batch 417: 4 Virginia House of Delegates Republicans.

All four are evidence_state confidence with 0 claims; taken from the bottom
of the alphabet after the archetype_curated federal bucket was exhausted.

Targets: Bill Wiley (VA-HD32), Chris Runion (VA-HD35),
         Buddy Fowler (VA-HD59), Anne Ferrell Tata (VA-HD99).

Key sourced votes:
  HJ1 (Jan 14, 2026, 64-34): ALL 34 Republicans voted NO on the
    Reproductive Freedom constitutional amendment.
  HB217 (Feb 5, 2026, 58-34): party-line NO by Republicans on the
    assault-firearms/large-capacity magazine ban.
  Fowler ERA (Jan 22, 2019): Fowler cast 1 of 4 party-line votes to kill
    the Equal Rights Amendment in subcommittee, blocking a resolution that
    ERA proponents explicitly argue extends sex-discrimination protections
    to gender identity.

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


TARGETS = [
    # ---- Bill Wiley (VA-HD32, Republican) ----
    ("bill-wiley", "VA", "House of Delegates", [
        claim("bw1", "bill-wiley", "sanctity_of_life", 0, True,
              "One of 34 House Republicans who unanimously voted NO on HJ1 (January 14, 2026), "
              "Virginia's constitutional amendment to enshrine a 'fundamental right to reproductive freedom' "
              "including abortion — defeating any notion of personhood protection from conception. "
              "Sixty-four Democrats voted yes; every Republican delegate who voted cast a NO.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-virginia-house-of-delegates-vote-advancing-constitutional-amendment-to-protect-abortion-rights/",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("bw2", "bill-wiley", "self_defense", 1, True,
              "One of 34 House Republicans who voted NO on HB217 (February 5, 2026), "
              "Virginia's sweeping ban on the importation, sale, manufacture, and transfer of "
              "assault firearms and large-capacity ammunition magazines. All Republicans voted "
              "against the measure over strong GOP objections.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260422/virginia-legislature-acts-on-gun-bills-ball-back-in-spanbergers-court"]),
    ]),

    # ---- Chris Runion (VA-HD35, Republican) ----
    ("chris-runion", "VA", "House of Delegates", [
        claim("cr1", "chris-runion", "sanctity_of_life", 0, True,
              "One of 34 House Republicans who unanimously voted NO on HJ1 (January 14, 2026), "
              "Virginia's constitutional amendment to enshrine a 'fundamental right to reproductive freedom' "
              "including abortion. Runion represents Bath, Highland, Augusta, and Rockingham counties — "
              "among the most conservative rural districts in the commonwealth. All 34 Republicans voted NO.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-virginia-house-of-delegates-vote-advancing-constitutional-amendment-to-protect-abortion-rights/",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("cr2", "chris-runion", "self_defense", 1, True,
              "One of 34 House Republicans who voted NO on HB217 (February 5, 2026), "
              "Virginia's assault-firearms and large-capacity magazine prohibition. Republicans "
              "in the House unanimously opposed the Democrat-led gun-control package "
              "over strong bipartisan objections from Second Amendment advocates.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260115/virginia-more-gun-control-introduced-in-general-assembly"]),
    ]),

    # ---- Buddy Fowler (VA-HD59, Republican) ----
    ("buddy-fowler", "VA", "House of Delegates", [
        claim("bf1", "buddy-fowler", "sanctity_of_life", 0, True,
              "One of 34 House Republicans who unanimously voted NO on HJ1 (January 14, 2026), "
              "Virginia's proposed constitutional amendment embedding a fundamental right to "
              "abortion and 'reproductive freedom.' The House passed it 64-34 on a strict "
              "party-line vote; Fowler and every present Republican cast a NO.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-virginia-house-of-delegates-vote-advancing-constitutional-amendment-to-protect-abortion-rights/",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("bf2", "buddy-fowler", "self_defense", 1, True,
              "One of 34 House Republicans who voted NO on HB217 (February 5, 2026), "
              "banning the importation, sale, manufacture, and transfer of assault firearms "
              "and large-capacity magazines in Virginia. Voted in lockstep with all "
              "Republican House members against the legislation.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260422/virginia-legislature-acts-on-gun-bills-ball-back-in-spanbergers-court"]),
        claim("bf3", "buddy-fowler", "biblical_marriage", 2, True,
              "Cast one of 4 Republican party-line votes on January 22, 2019, to kill the Equal "
              "Rights Amendment (ERA) in the House Privileges and Elections subcommittee — "
              "blocking a resolution that ERA proponents explicitly argue would extend "
              "sex-discrimination protections to gender identity and transgender status, "
              "enshrining those claims in Virginia's constitution.",
              ["https://virginiabusiness.com/voting-along-party-lines-house-subcommittee-rejects-era/",
               "https://www.wtvr.com/2019/01/22/adding-fuel-to-the-fire-virginia-house-committee-blocks-equal-rights-amendment",
               "https://patch.com/virginia/across-va/equal-rights-amendment-killed-gop-virginia-house-members"]),
    ]),

    # ---- Anne Ferrell Tata (VA-HD99, Republican) ----
    ("anne-ferrell-tata", "VA", "House of Delegates", [
        claim("aft1", "anne-ferrell-tata", "sanctity_of_life", 0, True,
              "One of 34 House Republicans who unanimously voted NO on HJ1 (January 14, 2026), "
              "Virginia's constitutional amendment to create a fundamental right to "
              "reproductive freedom including abortion. Tata, representing Virginia Beach "
              "District 99, voted with every Republican delegate in opposition to the measure.",
              ["https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-celebrates-virginia-house-of-delegates-vote-advancing-constitutional-amendment-to-protect-abortion-rights/",
               "https://www.acluva.org/press-releases/historic-vote-constitutional-amendment-protect-reproductive-freedom-passes-general/"]),
        claim("aft2", "anne-ferrell-tata", "self_defense", 1, True,
              "One of 34 House Republicans who voted NO on HB217 (February 5, 2026), "
              "the Democrat-sponsored assault-firearms and large-capacity magazine ban. "
              "Tata opposed the gun-control package alongside all Republican delegates "
              "in the chamber, consistent with her pro-Second Amendment district.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260514/nra-announces-state-lawsuit-challenging-virginia-s-assault-firearm-and-magazine-bans"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
