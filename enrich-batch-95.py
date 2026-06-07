#!/usr/bin/env python3
"""Enrichment batch 95: hand-curated claims for 4 state-level R candidates.

Targets archetype_curated governor candidates (HI/KS/MA) that had 0 evidence
claims. Uses the (slug + state + office_keyword) matcher from prior batches.

Candidates (all R):
  - James "Duke" Aiona   (HI, Gov candidate)
  - Vicki Schmidt        (KS, Gov candidate)
  - Scott Schwab         (KS, Gov candidate)
  - Brian Shortsleeve    (MA, Gov candidate)

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
    # ---------------- James "Duke" Aiona (HI-R, Gov candidate) ----------------
    ("james-aiona-gov-2026", "HI", "Governor", [
        claim("ja1", "james-aiona-gov-2026", "sanctity_of_life", 0, True,
              "Calls himself pro-life 'from conception to death,' stating 'we must respect all human life' and pledging to 'do everything we can to stand up and speak out for the most innocent among us.' Has been associated with Hawaii Family Advocates and consistently grounds his pro-life stance in his Christian faith.",
              ["https://en.wikipedia.org/wiki/Duke_Aiona",
               "https://www.ontheissues.org/Governor/Duke_Aiona_Abortion.htm",
               "https://ballotpedia.org/Duke_Aiona"]),
        claim("ja2", "james-aiona-gov-2026", "christian_liberty", 0, True,
              "Regularly and explicitly cites his Christian faith as the foundation of his public positions; associated with Hawaii Family Advocates (described as ultra-conservative Christian advocacy group); has made his faith central to each of his gubernatorial campaigns.",
              ["https://www.staradvertiser.com/2022/08/17/hawaii-news/differences-emerge-between-aiona-and-new-running-mate/",
               "https://ballotpedia.org/Duke_Aiona"]),
    ]),

    # ---------------- Vicki Schmidt (KS-R, Gov candidate) ----------------
    ("vicki-schmidt-gov", "KS", "Governor", [
        claim("vs1", "vicki-schmidt-gov", "sanctity_of_life", 0, False,
              "As a Kansas state senator, was the only Republican to vote against banning live dismemberment abortion; also voted against seven separate bills to close late-term abortion loopholes and opposed legislation that would allow prosecutors to bring double-homicide charges when a pregnant woman is murdered — indicating she rejects a life-at-conception framework in law.",
              ["https://www.lifenews.com/2026/05/26/vicki-schmidt-is-a-pro-abortion-republican-who-shouldnt-be-kansas-governor/",
               "https://ballotpedia.org/Vicki_Schmidt"]),
        claim("vs2", "vicki-schmidt-gov", "family_child_sovereignty", 0, False,
              "Voted against parental consent requirements for minors seeking abortions during her 14 years in the Kansas state senate — opposing one of the most basic parental-rights protections in the pro-life legislative toolkit.",
              ["https://www.lifenews.com/2026/05/26/vicki-schmidt-is-a-pro-abortion-republican-who-shouldnt-be-kansas-governor/",
               "https://ballotpedia.org/Vicki_Schmidt"]),
    ]),

    # ---------------- Scott Schwab (KS-R, Gov candidate) ----------------
    ("scott-schwab-gov", "KS", "Governor", [
        claim("ss1", "scott-schwab-gov", "election_integrity", 0, True,
              "As chair of the Kansas House Elections Committee in 2011, championed legislation requiring a government-issued photo ID for every election and documentary proof of citizenship to register to vote — making Kansas a national early mover on voter-ID and citizenship verification.",
              ["https://scottschwab.com/",
               "https://www.congress.gov/119/meeting/house/119160/witnesses/HHRG-119-HA00-Wstate-SchwabS-20260416.pdf"]),
        claim("ss2", "scott-schwab-gov", "border_immigration", 4, True,
              "Supported 2024 Kansas legislation banning China and other foreign adversaries from purchasing real estate within 100 miles of U.S. military bases and critical infrastructure; stated 'our nation's adversaries have no business setting up covert operations next to critical infrastructure.'",
              ["https://kansasreflector.com/2024/05/02/legislature-adopts-potentially-unconstitutional-ban-on-foreign-adversary-property-ownership/",
               "https://scottschwab.com/"]),
        claim("ss3", "scott-schwab-gov", "economic_stewardship", 2, True,
              "Campaigns on the B.A.L.D. property-tax cut initiative — immediately eliminating Kansas' 20-mill state property tax and requiring voter approval for future local property-tax increases — as part of a platform of lowering taxes and cutting regulations.",
              ["https://kansasreflector.com/briefs/scott-schwab-aims-gop-gubernatorial-campaign-at-property-tax-reform/",
               "https://scottschwab.com/"]),
    ]),

    # ---------------- Brian Shortsleeve (MA-R, Gov candidate) ----------------
    ("brian-shortsleeve-gov", "MA", "Governor", [
        claim("bs1", "brian-shortsleeve-gov", "sanctity_of_life", 0, False,
              "Declared 'I Am the Pro-Choice Candidate' in the 2026 Massachusetts Republican gubernatorial primary; has repeatedly described himself as the 'pro-choice Republican' and criticized primary opponent Mike Minogue's pro-life stance as unelectable — explicitly rejecting a life-at-conception framework.",
              ["https://www.newbostonpost.com/brian-shortsleeve-pro-choice-candidate-gop-gov-primary/",
               "https://www.wgbh.org/news/politics/2026-05-13/he-will-never-win-a-statewide-election-shortsleeve-knocks-minogue-for-abortion-stance"]),
        claim("bs2", "brian-shortsleeve-gov", "border_immigration", 2, True,
              "Pledged to end Massachusetts' sanctuary state policies on day one, cooperate with ICE, and reform the Right to Shelter law so migrants are no longer entitled to taxpayer-funded benefits; stated the state must 'enforce the law' and criticized Healey for handcuffing law enforcement.",
              ["https://brianshortsleeve.com/shortsleeve-slams-healey-for-turning-massachusetts-into-a-sanctuary-state/",
               "https://www.nbcboston.com/news/politics/at-issue/brian-shortsleeve-governor-massachusetts/3868637/"]),
        claim("bs3", "brian-shortsleeve-gov", "economic_stewardship", 2, True,
              "A Marine Corps veteran and venture capitalist running as a 'strong fiscal conservative' on a platform of cutting taxes, slashing waste and overregulation, and rolling back green energy mandates to lower utility bills for Massachusetts families.",
              ["https://www.wbur.org/news/2026/02/19/brian-shortsleeve-governor-massachusetts-gop-baker-romney",
               "https://brianshortsleeve.com/mission-for-mass/"]),
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
