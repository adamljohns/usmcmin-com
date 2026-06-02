#!/usr/bin/env python3
"""Enrichment batch 4: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators that had 0 evidence claims. Uses the
(slug + state + office_keyword) matcher from batches 2-3 to avoid the
batch-1 Mike Lee name-collision bug.

Mix (3 R / 2 D): Mark Kelly (AZ-D), Roger Marshall (KS-R),
Cory Booker (NJ-D), Ron Johnson (WI-R), Cynthia Lummis (WY-R).
Each claim cites >=1 reliable source and reflects 2024-2026 voting
record / public positions.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. build-data.py only re-minifies the
master when meta changes; since meta is already current today, the enrich
step must preserve minification itself.
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
    # ---------------- Mark Kelly (AZ-D, US Senator) ----------------
    ("mark-kelly", "AZ", "Senator", [
        claim("mk1", "mark-kelly", "self_defense", 1, False,
              "A leading gun-control advocate who, with his wife Gabby Giffords, founded the Giffords gun-control organization. Backs an assault-weapons ban, universal background checks, waiting periods, and red-flag laws, and in 2024-2025 reintroduced the GOSAFE Act to restrict gas-operated semi-automatic rifles — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://en.wikipedia.org/wiki/Mark_Kelly",
               "https://www.kelly.senate.gov/newsroom/press-releases/kelly-introduces-legislation-to-save-lives-protect-communities-from-gun-violence/"]),
        claim("mk2", "mark-kelly", "sanctity_of_life", 4, False,
              "Endorsed by Planned Parenthood and carries a 2024 score of 100 from Reproductive Freedom for All (successor to NARAL), placing him squarely inside the abortion-industry endorsement-and-funding network.",
              ["https://reproductivefreedomforall.org/lawmaker/mark-kelly/",
               "https://en.wikipedia.org/wiki/Mark_Kelly"]),
        claim("mk3", "mark-kelly", "sanctity_of_life", 0, False,
              "Identifies as pro-choice, supports codifying Roe v. Wade into federal law, and has said late-term abortions should remain legally protected — rejecting any recognition of personhood from conception.",
              ["https://en.wikipedia.org/wiki/Mark_Kelly"]),
    ]),

    # ---------------- Roger Marshall (KS-R, US Senator) ----------------
    ("roger-marshall", "KS", "Senator", [
        claim("rm1", "roger-marshall", "sanctity_of_life", 0, True,
              "An obstetrician who delivered thousands of babies before the Senate; holds an A+ rating from SBA Pro-Life America and a 100% pro-life voting record. His first bill as a U.S. Senator was legislation to protect the lives of the unborn, and he affirms life from conception.",
              ["https://sbaprolife.org/senator/roger-marshall",
               "https://www.marshall.senate.gov/newsroom/press-releases/dr-marshalls-first-bill-as-u-s-senator-protects-life-of-the-unborn/"]),
        claim("rm2", "roger-marshall", "border_immigration", 0, True,
              "A border-security hawk who cosponsored the Secure the Border Act of 2023 (which funds border-wall construction and tightens asylum) and voted against the 2024 bipartisan border deal as too weak, demanding hard enforcement and safe-third-country asylum bars.",
              ["https://www.marshall.senate.gov/newsroom/press-releases/sen-marshall-supports-secure-the-border-act/",
               "https://www.marshall.senate.gov/newsroom/press-releases/senator-marshall-votes-against-democrats-border-bailout/"]),
        claim("rm3", "roger-marshall", "self_defense", 1, True,
              "Holds an A+ rating from the National Rifle Association and a consistent pro-gun record, opposing new firearm restrictions such as bans and registries.",
              ["https://en.wikipedia.org/wiki/Roger_Marshall",
               "https://www.ontheissues.org/house/Roger_Marshall_Gun_Control.htm"]),
    ]),

    # ---------------- Cory Booker (NJ-D, US Senator) ----------------
    ("cory-booker", "NJ", "Senator", [
        claim("cb1", "cory-booker", "biblical_marriage", 0, False,
              "A vocal champion of same-sex marriage who voted for the Respect for Marriage Act (2022) codifying federal recognition of same-sex unions, and who as Newark mayor and senator repeatedly attacked civil-union-only frameworks as discriminatory — rejecting the one-man-one-woman definition.",
              ["https://www.booker.senate.gov/news/press/booker-applauds-passage-of-respect-for-marriage-act",
               "https://en.wikipedia.org/wiki/Political_positions_of_Cory_Booker"]),
        claim("cb2", "cory-booker", "biblical_marriage", 4, False,
              "A leading Senate advocate for the Equality Act, which would write sexual-orientation and gender-identity protections into federal civil-rights law and extend them into schools and public accommodations — the policy promotion of LGBTQ ideology the rubric opposes.",
              ["https://www.booker.senate.gov/news/videos/watch/senator-cory-booker-speaks-about-the-equality-act",
               "https://en.wikipedia.org/wiki/Political_positions_of_Cory_Booker"]),
        claim("cb3", "cory-booker", "sanctity_of_life", 0, False,
              "Supports abortion rights and cosponsored Senate legislation to roll back state limits on abortion access (the Women's Health Protection Act), rejecting any personhood-from-conception standard.",
              ["https://www.pbs.org/newshour/politics/what-does-cory-booker-believe-where-the-candidate-stands-on-7-issues",
               "https://en.wikipedia.org/wiki/Political_positions_of_Cory_Booker"]),
    ]),

    # ---------------- Ron Johnson (WI-R, US Senator) ----------------
    ("ron-johnson", "WI", "Senator", [
        claim("rj1", "ron-johnson", "foreign_policy_restraint", 1, True,
              "Voted against the February 2024 $95B Ukraine/Israel foreign-aid package and has repeatedly opposed open-ended Ukraine funding, arguing the war is not winnable and U.S. money should not flow indefinitely — aligning with the rubric's call to wind down foreign military entanglements.",
              ["https://thebadgerproject.org/2024/02/14/ron-johnson-votes-against-aid-package-for-ukraine-and-israel-tammy-baldwin-joins-most-dems-22-repubs-to-approve-it/",
               "https://en.wikipedia.org/wiki/Ron_Johnson"]),
        claim("rj2", "ron-johnson", "industry_capture", 0, True,
              "A persistent critic of COVID-era pharmaceutical and public-health mandates: convened Senate roundtables on vaccine injuries and demanded a vote to end the military's COVID-19 vaccine mandate, challenging the pharma-government consensus the rubric warns against.",
              ["https://www.ronjohnson.senate.gov/covid",
               "https://en.wikipedia.org/wiki/Ron_Johnson"]),
        claim("rj3", "ron-johnson", "economic_stewardship", 2, True,
              "A longtime fiscal hawk who has stalled or voted against large unoffset spending bills from both parties and seeks a balanced budget, objecting to multi-trillion-dollar packages 'no one has had time to read.'",
              ["https://en.wikipedia.org/wiki/Ron_Johnson"]),
    ]),

    # ---------------- Cynthia Lummis (WY-R, US Senator) ----------------
    ("cynthia-lummis", "WY", "Senator", [
        claim("cl1", "cynthia-lummis", "economic_stewardship", 0, True,
              "Has called a U.S. central bank digital currency 'unnecessary' and frames Bitcoin as the decentralized 'anti-CBDC,' opposing a surveillance-capable government digital dollar — directly matching the rubric's opposition to a CBDC.",
              ["https://www.coindesk.com/video/sen-cynthia-lummis-says-cbdcs-are-unnecessary-in-the-us",
               "https://www.nasdaq.com/articles/cynthia-lummis:-bitcoin-is-the-anti-cbdc"]),
        claim("cl2", "cynthia-lummis", "economic_stewardship", 1, True,
              "Author of the BITCOIN Act to establish a U.S. Strategic Bitcoin Reserve as a hard-money store of value hedging against fiat debasement — a sound-money posture consistent with the rubric's preference for currency outside discretionary central-bank control.",
              ["https://www.lummis.senate.gov/press-releases/lummis-introduces-strategic-bitcoin-reserve-legislation/",
               "https://www.congress.gov/bill/118th-congress/senate-bill/4912"]),
        claim("cl3", "cynthia-lummis", "sanctity_of_life", 0, True,
              "Holds an A+/100% pro-life record (National Right to Life) and helped pass the one-year Medicaid defunding of Planned Parenthood in the 2025 reconciliation bill (H.R.1); affirms protection of the unborn from conception.",
              ["https://sbaprolife.org/senator/cynthia-lummis",
               "https://en.wikipedia.org/wiki/Cynthia_Lummis"]),
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
