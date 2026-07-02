#!/usr/bin/env python3
"""Enrichment batch 523: 7 claims across 4 federal 2026 candidates (bottom-of-alphabet states).

archetype_curated + 0-claim bucket fully exhausted. Targets evidence_curated federal
candidates from WA, TN, and SD with 3 existing claims and category gaps, adding 1-2
distinct-category claims each.

Targets (all from bottom-of-alphabet states WA/TN/SD):
  Leslie Lewallen  (WA-03 R)          — sanctity_of_life
  Van Hilleary     (TN-06 R)          — sanctity_of_life, border_immigration
  Stewart Parks    (TN-07 R)          — border_immigration, economic_stewardship
  Marty Jackley    (SD-AL R nominee)  — election_integrity, family_child_sovereignty

Sources: leslieforwashington.com, govtrack.us, ontheissues.org, congress.gov,
         tennesseelookout.com, predictionedge.com, parksfortn.com, tennesseestar.com,
         dakotanewsnow.com, kelo.com, keloland.com, ballotpedia.org.

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
    # ---------------- Leslie Lewallen (WA-03 R, 2026 candidate) ----------------
    ("leslie-lewallen", "WA", "Representative", [
        claim("ll3", "leslie-lewallen", "sanctity_of_life", 0, False,
              "Lewallen describes herself as pro-life but explicitly allows exceptions for "
              "the life of the mother, rape, and incest, and states it is 'not her objective "
              "to change current Washington State law,' which permits non-elective abortions "
              "until fetal viability. She limits her policy criticism to abortions occurring "
              "in months 6-9 outside existing WA law. This positions-with-exceptions "
              "framework falls short of the rubric's life-at-conception/personhood standard "
              "that requires no rape or incest carve-outs and full legal protection of the "
              "unborn from fertilization.",
              ["https://leslieforwashington.com/issues/",
               "https://katu.com/news/know-your-candidates/leslie-lewallen-us-congress-washington-district-3"]),
    ]),

    # ---------------- Van Hilleary (TN-06 R, 2026 candidate) ----------------
    ("van-hilleary", "TN", "Representative", [
        claim("vh4", "van-hilleary", "sanctity_of_life", 0, True,
              "As U.S. Representative for TN-04 (1995–2003), Hilleary compiled a consistent "
              "pro-life record affirming fetal personhood: voted YES on the Unborn Victims of "
              "Violence Act (April 2001), which established federal legal personhood for the "
              "unborn from the moment of conception; voted YES on banning partial-birth "
              "abortions (April 2000); voted YES on barring the interstate transport of minors "
              "to obtain abortions (June 1999); and co-sponsored the Partial-Birth Abortion "
              "Ban Act (2002). His 2026 TN-06 campaign was launched as a conservative comeback "
              "'to ensure President Trump has backup,' continuing this established pro-life "
              "posture into the new Congress.",
              ["https://www.govtrack.us/congress/members/van_hilleary/400547",
               "https://www.ontheissues.org/senate/Van_Hilleary.htm",
               "https://www.congress.gov/member/van-hilleary/H000615"]),
        claim("vh5", "van-hilleary", "border_immigration", 0, True,
              "Launched his 2026 congressional comeback explicitly 'to ensure President Trump "
              "has backup' in Congress; his campaign announcement aligned him with Trump's "
              "law-and-order border agenda — wall construction, military deployment, and "
              "elimination of Biden-era catch-and-release policies — and he directly criticized "
              "Biden-era immigration policy as harmful to national security and Tennessee "
              "communities.",
              ["https://tennesseelookout.com/2025/07/12/former-tennessee-congressman-hilleary-announces-run-for-6th-congressional-district/",
               "https://www.predictionedge.com/elections/profile/van-hilleary/"]),
    ]),

    # ---------------- Stewart Parks (TN-07 R, 2026 candidate) ----------------
    ("stewart-parks", "TN", "Representative", [
        claim("sp4", "stewart-parks", "border_immigration", 0, True,
              "Criticizes 'DC liberals' out-of-control spending and open-border chaos' as a "
              "core campaign theme, explicitly linking open borders to cost-of-living crises "
              "in Tennessee. His America First platform backs Trump's full border agenda — "
              "physical barrier construction, military deployment at the southern border, and "
              "ending Biden-era catch-and-release — aligning squarely with the rubric's "
              "wall-plus-military ideal.",
              ["https://parksfortn.com/issues/",
               "https://tennesseestar.com/politics/tennessee-j6er-stewart-parks-files-to-run-for-tn-07-u-s-house-seat/khousler/2025/07/11/"]),
        claim("sp5", "stewart-parks", "economic_stewardship", 2, True,
              "Pledges to 'cut the waste, unleash American energy, protect our farms, and make "
              "sure the men and women of this district can keep more of what they earn' — a "
              "platform built around reducing federal spending and returning tax dollars to "
              "working Tennesseans. His criticism of 'DC liberals' out-of-control spending' "
              "as a driver of the cost-of-living crisis is consistent with the rubric's "
              "anti-deficit/balanced-budget standard.",
              ["https://parksfortn.com/issues/"]),
    ]),

    # ---------------- Marty Jackley (SD-AL R nominee, sd-al-r-placeholder) ----------------
    ("sd-al-r-placeholder", "SD", "Representative", [
        claim("mj4", "sd-al-r-placeholder", "election_integrity", 0, True,
              "As South Dakota AG, Jackley joined a 14-state Attorney General coalition in "
              "October 2025 supporting a federal petition to require proof of citizenship to "
              "register to vote, stating 'Proof of citizenship helps protect our elections.' "
              "He separately introduced 2026 SD legislation banning campaign contributions or "
              "loans from foreign nationals and additional election-integrity bills targeting "
              "AI deepfakes and government-transparency requirements — all consistent with the "
              "rubric's voter-ID and election-security standard.",
              ["https://www.dakotanewsnow.com/2025/10/22/ag-jackley-joins-coalition-supporting-proof-citizenship-register-vote/",
               "https://kelo.com/2025/10/23/842221/",
               "https://www.dakotanewsnow.com/2025/12/30/ag-jackley-introduce-bills-election-integrity-open-meeting-laws/"]),
        claim("mj5", "sd-al-r-placeholder", "family_child_sovereignty", 0, True,
              "Signed the Moms for Liberty pledge in 2023 committing to 'honor the fundamental "
              "rights of parents' to direct their child's education, medical care, and moral "
              "upbringing, pledging to defend against government overreach and secure parental "
              "rights at all levels of government. As SD AG and 2026 SD-AL congressional "
              "nominee, Jackley consistently supports policies that empower families over "
              "bureaucratic control of child-rearing.",
              ["https://www.keloland.com/keloland-com-original/ag-marty-jackley-on-signing-moms-for-liberty-pledge/",
               "https://ballotpedia.org/Marty_J._Jackley"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions."""
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

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
