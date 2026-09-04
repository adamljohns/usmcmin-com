#!/usr/bin/env python3
"""
add-va-sheriffs-roster-2026-09-04.py — sitting Virginia sheriffs (123 offices).

Harvested 2026-09-04 from VSA directory (vasheriff.org/va-sheriffs-directory/).
Direct curl/playwright blocked by SiteGround captcha; roster parsed from
official directory page content + VSA person URL slugs validated against seed.

Roster-only scaffolds: LOCAL_SCORES null/N/A mask, confidence null, party null.
Does not overwrite Middlesex candidate records (Schomburg/Easter/Longest/Justis).
"""
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).parent
SCORECARD = BASE / "data" / "scorecard.json"
DIRECTORY = "https://vasheriff.org/va-sheriffs-directory/"

LOCAL_SCORES = {
    "sanctity_of_life": [None, None, "N/A", "N/A", "N/A"],
    "biblical_marriage": [None, "N/A", None, "N/A", None],
    "family_child_sovereignty": [None, None, None, "N/A", "N/A"],
    "christian_liberty": [None, "N/A", None, None, None],
    "economic_stewardship": ["N/A", "N/A", None, "N/A", "N/A"],
    "election_integrity": [None, None, "N/A", "N/A", None],
    "border_immigration": ["N/A", None, None, "N/A", "N/A"],
    "self_defense": [None, None, "N/A", "N/A", "N/A"],
    "foreign_policy_restraint": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "industry_capture": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "public_justice": [None, None, None, None, None],
    "refuse_federal_overreach": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "refuse_state_overreach": [None, None, None, None, None],
}

SCaffold_NOTE = (
    "Roster-only scaffold pending grind evidence — sitting Virginia sheriff verified "
    "from VSA directory harvest 2026-09-04; not scored."
)

PROTECTED = {
    "kristen-l-schomburg",
    "christopher-j-easter",
    "bryan-p-longest",
    "thomas-g-justis",
}


def rec(name, slug, jurisdiction, vsa_url):
    return {
        "name": name,
        "slug": slug,
        "office": "Sheriff (sitting)",
        "jurisdiction": jurisdiction,
        "level": "local",
        "party": None,
        "district": None,
        "state": "VA",
        "status": "active",
        "scores": {k: list(v) for k, v in LOCAL_SCORES.items()},
        "notes": SCaffold_NOTE,
        "photo": None,
        "website": None,
        "sources": [DIRECTORY, vsa_url],
        "profile": {
            "religion": None,
            "net_worth": None,
            "birthplace": None,
            "education": None,
            "background": None,
            "twitter": None,
            "prev_election_opponent": None,
            "next_election_year": None,
            "next_election_contenders": [],
            "confidence": None,
        },
        "claims": [],
    }


NEW = [
    rec("W. Todd Wessells", "w-todd-wessells", "Accomack County", "https://vasheriff.org/va-sheriffs-directory/accomack-county-w-todd-wessells/"),
    rec("Chan R. Bryant", "chan-r-bryant", "Albemarle County", "https://vasheriff.org/va-sheriffs-directory/albemarle-county-chan-r-bryant/"),
    rec("Sean Casey", "sean-casey", "Alexandria", "https://vasheriff.org/va-sheriffs-directory/alexandria-sean-casey/"),
    rec("Kyle M. Moore", "kyle-m-moore", "Alleghany County-Covington", "https://vasheriff.org/va-sheriffs-directory/alleghany-county-covington-kyle-m-moore/"),
    rec("Ricky L. Walker", "ricky-l-walker", "Amelia County", "https://vasheriff.org/va-sheriffs-directory/amelia-county-ricky-l-walker/"),
    rec("L.J. \"Jimmy\" Ayers , III", "lj-jimmy-ayers", "Amherst County", "https://vasheriff.org/va-sheriffs-directory/amherst-county-lj-jimmy-ayers/"),
    rec("Robert N. \"Robby\" Richardson", "robert-n-robby-richardson", "Appomattox County", "https://vasheriff.org/va-sheriffs-directory/appomattox-county-robert-n-robby-richardson/"),
    rec("Jose Quiroz", "jose-quiroz", "Arlington County", "https://vasheriff.org/va-sheriffs-directory/arlington-county-jose-quiroz/"),
    rec("Donald L. Smith", "donald-l-smith", "Augusta County", "https://vasheriff.org/va-sheriffs-directory/augusta-county-donald-l-smith/"),
    rec("Robert W. Plecker", "robert-w-plecker", "Bath County", "https://vasheriff.org/va-sheriffs-directory/bath-county-robert-w-plecker/"),
    rec("Mike W. Miller", "mike-w-miller", "Bedford County", "https://vasheriff.org/va-sheriffs-directory/bedford-county-mike-w-miller/"),
    rec("Jason R. Ramsey", "jason-r-ramsey", "Bland County", "https://vasheriff.org/va-sheriffs-directory/bland-county-jason-r-ramsey/"),
    rec("Matthew T. Ward", "matthew-t-ward", "Botetourt County", "https://vasheriff.org/va-sheriffs-directory/botetourt-county-matthew-t-ward/"),
    rec("R. Tyrone Foster", "r-tyrone-foster", "Bristol", "https://vasheriff.org/va-sheriffs-directory/bristol-r-tyrone-foster/"),
    rec("Brian K. Roberts", "brian-k-roberts", "Brunswick County", "https://vasheriff.org/va-sheriffs-directory/brunswick-county-brian-k-roberts/"),
    rec("Allen W. Boyd", "allen-w-boyd", "Buchanan County", "https://vasheriff.org/va-sheriffs-directory/buchanan-county-allen-w-boyd/"),
    rec("W. G. \"Billy\" Kidd Jr.", "w-g-billy-kidd", "Buckingham County", "https://vasheriff.org/va-sheriffs-directory/buckingham-county-w-g-billy-kidd/"),
    rec("W. Randolph Hamilton Jr.", "w-randolph-hamilton", "Buena Vista", "https://vasheriff.org/va-sheriffs-directory/buena-vista-w-randolph-hamilton/"),
    rec("Whit W. Clark III", "whit-w-clark", "Campbell County", "https://vasheriff.org/va-sheriffs-directory/campbell-county-whit-w-clark/"),
    rec("C. Scott Moser", "c-scott-moser", "Caroline County", "https://vasheriff.org/va-sheriffs-directory/caroline-county-c-scott-moser/"),
    rec("Kevin A. Kemp", "kevin-a-kemp", "Carroll County", "https://vasheriff.org/va-sheriffs-directory/carroll-county-kevin-a-kemp/"),
    rec("Jayson T. Crawley", "jayson-t-crawley", "Charles City County", "https://vasheriff.org/va-sheriffs-directory/charles-city-county-jayson-t-crawley/"),
    rec("James R. \"Randy\" Grissom", "james-r-randy-grissom", "Charlotte County", "https://vasheriff.org/va-sheriffs-directory/charlotte-county-james-r-randy-grissom/"),
    rec("James E. Brown III", "james-e-brown", "Charlottesville", "https://vasheriff.org/va-sheriffs-directory/charlottesville-james-e-brown/"),
    rec("Wallace W. Chadwick , III", "wallace-w-chadwick", "Chesapeake", "https://vasheriff.org/va-sheriffs-directory/chesapeake-wallace-w-chadwick/"),
    rec("Karl S. Leonard", "karl-s-leonard", "Chesterfield County", "https://vasheriff.org/va-sheriffs-directory/chesterfield-county-karl-s-leonard/"),
    rec("Travis M. Sumption", "travis-m-sumption", "Clarke County", "https://vasheriff.org/va-sheriffs-directory/clarke-county-travis-m-sumption/"),
    rec("Todd B. Wilson", "todd-b-wilson", "Colonial Heights", "https://vasheriff.org/va-sheriffs-directory/colonial-heights-todd-b-wilson/"),
    rec("L. Trevor N. Craddock", "l-trevor-n-craddock", "Craig County", "https://vasheriff.org/va-sheriffs-directory/craig-county-l-trevor-n-craddock/"),
    rec("Timothy W. Chilton", "timothy-w-chilton", "Culpeper County", "https://vasheriff.org/va-sheriffs-directory/culpeper-county-timothy-w-chilton/"),
    rec("Darrell L. Hodges", "darrell-l-hodges", "Cumberland County", "https://vasheriff.org/va-sheriffs-directory/cumberland-county-darrell-l-hodges/"),
    rec("Michael S. Mondul", "michael-s-mondul", "Danville", "https://vasheriff.org/va-sheriffs-directory/danville-michael-s-mondul/"),
    rec("Jeremy D. Fleming", "jeremy-d-fleming", "Dickenson County", "https://vasheriff.org/va-sheriffs-directory/dickenson-county-jeremy-d-fleming/"),
    rec("D. T. \"Duck\" Adams", "d-t-duck-adams", "Dinwiddie County", "https://vasheriff.org/va-sheriffs-directory/dinwiddie-county-d-t-duck-adams/"),
    rec("Dameon White", "dameon-white", "Emporia", "https://vasheriff.org/va-sheriffs-directory/emporia-dameon-white/"),
    rec("W. A. \"Arnie\" Holmes", "w-a-arnie-holmes", "Essex County", "https://vasheriff.org/va-sheriffs-directory/essex-county-w-a-arnie-holmes/"),
    rec("Stacey A. Kincaid", "stacey-a-kincaid", "Fairfax County", "https://vasheriff.org/va-sheriffs-directory/fairfax-county-stacey-a-kincaid/"),
    rec("Metin \"Matt\" Cay", "metin-matt-cay", "Falls Church", "https://vasheriff.org/va-sheriffs-directory/falls-church-metin-matt-cay/"),
    rec("Jeremy A. Falls", "jeremy-a-falls", "Fauquier County", "https://vasheriff.org/va-sheriffs-directory/fauquier-county-jeremy-a-falls/"),
    rec("Brian J. Craig", "brian-j-craig", "Floyd County", "https://vasheriff.org/va-sheriffs-directory/floyd-county-brian-j-craig/"),
    rec("Eric B. Hess", "eric-b-hess", "Fluvanna County", "https://vasheriff.org/va-sheriffs-directory/fluvanna-county-eric-b-hess/"),
    rec("W. Q. \"Bill\" Overton Jr.", "w-q-bill-overton", "Franklin County", "https://vasheriff.org/va-sheriffs-directory/franklin-county-w-q-bill-overton/"),
    rec("L. W. \"Lenny\" Millholland", "l-w-lenny-millholland", "Frederick County", "https://vasheriff.org/va-sheriffs-directory/frederick-county-l-w-lenny-millholland/"),
    rec("Rashawn Cowles", "rashawn-cowles", "Fredericksburg", "https://vasheriff.org/va-sheriffs-directory/fredericksburg-rashawn-cowles/"),
    rec("W. Morgan Millirons", "w-morgan-millirons", "Giles County", "https://vasheriff.org/va-sheriffs-directory/giles-county-w-morgan-millirons/"),
    rec("Darrell W. Warren, Jr.", "darrell-w-warren", "Gloucester County", "https://vasheriff.org/va-sheriffs-directory/gloucester-county-darrell-w-warren/"),
    rec("Steven N. Creasey", "steven-n-creasey", "Goochland County", "https://vasheriff.org/va-sheriffs-directory/goochland-county-steven-n-creasey/"),
    rec("Gary C. Hash", "gary-c-hash", "Grayson County", "https://vasheriff.org/va-sheriffs-directory/grayson-county-gary-c-hash/"),
    rec("Steven S. Smith", "steven-s-smith", "Greene County", "https://vasheriff.org/va-sheriffs-directory/greene-county-steven-s-smith/"),
    rec("William T. \"Tim\" Jarratt, Jr.", "william-t-tim-jarratt", "Greensville County", "https://vasheriff.org/va-sheriffs-directory/greensville-county-william-t-tim-jarratt/"),
    rec("Fred S. Clark", "fred-s-clark", "Halifax County", "https://vasheriff.org/va-sheriffs-directory/halifax-county-fred-s-clark/"),
    rec("Karen E. Bowden", "karen-e-bowden", "Hampton", "https://vasheriff.org/va-sheriffs-directory/hampton-karen-e-bowden/"),
    rec("Gregory W. Six", "gregory-w-six", "Hanover County", "https://vasheriff.org/va-sheriffs-directory/hanover-county-gregory-w-six/"),
    rec("Alisa A. Gregory", "alisa-a-gregory", "Henrico County", "https://vasheriff.org/va-sheriffs-directory/henrico-county-alisa-a-gregory/"),
    rec("Wayne Davis", "wayne-davis", "Henry County", "https://vasheriff.org/va-sheriffs-directory/henry-county-wayne-davis/"),
    rec("Robert W. \"Bob\" Kelly", "robert-w-bob-kelly", "Highland County", "https://vasheriff.org/va-sheriffs-directory/highland-county-robert-w-bob-kelly/"),
    rec("Travis L. Stanley", "travis-l-stanley", "Hopewell", "https://vasheriff.org/va-sheriffs-directory/hopewell-travis-l-stanley/"),
    rec("James R. Clarke Jr.", "james-r-clarke", "Isle of Wight County", "https://vasheriff.org/va-sheriffs-directory/isle-of-wight-county-james-r-clarke/"),
    rec("William R. \"Rob\" Balderson", "william-r-rob-balderson", "King and Queen County", "https://vasheriff.org/va-sheriffs-directory/king-and-queen-county-william-r-rob-balderson/"),
    rec("Chris A. Giles", "chris-a-giles", "King George County", "https://vasheriff.org/va-sheriffs-directory/king-george-county-chris-a-giles/"),
    rec("T. D. \"Don\" Lumpkin , Jr.", "t-d-don-lumpkin", "King William County", "https://vasheriff.org/va-sheriffs-directory/king-william-county-t-d-don-lumpkin/"),
    rec("Patrick McCranie", "patrick-mccranie", "Lancaster County", "https://vasheriff.org/va-sheriffs-directory/lancaster-county-patrick-mccranie/"),
    rec("Gary B. Parsons", "gary-b-parsons", "Lee County", "https://vasheriff.org/va-sheriffs-directory/lee-county-gary-b-parsons/"),
    rec("Michael L. Chapman", "michael-l-chapman", "Loudoun County", "https://vasheriff.org/va-sheriffs-directory/loudoun-county-michael-l-chapman/"),
    rec("Donald A. Lowe", "donald-a-lowe", "Louisa County", "https://vasheriff.org/va-sheriffs-directory/louisa-county-donald-a-lowe/"),
    rec("Arthur Townsend, Jr.", "arthur-townsend", "Lunenburg County", "https://vasheriff.org/va-sheriffs-directory/lunenburg-county-arthur-townsend/"),
    rec("Donald T. Sloan", "donald-t-sloan", "Lynchburg", "https://vasheriff.org/va-sheriffs-directory/lynchburg-donald-t-sloan/"),
    rec("Erik J. Weaver", "erik-j-weaver", "Madison County", "https://vasheriff.org/va-sheriffs-directory/madison-county-erik-j-weaver/"),
    rec("Steve M. Draper", "steve-m-draper", "Martinsville", "https://vasheriff.org/va-sheriffs-directory/martinsville-steve-m-draper/"),
    rec("April L. Edwards", "april-l-edwards", "Mathews County", "https://vasheriff.org/va-sheriffs-directory/mathews-county-april-l-edwards/"),
    rec("R. W. \"Bobby\" Hawkins Jr.", "r-w-bobby-hawkins", "Mecklenburg County", "https://vasheriff.org/va-sheriffs-directory/mecklenburg-county-r-w-bobby-hawkins/"),
    rec("Michael \"Mickey\" E. Sampson", "michael-mickey-e-sampson", "Middlesex County", "https://vasheriff.org/va-sheriffs-directory/middlesex-county-michael-e-mickey-sampson/"),
    rec("Robert G. Page", "robert-g-page", "Montgomery County", "https://vasheriff.org/va-sheriffs-directory/montgomery-county-robert-g-page/"),
    rec("Mark E. Embrey", "mark-e-embrey", "Nelson County", "https://vasheriff.org/va-sheriffs-directory/nelson-county-mark-e-embrey/"),
    rec("Lee S. Bailey", "lee-s-bailey", "New Kent County", "https://vasheriff.org/va-sheriffs-directory/new-kent-county-lee-s-bailey/"),
    rec("Gabe A. Morgan", "gabe-a-morgan", "Newport News", "https://vasheriff.org/va-sheriffs-directory/newport-news-gabe-a-morgan/"),
    rec("Joe Baron", "joe-baron", "Norfolk", "https://vasheriff.org/va-sheriffs-directory/norfolk-joe-baron/"),
    rec("David L. Doughty Jr.", "david-l-doughty", "Northampton County", "https://vasheriff.org/va-sheriffs-directory/northampton-county-david-l-doughty/"),
    rec("John A. \"Johnny\" Beauchamp", "john-a-johnny-beauchamp", "Northumberland County", "https://vasheriff.org/va-sheriffs-directory/northumberland-county-john-a-johnny-beauchamp/"),
    rec("Jason F. McConnell", "jason-f-mcconnell", "Norton", "https://vasheriff.org/va-sheriffs-directory/norton-jason-f-mcconnell/"),
    rec("Robert L. Jones Sr.", "robert-l-jones", "Nottoway County", "https://vasheriff.org/va-sheriffs-directory/nottoway-county-robert-l-jones/"),
    rec("Jason C. Smith", "jason-c-smith", "Orange County", "https://vasheriff.org/va-sheriffs-directory/orange-county-jason-c-smith/"),
    rec("Chadwick W. \"Chad\" Cubbage", "chadwick-w-chad-cubbage", "Page County", "https://vasheriff.org/va-sheriffs-directory/page-county-chadwick-w-chad-cubbage/"),
    rec("Daniel M. Smith", "daniel-m-smith", "Patrick County", "https://vasheriff.org/va-sheriffs-directory/patrick-county-daniel-m-smith/"),
    rec("Vanessa R. Crawford", "vanessa-r-crawford", "Petersburg", "https://vasheriff.org/va-sheriffs-directory/petersburg-vanessa-r-crawford/"),
    rec("Michael W. \"Mike\" Taylor", "michael-w-mike-taylor", "Pittsylvania County", "https://vasheriff.org/va-sheriffs-directory/pittsylvania-county-michael-w-mike-taylor/"),
    rec("Michael A. Moore", "michael-a-moore", "Portsmouth", "https://vasheriff.org/va-sheriffs-directory/portsmouth-michael-a-moore/"),
    rec("Brad W. Nunnally Jr.", "brad-w-nunnally", "Powhatan County", "https://vasheriff.org/va-sheriffs-directory/powhatan-county-brad-w-nunnally/"),
    rec("L. A. \"Tony\" Epps", "l-a-tony-epps", "Prince Edward County", "https://vasheriff.org/va-sheriffs-directory/prince-edward-county-l-a-tony-epps/"),
    rec("R. W. \"Buck\" Vargo", "r-w-buck-vargo", "Prince George County", "https://vasheriff.org/va-sheriffs-directory/prince-george-county-r-w-buck-vargo/"),
    rec("Glendell Hill", "glendell-hill", "Prince William County", "https://vasheriff.org/va-sheriffs-directory/prince-william-county-glendell-hill/"),
    rec("Michael W. Worrell", "michael-w-worrell", "Pulaski County", "https://vasheriff.org/va-sheriffs-directory/pulaski-county-michael-w-worrell/"),
    rec("Mark R. Armentrout", "mark-r-armentrout", "Radford", "https://vasheriff.org/va-sheriffs-directory/radford-mark-r-armentrout/"),
    rec("Connie S. Compton", "connie-s-compton", "Rappahannock County", "https://vasheriff.org/va-sheriffs-directory/rappahannock-county-connie-s-compton/"),
    rec("Antionette V. Irving", "antionette-v-irving", "Richmond", "https://vasheriff.org/va-sheriffs-directory/richmond-antionette-v-irving/"),
    rec("Stephan B. Smith", "stephan-b-smith", "Richmond County", "https://vasheriff.org/va-sheriffs-directory/richmond-county-stephan-b-smith/"),
    rec("Antonio D. Hash", "antonio-d-hash", "Roanoke", "https://vasheriff.org/va-sheriffs-directory/roanoke-antonio-d-hash/"),
    rec("J. Eric Orange", "j-eric-orange", "Roanoke County", "https://vasheriff.org/va-sheriffs-directory/roanoke-county-j-eric-orange/"),
    rec("Tony A. McFaddin Jr.", "tony-a-mcfaddin", "Rockbridge County", "https://vasheriff.org/va-sheriffs-directory/rockbridge-county-tony-a-mcfaddin/"),
    rec("Bryan F. Hutcheson", "bryan-f-hutcheson", "Rockingham County", "https://vasheriff.org/va-sheriffs-directory/rockingham-county-bryan-f-hutcheson/"),
    rec("William J. \"Bill\" Watson", "william-j-bill-watson", "Russell County", "https://vasheriff.org/va-sheriffs-directory/russell-county-william-j-bill-watson/"),
    rec("Chris Shelor", "chris-shelor", "Salem", "https://vasheriff.org/va-sheriffs-directory/salem-chris-shelor/"),
    rec("Jeff B. Edds", "jeff-b-edds", "Scott County", "https://vasheriff.org/va-sheriffs-directory/scott-county-jeff-b-edds/"),
    rec("Timothy C. Carter", "timothy-c-carter", "Shenandoah County", "https://vasheriff.org/va-sheriffs-directory/shenandoah-county-timothy-c-carter/"),
    rec("B. C. \"Chip\" Shuler", "b-c-chip-shuler", "Smyth County", "https://vasheriff.org/va-sheriffs-directory/smyth-county-b-c-chip-shuler/"),
    rec("Josh A. Wyche Sr.", "josh-a-wyche", "Southampton County", "https://vasheriff.org/va-sheriffs-directory/southampton-county-josh-a-wyche/"),
    rec("Roger L. Harris", "roger-l-harris", "Spotsylvania County", "https://vasheriff.org/va-sheriffs-directory/spotsylvania-county-roger-l-harris/"),
    rec("David P. \"DP\" Decatur , Jr.", "david-p-dp-decatur", "Stafford County", "https://vasheriff.org/va-sheriffs-directory/stafford-county-david-p-dp-decatur/"),
    rec("Christopher M. Hartless", "christopher-m-hartless", "Staunton", "https://vasheriff.org/va-sheriffs-directory/staunton-christopher-m-hartless/"),
    rec("David Miles", "david-miles", "Suffolk", "https://vasheriff.org/va-sheriffs-directory/suffolk-david-miles/"),
    rec("Carlos Turner", "carlos-turner", "Surry County", "https://vasheriff.org/va-sheriffs-directory/surry-county-carlos-turner/"),
    rec("Ernest L. Giles Sr.", "ernest-l-giles", "Sussex County", "https://vasheriff.org/va-sheriffs-directory/sussex-county-ernest-l-giles/"),
    rec("Brian L. Hieatt", "brian-l-hieatt", "Tazewell County", "https://vasheriff.org/va-sheriffs-directory/tazewell-county-brian-l-hieatt/"),
    rec("Rocky Holcomb", "rocky-holcomb", "Virginia Beach", "https://vasheriff.org/va-sheriffs-directory/virginia-beach-rocky-holcomb/"),
    rec("Crystal M. Cline", "crystal-m-cline", "Warren County", "https://vasheriff.org/va-sheriffs-directory/warren-county-crystal-m-cline/"),
    rec("Blake Andis", "blake-andis", "Washington County", "https://vasheriff.org/va-sheriffs-directory/washington-county-blake-andis/"),
    rec("Christopher Johnson Jr.", "christopher-johnson", "Waynesboro", "https://vasheriff.org/va-sheriffs-directory/waynesboro-christopher-johnson/"),
    rec("C. O. Balderson", "c-o-balderson", "Westmoreland County", "https://vasheriff.org/va-sheriffs-directory/westmoreland-county-c-o-balderson/"),
    rec("David J. Hardin", "david-j-hardin", "Williamsburg-James", "https://vasheriff.org/va-sheriffs-directory/williamsburg-james-david-j-hardin/"),
    rec("William Sales", "william-sales", "Winchester", "https://vasheriff.org/va-sheriffs-directory/winchester-william-sales/"),
    rec("E. Grant Kilgore", "e-grant-kilgore", "Wise County", "https://vasheriff.org/va-sheriffs-directory/wise-county-e-grant-kilgore/"),
    rec("Anthony R. Cline", "anthony-r-cline", "Wythe County", "https://vasheriff.org/va-sheriffs-directory/wythe-county-anthony-r-cline/"),
    rec("Ronald G. Montgomery", "ronald-g-montgomery", "York County-Poquoson", "https://vasheriff.org/va-sheriffs-directory/york-county-poquoson-ronald-g-montgomery/"),
]


def main():
    with open(SCORECARD, encoding="utf-8") as f:
        data = json.load(f)

    by_slug = {c.get("slug"): c for c in data["candidates"] if c.get("state") == "VA"}
    existing = {(c.get("slug"), c.get("state")) for c in data["candidates"]}
    next_id = max(c.get("id", 0) for c in data["candidates"] if isinstance(c.get("id"), int)) + 1
    added, skipped = [], []

    for candidate in NEW:
        slug = candidate["slug"]
        if slug in PROTECTED:
            skipped.append((slug, "protected-middlesex-candidate"))
            continue
        key = (slug, candidate["state"])
        if key in existing:
            cur = by_slug.get(slug)
            if cur and cur.get("office", "").startswith("Sheriff (candidate"):
                skipped.append((slug, "exists-as-candidate"))
            else:
                skipped.append((slug, "exists"))
            continue
        candidate["id"] = next_id
        next_id += 1
        data["candidates"].append(candidate)
        added.append(slug)
        print(f"  ADD: {candidate['name']} ({slug})")

    data.setdefault("meta", {})
    data["meta"]["total_candidates"] = len(data["candidates"])
    data["meta"]["last_updated"] = "2026-09-04"

    with open(SCORECARD, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nAdded {len(added)} sitting VA sheriff(s). Total candidates: {len(data['candidates'])}")
    if skipped:
        print(f"Skipped {len(skipped)}:")
        for s, why in skipped:
            print(f"  {s}: {why}")

    subprocess.run([sys.executable, str(BASE / "build-data.py"), "--quiet"], check=True)


if __name__ == "__main__":
    main()
