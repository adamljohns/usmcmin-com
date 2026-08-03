'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one replacement practice this week',
  missionDurationMinutes: 60,
  opening: [
    'Every husband enters marriage with a working model of family, even if he has never described it. Childhood taught him what conflict sounds like, who handles money, whether affection is spoken, and what happens when someone fails.',
    'Family of origin is influence, not destiny. The point is neither to blame parents for every choice nor to romanticize endurance. It is to bring inherited assumptions into the light so they can be tested instead of obeyed automatically.',
    'This week, identify one pattern to retain and one to replace. Write each as behavior, not a label. Tell your wife only your own findings — she may decline to participate.'
  ],
  scripture: [
    { reference: 'Genesis 2:24', note: 'Marriage forms a new primary household allegiance. Leaving and holding fast do not require contempt for parents; honoring parents does not require unsafe access.' },
    { reference: 'Ezekiel 18:19–23', note: 'The chapter rejects fatalism about inherited guilt and calls each person to present repentance. Generations influence one another, but a father\'s sin does not seal a son\'s destiny.' },
    { reference: '2 Corinthians 5:17', note: 'New creation in Christ grounds hope for changed patterns without pretending learned habits disappear without repentance and practice.' },
    { reference: 'Romans 12:2', note: 'Renewed thinking resists unconscious conformity. A family pattern should be tested by truth and faithful fruit, not defended because it is familiar.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Observe your family-of-origin patterns',
      actions: [
        'Describe who made decisions in your home growing up, and how.',
        'Note whether apologies were common, rare, or demanded only from children.',
        'Ask what rule about men, emotion, money, conflict, or loyalty your childhood taught.',
        'Describe patterns and effects — do not put relatives on trial.'
      ]
    },
    {
      number: '2',
      title: 'Notice present triggers',
      tagline: 'Making sense of a reaction is not the same as being right for this marriage.',
      actions: [
        'Identify one ordinary marital moment that produces a reaction larger than the event.',
        'Ask: "What old rule does this moment activate?"',
        'Create a small gap between sensation and action before you respond.',
        'Do not weaponize background: "You are acting just like your mother" rarely creates understanding.'
      ]
    },
    {
      number: '3',
      title: 'Retain one gift intentionally',
      actions: [
        'Name one inherited strength that actually serves your marriage now.',
        'Ask your wife whether she experiences it as a gift — she may see it differently.',
        'Even virtues can distort: loyalty can become secrecy, thrift can become control.',
        'Retaining a pattern intentionally is different from repeating it unconsciously.'
      ]
    },
    {
      number: '4',
      title: 'Replace one harmful pattern',
      actions: [
        'Choose one specific behavior, not your entire family system.',
        'Identify the cue that usually activates the old pattern.',
        'Write one replacement response that can be observed: "I need twenty minutes and will return at 7:40."',
        'Practice the replacement once when the cue appears, or rehearse it calmly if it does not.'
      ],
      callout: {
        label: 'Trauma and abuse histories',
        body: 'Do not demand disclosure, contact with relatives, or reconciliation. Past harm may explain present protection, but it never excuses current coercion or violence. Qualified trauma-informed care may be essential.'
      }
    }
  ],
  selfCheck: [
    'Which ordinary marital moment produces a reaction in me that seems larger than the event?',
    'What rule about men, emotion, money, conflict, or loyalty did my childhood teach?',
    'Which inherited strength does my wife actually experience as a gift?',
    'What family comparison have I used unfairly against her?'
  ],
  fieldAction: {
    title: 'Retain one pattern and replace one pattern',
    steps: [
      'Describe one inherited behavior that serves your marriage.',
      'Describe one inherited behavior that no longer serves it.',
      'Choose a cue and a specific replacement response.',
      'Practice or rehearse the replacement once without diagnosing your wife.'
    ],
    finishLine: 'You named one pattern to retain, one to replace, and carried out or rehearsed the replacement without assigning homework to your wife.'
  },
  conversation: {
    intro: 'Share your own findings first. Your wife may decline, correct your interpretation, or stop the conversation.',
    items: [
      'Would you be willing to tell me how one pattern from my family affects our home?',
      'Which strength from my background do you experience as a gift?',
      'When my old pattern appears, what response from me would feel different?',
      'Is there a family topic or boundary you do not want this exercise to cross?'
    ]
  },
  caution: 'Do not blame every present choice on your parents, diagnose relatives, force your wife to disclose trauma, or use "honor your father and mother" to demand unsafe contact. Cultural difference is not automatically dysfunction. Past influence may explain a reaction; it never excuses current abuse, coercion, or violence.',
  support: {
    lead: 'Ordinary family-pattern work may benefit from mature pastoral counsel or a licensed marriage and family therapist.',
    referrals: [
      { label: 'Trauma or abuse history', body: 'Requires individual, trauma-informed help and careful safety planning — not couple processing of traumatic history in this course.' },
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' },
      { label: 'Mental-health crisis', body: 'In the U.S., call or text 988.', href: 'https://988lifeline.org/', linkLabel: '988lifeline.org' }
    ],
    close: 'This course does not require disclosure, renewed family contact, or couple processing of traumatic history.'
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
    notebook: {
      "title": "Your Notebook by Gemini notebook",
      "body": "Google account required. This is the source for the study aids on this page.",
      "label": "Open \"TMC (pt5): The Impact of Family\" in Notebook by Gemini",
      "href": "https://notebooklm.google.com/notebook/e6e7bc4f-8dd9-407e-9b70-894acafe3fa4"
    },
    journal: {
      "heading": "Optional companion journal",
      "label": "The Marriage Course Study Journal",
      "href": "https://www.amazon.com/dp/0310116694?tag=usmcministrie-20",
      "body": "Optional written exercises. This module works without it.",
      "disclosure": "Affiliate disclosure: Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you."
    }
  },
  artifacts: [
    { slug: "video-family-impact-past-and-present", state: "local", group: "video", kind: "Video", title: "The Impact of Family: Past and Present", summary: "Session video on the family you brought into the marriage.", href: "../assets/media/tmc-husband/m05/video/family-impact-past-and-present.mp4", mediaType: "video" },
    { slug: "video-family-dynamics-in-marriage", state: "local", group: "video", kind: "Video", title: "Family Dynamics in Marriage", summary: "How inherited patterns show up in a marriage nobody planned them for.", href: "../assets/media/tmc-husband/m05/video/family-dynamics-in-marriage.mp4", mediaType: "video" },
    { slug: "audio-trauma-informed-forgiveness-and-cultural-marriage-boundaries", state: "local", group: "audio", kind: "Audio", title: "Trauma-Informed Forgiveness and Boundaries", summary: "Deep-dive audio on forgiveness that does not require unsafe contact.", href: "../assets/media/tmc-husband/m05/audio/trauma-informed-forgiveness-and-cultural-marriage-boundaries.mp3", mediaType: "audio" },
    { slug: "audio-why-ai-flagged-the-marriage-course-trauma", state: "local", group: "audio", kind: "Audio", title: "Where This Session Needs Care", summary: "Critical audio on the limits of a formation course around trauma. Read against the module caution.", href: "../assets/media/tmc-husband/m05/audio/why-ai-flagged-the-marriage-course-trauma.mp3", mediaType: "audio" },
    { slug: "slides-navigating-family-legacies", state: "local", group: "slides", kind: "PDF", title: "Navigating Family Legacies", summary: "Leaving, cleaving, and the new centre of gravity.", href: "../assets/media/tmc-husband/m05/slides/navigating-family-legacies.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-the-marital-blueprint", state: "local", group: "slides", kind: "PDF", title: "The Marital Blueprint", summary: "Session overview deck.", href: "../assets/media/tmc-husband/m05/slides/the-marital-blueprint.pdf", linkLabel: "Open slide deck" },
    { slug: "infographic-navigating-the-family-tree-guide", state: "local", group: "infographics", title: "Navigating the Family Tree", summary: "Leaving as an emotional shift, inherited conflict styles, and a critical panel on when advice is not enough.", href: "../assets/media/tmc-husband/m05/infographics/navigating-the-family-tree-guide.png", alt: "Illustrated field guide titled Navigating the Family Tree: A Field Guide for Married Couples, with panels on creating a new centre of gravity, inherited conflict styles, evaluating your roots, a healing action plan, and a red-flag note to seek professional help." },
    { slug: "infographic-navigating-family-patterns-in-marriage", state: "local", group: "infographics", title: "Navigating Family Patterns in Marriage", summary: "Companion guide on inherited patterns and boundaries.", href: "../assets/media/tmc-husband/m05/infographics/navigating-family-patterns-in-marriage.png", alt: "Illustrated multi-panel field guide titled Navigating Family Patterns in Marriage." },
    { slug: "report-episode-5-the-marriage-course-the-impact-of-family-past-and-present", state: "local", group: "reports", title: "The Impact of Family: Past and Present", summary: "Executive briefing — best starting point for this module.", href: "../assets/media/tmc-husband/m05/reports/episode-5-the-marriage-course-the-impact-of-family-past-and-present.pdf", linkLabel: "Read the report" },
    { slug: "report-the-ghost-at-the-dinner-table-navigating-family-baggage-and-in-law-dynamics", state: "local", group: "reports", title: "The Ghost at the Dinner Table", summary: "Longer treatment of in-law dynamics and inherited expectations.", href: "../assets/media/tmc-husband/m05/reports/the-ghost-at-the-dinner-table-navigating-family-baggage-and-in-law-dynamics.pdf", linkLabel: "Read the report" },
    { slug: "report-why-your-in-laws-are-secretly-living-in-your-marriage-5-radical-shifts-for-every-couple", state: "local", group: "reports", title: "Why Your In-Laws Are Living in Your Marriage", summary: "Popular-article register — the headline overclaims; use as a prompt.", href: "../assets/media/tmc-husband/m05/reports/why-your-in-laws-are-secretly-living-in-your-marriage-5-radical-shifts-for-every-couple.pdf", linkLabel: "Read the report" },
    { slug: "quiz-marriage-quiz", state: "local", group: "quiz", title: "Marriage Quiz", summary: "Knowledge check over this module.", href: "../assets/media/tmc-husband/m05/quiz/marriage-quiz.html", linkLabel: "Open the quiz" },
    { slug: "flashcards-marriage-flashcards", state: "local", group: "flashcards", title: "Marriage Flashcards", summary: "Flashcard drill over this module.", href: "../assets/media/tmc-husband/m05/flashcards/marriage-flashcards.html", linkLabel: "Open the flashcards" }
  ]
};

module.exports = { fieldManual };
