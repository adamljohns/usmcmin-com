---
# RESOLUTE Citizen per-state contribution template.
# Copy this file to contributions/<state>/<slug>.md and edit.
# See ../../CONTRIBUTING-PER-STATE.md for the full guide.

# REQUIRED — must match the existing profile slug exactly (lowercase, hyphenated).
# Visit https://usmcmin.com/candidates/<state>/<slug>.html to find the slug.
slug: example-candidate-name

# REQUIRED — 2-letter state code (lowercase). Use 'us' for federal-only roles
# like cabinet members or US Senators not tied to a single state.
state: va

# OPTIONAL — your handle/name + contact email so we can credit you in the
# commit message and reach out with questions. Email won't be published.
contributor: Your Name Here
contributor_email: you@example.com

# OPTIONAL — update office field if it has changed (resignation, election
# loss, new appointment, retirement announcement, etc.).
office: "U.S. Senator (Virginia)"

# OPTIONAL — update status if applicable: 'active' (default), 'former',
# 'lost', or 'lame_duck'. Provide evidence URL in `evidence` below.
# status: former

# OPTIONAL — proposed score changes. Each entry is one of the 10 v4.0
# categories with an array of 5 values per question (q0 .. q4). Values:
#   true        → Boolean true (counts toward score + max)
#   false       → Boolean false (counts toward max only)
#   "N/A"       → not applicable to this office tier (counts toward neither)
#   null        → unanswered (counts toward neither)
#   "keep"      → don't propose a change for this question
#
# Categories you don't include here will NOT be touched.
scores:
  sanctity_of_life: ["keep", "keep", "keep", "keep", "keep"]
  biblical_marriage: ["keep", "keep", "keep", "keep", "keep"]
  family_child_sovereignty: ["keep", "keep", "keep", "keep", "keep"]
  christian_liberty: ["keep", "keep", "keep", "keep", "keep"]
  economic_stewardship: ["keep", "keep", "keep", "keep", "keep"]
  election_integrity: ["keep", "keep", "keep", "keep", "keep"]
  border_immigration: ["keep", "keep", "keep", "keep", "keep"]
  self_defense: ["keep", "keep", "keep", "keep", "keep"]
  foreign_policy_restraint: ["keep", "keep", "keep", "keep", "keep"]
  industry_capture: ["keep", "keep", "keep", "keep", "keep"]

# OPTIONAL — church affiliation cross-pollination with usmcmin.org church
# directory. Only include if you have a verifiable source.
# church_affiliation:
#   name: "First Baptist Church Houston"
#   denomination: "Southern Baptist Convention (SBC)"
#   evidence_url: "https://example.com/article-naming-attendee"
#   evidence_date: "2026-05-19"

# REQUIRED — at least one primary-source URL backing your score changes
# or office/status updates. URLs should be:
#   - Campaign websites or official government bios
#   - Recorded votes (Congress.gov, state legislature roll calls)
#   - Public statements (press releases, official social media)
#   - Local press coverage from named outlets
# AVOID: anonymous accusations, opposition-research talking points,
# unattributed social media screenshots.
evidence:
  - "https://example.com/source-1-citation"
  - "https://example.com/source-2-citation"

---

## Narrative notes (optional)

Use this section for any context that doesn't fit in the structured frontmatter
above. For example:

- Explanation of a contested score change
- Notes on why a question was marked N/A vs null
- Context for an office/status update
- Background on the contributor's source of evidence

If you don't have anything to add, leave this section blank or delete it.
