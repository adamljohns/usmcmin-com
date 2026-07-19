#!/usr/bin/env python3
"""Enrichment batch 777: 5 claims for 5 WI Republican Assembly Members.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches pivot to state-level officials. This batch adds a third claim
to five WI Republican Assembly Members that already carry 2 evidence_curated
claims, continuing the bottom-of-alphabet sequence (WI is the next state
below WV in reverse-alpha order):

  Tyler August        (WI-31, Assembly Majority Leader)
  Shannon Zimmerman   (WI-30)
  Shae Sortwell       (WI-2)
  Scott Krug          (WI-72)
  Scott Allen         (WI-82)

Each new claim spans a DISTINCT rubric category not already filed per member:
  August     → biblical_marriage[2]        (AB 465, 2023 gender-affirming care ban)
  Zimmerman  → family_child_sovereignty[0] (AB 579, 2023 Parents' Bill of Rights)
  Sortwell   → election_integrity[0]       (SJR 73, 2023 voter ID constitutional amendment)
  Krug       → family_child_sovereignty[0] (AB 579, 2023 Parents' Bill of Rights)
  Allen      → biblical_marriage[2]        (AB 465, 2023 gender-affirming care ban)

Key sourced votes used:
  WI AB 465 (2023): ban on gender-affirming care for minors — Assembly 63-35
    party-line vote, October 2023; Senate 22-10; vetoed by Gov. Evers Dec 6 2023
    (jurist.org + wpr.org).
  WI AB 579 (2023): Parents' Bill of Rights — parental curriculum review,
    name/pronoun control, health-care opt-out — Assembly 62-35 party-line vote
    (wpr.org + legis.wisconsin.gov).
  WI SJR 73 (2023): Voter ID constitutional amendment (first consideration) —
    Assembly 62-35 Nov 9 2023, Senate 21-10 Nov 7 2023; approved by WI voters
    April 2025 (legis.wisconsin.gov + ballotpedia.org).

NOTE: writes scorecard.json MINIFIED to keep master ~35-36MB under
GitHub's 50MB limit.
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
    # --- Tyler August (WI-31, Assembly Majority Leader) ---
    # Existing: sanctity_of_life, self_defense
    # Adding:   biblical_marriage[2]
    ("tyler-august-wi-31", "WI", "Assembly Member", [
        claim("ta3", "tyler-august-wi-31", "biblical_marriage", 2, True,
              "Voted YES on Wisconsin Assembly Bill 465 (2023), which would prohibit "
              "physicians from performing gender-transition surgeries, administering "
              "puberty-blocking drugs, or prescribing cross-sex hormones (testosterone "
              "or estrogen) to minors for the purpose of changing a minor's body to "
              "correspond to a sex discordant with their biological sex. AB 465 passed "
              "the Wisconsin State Assembly on a 63-35 party-line vote in October 2023, "
              "with all Republicans voting in favor and all Democrats voting against. "
              "The Wisconsin Senate subsequently passed the bill 22-10, also along "
              "strict party lines with every Republican senator voting YES. As Assembly "
              "Majority Leader, August was integral to advancing the bill through the "
              "chamber. Democratic Gov. Tony Evers vetoed AB 465 in a private ceremony "
              "on December 6, 2023, but the lopsided Republican supermajority vote "
              "establishes August's clear and documented rejection of the transgender "
              "ideology that the rubric opposes.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.jurist.org/news/2023/10/wisconsin-state-assembly-passes-ban-on-gender-affirming-care-for-minors-and-limit-on-transgender-sports-participation/",
               "https://www.wpr.org/news/wisconsin-assembly-gender-healthcare-transgender-sports"]),
    ]),

    # --- Shannon Zimmerman (WI-30) ---
    # Existing: sanctity_of_life, election_integrity
    # Adding:   family_child_sovereignty[0]
    ("shannon-zimmerman-wi-30", "WI", "Assembly Member", [
        claim("sz3", "shannon-zimmerman-wi-30", "family_child_sovereignty", 0, True,
              "Voted YES on Wisconsin Assembly Bill 579 (2023), the 'Parents' Bill of "
              "Rights,' which passed the Wisconsin State Assembly 62-35 on a strict "
              "party-line vote with all Republicans voting in favor. AB 579 guarantees "
              "parents the right to review all instructional materials before they are "
              "presented to their child, including a full list of curriculum content "
              "touching on controversial topics. It grants parents an unconditional "
              "right to opt their child out of such instruction and requires school "
              "staff to use only the name and pronouns that parents designate for their "
              "child — not a name or pronouns the child has chosen contrary to parental "
              "wishes. The bill also guarantees parents control over all health care "
              "services, including vaccinations, that may be administered to their child "
              "at school. Democratic Gov. Tony Evers vetoed AB 579 as targeting LGBTQ+ "
              "students, but Zimmerman's party-line YES vote marks a firm commitment to "
              "parental authority over children's education and medical care — the core "
              "concern of the family-sovereignty rubric.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab579",
               "https://www.wpr.org/education/assembly-republicans-approve-bill-to-let-parents-opt-kids-out-of-controversial-lessons"]),
    ]),

    # --- Shae Sortwell (WI-2) ---
    # Existing: sanctity_of_life, self_defense
    # Adding:   election_integrity[0]
    ("shae-sortwell-wi-2", "WI", "Assembly Member", [
        claim("sso3", "shae-sortwell-wi-2", "election_integrity", 0, True,
              "Voted YES on Wisconsin Senate Joint Resolution 73 (2023), the first "
              "legislative consideration of a proposed constitutional amendment to "
              "enshrine Wisconsin's photo voter ID requirement directly in the state "
              "constitution. SJR 73 would add language to Article III of the Wisconsin "
              "Constitution requiring that no qualified elector may cast a ballot in "
              "any election unless the elector presents valid photographic "
              "identification issued by the state, the federal government, a federally "
              "recognized American Indian tribe or band in the state, or a college or "
              "university in the state. The Wisconsin State Assembly passed SJR 73 "
              "62-35 on November 9, 2023, with Republicans voting unanimously in favor; "
              "the Senate had approved the resolution 21-10 on November 7, 2023. Under "
              "Wisconsin's two-session constitutional amendment process, the 2025 "
              "legislature approved SJR 73 for a second time, placing it before "
              "Wisconsin voters; on April 1, 2025, Wisconsin voters approved the "
              "amendment by a wide margin, enshrining voter photo ID as a constitutional "
              "requirement. Sortwell's YES vote in the first consideration is a core "
              "election-integrity position the rubric supports.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/sjr73",
               "https://ballotpedia.org/Wisconsin_Question_1,_Require_Voter_Photo_ID_Amendment_(April_2025)",
               "https://www.wpr.org/news/voter-identification-constitutional-amendment-wisconsin"]),
    ]),

    # --- Scott Krug (WI-72) ---
    # Existing: self_defense, sanctity_of_life
    # Adding:   family_child_sovereignty[0]
    ("scott-krug-wi-72", "WI", "Assembly Member", [
        claim("skr3", "scott-krug-wi-72", "family_child_sovereignty", 0, True,
              "Voted YES on Wisconsin Assembly Bill 579 (2023), the 'Parents' Bill of "
              "Rights,' which passed the Wisconsin State Assembly 62-35 on a strict "
              "party-line vote with all Republicans voting in favor. AB 579 guarantees "
              "parents the right to inspect all curriculum and instructional materials "
              "proposed for use with their child, with an unconditional right to opt "
              "the child out of any lesson touching on controversial topics. It "
              "mandates that school staff use only the name and pronouns that parents "
              "designate for their child — blocking school personnel from socially "
              "transitioning a child behind parents' backs. The bill also places "
              "control over all health services administered at school, including "
              "vaccination decisions, firmly with parents rather than school "
              "administrators. Democratic Gov. Tony Evers vetoed the bill, framing "
              "its name-and-pronoun provision as harmful to LGBTQ+ students; "
              "Krug's party-line YES vote demonstrates his consistent support for "
              "parental rights over children's schooling and medical care.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab579",
               "https://www.wpr.org/education/assembly-republicans-approve-bill-to-let-parents-opt-kids-out-of-controversial-lessons"]),
    ]),

    # --- Scott Allen (WI-82) ---
    # Existing: sanctity_of_life, self_defense
    # Adding:   biblical_marriage[2]
    ("scott-allen-wi-82", "WI", "Assembly Member", [
        claim("sca3", "scott-allen-wi-82", "biblical_marriage", 2, True,
              "Voted YES on Wisconsin Assembly Bill 465 (2023), which would have "
              "banned physicians from performing gender-transition surgeries, "
              "prescribing puberty-blocking drugs, or administering cross-sex "
              "hormones to anyone under 18 in Wisconsin for the purpose of changing "
              "a minor's body to correspond to a sex discordant with their biological "
              "sex. AB 465 passed the Wisconsin State Assembly 63-35 in October 2023 "
              "on a strict party-line vote, with all Republicans voting YES and all "
              "Democrats voting against. The Wisconsin Senate passed the bill 22-10 "
              "along identical party lines. Democratic Gov. Tony Evers vetoed AB 465 "
              "on December 6, 2023. Allen's YES vote aligns with the rubric's "
              "insistence that transgender ideology — specifically its medical "
              "application to children — must be rejected, and places him alongside "
              "the full Republican caucus in affirming that a child's biological sex "
              "may not be surgically or hormonally altered by the medical establishment.",
              ["https://docs.legis.wisconsin.gov/2023/proposals/ab465",
               "https://www.jurist.org/news/2023/10/wisconsin-state-assembly-passes-ban-on-gender-affirming-care-for-minors-and-limit-on-transgender-sports-participation/",
               "https://www.wpr.org/news/wisconsin-assembly-gender-healthcare-transgender-sports"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug-collision bugs.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
