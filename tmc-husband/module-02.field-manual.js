'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one listen-back conversation',
  missionDurationMinutes: 45,
  finishLineHero: 'Complete one 15-minute listen-back conversation on a low-to-moderate concern — restate her view accurately before you give yours.',
  opening: [
    'Listening is not silence while preparing a rebuttal. Your wife is asking whether her words reached you without being filtered through self-protection.',
    'Accurate restatement is not agreement. The win is proving that disagreement does not have to erase her voice or your self-control.',
    'This week you practice once on a manageable concern — not the most explosive issue in your marriage.'
  ],
  scripture: [
    { reference: 'James 1:19–20', note: 'Quick listening and slow anger are practices of righteousness, not tactics for winning an argument.' },
    { reference: 'Proverbs 18:13, 17', note: 'Answering before listening is folly. Humility attends before concluding.' },
    { reference: 'Ephesians 4:25, 29', note: 'Truthful speech should fit the need and build up; truth is not permission for contempt or verbal force.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Name your listening failure',
      tagline: 'Pick one habit. Replace it for this week.',
      actions: [
        'Write one observable habit: interrupting, fixing, reassuring too quickly, hijacking with your own story, withdrawing, or rehearsing a rebuttal.',
        'Choose one replacement behavior for this week.',
        'Tell her which habit you are working on — with permission, not as a gotcha.'
      ]
    },
    {
      number: '2',
      title: 'Choose the conditions',
      actions: [
        'Ask for a workable time and select a quiet walk, porch, drive, or seated conversation.',
        'Do not choose bedtime, the bedroom, late night, the first minutes after work, or a moment when either of you is rushed or flooded.',
        'Sit at respectful distance. Keep the way out clear. Phone away.'
      ]
    },
    {
      number: '3',
      title: 'Ask permission and listen',
      actions: [
        'Say: "Is now a workable time for me to understand this without trying to fix it?"',
        'Give her up to five uninterrupted minutes.',
        'Do not cross-examine, correct chronology, or introduce your counter-case while she speaks.'
      ]
    },
    {
      number: '4',
      title: 'Listen back accurately',
      tagline: 'Fair does not mean she agrees with you.',
      actions: [
        'Say: "What I hear is… and it mattered because…"',
        'Ask: "What did I miss or distort?" Revise without defending yourself.',
        'Do not demand that she perform the same exercise in return.'
      ]
    },
    {
      number: '5',
      title: 'Clarify the need',
      actions: [
        'Ask: "Would empathy, an idea, a specific action, or more time help most?"',
        'Do not smuggle advice into the question.',
        'Write the action you own in your own task system — not her sensitive details.',
        'Return with evidence of follow-through rather than making her raise the subject again.'
      ]
    }
  ],
  selfCheck: [
    'What do I do in the first ten seconds after hearing criticism?',
    'Do I summarize her strongest point, or a weaker version I can dismiss?',
    'Can I tolerate her distress without rushing to make myself feel innocent?',
    'Would honest disclosure feel safe with my current patterns?'
  ],
  fieldAction: {
    title: 'Complete one listen-back conversation',
    steps: [
      'Choose one low-to-moderate concern and ask consent to practice.',
      'Listen without interruption for up to five minutes.',
      'Restate content and significance in your own words.',
      'Ask what you missed and revise before responding.'
    ],
    finishLine: 'Before giving your view, you restated her concern and its significance, asked what you missed, and revised until she said it was fair — without requiring agreement or reciprocal performance.'
  },
  conversation: {
    intro: 'Invite; do not assign. Your wife may decline any prompt without penalty.',
    items: [
      'When I listen poorly, what do you notice first?',
      'What helps you know I understood, even when we disagree?',
      'Is there a phrase or habit that makes you shut down?',
      'Would empathy, an idea, a specific action, or more time be most helpful?'
    ]
  },
  caution: 'Communication methods assume enough safety for honest speech. They fail where disclosure is punished, monitored, or weaponized. Not every problem is a misunderstanding — sometimes the issue is deception, intimidation, addiction, or injustice.',
  support: {
    lead: 'This course is formation for a basically safe marriage. It is not crisis care or a substitute for qualified help.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' },
      { label: 'Abuse or coercive control', body: 'Do not coach victims to "open up more" to an abuser. Seek confidential individual safety planning.' },
      { label: 'Betrayal, addiction, or entrenched high conflict', body: 'A licensed clinician with relevant specialisation.' }
    ],
    close: 'Never use Scripture, headship, money, children, or course completion to demand access, silence concern, or prevent help.'
  },
  resources: {
    intro: 'Optional study aids from your Notebook by Gemini notebook.',
    groups: [
      { key: 'video', heading: 'Watch', note: 'Video overviews.' },
      { key: 'audio', heading: 'Listen', note: 'Audio briefings.' },
      { key: 'slides', heading: 'Slide decks', note: 'PDF study decks.' },
      { key: 'infographics', heading: 'Field graphics', note: 'Visual summaries.' },
      { key: 'reports', heading: 'Read', note: 'Markdown study aids.' },
      { key: 'quiz', heading: 'Drill', note: 'Knowledge check.' },
      { key: 'flashcards', heading: 'Drill', note: 'Flashcard practice.' }
    ],
    withheldNotice: null,
    notebook: {
      title: 'Your Notebook by Gemini notebook',
      body: 'Google account required. Source for all study aids below.',
      label: 'Open "TMC (pt2): The Art of Effective Communication" in Notebook by Gemini',
      href: 'https://notebooklm.google.com/notebook/e9c6dfcf-b600-4159-b595-2723c4b0c252'
    },
    journal: {
      heading: 'Optional companion journal',
      label: 'The Marriage Course Study Journal',
      href: 'https://www.amazon.com/dp/0310116694?tag=usmcministrie-20',
      body: 'Optional journal exercises. This module works without it.',
      disclosure: 'Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.'
    }
  },
  assessment: {
    intro: 'Complete the quiz after working through the module tasks and field action.',
    quizHref: '../assets/media/tmc-husband/m02/quiz/communication-quiz.html',
    quizTitle: 'Module 2 Communication Quiz',
    flashcardsHref: '../assets/media/tmc-husband/m02/flashcards/marriage-flashcards.html',
    flashcardsTitle: 'Module 2 Marriage Flashcards'
  },
  artifacts: [
    { slug: 'video-effective-communication', state: 'local', group: 'video', kind: 'Video', title: 'Effective Communication', summary: 'Video overview of communication themes.', href: '../assets/media/tmc-husband/m02/video/effective-communication.mp4', mediaType: 'video' },
    { slug: 'video-five-listening-habits', state: 'local', group: 'video', kind: 'Video', title: '5 Listening Habits That Ruin Communication', summary: 'The five bad habits and how to interrupt them.', href: '../assets/media/tmc-husband/m02/video/five-listening-habits.mp4', mediaType: 'video' },
    { slug: 'audio-vulnerability-safety', state: 'local', group: 'audio', kind: 'Audio', title: 'Why vulnerability needs a safety check', summary: 'When disclosure exercises misfire.', href: '../assets/media/tmc-husband/m02/audio/vulnerability-safety-check.mp3', mediaType: 'audio' },
    { slug: 'audio-three-levels', state: 'local', group: 'audio', kind: 'Audio', title: 'The Three Levels of Deep Communication', summary: 'Facts, ideas, and feelings.', href: '../assets/media/tmc-husband/m02/audio/three-levels-of-communication.mp3', mediaType: 'audio' },
    { slug: 'slides-signal-noise', state: 'local', group: 'slides', kind: 'PDF', title: 'Signal and Noise', summary: 'Filtering signal from noise in marital talk.', href: '../assets/media/tmc-husband/m02/slides/signal-and-noise.pdf', linkLabel: 'Open slide deck' },
    { slug: 'slides-relational-architecture', state: 'local', group: 'slides', kind: 'PDF', title: 'Relational Architecture', summary: 'Communication structure and habits.', href: '../assets/media/tmc-husband/m02/slides/relational-architecture.pdf', linkLabel: 'Open slide deck' },
    { slug: 'infographic-art-of-communication', state: 'local', group: 'infographics', title: 'The Art of Effective Communication', summary: 'Visual summary of levels, habits, and listening.', href: '../assets/media/tmc-husband/m02/infographics/art-of-effective-communication.png', alt: 'Infographic titled The Art of Effective Communication showing three communication levels and listening habits.' },
    { slug: 'infographic-mastering-communication', state: 'local', group: 'infographics', title: 'Mastering Marriage Communication Guide', summary: 'Field guide for daily connection practices.', href: '../assets/media/tmc-husband/m02/infographics/mastering-marriage-communication.png', alt: 'Infographic titled Mastering Marriage Communication Guide with panels on listening and emotional disclosure.' },
    { slug: 'report-beyond-small-talk', state: 'local', group: 'reports', title: 'Beyond Small Talk', summary: 'Moving past logistics.', href: '../assets/media/tmc-husband/m02/reports/beyond-small-talk.md', linkLabel: 'Read the report' },
    { slug: 'report-lonelier', state: 'local', group: 'reports', title: 'Why You\'re Lonelier Than You Should Be', summary: 'Counter-intuitive truths about connection.', href: '../assets/media/tmc-husband/m02/reports/lonelier-than-you-should-be.md', linkLabel: 'Read the report' },
    { slug: 'report-effective-connection', state: 'local', group: 'reports', title: 'Effective Communication and Connection', summary: 'Executive briefing on communication.', href: '../assets/media/tmc-husband/m02/reports/effective-communication-and-connection.md', linkLabel: 'Read the report' },
    { slug: 'quiz-communication', state: 'local', group: 'quiz', title: 'Communication Quiz', summary: 'Knowledge check.', href: '../assets/media/tmc-husband/m02/quiz/communication-quiz.html', linkLabel: 'Open the quiz' },
    { slug: 'flashcards-marriage', state: 'local', group: 'flashcards', title: 'Marriage Flashcards', summary: 'Flashcard drill.', href: '../assets/media/tmc-husband/m02/flashcards/marriage-flashcards.html', linkLabel: 'Open the flashcards' }
  ]
};

module.exports = { fieldManual };
