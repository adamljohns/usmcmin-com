#!/usr/bin/env python3
"""Enrichment batch 219: third-claim enrichment for 5 bottom-of-alphabet federal candidates.

Targets (evidence_curated with 2 claims, bottom of alphabet):
  WY-D  Scott Morrow         (U.S. Senate WY 2026 D candidate)
  WY-D  James W. Byrd        (U.S. Senate WY 2026 D candidate · Lummis seat)
  WV-D  Glenn Elliott        (U.S. Senate WV 2026 D candidate)
  WI-D  Rebecca Cooke        (U.S. Representative WI-03 2026 D candidate)
  WI-D  Peter Barca          (U.S. Representative WI-01 2026 D candidate)

Each target gets one new claim in a distinct rubric category not yet covered.
Sources: WyoFile, WV Gazette Mail, PBS Wisconsin, Wisconsin Examiner / Ballotpedia.

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
    # ---------------- Scott Morrow (WY-D, U.S. Senate 2026) ----------------
    ("scott-morrow-wy-senate", "WY", "Senate", [
        claim("sm3", "scott-morrow-wy-senate", "biblical_marriage", 2, False,
              "In his 2024 Senate campaign Q&A (WyoFile 2024 Election Guide), Morrow pledged to be 'the strongest and most vocal advocate for women's equality' and to push for Senate passage of the Equal Rights Amendment — a constitutional amendment that legal advocates routinely invoke to challenge sex-distinct statutes and advance transgender-policy claims, rejecting any legislative distinction grounded in biological sex.",
              ["https://projects.wyofile.com/election-guide-2024/candidates/scott-morrow/",
               "https://en.wikipedia.org/wiki/2024_United_States_Senate_election_in_Wyoming"]),
    ]),

    # ---------------- James W. Byrd (WY-D, U.S. Senate 2026 · Lummis seat) ----------------
    ("james-w-byrd-wy-senate", "WY", "Senator", [
        claim("jb3", "james-w-byrd-wy-senate", "border_immigration", 1, False,
              "Appeared as a featured speaker at Wyoming's 'ICE Out' protest at the State Capitol in Cheyenne on February 2, 2026 — a rally explicitly calling on Wyoming officials to obstruct federal ICE deportation operations — placing him publicly on record in opposition to mandatory deportation enforcement.",
              ["https://wyofile.com/five-republicans-2-democrats-vie-for-us-senate-in-wyoming-primaries/",
               "https://ballotpedia.org/James_Byrd"]),
    ]),

    # ---------------- Glenn Elliott (WV-D, U.S. Senate WV 2026) ----------------
    ("glenn-elliott-senate", "WV", "Senate", [
        claim("ge3", "glenn-elliott-senate", "border_immigration", 1, False,
              "In his 2024 West Virginia U.S. Senate campaign, Elliott explicitly endorsed 'a path to citizenship for undocumented workers,' arguing it would strengthen Social Security by expanding the contributor base — opposing mandatory deportation in favor of normalization and legal status for illegal immigrants.",
              ["https://www.wvgazettemail.com/elections/election-2024-a-closer-look-at-glenn-elliott-jim-justice-running-for-u-s-senate/article_cdadafce-8594-11ef-9f86-af3f4bd90c59.html",
               "https://ballotpedia.org/Glenn_Elliott"]),
    ]),

    # ---------------- Rebecca Cooke (WI-D, U.S. Representative WI-03 2026) ----------------
    ("rebecca-cooke", "WI", "Representative", [
        claim("rc3", "rebecca-cooke", "election_integrity", 0, False,
              "Has publicly called for 'finally enacting the Freedom to Vote Act' — the Democratic bill that would pre-empt state photo voter-ID requirements, mandate automatic voter registration, and expand no-excuse mail-in voting nationwide — in direct opposition to the rubric's insistence on strict voter-ID and secure in-person balloting.",
              ["https://ballotpedia.org/Rebecca_Cooke",
               "https://en.wikipedia.org/wiki/Rebecca_Cooke_(politician)"]),
    ]),

    # ---------------- Peter Barca (WI-D, U.S. Representative WI-01 2026) ----------------
    ("peter-barca", "WI", "Representative", [
        claim("pb3", "peter-barca", "border_immigration", 1, False,
              "In his 2024 Wisconsin 1st-District congressional campaign, Barca called for 'pathways to citizenship' for undocumented immigrants and 'a process for refugees to seek asylum' alongside incremental border-technology improvements — explicitly rejecting mandatory deportation in favor of legalization and normalization.",
              ["https://wisconsinexaminer.com/race-details/wisconsins-1st-congressional-district/",
               "https://pbswisconsin.org/news-item/peter-barca-on-foreign-policy-and-the-2024-election/"]),
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
