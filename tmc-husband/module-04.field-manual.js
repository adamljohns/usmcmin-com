'use strict';

const fieldManual = {
  timeEstimate: '45–60 minutes, plus one repair action this week',
  missionDurationMinutes: 60,
  opening: [
    'Hurt in marriage is not healed by saying the word forgiveness faster. Repair begins with truth. A husband who has caused harm must face what he did, the effect it had, and what responsibility now requires.',
    'Forgiveness, reconciliation, and trust are related but not interchangeable. Forgiveness releases personal vengeance; reconciliation requires truth from both people; trust is a judgment about demonstrated reliability that may return gradually or not at all.',
    'This week, choose one specific wrong you can safely address. Prepare what you did, why it was wrong, the impact you understand, and one repair you will make — without demanding closure.'
  ],
  scripture: [
    { reference: 'Psalm 51:1–12', note: 'David names sin before God without bargaining. Grace grounds repentance; it does not remove temporal consequences or entitle restored trust.' },
    { reference: 'Luke 19:1–10', note: 'Zacchaeus responds to salvation with material restitution. Grace produces accountable action, not vague regret.' },
    { reference: 'Colossians 3:12–14', note: 'Compassion, patience, and forgiveness belong to Christian character. They must not be severed from truth, justice, or safety.' },
    { reference: 'Romans 12:17–21', note: 'Releasing vengeance belongs to God\'s people. Refusing personal revenge does not forbid reporting harm or pursuing safety.' }
  ],
  tasks: [
    {
      number: '1',
      title: 'Name the wrong specifically',
      tagline: 'Confession is agreement with reality — not self-hatred.',
      actions: [
        'Choose one specific behavior, not a global character flaw.',
        'Write what you did in active voice: "I disclosed private information" not "Things were shared."',
        'Name the likely impact without dictating how she must feel.',
        'Remove every "but," counter-accusation, and request for reassurance.'
      ]
    },
    {
      number: '2',
      title: 'Separate forgiveness, reconciliation, and trust',
      setup: 'Quoting forgiveness to avoid disclosure, treatment, or safety separation is spiritual language resisting accountability.',
      actions: [
        'Ask yourself: Am I seeking relief from guilt or willing to bear the cost of repair?',
        'Identify what restitution might look like for this specific harm.',
        'Accept that she does not owe immediate conversation, affection, or public unity.',
        'If the harm involves abuse, infidelity, addiction, or criminal conduct, seek qualified individual guidance before joint conversation.'
      ]
    },
    {
      number: '3',
      title: 'Repair small injuries promptly',
      tagline: 'Do not reserve repentance for dramatic failure.',
      actions: [
        'Notice minor harm: interrupting, dismissive humor, broken promises, phone use during vulnerable conversation.',
        'Make one clear confession followed by changed conduct.',
        'Avoid compulsive apology that asks your wife to manage your shame.',
        'If both spouses have harmed each other, own your conduct without turning confession into a trade.'
      ]
    },
    {
      number: '4',
      title: 'Choose accountability that fits the harm',
      actions: [
        'Identify whether a pastor, counselor, recovery group, financial professional, or legal authority is appropriate.',
        'Choose helpers who will not collude with secrecy or rush her response.',
        'Do not recruit friends to persuade her that you have changed.',
        'Track commitments with dates and actions — not vague claims of "working on it."'
      ]
    }
  ],
  selfCheck: [
    'Do my apologies name my action, or mainly explain my intentions?',
    'What consequence, disclosure, or restitution have I been trying to avoid?',
    'Have I confused forgiveness with reconciliation or restored trust?',
    'Do I pressure my wife to comfort me when I should be listening to harm?'
  ],
  fieldAction: {
    title: 'Make one specific confession or repair attempt',
    steps: [
      'Choose a specific behavior rather than a global flaw.',
      'Name the wrong and its impact without "but."',
      'Offer one concrete repair or accountability step.',
      'Allow time and boundaries without demanding forgiveness or closure.'
    ],
    finishLine: 'You made a safe, specific repair attempt and completed or scheduled the concrete action you offered, without requiring a particular response.'
  },
  conversation: {
    intro: 'Invite; do not assign. Your wife may decline any question or the entire conversation.',
    items: [
      'Is there a manageable hurt from me that you want me to hear without defending?',
      'What impact of my action have I failed to understand?',
      'What repair would be meaningful, if any?',
      'What boundary or time do you need me to respect now?'
    ]
  },
  caution: 'Do not use Scripture, headship, forgiveness, prayer, money, children, or course completion to demand silence, access, affection, reconciliation, or restored trust. Where abuse, coercion, retaliation, active addiction, serious betrayal, or fear is present, joint repair exercises may increase danger. Seek confidential individual help first.',
  support: {
    lead: 'This course is formation for a basically safe marriage. It is not crisis care, clinical treatment, or a substitute for qualified pastoral counsel.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.' },
      { label: 'Abuse or coercive control', body: 'Seek confidential individual safety planning first. Joint exercises are not automatically appropriate when control or fear is present.' },
      { label: 'Mental-health crisis', body: 'In the U.S., call or text 988.', href: 'https://988lifeline.org/', linkLabel: '988lifeline.org' },
      { label: 'Betrayal, addiction, or financial exploitation', body: 'Use a qualified specialist and the proper legal or clinical authority.' }
    ],
    close: 'A husband must never use Scripture, forgiveness, headship, money, children, or course completion to demand access, silence concern, or prevent help.'
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
    { slug: "video-healing-hurt-and-forgiveness", state: "local", group: "video", kind: "Video", title: "Healing Hurt and Forgiveness", summary: "Session video on naming a hurt and making a specific repair.", href: "../assets/media/tmc-husband/m04/video/healing-hurt-and-forgiveness.mp4", mediaType: "video" },
    { slug: "video-navigating-marital-conflict", state: "local", group: "video", kind: "Video", title: "Navigating Marital Conflict", summary: "Where unresolved anger goes when nobody addresses it.", href: "../assets/media/tmc-husband/m04/video/navigating-marital-conflict.mp4", mediaType: "video" },
    { slug: "audio-the-danger-of-forgiving-rhinos-and-hedgehogs", state: "local", group: "audio", kind: "Audio", title: "The Danger of Forgiving: Rhinos and Hedgehogs", summary: "Deep-dive audio on the two anger styles and where the model stops applying.", href: "../assets/media/tmc-husband/m04/audio/the-danger-of-forgiving-rhinos-and-hedgehogs.mp3", mediaType: "audio" },
    { slug: "audio-when-marriage-advice-becomes-ammunition", state: "local", group: "audio", kind: "Audio", title: "When Marriage Advice Becomes Ammunition", summary: "Safety inversion: how repair language gets weaponised. Read against the module caution.", href: "../assets/media/tmc-husband/m04/audio/when-marriage-advice-becomes-ammunition.mp3", mediaType: "audio" },
    { slug: "slides-marital-repair-blueprint", state: "local", group: "slides", kind: "PDF", title: "Marital Repair Blueprint", summary: "The three-step repair, start to finish.", href: "../assets/media/tmc-husband/m04/slides/marital-repair-blueprint.pdf", linkLabel: "Open slide deck" },
    { slug: "slides-the-topography-of-repair", state: "local", group: "slides", kind: "PDF", title: "The Topography of Repair", summary: "Mapping how deep a given hurt actually runs.", href: "../assets/media/tmc-husband/m04/slides/the-topography-of-repair.pdf", linkLabel: "Open slide deck" },
    { slug: "infographic-marriage-healing-and-forgiveness-guide", state: "local", group: "infographics", title: "The Path to Healing", summary: "Anger as signal, the three-step repair, and a red-flag panel on when to seek help.", href: "../assets/media/tmc-husband/m04/infographics/marriage-healing-and-forgiveness-guide.png", alt: "Illustrated field guide titled The Path to Healing: Navigating Hurt and Forgiveness in Marriage, with panels on anger as an alarm, the rhino and hedgehog styles, a three-step repair, a safety filter, and a seven-day plan." },
    { slug: "infographic-marriage-conflict-and-forgiveness-guide", state: "local", group: "infographics", title: "Marriage Conflict and Forgiveness Guide", summary: "Companion guide on repair sequence and boundaries.", href: "../assets/media/tmc-husband/m04/infographics/marriage-conflict-and-forgiveness-guide.png", alt: "Illustrated field guide titled Healing the Heart: A Married Couple's Field Guide to Conflict and Forgiveness, with sections on rhino and hedgehog conflict styles, a downward spiral shown as a clogged drain, a three-part healing process, and an action checklist." },
    { slug: "report-episode-4-the-marriage-course-healing-hurt-and-anger", state: "local", group: "reports", title: "Healing Hurt and Anger", summary: "Executive briefing — best starting point for this module.", href: "../assets/media/tmc-husband/m04/reports/episode-4-the-marriage-course-healing-hurt-and-anger.pdf", linkLabel: "Read the report" },
    { slug: "report-beyond-the-apple-throw-navigating-anger-and-healing-in-marriage", state: "local", group: "reports", title: "Beyond the Apple Throw", summary: "Longer treatment of anger, repair, and what forgiveness does not mean.", href: "../assets/media/tmc-husband/m04/reports/beyond-the-apple-throw-navigating-anger-and-healing-in-marriage.pdf", linkLabel: "Read the report" },
    { slug: "report-rhinos-hedgehogs-and-the-buried-alive-rule-5-surprising-lessons-for-a-healthier-marriage", state: "local", group: "reports", title: "Rhinos, Hedgehogs, and the Buried-Alive Rule", summary: "Popular-article register — use as a prompt, not as proof.", href: "../assets/media/tmc-husband/m04/reports/rhinos-hedgehogs-and-the-buried-alive-rule-5-surprising-lessons-for-a-healthier-marriage.pdf", linkLabel: "Read the report" },
    { slug: "quiz-marriage-quiz", state: "local", group: "quiz", title: "Marriage Quiz", summary: "Knowledge check over this module.", href: "../assets/media/tmc-husband/m04/quiz/marriage-quiz.html", linkLabel: "Open the quiz" },
    { slug: "flashcards-marriage-flashcards", state: "local", group: "flashcards", title: "Marriage Flashcards", summary: "Flashcard drill over this module.", href: "../assets/media/tmc-husband/m04/flashcards/marriage-flashcards.html", linkLabel: "Open the flashcards" }
  ]
};

module.exports = { fieldManual };
