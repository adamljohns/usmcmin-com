#!/usr/bin/env python3
"""Enrichment batch 238: hand-curated claims for 5 federal House members.

Targets archetype_party_default U.S. Representatives with 0 claims, taken
from the BOTTOM of the alphabet (TX, NV×3, NM) to avoid collision with the
top-of-alphabet enrichment loop.

Mix (1 R / 4 D): Tony Gonzales (TX-R), Susie Lee (NV-D), Steven Horsford
(NV-D), Dina Titus (NV-D), Teresa Leger Fernandez (NM-D).
Each claim cites >=1 reliable source and reflects 2022-2025 voting record /
public positions.

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
    # ---------------- Tony Gonzales (TX-23, R) ----------------
    ("tony-gonzales", "TX", "U.S. Representative", [
        claim("tg1", "tony-gonzales", "self_defense", 1, False,
              "Voted YES on the Bipartisan Safer Communities Act (2022) — one of only 14 Republicans — which expands background checks for gun buyers under 21, funds state red-flag law programs, and closes the 'boyfriend loophole.' The Texas GOP censured him in March 2023 partly for this vote.",
              ["https://gonzalez.house.gov/media/press-releases/congressman-gonzalez-votes-bipartisan-safer-communities-act-keep-our-children",
               "https://ballotpedia.org/Tony_Gonzales"]),
        claim("tg2", "tony-gonzales", "biblical_marriage", 0, False,
              "The only Texas Republican to vote for the Respect for Marriage Act (2022), which codifies federal recognition of same-sex unions and requires interstate recognition. The Texas Republican Party censured him 57-5 in March 2023, citing this vote as violating principles of 'traditional marriage of a natural man and a natural woman.'",
              ["https://texasgop.org/resolution-censuring-congressman-tony-gonzales-by-the-republican-party-of-texas/",
               "https://www.foxnews.com/politics/texas-gop-votes-censure-rep-tony-gonzalez-over-votes-same-sex-marriage-guns-border-security"]),
    ]),

    # ---------------- Susie Lee (NV-03, D) ----------------
    ("susie-lee", "NV", "US House", [
        claim("sl1", "susie-lee", "sanctity_of_life", 0, False,
              "Supports abortion access through 24 weeks, calling it 'a woman's decision with her doctor,' and opposes any legal recognition of fetal personhood from conception; made abortion protection a centerpiece of her 2024 re-election campaign.",
              ["https://ballotpedia.org/Susie_Lee",
               "https://reproductivefreedomforall.org/lawmaker/susie-lee/"]),
        claim("sl2", "susie-lee", "self_defense", 1, False,
              "Signed three discharge petitions to force House floor votes on gun-control measures blocked by Republican leadership, and voted for the Bipartisan Safer Communities Act (2022), which funds red-flag law programs and expands background checks — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://susielee.house.gov/media/press-releases/congresswoman-lee-signs-three-discharge-petitions-bring-common-sense-gun-safety",
               "https://ballotpedia.org/Bipartisan_Safer_Communities_Act_of_2022"]),
    ]),

    # ---------------- Steven Horsford (NV-04, D) ----------------
    ("steven-horsford", "NV", "US House", [
        claim("sh1", "steven-horsford", "sanctity_of_life", 0, False,
              "Cosponsored the Women's Health Protection Act (WHPA), which would establish a federal statutory right to abortion and preempt state pro-life laws; Reproductive Freedom for All (NARAL successor) has celebrated his elections as victories for reproductive freedom and describes him as 'a true leader for reproductive freedom.'",
              ["https://reproductivefreedomforall.org/news/naral-pro-choice-america-celebrates-steven-horsfords-reelection-u-s-house-representatives/",
               "https://ballotpedia.org/Steven_Horsford"]),
        claim("sh2", "steven-horsford", "self_defense", 1, False,
              "Signed three discharge petitions to force a full House vote on gun-control measures currently blocked by Republican leadership — directly opposing the rubric's principle of protecting Second Amendment rights from new restrictions.",
              ["https://horsford.house.gov/issues/public-safety",
               "https://ballotpedia.org/Steven_Horsford"]),
    ]),

    # ---------------- Dina Titus (NV-01, D) ----------------
    ("dina-titus", "NV", "US House", [
        claim("dt1", "dina-titus", "sanctity_of_life", 0, False,
              "Vocal supporter of abortion access who received a 2024 score of 100 from Reproductive Freedom for All (NARAL successor), indicating a consistent pro-abortion voting record and rejection of any fetal personhood recognition from conception.",
              ["https://reproductivefreedomforall.org/lawmaker/dina-titus/",
               "https://ballotpedia.org/Dina_Titus"]),
        claim("dt2", "dina-titus", "biblical_marriage", 0, False,
              "A cosponsor of the Respect for Marriage Act (2022) and lead sponsor of the GLOBE Act promoting LGBTQ rights as U.S. foreign policy; endorsed by the Human Rights Campaign and a member of the House LGBTQ+ Equality Caucus — consistently advancing same-sex marriage and LGBTQ ideology in law and policy.",
              ["https://www.hrc.org/news/hrc-endorses-rep-dina-titus",
               "https://titus.house.gov/press-releases/titus-statement-on-supreme-court-marriage-equality-case-decision"]),
    ]),

    # ---------------- Teresa Leger Fernandez (NM-03, D) ----------------
    ("teresa-leger-fernandez", "NM", "US House", [
        claim("tf1", "teresa-leger-fernandez", "self_defense", 1, False,
              "Supports comprehensive gun control including universal background checks on all gun sales, a federal red-flag law, closing the 'boyfriend loophole,' and reinstating the assault weapons ban; co-sponsored the Background Check Expansion Act.",
              ["https://www.ontheissues.org/House/Teresa_Leger_Fernandez_Gun_Control.htm",
               "https://ballotpedia.org/Teresa_Leger_Fernandez"]),
        claim("tf2", "teresa-leger-fernandez", "sanctity_of_life", 0, False,
              "Consistently voted against pro-life protections: opposed the 2025 reconciliation bill (H.R. 1) that would have defunded Planned Parenthood, and voted to protect federal abortion-access funding — rejecting any recognition of personhood from conception.",
              ["https://sbaprolife.org/representative/teresa-leger-fernandez",
               "https://ballotpedia.org/Teresa_Leger_Fernandez"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
