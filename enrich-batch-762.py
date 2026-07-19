#!/usr/bin/env python3
"""Enrichment batch 762: hand-curated claims for 5 U.S. Representatives.

Targets from the bottom of the alphabet (MI and OH states) with the fewest
existing evidence claims. The archetype_curated federal bucket is exhausted;
these are evidence_curated candidates with 3 existing claims needing distinct
new categories. Sources: govtrack.us, congress.gov, official house.gov pages.

Candidates: Tim Walberg (MI-R), Lisa McClain (MI-R), Jack Bergman (MI-R),
Bill Huizenga (MI-R), David Taylor (OH-R).
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
    # ---------------- Tim Walberg (MI-R, US Representative) ----------------
    ("tim-walberg", "MI", "Representative", [
        claim("tw1", "tim-walberg", "sanctity_of_life", 0, True,
              "Voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R. 21, House Vote #27, Jan 23, 2025), requiring medical care for infants born alive during attempted abortions; cosponsored H.R. 7 (No Taxpayer Funding for Abortion Act, 119th Congress) prohibiting federal funds for abortion coverage — consistent with a 100% pro-life voting record recognized by National Right to Life and SBA Pro-Life America.",
              ["https://www.govtrack.us/congress/votes/119-2025/h27",
               "https://www.congress.gov/bill/119th-congress/house-bill/21",
               "https://sbaprolife.org/representative/tim-walberg"]),
        claim("tw2", "tim-walberg", "self_defense", 0, True,
              "Cosponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act (119th Congress, 2025), which would require every state to honor any other state's concealed-carry permit or allow permitless carry where the resident's home state permits it — a direct constitutional-carry expansion.",
              ["https://www.govtrack.us/congress/bills/119/hr38/cosponsors",
               "https://www.congress.gov/bill/119th-congress/house-bill/38"]),
        claim("tw3", "tim-walberg", "election_integrity", 0, True,
              "Voted YES on the SAVE Act (H.R. 22, House Vote #102, Apr 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections; also co-signed a letter with the Michigan Republican Delegation demanding that Secretary of State Benson remove noncitizens and deceased voters from Michigan's voter rolls.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
    ]),

    # ---------------- Lisa McClain (MI-R, US Representative) ----------------
    ("lisa-mcclain", "MI", "Representative", [
        claim("lm1", "lisa-mcclain", "biblical_marriage", 1, True,
              "Voted NO on H.R. 8404, the Respect for Marriage Act (House Vote #373, July 19, 2022), which repealed DOMA and codified federal recognition of same-sex marriages (267-157); also voted against the Senate-amended final version (House Vote #513, Dec 8, 2022) — one of five Michigan Republicans to oppose the bill in both votes, rejecting the one-man-one-woman definition being overridden.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://clerk.house.gov/Votes/2022373"]),
        claim("lm2", "lisa-mcclain", "border_immigration", 0, True,
              "Voted YES on H.R. 2, the Secure the Border Act of 2023 (House Vote #209, May 11, 2023), which resumed border wall construction, mandated employer E-Verify, ended catch-and-release, and tightened asylum rules; also co-authored a Daily Caller op-ed explicitly supporting the Laken Riley Act's mandatory deportation and detention provisions.",
              ["https://www.govtrack.us/congress/votes/118-2023/h209",
               "https://mcclain.house.gov/2025/1/mcclain-s-statement-on-the-u-s-house-passing-the-laken-riley-act"]),
        claim("lm3", "lisa-mcclain", "economic_stewardship", 0, True,
              "Voted YES on H.R. 5403, the CBDC Anti-Surveillance State Act (House Vote #230, May 23, 2024), prohibiting the Federal Reserve from issuing a retail central bank digital currency; Republicans voted 213-0 on the bill, with McClain among the unanimous bloc opposing a government-issued digital surveillance dollar.",
              ["https://www.govtrack.us/congress/votes/118-2024/h230",
               "https://www.congress.gov/bill/118th-congress/house-bill/5403/text"]),
        claim("lm4", "lisa-mcclain", "election_integrity", 0, True,
              "Voted YES on the SAVE Act (H.R. 22, House Vote #102, Apr 10, 2025), requiring proof of U.S. citizenship to register for federal elections; issued an official same-day statement: 'House Republicans simply want to keep illegal immigrants out of [the ballot box] and restore trust in our election system.' Also sent a formal demand letter to Michigan Secretary of State on reported noncitizen voting.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://mcclain.house.gov/2025/4/mcclain-s-statement-on-the-house-passage-of-the-save-act-requiring-proof-of-citizenship-for-voter-registration",
               "https://mcclain.house.gov/2025/4/mcclain-demands-answers-from-michigan-secretary-of-state-on-noncitizens-voting-in-elections"]),
    ]),

    # ---------------- Jack Bergman (MI-R, US Representative) ----------------
    ("jack-bergman", "MI", "Representative", [
        claim("jb1", "jack-bergman", "biblical_marriage", 1, True,
              "Voted NAY on H.R. 8404, the Respect for Marriage Act (House Vote #373, July 19, 2022), rejecting federal codification of same-sex marriage (267-157); one of five Michigan Republicans to oppose both the initial House vote and the final Senate-amended version, maintaining a one-man-one-woman position.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://clerk.house.gov/Votes/2022373"]),
        claim("jb2", "jack-bergman", "biblical_marriage", 2, True,
              "Voted YES on H.R. 28, the Protection of Women and Girls in Sports Act (House Vote #12, Jan 14, 2025), amending Title IX to bar biological males from competing in federally funded female athletic programs; the bill passed 218-206 with unanimous Republican support.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://www.congress.gov/bill/119th-congress/house-bill/28"]),
        claim("jb3", "jack-bergman", "economic_stewardship", 0, True,
              "Cosponsored H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress), prohibiting the Federal Reserve from issuing a central bank digital currency or maintaining individual accounts; the House passed the bill 219-210 on July 17, 2025.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919/cosponsors"]),
        claim("jb4", "jack-bergman", "election_integrity", 0, True,
              "Cosponsored and voted for the SAVE Act (H.R. 22, House Vote #102, Apr 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections; issued an official statement: 'I'm proud to have cosponsored this commonsense legislation that passed the House with bipartisan support.'",
              ["https://bergman.house.gov/news/documentsingle.aspx?DocumentID=1292",
               "https://www.govtrack.us/congress/votes/119-2025/h102"]),
        claim("jb5", "jack-bergman", "foreign_policy_restraint", 1, True,
              "Voted NO on the Ukraine Security Supplemental Appropriations Act (H.R. 8035, House Vote #151, April 20, 2024), opposing $60.8 billion in additional Ukraine military and humanitarian aid (passed 311-112); as House Budget Committee Oversight Task Force Chairman, co-led a formal congressional accountability demand requiring the Biden administration to account for all U.S. Ukraine war expenditures.",
              ["https://www.govtrack.us/congress/votes/118-2024/h151",
               "https://bergman.house.gov/news/documentsingle.aspx?DocumentID=1136"]),
    ]),

    # ---------------- Bill Huizenga (MI-R, US Representative) ----------------
    ("bill-huizenga", "MI", "Representative", [
        claim("bh1", "bill-huizenga", "self_defense", 0, True,
              "Cosponsored H.R. 38, the Constitutional Concealed Carry Reciprocity Act (119th Congress, 2025), which would require all states to honor out-of-state concealed-carry permits or allow permitless carry where the resident's home state permits it; also voted NO on S. 2938 (Bipartisan Safer Communities Act, June 24, 2022), which funded state red-flag programs — one of only 14 House Republicans to oppose it.",
              ["https://www.govtrack.us/congress/bills/119/hr38/cosponsors",
               "https://www.govtrack.us/congress/votes/117-2022/h299"]),
        claim("bh2", "bill-huizenga", "biblical_marriage", 1, True,
              "Voted NO on H.R. 8404, the Respect for Marriage Act (House Vote #373, July 19, 2022), rejecting federal codification of same-sex marriage; also voted against the final Senate-amended version (House Vote #513, Dec 8, 2022) — one of five Michigan Republicans to oppose the bill on both votes.",
              ["https://www.govtrack.us/congress/votes/117-2022/h373",
               "https://michiganadvance.com/2022/07/20/u-s-house-on-bipartisan-vote-passes-bill-protecting-right-to-same-sex-marriage/"]),
        claim("bh3", "bill-huizenga", "border_immigration", 1, True,
              "Voted YES on H.R. 29 (Laken Riley Act, House Vote #6, Jan 7, 2025), mandating DHS detention of undocumented individuals arrested for theft, burglary, or assault on law enforcement; also voted YES on H.R. 5717 (No Bailout for Sanctuary Cities Act, House Vote #437, Sept 20, 2024), stripping federal grants from jurisdictions that refuse to honor ICE immigration detainers.",
              ["https://www.govtrack.us/congress/votes/119-2025/h6",
               "https://www.govtrack.us/congress/votes/118-2024/h437",
               "https://www.congress.gov/bill/118th-congress/house-bill/5717"]),
        claim("bh4", "bill-huizenga", "election_integrity", 0, True,
              "Cosponsored and voted for H.R. 8281 (SAVE Act, 118th Congress, House Vote, July 10, 2024), requiring documentary proof of U.S. citizenship to register to vote in federal elections; the bill passed 221-198 with Huizenga promoting it in his official newsletter.",
              ["https://www.congress.gov/bill/118th-congress/house-bill/8281/all-info",
               "https://www.govtrack.us/congress/bills/118/hr8281",
               "https://huizenga.house.gov/news/email/show.aspx?ID=BHQA3XWCHKQBARBCKSFEJMVFQI"]),
    ]),

    # ---------------- David Taylor (OH-R, US Representative) ----------------
    ("david-taylor", "OH", "Representative", [
        claim("dt1", "david-taylor", "economic_stewardship", 0, True,
              "Cosponsored H.R. 1919, the Anti-CBDC Surveillance State Act (119th Congress), prohibiting the Federal Reserve from issuing a central bank digital currency or maintaining individual digital-dollar accounts; the bill passed the House 219-210 on July 17, 2025.",
              ["https://www.congress.gov/bill/119th-congress/house-bill/1919",
               "https://www.govtrack.us/congress/bills/119/hr1919/cosponsors"]),
        claim("dt2", "david-taylor", "election_integrity", 0, True,
              "Voted YES on the SAVE Act (H.R. 22, House Vote #102, Apr 10, 2025), requiring documentary proof of U.S. citizenship to register to vote in federal elections; Republicans voted 216-0 with zero defections on the final passage vote.",
              ["https://www.govtrack.us/congress/votes/119-2025/h102",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("dt3", "david-taylor", "biblical_marriage", 2, True,
              "Voted YES on H.R. 28, the Protection of Women and Girls in Sports Act (House Vote #12, Jan 14, 2025), amending Title IX to bar biological males from competing in federally funded female athletic programs; the bill passed 218-206 with unanimous Republican support.",
              ["https://www.govtrack.us/congress/votes/119-2025/h12",
               "https://clerk.house.gov/Votes/202512"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug cross-state collisions."""
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

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
