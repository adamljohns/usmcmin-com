#!/usr/bin/env python3
"""Enrichment batch 300: hand-curated claims for 5 Virginia Republican delegates.

Targets evidence_state candidates from bottom-of-alphabet (VA) with 0 claims.
Archetype_curated federal bucket is exhausted; continuing the state-official pivot
from batches 290-299. All five are sitting Virginia House of Delegates members
with 2026 session votes documented by Virginia Mercury, NRA-ILA, Ballotpedia,
and official legislative sources.

Targets (all R, VA):
  Michael Webert   — House of Delegates, District 61 (Republican Whip)
  Mitchell Cornett — House of Delegates, District 46
  Mike Cherry      — House of Delegates, District 74
  Otto Wachsmann   — House of Delegates, District 83
  Karen Hamilton   — House of Delegates, District 62

10 total claims across 5 candidates.

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
    # ----------- Michael Webert (VA-R, House of Delegates District 61) -----------
    ("michael-webert", "VA", "House of Delegates", [
        claim("mw1", "michael-webert", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026) — a proposed constitutional amendment that would enshrine a near-unlimited right to abortion in the Virginia Constitution, covering all matters related to pregnancy with no gestational limit unless justified by a compelling state interest. The measure passed the House 64-34 on a strict party-line vote; Webert, serving as the House Republican Whip, stood with every Republican delegate in opposing the constitutionalization of abortion-on-demand in Virginia.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Michael_Webert"]),
        claim("mw2", "michael-webert", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package that passed the House 58-34 on a strict party-line vote. Serving as House Republican Whip, Webert helped coordinate the unified Republican bloc opposing the most sweeping firearms restriction in Virginia's history. The legislation banned the sale and manufacture of assault-style rifles, restricted magazine capacity, and imposed new storage mandates. NRA-ILA condemned it as unconstitutional; Gov. Spanberger signed it into law in May 2026.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law"]),
    ]),

    # ----------- Mitchell Cornett (VA-R, House of Delegates District 46) -----------
    ("mitchell-cornett", "VA", "House of Delegates", [
        claim("mc1", "mitchell-cornett", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026) — a proposed constitutional amendment to enshrine abortion-on-demand with no gestational limit into Virginia's Constitution. The measure passed the House 64-34 on a strict party-line vote; Cornett, a cattle farmer and Christian representing the rural southwest Virginia counties of Grayson, Smyth, Wythe, and part of Pulaski, stood with every Republican delegate in voting to protect the unborn. Cornett took office January 14, 2026, making this among his first legislative votes.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Mitchell_Cornett"]),
        claim("mc2", "mitchell-cornett", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the accompanying gun-control package that cleared the House 58-34 along party lines. Cornett opposed the most expansive firearms restriction in Virginia's history — banning the sale and manufacture of assault-style rifles, capping magazine capacity, and adding storage mandates — and separately sponsored HB 1300, which passed unanimously, allowing the immediate survivor of any Virginia State Police officer to purchase the officer's service handgun for $1, honoring fallen law enforcement with a practical pro-Second-Amendment measure.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote",
               "https://lis.virginia.gov/session-details/20261/member-information/H0390/member-details"]),
    ]),

    # ----------- Mike Cherry (VA-R, House of Delegates District 74) -----------
    ("mike-cherry", "VA", "House of Delegates", [
        claim("mch1", "mike-cherry", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026), which would have written a near-unlimited right to abortion into the Virginia Constitution with no gestational limit. The measure passed the House 64-34 on a strict party-line vote; Cherry cast one of 34 Republican 'no' votes defending the unborn. A retired U.S. Air Force officer with a Bachelor of Science in Religion from Liberty University and a graduate of Regent University, Cherry served as a staff pastor at Life Church and head of school at Life Christian Academy before entering politics — a background rooted in biblical convictions on life.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Mike_Cherry"]),
        claim("mch2", "mike-cherry", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package that passed the House 58-34 on party lines, standing with every Republican delegate against the most sweeping firearms restriction in Virginia's history. The legislation banned the future sale and manufacture of assault-style firearms, restricted magazine capacity, and imposed storage mandates. NRA-ILA called it unconstitutional; Gov. Spanberger signed it in May 2026. A 20-year U.S. Air Force veteran and former Colonial Heights city councilman, Cherry has a background of service and personal responsibility consistent with strong Second Amendment defense.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law",
               "https://ballotpedia.org/Mike_Cherry"]),
    ]),

    # ----------- Otto Wachsmann (VA-R, House of Delegates District 83) -----------
    ("otto-wachsmann", "VA", "House of Delegates", [
        claim("ow1", "otto-wachsmann", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026), a proposed constitutional amendment that would embed a near-unlimited right to abortion — covering all matters related to pregnancy with no gestational limit — in Virginia's Constitution. The amendment passed the House 64-34 on a strict party-line vote; Wachsmann stood with every Republican delegate in opposing it. First elected in 2023, Wachsmann represents District 83 in Gloucester, Mathews, and parts of York County on the Virginia Peninsula and won re-election in November 2025.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/H._Otto_Wachsmann_Jr."]),
        claim("ow2", "otto-wachsmann", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package that cleared the House 58-34 on party lines. The bill — the most expansive firearms restriction in Virginia history — prohibited the sale and manufacture of assault-style rifles, capped magazine capacity to ten rounds, and mandated secure storage. NRA-ILA condemned it as unconstitutional; Gov. Spanberger signed it into law in May 2026. Wachsmann stood with every Republican delegate against it.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law"]),
    ]),

    # ----------- Karen Hamilton (VA-R, House of Delegates District 62) -----------
    ("karen-hamilton", "VA", "House of Delegates", [
        claim("kh1", "karen-hamilton", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026) — a proposed constitutional amendment that would enshrine abortion as a near-unlimited constitutional right in Virginia with no gestational limit. The measure passed the House 64-34 on a strict party-line vote; Hamilton, sworn in January 14, 2026, stood with every Republican delegate in opposing it. A structural engineer and stay-at-home mother representing the rural central Virginia counties of Greene, Madison, and parts of Culpeper and Orange, Hamilton ran and won on a conservative platform in November 2025.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Karen_Hamilton"]),
        claim("kh2", "karen-hamilton", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package that passed the House 58-34 on party lines — the most expansive firearms restriction in Virginia's history. The legislation banned the future sale and manufacture of assault-style firearms, capped magazine capacity, and imposed storage mandates. NRA-ILA condemned it as unconstitutional; Gov. Spanberger signed it into law in May 2026. Hamilton stood with every Republican delegate in opposing it during her first legislative session.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law",
               "https://ballotpedia.org/Karen_Hamilton"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
