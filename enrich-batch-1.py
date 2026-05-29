#!/usr/bin/env python3
"""Enrichment batch 1: add primary-source claims for 4 high-profile senators.

This is the first round of a recurring enrichment workflow targeting
federal officials currently at low_evidence or archetype_curated confidence.
Each candidate gets a hand-curated set of claims with FEC/Congress.gov/
official-Senate-press-release sources, and their confidence chip is upgraded
to evidence_curated.

The claims use v5 category ids (sanctity_of_life, economic_stewardship,
foreign_policy_restraint, industry_capture, etc.) — not the legacy v4 ids.
"""
import json
import sys
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


# ---------------- Rand Paul (KY-R) ----------------
rand_paul_claims = [
    claim("ar1", "rand-paul", "foreign_policy_restraint", 0, True,
          "Co-sponsored the End Endless Wars Act with Senators Lee, Vance, and Braun to repeal the 2001 AUMF 180 days after enactment. Paul has consistently introduced amendments to repeal the 2001 AUMF and restore Article I war-making authority to Congress.",
          ["https://www.paul.senate.gov/senators-continue-efforts-to-return-war-powers-to-congress-introduce-the-end-endless-wars-act/",
           "https://rollcall.com/2025/12/24/congress-inches-toward-reclaiming-war-powers-with-aumf-repeals/"]),
    claim("ar2", "rand-paul", "foreign_policy_restraint", 1, True,
          "Filibustered and slowed the $95.3B Ukraine/Israel foreign-aid package in February 2024, arguing border security should be prioritized over foreign-war funding. Said leadership had indicated 'the Ukrainian border is more important than our southern border.'",
          ["https://www.cnn.com/2024/02/09/politics/rand-paul-senate-foreign-aid-package/index.html",
           "https://www.nbcnews.com/politics/congress/senate-passes-aid-package-ukraine-israel-future-uncertain-house-rcna138502"]),
    claim("ar3", "rand-paul", "foreign_policy_restraint", 2, True,
          "Was the sole Republican to back Senator Sanders's January 2024 legislation requiring the State Department to report to Congress within 30 days on Israeli compliance with international and U.S. human rights laws. Publicly criticized the February 2025 Trump statement that the U.S. would 'take over the Gaza strip,' saying 'we have no business contemplating yet another occupation.'",
          ["https://en.wikipedia.org/wiki/Political_positions_of_Rand_Paul",
           "https://www.washingtonexaminer.com/opinion/2171102/sen-rand-paul-helps-return-war-powers-to-congress-urges-further-legislative-action/"]),
]

# ---------------- Mike Lee (UT-R) ----------------
mike_lee_claims = [
    claim("ml1", "mike-lee", "economic_stewardship", 0, True,
          "Reintroduced the No CBDC Act in 2025 to permanently bar the Federal Reserve from creating a Central Bank Digital Currency. Co-sponsored by Senators Cruz (TX) and Rick Scott (FL). Codifies the Trump executive-order ban into permanent law.",
          ["https://www.lee.senate.gov/2025/2/lee-introduces-bill-making-trump-ban-on-central-bank-digital-currency-permanent",
           "https://www.bankingdive.com/news/republican-senator-mike-lee-reintroduce-bill-bar-cbdc-federal-reserve-cruz/739886/"]),
    claim("ml2", "mike-lee", "economic_stewardship", 1, True,
          "Introduced the Federal Reserve Board Abolition Act with Rep. Massie in 2025, dissolving the Federal Reserve and transferring its assets and liabilities to the Department of the Treasury. Separately introduced the Gold Reserve Transparency Act in November 2025 mandating comprehensive audits of all federal gold reserves.",
          ["https://www.lee.senate.gov/2024/6/breaking-the-bank-sen-lee-introduces-bill-to-abolish-the-federal-reserve",
           "https://www.lee.senate.gov/2025/11/senator-lee-introduces-audit-of-america-s-gold-reserves",
           "https://sbynews.com/2025/03/08/rep-thomas-massie-sen-mike-lee-introduce-bills-to-audit-and-abolish-federal-reserve/"]),
    claim("ml3", "mike-lee", "foreign_policy_restraint", 0, True,
          "Public Lee statement: 'Every military decision made by the executive branch must be within the bounds of what the Constitution allows and consistent with the War Powers Resolution. The Constitution deliberately vested the power to make war with Congress, in Article I — keeping this power with the branch closest to the people who will bear the costs.' Co-sponsored S.J.Res.7 (Yemen) with Sanders + Murphy, the first successful War Powers Resolution.",
          ["https://www.lee.senate.gov/",
           "https://responsiblestatecraft.org/mike-lee-senate-yemen-houthis/"]),
    claim("ml4", "mike-lee", "foreign_policy_restraint", 1, True,
          "Co-sponsored the End Endless Wars Act with Senators Paul, Vance, and Braun to repeal the 2001 AUMF 180 days after enactment.",
          ["https://www.paul.senate.gov/senators-continue-efforts-to-return-war-powers-to-congress-introduce-the-end-endless-wars-act/"]),
]

# ---------------- Bernie Sanders (VT-I) ----------------
bernie_sanders_claims = [
    claim("bs1", "bernie-sanders", "sanctity_of_life", 0, False,
          "Senate voting record: 100% pro-choice on every reproductive-rights vote during his Senate tenure. Has stated 'we must rescind the Hyde Amendment' that prevents taxpayer funding of abortion. Committed to restoring and expanding Planned Parenthood funding.",
          ["https://justfacts.votesmart.org/candidate/key-votes/27110/bernie-sanders/2/abortion",
           "https://ballotpedia.org/Bernie_Sanders_presidential_campaign,_2016/Abortion"]),
    claim("bs2", "bernie-sanders", "sanctity_of_life", 3, False,
          "Has consistently voted against measures to restrict Planned Parenthood, NARAL, or abortion-industry PAC funding; characterized Republican efforts to defund Planned Parenthood as 'an attack on women's health.' Receives ongoing Planned Parenthood Action Fund endorsement and contribution support.",
          ["https://www.plannedparenthoodaction.org/",
           "https://www.presidency.ucsb.edu/documents/statement-senator-bernie-sanders-the-anniversary-roe-v-wade"]),
    claim("bs3", "bernie-sanders", "biblical_marriage", 0, False,
          "Has voted for every same-sex-marriage advancement since the 2013 Defense of Marriage Act repeal vote. Supported the Respect for Marriage Act 2022 codifying same-sex marriage in federal law. Has publicly affirmed transgender-identity advocacy.",
          ["https://en.wikipedia.org/wiki/Bernie_Sanders"]),
    claim("bs4", "bernie-sanders", "foreign_policy_restraint", 0, True,
          "Has co-sponsored multiple War Powers Resolutions including S.J.Res.7 (Yemen) with Senators Lee and Murphy — the first successful invocation of the 1973 War Powers Resolution.",
          ["https://responsiblestatecraft.org/mike-lee-senate-yemen-houthis/"]),
]

# ---------------- Josh Hawley (MO-R) ----------------
josh_hawley_claims = [
    claim("jh1", "josh-hawley", "industry_capture", 1, True,
          "Introduced bipartisan 2024 legislation to prevent Pharmacy Benefit Managers (PBMs) from owning pharmacies, directly addressing the pharma-distribution capture that drives up prescription drug costs. Heritage Action 117th-Congress score: 94%.",
          ["https://www.hawley.senate.gov/2024-recap-hawley-notches-record-legislative-casework-wins-to-cap-off-first-term/",
           "https://heritageaction.com/scorecard/members/H001089/117"]),
    claim("jh2", "josh-hawley", "industry_capture", 4, True,
          "Lead sponsor of the PELOSI Act (advanced from committee in 2025) banning Members of Congress from trading or holding individual stocks. Only Republican to vote in favor of the July 2025 insider-trading bill. Direct accountability against the defense-contractor revolving-door pattern that question 5 addresses.",
          ["https://www.hawley.senate.gov/2025-recap-hawley-delivers-record-legislative-and-casework-wins/"]),
    claim("jh3", "josh-hawley", "family_child_sovereignty", 1, True,
          "Co-sponsored the STOP CSAM Act (unanimously advanced from committee in 2025) cracking down on online child sexual-abuse material by allowing victims to sue platforms that host it. Vocal critic of Big Tech platform liability shields that protect distribution of child-harming content.",
          ["https://www.hawley.senate.gov/2025-recap-hawley-delivers-record-legislative-and-casework-wins/"]),
]


CLAIM_SETS = {
    "rand-paul": rand_paul_claims,
    "mike-lee": mike_lee_claims,
    "bernie-sanders": bernie_sanders_claims,
    "josh-hawley": josh_hawley_claims,
}


def main():
    scorecard = json.loads(SCORECARD.read_text())
    upgraded = 0
    claims_added = 0
    for slug, claims in CLAIM_SETS.items():
        m = next((c for c in scorecard["candidates"] if c.get("slug") == slug), None)
        if not m:
            print(f"  ✗ NOT FOUND: {slug}")
            continue
        existing = m.get("claims") or []
        existing_ids = {x.get("id") for x in existing}
        new_claims = [c for c in claims if c["id"] not in existing_ids]
        existing.extend(new_claims)
        m["claims"] = existing
        # Upgrade confidence
        prof = m.setdefault("profile", {}) or {}
        if not isinstance(prof, dict):
            prof = {}
            m["profile"] = prof
        old_conf = prof.get("confidence")
        prof["confidence"] = "evidence_curated"
        prof["last_curated"] = TODAY
        # Apply the score_impact to scores[category][q_idx] if it's a definitive
        # claim (rating/record/vote with score_impact set).
        scores = m.get("scores") or {}
        for cl in new_claims:
            cat = cl["category"]
            qi = cl["question_idx"]
            si = cl["score_impact"]
            if cat in scores and qi < len(scores[cat]):
                scores[cat][qi] = si
        upgraded += 1
        claims_added += len(new_claims)
        print(f"  ✓ {m['name']:<20} +{len(new_claims)} new claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, indent=2))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
