---
name: israeli-citizenship-by-descent
description: "Help an Israeli check whether they can claim a European passport by descent or Nazi-era restitution and build the do-it-yourself application path from Israel. Use when someone says a parent, grandparent, or great-grandparent came from Europe and they want to know if a passport is realistic and how to file it without paying an agency. Covers the German and Austrian restitution routes, citizenship by descent for Poland, Romania, Hungary and smaller routes, and the Israeli-side document pipeline (population-registry extract, apostille, certified translation). Explains why getting the route and the document chain right is what decides approval. Do NOT use for immigrating to Israel, work or relocation visas, wills and inheritance, or as a substitute for a licensed immigration lawyer on a complex or contested case."
license: MIT
---

# European Passport by Descent Navigator

## Problem

Hundreds of thousands of Israelis are descended from Europeans who fled, were expelled, or were stripped of their citizenship, which can make them eligible for an EU passport today. But the rules differ by country, change often, and turn on small lineage and document details, so most people either assume they do not qualify or pay a private agency thousands of shekels to find out. The hard part is rarely the foreign form: it is figuring out which route fits the family story and assembling the exact chain of Israeli and ancestral documents, apostilles, and translations each authority demands.

## Instructions

You are helping an Israeli triage their eligibility for a foreign (mostly EU) citizenship by descent or restitution, then handing them a realistic do-it-yourself roadmap. You are NOT giving binding legal advice and NOT filing anything for them. Be honest about uncertainty: these laws change, and a wrong assumption about a single ancestor can flip eligibility.

Work through these stages, adapting to what the user already knows rather than forcing every question:

### Step 1: Map the ancestry (intake)

Establish the family chain before discussing any country. Ask for:
- Which ancestor is the anchor (parent, grandparent, great-grandparent) and their country/region of origin.
- What happened to them and when: emigration, flight, persecution, loss or denial of citizenship, and the rough dates.
- Whether documents survive (the ancestor's birth/marriage records, naturalization or emigration papers, an old passport, Yad Vashem or archive references).
- The unbroken line from the anchor to the user (each birth, marriage, name change).

The script in `scripts/eligibility_intake.py` produces a structured worksheet to capture this.

### Step 2: Triage which routes are worth pursuing

Match the family story to candidate routes using the country table below. A single family can qualify under more than one (for example a German restitution route AND a Polish confirmation). Surface all plausible routes, then rank them by feasibility for someone living in Israel (restitution routes with no residency or language requirement rank highest; routes needing in-country residence or a language exam rank lowest).

### Step 3: Per-country deep dive

For the routes that survive triage, lay out the specific legal basis, who in the chain must have held the citizenship, the generational reach, and any language or residency catch. Always pair a specific claim with "confirm the current terms with the consulate or a lawyer," because these rules shift.

### Step 4: Build the Israeli document pipeline

This is the part agencies charge the most for and where most DIY applications stall. Walk the user through obtaining Israeli civil documents (especially the population-registry extract), the correct apostille authority for each document type, and certified/sworn translation. See the "Israeli document pipeline" section.

### Step 5: Filing roadmap

Tell the user where the application is actually filed (the relevant consulate in Israel or the home-country authority), the realistic order of operations, and that timelines for restitution and descent cases are typically measured in many months to years. Do not invent a specific processing time for a given consulate; direct them to the consulate's current published estimate.

### Step 6: Set expectations and route out

Close with the dual-citizenship implications for Israelis (below) and a clear handoff: for a contested lineage, a broken chain, or a high-value decision, recommend a licensed immigration lawyer or the consulate. State the legal facts plainly, but do not tell the user they can skip professional help on a complex case.

## Country routes

Ranked roughly by relevance to Israelis. Treat every specific as "verify current terms" - restitution and descent law changes frequently.

### Tier 1: Nazi-era restitution (uniquely relevant to Jewish families)

| Route | Who qualifies | Key points |
|-------|---------------|------------|
| Germany - Art. 116(2) Basic Law | People the Nazis stripped of German citizenship between 1933 and 1945 on political, racial, or religious grounds, and their descendants | Restoration, not ordinary naturalization. No language or residency requirement. Source: bva.bund.de |
| Germany - §15 StAG | Persecuted persons who lost or were denied/never able to acquire German citizenship, plus descendants. In force since 2021 | Closes gaps Art. 116(2) does not cover. Many Israeli families fit here, not under Art. 116(2) |
| Germany - §5 StAG declaration | Descendants excluded by old gender-discriminatory descent rules (for example descent through a German mother before 1975, or a child of a German father born out of wedlock before 1993) | A faster declaration route created in 2021 (a ten-year window). Check whether the family situation fits before defaulting to §15 |
| Austria - §58c | Direct descendants (children, grandchildren, great-grandchildren) of victims of Nazi/Austrofascist persecution | Acquired by filing a declaration at the Austrian representation where you live, so no residence in Austria is required. Covers ancestors persecuted between 1933 and 1945, or who emigrated with a main residence in Austria before 15 May 1955. Israel allows dual citizenship, so claiming Austrian citizenship does not cost you the Israeli one. Source: bmeia.gv.at |

Germany note on dual citizenship: the restitution routes did not require giving up another citizenship even before Germany's broader reform. Since 27 June 2024 Germany generally permits multiple nationality, so acquiring German citizenship no longer threatens the Israeli one. Do not tell a restitution applicant they must renounce.

### Tier 2: Citizenship by descent (large Israeli ancestry base)

| Route | Who qualifies | Key catch |
|-------|---------------|-----------|
| Poland | Descendants in an unbroken bloodline from a Polish citizen (jus sanguinis) | Usually a confirmation of citizenship you already hold, not a new grant. The chain commonly breaks for Israeli families: before 1951 a Polish man who served in a foreign army or acquired Mandatory-Palestine or Israeli citizenship lost his Polish citizenship, and citizenship passed through the father. If the chain is broken, ask about the restoration route (przywrocenie) for involuntary loss |
| Romania | Former Romanian citizens who lost citizenship and their descendants (children and grandchildren; some practitioners cite up to great-grandchildren - confirm) | Prefer the restoration route (Art. 11, Law 21/1991, no residency) over Art. 10 (re-acquisition, which can require residency). Most eligible Israeli families trace to the interwar territories (Bessarabia, Bukovina) of 1918-1940. Romania permits dual citizenship. A 2025 amendment may add language/documentation steps - confirm current terms |
| Hungary | Descendants of a Hungarian citizen (pre-1920 Kingdom of Hungary, or 1941-1945) | Simplified naturalization, but Hungarian-language ability is checked at the consular interview. This stops most descendants who do not speak Hungarian |

### Tier 3: Smaller descent routes

| Route | Who qualifies | Status |
|-------|---------------|--------|
| Czech | Children and grandchildren of a former Czech/Czechoslovak citizen, by declaration (not open to current Slovak citizens) | The ancestor must have lost citizenship by 31 December 2013. Source: mzv.gov.cz |
| Lithuania | Descendants of citizens of interwar (pre-1940) Lithuania | Those whose ancestor left before Lithuania restored independence on 11 March 1990 may keep their other citizenship (a dual exception). Holocaust-era document gaps are the practical hurdle |
| Bulgaria / Greece / Slovakia | Descent through parent/grandparent (and sometimes great-grandparent) | Routes exist; generational reach and procedure vary. Confirm the current statute with the consulate before relying on them |

### Tier 4: Restricted, closed, or low-relevance

| Route | Status |
|-------|--------|
| Portugal - Sephardic origin | Heavily restricted. Following the 2024 amendment, new applicants must show three years of legal residence in Portugal before applying, on top of a Jewish-community certificate. For nearly all Israel-based applicants this route is now impractical |
| Spain - Sephardic origin | Closed to new applicants. The Law 12/2015 window ended on 1 October 2019. Sephardic Israelis now use ordinary residency-based naturalization instead |
| Cyprus | Descent only, through a Cypriot parent (a grandparent alone is generally not enough). The citizenship-by-investment "golden passport" was suspended on 1 November 2020. Low relevance for most Israelis |

Other descent routes exist (for example Italy, Latvia, Estonia). If the family origin is not in the tables above, check that country's consulate; the same document logic below still applies. Treat any specific rule as "confirm current terms" - these change often.

## Israeli document pipeline

The foreign authority will want a documented, translated, apostilled chain from the anchor ancestor to the applicant. This is where most DIY files stall.

**Start with the ancestor's foreign record.** The linchpin, and usually the hardest document, is proof of the ancestor's foreign birth, citizenship, or persecution, not the Israeli paperwork. Obtain it from the country-of-origin civil registry or state archives, and for Nazi-era cases from the Arolsen Archives, Yad Vashem, the Central Archives for the History of the Jewish People, or JewishGen. Without this record the rest of the chain is moot, so chase it first.

Then assemble the Israeli side:

1. **Population-registry extract (tamtzit rishum).** The most useful Israeli document for proving lineage, because it lists parents' names, dates of birth, and status. Israeli citizens and residents can request a standard or extended Population Registry extract from the Population and Immigration Authority (gov.il). It is in Hebrew with Hebrew-calendar dates (convert to Gregorian) and may not show the ancestor's foreign birthplace, so it supplements but rarely replaces the foreign record.
2. **Civil certificates.** Birth, marriage, and death certificates for each link in the chain, as the destination authority specifies.
3. **Apostille - use the correct authority for each document type.** Do NOT assume everything goes through one office. In Israel, public documents issued by Israeli courts and signatures on notarized documents are apostilled through the courts / Ministry of Justice channel, while other public documents issued by state bodies are verified by the Ministry of Foreign Affairs. A notarized translation and the original public certificate may need apostilles from different authorities. Check the current routing on gov.il.
4. **Certified / sworn translation.** Israel uses notarial translations (a notary attests the translation). Some destinations require a sworn or court-registered translator in that country, in which case an Israeli notarial translation may be rejected. The translation itself often needs its own apostille. Confirm the destination's exact translation rule before paying for translations.
5. **Name transliteration.** Hebrew has no single Latin spelling standard, so an ancestor's name often appears differently across generations and documents. This is a top cause of stalled files. Pre-empt it with a notarized same-person / name-equivalence affidavit when spellings differ.

## Dual-citizenship implications for an Israeli

Surface these before the user commits, because people routinely misunderstand them:
- **IDF service is unaffected.** A second passport does not reduce Israeli military-service obligations. Anyone unsure of their status should get it determined through the Israeli authorities.
- **Israeli tax does not change.** Israeli tax residency is based on where your life is centred, not which passport you carry. A foreign passport does not, by itself, remove Israeli worldwide-income exposure.
- **Border rule.** Israeli citizens must enter and leave Israel on an Israeli passport. An Israeli flying back into Israel on a foreign passport must present their Israeli passport (even if expired) or an ETA approval. Source: gov.il.

## Bundled Resources

- `references/domain-checklist.md` - the full coverage checklist (every route, the Israeli pipeline, and the authoritative sources behind each claim).
- `scripts/eligibility_intake.py` - generates a structured ancestry-and-documents worksheet to run the Step 1 intake and produce a starting document checklist.

## Gotchas

These are mistakes an AI agent makes in this domain if not warned:
- **Treating Germany and Austria as ordinary naturalization.** They are restitution routes with their own sections (Art. 116(2), §15, §5; §58c). Restitution applicants do not face the renunciation, language, or residency hurdles of standard naturalization. Defaulting to "you must live there / pass a language test / give up Israeli citizenship" is wrong for these routes.
- **Assuming a clean bloodline equals eligibility for Poland.** Polish cases turn on the unbroken chain. Probe specifically for pre-1951 foreign military service and for acquisition of Mandatory-Palestine or Israeli citizenship, both of which broke Polish citizenship, and raise the restoration route (przywrocenie) when the chain is broken instead of treating it as a dead end.
- **Sending a non-German-origin family down the German route.** German restitution (Art. 116(2), §15) requires the ancestor to have held German citizenship and lost it. A Polish, Hungarian, or Romanian Jew persecuted by the Nazis does NOT qualify for a German passport on that basis; match them to their own country's route. The same nexus rule applies to Austria, where §58c needs an Austrian-citizen or Austrian-resident persecuted ancestor.
- **Citing a single processing time or fee.** Consular timelines and fees change constantly and differ per consulate. Route the user to the consulate's current figure instead of stating one.
- **Saying "just apostille it at the Foreign Ministry."** Israel splits apostille authority by document type; notarized/translated documents and court documents go through the courts / Justice channel, not the MFA. Sending everything to the MFA gets documents bounced.
- **Presenting Portugal or Spain as open Sephardic shortcuts.** The Spanish window closed in 2019 and Portugal's route now requires Portuguese residence. Repeating the old "easy Sephardic passport" framing sends users down a dead end.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Germany BVA - Art. 116(2) and §15 | https://www.bva.bund.de/EN/Services/Citizens/ID-Documents-Law/Citizenship/116GG_15StA.html | Restitution eligibility and the difference between the two routes |
| Germany - §5 declaration route | https://www.germany.info/us-en/service/03-citizenship/2479488-2479488 | The declaration right for gender-discrimination descent gaps |
| Germany Federal Foreign Office - 2024 dual citizenship | https://www.auswaertiges-amt.de/en/2664476-2664476 | That multiple nationality is allowed since 27 June 2024 |
| Austria §58c (BMEIA) | https://www.bmeia.gv.at/en/consular-section-of-the-austrian-embassy-in-washington/service-for-citizens/citizenship-for-persecuted-persons-and-their-direct-descendants/declaration-pursuant-to-58c-of-the-austrian-citizenship-act | The declaration procedure and the pre-15-May-1955 residence condition |
| Poland - confirmation of citizenship | https://www.gov.pl/web/usa-en/confirming-polish-citizenship-or-its-loss | That descent is a confirmation, not a new grant |
| Hungary - simplified naturalization (Tel Aviv) | https://telaviv.mfa.gov.hu/en/egyszerusitett-honositas | The Hungarian-language check at the interview |
| Czech - children and grandchildren by declaration | https://mzv.gov.cz/losangeles/en/consular_information/czech_citizenship_and_vital_records/children_and_grandchildren_of_former.html | Generational reach and the 31 December 2013 loss date |
| Portugal - Sephardic route (current status) | https://www.globalcitizensolutions.com/portuguese-citizenship-sephardic-jews/ | The post-2024 three-year residence requirement |
| Israel - apostille authorities | https://www.gov.il/en/service/apostille-approval-for-countries | Which Israeli body apostilles which document type |
| Israel - population-registry extract | https://www.gov.il/en/service/summaryinfofromthepopulationregistrylisting | How to order the tamtzit rishum used to prove lineage |
| Israel - foreign-passport border rule | https://www.gov.il/en/pages/news-exit-foriegn-passport-2025 | The requirement to present an Israeli passport or ETA on return |

## Troubleshooting

- **"My grandparent emigrated before WWII, do I still qualify for Germany?"** Only if the ancestor actually held German citizenship and was stripped of it (Art. 116(2) or §15). A grandparent who was, for example, a Polish or Hungarian Jew persecuted by the Nazis does NOT get German citizenship this way; match them to their country of citizenship instead. Where there was a German citizenship loss, its timing matters more than the emigration date. Map the loss event, then confirm with the German mission.
- **"The family name is spelled three different ways across the documents."** Expected. Gather all variants and prepare a notarized same-person affidavit; do not assume the mismatch disqualifies the claim.
- **"An agency quoted me thousands of shekels."** Agencies mostly assemble and translate the document chain, which a motivated applicant can do themselves. Use the Israeli document pipeline above; reserve a lawyer for a genuinely contested lineage or a broken chain.
- **"Which country should I pick if I qualify for several?"** Rank by feasibility from Israel: restitution routes with no residence/language requirement first, language-exam or in-country-residence routes last. Then weigh processing time and the documents you can actually obtain.
