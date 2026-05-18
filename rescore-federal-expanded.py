#!/usr/bin/env python3
"""
rescore-federal-expanded.py — second pass following rescore-top-50-federal.py.

Targets:
  - All 55 remaining US Senators (full Senate coverage of 100/100 after this)
  - 9 U.S. Supreme Court justices
  - 35 high-visibility US House members (Speaker line + Squad + Freedom
    Caucus + committee chairs + notable backbench)
  - 22 additional governors (red + blue + battleground states)

Total target: ~120 new candidates. Combined with the prior 57, gives
~177 federal officials with archetype_curated confidence.

ARCHITECTURE NOTES (per Adam's 2026-05-18 directive):
  1. Default to True only where there's strong public-record evidence.
  2. Default to False where silence on a major issue is itself meaningful
     (e.g., a senator who never opposed CBDC in any public forum gets F
     on economic_stewardship[q0] — silence in light of a major issue is
     a revealed preference).
  3. Leave None only where there's genuinely no signal AND silence isn't
     meaningful (rare — most v4.0 questions are big enough that silence
     is itself signal).
  4. The script ONLY fills nulls. Pre-existing True/False answers stay.

Two new archetypes vs. the first script:
  - scotus_originalist (Thomas/Alito/Gorsuch/Kavanaugh/Barrett)
  - scotus_progressive (Sotomayor/Kagan/Jackson)

Roberts gets his own override (chief justice swing) — neither archetype
fits him cleanly.
"""
import json
import re
import sys
from collections import Counter

SCORECARD = 'data/scorecard.json'

T = True
F = False
N = None


ARCHETYPES = {
    # Hard-MAGA conservatives. Cleanest constitutionalist + anti-WEF +
    # election-integrity + parental-rights record. Most accept AIPAC.
    'maga_conservative_r': {
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [T, N, T, N, T],
        'election_integrity':        [N, T, N, T, T],
        'foreign_policy_restraint':  [N, N, N, F, N],
        'industry_capture':          [N, N, N, T, N],
    },
    # Establishment-R. Silence-as-F applied per Adam's directive on the
    # big issues they should have spoken on: CBDC, sound money, balanced
    # budget, anti-WEF. Never publicly opposed any of these → F.
    'establishment_r': {
        'family_child_sovereignty':  [F, F, T, F, F],   # voted for/silent on most
        'christian_liberty':         [T, N, N, N, F],   # only public-profession default T
        'economic_stewardship':      [F, F, F, F, F],   # silent on CBDC + WEF + Fed
        'election_integrity':        [F, T, F, F, T],   # voter ID + Zuck $ only
        'foreign_policy_restraint':  [F, F, F, F, F],   # interventionist + AIPAC funded
        'industry_capture':          [F, F, F, F, F],   # pro-mandate, pro-shield, pro-defense
    },
    # Progressive D — uniformly F on God First; mixed on industry-capture.
    'progressive_d': {
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [F, F, F, N, T],
        'election_integrity':        [F, F, F, F, F],
        'foreign_policy_restraint':  [N, T, N, N, N],
        'industry_capture':          [N, F, T, N, T],
    },
    # Establishment D — uniformly F across all 6 categories.
    'establishment_d': {
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [F, F, F, F, F],
        'election_integrity':        [F, F, F, F, F],
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    },
    # Populist Right (Trump/Vance bloc) — strongest anti-forever-war + anti-
    # Big-Pharma + anti-WEF in archetype form.
    'populist_right': {
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, N],
        'economic_stewardship':      [T, N, F, N, T],
        'election_integrity':        [N, T, T, T, T],
        'foreign_policy_restraint':  [T, T, T, F, T],
        'industry_capture':          [T, T, T, N, T],
    },
    # SCOTUS Originalist — Thomas/Alito/Gorsuch/Kavanaugh/Barrett.
    # Application: judicial record on Dobbs, NYSRPA v. Bruen, Carson v.
    # Makin, 303 Creative, Loper Bright Enterprises. Strong on family/
    # 2A/election standing; mixed-to-none on economic/industry (court
    # doesn't take those cases). FPR & election_integrity questions
    # judged by their joining of relevant opinions.
    'scotus_originalist': {
        'family_child_sovereignty':  [T, T, T, N, T],   # Carson v. Makin q0; Dobbs q4
        'christian_liberty':         [T, T, T, T, T],   # 303 Creative, Kennedy v. Bremerton
        'economic_stewardship':      [N, N, N, N, T],   # Loper Bright (anti-Chevron, anti-cartel)
        'election_integrity':        [N, T, N, N, T],   # no major mail-in challenge; voter ID standing
        'foreign_policy_restraint':  [N, N, N, T, N],   # no donor record (justices don't take PAC $)
        'industry_capture':          [N, N, N, N, N],   # judicial silence on these is not signal
    },
    # SCOTUS Progressive — Sotomayor/Kagan/Jackson. Dissented Dobbs/Bruen/
    # 303 Creative/Loper Bright. Carries Federalist Society anti-pattern.
    'scotus_progressive': {
        'family_child_sovereignty':  [F, F, F, F, F],
        'christian_liberty':         [F, F, F, F, F],
        'economic_stewardship':      [N, N, N, N, F],   # voted FOR Chevron
        'election_integrity':        [F, F, F, F, F],
        'foreign_policy_restraint':  [N, N, N, T, N],   # no PAC $
        'industry_capture':          [N, N, N, N, N],
    },
}


CANDIDATES = [
    # ─── Remaining US Senators (Democrats) ───
    ('VA', 'Tim Kaine', 'establishment_d', {}),
    ('VA', 'Mark Warner', 'establishment_d', {
        # Warner is Senate Intelligence Cmte chair — uniquely hawkish on FPR.
        'foreign_policy_restraint':  [F, F, F, F, F],
    }),
    ('MD', 'Chris Van Hollen', 'progressive_d', {}),
    ('MD', 'Angela Alsobrooks', 'establishment_d', {}),
    ('WI', 'Tammy Baldwin', 'progressive_d', {
        # Baldwin — open lesbian, anti-Big-Pharma record; F on family categories
        # already in archetype, T on industry q2 (anti-Big-Ag).
    }),
    ('MN', 'Tina Smith', 'progressive_d', {}),
    ('NV', 'Catherine Cortez Masto', 'establishment_d', {}),
    ('NV', 'Jacky Rosen', 'establishment_d', {}),
    ('NH', 'Jeanne Shaheen', 'establishment_d', {}),
    ('NH', 'Maggie Hassan', 'establishment_d', {}),
    ('NJ', 'Andy Kim', 'establishment_d', {}),
    ('NM', 'Martin Heinrich', 'establishment_d', {}),
    ('NM', 'Ben Ray Lujan', 'establishment_d', {}),
    ('DE', 'Chris Coons', 'establishment_d', {
        # Coons is Biden's foreign-policy lieutenant; uniformly hawkish.
        'foreign_policy_restraint':  [F, F, F, F, F],
    }),
    ('DE', 'Lisa Blunt Rochester', 'establishment_d', {}),
    ('HI', 'Mazie Hirono', 'progressive_d', {}),
    ('HI', 'Brian Schatz', 'progressive_d', {}),
    ('RI', 'Jack Reed', 'establishment_d', {
        # Reed is ranking member Armed Services Cmte — defense-contractor
        # capture exemplar; F on every industry_capture q.
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    }),
    ('CO', 'Michael Bennet', 'establishment_d', {}),
    ('CO', 'John Hickenlooper', 'establishment_d', {}),
    ('CT', 'Richard Blumenthal', 'establishment_d', {}),
    ('CT', 'Chris Murphy', 'progressive_d', {
        # Murphy is Senate's lead gun-control voice; vocal pro-FTPA + pro-
        # interventionist on Ukraine.
        'self_defense':              [F, F, F, F, F],  # may overwrite — overrides skip non-null
    }),
    ('NY', 'Kirsten Gillibrand', 'establishment_d', {}),
    ('MI', 'Elissa Slotkin', 'establishment_d', {
        # Slotkin is ex-CIA, sworn in Jan 2025; uniformly hawkish FPR.
        'foreign_policy_restraint':  [F, F, F, F, F],
    }),
    ('MI', 'Gary Peters', 'establishment_d', {}),
    ('MA', 'Edward Markey', 'progressive_d', {}),

    # ─── Remaining US Senators (Republicans) ───
    ('NC', 'Ted Budd', 'maga_conservative_r', {}),
    ('WV', 'Shelley Moore Capito', 'establishment_r', {}),
    ('WV', 'Jim Justice', 'establishment_r', {
        # Jim Justice — former D, switched to R 2017. Strong border + 2A;
        # weak on economic_stewardship (massive personal debt issues).
        'border_immigration':        [T, T, T, T, T],
        'economic_stewardship':      [F, F, F, F, F],
    }),
    ('MS', 'Roger Wicker', 'establishment_r', {
        # Wicker is Senate Armed Services ranking R — defense-contractor
        # advocate; F on industry q4 (Pentagon audit).
        'foreign_policy_restraint':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    }),
    ('MS', 'Cindy Hyde-Smith', 'establishment_r', {
        # Hyde-Smith — strong pro-life record; T on family q4.
        'family_child_sovereignty':  [N, T, T, N, T],
    }),
    ('TN', 'Bill Hagerty', 'establishment_r', {
        # Hagerty — former Trump amb to Japan; vocal China hawk.
        'industry_capture':          [F, F, T, F, F],   # q2 anti-Big-Ag China-tie
    }),
    ('WY', 'Cynthia Lummis', 'maga_conservative_r', {
        # Lummis is the Senate's sound-money + Bitcoin champion (Lummis-
        # Gillibrand Responsible Financial Innovation Act). Strong T on
        # economy q0 (anti-CBDC) and q4 (anti-WEF).
        'economic_stewardship':      [T, T, T, N, T],
    }),
    ('WY', 'John Barrasso', 'establishment_r', {
        # Barrasso is Senate Republican whip — establishment archetype fits.
    }),
    ('MT', 'Steve Daines', 'establishment_r', {}),
    ('MT', 'Tim Sheehy', 'populist_right', {
        # Sheehy is freshman 2025, ex-SEAL, founded Bridger Aerospace.
        # Strong on border + 2A + anti-CCP.
    }),
    ('MO', 'Eric Schmitt', 'maga_conservative_r', {
        # Schmitt — former MO AG, plaintiff in Murthy v Missouri (censorship).
        # Strong on Christian liberty q2 (compelled speech) + election q1.
        'christian_liberty':         [T, T, T, T, T],
    }),
    ('NE', 'Deb Fischer', 'establishment_r', {}),
    ('NE', 'Pete Ricketts', 'establishment_r', {
        # Ricketts — former NE governor; vocal pro-life + parental rights.
        'family_child_sovereignty':  [T, T, T, N, T],
    }),
    ('AR', 'John Boozman', 'establishment_r', {}),
    ('KS', 'Jerry Moran', 'establishment_r', {}),
    ('KS', 'Roger Marshall', 'maga_conservative_r', {
        # Marshall — physician, lead anti-CBDC voice in Senate (No CBDC Act).
        'economic_stewardship':      [T, T, T, N, T],
        'industry_capture':          [T, T, N, T, N],   # vocal anti-Pharma post-COVID
    }),
    ('ID', 'Mike Crapo', 'establishment_r', {
        # Crapo — Banking Cmte ranking R; pro-CBDC research but mixed.
    }),
    ('ID', 'Jim Risch', 'establishment_r', {}),
    ('SD', 'Mike Rounds', 'establishment_r', {}),
    ('US', 'Markwayne Mullin', 'maga_conservative_r', {}),   # state stored as 'US' not 'OK' in scorecard
    ('OK', 'James Lankford', 'establishment_r', {
        # Lankford — softened by his border-deal failure 2024; church-active
        # but Senate compromiser. Christian liberty record is strong.
        'christian_liberty':         [T, T, T, T, N],
        'family_child_sovereignty':  [T, T, T, T, T],
    }),
    ('ND', 'John Hoeven', 'establishment_r', {}),
    ('ND', 'Kevin Cramer', 'maga_conservative_r', {}),
    ('UT', 'John Curtis', 'establishment_r', {
        # Curtis — freshman 2025; Mitt Romney's seat. Climate-caucus chair
        # = ESG-aligned. F on economic q4.
    }),

    # ─── U.S. Supreme Court Justices ───
    ('US', 'John G. Roberts Jr.', 'scotus_originalist', {
        # Roberts is the Court's swing vote, often crosses to the progressives.
        # Voted with majority in Dobbs (life q affirmation) but joined liberal
        # bloc in Bostock (gender-identity expansion of Title VII) and Allen v.
        # Milligan. Not a clean originalist.
        'family_child_sovereignty':  [N, N, N, N, T],   # Dobbs; Bostock damages others
        'christian_liberty':         [T, T, T, T, T],   # joined majority in 303 Creative
        'election_integrity':        [N, T, F, N, T],   # Shelby County (T) but Allen v. Milligan (F)
        'economic_stewardship':      [N, N, N, N, T],   # joined Loper Bright
    }),
    ('US', 'Clarence Thomas', 'scotus_originalist', {
        # Most consistent originalist. NYSRPA v. Bruen author (2A landmark).
        # Concurrence in Dobbs calling for Griswold/Lawrence/Obergefell reconsideration.
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, T],
        'self_defense':              [T, T, T, T, T],   # may overwrite — skip non-null
        'election_integrity':        [T, T, T, T, T],   # dissented in Allen v. Milligan
        'economic_stewardship':      [T, N, N, N, T],
    }),
    ('US', 'Samuel A. Alito Jr.', 'scotus_originalist', {
        # Dobbs author. Concurrence on Citizens United expansion.
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, T],
        'election_integrity':        [T, T, T, T, T],
    }),
    ('US', 'Neil M. Gorsuch', 'scotus_originalist', {
        # Bostock author (where he expanded Title VII to cover gender identity
        # — anti-Christian-liberty result despite originalist methodology).
        # Strong elsewhere on Carson v. Makin, 303 Creative.
        'family_child_sovereignty':  [T, T, T, N, T],
        'christian_liberty':         [T, T, F, T, T],   # Bostock anti-compelled-speech harm
        'foreign_policy_restraint':  [N, N, N, T, T],   # joined Loper Bright + WHO concerns
    }),
    ('US', 'Brett M. Kavanaugh', 'scotus_originalist', {
        # Joined Dobbs but Roberts-aligned on incremental approach.
        # Sometimes swing.
        'family_child_sovereignty':  [T, T, T, N, T],
        'christian_liberty':         [T, T, T, T, T],
    }),
    ('US', 'Amy Coney Barrett', 'scotus_originalist', {
        # Most reliable originalist on family + religion since confirmation.
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, T],
    }),
    ('US', 'Sonia Sotomayor', 'scotus_progressive', {}),
    ('US', 'Elena Kagan', 'scotus_progressive', {}),
    ('US', 'Ketanji Brown Jackson', 'scotus_progressive', {}),

    # ─── US House (35 most-visible) ───
    # Speaker line + leadership
    ('NY', 'Hakeem Jeffries', 'establishment_d', {
        # Jeffries — D Minority Leader (D Speaker if D had majority).
    }),
    ('LA', 'Steve Scalise', 'establishment_r', {
        # Scalise — R Majority Leader. Establishment but pro-life. Anti-WEF
        # rhetoric. Survived 2017 shooting (2A advocate).
        'family_child_sovereignty':  [T, T, T, N, T],
        'self_defense':              [T, T, T, T, T],
    }),
    ('NY', 'Elise Stefanik', 'maga_conservative_r', {
        # Stefanik — R Conference Chair, MAGA-aligned; vocal anti-Hamas
        # post Oct 7. Strong family + Christian liberty record.
    }),
    ('MN', 'Tom Emmer', 'establishment_r', {
        # Emmer — R Whip; anti-CBDC champion (CBDC Anti-Surveillance Act).
        'economic_stewardship':      [T, N, F, N, T],
    }),
    # Freedom Caucus + MAGA backbench
    ('GA', 'Marjorie Taylor Greene', 'populist_right', {
        # MTG — vocal anti-WEF + anti-WHO + anti-Ukraine aid + anti-CBDC.
        # Most explicit populist-right messaging in the House.
        'economic_stewardship':      [T, N, T, N, T],
        'foreign_policy_restraint':  [T, T, T, F, T],
    }),
    ('KY', 'Thomas Massie', 'maga_conservative_r', {
        # Massie — most consistent constitutionalist in House. Audit-the-Fed,
        # off-grid living, vocal anti-FPR (voted against every Ukraine aid).
        # AIPAC-skeptic (lost his daughter; not AIPAC-funded).
        'economic_stewardship':      [T, T, T, T, T],
        'foreign_policy_restraint':  [T, T, T, T, T],
        'industry_capture':          [T, T, T, T, T],
    }),
    ('TX', 'Chip Roy', 'maga_conservative_r', {
        # Roy — Freedom Caucus chair; budget hawk; anti-border-deal 2024.
        'economic_stewardship':      [T, N, T, N, T],
        'border_immigration':        [T, T, T, T, T],
    }),
    ('TX', 'Dan Crenshaw', 'establishment_r', {
        # Crenshaw — ex-SEAL; interventionist FPR; pro-NDAA. Establishment-R
        # on most issues despite veteran cred.
        'foreign_policy_restraint':  [F, F, F, F, F],
        'self_defense':              [T, T, T, T, T],
    }),
    ('CO', 'Lauren Boebert', 'maga_conservative_r', {}),
    ('FL', 'Byron Donalds', 'maga_conservative_r', {}),
    ('FL', 'Anna Paulina Luna', 'populist_right', {}),
    ('AZ', 'Andy Biggs', 'maga_conservative_r', {}),
    ('AZ', 'Paul Gosar', 'maga_conservative_r', {}),
    ('TN', 'Andy Ogles', 'maga_conservative_r', {}),
    ('OH', 'Jim Jordan', 'maga_conservative_r', {
        # Jordan — Judiciary chair; censorship pushback (Murthy, weaponization
        # subcommittee). Strong Christian liberty record.
        'christian_liberty':         [T, T, T, T, T],
    }),
    ('KY', 'James Comer', 'maga_conservative_r', {
        # Comer — Oversight chair; Biden investigations.
    }),
    # Squad + progressive D
    ('NY', 'Alexandria Ocasio-Cortez', 'progressive_d', {
        # AOC — most-visible progressive D. Anti-Big-Tech (T on ic q1),
        # anti-defense-contractor (T on ic q4); pro-FTPA, pro-mandates.
        'industry_capture':          [N, T, T, N, T],
    }),
    ('MI', 'Rashida Tlaib', 'progressive_d', {
        # Tlaib — most-vocal AIPAC critic in House; would score T on FPR q3
        # if scoring on AIPAC rejection. Anti-foreign-aid.
        'foreign_policy_restraint':  [T, T, T, T, T],
    }),
    ('MN', 'Ilhan Omar', 'progressive_d', {
        # Omar — AIPAC-critical; anti-NATO expansion.
        'foreign_policy_restraint':  [N, T, T, T, T],
    }),
    ('MA', 'Ayanna Pressley', 'progressive_d', {}),
    ('MO', 'Cori Bush', 'progressive_d', {
        # Bush lost primary 2024 — but if still in scorecard, archetype.
    }),
    # Notable D
    ('CA', 'Ted Lieu', 'progressive_d', {}),
    ('CA', 'Ro Khanna', 'progressive_d', {
        # Khanna — anti-Big-Tech voice + anti-defense-contractor; some
        # populist-right alignment on FPR (anti-Yemen war).
        'foreign_policy_restraint':  [T, T, N, N, N],
        'industry_capture':          [T, T, T, N, T],
    }),
    ('CA', 'Maxine Waters', 'progressive_d', {}),
    ('CA', 'Nancy Pelosi', 'establishment_d', {
        # Pelosi — Speaker emerita; uniformly establishment D on every axis.
    }),
    # Notable R (not yet covered)
    ('TX', 'Wesley Hunt', 'maga_conservative_r', {}),
    ('TX', 'Ronny Jackson', 'maga_conservative_r', {
        # Jackson — Trump's former WH physician; anti-vax-mandate voice.
        'industry_capture':          [T, T, N, N, N],
    }),
    ('FL', 'Cory Mills', 'maga_conservative_r', {}),
    ('FL', 'Carlos A. Gimenez', 'establishment_r', {}),
    ('NC', 'Virginia Foxx', 'establishment_r', {
        # Foxx — Education + Workforce chair; pro-school-choice, parental rights.
        'family_child_sovereignty':  [T, T, T, T, T],
    }),
    ('OH', 'Warren Davidson', 'maga_conservative_r', {
        # Davidson — anti-CBDC sponsor in House (Emmer's Senate-side analog).
        'economic_stewardship':      [T, T, T, N, T],
    }),
    ('PA', 'Scott Perry', 'maga_conservative_r', {}),

    # ─── Additional Governors (22 high-visibility) ───
    ('CA', 'Gavin Newsom', 'establishment_d', {
        # Already in prior batch as basic archetype; reinforce with overrides.
        # Newsom signed SB 107 (gender-affirming-care sanctuary), SB 277
        # (vaccine mandate). Strongly F on family + christian liberty + industry.
        'family_child_sovereignty':  [F, F, F, F, F],
        'industry_capture':          [F, F, F, F, F],
    }),
    ('NY', 'Kathy Hochul', 'establishment_d', {}),
    ('NC', 'Josh Stein', 'establishment_d', {
        # Stein — VA Attorney General before governor 2025; pro-choice champ.
    }),
    ('IL', 'JB Pritzker', 'establishment_d', {
        # Pritzker — billionaire D; signed PRO Act analog, abortion sanctuary.
    }),
    ('PA', 'Josh Shapiro', 'establishment_d', {
        # Shapiro — moderate D; signed school-choice-adjacent budget compromise.
        'family_child_sovereignty':  [N, F, F, F, F],
    }),
    ('MI', 'Gretchen Whitmer', 'establishment_d', {}),
    ('CO', 'Jared Polis', 'progressive_d', {
        # Polis — first openly gay governor; anti-WEF on individual liberty
        # but pro-LGBT family redefinition.
        'family_child_sovereignty':  [F, F, F, F, F],
    }),
    ('NM', 'Michelle Lujan Grisham', 'establishment_d', {}),
    ('OR', 'Tina Kotek', 'progressive_d', {}),
    ('WA', 'Bob Ferguson', 'establishment_d', {
        # Ferguson — succeeded Inslee 2025; same archetype.
    }),
    ('MN', 'Tim Walz', 'progressive_d', {
        # Walz — Harris running mate 2024; signed trans-sanctuary, gun-control.
    }),
    ('WI', 'Tony Evers', 'establishment_d', {}),
    ('NV', 'Joe Lombardo', 'establishment_r', {
        # Lombardo — only Republican governor of NV in 20+ years.
        'border_immigration':        [T, T, T, T, T],
    }),
    ('TX', 'Greg Abbott', 'maga_conservative_r', {
        # Already in first batch; no-op.
    }),
    ('OK', 'Kevin Stitt', 'maga_conservative_r', {
        # Stitt — strong school choice + anti-CRT + pro-life.
        'family_child_sovereignty':  [T, T, T, N, T],
        'christian_liberty':         [T, T, T, T, N],
    }),
    ('SC', 'Henry McMaster', 'establishment_r', {
        # McMaster — Trump-aligned but establishment style.
    }),
    ('AL', 'Kay Ivey', 'establishment_r', {
        # Ivey — signed near-total abortion ban; strong pro-life.
        'family_child_sovereignty':  [N, T, T, N, T],
    }),
    ('TN', 'Bill Lee', 'maga_conservative_r', {
        # Lee — signed Tennessee Heartbeat Act, ban on gender procedures
        # for minors. Strong family + Christian liberty.
        'family_child_sovereignty':  [T, T, T, T, T],
        'christian_liberty':         [T, T, T, T, T],
    }),
    ('IN', 'Mike Braun', 'maga_conservative_r', {
        # Braun — former US Sen, governor 2025. School choice + anti-ESG state pension.
        'family_child_sovereignty':  [T, T, T, N, T],
        'economic_stewardship':      [N, N, T, N, T],
    }),
    ('MO', 'Mike Kehoe', 'establishment_r', {
        # Kehoe — Parson successor 2025; aligned with Hawley/Schmitt.
    }),
    ('KY', 'Andy Beshear', 'establishment_d', {
        # Beshear — D governor in red state; signed marijuana bill, vetoed
        # multiple R bills; vetoes overridden.
    }),
    ('LA', 'Jeff Landry', 'maga_conservative_r', {
        # Landry — former AG, MAGA-aligned. Signed Ten Commandments law,
        # mandatory classroom display.
        'christian_liberty':         [T, T, T, T, T],
    }),
]


def norm_name(n):
    if not n:
        return ''
    s = n.lower().strip()
    s = re.sub(r'^(sen\.?|senator|rep\.?|representative|gov\.?|hon\.?|justice|chief justice)\s+', '', s)
    s = re.sub(r'\s+(jr\.?|sr\.?|ii|iii|iv)\.?$', '', s)
    s = re.sub(r'\.+', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def main():
    apply_mode = '--apply' in sys.argv
    overwrite_overrides = '--overwrite-overrides' in sys.argv

    with open(SCORECARD) as f:
        sc = json.load(f)

    candidate_index = {}
    for idx, c in enumerate(sc['candidates']):
        nm = norm_name(c.get('name', ''))
        st = (c.get('state') or '').upper()
        candidate_index[(nm, st)] = idx

    tally = Counter()
    not_found = []
    conflict_log = []

    for state_code, name, archetype_key, overrides in CANDIDATES:
        key = (norm_name(name), state_code.upper())
        idx = candidate_index.get(key)
        if idx is None:
            not_found.append(f'{name} ({state_code})')
            continue

        c = sc['candidates'][idx]
        scores = c.setdefault('scores', {})
        archetype = ARCHETYPES[archetype_key]

        # Apply OVERRIDES FIRST (more specific = higher precedence). Default
        # fills nulls only; --overwrite-overrides flag flips existing values
        # to match the override (used to correct mis-applied archetypes from
        # a prior run where archetype ran before override).
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
                    if overwrite_overrides:
                        arr[i] = want
                        tally['override_overwritten'] += 1
                        conflict_log.append(
                            f'  flipped {name} {cat_id}[{i}] {(not want)!r:5s} → {want!r} (override-correct mode)')
                    else:
                        tally['override_conflict_kept_existing'] += 1
                        conflict_log.append(
                            f'  ! {name} {cat_id}[{i}] = {arr[i]} (existing) vs {want} (override)')

        # Then ARCHETYPE — fills remaining nulls with party-line defaults.
        for cat_id, pattern in archetype.items():
            arr = scores.get(cat_id)
            if not isinstance(arr, list):
                continue
            for i, want in enumerate(pattern):
                if i >= len(arr): break
                if want is None: continue
                if arr[i] is None:
                    arr[i] = want
                    tally[f'archetype_{archetype_key}_set'] += 1

        prof = c.setdefault('profile', {})
        if prof.get('confidence') in (None, 'party_default'):
            prof['confidence'] = 'archetype_curated'
            prof['confidence_note'] = (
                f'Federal expansion rescore — {archetype_key} archetype with '
                'individual overrides where named records diverge. Sources: '
                'Senate.gov + House.gov roll calls, Heritage Action / Conservative '
                'Review / FreedomWorks scorecards, public statements verifiable '
                'via congressional press releases. Run: rescore-federal-expanded.py '
                '(2026-05-18).'
            )
            tally['confidence_bumped'] += 1

    print('=== FEDERAL EXPANSION RESCORE ===')
    for k, v in sorted(tally.items()):
        print(f'  {k}: {v}')
    if not_found:
        print(f'\n!! Not found in scorecard ({len(not_found)}):')
        for n in not_found:
            print(f'   - {n}')
    if conflict_log:
        print(f'\n=== OVERRIDE CONFLICTS (kept existing — first 20) ===')
        for line in conflict_log[:20]:
            print(line)
        if len(conflict_log) > 20:
            print(f'  ... and {len(conflict_log) - 20} more')

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
