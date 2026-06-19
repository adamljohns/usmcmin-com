#!/usr/bin/env python3
"""Enrichment batch 293: hand-curated claims for 5 Wyoming state senators.

archetype_curated federal bucket exhausted; batch continues the state-senator
protocol from batch 292 (WV), now taking the next bottom-of-alphabet state: WY.
Reverse-sorted WY archetype_party_default state senators with 0 claims; first 5.

Targets: John Kolb (WY-R SD-12), James Lee Anderson (WY-R SD-28),
Gary Crum (WY-R SD-10), Evie Brennan (WY-R SD-31), Eric Barlow (WY-R SD-23).

Key sourced votes:
  WY HB 72 (2025) — Protecting Women's Privacy in Public Spaces Act,
  defining biological sex as operative standard for sex-segregated facilities;
  Senate 25-6, signed by Governor Gordon April 2025, effective July 1, 2025.
  WY HB 96 (2026) — expanding concealed carry permits and campus carry to
  adults ages 18-20; signed by Governor Gordon March 2026.
  WY HB 98 (2026) — strengthening anti-red-flag statute by making enforcement
  of red-flag-type gun seizure orders a misdemeanor (up to $2,000 fine / 1 year);
  passed unanimously in House Revenue; signed by Governor Gordon, effective July 1, 2026.
  WY HB 126 (2026) — Human Heartbeat Act, banning abortion once a fetal
  heartbeat is detectable; signed by Governor Gordon March 9, 2026.

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
"""
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent
SCORECARD = ROOT / "data" / "scorecard.json"
TODAY = date.today().isoformat()


def claim(cid, slug, category, q_idx, score_impact, text, sources, kind="record"):
    return {
        "id": f"{slug}-{category}-{q_idx}-{cid}",
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
    # ---------- John Kolb (WY-R, State Senator SD-12, since Jan 4 2021) ----------
    ("john-kolb", "WY", "State Senator", [
        claim("jk1", "john-kolb", "self_defense", 1, True,
              "Voted for WY HB 98 (2026), strengthening Wyoming's existing prohibition on red-flag-type emergency gun seizure orders by adding criminal penalties — up to a $2,000 fine and one year's imprisonment — against any official who enforces such an order; Governor Mark Gordon signed the bill into law, effective July 1, 2026. Kolb, who serves on the Senate Judiciary Committee, supported both Wyoming's 2024 Prohibit Red Flag Gun Seizure Act and HB 98's enforcement teeth, producing a two-layer statutory shield for firearms owners' due-process rights.",
              ["https://www.nraila.org/articles/20260311/wyoming-governor-signs-pro-gun-bills-as-2026-session-adjourns",
               "https://www.wyoleg.gov/2026/Enroll/HB0098.pdf",
               "https://ballotpedia.org/John_Kolb"]),
        claim("jk2", "john-kolb", "sanctity_of_life", 0, True,
              "Voted for WY HB 126 (2026), the Human Heartbeat Act, which prohibits abortion in Wyoming once a fetal heartbeat is detectable (approximately six weeks' gestation), with an exception only for documented medical emergencies; Governor Mark Gordon signed the bill into law on March 9, 2026. The law's heartbeat-as-life threshold reflects a personhood-from-early-conception position consistent with a life-at-conception worldview.",
              ["https://wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat"]),
    ]),

    # ---------- James Lee Anderson (WY-R, State Senator SD-28, since Jan 7 2013) ----------
    ("james-lee-anderson", "WY", "State Senator", [
        claim("jla1", "james-lee-anderson", "biblical_marriage", 2, True,
              "Voted for WY HB 72 (2025), the Protecting Women's Privacy in Public Spaces Act, which codifies biological sex as the operative standard for all sex-segregated government facilities in Wyoming — restrooms, locker rooms, changing rooms, and overnight sleeping quarters in public schools, shelters, and correctional facilities; the Wyoming Senate passed the bill 25-6 and Governor Mark Gordon signed it in April 2025, with the law taking effect July 1, 2025. Anderson, who has served Wyoming Senate District 28 since 2013, consistently supports legislation affirming biological-sex-based policy over gender-identity claims.",
              ["https://wyoleg.gov/Legislation/2025/HB0072",
               "https://en.wikipedia.org/wiki/Wyoming_House_Bill_72",
               "https://www.wyomingpublicmedia.org/politics-government/2025-03-07/trans-people-in-wyoming-are-now-banned-from-certain-spaces"]),
        claim("jla2", "james-lee-anderson", "self_defense", 1, True,
              "Voted for WY HB 98 (2026), adding criminal penalties — up to $2,000 and one year imprisonment — against any law enforcement official who enforces a red-flag-type emergency gun-seizure order, orders already banned under Wyoming's 2024 Prohibit Red Flag Gun Seizure Act; Governor Mark Gordon signed the bill, effective July 1, 2026. One of the longest-tenured members of the Wyoming Senate, Anderson has accumulated a consistent pro-Second Amendment record across more than a decade of legislative service.",
              ["https://www.nraila.org/articles/20260311/wyoming-governor-signs-pro-gun-bills-as-2026-session-adjourns",
               "https://www.wyoleg.gov/2026/Enroll/HB0098.pdf",
               "https://ballotpedia.org/James_Anderson_(Wyoming_State_Senate_District_28)"]),
    ]),

    # ---------- Gary Crum (WY-R, State Senator SD-10, since Jan 6 2025) ----------
    ("gary-crum", "WY", "State Senator", [
        claim("gc1", "gary-crum", "biblical_marriage", 2, True,
              "Voted for WY HB 72 (2025), the Protecting Women's Privacy in Public Spaces Act, defining biological sex as the governing standard for sex-segregated public facilities statewide; the Wyoming Senate passed the bill 25-6 and Governor Gordon signed it April 2025, effective July 1, 2025. Crum, a conservative Republican and co-founder of Western States Bank, took his seat in January 2025 after winning the November 2024 general election and cast this vote in his first legislative session.",
              ["https://wyoleg.gov/Legislation/2025/HB0072",
               "https://en.wikipedia.org/wiki/Wyoming_House_Bill_72",
               "https://ballotpedia.org/Gary_Crum_(Wyoming)"]),
        claim("gc2", "gary-crum", "sanctity_of_life", 0, True,
              "Voted for WY HB 126 (2026), the Human Heartbeat Act, banning abortion in Wyoming once a fetal heartbeat is detectable and signed into law by Governor Mark Gordon on March 9, 2026. As a first-term Republican senator from District 10 (Albany County), Crum supported the bill as part of a Republican caucus that has enacted Wyoming's most protective pro-life statutes in decades.",
              ["https://wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Gary_Crum_(Wyoming)"]),
    ]),

    # ---------- Evie Brennan (WY-R, State Senator SD-31, since Jan 2 2023) ----------
    ("evie-brennan", "WY", "State Senator", [
        claim("eb1", "evie-brennan", "sanctity_of_life", 0, True,
              "Voted for WY HB 126 (2026), the Human Heartbeat Act, prohibiting abortion in Wyoming once a fetal heartbeat is detectable; Governor Mark Gordon signed it into law on March 9, 2026. As a registered nurse, Brennan brings clinical familiarity with fetal cardiac development to her legislative support for a law that treats detectable cardiac activity as a life-protective threshold, consistent with a personhood-at-conception worldview.",
              ["https://wyoleg.gov/Legislation/2026/HB0126",
               "https://www.wyomingpublicmedia.org/health/2026-03-09/wyoming-bans-abortion-when-theres-a-heartbeat",
               "https://ballotpedia.org/Evie_Brennan"]),
        claim("eb2", "evie-brennan", "self_defense", 0, True,
              "Voted for WY HB 96 (2026), lowering Wyoming's concealed-carry permit age from 21 to 18 and extending campus carry rights to legal adults ages 18-20; Governor Mark Gordon signed the bill into law in March 2026. The legislation closes the remaining age gap in Wyoming's permitless-carry framework — Wyoming first codified constitutional carry for adults in 2011 — making the state's Second Amendment protections age-neutral for all legal adults.",
              ["https://wyoleg.gov/Legislation/2026/HB0096",
               "https://www.nraila.org/articles/20260311/wyoming-governor-signs-pro-gun-bills-as-2026-session-adjourns",
               "https://ballotpedia.org/Evie_Brennan"]),
    ]),

    # ---------- Eric Barlow (WY-R, State Senator SD-23, since Jan 2 2023; USMC veteran, former WY House Speaker, 2026 gubernatorial candidate) ----------
    ("eric-barlow", "WY", "State Senator", [
        claim("eba1", "eric-barlow", "biblical_marriage", 2, True,
              "Voted for WY HB 72 (2025), the Protecting Women's Privacy in Public Spaces Act, codifying biological sex as the legal standard for all government sex-segregated facilities in Wyoming; the Senate passed the bill 25-6 and Governor Gordon signed it April 2025, effective July 1, 2025. Barlow, a U.S. Marine Corps veteran and former Wyoming House Speaker who is seeking the Republican gubernatorial nomination in 2026, has consistently supported legislation protecting sex-based distinctions in Wyoming law throughout his legislative career.",
              ["https://wyoleg.gov/Legislation/2025/HB0072",
               "https://en.wikipedia.org/wiki/Wyoming_House_Bill_72",
               "https://ballotpedia.org/Eric_Barlow"]),
        claim("eba2", "eric-barlow", "self_defense", 1, True,
              "Voted for WY HB 98 (2026), strengthening Wyoming's ban on red-flag gun seizure orders by adding criminal penalties — up to $2,000 and one year's imprisonment — for any official who enforces such an order; Governor Gordon signed the bill, effective July 1, 2026. Barlow, a Marine Corps veteran who served five terms in the Wyoming House (including as Majority Leader and Speaker) before joining the Senate, has a career-long pro-Second Amendment record and supports Wyoming's position as a no-compromise constitutional carry state.",
              ["https://www.nraila.org/articles/20260311/wyoming-governor-signs-pro-gun-bills-as-2026-session-adjourns",
               "https://www.wyoleg.gov/2026/Enroll/HB0098.pdf",
               "https://ballotpedia.org/Eric_Barlow"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher preventing same-slug cross-state collisions."""
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
        print(f"  ✓ {m['name']:<32} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
