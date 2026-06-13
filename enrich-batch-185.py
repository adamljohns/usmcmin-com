#!/usr/bin/env python3
"""Enrichment batch 185: 5 sitting Republican U.S. Representatives with 0 claims.

archetype_curated federal bucket is exhausted (only 2 remain, both with claims).
Targets taken from sitting archetype_party_default reps at the bottom of the
alphabet: Mann (KS), Estes (KS), Spartz (IN), Miller (IL), Guthrie (KY).

NOTE: writes scorecard.json MINIFIED to keep the master under GitHub's 50MB limit.
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
    # ---------- Tracey Mann (KS-01, R) ----------
    ("tracey-mann", "KS", "Representative", [
        claim("tm1", "tracey-mann", "sanctity_of_life", 0, True,
              "Holds an A+ rating from SBA Pro-Life America; cosponsored H.R. 18 (No Taxpayer Funding for Abortion Act) and voted more than 20 times for pro-life legislation in 2021 alone — affirming protection of the unborn from conception.",
              ["https://sbaprolife.org/representative/tracey-mann",
               "https://mann.house.gov/media/press-releases/rep-mann-receives-rating-pro-life-susan-b-anthony-list"]),
        claim("tm2", "tracey-mann", "self_defense", 1, True,
              "Cosponsored the Constitutional Concealed Carry Reciprocity Act (H.R. 38), which would establish nationwide reciprocity for concealed-carry permit holders; voted against assault-weapons ban legislation; consistently opposed new federal gun restrictions.",
              ["https://mann.house.gov/media/press-releases/reps-mann-hudson-introduce-bill-expand-concealed-carry-permits",
               "https://mann.house.gov/media/press-releases/rep-tracey-mann-stands-second-amendment-rights-votes-against-gun-ban"]),
        claim("tm3", "tracey-mann", "self_defense", 4, True,
              "Introduced the RIFLE Act to rein in what he considers unconstitutional ATF overreach against federal firearms licensees — directly targeting agency overreach on Second Amendment enforcement.",
              ["https://mann.house.gov/media/press-releases/rep-mann-fortifies-gun-rights-continues-fight-rein-atf",
               "https://mann.house.gov/issues/second-amendment"]),
    ]),

    # ---------- Ron Estes (KS-04, R) ----------
    ("ron-estes", "KS", "Representative", [
        claim("re1", "ron-estes", "sanctity_of_life", 0, True,
              "Led a 140-member Congressional letter to HHS urging adoption of the Protect Life Rule, which requires Title X-funded providers to refer patients only to life-affirming alternatives rather than abortion providers — a key pro-life regulatory priority.",
              ["https://sbaprolife.org/representative/ron-estes",
               "https://estes.house.gov/"]),
        claim("re2", "ron-estes", "election_integrity", 0, True,
              "Voted against certifying the Electoral College votes from Arizona and Pennsylvania in the January 2021 joint session of Congress, citing unresolved concerns about election-process irregularities and demanding accountability for the integrity of the 2020 presidential election.",
              ["https://en.wikipedia.org/wiki/Ron_Estes",
               "https://ballotpedia.org/Ron_Estes"]),
        claim("re3", "ron-estes", "border_immigration", 0, True,
              "Member of the House Border Security Caucus; led colleagues in formally demanding answers from the Biden administration on what he characterized as a deliberate 'open border' crisis — supporting physical barrier construction and robust enforcement at the southern border.",
              ["https://estes.house.gov/news/documentsingle.aspx?DocumentID=3341",
               "https://en.wikipedia.org/wiki/Ron_Estes"]),
    ]),

    # ---------- Victoria Spartz (IN-05, R) ----------
    ("victoria-spartz", "IN", "Representative", [
        claim("vs1", "victoria-spartz", "sanctity_of_life", 0, True,
              "Endorsed by SBA List's Candidate Fund PAC and holds an A+ pro-life voting record in the House, opposing every federal measure that would have expanded abortion access or compelled taxpayer funding of abortion.",
              ["https://sbaprolife.org/representative/victoria-spartz",
               "https://sbaprolife.org/newsroom/press-releases/sba-lists-candidate-fund-pac-endorses-rep-victoria-spartz-in-in-05"]),
        claim("vs2", "victoria-spartz", "economic_stewardship", 2, True,
              "Self-described fiscal hawk who cosponsored the Fiscal Commission Act of 2023 to confront runaway federal debt, and in 2025 publicly opposed the Republican budget resolution she said would 'balloon the deficit by trillions of dollars' — standing on principle against deficit spending even under party pressure.",
              ["https://en.wikipedia.org/wiki/Victoria_Spartz",
               "https://ballotpedia.org/Victoria_Spartz"]),
        claim("vs3", "victoria-spartz", "foreign_policy_restraint", 0, True,
              "Demanded Congress exercise Article I oversight of more than $50 billion in Ukraine wartime aid, introducing legislation for a joint congressional task force to track how the money is spent — insisting that funding foreign wars without accountability violates the constitutional role of the legislature.",
              ["https://spartz.house.gov/media/press-releases/congress-must-be-proactive-implement-proper-oversight-and-joint-task-force",
               "https://en.wikipedia.org/wiki/Victoria_Spartz"]),
    ]),

    # ---------- Mary Miller (IL-15, R) ----------
    ("mary-miller", "IL", "Representative", [
        claim("mm1", "mary-miller", "family_child_sovereignty", 0, True,
              "Introduced H.J.Res.127 (September 2025), a constitutional amendment to permanently enshrine parental rights to direct the upbringing and education of their children — placing that authority beyond the reach of federal agencies or school bureaucracies.",
              ["https://marymiller.house.gov/media/press-releases/rep-mary-miller-introduces-constitutional-amendment-enshrine-parental-rights",
               "https://en.wikipedia.org/wiki/Mary_Miller_(politician)"]),
        claim("mm2", "mary-miller", "border_immigration", 0, True,
              "Co-sponsored the Secure America's Borders First Act (February 2022), legislation that would have prohibited military and security assistance to Ukraine until the southern border with Mexico was secured — explicitly tying national defense spending to border enforcement.",
              ["https://en.wikipedia.org/wiki/Mary_Miller_(politician)",
               "https://ballotpedia.org/Mary_Miller_(Illinois)"]),
        claim("mm3", "mary-miller", "sanctity_of_life", 0, True,
              "Freedom Caucus member with a consistently pro-life voting record; opposed every federal measure that would have expanded abortion access, codified Roe, or compelled taxpayer funding of abortion.",
              ["https://en.wikipedia.org/wiki/Mary_Miller_(politician)",
               "https://marymiller.house.gov/about"]),
    ]),

    # ---------- Brett Guthrie (KY-02, R) ----------
    ("brett-guthrie", "KY", "Representative", [
        claim("bg1", "brett-guthrie", "sanctity_of_life", 0, True,
              "Voted against H.R. 3755, the Women's Health Protection Act, which would have codified abortion rights through all nine months of pregnancy at the federal level; maintains a consistent pro-life voting record recognized by SBA Pro-Life America.",
              ["https://sbaprolife.org/representative/brett-guthrie",
               "https://en.wikipedia.org/wiki/Brett_Guthrie"]),
        claim("bg2", "brett-guthrie", "economic_stewardship", 2, True,
              "As Chairman of the House Energy and Commerce Committee in the 119th Congress (2025), authored reconciliation provisions including Medicaid work requirements and significant reductions to federal health entitlement spending — advancing the committee's largest spending-restraint package in decades.",
              ["https://energycommerce.house.gov/representatives/guthrie",
               "https://en.wikipedia.org/wiki/Brett_Guthrie"]),
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
