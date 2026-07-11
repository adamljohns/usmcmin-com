#!/usr/bin/env python3
"""Enrichment batch 637: hand-curated claims for 2 Oklahoma State Senators.

Senators: Brent Howard (SD-38), Brian Guthrie (SD-25).
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
    # --- Brent Howard (OK SD-38, State Senator — Altus/SW Oklahoma) ---
    ("brent-howard", "OK", "State Senator", [
        claim("bh1", "brent-howard", "election_integrity", 0, True,
              "Howard prime-authored SB 377 (2023), requiring voter registration cancellation for any person who is excused from jury duty because they are not a U.S. citizen, and directing court clerks to report such persons to the district attorney and U.S. attorney; the Senate passed it 45-1 on March 9, 2023, and Gov. Stitt signed it effective November 1, 2023.",
              ["https://oksenate.gov/press-releases/senate-approves-measure-stop-noncitizens-voting-oklahoma-elections",
               "https://thefederalist.com/2023/02/23/oklahoma-senate-moves-to-ensure-only-u-s-citizens-are-voting-in-state-elections/"]),
        claim("bh2", "brent-howard", "sanctity_of_life", 0, True,
              "Howard voted YES on SB 918 (2021), Oklahoma's abortion trigger law authored by Senate Pro Tempore Greg Treat, which would restore Oklahoma's authority to prohibit abortion if Roe v. Wade were overturned; the Senate passed it 38-9 on March 10, 2021, and Gov. Stitt signed it April 27, 2021.",
              ["https://legiscan.com/OK/bill/SB918/2021",
               "https://oksenate.gov/senate-votes/2021-votes-1"]),
        claim("bh3", "brent-howard", "sanctity_of_life", 1, False,
              "As chair of the Senate Judiciary Committee, Howard voted NO on SB 456 (2025), the Abolition of Abortion Act, which would have classified abortion as homicide and exposed women to criminal prosecution; the bill died in committee 6-2 on February 20, 2025. Howard stated 'I think that that's a step too far,' signaling support for existing abortion bans but opposition to the most punitive abolition approach.",
              ["https://www.kosu.org/politics/2025-02-20/abolition-of-abortion-act-fails-in-oklahoma-senate-judiciary-committee",
               "https://okcfox.com/news/local/protect-life-advocates-dismayed-after-committee-nixes-abolition-of-abortion-act-dusty-deevers-state-sen-oklahoma-politics-nathan-weisser-brent-howard-todd-gollihare-darcy-jech-paul-rosino-mary-boren-michael-brooks-judiciary-david-bullard-covenant-command"]),
    ]),

    # --- Brian Guthrie (OK SD-25, State Senator — Bixby/S Tulsa, in office since Nov 2024) ---
    ("brian-guthrie", "OK", "State Senator", [
        claim("bg1", "brian-guthrie", "sanctity_of_life", 0, True,
              "Guthrie voted YES on HB 1168 (2026), making it a felony (up to 10 years prison and $100,000 fine) to knowingly possess or deliver abortion-inducing drugs — mifepristone, misoprostol, or methotrexate — to someone intending to use them for an abortion; Guthrie stated on the floor 'this is a step in the right direction.' The Senate passed it 37-10 on April 30, 2026, and Gov. Stitt signed it May 5, 2026.",
              ["https://www.oklegislature.gov/cf/2025-26%20SUPPORT%20DOCUMENTS/votes/Senate/HB1168_VOTES.HTM",
               "https://legiscan.com/OK/bill/HB1168/2026"]),
        claim("bg2", "brian-guthrie", "border_immigration", 0, True,
              "Guthrie prime-authored SB 1582 (2026), closing loopholes in Oklahoma's foreign land ownership law by defining 'bona fide resident' as a lawful permanent resident of the United States, requiring persons who cease to qualify to sell their Oklahoma land within five years or face forfeiture to the state; the bill passed both chambers and was signed into law by Gov. Stitt.",
              ["https://oksenate.gov/press-releases/senator-guthrie-introduces-legislation-prohibit-foreign-ownership-oklahoma-land",
               "https://oksenate.gov/press-releases/judiciary-committee-approves-guthrie-bill-close-foreign-land-ownership-loopholes"]),
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
