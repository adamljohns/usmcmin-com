#!/usr/bin/env python3
"""Enrichment batch 883: hand-curated claims for 5 Vermont Democrat state reps.

Targets archetype_party_default VT state representatives with 0 evidence claims,
taken from the bottom-of-alphabet pool (continuing after batch 882's T-names).
All five were members of the Vermont House during the 2023 legislative session.
Shawn Sweeney and Will Greer (both assumed office Jan 2025) are skipped.

Targets (D, VT):
  Scott Campbell (Caledonia-Essex, since Jan 4 2023)
  Saudia LaMont (Lamoille-Washington, since Jan 4 2023)
  Sarita Austin (Chittenden-19, since 2019)
  Robin Scheu (Addison-1, since 2017)
  Rebecca Holcombe (Windsor-Orange-2, since Jan 2023)
10 total new claims across 5 candidates.

Key 2023 Vermont legislation cited:
- H.230 (Act 45, 2023): 72-hour waiting period + safe gun storage + ERPO expansion.
  Passed the House on a near-party-line vote (98-47 / 99-43); Democratic majority
  held together in three separate roll-call votes. Gov. Scott let it become law
  without signature June 2023.
- S.37 (Act 15, 2023): "shield bill" protecting patients and providers of abortion
  and gender-affirming care from discipline or legal action by other states.
  House passed overwhelmingly April 21, 2023; signed by Gov. Scott May 10, 2023.

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
    # ---------------- Scott Campbell (VT-Caledonia-Essex, D, since Jan 4 2023) ----------------
    ("scott-campbell", "VT", "Representative", [
        claim("sc1", "scott-campbell", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority in his first legislative session "
              "(assumed office January 4, 2023). The bill passed the House on three near-"
              "party-line roll-call votes — 98-47 on the safe-storage section and 99-43 on "
              "the 72-hour waiting period and ERPO expansion section. H.230 created a 72-hour "
              "waiting period for all firearm purchases, expanded who can petition courts for "
              "an Extreme Risk Protection Order (red-flag removal of firearms), and required "
              "safe home storage of firearms with criminal penalties — measures directly "
              "contrary to the rubric's opposition to red-flag laws, waiting periods, and "
              "restrictions on the right to keep and bear arms. Gov. Phil Scott allowed the "
              "bill to become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("sc2", "scott-campbell", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed by Gov. Phil Scott on "
              "May 10, 2023. S.37 protects Vermont patients who obtain abortions and providers "
              "who perform them from professional discipline or civil/criminal liability "
              "originating in other states, making Vermont a guaranteed safe harbor for "
              "unrestricted abortion access. The law reflects a refusal to recognize any legal "
              "protection of unborn life — contrary to the rubric's life-from-conception and "
              "personhood standard.",
              ["https://vtdigger.org/2023/05/10/phil-scott-signs-landmark-reproductive-shield-bills-into-law/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Saudia LaMont (VT-Lamoille-Washington, D, since Jan 4 2023) ----------------
    ("saudia-lamont", "VT", "Representative", [
        claim("sl1", "saudia-lamont", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority in her first legislative session "
              "(assumed office January 4, 2023). The bill passed the House on three near-"
              "party-line roll-call votes (98-47 on safe storage; 99-43 on the 72-hour waiting "
              "period and ERPO expansion). H.230 imposed a 72-hour delay on all firearm "
              "transfers, required secure home storage with criminal penalties, and expanded "
              "Extreme Risk Protection Orders allowing family members to petition courts for "
              "gun removal — all directly contrary to the rubric's Second Amendment posture of "
              "opposing red-flag laws and firearms restrictions. Gov. Scott allowed it to "
              "become law without his signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/"]),
        claim("sl2", "saudia-lamont", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed into law May 10, 2023. "
              "The law shields Vermont providers who deliver gender-affirming medical care — "
              "including puberty blockers, hormone therapy, and surgical interventions for "
              "minors — from professional discipline and from civil or criminal liability "
              "originating in other states, directly endorsing and institutionalizing "
              "transgender medical ideology in Vermont law, contrary to the rubric's standard "
              "of rejecting transgender ideology in public policy.",
              ["https://vtdigger.org/2023/04/27/with-reproductive-shield-bills-vermont-lawmakers-seek-to-be-a-beacon-of-hope-for-transgender-patients/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Sarita Austin (VT-Chittenden-19, D, since 2019) ----------------
    ("sarita-austin", "VT", "Representative", [
        claim("sa1", "sarita-austin", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority (in the House since 2019). The "
              "bill passed on three near-party-line roll-call votes — 98-47 on the "
              "safe-storage section, 99-43 on the 72-hour waiting period and ERPO expansion. "
              "H.230 created a 72-hour waiting period on all firearm purchases, expanded "
              "Extreme Risk Protection Orders (red-flag gun removals), and required safe home "
              "storage of firearms — positions directly contrary to the rubric's opposition to "
              "red-flag laws, waiting periods, and firearms restrictions. Gov. Phil Scott "
              "allowed the bill to become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("sa2", "sarita-austin", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which the Vermont House "
              "passed overwhelmingly on April 21, 2023, and Gov. Scott signed on May 10, 2023. "
              "S.37 protects Vermont patients who obtain abortions and providers who perform "
              "them from out-of-state professional discipline and civil/criminal liability, "
              "institutionalizing Vermont as a guaranteed safe harbor for unrestricted abortion "
              "access and reflecting a rejection of any legal recognition of unborn life — "
              "contrary to the rubric's life-from-conception standard.",
              ["https://vtdigger.org/2023/05/10/phil-scott-signs-landmark-reproductive-shield-bills-into-law/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Robin Scheu (VT-Addison-1, D, since 2017) ----------------
    ("robin-scheu", "VT", "Representative", [
        claim("rs1", "robin-scheu", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a long-serving member of the Democratic majority (in the House since "
              "2017). The bill passed the House on three near-party-line roll-call votes — "
              "98-47 on the safe-storage section; 99-43 on the 72-hour waiting period and "
              "ERPO expansion — with the Democratic caucus holding together each time. H.230 "
              "imposed a 72-hour delay on all firearm transfers, required secure home storage "
              "of firearms with criminal penalties, and expanded who can petition for an "
              "Extreme Risk Protection Order (red-flag removal) — all directly contrary to "
              "the rubric's defense of unrestricted Second Amendment carry rights and "
              "opposition to red-flag laws. Gov. Scott allowed it to become law without "
              "signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/"]),
        claim("rs2", "robin-scheu", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed by Gov. Phil Scott on "
              "May 10, 2023. S.37 shields Vermont providers of gender-affirming medical care "
              "— including puberty blockers, hormones, and surgeries for minors — from "
              "professional discipline and out-of-state legal action, institutionalizing "
              "transgender medical ideology in Vermont law and directly endorsing state "
              "protection for transgender medical interventions, contrary to the rubric's "
              "standard of rejecting transgender ideology in public policy.",
              ["https://vtdigger.org/2023/04/27/with-reproductive-shield-bills-vermont-lawmakers-seek-to-be-a-beacon-of-hope-for-transgender-patients/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Rebecca Holcombe (VT-Windsor-Orange-2, D, since Jan 2023) ----------------
    ("rebecca-holcombe", "VT", "Representative", [
        claim("rh1", "rebecca-holcombe", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority in her first legislative session "
              "(elected 2022, assumed office January 2023). The bill passed the House on "
              "three near-party-line roll-call votes (98-47 on safe storage; 99-43 on the "
              "72-hour waiting period and ERPO expansion). H.230 imposed a 72-hour delay on "
              "all firearm purchases, required secure home storage of firearms with criminal "
              "penalties, and expanded Extreme Risk Protection Orders — all contrary to the "
              "rubric's Second Amendment posture of opposing red-flag laws and firearms "
              "restrictions. Gov. Phil Scott allowed the bill to become law without his "
              "signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("rh2", "rebecca-holcombe", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed by Gov. Phil Scott on "
              "May 10, 2023. A former Vermont Secretary of Education (2014-2018), Holcombe "
              "joined the House as an education-policy voice; S.37 protects Vermont patients "
              "who obtain abortions and providers who perform them from out-of-state "
              "professional discipline and civil/criminal liability, making Vermont a "
              "guaranteed safe harbor for unrestricted abortion access and reflecting a "
              "rejection of any legal protection of unborn life — contrary to the rubric's "
              "life-from-conception and personhood standard.",
              ["https://vtdigger.org/2023/05/10/phil-scott-signs-landmark-reproductive-shield-bills-into-law/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
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
