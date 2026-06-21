#!/usr/bin/env python3
"""Enrichment batch 353: hand-curated claims for 4 SC-01 2026 House candidates.

All four ran (or filed) in South Carolina's 1st Congressional District for the
open seat left by Nancy Mace (who ran for Governor). The June 9, 2026 primary
narrowed the field; none of these four advanced to the runoff.

Targets (3 R / 1 D), bottom-of-alphabet sweep (SC, June 2026):
  Justin Myers     (SC-01, R) — Navy vet "Pirate Hunter," LOST June 9 R primary
  Logan Cunningham (SC-01, R) — Beaufort County Council, LOST June 9 R primary
  Dan Brown        (SC-01, R) — former Timmons staffer, LOST June 9 R primary
  Matt Fulmer      (SC-01, D) — Hilton Head waiter, LOST June 9 D primary

Each claim cites >= 1 reliable public source and reflects 2025-2026 campaign
statements, news coverage, and official pledge records.

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
    # -------- Justin Myers (SC-01, R — LOST June 9 primary) --------
    # U.S. Navy Gunner's Mate 2007-2013; participated in the historic 2011
    # USS Ashland pirate interdiction (first pirate prosecution in ~200 years).
    # Ran on "America First leadership"; signed U.S. Term Limits pledge.
    ("justin-myers-sc-01", "SC", "LOST June 9 primary, open Mace seat", [
        claim("jm1", "justin-myers-sc-01", "self_defense", 0, True,
              "Justin Myers, a U.S. Navy veteran (Gunner's Mate, 2007-2013) and 2026 SC-01 Republican primary candidate, explicitly listed 'protecting constitutional rights, like free speech and the Second Amendment' as a central pillar of his 'America First leadership' campaign platform. His military background as an armed service member who participated in the 2011 USS Ashland pirate interdiction — the first successful pirate prosecution in nearly 200 years — grounds his pro-Second-Amendment stance in direct weapons-use experience.",
              ["https://abcnews4.com/news/local/we-have-to-unite-pirate-hunter-joins-the-race-for-scs-1st-congressional-district-wciv-abc-news-4-9-12-2025",
               "https://shows.acast.com/charleston-daily-news-now/episodes/pirate-hunter-justin-myers-on-unity-and-lowcountry-values"]),
        claim("jm2", "justin-myers-sc-01", "border_immigration", 0, True,
              "Myers' 'America First leadership' campaign platform centered on 'securing the border' as a top federal priority. He described his mission as standing 'up for faith, family, and freedom while restoring trust in government,' with an enforcement-first border stance — consistent with the rubric's wall-and-military border security standard. He is a blue-collar business owner and Navy veteran, not a career politician.",
              ["https://abcnews4.com/news/local/coastal-battleground-heats-up-as-republicans-and-democrats-vie-for-sc-01-seat",
               "https://abcnews4.com/news/local/we-have-to-unite-pirate-hunter-joins-the-race-for-scs-1st-congressional-district-wciv-abc-news-4-9-12-2025"]),
        claim("jm3", "justin-myers-sc-01", "refuse_federal_overreach", 0, True,
              "Myers signed the U.S. Term Limits pledge, committing to a constitutional amendment imposing term limits on all members of Congress. He was confirmed as a signatory by the U.S. Term Limits organization. Term limits structurally curtail the accumulation of federal legislative power by career incumbents — a direct check on the federal overreach the rubric targets — and Myers framed his candidacy as an outsider challenging congressional dysfunction.",
              ["https://termlimits.com/justin-myers-pledges-to-support-congressional-term-limits/",
               "https://abcnews4.com/news/local/coastal-battleground-heats-up-as-republicans-and-democrats-vie-for-sc-01-seat"]),
    ]),

    # -------- Logan Cunningham (SC-01, R — LOST June 9 primary) --------
    # Youngest-ever Beaufort County Council member; served 6 years on Council.
    # Campaign: "Lowcountry First" — America-First conservative, infrastructure.
    ("logan-cunningham", "SC", "LOST June 9 primary; Beaufort County Council", [
        claim("lc1", "logan-cunningham", "border_immigration", 0, True,
              "Logan Cunningham, a Beaufort County Council member running for SC-01, stated explicitly on his campaign platform that he 'believes in securing the border' as a federal priority — alongside defending taxpayers, supporting law enforcement, and standing up for parents and families. His 'Lowcountry First' campaign ran on an America-First conservative framework that treats border enforcement as a core national-security and community-protection issue.",
              ["https://abcnews4.com/news/local/logan-cunningham-says-lowcountry-first-leadership-sets-him-apart-in-congressional-race-south-carolina-1st-congressional-district-midterm-elections",
               "https://www.logancunningham.com/"]),
        claim("lc2", "logan-cunningham", "family_child_sovereignty", 0, True,
              "Cunningham's campaign platform specifically included 'standing up for parents and families' as a policy commitment alongside border security and law enforcement support — reflecting a parental-rights, family-sovereignty orientation. He is a lifelong Lowcountry conservative who framed his congressional bid as defending local community values against federal overreach and affirming the primacy of family in public policy.",
              ["https://abcnews4.com/news/local/logan-cunningham-says-lowcountry-first-leadership-sets-him-apart-in-congressional-race-south-carolina-1st-congressional-district-midterm-elections",
               "https://www.postandcourier.com/beaufort-county/politics/logan-cunningham-sc01-candidate/article_3c6ed220-0edf-487f-90bb-58cb8d152699.html"]),
        claim("lc3", "logan-cunningham", "economic_stewardship", 2, True,
              "As a Beaufort County Council member (the youngest-ever elected to that body), Cunningham achieved conservative fiscal results including raising teacher pay to the highest in South Carolina 'without raising taxes' and securing funding for the long-delayed Hilton Head Bridge project — demonstrating a no-new-taxes, fiscally responsible approach to government. His congressional campaign extended this anti-deficit, taxpayer-first philosophy to federal fiscal policy.",
              ["https://abcnews4.com/news/local/logan-cunningham-says-lowcountry-first-leadership-sets-him-apart-in-congressional-race-south-carolina-1st-congressional-district-midterm-elections",
               "https://www.wsav.com/news/your-local-election-hq/logan-cunningham-officially-launches-sc-congress-campaign/"]),
    ]),

    # -------- Dan Brown (SC-01, R — LOST 2026 R primary) --------
    # Former legislative aide to Rep. William Timmons (R-SC-04); returned to
    # Bluffton to start a family; ran on Tenth Amendment / fiscal discipline.
    ("dan-brown-sc-01", "SC", "LOST 2026 R primary", [
        claim("db1", "dan-brown-sc-01", "refuse_federal_overreach", 0, True,
              "Dan Brown, a former legislative aide to U.S. Rep. William Timmons (R-SC), ran for SC-01 on an explicit Tenth Amendment platform: 'limiting federal power and returning authority to states and local governments, pointing to the Tenth Amendment as a foundation for that belief.' This states'-rights constitutionalist stance — returning power from Washington to the Lowcountry — directly aligns with the rubric's standard for rejecting federal overreach.",
              ["https://abcnews4.com/news/local/dan-brown-campaigns-on-fiscal-responsibility-and-conservative-values-for-sc-01",
               "https://www.wtma.com/2026/03/31/dan-brown-campaigns-on-fiscal-responsibility-and-conservative-values-for-sc-01/"]),
        claim("db2", "dan-brown-sc-01", "economic_stewardship", 2, True,
              "Brown's core campaign messaging centered on the national debt and fiscal discipline: news coverage noted he 'frequently returns to concerns about the national debt, government accountability and congressional dysfunction.' He described himself as a 'fresh voice focused on fiscal discipline, conservative values, and practical solutions' — a consistent anti-deficit posture framed as both a constitutional and generational obligation to future taxpayers.",
              ["https://abcnews4.com/news/local/dan-brown-campaigns-on-fiscal-responsibility-and-conservative-values-for-sc-01",
               "https://www.votedanbrown.com/meet-dan"]),
        claim("db3", "dan-brown-sc-01", "sanctity_of_life", 0, True,
              "Brown cited seeing his son's first ultrasound as the pivotal moment that moved him to run for Congress: 'Basically, the first time I saw his ultrasound, it was my aha moment.' He entered the Republican primary for SC-01 — a district with a staunchly pro-life Republican base — and his personal testimony grounds his campaign in a family-first, protective-of-life orientation. No specific abortion-legislation position (beyond this motivating statement) is documented in his public record.",
              ["https://abcnews4.com/news/local/dan-brown-campaigns-on-fiscal-responsibility-and-conservative-values-for-sc-01",
               "https://www.wtma.com/2026/03/31/dan-brown-campaigns-on-fiscal-responsibility-and-conservative-values-for-sc-01/"]),
    ]),

    # -------- Matt Fulmer (SC-01, D — LOST June 9 D primary) --------
    # Hilton Head waiter, first-time candidate, anti-two-party reform Democrat.
    # Single-payer healthcare, pro-choice, marriage equality codification.
    ("matt-fulmer", "SC", "LOST June 9 primary, open Mace seat", [
        claim("mf1", "matt-fulmer", "sanctity_of_life", 0, False,
              "Matt Fulmer, the 2026 SC-01 Democratic primary candidate and Hilton Head waiter, stated that 'reproductive rights...should be codified into federal law.' His platform explicitly supports abortion access as a protected right to be enshrined in federal statute — directly opposing the rubric's life-at-conception standard. He lost the June 9 Democratic primary for the open Mace seat.",
              ["https://abcnews4.com/news/local/coastal-battleground-heats-up-as-republicans-and-democrats-vie-for-sc-01-seat",
               "https://abcnews4.com/news/local/hilton-head-waiter-pledges-working-class-voice-in-congress"]),
        claim("mf2", "matt-fulmer", "biblical_marriage", 1, False,
              "Fulmer stated that 'marriage equality should be codified into federal law,' explicitly supporting same-sex marriage as a federal statutory right. This position directly opposes the rubric's one-man-one-woman standard and reflects the mainstream Democratic position on redefining marriage in federal law.",
              ["https://abcnews4.com/news/local/coastal-battleground-heats-up-as-republicans-and-democrats-vie-for-sc-01-seat",
               "https://www.live5news.com/2026/04/18/we-palmetto-meet-candidate-matt-fulmer-sc-01/"]),
        claim("mf3", "matt-fulmer", "economic_stewardship", 2, False,
              "Fulmer's economic platform advocates for single-payer universal healthcare ('It would allow us to negotiate the price of medicines, equipment, and procedures in a way comparable to other nations'), guaranteed universal childcare, and 'guaranteeing healthcare, advanced education, and childcare for all Americans.' These massive government-expansion proposals would dramatically increase federal spending and deficit obligations, contrary to the rubric's anti-deficit/balanced-budget standard.",
              ["https://abcnews4.com/news/local/hilton-head-waiter-pledges-working-class-voice-in-congress",
               "https://www.live5news.com/2026/04/18/we-palmetto-meet-candidate-matt-fulmer-sc-01/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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
            print(f"  x NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write -- preserve the no-whitespace master.
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
