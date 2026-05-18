#!/usr/bin/env python3
"""
build-category-pages.py — generate 10 per-category deep-dive pages under
/citizen/<slug>.html. Each page is a focused (~1-page) explainer:
  • Hero with tier badge + the 10-pt allocation
  • What this measures (description)
  • Why it matters (Christian-framework rationale + Scripture anchor)
  • The 5 scored questions (verbatim from index.json)
  • Key bills, votes, organizations, and orgs we track
  • Methodology link + back to scorecard

Adam's brief: "don't need to be super long but I'd be happy for you to spend
an hour on each of them and then we have a source for our scoring."
Output: under 250 lines each, focused content, silver palette matching
the rest of usmcmin.com.

Run from repo root:
    python3 build-category-pages.py
"""
import os
import re

OUT_DIR = 'citizen'

# Each category gets the rubric fields PLUS extra editorial fields:
# - tier: "god_first" | "america_first"
# - scripture: anchor verse with reference
# - why_it_matters: 2-3 sentence rationale
# - key_bills: list of (label, description) tuples
# - key_orgs: list of (label, description) tuples
# - disqualifiers: list of position-strings that fail the category outright
CATEGORIES = [
    {
        'slug': 'sanctity-of-life',
        'id': 'sanctity_of_life',
        'tier': 'god_first',
        'tier_pts': 60,
        'num': 1,
        'label': 'Sanctity of Life',
        'tagline': 'Personhood from conception. No carve-outs.',
        'description': 'Does this candidate affirm full personhood from conception and oppose abortion, infanticide, euthanasia, and embryonic experimentation?',
        'scripture': ('Psalm 139:13–16', 'For You formed my inward parts; You wove me in my mother\'s womb. I will give thanks to You, for I am fearfully and wonderfully made.'),
        'why_it_matters': (
            'The line between civilization and barbarism is drawn at the womb. A regime that '
            'permits the deliberate killing of pre-born image-bearers (Genesis 1:27) has '
            'abdicated the first duty of righteous government (Romans 13:4). Every other '
            'category in this scorecard is downstream of this one — a candidate who cannot '
            'protect the unborn cannot be trusted with any lesser jurisdiction.'),
        'questions': [
            'Candidate affirms life begins at conception and personhood from conception',
            'Candidate has voted for or actively advocates abortion abolition (not merely restrictions)',
            'Candidate opposes embryonic stem-cell research, IVF embryo discard, and chimeric experimentation',
            'Candidate opposes euthanasia, physician-assisted suicide, and quality-of-life rationing',
            'Candidate has never accepted Planned Parenthood, NARAL, EMILY\'s List, or abortion-industry PAC funding',
        ],
        'key_bills': [
            ('Hyde Amendment', 'Annual rider banning federal funding of elective abortion. We track every vote since 1976.'),
            ('Born-Alive Abortion Survivors Protection Act', 'Requires medical care for infants who survive attempted abortion. Most recent votes 2019, 2023, 2025.'),
            ('Pain-Capable Unborn Child Protection Act', '20-week federal abortion limit. Candidate support/opposition fully scored.'),
            ('Life at Conception Act', 'Federal legislative recognition of personhood from fertilization. Co-sponsors get full credit.'),
        ],
        'key_orgs': [
            ('Planned Parenthood Action Fund / NARAL', 'Donations or endorsements from these PACs zero out this category.'),
            ('National Right to Life', 'Endorsements and grading factored as positive evidence (verify by primary source — NRLC has softened on incrementalism).'),
            ('Susan B. Anthony Pro-Life America', 'Endorsements and ratings factored as positive evidence.'),
            ('Operation Save America / Free the States', 'Abolitionist orgs whose endorsements indicate the strongest position.'),
        ],
        'disqualifiers': [
            'Voted for any expansion of abortion access (state or federal)',
            'Affirms "Roe should be restored" or "abortion is healthcare"',
            'Took identifiable donations from Planned Parenthood / NARAL / EMILY\'s List PACs',
        ],
    },
    {
        'slug': 'biblical-marriage',
        'id': 'biblical_marriage',
        'tier': 'god_first',
        'tier_pts': 60,
        'num': 2,
        'label': 'Biblical Marriage',
        'tagline': 'One man, one woman, for life — and no redefinition of sex.',
        'description': 'Does this candidate affirm biblical marriage and reject the redefinition of family, sex, and gender in law?',
        'scripture': ('Matthew 19:4–6', 'Have you not read that He who created them from the beginning made them male and female, and said, "For this reason a man shall leave his father and his mother and be joined to his wife, and the two shall become one flesh"? So they are no longer two but one flesh.'),
        'why_it_matters': (
            'Marriage is not a state-issued license. It is the first institution God established '
            '(Genesis 2:24), prior to civil government, and the state\'s only legitimate role is '
            'to recognize and protect what God already defined. Candidates who voted for '
            'Obergefell-style redefinition, the Respect for Marriage Act, or transgender '
            'recognition in law have used civil power against an institution that predates them. '
            'A house built on redefined marriage cannot stand.'),
        'questions': [
            'Candidate affirms marriage as exclusively the lifelong union of one man and one woman as instituted by God',
            'Candidate opposes all forms of same-sex marriage, civil unions, and domestic partnerships in law',
            'Candidate rejects transgender ideology and affirms biological sex (male/female) as immutable and God-given',
            'Candidate supports no-fault divorce reform and policies that strengthen the marriage covenant',
            'Candidate opposes promotion of LGBTQ+ identity in public policy, schools, military, and corporate-government partnerships',
        ],
        'key_bills': [
            ('Respect for Marriage Act (2022)', 'Federal codification of same-sex marriage recognition. Yes-votes are disqualifying.'),
            ('Equality Act', 'Adds "sexual orientation" + "gender identity" to civil-rights law, overriding religious-conscience protections. We track sponsors + every floor vote.'),
            ('PROTECT Kids Act (state-level)', 'Bans transgender procedures on minors. State-by-state tracking.'),
            ('Save Women\'s Sports Act / Title IX Restoration', 'Defends biological-sex categories in athletics + intimate spaces.'),
        ],
        'key_orgs': [
            ('Family Research Council Action', 'Endorsements + ratings factored as positive evidence.'),
            ('Alliance Defending Freedom', 'Tracked for legal-amicus filings on marriage / sex / gender cases.'),
            ('HRC (Human Rights Campaign)', 'High score from HRC zeros out this category.'),
            ('GLAAD / GLSEN', 'Endorsements or board positions disqualify.'),
        ],
        'disqualifiers': [
            'Voted YES on Respect for Marriage Act or any state equivalent',
            'Marched in a "Pride" parade or attended a Pride event as a sitting elected official',
            'Sponsored or co-sponsored any legislation expanding "gender identity" protections',
        ],
    },
    {
        'slug': 'family-child-sovereignty',
        'id': 'family_child_sovereignty',
        'tier': 'god_first',
        'tier_pts': 60,
        'num': 3,
        'label': 'Family & Child Sovereignty',
        'tagline': 'Parents over the state. The state out of the school. The predator off the platform.',
        'description': 'Does this candidate defend parental authority over children and protect children from state intrusion, predators, and ideological capture?',
        'scripture': ('Ephesians 6:4 / Deuteronomy 6:6–7', 'Fathers, do not provoke your children to anger, but bring them up in the discipline and instruction of the Lord. … And these words which I am commanding you today shall be on your heart; and you shall teach them diligently to your sons.'),
        'why_it_matters': (
            'God gave children to parents, not to schools, not to the state, not to corporations. '
            'When public school systems teach gender ideology to kindergarteners without parental '
            'notice, when social-media platforms surface adult content to minors, when foster '
            'agencies prioritize same-sex placement over kinship preservation — the family\'s '
            'God-ordained authority is being usurped. This category catches the politicians who '
            'enabled that usurpation.'),
        'questions': [
            'Candidate supports universal school choice, homeschool freedom, and opposes compulsory public-school attendance',
            'Candidate supports parental notification and consent on all medical, mental-health, and gender-related interventions for minors',
            'Candidate opposes CRT, SOGI, "comprehensive sex ed," and gender-ideology curricula in K-12 public schools',
            'Candidate supports age-verification on pornographic content and criminal penalties for sexualized content marketed to minors',
            'Candidate supports faith-based adoption/foster agencies and opposes placement of children with same-sex couples',
        ],
        'key_bills': [
            ('Universal School Choice Act / ESA legislation', 'State-by-state Education Savings Account programs. Adam tracks every governor + state legislator vote.'),
            ('Parental Bill of Rights Act', 'Federal version 2023 H.R. 5; state versions tracked since 2021.'),
            ('Age-Verification on Adult Content Act', 'Texas-style age verification for pornographic websites. Tracked state-by-state.'),
            ('Save Adolescents from Experimentation (SAFE) Act', 'Bans cross-sex hormones + gender-related surgeries on minors. State-by-state tracking.'),
        ],
        'key_orgs': [
            ('Moms for Liberty', 'Local-chapter endorsement = strong positive signal.'),
            ('Heritage Foundation Parents Bill of Rights', 'Scoring + endorsements tracked.'),
            ('Family Research Council', 'Voter-guide alignment.'),
            ('NEA / AFT (teacher unions)', 'Endorsements zero out this category.'),
            ('GLSEN', 'Curriculum-partner relationships disqualify.'),
        ],
        'disqualifiers': [
            'Voted to require gender-affirming care for minors',
            'Voted against parental notification on a child\'s gender identity in schools',
            'Took campaign money from teacher-union PACs above $10K cycle',
        ],
    },
    {
        'slug': 'christian-liberty',
        'id': 'christian_liberty',
        'tier': 'god_first',
        'tier_pts': 60,
        'num': 4,
        'label': 'Christian Liberty',
        'tagline': 'Freedom to profess Christ — including the freedom of others to disagree.',
        'description': 'Does this candidate defend the freedom to publicly profess Christ — including the freedom of others to disagree — without state compulsion against Christian conscience?',
        'scripture': ('Acts 5:29', 'But Peter and the apostles answered, "We must obey God rather than men."'),
        'why_it_matters': (
            'We use "Christian Liberty" rather than the generic "religious liberty" deliberately. '
            'Religious liberty implies a state-blessed pluralism in which every path is equally '
            'valid — including the path to hell. Christian Liberty names what we actually want: '
            'the freedom to publicly profess Christ as Lord in every sphere, the freedom to '
            'decline participation in what violates Christian conscience (gay weddings, '
            'gender-transition medicine, abortion procedures), and the freedom of others to '
            'disagree without state coercion in either direction. This is the apostolic posture '
            'of Acts 5:29 made political.'),
        'questions': [
            'Candidate affirms the right to publicly profess Christ in all spheres (workplace, military, public office, schools)',
            'Candidate supports conscience exemptions for Christian medical professionals, business owners, adoption agencies, and educators',
            'Candidate opposes compelled speech against Christian conviction (pronoun mandates, gospel-proclamation hate-speech laws)',
            'Candidate supports public-square Christian symbols, prayer in public bodies, and Sabbath/Sunday closure protections',
            'Candidate opposes state-funded promotion of non-Christian religious displays, curricula, or holidays in public institutions',
        ],
        'key_bills': [
            ('Religious Freedom Restoration Act (RFRA)', 'Federal 1993 + state-level versions. Sponsorship + defense votes tracked.'),
            ('First Amendment Defense Act', 'Protects religious organizations from federal discrimination based on marriage beliefs.'),
            ('Conscience Protection Act', 'Defends medical professionals + institutions from being forced to participate in abortion.'),
            ('Equality Act (opposition)', 'Federal bill that would gut RFRA — opposition is scored positively here.'),
        ],
        'key_orgs': [
            ('Alliance Defending Freedom', 'Christian-liberty litigation tracker.'),
            ('First Liberty Institute', 'Conscience-clause case tracker.'),
            ('Becket Fund for Religious Liberty', 'Religious-liberty amicus tracker (broader than Christian-specific but tracked).'),
            ('Freedom from Religion Foundation', 'High-profile FFRF support or partnership disqualifies.'),
        ],
        'disqualifiers': [
            'Voted YES on the federal Equality Act (would override RFRA conscience protections)',
            'Voted to strip Christian symbols from public buildings, holidays, or curricula',
            'Mandated pronoun-compliance speech in public employment under penalty',
        ],
    },
    {
        'slug': 'economic-stewardship',
        'id': 'economic_stewardship',
        'tier': 'god_first',
        'tier_pts': 60,
        'num': 5,
        'label': 'Economic Stewardship',
        'tagline': 'Sound money. No CBDC. No debt-slavery. Audit the Fed.',
        'description': 'Does this candidate honor biblical economic mandates — sound money, anti-usury, debt restraint, and opposition to globalist financial capture (Prov 22:7)?',
        'scripture': ('Proverbs 22:7', 'The rich rules over the poor, and the borrower becomes the lender\'s slave.'),
        'why_it_matters': (
            'Modern Christian conservatives stopped scoring on money roughly 50 years ago — about '
            'the time Nixon ended the gold standard. The result: a nation $35 trillion in '
            'sovereign debt, a Federal Reserve no member of Congress controls, and a coming '
            'Central Bank Digital Currency that would make every transaction permission-based. '
            'Proverbs 22:7 is policy as much as personal counsel. A free Christian people cannot '
            'be Federal-Reserve-printed serfs. This category catches the politicians who voted '
            'against every audit-the-Fed bill, supported COVID stimulus that quintupled the '
            'money supply, or shrugged when Operation Choke Point 2.0 began debanking Christian '
            'organizations.'),
        'questions': [
            'Candidate opposes a Central Bank Digital Currency (CBDC) and supports cash and decentralized crypto as legal tender',
            'Candidate supports sound-money policies including gold/silver as constitutional money and audit/abolition of the Federal Reserve',
            'Candidate opposes deficit spending and supports a balanced-budget constitutional amendment',
            'Candidate supports usury limits, anti-debt-slavery protections, and tithe-friendly tax structures',
            'Candidate opposes WEF/ESG/Davos economic capture and supports anti-trust action against monopolistic financial cartels',
        ],
        'key_bills': [
            ('Federal Reserve Transparency Act ("Audit the Fed")', 'Annual reintroduction since Ron Paul. Co-sponsors get full credit.'),
            ('CBDC Anti-Surveillance State Act (HR 5403)', 'Bans the Fed from issuing a CBDC directly to individuals. Cleanest CBDC vote in modern memory.'),
            ('Balanced Budget Amendment proposals', 'Multiple state-by-state Article V convention applications tracked.'),
            ('Gold Reserve Transparency Act', 'Mandates an audit of the U.S. gold holdings at Fort Knox + Federal Reserve banks.'),
            ('Anti-CBDC state legislation', 'Florida HB 7049, Texas SB 2334, etc. — state-level resistance tracked.'),
        ],
        'key_orgs': [
            ('Sound Money Defense League', 'Endorsements + grading tracked.'),
            ('Mises Institute', 'Speaker invitations + book-citation tracker.'),
            ('Heritage Foundation Index of Economic Freedom', 'Voter-guide alignment.'),
            ('World Economic Forum (WEF)', 'Membership, "Young Global Leaders" alumni status, or Davos attendance zero out this category.'),
            ('BlackRock / Vanguard / State Street', 'ESG-mandate sponsorship or paid speaking engagements counted negatively.'),
        ],
        'disqualifiers': [
            'Voted YES on any CBDC enabling legislation',
            'Voted YES on the 2020 CARES Act, 2021 American Rescue Plan, or 2022 Inflation Reduction Act without offsetting deficit-reduction',
            'Member of the WEF, "Young Global Leaders" alumnus, or attended Davos as a sitting elected official',
        ],
    },
    {
        'slug': 'election-integrity',
        'id': 'election_integrity',
        'tier': 'god_first',
        'tier_pts': 60,
        'num': 6,
        'label': 'Election Integrity',
        'tagline': 'Paper. Hand-counted. Single-day. Citizen-only.',
        'description': 'Does this candidate support verifiable elections grounded in citizen accountability, free from machine manipulation, mass mail-in, or foreign interference?',
        'scripture': ('Exodus 18:21', 'Furthermore, you shall select out of all the people able men who fear God, men of truth, those who hate dishonest gain; and you shall place these over them as leaders of thousands, of hundreds, of fifties and of tens.'),
        'why_it_matters': (
            'If you cannot trust the count, nothing else on this scorecard matters. Christian '
            'consent of the governed (Romans 13:1 properly understood) requires elections '
            'that the people can verify with their own eyes. Hand-counted paper ballots, '
            'photo voter ID, single-day in-person voting — these are not partisan positions, '
            'they are the engineering specifications for a government that claims its '
            'authority from God through the consent of the governed. Mass mail-in voting, '
            'electronic tabulation no citizen can audit, private election funding from '
            'Mark Zuckerberg, ballot harvesting — these break the chain. This is why '
            'Election Integrity sits in the God First tier rather than as a sub-bullet of '
            'America First.'),
        'questions': [
            'Candidate supports hand-counted paper ballots and opposes electronic voting machines',
            'Candidate supports photo voter ID with citizenship verification',
            'Candidate supports single-day in-person voting with absentee only for verified medical/military exceptions',
            'Candidate opposes mass mail-in voting, drop boxes, and ballot harvesting',
            'Candidate opposes private election funding ("Zuckerbucks") and foreign-government election interference',
        ],
        'key_bills': [
            ('Save Voter ID Act / SAVE Act (HR 22)', 'Federal proof-of-citizenship requirement for voter registration.'),
            ('Voter Confidence Act variants', 'Mandates hand-counted paper ballots in federal elections. Co-sponsors tracked.'),
            ('Anti-Zuckerbuck legislation (state-level)', 'Wisconsin, Florida, Georgia, Texas, Pennsylvania state-by-state tracking.'),
            ('For the People Act / Freedom to Vote Act', 'Democratic-sponsored federalization of mass mail-in — opposition is scored positively.'),
        ],
        'key_orgs': [
            ('True the Vote', 'Election-integrity training + investigation tracker.'),
            ('Public Interest Legal Foundation', 'Voter-roll integrity litigation tracker.'),
            ('Election Integrity Network (Cleta Mitchell)', 'Coalition-membership tracking.'),
            ('Center for Tech and Civic Life', 'Recipient of "Zuckerbucks" — partnership disqualifies.'),
            ('Brennan Center for Justice', 'Mass-mail-in advocacy — alignment scored negatively.'),
        ],
        'disqualifiers': [
            'Voted YES on the For the People Act or Freedom to Vote Act',
            'Accepted Center for Tech and Civic Life ("Zuckerbuck") funding for their election office',
            'Publicly stated "the 2020 election was the most secure in history" while opposing audits',
        ],
    },
    {
        'slug': 'border-immigration',
        'id': 'border_immigration',
        'tier': 'america_first',
        'tier_pts': 40,
        'num': 7,
        'label': 'Border & Immigration',
        'tagline': 'A nation that cannot enforce its border is not a nation.',
        'description': 'Does this candidate enforce U.S. borders, oppose illegal immigration, and defend American sovereignty over foreign claims to U.S. territory and labor?',
        'scripture': ('Nehemiah 4:13–14', 'Then I stationed men in the lowest parts of the space behind the wall, the exposed places, and I stationed the people in families with their swords, spears, and bows. … "Remember the Lord who is great and awesome, and fight for your brothers, your sons, your daughters, your wives, and your houses."'),
        'why_it_matters': (
            'God establishes the boundaries of nations (Acts 17:26, Deuteronomy 32:8). A nation '
            'that cannot define and enforce its border has abdicated its first civic '
            'responsibility — protecting the household, the inheritance, and the gospel '
            'commission inside it. This category catches not just the border-wall vote but the '
            'whole machinery: sanctuary policies that nullify federal enforcement, E-Verify '
            'opposition that subsidizes illegal labor, birthright citizenship for tourist '
            'births, and foreign ownership of U.S. farmland that compromises food sovereignty.'),
        'questions': [
            'Candidate supports completed physical border barrier and active military border presence',
            'Candidate supports mandatory deportation of all illegal aliens, including those who entered as minors',
            'Candidate opposes sanctuary city/state policies and supports federal preemption against them',
            'Candidate supports mandatory E-Verify for all employment and benefit eligibility',
            'Candidate opposes birthright citizenship for children of illegal aliens, tourist births, and opposes foreign ownership of U.S. farmland',
        ],
        'key_bills': [
            ('Secure the Border Act (HR 2)', '2023 House-passed comprehensive border-enforcement package.'),
            ('Laken Riley Act', '2025 mandatory-detention law for illegal aliens charged with theft. Bipartisan vote tracker.'),
            ('Sanctuary City Defunding Acts', 'Federal preemption against sanctuary jurisdictions. Annual reintroduction.'),
            ('Stop Chinese Communist Prying by Vindicating Intellectual Safeguards in Our Republic Act (SCV)', 'Bans CCP-linked entities from buying U.S. farmland near military installations.'),
            ('PROTECT Our Communities Act', 'Mandatory E-Verify nationwide for all employers.'),
        ],
        'key_orgs': [
            ('NumbersUSA', 'Grading + voter guide.'),
            ('Federation for American Immigration Reform (FAIR)', 'Endorsements + scorecard.'),
            ('Center for Immigration Studies', 'Voter-guide alignment.'),
            ('U.S. Chamber of Commerce', 'Open-borders cheap-labor advocacy — alignment scored negatively.'),
            ('La Raza / UnidosUS', 'Endorsements disqualify.'),
        ],
        'disqualifiers': [
            'Voted YES on the 2013 "Gang of 8" amnesty (Marco Rubio, Lindsey Graham, etc.)',
            'Voted YES on any 2025 amnesty / DACA-codification bill',
            'Mayor or governor of a sanctuary jurisdiction who actively defended that status',
        ],
    },
    {
        'slug': 'self-defense-2a',
        'id': 'self_defense',
        'tier': 'america_first',
        'tier_pts': 40,
        'num': 8,
        'label': 'Self-Defense & 2A',
        'tagline': 'The God-given right to protect household and neighbor.',
        'description': 'Does this candidate defend the unalienable right to bear arms as a check against tyranny and a defense of household, neighbor, and homeland?',
        'scripture': ('Luke 22:36 / Nehemiah 4:18', 'And He said to them, "But now, whoever has a money belt is to take it along, likewise also a bag, and whoever has no sword is to sell his coat and buy one." … Each of the builders had his sword strapped at his side as he built.'),
        'why_it_matters': (
            'The Second Amendment recognizes — it does not grant — a right that predates the '
            'Constitution. The God-given duty of every head-of-household to defend his family '
            '(1 Timothy 5:8) requires the practical means to do so. A disarmed Christian '
            'population is a population without recourse when civil authorities turn unjust, '
            'and history (Russia 1917, Germany 1938, China 1949, Cambodia 1975, Venezuela 2012) '
            'is unambiguous about what happens next. This category catches the politicians '
            'who voted for the Bipartisan Safer Communities Act, who took the NRA grade then '
            'voted with Bloomberg, who quietly funded the ATF\'s pistol-brace reclassification.'),
        'questions': [
            'Candidate supports constitutional carry without permit requirements',
            'Candidate opposes red-flag laws, magazine limits, "assault weapons" bans, and gun registries',
            'Candidate supports repeal of the National Firearms Act (NFA), Gun Control Act (GCA), and other federal gun regulations',
            'Candidate supports castle doctrine and stand-your-ground laws with full civil immunity for lawful defense',
            'Candidate opposes ATF overreach, citizen disarmament initiatives, and U.N. small-arms treaty participation',
        ],
        'key_bills': [
            ('Constitutional Carry / Permitless Carry Acts', 'State-by-state — 29 states as of 2025. Adam tracks every governor signature + state-rep vote.'),
            ('National Reciprocity Act (HR 38)', 'Federal recognition of state concealed-carry permits across state lines.'),
            ('Bipartisan Safer Communities Act (2022)', 'Yes-vote = -2 in this category. 15 Republican senators crossed.'),
            ('Repeal the NFA / Hearing Protection Act', 'Co-sponsorship gets full credit.'),
        ],
        'key_orgs': [
            ('Gun Owners of America (GOA)', 'Strictest pro-2A grading. A-rating = positive signal.'),
            ('National Rifle Association (NRA)', 'Useful but inflated — verify NRA grades against actual votes.'),
            ('Virginia Citizens Defense League (VCDL)', 'State-level Virginia tracking.'),
            ('Everytown for Gun Safety / Moms Demand Action', 'Endorsements disqualify.'),
            ('Brady Campaign', 'Endorsements disqualify.'),
        ],
        'disqualifiers': [
            'Voted YES on the Bipartisan Safer Communities Act (2022)',
            'Voted YES on a red-flag law or "extreme risk protection order" statute',
            'Took identifiable Bloomberg / Everytown / Brady PAC money',
        ],
    },
    {
        'slug': 'foreign-policy-restraint',
        'id': 'foreign_policy_restraint',
        'tier': 'america_first',
        'tier_pts': 40,
        'num': 9,
        'label': 'Foreign Policy Restraint',
        'tagline': 'Article I war powers. No forever wars. No foreign-lobby ownership.',
        'description': 'Does this candidate honor Article I war powers, oppose forever wars, and refuse foreign-lobby capture of U.S. policy?',
        'scripture': ('1 Timothy 2:1–2', 'First of all, then, I urge that requests, prayers, intercession, and thanksgiving be made in behalf of all people, for kings and all who are in authority, so that we may lead a tranquil and quiet life in all godliness and dignity.'),
        'why_it_matters': (
            'George Washington warned against "passionate attachments" to foreign nations in his '
            '1796 farewell address. A republic that lets foreign lobbies — AIPAC chief among '
            'them, but also China-linked PACs and Soros-network donor vectors — write its '
            'foreign policy has stopped being a republic. The Article I war-powers question '
            'is doctrinal, not partisan: Congress declares war, not the executive, and not '
            'the executive at the urging of a foreign ally. This category catches the '
            'standing-AUMF defenders, the "we must fund Ukraine forever" caucus, and the '
            'politicians who collected six-figure AIPAC contributions while voting yes on '
            'every aid package.'),
        'questions': [
            'Candidate supports Article I congressional war-powers requirement before any U.S. military action',
            'Candidate supports immediate withdrawal from forever wars and repeal of standing AUMFs',
            'Candidate opposes foreign aid to nations hostile to U.S. interests or actively persecuting Christians',
            'Candidate has never accepted donations from foreign-backed lobbies (e.g., AIPAC) or foreign-linked PACs',
            'Candidate opposes U.S. participation in WHO, U.N. governance overreach, NATO expansion, and supranational governance',
        ],
        'key_bills': [
            ('War Powers Resolution invocations', 'Yemen 2019, Iran 2020 — restraint votes scored positively.'),
            ('AUMF Repeal (2001 + 2002)', 'Co-sponsorship + floor votes tracked.'),
            ('Defending American Citizens Against Foreign Lobbyists Act', 'Bans members of Congress from accepting foreign-lobby money.'),
            ('No Funds for Iran-Backed Terrorism Act', 'Restraint votes against Iran-funded proxies tracked.'),
            ('WHO Withdrawal Act', 'Cleanly identifies anti-supranational candidates.'),
        ],
        'key_orgs': [
            ('Concerned Veterans for America', 'Restraint-focused veterans organization. Endorsements positive.'),
            ('Defense Priorities', 'Foreign-policy restraint think tank. Citation alignment scored.'),
            ('American Israel Public Affairs Committee (AIPAC)', 'PAC + United Democracy Project donations zero out this category.'),
            ('China-linked PAC vectors (per OpenSecrets)', 'Identified donor patterns disqualify.'),
            ('George Soros / Open Society Foundations', 'Donor-network alignment scored negatively in this category (see foreign-influence methodology page).'),
        ],
        'disqualifiers': [
            'Accepted AIPAC / United Democracy Project funding above any threshold',
            'Voted YES on every Ukraine aid package without conditions',
            'Member of WEF, "Young Global Leaders" alumni status, or Davos attendance',
        ],
    },
    {
        'slug': 'industry-capture',
        'id': 'industry_capture',
        'tier': 'america_first',
        'tier_pts': 40,
        'num': 10,
        'label': 'Industry Capture & Sovereignty',
        'tagline': 'Anti-Pharma. Anti-Big-Ag. Anti-MIC. Anti-cartel.',
        'description': 'Does this candidate oppose corporate-state capture across Pharma, Big Ag, and the Military-Industrial Complex — defending citizens against cartel power?',
        'scripture': ('Isaiah 5:20', 'Woe to those who call evil good, and good evil; who substitute darkness for light and light for darkness; who substitute bitter for sweet and sweet for bitter!'),
        'why_it_matters': (
            'The three deepest captures of the modern American state are pharmaceutical '
            '(1986 NCVIA liability shield through COVID mandates), agricultural (Bayer/Monsanto/'
            'Cargill consolidation + USDA capture against family farms), and military-industrial '
            '(revolving-door appointments between DoD and top-5 defense contractors, never-'
            'completed Pentagon audit). Each is a cartel that has converted citizen-protective '
            'regulation into industry-protective regulation. A Christian voter scorecard that '
            'doesn\'t score on this catches nothing the GOP establishment has been doing wrong '
            'for 40 years. This category is the differentiator that separates resolute citizens '
            'from establishment cosplay.'),
        'questions': [
            'Candidate opposes pharmaceutical mandates of any kind (COVID, childhood, employer-required) and supports informed consent',
            'Candidate supports repeal of pharma liability shields (1986 NCVIA, PREP Act) and restoration of tort accountability',
            'Candidate opposes Big Ag consolidation (Bayer/Monsanto/Cargill) and supports anti-trust action against agricultural cartels',
            'Candidate supports raw-milk freedom, small-farm protections, and opposes USDA / EPA overreach against family farms',
            'Candidate supports defense-contractor accountability, completion of Pentagon audits, and ending revolving-door appointments',
        ],
        'key_bills': [
            ('Repeal the National Childhood Vaccine Injury Act (NCVIA, 1986)', 'No major federal repeal bill yet — co-sponsors of any related accountability legislation get credit.'),
            ('PREP Act Reform', 'Restores tort accountability for COVID-era liability shields.'),
            ('PRIME Act', 'Allows state-inspected meat to be sold across state lines — frees small ranchers from USDA centralization.'),
            ('Raw Milk Freedom Act (state + federal)', 'State-by-state tracking + federal interstate-commerce reform.'),
            ('Audit the Pentagon Act', 'Annual reintroduction. Co-sponsorship gets full credit.'),
        ],
        'key_orgs': [
            ('Children\'s Health Defense (RFK Jr. founded)', 'Endorsements + alignment scored positively.'),
            ('Farm-to-Consumer Legal Defense Fund', 'Raw-milk + small-farm litigation tracker.'),
            ('Project on Government Oversight (POGO)', 'Defense-contractor accountability tracker.'),
            ('Pfizer / Moderna / Merck / Johnson & Johnson PACs', 'Donations above $25K cycle trigger per-category penalty.'),
            ('Bayer / Monsanto / Cargill / Tyson Foods PACs', 'Donations above $25K cycle trigger per-category penalty.'),
            ('Lockheed / Raytheon / Northrop / Boeing / General Dynamics PACs', 'Donations above $50K cycle trigger per-category penalty.'),
        ],
        'disqualifiers': [
            'Voted YES on a pharmaceutical mandate of any kind (including state-level COVID mandates)',
            'Voted YES on any expansion of pharma liability shields beyond the 1986 NCVIA baseline',
            'Took identifiable donations from top-5 defense contractor PACs above $50K per cycle',
        ],
    },
]

# ────────────────────────────────────────────────────────────────────────────
# HTML TEMPLATE
# ────────────────────────────────────────────────────────────────────────────
def render_page(cat):
    tier_color = '#dadada' if cat['tier'] == 'god_first' else '#c9a84c'
    tier_emoji = '✝' if cat['tier'] == 'god_first' else '🇺🇸'
    tier_label = 'God First' if cat['tier'] == 'god_first' else 'America First'
    tier_pts = '60 pts total' if cat['tier'] == 'god_first' else '40 pts total'

    questions_html = '\n'.join(
        f'        <li><strong>Q{i+1}.</strong> {q}</li>'
        for i, q in enumerate(cat['questions']))

    bills_html = '\n'.join(
        f'        <li><strong>{lbl}</strong> &mdash; {desc}</li>'
        for lbl, desc in cat['key_bills'])

    orgs_html = '\n'.join(
        f'        <li><strong>{lbl}</strong> &mdash; {desc}</li>'
        for lbl, desc in cat['key_orgs'])

    disqs_html = '\n'.join(
        f'        <li>{d}</li>' for d in cat['disqualifiers'])

    scrip_ref, scrip_text = cat['scripture']

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="canonical" href="https://usmcmin.com/citizen/{cat['slug']}.html">
  <title>{cat['label']} — RESOLUTE Citizen Scorecard | U.S.M.C. Ministries</title>
  <meta name="description" content="{cat['label']} ({tier_label}, 10 pts). {cat['description']} — full rubric, 5 scored questions, key bills + orgs we track.">
  <meta property="og:title" content="{cat['label']} — RESOLUTE Citizen Scorecard">
  <meta property="og:description" content="{cat['tagline']} The full rubric for category #{cat['num']} of the RESOLUTE Citizen 100-point Christian voter scorecard.">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://usmcmin.com/citizen/{cat['slug']}.html">
  <meta property="og:image" content="https://usmcmin.com/assets/og/og-citizen.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://usmcmin.com/assets/og/og-citizen.jpg">
  <link rel="stylesheet" href="/assets/css/main.min.css">
  <link rel="icon" href="/assets/img/favicon.png" type="image/png">
  <style>
    .cp-container {{ max-width: 820px; margin: 0 auto; padding: 24px 20px 60px; }}
    .cp-hero {{
      padding: 32px 20px 26px; border-bottom: 2px solid var(--border);
      margin-bottom: 24px; text-align: center;
    }}
    .cp-tier-badge {{
      display: inline-block; font-size: 0.7rem; font-weight: 700;
      letter-spacing: 2.5px; text-transform: uppercase;
      color: {tier_color}; background: rgba(168,176,188,0.08);
      border: 1px solid rgba(168,176,188,0.25);
      padding: 5px 16px; border-radius: 20px; margin-bottom: 12px;
    }}
    .cp-hero h1 {{
      font-size: clamp(1.7rem, 4vw, 2.4rem); color: var(--white);
      margin-bottom: 8px; font-weight: 800; line-height: 1.2;
    }}
    .cp-tagline {{ color: var(--accent); font-size: 1.05rem; margin-bottom: 14px; font-weight: 500; }}
    .cp-meta {{ color: var(--gray); font-size: 0.82rem; }}
    .cp-meta a {{ color: var(--accent); text-decoration: none; }}
    .cp-meta a:hover {{ text-decoration: underline; }}

    .cp-section {{ margin-top: 28px; padding-top: 22px; border-top: 1px solid var(--border); }}
    .cp-section:first-of-type {{ border-top: none; padding-top: 0; margin-top: 0; }}
    .cp-section h2 {{ color: var(--accent); font-size: 1.25rem; margin-bottom: 8px; font-weight: 700; }}
    .cp-section p {{ color: var(--gray); font-size: 0.95rem; line-height: 1.7; margin-bottom: 12px; }}
    .cp-section ol, .cp-section ul {{
      color: var(--gray); font-size: 0.92rem; line-height: 1.7;
      margin: 8px 0 12px 22px;
    }}
    .cp-section li {{ margin-bottom: 6px; }}
    .cp-section strong {{ color: var(--white); }}

    .cp-scripture {{
      background: rgba(168,176,188,0.06);
      border-left: 3px solid var(--accent);
      padding: 14px 18px; margin: 12px 0 18px;
      border-radius: 0 8px 8px 0;
    }}
    .cp-scripture p {{ color: #e0e0e0; font-style: italic; font-size: 0.95rem; line-height: 1.7; margin: 0 0 6px 0; }}
    .cp-scripture cite {{ color: var(--accent); font-size: 0.82rem; font-style: normal; font-weight: 600; }}

    .cp-disq {{
      background: rgba(244,67,54,0.06);
      border-left: 3px solid #f44336;
      padding: 14px 18px; border-radius: 0 8px 8px 0; margin: 12px 0;
    }}
    .cp-disq h3 {{ color: #ff8a80; font-size: 0.95rem; margin-bottom: 6px; font-weight: 700; }}
    .cp-disq ul {{ margin: 0 0 0 22px; color: #ffb3ad; font-size: 0.9rem; }}

    .cp-back {{
      display: inline-block; color: var(--accent); text-decoration: none;
      font-size: 0.88rem; margin-top: 28px; padding: 8px 14px;
      border: 1px solid var(--accent); border-radius: 6px;
    }}
    .cp-back:hover {{ background: rgba(168,176,188,0.1); }}

    .cp-nav-categories {{
      display: flex; flex-wrap: wrap; gap: 6px;
      margin: 14px 0; justify-content: center;
    }}
    .cp-nav-categories a {{
      font-size: 0.74rem; color: var(--gray); text-decoration: none;
      padding: 4px 10px; border: 1px solid var(--border); border-radius: 12px;
    }}
    .cp-nav-categories a:hover {{ color: var(--accent); border-color: var(--accent); }}
    .cp-nav-categories a.active {{ background: var(--accent-dim); color: var(--accent); border-color: var(--accent); }}

    footer {{
      text-align: center; padding: 30px 20px; color: var(--gray);
      font-size: 0.82rem; border-top: 1px solid var(--border); margin-top: 40px;
    }}
    footer a {{ color: var(--accent); text-decoration: none; }}
  </style>
</head>
<body>

<a href="#main" class="skip-link">Skip to content</a>

<nav>
  <a href="/" class="nav-brand" style="text-decoration:none">
    <img src="/assets/img/logo.png" alt="U.S.M.C. Ministries" style="object-fit:contain">
    <div class="nav-brand-text">
      <div class="name">U.S.M.C. Ministries</div>
      <div class="tag">Warriors Equipped</div>
    </div>
  </a>
  <ul class="nav-links">
    <li><a href="/citizen.html">Scorecard</a></li>
    <li><a href="/find-my-reps.html">Find My Reps</a></li>
    <li><a href="/state.html">By State</a></li>
    <li><a href="/map.html">Maps</a></li>
    <li><a href="/scoring-system.html">Scoring</a></li>
    <li><a href="/compare.html">Compare</a></li>
    <li><a href="/petition.html">Petition</a></li>
    <li><a href="/changelog.html">Changelog</a></li>
  </ul>
  <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">🌙</button>
</nav>

<div id="main" class="cp-container">

  <header class="cp-hero">
    <span class="cp-tier-badge">{tier_emoji} {tier_label} &middot; Category #{cat['num']} &middot; 10 pts</span>
    <h1>{cat['label']}</h1>
    <p class="cp-tagline">{cat['tagline']}</p>
    <p class="cp-meta">5 questions &times; 2 pts = 10 max &middot; <a href="/scoring-system.html">How scoring works</a> &middot; <a href="/citizen.html">Back to scorecard</a></p>
  </header>

  <nav class="cp-nav-categories" aria-label="Jump to another category">
    {{NAV_LINKS}}
  </nav>

  <section class="cp-section">
    <h2>What this measures</h2>
    <p>{cat['description']}</p>
  </section>

  <section class="cp-section">
    <h2>Why it matters</h2>
    <p>{cat['why_it_matters']}</p>
    <div class="cp-scripture">
      <p>{scrip_text}</p>
      <cite>&mdash; {scrip_ref}</cite>
    </div>
  </section>

  <section class="cp-section">
    <h2>The 5 scored questions</h2>
    <p>Each question is binary (True / False / null). True earns +2 points. Null is "not yet verified from primary sources" — neither penalized nor credited.</p>
    <ol>
{questions_html}
    </ol>
  </section>

  <section class="cp-section">
    <h2>Key bills, votes, and laws we track</h2>
    <ul>
{bills_html}
    </ul>
  </section>

  <section class="cp-section">
    <h2>Organizations and PAC vectors we score</h2>
    <ul>
{orgs_html}
    </ul>
  </section>

  <section class="cp-section">
    <div class="cp-disq">
      <h3>⚠️ Position-level disqualifiers</h3>
      <ul>
{disqs_html}
      </ul>
      <p style="font-size:0.82rem;color:#ffb3ad;margin-top:8px;margin-bottom:0;font-style:italic;">A candidate matching any of the above is graded down to the floor of this category regardless of other answers in the rubric.</p>
    </div>
  </section>

  <section class="cp-section">
    <h2>Where this lives in the scorecard</h2>
    <p>This category contributes <strong>10 of {tier_pts.split()[0]}</strong> in the <strong>{tier_emoji} {tier_label}</strong> tier ({tier_pts}) and <strong>10 of 100</strong> in the grand total. See the <a href="/scoring-system.html">full scoring system</a> for the 60/40 weighting rationale and the letter-grade scale (A 90+ / B 80 / C 70 / D 60 / F &lt;60).</p>
  </section>

  <p><a href="/citizen.html" class="cp-back">&larr; Back to the Scorecard</a></p>

</div>

<footer>
  <p><strong>{cat['label']}</strong> &mdash; category #{cat['num']} of 10 &middot; <a href="https://usmcmin.org">U.S.M.C. Ministries</a></p>
  <p style="margin-top:6px;font-size:0.75rem;">"When the righteous are in authority, the people rejoice; but when the wicked beareth rule, the people mourn." &mdash; Proverbs 29:2 (KJV)</p>
</footer>

<script>
(function(){{var t=document.getElementById('themeToggle');if(!t)return;var s=localStorage.getItem('usmc-theme');if(s!=='light'){{document.documentElement.setAttribute('data-theme','dark');t.textContent='☀️';}}t.addEventListener('click',function(){{var d=document.documentElement.getAttribute('data-theme')==='dark';if(d){{document.documentElement.removeAttribute('data-theme');localStorage.setItem('usmc-theme','light');t.textContent='🌙';}}else{{document.documentElement.setAttribute('data-theme','dark');localStorage.setItem('usmc-theme','dark');t.textContent='☀️';}}}});}})();
</script>
<script data-goatcounter="https://usmcmin.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''

def build_nav_links(active_slug):
    """Build a row of all 10 category chips with the current one marked active."""
    links = []
    for c in CATEGORIES:
        cls = ' class="active"' if c['slug'] == active_slug else ''
        links.append(f'    <a href="/citizen/{c["slug"]}.html"{cls}>{c["num"]}. {c["label"]}</a>')
    return '\n'.join(links)

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    written = 0
    for cat in CATEGORIES:
        html = render_page(cat)
        html = html.replace('{NAV_LINKS}', build_nav_links(cat['slug']))
        out_path = os.path.join(OUT_DIR, f"{cat['slug']}.html")
        with open(out_path, 'w') as f:
            f.write(html)
        written += 1
        print(f'  wrote {out_path}')
    print(f'\nGenerated {written} category pages in {OUT_DIR}/')

if __name__ == '__main__':
    main()
