#!/usr/bin/env python3
"""Enrichment batch 512: hand-curated claims for 5 WA state representatives.

All federal-senator and federal-representative archetype_curated pools are
fully exhausted. This batch pivots to Washington State (WA) Republican state
representatives taken from the bottom of the candidate alphabet.

Targets (all R, archetype_party_default → evidence_curated):
  Jim Walsh         (WA-19, State Rep)
  Jeremie Dufault   (WA-15, State Rep)
  Jenny Graham      (WA-6,  State Rep)
  Hunter Abell      (WA-7,  State Rep)
  Gloria Mendoza    (WA-14, State Rep)

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
    # ---------------- Jim Walsh (WA-19, State Rep) ----------------
    ("jim-walsh", "WA", "Representative", [
        claim("jw1", "jim-walsh", "sanctity_of_life", 0, True,
              "Spoke on the Washington House floor in February 2023 in direct opposition to SHB 1469, the Democrat-backed abortion-access bill that would have made Washington a nationwide 'abortion destination.' Walsh called the bill an overreach, offered pro-life amendments, and voted against passage — placing him firmly in the pro-life camp in an otherwise pro-choice state legislature.",
              ["https://jimwalsh.houserepublicans.wa.gov/2023/03/01/rep-jim-walsh-speaks-in-favor-of-his-amendment-to-controversial-abortion-access-bill/",
               "https://ballotpedia.org/Jim_Walsh_(Washington)"]),
        claim("jw2", "jim-walsh", "family_child_sovereignty", 0, True,
              "Called HB 1296 — the 2025 Democrat bill gutting Washington's Initiative 2081 Parents' Bill of Rights — 'the worst bill of the session.' Walsh fought to restore parental-notification rights and opposed any OSPI authority to defund schools that honor parental oversight, casting a 'no' vote on final passage.",
              ["https://jimwalsh.houserepublicans.wa.gov/2025/03/13/rep-jim-walsh-fights-to-protect-parental-rights-house-bill-1296/",
               "http://jimwalsh.houserepublicans.wa.gov/2025/04/25/rep-jim-walsh-calls-house-bill-1296-the-worst-bill-of-the-session/"]),
        claim("jw3", "jim-walsh", "sanctity_of_life", 3, True,
              "Urged a 'no' vote on HB 1215 (2025), which would remove all references to pregnancy from Washington's model advance health care directive form — a stealth push to normalize death-positive end-of-life norms. Walsh argued the bill 'tilts away from life and toward death' and voted against it.",
              ["https://jimwalsh.houserepublicans.wa.gov/2025/02/13/rep-jim-walsh-opposes-house-bill-1215/",
               "https://ballotpedia.org/Jim_Walsh_(Washington)"]),
    ]),

    # ---------------- Jeremie Dufault (WA-15, State Rep) ----------------
    ("jeremie-dufault", "WA", "Representative", [
        claim("jd1", "jeremie-dufault", "biblical_marriage", 2, True,
              "Fights for gender-appropriate bathroom and locker-room policies in public schools, opposing Democrat-backed legislation that would allow biological males into female-only spaces. He gave floor speeches opposing bills that would gut the Parents' Bill of Rights and enable schools to withhold gender-identity information from parents.",
              ["https://ballotpedia.org/Jeremie_Dufault",
               "https://jeremiedufault.houserepublicans.wa.gov/2025/03/25/rep-jeremie-dufault-legislature-tries-to-gut-parents-bill-of-rights/"]),
        claim("jd2", "jeremie-dufault", "family_child_sovereignty", 0, True,
              "A vocal defender of Initiative 2081, Washington's Parents' Bill of Rights, which requires schools to notify parents about their children's health, welfare, and academic progress. When the Democrat majority moved to gut I-2081 via HB 1296 in 2025, Dufault actively opposed the bill in committee and on the floor, fighting to keep parental-notification rights intact.",
              ["https://jeremiedufault.houserepublicans.wa.gov/2025/03/25/rep-jeremie-dufault-legislature-tries-to-gut-parents-bill-of-rights/",
               "https://jeremiedufault.houserepublicans.wa.gov/2025/01/29/rep-dufault-back-in-olympia-representing-yakima-and-benton-counties/"]),
    ]),

    # ---------------- Jenny Graham (WA-6, State Rep) ----------------
    ("jenny-graham", "WA", "Representative", [
        claim("jg1", "jenny-graham", "self_defense", 1, True,
              "As Ranking Member on the House Community Safety Committee, Graham actively opposed Democrat anti-gun bills in the 2025 session — including HB 1163 (permit-to-purchase requirement) and an 11% excise tax on firearms — calling them unconstitutional infringements on law-abiding Washingtonians' Second Amendment rights. She also introduced HB 1799 to end early-release credits for violent firearms offenders.",
              ["https://jennygraham.houserepublicans.wa.gov/2025/02/14/rep-jenny-graham-breaks-down-firearm-legislation-including-her-house-bill-1799/",
               "https://jennygraham.houserepublicans.wa.gov/2025/02/03/rep-jenny-graham-fights-to-end-early-release-for-violent-firearms-offenders/",
               "https://ballotpedia.org/Jenny_Graham"]),
        claim("jg2", "jenny-graham", "family_child_sovereignty", 0, True,
              "Proposed the original 'Parental Bill of Rights' legislation in Olympia in 2023 — a precursor to the Initiative 2081 Parents' Bill of Rights approved by Washington voters in 2024. In 2025, she fought to block HB 1296, the Democrat bill to undo those voter-approved parental-notification rights, calling it an attack on families.",
              ["https://jennygraham.houserepublicans.wa.gov/2023/01/26/graham-proposes-parental-bill-of-rights-in-olympia/",
               "https://jennygraham.houserepublicans.wa.gov/2025/03/04/rep-jenny-graham-exposes-hb-1296-the-bill-that-strips-parents-of-their-rights/"]),
    ]),

    # ---------------- Hunter Abell (WA-7, State Rep) ----------------
    ("hunter-abell", "WA", "Representative", [
        claim("ha1", "hunter-abell", "sanctity_of_life", 0, True,
              "A constitutional attorney who explicitly campaigns on protecting the unborn and fighting for women and children who have been trafficked and abused. His official platform states he will 'fight to protect the unborn' and he has maintained a consistent pro-life position throughout his tenure in the Washington House.",
              ["https://hunterabell.houserepublicans.wa.gov/about/",
               "https://ballotpedia.org/Hunter_Abell"]),
        claim("ha2", "hunter-abell", "self_defense", 1, True,
              "In his first 2025 legislative update, Abell named Second Amendment defense his highest priority. He opposed HB 1163 (the new permit-to-purchase system requiring training before firearm purchase), HB 1386 (an 11% gun-and-ammo excise tax he dubbed 'The Idaho Firearms Stimulus Act'), SB 5098 (restricting concealed carry in parks and public buildings), and SB 5099 (burdensome dealer-licensing fees) — opposing the full Democrat anti-gun agenda.",
              ["https://hunterabell.houserepublicans.wa.gov/2025/02/01/gun-bills-my-bills-and-how-you-can-be-involved-my-first-legislative-update-to-you-the-mighty-7th-rep-hunter-abell/",
               "https://ballotpedia.org/Hunter_Abell"]),
    ]),

    # ---------------- Gloria Mendoza (WA-14, State Rep) ----------------
    ("gloria-mendoza", "WA", "Representative", [
        claim("gm1", "gloria-mendoza", "family_child_sovereignty", 0, True,
              "Fought to protect Washington's voter-approved Initiative 2081 Parents' Bill of Rights, opposing both HB 1296 and SB 5181 — the dual 2025 Democrat bills that would have stripped parental rights to be notified about their children's health and educational status. Mendoza publicly highlighted the damage these bills would do to family sovereignty.",
              ["https://gloriamendoza.houserepublicans.wa.gov/2025/01/24/meet-rep-gloria-mendoza-your-new-14th-district-state-representative/",
               "https://ballotpedia.org/Gloria_Mendoza"]),
        claim("gm2", "gloria-mendoza", "economic_stewardship", 2, True,
              "Issued a joint statement condemning Governor Ferguson's 2025 budget for its 'significant tax increases' on Washingtonians and opposed the revenue package on the grounds that it burdens families and small businesses without restraining state spending. Mendoza consistently votes against new taxes and was a vocal critic of the 2025 Democrat majority budget.",
              ["https://gloriamendoza.houserepublicans.wa.gov/2025/05/23/tax-increase-statement/",
               "https://gloriamendoza.houserepublicans.wa.gov/2025/05/01/a-session-of-tax-increases-update-from-rep-gloria-mendoza/"]),
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
        print(f"  ✓ {m['name']:<30} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
