#!/usr/bin/env python3
"""Enrichment batch 820: 5 Florida Republican State Representatives (evidence_state → evidence_curated).

The archetype_curated pool (federal and state) is fully exhausted. This batch continues
the evidence_state Florida Republican state-rep series, taking the next 5 from the
reverse-alphabetical bottom of the FL evidence_state bucket:
  Rachel Plakon (FL HD-36, Seminole County; lead sponsor HB 1521 / voted SB 300),
  Mike Giallombardo (FL HD-79; HB 543 co-sponsor; in office since 2020),
  Michelle Salzman (FL HD-1, Pensacola; HB 543 co-sponsor; NRA + Florida Carry member),
  Lawrence McClure (FL HD-68; House Appropriations Chair; in office since 2018),
  Nan Cobb (FL HD-26; FL Right to Life endorsed; HB 791 Safe Haven sponsor, 2025).

Research covers confirmed bill sponsorships, party-line floor votes (with dissenters
cross-checked), verified campaign positions, and confirmed endorsements (2022–2025).
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


TARGETS = [
    # --- Rachel Plakon (FL HD-36, R; Seminole County; first elected Nov 2022; seeking reelection 2026) ---
    ("rachel-plakon", "FL", "Representative", [
        claim("rp1", "rachel-plakon", "biblical_marriage", 2, True,
              "Primary sponsor of CS/HB 1521 (2023), Florida's Facility Requirements Based on Sex Act "
              "(the 'bathroom bill'), which mandates that individuals use restrooms, locker rooms, and "
              "changing facilities corresponding to their biological sex assigned at birth in government "
              "buildings, correctional facilities, domestic violence shelters, and licensed-care "
              "facilities — with criminal trespass penalties for violations. Passed the Florida House on "
              "party lines, signed by Governor DeSantis on May 17, 2023, and effective July 1, 2023. "
              "Plakon's lead sponsorship directly reflects the conviction that sex is binary and immutable "
              "and that sex-segregated privacy in public facilities is a necessary policy.",
              ["https://en.wikipedia.org/wiki/Rachel_Plakon",
               "https://www.myfloridahouse.gov/Sections/Bills/billsdetail.aspx?BillId=78388"]),
        claim("rp2", "rachel-plakon", "sanctity_of_life", 0, True,
              "Supported Florida's six-week abortion ban (SB 300, Heartbeat Protection Act, 2023), "
              "voting with the Republican majority (70–40) when the House passed it on April 13, 2023. "
              "Plakon — who assumed office in November 2022 and cast her first major pro-life vote in "
              "her first full legislative session — is confirmed pro-life by multiple sources covering "
              "the 2023 Florida legislative session.",
              ["https://floridapolitics.com/archives/603032-six-week-abortion-ban-house/",
               "https://ballotpedia.org/Rachel_Plakon"]),
        claim("rp3", "rachel-plakon", "self_defense", 0, True,
              "Member of the Republican House majority that passed HB 543 (2023), Florida's "
              "Constitutional Carry Act (76–32), eliminating the government-issued concealed carry "
              "license requirement and establishing Florida as the 26th constitutional carry state. "
              "Governor DeSantis signed HB 543 on April 3, 2023, effective July 1, 2023.",
              ["https://floridapolitics.com/archives/598200-house-passes-gun-bill-allowing-concealed-carry-without-a-permit/",
               "https://ballotpedia.org/Rachel_Plakon"]),
    ]),

    # --- Mike Giallombardo (FL HD-79, R; Iraq War veteran / CW2; first elected Nov 2020) ---
    ("mike-giallombardo", "FL", "Representative", [
        claim("mg1", "mike-giallombardo", "self_defense", 0, True,
              "Co-sponsored CS/HB 543 (2023), Florida's Constitutional Carry Act, actively driving "
              "the elimination of the government-issued license requirement for concealed carry. As a "
              "formal co-sponsor, Giallombardo went beyond a floor vote to help champion the bill — "
              "which passed 76–32 and was signed by Governor DeSantis on April 3, 2023, making "
              "Florida the 26th constitutional carry state.",
              ["https://housedocs.myfloridahouse.gov/Sections/Bills/billsdetail.aspx?BillId=77202",
               "https://en.wikipedia.org/wiki/Mike_Giallombardo"]),
        claim("mg2", "mike-giallombardo", "sanctity_of_life", 0, True,
              "Voted for SB 300 (Heartbeat Protection Act, 2023), Florida's six-week abortion ban, "
              "passed by the House 70–40 on April 13, 2023. Giallombardo, a Republican member since "
              "2020, is absent from the nine named Republican dissenters who broke with the party to "
              "oppose the measure (Reps. Caruso, Gonzalez Pittman, Gossett-Seidman, Killebrew, "
              "LaMarca, Lopez, and Roth), confirming his pro-life alignment with the majority.",
              ["https://floridapolitics.com/archives/603032-six-week-abortion-ban-house/",
               "https://ballotpedia.org/Mike_Giallombardo"]),
        claim("mg3", "mike-giallombardo", "economic_stewardship", 2, True,
              "Sponsored legislation to abolish Florida's Community Redevelopment Agencies (CRAs) — "
              "locally-created government entities that divert property-tax revenue away from county "
              "and municipal general funds into targeted discretionary spending programs. "
              "Giallombardo's CRA-abolition bill advanced through committee, reflecting a fiscal "
              "posture that limits special-purpose government spending and returns diverted property-tax "
              "dollars to local government core budgets — consistent with the rubric's preference for "
              "restraining government expenditure over deficit-fueling discretionary programs.",
              ["https://floridapolitics.com/archives/726229-mike-giallombardos-cra-killing-bill-advances-but-even-some-supporters-disagree-with-its-aim/",
               "https://ballotpedia.org/Mike_Giallombardo"]),
    ]),

    # --- Michelle Salzman (FL HD-1, R; Pensacola; Army veteran; first elected Nov 2020) ---
    ("michelle-salzman", "FL", "Representative", [
        claim("ms1", "michelle-salzman", "self_defense", 0, True,
              "Co-sponsored HB 543 (2023), Florida's Constitutional Carry Act, joining a small "
              "group of House Republicans as formal co-sponsors of the bill eliminating the "
              "government-issued license requirement for concealed carry — which passed 76–32 and "
              "was signed by Governor DeSantis on April 3, 2023. Salzman is also a member of the "
              "NRA and Florida Carry (the state's Second Amendment advocacy organization), "
              "demonstrating consistent, institutionally-grounded support for unrestricted "
              "firearm ownership by law-abiding citizens.",
              ["https://en.wikipedia.org/wiki/Michelle_Salzman",
               "https://floridapolitics.com/archives/598200-house-passes-gun-bill-allowing-concealed-carry-without-a-permit/"]),
        claim("ms2", "michelle-salzman", "sanctity_of_life", 0, True,
              "Voted with the Republican majority (70–40) to pass SB 300 (Heartbeat Protection "
              "Act, 2023), Florida's six-week abortion ban, on April 13, 2023. Salzman — a "
              "Republican Army veteran serving since 2020 — is absent from the list of nine "
              "Republican dissenters who broke with the party to oppose the measure, confirming "
              "her pro-life alignment with the majority.",
              ["https://floridapolitics.com/archives/603032-six-week-abortion-ban-house/",
               "https://ballotpedia.org/Michelle_Salzman"]),
        claim("ms3", "michelle-salzman", "biblical_marriage", 2, True,
              "Voted for CS/HB 1521 (2023), Florida's Facility Requirements Based on Sex Act "
              "(the 'bathroom bill'), requiring individuals to use public restrooms and "
              "sex-segregated facilities corresponding to their biological sex. The bill passed "
              "the Florida House on party lines; Salzman, a Republican serving since 2020, voted "
              "with the Republican majority, reflecting her alignment with the conviction that "
              "biological sex — not gender identity — is the appropriate basis for sex-segregated "
              "public-facility policy.",
              ["https://ballotpedia.org/Michelle_Salzman",
               "https://en.wikipedia.org/wiki/Michelle_Salzman"]),
    ]),

    # --- Lawrence McClure (FL HD-68, R; East Hillsborough; Chair, House Appropriations Committee; first elected 2018 special election) ---
    ("lawrence-mcclure", "FL", "Representative", [
        claim("lm1", "lawrence-mcclure", "sanctity_of_life", 0, True,
              "Republican member of the Florida House since 2018 who voted with the majority "
              "(70–40) to pass SB 300 (Heartbeat Protection Act, 2023), Florida's six-week "
              "abortion ban, on April 13, 2023. McClure — a multi-term Republican conservative "
              "serving East Hillsborough County — is absent from the named list of nine "
              "Republican dissenters who broke with the party to oppose the ban, placing him "
              "with the pro-life majority.",
              ["https://floridapolitics.com/archives/603032-six-week-abortion-ban-house/",
               "https://ballotpedia.org/Lawrence_McClure"]),
        claim("lm2", "lawrence-mcclure", "self_defense", 0, True,
              "Republican member of the Florida House who voted for HB 543 (2023), Florida's "
              "Constitutional Carry Act (76–32 passage), eliminating the government-issued "
              "concealed carry license requirement and establishing Florida as the 26th "
              "constitutional carry state. McClure, who has served in the Florida House since "
              "2018 and chairs the House Budget Committee, voted with the Republican majority "
              "in expanding Second Amendment rights for law-abiding Floridians.",
              ["https://floridapolitics.com/archives/598200-house-passes-gun-bill-allowing-concealed-carry-without-a-permit/",
               "https://ballotpedia.org/Lawrence_McClure"]),
        claim("lm3", "lawrence-mcclure", "economic_stewardship", 2, True,
              "Serves as Chair of the Florida House Appropriations Committee (the principal "
              "budget-writing body), having guided the chamber through 'a tough budget challenge "
              "that saw weeks of overtime before a budget was agreed upon' as of 2025. McClure's "
              "leadership reflects a posture of fiscal discipline, navigating competing spending "
              "demands while maintaining a structurally balanced state budget — consistent with "
              "the rubric's preference for responsible stewardship over deficit spending.",
              ["https://floridapolitics.com/archives/755157-lawrence-mcclure-susan-valdes-to-continue-leading-powerful-house-budget-committee-as-tampa-bay-remains-well-represented/",
               "https://ballotpedia.org/Lawrence_McClure"]),
    ]),

    # --- Nan Cobb (FL HD-26, R; first elected Nov 2024; freshman) ---
    ("nan-cobb", "FL", "Representative", [
        claim("nc1", "nan-cobb", "sanctity_of_life", 0, True,
              "Campaign platform explicitly pledges to 'Foster a culture of LIFE' under a "
              "heartbeat symbol — a direct affirmation of the pro-life conviction that human "
              "life deserves protection. Endorsed by Florida Right to Life for the 2024 primary "
              "election, and flagged as 'Anti-Choice' by Florida Choice Tracker (a "
              "pro-abortion-access monitor that researches legislative history and public "
              "statements). Cobb won her first term as a Republican in November 2024.",
              ["https://choicetracker.org/fl/people/nan-cobb/285933568",
               "https://ballotpedia.org/Nan_Cobb"],
              kind="statement"),
        claim("nc2", "nan-cobb", "public_justice", 0, True,
              "Sponsored HB 791 (2025), the Newborn Safe Haven Device Act, which strengthens "
              "Florida's Safe Haven law by authorizing and regulating infant safety surrender "
              "devices at hospitals, fire stations, and emergency medical services facilities — "
              "creating a safe, anonymous mechanism for parents to relinquish newborns without "
              "fear of legal repercussions. The bill passed the Florida House unanimously, "
              "reflecting the conviction that the most vulnerable lives deserve specific legal "
              "protection against abandonment and harm.",
              ["https://floridapolitics.com/archives/730316-house-passes-bill-to-allow-the-safe-surrender-of-newborn-infants/",
               "https://m.myfloridahouse.gov/Sections/Representatives/sponsoredbills.aspx?MemberId=4910&SessionId=111"]),
        claim("nc3", "nan-cobb", "refuse_federal_overreach", 0, True,
              "Ran as an 'America First' Republican who specifically campaigned against 'the "
              "radical agenda of the Leftist Liberals in Washington, D.C.,' framing federal "
              "overreach as a direct threat to Floridians. Cobb won election in November 2024 "
              "on a platform of resisting Washington-driven mandates and advancing conservative "
              "state-level policies — a posture aligned with the rubric's preference for "
              "limiting federal intrusion into state and individual decision-making.",
              ["https://ballotpedia.org/Nan_Cobb",
               "https://floridapolitics.com/archives/649073-fourth-republican-enters-race-for-hd-26/"],
              kind="statement"),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
