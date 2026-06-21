#!/usr/bin/env python3
"""Enrichment batch 333: 4 WV State Senators from the bottom of the alphabet.

The archetype_curated federal senator/representative bucket is now exhausted;
this batch pivots to archetype_party_default state senators starting at the
bottom of the alphabet (WV = second in reverse alpha after WY for states
filtered here; WY senators already enriched by concurrent batches).

Targets (all WV-R): Mike Azinger (D3), Randy E. Smith (D14, Senate President),
Mike Oliverio (D13), Patrick Martin (D12, Majority Leader).
Each holds a documented 2024-2026 public record supporting the rubric.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub 50MB limit.
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
    # ---------- Mike Azinger (WV-R, District 3, State Senator) ----------
    ("mike-azinger", "WV", "State Senator", [
        claim("az1", "mike-azinger", "christian_liberty", 0, True,
              "Lead Senate sponsor of West Virginia's 'In God We Trust' legislation requiring the national motto to be displayed in every public school and university classroom. The bill passed the WV Senate 33-1 in 2025 (and cleared the Senate in 2024 as well, then the House). Azinger, who holds a Master of Pastoral Theology, explicitly cited Christian conviction as his motive: 'The reason first that I love it... is because it has God in it. I think that we've removed God from the culture. We've removed God from the schools.'",
              ["https://wvmetronews.com/2025/03/12/in-god-we-trust-gets-another-run-in-the-legislature/",
               "https://www.theintelligencer.net/news/top-headlines/2024/01/in-god-we-trust-classroom-mandate-passes-w-va-state-senate/"]),
        claim("az2", "mike-azinger", "family_child_sovereignty", 0, True,
              "Chairs the West Virginia Senate's Select Committee on School Choice — the standing legislative committee responsible for advancing parental rights in education, school voucher programs, and alternatives to government-run public schools across the state.",
              ["https://home.wvlegislature.gov/senator/mike-azinger/"]),
        claim("az3", "mike-azinger", "self_defense", 1, True,
              "Sponsored legislation to loosen restrictions on licensed adults carrying firearms at public school buildings and school-sponsored events in West Virginia, characterizing the bill as 'a good bill for gun freedom' — expanding Second Amendment carry rights in settings where they had previously been restricted.",
              ["https://www.wvgazettemail.com/news/education/wv-senators-debate-bible-classes-bill-ok-changes-to-school/article_bedbab11-8b3e-5fb8-b223-dad67b8a0e99.html"]),
    ]),

    # ---------- Randy E. Smith (WV-R, District 14, Senate President/Lt. Gov.) ----------
    ("randy-e-smith", "WV", "State Senator", [
        claim("rsmith1", "randy-e-smith", "economic_stewardship", 4, True,
              "A 44-year coal-industry veteran (mine foreman and safety manager) elected Senate President and Lieutenant Governor of West Virginia in January 2025, who explicitly opposes preferential tax incentives for green-energy sources: 'I'm not against green energy but I am against tax incentives for some energy sources... I just want everybody on the same playing field.' His career and stated policy resist the ESG-driven energy transition agenda promoted by WEF-aligned institutions.",
              ["https://westvirginiawatch.com/2024/12/08/randy-smith-former-coal-miner-turned-politician-nominated-as-next-senate-president/",
               "https://wvmetronews.com/2025/01/08/randy-smith-retired-coal-miner-is-new-senate-president-hanshaw-returns-as-house-speaker/"]),
        claim("rsmith2", "randy-e-smith", "biblical_marriage", 2, True,
              "Voted NO on amendments that would have softened conservative bills addressing social issues in the WV Senate, and as Senate President publicly stated his intention for the 2025 Legislature to address transgender bathroom access policy — reflecting firm rejection of government-mandated accommodation of transgender ideology in public facilities.",
              ["https://westvirginiawatch.com/2024/12/08/randy-smith-former-coal-miner-turned-politician-nominated-as-next-senate-president/"]),
        claim("rsmith3", "randy-e-smith", "self_defense", 1, True,
              "National Rifle Association member with a voting record on the more conservative side of the WV Senate Republican caucus. Opposed amendments to gun-rights legislation and as Senate President has maintained West Virginia's permissive Second Amendment environment, resisting restrictions on firearm ownership or carry.",
              ["https://wvmetronews.com/2025/01/08/randy-smith-retired-coal-miner-is-new-senate-president-hanshaw-returns-as-house-speaker/"]),
    ]),

    # ---------- Mike Oliverio (WV-R, District 13, State Senator) ----------
    ("mike-oliverio", "WV", "State Senator", [
        claim("oliv1", "mike-oliverio", "sanctity_of_life", 0, True,
              "Publicly advocates a government ban on abortion (per Ballotpedia) and has served in the WV Senate Republican supermajority upholding WV's near-total abortion ban enacted in 2022. In February 2026, the WV Senate passed SB173 (31-1) to prohibit out-of-state entities from prescribing or mailing abortifacient drugs to West Virginia, a felony-level enforcement extension of the state's abortion ban — with Oliverio among the overwhelming majority.",
              ["https://ballotpedia.org/Mike_Oliverio",
               "https://westvirginiawatch.com/2026/02/13/senate-passes-bill-prohibiting-abortifacients-being-prescribed-or-mailed-to-west-virginia/"]),
        claim("oliv2", "mike-oliverio", "election_integrity", 0, True,
              "Voted with the WV Senate Republican supermajority in the 2025 regular session to pass five election security laws, including SB486 — explicitly requiring U.S. citizenship as a prerequisite for voter registration in all West Virginia elections — and SB490, banning ranked-choice voting statewide. All five bills were signed by Gov. Patrick Morrisey and were praised by ALEC as model election-integrity legislation.",
              ["https://alec.org/article/west-virginia-leads-the-charge-in-securing-elections/",
               "https://wvpublic.org/bill-prohibiting-ranked-choice-voting-passes-both-chambers/"]),
    ]),

    # ---------- Patrick Martin (WV-R, District 12, Senate Majority Leader) ----------
    ("patrick-martin", "WV", "State Senator", [
        claim("pmart1", "patrick-martin", "election_integrity", 0, True,
              "As Senate Majority Leader since January 2025, led the 2025 passage of five election security bills through the WV Senate, including SB486 (requiring explicit U.S. citizenship for voter registration in all WV elections) and SB490 (banning ranked-choice voting). All five were signed by Gov. Patrick Morrisey and recognized by ALEC as a national model for election-integrity legislation.",
              ["https://alec.org/article/west-virginia-leads-the-charge-in-securing-elections/",
               "https://wvmetronews.com/2025/03/04/ranked-choice-voting-would-be-banned-under-bill-passed-by-west-virginia-senate/"]),
        claim("pmart2", "patrick-martin", "biblical_marriage", 4, True,
              "The WV Senate under Martin's majority leadership passed Senate Bill 590 in March 2026 (with only 2 no votes, both Democrats) to ban adult cabaret performances — including drag shows — on public property or in locations viewable by minors. The same Senate also approved in 2025 a bill signed by Gov. Morrisey defining 'men' and 'women' in state code and barring transgender individuals from using cross-sex restrooms in specified public venues.",
              ["https://westvirginiawatch.com/2026/03/04/wv-senate-passes-bills-targeting-transgender-people-drag-performances/"]),
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
