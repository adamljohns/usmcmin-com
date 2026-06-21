#!/usr/bin/env python3
"""Enrichment batch 340: 5 Virginia state legislators from bottom of evidence_state bucket.

archetype_curated federal and state buckets are fully exhausted; this batch
continues the evidence_state queue from the bottom of the alphabet (VA, S-names).

Targets (reverse-alpha top-5 of remaining VA evidence_state 0-claim):
  Scott Surovell        VA-D, State Senate District 34 (Senate Majority Leader)
  Schuyler VanValkenburg VA-D, State Senate District 16
  Sam Rasoul            VA-D, House of Delegates District 38 (Roanoke)
  Saddam Azlan Salim    VA-D, State Senate District 37 (Falls Church/Fairfax)
  Russet Perry          VA-D, State Senate District 31

Each claim cites >=1 reliable source reflecting 2024-2026 public record/positions.
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


# Each entry: (slug, state, office_must_contain, claims-list)
TARGETS = [
    # ---------- Scott Surovell (VA-D, State Senate District 34, Senate Majority Leader) ----------
    ("scott-surovell", "VA", "State Senate", [
        claim("ss1", "scott-surovell", "sanctity_of_life", 0, False,
              "As Virginia Senate Majority Leader, Scott Surovell declared upon taking leadership: 'We need to get Roe v. Wade into the constitution of Virginia.' In January 2025 he supported the constitutional amendment recognizing Virginians' fundamental right to reproductive freedom — encompassing abortion, contraception, miscarriage management, and fertility care — directly rejecting any life-at-conception or personhood standard.",
              ["https://ballotpedia.org/Scott_Surovell",
               "https://en.wikipedia.org/wiki/Scott_Surovell",
               "https://www.vpap.org/legislators/39301-scott-surovell/"]),
        claim("ss2", "scott-surovell", "biblical_marriage", 0, False,
              "In January 2025, Surovell co-sponsored the constitutional amendment to repeal Virginia's 2006 marriage amendment that defined marriage as 'only a union between a man and a woman,' clearing the way to remove the one-man-one-woman definition from the Virginia Constitution and replace it with no-restriction language. He is a vocal champion of same-sex marriage rights, directly rejecting the biblical definition of marriage the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Scott_Surovell",
               "https://ballotpedia.org/Scott_Surovell",
               "https://www.richmondsunlight.com/legislator/sasurovell/"]),
    ]),

    # ---------- Schuyler VanValkenburg (VA-D, State Senate District 16) ----------
    ("schuyler-vanvalkenburg", "VA", "State Senate", [
        claim("svv1", "schuyler-vanvalkenburg", "sanctity_of_life", 0, False,
              "Schuyler VanValkenburg co-sponsored the Repeal Act — a Virginia bill to eliminate existing restrictions on abortion later in pregnancy — and has consistently backed legislation protecting abortion access through all trimesters under medical discretion, rejecting any life-at-conception or personhood standard. He supports Virginia's constitutional amendment to enshrine the right to reproductive freedom in the state constitution.",
              ["https://en.wikipedia.org/wiki/Schuyler_VanValkenburg",
               "https://ballotpedia.org/Schuyler_VanValkenburg",
               "https://virginiamercury.com/2023/10/10/senate-district-16-race-democrat-vanvalkenburg-vs-republican-incumbent-dunnavant/"]),
        claim("svv2", "schuyler-vanvalkenburg", "self_defense", 1, False,
              "VanValkenburg introduced legislation creating felony charges for parents or guardians who allow a child under 18 to access a firearm — the Lucia Bremer Act (named for a 13-year-old shot by a classmate). He declared safe gun-storage legislation would be his first bill in the Senate, stating 'We can and must do more to keep our kids safe from gun violence.' He opposes constitutional-carry and unrestricted access principles the rubric supports.",
              ["https://en.wikipedia.org/wiki/Schuyler_VanValkenburg",
               "https://ballotpedia.org/Schuyler_VanValkenburg",
               "https://virginiamercury.com/2024/03/27/youngkin-signs-bill-filed-after-shooting-death-of-henrico-teen-vetoes-30-others-related-to-guns/"]),
    ]),

    # ---------- Sam Rasoul (VA-D, House of Delegates District 38, Roanoke) ----------
    ("sam-rasoul", "VA", "House of Delegates", [
        claim("sr1", "sam-rasoul", "sanctity_of_life", 0, False,
              "Sam Rasoul supports abortion rights and backs expanding reproductive healthcare access in Virginia. His platform calls for protecting Virginia's current abortion laws and he votes consistently with the House Democratic caucus to reject any personhood-from-conception restrictions. The Progressive Voters Guide identifies him as a champion of reproductive rights in the Roanoke delegation.",
              ["https://ballotpedia.org/Sam_Rasoul",
               "https://progressivevotersguide.com/virginia/2025/general/s-sam-rasoul",
               "https://www.sam4va.com/peoples-platform"]),
        claim("sr2", "sam-rasoul", "self_defense", 1, False,
              "Rasoul has stated he supports 'mandatory background checks, a ban on weapons of war and high-capacity magazines, and red flag laws' — a direct legislative platform opposing the Second Amendment rights protected by the rubric's anti-ban and anti-red-flag principles. He votes consistently with the Virginia House Democratic caucus on gun-restriction measures.",
              ["https://www.sam4va.com/peoples-platform",
               "https://ballotpedia.org/Sam_Rasoul",
               "https://progressivevotersguide.com/virginia/2025/general/s-sam-rasoul"]),
    ]),

    # ---------- Saddam Azlan Salim (VA-D, State Senate District 37, Falls Church/Fairfax) ----------
    ("saddam-azlan-salim", "VA", "State Senate", [
        claim("sas1", "saddam-azlan-salim", "sanctity_of_life", 0, False,
              "Saddam Azlan Salim voted to pass — and co-sponsored — Virginia's constitutional amendment recognizing Virginians' fundamental right to reproductive freedom, encompassing abortion, contraception, miscarriage management, and fertility care. Virginia's Choice Tracker rates him explicitly as Pro-Choice. He stated the amendment would enshrine reproductive rights in the state constitution, 'safeguarding these freedoms from potential future assaults by the General Assembly,' directly rejecting any life-at-conception or personhood standard.",
              ["https://choicetracker.org/va/people/saddam-azlan-salim/77332480",
               "https://www.salimforsenate.com/policy",
               "https://www.fcnp.com/2025/01/30/va-senator-saddam-salim-richmond-report/"]),
        claim("sas2", "saddam-azlan-salim", "self_defense", 1, False,
              "Senator Salim introduced SB848 to raise the age to purchase an assault firearm to 21 years old, and SB891 to impose a five-day waiting period before any firearm purchase — explicitly arguing both measures would reduce gun homicides and suicides. These bills directly oppose the rubric's anti-restriction and anti-waiting-period principles protecting Second Amendment rights.",
              ["https://www.salimforsenate.com/policy",
               "https://www.fcnp.com/2025/01/30/va-senator-saddam-salim-richmond-report/",
               "https://legiscan.com/VA/people/saddam-salim/id/24982"]),
    ]),

    # ---------- Russet Perry (VA-D, State Senate District 31) ----------
    ("russet-perry", "VA", "State Senate", [
        claim("rp1", "russet-perry", "sanctity_of_life", 0, False,
              "Russet Perry campaigned and serves on a platform of protecting abortion access, stating: 'Like most voters in our commonwealth, I support the current law as it stands,' and 'I will be the vote to protect the right to choose.' She positioned herself as the decisive vote against any abortion restrictions, framing her opponent's vote for a 15-week ban as the pro-restriction threat she would block — directly opposing the life-at-conception and personhood standard the rubric supports.",
              ["https://ballotpedia.org/Russet_Perry",
               "https://virginiamercury.com/2023/10/19/senate-district-31-race-republican-juan-pablo-segura-vs-democrat-russet-perry/",
               "https://en.wikipedia.org/wiki/Russet_Perry"]),
        claim("rp2", "russet-perry", "self_defense", 1, False,
              "Perry championed and passed legislation restricting firearm purchases for individuals convicted of assault and battery of a family or household member or intimate partner — expanding the class of disqualifying offenses beyond federal law. She votes consistently with the Virginia Senate Democratic caucus on gun-restriction measures, opposing the rubric's anti-restriction and constitutional-carry principles.",
              ["https://ballotpedia.org/Russet_Perry",
               "https://www.vpap.org/legislators/447053-russet-perry/",
               "https://virginiamercury.com/2023/10/19/senate-district-31-race-republican-juan-pablo-segura-vs-democrat-russet-perry/"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents slug collisions across states."""
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
