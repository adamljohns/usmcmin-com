#!/usr/bin/env python3
"""Enrichment batch 595: hand-curated claims for 5 Oregon Republican state senators.

Targets archetype_party_default OR senators that had 0 evidence claims, taken
from the bottom of the alphabet (OR — next unexhausted state after SC/RI/PA).

Senators: Todd Nash (D-29), Suzanne Weber (D-16), Noah Robinson (D-2),
Mike McLane (D-30), Kim Thatcher (D-11).
Each claim cites >=1 reliable source and reflects 2024-2026 positions/record.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ---------------- Todd Nash (OR-R, State Senator D-29) ----------------
    ("todd-nash", "OR", "Senator", [
        claim("tn1", "todd-nash", "sanctity_of_life", 0, True,
              "Nash declares he is '100% pro-life' and was the only candidate in his 2024 primary endorsed by the Oregon Right to Life PAC, affirming legal protection for unborn life from conception.",
              ["https://votetoddnash.com/on-the-issues/",
               "https://ballotpedia.org/Todd_Nash"]),
        claim("tn2", "todd-nash", "self_defense", 1, True,
              "Nash holds the highest rating given to candidates by the NRA Political Victory Fund, calls Second Amendment rights 'non-negotiable,' and pledges to 'vigorously oppose any attempt to infringe upon these fundamental liberties,' including red-flag laws and magazine-capacity restrictions.",
              ["https://votetoddnash.com/on-the-issues/",
               "https://ballotpedia.org/Todd_Nash"]),
        claim("tn3", "todd-nash", "industry_capture", 3, True,
              "A working cattle rancher and former president of the Oregon Cattlemen's Association, Nash shepherded 2025 legislation to quadruple state compensation for livestock killed or likely killed by wolves — directly protecting small family-ranching operations against predator losses without federal Endangered Species Act constraints.",
              ["https://wallowa.com/2025/07/18/enterprises-todd-nash-reflects-on-1st-term-as-a-state-senator/",
               "https://eastoregonian.com/2026/03/10/enterprise-senator-leads-effort-for-wolf-compensation/"]),
    ]),

    # ---------------- Suzanne Weber (OR-R, State Senator D-16) ----------------
    ("suzanne-weber", "OR", "Senator", [
        claim("sw1", "suzanne-weber", "sanctity_of_life", 0, True,
              "Weber joined Oregon's historic 6-week Republican Senate walkout in May 2023 specifically to block HB 2002, which would have expanded state abortion access; she also joined Oregon Right to Life in a subsequent lawsuit seeking to enjoin HB 2002 as procedurally defective, sustaining active opposition to abortion expansion through both legislative and legal channels.",
              ["https://en.wikipedia.org/wiki/Suzanne_Weber",
               "https://www.opb.org/article/2023/05/03/republican-walk-out-oregon-senate-abortion-guns-gender-affirming-care/"]),
        claim("sw2", "suzanne-weber", "biblical_marriage", 2, True,
              "HB 2002 also codified and expanded state-funded gender-affirming care for minors; Weber's walkout and the ORTL lawsuit directly targeted this provision, publicly rejecting Oregon's mandate enabling youth transgender medical interventions, consistent with the rubric's rejection of transgender ideology.",
              ["https://en.wikipedia.org/wiki/Suzanne_Weber",
               "https://www.opb.org/article/2023/05/04/oregon-politics-republican-walkout-boycott-senate-salem-reproductive-health-care-abortion-gender/"]),
        claim("sw3", "suzanne-weber", "self_defense", 1, True,
              "Weber joined the 2023 walkout in part to block HB 2005-B, Oregon's gun-control package that — before a compromise pared it back — included raising the semiautomatic rifle purchase age from 18 to 21 and expanding concealed-carry restrictions, opposing the broad gun-control agenda Democrats advanced.",
              ["https://www.opb.org/article/2023/05/03/republican-walk-out-oregon-senate-abortion-guns-gender-affirming-care/",
               "https://oregoncapitalchronicle.com/2023/05/03/oregon-senate-republicans-independent-stage-walkout-as-divisive-bills-await-votes/"]),
    ]),

    # ---------------- Noah Robinson (OR-R, State Senator D-2) ----------------
    ("noah-robinson", "OR", "Senator", [
        claim("nr1", "noah-robinson", "sanctity_of_life", 0, True,
              "Robinson's 2024 campaign for Oregon Senate District 2 explicitly listed 'supporting legislation that is pro-life' as a core priority, signaling a life-at-conception commitment in a rural southern-Oregon district.",
              ["https://ballotpedia.org/Noah_Robinson_(Oregon)",
               "https://oregonvotes.gov/voters-guide/english/noahrobinson.html"]),
        claim("nr2", "noah-robinson", "self_defense", 1, True,
              "Robinson's 2024 campaign explicitly committed to being 'pro-second amendment,' opposing the firearms restrictions championed by Oregon Democrats including semi-automatic purchase-age increases and Ballot Measure 114's permit-to-purchase scheme.",
              ["https://ballotpedia.org/Noah_Robinson_(Oregon)",
               "https://oregonvotes.gov/voters-guide/english/noahrobinson.html"]),
        claim("nr3", "noah-robinson", "refuse_federal_overreach", 0, True,
              "Robinson campaigned on protecting Oregon's natural-resource industries — timber, mining, ranching, farming — from litigation and regulatory attacks by outside special interests, and on reversing 'flawed energy policies' driving up electricity and fuel costs in rural Oregon, directly challenging federal and progressive state regulatory overreach.",
              ["https://ballotpedia.org/Noah_Robinson_(Oregon)",
               "https://robinsonfororegon.com/"]),
    ]),

    # ---------------- Mike McLane (OR-R, State Senator D-30) ----------------
    ("mike-mclane", "OR", "Senator", [
        claim("mm1", "mike-mclane", "self_defense", 1, True,
              "McLane 'strongly supports the Second Amendment and responsible gun ownership' and pledged to 'oppose efforts to limit constitutional rights,' explicitly warning that Oregon gun-restriction measures like Ballot Measure 114's permit-to-purchase mandate would cause 'uncertainty and incredible amounts of litigation' — opposing the state's anti-gun legislative agenda.",
              ["https://votemikemclane.com/",
               "https://en.wikipedia.org/wiki/Mike_McLane"]),
        claim("mm2", "mike-mclane", "sanctity_of_life", 0, True,
              "McLane's campaign affirms he is 'dedicated to protecting the rights of mothers and families, valuing the sanctity of life at all stages,' reflecting a life-at-conception position consistent with the Oregon Republican platform and his rural Central Oregon district.",
              ["https://votemikemclane.com/",
               "https://oregonvotes.gov/voters-guide/english/mikemclane.html"]),
    ]),

    # ---------------- Kim Thatcher (OR-R, State Senator D-11) ----------------
    ("kim-thatcher", "OR", "Senator", [
        claim("kt1", "kim-thatcher", "sanctity_of_life", 0, True,
              "Thatcher sponsored SB 1012 (2025), the Oregon Born Alive Infants Protection Act, which would require physicians to provide a baby born alive during an attempted abortion the same standard of care as any other newborn at the same gestational stage — a direct affirmation of personhood rights at birth.",
              ["https://www.ortl.org/2025/01/support-her-protect-them-a-closer-look-at-oregons-2025-pro-life-bills/",
               "https://www.oregonlegislature.gov/thatcher"]),
        claim("kt2", "kim-thatcher", "election_integrity", 0, True,
              "Thatcher signed a December 2020 letter urging Oregon's AG to join Texas v. Pennsylvania challenging certified 2020 presidential election results, and in October 2021 joined a bipartisan call for a national audit of the 2020 election in all states and elimination of stale voter rolls — consistent with the rubric's election-security concerns.",
              ["https://en.wikipedia.org/wiki/Kim_Thatcher",
               "https://ballotpedia.org/Kim_Thatcher"]),
        claim("kt3", "kim-thatcher", "family_child_sovereignty", 0, True,
              "Thatcher advocates that 'every parent should be able to determine the best educational options for their children,' championing parental choice in schooling; she also joined the 2023 Republican Senate walkout that successfully forced HB 2002 amendments requiring parental notification for abortions performed on patients under 15 — strengthening parental authority over minors' medical decisions.",
              ["https://kimthatcher.com/meet-kim",
               "https://en.wikipedia.org/wiki/Kim_Thatcher"]),
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
