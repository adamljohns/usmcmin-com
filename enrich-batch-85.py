#!/usr/bin/env python3
"""Enrichment batch 85: evidence-curate 5 Democrat mayors (bottom of alphabet bucket).

Targets archetype_curated city mayors with 0 claims, taken from the BOTTOM of the
reverse-alpha-sorted bucket (TX, TN states) to avoid collision with the top-of-alpha
enrichment agent.

Targets: Kirk Watson (Austin TX), John Whitmire (Houston TX),
         Freddie O'Connell (Nashville TN), Gina Ortiz Jones (San Antonio TX),
         Paul Young (Memphis TN).

All claims sourced from 2024-2026 public record. All five are D mayors whose
positions score False (do not align) against the God-First/America-First rubric.

NOTE: writes scorecard.json MINIFIED to stay under GitHub's 50MB limit.
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
    # ---------------- Kirk Watson (TX-D, Mayor of Austin) ----------------
    ("kirk-watson-mayor", "TX", "Mayor", [
        claim("kw1", "kirk-watson-mayor", "sanctity_of_life", 0, False,
              "Championed the Austin Reproductive Justice Fund ($400K, FY2024-25 budget) to subsidize out-of-state abortion travel for Texas women, publicly attacking AG Paxton for 'undermining the fundamental rights of women' and vowing to fight for reproductive rights in City Hall — rejecting any life-at-conception standard.",
              ["https://austinmonitor.com/stories/2024/09/austin-plans-to-move-forward-with-abortion-travel-fund-officials-say/",
               "https://www.kut.org/austin/2024-08-30/austin-tx-city-council-abortion-travel-fund"]),
        claim("kw2", "kirk-watson-mayor", "border_immigration", 2, False,
              "Declared in December 2024 that Austin police were not participating in Trump administration immigration enforcement operations, maintaining the city's non-cooperation stance with federal immigration authorities — the opposite of anti-sanctuary policy.",
              ["https://www.texastribune.org/2024/12/18/austin-mayor-kirk-watson/"]),
        claim("kw3", "kirk-watson-mayor", "biblical_marriage", 2, False,
              "Pledged as mayor to convene LGBTQ+ community leaders, university officials, and legislators to replace state-cut LGBTQ services and described university LGBTQ centers as 'life-saving' — affirming LGBTQ identity and declining to reject transgender ideology.",
              ["https://justfacts.votesmart.org/candidate/57991/kirk-watson"]),
    ]),

    # ---------------- John Whitmire (TX-D, Mayor of Houston) ----------------
    ("john-whitmire-mayor", "TX", "Mayor", [
        claim("jw1", "john-whitmire-mayor", "sanctity_of_life", 0, False,
              "Carried a 100 percent pro-abortion-rights voting record throughout his 40-year Texas Senate career, opposing all legislative restrictions on abortion and supporting abortion access — rejecting any recognition of life at conception.",
              ["https://justfacts.votesmart.org/candidate/key-votes/5464/john-whitmire/2/abortion",
               "https://ballotpedia.org/John_Whitmire"]),
        claim("jw2", "john-whitmire-mayor", "border_immigration", 2, False,
              "Led Houston City Council to adopt a sanctuary-style ordinance in April 2026 directing Houston police not to detain individuals solely on civil immigration warrants; the measure triggered a lawsuit from Texas AG Paxton and a $110M funding threat from Gov. Abbott — the opposite of anti-sanctuary enforcement.",
              ["https://www.click2houston.com/news/local/2026/04/22/houston-city-council-passes-whitmires-amended-immigration-ordinance-in-13-4-vote-to-preserve-state-funding/",
               "https://www.texastribune.org/2026/04/15/texas-houston-police-ice-city-policy/"]),
    ]),

    # ---------------- Freddie O'Connell (TN-D, Mayor of Nashville) ----------------
    ("freddie-oconnell", "TN", "Mayor", [
        claim("fo1", "freddie-oconnell", "border_immigration", 2, False,
              "Issued Nashville Executive Order No. 030 requiring Metro agencies to report all communications with federal immigration authorities within 24 hours — limiting ICE cooperation and drawing federal investigations from two House committees and a DHS 'sanctuary jurisdictions' designation in 2025.",
              ["https://www.nashville.gov/departments/metro-clerk/legal-resources/executive-orders/mayor-freddie-oconnell/fo030",
               "https://www.axios.com/local/nashville/2025/06/09/nashville-mayor-immigration-executive-order"]),
        claim("fo2", "freddie-oconnell", "sanctity_of_life", 4, False,
              "Endorsed by Tennessee Advocates for Planned Parenthood in his 2023 mayoral campaign — placing him within the Planned Parenthood endorsement network, directly contrary to the rubric's requirement that candidates have never taken PP/NARAL endorsements or money.",
              ["https://ballotpedia.org/Freddie_O%27Connell"]),
        claim("fo3", "freddie-oconnell", "self_defense", 1, False,
              "Distributed more than 10,000 gun locks at Metro Nashville Public Health Centers, framing safe-storage mandates as a public-health intervention — a gun-control initiative inconsistent with the rubric's opposition to new firearm restrictions.",
              ["https://www.nashville.gov/departments/mayor/news/numbers-2024-accomplishments-oconnell-administration"]),
    ]),

    # ---------------- Gina Ortiz Jones (TX-D, Mayor of San Antonio) ----------------
    ("gina-ortiz-jones-mayor", "TX", "Mayor", [
        claim("goj1", "gina-ortiz-jones-mayor", "sanctity_of_life", 4, False,
              "Endorsed by NARAL Pro-Choice America (now Reproductive Freedom for All) during her 2018 and 2020 congressional campaigns, running as a champion for 'full, safe, and affordable access to reproductive health services' including abortion — placing her within the abortion-industry endorsement network the rubric disqualifies.",
              ["https://reproductivefreedomforall.org/news/naral-celebrates-gina-ortiz-jones/",
               "https://ballotpedia.org/Gina_Ortiz_Jones"]),
        claim("goj2", "gina-ortiz-jones-mayor", "biblical_marriage", 0, False,
              "The first openly lesbian mayor of San Antonio, celebrated by the LGBTQ Victory Institute as a landmark election — a self-identification irreconcilable with the rubric's one-man-one-woman definition of marriage.",
              ["https://victoryinstitute.org/team/san-antonio-mayor-gina-ortiz-jones/",
               "https://en.wikipedia.org/wiki/Gina_Ortiz_Jones"]),
    ]),

    # ---------------- Paul Young (TN-D, Mayor of Memphis) ----------------
    ("paul-young-mayor", "TN", "Mayor", [
        claim("py1", "paul-young-mayor", "self_defense", 0, False,
              "Member of Mayors Against Illegal Guns (Everytown's national gun-control coalition) and created the Black Mayors' Coalition on Crime with Everytown to advance gun safety legislation at local, state, and federal levels — directly opposing constitutional-carry and unrestricted Second Amendment rights.",
              ["https://mayors.everytown.org/press/everytown-celebrates-mayors-against-illegal-guns-member-paul-young-for-creating-black-mayors-coalition-on-crime-uniting-dozens-of-leaders-in-nationwide-fight-for-public-safety/",
               "https://everytownsupportfund.org/mayor-paul-young-memphis-tennessee/"]),
        claim("py2", "paul-young-mayor", "border_immigration", 1, False,
              "Negotiated with Trump administration federal agencies to redirect immigration enforcement away from deportations and toward violent-crime investigations in Memphis, explicitly opposing mass deportation — rejecting the rubric's position that deportation of illegal immigrants should be mandatory.",
              ["https://www.newsweek.com/memphis-mayor-paul-young-ice-national-guard-trump-11684300",
               "https://mlk50.com/2025/02/07/as-deportation-fears-spread-memphis-mayor-promises-to-focus-elsewhere/"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
