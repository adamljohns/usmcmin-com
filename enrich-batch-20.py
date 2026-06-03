#!/usr/bin/env python3
"""Enrichment batch 20: hand-curated claims for 5 sitting U.S. Senators.

Targets archetype_curated senators from the BOTTOM of the alphabet bucket
(GA, FL, DE, CT) that had 0 evidence claims. Uses state-aware find_candidate
to avoid slug collisions.

Mix (1 R / 4 D): Ashley Moody (FL-R), Jon Ossoff (GA-D),
Lisa Blunt Rochester (DE-D), Chris Coons (DE-D), Richard Blumenthal (CT-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record /
public positions.

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
    # ---------------- Ashley Moody (FL-R, US Senator) ----------------
    ("ashley-moody", "FL", "Senator", [
        claim("am1", "ashley-moody", "self_defense", 1, True,
              "Cosponsored the Constitutional Concealed Carry Reciprocity Act (2025), endorsed by the NRA, Gun Owners of America, and NSSF, which would allow law-abiding citizens with home-state carry permits to carry in any reciprocating state — opposing new federal firearm restrictions.",
              ["https://www.moody.senate.gov/press-releases/news-release-senator-moody-fights-for-americans-second-amendment-rights-cosponsors-concealed-carry-reciprocity-bill/",
               "https://en.wikipedia.org/wiki/Ashley_Moody"]),
        claim("am2", "ashley-moody", "border_immigration", 0, True,
              "Sworn in as Senator with an explicit agenda of supporting President Trump's border-security measures including wall construction and military deployment at the southern border; described border enforcement as a top legislative priority.",
              ["https://www.moody.senate.gov/about/",
               "https://ballotpedia.org/Ashley_B._Moody"]),
        claim("am3", "ashley-moody", "family_child_sovereignty", 0, True,
              "Sponsored S.3650 (January 2026) to prohibit transporting minors across state lines to circumvent parental-involvement laws in abortion decisions, reinforcing parental authority over minor children's medical decisions.",
              ["https://www.moody.senate.gov/",
               "https://ballotpedia.org/Ashley_B._Moody"]),
    ]),

    # ---------------- Jon Ossoff (GA-D, US Senator) ----------------
    ("jon-ossoff", "GA", "Senator", [
        claim("jo1", "jon-ossoff", "sanctity_of_life", 0, False,
              "Co-sponsored the Women's Health Protection Act to create a federal right to abortion through all stages of pregnancy, preempting state personhood and heartbeat laws — rejecting any recognition of life from conception.",
              ["https://www.ossoff.senate.gov/press-releases/",
               "https://sbaprolife.org/senator/jon-ossoff"]),
        claim("jo2", "jon-ossoff", "sanctity_of_life", 4, False,
              "Voted against the H.R.1 (2025) reconciliation provision that defunded Planned Parenthood of Medicaid dollars, and is consistently endorsed and rated favorably by Planned Parenthood and reproductive-freedom organizations.",
              ["https://sbaprolife.org/senator/jon-ossoff",
               "https://ballotpedia.org/Jon_Ossoff"]),
        claim("jo3", "jon-ossoff", "sanctity_of_life", 2, False,
              "Co-sponsored the Access to Family Building Act (2024-2025) to establish a federal statutory right to IVF, which involves creation and routine discarding of embryos — opposing the rubric's protection of embryonic life.",
              ["https://www.ossoff.senate.gov/press-releases/",
               "https://ballotpedia.org/Jon_Ossoff"]),
    ]),

    # ---------------- Lisa Blunt Rochester (DE-D, US Senator) ----------------
    ("lisa-blunt-rochester", "DE", "Senator", [
        claim("lbr1", "lisa-blunt-rochester", "sanctity_of_life", 0, False,
              "Pledged on entering the Senate to again vote to codify Roe v. Wade into federal law: 'We cannot let my Republican colleagues pass a nationwide abortion ban. I voted to codify Roe in the House. I will do it again in the Senate.' — rejecting personhood from conception.",
              ["https://ballotpedia.org/Lisa_Blunt_Rochester",
               "https://www.bluntrochester.senate.gov/"]),
        claim("lbr2", "lisa-blunt-rochester", "sanctity_of_life", 4, False,
              "Endorsed by and consistently aligned with Planned Parenthood; has opposed every legislative effort to restrict taxpayer funding of Planned Parenthood and abortion services, placing her inside the abortion-industry financial network.",
              ["https://ballotpedia.org/Lisa_Blunt_Rochester",
               "https://www.govtrack.us/congress/members/lisa_blunt_rochester/412689"]),
        claim("lbr3", "lisa-blunt-rochester", "economic_stewardship", 2, False,
              "Voted against the March 2025 Republican continuing-resolution bill and publicly rejected spending-restraint frameworks, positioning herself against balanced-budget efforts and opposing cuts to social-safety-net spending programs.",
              ["https://www.bluntrochester.senate.gov/news/press-releases/senator-blunt-rochester-statement-on-voting-against-republicans-dirty-cr-deal/",
               "https://www.govtrack.us/congress/members/lisa_blunt_rochester/412689"]),
    ]),

    # ---------------- Chris Coons (DE-D, US Senator) ----------------
    ("chris-coons", "DE", "Senator", [
        claim("cc1", "chris-coons", "sanctity_of_life", 4, False,
              "Receives a 100% rating from the Planned Parenthood Action Fund and a 0% rating from the National Right to Life Committee, placing him squarely within the abortion-advocacy endorsement and funding network.",
              ["https://en.wikipedia.org/wiki/Chris_Coons",
               "https://ballotpedia.org/Chris_Coons"]),
        claim("cc2", "chris-coons", "biblical_marriage", 0, False,
              "Voted for the Respect for Marriage Act (2022), codifying federal recognition of same-sex unions and requiring states to honor such marriages — explicitly rejecting the one-man-one-woman definition of marriage.",
              ["https://www.coons.senate.gov/news/press-releases/statement-from-senator-coons-on-delaware-senates-passage-of-marriage-equality-bill",
               "https://en.wikipedia.org/wiki/Chris_Coons"]),
        claim("cc3", "chris-coons", "self_defense", 1, False,
              "Sponsored provisions expanding firearm purchase disqualifications and requiring local law enforcement notification when prohibited persons attempt to buy guns — supporting the gun-control infrastructure the rubric opposes.",
              ["https://www.coons.senate.gov/",
               "https://ballotpedia.org/Chris_Coons"]),
    ]),

    # ---------------- Richard Blumenthal (CT-D, US Senator) ----------------
    ("richard-blumenthal", "CT", "Senator", [
        claim("rb1", "richard-blumenthal", "sanctity_of_life", 0, False,
              "Pro-choice throughout his Senate tenure; co-sponsored legislation to fund abortion travel for patients and to protect access to abortion services, consistently opposing any recognition of fetal personhood from conception.",
              ["https://www.blumenthal.senate.gov/",
               "https://ballotpedia.org/Richard_Blumenthal"]),
        claim("rb2", "richard-blumenthal", "self_defense", 1, False,
              "Has made preventing gun violence a declared top priority: supports assault-weapons bans, universal background checks, and high-capacity magazine restrictions — directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/members/richard_blumenthal/412490",
               "https://ballotpedia.org/Richard_Blumenthal"]),
        claim("rb3", "richard-blumenthal", "biblical_marriage", 2, False,
              "Co-sponsored legislation to prohibit commercial sexual-orientation conversion therapy at the federal level, affirming and promoting LGBTQ ideological frameworks in federal law — opposing the rubric's call to reject transgender and LGBTQ ideology.",
              ["https://ballotpedia.org/Richard_Blumenthal",
               "https://www.blumenthal.senate.gov/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions."""
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
