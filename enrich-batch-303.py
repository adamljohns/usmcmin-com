#!/usr/bin/env python3
"""Enrichment batch 303: 3rd claims for 5 federal candidates (bottom-of-alphabet states).

Archetype_curated federal-senator/representative bucket fully exhausted.
Batch targets evidence_curated federal candidates with exactly 2 claims —
taken from the bottom of the alphabet (TX, TN, OH, GA, FL) spanning
distinct rubric categories not yet covered in each candidate's profile.

Targets:
  Josh Williams   (OH-09, R) — pro-life caucus + SHE WINS Act → sanctity_of_life
  Craig Ballin    (TN-06, D) — "Christian for Pro-Choice" → sanctity_of_life
  Tony Gonzales   (TX-23, R) — NRLC endorsed, anti-WHPA vote → sanctity_of_life
  Barry Loudermilk(GA-11, R) — NRA lifetime A, anti-background-check vote → self_defense
  Mario Diaz-Balart(FL-26, R)— DIGNIDAD Act cosponsor, pathway to legal status → border_immigration

Each claim cites >=1 reliable source and reflects 2024-2026 positions.

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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---- Josh Williams (OH-09, R — OH state rep, LOST 5/5 R primary to Merrin) ----
    ("josh-williams-oh-09", "OH", "OH-09", [
        claim("jw1", "josh-williams-oh-09", "sanctity_of_life", 0, True,
              "A member of the Ohio House Pro-Life Caucus in the 136th General Assembly, Williams co-introduced the SHE WINS Act (Share the Health and Empower With Informed Notices Act), which the Ohio House passed 64–32, requiring a 24-hour informed consent waiting period before any abortion, including disclosure of the procedure and alternatives; he also introduced HB 475 to prohibit state funds from any entity that supports, promotes, or provides abortions — confirming a consistent legislative pro-life posture.",
              ["https://www.ohiohouse.gov/members/josh-williams/news/odioso-williams-champion-she-wins-act-133967",
               "https://spectrumnews1.com/oh/columbus/news/2026/03/18/bill-proposes-24-hour-waiting-period-for-abortions",
               "https://ohiohouse.gov/news/republican/ohio-house-pro-life-caucus-convenes-first-meeting-of-the-136th-general-assembly-135405"]),
    ]),

    # ---- Craig Ballin (TN-06, D — 2026 D Candidate, open Rose seat) ----
    ("craig-ballin", "TN", "TN-06", [
        claim("cb1", "craig-ballin", "sanctity_of_life", 0, False,
              "On his campaign website's issues page, Ballin identifies as 'Christian for Pro-Choice' and states 'Private decisions are private—and government interference is unacceptable,' expressly rejecting government restrictions on abortion including any life-at-conception or personhood framework.",
              ["https://ballinforcongress.com/the-issues/"]),
    ]),

    # ---- Tony Gonzales (TX-23, R — resigned April 2026, seat vacant) ----
    ("tony-gonzales", "TX", "resigned", [
        claim("tg1", "tony-gonzales", "sanctity_of_life", 0, True,
              "The National Right to Life Committee (NRLC) — the nation's oldest and largest pro-life organization — endorsed Gonzales and reaffirmed that endorsement during his congressional runoff campaign, citing his strong pro-life voting record; Gonzales cosponsored and voted for the No Taxpayer Funding for Abortion Act (banning taxpayer-funded abortions government-wide with narrow exceptions) and voted against the Women's Health Protection Act, the most sweeping federal abortion-access bill of the 119th Congress.",
              ["https://nrlc.org/communications/nrlc-reaffirms-endorsement-of-texas-congressman-tony-gonzales-in-runoff-election/",
               "https://sbaprolife.org/representative/Tony-Gonzales"]),
    ]),

    # ---- Barry Loudermilk (GA-11, R — retiring, seat open 2026) ----
    ("barry-loudermilk", "GA", "retiring", [
        claim("bl1", "barry-loudermilk", "self_defense", 1, True,
              "Holds an NRA lifetime A rating, reflecting a consistent record of opposing gun-control expansions; he voted NAY on the Bipartisan Background Checks Act (H.R. 8, 118th Congress), which would have required universal background checks for all private firearm sales — opposing the kind of registry-adjacent federal tracking infrastructure the rubric identifies as a Second Amendment threat.",
              ["https://www.nrapvf.org/emails/2020/georgia/barry-loudermilk-ga-11-general",
               "https://www.ontheissues.org/GA/Barry_Loudermilk_Gun_Control.htm"]),
    ]),

    # ---- Mario Diaz-Balart (FL-26, R — sitting U.S. Representative) ----
    ("mario-diaz-balart", "FL", "US Representative", [
        claim("md1", "mario-diaz-balart", "border_immigration", 1, False,
              "In the 119th Congress (2025–2026), Diaz-Balart is a cosponsor of the DIGNIDAD Act (H.R. 4393), which establishes a 7-year renewable 'Dignity Program' deferring deportation for eligible undocumented immigrants who meet employment or education requirements and pay restitution, and creates a pathway to lawful permanent residency for DACA recipients — providing legal status rather than mandatory deportation for millions of undocumented individuals.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/4393",
               "https://www.presidentialprayerteam.org/2026/04/11/house-of-representatives-dignidad-act-promotes-amnesty-for-millions/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher; prevents wrong-state same-slug collisions."""
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
        print(f"  ✓ {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
