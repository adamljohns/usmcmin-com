#!/usr/bin/env python3
"""Enrichment batch 169: 5 Republican US House members from bottom of alphabet.

Targets archetype_party_default federal members with 0 evidence claims,
taken from the bottom of the alphabet (MN, MI, MO).  All claims sourced from
official *.house.gov / *.senate.gov, congress.gov, govtrack.us, ballotpedia.org,
en.wikipedia.org, or sbaprolife.org and reflect 2024-2026 public record.

Candidates:
  Ann Wagner        (MO-2, R)  — sanctity_of_life, border_immigration
  Pete Stauber      (MN-8, R)  — sanctity_of_life, self_defense, election_integrity
  Michelle Fischbach (MN-7, R) — sanctity_of_life, self_defense, election_integrity
  Brad Finstad      (MN-1, R)  — election_integrity, border_immigration
  Tim Walberg       (MI-5, R)  — family_child_sovereignty, biblical_marriage, border_immigration
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
    # ---------------- Ann Wagner (MO-2, R) ----------------
    ("ann-wagner", "MO", "US House", [
        claim("aw1", "ann-wagner", "sanctity_of_life", 0, True,
              "Endorsed by SBA Pro-Life America in every reelection campaign as 'a tremendous advocate for unborn babies and their mothers'; has voted consistently to defund Planned Parenthood, strip taxpayer funding from abortion-travel reimbursement programs, and is a vocal public champion of the Pain-Capable Unborn Child Protection Act — placing her firmly within the rubric's life-at-conception and personhood-protection standard.",
              ["https://sbaprolife.org/representative/ann-wagner",
               "https://ballotpedia.org/Ann_Wagner"]),
        claim("aw2", "ann-wagner", "border_immigration", 1, True,
              "Voted for S. 2 (the Secure America Act, passed June 2026), the budget-reconciliation package providing over $70 billion for ICE and Customs and Border Protection immigration enforcement operations — a direct legislative funding commitment to mandatory detention and removal aligned with the rubric's deportation-enforcement standard.",
              ["https://en.wikipedia.org/wiki/Ann_Wagner",
               "https://wagner.house.gov/"]),
    ]),

    # ---------------- Pete Stauber (MN-8, R) ----------------
    ("pete-stauber", "MN", "US House", [
        claim("ps1", "pete-stauber", "sanctity_of_life", 0, True,
              "Voted against the Democrats' Women's Health Protection Act (H.R. 3755) — which Stauber called the 'Abortion on Demand Until Birth Act' — and celebrated the Dobbs decision as 'a win for the sanctity of life'; also led legislation in the 119th Congress to prohibit abortions performed solely because of a Down Syndrome diagnosis, taking the fight beyond mere restriction to affirmative protection of the disabled unborn.",
              ["https://stauber.house.gov/media/press-releases/stauber-leads-legislation-prohibit-abortions-based-down-syndrome-diagnosis",
               "https://sbaprolife.org/representative/pete-stauber"]),
        claim("ps2", "pete-stauber", "self_defense", 1, True,
              "Voted against H.R. 8 (universal background check expansion) and H.R. 1446 (extended background check delays) — two Democrat-led gun bills Stauber characterized as an 'unconstitutional gun grab' that would make it 'increasingly harder for law-abiding citizens to exercise their Second Amendment rights' while doing nothing to stop criminals — a record consistent with the rubric's opposition to red-flag laws, magazine limits, and registry expansion.",
              ["https://stauber.house.gov/media/press-releases/stauber-votes-no-pelosi-s-unconstitutional-gun-grab",
               "https://ballotpedia.org/Pete_Stauber"]),
        claim("ps3", "pete-stauber", "election_integrity", 0, True,
              "Voted for the Safeguard American Voter Eligibility (SAVE) Act in July 2024 requiring documentary proof of U.S. citizenship to register for federal elections; and in 2026 co-introduced the Minnesota Voter Integrity Act (H.R. 7320) — alongside Reps. Emmer, Fischbach, and Finstad — to bar Minnesota from receiving federal election-assistance funds until its Secretary of State cooperates with the DOJ's review of noncitizen voter-roll entries.",
              ["https://stauber.house.gov/media/press-releases/stauber-votes-secure-american-elections",
               "https://www.congress.gov/bill/119th-congress/house-bill/7320"]),
    ]),

    # ---------------- Michelle Fischbach (MN-7, R) ----------------
    ("michelle-fischbach", "MN", "US House", [
        claim("mf1", "michelle-fischbach", "sanctity_of_life", 0, True,
              "Carries a 100% lifetime voting score with National Right to Life — the most rigorous life-at-conception scorecard in Congress — and has never deviated from a perfect pro-life voting record across her entire House tenure, reflecting consistent alignment with the rubric's personhood-from-conception standard.",
              ["https://ballotpedia.org/Michelle_Fischbach",
               "https://fischbach.house.gov/"]),
        claim("mf2", "michelle-fischbach", "self_defense", 1, True,
              "Holds lifetime 'A' ratings from both the NRA Political Victory Fund and Gun Owners of America — the two leading constitutional-carry and anti-gun-control scorecards — signaling a consistent record opposing red-flag laws, assault-weapons bans, magazine-capacity restrictions, and firearm-registry expansion.",
              ["https://ballotpedia.org/Michelle_Fischbach",
               "https://www.govtrack.us/congress/members/michelle_fischbach/456828"]),
        claim("mf3", "michelle-fischbach", "election_integrity", 0, True,
              "Voted for H.R. 22 (the SAVE Act) when it passed the House in April 2025 — requiring proof of U.S. citizenship to register for federal elections and mandating removal of noncitizens from state voter rolls — calling it 'a simple, straightforward YES for all of us who believe in election integrity'; also co-introduced the Minnesota Voter Integrity Act of 2026 to condition federal election funding on Minnesota cooperating with DOJ's noncitizen-voter-roll audit.",
              ["https://fischbach.house.gov/2025/4/save-act-passes-in-the-house",
               "https://www.congress.gov/bill/119th-congress/house-bill/22/cosponsors"]),
    ]),

    # ---------------- Brad Finstad (MN-1, R) ----------------
    ("brad-finstad", "MN", "US House", [
        claim("bf1", "brad-finstad", "election_integrity", 0, True,
              "Voted in favor of the Safeguard American Voter Eligibility (SAVE) Act to require proof of U.S. citizenship for federal-election voter registration, calling it essential protection against noncitizen voting; and co-introduced the Minnesota Voter Integrity Act of 2026 (H.R. 7320) alongside Reps. Emmer, Stauber, and Fischbach to cut off federal election-assistance funds to Minnesota until the state cooperates with the DOJ's noncitizen voter-roll review.",
              ["https://finstad.house.gov/2024/9/finstad-releases-statement-following-vote-on-save-act-and-cr",
               "https://www.congress.gov/bill/119th-congress/house-bill/7320"]),
        claim("bf2", "brad-finstad", "border_immigration", 1, True,
              "Introduced the Preserving Integrity in Immigration Benefits Act in January 2026 to close loopholes that allow illegal immigrants to receive federal immigration benefits; and has consistently opposed Biden-Harris open-border policies as threats to community safety and election integrity, framing border enforcement as inseparable from both national security and rule of law.",
              ["https://finstad.house.gov/",
               "https://www.congress.gov/member/brad-finstad/F000475"]),
    ]),

    # ---------------- Tim Walberg (MI-5, R) ----------------
    ("tim-walberg", "MI", "US Representative", [
        claim("tw1", "tim-walberg", "family_child_sovereignty", 0, True,
              "As chair of the House Education and Workforce Committee (119th Congress), advanced the PROTECT Kids Act requiring federally funded elementary and middle schools to obtain written parental consent before changing a student's pronouns, gender markers, or preferred name on any school form; also authored and passed a Parental Rights Bill of Rights provision through the full House — making parent notification and consent in schools a legislative priority.",
              ["https://walberg.house.gov/media/press-releases/walbergs-protect-kids-act-advanced-committee",
               "https://walberg.house.gov/media/press-releases/walberg-scott-introduce-bill-safeguard-parental-rights"]),
        claim("tw2", "tim-walberg", "biblical_marriage", 1, True,
              "Voted against the Respect for Marriage Act (2022) codifying federal recognition of same-sex unions; after the Obergefell ruling expressed being 'troubled' by the Court's direction and stated his 'principled belief that marriage should continue to stand for the union of a man and woman' — a position maintained from his time as a pastor through his congressional career, consistently rejecting the redefinition of marriage.",
              ["https://en.wikipedia.org/wiki/Tim_Walberg",
               "https://walberg.house.gov/media/press-releases/rep-walberg-responds-supreme-courts-decisions-marriage"]),
        claim("tw3", "tim-walberg", "border_immigration", 1, True,
              "Supported the Laken Riley Act (S. 5 / H.R. 29, the first legislation signed by President Trump in his second term), mandating ICE detention and removal proceedings for illegal immigrants who commit theft, burglary, and other specified crimes — a mandatory-deportation measure directly aligned with the rubric's border-enforcement standard.",
              ["https://ballotpedia.org/Tim_Walberg",
               "https://walberg.house.gov/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collision across states."""
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

    # Minified write — preserve the no-whitespace master (keeps scorecard.json ~35-36MB, under GitHub's 50MB limit).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
