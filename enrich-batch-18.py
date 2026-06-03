#!/usr/bin/env python3
"""Enrichment batch 18: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators from the bottom of the alphabet (MA, IN,
ID, ID, IL) that had 0 evidence claims. Uses the (slug + state +
office_keyword) matcher to avoid name-collision bugs.

Mix (3 R / 2 D): Jim Banks (IN-R), Mike Crapo (ID-R), Jim Risch (ID-R),
Tammy Duckworth (IL-D), Edward Markey (MA-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

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
    # ---------------- Jim Banks (IN-R, US Senator) ----------------
    ("jim-banks", "IN", "Senator", [
        claim("jb1", "jim-banks", "sanctity_of_life", 0, True,
              "Elected to the U.S. Senate in November 2024 with an SBA Pro-Life America endorsement and a House pro-life record spanning 2017–2024, including sponsoring the Patients First Act (H.R.64) and co-sponsoring the Dignity for Aborted Children Act; pledged during his Senate campaign to defund Planned Parenthood and stated 'there is more that federal and state lawmakers must do to protect life' after Dobbs — affirming a life-from-conception standard.",
              ["https://sbaprolife.org/representative/jim-banks",
               "https://en.wikipedia.org/wiki/Jim_Banks"]),
        claim("jb2", "jim-banks", "border_immigration", 0, True,
              "Introduced the Border Security is National Security Act (S.301) on January 29, 2025 — one of his first acts as a new U.S. Senator — directing military personnel and resources to enforce the southern border, consistent with the wall-and-military enforcement posture the rubric calls for.",
              ["https://www.congress.gov/member/jim-banks/B001299",
               "https://en.wikipedia.org/wiki/Jim_Banks"]),
        claim("jb3", "jim-banks", "self_defense", 1, True,
              "Carries an NRA-endorsed, pro-Second Amendment record from his House tenure (2017–2024), having opposed red-flag law incentives, background-check expansions, and assault-weapons restrictions; voted against the Bipartisan Safer Communities Act (June 2022), which funded state red-flag programs.",
              ["https://en.wikipedia.org/wiki/Jim_Banks",
               "https://ballotpedia.org/Jim_Banks_(Indiana)"]),
    ]),

    # ---------------- Mike Crapo (ID-R, US Senator) ----------------
    ("mike-crapo", "ID", "Senator", [
        claim("mc1", "mike-crapo", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (Senate Vote #362, November 29, 2022), which federally codified same-sex marriage. Crapo was not among the 12 Republicans who joined Democrats in passing the bill 61–36; his no vote reflects the one-man-one-woman definition of marriage the rubric upholds.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://en.wikipedia.org/wiki/Mike_Crapo"]),
        claim("mc2", "mike-crapo", "sanctity_of_life", 0, True,
              "A consistent pro-life senator who praised the Supreme Court's June 2022 Dobbs ruling overturning Roe v. Wade and has voted to protect the unborn throughout his Senate tenure; backed by National Right to Life and SBA Pro-Life America.",
              ["https://en.wikipedia.org/wiki/Mike_Crapo",
               "https://ballotpedia.org/Mike_Crapo"]),
        claim("mc3", "mike-crapo", "economic_stewardship", 2, True,
              "Voted against both the $1.9 trillion American Rescue Plan Act (2021) and the $737 billion Inflation Reduction Act (2022), citing deficit expansion concerns; as chair of the Senate Finance Committee he has repeatedly demanded offsets and spending discipline, opposing unlimted federal outlays that deepen the national debt.",
              ["https://en.wikipedia.org/wiki/Mike_Crapo",
               "https://www.govtrack.us/congress/members/michael_crapo/300030"]),
    ]),

    # ---------------- Jim Risch (ID-R, US Senator) ----------------
    ("jim-risch", "ID", "Senator", [
        claim("jr1", "jim-risch", "sanctity_of_life", 0, True,
              "States publicly: 'I am strongly pro-life and always have been.' In February 2024 led a bicameral amicus brief to the U.S. Supreme Court defending Idaho's Defense of Life Act, and holds an A-rated record with SBA Pro-Life America spanning his full Senate tenure.",
              ["https://sbaprolife.org/senator/jim-risch",
               "https://www.risch.senate.gov/public/index.cfm/2024/2/risch-fulcher-lead-bicameral-amicus-supporting-idaho-s-pro-life-scotus-case"]),
        claim("jr2", "jim-risch", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (Senate Vote #362, November 29, 2022); his official website affirms his Family Values positions against federally imposed redefinitions of marriage. He was not among the 12 Republicans who crossed over to pass the bill.",
              ["https://www.govtrack.us/congress/votes/117-2022/s362",
               "https://www.risch.senate.gov/public/index.cfm/familyvalues"]),
        claim("jr3", "jim-risch", "foreign_policy_restraint", 0, True,
              "As Chairman of the Senate Foreign Relations Committee, Risch has stated the constitutional debate over war-making authority 'has been going on since George Washington was president — this is a democracy and this is how it should work,' signaling that Congress, not the executive alone, must authorize military action under Article I.",
              ["https://en.wikipedia.org/wiki/Jim_Risch",
               "https://www.risch.senate.gov/public/index.cfm/defense"]),
    ]),

    # ---------------- Tammy Duckworth (IL-D, US Senator) ----------------
    ("tammy-duckworth", "IL", "Senator", [
        claim("td1", "tammy-duckworth", "sanctity_of_life", 0, False,
              "Called the Supreme Court's Dobbs decision 'outraged and horrified' her and a 'nightmare'; cosponsored the Women's Health Protection Act of 2025 to restore nationwide abortion access and has repeatedly voted against any restrictions on abortion — rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/Tammy_Duckworth",
               "https://ballotpedia.org/Tammy_Duckworth"]),
        claim("td2", "tammy-duckworth", "self_defense", 1, False,
              "A prominent gun-control advocate who joined the 2016 Senate filibuster demanding floor votes on firearm restrictions and was endorsed by the Brady Campaign to Prevent Gun Violence; supports assault-weapons restrictions and universal background check expansion — earning a failing grade from the NRA and directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Tammy_Duckworth",
               "https://ballotpedia.org/Tammy_Duckworth"]),
        claim("td3", "tammy-duckworth", "border_immigration", 2, False,
              "Supports comprehensive immigration reform that includes a pathway to citizenship for those in the country unlawfully and backs DACA protections — positions incompatible with the rubric's anti-sanctuary standard demanding enforcement and deportation over legalization.",
              ["https://en.wikipedia.org/wiki/Tammy_Duckworth",
               "https://ballotpedia.org/Tammy_Duckworth"]),
    ]),

    # ---------------- Edward Markey (MA-D, US Senator) ----------------
    ("edward-markey", "MA", "Senator", [
        claim("em1", "edward-markey", "sanctity_of_life", 4, False,
              "A decades-long opponent of any restrictions on abortion who joined the entire Senate Democratic caucus in cosponsoring the Women's Health Protection Act of 2025 to restore nationwide abortion access, and has consistently opposed Congressional bills that would defund Planned Parenthood — placing him squarely inside the abortion-industry funding network the rubric prohibits.",
              ["https://www.markey.senate.gov/news/press-releases/on-3rd-anniversary-of-roe-being-overturned-markey-joins-senate-dems-in-a-bill-to-restore-abortion-access-nationwide",
               "https://en.wikipedia.org/wiki/Ed_Markey"]),
        claim("em2", "edward-markey", "economic_stewardship", 2, False,
              "Lead Senate sponsor of the Green New Deal resolution (S.Res.59) — a proposal to mandate net-zero emissions within ten years through trillions in new federal spending with no credible offset mechanism — the antithesis of the balanced-budget / anti-deficit posture the rubric requires.",
              ["https://www.markey.senate.gov/view/sen-markey-and-rep-ocasio-cortez-announce-green-new-deal-resolution",
               "https://en.wikipedia.org/wiki/Ed_Markey"]),
        claim("em3", "edward-markey", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (December 2022), federally codifying same-sex marriage by requiring all states to recognize it, and has publicly pushed to keep anti-LGBTQ provisions out of federal funding bills — rejecting the one-man-one-woman definition the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Respect_for_Marriage_Act",
               "https://en.wikipedia.org/wiki/Ed_Markey"]),
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
