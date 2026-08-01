'use strict';

// Module 2 field-manual — Episode 2: The Art of Effective Communication.
// Reconciled from 5 verified sources and 13 NotebookLM artifacts (pt2 notebook e9c6dfcf).

const fieldManual = {
  classification: 'Formation brief · approximately 75–90 minutes plus one week of fieldwork',
  objective: 'Widen the communication channel from logistics to understanding — listen back before you fix',
  sourceBase: 'The Marriage Course, Episode 2 — The Art of Effective Communication',
  reviewStatus: 'Live',
  missionDurationMinutes: 80,

  sectionNav: [
    { href: '#mission-brief', label: 'Brief', sectionId: 'mission-brief' },
    { href: '#scripture-frame', label: 'Scripture', sectionId: 'scripture-frame' },
    { href: '#communication-framework', label: 'Levels', sectionId: 'communication-framework' },
    { href: '#fair-insight', label: 'Fair', sectionId: 'fair-insight' },
    { href: '#caution-boundary', label: 'Caution', sectionId: 'caution-boundary' },
    { href: '#self-check', label: 'Check', sectionId: 'self-check' },
    { href: '#five-steps', label: 'Protocol', sectionId: 'five-steps' },
    { href: '#field-action', label: 'Exercise', sectionId: 'field-action' },
    { href: '#discussion-prompts', label: 'Prompts', sectionId: 'discussion-prompts' },
    { href: '#conversation-guide', label: 'Guide', sectionId: 'conversation-guide' },
    { href: '#resources', label: 'Media', sectionId: 'resources' },
    { href: '#assessment', label: 'Quiz', sectionId: 'assessment' },
    { href: '#completion', label: 'Finish', sectionId: 'completion' }
  ],

  inventory: {
    heading: 'Source and artifact reconciliation',
    summary: 'This module reconciles 5 verified sources and 13 completed artifacts from the Episode 2 research package. All thirteen review-safe artifacts are stored locally — video, audio, slides, graphics, reports, quiz, and flashcards from your pt2 NotebookLM notebook.',
    counts: [
      { value: '5', label: 'sources', detail: 'Episode 2 transcript plus four independent model reviews' },
      { value: '13', label: 'artifacts', detail: '2 video · 2 audio · 2 decks · 2 graphics · 3 reports · 1 quiz · 1 flashcards' },
      { value: '13', label: 'stored locally', detail: 'Full media room embedded below — not withheld' },
      { value: '0', label: 'withheld', detail: 'Episode 2 curated package is complete in-repo for this prototype' }
    ]
  },

  sources: [
    {
      slug: 'episode-2-transcript',
      lane: 'Primary source',
      title: 'Episode 2 transcript, The Marriage Course',
      note: 'A 1:47:32 session locally transcribed. Hosts appear as Nicky and Sila. Vimeo source: player.vimeo.com/video/403011574. Validate exact quotations before treating any line as canonical.'
    },
    {
      slug: 'chatgpt-review',
      lane: 'Chaplain and counsellor lens',
      title: 'ChatGPT independent review',
      note: 'Strongest on naming five listening habits as observable behaviors and on separating reassurance from empathy.'
    },
    {
      slug: 'claude-review',
      lane: 'Systems-analyst lens',
      title: 'Claude independent review',
      note: 'Strongest on the three-level model as a bandwidth diagnostic and on separating reflection from agreement.'
    },
    {
      slug: 'gemini-review',
      lane: 'Brotherly friend lens',
      title: 'Gemini independent review',
      note: 'Emphasises safety prerequisites before vulnerability exercises and facilitator boundaries.'
    },
    {
      slug: 'grok-review',
      lane: 'Grandfatherly theologian lens',
      title: 'Grok independent review',
      note: 'Strongest on graduated practice design and on when reflective listening must not be attempted.'
    }
  ],

  missionBrief: {
    heading: 'Connection runs on communication bandwidth',
    teaching: {
      heading: 'What the session actually teaches',
      paragraphs: [
        'Episode 2 opens with a plain claim: close connection in marriage depends on good communication, and communication is a skill couples must keep learning. The presenters model their own early failures — letters that worked, phone boxes that did not — before offering a teachable framework.',
        'The engine of the session is practical: three levels of communication (facts, ideas, feelings), five bad listening habits, a five-step reflective-listening protocol demonstrated live, and couple practice starting with a low-stakes memory before any contentious issue.'
      ],
      map: 'Teaching map: 00:04:40–00:06:06 · 00:47:05–00:52:47 · 01:00:41–01:03:35 · 01:04:04–01:10:19 · 01:42:01–01:42:17'
    },
    analysis: {
      heading: 'The husband’s assignment',
      paragraphs: [
        'Your assignment is not to win arguments or become the household therapist. It is to listen long enough that your wife can tell whether her words reached you — before you fix, explain, or defend. Listen-back is not agreement; it is disciplined attention.',
        'This module keeps two jobs separate. Where the marriage is ordinary and basically safe, practice widening the channel: add Level 3 moments, name your worst listening habit, and use reflective listening on one manageable concern. Where disclosure is punished, monitored, or weaponized, stop treating “talk more” as the problem and seek individual help first.'
      ]
    },
    endState: 'You can name which communication level dominates your marriage, interrupt one bad listening habit, and complete one listen-back conversation where your wife confirms your summary was fair.'
  },

  scripture: {
    heading: 'Quick to hear, slow to speak',
    quote: {
      text: 'Know this, my beloved brothers: let every person be quick to hear, slow to speak, slow to anger.',
      cite: 'James 1:19 (ESV)'
    },
    intro: 'Read each passage in its wider context before applying it. The caveat under each one is ministry analysis, not the text.',
    entries: [
      {
        reference: 'James 1:19–20',
        teaching: 'Episode 2 quotes this as the plainest warrant for listening first — quick to hear, slow to speak, slow to anger.',
        caveat: 'Slow to speak is not silence about real wrong. James requires doing, not only hearing. Anger is not always sin; injustice may rightly grieve you.'
      },
      {
        reference: 'Proverbs 18:13, 17',
        teaching: 'Answering before listening is folly; the first account deserves examination before conclusion.',
        caveat: 'Humility attends before concluding — but prolonged “listening” can also become avoidance of necessary truth-telling.'
      },
      {
        reference: 'Ephesians 4:25, 29',
        teaching: 'Truthful speech should fit the need and build up; communication serves love, not performance.',
        caveat: 'Truth is not permission for contempt or verbal force. “Speak truth” must never authorize coercion.'
      }
    ]
  },

  communicationFramework: {
    heading: 'Three levels and five listening habits',
    lead: 'The session’s central diagnostic is bandwidth: many couples live as polite roommates on Level 1 logistics while wondering why intimacy feels thin. Your job is to notice which level you are on and which listening habit terminates your wife’s disclosure.',
    levels: [
      {
        number: '01',
        name: 'Level 1 — Facts',
        source: 'Weather, trains, overdraft notices, schedules. Necessary logistics that produce only a weak connection if they are all you ever share.',
        husbandMove: 'Run a one-day audit: count conversations that never leave Level 1. If the count is high, schedule one protected block this week for Level 2 or 3 — not both at once.',
        guardrail: 'Logistics are not the enemy. Pretending you “never talk” when you talk constantly about logistics is a misdiagnosis.'
      },
      {
        number: '02',
        name: 'Level 2 — Ideas and opinions',
        source: 'Politics, parenting choices, weekend plans, job suggestions. Stronger connection than facts alone.',
        husbandMove: 'Before offering your opinion, ask whether she wanted ideas or only to be heard. Default to hearing first on emotional topics.',
        guardrail: 'Opinions can smuggle verdicts. “I think you should…” about her body, family, or competence is not Level 2 dialogue — it is pressure.'
      },
      {
        number: '03',
        name: 'Level 3 — Feelings and needs',
        source: 'Hurt, fear, gratitude, need for reassurance. Requires vulnerability and trust; the session treats this as where deep intimacy is built.',
        husbandMove: 'Once daily, add one brief Level 3 sentence that is not a preface to a request: “I felt proud when…” or “I’m anxious about…”',
        guardrail: 'Level 3 is not safe in every marriage. Do not coach more disclosure where feelings are used against the speaker.'
      }
    ],
    habits: [
      {
        number: '01',
        name: 'Disengaging',
        source: 'Internal monologue, memories, screens, lack of interest while the other person speaks.',
        husbandMove: 'When she speaks, phone face-down and out of reach. If you cannot attend now, name a return time instead of half-listening.',
        failureMode: 'Looking up from the phone occasionally while still scrolling.'
      },
      {
        number: '02',
        name: 'Reassuring too soon',
        source: 'Premature cheerfulness that blocks negative emotion — “Don’t worry, you’ll be fine.”',
        husbandMove: 'Replace reassurance with reflection: “That sounds exhausting” before any fix.',
        failureMode: 'Using positivity to shut down hurt because her distress makes you uncomfortable.'
      },
      {
        number: '03',
        name: 'Giving advice',
        source: 'Fixing instead of understanding — the session’s classic husband move.',
        husbandMove: 'Ask: “Do you want empathy, ideas, or action?” Default to empathy unless she chooses otherwise.',
        failureMode: 'Offering three solutions before she finishes the first sentence.'
      },
      {
        number: '04',
        name: 'Going off on a tangent',
        source: 'Hijacking with your own story before she finishes hers.',
        husbandMove: 'Keep a mental note: “My story can wait.” Save it until after her point is reflected accurately.',
        failureMode: '“That reminds me of when I…” within thirty seconds of her opening.'
      },
      {
        number: '05',
        name: 'Interrupting',
        source: 'Nicky models himself as a serial interrupter; Sila names the same habit.',
        husbandMove: 'Let her partner flag interruptions in real time — with mutual permission, not as a gotcha.',
        failureMode: 'Finishing her sentences because you are “helping.”'
      }
    ]
  },

  fairInsight: {
    heading: 'What the source gets right',
    paragraphs: [
      'All four independent reviews converge: Episode 2 lowers shame by treating communication as learnable engineering, not character verdict. The presenters admit their own habits — interrupter, reassurer — which makes the skills adoptable.',
      'The three-level model, five habits, and reflective-listening protocol give husbands something observable on an ordinary evening. Separating reflect from respond is the load-bearing move: understanding before advocacy.'
    ]
  },

  caution: {
    heading: 'Where caution is required',
    paragraphs: [
      'The session assumes two willing, roughly safe partners. Reflective listening asks for vulnerability; in coercive or contemptuous marriages that can increase risk. The episode names the need for safety but offers little verification.',
      '“Based on a lot of research” is asserted without citation. Anecdotes — celebrity divorce quotes, Nick-and-Allison’s reconciliation — illustrate; they do not prove outcomes.'
    ],
    slogans: [
      {
        line: 'Listen twice as much as we talk.',
        stamp: 'Source teaching, near 00:07:50',
        qualification: 'Useful corrective for monologues. Unhelpful if one partner already over-functions as listener while the other dominates.'
      },
      {
        line: 'Change is possible — it takes courage.',
        stamp: 'Source teaching, near 00:27:08',
        qualification: 'Hope, not guarantee. Difficulty naming feelings may reflect trauma, neurodivergence, or depression — not only reticence.'
      },
      {
        line: 'They need to know you’re not going to get angry, reject, or blame them.',
        stamp: 'Source teaching, near 00:30:01',
        qualification: 'Essential requirement — but the episode does not say what to do when that requirement is not met.'
      }
    ],
    additional: [
      'Level 3 as gold standard can bias against cultures and temperaments that show love through action, not feeling-words.',
      'Reflecting back an accusatory read validates it unless you separate feeling from assumed intent.',
      'Do not use this protocol on infidelity, abuse, addiction, or gridlocked betrayal without qualified help.',
      'The napkin/talking-object exercise is wise for turn-taking — not a substitute for safety planning.'
    ]
  },

  selfCheck: {
    heading: 'Husband’s self-check',
    intro: 'Reflect privately. Do not use these prompts to diagnose or score your wife.',
    items: [
      'Which level do most of our conversations stay on — facts, ideas, or feelings?',
      'Which of the five bad listening habits is mine — not hers?',
      'What do I do in the first ten seconds after hearing criticism?',
      'Do I summarize her fairly, or a weaker version that is easy to dismiss?',
      'Can I ask whether she wants empathy, ideas, or action before choosing for her?',
      'Would deeper disclosure feel safe to her with my current patterns — honestly?'
    ]
  },

  fiveSteps: {
    heading: 'Five-step reflective listening',
    intro: 'The session’s protocol near 01:00:41–01:03:35. Use for emotional or unresolved topics — not for “please make coffee.”',
    preconditions: [
      'Basically safe marriage; either spouse may stop without penalty.',
      'One manageable concern — not the most explosive issue in the marriage.',
      'Physical talking object optional (napkin, pen) to mark whose turn it is.',
      'Understanding before agreement; reflection is not surrender.'
    ],
    steps: [
      {
        number: '1',
        step: 'Put yourself in her shoes; do not rush',
        source: 'Tolerate silence. The listener’s job is presence, not performance.',
        execution: 'Sit at respectful distance, eyes available but not staring her down. Let five seconds of silence pass without filling it.',
        failureMode: 'Nodding rapidly while composing your rebuttal.'
      },
      {
        number: '2',
        step: 'Reflect content and feelings',
        source: 'Repeat main points in your own words — without agreeing, disagreeing, or offering your view yet.',
        execution: '“You felt alone when I stayed on my phone, and it made you wonder whether your exhaustion mattered to me.”',
        failureMode: 'Reflecting a weaker version: “So you’re annoyed about the phone sometimes.”'
      },
      {
        number: '3',
        step: 'Ask what mattered most; reflect again',
        source: '“What’s the most important part of what you’ve been saying?” then summarize that priority.',
        execution: 'If she corrects you, revise without defending. Accuracy matters more than speed.',
        failureMode: 'Treating correction as an attack on your intelligence.'
      },
      {
        number: '4',
        step: 'Draw out her ideas before advising',
        source: 'Ask what she might want to do — resist inserting your solution first.',
        execution: '“What would help?” or “What do you wish I understood better?” Then listen again.',
        failureMode: 'Smuggling advice inside a question: “Have you considered just…”'
      },
      {
        number: '5',
        step: 'Ask if there is anything else',
        source: 'Close the loop before you take your turn to share your perspective.',
        execution: 'Only after she confirms the summary: ask permission to share your view. Speak from your experience, not verdicts on her character.',
        failureMode: 'Using step five to close the topic: “Anything else? Good — here’s why you’re wrong.”'
      }
    ],
    close: 'The win is not persuasion. It is proving disagreement does not have to erase her voice or your self-control.'
  },

  fieldExercise: {
    heading: 'One-week listen-back exercise',
    intro: 'Either spouse may stop any step. If fear or contempt dominates, stop and seek help instead of powering through.',
    days: [
      { day: 'Day 1', title: 'Bandwidth audit.', body: 'Each partner tallies conversations by level (1/2/3). Compare at night — no fixing, only counting.' },
      { day: 'Day 2', title: 'Name your habit.', body: 'Each picks one worst listening habit from the five and tells the other — “I interrupt when excited.”' },
      { day: 'Day 3', title: 'Reflect once.', body: 'Ten minutes on a low-stakes topic: listener does steps 1–2 only, zero advice.' },
      { day: 'Day 4', title: 'Talking object.', body: 'Repeat with a napkin or pen marking the speaker. Count interruptions.' },
      { day: 'Day 5', title: 'Feeling without verdict.', body: 'Each names one feeling and separates it from assumed intent about the other.' },
      { day: 'Day 6', title: 'Full protocol.', body: 'Fifteen minutes on a mildly contentious issue — all five steps, then swap if willing.' },
      { day: 'Day 7', title: 'Review.', body: 'Re-tally levels vs Day 1. Each names one help and one contrivance. Stop if unsafe.' }
    ],
    finishLine: 'Your wife confirms that one listen-back summary represented her concern accurately enough, without being required to agree with you or repeat the exercise.'
  },

  discussionPrompts: {
    heading: 'Discussion prompts',
    intro: 'Invite; do not assign. Your wife may decline any prompt without penalty.',
    items: [
      'Which level do we spend most conversation on — and what pushes us down to logistics only?',
      'Of the five habits, which is mine? How would you know?',
      'When I reassure you, what am I protecting — you, or my discomfort with your distress?',
      'What would make Level 3 feel safe enough for you — one concrete behavior from me?',
      'Where does this technique not belong for us — what topics need a counselor, not a napkin?'
    ]
  },

  conversationGuide: {
    heading: 'Optional listen-back conversation',
    intro: 'Use after the field exercise or on its own. Choose one low-to-moderate concern.',
    steps: [
      { label: 'Ask consent', body: '“Is now a workable time for me to listen without trying to fix?”' },
      { label: 'Listen', body: 'Up to five minutes without interruption. Phone away.' },
      { label: 'Reflect', body: 'Restate content and significance in your own words.' },
      { label: 'Revise', body: '“What did I miss or distort?” Adjust until she confirms accuracy.' },
      { label: 'Ask need', body: '“Would empathy, an idea, a specific action, or more time be most helpful?”' }
    ],
    pauseSignal: 'If either person becomes flooded, name a pause and a specific return time — same rules as Module 3’s pause protocol.'
  },

  referral: {
    heading: 'Support and safety boundary',
    lead: 'This module is education for a basically safe marriage. It is not crisis care, clinical treatment, or a substitute for qualified help.',
    distinction: 'Communication skills assume enough safety for honest speech. They fail where disclosure is punished or weaponized.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.', href: null },
      { label: 'Abuse or coercive control', body: 'Do not coach victims to “open up more” or “listen better” to an abuser. Seek confidential individual safety planning.' },
      { label: 'Betrayal, addiction, trauma, or entrenched high conflict', body: 'A licensed clinician with relevant specialisation. Trained pastoral care supports that work; it does not replace it.', href: null }
    ],
    close: 'Never use Scripture, headship, money, children, or course completion to demand access, silence concern, or prevent help.'
  },

  verification: {
    heading: 'Claims carried forward for verification',
    intro: 'Ministry analysis. Flagged by independent review; not settled on this page.',
    items: [
      '“Reflective listening is based on a lot of research” near 01:00:45 — no source named.',
      'Celebrity-divorce newspaper quote near 00:08:43 — anonymous illustration only.',
      'Nick-and-Allison reconciliation story near 00:27:43 — testimony, not mechanism.',
      'Presenter surnames — transcript gives Nicky and Sila; Gumbel not confirmed in every segment.'
    ]
  },

  resources: {
    heading: 'Resource room',
    intro: 'Thirteen NotebookLM artifacts from your Episode 2 notebook, embedded here. Treat generated media as study aids — read against the caution section above.',
    groups: [
      { key: 'video', heading: 'Video overviews', count: '2 artifacts', note: 'Explainer videos from NotebookLM.' },
      { key: 'audio', heading: 'Audio briefings', count: '2 artifacts', note: 'Critical companion listens — safety and levels.' },
      { key: 'slides', heading: 'Slide decks', count: '2 artifacts', note: 'PDF exports from NotebookLM.' },
      { key: 'infographics', heading: 'Field graphics', count: '2 artifacts', note: 'Single-page visual summaries.' },
      { key: 'reports', heading: 'Readable reports', count: '3 artifacts', note: 'Markdown study aids in different registers.' },
      { key: 'quiz', heading: 'Knowledge check', count: '1 artifact', note: 'Interactive NotebookLM export — also embedded below.' },
      { key: 'flashcards', heading: 'Flashcards', count: '1 artifact', note: 'Interactive NotebookLM export — also embedded below.' }
    ],
    withheldNotice: null,
    notebook: {
      title: 'Your NotebookLM notebook',
      body: 'Google account required. This is the canonical source for all artifacts below.',
      label: 'Open “TMC (pt2): The Art of Effective Communication” in NotebookLM',
      href: 'https://notebooklm.google.com/notebook/e9c6dfcf-b600-4159-b595-2723c4b0c252'
    },
    journal: {
      heading: 'Optional companion journal',
      label: 'The Marriage Course Study Journal',
      href: 'https://www.amazon.com/dp/0310116694?tag=usmcministrie-20',
      body: 'Episode 2 directs couples to journal exercises for emotion identification and practice conversations. Optional — this module works without it.',
      disclosure: 'Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.'
    }
  },

  assessment: {
    heading: 'Knowledge check and flashcards',
    intro: 'Complete the quiz and flashcard drill after working through the module.',
    quizHref: '../assets/media/tmc-husband/m02/quiz/communication-quiz.html',
    quizTitle: 'Episode 2 Communication Quiz',
    flashcardsHref: '../assets/media/tmc-husband/m02/flashcards/marriage-flashcards.html',
    flashcardsTitle: 'Episode 2 Marriage Flashcards'
  },

  artifacts: [
    {
      slug: 'video-effective-communication',
      state: 'local',
      group: 'video',
      kind: 'Video',
      title: 'Effective Communication',
      summary: 'NotebookLM explainer on Episode 2 themes.',
      href: '../assets/media/tmc-husband/m02/video/effective-communication.mp4',
      mediaType: 'video'
    },
    {
      slug: 'video-five-listening-habits',
      state: 'local',
      group: 'video',
      kind: 'Video',
      title: '5 Listening Habits That Ruin Communication',
      summary: 'Video on the five bad habits and how to interrupt them.',
      href: '../assets/media/tmc-husband/m02/video/five-listening-habits.mp4',
      mediaType: 'video'
    },
    {
      slug: 'audio-vulnerability-safety',
      state: 'local',
      group: 'audio',
      kind: 'Audio',
      title: 'Why vulnerability needs a safety check',
      summary: 'Critical audio on when disclosure exercises misfire.',
      href: '../assets/media/tmc-husband/m02/audio/vulnerability-safety-check.mp3',
      mediaType: 'audio'
    },
    {
      slug: 'audio-three-levels',
      state: 'local',
      group: 'audio',
      kind: 'Audio',
      title: 'The Three Levels of Deep Communication',
      summary: 'Audio walkthrough of facts, ideas, and feelings.',
      href: '../assets/media/tmc-husband/m02/audio/three-levels-of-communication.mp3',
      mediaType: 'audio'
    },
    {
      slug: 'slides-signal-noise',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'Signal and Noise',
      summary: 'Slide deck on filtering signal from noise in marital talk.',
      href: '../assets/media/tmc-husband/m02/slides/signal-and-noise.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'slides-relational-architecture',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'Relational Architecture',
      summary: 'Slide deck on communication structure and habits.',
      href: '../assets/media/tmc-husband/m02/slides/relational-architecture.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'infographic-art-of-communication',
      state: 'local',
      group: 'infographics',
      title: 'The Art of Effective Communication',
      summary: 'Visual summary of levels, habits, and listening protocol.',
      href: '../assets/media/tmc-husband/m02/infographics/art-of-effective-communication.png',
      alt: 'Infographic titled The Art of Effective Communication showing three communication levels and listening habits.'
    },
    {
      slug: 'infographic-mastering-communication',
      state: 'local',
      group: 'infographics',
      title: 'Mastering Marriage Communication Guide',
      summary: 'Field guide graphic for daily connection practices.',
      href: '../assets/media/tmc-husband/m02/infographics/mastering-marriage-communication.png',
      alt: 'Infographic titled Mastering Marriage Communication Guide with panels on listening and emotional disclosure.'
    },
    {
      slug: 'report-beyond-small-talk',
      state: 'local',
      group: 'reports',
      title: 'Beyond Small Talk',
      summary: 'Popular-article register on moving past logistics.',
      href: '../assets/media/tmc-husband/m02/reports/beyond-small-talk.md',
      linkLabel: 'Read the report'
    },
    {
      slug: 'report-lonelier',
      state: 'local',
      group: 'reports',
      title: 'Why You’re Lonelier Than You Should Be',
      summary: 'Five counter-intuitive truths about connection — read against caution.',
      href: '../assets/media/tmc-husband/m02/reports/lonelier-than-you-should-be.md',
      linkLabel: 'Read the report'
    },
    {
      slug: 'report-effective-connection',
      state: 'local',
      group: 'reports',
      title: 'Effective Communication and Connection',
      summary: 'Neutral executive briefing on Episode 2.',
      href: '../assets/media/tmc-husband/m02/reports/effective-communication-and-connection.md',
      linkLabel: 'Read the report'
    },
    {
      slug: 'quiz-communication',
      state: 'local',
      group: 'quiz',
      title: 'Communication Quiz',
      summary: 'Knowledge check over Episode 2 material.',
      href: '../assets/media/tmc-husband/m02/quiz/communication-quiz.html',
      linkLabel: 'Open the quiz'
    },
    {
      slug: 'flashcards-marriage',
      state: 'local',
      group: 'flashcards',
      title: 'Marriage Flashcards',
      summary: 'Flashcard drill over the same material.',
      href: '../assets/media/tmc-husband/m02/flashcards/marriage-flashcards.html',
      linkLabel: 'Open the flashcards'
    }
  ]
};

module.exports = { fieldManual };
