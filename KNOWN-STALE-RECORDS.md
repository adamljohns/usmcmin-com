# Known stale records — RESOLUTE Citizen v4.0

**Last updated: 2026-06-01**
**Maintainer: regenerate this on every web-validation sweep.**

---

## SWEEP 2026-06-01 — Fredericksburg + VA delegation finalization (via refine-records.py engine)

**Done (evidence-based, cited, applied + rebuilt):**
- **All 16 City of Fredericksburg records finalized.** Roster verified current (7 council, CA Humphries, 6 school board, 2 formers). Added the v5.0 local categories (`public_justice`, `refuse_state_overreach`) that every local record was missing; cleared speculative party-default FALSEs to null. Scores: Frye 25 (documented police-partnership credit, docked for gun give-back + taxes), all other council 0, Humphries 0 (self-described reform prosecutor), school-board incumbents 0 (one documented board-posture FALSE), new board members + formers = roster-verified scaffolding. Dossiers: `refinements/fxbg-2026-06.json`, `refinements/fxbg-schoolboard-2026-06.json`.
- **VA roster currency fixed:** Senate now 40/40 (added the missing **SD-27 = Tara Durant**, converted from a stray federal-only record per the dual-office rule), House 100/100. **Deduped Joshua Cole** (two HD-65 records → one). **Miyares** → `lost` (lost AG 2025 to Jay Jones); **Jay Jones** → `won`/sitting AG.
- **VA Fredericksburg delegation finalized (state tier):** **Tara Durant (SD-27, R) = 82** — conservative record, docked for her VERIFIED same-sex-marriage YES vote (HJ3, 01/16/2026). **Joshua Cole (HD-65, D) = 0** — chief sponsor of the abortion-rights AND same-sex-marriage amendments, Giffords-endorsed. Dossier: `refinements/va-fxbg-delegation-2026-06.json`.

**Backlog opened by this sweep:**
- **VA legislature (~138 of 140 seats) still archetype/party-default** — only the FXBG delegation + statewide execs are individually evidenced. Next pass; the `refine-scorecard` skill + engine make it systematic.
- **⚠️ SLUG COLLISION — `mike-thompson` (BLOCKER, identified 2026-06-05 0307 federal-CA batch):** Three active records share the bare slug `mike-thompson` — (1) Rep. Mike Thompson, US Representative CA-4 (federal tier, D, sitting since 1999); (2) State Sen. Mike Thompson, MS State Senate District 48 (state tier, R); (3) State Sen. Mike Thompson, KS State Senate District 10 (state tier, R). The `refine-records.py` engine keys by bare slug only (`by_slug = {c.get('slug'): c for c in sc['candidates']}`), so a dossier entry under `mike-thompson` would resolve to the LAST candidate with that slug — currently the KS state senator (index 6805) — and a federal-tier dossier would fail tier validation against a state record. The CA-4 federal Democrat is the highest-priority federal House Dem unrefined record (skipped this batch 2026-06-05 0307 and substituted with mark-takano CA-39). **Fix:** same pattern as `rick-west` — rename slugs e.g. `mike-thompson-ca-4` (federal) + `mike-thompson-ms-48` (MS) + `mike-thompson-ks-10` (KS), update profile HTML paths in candidates/<state>/, then refine. Three-way collision: pick canonical for each + rename two.
- **✅ RESOLVED 2026-06-05 — `rick-west` slug collision.** Helper `disambiguate-rick-west.py` renamed the VA Mayor's slug from `rick-west` → `rick-west-chesapeake` in `data/scorecard.json` + `data/proposed_claims.json`; OK State Rep keeps the canonical `rick-west`. Orphan `candidates/va/rick-west.html` pruned in same commit; new page lives at `candidates/va/rick-west-chesapeake.html`. The Chesapeake-mayor evidence refinement (research preserved in `refinements/research-notes-rick-west-chesapeake-2026-06-05.md`) is now unblocked and folds into the next LOCAL batch dossier under the new slug.
- **✅ RESOLVED 2026-06-01 — Stacy Garrity (PA) dup.** Two records (`stacy-garrity-2026` Treasurer + `stacy-garrity-gov` Governor nominee) violated the one-record rule. Merged to one per the dual-office rule (Tara Durant precedent): kept the sitting-office record `stacy-garrity-2026`, extended `office` + `candidacy_status` → `running_higher_office` (2026 R gubernatorial nominee), merged in the gov-race sources (NBC primary results, Spotlight PA, Wikipedia); deleted `stacy-garrity-gov` + pruned its orphan profile. Web-verified: won the uncontested R primary 05/19/2026, faces D incumbent Gov. Josh Shapiro in the Nov general. Engine auto-upgraded the stale v4 score keys to the v5.0 state rubric (65→68 — scores still establishment_r archetype, evidence-based refinement pending). Dedup script `dedup-garrity-2026-06.py` + dossier `refinements/pa-garrity-dedup-2026-06.json`. **Evidence refinement DONE 2026-06-02 (68→88/100 B):** cited state-rubric scoring — pro-life, school choice, fiscal discipline, voter ID, ICE cooperation, GOA-endorsed guns; documented marriage non-affirmation (dodged when asked); honest nulls on religious liberty / public justice / refuse-federal-overreach / ESG. Dossier `refinements/garrity-klobuchar-2026-06.json`.
- **FXBG school board possible 7th/Ward-3 seat** — confirm board size (6 confirmed sitting members).
- **✅ NOTE (reconciled 2026-06-02):** master `scorecard.json` is minified by `build-data.py` (~37MB, under GitHub's 50MB warn). DATABASE-LAYOUT §5 + MAINTENANCE §2 rule 6 now both document this; the old "always indent=2 / never compact" guidance is superseded.

---

This document tracks records in `data/scorecard.json` that are KNOWN to
need evidence review or have CONFIRMED stale information. Use it as the
punch list for the next individual-rescoring session.

---

## A. Records corrected in commit `4cfcb37345` (already done)

These were stale; web search resolved them.

| Slug | What changed | When |
|------|--------------|------|
| `marjorie-taylor-greene` | Resigned US House (GA-14) | Jan 5, 2026 |
| `pam-bondi` | Fired as US AG; replaced by Todd Blanche | Apr 2, 2026 |
| `markwayne-mullin` | OK Senator → DHS Secretary | Mar 24, 2026 |
| `donald-j-trump` | Office field was empty → set to POTUS | (always was) |
| `jd-vance` | Office field was empty → set to VPOTUS | (always was) |
| `alan-armstrong` | OK Senator (appointed, can't seek full term) | Mar 24, 2026 |
| `todd-blanche` | NEW — acting US AG | Added 2026-05-18 |
| `kristi-noem` | NEW — Shield of Americas Envoy (formerly DHS) | Added 2026-05-18 |
| `sean-duffy` | NEW — Sec of Transportation | Added 2026-05-18 |
| `mikie-sherrill` | Refreshed: now NJ Governor (sworn Jan 20, 2026) | Refreshed 2026-05-18 |

---

## B. Records known to be stale — NOT YET FIXED

### ✅ Foreign Policy Restraint scoring across House — RESOLVED 2026-05-18

**Resolved via `apply-iran-war-powers-vote.py`** (one-off evidence applier).
All 419 House members (217 R + 212 D minus a few with no-party) now
have evidence-based FPR[0]/[1] values per the March 5, 2026 vote on
H.Con.Res.38 (Iran war powers, defeated 212-219):

- 212 House Ds (with party for restraint) → T, T
- 217 House Rs (with Speaker against restraint) → F, F
- 2 R defectors (Massie, Davidson) → T, T
- 4 D defectors (Landsman OH, Cuellar TX, Golden ME, Vargas CA) → F, F

This is the FIRST evidence-based score in the v4.0 rubric (vs. archetype-
default). Next high-value votes to walk: HR 1 (For the People Act)
for `election_integrity`, BSCA + RFMA already done in `enrich-
scorecard-v4.py`, etc.

### Cabinet members already in scorecard with potentially-stale offices

Several T2 cabinet members were in scorecard before I added them. The
add-missing-federal-figures.py refresh updated their office field, but
their scores from the Senate / pre-cabinet era may not reflect their
current cabinet behavior. Worth a manual re-verify:

- **Marco Rubio** (Sec of State) — score 48/F. His Senate-era hawk
  record is consistent with his current State Dept role, but his
  positions on China, Iran, Israel may have shifted in office.
- **Pete Hegseth** (Sec of Defense) — score 90/A. Possibly too high?
  Did NOT find time to verify his actual SecDef actions vs. campaign
  positions.
- **RFK Jr.** (HHS) — score 48/F. Did NOT verify his HHS actions on
  vaccine schedule, fluoride, raw milk vs. CHD-era positions.
- **Linda McMahon** (Education) — score 42/D. Did NOT verify her
  actual ED actions during Trump's stated DoE-elimination push.
- **Doug Burgum** (Interior) — added 2026-05-18 but archetype-based,
  did NOT verify his actual Interior actions.

### Governors I assigned archetypes to without per-individual verification

| Slug | State | Concern |
|------|-------|---------|
| `gavin-newsom` | CA | Confirmed sitting, but signature vetoes/sign-ons in 2025-26 not reviewed |
| `kathy-hochul` | NY | Same |
| `gretchen-whitmer` | MI | Confirmed term-limited; running for nothing |
| `jb-pritzker` | IL | Did not verify if running for higher office 2028 |
| `josh-shapiro` | PA | Confirmed sitting; 2028 D presidential speculation not in record |
| `jared-polis` | CO | Confirmed sitting |
| `michelle-lujan-grisham` | NM | Confirmed sitting |
| `tina-kotek` | OR | Confirmed sitting |
| `bob-ferguson` | WA | Confirmed sitting (Inslee successor) |
| `tim-walz` | MN | **Announced will NOT seek re-election 2026** — should add note |
| `tony-evers` | WI | **Announced retirement, will NOT seek re-election 2026** — should add note |
| `joe-lombardo` | NV | Confirmed sitting |
| `kevin-stitt` | OK | Confirmed sitting |
| `henry-mcmaster` | SC | Confirmed sitting |
| `kay-ivey` | AL | Confirmed sitting |
| `bill-lee` | TN | Confirmed sitting |
| `mike-braun` | IN | Confirmed sitting since Jan 13, 2025 |
| `mike-kehoe` | MO | Confirmed sitting (Parson successor) |
| `andy-beshear` | KY | Confirmed sitting; 2028 D presidential speculation |
| `jeff-landry` | LA | Confirmed sitting |

### Senators "not seeking re-election" — 11 incumbents

Per Ballotpedia: 4 Ds + 7 Rs announced they will not seek re-election
in 2026. Their lame-duck status should be reflected in their records.
**Action needed:** pull the Ballotpedia list, mark each.

Source: https://ballotpedia.org/List_of_U.S._Senate_incumbents_who_are_not_running_for_re-election_in_2026

### ✅ Senators running for governor — RESOLVED 2026-06-02

- **Marsha Blackburn** (R-TN) — already a clean single state-tier gov record (`marsha-blackburn-gov`, `primary_candidate`, office notes "sitting U.S. Senator · seat not up till 2030"). Verified current — TN GOP primary Aug 6, 2026 (not yet held). No change.
- **Michael Bennet** (D-CO) — already a clean single state-tier gov record (`michael-bennet-gov`, `primary_candidate`, "sitting U.S. Senator"). Verified current — CO Dem primary Jun 30, 2026 (not yet held). No change.
- **Amy Klobuchar** (D-MN) — was stale (still a federal "US Senator" record, no candidacy_status). Converted to the gov race to match the Blackburn/Bennet pattern: office "Governor of Minnesota (2026 DFL Candidate · sitting U.S. Senator · DFL convention endorsee · Senate seat not up till 2030)", level state, `primary_candidate`. Web-verified: announced Jan 29 2026 after Walz dropped out; won the DFL convention endorsement May 29 2026; primary Aug 11. Dossier `refinements/garrity-klobuchar-2026-06.json`.

None were duplicates (no dedup needed). If any WIN Nov 2026, flip to `won` + mark the Senate seat resigned/open. All three scored on their federal Senate records (archetype) pending evidence refinement.

### State governor 2025 outcomes not validated

- **VA**: Spanberger won, sworn Jan 17, 2026 ✓ (validated)
- **NJ**: Sherrill won, sworn Jan 20, 2026 ✓ (validated)
- That's the only two 2025 statewide gubernatorial races (VA + NJ).

### State legislature bulk party-default records

~6,650 state legislators were bulk-assigned `state_r` or `state_d`
archetype scores via `rescore-state-leg-by-party.py`. These are tagged
`archetype_party_default` so visitors can see they're not individually-
researched. Individual research at scale is impractical (5,000+ hours);
the dispute form on each profile page is the intended upgrade path.

### Local officials (~3,000 records)

School board members, county commissioners, city council. Mostly
non-partisan and not directly engaged with the v4.0 federal/state-leg
issues this rubric tracks. Lowest priority for individual review.

---

## C. Structural issues with the rubric / scoring layer

### Bonus adjustments push pct over 100%

When a candidate has `score_adjustments.aipac.delta = +7` (verified
rejection of AIPAC money), their adjusted score can exceed their
dynamic max, producing a percentage > 100. Examples:
- Thomas Massie: 100/90 = 111%
- James Fishback: 38/26 = 146%

This is visually a bit weird but content-wise it's a meaningful signal
(the candidate earned more credit than the question rubric alone would
give). Decision pending: cap display at 100% or leave the over-100
visible as a badge?

### SCOTUS records have null state/party display issues

Justices show party='Unknown' in tables. They're constitutionally
nonpartisan. Could relabel as 'N' (nonpartisan) or skip the party badge
entirely for them.

### Numeric type drift in scorecard.json on save

When `enrich-scorecard-v4.py` and `enrich-church-affiliation-from-org.py`
write back, they used `separators=(',', ':')` (compact) which exploded
git diffs by 2.2M lines. Both scripts now updated to use `indent=2` +
trailing newline (matches `build-data.py` convention). Re-running any
older enrichment script may still hit the bug.

---

## D. Recommended next-session plan

In priority order:

1. **Walk the Iran war powers roll call (March 2026)** — apply T/F to
   `foreign_policy_restraint[0]` and `[1]` for all ~430 House members.
   Single high-value vote that calibrates ~210 R records that are
   currently wrong on this dimension.
2. **Verify cabinet behavior** — for the 11 cabinet members, check at
   least one signature 2025-26 action and update record accordingly.
3. **Process retiring/lame-duck senators** — pull Ballotpedia list,
   add a `lame_duck` candidacy flag, update notes.
4. **Senate elections-for-governor** — Blackburn, Bennet, Klobuchar
   notes updated to reflect their gubernatorial campaigns.
5. **SCOTUS display polish** — fix party='Unknown' rendering.

Estimated time for all 5: 4-6 hours of focused web research + tooling.

---

## E. What NOT to bulk-revise without individual evidence

- The 200 individually-curated officials are based on training-data
  knowledge of voting records. Some may have shifted positions since.
- The 6,650 state-leg party-default records are explicitly lower-trust;
  individual upgrade requires actual evidence per candidate.
- The Soros DA records (~30, mostly at -50 with mostly nulls) need
  individual evidence work, not bulk re-application.

---

*Generated by add-missing-federal-figures.py + manual audit. Update
this file at the top of every validation sweep with date and findings.*
