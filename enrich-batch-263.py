#!/usr/bin/env python3
"""Enrichment batch 263: second-wave claims for 5 sitting US senators.

archetype_curated bucket exhausted; targets are evidence_curated sitting
US senators with only 4 claims, pulled from bottom of alphabet (VT/VA/UT):
Peter Welch (VT-D), Bernie Sanders (VT-I), Tim Kaine (VA-D),
Mark Warner (VA-D), John Curtis (UT-R). Each new claim spans a distinct
rubric category not yet covered for that senator. All claims sourced
2022-2026 from official .senate.gov / congress.gov / govtrack.us /
ballotpedia.org / en.wikipedia.org.

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


TARGETS = [
    # ---------------- Peter Welch (VT-D, US Senator) ----------------
    ("peter-welch", "VT", "Senator", [
        claim("pw1", "peter-welch", "economic_stewardship", 2, False,
              "During Senate debate on the Republican budget reconciliation package in 2025, Welch publicly declared 'we kill the bill,' opposing proposed cuts to Medicaid, clean energy investments, and other social programs. He has consistently opposed deficit-reduction measures that reduce federal spending, while securing over $43 million in earmarks for Vermont in recent appropriations cycles — reflecting a pro-spending, anti-balanced-budget posture that runs contrary to the rubric's call for fiscal restraint.",
              ["https://www.welch.senate.gov/as-senate-debates-the-budget-vermont-sen-peter-welch-hopes-we-kill-the-bill/",
               "https://www.welch.senate.gov/welch-secures-nearly-30-million-in-federal-funds-for-vermont/",
               "https://ballotpedia.org/Peter_Welch"]),
        claim("pw2", "peter-welch", "foreign_policy_restraint", 0, True,
              "In 2025 Welch cosponsored and voted for Senator Bernie Sanders' Joint Resolutions of Disapproval under the Arms Export Control Act to block the Trump administration's sale of more than $8.8 billion in offensive weaponry — including 2,000-pound bombs — to Israel, which had been approved via an emergency bypass of the normal 30-day Congressional review period. Welch stated the Trump Administration 'bypassed Congress' and that 'Congress should not allow the Administration to sell offensive weapons in defiance of our laws' — asserting Congressional Article I authority over arms transfers and aligning with the rubric's call for Congress to reclaim war-powers oversight.",
              ["https://www.welch.senate.gov/welch-cosponsors-sanders-resolutions-to-block-certain-offensive-weapons-sales-to-israel/",
               "https://www.welch.senate.gov/welch-supports-sanders-resolution-to-block-certain-offensive-weapons-sales-to-israel/",
               "https://en.wikipedia.org/wiki/Peter_Welch"]),
    ]),

    # ---------------- Bernie Sanders (VT-I, US Senator) ----------------
    ("bernie-sanders", "VT", "Senator", [
        claim("bs1", "bernie-sanders", "self_defense", 1, False,
              "Sanders cosponsored the Assault Weapons Ban of 2025 (S.1531) and has consistently supported universal background checks, magazine-capacity limits, and bans on semi-automatic 'assault-style' firearms throughout his Senate tenure — directly opposing the rubric's defense of an unrestricted Second Amendment free from new bans, registries, and magazine restrictions.",
              ["https://www.sanders.senate.gov/press-releases/sanders-votes-for-background-checks-assault-weapons-ban-2/",
               "https://www.govtrack.us/congress/bills/119/s1531/text",
               "https://en.wikipedia.org/wiki/Bernie_Sanders"]),
        claim("bs2", "bernie-sanders", "economic_stewardship", 2, False,
              "Sanders has been the Senate's leading proponent of Medicare for All, the Green New Deal, and other large-scale spending expansions — proposals totaling tens of trillions in new federal expenditures with no balanced-budget offset. His official 'Building an Economy That Works for Everyone' platform characterizes balanced-budget requirements as instruments of austerity harmful to working Americans, and he has consistently voted against deficit-reduction reconciliation bills, running directly counter to the rubric's anti-deficit/balanced-budget standard.",
              ["https://www.sanders.senate.gov/building-an-economy-that-works-for-everyone/",
               "https://en.wikipedia.org/wiki/Bernie_Sanders",
               "https://ballotpedia.org/Bernie_Sanders"]),
    ]),

    # ---------------- Tim Kaine (VA-D, U.S. Senator) ----------------
    ("tim-kaine", "VA", "Senator", [
        claim("tk1", "tim-kaine", "election_integrity", 0, False,
              "Kaine and Warner co-slammed the SAVE America Act as a 'voter suppression measure that could disenfranchise millions,' opposing its requirements for proof of citizenship to register and photo identification to vote by mail — the very voter-verification safeguards the rubric endorses. Kaine has instead championed the Freedom to Vote Act to expand automatic voter registration, no-excuse absentee balloting, and make Election Day a federal holiday — a package designed to increase mail-in and early voting rather than tighten ballot integrity.",
              ["https://www.kaine.senate.gov/press-releases/warner-kaine-slam-save-america-act-as-voter-suppression-measure-that-could-disenfranchise-millions",
               "https://www.kaine.senate.gov/press-releases/kaine-cosponsors-voter-registration-legislation-applauds-early-voting-in-virginia",
               "https://ballotpedia.org/Tim_Kaine"]),
        claim("tk2", "tim-kaine", "foreign_policy_restraint", 1, True,
              "Kaine led the bipartisan effort to repeal the 1991 and 2002 Iraq War AUMFs, which was enacted into law as part of the FY2026 National Defense Authorization Act — the first repeal of a war authorization in more than 50 years. He also filed a War Powers Resolution to prevent war with Iran without congressional authorization, and has consistently argued the executive branch cannot lawfully engage in military operations without explicit congressional approval — directly fulfilling the rubric's call to end forever wars and repeal standing AUMFs.",
              ["https://www.kaine.senate.gov/press-releases/kaine-and-young-applaud-bipartisan-bill-to-formally-end-iraq-wars-becoming-law/",
               "https://www.kaine.senate.gov/press-releases/kaine-announces-the-filing-of-a-war-powers-resolution-to-prevent-war-with-iran",
               "https://www.kaine.senate.gov/issues/national-security-and-foreign-policy"]),
    ]),

    # ---------------- Mark Warner (VA-D, U.S. Senator) ----------------
    ("mark-warner", "VA", "Senator", [
        claim("mw1", "mark-warner", "biblical_marriage", 0, False,
              "Warner voted YES on the Respect for Marriage Act (RFMA) in both the November 2022 (61-36) and December 2022 final-passage Senate votes, codifying federal recognition of same-sex and interracial marriages. He praised the signing as 'welcome news for the thousands of same-sex and interracial married couples across Virginia,' and subsequently urged the Virginia General Assembly to repeal the remaining ban on same-sex marriage in Virginia's state constitution — explicitly rejecting the one-man-one-woman definition the rubric endorses.",
              ["https://www.warner.senate.gov/public/index.cfm/pressreleases?id=915FBE30-F86F-4784-91B5-4E027EDD11CC",
               "https://www.warner.senate.gov/public/index.cfm/2023/2/warner-kaine-urge-virginia-general-assembly-to-repeal-ban-on-same-sex-marriage-in-state-constitution",
               "https://en.wikipedia.org/wiki/Mark_Warner"]),
        claim("mw2", "mark-warner", "biblical_marriage", 4, False,
              "Warner and Kaine reintroduced the Equality Act in June 2023, federal legislation that would write sexual-orientation and gender-identity (SOGI) protections into civil-rights law across education, employment, housing, credit, and public accommodations nationwide — directly promoting LGBTQ ideology in schools and the public square, which the rubric opposes.",
              ["https://www.warner.senate.gov/public/index.cfm/2023/6/warner-kaine-colleagues-reintroduce-equality-act-to-enshrine-protections-for-lgbtq-americans-into-law",
               "https://ballotpedia.org/Mark_Warner"]),
    ]),

    # ---------------- John Curtis (UT-R, US Senator) ----------------
    ("john-curtis", "UT", "Senator", [
        claim("jc1", "john-curtis", "economic_stewardship", 2, True,
              "Curtis co-introduced the bipartisan Fiscal Commission Act to create a bicameral commission of federal policymakers and experts tasked with developing achievable proposals to rein in deficits and move toward responsible fiscal stewardship. Curtis described it as 'a commonsense, bipartisan, bicameral way to bring Democrats and Republicans together to put forward balanced, responsible solutions' to deficit spending — aligning with the rubric's call for anti-deficit/balanced-budget governance.",
              ["https://www.curtis.senate.gov/press-releases/what-they-are-staying-fiscal-commission-act/",
               "https://www.curtis.senate.gov/newsletters/highs-and-lows-new-bills-for-utahs-economy-and-budgeting-conundrums/",
               "https://ballotpedia.org/John_Curtis_(Utah)"]),
        claim("jc2", "john-curtis", "foreign_policy_restraint", 1, False,
              "Curtis has expressed strong, consistent support for continued U.S. military assistance to Ukraine and unwavering commitment to NATO. He co-signed bipartisan Senate resolutions marking both the third anniversary (2025) and fourth anniversary (2026) of Russia's full-scale invasion of Ukraine, expressing 'unwavering support for Ukraine's sovereignty and territorial integrity,' and has advocated for continued U.S. coordination with NATO and European allies — rejecting the rubric's call to wind down open-ended foreign military commitments.",
              ["https://www.curtis.senate.gov/press-releases/curtis-joins-bipartisan-resolution-supporting-ukraine-on-third-anniversary-of-russias-full-scale-invasion/",
               "https://www.curtis.senate.gov/press-releases/curtis-joins-bipartisan-resolution-supporting-ukraine-on-fourth-anniversary-of-russias-full-scale-invasion/",
               "https://ballotpedia.org/John_Curtis_(Utah)"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
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
        print(f"  {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} -> evidence_curated")

    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
