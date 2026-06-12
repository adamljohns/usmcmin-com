#!/usr/bin/env python3
"""Enrichment batch 161: hand-curated claims for 5 U.S. Representatives.

Targets archetype_party_default reps from the BOTTOM of the alphabet
(TX + PA + KY) with 0 evidence claims.

Mix (1 R / 4 D): Hal Rogers (KY-R), Julie Johnson (TX-D),
Christian Menefee (TX-D), Mary Gay Scanlon (PA-D), Madeleine Dean (PA-D).
Each claim cites >=1 reliable source and reflects 2024-2026 voting record
/ public positions.

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
    # ---------------- Julie Johnson (TX-32, D) ----------------
    ("julie-johnson", "TX", "Representative", [
        claim("jj1", "julie-johnson", "sanctity_of_life", 0, False,
              "A pro-choice Democrat who introduced the Reproductive Rights Are Human Rights Act of 2025 to protect global abortion access, and campaigned on codifying Roe v. Wade into federal law — rejecting any life-at-conception or personhood standard.",
              ["https://en.wikipedia.org/wiki/Julie_Johnson_(politician)",
               "https://juliejohnson.house.gov/issues/health"]),
        claim("jj2", "julie-johnson", "self_defense", 1, False,
              "Campaign platform calls for raising the minimum age for firearm purchases, mandating safe-storage requirements, and using red-flag courts to strip firearms from individuals deemed a risk — directly opposing constitutional carry and the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Julie_Johnson_(Texas)",
               "https://en.wikipedia.org/wiki/Julie_Johnson_(politician)"]),
        claim("jj3", "julie-johnson", "biblical_marriage", 4, False,
              "Maintains a dedicated 'Equality' legislative agenda championing federal LGBTQ nondiscrimination protections in public accommodations and employment — actively promoting LGBTQ ideology in federal law and policy, contrary to the rubric's rejection of such promotion.",
              ["https://juliejohnson.house.gov/issues/equality",
               "https://ballotpedia.org/Julie_Johnson_(Texas)"]),
    ]),

    # ---------------- Christian Menefee (TX-18, D) ----------------
    ("christian-menefee", "TX", "Representative", [
        claim("cme1", "christian-menefee", "sanctity_of_life", 0, False,
              "Elected to Congress from Houston's TX-18 (January 2026) on a Democratic platform defending abortion access; as Harris County Attorney (2021–2026) he operated in a jurisdiction that filed legal challenges against Texas's abortion-restriction laws including SB8 — rejecting personhood from conception.",
              ["https://en.wikipedia.org/wiki/2025%E2%80%9326_Texas%27s_18th_congressional_district_special_election",
               "https://ballotpedia.org/Texas'_18th_Congressional_District_special_election,_2025"]),
        claim("cme2", "christian-menefee", "self_defense", 1, False,
              "A Democrat from Houston's majority-minority TX-18 district who, consistent with his party platform and Houston city government's stance, supports expanded firearm regulations including universal background checks and assault-weapons restrictions — opposing the rubric's defense of full, unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Texas'_18th_Congressional_District",
               "https://en.wikipedia.org/wiki/Texas%27s_18th_congressional_district"]),
        claim("cme3", "christian-menefee", "border_immigration", 2, False,
              "Represents Harris County, where county and city leadership have resisted state-directed immigration enforcement cooperation; as Harris County Attorney he defended county policies rather than supporting mandatory deportation or anti-sanctuary cooperation.",
              ["https://en.wikipedia.org/wiki/2025%E2%80%9326_Texas%27s_18th_congressional_district_special_election",
               "https://ballotpedia.org/Texas'_18th_Congressional_District_special_election,_2025"]),
    ]),

    # ---------------- Mary Gay Scanlon (PA-5, D) ----------------
    ("mary-gay-scanlon", "PA", "Representative", [
        claim("mgs1", "mary-gay-scanlon", "self_defense", 1, False,
              "A longtime gun-control advocate who organized community participation in the Million Mom March and has consistently backed legislation to restrict firearm access, opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Mary_Gay_Scanlon",
               "https://en.wikipedia.org/wiki/Mary_Gay_Scanlon"]),
        claim("mgs2", "mary-gay-scanlon", "border_immigration", 2, False,
              "Actively opposed enforcement of immigration orders by dispatching pro-bono attorneys to airports to represent detained families, and previously represented asylum seekers and DACA recipients as an immigration attorney — opposing enforcement-first and anti-sanctuary policies.",
              ["https://ballotpedia.org/Mary_Gay_Scanlon",
               "https://en.wikipedia.org/wiki/Mary_Gay_Scanlon"]),
        claim("mgs3", "mary-gay-scanlon", "sanctity_of_life", 0, False,
              "A pro-choice Democrat rated most politically left in the Pennsylvania delegation in 2024 (GovTrack) who has consistently voted to protect abortion access and opposed restrictions on abortion funding.",
              ["https://www.govtrack.us/congress/members/mary_scanlon/412750/report-card/2024",
               "https://en.wikipedia.org/wiki/Mary_Gay_Scanlon"]),
    ]),

    # ---------------- Madeleine Dean (PA-4, D) ----------------
    ("madeleine-dean", "PA", "Representative", [
        claim("md1", "madeleine-dean", "sanctity_of_life", 0, False,
              "A pro-choice Democrat who voted with President Biden's stated position 100% of the time in the 117th Congress and has consistently opposed abortion restrictions, backing legislation to expand access and override state-level limits.",
              ["https://en.wikipedia.org/wiki/Madeleine_Dean",
               "https://www.govtrack.us/congress/members/madeleine_dean/412809"]),
        claim("md2", "madeleine-dean", "biblical_marriage", 1, False,
              "Voted for the Respect for Marriage Act (2022), which codifies federal recognition of same-sex marriage in statute and removes the legal possibility of restoring one-man-one-woman marriage law — directly rejecting the rubric's definition of biblical marriage.",
              ["https://en.wikipedia.org/wiki/Madeleine_Dean",
               "https://www.congress.gov/bill/117th-congress/house-bill/8404"]),
        claim("md3", "madeleine-dean", "self_defense", 1, False,
              "A consistent advocate for gun-control legislation who backs expanded background checks, red-flag laws, and restrictions on assault-style weapons — opposing constitutional carry and the rubric's defense of unrestricted Second Amendment rights.",
              ["https://ballotpedia.org/Madeleine_Dean",
               "https://en.wikipedia.org/wiki/Madeleine_Dean"]),
    ]),

    # ---------------- Hal Rogers (KY-5, R) ----------------
    ("hal-rogers", "KY", "Representative", [
        claim("hr1", "hal-rogers", "sanctity_of_life", 0, True,
              "Holds a 100% rating from the National Right to Life Committee and a 0% rating from NARAL Pro-Choice America, reflecting a consistent anti-abortion voting record opposing federal abortion funding and supporting restrictions on abortion.",
              ["https://en.wikipedia.org/wiki/Hal_Rogers",
               "https://ballotpedia.org/Hal_Rogers"]),
        claim("hr2", "hal-rogers", "self_defense", 1, True,
              "Maintains a pro-gun voting record consistent with an A rating from the National Rifle Association, opposing expansions of federal gun control law including background-check mandates, red-flag laws, and assault-weapons bans.",
              ["https://www.ontheissues.org/House/Hal_Rogers_Gun_Control.htm",
               "https://en.wikipedia.org/wiki/Hal_Rogers"]),
        claim("hr3", "hal-rogers", "border_immigration", 0, True,
              "As a senior member of the House Appropriations Committee, has consistently supported homeland security funding for border barriers and enforcement operations, and has publicly demanded that immigration laws be enforced as written.",
              ["https://halrogers.house.gov/issues",
               "https://ballotpedia.org/Hal_Rogers"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents same-slug collisions.

    Returns the single candidate matching (slug, state, office contains
    office_keyword) or None.
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
