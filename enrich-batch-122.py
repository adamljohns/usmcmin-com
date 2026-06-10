#!/usr/bin/env python3
"""Enrichment batch 122: hand-curated claims for 4 sitting VA U.S. Representatives.

Targets evidence_federal VA reps with 0 claims, taken from the bottom of the
alphabet (VA = bottom of available evidence_federal rep bucket). All sources
are official or major reference sites; all votes are documented roll-call votes.

Targets (4 D): Bobby Scott (VA-03), Don Beyer (VA-08),
Jennifer McClellan (VA-04), Eugene Vindman (VA-07).
Each candidate receives 2-3 claims spanning distinct rubric categories.

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
    # ---------------- Bobby Scott (VA-03, D) ----------------
    ("bobby-scott", "VA", "District 3", [
        claim("bs1", "bobby-scott", "sanctity_of_life", 0, False,
              "Voted YES on H.R. 8296, the Women's Health Protection Act of 2022 (House Vote #360, July 15, 2022), which would have codified a federal right to abortion up to viability — rejecting any personhood-from-conception standard. Scott issued a press release affirming his vote as defending 'reproductive health freedom.'",
              ["https://www.govtrack.us/congress/votes/117-2022/h360",
               "https://bobbyscott.house.gov/media-center/press-releases/scott-votes-defend-reproductive-health-freedom"]),
        claim("bs2", "bobby-scott", "self_defense", 1, False,
              "Voted YES on H.R. 1808, the Assault Weapons Ban of 2022 (House Vote #410, July 29, 2022), to prohibit the manufacture, sale, and transfer of semiautomatic assault weapons and large-capacity ammunition magazines — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.govtrack.us/congress/votes/117-2022/h410",
               "https://ballotpedia.org/Bobby_Scott_(Virginia)"]),
        claim("bs3", "bobby-scott", "border_immigration", 1, False,
              "Voted NO on S. 5, the Laken Riley Act (House Vote #23, Jan. 22, 2025), opposing mandatory detention of illegal immigrants arrested for theft or violent offenses. In his official statement Scott argued the bill was unconstitutional and that 'migrants are less likely to commit crimes than American citizens.'",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://bobbyscott.house.gov/media-center/press-releases/scott-statement-laken-riley-act"]),
    ]),

    # ---------------- Don Beyer (VA-08, D) ----------------
    ("don-beyer", "VA", "District 8", [
        claim("db1", "don-beyer", "sanctity_of_life", 0, False,
              "Cosponsored H.R. 3755, the Women's Health Protection Act of 2021, to codify a federal abortion right through viability into federal law — rejecting any personhood-from-conception standard.",
              ["https://www.congress.gov/bill/117th-congress/house-bill/3755",
               "https://ballotpedia.org/Don_Beyer"]),
        claim("db2", "don-beyer", "self_defense", 1, False,
              "In June 2022, introduced a bill to impose a 1,000% excise tax on assault-style rifles and high-capacity magazines as 'another creative pathway to actually make some sensible gun control happen,' and cosponsored H.R. 1808, the Assault Weapons Ban of 2022 — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://beyer.house.gov/voterecord/default.aspx",
               "https://ballotpedia.org/Don_Beyer"]),
        claim("db3", "don-beyer", "biblical_marriage", 0, False,
              "Voted YES on H.R. 8404, the Respect for Marriage Act (2022), codifying federal recognition of same-sex marriage and overriding any future Supreme Court reversal of Obergefell — rejecting the one-man-one-woman definition of marriage.",
              ["https://www.govtrack.us/congress/bills/117/hr8404",
               "https://en.wikipedia.org/wiki/Don_Beyer"]),
    ]),

    # ---------------- Jennifer McClellan (VA-04, D) ----------------
    ("jennifer-mcclellan", "VA", "District 4", [
        claim("jm1", "jennifer-mcclellan", "sanctity_of_life", 0, False,
              "Serves as Chair of the House Abortion Rights and Access Task Force and was an original cosponsor of H.R. 12, the Women's Health Protection Act of 2023 and 2025, to create a federal statutory right to abortion — rejecting any personhood-from-conception standard.",
              ["https://mcclellan.house.gov/issues",
               "https://www.congress.gov/bill/118th-congress/house-bill/12/cosponsors"]),
        claim("jm2", "jennifer-mcclellan", "border_immigration", 1, False,
              "Voted NO on S. 5, the Laken Riley Act (House Vote #23, Jan. 22, 2025), and released a statement opposing mandatory detention of undocumented immigrants arrested for certain crimes, arguing it violated due process and would harm immigrant communities.",
              ["https://www.govtrack.us/congress/votes/119-2025/h23",
               "https://mcclellan.house.gov/media/press-releases/mcclellan-statement-laken-riley-act"]),
        claim("jm3", "jennifer-mcclellan", "self_defense", 1, False,
              "Member of the House Gun Violence Prevention Task Force; supports expanded background checks, assault-weapons bans, and red-flag laws — opposing the rubric's defense of constitutional carry and opposition to new firearm restrictions.",
              ["https://ballotpedia.org/Jennifer_McClellan",
               "https://mcclellan.house.gov/issues"]),
    ]),

    # ---------------- Eugene Vindman (VA-07, D) ----------------
    ("eugene-vindman", "VA", "District 7", [
        claim("ev1", "eugene-vindman", "sanctity_of_life", 0, False,
              "Campaigned on a pledge to 'protect reproductive freedom' by stopping any national abortion ban and passing legislation to restore abortion access, rejecting any personhood-from-conception standard.",
              ["https://ballotpedia.org/Eugene_Vindman",
               "https://en.wikipedia.org/wiki/Eugene_Vindman"]),
        claim("ev2", "eugene-vindman", "self_defense", 1, False,
              "Voted in February 2026 for a sweeping House Democratic gun-control package, including the Law-Enforcement Innovate to De-Escalate Act providing nonlethal-option funding, and publicly backed 'commonsense policies … getting illegal guns off streets' — opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://vindman.house.gov/2026/02/12/vindman-votes-to-provide-non-lethal-options-to-law-enforcement-prevent-gun-violence/",
               "https://virginiamercury.com/2026/02/05/house-democrats-pass-sweeping-gun-control-package-over-gop-objections/"]),
        claim("ev3", "eugene-vindman", "border_immigration", 1, False,
              "Came to the U.S. as a Soviet Jewish refugee and consistently favors expanded legal-immigration pathways and humanitarian protections; opposes mandatory mass deportation, aligning with open-border rather than enforcement-first immigration policy — contra the rubric's mandatory-deportation standard.",
              ["https://ballotpedia.org/Eugene_Vindman",
               "https://en.wikipedia.org/wiki/Eugene_Vindman"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents name-collision bugs."""
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
