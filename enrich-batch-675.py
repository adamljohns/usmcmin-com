#!/usr/bin/env python3
"""Enrichment batch 675: hand-curated claims for 5 state legislators (OR + OH).

archetype_curated federal bucket exhausted; targets next tier: archetype_party_default
state senators from bottom of alphabet (OR, OH). Uses state-aware find_candidate()
to avoid cross-state slug collisions (dick-anderson exists in both ND and OR).

Targets: David Brock Smith (OR), Dick Anderson (OR), Fred Girod (OR),
Tim Schaffer (OH), Thomas F. Patton (OH).
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
    # ---------- David Brock Smith (OR, State Senator / 2026 U.S. Senate candidate) ----------
    ("david-brock-smith", "OR", "State Senator", [
        claim("dbs1", "david-brock-smith", "sanctity_of_life", 0, True,
              "Publicly affirms 'Human life deserves legal protection from conception until natural death' and supports enforcing the Comstock Act banning interstate transportation of abortion-inducing drugs — one of the most explicit personhood positions among 2026 Pacific Northwest candidates.",
              ["https://ivoterguide.com/candidate/91853/race/26570/election/1403",
               "https://oregonvotes.gov/voters-guide/english/davidbrocksmith.html"]),
        claim("dbs2", "david-brock-smith", "sanctity_of_life", 4, True,
              "Opposes Planned Parenthood and all abortion providers receiving taxpayer funds from federal, state, or local governments — rejecting public subsidies for the abortion industry at every level.",
              ["https://ivoterguide.com/candidate/91853/race/26570/election/1403",
               "https://ballotpedia.org/David_Brock_Smith_(Oregon_state_senator)"]),
        claim("dbs3", "david-brock-smith", "self_defense", 1, True,
              "Wrote a formal letter to the Oregon courts calling Ballot Measure 114 'abusive and unconstitutional,' opposing its permit-to-purchase firearm requirement and ban on magazines holding more than 10 rounds — urging the court to grant a preliminary injunction and block the gun-control law.",
              ["https://www.oregonlegislature.gov/smithd/Documents/Letter-%20Ballot%20Measure%20114%20is%20Unconstitutional.pdf",
               "https://ballotpedia.org/David_Brock_Smith_(Oregon_state_senator)"]),
    ]),

    # ---------- Dick Anderson (OR SD5, State Senator — state=OR to avoid ND collision) ----------
    ("dick-anderson", "OR", "State Senator", [
        claim("da1", "dick-anderson", "sanctity_of_life", 0, True,
              "Voted NO on Oregon HB 2002 (2023), a sweeping bill that expanded abortion access, required Medicaid and private insurers to cover abortion services, and allowed minors of any age to obtain abortions without parental notification — opposing codification of unrestricted abortion into Oregon law.",
              ["https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/",
               "https://ballotpedia.org/Dick_Anderson_(Oregon)"]),
        claim("da2", "dick-anderson", "biblical_marriage", 2, True,
              "Voted NO on Oregon HB 2002 (2023), which also mandated Medicaid and private insurance coverage for gender-affirming medical procedures and deployed mobile clinics to expand minors' access to cross-sex treatments — opposing state-sponsored promotion of transgender ideology.",
              ["https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/",
               "https://oregoncapitalchronicle.com/2023/05/22/heres-what-oregons-controversial-abortion-gender-affirming-care-bill-would-do/"]),
        claim("da3", "dick-anderson", "family_child_sovereignty", 0, True,
              "Voted YES on a June 2023 motion to re-refer HB 2002 to the Oregon Senate Rules Committee — a procedural move to block the bill's provision allowing minors of any age to terminate pregnancies without parental notification, affirming parental authority over their children's medical decisions.",
              ["https://fastdemocracy.com/bill-search/or/2023/bills/ORB00017712/",
               "https://ballotpedia.org/Dick_Anderson_(Oregon)"]),
    ]),

    # ---------- Fred Girod (OR SD9, State Senator, former Senate Minority Leader) ----------
    ("fred-girod", "OR", "State Senator", [
        claim("fg1", "fred-girod", "sanctity_of_life", 0, True,
              "Voted NO on Oregon HB 4127 (2026), a bill directing Medicaid payments to reproductive health care providers — opposing public funding for abortion-related services through the state Medicaid program.",
              ["https://fastdemocracy.com/bill-search/or/2026/bills/ORB00021809/",
               "https://www.oregonlegislature.gov/girod"]),
        claim("fg2", "fred-girod", "economic_stewardship", 4, True,
              "Participated in the 2019 Oregon Senate Republican walkout against HB 2020 — Oregon's sweeping cap-and-trade carbon regulation bill — preventing a quorum and helping defeat a government-mandated carbon tax that would have imposed ESG-aligned climate burdens on Oregon's farms, rural businesses, and working families.",
              ["https://en.wikipedia.org/wiki/2019_Oregon_Senate_Republican_walkouts",
               "https://ballotpedia.org/Fred_Girod"]),
    ]),

    # ---------- Tim Schaffer (OH SD20, State Senator) ----------
    ("tim-schaffer", "OH", "State Senator", [
        claim("ts1", "tim-schaffer", "sanctity_of_life", 0, True,
              "Believes human life begins at conception and deserves legal protection at every stage until natural death; endorsed by Ohio Right to Life and Right to Life Action Coalition of Ohio; supports the Born Alive Abortion Survivors Protection Act requiring life-saving care for infants who survive abortion attempts.",
              ["https://ivoterguide.com/candidate?canK=19267&elecK=766&primarypartyk=-&raceK=11076",
               "https://www.buckeyefirearms.org/all-politicians-are-not-same-interview-state-sen-tim-schaffer"]),
        claim("ts2", "tim-schaffer", "sanctity_of_life", 4, True,
              "Opposes taxpayer funding for Planned Parenthood and all abortion providers at the federal, state, and local level — a stated position defunding the abortion industry from public dollars.",
              ["https://ivoterguide.com/candidate?canK=19267&elecK=766&primarypartyk=-&raceK=11076",
               "https://ballotpedia.org/Tim_Schaffer"]),
        claim("ts3", "tim-schaffer", "self_defense", 0, True,
              "A staunch Second Amendment defender recognized by the Buckeye Firearms Association; as an Ohio legislator sponsored an NRA-backed bill allowing licensed concealed carry holders to carry in bars and restaurants — expanding armed self-defense rights in everyday settings — signed into law by the governor.",
              ["https://www.buckeyefirearms.org/all-politicians-are-not-same-interview-state-sen-tim-schaffer",
               "https://en.wikipedia.org/wiki/Tim_Schaffer"]),
    ]),

    # ---------- Thomas F. Patton (OH SD24, State Senator, former Senate Majority Leader) ----------
    ("thomas-f-patton", "OH", "State Senator", [
        claim("tp1", "thomas-f-patton", "sanctity_of_life", 0, True,
              "Endorsed by Ohio Right to Life PAC in both his 2022 Ohio House (HD-17) and 2024 Ohio State Senate (SD-24) races, reflecting a consistent pro-life record spanning multiple terms recognized by Ohio's leading pro-life organization.",
              ["https://ohiolife.org/endorsements/",
               "https://ballotpedia.org/Thomas_Patton"]),
        claim("tp2", "thomas-f-patton", "self_defense", 0, True,
              "Served in the Ohio House of Representatives when the Republican majority passed SB 215 (Ohio's constitutional carry law, signed March 14, 2022), allowing any Ohioan 21 or older who may legally possess a firearm to carry concealed without a permit — a landmark gun-rights expansion backed by the NRA and Buckeye Firearms Association.",
              ["https://www.buckeyefirearms.org/breaking-sb-215-constitutional-carry-passes-out-committee",
               "https://ballotpedia.org/Thomas_Patton"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents cross-state slug collisions (e.g. dick-anderson ND vs OR).

    Returns the single candidate matching (slug, state, office contains office_keyword)
    or None — never returns a wrong-state same-slug record.
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
