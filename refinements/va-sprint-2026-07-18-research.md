# VA RESOLUTE Sprint Research — 2026-07-18

## Inventory
- **296** VA candidates in scorecard.json (285 active, 6 lost, 5 former)
- Confidence mix: evidence_curated 162 · evidence_local 119 · evidence_state 6 · evidence_federal 4 · thin rest
- FXBG / Spotsy / Stafford locals mostly `evidence_local` with low dens (many den 1–6)

## Statewide / federal (high visibility)

### Abigail Spanberger — Governor (sitting, sworn Jan 17, 2026) · D
- **Roster:** Sitting 75th Governor of Virginia (first woman). Won 2025 over Winsome Earle-Sears (~57%).
- **HARD evidence (2026):**
  - Signed Right to Contraception Act; statement marking 4 years since *Dobbs* reaffirming reproductive rights. Source: https://www.governor.virginia.gov/newsroom/news-releases/2026/june-releases/name-1120192-en.html
  - Signed legislation putting **Virginia Right to Reproductive Freedom Amendment** on Nov 3, 2026 ballot. Sources: Planned Parenthood Action (2026-02-06); Ballotpedia https://ballotpedia.org/Virginia_Right_to_Reproductive_Freedom_Amendment_(2026)
  - As House member: voted **against** Protection of Women and Girls in Sports Act (2023, clerk.house.gov/Votes/2023192) — documented in Virginia Mercury 2025-09-09: https://virginiamercury.com/2025/09/09/on-the-record-abigail-spanberger/
  - Mercury: opposes Youngkin-era bathroom/pronoun policies; pledged to protect LGBTQ+ student rights; would veto further abortion restrictions.
- **Scorecard implication:** Reinforces existing FALSE dens on life / marriage / family-child; not a re-score invent. conf remains evidence_state.

### Ghazala Hashmi — Lt. Governor · D · sworn Jan 17, 2026
- First Muslim woman elected statewide in US (per prior notes). Thin dens relative to Spanberger. Needs deeper AG-era voting if any as LG (ceremonial) — mostly prior Senate record.

### Jay Jones — Attorney General · D · sworn Jan 17, 2026
- Defeated R Jason Miyares 2025 (~53-46). Prior HD-89. Scorecard dens thinner than ideal for AG-tier power.

### Winsome Earle-Sears — former LG · failed 2025 gubernatorial
- Thick dens (44 cells, 82%). Status correctly former/failed.

### US Senate VA
- Tim Kaine, Mark Warner — dens=50 each (federal max). Hung Cao 2026 R challenger dens=38.

### US House VA (sample)
- R: Wittman VA-01, Kiggans VA-02, McGuire VA-05, Cline VA-06, Griffith VA-09 — generally high dens
- D: Scott VA-03, McClellan VA-04, Vindman VA-07, Beyer VA-08, Subramanyam VA-10, Walkinshaw VA-11
- Connolly deceased / seat filled — status_hygiene_only, dens=0 (correct hygiene)

## Fredericksburg City Council (roster web-verified 2026-07-18)

Official: https://www.fredericksburgva.gov/263/Council-Members

| Office | Name | Scorecard slug | Term (official) |
|--------|------|----------------|-----------------|
| Mayor At-Large | Kerry P. Devine | kerry-devine | Jan 1 2024 – Dec 31 2027 |
| Ward 1 | Matt D. Rowe | matt-rowe-fxbg | Jan 1 2026 – Dec 31 2029 |
| Ward 2 | Joy Y. Crump | joy-crump-fxbg | Jan 1 2026 – Dec 31 2029 |

Also on council (see official page for full seven): at-large + wards 3–4. Scorecard has jannan-holmes, will-mackintosh, susanna-finn, charlie-frye-jr, etc.

### Joy Crump
- First Black woman on FXBG City Council; part of first female-majority council (Nov 2025 election). https://www.fredericksburgfreepress.com/2025/11/04/crump-makes-history-as-fredericksburg-elects-first-female-majority-to-city-council/
- Short voting record (took office 2026) — thin dens expected; do not invent policy cells.

### Matt Rowe
- Former school board chair → Ward 1 2026. Prior notes: YES on FY2027 4-cent RE tax (local economic_stewardship).

## Spotsylvania / Stafford
- Supervisors & school boards present with evidence_local dens 1–11. Crystal Vanuch Rock Hill dens=11 pct=100 is a relative local thick record.
- School board members many den=1 — priority queue for social/policy research (not this hour’s deep pass).

## Gaps ranked by impact
1. Sitting statewide trio (Spanberger/Hashmi/Jones) — keep sources current as 2026 session bills land
2. FXBG school board (andy-wolfenbarger et al. dens 0–1)
3. Thin city councils statewide (Suffolk/Norfolk boroughs den=0)
4. VA-02 / VA-07 2026 primary churn (withdrawn candidates hygiene)
5. Space-in-id church network hygiene is org-side, not RESOLUTE

## Method notes
- Cardinal rule: web-verified before score changes
- Null ≠ False; sparse dens trap avoided for new FXBG members

---

## Appendix: dry-run + apply (2026-07-18)

```
python3 refine-records.py refinements/va-sprint-2026-07-18.json --dry-run
```

| slug | tier | old | new | chg | ev | src |
|------|------|----:|----:|----:|---:|----:|
| abigail-spanberger | state | 5 | 5 | 0 | 0 | 24 |
| ben-cline | federal | 100 | 100 | 0 | 0 | 9 |
| charlie-frye-jr | local | 25 | 25 | 0 | 0 | 8 |
| crystal-vanuch | local | 100 | 100 | 0 | 0 | 17 |
| deuntay-diggs | local | 60 | 60 | 0 | 0 | 21 |
| eugene-vindman | federal | 22 | 22 | 0 | 0 | 28 |
| ghazala-hashmi | state | 0 | 0 | 0 | 0 | 23 |
| hung-cao-senate-2026 | federal | 50 | 50 | 0 | 0 | 8 |
| jannan-holmes | local | 0 | 0 | 0 | 0 | 5 |
| jason-miyares-ag-2026 | state | 62 | 64 | 16 | 0 | 12 |
| jay-jones | state | 0 | 0 | 0 | 0 | 25 |
| john-reid | state | 93 | 93 | 9 | 0 | 10 |
| joy-crump-fxbg | local | 0 | 0 | 0 | 0 | 7 |
| kerry-devine | local | 0 | 0 | 0 | 0 | 7 |
| lori-hayes | local | 100 | 100 | 0 | 0 | 14 |
| mark-warner | federal | 0 | 0 | 0 | 0 | 13 |
| matt-rowe-fxbg | local | 0 | 0 | 0 | 0 | 6 |
| maya-guy | local | 0 | 0 | 0 | 0 | 22 |
| rob-wittman | federal | 86 | 86 | 0 | 0 | 10 |
| susanna-finn | local | 0 | 0 | 0 | 0 | 6 |
| tim-kaine | federal | 0 | 0 | 0 | 0 | 14 |
| will-mackintosh | local | 0 | 0 | 0 | 0 | 8 |
| winsome-earle-sears | state | 88 | 88 | 9 | 0 | 10 |

**Summary:** 23 records refined, **0 evidence cells set** (hygiene + sources + conf only).  
Only score headline move: `jason-miyares-ag-2026` 62→64 (tier rebuild / notes_set side-effect; not a cell evidence swing).

**Applied:** yes — `python3 refine-records.py refinements/va-sprint-2026-07-18.json --no-build`  
**Backup:** `data/.backups/scorecard.20260718-164350.json`  
**Build:** deferred to parent (generate-profiles / category pages / sitemap not run).


---

## HOTFIX (same day, post-apply recheck)

Stale scorecard notes claimed Warner "RETIRING 2026" and listed Hung Cao as 2026 Senate contender. **Web recheck contradicted both:**

1. **Mark Warner** announced Dec 2, 2025 he is seeking a fourth term — https://wtop.com/virginia/2025/12/sen-mark-warner-announces-reelection-campaign-in-virginia/ ; GovTrack next reelection 2026. Restored `incumbent_seeking_reelection`.
2. **Hung Cao** confirmed Acting Secretary of the Navy Apr 2026 (Wikipedia/Ballotpedia) — **not** a 2026 Senate candidate. Office/candidacy corrected via `refinements/va-sprint-2026-07-18-hotfix.json` (applied `--no-build`).

Lesson: treat old notes as hypotheses; always re-verify high-stakes status against current Ballotpedia/official sources before writing candidacy_status.


## King George County (coverage hole closed at roster level)
See `king-george-va-roster-2026-07-18.md` + ingest skeleton (15 slugs, no scores). BoS: Sullins/Davis/Binder/Metts/Stroud; Sheriff Giles; CA Gusmann; SB Davis chair.
