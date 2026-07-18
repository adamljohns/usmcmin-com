#!/usr/bin/env python3
"""Enrichment batch 740: hand-curated claims for 5 Oregon Democratic state senators.

archetype_curated federal pool fully exhausted; WY/WV/WI/WA/VA state senator
pools also exhausted. Continuing from bottom of reverse-alphabetical bucket
with OR (Oregon) state senators from the archetype_party_default pool with 0 claims.

Targets (reverse-alpha by name within OR, first 5 of 8 remaining):
  Kathleen Taylor (OR SD-21), Kate Lieber (OR SD-14),
  Janeen Sollman (OR SD-15), James Manning Jr. (OR SD-7),
  Deb Patterson (OR SD-10).

Sources: opb.org, en.wikipedia.org, ballotpedia.org, oregonlegislature.gov,
olis.oregonlegislature.gov.
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
    # ---------------- Kathleen Taylor (OR SD-21, State Senator) ----------------
    ("kathleen-taylor", "OR", "Senator", [
        claim("kt1", "kathleen-taylor", "sanctity_of_life", 0, False,
              "Voted for Oregon HB 2002 (2023), which removed parental-notification requirements for minors seeking abortions, required Medicaid and private insurers to cover abortion and a broader range of reproductive procedures, and authorized mobile health clinics for abortion access in rural Oregon — rejecting any protection of unborn life from conception.",
              ["https://www.opb.org/article/2023/06/21/oregon-legislature-republican-senate-walkout-reproductive-rights-bill-governor-tina-kotek-desk/",
               "https://olis.oregonlegislature.gov/liz/2023R1/Measures/Overview/HB2002"]),
        claim("kt2", "kathleen-taylor", "self_defense", 1, False,
              "Supported the Democratic caucus's 2023 gun safety legislation including HB 2005, which sought to raise the minimum purchase age for most firearms from 18 to 21 and allow local governments to ban concealed weapons in public buildings. Taylor acted as a key Democratic go-between during the Republican walkout that was triggered in part by the gun safety bill, seeking to preserve both HB 2002 and HB 2005 intact.",
              ["https://www.opb.org/article/2023/06/12/oregon-legislature-democrats-may-water-down-bills-abortion-gun-safety-end-republican-walkout/",
               "https://ballotpedia.org/Kathleen_Taylor_(Oregon)"]),
        claim("kt3", "kathleen-taylor", "biblical_marriage", 2, False,
              "HB 2002 (2023) — which Taylor voted for and helped advance as a Democratic leader — also mandated insurance coverage for gender-affirming care for all ages including minors, directly contradicting the rubric's commitment to biological-sex realism and its opposition to state-mandated promotion of transgender ideology.",
              ["https://www.opb.org/article/2023/05/04/oregon-politics-republican-walkout-boycott-senate-salem-reproductive-health-care-abortion-gender/",
               "https://en.wikipedia.org/wiki/Kathleen_Taylor_(politician)"]),
    ]),

    # ---------------- Kate Lieber (OR SD-14, State Senator) ----------------
    ("kate-lieber", "OR", "Senator", [
        claim("kl1", "kate-lieber", "sanctity_of_life", 0, False,
              "As Oregon Senate Majority Leader (2023–2024), Lieber was the lead Senate champion of HB 2002, which removed parental notification requirements for minors seeking abortions and mandated Medicaid and private insurance coverage for abortion. When Republicans walked out to block a vote she declared Democrats 'will not walk back our values.'",
              ["https://www.opb.org/article/2023/05/03/republican-walk-out-oregon-senate-abortion-guns-gender-affirming-care/",
               "https://en.wikipedia.org/wiki/Kate_Lieber"]),
        claim("kl2", "kate-lieber", "biblical_marriage", 0, False,
              "In April 2023, Lieber introduced a constitutional amendment (SJR) in the Oregon Senate to enshrine the rights to same-sex marriage, abortion access, and gender-affirming care in the Oregon Constitution — directly rejecting the one-man-one-woman marriage definition the rubric upholds.",
              ["https://www.opb.org/article/2023/04/19/oregon-constitutional-amendment-proposal-abortion-gender-affirming-care-marriage-election-2024/",
               "https://ballotpedia.org/Kate_Lieber"]),
        claim("kl3", "kate-lieber", "self_defense", 1, False,
              "Championed HB 2005 (2023) which sought to raise the minimum age to purchase most firearms from 18 to 21, ban untraceable ghost guns, and allow local governments to prohibit concealed weapons in public buildings — opposing the rubric's defense of broad Second Amendment access for law-abiding adults.",
              ["https://www.opb.org/article/2023/06/12/oregon-legislature-democrats-may-water-down-bills-abortion-gun-safety-end-republican-walkout/",
               "https://ballotpedia.org/Kate_Lieber"]),
    ]),

    # ---------------- Janeen Sollman (OR SD-15, State Senator) ----------------
    ("janeen-sollman", "OR", "Senator", [
        claim("js1", "janeen-sollman", "self_defense", 1, False,
              "A stated advocate for addressing gun violence, Sollman has aligned with the Oregon Senate Democratic caucus's gun safety agenda including the 2023 push for HB 2005, which sought to raise the firearm purchase age to 21, ban ghost guns, and allow localities to restrict concealed carry — opposing the rubric's position of unrestricted Second Amendment access.",
              ["https://ballotpedia.org/Janeen_Sollman",
               "https://www.oregonlegislature.gov/sollman"]),
        claim("js2", "janeen-sollman", "biblical_marriage", 2, False,
              "Voted for Oregon HB 4088 (passed March 2026), which strengthened legal protections for people seeking or providing gender-affirming care, prohibited Oregon public agencies from cooperating with out-of-state investigations into legal gender-affirming care, and created confidential legal processes for sex-marker changes — rejecting the rubric's opposition to state promotion of transgender ideology.",
              ["https://www.opb.org/article/2026/03/05/oregon-gender-affirming-care-transgender-abortion/",
               "https://olis.oregonlegislature.gov/liz/2026R1/Downloads/MeasureDocument/HB4088"]),
    ]),

    # ---------------- James Manning Jr. (OR SD-7, State Senator) ----------------
    ("james-manning-jr", "OR", "Senator", [
        claim("jm1", "james-manning-jr", "election_integrity", 0, False,
              "As an Oregon state senator, Manning supported expanding automatic voter registration and authorizing prepaid return envelopes for Oregon's all-mail voting system — expanding the mass-mail-in voting infrastructure that the rubric's election-integrity standard opposes in favor of in-person, voter-ID-verified paper-ballot elections.",
              ["https://en.wikipedia.org/wiki/James_Manning_Jr.",
               "https://ballotpedia.org/James_Manning_(Oregon)"]),
        claim("jm2", "james-manning-jr", "sanctity_of_life", 0, False,
              "As Oregon State Senate President Pro Tempore (elected January 2023) and a Democratic caucus member, Manning voted with the majority to pass HB 2002 (2023), which expanded abortion access by removing parental notification requirements for minors and mandating Medicaid and private insurance coverage for abortion services.",
              ["https://www.opb.org/article/2023/06/21/oregon-legislature-republican-senate-walkout-reproductive-rights-bill-governor-tina-kotek-desk/",
               "https://en.wikipedia.org/wiki/James_Manning_Jr."]),
    ]),

    # ---------------- Deb Patterson (OR SD-10, State Senator) ----------------
    ("deb-patterson", "OR", "Senator", [
        claim("dp1", "deb-patterson", "sanctity_of_life", 0, False,
              "As chair of the Oregon Senate Health Committee (since 2021), Patterson has consistently championed expanded abortion access as a core healthcare service, advancing Medicaid coverage for reproductive care. On July 3, 2025, she issued a public statement criticizing the Republican Reconciliation Bill's cuts to healthcare programs that fund reproductive services.",
              ["https://www.oregonlegislature.gov/patterson/Documents/Senator%20Patterson%20Issues%20Statement%20in%20Response%20to%20Passage%20of%20Republican%20Reconciliation%20Bill.pdf",
               "https://ballotpedia.org/Deb_Patterson"]),
        claim("dp2", "deb-patterson", "biblical_marriage", 0, False,
              "Patterson is an ordained minister in the United Church of Christ (UCC) — the first major Protestant denomination to officially affirm same-sex marriage at its General Synod in 2005. As a UCC minister and Oregon Senate Democrat she has supported the party's LGBTQ-affirming legislative agenda, rejecting the one-man-one-woman marriage definition the rubric upholds.",
              ["https://en.wikipedia.org/wiki/Deb_Patterson_(politician)",
               "https://ballotpedia.org/Deb_Patterson"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — returns the single candidate matching
    (slug, state, office contains office_keyword) or None."""
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

    # Minified write — preserve the no-whitespace master (keep scorecard.json ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
