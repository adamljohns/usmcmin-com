'use strict';

// Module 3 field-manual content.
//
// Reconciled from the Episode 3 research package: 5 verified sources and
// 17 completed artifacts. Prose here is original U.S.M.C. Ministries writing.
// The transcript is cited by timestamp and paraphrase only; it is never
// republished. Every claim attributed to the source is marked as source
// teaching, and every judgement is marked as ministry analysis.
//
// This object is the canonical Module 3 content. tmc-husband/generate.js
// renders it; regenerating the course reproduces the page exactly, so a
// future generator run cannot silently erase it.

const fieldManual = {
  classification: 'Formation brief · approximately 60–75 minutes plus one week of fieldwork',
  objective: 'Move from fighting your wife to fighting the problem beside her',
  sourceBase: 'The Marriage Course, Episode 3',
  reviewStatus: 'Local prototype',

  sectionNav: [
    { href: '#mission-brief', label: 'Brief' },
    { href: '#scripture-frame', label: 'Scripture' },
    { href: '#core-framework', label: 'Framework' },
    { href: '#fair-insight', label: 'Fair' },
    { href: '#caution-boundary', label: 'Caution' },
    { href: '#self-check', label: 'Check' },
    { href: '#pause-protocol', label: 'Pause' },
    { href: '#five-steps', label: 'Five steps' },
    { href: '#field-action', label: 'Exercise' },
    { href: '#discussion-prompts', label: 'Prompts' },
    { href: '#support-boundary', label: 'Safety' },
    { href: '#resources', label: 'Resources' },
    { href: '#completion', label: 'Finish' }
  ],

  inventory: {
    heading: 'Source and artifact reconciliation',
    summary: 'This module reconciles 5 verified sources and 17 completed artifacts from the Episode 3 research package. Eleven review-safe artifacts are stored locally with this prototype. Six heavy media artifacts stay in the local research package and are named here without being published.',
    counts: [
      { value: '5', label: 'sources', detail: 'Episode 3 transcript plus four independent model reviews' },
      { value: '17', label: 'artifacts', detail: '3 audio · 3 video · 3 decks · 3 graphics · 3 reports · 1 quiz · 1 flashcard set' },
      { value: '11', label: 'stored locally', detail: 'Decks, graphics, reports, quiz, and flashcards copied into this prototype' },
      { value: '6', label: 'withheld', detail: 'Audio and video held in the research package pending rights and approval' }
    ]
  },

  sources: [
    {
      slug: 'episode-3-transcript',
      lane: 'Primary source',
      title: 'Episode 3 transcript, The Marriage Course',
      note: 'A partial transcript of a 1:44:01 session. Dialogue is missing across roughly 00:10–00:19, 00:30–00:39, and 01:00–01:28. Everything on this page is provisional to that extent, and no conclusion here should be presented as covering the whole episode.'
    },
    {
      slug: 'chatgpt-review',
      lane: 'Chaplain and counsellor lens',
      title: 'ChatGPT independent review',
      note: 'Strongest on facilitator safeguards. It supplies the distinction this module builds on: a preference, a skill gap, a broken agreement, and abusive conduct are four different problems and must not be treated as one.'
    },
    {
      slug: 'claude-review',
      lane: 'Systems-analyst lens',
      title: 'Claude independent review',
      note: 'Strongest on the design of the tools. It names the pause rule as a circuit breaker that works because either spouse can call it unilaterally, and it identifies unreciprocated service as a structural warning sign rather than a virtue.'
    },
    {
      slug: 'gemini-review',
      lane: 'Brotherly friend lens',
      title: 'Gemini independent review',
      note: 'Written under a 1,300-word ceiling. Reconciliation note: it describes a speaker–listener tool and a four-pattern taxonomy of escalation, invalidation, negative interpretation, and withdrawal that do not appear in the supplied transcript. Those are treated here as reviewer framing, not as Episode 3 content.'
    },
    {
      slug: 'grok-review',
      lane: 'Grandfatherly theologian lens',
      title: 'Grok independent review',
      note: 'Strongest on where a practical session stops short of a theology of conflict. Reconciliation note: it gives the presenters a surname the transcript never states, so that attribution is carried here as unverified.'
    }
  ],

  missionBrief: {
    heading: 'Conflict is a task, not a verdict',
    teaching: {
      heading: 'What the session actually teaches',
      paragraphs: [
        'Episode 3 runs one hour and forty-four minutes and is presented by a married couple identified in the transcript only as Nicky and Sila. It opens by normalising disagreement. Spouses arrive with different backgrounds, desires, priorities, and personalities, and each of us is selfish to some degree, so conflict is inevitable. It is not evidence that the wrong person was chosen. Burying a difference is treated as worse than discussing it.',
        'From there the session teaches four principles for resolving conflict — remember your partner’s positive qualities, recognise that differences are good, look for an “us” solution, and support your partner — alongside a timing rule that lets either spouse postpone a late-night argument and a five-step procedure for reaching a workable decision. A rowing illustration carries the argument: two people pulling against each other lurch and stall; two people matching strokes glide.'
      ],
      map: 'Teaching map: 00:01:25–00:03:41 · 00:04:44–00:09:29 · 00:20:00–00:29:43 · 00:40:27–00:51:43 · 01:29:02–01:35:05'
    },
    analysis: {
      heading: 'The husband’s assignment',
      paragraphs: [
        'Your assignment is not to grade your wife’s conflict style. It is to identify the move you make when pressure rises, say it out loud without diagnosing her, and change it. All four independent reviews converge on the same limit: these tools work between two people who are safe, free to disagree, and willing to change. They do not work on a problem that is not a disagreement.',
        'So this module keeps two jobs separate. Where the marriage is ordinary and basically safe, learn the protocol and run it. Where the pattern involves fear, control, or harm, stop running couple exercises and get individual help. Sorting which one you are in is the first act of leadership, and it is a judgement you make honestly rather than the one that protects your self-image.'
      ]
    },
    endState: 'You can name your own conflict move in concrete behaviour, hold a pause that includes a real return, and run one disagreement through five steps to a reviewable decision.'
  },

  scripture: {
    heading: 'Responsibility with a stated limit',
    quote: {
      text: 'If possible, so far as it depends on you, live peaceably with all.',
      cite: 'Romans 12:18 (ESV)'
    },
    intro: 'Read each passage in its wider context before applying it. The caveat under each one is ministry analysis, not the text.',
    entries: [
      {
        reference: 'Romans 12:18',
        teaching: 'Paul places genuine responsibility on the believer to pursue peace, and this module treats that as binding on a husband’s conduct in every disagreement.',
        caveat: 'The verse builds in two limits — “if possible” and “so far as it depends on you.” Peace is not always available, and it is never wholly in one person’s power. This text does not require a husband to purchase quiet by concealing wrong, and it does not make a wife responsible for a peace her husband refuses.'
      },
      {
        reference: 'Matthew 7:3–5',
        teaching: 'Episode 3 uses the speck and the plank near 00:53:30 to argue that self-examination comes before correction, and concludes that the only person you can change is yourself.',
        caveat: 'Jesus addresses hypocritical judgement inside the community of disciples. He tells the man to remove his own plank so that he can see clearly to help — not to fall silent. The passage does not mean a harmed spouse must locate an equal fault of her own before naming serious wrong, and it is not a rule that the person being harmed carries the change.'
      },
      {
        reference: 'Ephesians 4:26–27, 31–32',
        teaching: 'The session’s counsel to apologise before sleeping even when the issue stays open runs along the same line as Paul’s warning not to let anger take root.',
        caveat: 'Paul is naming bitterness and the foothold it gives, not setting a nightly deadline for resolution. Kindness and forgiveness in this passage are not a demand that a wronged person produce immediate emotional closure, and they do not cancel accountability, boundaries, or the time repair actually takes.'
      },
      {
        reference: 'Proverbs 15:1, 18',
        teaching: 'A gentle answer turns away wrath, and a hot temper stirs up strife. This underwrites the session’s emphasis on tone and timing.',
        caveat: 'Proverbs give general wisdom about how life usually goes; they are not guarantees. A gentle answer reliably lowers heat with a person who is arguing. It does not make an intimidating person safe, and its failure is not proof that the gentler spouse did it wrong.'
      },
      {
        reference: 'James 1:19–20',
        teaching: 'Quick to hear, slow to speak, slow to anger. This is the plainest scriptural warrant for the turn-taking and listening rules in the five-step protocol.',
        caveat: 'Slow to speak is a discipline of the tongue, not a vow of silence about real harm. James goes on to require doing, not only hearing, so a husband who listens beautifully and changes nothing has not obeyed this text.'
      }
    ]
  },

  coreFramework: {
    heading: 'Four principles, four postures, one externalised problem',
    lead: 'The session’s framework is genuinely usable. What follows states each part as the source gives it, then names the husband’s move and the guardrail that keeps the move honest.',
    principles: [
      {
        number: '01',
        name: 'Remember her positive qualities',
        source: 'Appreciation is taught as protection: keeping admiration spoken guards the marriage from sliding into nagging and complaint, and the journal exercise asks each spouse to write six appreciations — a mix of character and concrete action — and read them aloud.',
        husbandMove: 'Name six specific things, half character and half action, and say them without attaching a request. “I admired how you handled the call with your mother” is worth more than “you’re great.”',
        guardrail: 'Appreciation must not be used to soften a hard truth into silence, and it must never function as payment for an unaddressed injury. If you cannot raise a real concern, more compliments will not fix that.'
      },
      {
        number: '02',
        name: 'Treat differences as differences',
        source: 'Decision speed, introversion and extroversion, internal and external processing, punctuality, and money habits are offered as differences rather than defects. The reframe the session lands on is that neither spouse is better with money; they are better at different things with money.',
        husbandMove: 'Take one recurring friction point and write the sentence that converts a ranking into a division of labour. Then design a team procedure for it instead of relitigating it monthly.',
        guardrail: 'Not every difference is a neutral style. Hidden debt, a broken agreement, compulsive spending, or withholding access to money is not a “money personality.” Sort each friction into a preference, a skill gap, a broken agreement, or a safety concern before applying this principle.'
      },
      {
        number: '03',
        name: 'Look for an “us” solution',
        source: 'Three postures are rejected as ineffective — attacking to force your way, surrendering to avoid confrontation, and bargaining that decays into “I won’t do my part because you haven’t done yours.” The alternative is working the issue together, sometimes after pressing an imaginary pause button.',
        husbandMove: 'Say the issue in one sentence before you say anything about her. If you cannot state it in one sentence, you are not ready to discuss it yet.',
        guardrail: '“We’re on the same team” is a description of two people who both hold power, not a slogan that settles who is right. If team language is being used to require agreement, it has stopped meaning anything.'
      },
      {
        number: '04',
        name: 'Support her',
        source: 'The final principle contrasts expecting a spouse to meet every need with focusing on meeting hers, illustrated by a husband who asked each morning how he could make his wife’s day better. The session grounds this in looking first to God for love, significance, and security, and offers a daily practice of brief mutual prayer with a plain alternative question for those not comfortable praying.',
        husbandMove: 'Ask the question once a day for a week and do one reasonable thing that comes back. Ask before you decide what she needs.',
        guardrail: 'In the story the practice worked because it was returned. Service that runs one way for months without reciprocity is a signal to get help, not a standard to sustain. And no one should be told that anxiety, depression, or trauma would lift with more faith.'
      }
    ],
    postures: {
      heading: 'The four postures, named in a husband’s terms',
      note: 'Source teaching supplies the first three labels. The behavioural descriptions are ministry analysis.',
      items: [
        { name: 'Attack', looksLike: 'Volume, speed, stacked evidence, character verdicts, dragging in ten years of history, threatening the relationship to win the hour.', cost: 'You may end the argument. You will not be told the truth next time.' },
        { name: 'Surrender', looksLike: 'Agreeing to end the discomfort, going quiet, leaving with no return, saying “fine” and retaliating later in a smaller way.', cost: 'The issue survives untouched and collects interest. Note carefully: surrender can also be what fear looks like, and that is a different problem entirely.' },
        { name: 'Bargain', looksLike: 'Trading compliance, keeping a ledger, holding your part hostage until she performs hers.', cost: 'The marriage becomes a contract that either party can breach, and the ledger always reads in your favour.' },
        { name: 'Collaborate', looksLike: 'One issue, stated plainly. Your own contribution named first. Turn-taking. A decision small enough to test.', cost: 'It is slower, it requires you to be wrong out loud, and it is the only one of the four that compounds.' }
      ]
    },
    externalise: {
      heading: 'Put the issue in front of you',
      teaching: 'The session’s most transferable image places a couple at opposite ends of a sofa with the contentious issue sitting between them, blocking sight and hearing. Focusing on the issue means lifting it out from between you and setting it out in front, so you can move together and face it rather than face off.',
      analysis: 'Externalising the problem is not the same as excusing the person. Your conduct still belongs to you. The image works because it changes the seating, not because it dissolves responsibility — and a husband who uses “let’s attack the problem” to avoid saying “I did that” has inverted it.',
      criticalNote: 'Independent review flagged a real failure mode here: the same image, used on an issue that is actually one person’s ongoing harm, converts a one-sided problem into a shared one. Externalise disagreements. Do not externalise conduct.'
    },
    extendedBriefHeading: 'Extended field brief'
  },

  fairInsight: {
    heading: 'What the source gets right',
    paragraphs: [
      'All four independent reviews agree on the same strengths, and this module adopts them without hedging. Decoupling “we have conflict” from “we chose wrong” removes a genuine source of panic. Insisting that appreciation is a daily habit rather than a mood gives a husband something to do on an ordinary Tuesday. Recasting a status contest into a division of labour dissolves an argument that cannot otherwise be won.',
      'The two strongest contributions are structural. A pause rule that either spouse can call unilaterally is well designed precisely because it does not require agreement in a moment when agreement is unavailable. And the five steps are a real protocol: they interrupt escalation with sequenced, observable actions rather than asking anyone to feel differently first. The distinction between requesting change and demanding it is a compact ethical boundary worth memorising.'
    ]
  },

  caution: {
    heading: 'Where caution is required',
    paragraphs: [
      'The framework assumes symmetry — two people with roughly equal power, both free to speak, both able to say no without consequence. Every reviewer named this as the central blind spot, and it is the reason this module carries a referral boundary rather than a footnote. Where that symmetry does not exist, the tools do not merely underperform. Several of them invert.',
      'A husband should also know that some of the session’s most quotable lines are the ones that need the most care. They are not wrong between equals. They are hazardous when transposed onto a relationship where one person is the source of harm.'
    ],
    slogans: [
      {
        line: 'The only person we can change is ourselves.',
        stamp: 'Source teaching, near 00:53:45',
        qualification: 'Freeing between two safe people, because it ends the futile project of managing another adult. Used on someone being harmed, it relocates responsibility for another person’s conduct onto the person absorbing it. Personal agency is not the same as personal fault.'
      },
      {
        line: 'We’re not incompatible unless we refuse to change.',
        stamp: 'Source teaching, near 00:56:06',
        qualification: 'Motivating for a flexible couple stuck on habits. As a general account of why marriages fail, it is too sweeping — and it can pressure someone to keep adjusting to untreated addiction, repeated betrayal, or an unsafe home. Willingness to change is necessary. It is not always sufficient.'
      },
      {
        line: 'Trying to make our husband or wife think and behave like us never works.',
        stamp: 'Source teaching, near 00:20:10',
        qualification: 'Directionally true about coercion, and stated as an absolute. People do influence and change each other, and marriages do require some behaviour to change. What reliably fails is compelling it.'
      }
    ],
    additional: [
      'The transformed-marriage story near 01:29:17 is a second-hand anecdote with an unusually clean arc. It is inspiration, not a mechanism you can rely on.',
      'The research citation near 00:08:34 — that a well-known researcher can tell within five minutes whether a relationship is in trouble, with appreciation as the key indicator — is compressed. Do not repeat the five-minute framing as settled fact, and do not try to diagnose your marriage with it.',
      'Humour is commended as the oil in the engine, and teasing about a spouse’s speech style is modelled. There is no guard attached. Add one: humour that mocks vulnerability is contempt wearing a friendly face.',
      'Introvert and extrovert, saver and spender, are useful folk categories stated as clean binaries. They become excuses the moment “that’s just how I am” closes a conversation — which the session itself warns against elsewhere.',
      'Processing differences may reflect neurodivergence, trauma, hearing or language differences, or exhaustion rather than personality. Adapt the format — written notes, longer pauses, a walk instead of eye contact — without abandoning the aim.'
    ]
  },

  selfCheck: {
    heading: 'Husband’s self-check',
    intro: 'Use these privately. They are prompts, not a scorecard, and none of them is about her. If an answer stings, resist building a case and name your next action instead.',
    items: [
      'I can describe my first predictable move under pressure in behaviour, not in temperament.',
      'I state the problem in one sentence before I say anything about my wife.',
      'I name my own contribution before I assign hers.',
      'My pauses include a specific return time, and I have kept the last three.',
      'I do not follow her from room to room, block a doorway, take her phone or keys, or stand over her to keep a conversation going.',
      'I can hear a concern without immediately explaining my intent.',
      'I do not use sarcasm, mockery, imitation, or jokes at her expense during a disagreement.',
      'I do not invoke Scripture, headship, prayer, money, or the children to end a discussion I am losing.',
      'When conflict happens in front of our children, I repair it in front of them and never make them messengers, referees, or allies.',
      'I can tell the difference between a preference, a skill gap, a broken agreement, and a safety concern — and I respond to each differently.'
    ]
  },

  pauseProtocol: {
    heading: 'The pause-and-return protocol',
    teaching: {
      heading: 'Original source teaching',
      paragraphs: [
        'The session names bad times to argue — in front of others, just before a special occasion, in a rush, on walking through the door — and identifies late at night as the worst, because fatigue distorts perspective. It then teaches a rule borrowed from friends, in which either spouse can unilaterally call a late-evening argument paused and postponed to a better time, perhaps the next evening or over coffee at the weekend.',
        'Two refinements matter. Waiting for a better time requires self-discipline, and the postponement does not mean going to bed still angry: if unkind things were said, apologise and forgive so the relationship is repaired even while the issue stays open.'
      ]
    },
    analysis: {
      heading: 'U.S.M.C. Ministries analysis & application',
      lead: 'A pause without a return is not a pause; it is abandonment with better manners. The rule below is what makes the source’s tool honest, and it must be negotiated while you are calm, not invented mid-argument.',
      rules: [
        'Either spouse may call the pause. It does not require the other’s agreement, and it is not overruled by whoever is more articulate.',
        'The person calling it names a specific return time out loud: “I am too activated to speak carefully. Twenty minutes. I will be back at 7:40.”',
        'A minimum of twenty minutes is usually needed for a body to come down. Set a maximum too, so “later” cannot mean never.',
        'During the pause, do not draft a closing argument, text allies, drink, drive angry, or punish with silence. Walk, breathe, pray.',
        'If the named time becomes impossible, send a short message with another specific time. One missed return is a mistake; a pattern of missed returns is the actual issue.',
        'Repair the conduct before sleep even if the topic stays open. “I was contemptuous and I am sorry” does not require the budget to be solved first.',
        'Do not use the apology to close the subject. “I said sorry, so can we drop it?” converts repair into a control tactic.'
      ],
      notAPause: [
        'Leaving with no return time.',
        'Refusing every proposed time until the concern expires.',
        'Using the pause to escape accountability you have already been given.',
        'Following her, blocking the exit, or requiring her to stay while you regulate.'
      ]
    },
    safetyLine: 'One clarification the source does not make. If you are afraid of your spouse, leaving is not a “pause” and you owe no return time. A safety exit and a conflict pause are different actions with different rules, and nothing on this page should be read as requiring anyone to come back to a room that is not safe.'
  },

  fiveSteps: {
    heading: 'The five-step problem-solving protocol',
    intro: 'The five steps are stated by the source near 00:47:12–00:51:43. The execution note and failure mode under each are ministry analysis.',
    preconditions: [
      'One issue, agreed in advance and stated in a single sentence.',
      'A time both of you actually chose, with a stated length — thirty to forty minutes is plenty.',
      'Both of you free to decline, pause, or reschedule without penalty.',
      'Not the most explosive issue in your marriage. Learn the protocol on something moderate.'
    ],
    steps: [
      {
        number: '1',
        step: 'Focus on the issue causing the conflict',
        source: 'Arguments widen until nobody remembers what started them. Identifying and staying on the main issue prevents escalation.',
        execution: 'Write the issue on paper in one sentence and put it where you can both see it. Anything else that surfaces gets written on a second list for another day.',
        failureMode: 'Kitchen-sinking. The moment you reach for an unrelated failure from two years ago, you have left the protocol.'
      },
      {
        number: '2',
        step: 'Use “I” statements',
        source: '“You always” and “you never” label character. Describing your own experience — “I was upset that I cleared up alone after dinner last night” — is more workable.',
        execution: 'Name the event, the effect on you, and what you want. Keep it to one event with a date.',
        failureMode: 'A verdict wearing the grammar of a feeling. “I feel disrespected whenever you disagree with me” is still an accusation. And when conduct needs naming plainly — money moved without consent, a threat made — say the conduct.'
      },
      {
        number: '3',
        step: 'Listen and take turns',
        source: 'In an argument both people want to be understood and neither wants to understand. The ground rule is to take it in turns to talk, which matters most when one spouse is better with words.',
        execution: 'Summarise what she said and ask what you missed before you reply. If you are the faster talker, take the second turn.',
        failureMode: 'Listening as reload time. If your summary is a weaker version of her point that is easy to dismiss, you were building a case.'
      },
      {
        number: '4',
        step: 'Brainstorm possible solutions',
        source: 'Once the first three steps are done, options come more easily than expected. On money the session lists changing who organises the finances, building an annual budget together, using cash instead of credit, a weekly spending review, or asking for help from someone competent.',
        execution: 'Write at least four options before evaluating any of them, and include one you do not like. Say them out loud.',
        failureMode: 'Proposing your preferred answer first and calling it brainstorming.'
      },
      {
        number: '5',
        step: 'Decide the best solution for now, and review later',
        source: 'Pick a solution for now and try it. If it works, the issue stops causing conflict. If it does not, go back to the list and try another.',
        execution: 'Write who does what, by when, and the date you will review it. Two weeks is usually long enough to learn something.',
        failureMode: 'Treating agreement as final. And this: compliance produced by fear is not a decision. If she agreed quickly and looked relieved, check whether she was free to say no.'
      }
    ],
    close: 'The session adds two boundaries this module keeps. Requesting change is good; demanding it is harmful. And you cannot assume your spouse knows what matters to you — the things that frustrate and hurt have to be said.'
  },

  fieldExercise: {
    heading: 'One-week field exercise',
    intro: 'Success is completion and learning, not a conflict-free week and not identical feelings. Either spouse may stop any day of this without explanation. If fear or contempt dominates, stop the exercise and get help rather than powering through.',
    days: [
      { day: 'Day 1', title: 'Name your own move.', body: 'Write, privately, what you do first when conflict becomes uncomfortable — in behaviour, not temperament. Then say it to your wife in one sentence without diagnosing hers.' },
      { day: 'Day 2', title: 'Six appreciations.', body: 'Each writes six things you appreciate — three character, three concrete action — and reads them aloud. No rebuttal, no requests attached.' },
      { day: 'Day 3', title: 'Negotiate the pause rule.', body: 'Agree the phrase, the minimum and maximum length, and how a return time gets named. Write it down. Ask what would make it feel fair to her.' },
      { day: 'Day 4', title: 'Sort one friction.', body: 'Take one recurring disagreement and decide together whether it is a preference, a skill gap, a broken agreement, or something that needs outside help. Handle it accordingly.' },
      { day: 'Day 5', title: 'Listen back.', body: 'Pick a low-stakes concern. She speaks for five minutes; you summarise content and significance, ask what you missed, and revise until she says it is fair. Do not require her to do the same.' },
      { day: 'Day 6', title: 'Run the five steps.', body: 'Take the Day 4 friction through all five steps in forty minutes or less. Finish with a written decision, an owner, and a review date.' },
      { day: 'Day 7', title: 'After-action review.', body: 'Fifteen minutes. What helped? What felt unsafe or unhelpful? Did the pause get used, and did the return happen? Record one thing to keep and one to change.' }
    ],
    finishLine: 'You interrupted your usual conflict move at least once, honoured every physical and verbal boundary, returned at the time you promised or named a specific new one, and produced one written decision with a review date.'
  },

  discussionPrompts: {
    heading: 'Discussion prompts',
    intro: 'Invite; do not assign. Your wife may decline any of these, stop partway, or answer a different one. A prompt she did not agree to is an interrogation.',
    items: [
      'When conflict starts, what do I do that makes it harder for you to stay in the room?',
      'Which of our differences have I been quietly scoring as better and worse rather than different?',
      'What are our genuinely bad times to argue, and what pause phrase would you actually honour?',
      'When we pause something, do we come back to it — or has “later” been doing the work of “never”?',
      'Which of the five steps is hardest for each of us, and why?',
      'When I ask you to change something, does it usually land as a request or a demand?',
      'How do we repair the relationship on a night when the issue is not solved?',
      'Where are these tools the wrong tool for us, and what would wise outside help look like?'
    ]
  },

  conversationGuide: {
    heading: 'Optional conversation guide',
    intro: 'A thirty-minute structure for the Day 6 run. Invite; do not assign. Either of you may call the pause at any point, including in the first minute.',
    steps: [
      { label: 'Set the conditions (3 min)', body: '“I want to understand this, not win it. Is now workable for thirty minutes? Either of us can call a pause and we will name a return time.”' },
      { label: 'State the issue (2 min)', body: 'One sentence, agreed out loud, written down where you can both see it. Anything else goes on the second list.' },
      { label: 'Speaker one (7 min)', body: 'One event, the effect on you, what you want. No “always,” no “never,” no history that is not this issue.' },
      { label: 'Listen back (3 min)', body: '“What I heard was… What did I miss?” Revise until she says it is fair. Do not rebut.' },
      { label: 'Switch (10 min)', body: 'Same structure, equal time. If you are the faster talker, this is where you keep your mouth shut.' },
      { label: 'Decide and close (5 min)', body: 'Four options minimum, then one to test. Who does what, by when, review date. End with appreciation or prayer if that is mutually welcome.' }
    ],
    pauseSignal: 'If voices rise, contempt appears, or either of you is flooded, stop and name a return time. If returns repeatedly become frightening, degrading, or circular, that is not a technique problem — move to the referral boundary below.'
  },

  referral: {
    heading: 'Support and safety boundary',
    lead: 'This module is education and practice for a basically safe marriage. It is not counselling, crisis care, addiction treatment, or trauma care, and completing it is not evidence that a marriage is safe.',
    distinction: 'Ordinary marital conflict is not coercive control, threats, stalking, violence, sexual coercion, active addiction, or retaliation for honest speech. Those are different problems with different responses. Where any of them is present, the joint exercises on this page — the shared pause rule, the five steps, the appreciation lists, the daily support question — may be ineffective or actively unsafe, because what is disclosed in a joint exercise can be used later. Seek confidential individual help first and prioritise immediate safety over any exercise in this course.',
    referrals: [
      { label: 'Immediate danger', body: 'Call or text 911 in the United States, or your local emergency service.', href: null },
      { label: 'Abuse or coercive control', body: 'Seek confidential individual safety planning and prioritize immediate safety. Joint exercises are not automatically appropriate when control or fear is present.' },
      { label: 'Suicidal or mental-health crisis', body: 'In the U.S., call or text 988.', href: 'https://988lifeline.org/', linkLabel: '988lifeline.org' },
      { label: 'Betrayal, addiction, trauma, or entrenched high conflict', body: 'A licensed clinician with relevant specialisation. Trained pastoral care supports that work; it does not replace it.', href: null }
    ],
    close: 'A husband must never use Scripture, forgiveness, headship, money, the children, or completion of this course to demand access, silence a concern, or prevent someone from getting help. Forgiveness does not cancel boundaries, consequences, reporting, safety planning, or the requirement for demonstrated change.'
  },

  verification: {
    heading: 'Claims carried forward for verification',
    intro: 'Ministry analysis. These were flagged by more than one independent review and are not settled on this page.',
    items: [
      'The presenters’ surname. The transcript gives only first names; one review supplies a surname the transcript never states.',
      'The five-minute prediction claim and the appreciation indicator attributed to a named researcher near 00:08:34, which should be checked against a primary publication before being repeated.',
      'The compliment quotation attributed to Mark Twain near 00:06:42, commonly attributed and thinly sourced.',
      'The surgical passage read near 00:56:15, attributed in the transcript to Richard Seltzer. Authorship, exact wording, and reprint permission all require checking; it is deliberately not reproduced here.',
      'The transformed-marriage account near 01:29:17, which is second-hand and should never be cited as evidence.',
      'Transcript completeness. Roughly 00:10–00:19, 00:30–00:39, and 01:00–01:28 carry no dialogue in the supplied source.'
    ]
  },

  resources: {
    heading: 'Resource room',
    intro: 'Seventeen completed artifacts came out of the Episode 3 research package. Eleven are stored locally with this prototype and open from here. Six are named but not published. Everything below was generated by NotebookLM from the source material: treat it as a study aid, not as independent authority, and read it against the caution section above.',
    groups: [
      { key: 'slides', heading: 'Slide decks', count: '3 artifacts', note: 'PDF exports. Large files; not yet size-optimised for the web.' },
      { key: 'infographics', heading: 'Field graphics', count: '3 artifacts', note: 'Single-page visual summaries. Two of the three contain visible generated-text errors, noted per graphic.' },
      { key: 'reports', heading: 'Readable reports', count: '3 artifacts', note: 'Markdown study aids in three different registers.' },
      { key: 'quiz', heading: 'Knowledge check', count: '1 artifact', note: 'Interactive NotebookLM export.' },
      { key: 'flashcards', heading: 'Flashcards', count: '1 artifact', note: 'Interactive NotebookLM export.' },
      { key: 'withheld', heading: 'Held in the research package', count: '6 artifacts', note: 'Three audio briefings and three video overviews. Named here, not published here.' }
    ],
    withheldNotice: 'These six were produced and reviewed, and they stay in the local research package for now. Publishing them requires clearing rights on the underlying course material, producing captions and transcripts so they are accessible, normalising codecs and bitrates, choosing a hosting arrangement that will not be paid for by a static bucket, and Adam’s approval. None of that is done, so none of them is copied into this prototype.',
    notebook: {
      title: 'Verified NotebookLM notebook',
      body: 'Google account required. Access depends on notebook permissions and the signed-in account. The notebook holds the sources and every artifact, including the six not published here.',
      label: 'Open “TMC Episode 3” in NotebookLM',
      href: 'https://notebooklm.google.com/notebook/9237c8b2-4f96-4cb7-9f32-040305833123'
    },
    journal: {
      heading: 'Optional companion journal',
      label: 'The Marriage Course Study Journal',
      href: 'https://www.amazon.com/dp/0310116694?tag=usmcministrie-20',
      body: 'The session repeatedly directs couples to written conversations in the companion journal — the six appreciations, the differences map, and the five-steps exercise. It is optional and this module works without it.',
      disclosure: 'Affiliate disclosure: this is an Amazon Associates link. As an Amazon Associate I earn from qualifying purchases, at no extra cost to you.'
    }
  },

  artifacts: [
    {
      slug: 'slides-engineering-us',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'Engineering Us',
      summary: 'A deck built from the systems-analyst reading of the episode: the marriage treated as a system with failure points and feedback loops. Not reviewed line by line.',
      href: '../assets/media/tmc-husband/m03/slides/engineering-us.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'slides-marital-conflict-blueprint',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'Marital Conflict Blueprint',
      summary: 'A deck walking the conflict pathway from the four principles through the five steps. Not reviewed line by line.',
      href: '../assets/media/tmc-husband/m03/slides/marital-conflict-blueprint.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'slides-the-marriage-blueprint',
      state: 'local',
      group: 'slides',
      kind: 'PDF',
      title: 'The Marriage Blueprint',
      summary: 'A broader overview deck covering the session as a whole. Not reviewed line by line.',
      href: '../assets/media/tmc-husband/m03/slides/the-marriage-blueprint.pdf',
      linkLabel: 'Open slide deck'
    },
    {
      slug: 'infographic-conflict-resolution-field-guide',
      state: 'local',
      group: 'infographics',
      title: 'Marriage Conflict Resolution Field Guide',
      summary: 'Headlined “Navigating the Waves Together.” Covers the rowing contrast, daily appreciation, differences as strengths, a do-and-do-not panel, the five-step protocol, and a red-flag panel directing coercion, abuse, trauma, and serious trust violations to professional help. Review note: several captions contain garbled generated text.',
      href: '../assets/media/tmc-husband/m03/infographics/marriage-conflict-resolution-field-guide.png',
      alt: 'Illustrated one-page field guide titled “Navigating the Waves Together: A Marriage Field Guide to Conflict Resolution,” with panels on competitive versus synchronised rowing, the same-team mindset, daily appreciation, differences as strengths, a do-and-do-not comparison, the sofa visualisation, a five-step “us” solution protocol, and a red-flag panel on when to seek professional intervention.'
    },
    {
      slug: 'infographic-conflict-and-teamwork-guide',
      state: 'local',
      group: 'infographics',
      title: 'Marriage Conflict and Teamwork Guide',
      summary: 'Headlined “Navigating the Storm.” The most complete of the three: four pillars, the conflict toolkit, the five-step protocol, a seven-day action plan, and an explicit safety overlay stating that the tools require mutual goodwill and that changing yourself must not be used to accommodate abuse. Review note: several captions contain garbled generated text.',
      href: '../assets/media/tmc-husband/m03/infographics/marriage-conflict-and-teamwork-guide.png',
      alt: 'Illustrated one-page guide titled “Navigating the Storm: A Practical Guide to Marital Conflict and Teamwork,” with sections on conflict as normal, the four pillars of resolution, a conflict toolkit covering the ten o’clock rule and the sofa metaphor, a five-step protocol, a yellow safety overlay warning that the tools require mutual goodwill and are not a substitute for crisis care, and a seven-day action plan table.'
    },
    {
      slug: 'infographic-teamwork-guide',
      state: 'local',
      group: 'infographics',
      title: 'Marriage Teamwork Guide',
      summary: 'The simplest of the three: five cards covering appreciation, differences, the timing rule, the “us” solution, and the daily support question. Cleanly typeset, but it carries no safety panel at all — do not hand it out on its own.',
      href: '../assets/media/tmc-husband/m03/infographics/marriage-teamwork-guide.png',
      alt: 'Illustrated one-page guide titled “From Conflict to Connection: Your Marriage Teamwork Guide,” showing two people pulling a rope across a bridge above five stacked cards on daily appreciation, differences as strengths, the ten o’clock rule, seeking the “us” solution, and asking how to make your spouse’s day better.'
    },
    {
      slug: 'report-conflict-resolution-and-partnership',
      state: 'local',
      group: 'reports',
      title: 'Conflict Resolution and Partnership: A Briefing on The Marriage Course Episode 3',
      summary: 'An executive briefing mapping the four principles and the five steps. The most neutral of the three reports and the best starting point.',
      href: '../assets/media/tmc-husband/m03/reports/conflict-resolution-and-partnership-briefing.md',
      linkLabel: 'Read the local Markdown report'
    },
    {
      slug: 'report-from-clashing-oars-to-gliding-boats',
      state: 'local',
      group: 'reports',
      title: 'From Clashing Oars to Gliding Boats: Mastering Conflict as a Team',
      summary: 'A systems-flavoured treatment written in a family-life-educator voice, working the rowing metaphor through feedback loops and equilibrium. Its systems language is analysis, not measurement.',
      href: '../assets/media/tmc-husband/m03/reports/from-clashing-oars-to-gliding-boats.md',
      linkLabel: 'Read the local Markdown report'
    },
    {
      slug: 'report-biggest-disagreements-secret-weapon',
      state: 'local',
      group: 'reports',
      title: 'Why Your Biggest Disagreements Might Actually Be Your Relationship’s Secret Weapon',
      summary: 'A popular-article treatment. The headline overclaims: some disagreements are not a secret weapon, they are a warning. Read it against the caution section above.',
      href: '../assets/media/tmc-husband/m03/reports/why-your-biggest-disagreements-secret-weapon.md',
      linkLabel: 'Read the local Markdown report'
    },
    {
      slug: 'quiz-marriage-quiz',
      state: 'local',
      group: 'quiz',
      title: 'Marriage Quiz',
      summary: 'A knowledge check over the Episode 3 material. Review note: this export loads web fonts from an external host, so it is not offline-clean and is not publication-ready as shipped.',
      href: '../assets/media/tmc-husband/m03/quiz/marriage-quiz.html',
      linkLabel: 'Open the quiz'
    },
    {
      slug: 'flashcards-marriage-flashcards',
      state: 'local',
      group: 'flashcards',
      title: 'Marriage Flashcards',
      summary: 'A flashcard drill over the same material. Review note: same external web-font dependency as the quiz.',
      href: '../assets/media/tmc-husband/m03/flashcards/marriage-flashcards.html',
      linkLabel: 'Open the flashcards'
    },
    {
      slug: 'audio-when-good-marriage-advice-goes-wrong',
      state: 'withheld',
      group: 'withheld',
      kind: 'Audio briefing',
      title: 'When Good Marriage Advice Goes Wrong',
      summary: 'A critical audio companion on where sound conflict advice misfires. Held in the local research package.'
    },
    {
      slug: 'audio-when-marriage-tools-become-dangerous-weapons',
      state: 'withheld',
      group: 'withheld',
      kind: 'Audio briefing',
      title: 'When Marriage Tools Become Dangerous Weapons',
      summary: 'An audio discussion of the safety inversion at the centre of this module. Held in the local research package.'
    },
    {
      slug: 'audio-why-your-partner-is-not-the-problem',
      state: 'withheld',
      group: 'withheld',
      kind: 'Audio briefing',
      title: 'Why your partner is not the problem',
      summary: 'An audio treatment of externalising the issue. Held in the local research package; its title needs the caution above attached before it goes anywhere.'
    },
    {
      slug: 'video-how-to-externalize-marriage-conflict',
      state: 'withheld',
      group: 'withheld',
      kind: 'Video overview',
      title: 'How to Externalize Marriage Conflict',
      summary: 'A short video on the sofa image. Held in the local research package.'
    },
    {
      slug: 'video-navigating-conflict',
      state: 'withheld',
      group: 'withheld',
      kind: 'Video overview',
      title: 'Navigating Conflict',
      summary: 'A longer video overview of the session. Held in the local research package.'
    },
    {
      slug: 'video-resolving-conflict',
      state: 'withheld',
      group: 'withheld',
      kind: 'Video overview',
      title: 'Resolving Conflict',
      summary: 'A longer video overview of the four principles and five steps. Held in the local research package.'
    }
  ]
};

module.exports = { fieldManual };
