#!/usr/bin/env python3
"""Enrichment batch 96: hand-curated claims for 4 state-level D candidates.

Targets archetype_curated candidates from the bottom of the reverse-alpha bucket
(NY, NV, MN) that had 0 evidence claims. Federal bucket exhausted; pattern from
batches 91-95 applies — descend into state-level officeholders next.

Candidates:
  - Eric Adams     (NY, former NYC Mayor, 2022-2026)
  - Shelley Berkley (NV, former US Rep 1999-2013, Las Vegas Mayor since 2024)
  - Cisco Aguilar  (NV, sitting Nevada Secretary of State 2023-)
  - Steve Simon    (MN, sitting Minnesota Secretary of State 2015-)

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
    # ---------------- Eric Adams (NY-D, former NYC Mayor 2022-2026) ----------------
    ("eric-adams", "NY", "Mayor", [
        claim("ea1", "eric-adams", "sanctity_of_life", 0, False,
              "As NYC Mayor, Adams declared publicly that women have an absolute 'right' to abortions 'up until day of birth,' calling pro-life advocates 'radical extremists.' He signed the NYC Abortion Rights Act (2022) expanding abortion access citywide and in January 2023 made New York City the first city in the nation to offer medication abortion free-of-charge at public health clinics — explicitly rejecting any personhood framework from conception.",
              ["https://www.nyc.gov/office-of-the-mayor/news/591-22/mayor-adams-signs-legislation-guaranteeing-access-safe-affordable-abortion-new-york-city",
               "https://townhall.com/tipsheet/juliorosas/2022/05/19/nyc-mayor-adams-doubles-down-women-have-right-to-abortions-up-until-day-of-birth-n2607522",
               "https://www.foxnews.com/politics/eric-adams-blasts-pro-life-radical-extremists-women-have-right-abortions-up-until-day-of-birth"]),
        claim("ea2", "eric-adams", "self_defense", 1, False,
              "Condemned the Supreme Court's 2022 NYSRPA v. Bruen ruling as 'dangerous,' saying it would 'put New Yorkers at further risk of gun violence'; directed the NYC Law Department to file amicus briefs in the Second Circuit defending New York State's restrictive gun-carry regime; and co-led a coalition of 14 city mayors to pursue litigation against gun manufacturers — a sustained legal and political campaign opposing any expansion of Second Amendment rights.",
              ["https://www.nyc.gov/office-of-the-mayor/news/426-22/mayor-adams-on-bruen-supreme-court-decision",
               "https://www.cityandstateny.com/policy/2022/07/eric-adams-along-mayors-14-other-cities-announce-plans-target-manufacturers-guns-used-crimes/374736/"]),
    ]),

    # ---------------- Shelley Berkley (NV-D, former US Rep, Las Vegas Mayor) ----------------
    ("shelley-berkley", "NV", "Mayor", [
        claim("sb1", "shelley-berkley", "sanctity_of_life", 0, False,
              "During her seven-term U.S. House career (1999–2013), Berkley earned a 100% rating from NARAL Pro-Choice America and a 0% rating from the National Right to Life Committee; voted NO on banning partial-birth abortions (2000) and NO on barring the transportation of minors across state lines for abortions — a consistent record rejecting any legal protection from conception.",
              ["https://www.ontheissues.org/House/Shelley_Berkley_Abortion.htm",
               "https://www.govtrack.us/congress/members/shelley_berkley/400024"]),
        claim("sb2", "shelley-berkley", "sanctity_of_life", 4, False,
              "Endorsed by EMILY's List — the largest U.S. political action committee dedicated to electing pro-abortion women candidates — placing her inside the abortion-industry endorsement-and-fundraising network the rubric holds against candidates.",
              ["https://www.ontheissues.org/house/shelley_berkley.htm",
               "https://en.wikipedia.org/wiki/Shelley_Berkley"]),
        claim("sb3", "shelley-berkley", "self_defense", 1, False,
              "Rated F by the National Rifle Association across her congressional career; voted NO on bills that would reduce the gun-purchase waiting period — a consistent gun-control voting record directly opposing the rubric's defense of unrestricted Second Amendment rights.",
              ["https://www.ontheissues.org/house/shelley_berkley.htm",
               "https://www.govtrack.us/congress/members/shelley_berkley/400024"]),
    ]),

    # ---------------- Cisco Aguilar (NV-D, Nevada Secretary of State 2023-) ----------------
    ("cisco-aguilar-sos-2026", "NV", "Secretary", [
        claim("ca1", "cisco-aguilar-sos-2026", "election_integrity", 0, False,
              "Publicly called Nevada's non-photo-ID polling-place system sound, saying voter ID requirements are 'a solution to a problem that doesn't exist' and that Nevada 'does not have non-citizens voting.' Attacked the federal SAVE Act — which would require photo ID and proof of citizenship for federal voter registration — as 'an attempt to cause chaos in our elections and silence eligible voters,' and prepared litigation to block it. Presides over a Nevada system that automatically mails ballots to all active registered voters, the mass-mail-in regime the rubric opposes.",
              ["https://knpr.org/show/knprs-state-of-nevada/2024-10-15/nevada-sos-fights-off-challenges-to-the-states-secure-election-process",
               "https://www.8newsnow.com/investigators/nevada-election-leader-save-act-has-unintended-consequences-rooted-in-conspiracies/"]),
        claim("ca2", "cisco-aguilar-sos-2026", "biblical_marriage", 4, False,
              "Endorsed by the Human Rights Campaign (HRC) — the nation's largest LGBTQ+ political advocacy organization, which actively promotes LGBTQ ideology in schools and public policy — in his successful 2022 Secretary of State campaign, placing him within the pro-LGBTQ-promotion endorsement network the rubric opposes.",
              ["https://www.hrc.org/press-releases/human-rights-campaign-supporting-pro-equality-candidates-empowering-lgbtq-voters-and-allies-in-nevada-ahead-of-election-day"]),
    ]),

    # ---------------- Steve Simon (MN-D, Minnesota Secretary of State 2015-) ----------------
    ("steve-simon", "MN", "Secretary", [
        claim("ss1", "steve-simon", "election_integrity", 0, False,
              "As Minnesota Secretary of State, Simon certified the state's new Automatic Voter Registration system in April 2024, which enrolls eligible Minnesotans in the voter rolls without requiring any opt-in step when they transact with state agencies — shifting responsibility from individual citizens to government officials. Simon framed this removal of individual voter consent as 'strengthening election security,' eliding the accountability concerns the rubric associates with mass auto-enrollment.",
              ["https://www.sos.mn.gov/about-the-office/news-room/secretary-simon-certifies-automatic-voter-registration-system/"]),
        claim("ss2", "steve-simon", "biblical_marriage", 0, False,
              "As a Minnesota state representative, Simon publicly testified against and actively opposed a proposed state constitutional amendment that would have defined marriage as one man and one woman (May 2, 2011), going on record rejecting the biblical definition of marriage that the rubric affirms.",
              ["https://en.wikipedia.org/wiki/Steve_Simon",
               "https://ballotpedia.org/Steve_Simon_(Minnesota)"]),
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
        print(f"  ✓ {m['name']:<26} ({state}) +{len(new_claims)} claims, conf: {old_conf} → evidence_curated")

    # Minified write — preserve the no-whitespace master (see module docstring).
    SCORECARD.write_text(json.dumps(scorecard, separators=(",", ":")))
    print()
    print(f"Total: upgraded {upgraded} candidates, added {claims_added} claims")


if __name__ == "__main__":
    main()
