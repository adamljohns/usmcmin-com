'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one no-screen connection block',
  missionDurationMinutes: 60,
  opening: [
    'Marital intimacy is larger than sex. It includes friendship, safety, affection, delight, knowledge, privacy, and embodied closeness. Sexual intimacy matters, but it cannot be isolated from the rest of married life.',
    'Within the one-flesh covenant, sexual self-giving is mutual and never coerced. First Corinthians 7:3–5 speaks of mutual duty and temporary abstinence by shared agreement; not permission to force, threaten, punish, or demand what harms.',
    'This week, invite one no-screen connection block of at least thirty minutes. Offer two realistic options, make refusal safe, and state clearly that there is no expectation of sex or forced disclosure.'
  ],
  scripture: [
    { reference: '1 Corinthians 7:3–5', note: 'Paul teaches mutual sexual self-giving and shared agreement, not one-sided entitlement. Read alongside the whole biblical witness against force and harm; this passage must never justify coercion.' },
    { reference: 'Song of Songs 2:7; 8:6–7', note: 'The poetry honors love\'s covenantal fire and proper timing. Desire is powerful; it is not managed faithfully by pressure.' },
    { reference: '1 Corinthians 13:4–7', note: 'Patient, kind, non-self-seeking love provides the moral shape for marital intimacy alongside covenant mutuality.' },
    { reference: '1 Thessalonians 4:3–8', note: 'Holiness includes governing the body with honor rather than exploiting another person.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Protect unclaimed attention',
      tagline: 'Friendship requires presence, not performance.',
      actions: [
        'Schedule one no-screen connection block of at least thirty minutes.',
        'Offer two realistic options: walk, coffee, shared music, porch conversation, or quiet affection.',
        'State plainly that there is no expectation of sex or forced disclosure.',
        'Put devices away and protect the time you agreed on.'
      ]
    },
    {
      number: '2',
      title: 'Honor consent within covenant',
      actions: [
        'Accept that either spouse may decline any sexual or affectionate activity at any time.',
        'Offer kind words, practical partnership, and nonsexual touch as goods in themselves; not deposits toward access.',
        'Never criticize or compare your wife\'s body. Protect her privacy.',
        'After she states a boundary, keep ordinary warmth intact. Sulking and coldness punish a "no" without speaking a threat.'
      ]
    },
    {
      number: '3',
      title: 'Address structural pressure',
      actions: [
        'Ask about rest, pain, medication, privacy, unresolved hurt, body image, and caregiving load.',
        'Share household and caregiving responsibility as justice and love, not seduction strategy.',
        'Treat different desire patterns as shared information; not moral rank.',
        'Seek medical evaluation for pain; seek trauma-informed care where trauma is present.'
      ]
    },
    {
      number: '4',
      title: 'Guard fidelity and friendship',
      actions: [
        'Notice when secrecy, fantasy, messaging, pornography, or outside emotional disclosure draws energy from covenant truthfulness.',
        'Remember what makes your wife laugh, what drains her, and what she hopes for beyond household function.',
        'Speak about intimacy away from the bedroom and outside the immediate sting of rejection.',
        'Ask one question at a time and make opting out ordinary.'
      ]
    }
  ],
  selfCheck: [
    'Does my affection carry an unspoken expectation of sex or reassurance?',
    'How do my words, face, and behavior respond when my wife says no or not now?',
    'What structural pressure; workload, sleep, privacy, unresolved hurt; can I help address?',
    'Can my wife set a boundary without losing ordinary warmth from me afterward?'
  ],
  fieldAction: {
    title: 'Complete one pressure-free no-screen connection block',
    steps: [
      'Invite rather than announce, offering two realistic choices.',
      'Agree on at least thirty minutes and one mutually welcomed activity.',
      'State clearly that there is no expectation of sex or forced disclosure.',
      'Put devices away and ask one brief after-action question afterward.'
    ],
    finishLine: 'You shared at least thirty minutes of mutually chosen, no-screen connection while respecting every physical and conversational boundary.'
  },
  conversation: {
    intro: 'Ask away from the bedroom. Your wife may decline any question or stop at any point.',
    items: [
      'What kind of connection would feel welcome this week?',
      'What helps affection feel safe and free of hidden expectations?',
      'What pressure is affecting your capacity for friendship or intimacy?',
      'How can I respond better when your answer is no or not yet?'
    ]
  },
  caution: 'Do not use Scripture, marriage vows, headship, disappointment, money, affection, or course participation to demand sexual access or disclosure. Trauma, sexual pain, medical concerns, coercion, addiction, affairs, and major betrayal require specialized individual care; joint intimacy exercises may be unsafe or premature.',
  support: {
    lead: 'For ordinary differences, a licensed marriage therapist, physician, or mature pastoral counselor may help.',
    referrals: [
      { label: 'Sexual pain or medication effects', body: 'Consult a qualified medical professional.' },
      { label: 'Trauma, coercion, or compulsive sexual behavior', body: 'Seek specialized individual assessment and accountability before couple exercises.' },
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' }
    ],
    close: 'Consent is always voluntary, specific, ongoing, and reversible. Disappointment does not create entitlement.'
  },
  resources: {
    intro: "Optional study aids from your Notebook by Gemini notebook. Listen, watch, read, or drill \u2014 then return to your required action.",
    groups: [
      { key: "video", heading: "Watch", note: "Short video overviews." },
      { key: "audio", heading: "Listen", note: "Audio briefings for deeper reflection." },
      { key: "slides", heading: "Slide decks", note: "PDF study decks." },
      { key: "infographics", heading: "Study graphics", note: "Single-page visual summaries." },
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
    { slug: "video-keeping-the-spark-alive", state: "local", group: "video", kind: "Video", title: "Keeping the Spark Alive", summary: "Session video on friendship, attention, and desire over years.", href: "../assets/media/tmc-husband/m06/video/keeping-the-spark-alive.mp4", mediaType: "video" },
    { slug: "video-the-engine-of-intimacy", state: "local", group: "video", kind: "Video", title: "The Engine of Intimacy", summary: "Why emotional connection and physical intimacy feed each other.", href: "../assets/media/tmc-husband/m06/video/the-engine-of-intimacy.mp4", mediaType: "video" },
    { slug: "video-restoring-the-spark", state: "local", group: "video", kind: "Video", title: "Restoring the Spark", summary: "What to do when the connection has gone quiet.", href: "../assets/media/tmc-husband/m06/video/restoring-the-spark.mp4", mediaType: "video" },
    { slug: "video-the-7-day-intimacy-reset", state: "local", group: "video", kind: "Video", title: "The Seven-Day Intimacy Reset", summary: "A week of small, non-pressuring moves.", href: "../assets/media/tmc-husband/m06/video/the-7-day-intimacy-reset.mp4", mediaType: "video" },
    { slug: "audio-the-best-sex-starts-at-breakfast", state: "local", group: "audio", kind: "Audio", title: "It Starts Long Before the Bedroom", summary: "Deep-dive audio on intimacy as the whole day, not the last hour of it.", href: "../assets/media/tmc-husband/m06/audio/the-best-sex-starts-at-breakfast.mp3", mediaType: "audio" },
    { slug: "audio-why-responsive-desire-fuels-the-marital-spark", state: "local", group: "audio", kind: "Audio", title: "Responsive Desire", summary: "Deep-dive audio on desire that answers rather than initiates.", href: "../assets/media/tmc-husband/m06/audio/why-responsive-desire-fuels-the-marital-spark.mp3", mediaType: "audio" },
    { slug: "audio-modernizing-the-psychology-of-marital-intimacy", state: "local", group: "audio", kind: "Audio", title: "Modernising the Psychology of Intimacy", summary: "Critical audio on where the session dates. Read against the module caution.", href: "../assets/media/tmc-husband/m06/audio/modernizing-the-psychology-of-marital-intimacy.mp3", mediaType: "audio" },
    { slug: "slides-the-intimacy-blueprint", state: "local", group: "slides", kind: "PDF", title: "The Intimacy Blueprint", summary: "Session overview deck.", href: "../assets/media/tmc-husband/m06/slides/the-intimacy-blueprint.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-the-intimacy-blueprint-2", state: "local", group: "slides", kind: "PDF", title: "The Intimacy Blueprint (Part Two)", summary: "Second half of the blueprint deck.", href: "../assets/media/tmc-husband/m06/slides/the-intimacy-blueprint-2.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-relational-circuitry", state: "local", group: "slides", kind: "PDF", title: "Relational Circuitry", summary: "How connection, safety, and desire wire together.", href: "../assets/media/tmc-husband/m06/slides/relational-circuitry.pdf", linkLabel: "Open slide deck" },
    { slug: "infographic-the-spark-and-the-flame", state: "local", group: "infographics", title: "The Spark and the Flame", summary: "Friendship, attention, and desire over a long marriage.", href: "../assets/media/tmc-husband/m06/infographics/the-spark-and-the-flame.png", alt: "Illustrated field guide titled The Spark and the Flame: A Field Guide to Sexual Intimacy in Marriage, using a mower spark plug as its central image, with five secrets, a reality-check section on the young-children season, a red panel of warning signs including pornography and emotional adultery, and a three-step action checklist." },
    { slug: "infographic-keeping-the-spark-alive", state: "local", group: "infographics", title: "Keeping the Spark Alive", summary: "Habits that protect intimacy in an ordinary week.", href: "../assets/media/tmc-husband/m06/infographics/keeping-the-spark-alive.png", alt: "Illustrated field guide titled Keeping the Spark Alive: The Heart of Intimacy, with five points on emotional connection, guarding the bedroom as screen-free space, desire following a decision, kindness as the foundation of safety, and consent being voluntary and revocable." },
    { slug: "infographic-five-secrets-of-sexual-intimacy", state: "local", group: "infographics", title: "Five Secrets of Sexual Intimacy", summary: "Five practices, with a consent and safety panel.", href: "../assets/media/tmc-husband/m06/infographics/five-secrets-of-sexual-intimacy.png", alt: "Illustrated field guide titled Keeping the Spark Alive: The 5 Secrets of Sexual Intimacy, with five numbered points on speaking openly, protecting time and space, building anticipation, responding with trust, and other-centred kindness, closing with a note to seek help where there is fear, control, addiction, or abuse." },
    { slug: "report-briefing-document-the-marriage-course-episode-6-sexual-intimacy", state: "local", group: "reports", title: "Sexual Intimacy: Session Briefing", summary: "Executive briefing; best starting point for this module.", href: "../assets/media/tmc-husband/m06/reports/briefing-document-the-marriage-course-episode-6-sexual-intimacy.pdf", linkLabel: "Read the report" },
    { slug: "report-beyond-the-bedroom-reclaiming-the-spark-in-your-marriage", state: "local", group: "reports", title: "Beyond the Bedroom", summary: "Longer treatment of intimacy as friendship, safety, and attention.", href: "../assets/media/tmc-husband/m06/reports/beyond-the-bedroom-reclaiming-the-spark-in-your-marriage.pdf", linkLabel: "Read the report" },
    { slug: "report-good-luck-mr-gorsky-5-surprising-truths-about-keeping-the-spark-alive", state: "local", group: "reports", title: "Five Surprising Truths About Keeping the Spark Alive", summary: "Popular-article register; use as a prompt, not as proof.", href: "../assets/media/tmc-husband/m06/reports/good-luck-mr-gorsky-5-surprising-truths-about-keeping-the-spark-alive.pdf", linkLabel: "Read the report" },
    { slug: "quiz-marriage-quiz", state: "local", group: "quiz", title: "Marriage Quiz", summary: "Knowledge check over this module.", href: "../assets/media/tmc-husband/m06/quiz/marriage-quiz.html", linkLabel: "Open the quiz" },
    { slug: "flashcards-marriage-flashcards", state: "local", group: "flashcards", title: "Marriage Flashcards", summary: "Flashcard drill over this module.", href: "../assets/media/tmc-husband/m06/flashcards/marriage-flashcards.html", linkLabel: "Open the flashcards" }
  ]
};

module.exports = { fieldManual };
