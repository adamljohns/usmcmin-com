#!/usr/bin/env python3
"""Enrichment batch 301: hand-curated claims for 4 R legislators.

Primary archetype_curated federal-senator bucket is exhausted; batch pivots to
the next-best available targets from the bottom of the alphabet with 0 claims:
Steve Toth (TX, 2026 TX-02 R nominee / sitting TX State Rep),
Patricia Rucker (WV State Senator), Steve Nass (WI State Senator),
Van Wanggaard (WI State Senator).

Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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


# Each entry: (slug, state, office_keyword, claims-list)
TARGETS = [
    # ---------------- Steve Toth (TX, TX State Rep / 2026 TX-02 nominee) ----------------
    ("steve-toth", "TX", "Representative", [
        claim("st1", "steve-toth", "sanctity_of_life", 0, True,
              "A consistent pro-life Texas legislator: co-authored HB 1500 (the Heartbeat Protection Act, banning abortion after fetal heartbeat detection) and HB 896 to prohibit abortion outright; cosponsored SB 22, signed into law in June 2019, cutting all government funding to Planned Parenthood. Running for U.S. House TX-02 in 2026 as the R nominee having defeated incumbent Dan Crenshaw, he has declared his intent to join the House Freedom Caucus.",
              ["https://en.wikipedia.org/wiki/Steve_Toth",
               "https://ballotpedia.org/Steve_Toth"]),
        claim("st2", "steve-toth", "self_defense", 1, True,
              "Authored the Texas Firearm Protection Act (HB 112, 87th session), a Second Amendment sanctuary bill that would void any attempt to enforce federal gun laws in Texas not also enacted under Texas law — directly opposing federal firearm bans, registries, and restrictions. A companion bill, HB 2622, passed both chambers and was signed by Gov. Abbott on June 17, 2021.",
              ["https://en.wikipedia.org/wiki/Steve_Toth",
               "https://ballotpedia.org/Steve_Toth"]),
        claim("st3", "steve-toth", "border_immigration", 0, True,
              "As a member of the Texas House Appropriations Committee, Toth fought to appropriate billions of dollars for finishing the border wall and critical border security initiatives, explicitly opposing Democrats and moderate Republicans who sought to defund border construction — a record consistent with the rubric's wall-plus-military border standard.",
              ["https://ballotpedia.org/Steve_Toth",
               "https://news.ballotpedia.org/2026/03/04/steve-toth-r-defeated-incumbent-daniel-crenshaw-r-martin-etwop-r-and-nicholas-plumb-r-in-the-republican-primary-for-texas-2nd-congressional-district/"]),
    ]),

    # ---------------- Patricia Rucker (WV State Senator, District 16) ----------------
    ("patricia-rucker", "WV", "Senator", [
        claim("pr1", "patricia-rucker", "sanctity_of_life", 0, True,
              "Sponsored West Virginia SB 735 (2024) to prohibit the use or sale of abortifacients and impose criminal penalties and private causes of action against suppliers; also co-sponsored SB 246 addressing abortion restrictions. An affiliate of WV4Life, she has declared 'protecting life' a front-and-center Republican priority. WV enacted a near-total abortion ban in 2022 and Rucker has continued pressing life-affirming legislation each session.",
              ["https://www.wvlegislature.gov/Bill_Status/bills_text.cfm?billdoc=sb735+intr.htm&yr=2024&sesstype=RS&i=735",
               "https://en.wikipedia.org/wiki/Patricia_Rucker",
               "https://ballotpedia.org/Patricia_Rucker"]),
        claim("pr2", "patricia-rucker", "family_child_sovereignty", 0, True,
              "A homeschooling mother who served as chairwoman of the West Virginia Senate Education Committee (2019–2022), where she championed parental rights in education and opposed government overreach in schooling decisions. Her personal commitment to homeschooling and her tea-party roots inform her consistent advocacy for family sovereignty over educational choices against government and teachers-union control.",
              ["https://en.wikipedia.org/wiki/Patricia_Rucker",
               "https://ballotpedia.org/Patricia_Rucker"]),
    ]),

    # ---------------- Steve Nass (WI State Senator, District 11) ----------------
    ("steve-nass", "WI", "Senator", [
        claim("sn1", "steve-nass", "sanctity_of_life", 0, True,
              "Consistent pro-life legislator across three decades: sponsored WI SB 384 (2025) on born-alive infant protection requirements; earlier sponsored SB 175 (2019, born-alive), SB 173 (2019, ban on sex-selective and disability-selective abortions), and SB 174 (2019, informed-consent requirements for abortion-inducing drug regimens) — a sustained legislative record affirming the value of life from conception.",
              ["https://en.wikipedia.org/wiki/Stephen_Nass",
               "https://ballotpedia.org/Stephen_Nass",
               "https://docs.legis.wisconsin.gov/2025/legislators/senate/2822"]),
        claim("sn2", "steve-nass", "family_child_sovereignty", 0, True,
              "Sponsored WI legislation on rights reserved to parents and guardians; championed dramatically expanding all school choice programs to 'empower parents over teachers' unions'; pushed to restore in-person schooling and expand parental choice during and after the COVID-era school closures. Described as a fierce opponent of 'liberal indoctrination' in the University of Wisconsin System.",
              ["https://en.wikipedia.org/wiki/Stephen_Nass",
               "https://legis.wisconsin.gov/senate/11/nass/meet-steve/"]),
        claim("sn3", "steve-nass", "industry_capture", 0, True,
              "Moved to block University of Wisconsin System COVID-19 vaccine and mask mandates through the Joint Committee for Review of Administrative Rules (JCRAR), forcing the UW System to issue an emergency rule before imposing mandates; advocated to 'prohibit the excessive powers of both state and local public health bureaucrats' — directly opposing the pharma/government mandate apparatus the rubric flags under industry capture.",
              ["https://en.wikipedia.org/wiki/Stephen_Nass",
               "https://legis.wisconsin.gov/senate/11/nass/media/eupdates/The-Nass-Report-August-3-2021.html"]),
    ]),

    # ---------------- Van Wanggaard (WI State Senator, District 21) ----------------
    ("van-wanggaard", "WI", "Senator", [
        claim("vw1", "van-wanggaard", "self_defense", 0, True,
              "A 29-year Racine Police Department veteran who has made constitutional carry a signature legislative priority, publicly pledging to 'Continue to fight for Constitutional Carry with an optional permit for reciprocity purposes' and to 'Fight all efforts to restrict your 2nd Amendment rights.' As WI Senate Majority Caucus Chair, he has championed Second Amendment legislation throughout his tenure.",
              ["https://en.wikipedia.org/wiki/Van_H._Wanggaard",
               "https://legis.wisconsin.gov/senate/21/wanggaard/"]),
        claim("vw2", "van-wanggaard", "election_integrity", 0, True,
              "The lead Senate author of Wisconsin's voter photo ID constitutional amendment (Senate Joint Resolution 2, passed the legislature and approved by voters as Wisconsin Question 1 in April 2025), which permanently enshrines photo ID requirements to vote in the state constitution. Testified that 81% of Americans support voter ID and that the requirement is needed to ensure only eligible voters cast ballots.",
              ["https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://docs.legis.wisconsin.gov/misc/lc/hearing_testimony_and_materials/2025/sjr2/sjr0002_2025_01_07.pdf"]),
        claim("vw3", "van-wanggaard", "sanctity_of_life", 0, True,
              "Sponsored WI SB 384 (2025) on born-alive infant protection requirements, SB 61 (prior session, same born-alive subject), and SB 299 (clarification of medical necessity for abortion), reflecting a consistent anti-abortion legislative record. As Majority Caucus Chair he has used his leadership position to advance life-affirming bills in the Wisconsin Senate.",
              ["https://docs.legis.wisconsin.gov/2025/legislators/senate/2832",
               "https://ballotpedia.org/Van_Wanggaard"]),
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
