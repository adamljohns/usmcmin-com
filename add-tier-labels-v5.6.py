#!/usr/bin/env python3
"""
add-tier-labels-v5.6.py  (2026-05-23)

Per-tier rubric drill-down — Adam's v5.0 follow-up critique resolved.

v5.0 made the GOVERNMENT pillar tier-aware (federal=America First, state=
State First, local=Local First) and gave each shared God-First category its
own questions_state / questions_local. But the visible LABEL and DESCRIPTION
on every profile/cards/deep-dive page stayed canonical — so users browsing
a state-rep profile saw "Sanctity of Life" with the same description as a
federal Senator profile, even though the underlying questions had drilled
down. v5.6 fixes the visible drill-down: each shared category gets
{label_state, label_local, description_state, description_local} so the
render layer shows tier-tailored framing without re-scoring 9k candidates.

Approach (Adam approved 2026-05-23):
- Keep canonical names + add tier-specific subtitles ("— State abortion law
  & funding"), don't rename outright (preserves searchability + cross-tier
  comparability + audit trail).
- Focus descriptions on what THAT OFFICE actually decides at that tier.
- Federal uses the existing canonical fields (no override needed).

Bumps meta.version → 5.6.0 and meta.rubric_version → v3.6-tiered-rubrics.
Idempotent: skips fields already present.
"""
import json
import os
import sys

REPO = os.path.dirname(os.path.abspath(__file__))
SC = os.path.join(REPO, "data/scorecard.json")

# Per-category tier-specific labels + descriptions.
# `label_*` is the full label string for that tier (canonical + ' — subtitle').
# `description_*` is the full description for that tier (what THAT office decides).
TIER_CONTENT = {
    "sanctity_of_life": {
        "label_state":
            "Sanctity of Life — State abortion law & funding",
        "label_local":
            "Sanctity of Life — Protect the Vulnerable",
        "description_state":
            "Does this state official affirm full personhood and vote for "
            "state-level abortion abolition, Medicaid defunding of abortion, "
            "parental-consent requirements, clinic-safety regulation, and "
            "protection of unborn life under state criminal and civil code?",
        "description_local":
            "Does this local official prioritize prosecuting violence "
            "against the vulnerable, refuse to zone or publicly fund "
            "abortion providers, support crisis-pregnancy outreach, and "
            "protect children in schools, libraries, parks, and city "
            "contracts from harm and exploitation?",
    },
    "biblical_marriage": {
        "label_state":
            "Biblical Marriage — State family law",
        "label_local":
            "Biblical Marriage — Local public squares",
        "description_state":
            "Does this state official affirm marriage as one man + one "
            "woman in state family law, resist state recognition of same-"
            "sex 'marriage' beyond federal mandate, oppose state-funded "
            "gender ideology, prohibit hormone/surgical interventions on "
            "minors, and refuse 'pride' celebrations in state institutions?",
        "description_local":
            "Does this local official keep gender ideology and 'pride' "
            "programming out of public schools, libraries, parks, and city "
            "events; refuse to mandate trans-affirming policies on city "
            "employees or contractors; and respect parental authority over "
            "their children's identity?",
    },
    "family_child_sovereignty": {
        "label_state":
            "Family & Child Sovereignty — State parental rights",
        "label_local":
            "Family & Child Sovereignty — Local schools & libraries",
        "description_state":
            "Does this state official codify parental rights in state "
            "statute, ban gender procedures on minors, prevent state "
            "schools and CPS from undermining parents, fund school choice/"
            "ESAs, and protect homeschool, private, and religious education "
            "from state-board intrusion?",
        "description_local":
            "Does this local official keep age-inappropriate materials out "
            "of public libraries and schools, support parental opt-outs "
            "and curriculum transparency, defend religious freedom in "
            "local school policy, and prevent CPS/family-court overreach "
            "into faithful families?",
    },
    "christian_liberty": {
        "label_state":
            "Christian Liberty — State religious-exemption code",
        "label_local":
            "Christian Liberty — Local religious freedom",
        "description_state":
            "Does this state official write and protect religious-"
            "exemption carve-outs in state law (employment, healthcare, "
            "schooling, civil-rights enforcement), and refuse to compel "
            "Christian-owned businesses, ministries, and institutions to "
            "violate conscience under state nondiscrimination law?",
        "description_local":
            "Does this local official protect church property rights and "
            "zoning, allow Christian symbols and displays in public spaces, "
            "defend chaplains and religious gatherings, and refuse to "
            "weaponize anti-discrimination ordinances against Christian-"
            "owned business or worshipping communities?",
    },
    "economic_stewardship": {
        "label_state":
            "Economic Stewardship — State budget & taxation",
        "label_local":
            "Economic Stewardship — Local taxes & spending",
        "description_state":
            "Does this state official produce balanced budgets without "
            "borrowing, lower the state tax burden on working families, "
            "resist crony-capitalist subsidies, oppose ESG mandates in "
            "state procurement and pension funds, and prioritize productive "
            "investment over progressive vanity programs?",
        "description_local":
            "Does this local official keep property, sales, and business "
            "taxes low; audit and reduce city debt; refuse pension-fund "
            "manipulation; reject corporate subsidies and TIF giveaways; "
            "and prioritize roads, water, public safety, and core services "
            "over progressive vanity projects?",
    },
    "election_integrity": {
        "label_state":
            "Election Integrity — State election law",
        "label_local":
            "Election Integrity — Local election administration",
        "description_state":
            "Does this state official require photo ID at the polls, "
            "mandate citizenship verification on voter rolls, enforce "
            "signature verification on mail ballots, prohibit ballot "
            "harvesting, support hand-counted paper-ballot audits, and "
            "refuse federal/private-foundation election funding ('Zuck-"
            "bucks')?",
        "description_local":
            "Does this local official maintain clean voter rolls, run "
            "transparent precinct administration, accept paper-ballot "
            "audit access, refuse third-party election grant money, train "
            "poll workers fairly, and ensure ballot processing is "
            "observable by both parties?",
    },
    "border_immigration": {
        "label_state":
            "Border & Immigration — State enforcement cooperation",
        "label_local":
            "Border & Immigration — Local enforcement cooperation",
        "description_state":
            "Does this state official cooperate with ICE/CBP, oppose "
            "sanctuary-state policies, require E-Verify for state "
            "contracts, restrict in-state tuition / driver's licenses / "
            "public benefits to citizens and lawful residents, and "
            "prosecute human trafficking and cartel activity?",
        "description_local":
            "Does this local official refuse sanctuary status, cooperate "
            "with ICE detainers, prosecute illegal-alien crime fully, "
            "oppose city-issued ID cards for noncitizens, require "
            "contractor E-Verify, and refuse city funding of NGO 'aid' "
            "for illegal border-crossers?",
    },
    "self_defense": {
        "label_state":
            "Self-Defense & 2A — State firearm law",
        "label_local":
            "Self-Defense & 2A — Local public safety & enforcement",
        "description_state":
            "Does this state official pass or protect constitutional "
            "carry, oppose state 'assault weapons' or magazine bans, "
            "restore rights to non-violent offenders, refuse red-flag "
            "laws without robust due process, and codify castle-doctrine "
            "and stand-your-ground in state law?",
        "description_local":
            "Does this local official refuse to pass local gun ordinances "
            "that exceed state law, fully fund and back the line police, "
            "reject soft-on-crime diversion of gun offenses, and prosecute "
            "violent and armed crime to the fullest extent?",
    },
    # public_justice is STATE + LOCAL only (no federal). Both tiers need a
    # tier-specific framing — federal canonical doesn't apply here.
    "public_justice": {
        "label_state":
            "Public Justice — State courts & corrections",
        "label_local":
            "Public Justice — Local DA & sheriff priorities",
        "description_state":
            "Does this state official appoint or confirm faithful judges, "
            "defend tough sentencing for violent and predatory crime, "
            "oppose decarceration ideology, fund corrections adequately, "
            "and protect victims' rights in state courts and parole?",
        "description_local":
            "Does this local official back police funding and discretion, "
            "prosecute crimes against the vulnerable, refuse 'progressive "
            "prosecutor' diversion and bail reform that releases violent "
            "offenders, and support victims throughout local court "
            "proceedings?",
    },
    # refuse_federal_overreach is STATE-only — the canonical label already
    # tells you what tier it's for. No subtitle needed; tier description is
    # canonical.
    # refuse_state_overreach is LOCAL-only — same.
    # foreign_policy_restraint and industry_capture are FEDERAL-only — no
    # state/local variants apply.
}


def patch_scorecard():
    with open(SC) as f:
        data = json.load(f)

    updated = 0
    skipped = 0
    for cat in data["categories"]:
        cid = cat["id"]
        if cid not in TIER_CONTENT:
            continue
        new = TIER_CONTENT[cid]
        for k, v in new.items():
            if k in cat and cat[k] == v:
                skipped += 1
                continue
            cat[k] = v
            updated += 1

    # Bump version metadata
    meta = data["meta"]
    prev_v = meta.get("version")
    prev_r = meta.get("rubric_version")
    meta["version"] = "5.6.0"
    meta["rubric_version"] = "v3.6-tiered-rubrics-labels"
    print(f"meta.version       {prev_v} → {meta['version']}")
    print(f"meta.rubric_version {prev_r} → {meta['rubric_version']}")

    # Persist with stable formatting (matches existing scorecard.json shape)
    with open(SC, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nfields added/updated: {updated}")
    print(f"fields already present (skipped): {skipped}")
    print(f"categories patched: {sum(1 for c in data['categories'] if c['id'] in TIER_CONTENT)}")


if __name__ == "__main__":
    patch_scorecard()
