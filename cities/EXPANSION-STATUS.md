# RESOLUTE Local — Expansion Status

**Compiled:** 2026-06-19. Summary only — rolls up the five existing per-city
READINESS docs (no new research, no code). Each city's facts and sources live in
its own `cities/<city>-READINESS.md`; this is the at-a-glance index.

The expansion set is the five EXPANSION-PLAN targets researched after Fredericksburg
(the live build). All five verdicts are **Green** — broadcaster, agenda center, and
roster are sourced and stable for each. What differs is the vendor stack, the council
scale, and the party-label situation.

---

## Per-city summary

| City | Broadcaster (video) | Agenda center (docs) | Council size | Party labels | Readiness |
|---|---|---|---|---|---|
| **Richmond, VA** | Granicus player (`richmondva.granicus.com`) — not YouTube | Granicus **Legistar** (`richmondva.legistar.com`) | 9 single-member districts + separately elected Mayor (Danny Avula, D) | Formally **nonpartisan** | Green |
| **Raleigh, NC** | Granicus/RTN (`raleigh.granicus.com`) **+ official YouTube Live** | **BoardDocs** (Diligent) | 8 = Mayor + 2 At-Large + 5 District (A–E) | Formally **nonpartisan** | Green — split video/doc vendors |
| **Greenville, SC** | Official **YouTube** archive; live layer is Cisco **Webex** (no static URL) | **CivicClerk** (CivicPlus) | 7 = Mayor + 2 At-Large + 4 District | **PARTISAN now** (4–3 D); state law (May 2026) forces nonpartisan from **2027** | Green — ingest caveat + label twist |
| **Nashville, TN** (Metro/Davidson) | **YouTube** `@MetroNashvilleNetwork` (+ MNN cable, Roku, Cablecast) | Granicus **Legistar** (`nashville.legistar.com`) | **40** = 35 District + 5 At-Large (+ Mayor, + tie-breaking Vice Mayor) | Formally **nonpartisan** | Green — largest roster in the program |
| **Colorado Springs, CO** | **Granicus** VOD (`ViewPublisher.php?view_id=1`); YouTube cadence unverified | Granicus **Legistar** (`coloradosprings.legistar.com`) | 9 = 6 District + 3 At-Large; **Mayor sits outside Council** | Formally **nonpartisan** (Mayor Mobolade runs Independent) | Green — Granicus-not-YouTube ingest; separated executive |

**Roster source** for every city is the official municipal site (cross-checked
against Ballotpedia + local news); the exact URLs are in each READINESS doc.

---

## Patterns across the set

- **Agenda vendor — Legistar leads.** Granicus **Legistar** in 3 of 5 (Richmond,
  Nashville, Colorado Springs), so that scraper transfers across them. Raleigh uses
  **BoardDocs**; Greenville uses **CivicClerk (CivicPlus)** — two one-off scrapers.
- **Video ingest splits two ways.** Clean **YouTube VOD** at Raleigh, Greenville,
  and Nashville; **Granicus VOD** (no usable YouTube cadence) at Richmond and
  Colorado Springs. Plan the recap pipeline for the per-city source of record, not a
  single assumed YouTube URL.
- **Docs and video are usually separate platforms.** Raleigh (BoardDocs + Granicus),
  Greenville (CivicClerk + YouTube/Webex), and Richmond (Legistar + Granicus player)
  each need two ingest paths. Nashville and Colorado Springs are the exceptions —
  Legistar embeds recent video, so docs + video can come from one path (though
  YouTube/Granicus VOD stays the cleaner video source).
- **Council scale ranges wide.** 7 (Greenville) to **40** (Nashville, third-largest
  U.S. council). Budget the profile build for Nashville's 35 district + 5 at-large
  roster.
- **Party labels — one inverse case.** Four cities are formally **nonpartisan**, so
  party tags must be inferred from record, not the ballot (the same reconciliation
  question the F1 Fredericksburg audit flagged). **Greenville is the inverse:** it is
  *partisan today* (real 2025 D/R labels, 4–3 D majority) and converts to nonpartisan
  only with the **2027** cycle, so its labels are valid now but must be dropped after.
- **One separated executive.** Colorado Springs is **mayor-council** (strong-mayor):
  the Mayor is **not** a council member and must be built as its own record. The
  other four fold the mayor into (or alongside) the council body.

---

## Next steps (from the READINESS docs, not new work)

- **P2 backlog:** research the next EXPANSION-PLAN target city (one not yet covered),
  same CITED-research format.
- Before any build: confirm the per-city YouTube council playlist where the ingest
  path is YouTube (Greenville's and Raleigh's specific playlist URLs are still
  uncaptured), and reconcile each city's party-label policy against RESOLUTE's tags.

No code or profiles were produced here — this is a documentation roll-up only.
`data/scorecard.json` untouched.
