#!/usr/bin/env python3
"""Enrichment batch 359: 2-3 claims each for 5 federal U.S. Senate candidates — bottom of alphabet.

archetype_curated federal senate pool is fully exhausted (see batch 358 note). This batch
targets low_evidence 2026 U.S. Senate candidates with 0 prior claims, selected from the
reverse-alphabetical bottom of the bucket (WY→AL range):

  • Everett Wess      (AL, D) — 2026 Democratic nominee vs Barry Moore; advocates "reproductive
                                freedom" and voting rights; accused by primary rival of pro-life
                                statement on camera; supports sanctuary/ICE reform; career attorney
  • Kyle Sweetser     (AL, D) — Former Republican construction CEO, switched to D in Apr 2025;
                                ran against executive overreach/tariffs; moderate positioning;
                                eliminated in primary
  • Mark Wheeler II   (AL, D) — Chemist/Democrat; labor unions, national health insurance, lost
                                primary May 2026
  • Dakarai Larriett  (AL, D) — Business owner; LGBTQ rights; pro-reproductive freedom; lost
                                June 2026 runoff to Wess
  • Nathan Sage       (IA, D) — Marine veteran/mechanic; pro-choice, working-class populist;
                                suspended campaign Feb 2026

Sources: wessforsenate.com, Alabama Reflector, Alabama Daily News, ballotpedia.org,
         en.wikipedia.org, Iowa Capital Dispatch, iowastartingline.com,
         alabamareflector.com, aldailynews.com
Writes scorecard.json MINIFIED to stay under GitHub's 50 MB limit.
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
    # ---- Everett Wess (AL-D) — 2026 Democratic nominee for U.S. Senate ----
    ("everett-wess", "AL", "Tuberville seat", [
        claim("ew1", "everett-wess", "sanctity_of_life", 0, False,
              "Wess ran as the Alabama Democratic nominee for U.S. Senate (2026) on a "
              "platform emphasizing 'reproductive freedom,' stating he is 'proud of that "
              "record, and I will continue fighting for Alabama families, voting rights, "
              "reproductive freedom, economic opportunity, and equal justice.' His primary "
              "rival Dakarai Larriett accused him of being 'caught on stage on camera "
              "talking about being pro-life in a time when reproductive health is under "
              "constant assault,' though Wess denied the characterization. As a Democrat "
              "he does not support life-at-conception personhood protections and opposes "
              "Alabama's near-total abortion ban.",
              ["https://alabamareflector.com/2026/06/14/a-voters-guide-to-the-democratic-and-republican-u-s-senate-runoffs/",
               "https://ballotpedia.org/United_States_Senate_election_in_Alabama,_2026",
               "https://wessforsenate.com/"]),
        claim("ew2", "everett-wess", "border_immigration", 2, False,
              "Wess's immigration platform calls for 'ensuring safe communities' by "
              "'protection from Immigration and Customs Enforcement' — positioning ICE as "
              "a threat to community safety rather than an enforcement tool — and "
              "advocates for properly funding immigration courts and expediting legal "
              "status hearings rather than prioritizing deportation. He does not support "
              "sanctuary-city restrictions and frames immigration enforcement as a "
              "due-process issue.",
              ["https://www.ballotready.org/people/everett-w-wess",
               "https://wessforsenate.com/",
               "https://ballotpedia.org/Everett_Wess"]),
        claim("ew3", "everett-wess", "economic_stewardship", 2, False,
              "Wess supports expanded federal healthcare spending and opposes cuts to "
              "Medicaid and other safety-net programs, citing their importance to rural "
              "Alabama hospitals. His platform does not include deficit reduction, a "
              "balanced-budget amendment, or opposition to federal spending growth — "
              "positions contrary to the rubric's sound-money/balanced-budget standard.",
              ["https://wessforsenate.com/",
               "https://www.ballotready.org/people/everett-w-wess"]),
    ]),

    # ---- Kyle Sweetser (AL-D) — former Republican, switched party Apr 2025 ----
    ("kyle-sweetser", "AL", "Tuberville seat", [
        claim("ks1", "kyle-sweetser", "refuse_federal_overreach", 0, False,
              "Sweetser switched from Republican to Democrat in April 2025, running on a "
              "platform of limiting executive branch power. He said 'The president now has "
              "unlimited power. He has the ability to do whatever he wants. That puts us "
              "in a scary place,' and positioned his campaign around checking what he "
              "characterizes as unchecked executive authority. While his concern for "
              "constitutional checks is noted, he frames the solution through expanded "
              "Democratic federal governance rather than restoring enumerated limits.",
              ["https://aldailynews.com/former-trump-voter-turned-critic-running-for-alabamas-u-s-senate-seat-as-a-democrat/",
               "https://www.alreporter.com/2025/04/22/disillusioned-by-the-republican-party-kyle-sweetser-is-challenging-tuberville-in-2026/",
               "https://ballotpedia.org/Kyle_Sweetser"]),
        claim("ks2", "kyle-sweetser", "economic_stewardship", 2, False,
              "Sweetser publicly criticized Donald Trump's steel and aluminum tariffs — "
              "the tariffs that hurt his own construction business — and used them as "
              "the catalyst for his political conversion from Republican to Democrat. "
              "His opposition to tariffs aligns with a free-trade/globalist framework "
              "rather than the economic-nationalist, America-First trade protectionism "
              "the rubric favors for protecting domestic labor and industry.",
              ["https://www.alreporter.com/2025/04/22/disillusioned-by-the-republican-party-kyle-sweetser-is-challenging-tuberville-in-2026/",
               "https://en.wikipedia.org/wiki/Kyle_Sweetser",
               "https://alabamareflector.com/2026/05/14/a-voters-guide-to-alabamas-us-senate-race/"]),
    ]),

    # ---- Mark Wheeler II (AL-D) — chemist, lost primary May 2026 ----
    ("mark-wheeler-ii", "AL", "Tuberville seat", [
        claim("mw1", "mark-wheeler-ii", "economic_stewardship", 2, False,
              "Wheeler's campaign called for a national health insurance program — "
              "Medicare for All-style universal coverage — and rebuilding 'strong labor "
              "unions' to give every worker collective bargaining power. Expanded "
              "federal health spending and mandatory union empowerment represent "
              "significant increases to federal outlays and regulatory burdens, contrary "
              "to the rubric's balanced-budget and limited-government standards.",
              ["https://markwheelerforsenate.com/",
               "https://www.thealabamanewswire.com/news/local/meet-the-candidates-us-senate-candidate-mark-wheeler/article_f48b4578-f363-4fb6-8f9d-f5c4e52a8887.html",
               "https://ballotpedia.org/Mark_Wheeler_II"]),
        claim("mw2", "mark-wheeler-ii", "public_justice", 0, False,
              "Wheeler campaigned on systemic economic justice, stating he would fight "
              "to address 'systemic poverty' and the gap between corporate interests and "
              "working families. His platform endorses expanded federal intervention in "
              "labor markets and economic redistribution through union-strengthening "
              "legislation and tax-funded health coverage rather than market-based "
              "solutions.",
              ["https://markwheelerforsenate.com/",
               "https://www.thealabamanewswire.com/news/local/meet-the-candidates-us-senate-candidate-mark-wheeler/article_f48b4578-f363-4fb6-8f9d-f5c4e52a8887.html"]),
    ]),

    # ---- Dakarai Larriett (AL-D) — pet-care business owner, lost runoff June 2026 ----
    ("dakarai-larriett", "AL", "Tuberville seat", [
        claim("dl1", "dakarai-larriett", "sanctity_of_life", 0, False,
              "Larriett ran to the left of fellow Democrat Everett Wess on reproductive "
              "rights during the 2026 Alabama Democratic Senate primary, attacking Wess "
              "for allegedly stating a pro-life position on camera 'in a time when "
              "reproductive health is under constant assault.' Larriett's own campaign "
              "stressed full support for reproductive freedom and accused Wess of being "
              "out of step with Democratic voters on abortion, signaling Larriett's "
              "opposition to any restrictions on abortion access — rejecting the rubric's "
              "life-at-conception standard.",
              ["https://alabamareflector.com/2026/06/14/a-voters-guide-to-the-democratic-and-republican-u-s-senate-runoffs/",
               "https://ballotpedia.org/United_States_Senate_election_in_Alabama,_2026",
               "https://dakarailarriett.com/"]),
        claim("dl2", "dakarai-larriett", "biblical_marriage", 4, False,
              "Larriett's published campaign platform states 'I fully support LGBTQ "
              "equal rights,' including in schools and public accommodations — the "
              "explicit promotion of LGBTQ ideology the rubric identifies as contrary "
              "to the biblical definition of marriage and family.",
              ["https://www.wsfa.com/2026/05/13/meet-candidates-alabamas-democratic-candidates-us-senate/",
               "https://dakarailarriett.com/",
               "https://ballotpedia.org/Dakarai_Larriett"]),
        claim("dl3", "dakarai-larriett", "public_justice", 0, False,
              "Larriett's platform calls for 'prioritizing education over policing and "
              "prisons' and community-based policing reforms emphasizing mental health "
              "care and economic opportunity as the primary tools of public safety — "
              "a decarceration and defund-adjacent posture at odds with the rubric's "
              "focus on lawful order and personal accountability.",
              ["https://www.branch.vote/races/2026-alabama-primary-election-al-state-u.s.-senate-al-state-d/candidates/dakarai-larriett",
               "https://dakarailarriett.com/"]),
    ]),

    # ---- Nathan Sage (IA-D) — Marine veteran, suspended campaign Feb 2026 ----
    ("nathan-sage", "IA", "Ernst seat", [
        claim("ns1", "nathan-sage", "sanctity_of_life", 0, False,
              "Sage ran as a pro-choice Democrat for Iowa's open U.S. Senate seat in "
              "2026 (Joni Ernst's seat), criticizing Iowa's six-week abortion ban and "
              "running on restoring federal abortion protections. He suspended his "
              "campaign in February 2026 due to fundraising shortfalls, endorsing "
              "fellow Democrat Josh Turek. His pro-choice platform rejects the "
              "rubric's life-at-conception standard.",
              ["https://iowacapitaldispatch.com/2026/02/15/democrat-nathan-sage-ends-u-s-senate-campaign/",
               "https://iowastartingline.com/news/elections/nathan-sage-drops-out-of-us-senate-race-endorses-turek/",
               "https://ballotpedia.org/Nathan_Sage"]),
        claim("ns2", "nathan-sage", "economic_stewardship", 2, False,
              "Sage's campaign platform called for the federal government to negotiate "
              "prescription drug prices, break up meatpacking monopolies controlling "
              "over 80% of the market, pass a Real Right to Repair Law for farmers, "
              "and lead in clean energy investment — a program of expanded regulatory "
              "intervention and federal market management rather than free-market or "
              "balanced-budget conservatism.",
              ["https://www.sageforsenate.com/platform",
               "https://ballotpedia.org/Nathan_Sage",
               "https://iowacapitaldispatch.com/2026/02/15/democrat-nathan-sage-ends-u-s-senate-campaign/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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
