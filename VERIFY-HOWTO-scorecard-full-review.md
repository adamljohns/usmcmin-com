# How to verify the scorecard full-review dry run (for the independent verifier)

Ticket item 2: pick 10 proposed changes from the dry run and confirm, against LIVE sources, that each
one is supported by its cited evidence and that its gate is right. This file tells you where everything
is and how each evidence type is checked. It holds no results; write those yourself in a VERIFY file.

Worktree: `/Users/moop_bot_pro/worktrees/scorecard-full-review` (branch `feat/scorecard-full-review`).
Read-only work. Do not edit `data/scorecard.json` (here or in `~/.openclaw/workspace/usmcmin-com`), do not
run `apply.py --live`, do not push.

## Files

The patch and HOLD files are deliberately NOT in the repo (the repo root deploys to usmcmin.com). They live in
`~/.openclaw/state/scorecard-full-review/`:

| What | Path |
|---|---|
| Review patch (every proposal, per politician) | `rounds/ROUND_ID/review-patch.json` |
| This round's HOLD rows | `rounds/ROUND_ID/hold.json` |
| Cumulative HOLD queue (latest round per politician) | `hold-queue.json` |
| Per-politician fetch + model record | `rounds/ROUND_ID/obs/<slug>@<ST>.json` |
| Every page the round read (raw + text, as read) | `rounds/ROUND_ID/pages/` (`index.json` maps URL -> files) |
| scorecard.json checksums | `rounds/ROUND_ID/sha256-before.txt`, `sha256-after.txt` |
| Round log | `~/Library/Logs/scorecard-full-review.log` |
| Public counts (the only thing that goes on the site) | `data/full-review-stats.json` in the worktree; panel on `stats.html` |

ROUND_ID for the dry run: see "Dry run" at the end of this file.

## How a change maps to its evidence

`review-patch.json` -> `politicians[]` (one per politician) -> `changes[]`:

```
change_id        "<round>:<slug@ST>:<n>"  (same id as hold_id in hold.json)
field            the scorecard field: "scores.<category>[<question index>]", "website", "party", "district",
                 "profile.term_start", "profile.term_end", "profile.phone", "profile.twitter|facebook|youtube|instagram"
op               fill (field was empty) | replace (field had a value)
old / new        stored value now / proposed value  (social: new is the stored-format handle; new_url is the link)
kind             score | roster | fact | contact
rule             score changes only: {text, context, url} = the question as PUBLISHED on usmcmin.com and the page's
                 binary rule ("Each question is binary (True / False / null). True earns +2 points.")
evidence.quote   the passage, cut from the page's own characters
evidence.url     the page that passage is on
evidence.evidence_type   page_text | xml_record | html_record | html_link | site-config | archive_copy
evidence.source_rank     1 roll call / bill sponsor / official structured roster · 2 official's own government page ·
                         3 campaign site · 4 endorsing/rating org · 5 news/aggregator
evidence.context ~300 characters either side of the quote on that page (score changes)
evidence_more    other passages that point the same way (score changes)
crosscheck       the second local model's answers (score changes)
gate             auto (would apply on a live run) | hold (waits for Roy QA)
hold_reasons     why it is held
```

`politicians[].flags[]` (kind `flag` or `ruling`) and `politicians[].rechecks[]` are HOLD rows that are not
changes: out-of-office / currency flags, dedupe flags, `needs-ruling` judgments, citation re-checks. They
never apply. `politicians[].confirms[]` are stored answers the review re-found evidence for (no change).
`politicians[].dropped[]` lists what the gates threw away and why.

## How to check one change

1. Open `evidence.url` in a browser (a browser user agent; some hosts 403 a bare fetch).
2. Find `evidence.quote` on it.
   - `page_text`: visible page text. Matching ignores case, runs of whitespace, and curly vs straight
     quotes/dashes; everything else must match character for character. Trailing punctuation may be trimmed.
   - `xml_record` (House Clerk `MemberData.xml`, Senate `senators_cfm.xml`): the quote is an exact
     contiguous slice of the raw XML, from the member's name element to the field (party, phone, sworn date,
     website). View source / download the XML and search for it.
   - `html_record` (Virginia House / Senate member lists): exact contiguous slice of the raw HTML card
     (name link through district, and party for the Senate). View source.
   - `html_link`: the exact `<a ...href...>` tag in the raw HTML of `evidence.url` (house.gov member
     directory, or the official's own site for social links). View source.
   - `site-config`: the link appears only in page config/JSON (always HOLD). View source.
   - `archive_copy`: the URL is a web.archive.org copy of an official page that blocks automated reads
     (`archive_of` in the obs file names the original). Always HOLD.
   If the live page changed since the round, the exact text the round read is in `pages/` (look the URL up
   in `pages/index.json`, then open `<text_file>` or `<raw_file>`).
3. Judge:
   - Does the passage support `field: old -> new` for THIS person in THIS office (not a namesake, a
     predecessor, another district, or a joint statement where they are only listed)?
   - Score changes: is `rule.text` on `rule.url` (the live usmcmin.com category page), and does the quote
     meet that rule as written (TRUE = their record affirms the line; FALSE = it contradicts it)? A partial
     step (a restriction for an abolition line, a reform for a repeal line) should NOT be a change; the
     builder routes those to `needs-ruling`.
   - Is the gate right? `auto` is allowed only for filling an EMPTY website / term date / office phone from
     an official source, high confidence, and never for a Fredericksburg/Virginia official. Every score
     change, every replace, every Virginia record, first grades, letter moves, out-of-office and dedupe
     flags must be `hold`.

## Quick listing

```
cd ~/.openclaw/state/scorecard-full-review/rounds/ROUND_ID
/opt/homebrew/bin/python3 - <<'PY'
import json
p = json.load(open("review-patch.json"))
for P in p["politicians"]:
    for x in P.get("changes", []):
        print(" | ".join([x["change_id"], x["gate"], x["field"], json.dumps(x["old"]), "->", json.dumps(x["new"]),
                          x["evidence"]["evidence_type"], x["evidence"]["url"], json.dumps(x["evidence"]["quote"])[:220]]))
PY
```

## Checksums

```
cat rounds/ROUND_ID/sha256-before.txt rounds/ROUND_ID/sha256-after.txt
shasum -a 256 /Users/moop_bot_pro/worktrees/scorecard-full-review/data/scorecard.json
```
All three must be identical.

## Suggested spread for the 10

At least one Fredericksburg official (term dates from the city page), one Virginia General Assembly roster
item, one House Clerk XML fact (term start / phone), one house.gov directory website fill, one social link
from an official site, at least two score changes (if the round produced them; otherwise two `confirms` or
`needs-ruling` rows, judged as "is the hold right"), one citation re-check row (open the cited URL and look
for the name), and one out-of-office / currency flag.
