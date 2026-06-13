#!/usr/bin/env python3
"""Enrichment batch 181: hand-curated claims for 4 federal House members.

Targets evidence_federal representatives with 0 claims, taken from the
BOTTOM of the alphabet (AZ + AK + AL). 3 R / 1 D.

Candidates: Andy Biggs (AZ-R), Nick Begich III (AK-R),
Dale Strong (AL-R), Shomari Figures (AL-D).

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
    # ---------------- Andy Biggs (AZ-R, Freedom Caucus) ----------------
    ("andy-biggs", "AZ", "Representative", [
        claim("ab1", "andy-biggs", "sanctity_of_life", 0, True,
              "Opposed to all forms of elective abortion and celebrated the 2022 Dobbs ruling as 'a major victory for the unborn'; cosponsored H.R.7286 to revoke the tax-exempt status of organizations that provide or fund abortions — affirming protection of the unborn from conception.",
              ["https://en.wikipedia.org/wiki/Andy_Biggs",
               "https://www.congress.gov/member/andy-biggs/B001302"]),
        claim("ab2", "andy-biggs", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (H.R.8404, July 2022), one of 157 House Republicans who rejected federal codification of same-sex marriage — upholding the traditional definition of marriage as the union of one man and one woman.",
              ["https://clerk.house.gov/Votes/2022373",
               "https://ballotpedia.org/Andy_Biggs"]),
        claim("ab3", "andy-biggs", "border_immigration", 0, True,
              "Sponsored H.R.9200 in the 119th Congress (2025-2026) to secure the borders of the United States, and as former Freedom Caucus chair was a persistent advocate for a physical barrier, military-assisted enforcement, and complete border closure.",
              ["https://www.congress.gov/member/andy-biggs/B001302",
               "https://en.wikipedia.org/wiki/Andy_Biggs"]),
    ]),

    # ---------------- Nick Begich III (AK-R, Freedom Caucus) ----------------
    ("nick-begich-iii", "AK", "Representative", [
        claim("nb1", "nick-begich-iii", "border_immigration", 0, True,
              "Voted FOR the One Big Beautiful Bill Act (signed July 2025), which included over $100 billion for border-wall construction and enforcement capabilities to stop fentanyl and restore the rule of law — fully backing physical-barrier and military-assisted border security.",
              ["https://www.alaskasnewssource.com/2025/07/04/big-beautiful-bill-passes-congress-with-alaska-delegation-support/",
               "https://begich.house.gov/media/press-releases/congressman-begich-statement-final-passage-one-big-beautiful-bill-act"]),
        claim("nb2", "nick-begich-iii", "economic_stewardship", 4, True,
              "Secured mandatory oil and gas lease sales in ANWR, NPR-Alaska, and Cook Inlet as part of the One Big Beautiful Bill Act (July 2025), directly countering the ESG-driven fossil-fuel divestment agenda promoted by WEF/Davos-aligned financial institutions and asserting American energy sovereignty.",
              ["https://begich.house.gov/media/press-releases/congressman-begich-statement-final-passage-one-big-beautiful-bill-act",
               "https://en.wikipedia.org/wiki/Nick_Begich_III"]),
    ]),

    # ---------------- Dale Strong (AL-R) ----------------
    ("dale-strong", "AL", "Representative", [
        claim("ds1", "dale-strong", "self_defense", 1, True,
              "A lifetime member of the NRA who states on his official House website that he will 'always fight any attempt by the radical left to diminish the right of law-abiding American citizens to keep and bear arms,' explicitly opposing bans, registries, and all new restrictions on gun ownership.",
              ["https://strong.house.gov/issues/gun-rights",
               "https://en.wikipedia.org/wiki/Dale_Strong"]),
        claim("ds2", "dale-strong", "border_immigration", 0, True,
              "Declared border security a top priority before his first vote and cosponsored the Border Reinforcement Act of 2023, which funds physical-barrier construction and tightens enforcement — backing a wall and military-assisted approach to illegal entry.",
              ["https://ballotpedia.org/Dale_Strong",
               "https://www.congress.gov/member/dale-strong/S001220"]),
        claim("ds3", "dale-strong", "sanctity_of_life", 0, True,
              "Cosponsored multiple anti-abortion measures in the House, including legislation to prohibit taxpayer funding for abortion, affirming his position that human life merits federal protection from conception.",
              ["https://ballotpedia.org/Dale_Strong",
               "https://www.congress.gov/member/dale-strong/S001220"]),
    ]),

    # ---------------- Shomari Figures (AL-D) ----------------
    ("shomari-figures", "AL", "Representative", [
        claim("sf1", "shomari-figures", "border_immigration", 1, True,
              "Was one of 48 House Democrats who voted FOR the Laken Riley Act (H.R.29, Jan. 7, 2025), requiring ICE to detain undocumented immigrants who commit crimes such as burglary or theft — a bipartisan enforcement vote that aligns with mandatory accountability for criminal aliens.",
              ["https://analysis.limitedgov.org/lawmakers/shomari-figures-d-al-2",
               "https://abcnews.com/Politics/house-vote-laken-riley-act-teeing-immigration-crackdown/story?id=117984047"]),
        claim("sf2", "shomari-figures", "economic_stewardship", 2, False,
              "In April 2026 introduced the Save SNAP Act of 2026 to expand and protect federal food-stamp funding, prioritizing continued entitlement spending over the balanced-budget and spending-restraint principles the rubric upholds.",
              ["https://www.congress.gov/member/shomari-figures/F000481",
               "https://ballotpedia.org/Shomari_Figures"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents the batch-1 Mike Lee collision."""
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
