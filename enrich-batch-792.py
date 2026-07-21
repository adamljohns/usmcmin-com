#!/usr/bin/env python3
"""Enrichment batch 792: sanctity_of_life third claim for 5 WI Republican Assembly Members.

Primary archetype_curated federal pool was fully depleted by batch 757.
Recent batches pivot to state-level officials adding a third claim to WI
Republican Assembly members that already carry 2 evidence_curated claims.
This batch adds sanctity_of_life entries to the 5 remaining Assembly members
missing that category:

  Jerry O'Connor    (WI-60) — co-introduced 2023 Born Alive Infant Protection Act (AB 63)
  David Armstrong   (WI-67) — co-introduced 2024 14-week abortion restriction bill (AB 975)
  Duke Tucker       (WI-75) — 2024 campaign voter-guide statements recognizing unborn personhood
  Dean Kaufert      (WI-53) — 2024 campaign support for 14-week abortion restriction referendum
  Benjamin Franklin (WI-88) — self-identified as pro-life in 2024 campaign interview

Sources: Wisconsin Legislature bill texts (legis.wisconsin.gov), Wisconsin Public Radio,
PBS NewsHour, Wisconsin Watch 2024 voter guide, Burnett County Sentinel voter guide,
The Morning Mirror (Green Bay area local press).

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
    # --- Jerry O'Connor (WI-60) ---
    # Existing: election_integrity, public_justice
    # Adding:   sanctity_of_life[0]
    ("jerry-o-connor-wi-60", "WI", "Assembly Member", [
        claim("jo3", "jerry-o-connor-wi-60", "sanctity_of_life", 0, True,
              "Co-introduced Wisconsin Assembly Bill 63 (2023), the Born Alive Infant "
              "Protection Act, which requires any health care provider present when an "
              "infant is born alive during or following an abortion or attempted abortion "
              "to provide the same degree of professional skill, care, and diligence that "
              "a reasonably conscientious provider would render to any other child born "
              "alive at the same gestational age, and to ensure the child is immediately "
              "transported and admitted to a hospital — with criminal penalties for "
              "non-compliance. The Wisconsin State Assembly passed AB 63 on a "
              "near-party-line vote; the Wisconsin State Senate approved it 19-12 with "
              "every Republican senator voting in favor. Democratic Governor Tony Evers "
              "vetoed the bill. O'Connor's co-authorship of AB 63 documents a foundational "
              "pro-life conviction: that a child born alive — regardless of the "
              "circumstances of birth — is a person possessing a legally enforceable right "
              "to medical care equal to any other newborn, and that no political or medical "
              "objective may override the duty of care owed to that born-alive child.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab63",
               "https://www.wpr.org/health/wisconsin-assembly-passes-born-alive-bill",
               "https://www.wpr.org/health/wisconsin-senate-passes-born-alive-abortion-bill"]),
    ]),

    # --- David Armstrong (WI-67) ---
    # Existing: election_integrity, economic_stewardship
    # Adding:   sanctity_of_life[1]
    ("david-armstrong-wi-67", "WI", "Assembly Member", [
        claim("da3", "david-armstrong-wi-67", "sanctity_of_life", 1, False,
              "Co-introduced Wisconsin Assembly Bill 975 (January 2024), which would have "
              "prohibited abortion in Wisconsin once the probable post-fertilization age of "
              "an unborn child reaches 14 weeks and required the question to be placed "
              "before Wisconsin voters in a referendum at the April 2024 election. The bill "
              "passed the Assembly 53-46 on a largely party-line vote but was not sent to "
              "the governor. While Armstrong's co-authorship reflects a commitment to "
              "restrict abortion access and protect fetal life after 14 weeks, the bill "
              "is a restrictions-based measure — allowing abortions up to 14 weeks — "
              "rather than the full abolition of abortion the God-First rubric's "
              "abolition-not-restrictions standard holds as the ideal.",
              ["https://docs.legis.wisconsin.gov/2023/related/proposals/ab975",
               "https://www.pbs.org/newshour/politics/wisconsin-republicans-approve-bill-banning-abortions-after-14-weeks-of-pregnancy"]),
    ]),

    # --- Duke Tucker (WI-75) ---
    # Existing: self_defense, family_child_sovereignty
    # Adding:   sanctity_of_life[0]
    ("duke-tucker-wi-75", "WI", "Assembly Member", [
        claim("dt3", "duke-tucker-wi-75", "sanctity_of_life", 0, True,
              "In his 2024 campaign voter-guide responses, Tucker articulated an implicit "
              "pro-life understanding of the abortion debate, arguing that 'the unborn "
              "also have their \"reproductive rights\" terminated when aborted' and that "
              "'Unborn women would love to chime in on their health concerns before being "
              "killed.' These statements reflect a recognition that the unborn are persons "
              "with rights — a foundational premise of the life-at-conception/personhood "
              "position the God-First rubric requires. Tucker was elected to represent "
              "Wisconsin's 75th Assembly District in November 2024 and took office in "
              "January 2025.",
              ["https://www.burnettcountysentinel.com/news/kleiss-tucker-face-off-in-new-75th-assembly-district/article_1dee231a-916b-11ef-b058-8baf14f61c5c.html",
               "https://ballotpedia.org/Duke_Tucker"]),
    ]),

    # --- Dean Kaufert (WI-53) ---
    # Existing: economic_stewardship, family_child_sovereignty
    # Adding:   sanctity_of_life[1]
    ("dean-kaufert-wi-53", "WI", "Assembly Member", [
        claim("dk3", "dean-kaufert-wi-53", "sanctity_of_life", 1, False,
              "In his 2024 campaign for Wisconsin's 53rd Assembly District, Kaufert ran "
              "on a conservative platform that included support for a 14-week abortion "
              "restriction referendum — mirroring the approach taken by Assembly Bill 975 "
              "(January 2024), which passed the Assembly 53-46 on a party-line vote. While "
              "this position reflects a commitment to restrict abortion access, advocacy "
              "for a gestational-limit restriction is a restrictions-based strategy rather "
              "than full abolition of abortion, which the God-First rubric's "
              "abolition-not-restrictions standard holds as the ideal. Kaufert defeated "
              "his Democratic opponent on November 5, 2024, and took office in January 2025.",
              ["https://wisconsinwatch.org/2024/11/wisconsin-assembly-republican-democrat-kaufert-shukoski-fox-valley-neenah-menasha/",
               "https://ballotpedia.org/Dean_Kaufert"]),
    ]),

    # --- Benjamin Franklin (WI-88) ---
    # Existing: family_child_sovereignty, refuse_state_overreach
    # Adding:   sanctity_of_life[0]
    ("benjamin-franklin-wi-88", "WI", "Assembly Member", [
        claim("bf3", "benjamin-franklin-wi-88", "sanctity_of_life", 0, True,
              "During his 2024 campaign for Wisconsin's 88th Assembly District, Franklin "
              "directly stated his pro-life identity in an interview: 'My abortion [stance] "
              "is I'm pro life. I value life.' His explicit public declaration that he "
              "values life and identifies as pro-life is consistent with the "
              "sanctity-of-life principle the God-First rubric requires. Franklin won the "
              "November 5, 2024 election and was sworn into the Wisconsin State Assembly "
              "on January 6, 2025.",
              ["https://www.themorningmirror.com/localarticles/state-assembly-candidate-christy-welch-wants-to-restore-abortion-rights-opponent-ben-franklin-says-he-is-pro-life",
               "https://ballotpedia.org/Benjamin_Franklin_(Wisconsin)"]),
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
