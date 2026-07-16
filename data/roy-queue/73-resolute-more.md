# 73 — RESOLUTE more evidence-only cells (scorecard burn)

**Date:** 2026-07-16  
**Repo:** `~/.openclaw/workspace/usmcmin-com`  
**Branch:** `polish/proven-coaching-nav-20260716`  
**Skill:** refine-scorecard  
**Cells applied:** **30** (null→T/F only; no overwrites)

---

## Rule

- Evidence only from repo **`apply-*-vote.py` roll-call maps** (+ candidate notes where corroborating).
- **No invent.** **No overwrite** of existing True/False.
- Prefer **sitting** U.S. House members with residual marquee nulls.
- Special-election arrivals left alone on **pre-seating** cells (Patronis Laken/Sports stay null; only post-seating Protect filled).

---

## Cells applied (30)

| # | Member | State | Party | Cell | Value | Evidence |
|---|---|---|---|---|---|---|
| 1 | Brittany Pettersen | CO | D | `biblical_marriage[2]` | **F** | House D NAY H.R.28 (not Cuellar/Gonzalez) — `apply-women-sports-vote.py` |
| 2 | Brittany Pettersen | CO | D | `election_integrity[1]` | **F** | House D NAY SAVE Act H.R.22 RC 102 — `apply-save-act-vote.py` |
| 3 | Brittany Pettersen | CO | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 (not D_VOTED_YEA) — `apply-protect-children-vote.py` |
| 4 | Adam Gray | CA | D | `biblical_marriage[2]` | **F** | House D NAY H.R.28 (not sports defectors) |
| 5 | Adam Gray | CA | D | `election_integrity[1]` | **F** | House D NAY SAVE Act (not SAVE D_YEA list) |
| 6 | Jimmy Patronis | FL | R | `family_child_sovereignty[1]` | **T** | Seated Apr 2025; R YEA H.R.3492 Dec 2025 (not R_VOTED_NAY) |
| 7 | Nellie Pou | NJ | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492; freshman sworn Jan 2025 |
| 8 | Jay Obernolte | CA | R | `biblical_marriage[2]` | **T** | House R all YEA H.R.28 |
| 9 | Jay Obernolte | CA | R | `election_integrity[1]` | **T** | House R all YEA SAVE Act |
| 10 | Jay Obernolte | CA | R | `family_child_sovereignty[1]` | **T** | House R YEA H.R.3492 (not R_VOTED_NAY) |
| 11 | Herb Conaway | NJ | D | `election_integrity[1]` | **F** | House D NAY SAVE Act; freshman Jan 2025 |
| 12 | Herb Conaway | NJ | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 13 | Jill Tokuda | HI | D | `sanctity_of_life[0]` | **F** | Notes cite NAY Born-Alive; House D NAY H.R.21 RC 27 — `apply-born-alive-vote.py` |
| 14 | George Whitesides | CA | D | `border_immigration[1]` | **F** | House D NAY Laken Riley (not HOUSE_D_YEA) — `apply-laken-riley-vote.py` |
| 15 | George Whitesides | CA | D | `election_integrity[1]` | **F** | House D NAY SAVE Act |
| 16 | George Whitesides | CA | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 17 | Greg Stanton | AZ | D | `biblical_marriage[2]` | **F** | House D NAY H.R.28 |
| 18 | Greg Stanton | AZ | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 19 | Kelly Morrison | MN | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 20 | Nick Begich III | AK | R | `border_immigration[1]` | **T** | House R all YEA Laken Riley; freshman Jan 2025 |
| 21 | Derek Tran | CA | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 22 | Jason Crow | CO | D | `biblical_marriage[2]` | **F** | House D NAY H.R.28 |
| 23 | Jason Crow | CO | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 24 | Jared Moskowitz | FL | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 25 | Kat Cammack | FL | R | `border_immigration[1]` | **T** | House R all YEA Laken Riley; sitting since 2021 |
| 26 | Adelita Grijalva | AZ | D | `family_child_sovereignty[1]` | **F** | Seated ~Nov 2025; D NAY H.R.3492 (12/17/2025) |
| 27 | Robert Garcia | CA | D | `border_immigration[1]` | **F** | House D NAY Laken Riley |
| 28 | John Larson | CT | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |
| 29 | Aaron Bean | FL | R | `border_immigration[1]` | **T** | House R all YEA Laken Riley |
| 30 | Diana DeGette | CO | D | `family_child_sovereignty[1]` | **F** | House D NAY H.R.3492 |

---

## Deliberately not filled

| Member / cell | Why |
|---|---|
| Jimmy Patronis `border_immigration[1]`, `biblical_marriage[2]` | Seated 2025-04-01 — pre-dates Jan Laken Riley / H.R.28 |
| Randy Fine pre-seating Laken cell | Same special-election trap (already had other cells filled) |
| Clay Fuller any 2025 marquee | Seated ~2026-04 — after all 2025 votes |
| James Gallagher CA-01 `bi[1]` / `ei[1]` | Special 2026-06-02 — no 2025 House votes |
| James Walkinshaw SAVE / Laken-era | Post-Connolly special; pre-seating for SAVE |
| Yesli Vega / Thomas Galvin federal maps | Not sitting U.S. House |
| Challengers / primary-only / withdrew | Never cast House roll calls |

---

## Pipeline

```text
python3 refine-records.py refinements/hygiene-sitting-marquee-2026-07-16.json --no-build
  → 20 record(s) refined, 30 evidence cells set
  → Backup: data/.backups/scorecard.20260716-165933.json
python3 build-data.py          # OK — 8972 candidates, 53 states
python3 generate-profiles.py   # OK — 8972 profiles
```

Dossier: `refinements/hygiene-sitting-marquee-2026-07-16.json`

### Source scripts (canonical vote maps)

- `apply-laken-riley-vote.py` → `border_immigration[1]`
- `apply-born-alive-vote.py` → `sanctity_of_life[0]`
- `apply-women-sports-vote.py` → `biblical_marriage[2]`
- `apply-save-act-vote.py` → `election_integrity[1]`
- `apply-protect-children-vote.py` → `family_child_sovereignty[1]`

Primary URLs (in footnotes/sources): govtrack h27 / h102 / h351; Roll Call + New Republic Laken lists; ABC/Hill on H.R.28.

---

## Score deltas (selected)

| Slug | Old /100 | New /100 |
|---|---|---|
| jay-obernolte | 67 | **73** |
| jimmy-patronis | 91 | **92** |
| kat-cammack | 80 | **81** |
| adam-gray | 22 | **18** (added 2 documented FALSEs) |
| george-whitesides | 8 | **6** |
| adelita-grijalva | 13 | **12** |

---

## Git

- Branch: `polish/proven-coaching-nav-20260716`
- Commit message pattern: `RESOLUTE hygiene: fill 30 thin-sitting null score cells (evidence-only)`

---

## Bottom line

- **30 evidence cells** filled on **20 sitting** U.S. House members.
- **Zero fabricated positions.** Pre-seating special traps left null.
- Site data rebuilt; profiles regenerated.
