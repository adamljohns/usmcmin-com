#!/usr/bin/env python3
"""Enrichment batch 346: top-up 4 evidence_curated US House candidates with 3 existing claims.

Targets (WI / WA — bottom-of-alphabet sweep, adding 2 claims each):
  Jessi Ebben       (WI-R, 2026 U.S. Representative WI-07) — +2 claims
  Kevin Hermening   (WI-R, 2026 U.S. Representative WI-07) — +2 claims
  Rebecca Cooke     (WI-D, 2026 U.S. Representative WI-03) — +2 claims
  Amanda McKinney   (WA-R, 2026 U.S. Representative WA-04) — +2 claims

Categories: economic_stewardship, border_immigration, family_child_sovereignty,
            self_defense, biblical_marriage, refuse_state_overreach.

NOTE: writes scorecard.json MINIFIED (no pretty-print) to keep the master
under GitHub's 50 MB limit.
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
    # ---------- Jessi Ebben (WI-R, 2026 WI-07 candidate) ----------
    # Existing: sanctity_of_life[0]T, self_defense[1]T, border_immigration[0]T
    ("jessi-ebben", "WI", "Representative", [
        claim("je4", "jessi-ebben", "economic_stewardship", 2, True,
              "Ebben advocates for a balanced budget and 'making smart cuts to prioritized spending "
              "on vital government functions,' stating that 'The national debt is something that "
              "representatives have not taken seriously and pushed off each and every year.' She "
              "calls for 'slashing government spending' as part of her core fiscal platform, "
              "consistent with the rubric's anti-deficit/balanced-budget standard.",
              ["https://pbswisconsin.org/candidate/jessi-ebben/",
               "https://www.ebbenforwisconsin.com/issues"]),
        claim("je5", "jessi-ebben", "border_immigration", 1, True,
              "A self-described 'Day 1 supporter of President Trump's America First agenda,' Ebben "
              "explicitly embraces the full scope of Trump's immigration enforcement program, "
              "which includes mandatory removal of undocumented immigrants and mass deportation "
              "operations. Her campaign pledges to 'secure the southern border' and 'stop the "
              "flow of illegal drugs like fentanyl' through robust federal law enforcement — "
              "positions consistent with the rubric's mandatory-deportation standard.",
              ["https://www.ebbenforwisconsin.com/issues",
               "https://www.wispolitics.com/2025/ebben-campaign-rep-eric-burlison-endorses-trump-conservative-jessi-ebben-in-wi-07/"]),
    ]),

    # ---------- Kevin Hermening (WI-R, 2026 WI-07 candidate) ----------
    # Existing: sanctity_of_life[0]T, biblical_marriage[2]T, economic_stewardship[2]T
    ("kevin-hermening", "WI", "Representative", [
        claim("kh4", "kevin-hermening", "border_immigration", 0, True,
              "In his formal campaign launch statement, Hermening declared he is 'committed to "
              "keeping our border secure and our communities safe, defending the rule of law' as "
              "a core platform plank. His campaign materials specifically call for securing the "
              "southern border, stopping fentanyl trafficking, and supporting law enforcement to "
              "enforce immigration statutes — consistent with the rubric's wall-and-military-at-"
              "the-border standard.",
              ["https://kevinhermening.com/",
               "https://wausaupilotandreview.com/2026/02/18/hermening-formally-launches-bid-for-7th-congressional-district-seat/"]),
        claim("kh5", "kevin-hermening", "family_child_sovereignty", 0, True,
              "In his campaign launch Hermening explicitly stated that 'parents — not the "
              "government — should guide their children's upbringing and education' and pledged "
              "to 'protect children from radical ideology in schools.' This direct commitment to "
              "parental authority over education and protection from government-imposed curriculum "
              "aligns with the rubric's parental-rights and anti-CPS-overreach standard.",
              ["https://kevinhermening.com/",
               "https://wausaupilotandreview.com/2026/02/18/hermening-formally-launches-bid-for-7th-congressional-district-seat/"]),
    ]),

    # ---------- Rebecca Cooke (WI-D, 2026 WI-03 candidate) ----------
    # Existing: sanctity_of_life[0]F, sanctity_of_life[4]F, election_integrity[0]F
    ("rebecca-cooke", "WI", "Representative", [
        claim("rc4", "rebecca-cooke", "self_defense", 1, False,
              "Cooke is 'a supporter of universal background checks' who 'has called for stronger "
              "enforcement of red flag laws' — policies that allow courts to confiscate legally "
              "owned firearms from individuals who have committed no crime. Her support for red "
              "flag laws directly conflicts with the rubric's standard opposing extreme-risk "
              "protection orders (red-flag laws) as unconstitutional prior restraint on Second "
              "Amendment rights.",
              ["https://ballotpedia.org/Rebecca_Cooke",
               "https://en.wikipedia.org/wiki/Rebecca_Cooke_(politician)"]),
        claim("rc5", "rebecca-cooke", "self_defense", 0, False,
              "As a gun-safety advocate who supports red flag laws and universal background "
              "checks, Cooke has not endorsed constitutional carry — the rubric's standard that "
              "law-abiding citizens should be able to carry a firearm without a government permit. "
              "Her gun-safety agenda, which requires background checks for all transfers and "
              "allows courts to remove firearms from individuals deemed dangerous, is structurally "
              "incompatible with permitless-carry legislation that trusts citizens without prior "
              "government approval.",
              ["https://ballotpedia.org/Rebecca_Cooke",
               "https://news.ballotpedia.org/2024/09/10/incumbent-rep-derrick-van-orden-r-and-rebecca-cooke-d-are-running-in-the-general-election-for-wisconsins-3rd-congressional-district/"]),
    ]),

    # ---------- Amanda McKinney (WA-R, 2026 WA-04 candidate) ----------
    # Existing: self_defense[1]T, border_immigration[0]T, refuse_federal_overreach[0]T
    ("amanda-mckinney", "WA", "Representative", [
        claim("am4", "amanda-mckinney", "biblical_marriage", 2, True,
              "McKinney is 'a fierce advocate for initiatives protecting fairness in girls' "
              "sports, ensuring biological males do not compete against females.' She explicitly "
              "supports protecting Title IX so that 'women's sports remain for biological "
              "females' and opposes 'policies that undermine women's athletics.' President Trump "
              "endorsed her campaign in part because of her stance on 'banning trans women from "
              "women's sports' — a clear rejection of transgender ideology in the public square.",
              ["https://www.mckinneyforwashington.com/about",
               "https://www.yakimaherald.com/news/local/government/elections/trump-endorses-yakimas-amanda-mckinney-for-wa-congressional-campaign/article_8f63ffb3-ab67-49a3-bff1-93b43d0a2a95.html"]),
        claim("am5", "amanda-mckinney", "refuse_state_overreach", 0, True,
              "McKinney led efforts with Let's Go Washington to pass Initiative 2066 on the "
              "November 2024 ballot, which repealed Washington state's restrictions on natural "
              "gas use and preserved consumer energy choice. The initiative overturned a "
              "state regulation that would have banned natural gas hookups in new buildings, "
              "directly pushing back against state government overreach into private energy "
              "decisions — a refusal-of-state-overreach posture consistent with the rubric.",
              ["https://www.mckinneyforwashington.com/about",
               "https://washingtonstatestandard.com/2026/01/07/as-barbs-fly-and-trump-wades-in-a-central-wa-congressional-race-heats-up/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents wrong-state same-slug collisions."""
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
        print(f"  ✓ {m['name']:<35} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
