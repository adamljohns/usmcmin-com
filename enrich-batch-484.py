#!/usr/bin/env python3
"""Enrichment batch 484: 5 Vermont Republican state senators with 0 claims.

Targets archetype_party_default senators from VT — next bottom-of-alphabet
state after WY/WV/WI/WA/VA/UT were exhausted. Senators: Randy Brock,
Scott Beck, Brian Collamore, Russ Ingalls, Richard A. Westman.
Claims drawn from 2021-2026 Vermont legislative sessions, verified via
vermontbiz.com, wcax.com, vtdigger.org, hardwickgazette.org, en.wikipedia.org,
ballotpedia.org.

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # -------- Randy Brock (VT-R, State Senator, Franklin District, Minority Leader 2020-2024) --------
    ("randy-brock", "VT", "Senator", [
        claim("rb1", "randy-brock", "self_defense", 1, True,
              "One of only 3 senators (in a 26-3-1 vote) to oppose S.209 (2024, 'ghost guns' serial-number mandate), calling the bill 'impractical' and 'ineffective' because 'only lawful gun owners would comply.' Also voted against S.329 (May 2026), a Democratic omnibus banning guns in bars, restricting machine guns, and adding a 72-hour purchase waiting period — one of 13 unified Republican no-votes in a 17-13 party-line passage.",
              ["https://vermontbiz.com/news/2024/february/28/senate-passes-s209-ghost-guns-bill",
               "https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/"]),
        claim("rb2", "randy-brock", "sanctity_of_life", 0, False,
              "Publicly pro-choice; has supported Roe v. Wade and opposes prohibition of public funds for organizations that perform abortions. Did not join the four-senator minority that voted against Vermont Proposal 5 / Article 22, the 2022 constitutional amendment enshrining a broad 'personal reproductive autonomy' right (passed Senate 26-4 in 2021 with only Collamore, Terenzini, Ingalls, and one Democrat opposed).",
              ["https://en.wikipedia.org/wiki/Randy_Brock",
               "https://ballotpedia.org/Randy_Brock_(Vermont)"]),
    ]),

    # -------- Scott Beck (VT-R, State Senator, Caledonia District, Minority Leader 2025-) --------
    ("scott-beck", "VT", "Senator", [
        claim("sb1", "scott-beck", "economic_stewardship", 2, True,
              "As newly elected Senate Minority Leader since January 2025, Beck has led Republican efforts to control Vermont's runaway education-property-tax burden: opposing the yield bill formula driving a projected 11.9% tax increase, publicly committing the caucus to 'controlling education costs and reforming Vermont's education system,' and co-leading support for the 2025 Clean Heat Standard repeal (S.68) — blocking a multi-billion-dollar regulatory mandate that would have imposed major energy-cost burdens on Vermont households.",
              ["https://hardwickgazette.org/2025/12/02/senate-house-republicans-respond-to-tax-letter/",
               "https://vtdigger.org/2025/03/14/final-reading-vermont-senate-committee-votes-to-repeal-clean-heat-standard/",
               "https://vtdigger.org/2024/11/27/vermont-senate-republicans-tap-scott-beck-as-new-caucus-leader/"]),
        claim("sb2", "scott-beck", "self_defense", 1, True,
              "Voted against S.329 (May 2026), a Democratic omnibus gun-control bill that would have banned firearms in bars statewide, restricted machine guns, and imposed a new 72-hour waiting period — as one of the 13 unified Republican senators opposing the measure in a 17-13 party-line vote.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://www.mychamplainvalley.com/news/local-news/vermont/vermont-senate-passes-two-bills-on-alcohol-gun-laws/"]),
    ]),

    # -------- Brian Collamore (VT-R, State Senator, Rutland District, Govt Ops Chair) --------
    ("brian-collamore", "VT", "Senator", [
        claim("bc1", "brian-collamore", "sanctity_of_life", 0, True,
              "One of only 2 senators (28-2 in 2019) and one of only 4 (26-4 in 2021) to vote against Vermont Proposal 5 / Article 22, the constitutional amendment embedding a broad 'personal reproductive autonomy' right in the state constitution. After the 2021 vote Collamore stated that 'the majority of constituents who contacted him about the amendment asked him to oppose it'; he is publicly described as anti-abortion, with consistent pro-life votes across both required legislative passages.",
              ["https://vtdigger.org/2019/04/04/senate-oks-abortion-rights-constitutional-amendment/",
               "https://vtdigger.org/2021/04/09/senate-approves-state-constitutional-amendments-on-slavery-abortion-rights/"]),
        claim("bc2", "brian-collamore", "self_defense", 1, True,
              "Voted against S.329 (May 2026), a Democratic omnibus gun-control bill that would have banned firearms in bars statewide, restricted machine guns, and imposed a 72-hour purchase waiting period — casting one of the 13 unified Republican no-votes in a 17-13 party-line passage.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/"]),
    ]),

    # -------- Russ Ingalls (VT-R, State Senator, Essex-Orleans District) --------
    ("russ-ingalls", "VT", "Senator", [
        claim("ri1", "russ-ingalls", "sanctity_of_life", 0, True,
              "One of only 4 senators to vote against Vermont Proposal 5 / Article 22 in its 2021 legislative passage (26-4), joining Collamore and Terenzini (both R-Rutland) and one Democrat in opposing the amendment that enshrined a broad 'personal reproductive autonomy' right in the Vermont Constitution. The amendment was subsequently adopted by 76.8% of voters in November 2022.",
              ["https://vtdigger.org/2021/04/09/senate-approves-state-constitutional-amendments-on-slavery-abortion-rights/",
               "https://ballotpedia.org/Vermont_Proposal_5,_Right_to_Personal_Reproductive_Autonomy_Amendment_(2022)"]),
        claim("ri2", "russ-ingalls", "self_defense", 1, True,
              "Voted against S.329 (May 2026), a Democratic omnibus gun-control bill that would have banned firearms in bars statewide, restricted machine guns, and imposed a new 72-hour purchase waiting period — as part of the unified 13-senator Republican bloc opposing the measure in a 17-13 party-line vote.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/"]),
    ]),

    # -------- Richard A. Westman (VT-R, State Senator, Lamoille District, Transport Chair) --------
    ("richard-a-westman", "VT", "Senator", [
        claim("rw1", "richard-a-westman", "self_defense", 1, True,
              "Voted against S.329 (May 2026), a Democratic omnibus gun-control bill that would have banned firearms in bars statewide, restricted machine guns, and imposed a new 72-hour purchase waiting period — casting one of the 13 unified Republican no-votes in a 17-13 party-line vote.",
              ["https://www.wcax.com/2026/05/07/vermont-senate-advances-statewide-ban-guns-bars/",
               "https://www.mychamplainvalley.com/news/local-news/vermont/vermont-senate-passes-two-bills-on-alcohol-gun-laws/"]),
        claim("rw2", "richard-a-westman", "public_justice", 0, False,
              "In June 2024, initially voted to sustain Gov. Phil Scott's veto of H.72 — a bill authorizing Vermont's first overdose prevention center (supervised injection facility) in Burlington — but reversed course the same afternoon and changed his vote, enabling the 20-9 veto override. He was the sole Republican who switched sides to let the overdose-injection-center bill take effect.",
              ["https://vermontbiz.com/news/2024/june/17/do-over-legislature-overrides-veto-h72-safe-injection-sites-bill",
               "https://vtdigger.org/2024/06/17/vermont-legislature-overrides-six-vetoes-in-one-day-setting-new-record/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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
