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
    intro: 'Scripture and lawful outbound links only for this module.',
    groups: [],
    notebook: null,
    journal: null
  },
  artifacts: []
};

module.exports = { fieldManual };
