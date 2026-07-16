# 61 — RESOLUTE more evidence-only cells

**Date:** 2026-07-16  
**Branch:** polish/proven-coaching-nav-20260716  
**Pass:** VALHALLA BURN CONTINUED — thin sitting members  
**Cells applied:** 18 (null→T/F only; no overwrites)

## Rule

- Evidence only from existing candidate **notes/claims** and repo **apply-*-vote.py** roll-call maps.
- No invented votes for special-election arrivals before seating.
- No overwrite of existing True/False.
- Scope: thin sitting House members with residual key nulls.

## Applied

| Member | State | Party | Cell | Value | Evidence |
|---|---|---|---|---|---|
| Austin Scott | GA | R | `border_immigration[1]` | **T** | notes: "Yea HR2 + Laken Riley"; map all-R YEA apply-laken-riley-vote.py |
| Neal Dunn | FL | R | `border_immigration[1]` | **T** | notes: "YEA Laken Riley (23/2025)"; map all-R YEA |
| French Hill | AR | R | `border_immigration[1]` | **T** | notes: "YES HR 2 + Laken Riley Act"; map all-R YEA |
| Rick Crawford | AR | R | `border_immigration[1]` | **T** | notes: "YES HR 2 + Laken Riley Act + S.5"; map all-R YEA |
| Scott Franklin | FL | R | `border_immigration[1]` | **T** | notes: "Laken Riley x3"; map all-R YEA |
| Laurel Lee | FL | R | `border_immigration[1]` | **T** | notes: "Laken Riley"; map all-R YEA |
| Gus Bilirakis | FL | R | `border_immigration[1]` | **T** | notes: "HR 2 + Laken Riley yes"; map all-R YEA |
| Daniel Webster | FL | R | `border_immigration[1]` | **T** | notes: "HR 2 + Laken Riley yes"; map all-R YEA |
| Zach Nunn | IA | R | `border_immigration[1]` | **T** | notes: "Laken Riley S.5 2025-23"; map all-R YEA |
| Rick Crawford | AR | R | `sanctity_of_life[0]` | **T** | notes: "YES Born-Alive HR 26"; map all-R YEA HR 21 apply-born-alive-vote.py |
| Steve Womack | AR | R | `biblical_marriage[2]` | **T** | map all-R YEA H.R.28 apply-women-sports-vote.py; long-tenure AR-3 sitting |
| Abraham Hamadeh | AZ | R | `family_child_sovereignty[1]` | **T** | map R default YEA H.R.3492 apply-protect-children-vote.py (not R_VOTED_NAY); seated 1/3/2025 |
| Zach Nunn | IA | R | `family_child_sovereignty[1]` | **T** | map R default YEA H.R.3492 (not R_VOTED_NAY); sitting IA-3 |
| Paul Gosar | AZ | R | `family_child_sovereignty[1]` | **T** | map R default YEA H.R.3492 (not R_VOTED_NAY); long-tenure sitting |
| Juan Ciscomani | AZ | R | `biblical_marriage[2]` | **T** | notes: "HR28 Women in Sports cosponsor/YEA"; map all-R YEA |
| Juan Ciscomani | AZ | R | `election_integrity[1]` | **T** | notes: "SAVE Act HR22 YEA"; map all-R YEA apply-save-act-vote.py |
| Juan Ciscomani | AZ | R | `family_child_sovereignty[1]` | **T** | notes: "HR3492 Protect Children's Innocence"; map R default YEA |
| Sarah McBride | DE | D | `family_child_sovereignty[1]` | **F** | map D default NAY H.R.3492 apply-protect-children-vote.py (not D_VOTED_YEA); notes NAY pattern on women sports/SAVE/Laken/Born-Alive |

## Deliberately not filled

| Member | Why unsafe / deferred |
|---|---|
| Clay Fuller (GA-14) | Seated ~2026-04-14 after all 2025 marquee votes |
| Jimmy Patronis (FL-01) | Seated 2025-04-01 — pre-dates Jan Laken Riley / H.R.28; bi/bm left null |
| Randy Fine (FL-06) | Seated Apr 2025 — bi[1] pre-seating for Laken Riley |
| James Walkinshaw (VA-11) | Seated Sept 2025 — ei[1]/SAVE Apr 2025 pre-seating |
| Adelita Grijalva (AZ-07) | Seated ~Nov 2025 — ei[1]/SAVE pre-seating |
| Juan Ciscomani bi[1] | Already **False** — no overwrite even if notes mention Laken YEA |
| Challengers / placeholders / not_running non-members | Out of scope |

## Sources (repo)

- `apply-laken-riley-vote.py` → `border_immigration[1]`
- `apply-born-alive-vote.py` → `sanctity_of_life[0]`
- `apply-women-sports-vote.py` → `biblical_marriage[2]`
- `apply-save-act-vote.py` → `election_integrity[1]`
- `apply-protect-children-vote.py` → `family_child_sovereignty[1]`
- Existing per-candidate `notes` on scorecard cards (cited in table)

## Rebuild

`python3 build-data.py` then `python3 generate-profiles.py` (rank callouts refresh).

