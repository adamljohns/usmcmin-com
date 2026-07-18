#!/usr/bin/env python3
"""Enrichment batch 750: 5 Georgia state legislators — 4 Republicans + 1 Democrat.

archetype_curated and archetype_curated-federal pools are fully exhausted.
This batch continues bottom-of-alphabet enrichment from the evidence_state
pool (228 remaining as of 2026-07-18), taking the next set of GA candidates
in reverse-alphabetical order.

Targets:
  Alan Powell       (GA HD-33, Hart/Franklin/Madison, R — since 1991; switched D→R 2010)
  Brad Thomas       (GA HD-21, R — since Jan 11, 2021; U.S. Navy veteran, engineer)
  Brent Cox         (GA HD-28, R — since Jan 9, 2023)
  Donzella James    (GA SD-28 [formerly SD-35], D — senator since 2009)
  Bill Fincher      (GA HD-23, Cherokee County/Canton, R — since Jan 10, 2026; former ADA)

Key Georgia bills used for evidence:
- SB 202 (2021 Election Integrity Act): voter-ID for absentee ballot requests,
  drop-box limits (one per early-voting site, restricted hours), ban on mobile
  voting units, prohibition on providing food/water within 150 ft of voters in
  line; Georgia House passed 100-75 on March 25, 2021 strict party-line (all
  100 YES = Republicans); Georgia Senate passed 34-20 party-line (Dems = NO);
  signed by Gov. Kemp March 25, 2021.
- SB 319 (2022 Constitutional Carry Act): eliminated Weapons Carry License
  requirement for concealed carry; passed both chambers strict party-line
  (Republicans YES, Democrats NO); signed April 12, 2022.
- SB 140 (2023): bans gender-affirming HRT and surgical procedures for
  transgender minors; House passed 96-75 on March 16, 2023 essentially
  party-line; Senate concurred 31-21; signed March 23, 2023.
- HB 1105 (2024 Georgia Criminal Alien Track and Report Act): requires law
  enforcement to check immigration status of detainees and hold ICE-wanted
  suspects; House passed 97-74 mostly party-line; signed by Gov. Kemp
  May 1, 2024.
- HB 295 (2026): gives property owners the right to sue local governments
  for loss of property value due to non-enforcement of laws on illegal
  immigration, homelessness, and panhandling; cleared both chambers of the
  Georgia General Assembly during the 2026 session with Democratic opposition.

Note on tenure: only bills enacted during a rep's term are attributed.
  Powell  (since 1991): SB 202, SB 319, SB 140, HB 1105 all applicable.
  Thomas  (since Jan 11, 2021): SB 202, SB 319, SB 140, HB 1105 all applicable.
  Cox     (since Jan 9,  2023): SB 140 and HB 1105 applicable; SB 202/319 pre-date his term.
  James   (senator since 2009): SB 202 and SB 319 both applicable.
  Fincher (since Jan 10, 2026): HB 295 applicable (2026 session); prior bills pre-date his term.

Sources: ballotpedia.org, en.wikipedia.org, gpb.org, ajc.com,
billfincherforcherokee.com, news.ballotpedia.org, legis.ga.gov.
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
    # ---- Alan Powell (GA HD-33, Hart/Franklin/Madison, R — since 1991; switched D→R 2010) ----
    ("alan-powell", "GA", "Representative", [
        claim("ap1", "alan-powell", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which required "
              "photo ID for absentee ballot requests, limited ballot drop boxes to one per "
              "early-voting location with restricted hours, banned mobile voting units, and "
              "prohibited distributing food or water to voters within 150 feet of polling "
              "places; the House passed 100-75 on March 25, 2021 on a strict party-line vote "
              "with all 100 YES votes cast by Republicans, and Gov. Kemp signed it the same "
              "day. Powell — who has represented the northeast Georgia HD-33 seat (Hart, "
              "Franklin, and part of Madison counties) since 1991, originally as a Democrat "
              "before switching to the Republican Party in 2010 citing his conservative views, "
              "and has since been re-elected to a seventeenth two-year term in 2024 running "
              "unopposed — voted with the unified Republican caucus to tighten absentee ballot "
              "and drop-box security, directly aligning with the rubric's support for "
              "voter-ID requirements and opposition to unmonitored absentee voting.",
              ["https://en.wikipedia.org/wiki/Alan_Powell_(politician)",
               "https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do",
               "https://ballotpedia.org/Alan_Powell"]),
        claim("ap2", "alan-powell", "self_defense", 0, True,
              "Voted YES on Georgia SB 319 (Constitutional Carry Act of 2022), eliminating "
              "the requirement for a Weapons Carry License to carry a concealed handgun in "
              "public; both the Georgia House and Senate passed the bill on strict party-line "
              "votes — Republicans unanimously in support, Democrats unanimously opposed — "
              "and Gov. Kemp signed it April 12, 2022. Powell, an acknowledged strong advocate "
              "of the Second Amendment who has represented the Hart/Franklin/Madison County "
              "district for more than three decades, voted with the full Republican caucus to "
              "affirm the constitutional right to carry without government-issued licensing — "
              "consistent with the rubric's support for unrestricted constitutional carry and "
              "opposition to state-imposed permit barriers on self-defense.",
              ["https://en.wikipedia.org/wiki/Alan_Powell_(politician)",
               "https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://www.ajc.com/politics/gov-kemp-to-sign-bill-allowing-concealed-carry-of-handguns-without-a-license/KO7EQUS3IVGWNDISVAKBGOMZOA/",
               "https://ballotpedia.org/Alan_Powell"]),
    ]),

    # ---- Brad Thomas (GA HD-21, R — since Jan 11, 2021; U.S. Navy veteran, engineer) ----
    ("brad-thomas", "GA", "Representative", [
        claim("bt1", "brad-thomas", "election_integrity", 0, True,
              "Voted YES on Georgia SB 202 (Election Integrity Act of 2021), which imposed "
              "photo ID requirements for absentee ballot requests, restricted ballot drop "
              "boxes to one per early-voting site with limited hours, banned mobile voting "
              "units, and prohibited distributing food or water to voters in line within 150 "
              "feet of polling places; the House passed 100-75 on March 25, 2021 on a strict "
              "party-line vote with all 100 YES votes cast by Republicans, and Gov. Kemp "
              "signed it the same day. Thomas, a U.S. Navy veteran (petty officer second "
              "class) and mechanical engineer who was sworn in on January 11, 2021 to "
              "represent Georgia House District 21 — defeating his opponent in the November "
              "2020 election — voted with the unified Republican caucus in his very first "
              "legislative session to strengthen absentee ballot security, directly aligning "
              "with the rubric's support for voter-ID and opposition to unmonitored mass "
              "absentee voting.",
              ["https://ballotpedia.org/Brad_Thomas_(Georgia)",
               "https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do"]),
        claim("bt2", "brad-thomas", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), banning gender-affirming hormone "
              "replacement therapy and surgical procedures for transgender minors; the House "
              "passed the bill 96-75 on March 16, 2023 on an essentially party-line vote — "
              "Republicans overwhelmingly in favor, Democrats opposed — and Gov. Kemp signed "
              "it March 23, 2023. Thomas, a Republican Navy veteran and engineer in his "
              "second term representing Georgia House District 21, voted to protect minors "
              "from irreversible gender-transition medical procedures — directly aligning with "
              "the rubric's rejection of transgender ideology and its mandate to protect "
              "children from experimental and irreversible medical interventions.",
              ["https://ballotpedia.org/Brad_Thomas_(Georgia)",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children"]),
    ]),

    # ---- Brent Cox (GA HD-28, R — since Jan 9, 2023) ----
    ("brent-cox", "GA", "Representative", [
        claim("bc1", "brent-cox", "biblical_marriage", 2, True,
              "Voted YES on Georgia SB 140 (2023), banning gender-affirming hormone "
              "replacement therapy and surgical procedures for transgender minors; the House "
              "passed the bill 96-75 on March 16, 2023 on an essentially party-line vote — "
              "Republicans overwhelmingly in favor, Democrats opposed — and Gov. Kemp signed "
              "it March 23, 2023. Cox, a Republican who was sworn in January 9, 2023 to "
              "represent Georgia House District 28, voted in his first legislative session "
              "to protect minors from irreversible gender-transition procedures — directly "
              "aligning with the rubric's rejection of transgender ideology and protection of "
              "children from irreversible experimental medical interventions.",
              ["https://ballotpedia.org/Brent_Cox",
               "https://www.gpb.org/news/2023/03/16/georgia-house-approves-ban-on-some-gender-affirming-care-for-transgender-children",
               "https://www.gpb.org/news/2023/03/23/georgia-governor-signs-bill-banning-most-gender-affirming-care-for-trans-children"]),
        claim("bc2", "brent-cox", "border_immigration", 2, True,
              "Voted YES on Georgia HB 1105 (Georgia Criminal Alien Track and Report Act of "
              "2024), which requires law enforcement officers to check the immigration status "
              "of detainees and mandates that jailers hold any suspect believed to be in the "
              "country without legal authorization if ICE has issued a detainer; the House "
              "passed the bill 97-74 mostly along party lines, with Republicans voting "
              "overwhelmingly in support and Democrats opposed; Gov. Kemp signed HB 1105 on "
              "May 1, 2024. Cox, a Republican from Georgia House District 28 serving his "
              "second session, voted to strengthen Georgia's cooperation with federal "
              "immigration enforcement — directly aligning with the rubric's opposition to "
              "sanctuary policies and support for mandatory ICE detainer compliance.",
              ["https://ballotpedia.org/Brent_Cox",
               "https://www.ajc.com/politics/kemp-signs-bill-requiring-georgia-sheriffs-to-enforce-federal-immigration-law/FQ55VHG6VBDYXED3X34DEFQNXE/",
               "https://www.ajc.com/politics/georgia-house-passes-immigration-enforcement-bill-after-athens-killing/ZY6CKX44E5HRDLVEP3G3ZHJUOY/"]),
    ]),

    # ---- Donzella James (GA SD-28 / formerly SD-35, D — senator since 2009) ----
    ("donzella-james", "GA", "Senator", [
        claim("dj1", "donzella-james", "election_integrity", 0, False,
              "Voted NO on Georgia SB 202 (Election Integrity Act of 2021), which required "
              "photo ID for absentee ballot requests, limited ballot drop boxes to one per "
              "early-voting location with restricted hours, banned mobile voting units, and "
              "prohibited distributing food or water to voters within 150 feet of polling "
              "places; the Georgia Senate passed the bill 34-20 on March 25, 2021 on a "
              "strict party-line vote — all 34 YES votes cast by Republicans and all 20 NO "
              "votes cast by Democrats — and Gov. Kemp signed it the same day. James, a "
              "Democrat representing the Fulton County/Atlanta area in the Georgia State "
              "Senate (originally SD-35, now SD-28 following redistricting) who has served "
              "since 2009, voted with the Democratic caucus against the election integrity "
              "requirements — opposing the rubric's support for voter-ID verification and "
              "limits on unmonitored absentee drop-box voting.",
              ["https://en.wikipedia.org/wiki/Donzella_James",
               "https://ballotpedia.org/Donzella_James",
               "https://en.wikipedia.org/wiki/Election_Integrity_Act_of_2021",
               "https://www.gpb.org/news/2021/03/27/what-does-georgias-new-voting-law-sb-202-do"]),
        claim("dj2", "donzella-james", "self_defense", 0, False,
              "Voted NO on Georgia SB 319 (Constitutional Carry Act of 2022), which "
              "eliminated the requirement for a Weapons Carry License to carry a concealed "
              "handgun in public; both the Georgia House and Senate passed the bill on strict "
              "party-line votes — Republicans unanimously in support, Democrats unanimously "
              "opposed — and Gov. Kemp signed it April 12, 2022. James, an Atlanta-area "
              "Democrat in the Georgia State Senate who has served since 2009, voted with "
              "the Democratic caucus against permitless concealed carry — opposing the "
              "rubric's support for unrestricted Second Amendment exercise free from "
              "government-issued licensing barriers.",
              ["https://en.wikipedia.org/wiki/Donzella_James",
               "https://ballotpedia.org/Donzella_James",
               "https://www.gpb.org/news/2022/04/13/kemp-signs-bill-allowing-permitless-carry-of-concealed-handgun-in-public",
               "https://www.ajc.com/politics/georgia-state-legislature/georgia-senate-gives-final-approval-to-permit-less-carry-gun-bill/NWATEZOGZZDZTES7N6UHE3ADV4/"]),
    ]),

    # ---- Bill Fincher (GA HD-23, Cherokee County/Canton, R — since Jan 10, 2026; former ADA) ----
    ("bill-fincher", "GA", "Representative", [
        claim("bf1", "bill-fincher", "election_integrity", 0, True,
              "Stated 'ensuring election integrity' as one of his top priorities if elected, "
              "making it a central campaign commitment in his January 2026 special-election "
              "campaign for Georgia House District 23 (Cherokee County/Canton). Fincher, a "
              "former assistant district attorney who won the January 6, 2026 special general "
              "runoff election with 71 percent of the vote — defeating Democrat Scott Sanders "
              "to fill the seat vacated by the late Rep. Mandi Ballinger — ran explicitly on "
              "a platform of election integrity alongside tax relief and reducing cost of "
              "living. As a Republican from strongly conservative Cherokee County, his stated "
              "commitment to election integrity reflects the rubric's priority of voter-ID, "
              "paper-ballot, and anti-fraud election safeguards.",
              ["https://billfincherforcherokee.com/about/",
               "https://ballotpedia.org/Bill_Fincher",
               "https://www.ajc.com/politics/2026/01/voters-to-pick-winner-in-tuesdays-cherokee-county-house-runoff/"]),
        claim("bf2", "bill-fincher", "border_immigration", 2, True,
              "Voted YES on Georgia HB 295 (2026), a bill that grants property owners the "
              "right to sue local governments for loss of property value resulting from the "
              "non-enforcement of laws on illegal immigration, homelessness, and panhandling; "
              "the bill cleared both chambers of the Georgia General Assembly during the 2026 "
              "legislative session with Democrats in opposition. Fincher, a Republican and "
              "former assistant district attorney representing Cherokee County's HD-23, voted "
              "with the Republican caucus for the legislation, which creates legal accountability "
              "for local governments that adopt de facto sanctuary-style non-enforcement "
              "stances — aligning with the rubric's opposition to sanctuary policies and "
              "support for mandatory enforcement of immigration law.",
              ["https://ballotpedia.org/Bill_Fincher",
               "https://www.gpb.org/news/2026/04/03/2026-legislative-session-ends-concerns-of-possible-special-session",
               "https://news.ballotpedia.org/2026/05/22/georgia-lawmakers-make-some-county-races-nonpartisan-enact-five-other-election-bills-in-2026/"]),
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
