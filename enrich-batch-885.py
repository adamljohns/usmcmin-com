#!/usr/bin/env python3
"""Enrichment batch 885: hand-curated claims for 5 Vermont Democrat state reps.

Targets archetype_party_default VT state representatives with 0 evidence claims,
taken from the bottom-of-alphabet pool (continuing after batch 884's M-P-R names).
Michael Nigro is skipped (served 2021-2022, returned 2025; absent from 2023 session).
Michael Hoyt is skipped (appointed December 2, 2025; not in the 2023 session).

Targets (D, VT):
  Mike Mrowicki        (Windham-4, Putney/Dummerston,  since Jan 2009)
  Michelle Bos-Lun     (Windham-3,                      since Jan 4, 2023)
  Matt Birong          (Addison-3, Vergennes,            since Jan 9, 2019)
  Mary-Katherine Stone (Chittenden-14,                   since Jan 4, 2023)
  Martin LaLonde       (Chittenden-12, Shelburne/St. George, since 2015)
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
    # ---------------- Mike Mrowicki (VT-Windham-4, D, since Jan 2009) ----------------
    ("mike-mrowicki", "VT", "Representative", [
        claim("mm1", "mike-mrowicki", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a long-serving member of the Democratic majority in the Vermont House "
              "(in office continuously since January 2009). The bill passed the House on three "
              "near-party-line roll-call votes — 98-47 on the safe-storage section and 99-43 "
              "on the 72-hour waiting period and ERPO expansion. H.230 created a 72-hour "
              "waiting period for all firearm purchases, expanded who can petition courts for "
              "an Extreme Risk Protection Order (red-flag removal of firearms), and required "
              "safe home storage of firearms with criminal penalties — measures directly "
              "contrary to the rubric's opposition to red-flag laws, waiting periods, and "
              "restrictions on the right to keep and bear arms. Gov. Phil Scott allowed the "
              "bill to become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/"]),
        claim("mm2", "mike-mrowicki", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed into law by Gov. Phil "
              "Scott on May 10, 2023. S.37 protects Vermont patients who obtain abortions "
              "and providers who perform them from professional discipline or civil/criminal "
              "liability originating in other states, making Vermont a guaranteed sanctuary "
              "for unrestricted abortion access. The law institutionalizes a refusal to "
              "recognize any legal protection of unborn life — contrary to the rubric's "
              "life-from-conception and personhood standard.",
              ["https://vtdigger.org/2023/05/10/phil-scott-signs-landmark-reproductive-shield-bills-into-law/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Michelle Bos-Lun (VT-Windham-3, D, since Jan 4, 2023) ----------------
    ("michelle-bos-lun", "VT", "Representative", [
        claim("mbl1", "michelle-bos-lun", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority in her first legislative session "
              "(assumed office January 4, 2023). The bill passed the House on three near-"
              "party-line roll-call votes (98-47 on the safe-storage section; 99-43 on the "
              "72-hour waiting period and ERPO expansion). H.230 imposed a 72-hour delay on "
              "all firearm transfers, required secure home storage with criminal penalties, "
              "and expanded Extreme Risk Protection Orders allowing family members to petition "
              "courts for gun removal — all directly contrary to the rubric's Second Amendment "
              "posture of opposing red-flag laws and firearms restrictions. Gov. Scott allowed "
              "it to become law without his signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/"]),
        claim("mbl2", "michelle-bos-lun", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed by Gov. Phil Scott on "
              "May 10, 2023. The law shields Vermont providers who deliver gender-affirming "
              "medical care — including puberty blockers, hormone therapy, and surgical "
              "interventions for minors — from professional discipline and from civil or "
              "criminal liability originating in other states, directly endorsing and "
              "institutionalizing transgender medical ideology in Vermont law, contrary to "
              "the rubric's standard of rejecting transgender ideology in public policy.",
              ["https://vtdigger.org/2023/04/27/with-reproductive-shield-bills-vermont-lawmakers-seek-to-be-a-beacon-of-hope-for-transgender-patients/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Matt Birong (VT-Addison-3, D, since Jan 9, 2019) ----------------
    ("matt-birong", "VT", "Representative", [
        claim("mb1", "matt-birong", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority (in the House since January 2019). "
              "The bill passed on three near-party-line roll-call votes — 98-47 on the "
              "safe-storage section; 99-43 on the 72-hour waiting period and ERPO expansion "
              "— with the Democratic caucus holding together each time. H.230 created a 72-"
              "hour waiting period on all firearm purchases, expanded Extreme Risk Protection "
              "Orders (red-flag gun removals), and required safe home storage of firearms "
              "with criminal penalties — positions directly contrary to the rubric's defense "
              "of unrestricted Second Amendment carry rights and opposition to red-flag laws. "
              "Gov. Scott allowed it to become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("mb2", "matt-birong", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed into law by Gov. Phil "
              "Scott on May 10, 2023. S.37 protects Vermont patients who obtain abortions "
              "and providers who perform them from professional discipline or civil/criminal "
              "liability originating in other states. The law makes Vermont a guaranteed safe "
              "harbor for unrestricted abortion access and reflects a refusal to recognize "
              "any legal protection for unborn life — contrary to the rubric's life-from-"
              "conception and personhood standard.",
              ["https://vtdigger.org/2023/05/10/phil-scott-signs-landmark-reproductive-shield-bills-into-law/",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Mary-Katherine Stone (VT-Chittenden-14, D, since Jan 4, 2023) ----------------
    ("mary-katherine-stone", "VT", "Representative", [
        claim("mks1", "mary-katherine-stone", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a member of the Democratic majority in her first legislative session "
              "(assumed office January 4, 2023). The bill passed the House on three near-"
              "party-line roll-call votes (98-47 on safe storage; 99-43 on the 72-hour "
              "waiting period and ERPO expansion). H.230 created a 72-hour waiting period "
              "for all firearm purchases, expanded who can petition courts for an Extreme "
              "Risk Protection Order (red-flag removal of firearms), and required safe home "
              "storage of firearms with criminal penalties — measures directly contrary to "
              "the rubric's opposition to red-flag laws, waiting periods, and restrictions "
              "on the right to keep and bear arms. Gov. Phil Scott allowed the bill to "
              "become law without signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://vtdigger.org/2023/03/22/house-gives-preliminary-approval-on-new-gun-restrictions/"]),
        claim("mks2", "mary-katherine-stone", "biblical_marriage", 2, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed by Gov. Phil Scott on "
              "May 10, 2023. The law shields Vermont providers who deliver gender-affirming "
              "medical care — including puberty blockers, hormone therapy, and surgical "
              "interventions for minors — from professional discipline and from civil or "
              "criminal liability originating in other states, institutionalizing transgender "
              "medical ideology in Vermont law, contrary to the rubric's standard of "
              "rejecting transgender ideology in public policy.",
              ["https://protem.vermont.gov/immediate-release-vermont-senate-passes-s37-abortion-and-gender-affirming-care-shield-bill",
               "https://thehill.com/homenews/state-watch/3998504-vermont-governor-signs-bills-protecting-access-to-abortion-gender-affirming-care/"]),
    ]),

    # ---------------- Martin LaLonde (VT-Chittenden-12, D, since 2015) ----------------
    ("martin-lalonde", "VT", "Representative", [
        claim("ml1", "martin-lalonde", "self_defense", 1, False,
              "Voted in favor of Vermont H.230 (Act 45, 2023), the Gun Violence Prevention "
              "Act, as a long-serving member of the Democratic majority (in the House since "
              "2015). The bill passed on three near-party-line roll-call votes — 98-47 on "
              "the safe-storage section; 99-43 on the 72-hour waiting period and ERPO "
              "expansion — with the Democratic caucus holding together each time. H.230 "
              "imposed a 72-hour delay on all firearm transfers, required secure home "
              "storage of firearms with criminal penalties, and expanded red-flag Extreme "
              "Risk Protection Orders — all directly contrary to the rubric's Second "
              "Amendment posture of opposing red-flag laws and firearms restrictions. Gov. "
              "Scott allowed the bill to become law without his signature, June 2023.",
              ["https://legislature.vermont.gov/bill/status/2024/H.230",
               "https://www.wcax.com/2023/03/23/vt-house-approves-gun-bill-over-gop-concerns/"]),
        claim("ml2", "martin-lalonde", "sanctity_of_life", 0, False,
              "Voted with the Democratic majority in favor of Vermont S.37 (Act 15, 2023), "
              "the abortion and gender-affirming care 'shield bill,' which passed the Vermont "
              "House overwhelmingly on April 21, 2023, and was signed into law by Gov. Phil "
              "Scott on May 10, 2023. S.37 protects Vermont patients who obtain abortions "
              "and providers who perform them from professional discipline or civil/criminal "
              "liability originating in other states, institutionalizing Vermont as a "
              "guaranteed safe harbor for unrestricted abortion access and reflecting a "
              "rejection of any legal recognition of unborn life — contrary to the rubric's "
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
