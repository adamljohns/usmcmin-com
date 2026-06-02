#!/usr/bin/env python3
"""Enrichment batch 7: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims.  Uses the
(slug + state + office_keyword) matcher from prior batches to avoid slug
collisions.

Mix (5 R): Ted Cruz (TX-R), John Cornyn (TX-R), Bill Hagerty (TN-R),
Mike Rounds (SD-R), John Thune (SD-R).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.  Targets taken from the BOTTOM of the alphabet
bucket to avoid colliding with the top-of-alphabet in-session loop.

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
    # ---------------- Ted Cruz (TX-R, US Senator) ----------------
    ("ted-cruz", "TX", "Senator", [
        claim("tc1", "ted-cruz", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America and has a 100% pro-life voting record in the Senate. Cosponsored the Life at Conception Act and has voted against every pro-abortion bill, affirming personhood from the moment of fertilization.",
              ["https://sbaprolife.org/senator/ted-cruz",
               "https://en.wikipedia.org/wiki/Political_positions_of_Ted_Cruz"]),
        claim("tc2", "ted-cruz", "self_defense", 1, True,
              "Holds an A+ rating from the NRA and has been one of the Senate's most vocal opponents of gun-control proposals: led floor opposition to the Bipartisan Safer Communities Act, co-sponsored the Respect for the Second Amendment Act (S.840, 118th Congress), and publicly called colleagues who support red-flag laws and assault-weapons bans 'squishes' on the Second Amendment.",
              ["https://en.wikipedia.org/wiki/Political_positions_of_Ted_Cruz",
               "https://www.congress.gov/bill/118th-congress/senate-bill/840/text"]),
        claim("tc3", "ted-cruz", "border_immigration", 0, True,
              "A hard-line border hawk who has introduced multiple Build the Wall bills, demanded military deployment to the southern border, and in February 2024 voted against the bipartisan border deal as far too weak — insisting on mandatory removal, physical wall completion, and an end to catch-and-release.",
              ["https://ballotpedia.org/Ted_Cruz",
               "https://en.wikipedia.org/wiki/Ted_Cruz"]),
    ]),

    # ---------------- John Cornyn (TX-R, US Senator) ----------------
    ("john-cornyn", "TX", "Senator", [
        claim("jc1", "john-cornyn", "sanctity_of_life", 0, True,
              "Carries a 100% pro-life voting record; cosponsored the Born-Alive Abortion Survivors Protection Act, which would require full medical care for infants who survive a failed abortion; and has fought to make the Hyde Amendment permanent to block taxpayer funding of abortion.",
              ["https://www.johncornyn.com/on-the-issues/",
               "https://en.wikipedia.org/wiki/John_Cornyn"]),
        claim("jc2", "john-cornyn", "self_defense", 1, False,
              "Led and shepherded the Bipartisan Safer Communities Act (signed June 2022) — the first major federal gun-control legislation in nearly 30 years — which expanded background-check waiting periods for under-21 purchasers, closed the 'boyfriend loophole,' and provided federal grants to incentivize states to enact red-flag laws. He was booed at the Republican Party of Texas convention and rebuked by the state party for his role.",
              ["https://en.wikipedia.org/wiki/Bipartisan_Safer_Communities_Act",
               "https://www.cornyn.senate.gov/bipartisan-safer-communities-act/"]),
        claim("jc3", "john-cornyn", "border_immigration", 0, True,
              "A Texas border-security advocate who has consistently backed wall funding and military resources at the southern border; authored the Stop the Cartels Act to designate major drug cartels as foreign terrorist organizations and authorize military counterdrug operations.",
              ["https://en.wikipedia.org/wiki/John_Cornyn",
               "https://www.cornyn.senate.gov/news/"]),
    ]),

    # ---------------- Bill Hagerty (TN-R, US Senator) ----------------
    ("bill-hagerty", "TN", "Senator", [
        claim("bh1", "bill-hagerty", "economic_stewardship", 0, True,
              "A leading Senate opponent of a U.S. central bank digital currency: introduced the CBDC Anti-Surveillance State Act (S.3801, 118th Congress; reintroduced as S.1124, 119th Congress) with Ted Cruz to prohibit the Federal Reserve from issuing a CBDC directly to individuals, citing the government's history of exploiting the financial system to target political and religious dissidents.",
              ["https://www.hagerty.senate.gov/press-releases/2024/02/26/hagerty-cruz-colleagues-introduce-legislation-to-ban-central-bank-digital-currencies/",
               "https://www.congress.gov/bill/119th-congress/senate-bill/1124/text"]),
        claim("bh2", "bill-hagerty", "sanctity_of_life", 0, True,
              "A consistent pro-life voter who has earned a 96% conservative score from Heritage Action for the 119th Congress; supports legislation prohibiting taxpayer funding of abortion and federal penalties for administering abortion-inducing drugs without informed consent.",
              ["https://heritageaction.com/scorecard/members/h000601",
               "https://ballotpedia.org/Bill_Hagerty"]),
        claim("bh3", "bill-hagerty", "economic_stewardship", 2, True,
              "Publicly condemned Biden's FY2025 $7-trillion budget proposal as 'fiscally irresponsible,' emphasizing that runaway deficit spending threatens the dollar's reserve-currency status and demands credible debt management from the Treasury.",
              ["https://www.hagerty.senate.gov/press-releases/2024/03/11/hagerty-statement-on-bidens-2025-budget/",
               "https://www.govtrack.us/congress/members/bill_hagerty/456798/report-card/2024"]),
    ]),

    # ---------------- Mike Rounds (SD-R, US Senator) ----------------
    ("mike-rounds", "SD", "Senator", [
        claim("mr1", "mike-rounds", "sanctity_of_life", 0, True,
              "As Governor of South Dakota, signed the Women's Health and Human Life Protection Act (2006) — a near-total abortion ban aimed at challenging Roe v. Wade — and as U.S. Senator has maintained a 100% pro-life voting record, receiving Family Research Council Action's 'True Blue' award for voting to protect babies born alive after failed abortions and to end taxpayer-funded abortion.",
              ["https://www.rounds.senate.gov/newsroom/press-releases/rounds-receives-100-percent-rating-for-pro-life-voting-record",
               "https://en.wikipedia.org/wiki/Mike_Rounds"]),
        claim("mr2", "mike-rounds", "self_defense", 1, True,
              "A consistent Second Amendment advocate who opposes new federal gun restrictions; his Senate issues page highlights his work to protect law-abiding gun owners from regulatory overreach and he supported constitutional-carry-aligned legislation in the Senate.",
              ["https://www.rounds.senate.gov/issues/second-amendment",
               "https://ballotpedia.org/Mike_Rounds"]),
        claim("mr3", "mike-rounds", "border_immigration", 0, True,
              "Supports physical barrier construction and military-level resources at the southern border; has consistently backed border-wall funding and increased personnel for border enforcement, framing border security as inseparable from national security.",
              ["https://ballotpedia.org/Mike_Rounds",
               "https://www.rounds.senate.gov/issues/list"]),
    ]),

    # ---------------- John Thune (SD-R, US Senate Majority Leader) ----------------
    ("john-thune", "SD", "Senator", [
        claim("jt1", "john-thune", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record and an A+ rating from SBA Pro-Life America. As Senate Majority Leader in January 2025, brought the Born-Alive Abortion Survivors Protection Act to the Senate floor for a vote, and authored a January 2026 op-ed ('The Pro-Life Movement Marches Forward') celebrating the first pro-life federal law in decades — a provision in the reconciliation bill defunding Planned Parenthood via Medicaid.",
              ["https://www.thune.senate.gov/public/index.cfm/protectinglife",
               "https://www.thune.senate.gov/public/index.cfm/2025/1/thune-senate-to-vote-on-born-alive-abortion-survivors-protection-act"]),
        claim("jt2", "john-thune", "border_immigration", 0, True,
              "Called illegal immigration one of the defining issues of the 2024 election; as Senate Majority Leader, scheduled the first Senate vote of the new Republican majority on border and immigration enforcement — demonstrating that wall-and-deportation-first border policy is his caucus's legislative top priority.",
              ["https://www.thune.senate.gov/public/index.cfm/solutions",
               "https://en.wikipedia.org/wiki/John_Thune"]),
        claim("jt3", "john-thune", "self_defense", 0, True,
              "A long-standing gun-rights advocate who sponsored the National Right-to-Carry Reciprocity Act, legislation to require all states to honor concealed-carry permits issued by other states — a constitutional-carry expansion principle — and voted against banning standard-capacity magazines.",
              ["https://ballotpedia.org/John_Thune",
               "https://en.wikipedia.org/wiki/John_Thune"]),
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
