'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one check-in this week',
  missionDurationMinutes: 45,
  finishLineHero: 'Schedule a weekly 20-minute marriage check-in, complete the first one, and follow through with one act of care based on what you heard.',
  opening: [
    'A strong marriage is built out of protected attention and repeated habits, so this module asks for one small thing done once rather than a dramatic evening you will not repeat.',
    'Your first assignment is not to grade your wife but to establish a rhythm she can reasonably expect: invite, listen, own one responsibility, act, and come back.',
    'Her participation is invited, not demanded. If she declines today, you can still schedule the rhythm, write honest answers yourself, and complete a no-strings-attached act of care.'
  ],
  scripture: [
    { reference: 'Matthew 7:24–27', note: 'Jesus connects hearing with doing. Obedient discipleship is not a guarantee that a faithful husband controls every outcome.' },
    { reference: 'Ephesians 5:21, 25–33', note: 'Verse 21 opens a household code of paired commands, and Paul never reverses the direction inside a pair. A wife\'s submission and a husband\'s self-giving love are two different callings, not one symmetrical rule; both spouses answer to Christ, and headship never authorizes coercion, entitlement, or concealment of harm.' },
    { reference: 'James 1:19–22', note: 'Quick listening and practiced obedience expose the gap between religious speech and embodied faithfulness.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Schedule the check-in',
      tagline: 'Twenty uninterrupted minutes. Not a performance review.',
      actions: [
        'Ask: "I want to protect twenty minutes for us each week — not to grade our marriage, just to stay connected. Would [day/time] work?"',
        'Choose a quiet, neutral setting. Do not begin in bed, late at night, during a rushed transition, or when either of you is already upset.',
        'Put the time on your calendar only after she agrees — or after you have made a respectful invitation she may decline without penalty.'
      ]
    },
    {
      number: '2',
      title: 'Prepare three questions',
      actions: [
        'Write: "What felt good between us this week?"',
        'Write: "What felt heavy?"',
        'Write: "What is one small thing I could do that would help?"',
        'Do not prepare a defense, a correction script, or a list of complaints for her.'
      ]
    },
    {
      number: '3',
      title: 'Complete the first check-in',
      actions: [
        'Put phones away. Keep the meeting to twenty minutes unless she freely wants more.',
        'Listen without correcting her memory or explaining your intent.',
        'Share one pressure of your own without making her responsible to fix it.',
        'End on time. A trustworthy rhythm respects the boundary it promises.'
      ]
    },
    {
      number: '4',
      title: 'Act before the next check-in',
      actions: [
        'Complete one reasonable act of care connected to what you heard.',
        'Do it without announcing points, expecting praise, or requiring reciprocity.',
        'Write no private report about her answers. Store no sensitive details in this course.'
      ]
    },
    {
      number: '5',
      title: 'Protect the rhythm',
      actions: [
        'Put the next check-in on the calendar before the first one ends.',
        'If the first time did not work, repair the miss and choose another time — do not quit because it felt awkward.',
        'Do not turn consistency into surveillance. A check-in is not a performance review or evidence that you are now entitled to praise.'
      ]
    }
  ],
  selfCheck: [
    'Does my wife receive protected attention, or only what remains after everything else?',
    'When she names a need, do I get curious or begin proving my intent?',
    'What promise have my repeated habits contradicted?',
    'Am I pursuing connection calmly, or seeking reassurance that I am a good husband?'
  ],
  fieldAction: {
    title: 'Establish your weekly 20-minute marriage check-in',
    steps: [
      'Ask for a mutually workable time in a neutral setting.',
      'Complete the first check-in using your three questions.',
      'Choose one action you personally own before the next meeting.',
      'Schedule the next check-in before this one ends.'
    ],
    finishLine: 'The next check-in is on the calendar, the first check-in occurred, and you completed one small act of care based on what you heard — whether or not she participated.'
  },
  conversation: {
    intro: 'Invite; do not assign. Your wife may decline, stop, or suggest another format without penalty.',
    items: [
      'What would make a weekly check-in feel useful rather than burdensome?',
      'What helped you feel connected to me this week?',
      'What is one small pressure I could help carry?',
      'What one action would be most useful for me to own before we talk again?'
    ]
  },
  caution: 'Relationship habits help basically safe couples; they do not repair violence, coercive control, active betrayal, or addiction by themselves. A husband\'s initiative is not authority to compel participation. If there is fear, coercion, violence, or immediate danger, seek confidential individual help first — not a joint exercise.',
  support: {
    lead: 'This course is formation for a basically safe marriage. It is not crisis care, clinical treatment, or a substitute for qualified pastoral counsel.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' },
      { label: 'Abuse or coercive control', body: 'Seek confidential individual safety planning. Joint exercises are not automatically appropriate when control or fear is present.' },
      { label: 'Betrayal, addiction, or trauma', body: 'A licensed clinician with relevant specialisation. Trained pastoral care supports that work; it does not replace it.' }
    ],
    close: 'Never use Scripture, headship, money, children, or course completion to demand access, silence concern, or prevent help.'
  },
  resources: {
    intro: 'Optional study aids from your Notebook by Gemini notebook. Listen, watch, read, or drill — then return to your field action.',
    groups: [
      { key: 'video', heading: 'Watch', note: 'Short video overviews.' },
      { key: 'audio', heading: 'Listen', note: 'Audio briefings for deeper reflection.' },
      { key: 'slides', heading: 'Slide decks', note: 'PDF study decks.' },
      { key: 'infographics', heading: 'Field graphics', note: 'Single-page visual summaries.' },
      { key: 'reports', heading: 'Read', note: 'Study reports as clean, printable PDFs.' },
      { key: 'ministry', heading: 'From U.S.M.C. Ministries', note: 'Our own writing on questions this module raises.' },
      { key: 'quiz', heading: 'Drill', note: 'Interactive knowledge check.' }
    ],
    withheldNotice: null,
    notebook: {
      title: 'Your Notebook by Gemini notebook',
      body: 'Google account required. This is the source for all study aids below.',
      label: 'Open "TMC (pt1): Building Strong Connections" in Notebook by Gemini',
      href: 'https://notebooklm.google.com/notebook/a9e8db5b-8b6b-48f9-8d91-74165d6215ab'
    },
    journal: {
      heading: 'Optional companion journal',
      label: 'The Marriage Course Study Journal',
      href: 'https://www.amazon.com/dp/0310116694?tag=usmcministrie-20',
      body: 'Optional written exercises. This module works without it.',
      disclosure: 'Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.'
    }
  },
  assessment: {
    intro: 'Complete the quiz after working through the module tasks and field action.',
    quizHref: '../assets/media/tmc-husband/m01/quiz/marriage-quiz.html',
    quizTitle: 'Module 1 Marriage Quiz'
  },
  artifacts: [
    { slug: 'video-the-marriage-course', state: 'local', group: 'video', kind: 'Video', title: 'The Marriage Course', summary: 'Video overview of foundation themes.', href: '../assets/media/tmc-husband/m01/video/the-marriage-course.mp4', mediaType: 'video' },
    { slug: 'video-blueprint-stress-test', state: 'local', group: 'video', kind: 'Video', title: 'The Blueprint and the Stress Test', summary: 'Foundation habits under pressure.', href: '../assets/media/tmc-husband/m01/video/the-blueprint-and-stress-test.mp4', mediaType: 'video' },
    { slug: 'audio-blind-spots-vineyard', state: 'local', group: 'audio', kind: 'Audio', title: 'Blind spots in the vineyard marriage course', summary: 'Where vineyard metaphors and habits misfire.', href: '../assets/media/tmc-husband/m01/audio/blind-spots-in-the-vineyard.mp3', mediaType: 'audio' },
    { slug: 'audio-why-course-fails', state: 'local', group: 'audio', kind: 'Audio', title: 'Why The Marriage Course fails some couples', summary: 'Limits and safety inversions.', href: '../assets/media/tmc-husband/m01/audio/why-the-marriage-course-fails-some-couples.mp3', mediaType: 'audio' },
    { slug: 'slides-marital-maintenance', state: 'local', group: 'slides', kind: 'PDF', title: 'Marital Maintenance Playbook', summary: 'Maintenance habits and seasons.', href: '../assets/media/tmc-husband/m01/slides/marital-maintenance-playbook.pdf', linkLabel: 'Open slide deck' },
    { slug: 'slides-tending-vineyard', state: 'local', group: 'slides', kind: 'PDF', title: 'Tending the Marital Vineyard', summary: 'The four vineyard tasks.', href: '../assets/media/tmc-husband/m01/slides/tending-the-marital-vineyard.pdf', linkLabel: 'Open slide deck' },
    { slug: 'infographic-connection-roadmap', state: 'local', group: 'infographics', title: 'Marriage Connection Roadmap', summary: 'Visual roadmap of connection habits.', href: '../assets/media/tmc-husband/m01/infographics/marriage-connection-roadmap.png', alt: 'Infographic titled Marriage Connection Roadmap with panels on protected time, emotional needs, and vineyard maintenance tasks.' },
    { slug: 'infographic-vineyard-field-guide', state: 'local', group: 'infographics', title: 'Marriage Vineyard Field Guide', summary: 'Single-page field guide on adjusting, pruning, supporting, and renewing.', href: '../assets/media/tmc-husband/m01/infographics/marriage-vineyard-field-guide.png', alt: 'Infographic titled Marriage Vineyard Field Guide illustrating four vineyard tasks for marital maintenance.' },
    { slug: 'report-building-foundations', state: 'local', group: 'reports', title: 'Building Strong Foundations', summary: 'Executive briefing on foundation habits.', href: '../assets/media/tmc-husband/m01/reports/episode-1-building-strong-foundations.pdf', linkLabel: 'Read the report' },
    { slug: 'report-we-to-me', state: 'local', group: 'reports', title: 'From We to Me: Navigating the Seasons of Connection', summary: 'Seasons-of-life framing.', href: '../assets/media/tmc-husband/m01/reports/from-we-to-me-seasons-of-connection.pdf', linkLabel: 'Read the report' },
    { slug: 'report-vineyard-secret', state: 'local', group: 'reports', title: 'The Vineyard Secret: Five Surprising Lessons', summary: 'Popular-article register — use as prompt, not proof.', href: '../assets/media/tmc-husband/m01/reports/vineyard-secret-five-lessons.pdf', linkLabel: 'Read the report' },
    { slug: 'post-mutual-submission', state: 'local', group: 'ministry', kind: 'Article', title: 'What the Care and Counsel Bible Gets Wrong About Mutual Submission', summary: 'Why Ephesians 5:21 does not teach symmetrical submission, and what the household code actually commands a husband.', href: 'https://usmcmin.org/blog/what-the-care-and-counsel-bible-gets-wrong-about-mutual-submission.html', linkLabel: 'Read the article' },
    { slug: 'quiz-marriage-quiz', state: 'local', group: 'quiz', title: 'Marriage Quiz', summary: 'Knowledge check over Module 1 material.', href: '../assets/media/tmc-husband/m01/quiz/marriage-quiz.html', linkLabel: 'Open the quiz' }
  ]
};

module.exports = { fieldManual };
