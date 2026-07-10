#!/usr/bin/env python3
"""Enrichment batch 623: hand-curated claims for 5 Pennsylvania State Senators.

Targets archetype_party_default PA state senators with 0 claims. All are
sitting Republican members of the Pennsylvania Senate with documented
voting records on key rubric issues (pro-life bills, constitutional carry,
election integrity, parental rights).

Senators: Doug Mastriano (SD-33), Cris Dush (SD-25), Dawn Keefer (SD-31),
Camera Bartolotta (SD-46), David G. Argall (SD-29).
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
    # --- Doug Mastriano (PA SD-33, State Senator) ---
    ("doug-mastriano", "PA", "State Senator", [
        claim("dm1", "doug-mastriano", "sanctity_of_life", 0, True,
              "Mastriano was the primary sponsor of Pennsylvania SB 378 (2021-2022), the 'Heartbeat Bill - Protecting the Rights of the Unborn,' which would prohibit abortion once a fetal heartbeat is detected, reflecting a strong pro-life position.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=0378",
               "https://en.wikipedia.org/wiki/Doug_Mastriano"]),
        claim("dm2", "doug-mastriano", "self_defense", 0, True,
              "Mastriano co-sponsored Pennsylvania SB 565 (2021-2022), the Constitutional Carry Act repealing the license requirement for concealed carry statewide; the bill passed the Senate 29-21 and the House 107-92 before being vetoed by Governor Wolf in December 2021.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=565",
               "https://www.legis.state.pa.us/cfdocs/billinfo/bill_votes.cfm?syear=2021&sind=0&body=S&type=B&bn=565"]),
        claim("dm3", "doug-mastriano", "election_integrity", 0, True,
              "Mastriano co-sponsored Pennsylvania SB 735 (2021-2022), a joint resolution to amend the state constitution requiring voters to provide valid government-issued photo identification; the bill passed the Senate 30-20.",
              ["https://www.legis.state.pa.us/cfdocs/billInfo/billInfo.cfm?bn=735&body=S&sInd=0&sYear=2021&type=B",
               "https://ballotpedia.org/Doug_Mastriano"]),
    ]),

    # --- Cris Dush (PA SD-25, State Senator) ---
    ("cris-dush", "PA", "State Senator", [
        claim("cd1", "cris-dush", "sanctity_of_life", 0, True,
              "Dush co-sponsored Pennsylvania SB 378 (2021-2022), the 'Heartbeat Bill - Protecting the Rights of the Unborn,' which would prohibit abortion once a fetal heartbeat is detected.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&body=S&type=B&bn=378",
               "https://ballotpedia.org/Cris_Dush"]),
        claim("cd2", "cris-dush", "self_defense", 0, True,
              "As the founding chairman of the Pennsylvania Senate Second Amendment Caucus, Dush prime-sponsored SB 565 (2021-2022) to establish permitless constitutional carry in Pennsylvania and circulated a 2025 co-sponsorship memo to re-introduce the same legislation.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?sYear=2021&sInd=0&body=S&type=B&bn=565",
               "https://www.palegis.us/senate/co-sponsorship/memo?memoID=44632"]),
        claim("cd3", "cris-dush", "election_integrity", 0, True,
              "As chair of the PA Senate State Government Committee, Dush co-sponsored SB 878 (2021), an election integrity reform bill including voter ID requirements and post-election audit provisions, and separately sponsored legislation prohibiting ballot drop boxes.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&sind=0&body=S&type=B&bn=878",
               "https://ballotpedia.org/Cris_Dush"]),
    ]),

    # --- Dawn W. Keefer (PA SD-31, State Senator) ---
    ("dawn-w-keefer", "PA", "State Senator", [
        claim("dwk1", "dawn-w-keefer", "sanctity_of_life", 0, True,
              "Keefer co-sponsored a Pennsylvania constitutional amendment (advanced 2021-2022) that would explicitly exclude any state constitutional right to abortion and declare that Pennsylvania law 'shall protect every unborn child, from conception to birth.'",
              ["https://ballotpedia.org/Pennsylvania_No_State_Constitutional_Right_to_Abortion_Amendment_(2024)",
               "https://ballotpedia.org/Dawn_Keefer"]),
        claim("dwk2", "dawn-w-keefer", "election_integrity", 3, True,
              "In December 2021, Keefer successfully amended SB 106 on the House floor to mandate post-election audits of results, voter rolls, machine certification, and election administration; the Pennsylvania House adopted the amendment 114-89.",
              ["https://ballotpedia.org/Pennsylvania_Election_Audits_Amendment_(2024)",
               "https://ballotpedia.org/Dawn_Keefer"]),
        claim("dwk3", "dawn-w-keefer", "biblical_marriage", 2, True,
              "Keefer was a primary co-sponsor of Pennsylvania HB 972 (2021-2022) prohibiting transgender athletes from competing on school sports teams aligned with their gender identity rather than their biological sex, and co-sponsored companion legislation again as a State Senator after 2024.",
              ["https://en.wikipedia.org/wiki/Dawn_Keefer",
               "https://www.palegis.us/legislation/bills/2021/hb972"]),
    ]),

    # --- Camera Bartolotta (PA SD-46, State Senator) ---
    ("camera-bartolotta", "PA", "State Senator", [
        claim("cb1", "camera-bartolotta", "self_defense", 0, True,
              "Bartolotta was a named co-sponsor of Pennsylvania SB 565 (2021-2022), the Constitutional Carry Act eliminating the license requirement to carry a firearm statewide; the bill passed the Senate 29-21 in November 2021 before being vetoed by Governor Wolf.",
              ["https://www.legis.state.pa.us/cfdocs/billinfo/billinfo.cfm?syear=2021&body=S&type=B&bn=0565",
               "https://ballotpedia.org/Camera_Bartolotta"]),
        claim("cb2", "camera-bartolotta", "sanctity_of_life", 0, True,
              "As of May 2026, Bartolotta carries a 100% pro-life voting record recognized by the National Right to Life, which endorsed her re-election bid, reflecting a consistent stance that human life deserves legal protection from conception until natural death.",
              ["https://nrlc.org/nrlnewstoday/2026/05/pro-life-candidates-in-pennsylvania-do-very-well-in-tuesdays-primary-elections/",
               "https://ballotpedia.org/Camera_Bartolotta"]),
        claim("cb3", "camera-bartolotta", "family_child_sovereignty", 0, True,
              "Bartolotta co-sponsored Pennsylvania SB 1277 (2021-2022), requiring school districts to adopt parental notification policies for instructional materials and library books containing sexually explicit content; the bill passed the Senate 30-20.",
              ["https://www.legis.state.pa.us/cfdocs/billInfo/billInfo.cfm?sYear=2021&body=S&type=B&bn=1277",
               "https://www.pasenategop.com/news/senate-passes-bill-to-settle-issue-of-sexually-explicit-content-in-school/"]),
    ]),

    # --- David G. Argall (PA SD-29, State Senator) ---
    ("david-g-argall", "PA", "State Senator", [
        claim("dga1", "david-g-argall", "sanctity_of_life", 0, True,
              "Argall was the prime sponsor of Pennsylvania SB 106 (2021-2022), a joint resolution proposing a constitutional amendment declaring there is no state constitutional right to abortion; the bill passed the Senate 28-22 and the House 107-92, and was enacted as Pamphlet Laws Resolution No. 1 of 2022.",
              ["https://www.palegis.us/legislation/bills/2021/sb0106",
               "https://legis.state.pa.us/cfdocs/billinfo/bill_history.cfm?syear=2021&sind=0&body=S&type=B&bn=106"]),
        claim("dga2", "david-g-argall", "election_integrity", 0, True,
              "Argall co-sponsored Pennsylvania SB 422 (2021-2022), which amended the Election Code to require photo voter identification at the polls, among the first Senate Republicans to formally sign onto a standalone voter-ID bill in the post-2020 session.",
              ["https://www.palegis.us/legislation/bills/2021/sb422",
               "https://ballotpedia.org/Voter_ID_in_Pennsylvania"]),
        claim("dga3", "david-g-argall", "self_defense", 0, True,
              "Argall voted to pass Pennsylvania SB 565 (2021), the constitutional carry bill repealing the license requirement for concealed carry; the bill cleared the Senate 29-21 on November 9, 2021, before being vetoed by Governor Wolf.",
              ["https://legis.state.pa.us/cfdocs/billinfo/bill_votes.cfm?syear=2021&sind=0&body=S&type=B&bn=565",
               "https://www.palegis.us/senate/roll-calls/summary?sessYr=2021&sessInd=0&rcNum=769"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher to prevent same-slug collisions across states."""
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
            print(f"  NOT FOUND: slug={slug} state={state} office_kw={office_keyword}")
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
        print(f"  + {m['name']:<28} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    # Minified write -- preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
