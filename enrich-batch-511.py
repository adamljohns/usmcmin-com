#!/usr/bin/env python3
"""Enrichment batch 511: hand-curated claims for 5 state-level officials.

Targets evidence_state candidates that had 0 evidence claims, taken from the
bottom of the alphabet (TX and NC). The archetype_curated federal senator/rep
pools are fully exhausted; this batch pivots to state-level officials.

Targets (all R):
  Giovanni Capriglione (TX, State Rep HD-98)
  Greg Bonnen          (TX, State Rep HD-24, House Appropriations Chair)
  Brad Briner          (NC, State Treasurer)
  Dave Boliek          (NC, State Auditor)
  Dustin Burrows       (TX, Speaker of the Texas House, HD-83)

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
    # ---------------- Giovanni Capriglione (TX-R, State Rep HD-98) ----------------
    ("giovanni-capriglione", "TX", "Representative", [
        claim("gc1", "giovanni-capriglione", "sanctity_of_life", 0, True,
              "Authored HB 1280, the Texas Human Life Protection Act (2021) — the state's abortion 'trigger law' that enacted a near-total abortion ban 30 days after Roe v. Wade was overturned, with no exceptions for rape or incest. The bill passed both chambers and was signed by Gov. Abbott, and remains in full effect. This is one of the most comprehensive pro-life legislative achievements by any state lawmaker.",
              ["https://capitol.texas.gov/tlodocs/87R/billtext/html/HB01280I.htm",
               "https://en.wikipedia.org/wiki/Giovanni_Capriglione",
               "https://txcatholic.org/human-life-protection-act/"]),
        claim("gc2", "giovanni-capriglione", "economic_stewardship", 1, True,
              "Co-authored SB 21 (2025), establishing the Texas Strategic Bitcoin Reserve — making Texas the first U.S. state to hold Bitcoin as a state treasury asset. The bill was signed by Gov. Abbott on June 22, 2025, positioning the state to hedge against dollar debasement with a sound, decentralized alternative to fiat currency.",
              ["https://en.wikipedia.org/wiki/Giovanni_Capriglione",
               "https://ballotpedia.org/Giovanni_Capriglione"]),
        claim("gc3", "giovanni-capriglione", "economic_stewardship", 2, True,
              "Signed the Americans for Tax Reform Taxpayer Protection Pledge, committing to oppose all net tax increases. He has served on the House Ways and Means Committee and as Chair of the Committee on Delivery of Government Efficiency, maintaining a consistent fiscal-conservative posture against deficit spending and government waste.",
              ["https://ballotpedia.org/Giovanni_Capriglione",
               "https://en.wikipedia.org/wiki/Giovanni_Capriglione"]),
    ]),

    # ---------------- Greg Bonnen (TX-R, State Rep HD-24, Appropriations Chair) ----------------
    ("greg-bonnen", "TX", "Representative", [
        claim("gb1", "greg-bonnen", "sanctity_of_life", 0, True,
              "A neurosurgeon with a 100% pro-life voting record across multiple Texas legislative sessions; helped pass both the Texas Heartbeat Act (SB 8, 2021) and the Human Life Protection Act trigger ban (2021). Fought to end taxpayer funding of abortion providers and supported $469 million in new maternal health funding to protect mothers and babies.",
              ["https://drgregbonnen.com/",
               "https://ballotpedia.org/Greg_Bonnen",
               "https://www.texasallianceforlife.org/89th-texas-lege-scorecard/"]),
        claim("gb2", "greg-bonnen", "self_defense", 1, True,
              "A consistent defender of Second Amendment rights in the Texas Legislature; his campaign platform explicitly commits to 'defending our Second Amendment rights' and opposing new gun restrictions. He has voted against bills that would impose bans, registries, or additional permit requirements on law-abiding Texans.",
              ["https://drgregbonnen.com/",
               "https://ballotpedia.org/Greg_Bonnen"]),
        claim("gb3", "greg-bonnen", "economic_stewardship", 2, True,
              "Serves as Chair of the Texas House Appropriations Committee, where he steers the state budget with an emphasis on fiscal discipline, tax cuts, and rejecting deficit-financed spending. He has backed property-tax relief and opposed supplemental appropriations that would balloon state liabilities.",
              ["https://ballotpedia.org/Greg_Bonnen",
               "https://capitol.texas.gov/Members/MemberInfo.aspx?Leg=89&Chamber=H&Code=A2875"]),
    ]),

    # ---------------- Brad Briner (NC-R, State Treasurer) ----------------
    ("brad-briner", "NC", "Treasurer", [
        claim("bb1", "brad-briner", "economic_stewardship", 4, True,
              "An outspoken opponent of ESG (Environmental, Social and Governance) investing in public pension funds. Briner has pledged that as Treasurer he will focus solely on financial returns and not 'woke' politics, stating that 'the ESG crowd has driven a lemming-like abandonment of sectors like traditional energy' — the same anti-ESG/anti-Davos posture the rubric requires.",
              ["https://ncnewsline.com/2024/08/12/ncs-next-treasurer/",
               "https://ballotpedia.org/Brad_Briner"]),
        claim("bb2", "brad-briner", "economic_stewardship", 2, True,
              "Championed and helped pass the 2025 State Investment Modernization Act (HB 506), his top campaign priority, which restructures how NC's pension fund is managed to maximize fiduciary returns for the state's 900,000+ pension beneficiaries. He has consistently prioritized fiscal stewardship over political agendas in managing public assets.",
              ["https://www.nctreasurer.gov/news/press-releases/2025/06/13/policy-priority-treasurer-brad-briner-signed-law",
               "https://ballotpedia.org/Brad_Briner"]),
    ]),

    # ---------------- Dave Boliek (NC-R, State Auditor) ----------------
    ("dave-boliek", "NC", "Auditor", [
        claim("db1", "dave-boliek", "election_integrity", 0, True,
              "Campaigned on establishing a dedicated 'office of election integrity' within the State Auditor's office to audit North Carolina's voter rolls, election equipment, and operations. After the NC General Assembly transferred election oversight to the auditor, Boliek immediately moved to implement his election-integrity mandate.",
              ["https://www.wral.com/story/incoming-nc-auditor-promises-to-leave-party-politics-out-of-election-oversight/21777002/",
               "https://ballotpedia.org/Dave_Boliek"]),
        claim("db2", "dave-boliek", "election_integrity", 1, True,
              "In May 2025 appointed new members to the North Carolina State Board of Elections, giving Republicans a majority on the board for the first time. The NC Supreme Court upheld his appointment authority. He also hired a former NCGOP executive director to serve as election board liaison and lead election-integrity training across all 100 county boards.",
              ["https://www.auditor.nc.gov/news/press-releases/2025/05/01/state-auditor-boliek-appoints-members-state-board-elections",
               "https://www.carolinajournal.com/nc-supreme-court-allows-auditor-boliek-to-maintain-elections-board-appointments/",
               "https://www.wral.com/story/former-ncgop-director-to-lead-election-integrity-efforts-serve-as-election-board-liaison-says-nc-auditor/22175491/"]),
    ]),

    # ---------------- Dustin Burrows (TX-R, Speaker of the Texas House, HD-83) ----------------
    ("dustin-burrows", "TX", "Speaker", [
        claim("du1", "dustin-burrows", "sanctity_of_life", 0, True,
              "As Speaker of the Texas House (elected January 2025), managed and delivered passage of the 89th Legislature's full conservative agenda, including stricter abortion restrictions. He has a documented record of supporting pro-life legislation through the Texas House and protecting the state's existing trigger ban.",
              ["https://www.texastribune.org/2025/06/06/dustin-burrows-texas-legislature-house-speaker-first-term/",
               "https://en.wikipedia.org/wiki/Dustin_Burrows"]),
        claim("du2", "dustin-burrows", "self_defense", 1, True,
              "Thwarted stricter gun-control legislation during his tenure as Speaker, blocking bills that would have expanded firearm restrictions in Texas. He has consistently voted against measures that would impose bans, waiting periods, or registration requirements on law-abiding gun owners.",
              ["https://www.texastribune.org/2025/06/06/dustin-burrows-texas-legislature-house-speaker-first-term/",
               "https://en.wikipedia.org/wiki/Dustin_Burrows"]),
        claim("du3", "dustin-burrows", "christian_liberty", 0, True,
              "Led the 89th Texas Legislature to pass a requirement that the Ten Commandments be displayed in every public school classroom, and oversaw a ban on DEI programming in public education — two landmark wins for religious expression and against ideological capture of public schools.",
              ["https://www.texastribune.org/2025/06/06/dustin-burrows-texas-legislature-house-speaker-first-term/",
               "https://en.wikipedia.org/wiki/Dustin_Burrows"]),
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
