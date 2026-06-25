#!/usr/bin/env python3
"""Enrichment batch 403: hand-curated claims for 5 sitting U.S. Senators.

Targets senators with 5 existing claims from bottom-of-alphabet states (NC, NE, NE, ND, OK).
Adds 2 claims each in DISTINCT rubric categories not yet covered.
All positions verified via official senate.gov, congress.gov, govtrack.us, ballotpedia.org.

Targets: Ted Budd (NC-R), Deb Fischer (NE-R), Pete Ricketts (NE-R),
         John Hoeven (ND-R), James Lankford (OK-R).
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
    # ---------------- Ted Budd (NC-R, US Senator) ----------------
    ("ted-budd", "NC", "Senator", [
        claim("tb403a", "ted-budd", "christian_liberty", 0, True,
              "Led bipartisan legislation (with Sen. Chris Coons) to reauthorize the U.S. Commission on International Religious Freedom through FY2028; the bill cleared the Senate Foreign Relations Committee in June 2026. Also introduced the Banning Perpetrators of Religious Persecution Act (January 2026) restricting U.S. visas for foreign violators of religious freedom — a consistent record of defending free exercise worldwide.",
              ["https://www.budd.senate.gov/2026/06/18/budd-coons-bill-to-reauthorize-uscirf-advance-international-religious-freedom-heads-to-senate-floor/",
               "https://www.budd.senate.gov/2026/01/16/senator-budd-leads-legislation-banning-foreign-violators-of-religious-freedom-from-obtaining-u-s-visas/"]),
        claim("tb403b", "ted-budd", "election_integrity", 0, True,
              "Joined Senate colleagues Cornyn and Cruz in October 2025 pushing for a proof-of-U.S.-citizenship requirement on the National Mail Voter Registration Form; has publicly stated that voting bills expanding 'no excuse' absentee voting and weakening voter ID requirements 'undermine election integrity.'",
              ["https://www.cornyn.senate.gov/news/cornyn-cruz-colleagues-push-for-proof-of-citizenship-requirement-for-national-mail-voter-registration-form/",
               "https://www.govtrack.us/congress/members/ted_budd/412712"]),
    ]),

    # ---------------- Deb Fischer (NE-R, US Senator) ----------------
    ("deb-fischer", "NE", "Senator", [
        claim("df403a", "deb-fischer", "election_integrity", 0, True,
              "Cosponsored the Safeguard American Voter Eligibility (SAVE) America Act (S.128/H.R.22, 119th Congress) requiring proof of citizenship to register and photo ID to vote in federal elections; declared on the Senate floor 'Only U.S. citizens should vote in U.S. elections,' citing Nebraska's 2023 voter ID law as a model for the nation.",
              ["https://www.fischer.senate.gov/public/index.cfm/news?ID=684DC6F2-6A6B-4AC7-AD23-C6DC89969DAF",
               "https://www.congress.gov/bill/119th-congress/senate-bill/128"]),
        claim("df403b", "deb-fischer", "foreign_policy_restraint", 1, False,
              "A hawkish member of the Senate Armed Services Committee who cosponsored Russia sanctions legislation providing $500 million in emergency lethal military financing to Ukraine, advocated for expanding munitions production to sustain Ukraine's war effort indefinitely, and advanced defense legislation committing further U.S. resources to the Ukraine conflict — directly opposing the rubric's call to end open-ended foreign military entanglements.",
              ["https://www.fischer.senate.gov/public/index.cfm/news?ID=18CA3D4C-B54A-4B28-BCCF-6D7E78E791B4",
               "https://www.fischer.senate.gov/public/index.cfm/2023/6/fischer-advances-senate-armed-services-committee-fy24-defense-bill"]),
    ]),

    # ---------------- Pete Ricketts (NE-R, US Senator) ----------------
    ("pete-ricketts", "NE", "Senator", [
        claim("pr403a", "pete-ricketts", "christian_liberty", 0, True,
              "As a Catholic senator, publicly slammed the Vatican in 2025 for giving China's Xi Jinping a 'green light to construct state-approved, state-controlled Catholic Churches,' demanding that faith institutions resist communist state capture; also joined colleagues introducing a bipartisan resolution calling for continued U.S. leadership on international religious freedom — a record of defending free Christian exercise against authoritarian interference.",
              ["https://www.ricketts.senate.gov/news/press-releases/ricketts-slams-vatican-for-giving-xi-jinping-green-light-to-construct-state-approved-state-controlled-catholic-churches/",
               "https://www.foreign.senate.gov/press/rep/release/risch-colleagues-introduce-resolution-in-support-of-religious-freedom"]),
        claim("pr403b", "pete-ricketts", "foreign_policy_restraint", 4, False,
              "As Ranking Member of the Senate Foreign Relations Subcommittee on Europe and Regional Security Cooperation, publicly endorsed President Trump's move to sell U.S. munitions to European NATO allies in support of Ukraine, called for continued weapons supply so Ukraine can 'win,' and urged deepening NATO weapons commitments — opposing the rubric's skepticism of NATO expansion and open-ended foreign military commitments.",
              ["https://www.ricketts.senate.gov/news/press-releases/ricketts-supports-president-trumps-move-to-sell-weapons-to-europe-in-support-of-ukraine/",
               "https://www.ricketts.senate.gov/weekly_column/senator-ricketts-weekly-column-pushing-back-on-putin/"]),
    ]),

    # ---------------- John Hoeven (ND-R, US Senator) ----------------
    ("john-hoeven", "ND", "Senator", [
        claim("jh403a", "john-hoeven", "biblical_marriage", 0, True,
              "Voted Nay on the Respect for Marriage Act (Senate Vote #362, November 29, 2022), joining 35 other Senate Republicans in rejecting federal codification of same-sex marriage — 12 Republicans broke ranks to vote Yea while Hoeven upheld the traditional one-man-one-woman definition.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1172/vote_117_2_00362.htm"]),
        claim("jh403b", "john-hoeven", "foreign_policy_restraint", 1, False,
              "A consistent Ukraine hawk who joined colleagues introducing the NYET (Never Yielding Europe's Territory) Act to impose Russia sanctions and expand Ukraine military aid; declared the U.S. 'can and should expand efforts to push back against Russia's aggression in Ukraine' and backed supplemental Ukraine aid packages — opposing the rubric's call to end open-ended foreign military entanglements.",
              ["https://www.hoeven.senate.gov/news/news-releases/hoeven-joins-risch-colleagues-in-introducing-russia-sanctions-legislation",
               "https://www.hoeven.senate.gov/news/videos/watch/hoeven-us-can-do-more-to-support-ukraine-counter-russias-aggression"]),
    ]),

    # ---------------- James Lankford (OK-R, US Senator) ----------------
    ("james-lankford", "OK", "Senator", [
        claim("jl403a", "james-lankford", "biblical_marriage", 0, True,
              "Voted against the Respect for Marriage Act (2022), introducing an amendment to protect religious believers from its private-right-of-action provisions; declared that for him 'God's design for marriage is a core aspect of my faith, not a secondary doctrine' — affirming the one-man-one-woman definition of marriage and religious liberty for dissenters.",
              ["https://www.lankford.senate.gov/news/press-releases/lankford-pushes-for-equal-protection-in-the-respect-for-marriage-act/",
               "https://www.lankford.senate.gov/news/in-the-news/viewpoint-marriage-bill-is-disrespectful-of-religious-liberty/"]),
        claim("jl403b", "james-lankford", "election_integrity", 0, True,
              "As Senate Republican Conference Vice Chair, led the Senate floor push for the SAVE America Act (S.128 cosponsor, 119th Congress) requiring proof of citizenship to register to vote and photo ID to cast a ballot in federal elections, framing it as essential to 'ensure only American citizens vote.'",
              ["https://www.lankford.senate.gov/news/press-releases/icymi-lankford-leads-senate-republicans-on-floor-to-pass-save-america-act-ensure-only-american-citizens-vote/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/128"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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

    # Minified write — preserve the no-whitespace master (keeps file ~35-36MB under GitHub's 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
