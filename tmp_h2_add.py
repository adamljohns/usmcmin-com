#!/usr/bin/env python3
import json, os

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'issues.json')

NEW = [
{
  "id": "fl-homestead-tax-2026",
  "slug": "fl-homestead-tax-2026",
  "category": "economic-stewardship",
  "title": "Florida Homestead Tax Exemption & Property-Tax Relief Amendment (Nov 2026)",
  "state": "FL",
  "location": "Statewide — All Florida Voters",
  "date": "November 3, 2026",
  "urgency": "info",
  "urgency_label": "On the 2026 Ballot",
  "summary": "Legislatively referred constitutional amendment (HJR 1F) that would raise the homestead exemption on non-school property taxes from $25,000 to $150,000 in 2027 and $250,000 in 2028, index it to inflation, cut the annual assessment cap on non-homestead property from 10% to 5%, and place new restrictions on local-government spending. Referred to voters in the June 2026 special session; needs 60% to pass.",
  "body": "<h3>What The Amendment Does</h3><ul><li>Raises the homestead exemption that applies to county, city, and special-district (non-school) property taxes from $25,000 to $150,000 in 2027, then to $250,000 in 2028, with inflation indexing beginning in 2029.</li><li>Leaves the existing $25,000 exemption for school-district taxes unchanged — so a homeowner would effectively carry two exemptions.</li><li>Reduces the annual assessment-increase cap on non-homestead property from 10% to 5%, starting January 1, 2027.</li><li>Adds restrictions on how much county and municipal governments can spend in specified categories, and includes a five-year phase-in for new Florida residents.</li></ul><h3>How It Got On The Ballot</h3><ul><li>The Legislature referred it in the June 1–3, 2026 special session.</li><li><strong>House vote:</strong> 75-26 in favor.</li><li><strong>Senate vote:</strong> 30-9 in favor.</li><li>Like all Florida constitutional amendments, it needs <strong>60% voter approval</strong> to take effect.</li></ul>",
  "analysis": "This is a real, substantial tax cut for Florida homeowners, and the structure is honest about what it touches: it lowers the bite on county and city taxes while deliberately leaving school funding alone. For a family trying to hold onto a home, raising the exemption to $150,000 and then $250,000 is meaningful relief, and dropping the non-homestead assessment cap from 10% to 5% slows how fast the tax bill climbs on everything else. The harder question for a RESOLUTE voter is downstream: property taxes fund local services, so weigh whether your county can absorb the cut without leaning on new fees or debt, and read the spending-restriction language as a feature, not a footnote. A 'yes' favors letting households keep more of what they earn and tightening the leash on local spending; just go in clear-eyed that lost revenue lands somewhere.",
  "scripture": "A good man leaveth an inheritance to his children's children: and the wealth of the sinner is laid up for the just.",
  "scripture_ref": "Proverbs 13:22 (KJV)",
  "supporters": [
    "Florida legislative Republicans (referred it 75-26 House / 30-9 Senate)",
    "Gov. Ron DeSantis (R) and property-tax-relief advocates"
  ],
  "opponents": [
    "Some local-government officials and associations concerned about lost county/city revenue"
  ],
  "sources": [
    {
      "label": "Ballotpedia News — Florida voters to decide expanded homestead tax exemption amendment in November",
      "url": "https://news.ballotpedia.org/2026/06/03/florida-voters-to-decide-expanded-homestead-tax-exemption-amendment-in-november/"
    },
    {
      "label": "Tax Foundation — Florida Property Tax Proposal: 2026 Details & Analysis",
      "url": "https://taxfoundation.org/blog/florida-property-tax-proposal/"
    },
    {
      "label": "Florida Senate — Senate Passes Historic Property Tax Cut for Florida Homeowners (June 2, 2026)",
      "url": "https://www.flsenate.gov/PublishedContent/Offices/President/6_2_26_Senate_Passes_Historic_Property_Tax_Cut_for_Florida_Homeowners.pdf"
    }
  ]
},
{
  "id": "fl-budget-stabilization-2026",
  "slug": "fl-budget-stabilization-2026",
  "category": "economic-stewardship",
  "title": "Florida Budget Stabilization Fund Amendment (Nov 2026)",
  "state": "FL",
  "location": "Statewide — All Florida Voters",
  "date": "November 3, 2026",
  "urgency": "info",
  "urgency_label": "On the 2026 Ballot",
  "summary": "Legislatively referred constitutional amendment that would raise the cap on Florida's budget stabilization (rainy-day) fund from 10% to 25% of net general revenue and require an annual transfer of the lesser of $750 million or 25% of collections, while letting the Legislature suspend transfers under certain conditions. Needs 60% to pass.",
  "body": "<h3>What The Amendment Does</h3><ul><li>Increases the maximum size of Florida's budget stabilization fund from 10% to 25% of net general revenue.</li><li>Requires an annual transfer into the fund of whichever is lesser: $750 million, or 25% of the prior year's collections.</li><li>Allows the Legislature to suspend the required transfer under specified conditions.</li></ul><h3>How It Got On The Ballot</h3><ul><li>The Legislature referred the amendment to voters for the November 3, 2026 ballot.</li><li>Like all Florida constitutional amendments, it needs <strong>60% voter approval</strong> to take effect.</li></ul>",
  "analysis": "This is the quiet companion to the property-tax cut on the same ballot: a larger rainy-day fund. A bigger reserve is plain prudence — it lets the state weather a downturn or a hurricane season without scrambling, and it is the public-finance version of a household keeping savings on hand. The fair counter-question is whether parking up to a quarter of general revenue in reserve ties money up that could go to taxpayers or current needs, and the escape hatch — letting the Legislature suspend transfers — means the discipline is real only as long as lawmakers honor it. For a RESOLUTE voter, this leans stewardship-positive and low-drama; the case for 'yes' is simply that a government, like a family, should not spend to the edge of its income.",
  "scripture": "There is treasure to be desired and oil in the dwelling of the wise; but a foolish man spendeth it up.",
  "scripture_ref": "Proverbs 21:20 (KJV)",
  "supporters": [
    "Florida legislators backing a larger state reserve",
    "Fiscal-prudence and balanced-budget advocates"
  ],
  "opponents": [],
  "sources": [
    {
      "label": "Ballotpedia — Florida 2026 ballot measures",
      "url": "https://ballotpedia.org/Florida_2026_ballot_measures"
    },
    {
      "label": "Wikipedia — 2026 United States ballot measures (Florida)",
      "url": "https://en.wikipedia.org/wiki/2026_United_States_ballot_measures"
    }
  ]
},
{
  "id": "fl-ag-agritourism-tpp-2026",
  "slug": "fl-ag-agritourism-tpp-2026",
  "category": "economic-stewardship",
  "title": "Florida Agriculture & Agritourism Property-Tax Exemption Amendment (Nov 2026)",
  "state": "FL",
  "location": "Statewide — All Florida Voters",
  "date": "November 3, 2026",
  "urgency": "info",
  "urgency_label": "On the 2026 Ballot",
  "summary": "Legislatively referred constitutional amendment that would exempt tangible personal property — farm equipment and tools typically found on agricultural land and used for farming or agritourism by the landowner or leaseholder — from property taxes. Needs 60% to pass.",
  "body": "<h3>What The Amendment Does</h3><ul><li>Exempts tangible personal property from property taxes when it is the kind of equipment typically present on agricultural land and is used for farming or agritourism.</li><li>Applies whether the property is used by the landowner or by a leaseholder working the land.</li></ul><h3>How It Got On The Ballot</h3><ul><li>The Legislature referred the amendment to voters for the November 3, 2026 ballot.</li><li>Like all Florida constitutional amendments, it needs <strong>60% voter approval</strong> to take effect.</li></ul>",
  "analysis": "Farm equipment is a working tool, not idle wealth, and taxing the tractor a family needs to bring in a harvest is the kind of friction that pushes small agriculture toward consolidation or closure. Exempting that equipment is a targeted relief that lines up with stewarding the land and keeping family farms viable. The narrow watch-item is the 'agritourism' clause: it is sensible for a real working farm that hosts visitors, but loosely drawn agritourism language can become a side door for non-farm property to claim a farm break — so the value of a 'yes' depends on how tightly the term is applied in practice. On balance this is a modest, pro-family, pro-stewardship measure rather than a sweeping one.",
  "scripture": "Be thou diligent to know the state of thy flocks, and look well to thy herds.",
  "scripture_ref": "Proverbs 27:23 (KJV)",
  "supporters": [
    "Florida legislators backing agricultural tax relief",
    "Farm Bureau and agriculture/agritourism advocates"
  ],
  "opponents": [],
  "sources": [
    {
      "label": "Ballotpedia — Florida Exempt Tangible Personal Property Used for Agriculture or Agritourism from Property Taxes Amendment (2026)",
      "url": "https://ballotpedia.org/Florida_Exempt_Tangible_Personal_Property_Used_for_Agriculture_or_Agritourism_from_Property_Taxes_Amendment_(2026)"
    },
    {
      "label": "Wikipedia — 2026 United States ballot measures (Florida)",
      "url": "https://en.wikipedia.org/wiki/2026_United_States_ballot_measures"
    }
  ]
},
{
  "id": "ga-conservation-use-acreage-2026",
  "slug": "ga-conservation-use-acreage-2026",
  "category": "economic-stewardship",
  "title": "Georgia Conservation-Use Acreage Limit Amendment (Nov 2026)",
  "state": "GA",
  "location": "Statewide — All Georgia Voters",
  "date": "November 3, 2026",
  "urgency": "info",
  "urgency_label": "On the 2026 Ballot",
  "summary": "Legislatively referred constitutional amendment that would raise the maximum acreage one owner can enroll in Georgia's Conservation Use Valuation Assessment (CUVA) program — which taxes qualifying farm and timber land at its conservation-use value rather than fair-market value — from 2,000 to 4,000 acres. It would be the first acreage-limit increase since the program began.",
  "body": "<h3>What The Amendment Does</h3><ul><li>Increases the maximum acreage per owner that can qualify for Georgia's Conservation Use Valuation Assessment from 2,000 to 4,000 acres.</li><li>CUVA lets bona fide agricultural and timber land be taxed on its current-use value instead of its higher fair-market value, in exchange for a covenant to keep it in that use.</li><li>If approved, it would be the first increase to the acreage cap since the conservation-use program was established.</li></ul><h3>How It Got On The Ballot</h3><ul><li>The Georgia General Assembly referred the amendment to voters for the November 3, 2026 ballot.</li><li>A simple majority of votes statewide is required to ratify it.</li></ul>",
  "analysis": "Conservation-use assessment is a sound idea: it keeps farm and timber land from being taxed out of existence by suburban land values, which protects both food production and open ground. Doubling the cap to 4,000 acres extends that protection to larger holdings. The honest tension is who benefits at the margin — raising the ceiling helps bigger landowners most, and a RESOLUTE voter who values the small family farm should ask whether this strengthens working agriculture broadly or mainly eases the tax bill on large estates. There is no obvious moral red flag here; it is a question of how far to extend a stewardship-minded break. If you trust that the land stays in genuine agricultural or timber use under the program's covenant, a 'yes' is defensible.",
  "scripture": "The king himself is served by the field.",
  "scripture_ref": "Ecclesiastes 5:9 (KJV)",
  "supporters": [
    "Georgia legislators backing the amendment",
    "Georgia Farm Bureau and timber/agriculture landowners"
  ],
  "opponents": [
    "Critics who argue the higher cap chiefly benefits the largest landowners"
  ],
  "sources": [
    {
      "label": "Ballotpedia News — Georgia voters to decide 2026 amendment to increase acreage limit for conservation-use property tax classification",
      "url": "https://news.ballotpedia.org/2025/03/21/georgia-voters-to-decide-2026-constitutional-amendment-to-increase-acreage-limit-for-conservation-use-property-tax-classification/"
    },
    {
      "label": "Ballotpedia — Georgia Increase Acre Limit for Agriculture and Timber Conservation Use Property Tax Classification Amendment (2026)",
      "url": "https://ballotpedia.org/Georgia_Increase_Acre_Limit_for_Agriculture_and_Timber_Conservation_Use_Property_Tax_Classification_Amendment_(2026)"
    }
  ]
},
{
  "id": "ga-nextgen-911-fund-2026",
  "slug": "ga-nextgen-911-fund-2026",
  "category": "public-justice",
  "title": "Georgia Next Generation 9-1-1 Fund Amendment (Nov 2026)",
  "state": "GA",
  "location": "Statewide — All Georgia Voters",
  "date": "November 3, 2026",
  "urgency": "info",
  "urgency_label": "On the 2026 Ballot",
  "summary": "Legislatively referred constitutional amendment that would authorize the General Assembly to create a dedicated Georgia Next Generation 9-1-1 Fund and direct revenue to upgrading the state's emergency-call (911) systems. It passed both the state Senate and House unanimously before going to voters.",
  "body": "<h3>What The Amendment Does</h3><ul><li>Authorizes the Georgia General Assembly to create a Next Generation 9-1-1 Fund and dedicate revenue to it.</li><li>The fund is aimed at modernizing the state's 911 emergency-call infrastructure (the shift to IP-based 'Next Generation 911' that handles texts, data, and more precise location).</li></ul><h3>How It Got On The Ballot</h3><ul><li>The state Senate approved it unanimously on March 31, and the House approved it unanimously as well.</li><li>The amendment was referred to voters for the November 3, 2026 ballot; a simple majority statewide is required to ratify it.</li></ul>",
  "analysis": "Restraining evil and protecting life is a core, legitimate task of the civil magistrate, and a working 911 system is one of the plainest forms that takes — when a family dials for help, the call has to connect and find them. Dedicating revenue to modern emergency-call infrastructure is squarely within that duty, and the unanimous, bipartisan vote signals there is no real controversy about the need. The only stewardship question worth holding is the one that applies to any dedicated fund: a constitutional lockbox is harder to misuse but also harder to redirect if priorities change, so weigh whether you want this money walled off by the constitution rather than set yearly in the budget. For most RESOLUTE voters this is an easy, low-risk 'yes' on a genuine public-safety need.",
  "scripture": "If thou forbear to deliver them that are drawn unto death, and those that are ready to be slain.",
  "scripture_ref": "Proverbs 24:11 (KJV)",
  "supporters": [
    "State Sen. Harold Jones (D-22)",
    "State Rep. Chuck Martin (R-49)",
    "Georgia General Assembly (unanimous in both chambers)"
  ],
  "opponents": [],
  "sources": [
    {
      "label": "Ballotpedia News — Georgia General Assembly places amendments on 2026 ballot to fund emergency response and require nonpartisan probate-judge elections",
      "url": "https://news.ballotpedia.org/2026/04/02/georgia-general-assembly-places-constitutional-amendments-on-the-2026-ballot-to-fund-emergency-response-systems-and-require-nonpartisan-elections-for-probate-judges/"
    },
    {
      "label": "The Center Square — Georgians will consider three constitutional amendments in November",
      "url": "https://www.thecentersquare.com/georgia/article_92a5a24d-e401-44be-85f7-72f59e6c4b3a.html"
    }
  ]
},
{
  "id": "ga-nonpartisan-probate-judges-2026",
  "slug": "ga-nonpartisan-probate-judges-2026",
  "category": "election-integrity",
  "title": "Georgia Nonpartisan Probate Judge Elections Amendment (Nov 2026)",
  "state": "GA",
  "location": "Statewide — All Georgia Voters",
  "date": "November 3, 2026",
  "urgency": "info",
  "urgency_label": "On the 2026 Ballot",
  "summary": "Legislatively referred constitutional amendment (House Resolution 251) that would require all of Georgia's county probate judges to be elected on a nonpartisan basis rather than in partisan elections. It drew broad bipartisan support — about 94% of Republicans and 85% of Democrats in the General Assembly voted yes.",
  "body": "<h3>What The Amendment Does</h3><ul><li>Requires that elections for county probate judges in Georgia be conducted on a nonpartisan basis — candidates would appear without a party label.</li><li>Probate judges in Georgia handle wills and estates, guardianships, marriage and firearms licenses, and in many counties election administration and certain misdemeanor matters.</li></ul><h3>How It Got On The Ballot</h3><ul><li>Both chambers passed House Resolution 251; roughly 94.3% of Republicans and 85.4% of Democrats voted in favor.</li><li>The amendment was referred to voters for the November 3, 2026 ballot; a simple majority statewide is required to ratify it.</li></ul>",
  "analysis": "A judge's job is to apply the law without fear or favor, and stripping the party label off probate-judge races fits the biblical standard that justice should not respect persons — the question on the bench is what the law and the facts require, not which team the judge plays for. Supporters across the aisle, including the state's chief justice and two former governors of both parties, make the same case. The honest counter-argument, which a careful voter should hold, is that party labels give voters a quick shorthand about a candidate's judicial philosophy, and removing them can leave low-information down-ballot races even harder to judge. On balance this leans toward 'yes' for anyone who wants courts seen as impartial; just know that nonpartisan does not mean apolitical, and you will have to do more homework on the candidates themselves.",
  "scripture": "Ye shall do no unrighteousness in judgment: thou shalt not respect the person of the poor, nor honour the person of the mighty: but in righteousness shalt thou judge thy neighbour.",
  "scripture_ref": "Leviticus 19:15 (KJV)",
  "supporters": [
    "Georgia Chief Justice Michael Boggs",
    "Former Gov. Nathan Deal (R)",
    "Former Gov. Roy Barnes (D)",
    "Bipartisan majorities in both chambers (HR 251)"
  ],
  "opponents": [
    "Some legislators who preferred keeping party labels on judicial races (minority no votes)"
  ],
  "sources": [
    {
      "label": "Ballotpedia News — Georgia General Assembly places amendments on 2026 ballot to fund emergency response and require nonpartisan probate-judge elections",
      "url": "https://news.ballotpedia.org/2026/04/02/georgia-general-assembly-places-constitutional-amendments-on-the-2026-ballot-to-fund-emergency-response-systems-and-require-nonpartisan-elections-for-probate-judges/"
    },
    {
      "label": "Ballotpedia — Georgia Require Nonpartisan Elections for Probate Judges Amendment (2026)",
      "url": "https://ballotpedia.org/Georgia_Require_Nonpartisan_Elections_for_Probate_Judges_Amendment_(2026)"
    },
    {
      "label": "The Center Square — Georgians will consider three constitutional amendments in November",
      "url": "https://www.thecentersquare.com/georgia/article_92a5a24d-e401-44be-85f7-72f59e6c4b3a.html"
    }
  ]
}
]

def main():
    with open(PATH) as f:
        data = json.load(f)
    existing = {it.get('id') for it in data['issues']}
    added = []
    for entry in NEW:
        if entry['id'] in existing:
            print('SKIP existing', entry['id'])
            continue
        data['issues'].append(entry)
        added.append(entry['id'])
    data['meta']['last_updated'] = '2026-06-16'
    with open(PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print('ADDED', len(added), added)
    print('TOTAL issues now', len(data['issues']))

if __name__ == '__main__':
    main()
