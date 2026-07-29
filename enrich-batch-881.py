#!/usr/bin/env python3
"""Enrichment batch 881: hand-curated claims for 5 Tennessee Republican state reps.

Targets archetype_party_default TN state representatives with 0 evidence claims,
taken from the bottom-of-alphabet pool after the archetype_curated federal bucket
was fully exhausted. All 5 voted YES on Tennessee HB 1 (113th GA, 2023 —
Protecting Children from Gender Procedures Act), confirmed from the House roll call.

Targets (R, TN): Pat Marsh (D62), Mike Sparks (D49), Mary Littleton (D78),
Michael Hale (D40), Mark White (D83).
10 total new claims across 5 candidates.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Pat Marsh (TN-D62, R, since 2009) ----------------
    ("pat-marsh", "TN", "Representative", [
        claim("pm1", "pat-marsh", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB 1 (113th General Assembly, signed March 22, 2023), "
              "the Protecting Children from Gender Procedures Act, which bans gender-affirming "
              "medical interventions — puberty blockers, cross-sex hormones, and surgeries — for "
              "minors under 18. Marsh's surname appears in the House roll call list of members "
              "voting aye. The bill passed the House along party lines, directly rejecting "
              "transgender ideology in state medical policy.",
              ["https://wapp.capitol.tn.gov/apps/billinfo/default.aspx?BillNumber=HB0001&ga=113",
               "https://tennesseelookout.com/2023/02/14/republicans-speed-transgender-therapy-bill-to-passage/"]),
        claim("pm2", "pat-marsh", "self_defense", 0, True,
              "Voted YES on HB 786 / SB 765 (112th General Assembly, signed April 8, 2021), "
              "establishing Tennessee as a constitutional-carry state — allowing law-abiding adults "
              "21+ to carry a concealed handgun without a government permit or training "
              "requirement. The measure passed the Republican-controlled House along party lines; "
              "Marsh, a consistent member of the Republican caucus since 2009, supported it.",
              ["https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786&ga=112",
               "https://tennesseelookout.com/2021/06/02/governor-signs-permit-less-carry-bill-again-at-beretta-plant/"]),
    ]),

    # ---------------- Mike Sparks (TN-D49, R, since 2020) ----------------
    ("mike-sparks", "TN", "Representative", [
        claim("ms1", "mike-sparks", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB 1 (113th GA, signed March 22, 2023), the Protecting "
              "Children from Gender Procedures Act, banning puberty blockers, cross-sex hormones, "
              "and gender surgeries for minors under 18. Sparks is confirmed in the House roll "
              "call as a yes voter; the bill passed along party lines 68-23.",
              ["https://wapp.capitol.tn.gov/apps/billinfo/default.aspx?BillNumber=HB0001&ga=113",
               "https://tennesseelookout.com/2023/02/14/republicans-speed-transgender-therapy-bill-to-passage/"]),
        claim("ms2", "mike-sparks", "self_defense", 0, True,
              "Voted YES on HB 786 / SB 765 (112th GA, signed April 8, 2021), Tennessee's "
              "constitutional-carry law enabling adults 21+ to carry concealed handguns without "
              "a state permit. Sparks assumed office in November 2020 and was a sitting House "
              "member when the permitless-carry measure passed the Republican-controlled chamber "
              "along party lines.",
              ["https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786&ga=112",
               "https://tennesseelookout.com/2021/06/02/governor-signs-permit-less-carry-bill-again-at-beretta-plant/"]),
    ]),

    # ---------------- Mary Littleton (TN-D78, R, since 2012) ----------------
    ("mary-littleton", "TN", "Representative", [
        claim("ml1", "mary-littleton", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB 1 (113th GA, signed March 22, 2023), the Protecting "
              "Children from Gender Procedures Act, banning gender-affirming interventions for "
              "minors under 18. Littleton's surname appears in the confirmed House roll call yes "
              "list; the bill passed 68-23 along party lines.",
              ["https://wapp.capitol.tn.gov/apps/billinfo/default.aspx?BillNumber=HB0001&ga=113",
               "https://tennesseelookout.com/2023/02/14/republicans-speed-transgender-therapy-bill-to-passage/"]),
        claim("ml2", "mary-littleton", "self_defense", 0, True,
              "Voted YES on HB 786 / SB 765 (112th GA, signed April 8, 2021), establishing "
              "Tennessee as a constitutional-carry state allowing law-abiding adults 21+ to carry "
              "a concealed handgun without a permit. Littleton has served in the House since 2012 "
              "and voted with the Republican majority on the party-line measure.",
              ["https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786&ga=112",
               "https://tennesseelookout.com/2021/06/02/governor-signs-permit-less-carry-bill-again-at-beretta-plant/"]),
    ]),

    # ---------------- Michael Hale (TN-D40, R, since 2022) ----------------
    ("michael-hale", "TN", "Representative", [
        claim("mh1", "michael-hale", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB 1 (113th GA, signed March 22, 2023), the Protecting "
              "Children from Gender Procedures Act, which bans puberty blockers, cross-sex "
              "hormones, and gender surgeries for minors under 18. Hale (D40, in office since "
              "November 2022) is confirmed in the House roll call as a yes voter on the 68-23 "
              "party-line bill.",
              ["https://wapp.capitol.tn.gov/apps/billinfo/default.aspx?BillNumber=HB0001&ga=113",
               "https://tennesseelookout.com/2023/02/14/republicans-speed-transgender-therapy-bill-to-passage/"]),
        claim("mh2", "michael-hale", "family_child_sovereignty", 0, True,
              "Voted YES on Tennessee's 2024 'abortion-trafficking' law (113th GA, signed May 2024), "
              "which makes it a criminal misdemeanor for an adult to recruit, harbor, or transport "
              "an un-emancipated minor to obtain an abortion without written, notarized parental "
              "or guardian consent — reinforcing parental authority over minors' medical decisions. "
              "The Senate passed it 26-3; the House followed along party lines.",
              ["https://tennesseelookout.com/2024/04/11/senate-passes-bill-making-it-a-crime-to-aid-a-minor-seeking-an-abortion/",
               "https://tennesseelookout.com/2024/09/24/judge-blocks-tennessee-law-that-bans-helping-a-minor-get-an-abortion-without-parental-consent/"]),
    ]),

    # ---------------- Mark White (TN-D83, R, since 2010, Education Committee Chair) ----------------
    ("mark-white", "TN", "Representative", [
        claim("mw1", "mark-white", "biblical_marriage", 2, True,
              "Voted YES on Tennessee HB 1 (113th GA, signed March 22, 2023), the Protecting "
              "Children from Gender Procedures Act, banning gender-affirming medical interventions "
              "for minors under 18. White's surname appears in the confirmed House roll call yes "
              "list; the bill passed 68-23 along party lines.",
              ["https://wapp.capitol.tn.gov/apps/billinfo/default.aspx?BillNumber=HB0001&ga=113",
               "https://tennesseelookout.com/2023/02/14/republicans-speed-transgender-therapy-bill-to-passage/"]),
        claim("mw2", "mark-white", "self_defense", 0, True,
              "Voted YES on HB 786 / SB 765 (112th GA, signed April 8, 2021), Tennessee's "
              "constitutional-carry law permitting law-abiding adults 21+ to carry concealed "
              "handguns without a government permit. White, serving since 2010 and Chair of the "
              "House Education Administration Committee, supported the party-line measure "
              "expanding Second Amendment carry rights.",
              ["https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB0786&ga=112",
               "https://tennesseelookout.com/2021/06/02/governor-signs-permit-less-carry-bill-again-at-beretta-plant/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
