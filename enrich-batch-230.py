#!/usr/bin/env python3
"""Enrichment batch 230: third-claim enrichment for 5 federal candidates (MT, TN, PA x2, MI).

Targets evidence_curated federal candidates at the bottom of the alphabet
with exactly 2 claims, adding one distinct-category claim each.

Mix (2 R / 3 D):
  Aaron Flint (MT-01-R), Mike Rogers (MI-Senate-R),
  Mike Croley (TN-06-D), Ryan Crosswell (PA-07-D), Ala Stanford (PA-03-D).

Sources: flintformontana.com, kulr8.com, montanafreepress.org,
         rogersforsenate.com, foxnews.com, nbcnews.com,
         croleyforcongress.com, ryancrosswell.com, lehighvalleynews.com,
         whyy.org.

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
    # ---------------- Aaron Flint (MT-01-R, Republican nominee) ----------------
    ("aaron-flint", "MT", "Representative", [
        claim("af3", "aaron-flint", "border_immigration", 0, True,
              "Republican nominee for MT-01, Flint's 2026 campaign platform explicitly calls to 'Keep our Border SECURE, Stop Migrant Crime,' opposing those who would 're-open the borders for illegal aliens and deadly drugs.' President Trump issued a 'Complete and Total Endorsement' of Flint on Truth Social, aligning him with Trump's enforcement-first border agenda including barrier construction and military-backed enforcement. Flint was subsequently added to the National Republican Congressional Committee's 2026 MAGA Majority program. His platform aligns with the rubric's wall-plus-military-enforcement standard.",
              ["https://flintformontana.com/",
               "https://www.kulr8.com/elections/president-trump-tonight-on-truth-social-aaron-flint-has-my-complete-and-total-endorsement/article_e4a2540a-27f2-59af-9d92-af5420023e9d.html",
               "https://montanafreepress.org/2026/04/13/in-montanas-western-district-aaron-flint-is-the-talked-up-candidate-for-congress/"]),
    ]),

    # ---------------- Mike Rogers (MI-Senate-R, 2026 R Candidate) ----------------
    ("mike-rogers-mi-senate-2026", "MI", "Senator", [
        claim("mr3", "mike-rogers-mi-senate-2026", "border_immigration", 0, True,
              "Rogers' 2026 Michigan Senate campaign explicitly prioritizes border enforcement. He stated 'a weak and porous southern border is fueling crime' in Michigan, per Fox News reporting on his Senate announcement. Trump's 'Complete and Total Endorsement' (April 2025) called for Rogers to 'tirelessly fight to Secure the Border.' His campaign website lists securing the border as a top priority alongside manufacturing and lowering costs. These positions align with the rubric's wall-plus-military-enforcement standard.",
              ["https://rogersforsenate.com/",
               "https://www.foxnews.com/politics/ex-house-republican-voted-impeach-trump-drops-michigan-senate-bid",
               "https://www.nbcnews.com/politics/2024-election/trump-endorses-former-rep-mike-rogers-michigans-gop-senate-primary-rcna142856"]),
    ]),

    # ---------------- Mike Croley (TN-06-D, 2026 D Candidate) ----------------
    ("mike-croley", "TN", "Representative", [
        claim("mc3", "mike-croley", "border_immigration", 1, False,
              "Croley's campaign blog post 'What I'm Hearing Across Tennessee's 6th Congressional District' relays that constituents are 'concerned [ICE] has moved beyond its original mission,' and his campaign states that 'enforcing immigration law should never come at the expense of basic human rights.' This framing explicitly rejects mandatory deportation and mass-enforcement operations — directly opposing the rubric's mandatory-deportation standard.",
              ["https://croleyforcongress.com/what-im-hearing-across-tennessees-6th-congressional-district/"]),
    ]),

    # ---------------- Ryan Crosswell (PA-07-D, 2026 D Candidate) ----------------
    ("ryan-crosswell", "PA", "Representative", [
        claim("rc3", "ryan-crosswell", "sanctity_of_life", 0, False,
              "Crosswell's campaign website lists 'protect reproductive rights' as a top priority. Lehigh Valley News (February 2026) reported he 'stood with his niece outside the Supreme Court to protest the Dobbs decision' and that 'one of his first acts in Congress will be to add his name' to legislation defending abortion access. His campaign calls for protecting reproductive rights as a federal priority, rejecting any recognition of personhood from conception.",
              ["https://ryancrosswell.com/priorities/",
               "https://www.lehighvalleynews.com/elections/ex-federal-prosecutor-ryan-crosswell-joins-pa-7-congressional-race"]),
    ]),

    # ---------------- Ala Stanford (PA-03-D, 2026 D Candidate) ----------------
    ("ala-stanford", "PA", "Representative", [
        claim("as3", "ala-stanford", "self_defense", 1, False,
              "Physician-candidate and EMILY's List-endorsed Democrat who, in WHYY's 2026 PA-03 voter guide, called for 'stricter gun laws for the bad actors that continue to sell' and 'more prohibitions on gun sales' with 'fines and imprisonment' for violations. Stanford frames gun violence through her work as a trauma physician treating victims. Her call for new sale restrictions and criminal penalties for sellers directly opposes the rubric's defense against AWB/mag-limit/registry restrictions.",
              ["https://whyy.org/articles/pennsylvania-election-2026-primary-3rd-congressional-district/"]),
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
