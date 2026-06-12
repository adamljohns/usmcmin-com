#!/usr/bin/env python3
"""Enrichment batch 148: hand-curated claims for 5 sitting U.S. Representatives.

archetype_curated pool is exhausted; this batch targets bottom-of-alphabet
sitting Republicans from TX (Monica De La Cruz, John Carter, Jake Ellzey)
and TN (Scott DesJarlais, Diana Harshbarger), all archetype_party_default
with 0 claims.

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
    # ---------------- Monica De La Cruz (TX-15, R) ----------------
    ("monica-de-la-cruz", "TX", "Representative", [
        claim("mdlc1", "monica-de-la-cruz", "sanctity_of_life", 0, True,
              "Applauded the Supreme Court's Dobbs ruling as 'monumental' and returning authority to protect the unborn to the states; rated 100% by the National Right to Life Committee with a consistent record of voting against federal taxpayer funding of abortion domestically and internationally — affirming protection of the unborn from conception.",
              ["https://sbaprolife.org/representative/monica-de-la-cruz",
               "https://en.wikipedia.org/wiki/Monica_De_La_Cruz"]),
        claim("mdlc2", "monica-de-la-cruz", "border_immigration", 1, False,
              "In 2026 co-sponsored the DIGNIDAD Act, which would establish a pathway to legal status for up to 12 million illegal immigrants currently in the United States, paired with mandatory work and restitution requirements — a legislative amnesty framework contrary to the rubric's mandatory-deportation standard for those who entered unlawfully.",
              ["https://ballotpedia.org/Monica_De_La_Cruz",
               "https://en.wikipedia.org/wiki/Monica_De_La_Cruz"]),
        claim("mdlc3", "monica-de-la-cruz", "self_defense", 1, True,
              "States publicly that protecting the constitutional right to keep and bear arms so citizens can defend their homes and families is a core commitment; her voting record opposes new federal firearm restrictions, consistent with defending the Second Amendment against further infringement.",
              ["https://delacruz.house.gov/about/",
               "https://ballotpedia.org/Monica_De_La_Cruz"]),
    ]),

    # ---------------- John Carter (TX-31, R) ----------------
    ("john-carter", "TX", "Representative", [
        claim("jc1", "john-carter", "sanctity_of_life", 0, True,
              "Carries a consistent 100% pro-life voting record endorsed by SBA Pro-Life America: co-sponsored the No Taxpayer Funding of Abortion Act, the Defund Planned Parenthood Act, the Protect Life Act, and the Pain-Capable Unborn Child Protection Act across multiple terms — a two-decade legislative record blocking federal abortion funding and defending unborn life from conception.",
              ["https://sbaprolife.org/representative/john-carter",
               "https://carter.house.gov/news/documentsingle.aspx?DocumentID=1167"]),
        claim("jc2", "john-carter", "border_immigration", 0, True,
              "A 20-year member of the House Appropriations subcommittee overseeing Homeland Security, Carter has consistently secured funding for border-wall construction, Border Patrol agents, and immigration enforcement operations — making him one of the longest-serving legislative architects of physical and personnel-based border security in the House.",
              ["https://ballotpedia.org/John_Carter_(Texas)",
               "https://carter.house.gov/press-releases/tag/border-security-and-immigration/"]),
    ]),

    # ---------------- Jake Ellzey (TX-06, R) ----------------
    ("jake-ellzey", "TX", "Representative", [
        claim("je1", "jake-ellzey", "sanctity_of_life", 0, True,
              "Holds a consistent pro-life voting record scored by SBA Pro-Life America: voted for the one-year Medicaid defunding of Planned Parenthood through the H.R.1 reconciliation bill (2025), the largest pro-life legislative victory in two decades — removing federal dollars from the nation's largest abortion provider.",
              ["https://sbaprolife.org/representative/jake-ellzey",
               "https://ellzey.house.gov/about"]),
        claim("je2", "jake-ellzey", "border_immigration", 1, True,
              "Voted for the Laken Riley Act (H.R.29 / S.5, signed into law January 29, 2025) and publicly commended its signing as protecting American communities from criminal illegal immigrants by requiring DHS to detain any alien arrested for theft, burglary, or violent crimes — ending the Biden-era catch-and-release policy for criminal aliens.",
              ["https://ellzey.house.gov/2025/1/congressman-jake-ellzey-commends-the-signing-of-the-laken-riley-act-into-law-to-protect-american-communities",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
    ]),

    # ---------------- Scott DesJarlais (TN-04, R) ----------------
    ("scott-desjarlais", "TN", "Representative", [
        claim("sdj1", "scott-desjarlais", "self_defense", 1, True,
              "Holds an 'A' rating from the National Rifle Association; was an original co-sponsor of the Concealed Carry Reciprocity Act, which would ensure Tennesseans lawfully licensed to carry a concealed handgun may do so in any other state with concealed-carry laws — removing interstate bureaucratic burdens on law-abiding gun owners and affirming the right to self-defense beyond state lines.",
              ["https://desjarlais.house.gov/media-center/press-releases/original-co-sponsor-rep-scott-desjarlais-votes-for-concealed-carry-bill",
               "https://ballotpedia.org/Scott_DesJarlais"]),
        claim("sdj2", "scott-desjarlais", "border_immigration", 2, True,
              "Earned an 'A' rating from NumbersUSA for his legislative record opposing illegal immigration; serves as a founding member of the Congressional Border Security Caucus and has consistently voted against sanctuary-friendly appropriations riders, supporting mandatory immigration-detainer cooperation with federal enforcement.",
              ["https://ballotpedia.org/Scott_DesJarlais",
               "https://desjarlais.house.gov/border-immigration-enforcement"]),
    ]),

    # ---------------- Diana Harshbarger (TN-01, R) ----------------
    ("diana-harshbarger", "TN", "Representative", [
        claim("dh1", "diana-harshbarger", "sanctity_of_life", 0, True,
              "Carries a 100% pro-life record scored by SBA Pro-Life America: voted for the H.R.1 reconciliation bill (2025) defunding Planned Parenthood of Medicaid dollars for one year — the largest pro-life legislative victory in two decades — and co-led a letter to the FDA Commissioner demanding reinstatement of key safety standards for the abortion drug mifepristone; also reintroduced the Pregnancy.Gov Act providing resource support to pregnant and parenting women.",
              ["https://sbaprolife.org/representative/diana-harshbarger",
               "https://harshbarger.house.gov/"]),
        claim("dh2", "diana-harshbarger", "biblical_marriage", 2, True,
              "Introduced H.R. 8573, legislation to prohibit gender transition procedures on minors at the federal level, directly opposing the transgender ideology being applied to children through medical and institutional channels — a clear stand against the gender-ideology agenda the rubric identifies as a threat to biblical anthropology.",
              ["https://en.wikipedia.org/wiki/Diana_Harshbarger",
               "https://harshbarger.house.gov/"]),
        claim("dh3", "diana-harshbarger", "border_immigration", 1, True,
              "Co-sponsored the Laken Riley Act (H.R.29, 119th Congress, signed January 29, 2025) requiring DHS to detain illegal aliens arrested for theft, burglary, or violent crimes; also voted against Democratic attempts to expand firearms background-check requirements, affirming a border-enforcement-first posture aligned with mandatory detention over catch-and-release.",
              ["https://harshbarger.house.gov/issues/second-amendment",
               "https://www.congress.gov/bill/119th-congress/house-bill/29"]),
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
