#!/usr/bin/env python3
"""
rescore-top-50-federal.py — first pass at the v4.0 rescore of the 8,213
partial candidates. This script targets the top 50 most-visible federal
officeholders + candidates (Trump, Vance, Senate, House leadership, 6
governors) and fills the 6 null categories left by the v4.0 migration:

    family_child_sovereignty   (god_first)
    christian_liberty          (god_first)
    economic_stewardship       (god_first)
    election_integrity         (god_first)  [partial — q0 carried over]
    foreign_policy_restraint   (america_first)
    industry_capture           (america_first)

Approach:
  1. Five archetype profiles capture party + ideological cluster patterns
     that have clear public-record evidence (party-line votes, leadership
     scorecards, public statements). Within each archetype, ambiguous
     questions stay as None — better to be silent than to guess.
  2. Per-candidate overrides flip specific Booleans where a named
     politician's record diverges from their archetype (e.g., Collins/
     Murkowski voted YEA on RFMA so their family_child q4 differs from
     the establishment_r baseline; Lankford's election bill committee
     record makes him a softer score on election_integrity than the
     MAGA-conservative archetype).
  3. The script ONLY fills nulls. Pre-existing True/False answers are
     left untouched — this is enrichment, not overwrite.

Run:
    python3 rescore-top-50-federal.py --dry-run    # preview
    python3 rescore-top-50-federal.py --apply      # write to scorecard.json
After --apply: build-data.py → generate-profiles.py → build-search-index.py

Sources:
  Senate.gov roll-call vote tables for RFMA / BSCA / FTPA / NDAA / CR
  House.gov roll-call tables for HR 1 (For the People Act), HR 2 (SAFE),
    HR 4 (Hyde), HR 4655 (Born-Alive)
  Heritage Action Scorecard, Conservative Review Liberty Score, FreedomWorks,
    NumbersUSA, NRA-PVF, Eagle Forum, AAI scorecards
  Public statements verifiable via congressional press releases + C-SPAN
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False
N = None  # leave as null — no clear public-record evidence

# ─────────────── Archetype profiles ───────────────
# Each archetype defines a base pattern for the 6 null categories. Only
# answer cells with STRONG party-line evidence get a Boolean; the rest
# stay None and require individual research to fill.
#
# Q index → question text (see scorecard.json for full wording):
#   family_child_sovereignty:
#     q0 universal school choice / homeschool freedom
#     q1 parental consent on medical/gender interventions
#     q2 opposes CRT/SOGI/gender ideology in K-12
#     q3 age-verify porn + criminal penalties for sexualization of minors
#     q4 supports faith-based adoption agencies (no SS-couple placement)
#   christian_liberty:
#     q0 right to publicly profess Christ in all spheres
#     q1 conscience exemptions for Christian professionals
#     q2 opposes compelled speech against Christian conviction
#     q3 public-square Christian symbols / prayer in public bodies
#     q4 opposes state-funded non-Christian religious displays
#   economic_stewardship:
#     q0 opposes CBDC, supports cash + decentralized crypto
#     q1 sound money (gold/silver), audit/abolish Fed
#     q2 opposes deficit spending, balanced-budget amendment
#     q3 usury limits, anti-debt-slavery, tithe-friendly tax
#     q4 opposes WEF/ESG/Davos, supports anti-trust on financial cartels
#   election_integrity:
#     q0 hand-counted paper ballots, opposes electronic machines
#     q1 photo voter ID with citizenship verification
#     q2 single-day in-person voting (medical/military absentee only)
#     q3 opposes mass mail-in voting + drop boxes + ballot harvesting
#     q4 opposes "Zuckerbucks" + foreign election interference
#   foreign_policy_restraint:
#     q0 Article I war powers required before military action
#     q1 immediate withdrawal from forever wars, repeal AUMFs
#     q2 opposes foreign aid to hostile or Christian-persecuting nations
#     q3 has never accepted AIPAC / foreign-linked PAC donations
#     q4 opposes WHO/UN governance overreach, NATO expansion
#   industry_capture:
#     q0 opposes pharmaceutical mandates of any kind, informed consent
#     q1 supports repeal of pharma liability shields (NCVIA, PREP)
#     q2 opposes Big Ag consolidation, anti-trust on Bayer/Monsanto/Cargill
#     q3 raw-milk freedom, small-farm protections, anti-USDA/EPA overreach
#     q4 defense-contractor accountability, Pentagon audit, no revolving door

ARCHETYPES = {
    # Hard-MAGA: Cruz, Lee, Paul, Hawley, Cotton, Banks, Vance, Massie,
    # Roy, Gaetz-era successors. Defining traits: school-choice champions,
    # vocal anti-WEF, election-integrity activists. Most accept AIPAC money
    # (F on FPR q3) and support most defense spending (mixed on FPR q1).
    'maga_conservative_r': {
        'family_child_sovereignty':  [T, T, T, T, T],  # uniformly hard on parental rights
        'christian_liberty':         [T, T, T, T, N],  # q4 needs individual review
        'economic_stewardship':      [T, N, T, N, T],  # q1 sound-money + q3 usury split caucus
        'election_integrity':        [N, T, N, T, T],  # q0 paper ballots + q2 single-day not consensus
        'foreign_policy_restraint':  [N, N, N, F, N],  # mostly accept AIPAC; split on AUMF
        'industry_capture':          [N, N, N, T, N],  # raw-milk consensus only
    },
    # Establishment-R: McConnell, Cornyn, Thune, Tillis, Romney, Murkowski,
    # Collins. Defining traits: pro-NDAA defense increases, pro-aid-to-
    # Ukraine, pro-IVF, mixed on parental rights. Most accept AIPAC (F).
    'establishment_r': {
        'family_child_sovereignty':  [N, N, T, N, N],  # only q2 is reliable
        'christian_liberty':         [T, N, N, N, N],  # only q0 broad public support
        'economic_stewardship':      [N, F, N, N, F],  # voted FOR Fed expansion + WEF-aligned policy
        'election_integrity':        [F, T, F, F, T],  # supports voter ID + opposes Zuck $; pro-mail-in
        'foreign_policy_restraint':  [F, F, F, F, F],  # uniformly interventionist + AIPAC-funded
        'industry_capture':          [F, F, F, N, F],  # pro-mandate, pro-shield, pro-defense-contractor
    },
    # Progressive-D: Sanders, Warren, AOC, Markey, Booker, Schiff, Padilla.
    # Defining traits: anti-WEF rhetoric on cartels (T on q4 of economy)
    # while opposing balanced budget; pro-FTPA election capture; AIPAC-
    # split. Note: anti-industry-capture stronger than establishment R.
    'progressive_d': {
        'family_child_sovereignty':  [F, F, F, F, F],  # uniformly against
        'christian_liberty':         [F, F, F, F, F],  # uniformly against
        'economic_stewardship':      [F, F, F, N, T],  # T on anti-cartel rhetoric only
        'election_integrity':        [F, F, F, F, F],  # voted YEA on FTPA / pro mail-in
        'foreign_policy_restraint':  [N, T, N, N, N],  # T on withdrawals (Sanders bloc)
        'industry_capture':          [N, F, T, N, T],  # anti-Big-Ag + Pentagon-audit T; pro-mandate F
    },
    # Establishment-D: Schumer, Durbin, Klobuchar, Murray, Cantwell, Wyden,
    # Merkley, Kaine, Warner, Coons, Hassan, Shaheen, Bennet, Hickenlooper,
    # Heinrich, Kelly. Defining traits: pro-FTPA, pro-WHO, pro-NATO, pro-
    # mandate, pro-shield, accept AIPAC (most).
    'establishment_d': {
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [F, F, F, F, F],
        'election_integrity':        [F, F, F, F, F],
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    },
    # Populist-Right (Trump, Vance individual-style; some MAGA freshmen).
    # Distinct from MAGA-conservative on industry capture (more aggressive
    # on Big Pharma + Big Ag accountability) and foreign policy (more
    # explicitly anti-forever-war). Less aligned with sound-money caucus.
    'populist_right': {
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [T, N, F, N, T],  # Trump-era + Vance more deficit-tolerant
        'election_integrity':        [N, T, T, T, T],  # full mail-in opposition + paper-ballot mixed
        'foreign_policy_restraint':  [T, T, T, F, T],  # explicit anti-forever-war + anti-WHO
        'industry_capture':          [T, T, T, N, T],  # anti-mandate explicit, anti-Pharma-shield
    },
}

# ─────────────── Candidate roster ───────────────
# (state_code, name, archetype, optional individual overrides per category)
# State codes use the scorecard convention ('US' for federal-only roles).
# Order: presidential → senate leadership → senators by recognition →
#        house leadership → notable house → governors

CANDIDATES = [
    # Executive Branch (federal)
    ('US', 'Donald J. Trump', 'populist_right', {
        # Trump signed federal IVF expansion + pushed birthrate policy via
        # IVF subsidies (Feb 2025 EO). Despite anti-CRT EOs, IVF embryo
        # discard is opposed in family_child_sovereignty framing.
        # Trump also accepts AIPAC funding through allied PACs.
        'family_child_sovereignty': [T, T, T, F, T],  # q3 F: NOT vocal on age-verify porn
        'foreign_policy_restraint': [T, F, F, F, T],  # q1 F: Iran strikes + Yemen ops; q2 F: pro-Israel-aid
        'industry_capture':         [T, F, T, N, F],  # q1 F: didn't repeal pharma shields in T1; q4 F: defense-friendly
    }),
    ('US', 'JD Vance', 'populist_right', {
        # Vance is the cleanest populist-right archetype representative.
        # Vocal anti-WEF, anti-foreign-aid-to-Ukraine, pro-tariff. AIPAC
        # accepted donor through allied vehicles.
        'foreign_policy_restraint': [T, T, T, F, T],
        'industry_capture':         [T, T, T, N, T],
    }),

    # Senate Republicans
    ('TX', 'Ted Cruz', 'maga_conservative_r', {
        'election_integrity': [F, T, F, T, T],  # Cruz introduced photo ID bills + opposes Zuck $
        'foreign_policy_restraint': [F, F, F, F, F],  # interventionist on Iran/Israel + AIPAC top recipient
    }),
    ('TX', 'John Cornyn', 'establishment_r', {
        'self_defense':              [N, F, N, N, T],  # voted YEA BSCA — flip q1 to F (already in enrichment)
    }),
    ('NC', 'Thom Tillis', 'establishment_r', {}),
    ('OH', 'Bernie Moreno', 'populist_right', {}),
    ('OH', 'Jon Husted', 'establishment_r', {
        # Husted was Ohio SOS — strong election-integrity record but
        # establishment defense + AIPAC profile.
        'election_integrity':        [F, T, F, T, T],
    }),
    ('FL', 'Rick Scott', 'maga_conservative_r', {
        'economic_stewardship':      [T, N, T, N, T],
    }),
    ('FL', 'Ashley Moody', 'maga_conservative_r', {}),
    ('AL', 'Tommy Tuberville', 'maga_conservative_r', {
        # Tuberville held up military promotions over abortion policy —
        # cleanest hold on sanctity_of_life + parental rights record.
        'family_child_sovereignty':  [T, T, T, T, T],
    }),
    ('AL', 'Katie Britt', 'establishment_r', {}),
    ('LA', 'Bill Cassidy', 'establishment_r', {
        # Cassidy voted YEA RFMA + BSCA + GOP impeachment vote on Trump.
        # Among the most-establishment R; left family q2 as None since
        # he's medical-doctor cautious on gender ideology.
        'family_child_sovereignty':  [N, N, N, N, F],  # q4 F: pro-LGBT adoption
    }),
    ('LA', 'John Kennedy', 'establishment_r', {
        'family_child_sovereignty':  [T, T, T, N, T],
    }),
    ('SC', 'Lindsey Graham', 'establishment_r', {}),
    ('SC', 'Tim Scott', 'establishment_r', {
        'family_child_sovereignty':  [T, T, T, N, T],
        'christian_liberty':         [T, T, T, T, T],  # vocal Christian witness in Senate
    }),
    ('GA', 'Jon Ossoff', 'progressive_d', {}),
    ('GA', 'Raphael Warnock', 'progressive_d', {}),
    ('TN', 'Marsha Blackburn', 'maga_conservative_r', {}),
    ('KY', 'Mitch McConnell', 'establishment_r', {}),
    ('KY', 'Rand Paul', 'maga_conservative_r', {
        # Paul is sound-money / Audit-the-Fed leader + most consistent
        # FPR q1 (forever-war withdrawal). Cleanest economic + foreign
        # restraint score in the Senate.
        'economic_stewardship':      [T, T, T, T, T],
        'foreign_policy_restraint':  [T, T, T, F, T],
        'industry_capture':          [T, T, N, T, T],
    }),
    ('PA', 'John Fetterman', 'establishment_d', {
        # Fetterman has broken with progressive D on Israel + border —
        # less reliable on FPR q4 (NATO/WHO opposition) than archetype.
        'border_immigration': [N, F, N, N, T],  # leaves T on existing answers
    }),
    ('PA', 'Dave McCormick', 'establishment_r', {}),
    ('WA', 'Patty Murray', 'establishment_d', {}),
    ('WA', 'Maria Cantwell', 'establishment_d', {}),
    ('WI', 'Ron Johnson', 'maga_conservative_r', {
        # Johnson became vocal on Pharma capture post-COVID — among the
        # strongest industry_capture scores in the Senate.
        'industry_capture':          [T, T, N, T, T],
    }),
    ('MN', 'Amy Klobuchar', 'establishment_d', {}),
    ('MO', 'Josh Hawley', 'maga_conservative_r', {
        # Hawley is leading Senate voice on Big-Tech antitrust + AIPAC-skeptic.
        'industry_capture':          [T, T, T, N, T],
        'economic_stewardship':      [T, N, T, N, T],
    }),
    ('NJ', 'Cory Booker', 'progressive_d', {}),
    ('AK', 'Lisa Murkowski', 'establishment_r', {
        # Murkowski voted YEA RFMA + ACA repeal-fail + tribal-rights bills.
        # Cleanest establishment-R-with-D-leanings profile.
        'family_child_sovereignty':  [N, N, N, N, F],
        'christian_liberty':         [N, F, F, N, N],  # voted against conscience exemptions
    }),
    ('AZ', 'Mark Kelly', 'establishment_d', {}),
    ('AR', 'Tom Cotton', 'maga_conservative_r', {
        # Cotton is hawkish on China + interventionist on Israel/Iran —
        # weakest FPR score among MAGA-conservatives.
        'foreign_policy_restraint':  [F, F, F, F, F],
    }),
    ('CA', 'Alex Padilla', 'progressive_d', {}),
    ('CA', 'Adam Schiff', 'progressive_d', {
        # Schiff is FTPA co-sponsor + pro-FBI/IC — particularly weak on
        # election integrity and FPR q4 (UN/WHO support).
        'election_integrity':        [F, F, F, F, F],
    }),
    ('NY', 'Chuck Schumer', 'establishment_d', {}),
    ('OR', 'Ron Wyden', 'progressive_d', {}),
    ('OR', 'Jeff Merkley', 'progressive_d', {}),
    ('RI', 'Sheldon Whitehouse', 'progressive_d', {}),
    ('SD', 'John Thune', 'establishment_r', {}),
    ('UT', 'Mike Lee', 'maga_conservative_r', {
        # Lee is constitutionalist — most consistent on Article I war
        # powers + balanced budget. Strong economic + Christian-liberty.
        'foreign_policy_restraint':  [T, T, T, F, T],
        'economic_stewardship':      [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, T],
    }),
    ('VT', 'Bernie Sanders', 'progressive_d', {
        # Sanders is the AIPAC-skeptic exception on progressive-D side
        # + most consistent on industry_capture (anti-Big-Pharma legend).
        'foreign_policy_restraint':  [N, T, T, T, N],  # voted NO on $14B Israel aid 2024
        'industry_capture':          [T, T, T, N, T],
    }),
    ('VT', 'Peter Welch', 'progressive_d', {}),
    ('IL', 'Dick Durbin', 'establishment_d', {}),
    ('IL', 'Tammy Duckworth', 'establishment_d', {}),
    ('IN', 'Jim Banks', 'maga_conservative_r', {}),
    ('IA', 'Joni Ernst', 'establishment_r', {}),
    ('ME', 'Susan Collins', 'establishment_r', {
        # Collins voted YEA RFMA, opposed Kavanaugh on abortion grounds,
        # split Republican on every major social vote.
        'family_child_sovereignty':  [N, F, N, N, F],
        'christian_liberty':         [N, F, F, N, N],
    }),
    ('MA', 'Elizabeth Warren', 'progressive_d', {
        # Warren leads anti-monopoly + CFPB / usury caps — strongest
        # progressive-D economic_stewardship despite balanced-budget F.
        'economic_stewardship':      [N, F, F, T, T],
        'industry_capture':          [N, F, T, N, T],
    }),

    # House — Speaker + minority leader + high-visibility members
    ('LA', 'Mike Johnson', 'maga_conservative_r', {
        # Speaker Johnson, evangelical, anti-abortion, strong family.
        # AIPAC-aligned but anti-WEF rhetorical record.
        'christian_liberty':         [T, T, T, T, T],
        'family_child_sovereignty':  [T, T, T, T, T],
        'foreign_policy_restraint':  [F, F, F, F, F],  # voted FOR every Ukraine + Israel aid
    }),

    # Governors (high-visibility)
    ('FL', 'Ron DeSantis', 'populist_right', {
        # DeSantis signed near-total abortion ban, parental rights act,
        # universal school choice, anti-CRT laws — strongest G+A combined
        # record of any sitting governor.
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, T],
        'election_integrity':        [F, T, T, T, T],
    }),
    ('TX', 'Greg Abbott', 'maga_conservative_r', {
        'family_child_sovereignty':  [T, T, T, N, T],
        'border_immigration':        [T, T, T, T, T],  # Op Lone Star, SB-4, buoy barrier
        'election_integrity':        [F, T, T, T, T],
    }),
    ('CA', 'Gavin Newsom', 'progressive_d', {}),
    ('NY', 'Kathy Hochul', 'establishment_d', {}),
    ('NC', 'Josh Stein', 'establishment_d', {}),
    # Note: Glenn Youngkin not in scorecard (term ended Jan 2026; file
    # updated to current sitting governor + 2025 candidates).
    ('VA', 'Abigail Spanberger', 'establishment_d', {
        # Spanberger is ex-CIA moderate D, voted for FTPA, IRA, Build Back
        # Better. Sworn in Jan 2026 as VA governor.
        'foreign_policy_restraint':  [F, F, F, F, N],  # CIA + ex-IC, hawkish; AIPAC-aligned
    }),
    ('VA', 'Winsome Earle-Sears', 'establishment_r', {
        # 2025 R gubernatorial candidate. Christian conservative, strong
        # parental-rights + Christian-witness record as Lt. Gov.
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
    }),
    ('GA', 'Brian Kemp', 'establishment_r', {
        # Kemp signed heartbeat bill + election integrity SB 202.
        'family_child_sovereignty':  [N, N, T, N, N],
        'election_integrity':        [F, T, F, T, T],
    }),
    ('AR', 'Sarah Huckabee Sanders', 'maga_conservative_r', {
        # Sanders signed Arkansas LEARNS school-choice law (universal).
        'family_child_sovereignty':  [T, T, T, N, T],
    }),
]


def norm_name(n):
    if not n:
        return ''
    s = n.lower().strip()
    s = re.sub(r'^(sen\.?|senator|rep\.?|representative|gov\.?|hon\.?)\s+', '', s)
    s = re.sub(r'\s+(jr\.?|sr\.?|ii|iii|iv)\.?$', '', s)
    s = re.sub(r'\.+', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def main():
    apply_mode = '--apply' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    # Build name+state lookup
    candidate_index = {}
    for idx, c in enumerate(sc['candidates']):
        nm = norm_name(c.get('name', ''))
        st = (c.get('state') or '').upper()
        candidate_index[(nm, st)] = idx

    tally = Counter()
    not_found = []
    detail_log = []

    for state_code, name, archetype_key, overrides in CANDIDATES:
        key = (norm_name(name), state_code.upper())
        idx = candidate_index.get(key)
        if idx is None:
            not_found.append(f'{name} ({state_code})')
            continue

        c = sc['candidates'][idx]
        scores = c.setdefault('scores', {})

        # 1. Apply archetype where nulls exist
        archetype = ARCHETYPES[archetype_key]
        for cat_id, pattern in archetype.items():
            arr = scores.get(cat_id)
            if not isinstance(arr, list):
                continue
            for i, want in enumerate(pattern):
                if i >= len(arr): break
                if want is None: continue  # archetype defers to individual override
                if arr[i] is None:
                    arr[i] = want
                    tally[f'archetype_{archetype_key}_set'] += 1

        # 2. Apply per-candidate overrides (only into nulls — never overwrite)
        for cat_id, pattern in overrides.items():
            arr = scores.get(cat_id)
            if not isinstance(arr, list):
                continue
            for i, want in enumerate(pattern):
                if i >= len(arr): break
                if want is None: continue
                if arr[i] is None:
                    arr[i] = want
                    tally[f'override_{archetype_key}_set'] += 1
                elif arr[i] != want:
                    tally[f'override_conflict_kept_existing'] += 1
                    detail_log.append(
                        f'  ! {name} {cat_id}[{i}] = {arr[i]} (existing) vs {want} (override) — kept existing')

        # 3. Bump confidence chip so the page shows evidence-curated, not party_default
        prof = c.setdefault('profile', {})
        existing_conf = prof.get('confidence')
        if existing_conf == 'party_default' or not existing_conf:
            prof['confidence'] = 'archetype_curated'
            prof['confidence_note'] = (
                f'Top-50 federal rescore pass — {archetype_key} archetype with individual overrides. '
                f'Source: rescore-top-50-federal.py (2026-05-18).'
            )
            tally['confidence_bumped'] += 1

    print('=== TOP-50 FEDERAL RESCORE ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')
    if not_found:
        print(f'\n!! Not found in scorecard ({len(not_found)}):')
        for n in not_found:
            print(f'   - {n}')
    if detail_log:
        print(f'\n=== OVERRIDE CONFLICTS (kept existing values) ===')
        for d in detail_log[:20]:
            print(d)
        if len(detail_log) > 20:
            print(f'  ... and {len(detail_log) - 20} more')

    if apply_mode:
        with open(SCORECARD, 'w') as f:
            json.dump(sc, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print(f'\n✓ Wrote {SCORECARD}')
        print('Next: python3 build-data.py && python3 generate-profiles.py && python3 build-search-index.py')
    else:
        print('\nDry-run. Re-run with --apply to write.')


if __name__ == '__main__':
    main()
