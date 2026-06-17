# RESOLUTE Local — Readiness: Richmond, VA

**Status:** Research only (F2 scaffold). No code, no profiles, no scorecard data yet.
**Compiled:** 2026-06-16. EXPANSION-PLAN target #1 (second city after Fredericksburg).

Richmond is the next expansion candidate because it has a clean, machine-friendly
civic stack: a Granicus video archive (live + on-demand) and a Granicus/Legistar
agenda center with per-meeting agendas, action summaries, and video links. Both
are the same vendor family already understood from the Fredericksburg build.

---

## Meeting broadcaster (video)

- **Vendor:** Granicus (Richmond hosts on `richmondva.granicus.com`).
- **Live stream:** Formal Meetings stream live; live audio for Informal,
  Standing Committee, and Special Meetings.
  `http://richmondva.granicus.com/MediaPlayer.php?publish_id=1`
- **On-demand archive (Council Meetings):**
  `https://richmondva.granicus.com/ViewPublisher.php?view_id=2`
  (individual clips use the `richmondva.granicus.com/player/clip/<id>` pattern).
- **Also broadcast (not the ingest path):** Formal Meetings air live on PBS
  station WCVW (OTA 57.1, Comcast/Verizon FIOS ch. 24, DirecTV/Dish ch. 57) and
  replay twice daily for two weeks on Richmond Government Access TV cable ch. 17.
- **Note vs. EXPANSION-PLAN spec:** Richmond uses the Granicus player, **not**
  YouTube/Vimeo. The Granicus archive is the equivalent on-demand source; plan
  the recap pipeline around the Granicus clip player, not a YouTube URL.

Source: City Clerk meeting-media page —
`https://www.rva.gov/office-city-clerk/richmond-city-council-meeting-media`
and `https://www.rva.gov/richmond-city-council/meeting-audiovideo`.

## Agenda center (agendas / minutes)

- **Vendor:** Granicus **Legistar** (`richmondva.legistar.com`).
- **Calendar / agenda center:** `https://richmondva.legistar.com/Calendar.aspx`
  — covers City Council, the five Standing Committees (Finance & Economic
  Development; Public Safety; Governmental Operations; Land Use, Housing &
  Transportation; Education & Human Services), Planning Commission, BZA, and more.
  Provides agendas (some EN/ES), action summaries/minutes, per-meeting video
  links, and iCal/Excel/PDF/Word export.
- **Department detail:** `https://richmondva.legistar.com/DepartmentDetail.aspx?ID=24010`
- **Chambers:** Richmond City Hall, 2nd Floor, 900 E. Broad St., Richmond, VA 23219.

## Council roster source

- **Primary (official):** `https://www.rva.gov/richmond-city-council/council-contacts`
- **Cross-check:** Ballotpedia (`https://ballotpedia.org/Richmond,_Virginia`);
  RVAHub oath-of-office writeup for the seated 2025–2028 class
  (`https://rvahub.com/2025/01/03/new-2025-2028-richmond-city-council-members-administered-oaths-of-office/`).

**9 single-member voter districts. Term: Jan. 2, 2025 – Dec. 31, 2028.**
Richmond council seats are formally **nonpartisan** (like Fredericksburg) — expect
the same party-label reconciliation question the F1 audit flagged.

| District | Name | Notes |
|---|---|---|
| 1st / West End | Andrew S. Breton | |
| 2nd / North Central | Katherine L. Jordan | Vice President (2025–2026) |
| 3rd / Northside | Kenya J. Gibson | |
| 4th / Southwest | Sarah M. A. Abubaker | |
| 5th / Central | Stephanie A. Lynch | |
| 6th / Gateway | Ellen F. Robertson | |
| 7th / East End | Cynthia I. Newbille | Council President |
| 8th / Southside | Reva M. Trammell | |
| 9th / South Central | Nicole Jones | |

**Mayor (separate executive, directly elected):** Danny Avula (D), in office
Jan. 1, 2025 – Jan. 1, 2029. Source:
`https://ballotpedia.org/Danny_Avula` and `https://www.rva.gov/mayors-office/about-danny`.

---

## Readiness verdict

**Green.** Broadcaster + agenda center + roster all sourced and stable; same
Granicus/Legistar vendor stack as Fredericksburg. Two things to decide before a
build: (1) the recap pipeline must read the **Granicus clip player**, not
YouTube/Vimeo; (2) reconcile the formally **nonpartisan** city labels against
RESOLUTE's party tags (same open question as F1). No code written here.
