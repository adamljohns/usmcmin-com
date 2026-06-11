#!/usr/bin/env python3
"""Enrichment batch 132: hand-curated claims for 5 sitting U.S. Representatives.

Targets evidence_federal representatives with 0 claims taken from the bottom
of the alphabet (FL + CO states) after the archetype_curated federal bucket
was exhausted at batch 131.

Targets (all R): Maria Elvira Salazar (FL-27), Laurel Lee (FL-15),
John Rutherford (FL-5), Gabe Evans (CO-8), Jeff Hurd (CO-3).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- Maria Elvira Salazar (FL-27, US Representative) ----------------
    ("maria-elvira-salazar", "FL", "representative", [
        claim("mes1", "maria-elvira-salazar", "sanctity_of_life", 0, True,
              "Holds 100% rating from SBA Pro-Life America and National Right to Life Committee; voted for One Big Beautiful Bill (H.R.1, July 2025), the first federal law to defund Planned Parenthood of Medicaid dollars.",
              ["https://sbaprolife.org/representative/maria-elvira-salazar",
               "https://en.wikipedia.org/wiki/Maria_Elvira_Salazar"]),
        claim("mes2", "maria-elvira-salazar", "election_integrity", 0, True,
              "Voted YES on H.R. 8281 — Safeguard American Voter Eligibility (SAVE) Act (April 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections.",
              ["https://ballotpedia.org/Maria_Elvira_Salazar"]),
        claim("mes3", "maria-elvira-salazar", "self_defense", 1, False,
              "Joined 7 other Republicans in voting for the Bipartisan Background Checks Act of 2021 (H.R.8), expanding federal background-check requirements to all commercial firearm transfers — contrary to the rubric's opposition to new gun restrictions.",
              ["https://en.wikipedia.org/wiki/Maria_Elvira_Salazar"]),
    ]),

    # ---------------- Laurel Lee (FL-15, US Representative) ----------------
    ("laurel-lee", "FL", "representative", [
        claim("ll1", "laurel-lee", "sanctity_of_life", 0, True,
              "Carries 100% rating from SBA Pro-Life America; voted consistently to protect life and defund Big Abortion businesses including Planned Parenthood of Medicaid dollars via H.R.1 One Big Beautiful Bill (July 2025).",
              ["https://sbaprolife.org/representative/laurel-lee",
               "https://www.congress.gov/member/laurel-lee/L000597"]),
        claim("ll2", "laurel-lee", "election_integrity", 0, True,
              "Former Florida Secretary of State (2018–2022) who built the state's election-security infrastructure; introduced a constitutional amendment in the 119th Congress (2025) restricting federal voting eligibility to U.S. citizens only.",
              ["https://ballotpedia.org/Laurel_Lee",
               "https://www.congress.gov/member/laurel-lee/L000597"]),
    ]),

    # ---------------- John Rutherford (FL-5, US Representative) ----------------
    ("john-rutherford", "FL", "representative", [
        claim("jr1", "john-rutherford", "sanctity_of_life", 0, True,
              "Ranked as a pro-life champion by SBA Pro-Life America; voted for H.R.1 (One Big Beautiful Bill, July 2025), the first federal law to defund Planned Parenthood of Medicaid dollars.",
              ["https://sbaprolife.org/representative/john-rutherford",
               "https://en.wikipedia.org/wiki/John_Rutherford_(Florida_politician)"]),
        claim("jr2", "john-rutherford", "border_immigration", 1, True,
              "Defended Trump administration's family-separation immigration enforcement policy in 2018, opposing legislation to halt it; has consistently backed mandatory deportation enforcement at the southern border.",
              ["https://en.wikipedia.org/wiki/John_Rutherford_(Florida_politician)"]),
        claim("jr3", "john-rutherford", "self_defense", 0, True,
              "Introduced the Federal Firearms Licensee Protection Act of 2025, legislation to protect federally licensed gun dealers from frivolous civil litigation.",
              ["https://www.congress.gov/member/john-rutherford/R000609"]),
    ]),

    # ---------------- Gabe Evans (CO-8, US Representative) ----------------
    ("gabe-evans", "CO", "representative", [
        claim("ge1", "gabe-evans", "border_immigration", 1, False,
              "Cosponsored the DIGNIDAD Act (2026), proposing legal status for up to 12 million illegal immigrants currently in the country — directly contrary to mandatory deportation.",
              ["https://en.wikipedia.org/wiki/Gabe_Evans"]),
        claim("ge2", "gabe-evans", "sanctity_of_life", 0, False,
              "Stated that the question of whether to ban abortion access should be left entirely to states, opposing any federal life-at-conception or personhood law.",
              ["https://ballotpedia.org/Gabe_Evans"]),
        claim("ge3", "gabe-evans", "self_defense", 0, True,
              "Teaches a concealed carry class in Colorado's 8th Congressional District and has publicly supported the right of law-abiding citizens to carry firearms.",
              ["https://www.govtrack.us/congress/members/gabe_evans/456984",
               "https://en.wikipedia.org/wiki/Gabe_Evans"]),
    ]),

    # ---------------- Jeff Hurd (CO-3, US Representative) ----------------
    ("jeff-hurd", "CO", "representative", [
        claim("jh1", "jeff-hurd", "sanctity_of_life", 0, True,
              "Voted YES on H.R.1 (One Big Beautiful Bill, July 2025), the first federal law to defund Planned Parenthood of Medicaid dollars — describing the bill as delivering 'key priorities we campaigned on.'",
              ["https://www.gjsentinel.com/news/western_colorado/cd3-house-rep-jeff-hurd-a-yes-vote-for-trumps-big-beautiful-bill/article_9c67b3c7-c9bb-4894-b605-3a4bd221ffaf.html",
               "https://coloradosun.com/2025/07/03/colorado-votes-big-beautiful-bill-congress/"]),
        claim("jh2", "jeff-hurd", "border_immigration", 0, True,
              "Voted YES on H.R.1 (One Big Beautiful Bill, July 2025), which directed approximately $150 billion toward border wall construction, military deployment, and immigration enforcement.",
              ["https://coloradosun.com/2025/07/03/colorado-votes-big-beautiful-bill-congress/",
               "https://www.gjsentinel.com/news/western_colorado/cd3-house-rep-jeff-hurd-a-yes-vote-for-trumps-big-beautiful-bill/article_9c67b3c7-c9bb-4894-b605-3a4bd221ffaf.html"]),
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
