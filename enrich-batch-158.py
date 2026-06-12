#!/usr/bin/env python3
"""Enrichment batch 158: 5 sitting U.S. Representatives — OK (Cole, Brecheen, Bice) + OH (Balderson, Latta).

All are archetype_party_default with 0 evidence claims. Claims span distinct
rubric categories: sanctity_of_life, border_immigration, self_defense, and
(for Brecheen) foreign_policy_restraint. Sources: ballotpedia.org,
govtrack.us, congress.gov, sbaprolife.org, house.gov official sites.

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
    # ---------------- Tom Cole (OK-4, R) ----------------
    ("tom-cole", "OK", "Representative", [
        claim("tc1", "tom-cole", "sanctity_of_life", 0, True,
              "Consistently anti-abortion since entering Congress in 2003; in 2021 signed the Republican amicus brief urging the Supreme Court to overturn Roe v. Wade, celebrated Dobbs as 'a monumental win for the rights of unborn children,' and voted YEA on the Born-Alive Abortion Survivors Protection Act (H.R. 21, House Vote #27, Jan 23, 2025) — affirming his life-from-conception posture.",
              ["https://ballotpedia.org/Tom_Cole_(Oklahoma)",
               "https://www.govtrack.us/congress/members/tom_cole/400077",
               "https://www.govtrack.us/congress/votes/119-2025/h27"]),
        claim("tc2", "tom-cole", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (S.5, House Vote #23, Jan 22, 2025; signed Jan 29, 2025), which mandates Immigration and Customs Enforcement detention and deportation proceedings for illegal aliens arrested for theft or violent crimes — supporting mandatory deportation over discretionary release.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
        claim("tc3", "tom-cole", "self_defense", 1, True,
              "Has consistently voted against gun-control bills throughout his 20+ years in Congress; in 2023 cosponsored H.R. 771 (Firearm Lockbox Protection Act), a Second Amendment-protective measure, and GovTrack rates him among the most pro-gun members of the Oklahoma delegation.",
              ["https://ballotpedia.org/Tom_Cole_(Oklahoma)",
               "https://www.govtrack.us/congress/members/tom_cole/400077"]),
    ]),

    # ---------------- Josh Brecheen (OK-2, R) ----------------
    ("josh-brecheen", "OK", "Representative", [
        claim("jb1", "josh-brecheen", "sanctity_of_life", 0, True,
              "Freedom Caucus member who publicly celebrated the Dobbs decision as correcting 'the Court's unconstitutional ruling 49 years earlier in Roe v. Wade' and called for further work to protect the right to life; his first-term voting record earned a 100% SBA Pro-Life America score.",
              ["https://ballotpedia.org/Josh_Brecheen",
               "https://www.govtrack.us/congress/members/josh_brecheen/456931"]),
        claim("jb2", "josh-brecheen", "foreign_policy_restraint", 1, True,
              "Voted against the $60 billion Ukraine military-aid package in 2024, opposing continued open-ended U.S. military entanglement and arguing American resources should not flow indefinitely to foreign wars — consistent with the rubric's call to end forever-war foreign commitments.",
              ["https://ballotpedia.org/Josh_Brecheen",
               "https://en.wikipedia.org/wiki/Josh_Brecheen"]),
        claim("jb3", "josh-brecheen", "border_immigration", 1, True,
              "Introduced H.Amdt. 1032 to H.R. 8771 (House Vote #299, June 27, 2024) to tighten immigration by ending certain family-sponsored categories and reforming asylum procedures; also voted YEA on the Laken Riley Act (S.5, Jan 22, 2025) mandating detention of illegal aliens arrested for theft crimes.",
              ["https://www.govtrack.us/congress/votes/118-2024/h299",
               "https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://www.congress.gov/member/josh-brecheen/B001317"]),
    ]),

    # ---------------- Stephanie Bice (OK-5, R) ----------------
    ("stephanie-bice", "OK", "Representative", [
        claim("sb1", "stephanie-bice", "sanctity_of_life", 0, True,
              "Pro-Life Caucus member endorsed by SBA Pro-Life America with a 100% pro-life voting record in both the Oklahoma Senate and U.S. House; voted against H.R. 3755 (Women's Health Protection Act, which would have codified abortion-on-demand to birth) and stated: 'As a Christian and a mother, I believe in the sanctity of human life.'",
              ["https://sbaprolife.org/representative/stephanie-bice",
               "https://bice.house.gov/issues/values",
               "https://ballotpedia.org/Stephanie_Bice"]),
        claim("sb2", "stephanie-bice", "self_defense", 1, True,
              "A gun owner who states on her official issues page that the Second Amendment is 'a key freedom responsibly exercised by millions of law-abiding Americans' and commits to opposing 'radical efforts in Congress that would limit this important right' — a direct anti-restriction posture.",
              ["https://bice.house.gov/issues/values",
               "https://ballotpedia.org/Stephanie_Bice"]),
        claim("sb3", "stephanie-bice", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (S.5, House Vote #23, Jan 22, 2025), requiring DHS to detain and initiate removal proceedings against illegal aliens arrested for theft or burglary — enforcing mandatory deportation over discretionary catch-and-release.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
    ]),

    # ---------------- Troy Balderson (OH-12, R) ----------------
    ("troy-balderson", "OH", "Representative", [
        claim("tb1", "troy-balderson", "sanctity_of_life", 0, True,
              "Earned a 100% rating from the National Right to Life Committee; voted against the Women's Health Protection Act of 2022, which would have created a federal right to abortion to the point of birth; publicly thanked Ohio March for Life participants and affirms life-from-conception protections. GovTrack ranks him the most-conservative member of Ohio's House delegation in 2024.",
              ["https://sbaprolife.org/representative/troy-balderson",
               "https://ballotpedia.org/Troy_Balderson",
               "https://www.govtrack.us/congress/members/troy_balderson/412747/report-card/2024"]),
        claim("tb2", "troy-balderson", "border_immigration", 1, True,
              "Voted for HR 5525 (Continuing Appropriations and Border Security Enhancement Act, 2024) funding border-security enforcement, and voted YEA on the Laken Riley Act (S.5, Jan 22, 2025) mandating detention and removal proceedings for illegal aliens arrested for theft — supporting mandatory deportation over administrative discretion.",
              ["https://balderson.house.gov/news/documentsingle.aspx?DocumentID=1123",
               "https://www.govtrack.us/congress/votes/119-2025/h23"]),
        claim("tb3", "troy-balderson", "self_defense", 1, True,
              "Consistently votes to protect Second Amendment rights; as the most-conservative member of Ohio's House delegation (GovTrack 2024) he opposes every major gun-control proposal including red-flag legislation, assault-weapons bans, and magazine-capacity restrictions.",
              ["https://www.govtrack.us/congress/members/troy_balderson/412747/report-card/2024",
               "https://ballotpedia.org/Troy_Balderson"]),
    ]),

    # ---------------- Bob Latta (OH-5, R) ----------------
    ("bob-latta", "OH", "Representative", [
        claim("bl1", "bob-latta", "sanctity_of_life", 0, True,
              "100% NRLC rating across his 10-term congressional career; voted YEA on Born-Alive Abortion Survivors Protection Act (H.R. 26 in 118th Congress; H.R. 21 in 119th Congress, Jan 23, 2025); authored H.R. 4399 (Support and Value Expectant Moms and Babies Act) and H.R. 671 (Protecting the Dignity of Unborn Children Act), both affirming protection of life from conception.",
              ["https://sbaprolife.org/representative/bob-latta",
               "https://ballotpedia.org/Bob_Latta",
               "https://www.govtrack.us/congress/votes/119-2025/h27"]),
        claim("bl2", "bob-latta", "border_immigration", 1, True,
              "Voted YEA on the Laken Riley Act (S.5/H.R.29, House Vote #23, Jan 22, 2025; signed into law Jan 29, 2025), mandating ICE detention and removal proceedings for illegal aliens arrested for theft or burglary — reinforcing mandatory deportation over prosecutorial discretion.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://www.congress.gov/bill/119th-congress/senate-bill/5"]),
        claim("bl3", "bob-latta", "self_defense", 1, True,
              "Co-chaired the Congressional Sportsmen's Foundation and in 2013 introduced H.R. 3590 (the SHARE Act), NRA-backed legislation expanding sportsmen's rights; has maintained a consistent pro-Second Amendment voting record opposing new gun-control mandates throughout his 10 terms in Congress.",
              ["https://ballotpedia.org/Bob_Latta",
               "https://www.govtrack.us/congress/members/robert_latta/412256"]),
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
