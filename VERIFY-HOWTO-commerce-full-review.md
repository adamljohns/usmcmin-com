# How to verify the commerce full-review dry run (for the independent verifier)

Ticket item 2 (`~/.openclaw/workspace/commerce-full-review-strike-ticket-2026-11-09.md`): pick 10
proposed changes from the dry run, check each one yourself against the live site, and record PASS or
FAIL in a VERIFY file. At least 9 of 10 must pass. This file only tells you where everything is. It
contains no verification results; you write those.

Worktree: `/Users/moop_bot_pro/worktrees/commerce-full-review` (branch `feat/commerce-full-review`).
Treat everything as read-only. Do not edit `fxbg/commerce/data/businesses.json` here or in
`~/.openclaw/workspace/usmcmin-com`, and do not run the applier with `--live`.

## Files

Patches and HOLD rows are kept OUTSIDE the repo, which is public on GitHub and synced to R2:
`FR=~/commerce-full-review`.

| What | Path |
|---|---|
| Review patch (every proposal, per business) | `$FR/rounds/<ROUND>/review-patch.json` |
| This round's HOLD rows | `$FR/rounds/<ROUND>/hold.json` |
| Cumulative HOLD queue (latest round per business, `dry_run: true`) | `$FR/hold-queue.json` |
| Pages read + cached page text + model output | `$FR/rounds/<ROUND>/observations.json` |
| sha256 of businesses.json before/after | `$FR/rounds/<ROUND>/checksums.txt` |
| Round log | `~/Library/Logs/commerce-full-review-round.log` |
| Public counts only | `fxbg/commerce/data/full-review-stats.json` |
| Strict-order round (ticket selection order, mostly no-website listings) | `$FR/rounds/fr-20261109-0655/` |
| Superseded first attempt | `$FR/rounds/fr-20261109-0649/` (`"superseded"` set) |

Main dry run: **`<ROUND>` = `fr-20261109-0701`**, started with `--spread` (sample mode, round-robin across
selection tiers a/b/c so every gate runs; its `selection_tier` values end in "(spread sample)").
It holds 25 businesses, including 2400-diner and 2400-diner-fxbg. There are 27 proposed changes: 12
`auto` and 15 `hold`. The patch was rebuilt from the same `observations.json` after the gate fixes, with
no re-fetch. The strict ticket-order round `fr-20261109-0655` has 24 of 25 listings with no reachable
site, because tier (a) is all no-website stubs and SearXNG's engines were blocked. It has 5 changes,
all on bad-truck-pottery, and they repeat in 0701.

## How a proposed change maps to its evidence

`review-patch.json` → `businesses[]`, one per business. Each `changes[]` entry has these fields:

```
change_id      "<round>:<slug>:<n>"  (same id as hold_id in hold.json when held)
field          businesses.json field: hours | phone | zip | web | owner_operator | sources | scores.<factor>
op             fill (was empty) | set | replace | append (sources) | research (information for QA, never applied)
old / new      value in businesses.json when the patch was built -> proposed value
also_sets      extra fields written with it (hours_source, scores.<factor>_meta)
confidence     high | medium | low
gate           auto (would apply on a live run) | hold (waits for QA: Sheriff Roy)
hold_reasons   why it is held
evidence.url   the page the evidence is on
evidence.quote the evidence (see evidence_type)
evidence.evidence_type
               html_text      quote is visible page text; find it on the page
               html_link      quote is the exact <a ...> tag in the page HTML (view source)
               site-config    quote is a raw config/JSON snippet in the HTML (view source); always hold
               http_redirect  "<stored url> -> <final url>": request the stored site and watch it redirect
               http_status    the stored site failed to load; the quote is the HTTP result
rule           (scores only) [{text, context, url}] — rule text printed on methodology.html
evidence_more  extra evidence (e.g. the street-address passage behind an ownership score)
```

To check one change:
1. Open `evidence.url` in a browser. Some hosts 403 a bare fetch, so use a browser user agent.
2. Find `evidence.quote`. Matching ignores case, runs of whitespace (including the line breaks in
   quotes, which mark boundaries between page elements) and curly vs straight quotes; everything else
   must match exactly. For `html_link` and `site-config`, search the page source.
   If the live page changed after the round, the cached text is in `observations.json`:
   `observations[]` (by `slug`) → `pages[]` (or `recovery.review.pages[]` for a recovered site) → `text`.
3. Decide whether the quote supports `field: old -> new` for THIS business at THIS location. It must
   not be about another branch, a partner or sponsor, or a same-name firm elsewhere.
4. Check the gate. Only hours, phone fills and social links from the business's own (not recovered)
   site may be `auto`. Scores, website recovery, owner, ZIP/address, category, closures and duplicates
   must be `hold`.

Hours: `businesses[].hours` has `stored_tokens` and `page_tokens` (day+time tokens). A change exists
only when the two sets differ. `new` is the structured list in the stored format. `evidence.quote` is
the page passage it was parsed from.

Scores: every `scores.*` change has `rule` texts that must be printed on
https://usmcmin.com/fxbg/commerce/methodology.html. Check that they map the quote to `new`. Rules in use:
#1 "Who owns/operates it? Real address?" (owner named plus street on the business's own page), #3 type A
"Explicitly Christian business — faith is public identity", #8 "Scam-adjacent? Licensed/transparent?"
(licence number printed) and #9 "Can a neighbor actually reach them?". Proposals only move a factor off
Gray. Model judgments with no written rule are HOLD rows `kind: "ruling"` (title `needs-ruling: …`).
They are not changes; do not count them among your 10.

Website recovery (`field: web`, `op: fill`): the candidate site must print the business name and the
listing's stored street, ZIP or phone. `evidence.quote` is that identifier passage on the candidate.
Always `hold`. Fills read from a recovered site are also `hold`.

Flags (`businesses[].flags[]`; `kind: "flag"` in hold.json) cover duplicate-candidate, possibly-closed,
possibly-moved, possibly-renamed, category-review, phone-ambiguous and site-unreachable. They are QA
items, not changes. `businesses[].duplicate_result` is the plain-language duplicate finding.
`businesses[].scope_dropped` lists evidence that was excluded and the reason.

## Quick listing

```
FR=~/commerce-full-review; R=$(ls -d $FR/rounds/fr-* | tail -1)
python3 -c '
import json,sys; p=json.load(open(sys.argv[1]+"/review-patch.json"))
for b in p["businesses"]:
  for c in b["changes"]:
    print(" | ".join([c["change_id"], c["gate"], c["field"], json.dumps(c["old"])[:50], "->", json.dumps(c["new"])[:80], c["evidence"]["url"], c["evidence"]["evidence_type"], json.dumps(c["evidence"]["quote"])[:140]]))' "$R"
```

This round has no score changes and no owner_operator changes. No Gray factor met a written rule
from in-scope evidence: Robinson's "Christian Owned" brand is already Green, so it is only a
confirmation. Model-only signals went to `needs_ruling`.

Suggested spread for the 10 (all from fr-20261109-0701):
- the three `auto` hours or social changes on nk-floors-fxbg (`:1` hours fill, `:2` Instagram, `:3` LinkedIn);
- all-fixed-appliance-repair-fxbg `:1` (auto hours set: adds "Sat–Sun: Closed") and `:2` (auto Facebook);
- robinsons-roofing-fxbg `:1` (hold hours, "more than one hours block") and `:2` (auto Facebook, numeric page id);
- all-air-heating-cooling-fxbg `:1` (hold phone replace, stored number not on site);
- bad-truck-pottery `:1` (hold website recovery via name-domain probe);
- forte-construction-design-fxbg `:1`–`:3` (auto socials) or krispy-kreme `:1` (hold hours on a chain
  location page; two hours blocks).

Also read `duplicate_result` for 2400-diner and 2400-diner-fxbg. It is a finding, not a change.
