#!/usr/bin/env python3
"""Enrichment batch 345: 4 bottom-of-alphabet federal Senate/House candidates.

Targets (WY / RI / VT / OK — bottom-of-alphabet sweep):
  Scott Morrow       (WY-D, 2026 U.S. Senate challenger)   — 1 new claim
  Allen Waters       (RI-R, 2026 U.S. Senate candidate)    — 2 new claims
  Becca Balint       (VT-D, sitting U.S. Representative)   — 2 new claims
  N'Kiyla Jasmine Thomas (OK-D, 2026 U.S. Senate candidate)— 2 new claims

Categories: border_immigration, economic_stewardship, biblical_marriage, self_defense.

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
    # ---------- Scott Morrow (WY-D, 2026 U.S. Senate challenger) ----------
    # Existing: sanctity_of_life[0]F, economic_stewardship[2]F, biblical_marriage[2]F
    ("scott-morrow-wy-senate", "WY", "Senate", [
        claim("sm4", "scott-morrow-wy-senate", "border_immigration", 0, False,
              "In his WyoFile 2024 Election Guide Q&A, Morrow dismissed the southern border as 'really "
              "a non issue,' adding that 'the hyperbole of my friends and associates on the right about "
              "the border are not really a huge issue and are made up to simply have a political agenda "
              "to whine about.' He further noted that the only undocumented workers he had ever observed "
              "in Wyoming 'were roofers next door on Spring Creek back during the George Bush Era.' His "
              "position categorically rejects the rubric's wall-and-military-at-the-border standard as "
              "nothing more than manufactured political grievance.",
              ["https://projects.wyofile.com/election-guide-2024/candidates/scott-morrow/",
               "https://ballotpedia.org/Scott_Morrow_(Wyoming)"]),
    ]),

    # ---------- Allen Waters (RI-R, 2026 U.S. Senate candidate) ----------
    # Existing: sanctity_of_life[0]T, border_immigration[1]T, self_defense[1]T
    ("allen-waters-ri-senate", "RI", "Senate", [
        claim("aw4", "allen-waters-ri-senate", "economic_stewardship", 2, True,
              "Waters signed the Americans for Tax Reform (ATR) Taxpayer Protection Pledge, making a "
              "written commitment to oppose any and all income tax increases if elected to Congress. He "
              "explicitly supports a Balanced Budget Amendment to the U.S. Constitution via a Convention "
              "of States to 'force politicians on both sides of the aisle to live within their means,' "
              "noting that it costs America '$1,000,000,000,000 just to service the interest expense' "
              "on the national debt. He also supports the Fair Tax Act (HR 25) to close the IRS and "
              "replace the federal income tax — consistent with the rubric's anti-deficit/balanced-"
              "budget standard.",
              ["https://www.atr.org/atr-commends-allen-waters-for-signing-the-taxpayer-protection-pledge-in-rhode-island/",
               "https://rhodeislandcurrent.com/2026/02/12/instead-of-running-for-congress-allen-waters-launches-providence-mayoral-bid-as-an-independent/"]),
        claim("aw5", "allen-waters-ri-senate", "biblical_marriage", 0, False,
              "In a 2026 campaign statement, Waters' spokesperson confirmed he is 'an individual-rights "
              "absolutist who believes every adult, gay or straight, has the absolute right to live and "
              "love exactly as they choose' — a position explicitly embracing same-sex relationships as "
              "equal to opposite-sex ones and rejecting the one-man-one-woman definition of marriage the "
              "rubric's biblical_marriage standard requires. Waters made the statement in the context of "
              "his campaign after controversy arose over a Facebook post about the race; his campaign's "
              "formal response affirmed his libertarian stance on LGBTQ relationships as a settled "
              "political principle.",
              ["https://rhodeislandcurrent.com/2026/02/12/instead-of-running-for-congress-allen-waters-launches-providence-mayoral-bid-as-an-independent/",
               "https://ballotpedia.org/Allen_Waters"]),
    ]),

    # ---------- Becca Balint (VT-D, U.S. Representative at-large) ----------
    # Existing: sanctity_of_life[0]F, biblical_marriage[0]F, biblical_marriage[2]F
    ("becca-balint", "VT", "Representative", [
        claim("bb4", "becca-balint", "self_defense", 1, False,
              "As a U.S. Representative in the 118th Congress, Balint co-sponsored H.R. 698 (Assault "
              "Weapons Ban of 2023), legislation that would ban the manufacture, sale, transfer, and "
              "importation of semi-automatic assault-style rifles and high-capacity ammunition magazines. "
              "Her co-sponsorship directly opposes the rubric's self_defense standard of opposing "
              "assault-weapons bans and magazine-capacity restrictions. This follows her record as "
              "Vermont State Senate Majority Leader where she led passage of the state's first gun-"
              "safety laws.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/698",
               "https://www.govtrack.us/congress/bills/118/hr698"]),
        claim("bb5", "becca-balint", "border_immigration", 0, False,
              "On May 11, 2023, Balint voted NAY on H.R. 2 (Secure the Border Act of 2023), which "
              "would have resumed construction of a physical barrier on the southern border, expanded "
              "Border Patrol and ICE staffing, reimposed 'Remain in Mexico' (MPP) policies, and tightened "
              "asylum eligibility standards. The bill passed 219-213 with nearly all Democrats voting "
              "against. Her vote directly contradicts the rubric's wall-and-military-at-the-border "
              "standard.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://www.congress.gov/member/becca-balint/B001318"]),
    ]),

    # ---------- N'Kiyla Jasmine Thomas (OK-D, 2026 U.S. Senate candidate) ----------
    # Existing: sanctity_of_life[0]F, biblical_marriage[0]F, biblical_marriage[4]F
    ("nkiyla-jasmine-thomas", "OK", "Senator", [
        claim("njt4", "nkiyla-jasmine-thomas", "border_immigration", 2, False,
              "Thomas explicitly calls for 'abolishing ICE and replacing it with humane immigration "
              "policy that honors human rights' — a pro-sanctuary stance that rejects federal interior "
              "enforcement cooperation and is directly contrary to the rubric's anti-sanctuary standard. "
              "She also supports granting driver's licenses to undocumented residents and creating a "
              "pathway to legal residency — positions that normalize the presence of unlawfully present "
              "individuals rather than enforcing existing law.",
              ["https://www.jasmineforok.com/policies",
               "https://ballotpedia.org/N'Kiyla_Thomas"]),
        claim("njt5", "nkiyla-jasmine-thomas", "economic_stewardship", 2, False,
              "Thomas campaigns on making healthcare 'more affordable' through federal expansion and "
              "putting 'people over profits,' explicitly prioritizing increased government spending on "
              "healthcare and social services. Her platform contains no commitment to deficit reduction, "
              "balanced-budget enforcement, or spending restraint — her stated agenda requires increased "
              "federal outlays without any offsetting fiscal discipline, contrary to the rubric's "
              "anti-deficit/balanced-budget standard.",
              ["https://www.jasmineforok.com/about",
               "https://ballotpedia.org/N'Kiyla_Thomas"]),
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
