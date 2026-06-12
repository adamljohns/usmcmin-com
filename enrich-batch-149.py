#!/usr/bin/env python3
"""Enrichment batch 149: 5 TN/PA sitting U.S. Representatives with 0 claims.

Targets (all office='U.S. Representative', archetype_party_default, 0 claims,
taken from the bottom of the alphabet per collision-avoidance protocol):
  David Kustoff (TN-08, R), Chuck Fleischmann (TN-03, R),
  Mike Kelly (PA-16, R), Lloyd Smucker (PA-11, R), John Joyce (PA-13, R).

Sources: sbaprolife.org, house.gov, en.wikipedia.org, ballotpedia.org.
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
    # ---------------- David Kustoff (TN-08, R) ----------------
    ("david-kustoff", "TN", "Representative", [
        claim("dk1", "david-kustoff", "sanctity_of_life", 0, True,
              "An A+ pro-life legislator (SBA Pro-Life America, four consecutive years) who publicly states 'I believe that life begins at conception and that abortion is wrong'; rated 100% by National Right to Life Committee and 9% by Planned Parenthood Action Fund — a clear personhood-from-conception record.",
              ["https://kustoff.house.gov/media/press-releases/kustoff-receives-rating-susan-b-anthony-list-s-national-pro-life-scorecard",
               "https://en.wikipedia.org/wiki/David_Kustoff"]),
        claim("dk2", "david-kustoff", "self_defense", 1, True,
              "Rated 100% by Gun Owners of America; voted against HR 1808 (Assault Weapons Ban of 2022) and against other gun-control measures brought in the 117th Congress — a consistent record of opposing semi-automatic firearm bans, magazine limits, and new restrictions on law-abiding gun owners.",
              ["https://kustoff.house.gov/media/press-releases/kustoff-votes-against-two-gun-control-bills",
               "https://en.wikipedia.org/wiki/David_Kustoff"]),
    ]),

    # ---------------- Chuck Fleischmann (TN-03, R) ----------------
    ("chuck-fleischmann", "TN", "Representative", [
        claim("cf1", "chuck-fleischmann", "sanctity_of_life", 0, True,
              "Holds a 100% pro-life voting record recognized by the National Right to Life Committee and is scored by SBA Pro-Life America; has consistently voted against taxpayer funding of abortion domestically and internationally, and against Biden-era pro-abortion executive actions.",
              ["https://sbaprolife.org/representative/chuck-fleischmann",
               "https://fleischmann.house.gov/issues/right-to-life"]),
        claim("cf2", "chuck-fleischmann", "self_defense", 1, True,
              "Voted against HR 1808 (Assault Weapons Ban of 2022) and voted to overturn the Biden administration's unconstitutional pistol-brace ban; publicly opposes any legislation that threatens Second Amendment rights and supports national concealed-carry reciprocity.",
              ["https://fleischmann.house.gov/media/press-releases/rep-fleischmann-votes-to-overturn-unconstitutional-pistol-brace-ban",
               "https://en.wikipedia.org/wiki/Chuck_Fleischmann"]),
        claim("cf3", "chuck-fleischmann", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (January 2025) mandating detention and removal of illegal aliens who commit crimes, and voted for the Secure the Border Act of 2023 to fund border-wall construction and tighten enforcement; formerly the top Republican on Homeland Security Appropriations.",
              ["https://fleischmann.house.gov/media/press-releases/fleischmann-applauds-final-passage-of-the-laken-riley-act",
               "https://fleischmann.house.gov/media/press-releases/fleischmann-votes-to-secure-the-southern-border"]),
    ]),

    # ---------------- Mike Kelly (PA-16, R) ----------------
    ("mike-kelly", "PA", "Representative", [
        claim("mk1", "mike-kelly", "sanctity_of_life", 0, True,
              "Re-introduced H.R. 175, the Heartbeat Protection Act (January 2025), which prohibits abortions once a fetal heartbeat is detected; scored by SBA Pro-Life America and has consistently voted against taxpayer-funded abortion at home and abroad across his tenure since 2011.",
              ["https://sbaprolife.org/representative/mike-kelly",
               "https://kelly.house.gov/issues/pro-life-family-values"]),
        claim("mk2", "mike-kelly", "self_defense", 1, True,
              "Describes himself as 'a strong believer in the Second Amendment of the Constitution' who opposes government infringement on the right to keep and bear arms; has maintained a consistent pro-gun voting record across his House tenure, opposing gun-control measures advanced by House Democrats.",
              ["https://kelly.house.gov/issues",
               "https://en.wikipedia.org/wiki/Mike_Kelly_(Pennsylvania_politician)"]),
    ]),

    # ---------------- Lloyd Smucker (PA-11, R) ----------------
    ("lloyd-smucker", "PA", "Representative", [
        claim("ls1", "lloyd-smucker", "border_immigration", 1, False,
              "In 2021 voted for the Farm Workforce Modernization Act granting legal status to illegal immigrants in agriculture; in 2026 cosponsored the DIGNIDAD Act proposing a pathway to legal status for up to 12 million illegal immigrants — positions directly opposed to the rubric's mandatory-deportation standard.",
              ["https://en.wikipedia.org/wiki/Lloyd_Smucker",
               "https://ballotpedia.org/Lloyd_Smucker"]),
        claim("ls2", "lloyd-smucker", "sanctity_of_life", 0, True,
              "Voted for the One Big Beautiful Bill Act (H.R. 1, 2025; House 215-214), which includes Medicaid defunding of Planned Parenthood; votes in line with Trump's stated position 94% of the time (FiveThirtyEight), including support for pro-life executive actions and reconciliation provisions.",
              ["https://en.wikipedia.org/wiki/Lloyd_Smucker",
               "https://smucker.house.gov/issues/values"]),
    ]),

    # ---------------- John Joyce (PA-13, R) ----------------
    ("john-joyce", "PA", "Representative", [
        claim("jj1", "john-joyce", "sanctity_of_life", 0, True,
              "Received an A rating from SBA Pro-Life America; member of the Congressional Pro-Life Caucus; advocated on the House floor for the Born-Alive Abortion Survivors Protection Act and consistently voted to uphold the Hyde Amendment against taxpayer-funded abortion.",
              ["https://sbaprolife.org/representative/john-joyce",
               "https://johnjoyce.house.gov/media/press-releases/joyce-takes-house-floor-advocate-pro-life-agenda"]),
        claim("jj2", "john-joyce", "border_immigration", 1, True,
              "Voted for H.R. 2, the Secure the Border Act of 2023, to increase Border Patrol agents and strengthen enforcement; publicly calls for stopping 'de facto amnesty' and opposes any policies that create legal pathways outside orderly enforcement — consistent with the mandatory-deportation standard.",
              ["https://johnjoyce.house.gov/media/press-releases/joyce-stands-strong-border-security",
               "https://johnjoyce.house.gov/media/op-eds/congressman-john-joyce-we-must-stop-de-facto-amnesty-at-our-southern-border"]),
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
