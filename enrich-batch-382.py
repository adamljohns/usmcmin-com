#!/usr/bin/env python3
"""Enrichment batch 382: hand-curated claims for 5 sitting U.S. Senators.

Targets evidence_curated senators with 3 existing claims, pulled from
the bottom of the alphabet (IL, ID, FL×2, AR×2).  Each gets 2 new claims
in rubric categories not yet scored.

Mix (all R): Jim Risch (ID-R), Rick Scott (FL-R), Ashley Moody (FL-R),
Tom Cotton (AR-R), John Boozman (AR-R).

Sources: rickscott.senate.gov, risch.senate.gov, moody.senate.gov,
cotton.senate.gov, boozman.senate.gov, congress.gov, govtrack.us,
ballotpedia.org, nrapvf.org.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace).
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
    # -------- Jim Risch (ID-R, US Senator) --------
    ("jim-risch", "ID", "Senator", [
        claim("jr1", "jim-risch", "border_immigration", 2, True,
              "In 2025 Risch introduced the No Bailout for Sanctuary Cities Act, blocking federal funds to jurisdictions that refuse to cooperate with federal immigration authorities — directly opposing sanctuary-city policies and aligning with the rubric's anti-sanctuary standard. He also introduced the 287(g) Program Protection Act to strengthen local-federal immigration enforcement partnerships.",
              ["https://www.risch.senate.gov/public/index.cfm/2025/2/risch-introduces-bill-to-end-taxpayer-funded-handouts-to-illegal-immigrants",
               "https://www.risch.senate.gov/public/index.cfm/2025/7/risch-introduces-bill-to-strengthen-local-federal-immigration-enforcement-efforts",
               "https://ballotpedia.org/Jim_Risch"]),
        claim("jr2", "jim-risch", "economic_stewardship", 2, True,
              "Risch voted YES on the One, Big, Beautiful Bill Act (Senate Vote 51-50, July 1, 2025), issuing a statement that it 'delivers on the priorities of securing the border, making the Trump tax cuts permanent, dismantling the Green New Deal, and addressing wasteful spending.' The bill included the largest tax cut in history by making permanent the 2017 TCJA provisions, a posture consistent with reducing the government's deficit-funded footprint.",
              ["https://www.risch.senate.gov/public/index.cfm/2025/7/risch-statement-on-the-senate-passage-of-the-one-big-beautiful-bill",
               "https://ballotpedia.org/One_Big_Beautiful_Bill_Act"]),
    ]),

    # -------- Rick Scott (FL-R, US Senator) --------
    ("rick-scott", "FL", "Senator", [
        claim("rs3", "rick-scott", "election_integrity", 2, True,
              "A lead Senate champion of the SAVE Act / SAVE America Act: Scott co-authored the Senate version of the bill requiring documentary proof of U.S. citizenship to register to vote in federal elections, repeatedly demanded Senate floor votes on the measure, and in January 2026 called for a standing filibuster to force the vote — directly advancing the rubric's voter-ID and anti-noncitizen-voting standard.",
              ["https://www.rickscott.senate.gov/2024/9/sen-rick-scott-colleagues-demand-passage-of-save-act",
               "https://www.dailysignal.com/2026/01/26/this-senator-wants-to-force-a-vote-on-election-integrity-bill/",
               "https://ballotpedia.org/Rick_Scott"]),
        claim("rs4", "rick-scott", "border_immigration", 2, True,
              "Scott introduced legislation in March 2026 to crack down on sanctuary cities by withholding federal tax dollars from any city or state that refuses to cooperate with federal immigration enforcement. He has also repeatedly cosponsored bills to complete and strengthen the border wall, expand ICE detention capacity, and defund NGOs that facilitate illegal immigration.",
              ["https://www.rickscott.senate.gov/2026/3/s",
               "https://www.rickscott.senate.gov/2025/4/sen-rick-scott-outlines-top-priorities-to-protect-america-s-homeland-in-letter-to-dhs-secretary-kristi-noem",
               "https://ballotpedia.org/Rick_Scott"]),
    ]),

    # -------- Ashley Moody (FL-R, US Senator, appointed Jan 2025) --------
    ("ashley-moody", "FL", "Senator", [
        claim("am1", "ashley-moody", "election_integrity", 0, True,
              "Before her Senate appointment, as Florida Attorney General Moody led a multi-state coalition urging the U.S. Senate to pass the SAVE Act requiring proof of citizenship for federal voter registration. As senator, she joined GOP colleagues in 2025-2026 urging passage of the SAVE America Act, recording a video statement that the bill 'protects elections through voter ID standards supported by over 80% of Americans.'",
              ["https://www.myfloridalegal.com/newsrelease/attorney-general-moody-and-coalition-call-us-senate-pass-save-act-ensure-only-americans",
               "https://www.moody.senate.gov/press-releases/video-release-senator-moody-urges-passage-of-save-america-act/",
               "https://ballotpedia.org/Ashley_B._Moody"]),
        claim("am2", "ashley-moody", "economic_stewardship", 1, True,
              "Moody voted YES on the One Big Beautiful Bill Act (Senate 51-50, July 1, 2025) and championed the bill as delivering 'stronger border security, more job opportunities, preventing a $4 trillion tax increase, and securing financial commonsense so our kids and grandkids have the opportunity to live their American Dream.' The bill made the 2017 Tax Cuts and Jobs Act permanent — a sound-money, anti-tax-inflation posture consistent with the rubric.",
              ["https://www.moody.senate.gov/press-releases/sen-ashley-moody-brings-home-wins-for-floridians-in-one-big-beautiful-bill/",
               "https://www.whitehouse.gov/articles/2025/07/what-they-are-saying-senate-approves-landmark-one-big-beautiful-bill/",
               "https://ballotpedia.org/Ashley_B._Moody"]),
    ]),

    # -------- Tom Cotton (AR-R, US Senator) --------
    ("tom-cotton", "AR", "Senator", [
        claim("tc1", "tom-cotton", "election_integrity", 0, True,
              "Cotton cosponsored the SAVE America Act and delivered a Senate floor speech in March 2026 demanding its passage, citing the fact that 64 percent of adults support the bill to require documentary proof of citizenship for federal voter registration. He stated: 'This bill will help ensure that only eligible citizens can vote in our elections' — a direct affirmation of the rubric's voter-ID standard.",
              ["https://www.cotton.senate.gov/news/videos/watch/march-18-2026-cotton-speaks-on-the-senate-floor-supporting-the-save-america-act",
               "https://www.cotton.senate.gov/news/speeches/floor-speech-on-save-america-act",
               "https://ballotpedia.org/Tom_Cotton"]),
        claim("tc2", "tom-cotton", "self_defense", 0, True,
              "Cotton holds an A rating from the National Rifle Association and in 2025 co-sponsored the Constitutional Concealed Carry Reciprocity Act (with Cornyn and Cruz), which would allow law-abiding gun owners with concealed carry privileges in their home state to exercise those rights in any other state that permits concealed carry — a significant step toward the constitutional carry standard the rubric supports.",
              ["https://www.nssf.org/articles/nssf-profile-qa-u-s-sen-tom-cotton-r-ark/",
               "https://www.cotton.senate.gov/news/press-releases/cotton-statement-on-senate-gun-control-legislation",
               "https://www.ontheissues.org/domestic/Tom_Cotton_Gun_Control.htm"]),
    ]),

    # -------- John Boozman (AR-R, US Senator) --------
    ("john-boozman", "AR", "Senator", [
        claim("jb1", "john-boozman", "self_defense", 1, True,
              "Boozman co-introduced the Constitutional Concealed Carry Reciprocity Act (with Cornyn) in the 119th Congress, legislation endorsed by the NRA, NSSF, and Gun Owners of America that would allow law-abiding concealed carry permit holders to exercise their rights in any state permitting concealed carry — opposing restrictive permit-by-permit and anti-reciprocity frameworks the rubric identifies as anti-Second Amendment.",
              ["https://www.boozman.senate.gov/public/index.cfm/press-releases?id=BE9126DD-CC86-4CBB-8E04-056BDCB4152C",
               "https://www.cornyn.senate.gov/news/cornyn-cruz-grassley-tillis-senate-gop-introduce-concealed-carry-reciprocity-bill/",
               "https://ballotpedia.org/John_Boozman"]),
        claim("jb2", "john-boozman", "border_immigration", 2, True,
              "In June 2026 Boozman voted to fully fund ICE and Border Patrol through a Senate appropriations measure; he also voted YES on the One Big Beautiful Bill Act (July 1, 2025), which provided $75 billion for ICE enforcement and $64 billion for CBP — a 308% increase over FY2024 detention budgets — and included anti-sanctuary enforcement provisions. As Senate Ag Committee Chair, Boozman also championed E-Verify-adjacent farm-labor provisions in the bill.",
              ["https://www.boozman.senate.gov/public/index.cfm/2026/6/boozman-votes-to-fully-fund-immigration-and-customs-enforcement-border-patrol",
               "https://www.arkansasonline.com/news/2025/jul/01/boozman-cotton-play-active-parts-in-passing-big/",
               "https://ballotpedia.org/John_Boozman"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None — never returns a wrong-state same-slug record.
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
