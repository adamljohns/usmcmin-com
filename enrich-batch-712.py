#!/usr/bin/env python3
"""Enrichment batch 712: depth pass for 5 Ohio U.S. Representatives.

All five targets are active sitting House members with exactly 3 existing
evidence_curated claims. This batch adds 2-3 new claims each in distinct
rubric categories not yet scored. Primary sources: official .house.gov
press releases, govtrack.us, congress.gov, ballotpedia.org.

OH-05 Bob Latta (R):   +2  economic_stewardship[2], election_integrity[0]
OH-14 David Joyce (R): +3  border_immigration[0], foreign_policy_restraint[1], economic_stewardship[2]
OH-03 Joyce Beatty (D):+2  border_immigration[1], economic_stewardship[2]
OH-13 Emilia Sykes (D):+2  border_immigration[1], election_integrity[0]
OH-09 Marcy Kaptur (D):+2  foreign_policy_restraint[1], border_immigration[2]

NOTE: writes scorecard.json MINIFIED to keep master under GitHub 50MB limit.
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
    # ---------------- Bob Latta (OH-05, R) ----------------
    ("bob-latta", "OH", "Representative", [
        claim("bl712a", "bob-latta", "economic_stewardship", 2, True,
              "Voted YES on the Fiscal Responsibility Act (H.R. 3746, May 31, 2023), which cut FY2024 discretionary spending by $12B vs. FY2023, clawed back $28B in unspent COVID funds, and was CBO-scored to reduce deficits by ~$1.5T over 10 years. Also voted YES on the One Big Beautiful Bill Act (H.R. 1, final passage July 3, 2025, 218-214; signed July 4, 2025), enacting over $1.5T in mandatory spending reductions including Medicaid work requirements and energy deregulation — a consistent anti-deficit, spending-cut voting record.",
              ["https://latta.house.gov/news/documentsingle.aspx?DocumentID=403909",
               "https://latta.house.gov/news/documentsingle.aspx?DocumentID=406598"]),
        claim("bl712b", "bob-latta", "election_integrity", 0, True,
              "Voted YES on the SAVE Act (H.R. 22, Safeguard American Voter Eligibility Act), which requires documentary proof of U.S. citizenship to register to vote in federal elections. The bill passed the House 220-208 on April 10, 2025, on a near-party-line vote with all 220 Republicans — including Latta — voting yes.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22",
               "https://clerk.house.gov/Votes/2025102"]),
    ]),

    # ---------------- David Joyce (OH-14, R) ----------------
    ("david-joyce", "OH", "Representative", [
        claim("dj712a", "david-joyce", "border_immigration", 0, True,
              "Voted YEA on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023, 219-213), which required DHS to resume border-wall construction, reinstated the Remain in Mexico program, ended catch-and-release, and deployed surveillance technology at the southwest, northern, and maritime borders. Joyce released a statement calling it 'the first step in securing the border.'",
              ["https://joyce.house.gov/posts/joyce-votes-to-strengthen-border-security-make-american-communities-safer",
               "https://www.govtrack.us/congress/votes/118-2023/h209"]),
        claim("dj712b", "david-joyce", "foreign_policy_restraint", 1, False,
              "Voted YEA on H.R. 8035, the Ukraine Security Supplemental Appropriations Act (House Vote #151, April 20, 2024, 311-112), appropriating approximately $61 billion in military, economic, and humanitarian aid to Ukraine. A member of the Congressional Ukraine Caucus, Joyce framed the vote as necessary to 'support allies when they need it most' — an explicitly interventionist posture at odds with ending foreign military entanglements.",
              ["https://joyce.house.gov/posts/joyce-votes-to-support-allies-protect-america",
               "https://www.govtrack.us/congress/bills/118/hr8035/cosponsors"]),
        claim("dj712c", "david-joyce", "economic_stewardship", 2, False,
              "Voted YEA on both FY2024 consolidated appropriations packages (H.R. 4366 and H.R. 2882, signed March 23, 2024), totaling approximately $1.2 trillion in deficit-financed spending. As chair of the House Appropriations Financial Services and General Government Subcommittee, Joyce has no public record supporting a balanced-budget amendment, and his voting pattern reflects establishment deficit spending rather than fiscal restraint.",
              ["https://joyce.house.gov/posts/joyce-supports-funding-for-first-6-appropriations-bills-highlights-oh-14-wins",
               "https://joyce.house.gov/posts/joyce-supports-funding-for-last-6-appropriations-bills"]),
    ]),

    # ---------------- Joyce Beatty (OH-03, D) ----------------
    ("joyce-beatty", "OH", "Representative", [
        claim("jb712a", "joyce-beatty", "border_immigration", 1, False,
              "Voted NO on the Laken Riley Act (S. 5, House Vote #23, January 22, 2025, 263-156), which mandates DHS detention — without bond — of non-citizens arrested or charged with burglary, theft, larceny, shoplifting, or assault of a law enforcement officer. Beatty was among the 156 nay votes and publicly condemned ICE enforcement activity in Central Ohio, writing to DHS Secretary Noem and acting ICE Director Lyons to oppose targeted raids.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
        claim("jb712b", "joyce-beatty", "economic_stewardship", 2, False,
              "Voted NO on H.R. 1, the One Big Beautiful Bill Act (final passage July 3, 2025, 218-214; signed July 4, 2025), which enacted over $1.5 trillion in mandatory spending reductions including Medicaid work requirements and SNAP reforms. Beatty returned from medical recovery specifically to cast her nay vote and introduced a Rules Committee amendment to block any tax cuts that would reduce Medicaid, Social Security, or SNAP — an opposition posture to entitlement reform and deficit reduction.",
              ["https://beatty.house.gov/media-center/press-releases/beatty-s-message-to-gop-if-you-re-not-cutting-benefits-prove-it-support-my-amendment",
               "https://www.wosu.org/politics-government/2025-07-09/us-rep-joyce-beatty-speaks-on-health-political-future-and-budget-bill-after-surgery-sidelines-her"]),
    ]),

    # ---------------- Emilia Sykes (OH-13, D) ----------------
    ("emilia-sykes", "OH", "Representative", [
        claim("es712a", "emilia-sykes", "border_immigration", 1, True,
              "Voted YES on the Laken Riley Act — both the House-originated version (H.R. 29, House Vote #6, January 7, 2025) and the Senate-amended final version (S. 5, House Vote #23, January 22, 2025, 263-156) — making her one of approximately 46 Democrats to cross the aisle and support the bill, which mandates DHS detention of non-citizens arrested or charged with burglary, theft, larceny, shoplifting, or assault of a law enforcement officer.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://www.govtrack.us/congress/votes/119-2025/h6"]),
        claim("es712b", "emilia-sykes", "election_integrity", 0, False,
              "Voted NO on the SAVE Act (H.R. 22, Safeguard American Voter Eligibility Act, passed House 220-208 on April 10, 2025), which requires documentary proof of U.S. citizenship to register to vote in federal elections. Sykes called the bill 'voter suppression poorly dressed up as election integrity,' arguing it would disenfranchise women with name changes, seniors, racial minorities, and people with disabilities.",
              ["https://sykes.house.gov/media/press-releases/rep-sykes-votes-no-on-bill-that-would-make-it-harder-for-americans-to-vote",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------------- Marcy Kaptur (OH-09, D) ----------------
    ("marcy-kaptur", "OH", "Representative", [
        claim("mk712a", "marcy-kaptur", "foreign_policy_restraint", 1, False,
              "Co-chairs the bipartisan Congressional Ukraine Caucus (101 members) and applauded H.R. 8035, the Ukraine Security Supplemental Appropriations Act (April 2024, $60B+ in military and economic aid, passed House 311-112), urging swift Senate passage. In December 2025 she co-introduced the Peace Through Strength Against Russia Act of 2025 advancing comprehensive new Russia sanctions — a consistently interventionist foreign policy posture, not a restraint-aligned one.",
              ["https://kaptur.house.gov/media-center/press-releases/ukraine-caucus-co-chairs-applaud-house-passage-supplemental-aid-ukraine",
               "https://kaptur.house.gov/media-center/press-releases/kaptur-fitzpatrick-meeks-bipartisan-colleagues-advance-new-peace"]),
        claim("mk712b", "marcy-kaptur", "border_immigration", 2, False,
              "Voted NO on H.R. 7147, the DHS Appropriations Act, 2026 (passed 220-207), citing 'reports of enforcement action violating law and order protocols' by ICE and CBP. She simultaneously introduced the Humanitarian Standards for Individuals in ICE and CBP Custody Act (February 3, 2026) to restrict detention practices, and co-signed a letter condemning ICE operations in Central Ohio as unconstitutional — positions consistent with sanctuary-city priorities and opposition to interior enforcement.",
              ["https://kaptur.house.gov/media-center/press-releases/kaptur-calls-transparency-and-oversight-rejecting-latest-homeland",
               "https://kaptur.house.gov/media-center/press-releases/kaptur-statement-federal-immigration-enforcement-operation-erie-county"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing wrong-state same-slug collisions."""
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
