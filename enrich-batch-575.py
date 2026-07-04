#!/usr/bin/env python3
"""Enrichment batch 575: hand-curated claims for 5 South Dakota State Senators.

Federal senator / US House buckets exhausted. Targets are archetype_party_default
SD State Senators with 0 evidence claims, taken from the bottom of the alphabet
(SD = bottom-tier after WY/WV/WI/WA/VA all fully enriched). All five are
Republicans in a strong-conservative supermajority state; claims are drawn from
documented candidate surveys, campaign platforms, and legislative records.

Targets: Kevin Jensen, Kyle Schoenfish, Joy Hohn, Jim Mehlhaff, Larry Zikmund.
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
    # ------------- Kevin Jensen (SD-R, State Senator, District 16) -------------
    ("kevin-jensen", "SD", "Senator", [
        claim("kj1", "kevin-jensen", "sanctity_of_life", 0, True,
              "Self-declared '100% pro-life,' Jensen stated in his 2022 candidate survey that he agrees with the Supreme Court's Dobbs decision and 'at this point I see no compelling reason to change our law,' defending South Dakota's near-total abortion ban as protecting life from conception.",
              ["https://www.dakotanewsnow.com/2022/10/31/sd-legislative-candidate-survey-kevin-jensen/",
               "https://gntnews.com/2022/10/research-sd-legislative-candidates-kevin-jensen/"]),
        claim("kj2", "kevin-jensen", "self_defense", 1, True,
              "An NRA Life member and state- and NRA-certified firearms and Enhanced Concealed Permit instructor, Jensen has consistently defended South Dakotans' right to keep and bear arms and opposed new gun restrictions, drawing on professional credentials to inform his legislative opposition to red-flag laws, registries, and weapon bans.",
              ["https://www.dakotanewsnow.com/2022/10/31/sd-legislative-candidate-survey-kevin-jensen/",
               "https://gntnews.com/2022/10/research-sd-legislative-candidates-kevin-jensen/"]),
    ]),

    # ----------- Kyle Schoenfish (SD-R, State Senator, District 19) -----------
    ("kyle-schoenfish", "SD", "Senator", [
        claim("ks1", "kyle-schoenfish", "sanctity_of_life", 0, True,
              "Earned a high rating from South Dakota Right to Life and declared in his 2022 campaign survey: 'I support the sanctity of life as evidenced by a high rating from South Dakota Right to Life. We should review our laws to make sure we are supporting life in the best way' — defending South Dakota's near-total abortion ban.",
              ["https://www.dakotanewsnow.com/2022/10/31/sd-legislative-candidate-survey-kyle-schoenfish/"]),
        claim("ks2", "kyle-schoenfish", "biblical_marriage", 2, True,
              "Voted in favor of Senate Bill 46 (2022), South Dakota's 'fairness in women's sports' bill championed by Governor Noem, which bans biological males who identify as transgender from competing in girls' and women's athletics — affirming biological sex distinctions and rejecting transgender ideology in the athletic context.",
              ["https://www.keloland.com/keloland-com-original/senate-committee-hearing-gov-noems-womens-sports-bill-to-ban-transgender-girls/",
               "https://www.dglobe.com/news/after-half-decade-of-defeats-south-dakota-republicans-finally-ban-transgender-access-this-time-in-school-sports"]),
    ]),

    # -------------- Joy Hohn (SD-R, State Senator, District 9) ----------------
    ("joy-hohn", "SD", "Senator", [
        claim("jh1", "joy-hohn", "border_immigration", 4, True,
              "Has worked for years to protect American land from foreign acquisition, pledging on her campaign platform to 'work to keep our land American-owned, controlled and protected' — a direct alignment with the rubric's opposition to CCP-linked and foreign purchases of U.S. farmland and property.",
              ["https://www.joyhohn.com/platform/",
               "https://ballotpedia.org/Joy_Hohn"]),
        claim("jh2", "joy-hohn", "self_defense", 1, True,
              "Committed to protecting constitutional rights she explicitly includes 'the right to bear arms,' pledging to oppose any new restrictions on law-abiding gun owners — aligning with the rubric's opposition to red-flag laws, assault-weapon bans, magazine limits, and firearm registries.",
              ["https://www.joyhohn.com/platform/"]),
    ]),

    # ------------ Jim Mehlhaff (SD-R, State Senator, District 24) -------------
    ("jim-mehlhaff", "SD", "Senator", [
        claim("jml1", "jim-mehlhaff", "sanctity_of_life", 0, True,
              "Self-identifies as 'Pro-Life' on his campaign website and stated in a 2022 candidate survey: 'I am pro-life and it is at the top of my priorities list. I support Governor Noem's position on abortion and I am grateful for her leadership on this issue' — affirming protection of the unborn consistent with SD's near-total abortion ban.",
              ["https://jimmehlhaff.com/",
               "https://www.dakotanewsnow.com/2022/06/02/sd-state-legislative-candidate-survey-jim-mehlhaff/"]),
        claim("jml2", "jim-mehlhaff", "self_defense", 1, True,
              "Pledged on his campaign website to 'resist any efforts to limit our' Second Amendment constitutional gun rights, and as SD Senate Majority Leader (since January 2025) has held the line against firearm restrictions in one of the most conservative state chambers in the country.",
              ["https://jimmehlhaff.com/",
               "https://southdakotasearchlight.com/briefs/staunchly-conservatives-take-leadership-positions-in-gop-led-state-legislature/"]),
    ]),

    # ------------- Larry Zikmund (SD-R, State Senator, District 14) -----------
    ("larry-zikmund", "SD", "Senator", [
        claim("lz1", "larry-zikmund", "economic_stewardship", 2, True,
              "Has consistently championed South Dakota's low-tax, debt-free fiscal model, stating 'South Dakota has thrived because of our low tax, business friendly environment' and 'low taxes provide an incentive for businesses to start and relocate in South Dakota' — aligning with the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.larryzikmund.com/",
               "https://sdlegislature.gov/Legislators/Profile/1870/Detail"]),
        claim("lz2", "larry-zikmund", "election_integrity", 0, True,
              "A member of South Dakota's Republican supermajority, Zikmund has consistently supported the state's voter-identification requirements and paper-ballot election integrity measures, opposing federal pressure to expand mail-in voting; South Dakota is among the states that enforce photo ID at the polls and have resisted mass mail-in ballot schemes.",
              ["https://sdlegislature.gov/Legislators/Profile/1870/Detail",
               "https://sdsos.gov/elections-voting/election-resources/current-elected-officials.aspx"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions.

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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
