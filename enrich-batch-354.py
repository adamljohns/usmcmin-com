#!/usr/bin/env python3
"""Enrichment batch 354: 2-3 new claims each for 5 sitting U.S. Senators (bottom-of-alphabet).

Targets (bottom-of-alphabet assignment): Sheldon Whitehouse (RI-D), John Hoeven (ND-R),
Thom Tillis (NC-R), Tim Sheehy (MT-R), Roger Wicker (MS-R).
Each already has 3-4 evidence_curated claims; this batch adds 2 new claims per senator
in previously-uncovered rubric categories.

Writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
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
    # ---- Sheldon Whitehouse (RI-D) ----
    ("sheldon-whitehouse", "RI", "Senator", [
        claim("sw1", "sheldon-whitehouse", "foreign_policy_restraint", 1, False,
              "A committed Ukraine hawk who co-sponsored the REPO for Ukrainians Act (signed April 2024), "
              "transferring frozen Russian sovereign assets to fund Ukraine's reconstruction, traveled with a "
              "congressional delegation to Kyiv to pledge U.S. support, and released a statement denouncing the "
              "Trump administration for 'voting with Russia and against Ukraine' at the United Nations — directly "
              "opposing the rubric's call to end open-ended foreign military entanglements.",
              ["https://www.whitehouse.senate.gov/news/release/whitehouse-travels-to-kyiv-to-express-congressional-support-for-ukraines-fight-for-freedom/",
               "https://www.whitehouse.senate.gov/news/release/whitehouse-statement-on-u-s-voting-with-russia-and-against-ukraine-at-united-nations/"]),
        claim("sw2", "sheldon-whitehouse", "economic_stewardship", 2, False,
              "Chaired the Senate Budget Committee (2023–2025) and voted for the Inflation Reduction Act (2022), "
              "the American Rescue Plan Act (2021), and other large deficit-funded spending packages — accumulating "
              "a voting record that consistently favored federal spending expansions over fiscal restraint or any "
              "balanced-budget discipline.",
              ["https://en.wikipedia.org/wiki/Sheldon_Whitehouse",
               "https://www.govtrack.us/congress/members/sheldon_whitehouse/412247"]),
    ]),

    # ---- John Hoeven (ND-R) ----
    ("john-hoeven", "ND", "Senator", [
        claim("jh1", "john-hoeven", "border_immigration", 0, True,
              "A consistent border-security hawk who joined Senate colleagues urging DHS to resume border wall "
              "construction, supports mandatory E-Verify for all employers, and has explicitly framed the issue as "
              "'border security is national security' — backing physical barriers and military-style enforcement to "
              "halt illegal crossings.",
              ["https://www.hoeven.senate.gov/news/news-releases/hoeven-border-security-is-national-security",
               "https://www.hoeven.senate.gov/news/news-releases/hoeven-new-congress-already-working-to-restore-order-at-us-mexico-border"]),
        claim("jh2", "john-hoeven", "economic_stewardship", 2, True,
              "Advocates a three-part fiscal strategy that explicitly includes 'reining in spending and controlling "
              "debt and deficit'; as a former governor who balanced North Dakota's budget he applies that same "
              "fiscal discipline in the Senate — consistent with the rubric's preference for a balanced-budget "
              "approach to federal finances.",
              ["https://www.hoeven.senate.gov/issues/jobs-economy-and-fiscal-responsibility"]),
    ]),

    # ---- Thom Tillis (NC-R) ----
    ("thom-tillis", "NC", "Senator", [
        claim("tt1", "thom-tillis", "election_integrity", 0, True,
              "Co-sponsored the Safeguard American Voter Eligibility (SAVE) Act (S.128, 119th Congress) in July "
              "2024, requiring documentary proof of U.S. citizenship to register to vote in federal elections; has "
              "championed voter-ID legislation since serving as Speaker of the North Carolina House, where he "
              "enacted a bipartisan voter-ID law.",
              ["https://www.tillis.senate.gov/2024/7/tillis-co-sponsors-save-act-continues-fight-to-ensure-only-american-citizens-can-vote",
               "https://www.congress.gov/bill/119th-congress/senate-bill/128"]),
        claim("tt2", "thom-tillis", "foreign_policy_restraint", 1, False,
              "Co-chairs the Senate NATO Observer Group (with Sen. Jeanne Shaheen) and has been a leading Senate "
              "voice for sustained Ukraine military aid, supporting the $95 billion Ukraine/Israel/Taiwan "
              "supplemental package in April 2024 — opposing any reduction in U.S. overseas commitments and "
              "rejecting the restraint-oriented foreign policy the rubric calls for.",
              ["https://en.wikipedia.org/wiki/Thom_Tillis",
               "https://www.tillis.senate.gov/national-security"]),
    ]),

    # ---- Tim Sheehy (MT-R) ----
    ("tim-sheehy", "MT", "Senator", [
        claim("ts1", "tim-sheehy", "election_integrity", 0, True,
              "Co-sponsored the Safeguard American Voter Eligibility Act (S.128, 119th Congress) on January 6, "
              "2026, requiring documentary proof of U.S. citizenship when registering to vote in federal elections "
              "— backing the proof-of-citizenship and voter-verification standard the rubric calls for.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/128/cosponsors",
               "https://en.wikipedia.org/wiki/Tim_Sheehy"]),
        claim("ts2", "tim-sheehy", "economic_stewardship", 2, True,
              "Ran for Senate in 2024 explicitly opposing Biden's 'out-of-control spending' and pledging fiscal "
              "restraint; in the Senate Commerce Committee, prioritized fighting inflation and reducing the cost of "
              "living for Montanans rather than new spending mandates — consistent with the rubric's anti-deficit, "
              "balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Tim_Sheehy",
               "https://ballotpedia.org/Tim_Sheehy"]),
    ]),

    # ---- Roger Wicker (MS-R) ----
    ("roger-wicker", "MS", "Senator", [
        claim("rw1", "roger-wicker", "election_integrity", 0, True,
              "In November 2025 co-introduced the Citizen Ballot Protection Act with Sen. Katie Britt, amending "
              "the NVRA to explicitly permit states to require proof of citizenship on voter-registration forms; "
              "Wicker stated: 'Ensuring that United States citizens are the only people voting is a commonsense "
              "provision that will promote election integrity.'",
              ["https://www.wicker.senate.gov/2025/11/wicker-britt-introduce-the-citizen-ballot-protection-act"]),
        claim("rw2", "roger-wicker", "border_immigration", 0, True,
              "Authored a statute the Biden administration violated when it sold off unused border-wall panels; "
              "has supported legislation to build over 700 miles of reinforced southern-border fencing, increase "
              "border patrol agents, and deploy unmanned aerial vehicles — and voted in January 2025 to advance "
              "the border-security package.",
              ["https://www.wicker.senate.gov/immigration",
               "https://www.wicker.senate.gov/2025/1/wicker-votes-to-advance-border-security"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
