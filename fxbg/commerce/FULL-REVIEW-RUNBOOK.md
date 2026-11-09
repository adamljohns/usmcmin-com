# Commerce FULL REVIEW mode — runbook

Ticket: `commerce-full-review-strike-ticket-2026-11-09.md` (Adam order, Max TG 8996, 2026-11-08: same
standard as the church full review). Status: built and dry-run only. **No live apply until Adam's GO.**

The ordinary grind (`~/Scripts/commerce-enrichment-round.sh`, 22:00–06:00) fills Gray factors from a
quick read of one page. A full-review round reads each business's own site end to end with the local
model, checks every directory field (exists/open, name, address, phone, website, hours, category,
owner/operator, licence for trades), scores only against written methodology rules, and writes a
review patch plus a HOLD queue. It never writes `data/businesses.json`; the applier does, later.

## Trigger a round

```bash
cd <usmcmin-com checkout or worktree>
fxbg/commerce/scripts/full-review-round.sh            # 25 businesses, selection order below
fxbg/commerce/scripts/full-review-round.sh 40         # batch size (max 60)
fxbg/commerce/scripts/full-review-round.sh 25 --include 2400-diner,2400-diner-fxbg   # force slugs in
fxbg/commerce/scripts/full-review-round.sh 25 --spread      # sample mode: round-robin tiers a,b,c,d (dry runs / QA)
```

Needs LM Studio on `127.0.0.1:1234` (`COMMERCE_FR_MODEL`, default `gemma-4-31b-it`; `qwen/qwen3.6-35b-a3b`
also works). SearXNG `127.0.0.1:8888` is used for at most 10 queries a round (`FULL_REVIEW_SEARCH_MAX`).
Brave is never used; no paid API is called. Pages are fetched at most once per 1.1 s per host.
A round of 25 takes roughly 20–40 minutes, mostly model time.

The script refuses to start while the grind holds `/tmp/commerce-enrichment-round.lock.d`, takes its own
lock `/tmp/commerce-full-review.lock.d`, and checks the data file's sha256 before and after (it exits 2 if
the file changed). Log: `~/Library/Logs/commerce-full-review-round.log`.

## Selection order

(a) no website or no verified-at date, (b) licensed trades, (c) oldest verified first, (d) the rest.
Within a tier: licensed trades first, published before hidden, oldest first. verified-at is the newest of
`full_review.verified_at` and any `scores.*_meta.verified`. Listings fully reviewed in the last 30 days
are skipped (`FULL_REVIEW_COOLDOWN_DAYS`). Today tier (a) is about 1,500 listings, almost all OSM stubs
with no website, so early rounds are mostly website recovery.

## Stages and files

| Stage | Script (fxbg/commerce/scripts/) | Writes |
|---|---|---|
| select | `select-full-review-batch.py` | `$FR_HOME/rounds/<round>/batch.json` |
| observe | `full-review-fetch.py` | `…/observations.json` (pages read, cached text, model output) |
| patch | `full-review-build-patch.py` | `…/review-patch.json`, `…/hold.json`, `$FR_HOME/hold-queue.json` |
| counts | `build-full-review-stats.py` | `fxbg/commerce/data/full-review-stats.json` (numbers only) |
| apply (manual) | `apply-full-review-patch.py` | `data/businesses.json`, pages, ledger — only with `--live` |
| tests | `test-full-review.py` | nothing |

`$FR_HOME` defaults to `~/commerce-full-review`, outside the repository. This repo is public on GitHub
and its root syncs to R2, so patches, quotes and HOLD rows never go in it. Only the counts file does;
`build-stats.py` folds it into `data/stats.json` and the hub's Directory snapshot shows
"Full review: N reviewed · N with proposed changes · N held for QA · N applied".

## Gates

- No URL or quote, no change. Every quote is re-found verbatim in the cached page text before the patch
  is written. Social links are typed `html_link` (the exact `<a …>` tag) or `site-config` (only in page
  config/JSON). Site-config links are always HOLD. Junk such as `facebook.com/2008` and bare `profile.php` is skipped.
- Evidence must be on topic for the field: the phone's digits are in the quote, the parsed hours equal
  the proposal, and the owner's name appears next to an ownership word.
- Scope: the evidence must be about this business at this location. On a chain or multi-location site
  only a page that prints this location's street or phone, and no other street, counts. Passages about
  sponsors, partners, other locations or other towns are dropped and listed in `scope_dropped`.
- Hours: stored and page hours are compared as sets of day+time tokens. A change is proposed only when
  the sets differ, and `new` is the structured value (`["Mon–Fri: 7:00 AM–8:00 PM", …]`).
- Location gate (added after verify round 1, 8/10). An auto change needs the exact page holding
  its quote to print the stored street, or the stored ZIP in address form ("VA 22407"). A shared
  phone number, a service-area ZIP list, or no identifier at all never counts.
- Multi-location sites are detected by any of: "N Locations" / "two locations" wording, a location
  picker or `/locations/<x>` menu, or two or more street+ZIP addresses. On such a site every fill must
  come from the stored location's own page, or from its own section (the nearest street address before
  the passage is the stored one). Anything else is HOLD.
- Hours conflicts. Hours are read from every page as runs of day/time tokens; runs are split at street
  addresses, and one-day-per-line, "Closed on Saturdays" and "by appointment" are handled. If any other
  listing on the site disagrees on a day both state, the change is HOLD and every conflicting quote is
  in `evidence_more`.
- `possibly_moved` flag (HOLD): the stored URL's site prints a different street, and a different phone
  (or only our phone), than the listing. `stored` and `site` values are both in the flag.
- Licence numbers: a bare `#27xxxxxxxx` (footers) or a 27xxxxxxxx number next to licence wording is
  captured onto the DPOR-check HOLD row as `license_number_on_site`.
- Auto (would apply on a live run) only: hours, phone fills and social links from the business's own
  website. They also need high confidence, in-scope evidence, and no partial or inferred hours.
  Everything else is HOLD.
- Website recovery (OSM tag, then the name as .com/.org, then one SearXNG query) is accepted only when
  the candidate prints the business name and the stored street, ZIP or phone. Third-party listing
  sites (menu/review/directory pages) are rejected. A recovered website is always HOLD, and so is
  everything read from it.
- Scores come only from rules printed on `methodology.html`. Every score change carries `rule` with the
  rule text. The applicable rules are #1 owner named plus real address, #3 type A explicit Christian
  identity, #8 licence number printed and #9 own site reachable and printing the contact. Proposals
  only move a factor off Gray. All score changes are HOLD. Anything the model suggests that no written
  rule covers becomes a HOLD `needs-ruling` row, never a score.
- Closures, moves, renames, duplicates/merges and category changes are HOLD flags. Duplicates already
  folded through `duplicate_of` are reported as `already_linked` and not re-flagged.
- HOLD QA owner: Sheriff Roy (FXBG civic lane). Adam decides needs-ruling rows.

## Official lookups

- Virginia SCC entity search (`cis.scc.virginia.gov`): skipped. After a cookie-consent redirect, the
  search button runs Google reCAPTCHA v3.
- DPOR License Lookup (`dporweb.dpor.virginia.gov/LicenseLookup/`): skipped. The reCAPTCHA checkbox is
  required before every search.
- Locality business-licence pages (City of Fredericksburg, Spotsylvania, Stafford): not used in v1.
  Nobody has checked yet whether they offer a public per-business search. That is open work.

Every licensed trade gets a HOLD `lookup` row with the DPOR URL and any licence number the business
prints. A person checks it by hand. Facebook serves bots a login wall or HTTP 4xx, so the "posts in the
last 12 months" signal is recorded as not checked.

## Applying (after Adam's GO only)

```bash
python3 fxbg/commerce/scripts/apply-full-review-patch.py $FR_HOME/rounds/<round>/review-patch.json            # dry run, writes nothing
python3 fxbg/commerce/scripts/apply-full-review-patch.py … --data /tmp/copy.json                               # dry run on a copy
python3 fxbg/commerce/scripts/apply-full-review-patch.py … --live --approved roy-approved-ids.txt [--push]    # live
```

A live run applies auto rows plus the HOLD ids listed in `--approved`. It re-checks every `old` value
against the current file and skips anything stale. It takes the grind lock, merges duplicates and
retires closures through the existing `duplicate_of` / `closed` + `publish:false` + `notes_internal`
pattern, and never deletes. It then regenerates the touched pages, categories and stats, runs the
integrity checks, appends to `$FR_HOME/applied-ledger.json`, and commits only those paths. `--push` uses
the same pull --rebase / push HEAD:main as the grind, so deploy doctrine is unchanged. Run it from a
checkout level with origin/main, never from a stale one.

## Dry-run record (2026-11-09)

- `fr-20261109-0655` (strict ticket order, 25 listings): 24 had no reachable site. Tier (a) is all
  no-website OSM stubs, and SearXNG's upstream engines were blocked that morning (DuckDuckGo CAPTCHA,
  Google CSE suspended, Bing connection errors). Only bad-truck-pottery was recovered, through the
  name-domain probe.
- `fr-20261109-0701` (`--spread`, 25 listings including both 2400 Diner records): 12 reviewed,
  27 changes proposed (12 auto, 15 hold), 7 needs-ruling, 16 DPOR lookup rows. businesses.json
  sha256 was the same before and after.
- Until SearXNG engines recover, tier-(a) rounds mostly yield "unreachable". Name-domain probes still
  run.
- Verify round 1 on `fr-20261109-0701` scored 8/10. Every quote was real; both failures were location
  identity. NK Floors auto hours came from a location-less pop-up on a two-location site, and BIM's
  site prints a different street and phone. The gates were fixed (location gate, multi-location,
  cross-page hours conflicts, one-day-per-line hours, `possibly_moved`, bare licence numbers).
- `fr-20261109-0723` re-ran the same `--spread` sample: 28 changes, 4 auto, 24 hold. businesses.json
  sha256 was unchanged.
- `fr-20261109-0740` re-ran strict order on the fixed gates. SearXNG answered part of the round (Bing),
  then Bing was suspended again; DuckDuckGo was denied and Google CSE suspended. 2 of 25 sites were
  recovered (bad-truck-pottery, plumb-perfect-plumbing), giving 9 changes, all hold.
