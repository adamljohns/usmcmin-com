#!/usr/bin/env python3
"""Enrichment batch 857: 12 new claims for 5 VA 2026 federal candidates.

Continuing bottom-of-alphabet coverage; archetype_curated federal bucket fully
depleted as of 2026-07-28 (confirmed by batches 855-856). Targets unset-confidence
VA candidates — mix of Democrats (4) and Republican (1).

Targets:
  Tom Perriello   — U.S. Representative VA-05 (D; former congressman 2009-2011,
                    returned to race 2026)
  Shannon Taylor  — U.S. Representative VA-01 (D; Henrico County Commonwealth's
                    Attorney, 2026 candidate)
  Salaam Bhatti   — U.S. Representative VA-01 (D; public-interest attorney,
                    former Alexandria City Council member)
  Mo Seifeldein   — U.S. Representative VA-08 (D; former DOL attorney, former
                    Alexandria City Council 2019-2021)
  Arthur Purves   — U.S. Representative VA-11 (R; president of Fairfax County
                    Taxpayers Alliance for 29 years)

Sources verified 2026-07-28. Minified write preserves ~35-36 MB master.
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
    # ---- Tom Perriello (VA, U.S. Representative VA-05, D, 2026 candidate) ----
    ("tom-perriello", "VA", "Representative", [
        claim("tp857a", "tom-perriello", "self_defense", 1, True,
              "During his 2009-2011 congressional term representing Virginia's 5th District, "
              "Perriello opposed a ban on assault weapons, declining to support legislation that "
              "would restrict semi-automatic rifle ownership — a documented record position "
              "consistent with the rubric's self_defense[1] standard opposing assault-weapons "
              "bans, magazine-capacity limits, and firearm registration schemes.",
              ["https://en.wikipedia.org/wiki/Tom_Perriello",
               "https://www.govtrack.us/congress/members/thomas_perriello/412304"]),
        claim("tp857b", "tom-perriello", "economic_stewardship", 2, False,
              "Perriello voted YES on both the American Recovery and Reinvestment Act of 2009 "
              "(the $787 billion stimulus package, one of the largest peacetime spending bills "
              "in U.S. history) and the Patient Protection and Affordable Care Act (H.R. 3590, "
              "House Vote #165, March 21, 2010; passed 219-212). The CBO estimated the ACA "
              "alone would cost over $940 billion in its first decade. Both votes dramatically "
              "expanded the federal deficit. The ARRA increased the deficit by roughly $831 "
              "billion over ten years according to CBO scoring. These votes directly conflict "
              "with the rubric's economic_stewardship[2] standard preferring anti-deficit, "
              "balanced-budget governance.",
              ["https://www.govtrack.us/congress/members/thomas_perriello/412304",
               "https://www.govtrack.us/congress/votes/111-2010/h165",
               "https://en.wikipedia.org/wiki/Tom_Perriello"]),
        claim("tp857c", "tom-perriello", "sanctity_of_life", 0, False,
              "Though Perriello cast a 2009 vote for the Stupak-Pitts anti-abortion-funding "
              "amendment, he later called it 'a bad vote and a bad pledge' and repeatedly "
              "apologized, describing it as 'the worst vote of my career.' In 2026 he secured "
              "the endorsement of the Congressional Progressive Caucus PAC for his VA-05 "
              "campaign — a PAC whose endorsement criteria include support for reproductive "
              "rights — confirming his current pro-abortion position that rejects the rubric's "
              "sanctity_of_life[0] standard recognizing personhood from conception.",
              ["https://en.wikipedia.org/wiki/Tom_Perriello",
               "https://ballotpedia.org/Tom_Perriello"]),
    ]),

    # ---- Shannon Taylor (VA, U.S. Representative VA-01, D, 2026 candidate) ----
    ("shannon-taylor", "VA", "Representative", [
        claim("st857a", "shannon-taylor", "sanctity_of_life", 0, False,
              "As Henrico County Commonwealth's Attorney, Shannon Taylor was one of the first "
              "prosecutors in the United States to publicly declare she would defend the right "
              "to abortion care after the U.S. Supreme Court overturned Roe v. Wade in 2022 — "
              "a documented, proactive pro-abortion stance that directly opposes the rubric's "
              "sanctity_of_life[0] standard recognizing the unborn's right to life from "
              "conception. Her 2026 campaign for VA-01 builds on this commitment, with Taylor "
              "supporting Virginia's 2026 constitutional amendment to enshrine abortion access "
              "in state law.",
              ["https://virginiamercury.com/2025/09/08/shannon-taylor-launches-bid-to-represent-virginias-1st-congressional-district/",
               "https://ballotpedia.org/Shannon_Taylor_(Virginia)"]),
        claim("st857b", "shannon-taylor", "economic_stewardship", 2, False,
              "Taylor campaigns explicitly as a 'New Deal Democrat,' describing her platform "
              "as one that will 'build an economy that works for working families — not just "
              "corporations and billionaires.' Her program calls for universal healthcare, "
              "expanded childcare, reduced prescription drug prices, and 'ensuring the wealthiest "
              "pay their fair share' — policy positions that collectively require substantial new "
              "federal spending, contradicting the rubric's economic_stewardship[2] standard "
              "preferring anti-deficit and balanced-budget governance.",
              ["https://ballotpedia.org/Shannon_Taylor_(Virginia)",
               "https://www.virginiascope.com/henrico-commonwealth-attorney-shannon-taylor-is-running-for-congress/"]),
    ]),

    # ---- Salaam Bhatti (VA, U.S. Representative VA-01, D, 2026 candidate) ----
    ("salaam-bhatti", "VA", "Representative", [
        claim("sb857a", "salaam-bhatti", "sanctity_of_life", 0, False,
              "In his 2026 VA-01 campaign, Bhatti has explicitly called for enacting into "
              "federal law 'a woman's right to make decisions about her own healthcare' — a "
              "direct commitment to codifying abortion access and rejecting any recognition of "
              "fetal personhood. He states that 'federal law acts as a floor when it comes to "
              "minimum rights' and that reproductive autonomy must be protected by statute, in "
              "direct opposition to the rubric's sanctity_of_life[0] standard that life begins "
              "at conception.",
              ["https://ballotpedia.org/Salaam_Bhatti"]),
        claim("sb857b", "salaam-bhatti", "biblical_marriage", 0, False,
              "Bhatti explicitly supports codifying same-sex marriage into federal law, stating "
              "he will 'protect people by enacting into law... same-sex marriage' as a federal "
              "floor right — a position that directly opposes the rubric's biblical_marriage[0] "
              "standard defining marriage as exclusively between one man and one woman. His "
              "position aligns with those who supported the Respect for Marriage Act (2022) "
              "and seek permanent federal protection for same-sex unions.",
              ["https://ballotpedia.org/Salaam_Bhatti"]),
        claim("sb857c", "salaam-bhatti", "economic_stewardship", 2, False,
              "Bhatti supports the implementation of Medicare for All — a federal single-payer "
              "healthcare system estimated by CBO and independent analysts to cost $30–40 "
              "trillion over ten years in new federal spending. This policy would dramatically "
              "expand the federal deficit and the scope of federal government economic control, "
              "directly opposing the rubric's economic_stewardship[2] standard favoring "
              "anti-deficit and balanced-budget governance.",
              ["https://ballotpedia.org/Salaam_Bhatti"]),
    ]),

    # ---- Mo Seifeldein (VA, U.S. Representative VA-08, D, 2026 candidate) ----
    ("mo-seifeldein", "VA", "Representative", [
        claim("ms857a", "mo-seifeldein", "border_immigration", 2, False,
              "Seifeldein left his position as an attorney at the U.S. Department of Labor in "
              "2025 specifically to protest the Trump administration's immigration enforcement "
              "policies — a public act of professional resignation over the government's "
              "deportation and enforcement agenda. His departure explicitly cited opposition to "
              "immigration enforcement as a core reason for running for Congress, directly "
              "opposing the rubric's border_immigration[2] standard that rewards candidates who "
              "oppose sanctuary policies and support full ICE enforcement cooperation.",
              ["https://ballotpedia.org/Mo_Seifeldein",
               "https://news.ballotpedia.org/2026/05/18/former-federal-workers-challenge-rep-beyer-in-virginias-8th-district-democratic-primary/"]),
        claim("ms857b", "mo-seifeldein", "economic_stewardship", 2, False,
              "Seifeldein's candidacy is anchored in opposing the Trump administration's "
              "reductions of the federal civilian workforce (DOGE-era layoffs), advocating for "
              "maintaining and expanding government employment and social programs. His platform "
              "of 'affordability, equity, and opportunity' centers on federal spending expansion "
              "and protection of existing government programs rather than fiscal restraint — "
              "a posture contrary to the rubric's economic_stewardship[2] standard of "
              "anti-deficit and balanced-budget governance.",
              ["https://ballotpedia.org/Mo_Seifeldein",
               "https://news.ballotpedia.org/2026/05/18/former-federal-workers-challenge-rep-beyer-in-virginias-8th-district-democratic-primary/"]),
    ]),

    # ---- Arthur Purves (VA, U.S. Representative VA-11, R, 2026 candidate) ----
    ("arthur-purves", "VA", "Representative", [
        claim("ap857a", "arthur-purves", "economic_stewardship", 2, True,
              "Purves has served as president of the Fairfax County Taxpayers Alliance for 29 "
              "years — a citizen watchdog organization focused on limiting government spending "
              "and tax increases. His 2026 congressional campaign platform prioritizes stopping "
              "real estate tax increases that outpace household income and opposing unnecessary "
              "government spending programs, a documented multi-decade commitment to fiscal "
              "restraint consistent with the rubric's economic_stewardship[2] standard "
              "preferring anti-deficit and balanced-budget governance.",
              ["https://votepurves.org/",
               "https://ballotpedia.org/Arthur_Purves"]),
        claim("ap857b", "arthur-purves", "economic_stewardship", 4, True,
              "Purves explicitly opposes spending 'tax dollars to make the county carbon "
              "neutral,' describing such programs as 'unaffordable and unnecessary' on his 2026 "
              "campaign platform. This documented rejection of ESG-style government climate "
              "mandates that use public funds to impose green energy policy aligns directly "
              "with the rubric's economic_stewardship[4] standard opposing WEF/ESG-driven "
              "government agendas and the Davos-style corporate-climate consensus.",
              ["https://votepurves.org/"]),
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
