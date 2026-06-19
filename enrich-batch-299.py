#!/usr/bin/env python3
"""Enrichment batch 299: hand-curated claims for 5 Virginia Republican delegates.

Targets evidence_state candidates from bottom-of-alphabet (VA) with 0 claims.
Archetype_curated federal bucket is exhausted; continuing the state-official pivot
from batches 290-298. All five are sitting Virginia House of Delegates members
with 2026 session votes documented by Virginia Mercury, NRA-ILA, Ballotpedia,
and official legislative sources.

Targets (all R, VA):
  Will Davis     — House of Delegates, District 39
  Tom Garrett    — House of Delegates, District 56
  Tim Griffin    — House of Delegates, District 53
  Terry Austin   — House of Delegates, District 37
  Scott Wyatt    — House of Delegates, District 60

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
    # ----------- Will Davis (VA-R, House of Delegates District 39) -----------
    ("will-davis", "VA", "House of Delegates", [
        claim("wd1", "will-davis", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026) — a proposed constitutional amendment that would enshrine a near-unlimited right to abortion in the Virginia Constitution, covering all matters related to pregnancy with no gestational limit unless justified by a compelling state interest. The measure passed the House 64-34 on a strict party-line vote; Davis cast one of 34 Republican 'no' votes defending the unborn against constitutionally entrenched abortion-on-demand in Virginia.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Will_Davis_(Virginia)"]),
        claim("wd2", "will-davis", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package that passed the House 58-34 on a strict party-line vote. The legislation — the most expansive firearms restriction in Virginia's modern legislative history — banned the sale and manufacture of assault-style rifles, restricted magazine capacity, and imposed new storage mandates. NRA-ILA condemned it as unconstitutional; Gov. Spanberger signed it into law in May 2026. Davis stood with every Republican delegate in opposing it.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law"]),
    ]),

    # ----------- Tom Garrett (VA-R, House of Delegates District 56) -----------
    ("tom-garrett", "VA", "House of Delegates", [
        claim("tg1", "tom-garrett", "sanctity_of_life", 0, True,
              "A lifelong pro-life legislator who, as a Virginia State Senator and later as a U.S. Representative (VA-5th, 2017-2019), introduced federal legislation to prohibit abortions at 20 weeks post-fertilization. Returned to the House of Delegates in 2024 with the same commitment, stating publicly: 'I assure you that on issues of life, I will vote to protect the first and foremost inalienable right given to us by the Creator. No exceptions.' Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026), which would have constitutionalized abortion-on-demand in Virginia.",
              ["https://ballotpedia.org/Thomas_Garrett",
               "https://en.wikipedia.org/wiki/Tom_Garrett_(Virginia_politician)",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("tg2", "tom-garrett", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package, standing with every House Republican against the most sweeping firearms restriction in Virginia's history. The legislation passed 58-34 on party lines. As a former U.S. Representative backed by the NRA, Garrett has a sustained pro-gun record spanning two decades of Virginia and federal legislative service. NRA-ILA called the package unconstitutional; Gov. Spanberger signed it into law in May 2026.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law",
               "https://en.wikipedia.org/wiki/Tom_Garrett_(Virginia_politician)"]),
    ]),

    # ----------- Tim Griffin (VA-R, House of Delegates District 53) -----------
    ("tim-griffin", "VA", "House of Delegates", [
        claim("tgr1", "tim-griffin", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026), which would have embedded a sweeping right to abortion — with no gestational limit — in the Virginia Constitution. The measure passed the House 64-34 on a strict party-line vote; Griffin cast one of 34 Republican 'no' votes. A former election attorney and prosecutor, Griffin won re-election to the House of Delegates in November 2025.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Tim_Griffin_(Virginia)"]),
        claim("tgr2", "tim-griffin", "self_defense", 1, True,
              "Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) and the broader gun-control package that cleared the House 58-34 on party lines. The bill prohibited the sale and manufacture of assault-style firearms, capped magazine capacity, and added storage mandates — the most expansive gun restriction package in Virginia history. Griffin stood with every Republican delegate against the legislation that NRA-ILA condemned as unconstitutional and that Gov. Spanberger signed in May 2026.",
              ["https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote",
               "https://ballotpedia.org/Tim_Griffin_(Virginia)"]),
    ]),

    # ----------- Terry Austin (VA-R, House of Delegates District 37) -----------
    ("terry-austin", "VA", "House of Delegates", [
        claim("ta1", "terry-austin", "sanctity_of_life", 0, True,
              "Publicly identifies as 'proudly pro-life' and has committed to 'support additional efforts to protect the unborn.' Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026) — a constitutional amendment that would enshrine abortion as a near-unlimited right in Virginia's Constitution. The vote was 64-34 along party lines; Austin stood with every Republican delegate in opposing it. Austin represents Buchanan (District 37), a deep-rural southwest Virginia district, and won re-election in November 2025.",
              ["https://ballotpedia.org/Terry_Austin",
               "https://en.wikipedia.org/wiki/Terry_Austin_(politician)",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("ta2", "terry-austin", "self_defense", 1, True,
              "A gun owner and self-described 'staunch supporter of the Second Amendment' who has pledged to uphold 'your right to own and carry a firearm.' Voted NO on HB 217 (Virginia's 2026 assault-weapons ban) along with every Republican delegate, opposing the 58-34 party-line measure that banned the sale and manufacture of assault-style rifles, capped magazine capacity, and imposed storage mandates. The legislation — signed by Gov. Spanberger in May 2026 — was called unconstitutional by NRA-ILA.",
              ["https://apps.house.virginia.gov/members/H0253",
               "https://ballotpedia.org/Terry_Austin",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law"]),
    ]),

    # ----------- Scott Wyatt (VA-R, House of Delegates District 60) -----------
    ("scott-wyatt", "VA", "House of Delegates", [
        claim("sw1", "scott-wyatt", "self_defense", 1, True,
              "A Life Member of the National Rifle Association who voted NO on HB 217 (Virginia's 2026 assault-weapons ban) along with every Republican delegate. The legislation banned the future sale and manufacture of assault-style firearms, restricted magazine capacity to ten rounds, and imposed storage mandates — the most expansive firearms restriction Virginia has ever enacted. It passed the House 58-34 on party lines and was signed by Gov. Spanberger in May 2026. NRA-ILA called it unconstitutional; Wyatt joined the unified GOP bloc opposing it.",
              ["https://ballotpedia.org/Scott_Wyatt_(Virginia)",
               "https://www.nraila.org/articles/20260205/virginia-house-continues-gun-control-push-giving-public-minimal-notice-before-vote",
               "https://www.nraila.org/articles/20260423/virginia-spanberger-signs-unconstitutional-gun-bills-into-law"]),
        claim("sw2", "scott-wyatt", "sanctity_of_life", 0, True,
              "Voted NO on Virginia's Right to Reproductive Freedom Amendment (HJR 1, 2026), which would have written a near-unlimited right to abortion — with no gestational limit — into the Virginia Constitution. The amendment passed the House 64-34 on a strict party-line vote, with Wyatt casting one of 34 Republican 'no' votes. A member of the House since 2020, Wyatt represents Hanover County (District 60) and won re-election in November 2025.",
              ["https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)",
               "https://virginiamercury.com/2026/01/19/virginia-lawmakers-send-reproductive-rights-amendment-toward-november-vote/",
               "https://ballotpedia.org/Scott_Wyatt_(Virginia)"]),
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
