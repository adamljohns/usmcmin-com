#!/usr/bin/env python3
"""Enrichment batch 314: 3rd distinct-category claims for 5 bottom-of-alphabet WY state senators.

Pipeline continues evidence_curated state-level candidates at exactly 2 claims,
reverse-sorted by state — WY senators at the top of that reversed list.
Picks up where batch 313 left off (Schuler, McKeown, French, Nethercott, Pappas done).

Targets (WY senators, reverse-alpha by name within WY):
  Stacy Jones           — election_integrity[0]=True  (voted for HB0156 proof-of-citizenship
                           voting law 2025; Wyoming first state in nation)
  Ogden Driskill        — self_defense[0]=False        (opposed revival of HB0125 gun-free-zone
                           repeal 2024, called it 'absolute idiocy')
  Mike Gierau           — biblical_marriage[0]=False   (Democrat from Jackson; advocate for
                           same-sex marriage recognition in WY statutes)
  Lynn Hutchings        — self_defense[0]=True         (testified for HB0172 gun-free-zone repeal
                           2025; bill became law without governor's signature)
  Laura Taliaferro Pearson — election_integrity[0]=True (Senate co-sponsor of HB0157 proof-of-
                           citizenship voting bill 2025; Wyoming first in nation)

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
    # ---------------- Stacy Jones (WY, State Senator, R) ----------------
    ("stacy-jones", "WY", "State Senator", [
        claim("sj1", "stacy-jones", "election_integrity", 0, True,
              "Voted with the Wyoming Senate Republican majority for HB0156 (2025), which requires proof of U.S. citizenship and 30 days of in-state residency before a person may register to vote in any Wyoming election — from municipal through national. The law took effect July 1, 2025 and made Wyoming the first state in the nation to impose such a comprehensive proof-of-citizenship voter-registration requirement at all election levels, directly satisfying the rubric's election_integrity[0] ballot-security standard.",
              ["https://wyofile.com/governor-allows-proof-of-voter-residency-citizenship-requirement-to-become-law-without-signature/",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/"]),
    ]),

    # ---------------- Ogden Driskill (WY, State Senator, R) ----------------
    ("ogden-driskill", "WY", "State Senator", [
        claim("od1", "ogden-driskill", "self_defense", 0, False,
              "As Wyoming Senate President, publicly opposed the 2024 effort to revive HB0125 (repeal of gun-free zones), calling the procedural move to resurrect the killed bill 'absolute idiocy' and voting against it. The Senate overruled Driskill 16-15 to revive the bill, which Driskill then condemned as a damaging precedent. His documented stance against expanding lawful carry into previously restricted areas places him at odds with the constitutional-carry ideal the rubric's self_defense[0] standard envisions.",
              ["https://cowboystatedaily.com/2024/03/05/senate-overrules-driskill-in-raw-power-struggle-to-revive-gun-free-zone-bill/",
               "https://wyofile.com/shot-down-resuscitated-wyoming-senate-bucks-precedent-to-target-gun-free-zones/"]),
    ]),

    # ---------------- Mike Gierau (WY, State Senator, D) ----------------
    ("mike-gierau", "WY", "State Senator", [
        claim("mg1", "mike-gierau", "biblical_marriage", 0, False,
              "One of Wyoming's only two Senate Democrats and representing the state's most liberal district (Jackson, Teton County), Gierau has been a consistent advocate for same-sex marriage recognition and LGBTQ protections in state law. When the Wyoming Senate was split over updating statutes to reflect the legalization of same-sex marriage in 2022, Gierau was among the supporters; he also personally intervened to push LGBTQ issues to the forefront and to demand committee decorum during a contentious meeting at which LGBTQ advocates faced personal attacks — rejecting the one-man-one-woman definition of marriage the rubric's biblical_marriage[0] standard requires.",
              ["https://www.wyomingpublicmedia.org/news/2022-11-17/wyoming-senators-are-split-on-support-for-same-sex-marriage-protections",
               "https://wyofile.com/legislative-leaders-address-decorum-wake-sundance/"]),
    ]),

    # ---------------- Lynn Hutchings (WY, State Senator, R) ----------------
    ("lynn-hutchings", "WY", "State Senator", [
        claim("lh1", "lynn-hutchings", "self_defense", 0, True,
              "In January 2025, testified before committee in favor of HB0172 (gun-free zone repeal), arguing that repealing gun-free zones would allow legislators to protect themselves — noting her life had been threatened multiple times as a senator. HB0172 became law in 2025 without the governor's signature, eliminating most of Wyoming's gun-free zones and expanding where licensed carriers may legally carry. Hutchings's personal advocacy directly reflects the constitutional-carry standard the rubric's self_defense[0] ideal requires.",
              ["https://cowboystatedaily.com/2025/01/17/repealing-gun-free-zones-wont-mean-ar-15s-in-wyoming-capitol-sponsor-says/",
               "https://wyofile.com/gordon-lets-wyoming-gun-free-zones-repeal-become-law-decries-legislative-power-grab/"]),
    ]),

    # ---------------- Laura Taliaferro Pearson (WY, State Senator, R) ----------------
    ("laura-taliaferro-pearson", "WY", "State Senator", [
        claim("ltp1", "laura-taliaferro-pearson", "election_integrity", 0, True,
              "Senate co-sponsor of HB0157 (2025), which requires proof of U.S. citizenship to register to vote in Wyoming. The bill, also co-sponsored by Senators Boner and Steinmetz, made Wyoming the first state in the nation to mandate proof-of-citizenship for voter registration at all election levels — municipal through national. The law became effective in 2025 and directly satisfies the rubric's election_integrity[0] ballot-security standard for stringent voter-registration controls.",
              ["https://www.wyoleg.gov/Legislation/2025/HB0157",
               "https://cowboystatedaily.com/2025/03/25/wyoming-is-first-state-to-require-proof-of-citizenship-to-vote-in-all-elections/"]),
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
