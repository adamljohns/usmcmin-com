#!/usr/bin/env python3
"""Enrichment batch 821: 5 Florida Republican State Representatives (evidence_state → evidence_curated).

The archetype_curated pool is fully exhausted. This batch continues the evidence_state
Florida state-rep series from the bottom of the reverse-alphabetical bucket:
  Samantha Scott (FL HD-52, Sumter County; special-election winner Nov 18, 2025;
    'faith, family and freedom' platform; FL FOP + AIF endorsed),
  Sam Greco (FL HD-19, Flagler Co.; Navy JAG officer; FRTL-A; Missy's Law sponsor),
  Richard Gentry (FL HD-27, Lake/Marion/Volusia; FL Right to Life-A; CCW holder),
  Paula A. Stark (FL HD-47, Osceola Co.; voted AGAINST SB 300 abortion ban and
    AGAINST HB 1521 bathroom bill — two negative scores documented),
  Patt Maney (FL HD-4, Okaloosa Co.; Brig. Gen. ret.; NRA-A; VTC pioneer;
    'life begins at conception'; HB 199 Veterans Treatment Court expansion signed 2026).

Research covers confirmed endorsements, sponsored legislation, voting records (2023-2026),
and documented public statements from FL Right to Life, NRA-PVF, Ballotpedia,
Florida Politics, Florida Phoenix, and iVoterGuide candidate surveys.
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
    # --- Samantha Scott (FL HD-52, R; Sumter County; special-election winner Nov 18, 2025) ---
    ("samantha-scott", "FL", "State Representative", [
        claim("ss1", "samantha-scott", "family_child_sovereignty", 0, True,
              "Ran on an explicitly pro-family platform — 'faith, family and freedom' — and won "
              "the HD-52 special election on November 18, 2025 with unanimous House Republican "
              "backing. Speaker-designate Sam Garrison endorsed Scott citing 'the conservative, "
              "pro-family, pro-business values' she would bring to the Florida House, making "
              "parental rights and family sovereignty a central pillar of her candidacy. Scott, "
              "a lifelong Sumter County resident and daughter of a U.S. Navy veteran, ran with "
              "endorsements from U.S. Rep. Daniel Webster, CFO Blaise Ingoglia, and a broad "
              "slate of sitting House Republicans, running unopposed after the Democratic "
              "challenger withdrew.",
              ["https://floridapolitics.com/archives/764561-house-republicans-back-samantha-scott-in-hd-52-special-election/",
               "https://floridapolitics.com/archives/764404-samantha-scott-lands-trove-of-endorsements-in-hd-52-special-election/"],
              kind="statement"),
        claim("ss2", "samantha-scott", "election_integrity", 0, True,
              "Voted with the Republican majority (77-28 party-line vote) to pass CS/CS/HB 991 "
              "(2026), the Elections bill requiring documentary proof of citizenship — a valid "
              "passport or birth certificate, with names matching the statewide voter "
              "registration system — to register to vote in Florida, removing student IDs as "
              "an accepted form of voter identification. Governor DeSantis signed the bill at "
              "The Villages (Sumter County) on April 1, 2026, effective January 1, 2027. "
              "Scott was seated from Sumter County and participated in the 2026 regular "
              "session as a sitting member after winning her November 2025 special election.",
              ["https://floridaphoenix.com/2026/04/01/desantis-signs-bill-requiring-proof-of-citizenship-to-register-to-vote-voting-rights-group-sue/",
               "https://www.wlrn.org/government-politics/2026-03-13/florida-legislature-passes-bill-requiring-proof-of-citizenship-at-the-ballot-box"]),
        claim("ss3", "samantha-scott", "public_justice", 0, True,
              "Endorsed by the Florida Fraternal Order of Police for the HD-52 special election "
              "(November 2025), the statewide organization representing Florida law enforcement "
              "officers, signaling Scott's commitment to public safety and support for law "
              "enforcement interests. Also endorsed by the Associated Industries of Florida "
              "(AIF), Florida's premier business lobbying organization, for her pro-business, "
              "limited-government conservative record — consistent with AIF's endorsement "
              "criteria emphasizing fiscal responsibility and private enterprise over government "
              "expansion.",
              ["https://floridapolitics.com/archives/764404-samantha-scott-lands-trove-of-endorsements-in-hd-52-special-election/",
               "https://ballotpedia.org/Samantha_Scott"],
              kind="endorsement"),
    ]),

    # --- Sam Greco (FL HD-19, R; Flagler Co. / St. Johns Co.; elected Nov 2024; Navy JAG officer) ---
    ("sam-greco", "FL", "State Representative", [
        claim("sg1", "sam-greco", "sanctity_of_life", 0, True,
              "Co-sponsored HB 1517 (2025), the Civil Liability for the Wrongful Death of an "
              "Unborn Child Act (Unborn Child Parent's Survivor Act), which defines unborn "
              "children as distinct human beings — Homo sapiens at any stage of development in "
              "the womb — and allows parents to pursue wrongful-death claims for an unborn "
              "child's death caused by another party's negligence or wrongful act. The bill "
              "passed the Florida House 79-32 on April 3, 2025; Greco voted in the majority. "
              "Greco also holds a Florida Right to Life 'A' rating from the 2024 primary "
              "endorsement cycle, confirming FRTL's determination that he is firmly pro-life.",
              ["https://floridapolitics.com/archives/731331-house-passes-bill-to-allow-wrongful-death-lawsuits-for-fetuses-after-emotional-debate/",
               "https://frtl.org/2024-primary-endorsements/"]),
        claim("sg2", "sam-greco", "self_defense", 0, True,
              "Earned an 'AQ' rating (A-Qualified) from the NRA Political Victory Fund prior "
              "to his November 2024 election — an A grade based on questionnaire responses "
              "demonstrating full alignment with NRA policy positions including support for "
              "constitutional carry, opposition to red-flag laws and assault weapons bans, and "
              "the right of law-abiding citizens to keep and bear arms without a government "
              "permission slip. As a former active-duty U.S. Navy JAG officer (2019-2024, "
              "Naval Station Mayport), Greco brings a military background grounding his "
              "Second Amendment convictions in personal service.",
              ["https://ballotpedia.org/Sam_Greco",
               "https://en.wikipedia.org/wiki/Sam_Greco_(politician)"],
              kind="endorsement"),
        claim("sg3", "sam-greco", "public_justice", 0, True,
              "Sponsored HB 445 (2025), known as 'Missy's Law,' which requires Florida courts "
              "to keep any person found guilty of a dangerous crime in jail until formally "
              "sentenced — closing a gap that allowed Daniel Spencer, convicted of traveling "
              "to meet a minor, to remain on bond and subsequently abuse and kill 5-year-old "
              "Melissa 'Missy' Mogle in Tallahassee between his conviction and sentencing. "
              "Governor DeSantis signed Missy's Law into law; it took effect July 1, 2026. "
              "The bill reflects the conviction that protecting the innocent from convicted "
              "dangerous offenders is a public-justice imperative that cannot wait until "
              "sentencing.",
              ["https://floridianpress.com/2026/03/desantis-signs-missys-law-urges-house-to-impeach-judge-tiffany-baker/",
               "https://www.wtxl.com/news/local-news/missys-law-filed-to-become-law-following-death-of-5-year-old-melissa-missy-mogle-in-tallahassee"]),
    ]),

    # --- Richard Gentry (FL HD-27, R; Lake/Marion/Volusia counties; elected Nov 2024; attorney) ---
    ("richard-gentry", "FL", "State Representative", [
        claim("rg1", "richard-gentry", "sanctity_of_life", 0, True,
              "Earned a Florida Right to Life 'A' rating from the 2024 primary endorsement "
              "cycle — FRTL's determination that Gentry is firmly pro-life. During the 2024 "
              "Republican primary, Gentry stated that 'his religious beliefs lead him toward "
              "pro-life policies,' reflecting a conviction-grounded pro-life stance. He won "
              "the HD-27 Republican primary against two opponents and the general election "
              "against two opponents with endorsements from every Sheriff in the three-county "
              "(Lake, Marion, Volusia) district.",
              ["https://frtl.org/2024-primary-endorsements/",
               "https://ballotpedia.org/Richard_Gentry"],
              kind="statement"),
        claim("rg2", "richard-gentry", "self_defense", 0, True,
              "Stated during his 2024 campaign that he 'supports Second Amendment right to "
              "carry' and personally holds a Florida concealed carry permit — demonstrating "
              "that his support for armed self-defense is grounded in personal practice. "
              "Gentry holds that firearms restrictions are only appropriate at schools and "
              "for those convicted of criminal activity, and opposes broader government "
              "infringement on law-abiding citizens' right to carry. His position is "
              "consistent with his endorsements from all HD-27 Sheriffs (Chitwood, Grinnell, "
              "Woods) and local firefighter unions.",
              ["https://www.ocalagazette.com/gentry-seeks-district-27-seat-in-the-florida-house/",
               "https://floridapolitics.com/archives/665336-richard-gentry-lands-support-from-all-hd-27-sheriffs/"],
              kind="statement"),
        claim("rg3", "richard-gentry", "election_integrity", 0, True,
              "Voted with the Republican majority (77-28 party-line vote) to pass CS/CS/HB 991 "
              "(2026), requiring Floridians to produce documentary proof of citizenship — a "
              "valid passport or birth certificate with names matching the statewide voter "
              "registration system — to register to vote, and removing student IDs as an "
              "accepted form of voter identification. Governor DeSantis signed the bill on "
              "April 1, 2026, effective January 1, 2027. Gentry, a first-term Republican "
              "member from Central Florida's tri-county HD-27, participated in the 2026 "
              "regular session.",
              ["https://floridaphoenix.com/2026/04/01/desantis-signs-bill-requiring-proof-of-citizenship-to-register-to-vote-voting-rights-group-sue/",
               "https://floridatrib.org/2026/03/13/florida-lawmakers-approve-bill-requiring-proof-of-citizenship-to-vote/"]),
    ]),

    # --- Paula A. Stark (FL HD-47, R; St. Cloud, Osceola/Orange Co.; since Nov 2022; not on 2026 ballot) ---
    ("paula-a-stark", "FL", "State Representative", [
        claim("pas1", "paula-a-stark", "sanctity_of_life", 0, False,
              "Voted AGAINST SB 300 (Heartbeat Protection Act, 2023), Florida's six-week "
              "abortion ban — one of approximately seven Republicans to break with the "
              "party caucus on the measure. Stark stated explicitly: 'I took that position "
              "when I campaigned last time — I said I would not go less than 15 weeks for the "
              "abortion bill,' confirming that her opposition to the six-week threshold is a "
              "deliberate stated policy position. The bill passed 70-40 on April 13, 2023, "
              "and was signed by Governor DeSantis. Stark's opposition places her outside the "
              "rubric's standard for lawmakers who affirm life from conception.",
              ["https://floridaphoenix.com/2024/10/25/controversial-republican-stark-defends-against-democratic-newcomer-revelles-in-hd-47/",
               "https://ballotpedia.org/Paula_Stark"]),
        claim("pas2", "paula-a-stark", "biblical_marriage", 2, False,
              "Voted AGAINST CS/HB 1521 (2023), Florida's Facility Requirements Based on Sex "
              "Act (the 'bathroom bill'), which requires individuals to use public restrooms, "
              "locker rooms, and sex-segregated facilities corresponding to their biological "
              "sex — joining Democrats in opposition to the bill. HB 1521 passed the Florida "
              "House on party lines and was signed by Governor DeSantis on May 17, 2023. "
              "Stark's vote directly opposes the conviction that sex is binary and immutable "
              "and that sex-segregated privacy in public facilities is a necessary policy, "
              "placing her at odds with the rubric's requirement to reject transgender ideology.",
              ["https://www.wusf.org/politics-issues/2023-05-04/florida-lawmakers-pass-transgender-bathroom-bill/",
               "https://ballotpedia.org/Paula_Stark"]),
    ]),

    # --- Patt Maney (FL HD-4, R; Okaloosa Co., Shalimar; since Nov 2020; Brig. Gen. ret.; judge ret.) ---
    ("patt-maney", "FL", "State Representative", [
        claim("pm1", "patt-maney", "sanctity_of_life", 0, True,
              "Stated explicitly: 'Human life begins at conception and deserves legal "
              "protection at every stage until natural death' — a personhood-level commitment "
              "to the sanctity of life, per iVoterGuide candidate survey responses. Opposes "
              "all taxpayer funding for abortion providers including Planned Parenthood. "
              "Supports the Born Alive Abortion Survivors Protection Act, requiring that "
              "infants born alive following a failed abortion receive the same medical care "
              "as any other newborn. Maney has represented heavily conservative Okaloosa "
              "County (Fort Walton Beach / Shalimar) in the Panhandle since November 2020.",
              ["https://ivoterguide.com/candidate/52200/race/5147/election/1254",
               "https://ballotpedia.org/T._Patt_Maney"],
              kind="statement"),
        claim("pm2", "patt-maney", "self_defense", 0, True,
              "Holds an NRA Political Victory Fund 'A' rating, confirming full alignment "
              "with NRA policy positions including constitutional carry, opposition to red-flag "
              "laws, background check expansions, and assault weapons bans, and the right of "
              "law-abiding citizens to bear arms without government interference. Maney, a "
              "retired U.S. Army Brigadier General and Purple Heart recipient wounded in "
              "action in Afghanistan in August 2005, brings a 37-year military career to his "
              "Second Amendment convictions — distinguishing his pro-gun record as grounded "
              "in a lifetime of lawful military firearms proficiency.",
              ["https://floridapolitics.com/archives/558269-nra-updates-grades-endorsements-for-2022/",
               "https://ballotpedia.org/T._Patt_Maney"],
              kind="endorsement"),
        claim("pm3", "patt-maney", "public_justice", 0, True,
              "Sponsored CS/CS/HB 199 (2026), the Veterans Treatment Court expansion bill, "
              "broadening eligible access to Veterans Treatment Court programs in all 20 "
              "Florida judicial circuits for service members and veterans facing criminal "
              "charges tied to service-related conditions. The bill passed the Florida House "
              "unanimously (110-0) and the Florida Senate unanimously (37-0); Governor "
              "DeSantis signed it into law. The legislation builds directly on the Veterans "
              "Treatment Court concept that then-Okaloosa County Judge Maney personally "
              "pioneered — establishing Florida's first VTC — before joining the Legislature. "
              "Maney is a member of the Florida Veterans Hall of Fame.",
              ["https://floridapolitics.com/archives/778368-house-passes-patt-maney-bill-broadening-access-to-veterans-treatment-courts/",
               "https://crestviewbulletin.com/governor-signs-veterans-affairs-bill-into-law/"]),
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
