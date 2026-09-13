'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one conflict practice',
  missionDurationMinutes: 45,
  finishLineHero: 'Name your conflict pattern, establish a pause-and-return rule while calm, and use it once; with a specific return time so pause cannot become avoidance.',
  opening: [
    'Conflict is not proof that a marriage is defective. The decisive question is what you do when pressure rises; not whether disagreement appears.',
    'Your assignment is to name the move you make first, negotiate a pause rule while calm, and address one moderate issue as a team against the problem.',
    'Team language becomes dangerous when it hides one-sided abuse. If there is fear, control, or harm, stop couple exercises and seek individual help.'
  ],
  scripture: [
    { reference: 'Proverbs 15:1, 18', note: 'Gentleness can turn down heat; a hot temper multiplies conflict. Gentleness is strength under control, not silence about wrong.' },
    { reference: 'Ephesians 4:26–27, 31–32', note: 'Repair harmful conduct promptly. Emotional forgiveness, safety, and resolution cannot be forced onto a nightly deadline.' },
    { reference: 'Romans 12:18', note: '"If possible, so far as it depends on you" recognizes both personal responsibility and the limit of controlling another person.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Name your move',
      tagline: 'Name the behavior, not the temperament.',
      actions: [
        'Write what you do first under pressure; raise your voice, interrupt, pursue, withdraw, explain, become sarcastic, surrender, or widen the argument.',
        'Tell your wife in one sentence without naming her pattern.',
        'Watch for contempt: mockery, sneering, hostile imitation; stop and repair specifically if it appears.'
      ]
    },
    {
      number: '2',
      title: 'Set the pause rule while calm',
      actions: [
        'Agree on a phrase either spouse may use, a minimum pause length, a maximum return window, and how a new time will be communicated.',
        'A pause without a return time is avoidance; not stewardship.',
        'No following room to room, blocking doors, taking phones, or forcing eye contact.',
        'If returning reliably is beyond your current skill, seek support before the next heated moment.'
      ],
      callout: {
        label: 'This is not a pause',
        body: 'Leaving with no return time, blocking an exit, or requiring unsafe re-engagement. If you are afraid of your spouse, a safety exit is different from a conflict pause; you owe no return time.'
      }
    },
    {
      number: '3',
      title: 'Choose one moderate issue',
      actions: [
        'State the issue in one observable sentence before you say anything about her.',
        'Do not start in bed, late at night, while rushing, immediately after arriving home, before a special event, or in front of children.',
        'Name your own contribution before assigning hers.',
        'Agree on the one decision that actually needs to be made; not ten years of history.'
      ]
    },
    {
      number: '4',
      title: 'Work the issue as a team',
      actions: [
        'Each person describes one event, its effect, and a request.',
        'Listen back before replying.',
        'Generate at least three possible next steps before choosing one.',
        'If either person becomes flooded, call the pause and return at the promised time.'
      ]
    },
    {
      number: '5',
      title: 'Write the decision',
      actions: [
        'Record who will do what, by when, and when you will review it.',
        'If you use the pause, return when promised. If the time becomes impossible, name a specific replacement time.',
        'Repair conduct that happened during conflict; not only the original topic. Do not use apology to close the subject prematurely.'
      ]
    }
  ],
  selfCheck: [
    'Can I describe my first conflict move as behavior rather than personality?',
    'Do I name my contribution before assigning hers?',
    'Have I kept my last three promised return times?',
    'Do I ever use volume, pursuit, blocking, sarcasm, Scripture, money, or the children to gain leverage?'
  ],
  fieldAction: {
    title: 'Establish and use your pause-and-return rule',
    steps: [
      'Name your own pattern in concrete behavior.',
      'Negotiate the pause rule while calm; phrase, minimum pause, return window.',
      'Choose one moderate issue and work it as a team.',
      'Write the decision with a review date, or use the pause once with a honored return time.'
    ],
    finishLine: 'Your rule is written down, every boundary was honored, any pause included a specific return time, and one moderate issue ended with a written next step and review date.'
  },
  conversation: {
    intro: 'Invite; do not assign. Either spouse may call a pause at any point.',
    items: [
      'What do I do in conflict that makes it harder for you to stay engaged?',
      'What times or places should be off-limits for hard conversations?',
      'What pause phrase and return window would feel trustworthy?',
      'When we disagree, what would make it feel more like us versus the problem?'
    ]
  },
  caution: 'Team language becomes dangerous when it hides one-sided abuse. Violence, threats, coercive control, stalking, and intimidation are not merely a mutual "cycle." Couple exercises may be inappropriate until individual safety and accountability are established.',
  support: {
    lead: 'This module is education for a basically safe marriage. It is not counselling, crisis care, or trauma care.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' },
      { label: 'Abuse or coercive control', body: 'Seek confidential individual safety planning. Joint exercises may be unsafe when control or fear is present.' },
      { label: 'Suicidal or mental-health crisis', body: 'In the U.S., call or text 988.', href: 'https://988lifeline.org/', linkLabel: '988lifeline.org' },
      { label: 'Betrayal, addiction, or entrenched high conflict', body: 'A licensed clinician with relevant specialisation.' }
    ],
    close: 'Never use Scripture, forgiveness, headship, money, children, or course completion to demand access, silence concern, or prevent help.'
  },
  resources: {
    intro: 'Optional study aids. Three audio and three video overviews are not hosted here.',
    groups: [
      { key: 'video', heading: 'Watch', note: 'Short video overviews.' },
      { key: 'audio', heading: 'Listen', note: 'Audio briefings for deeper reflection.' },
      { key: 'slides', heading: 'Slide decks', note: 'PDF study decks.' },
      { key: 'infographics', heading: 'Study graphics', note: 'Visual summaries; read against the caution above.' },
      { key: 'reports', heading: 'Read', note: 'Study reports as clean, printable PDFs.' },
      { key: 'quiz', heading: 'Drill', note: 'Knowledge check.' },
      { key: 'flashcards', heading: 'Drill', note: 'Flashcard practice.' },
      { key: 'withheld', heading: 'In your notebook only', note: 'Audio and video overviews not hosted on this site.' }
    ],
    withheldNotice: null,

    journal: {
      heading: 'Optional companion journal',
      label: 'The Marriage Course Study Journal',
      href: 'https://www.amazon.com/dp/0310116694?tag=usmcministrie-20',
      body: 'Optional written exercises for appreciations and the five-step protocol.',
      disclosure: 'Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.'
    }
  },
  assessment: {
    intro: 'Complete the quiz after working through the module tasks and required action.',
    quizHref: '../assets/media/tmc-husband/m03/quiz/marriage-quiz.html',
    quizTitle: 'Module 3 Marriage Quiz',
    flashcardsHref: '../assets/media/tmc-husband/m03/flashcards/marriage-flashcards.html',
    flashcardsTitle: 'Module 3 Marriage Flashcards'
  },
  artifacts: [
    { slug: "video-resolving-conflict", state: "local", group: "video", kind: "Video", title: "Resolving Conflict", summary: "Session video on working a disagreement without making the marriage the battlefield.", href: "../assets/media/tmc-husband/m03/video/resolving-conflict.mp4", mediaType: "video" },
    { slug: "video-navigating-conflict", state: "local", group: "video", kind: "Video", title: "Navigating Conflict", summary: "How couples move from position-trading to shared problem-solving.", href: "../assets/media/tmc-husband/m03/video/navigating-conflict.mp4", mediaType: "video" },
    { slug: "video-how-to-externalize-marriage-conflict", state: "local", group: "video", kind: "Video", title: "How to Externalise a Conflict", summary: "Putting the problem on the table instead of across from you.", href: "../assets/media/tmc-husband/m03/video/how-to-externalize-marriage-conflict.mp4", mediaType: "video" },
    { slug: "audio-why-your-partner-is-not-the-problem", state: "local", group: "audio", kind: "Audio", title: "Why Your Partner Is Not the Problem", summary: "Deep-dive audio on separating the person from the problem.", href: "../assets/media/tmc-husband/m03/audio/why-your-partner-is-not-the-problem.mp3", mediaType: "audio" },
    { slug: "audio-when-good-marriage-advice-goes-wrong", state: "local", group: "audio", kind: "Audio", title: "When Good Marriage Advice Goes Wrong", summary: "Critical audio on where conflict advice misfires. Read against the module caution.", href: "../assets/media/tmc-husband/m03/audio/when-good-marriage-advice-goes-wrong.mp3", mediaType: "audio" },
    { slug: "audio-when-marriage-tools-become-dangerous-weapons", state: "local", group: "audio", kind: "Audio", title: "When Marriage Tools Become Dangerous Weapons", summary: "Safety inversion: how a fair-fighting rule becomes a control tactic.", href: "../assets/media/tmc-husband/m03/audio/when-marriage-tools-become-dangerous-weapons.mp3", mediaType: "audio" },
    { slug: "slides-the-marriage-blueprint", state: "local", group: "slides", kind: "PDF", title: "The Marriage Blueprint", summary: "Session overview deck.", href: "../assets/media/tmc-husband/m03/slides/the-marriage-blueprint.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-marital-conflict-blueprint", state: "local", group: "slides", kind: "PDF", title: "Marital Conflict Blueprint", summary: "Four principles through five steps.", href: "../assets/media/tmc-husband/m03/slides/marital-conflict-blueprint.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-engineering-us", state: "local", group: "slides", kind: "PDF", title: "Engineering Us", summary: "Systems view of marriage maintenance.", href: "../assets/media/tmc-husband/m03/slides/engineering-us.pdf", linkLabel: "Open slide deck" },
    { slug: "infographic-marriage-conflict-resolution-field-guide", state: "local", group: "infographics", title: "Marriage Conflict Resolution Field Guide", summary: "Navigating the Waves Together; includes a red-flag panel.", href: "../assets/media/tmc-husband/m03/infographics/marriage-conflict-resolution-field-guide.png", alt: "Illustrated field guide titled Navigating the Waves Together with panels on teamwork, appreciation, and the five-step protocol." },
    { slug: "infographic-marriage-conflict-and-teamwork-guide", state: "local", group: "infographics", title: "Marriage Conflict and Teamwork Guide", summary: "Navigating the Storm; includes a safety overlay.", href: "../assets/media/tmc-husband/m03/infographics/marriage-conflict-and-teamwork-guide.png", alt: "Illustrated guide titled Navigating the Storm with a conflict toolkit and a seven-day action plan." },
    { slug: "infographic-marriage-teamwork-guide", state: "local", group: "infographics", title: "Marriage Teamwork Guide", summary: "Five cards on appreciation, differences, timing, and support.", href: "../assets/media/tmc-husband/m03/infographics/marriage-teamwork-guide.png", alt: "Illustrated guide titled From Conflict to Connection showing five teamwork cards." },
    { slug: "report-conflict-resolution-and-partnership-briefing", state: "local", group: "reports", title: "Conflict Resolution and Partnership", summary: "Executive briefing; best starting point.", href: "../assets/media/tmc-husband/m03/reports/conflict-resolution-and-partnership-briefing.pdf", linkLabel: "Read the report" },
    { slug: "report-from-clashing-oars-to-gliding-boats", state: "local", group: "reports", title: "From Clashing Oars to Gliding Boats", summary: "Systems-flavoured treatment of the rowing metaphor.", href: "../assets/media/tmc-husband/m03/reports/from-clashing-oars-to-gliding-boats.pdf", linkLabel: "Read the report" },
    { slug: "report-why-your-biggest-disagreements-secret-weapon", state: "local", group: "reports", title: "Why Your Biggest Disagreements Might Be Your Secret Weapon", summary: "Popular-article register; the headline overclaims; read against the caution.", href: "../assets/media/tmc-husband/m03/reports/why-your-biggest-disagreements-secret-weapon.pdf", linkLabel: "Read the report" },
    { slug: "quiz-marriage-quiz", state: "local", group: "quiz", title: "Marriage Quiz", summary: "Knowledge check over this module.", href: "../assets/media/tmc-husband/m03/quiz/marriage-quiz.html", linkLabel: "Open the quiz" },
    { slug: "flashcards-marriage-flashcards", state: "local", group: "flashcards", title: "Marriage Flashcards", summary: "Flashcard drill over this module.", href: "../assets/media/tmc-husband/m03/flashcards/marriage-flashcards.html", linkLabel: "Open the flashcards" }
  ]
};

module.exports = { fieldManual };
