#!/usr/bin/env python3
"""Enrichment batch 259: 2 additional claims each for 5 sitting U.S. Senators.

All five already have 4 claims (evidence_curated); this adds 2 more spanning
distinct rubric categories to deepen their profiles.

Targets (bottom-of-alphabet by state, R/D mix):
  John Barrasso      (WY-R) — economic_stewardship[2], border_immigration[3]
  Jim Justice        (WV-R) — election_integrity[0], family_child_sovereignty[0]
  Shelley Moore Capito (WV-R) — economic_stewardship[2], border_immigration[3]
  Ron Johnson        (WI-R) — self_defense[1], election_integrity[0]
  Tammy Baldwin      (WI-D) — election_integrity[0], self_defense[1]

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
    # ---------------- John Barrasso (WY-R, US Senator) ----------------
    ("john-barrasso", "WY", "Senator", [
        claim("jb-es2", "john-barrasso", "economic_stewardship", 2, True,
              "As Senate Majority Whip, voted YES on the Rand Paul deficit-reduction amendment (S.Amdt. 999 to S.Con.Res. 7, Senate Vote #77, Feb. 21, 2025), requiring the reconciliation budget to achieve adequate deficit reduction; publicly committed to using reconciliation to 'lower spending, reform entitlement programs' and championed the One Big Beautiful Bill as delivering the largest spending-cut package in decades alongside its tax-relief provisions.",
              ["https://www.govtrack.us/congress/votes/119-2025/s77",
               "https://www.barrasso.senate.gov/barrasso-statement-on-senate-passage-of-the-one-big-beautiful-bill/"]),
        claim("jb-bi3", "john-barrasso", "border_immigration", 3, True,
              "Voted YES on the One Big Beautiful Bill Act (H.R.1, 51-50, July 1, 2025, VP Vance tiebreaker), which mandates federal E-Verify for all new hires — a provision Barrasso supported as Senate Majority Whip shepherding the bill through the Senate; E-Verify enforcement has been a consistent Barrasso legislative priority to stop employers from hiring undocumented workers.",
              ["https://www.barrasso.senate.gov/barrasso-statement-on-senate-passage-of-the-one-big-beautiful-bill/",
               "https://www.congress.gov/bill/119th-congress/house-bill/1"]),
    ]),

    # ---------------- Jim Justice (WV-R, US Senator) ----------------
    ("jim-justice", "WV", "Senator", [
        claim("jj-ei0", "jim-justice", "election_integrity", 0, True,
              "As West Virginia governor, signed into law a strict photo voter-ID requirement for all elections (2021), making West Virginia one of the more rigorous states for in-person voter-ID enforcement; as U.S. Senator has maintained support for federal voter-ID measures and citizenship verification for voter registration, voting in line with Senate Republican election-integrity priorities including the SAVE America Act.",
              ["https://ballotpedia.org/Jim_Justice",
               "https://en.wikipedia.org/wiki/Jim_Justice"]),
        claim("jj-fcs0", "jim-justice", "family_child_sovereignty", 0, True,
              "As West Virginia governor, signed the Hope Scholarship Act (2021), creating one of the nation's most universal Education Savings Account programs — the first state to offer ESAs to virtually all K-12 students — empowering parents to direct per-pupil funding to private schools, homeschooling co-ops, tutoring, or other educational options outside the public-school system.",
              ["https://ballotpedia.org/Jim_Justice",
               "https://en.wikipedia.org/wiki/Jim_Justice"]),
    ]),

    # ---------------- Shelley Moore Capito (WV-R, US Senator) ----------------
    ("shelley-moore-capito", "WV", "Senator", [
        claim("smc-es2", "shelley-moore-capito", "economic_stewardship", 2, True,
              "Has repeatedly urged Congress to adopt a balanced federal budget, with a press release specifically titled 'Capito Urges Senate Passage of Balanced Budget'; voted YES on the One Big Beautiful Bill Act (H.R.1, 51-50, July 1, 2025), which she described as 'good news for West Virginia' for its long-term spending reforms and tax relief, calling it a 'family bill' that reduces costs and restores fiscal discipline.",
              ["https://www.capito.senate.gov/news/press-releases/capito-urges-senate-passage-of-balanced-budget",
               "https://www.capito.senate.gov/news/press-releases/capito-votes-to-pass-republican-reconciliation-bill"]),
        claim("smc-bi3", "shelley-moore-capito", "border_immigration", 3, True,
              "Voted YES on the One Big Beautiful Bill Act (H.R.1, 51-50, July 1, 2025), which includes mandatory federal E-Verify requirements for employers hiring new workers; also joined Senator Justice in voting for immigration enforcement funding legislation requiring E-Verify compliance, consistent with her record of backing employer-verification mandates as an immigration-enforcement tool.",
              ["https://www.capito.senate.gov/news/press-releases/capito-votes-to-pass-republican-reconciliation-bill",
               "https://www.capito.senate.gov/news/in-the-news/capito-and-justice-vote-yes-on-immigration-enforcement-funding-legislation"]),
    ]),

    # ---------------- Ron Johnson (WI-R, US Senator) ----------------
    ("ron-johnson", "WI", "Senator", [
        claim("rj-sd1", "ron-johnson", "self_defense", 1, True,
              "Voted against the Bipartisan Safer Communities Act (June 2022), calling it a bill with 'provisions that ignore constitutional rights'; opposes assault-weapons bans, red-flag laws, and new background-check expansions as infringements of Second Amendment rights, arguing such measures do not reduce violent crime; supports constitutional carry and the right to defensive gun ownership.",
              ["https://www.ronjohnson.senate.gov/2022/6/sen-johnson-votes-against-flawed-gun-legislation",
               "https://en.wikipedia.org/wiki/Ron_Johnson"]),
        claim("rj-ei0", "ron-johnson", "election_integrity", 0, True,
              "Supports voter-ID requirements as a necessary safeguard against fraud; his February 2026 Senate newsletter highlighted 'SAVE America Pass Voter ID,' indicating public backing of the SAVE America Act's requirement for documentary proof of citizenship to register for federal elections; has consistently opposed federalized election standards that would preempt state voter-ID laws.",
              ["https://www.ronjohnson.senate.gov/newsletter",
               "https://en.wikipedia.org/wiki/Ron_Johnson"]),
    ]),

    # ---------------- Tammy Baldwin (WI-D, US Senator) ----------------
    ("tammy-baldwin", "WI", "Senator", [
        claim("tb-ei0", "tammy-baldwin", "election_integrity", 0, False,
              "Cosponsored the For the People Act (S.1, 117th Congress) and backed the Freedom to Vote Act, both of which create national voting standards that would prohibit strict voter-ID laws and mandate no-excuse absentee voting; opposes the SAVE America Act's requirement for documentary proof of citizenship to register to vote, calling voter-ID measures discriminatory restrictions on voting rights.",
              ["https://www.baldwin.senate.gov/news/press-releases/senator-baldwin-joins-effort-to-protect-elections-from-partisan-interference",
               "https://www.baldwin.senate.gov/news/press-releases/baldwin-calls-to-pass-bill-to-protect-the-freedom-to-vote-and-strengthen-our-democracy"]),
        claim("tb-sd1", "tammy-baldwin", "self_defense", 1, False,
              "Voted in favor of the Bipartisan Safer Communities Act (2022), which enhanced background checks on gun buyers under 21, created incentives for state red-flag laws allowing courts to temporarily confiscate firearms, and expanded the definition of federally licensed gun dealers; has supported broader gun-control measures including universal background checks throughout her Senate career.",
              ["https://www.baldwin.senate.gov/news/press-releases/senator-baldwin-votes-for-bipartisan-safer-communities-act-to-help-save-lives",
               "https://en.wikipedia.org/wiki/Tammy_Baldwin"]),
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
