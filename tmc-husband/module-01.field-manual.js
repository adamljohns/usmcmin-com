'use strict';

// Module 1 field-manual content — Episode 1: Building Strong Connections.
// Reconciled from 5 verified sources and 12 NotebookLM artifacts in Adam's
// pt1 notebook (a9e8db5b). Original ministry prose; transcript cited by
// timestamp/paraphrase only.

const fieldManual = {
  classification: 'Formation brief · approximately 75–90 minutes plus one week of fieldwork',
  objective: 'Install protected connection habits and name what you are building the marriage on',
  sourceBase: 'The Marriage Course, Episode 1 — Building Strong Connections',
  reviewStatus: 'Live',
  missionDurationMinutes: 75,

  sectionNav: [
    { href: '#mission-brief', label: 'Brief', sectionId: 'mission-brief' },
    { href: '#scripture-frame', label: 'Scripture', sectionId: 'scripture-frame' },
    { href: '#vineyard-framework', label: 'Vineyard', sectionId: 'vineyard-framework' },
    { href: '#fair-insight', label: 'Fair', sectionId: 'fair-insight' },
    { href: '#caution-boundary', label: 'Caution', sectionId: 'caution-boundary' },
    { href: '#self-check', label: 'Check', sectionId: 'self-check' },
    { href: '#field-action', label: 'Exercise', sectionId: 'field-action' },
    { href: '#discussion-prompts', label: 'Prompts', sectionId: 'discussion-prompts' },
    { href: '#resources', label: 'Media', sectionId: 'resources' },
    { href: '#assessment', label: 'Quiz', sectionId: 'assessment' },
    { href: '#completion', label: 'Finish', sectionId: 'completion' }
  ],

  inventory: {
    heading: 'Source and artifact reconciliation',
    summary: 'This module reconciles 5 verified sources and 12 completed artifacts from the Episode 1 research package. All twelve NotebookLM artifacts are embedded below — audio, video, slides, graphics, reports, and an interactive quiz.',
    counts: [
      { value: '5', label: 'sources', detail: 'Episode 1 transcript plus four independent model reviews' },
      { value: '12', label: 'artifacts', detail: '2 audio · 2 video · 2 decks · 2 graphics · 3 reports · 1 quiz' },
      { value: '12', label: 'stored locally', detail: 'Full media room embedded below — not withheld' },
      { value: '0', label: 'withheld', detail: 'Episode 1 package is complete in-repo for this prototype' }
    ]
  },

  sources: [
    {
      slug: 'episode-1-transcript',
      lane: 'Primary source',
      title: 'Episode 1 transcript, The Marriage Course',
      note: 'A 1:40:48 session locally transcribed (whisper.cpp + Silero VAD). Hosts appear as Nicky and Sila in the transcript. Validate exact quotations before treating any line as canonical.'
    },
    {
      slug: 'chatgpt-review',
      lane: 'Chaplain and counsellor lens',
      title: 'ChatGPT independent review',
      note: 'Strongest on practical habits and the distinction between covenant maintenance and crisis care. Flags when “meet her needs” language can invert in unsafe marriages.'
    },
    {
      slug: 'claude-review',
      lane: 'Systems-analyst lens',
      title: 'Claude independent review',
      note: 'Strongest on the vineyard metaphor as a diagnostic and on the plan/prioritize/protect date rule as the episode’s most transferable tool.'
    },
    {
      slug: 'gemini-review',
      lane: 'Brotherly friend lens',
      title: 'Gemini independent review',
      note: 'Written under a 1,300-word ceiling. Emphasises the four vineyard tasks as a season-check rather than a one-size prescription.'
    },
    {
      slug: 'grok-review',
      lane: 'Grandfatherly theologian lens',
      title: 'Grok independent review',
      note: 'Strongest on faith-frame honesty and on the limits of anecdotal reconciliation stories as evidence.'
    }
  ],

  missionBrief: {
    heading: 'Connection is cultivated, not discovered',
    teaching: {
      heading: 'What the session actually teaches',
      paragraphs: [
        'Episode 1 opens with a plain claim: marriage has the potential to be the closest human relationship, but that closeness is not self-sustaining. It must grow or it decays. The presenters use a vineyard metaphor — adjusting, pruning, supporting, renewing — to describe seasons of maintenance rather than a one-time fix.',
        'The real engine of the session is not the teaching segments but the paused couple conversations: private, structured, and never reported to the group. Two concrete practices close the episode: a weekly protected date (plan, prioritize, protect) and proactive nurture — learning and meeting emotional needs before resentment accumulates.'
      ],
      map: 'Teaching map: 00:03:59–00:04:24 · 00:11:27–00:12:01 · 00:15:02–00:22:07 · 01:09:46–01:11:09 · 01:22:25–01:26:18'
    },
    analysis: {
      heading: 'The husband’s assignment',
      paragraphs: [
        'Your assignment is not to grade your wife’s connection score or diagnose her needs from a checklist. It is to ask what kind of husband you are becoming, what your repeated conduct is placing into the home, and whether your marriage is receiving protected time and proactive care — or only leftover attention after everything else wins.',
        'This module keeps two jobs separate. Where the marriage is ordinary and basically safe, install the habits: protected weekly time, phone-down presence, one proactive act of nurture, and an honest season check using the four vineyard tasks. Where fear, control, betrayal, or violence is present, stop treating drift as the problem and seek individual help first.'
      ]
    },
    endState: 'You can name which vineyard season fits your marriage, schedule one protected connection block, and complete one proactive nurture act without keeping score or demanding reciprocation.'
  },

  scripture: {
    heading: 'Covenant ground with stated limits',
    quote: {
      text: 'Therefore a man shall leave his father and his mother and hold fast to his wife, and they shall become one flesh.',
      cite: 'Genesis 2:24 (ESV)'
    },
    intro: 'Read each passage in its wider context before applying it. The caveat under each one is ministry analysis, not the text.',
    entries: [
      {
        reference: 'Genesis 2:24',
        teaching: 'Episode 1 grounds intimacy in “two become one” — a new primary loyalty that is physical, emotional, psychological, and for Christian participants, spiritual.',
        caveat: 'Leaving father and mother is not contempt for parents; honoring parents does not require allowing harmful intrusion. “One flesh” is not a warrant for fusion that erases agency, safety, or truthful boundaries.'
      },
      {
        reference: 'Matthew 7:24–27',
        teaching: 'Jesus connects hearing with doing. A marriage built on practiced habits — not only good intentions — survives ordinary pressure better than one built on sentiment alone.',
        caveat: 'Obedient discipleship is not a guarantee that a faithful husband controls every outcome. Doing the right thing can still meet resistance, grief, or limits you cannot remove.'
      },
      {
        reference: 'Ephesians 5:21, 25–33',
        teaching: 'Mutual submission and a husband’s self-giving love belong together. Service and initiative are Christian virtues in the home.',
        caveat: 'Headship language must never authorize coercion, entitlement, or concealment of harm. Sacrificial love protects; it does not dominate.'
      },
      {
        reference: 'James 1:19–22',
        teaching: 'Quick listening and practiced obedience expose the gap between religious speech and embodied faithfulness — relevant to every check-in and nurture conversation.',
        caveat: 'Slow to speak is not silence about real wrong. James requires doing, not only hearing.'
      }
    ]
  },

  vineyardFramework: {
    heading: 'Four vineyard tasks — adjust, prune, support, renew',
    lead: 'The session’s central metaphor is maintenance, not magic. Each task names a season; your job is to identify the season honestly and act on that one task this week.',
    tasks: [
      {
        number: '01',
        name: 'Adjusting — from “I” to “we”',
        source: 'Marriage requires continuing adjustment as life changes. The session’s memorable line: you can change yourself but you cannot change your partner — stop remodeling your spouse.',
        husbandMove: 'Name one habit you keep defending as “just how I am” that actually costs the marriage. Change that one behavior for seven days before asking her to change anything.',
        guardrail: 'Accepting harmless differences is not accepting harmful conduct. Do not use “I can only change myself” to tolerate abuse, deception, or coercion.'
      },
      {
        number: '02',
        name: 'Pruning — protect couple time',
        source: 'Pruning means prioritising the marriage over competing demands — including, in the session’s striking line, loving your wife as part of how you love your children well.',
        husbandMove: 'Put one 90-minute protected block on a shared calendar this week. Write plan · prioritize · protect beside it. Phones away; no “we’ll try next week.”',
        guardrail: '“Prioritize over even the children” is a corrective to neglect, not an absolute. Single parents, special-needs seasons, and a spouse who is the source of insecurity need different scaffolding.'
      },
      {
        number: '03',
        name: 'Supporting — under load together',
        source: 'Supporting includes building a network and carrying each other through illness, job loss, infertility, empty nest, and aging parents.',
        husbandMove: 'Ask one concrete question: “What would lighten your load this week?” Do one reasonable thing that comes back — without turning it into a ledger.',
        guardrail: 'Service that runs one way for months without reciprocity is a structural warning, not a virtue to sustain indefinitely.'
      },
      {
        number: '04',
        name: 'Renewing — deliberate reconnection',
        source: 'Renewing addresses drift: the “invisible wall, brick by brick” stories in the session warn that disconnection compounds quietly.',
        husbandMove: 'Run a fifteen-minute renewal talk: one appreciation, one pressure, one small next step. End on time.',
        guardrail: 'Renewal is not forced intimacy. If she declines, respond with curiosity and respect — not punishment or guilt.'
      }
    ],
    practices: {
      heading: 'Two foundation practices',
      items: [
        {
          name: 'Plan · prioritize · protect',
          body: 'Weekly protected time is the episode’s most transferable tool. The failure mode is familiar: “quality time next week” never arrives because life stays just as busy. Name the phone as a specific enemy; keep the bar low enough to repeat (coffee counts).'
        },
        {
          name: 'Proactive over reactive',
          body: 'Meet emotional needs before resentment accumulates. Needs differ and change; they must be spoken — “if you loved me you’d know” is a script this module refuses. Ask before you assume; act before you are asked.'
        }
      ]
    }
  },

  fairInsight: {
    heading: 'What the source gets right',
    paragraphs: [
      'All four independent reviews converge: Episode 1 lowers the threat of talking. Private paused conversations, not group disclosure, are the real intervention — and that design is sound for anxious or conflict-avoidant couples.',
      'The plan/prioritize/protect date rule and the proactive-over-reactive reframe give husbands something observable to do on an ordinary Tuesday. The vineyard metaphor is memorable without requiring agreement on every analogy detail.'
    ]
  },

  caution: {
    heading: 'Where caution is required',
    paragraphs: [
      'The session assumes two reasonably safe, willing partners of roughly equal power. It offers almost nothing for abuse, addiction, active betrayal, or an unwilling spouse — and several lines can invert dangerously in those contexts.',
      'The expert assertion that conflict is “not the key issue” and that “aloneness destroys marriages” is presented as settled research. Even where disconnection matters, chronic contempt or violence may be the emergency — not secondary noise.'
    ],
    slogans: [
      {
        line: 'I can change myself but I can’t change my partner.',
        stamp: 'Source teaching, near 00:17:41',
        qualification: 'Freeing for harmless differences. Hazardous when used to silence naming of serious harm or to relocate fault onto the person being injured.'
      },
      {
        line: 'Prioritize the marriage over even the children.',
        stamp: 'Source teaching, near 01:19:25',
        qualification: 'Helpful corrective when logistics have swallowed the marriage. Not a universal hierarchy every family can adopt uncritically.'
      },
      {
        line: 'Conflict is not the key issue — aloneness destroys marriages.',
        stamp: 'Source teaching, near 01:21:44',
        qualification: 'May describe many drifting marriages. Must not minimize conflict that is itself the safety problem.'
      }
    ],
    additional: [
      'Reconciliation anecdotes are illustration, not proof that persistence always pays.',
      'Date night presumes discretionary time, childcare, and capacity — adapt the form; keep the aim.',
      'The faith frame promises relevance regardless of belief yet closes in Jesus’ name — facilitators should own that honestly.',
      'Attachment language is asserted, not explained; trauma histories often need more than a weekly date.'
    ]
  },

  selfCheck: {
    heading: 'Husband’s self-check',
    intro: 'Reflect privately. Do not use these prompts to diagnose or score your wife.',
    items: [
      'When did we last have protected time that was not logistics?',
      'Which vineyard season — adjusting, pruning, supporting, renewing — fits us right now?',
      'Do I meet her needs proactively, or only after complaint?',
      'What consistently defeats our protected time — and which of plan/prioritize/protect is weakest?',
      'Where do my promises and repeated habits currently disagree?',
      'Who is one wise, safe person I could approach before a crisis grows?'
    ]
  },

  fieldExercise: {
    heading: 'One-week foundation exercise',
    intro: 'Either spouse may stop any step without explanation. If fear or contempt dominates, stop and seek help instead of powering through.',
    days: [
      { day: 'Day 1', title: 'Schedule protected time.', body: 'Together, put one 90-minute date on a shared calendar. Write plan · prioritize · protect beside it.' },
      { day: 'Day 2', title: 'Needs disclosure.', body: 'Each partner writes three current emotional needs and swaps lists — no fixing yet, only understanding.' },
      { day: 'Day 3', title: 'One proactive act.', body: 'Each performs one small action meeting a need on the other’s list.' },
      { day: 'Day 4', title: 'Phone-free hour.', body: 'Both phones away for one shared hour. Measure completion, not perfection.' },
      { day: 'Day 5', title: 'Season check.', body: 'Ten minutes: which vineyard task fits us, and one change it implies.' },
      { day: 'Day 6', title: 'The date itself.', body: 'Keep the scheduled date; keep the bar low if needed.' },
      { day: 'Day 7', title: 'After-action review.', body: 'Fifteen minutes: what to keep, what to drop, what to adjust.' }
    ],
    finishLine: 'Protected time is scheduled and occurred once, one proactive nurture act is completed, and you named one vineyard season honestly.'
  },

  discussionPrompts: {
    heading: 'Discussion prompts',
    intro: 'Invite; do not assign. Your wife may decline any prompt without penalty.',
    items: [
      'What would make a brief weekly check-in feel safe rather than burdensome?',
      'Which vineyard season do you think we are in — and do we agree?',
      'What is one need of mine you would not guess unless I told you?',
      'What defeats our protected time, and how do we protect it differently?',
      'Where is “change yourself” freeing for us — and where might it excuse something we should not tolerate?'
    ]
  },

  referral: {
    heading: 'Support and safety boundary',
    lead: 'This module is education for a basically safe marriage. It is not crisis care, clinical treatment, or a substitute for qualified help.',
    distinction: 'Ordinary drift is not coercive control, threats, violence, or active betrayal. Where those are present, joint exercises may be unsafe — seek confidential individual help first.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.', href: null },
      { label: 'Abuse or coercive control', body: 'Seek confidential individual safety planning. Joint exercises are not automatically appropriate when control or fear is present.' },
      { label: 'Betrayal, addiction, trauma, or entrenched high conflict', body: 'A licensed clinician with relevant specialisation. Trained pastoral care supports that work; it does not replace it.', href: null }
    ],
    close: 'Never use Scripture, headship, money, children, or course completion to demand access, silence concern, or prevent help.'
  },

  verification: {
    heading: 'Claims carried forward for verification',
    intro: 'Ministry analysis. Flagged by independent review; not settled on this page.',
    items: [
      'Presenter surnames — transcript gives first names only.',
      'The “conflict is not the key issue / aloneness destroys marriages” research claim near 01:21:44.',
      'Attribution for the Ferguson “15 years / 15 years” quotation near 01:23:08.',
      'Unnamed guest speakers (winter-love author, attachment expert) — do not name without confirmation.'
    ]
  },

  resources: {
    heading: 'Resource room',
    intro: 'Twelve NotebookLM artifacts from your Episode 1 notebook, embedded here. Treat generated media as study aids — read against the caution section above.',
    groups: [
      { key: 'video', heading: 'Video overviews', count: '2 artifacts', note: 'Explainer videos from NotebookLM. Use captions where available.' },
      { key: 'audio', heading: 'Audio briefings', count: '2 artifacts', note: 'Critical companion listens — where good advice misfires.' },
      { key: 'slides', heading: 'Slide decks', count: '2 artifacts', note: 'PDF exports from NotebookLM.' },
      { key: 'infographics', heading: 'Field graphics', count: '2 artifacts', note: 'Single-page visual summaries.' },
      { key: 'reports', heading: 'Readable reports', count: '3 artifacts', note: 'Markdown study aids in different registers.' },
      { key: 'quiz', heading: 'Knowledge check', count: '1 artifact', note: 'Interactive NotebookLM export — also embedded in Assessment below.' }
    ],
    withheldNotice: null,
    notebook: {
      title: 'Your NotebookLM notebook',
      body: 'Google account required. This is the canonical source for all artifacts below.',
      label: 'Open “TMC (pt1): Building Strong Connections” in NotebookLM',
      href: 'https://notebooklm.google.com/notebook/a9e8db5b-8b6b-48f9-8d91-74165d6215ab'
    },
    journal: {
      heading: 'Optional companion journal',
      label: 'The Marriage Course Study Journal',
      href: 'https://www.amazon.com/dp/0310116694?tag=usmcministrie-20',
      body: 'The session directs couples to written exercises in the companion journal. Optional — this module works without it.',
      disclosure: 'Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.'
    }
  },

  assessment: {
    heading: 'Knowledge check',
    intro: 'Complete the quiz after working through the module. Flashcards: export from the same NotebookLM notebook if you want a drill deck — Episode 1 shipped quiz-first in this package.',
    quizHref: '../assets/media/tmc-husband/m01/quiz/marriage-quiz.html',
    quizTitle: 'Episode 1 Marriage Quiz'
  },

  artifacts: [
    {
      slug: 'video-the-marriage-course',
      state: 'local',
      group: 'video',
      kind: 'Video',
      title: 'The Marriage Course',
      summary: 'NotebookLM explainer overview of Episode 1 themes.',
      href: '../assets/media/tmc-husband/m01/video/the-marriage-course.mp4',
      mediaType: 'video'
    },
    {
      slug: 'video-blueprint-stress-test',
      state: 'local',
      group: 'video',
      kind: 'Video',
      title: 'The Blueprint and the Stress Test',
      summary: 'Systems-flavoured video on foundation habits under pressure.',
      href: '../assets/media/tmc-husband/m01/video/the-blueprint-and-stress-test.mp4',
      mediaType: 'video'
    },
    {
      slug: 'audio-blind-spots-vineyard',
      state: 'local',
      group: 'audio',
      kind: 'Audio',
      title: 'Blind spots in the vineyard marriage course',
      summary: 'Critical audio on where vineyard metaphors and habits misfire.',
      href: '../assets/media/tmc-husband/m01/audio/blind-spots-in-the-vineyard.mp3',
      mediaType: 'audio'
    },
    {
      slug: 'audio-why-course-fails',
      state: 'local',
      group: 'audio',
      kind: 'Audio',
      title: 'Why The Marriage Course fails some couples',
      summary: 'Audio briefing on limits and safety inversions.',
      href: '../assets/media/tmc-husband/m01/audio/why-the-marriage-course-fails-some-couples.mp3',
      mediaType: 'audio'
    },
    {
      slug: 'slides-marital-maintenance',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'Marital Maintenance Playbook',
      summary: 'Slide deck on maintenance habits and seasons.',
      href: '../assets/media/tmc-husband/m01/slides/marital-maintenance-playbook.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'slides-tending-vineyard',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'Tending the Marital Vineyard',
      summary: 'Slide deck walking the four vineyard tasks.',
      href: '../assets/media/tmc-husband/m01/slides/tending-the-marital-vineyard.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'infographic-connection-roadmap',
      state: 'local',
      group: 'infographics',
      title: 'Marriage Connection Roadmap',
      summary: 'Visual roadmap of connection habits and checkpoints.',
      href: '../assets/media/tmc-husband/m01/infographics/marriage-connection-roadmap.png',
      alt: 'Infographic titled Marriage Connection Roadmap with panels on protected time, emotional needs, and vineyard maintenance tasks.'
    },
    {
      slug: 'infographic-vineyard-field-guide',
      state: 'local',
      group: 'infographics',
      title: 'Marriage Vineyard Field Guide',
      summary: 'Single-page field guide on adjusting, pruning, supporting, and renewing.',
      href: '../assets/media/tmc-husband/m01/infographics/marriage-vineyard-field-guide.png',
      alt: 'Infographic titled Marriage Vineyard Field Guide illustrating four vineyard tasks for marital maintenance.'
    },
    {
      slug: 'report-building-foundations',
      state: 'local',
      group: 'reports',
      title: 'Building Strong Foundations',
      summary: 'Neutral executive briefing on Episode 1.',
      href: '../assets/media/tmc-husband/m01/reports/episode-1-building-strong-foundations.md',
      linkLabel: 'Read the report'
    },
    {
      slug: 'report-we-to-me',
      state: 'local',
      group: 'reports',
      title: 'From We to Me: Navigating the Seasons of Connection',
      summary: 'Seasons-of-life framing — read against the caution section.',
      href: '../assets/media/tmc-husband/m01/reports/from-we-to-me-seasons-of-connection.md',
      linkLabel: 'Read the report'
    },
    {
      slug: 'report-vineyard-secret',
      state: 'local',
      group: 'reports',
      title: 'The Vineyard Secret: Five Surprising Lessons',
      summary: 'Popular-article register. Headline overclaims — use as prompt, not proof.',
      href: '../assets/media/tmc-husband/m01/reports/vineyard-secret-five-lessons.md',
      linkLabel: 'Read the report'
    },
    {
      slug: 'quiz-marriage-quiz',
      state: 'local',
      group: 'quiz',
      title: 'Marriage Quiz',
      summary: 'Knowledge check over Episode 1 material.',
      href: '../assets/media/tmc-husband/m01/quiz/marriage-quiz.html',
      linkLabel: 'Open the quiz'
    }
  ]
};

module.exports = { fieldManual };
