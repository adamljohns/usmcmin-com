#!/usr/bin/env python3
"""Enrichment batch 699: third cited claim for 5 WV Republican State Senators.

Targets evidence_curated WV senators that had exactly 2 claims. Adds one
additional claim each in a distinct rubric category, drawn from 2024-2026
WV legislative votes and bill co-sponsorships.

Targets (all WV-R, State Senator):
  Robbie Morris    - border_immigration/2 (SB 615, 2026, ICE cooperation)
  Patrick Martin   - sanctity_of_life/0  (SB 173, 2026, abortifacient ban)
  Mike Oliverio    - biblical_marriage/2  (SB 456, 2025, Riley Gaines Act)
  Mark R. Maynard  - self_defense/0       (SB 478, 2026, 2A Reaffirmation Act)
  Jason Barrett    - election_integrity/0 (SB 487, 2025, voter-roll cleanup)

NOTE: writes scorecard.json MINIFIED — SCORECARD.write_text(json.dumps(scorecard,
separators=(",",":"))) — preserving the ~35-36MB master under GitHub's 50MB limit.
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
    # --- Robbie Morris (WV-R, State Senator) ---
    # Existing: sanctity_of_life/0, self_defense/0
    # Adding: border_immigration/2 (SB 615, ICE cooperation mandate, 2026)
    ("robbie-morris", "WV", "State Senator", [
        claim("rm1", "robbie-morris", "border_immigration", 2, True,
              "Voted in favor of WV Senate Bill 615 (2026), which mandates that all state, county, and "
              "local law enforcement immediately notify and fully cooperate with ICE whenever a person "
              "in custody is identified as unlawfully present in the United States, and prohibits any "
              "local government from adopting sanctuary-style policies limiting that cooperation. The "
              "bill passed the WV Senate 32-2 on February 9, 2026, with both no votes cast by the "
              "chamber's only two Democrats — every Republican senator, including Morris, voted in favor.",
              ["https://wvmetronews.com/2026/02/09/senate-passes-bill-mandating-local-officers-turn-over-people-to-ice-if-unlawful-immigration-status-is-determined/",
               "https://wtov9.com/news/local/west-virginia-senate-approves-sb-615-requiring-local-cooperation-with-ice-west-virginia-senate-bill-615-immigration-ice-law-enforcement-public-safety-deportation-legislation",
               "https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb615+sub1.htm&yr=2026&sesstype=RS&i=615"]),
    ]),

    # --- Patrick Martin (WV-R, State Senator, Senate Majority Leader) ---
    # Existing: election_integrity/0, biblical_marriage/4
    # Adding: sanctity_of_life/0 (SB 173, chemical abortifacient trafficking ban, 2026)
    ("patrick-martin", "WV", "State Senator", [
        claim("pm1", "patrick-martin", "sanctity_of_life", 0, True,
              "As Senate Majority Leader, Martin managed floor consideration and voted Yea on WV Senate "
              "Bill 173 (February 13, 2026), which makes it a felony punishable by 3-10 years to "
              "traffic or dispense chemical abortion medications in West Virginia without a valid "
              "physician-patient relationship, and strips medical licenses from any doctor who "
              "illegally prescribes abortifacients in the state. The bill passed 31-1 (sole no vote: "
              "Sen. Joey Garcia, D-Marion), with Martin's name appearing in the Yea column of the "
              "official Senate roll call (Roll Call 71, Feb 13, 2026).",
              ["https://www.wvlegislature.gov/legisdocs/2026/RS/votes/senate/02-13-0071.pdf",
               "https://wvpublic.org/story/health-science/abortion-medication-ban-passes-senate-moves-to-house/",
               "https://westvirginiawatch.com/2026/02/13/senate-passes-bill-prohibiting-abortifacients-being-prescribed-or-mailed-to-west-virginia/"]),
    ]),

    # --- Mike Oliverio (WV-R, State Senator) ---
    # Existing: sanctity_of_life/0, election_integrity/0
    # Adding: biblical_marriage/2 (SB 456, Riley Gaines Act, 2025 — individual vote confirmed)
    ("mike-oliverio", "WV", "State Senator", [
        claim("mo1", "mike-oliverio", "biblical_marriage", 2, True,
              "Voted Yes on WV Senate Bill 456 (2025) — the 'Riley Gaines Act' / 'Stand with Women' "
              "legislation — which codified in state law that 'sex' means biological characteristics "
              "present at birth and restricted access to single-sex restrooms, changing rooms, and "
              "overnight sleeping quarters in public schools, domestic violence shelters, state "
              "colleges, and correctional facilities to biological males and females only. The bill "
              "passed the Senate 32-1 on March 3, 2025 (sole no vote: Sen. Joey Garcia, D-Marion) "
              "and was signed into law by Governor Patrick Morrisey on March 12, 2025; Oliverio's "
              "individual Yes vote is confirmed by news coverage of the vote.",
              ["https://en.wikipedia.org/wiki/West_Virginia_Senate_Bill_456",
               "https://blog.wvlegislature.gov/headline/2025/03/03/senate-passes-bill-defining-male-and-female/",
               "https://wchstv.com/news/local/west-virginia-senate-passes-bill-that-defines-differences-in-sexes",
               "https://www.wvlegislature.gov/Bill_Text_HTML/2025_SESSIONS/RS/bills/sb456%20sub1%20enr.pdf"]),
    ]),

    # --- Mark R. Maynard (WV-R, State Senator) ---
    # Existing: sanctity_of_life/0, family_child_sovereignty/0
    # Adding: self_defense/0 (SB 478, Second Amendment Reaffirmation Act, 2026 — co-sponsor confirmed)
    ("mark-r-maynard", "WV", "State Senator", [
        claim("mm1", "mark-r-maynard", "self_defense", 0, True,
              "Co-sponsored West Virginia SB 478 (2026), the 'Second Amendment Reaffirmation and "
              "Protection Act,' which automatically preserves West Virginians' full firearms rights — "
              "including weapons regulated under the National Firearms Act, the Gun Control Act, and "
              "the Firearm Owners Protection Act — in the event any portion of those federal laws is "
              "repealed by Congress or nullified by federal courts. Maynard is named as a co-sponsor "
              "on the introduced bill text alongside Senators Rose, Helton, and Rucker; the WV Senate "
              "passed the bill unanimously 34-0 on February 12, 2026.",
              ["https://www.wvlegislature.gov/Bill_Text_HTML/2026_SESSIONS/RS/bills/sb478%20intr.pdf",
               "https://www.wdtv.com/2026/01/19/west-virginia-senate-introduces-second-amendment-reaffirmation-bill/",
               "https://www.guns.com/news/2026/02/20/west-virginia-passes-pro-gun-bills-as-its-neighbor-chooses-a-different-path"]),
    ]),

    # --- Jason Barrett (WV-R, State Senator, District 16, Senate Finance Chair) ---
    # Existing: sanctity_of_life/0, self_defense/0
    # Adding: election_integrity/0 (SB 487, 2025, voter-roll cleanup — named on roll call 33-1)
    ("jason-barrett", "WV", "State Senator", [
        claim("jb1", "jason-barrett", "election_integrity", 0, True,
              "Voted Aye (named on the official Senate roll call, 33-1) on WV SB 487 (2025 Regular "
              "Session), which reduced the voter-inactivity threshold from four years to two years, "
              "accelerating the removal of ineligible names from active voter rolls. Barrett also voted "
              "Aye on WV HB 3016 (2025), requiring government-issued photo identification at the polls "
              "(signed by Governor Morrisey April 30, 2025), and on WV SJR 9 (2026), a "
              "citizenship-only voting constitutional amendment placed on the November 2026 ballot by "
              "a unanimous 34-0 Senate vote — forming the core of West Virginia's 10-bill "
              "election-integrity package.",
              ["https://fastdemocracy.com/bill-search/wv/2025/bills/WVB00029506/",
               "https://news.ballotpedia.org/2026/04/23/west-virginia-legislators-place-citizenship-requirement-for-voting-on-the-ballot-enact-10-other-election-bills/",
               "https://westvirginiawatch.com/briefs/bill-requiring-stricter-voter-photo-id-clears-west-virginia-senate/",
               "https://governor.wv.gov/article/governor-patrick-morrisey-signs-voter-id-bill-law"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write — preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
