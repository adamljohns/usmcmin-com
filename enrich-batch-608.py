#!/usr/bin/env python3
"""Enrichment batch 608: 5 sitting U.S. Senators from NM/NV/MN — 13 claims.

Targets senators with 6 existing claims, adding 2-3 new claims each in
distinct rubric categories (election_integrity, christian_liberty,
foreign_policy_restraint, industry_capture).

Senators (all from bottom of alphabet — NM/NV/MN):
  Tina Smith (MN-D), Catherine Cortez Masto (NV-D), Jacky Rosen (NV-D),
  Ben Ray Luján (NM-D), Martin Heinrich (NM-D).

Sources: congress.gov, senate.gov, govtrack.us, opensecrets.org, fec.gov,
         official press releases, FEC disclosures.

NOTE: writes scorecard.json MINIFIED to keep master under GitHub's 50MB limit.
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
    # ------------ Tina Smith (MN-D, US Senator) ------------
    ("tina-smith", "MN", "Senator", [
        claim("ts608a", "tina-smith", "election_integrity", 0, False,
              "Co-sponsored S.1, the For the People Act of 2021 (117th Congress), and voted "
              "YES on cloture (Senate Roll Call Vote #358, June 22, 2021, 50–50 party-line) — "
              "legislation that would have banned strict photo voter-ID requirements, mandated "
              "automatic voter registration, and massively expanded vote-by-mail for federal "
              "elections. She also voted NO on the SAVE America Act (H.R.22, 119th Congress, "
              "motion to proceed March 17, 2026, failed 51–48) which would require documentary "
              "proof of citizenship to register to vote — directly opposing the rubric's "
              "voter-ID and election-integrity standards.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/1/cosponsors",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1171/vote_117_1_00358.htm",
               "https://www.congress.gov/bill/119th-congress/house-bill/22"]),
        claim("ts608b", "tina-smith", "christian_liberty", 0, False,
              "Co-sponsored the Equality Act (S.5, 118th Congress, June 2023, via Sen. Merkley "
              "with 50 Senate cosponsors), which adds sexual orientation and gender identity as "
              "protected classes across federal civil-rights law and explicitly states that the "
              "Religious Freedom Restoration Act of 1993 'shall not provide a claim concerning, "
              "or a defense to a claim under' any of its covered titles — stripping RFRA "
              "protections from religious employers, healthcare providers, schools, and adoption "
              "agencies with conscience objections.",
              ["https://www.congress.gov/bill/118th-congress/senate-bill/5/all-info",
               "https://www.merkley.senate.gov/senator-merkley-reintroduces-the-equality-act/"]),
    ]),

    # ------------ Catherine Cortez Masto (NV-D, US Senator) ------------
    ("catherine-cortez-masto", "NV", "Senator", [
        claim("ccm608a", "catherine-cortez-masto", "election_integrity", 0, False,
              "Co-introduced S.1, the For the People Act of 2021, and voted to advance it on "
              "cloture (Senate Roll Call Vote #358, June 22, 2021, 50–50 party-line) — "
              "legislation that would ban photo voter-ID requirements for federal elections and "
              "mandate nationwide automatic voter registration and mass mail-in voting. In 2026 "
              "she delivered a Senate floor speech calling the SAVE Act (H.R.22, requiring "
              "proof of citizenship for voter registration) 'more punitive than any voter "
              "suppression law that I have seen,' voted NO on its motion to proceed "
              "(March 17, 2026, 51–48), and signed a Democratic caucus letter demanding the "
              "USPS abandon plans implementing Trump's executive order restricting vote-by-mail "
              "(June 24, 2026).",
              ["https://www.cortezmasto.senate.gov/news/press-releases/cortez-masto-senate-democrats-introduce-sweeping-package-of-ethics-and-voting-rights-reforms/",
               "https://www.cortezmasto.senate.gov/news/press-releases/on-the-senate-floor-cortez-masto-exposes-republican-save-america-act-as-a-voter-suppression-bill/",
               "https://www.senate.gov/legislative/LIS/roll_call_votes/vote1171/vote_117_1_00358.htm"]),
        claim("ccm608b", "catherine-cortez-masto", "christian_liberty", 0, False,
              "Three-time co-sponsor of the Equality Act (2017, 2019, and S.5 in 118th Congress "
              "June 2023), which adds LGBTQ+ protections across federal civil-rights law with an "
              "explicit provision barring the Religious Freedom Restoration Act as a legal "
              "defense — removing RFRA protections for religious employers, hospitals, schools, "
              "and service providers. She also co-sponsored S.2752, the Do No Harm Act "
              "(117th Congress, Sept. 2021) and S.894 (119th Congress, 2025), which directly "
              "amend RFRA to prohibit its use in employment, benefits, and healthcare contexts.",
              ["https://www.cortezmasto.senate.gov/news/press-releases/cortez-masto-cosponsors-equality-act/",
               "https://www.congress.gov/bill/117th-congress/senate-bill/2752/cosponsors",
               "https://www.congress.gov/bill/119th-congress/senate-bill/894/cosponsors"]),
    ]),

    # ------------ Jacky Rosen (NV-D, US Senator) ------------
    ("jacky-rosen", "NV", "Senator", [
        claim("jr608a", "jacky-rosen", "foreign_policy_restraint", 3, False,
              "Rosen is one of the U.S. Senate's largest recipients of pro-Israel lobby money: "
              "AIPAC's United Democracy Project bundled over $1.1 million in contributions on "
              "her behalf (FEC disclosures, disclosed via OpenSecrets and ReadSludge, Apr 2024). "
              "She leveraged that support in Nov. 2024 delivering a floor speech opposing three "
              "Sanders resolutions (S.J.Res. 111, 113, 115) that would have restricted U.S. "
              "arms sales to Israel, and in Apr. 2026 was among only seven Democrats to vote "
              "against resolutions blocking sales of bulldozers and 1,000-lb bombs to Israel "
              "(Senate Roll Call Vote #80, 119th Congress). The rubric identifies AIPAC/foreign-"
              "linked PAC money as a marker of captured foreign-policy posture.",
              ["https://readsludge.com/2024/04/19/aipac-funded-senator-pushes-antisemitism-definition-that-could-silence-critics-of-israel/",
               "https://www.opensecrets.org/industries/summary?cycle=All&ind=Q05&recipdetail=S"]),
        claim("jr608b", "jacky-rosen", "industry_capture", 0, False,
              "Rosen's 2022 financial disclosures revealed she held up to approximately $300,000 "
              "in pharmaceutical company shares — including up to $50,000 each in Pfizer and "
              "Novartis — while publicly championing lower drug prices. She received "
              "pharmaceutical-sector PAC contributions in her Senate campaigns and introduced "
              "industry-friendly 'nonprofit generic' drug legislation (June 2021) rather than "
              "measures repealing pharma liability shields or mandating full pricing audits of "
              "federally contracted drug manufacturers.",
              ["https://freebeacon.com/democrats/jacky-rosen-pledges-to-combat-overpriced-drugs-as-she-rakes-in-cash-from-big-pharma/",
               "https://www.opensecrets.org/members-of-congress/jacky-rosen/industries"]),
        claim("jr608c", "jacky-rosen", "christian_liberty", 0, False,
              "Co-sponsored the Equality Act (S.393, 117th Congress, Feb. 2021), which "
              "explicitly provides that the Religious Freedom Restoration Act 'shall not provide "
              "a claim concerning, or a defense to a claim under' any of its covered titles — "
              "stripping RFRA protections from religious employers, healthcare providers, and "
              "faith-based organizations in employment, housing, and public accommodations. "
              "She also co-sponsored the Do No Harm Act, which would further restrict RFRA "
              "applicability, and receives a perfect 100% score from the Human Rights Campaign.",
              ["https://www.rosen.senate.gov/2021/02/22/rosen-co-sponsors-the-equality-act/",
               "https://www.congress.gov/bill/117th-congress/senate-bill/393/text"]),
    ]),

    # ------------ Ben Ray Luján (NM-D, US Senator) ------------
    ("ben-ray-lujan", "NM", "Senator", [
        claim("brl608a", "ben-ray-lujan", "election_integrity", 0, False,
              "Co-introduced the Freedom to Vote Act (S.2747, 117th Congress) alongside Sen. "
              "Heinrich, which would mandate no-excuse nationwide vote-by-mail, automatic and "
              "same-day voter registration, and allow any voter lacking photo ID to cast a "
              "ballot by signed sworn statement — overriding state voter-ID laws. He also "
              "co-sponsored the For the People Act (S.1) and publicly characterized the "
              "SAVE Act (H.R.22, requiring proof of citizenship for voter registration) as "
              "voter suppression.",
              ["https://www.lujan.senate.gov/newsroom/press-releases/heinrich-lujan-introduce-legislation-to-protect-the-freedom-to-vote-and-strengthen-our-democracy/",
               "https://www.govtrack.us/congress/bills/117/s2747"]),
        claim("brl608b", "ben-ray-lujan", "industry_capture", 0, False,
              "OpenSecrets records show the Pharmaceuticals/Health Products sector ranks among "
              "Luján's top industry donors across his congressional career, with PAC "
              "contributions in both his 2022 Senate race and 2024 cycle. He has not introduced "
              "or co-sponsored legislation to repeal pharmaceutical manufacturers' liability "
              "shields (including the 1986 NCVIA and PREP Act protections) or to mandate "
              "independent pricing audits of federally contracted drug companies.",
              ["https://www.opensecrets.org/members-of-congress/ben-ray-lujan/industries?cid=N00029562",
               "https://www.opensecrets.org/members-of-congress/ben-ray-lujan/pacs?cat=H04&cid=N00029562"]),
        claim("brl608c", "ben-ray-lujan", "christian_liberty", 0, False,
              "Co-sponsored the Equality Act (S.393, 117th Congress) as of Feb. 23, 2021 — "
              "legislation that explicitly bars the Religious Freedom Restoration Act from "
              "providing any claim or defense against its anti-discrimination mandates in "
              "employment, housing, education, and public accommodations. He also backed the "
              "Do No Harm Act, which would narrow RFRA's applicability to prevent its use by "
              "religious employers, healthcare providers, and service organizations with "
              "conscience objections.",
              ["https://www.congress.gov/bill/117th-congress/senate-bill/393/cosponsors",
               "https://www.hrc.org/news/hrc-endorses-rep-ben-ray-lujan-for-u-s-senate"]),
    ]),

    # ------------ Martin Heinrich (NM-D, US Senator) ------------
    ("martin-heinrich", "NM", "Senator", [
        claim("mh608a", "martin-heinrich", "election_integrity", 0, False,
              "Co-introduced the Freedom to Vote Act (S.2747, 117th Congress) with Sen. Luján, "
              "mandating national no-excuse vote-by-mail and permitting voters lacking photo ID "
              "to vote by sworn affidavit. He issued a formal press release calling the SAVE "
              "Act (H.R.22, 119th Congress — proof-of-citizenship for voter registration) 'one "
              "of the most extreme voter suppression bills in recent history,' and voted against "
              "the SAVE Act when it came to the Senate as a reconciliation amendment in "
              "June 2026 (failed 48-50).",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/heinrich-save-act-is-one-of-the-most-extreme-voter-suppression-bills-in-recent-history",
               "https://www.lujan.senate.gov/newsroom/press-releases/heinrich-lujan-introduce-legislation-to-protect-the-freedom-to-vote-and-strengthen-our-democracy/"]),
        claim("mh608b", "martin-heinrich", "industry_capture", 4, False,
              "As a long-serving member of the Senate Armed Services Committee and Ranking "
              "Member of the Strategic Forces Subcommittee, Heinrich has consistently voted for "
              "annual NDAAs increasing Pentagon budgets past $800 billion without requiring "
              "binding audit-completion standards. His own press releases boast that he "
              "delivered over $1.5 billion in military construction to New Mexico installations "
              "and doubled budgets for Sandia and Los Alamos national laboratories — touting "
              "'wins for the defense industry' rather than independent oversight or "
              "defense-contractor audit accountability.",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/annual-defense-bill-passes-senate-heinrich-announces-significant-gains-for-national-labs-military-installations-defense-industry-and-border-security",
               "https://www.heinrich.senate.gov/priorities/issues/military-and-national-security"]),
        claim("mh608c", "martin-heinrich", "christian_liberty", 0, False,
              "Has been a consistent co-sponsor and public advocate for the Equality Act across "
              "multiple Congresses (H.R.5, 116th; S.393, 117th), legislation that explicitly "
              "forbids the Religious Freedom Restoration Act from providing a claim or defense "
              "against its mandates — meaning faith-based employers, schools, and service "
              "organizations cannot invoke RFRA to protect employees or providers acting on "
              "religious conscience. He also co-sponsored the Do No Harm Act, which would "
              "amend RFRA to strip its applicability in employment, healthcare, and "
              "federal-contract settings.",
              ["https://www.heinrich.senate.gov/newsroom/press-releases/udall-heinrich-call-for-a-vote-on-equality-act-to-a-vote",
               "https://www.congress.gov/bill/117th-congress/senate-bill/393/cosponsors"]),
    ]),
]


def find_candidate(scorecard, slug, state, office_keyword):
    """State-aware matcher — prevents wrong-state slug collisions."""
    for c in scorecard["candidates"]:
        if c.get("slug") != slug:
            continue
        if (c.get("state") or "").upper() != state.upper():
            continue
        if office_keyword.lower() not in (c.get("office") or "").lower():
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

    # Minified write — preserve no-whitespace master (keeps file ~35-36MB).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
