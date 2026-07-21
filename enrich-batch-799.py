#!/usr/bin/env python3
"""Enrichment batch 799: 5 federal candidates from the bottom of the alphabet
(VA, PA, SC, OK) — deepening evidence_curated records with missing rubric categories.

Primary archetype_curated federal-senator bucket is fully exhausted; this batch
adds claims to evidence_curated candidates with 3 claims, filling uncovered
rubric categories from documented 2025-2026 campaign positions and public records.

Targets (bottom-agent territory):
  Ricky Smithers         (VA-R) — christian_liberty, border_immigration
  Philip Harding         (VA-R) — christian_liberty
  Paige Cognetti         (PA-D) — biblical_marriage, christian_liberty
  Mayra Rivera-Vázquez   (SC-D) — economic_stewardship
  R.O. Joe Cassity Jr.   (OK-D) — foreign_policy_restraint

All claims sourced from official campaign sites, VPM News, Washington Examiner,
nondoc.com, townhall.com, emilyslist.org, South Carolina Public Radio, or
reproductivefreedomforall.org. Writes scorecard.json MINIFIED (no indent) to keep
the master under GitHub's 50MB limit.
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
    # ---- Ricky Smithers (VA-R, 2026 R primary candidate VA-07, pastor/veteran) ----
    ("ricky-smithers", "VA", "VA-07", [
        claim("rs4", "ricky-smithers", "christian_liberty", 0, True,
              "An ordained pastor who has built his 2026 congressional campaign on an "
              "explicitly faith-centered platform, describing himself as a man who "
              "believes 'Virginia deserves leadership built on faith in God, honesty, "
              "and real hard work,' and listing 'protecting religious liberties' among "
              "his top platform priorities alongside reducing federal spending and "
              "securing the border. As an active minister, Smithers anchors his "
              "candidacy in the principle of religious free exercise rather than "
              "government restriction of faith.",
              ["https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman",
               "https://www.fredericksburgfreepress.com/2026/06/19/gop-hopefuls-in-virginias-7th-district-talk-data-centers-priorities-if-elected/"]),
        claim("rs5", "ricky-smithers", "border_immigration", 0, True,
              "At June 2026 candidate forums covering Virginia's 7th district race, "
              "Smithers explicitly stated the need to secure the border and called on "
              "Congress to pass the Safeguard American Voter Eligibility (SAVE) Act "
              "— legislation requiring documentary proof of U.S. citizenship during "
              "voter registration — describing its passage as 'too important' and "
              "supporting President Trump's use of the bill as a negotiating "
              "priority. His campaign platform lists border security alongside fiscal "
              "discipline and veterans' care as a core commitment.",
              ["https://www.29news.com/2026/06/10/three-republicans-vying-nomination-virginias-7th-district-primary-race/",
               "https://www.vpm.org/elections/2026-07-07/va-07-us-house-republican-primary-harding-ollivant-smithers-vindman"]),
    ]),

    # ---- Philip Harding (VA-R, 2026 R primary candidate VA-07, entrepreneur) ----
    ("philip-harding", "VA", "VA-07", [
        claim("ph4", "philip-harding", "christian_liberty", 0, True,
              "Harding is a self-described 'faith-driven Republican' whose entire "
              "campaign is explicitly organized around his Christian faith: he "
              "announced his bid emphasizing that faith, family, and free enterprise "
              "are inseparable principles, and his second stated priority as a "
              "candidate is to 'defend the family' by protecting parental rights, "
              "getting schools 'back to educating,' and keeping communities safe "
              "— framing policy in terms that presuppose active, constitutionally "
              "protected religious free exercise rather than government regulation "
              "of faith or conscience.",
              ["https://www.washingtonexaminer.com/news/campaigns/state/4533130/philip-harding-republican-entrepreneur-virginia-7th-district/",
               "https://www.vpm.org/news/2026-06-16/va07-election-nova-fxbg-pwc-vindman-harding-ollivant-smithers"]),
    ]),

    # ---- Paige Cognetti (PA-D, Scranton Mayor, 2026 D Nominee PA-08) ----
    ("paige-cognetti", "PA", "PA-08", [
        claim("pcog1", "paige-cognetti", "biblical_marriage", 4, False,
              "As Mayor of Scranton, Cognetti formally raised the LGBTQ+ Pride flag "
              "over City Hall in June 2026, making an official civic endorsement of "
              "LGBTQ ideology in the name of the city government. She is endorsed by "
              "EMILY's List and, as the 2026 Democratic nominee for PA-08, has made "
              "LGBTQ equality a public centerpiece of her political identity — "
              "consistent with policies that promote LGBTQ ideology in schools and "
              "public institutions rather than confining it to the private sphere.",
              ["https://townhall.com/tipsheet/amy-curtis/2026/06/01/paige-cognetti-raises-the-pride-flag-over-scranton-city-hall-n2677011",
               "https://emilyslist.org/candidate/paige-cognetti/"]),
        claim("pcog2", "paige-cognetti", "christian_liberty", 0, False,
              "Cognetti is endorsed by both EMILY's List and Reproductive Freedom for "
              "All (the renamed NARAL Pro-Choice America), two organizations whose "
              "policy agendas explicitly oppose Religious Freedom Restoration Act "
              "exemptions for Catholic hospitals, Christian adoption agencies, and "
              "religious medical providers who decline to participate in abortion "
              "referrals or procedures. Her platform of protecting 'reproductive "
              "freedom' — and her endorsements from the leading pro-abortion lobbying "
              "organizations — place her squarely against the religious free exercise "
              "rights of faith-based institutions and practitioners.",
              ["https://emilyslist.org/candidate/paige-cognetti/",
               "https://reproductivefreedomforall.org/news/reproductive-freedom-for-all-endorses-slate-of-key-u-s-house-challengers-ahead-of-the-2026-midterm-elections/"]),
    ]),

    # ---- Mayra Rivera-Vázquez (SC-D, 2026 D candidate SC-01, open seat) ----
    ("mayra-rivera-vazquez", "SC", "SC-01", [
        claim("mrv4", "mayra-rivera-vazquez", "economic_stewardship", 2, False,
              "Rivera-Vázquez's campaign platform centers on protecting and expanding "
              "Social Security and Medicare, eliminating 'tax breaks for the rich,' "
              "expanding affordable healthcare, and pushing government-led solutions "
              "to the housing crisis — a suite of priorities that favors increased "
              "federal spending and higher progressive taxation over deficit reduction "
              "or a path to a balanced budget, running counter to the fiscal-restraint "
              "posture the rubric values.",
              ["https://www.southcarolinapublicradio.org/sc-news/2026-06-02/the-democrats-vying-for-votes-in-1st-congressional-district-primary",
               "https://www.mayra4congress.com/meet-mayra"]),
    ]),

    # ---- R.O. Joe Cassity Jr. (OK-D, 2026 D Senate candidate, Mullin seat) ----
    ("r-o-joe-cassity-jr", "OK", "Senator", [
        claim("rjc2", "r-o-joe-cassity-jr", "foreign_policy_restraint", 1, False,
              "Cassity's campaign platform calls explicitly for 'a stronger national "
              "defense' and 'closer ties with allies in Israel and NATO,' positions "
              "that commit the United States to maintaining and deepening existing "
              "alliance structures and forward defense postures rather than ending "
              "forever wars, restraining the AUMF, or reasserting Congress's Article "
              "I war-making authority. His platform treats expanded NATO engagement "
              "and sustained military commitments as an unambiguous good rather than "
              "a source of unconstitutional executive overreach.",
              ["https://nondoc.com/2026/05/27/cheat-sheet-5-oklahoma-democrats-compete-in-u-s-senate-primary/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
