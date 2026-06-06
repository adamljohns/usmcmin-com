#!/usr/bin/env python3
"""Enrichment batch 86: hand-curated claims for 3 state/gubernatorial candidates.

Targets archetype_curated candidates at the bottom of the alphabet (ME, IL, GA)
that had 0 evidence claims. Pulled from both the federal-senator bucket (exhausted —
only Joe Mazzola MA with no findable public record) and the house/representative
bucket (bottom-of-alphabet).

Targets (1 D governor candidate + 2 state house speakers, 1 R / 2 D):
  Hannah Pingree (ME-D, 2026 Governor candidate)
  Emanuel Chris Welch (IL-D, Illinois House Speaker)
  Jon Burns (GA-R, Georgia House Speaker)

Joe Mazzola (MA-R) and Drew Wilson (FL-02-R) were in the bucket but lack any
sourced 2024-2026 public record in available search results; skipped this batch.

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
    # ------------ Hannah Pingree (ME-D, 2026 Governor Candidate) ------------
    ("hannah-pingree-gov", "ME", "Governor", [
        claim("hp1", "hannah-pingree-gov", "sanctity_of_life", 0, False,
              "As Speaker of the Maine House (2008–2010) Pingree championed abortion rights and introduced legislation guaranteeing reproductive access as a human right; her 2026 gubernatorial campaign continues to defend unrestricted abortion access, rejecting any legal protection for life from conception.",
              ["https://hannahforgovernor.com/accomplishments/",
               "https://www.mainepublic.org/politics/2026-04-17/your-vote-2026-profile-hannah-pingree-democrat-for-governor"]),
        claim("hp2", "hannah-pingree-gov", "self_defense", 1, False,
              "Supported banning military-style assault weapons and high-capacity magazines, and backed universal background checks including at gun shows and private sales — directly opposing the rubric's defense of semi-automatic firearms and the right to keep and bear arms without new restrictions.",
              ["https://www.mainepublic.org/politics/2026-04-17/your-vote-2026-profile-hannah-pingree-democrat-for-governor",
               "https://en.wikipedia.org/wiki/Hannah_Pingree"]),
        claim("hp3", "hannah-pingree-gov", "biblical_marriage", 0, False,
              "Stood publicly for same-sex marriage in 2009 when many politicians avoided it — while serving as Speaker — and has since advocated for full LGBTQ nondiscrimination protections in housing, employment, and public accommodations, rejecting a one-man-one-woman definition of marriage.",
              ["https://hannahforgovernor.com/accomplishments/",
               "https://en.wikipedia.org/wiki/Hannah_Pingree"]),
    ]),

    # ------------ Emanuel Chris Welch (IL-D, Illinois House Speaker) ------------
    ("chris-welch", "IL", "Illinois", [
        claim("cw1", "chris-welch", "self_defense", 1, False,
              "As Illinois House Speaker, Welch sponsored and passed the Protect Illinois Communities Act (signed January 2023), banning the manufacture, sale, and purchase of assault weapons and high-capacity magazines and requiring existing owners to register serial numbers with Illinois State Police — directly opposing the rubric's defense of semi-automatic firearms and the right against firearms registries.",
              ["https://en.wikipedia.org/wiki/Chris_Welch_(politician)",
               "https://www.nprillinois.org/illinois/2023-01-06/illinois-house-votes-to-ban-assault-weapons-and-broaden-abortion-protections"]),
        claim("cw2", "chris-welch", "sanctity_of_life", 0, False,
              "Led the Illinois House to expand abortion access in January 2023, passing legislation broadening protections for abortion providers and their patients in answer to post-Dobbs state restrictions, cementing Illinois as an abortion-access destination state and rejecting any legal recognition of personhood from conception.",
              ["https://illinoisnewsroom.org/illinois-house-votes-to-ban-assault-weapons-and-broaden-abortion-protections/",
               "https://www.nprillinois.org/illinois/2023-01-06/illinois-house-votes-to-ban-assault-weapons-and-broaden-abortion-protections"]),
        claim("cw3", "chris-welch", "biblical_marriage", 4, False,
              "Under Welch's speakership the Illinois House advanced LGBTQ-inclusive legislation, and Welch cited LGBTQ rights as a key factor in Democrats' 2022 electoral success, reflecting active promotion of LGBTQ ideology in state policy.",
              ["https://en.wikipedia.org/wiki/Chris_Welch_(politician)",
               "https://ballotpedia.org/Chris_Welch"]),
    ]),

    # ------------ Jon Burns (GA-R, Georgia House Speaker) ------------
    ("jon-burns", "GA", "Georgia", [
        claim("jb1", "jon-burns", "sanctity_of_life", 0, True,
              "Speaker Burns issued a formal statement defending Georgia's LIFE Act (the state's six-week heartbeat abortion law) after the Georgia Supreme Court upheld it, calling the law a legislative priority and affirming the state's protection of unborn life from a detectable heartbeat — consistent with a life-from-conception posture.",
              ["https://www.gahousegop.com/heartbeatbill",
               "https://en.wikipedia.org/wiki/Jon_G._Burns"]),
        claim("jb2", "jon-burns", "self_defense", 0, True,
              "After the September 2024 Apalachee High School shooting Burns presented a gun-safety agenda explicitly framed around 'protecting the right and privilege of our citizens to protect their families and property,' limiting proposals to voluntary safe-storage incentives and rejecting any mandate — consistent with Georgia's permitless/constitutional carry law and the rubric's support for unrestricted bearing of arms.",
              ["https://www.11alive.com/article/news/special-reports/apalachee-high-shooting/georgia-house-speaker-jon-burns-legislative-priorities-apalachee-high-shooting-safe-storage-incentives/85-6a915291-2ed4-48e4-8327-eaef108f208d",
               "https://ballotpedia.org/Jon_G._Burns"]),
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
