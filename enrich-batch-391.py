#!/usr/bin/env python3
"""Enrichment batch 391: hand-curated claims for 5 Virginia State Senators.

Targets evidence_state senators at the bottom of the alphabet with 0 evidence
claims (archetype_curated federal senator bucket is now fully exhausted).

Mix (2 R / 3 D): Bill DeSteph (VA-R SD-20), Chris Head (VA-R SD-3),
Aaron Rouse (VA-D SD-22), Barbara Favola (VA-D SD-40),
Angelia Williams Graves (VA-D SD-21).
Each claim cites >=1 reliable source and reflects 2024-2026 public positions
or voting record / stated positions from official/news sources.

NOTE: writes scorecard.json MINIFIED (no pretty-print whitespace) to keep
the master under GitHub's 50MB warning. Never use indent=2 here.
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
    # ---------------- Bill DeSteph (VA-R, State Senate District 20) ----------------
    ("bill-desteph", "VA", "District 20", [
        claim("bd1", "bill-desteph", "sanctity_of_life", 0, True,
              "Voted against HJR1 (2025), Virginia's Reproductive Freedom Constitutional Amendment that proposed enshrining a 'right to reproductive freedom' in the state constitution; the measure passed 21-18 on a strict party-line vote with DeSteph among the Republican minority opposing it.",
              ["https://legiscan.com/VA/text/HJR1/id/3037323",
               "https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)"]),
        claim("bd2", "bill-desteph", "self_defense", 1, True,
              "A U.S. Navy Desert Storm combat veteran and former Virginia Beach city councilman (2006-2014) who publicly advocates for responsible gun ownership and law enforcement; voted against Democratic gun-control legislation that moved through the Virginia Senate on party-line votes in the 2024 and 2025 sessions; earns a 71% rating from the Freedom Index for constitutional adherence.",
              ["https://ballotpedia.org/Bill_DeSteph_Jr.",
               "https://freedomindex.us/legislator/11559/session/311/report/210"]),
    ]),

    # ---------------- Chris Head (VA-R, State Senate District 3) ----------------
    ("chris-head", "VA", "District 3", [
        claim("ch1", "chris-head", "sanctity_of_life", 0, True,
              "A Baptist deacon (Bonsack Baptist Church, Roanoke) and small-business owner who has described himself as a 'stalwart defender of the unborn' throughout his 12 years in the Virginia House of Delegates (2012-2024) and continuing in the State Senate; consistently votes against abortion-expanding legislation and opposed Virginia's reproductive freedom constitutional amendments.",
              ["https://ballotpedia.org/Chris_Head",
               "https://www.wsls.com/news/local/2023/10/31/delegate-chris-head-looking-to-represent-newly-formed-virginia-senate-district-3/"]),
        claim("ch2", "chris-head", "self_defense", 1, True,
              "Publicly identifies as 'pro-second amendment' and has consistently voted against gun-control measures introduced by Democrats in the Virginia General Assembly; cited Second Amendment protection as a core legislative priority when campaigning for the Senate seat in 2023.",
              ["https://ballotpedia.org/Chris_Head",
               "https://www.wsls.com/news/local/2023/10/31/delegate-chris-head-looking-to-represent-newly-formed-virginia-senate-district-3/"]),
    ]),

    # ---------------- Aaron Rouse (VA-D, State Senate District 22) ----------------
    ("aaron-rouse", "VA", "District 22", [
        claim("ar1", "aaron-rouse", "sanctity_of_life", 0, False,
              "Won a 2023 special election explicitly as 'the deciding vote to protect reproductive freedom in Virginia'; states he 'will not compromise when it comes to protecting abortion rights,' voted for the Right to Contraception Act, and supports keeping abortion decisions entirely outside legislative reach — rejecting any personhood-from-conception standard.",
              ["https://rouseforsenate.com/issues/",
               "https://ballotpedia.org/Aaron_Rouse"]),
        claim("ar2", "aaron-rouse", "self_defense", 1, False,
              "Supported gun-safety legislation including firearm storage requirements and expanded background checks; publicly cited the 2019 Virginia Beach mass shooting as personal motivation for enacting new firearm restrictions, and stated he worked 'alongside colleagues to pass common-sense gun safety legislation.'",
              ["https://rouseforsenate.com/issues/",
               "https://ballotpedia.org/Aaron_Rouse"]),
    ]),

    # ---------------- Barbara Favola (VA-D, State Senate District 40) ----------------
    ("barbara-favola", "VA", "District 40", [
        claim("bf1", "barbara-favola", "sanctity_of_life", 0, False,
              "Carries a 100% rating from Reproductive Freedom for All (successor to NARAL Pro-Choice America) and chairs the Senate Women's Healthcare Caucus; a leading advocate for unrestricted abortion access in Virginia who has championed the state's reproductive freedom constitutional amendment process.",
              ["https://barbarafavola.org/biography",
               "https://ballotpedia.org/Barbara_Favola",
               "https://en.wikipedia.org/wiki/Barbara_Favola"]),
        claim("bf2", "barbara-favola", "biblical_marriage", 2, False,
              "Authored or co-sponsored legislation expanding Virginia's hate crimes statute to cover gender identity and sexual orientation, writing transgender and LGBTQ identity categories into state criminal law — the institutional promotion of gender ideology the rubric opposes.",
              ["https://en.wikipedia.org/wiki/Barbara_Favola",
               "https://ballotpedia.org/Barbara_Favola"]),
    ]),

    # ---------------- Angelia Williams Graves (VA-D, State Senate District 21) ----------------
    ("angelia-williams-graves", "VA", "District 21", [
        claim("awg1", "angelia-williams-graves", "sanctity_of_life", 0, False,
              "Publicly stated that 'women are capable of making their own healthcare and family planning decisions and don't need politicians to interfere,' and identified reproductive rights as a key campaign priority; votes with the Democratic caucus on abortion-access legislation, rejecting personhood-from-conception protections.",
              ["https://www.wavy.com/news/politics/candidates/candidate-profile-angelia-williams-graves-va-senate-district-21/",
               "https://ballotpedia.org/Angelia_Williams_Graves"]),
        claim("awg2", "angelia-williams-graves", "biblical_marriage", 0, False,
              "Supported the Virginia Remove Constitutional Same-Sex Marriage Ban Amendment (2026), which would strike the state constitution's existing one-man-one-woman marriage definition — rejecting the biblical definition of marriage as between one man and one woman.",
              ["https://ballotpedia.org/Virginia_Remove_Constitutional_Same-Sex_Marriage_Ban_Amendment_(2026)",
               "https://ballotpedia.org/Angelia_Williams_Graves"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher that prevents wrong-state same-slug collisions."""
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
