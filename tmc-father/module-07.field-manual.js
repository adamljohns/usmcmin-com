'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one seven-day practice',
  missionDurationMinutes: 60,
  opening: [
    'Love becomes credible through conduct. A husband may feel deep affection and still communicate neglect through inattention, unreliable promises, harsh speech, or leaving the mental load to his wife.',
    'Popular "love language" categories — words, time, gifts, service, and touch — can help you notice that care sent in one form may not be recognized in another. They are prompts, not diagnoses, contracts, or bargaining chips.',
    'This week, choose one small act your wife can recognize as care and repeat it for seven days. Ask what would help rather than announcing you know her category.'
  ],
  scripture: [
    { reference: '1 John 3:16–18', note: 'Christian love moves beyond speech into truthful action. Action must remain governed by truth — not manipulation.' },
    { reference: 'John 13:1–17', note: 'Jesus joins authority with humble service. His example confronts entitlement rather than assigning a wife to manage her husband\'s growth.' },
    { reference: 'Galatians 5:13–14, 22–23', note: 'Service through love and the Spirit\'s fruit include patience, kindness, faithfulness, gentleness, and self-control.' },
    { reference: 'Philippians 2:3–4', note: 'Looking to another\'s interests confronts selfish ambition without erasing truthful limits or personal responsibility.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Ask what would actually help',
      actions: [
        'Ask: "What one small action from me would make this week lighter or warmer?"',
        'Do not assign her a category or assume you already know the answer.',
        'Choose something specific and sustainable: "Prepare lunches before bed" not "be more loving."',
        'Ensure the action fits a real need and does not create more work for your wife.'
      ]
    },
    {
      number: '2',
      title: 'Repeat without keeping score',
      actions: [
        'Complete the chosen action for seven days without asking for repayment or daily praise.',
        'If resentment rises because she did not notice, examine the hidden contract.',
        'You may tell her you are building a faithful habit — do not require daily evaluation.',
        'Continue because the action is good, while remaining open to correction if it is not helpful.'
      ]
    },
    {
      number: '3',
      title: 'Own invisible responsibility',
      actions: [
        'Notice supplies before they run out, appointments before reminders arrive, and maintenance before crisis.',
        'Owning work means planning and completing it — not asking her to supervise every step.',
        'Ask what ownership would help, agree on the standard, then carry the mental as well as physical part.',
        'If you miss a day, repair the rhythm without drama or public streak-keeping.'
      ]
    },
    {
      number: '4',
      title: 'Review and receive feedback',
      actions: [
        'After day seven, review privately: Was the action generous or transactional?',
        'Ask one optional question: "Was this helpful, and should I continue, change, or stop?"',
        'Receive the answer without lobbying for your preferred gesture.',
        'Choose one course practice to continue for the next month.'
      ]
    }
  ],
  selfCheck: [
    'Which acts of care do I prefer because they cost me least?',
    'Have I asked what would help, or assigned my wife a category?',
    'Where does my service carry a hidden expectation of praise, sex, or repayment?',
    'Which one course practice should become a monthly rhythm?'
  ],
  fieldAction: {
    title: 'Repeat one recognizable act of love for seven days',
    steps: [
      'Ask what one observable action would genuinely help.',
      'Define it small enough to repeat for seven days.',
      'Complete it without asking for repayment or daily praise.',
      'After day seven, invite a continue/change/stop answer.'
    ],
    finishLine: 'You completed the chosen action on seven days, repaired any miss honestly, and received optional feedback without arguing for your preferred gesture.'
  },
  conversation: {
    intro: 'Your wife may decline to choose an action or give feedback. The practice remains your formation work, not her assignment.',
    items: [
      'What one small action from me would make this week lighter or warmer?',
      'Is there a form of care I offer that does not currently feel helpful?',
      'Should I continue, change, or stop this seven-day practice?',
      'Which course rhythm would you welcome for the next month?'
    ]
  },
  caution: 'Do not use a label, gift, chore, date, compliment, or touch as a bargaining chip for praise, sex, obedience, or repayment. No act of service cancels abuse, deception, addiction, injustice, or the need for accountability. A week of helpful conduct does not erase a pattern of harm or obligate restored trust.',
  support: {
    lead: 'This practice serves a basically safe marriage; it is not proof of repentance or a substitute for treatment.',
    referrals: [
      { label: 'Abuse, coercion, or active addiction', body: 'Require qualified individual help and accountable change before treating couple exercises as sufficient.' },
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' },
      { label: 'Mental-health crisis', body: 'In the U.S., call or text 988.', href: 'https://988lifeline.org/', linkLabel: '988lifeline.org' }
    ],
    close: 'Course completion is not marriage completion. Seven browser flags are not a spiritual score or evidence that a marriage is safe.'
  },
  resources: {
    intro: "Optional study aids from your Notebook by Gemini notebook. Listen, watch, read, or drill \u2014 then return to your field action.",
    groups: [
      { key: "video", heading: "Watch", note: "Short video overviews." },
      { key: "audio", heading: "Listen", note: "Audio briefings for deeper reflection." },
      { key: "slides", heading: "Slide decks", note: "PDF study decks." },
      { key: "infographics", heading: "Field graphics", note: "Single-page visual summaries." },
      { key: "reports", heading: "Read", note: "Study reports as clean, printable PDFs." }
    ],
    withheldNotice: null,

    journal: {
      "heading": "Optional companion journal",
      "label": "The Marriage Course Study Journal",
      "href": "https://www.amazon.com/dp/0310116694?tag=usmcministrie-20",
      "body": "Optional written exercises. This module works without it.",
      "disclosure": "Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you."
    }
  },
  artifacts: [
    { slug: "video-love-in-action", state: "local", group: "video", kind: "Video", title: "Love in Action", summary: "Session video on love as something you do on purpose.", href: "../assets/media/tmc-father/m07/video/love-in-action.mp4", mediaType: "video" },
    { slug: "video-5-languages-of-marriage", state: "local", group: "video", kind: "Video", title: "The Five Languages of Marriage", summary: "Giving love in the currency your wife actually receives.", href: "../assets/media/tmc-father/m07/video/5-languages-of-marriage.mp4", mediaType: "video" },
    { slug: "audio-giving-love-in-your-partner-s-currency", state: "local", group: "audio", kind: "Audio", title: "Giving Love in Her Currency", summary: "Deep-dive audio on paying attention to what actually lands.", href: "../assets/media/tmc-father/m07/audio/giving-love-in-your-partner-s-currency.mp3", mediaType: "audio" },
    { slug: "audio-why-love-languages-need-emotional-safety", state: "local", group: "audio", kind: "Audio", title: "Why Love Languages Need Safety First", summary: "Critical audio: the framework assumes a safe marriage. Read against the module caution.", href: "../assets/media/tmc-father/m07/audio/why-love-languages-need-emotional-safety.mp3", mediaType: "audio" },
    { slug: "slides-the-love-language-manual", state: "local", group: "slides", kind: "PDF", title: "The Love Language Manual", summary: "The five languages, applied.", href: "../assets/media/tmc-father/m07/slides/the-love-language-manual.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-marriage-field-manual", state: "local", group: "slides", kind: "PDF", title: "Marriage Field Manual", summary: "Session overview deck.", href: "../assets/media/tmc-father/m07/slides/marriage-field-manual.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-marriage-systems-manual", state: "local", group: "slides", kind: "PDF", title: "Marriage Systems Manual", summary: "Keeping the habits running after the course ends.", href: "../assets/media/tmc-father/m07/slides/marriage-systems-manual.pdf", linkLabel: "Open slide deck" },
    { slug: "infographic-love-in-action-relationship-guide", state: "local", group: "infographics", title: "Love in Action Relationship Guide", summary: "The five languages with a practice plan.", href: "../assets/media/tmc-father/m07/infographics/love-in-action-relationship-guide.png", alt: "Illustrated field guide titled Love in Action: Speaking Your Spouse's Language, covering the felt-benefit rule, the gap between intent and reception, five ways to communicate care, treating love like a foreign language, maintaining the relationship engine, and the six-second kiss rule." },
    { slug: "infographic-marriage-maintenance-storyboard-field-guide", state: "local", group: "infographics", title: "Marriage Maintenance Storyboard", summary: "The whole course as one maintenance rhythm.", href: "../assets/media/tmc-father/m07/infographics/marriage-maintenance-storyboard-field-guide.png", alt: "Illustrated storyboard field guide on marriage maintenance, running from the resentment trap of loving in the wrong language, through a learning-process toolkit of five ways to show love, to fluent connection, with a red safety panel and a four-step action checklist." },
    { slug: "report-love-in-action-insights-from-the-marriage-course-episode-7", state: "local", group: "reports", title: "Love in Action: Session Insights", summary: "Executive briefing — best starting point for this module.", href: "../assets/media/tmc-father/m07/reports/love-in-action-insights-from-the-marriage-course-episode-7.pdf", linkLabel: "Read the report" },
    { slug: "report-the-architecture-of-intimacy-why-lasting-love-is-a-learned-language-not-a-reflex", state: "local", group: "reports", title: "The Architecture of Intimacy", summary: "Longer treatment of love as a learned practice rather than a reflex.", href: "../assets/media/tmc-father/m07/reports/the-architecture-of-intimacy-why-lasting-love-is-a-learned-language-not-a-reflex.pdf", linkLabel: "Read the report" },
    { slug: "report-love-in-action-beyond-the-spontaneous-myth-and-into-the-five-languages", state: "local", group: "reports", title: "Beyond the Spontaneous Myth", summary: "Popular-article register — use as a prompt, not as proof.", href: "../assets/media/tmc-father/m07/reports/love-in-action-beyond-the-spontaneous-myth-and-into-the-five-languages.pdf", linkLabel: "Read the report" },
    { slug: "quiz-marriage-quiz", state: "local", group: "quiz", title: "Marriage Quiz", summary: "Knowledge check over this module.", href: "../assets/media/tmc-father/m07/quiz/marriage-quiz.html", linkLabel: "Open the quiz" },
    { slug: "flashcards-marriage-flashcards", state: "local", group: "flashcards", title: "Marriage Flashcards", summary: "Flashcard drill over this module.", href: "../assets/media/tmc-father/m07/flashcards/marriage-flashcards.html", linkLabel: "Open the flashcards" }
  ]
};

module.exports = { fieldManual };
