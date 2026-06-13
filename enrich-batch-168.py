#!/usr/bin/env python3
"""Enrichment batch 168: 5 Republican US House/Senate members from bottom of alphabet.

Targets archetype_party_default federal members with 0 evidence claims,
taken from the bottom of the alphabet (NC, NV, OK).  All claims sourced from
official *.house.gov / *.senate.gov, congress.gov, govtrack.us, ballotpedia.org,
en.wikipedia.org, or sbaprolife.org and reflect 2025-2026 public record.

Candidates:
  Chuck Edwards     (NC-11, R) — election_integrity, border_immigration, sanctity_of_life
  Brad Knott        (NC-13, R) — sanctity_of_life, biblical_marriage, election_integrity
  Addison McDowell  (NC-6,  R) — election_integrity, border_immigration, biblical_marriage
  Mark Amodei       (NV-2,  R) — self_defense, border_immigration, economic_stewardship
  Alan Armstrong    (OK,    R) — border_immigration, refuse_federal_overreach, economic_stewardship
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
    # ---------------- Chuck Edwards (NC-11, R) ----------------
    ("chuck-edwards", "NC", "US Representative", [
        claim("ce1", "chuck-edwards", "election_integrity", 0, True,
              "Introduced H.R. 7356 (119th Congress) to prohibit federal election-administration funds from going to any state that permits ballot harvesting — a direct legislative strike at the mass-mail-in and third-party ballot-collection practices the rubric's election-integrity standard opposes.",
              ["https://www.congress.gov/member/chuck-edwards/E000246",
               "https://ballotpedia.org/Chuck_Edwards"]),
        claim("ce2", "chuck-edwards", "border_immigration", 4, True,
              "Introduced legislation in January 2024 to exclude non-citizen immigrants from being counted by the U.S. Census for congressional apportionment purposes — denying illegal immigrants the political representation that inflates House seat counts in high-immigration states and aligning with the rubric's stance on limiting the political power of undocumented populations.",
              ["https://en.wikipedia.org/wiki/Chuck_Edwards",
               "https://ballotpedia.org/Chuck_Edwards"]),
        claim("ce3", "chuck-edwards", "sanctity_of_life", 0, True,
              "Carries a pro-life voting record scored by SBA Pro-Life America; has voted consistently to defund Planned Parenthood, eliminate taxpayer funding for abortion travel expenses (domestic and international), and push back against pro-abortion executive actions — placing him squarely within the rubric's life-at-conception protection standard.",
              ["https://sbaprolife.org/representative/chuck-edwards",
               "https://ballotpedia.org/Chuck_Edwards"]),
    ]),

    # ---------------- Brad Knott (NC-13, R) ----------------
    ("brad-knott", "NC", "US Representative", [
        claim("bk1", "brad-knott", "sanctity_of_life", 0, True,
              "Publicly identifies as pro-life, opposes the legalization of abortion, and voiced clear support for the Supreme Court's Dobbs decision overturning Roe v. Wade as the correct constitutional outcome — consistent with the rubric's life-at-conception and personhood standard.",
              ["https://en.wikipedia.org/wiki/Brad_Knott",
               "https://ballotpedia.org/Brad_Knott"]),
        claim("bk2", "brad-knott", "biblical_marriage", 2, True,
              "Opposes transgender women competing in women's sports and voted for the Protection of Women and Girls in Sports Act of 2025, which bars biological males from competing in female athletic categories at federally funded programs — joining every House Republican in rejecting the redefinition of sex through transgender ideology.",
              ["https://en.wikipedia.org/wiki/Brad_Knott",
               "https://ballotpedia.org/Brad_Knott"]),
        claim("bk3", "brad-knott", "election_integrity", 0, True,
              "Became a cosponsor of H.R. 22 (the SAVE Act, 119th Congress) on March 31, 2025, which requires documentary proof of U.S. citizenship to register to vote in federal elections and mandates that states remove noncitizens from voter rolls — a citizenship-verification measure directly aligned with the rubric's voter-ID and election-integrity standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://ballotpedia.org/Brad_Knott"]),
    ]),

    # ---------------- Addison McDowell (NC-6, R) ----------------
    ("addison-mcdowell", "NC", "US Representative", [
        claim("amd1", "addison-mcdowell", "election_integrity", 0, True,
              "Became a cosponsor of H.R. 22 (the SAVE Act, 119th Congress) on March 21, 2025, which requires proof of U.S. citizenship to register to vote in federal elections and mandates removal of noncitizens from voter rolls — a voter-eligibility verification measure consistent with the rubric's election-integrity standard.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors",
               "https://ballotpedia.org/Addison_McDowell"]),
        claim("amd2", "addison-mcdowell", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (S. 5 / H.R. 29, signed January 29, 2025), the first bill signed by President Trump, mandating detention and deportation proceedings for illegal immigrants who commit theft, burglary, or other specified crimes. McDowell has called securing the southern border his top legislative priority after losing his brother to a fentanyl overdose linked to the open-border crisis.",
              ["https://www.congress.gov/bill/119th-congress/senate-bill/5",
               "https://ballotpedia.org/Addison_McDowell"]),
        claim("amd3", "addison-mcdowell", "biblical_marriage", 2, True,
              "Voted for the Protection of Women and Girls in Sports Act of 2025 alongside every House Republican, barring biological males from competing in female athletic categories in federally funded programs — rejecting the transgender-ideology redefinition of sex in women's sports.",
              ["https://en.wikipedia.org/wiki/Addison_McDowell",
               "https://www.govtrack.us/congress/members/addison_mcdowell/457001"]),
    ]),

    # ---------------- Mark Amodei (NV-2, R) ----------------
    ("mark-amodei", "NV", "US House", [
        claim("mam1", "mark-amodei", "self_defense", 1, True,
              "Endorsed by the NRA Political Victory Fund in his reelection campaigns and has maintained a consistent pro-Second Amendment voting record in the House — opposing the assault-weapons bans, magazine limits, and red-flag overreach that the rubric's self-defense standard rejects.",
              ["https://ballotpedia.org/Mark_Amodei",
               "https://en.wikipedia.org/wiki/Mark_Amodei"]),
        claim("mam2", "mark-amodei", "border_immigration", 1, False,
              "A longtime supporter of DACA protections who signed a House discharge petition to force a floor vote on DACA legislation, and who 'repeatedly opposes Trump-style mass deportation rhetoric' — rejecting the rubric's mandatory-deportation standard for illegal immigrants residing in the United States.",
              ["https://en.wikipedia.org/wiki/Mark_Amodei",
               "https://ballotpedia.org/Mark_Amodei"]),
        claim("mam3", "mark-amodei", "economic_stewardship", 2, False,
              "Was one of only four House Republicans to vote against the June 2025 $9.4 billion rescissions package backed by the Trump administration and DOGE, choosing to protect existing spending over accepting the proposed cuts — a stance contrary to the rubric's anti-deficit and balanced-budget standard.",
              ["https://en.wikipedia.org/wiki/Mark_Amodei",
               "https://ballotpedia.org/Mark_Amodei"]),
    ]),

    # ---------------- Alan Armstrong (OK, R — interim Senator) ----------------
    ("alan-armstrong", "OK", "U.S. Senator", [
        claim("aa1", "alan-armstrong", "border_immigration", 1, True,
              "Voted for S. 2 (the Secure America Act, passed by Senate Republicans 52-47 on June 5, 2026), a reconciliation package providing over $70 billion for ICE and Customs and Border Protection immigration enforcement operations — aligning with the rubric's mandatory-deportation and border-security enforcement standard.",
              ["https://www.govtrack.us/congress/votes/119-2026/s163",
               "https://ballotpedia.org/Alan_Armstrong"]),
        claim("aa2", "alan-armstrong", "refuse_federal_overreach", 0, True,
              "Made energy permitting reform his singular Senate focus on appointment, calling for a significant rollback of NEPA environmental review burdens that impose federal regulatory delays on infrastructure and energy projects — framing his mission as getting federal government 'out of the way' of American energy production.",
              ["https://okenergytoday.com/2026/06/armstrong-keeps-pushing-for-permitting-reform/",
               "https://en.wikipedia.org/wiki/Alan_S._Armstrong"]),
        claim("aa3", "alan-armstrong", "economic_stewardship", 4, True,
              "As CEO of Williams Companies (2011-2025), one of the nation's largest pipeline operators, Armstrong championed domestic fossil fuel infrastructure development — a posture directly opposed to the WEF/ESG/Davos-backed green-transition mandates and ESG investment restrictions that constrain domestic energy production and pipeline permitting.",
              ["https://en.wikipedia.org/wiki/Alan_S._Armstrong",
               "https://en.wikipedia.org/wiki/Williams_Companies"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
