---
name: israeli-citizenship-by-descent
description: "Help an Israeli check whether they can claim a European passport by descent or Nazi-era restitution and build the do-it-yourself application path from Israel. Use when someone says a parent, grandparent, or great-grandparent came from Europe and they want to know if a passport is realistic and how to file it without paying an agency. Covers the German and Austrian restitution routes, citizenship by descent for Italy, Poland, Romania, Hungary and smaller routes, which routes have closed, and the Israeli-side document pipeline (population-registry extract, apostille, certified translation). Explains why getting the route and the document chain right is what decides approval. Do NOT use for immigrating to Israel, work or relocation visas, wills and inheritance, or as a substitute for a licensed immigration lawyer on a complex or contested case."
license: MIT
---

# European Passport by Descent Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the rules and calculates from the figures you enter, but it does not examine your full circumstances and does not constitute legal advice. All of its outputs are produced automatically, with no involvement, review, or approval by an advocate, and an AI model may err, omit data, or present a wrong conclusion. Actual entitlement depends on the circumstances and the documents, so consult an advocate for a binding answer. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person, and all use of its output is the user's sole responsibility.


## Problem

Hundreds of thousands of Israelis are descended from Europeans who fled, were expelled, or were stripped of their citizenship, which can make them eligible for an EU passport today. But the rules differ by country, change often, and turn on small lineage and document details, so most people either assume they do not qualify or pay a private agency thousands of shekels to find out. The hard part is rarely the foreign form: it is figuring out which route fits the family story, checking that the route is still open, and assembling the exact chain of Israeli and ancestral documents, apostilles, and translations each authority demands.

## Instructions

You are helping an Israeli triage their eligibility for a foreign (mostly EU) citizenship by descent or restitution, then handing them a realistic do-it-yourself roadmap. You are NOT giving binding legal advice and NOT filing anything for them. Be honest about uncertainty: these laws change, and a wrong assumption about a single ancestor can flip eligibility.

**Check the route status before anything else.** Two of the routes people ask about most (Portugal and Spain) are closed by statute, and Italy was closed retroactively in 2025. Sending someone to gather archive records and pay for translations on a dead route costs them real money. Every table below carries a Status column and the whole file carries a verification date. If a specific is older than a few months, say so and route the user to the primary source.

Work through these stages, adapting to what the user already knows rather than forcing every question:

### Step 1: Map the ancestry (intake)

Establish the family chain before discussing any country. Ask for:
- Which ancestor is the anchor (parent, grandparent, great-grandparent) and their country/region of origin.
- What happened to them and when: emigration, flight, persecution, loss or denial of citizenship, and the rough dates.
- Whether documents survive (the ancestor's birth/marriage records, naturalization or emigration papers, an old passport, Yad Vashem or archive references).
- The unbroken line from the anchor to the user (each birth, marriage, name change).
- Whether anyone in the family already filed, booked a consular appointment, or opened a court case, and on what date. For Italy this single fact decides the case.

The script in `scripts/eligibility_intake.py` produces a structured worksheet to capture this.

### Step 2: Triage which routes are worth pursuing

Match the family story to candidate routes using the country tables below. A single family can qualify under more than one (for example a German restitution route AND a Polish confirmation). Drop anything marked Closed immediately and say why. Then rank the survivors by feasibility for someone living in Israel: restitution routes with no residency and no language test rank highest, routes with a certified language exam or in-country residence rank lowest.

### Step 3: Per-country deep dive

For the routes that survive triage, lay out the specific legal basis, who in the chain must have held the citizenship, the generational reach, and any language or residency catch. Always pair a specific claim with "confirm the current terms with the consulate or a lawyer," because these rules shift.

### Step 4: Build the Israeli document pipeline

This is the part agencies charge the most for and where most DIY applications stall. Walk the user through obtaining Israeli civil documents (especially the population-registry extract), the correct apostille authority for each document type, and certified/sworn translation. See the "Israeli document pipeline" section.

### Step 5: Filing roadmap

Tell the user where the application is actually filed (the relevant consulate in Israel or the home-country authority), the realistic order of operations, and that timelines for restitution and descent cases are typically measured in many months to years. Do not invent a specific processing time for a given consulate; direct them to the consulate's current published estimate.

### Step 6: Set expectations and route out

Close with the dual-citizenship implications for Israelis (below) and a clear handoff: for a contested lineage, a broken chain, or a high-value decision, recommend a licensed immigration lawyer or the consulate. State the legal facts plainly, but do not tell the user they can skip professional help on a complex case.

## Country routes

**Verified as of 9 August 2026.** Status values: Open (route accepts new applicants from Israel), Restricted (open but with a hard gate such as a certified language exam or residence), Closed (repealed or the filing window has expired). Treat every specific as "verify current terms."

### Tier 1: Nazi-era restitution (uniquely relevant to Jewish families)

| Route | Status | Who qualifies | Key points |
|-------|--------|---------------|------------|
| Germany, Art. 116(2) Basic Law | Open | People the Nazis stripped of German citizenship between 1933 and 1945 on political, racial, or religious grounds, and their descendants | Restoration, not ordinary naturalization. No language or residency requirement. Source: bva.bund.de |
| Germany, §15 StAG | Open | Persons who lost or were denied German citizenship in connection with persecution between 30 January 1933 and 8 May 1945, plus their descendants | Closes gaps Art. 116(2) does not cover. Many Israeli families fit here, not under Art. 116(2). Entitlement to naturalization since 20 August 2021 |
| Germany, §5 StAG declaration | Open, with a deadline | Children of a German parent excluded by old gender-discriminatory descent rules, children who lost citizenship by legitimation, and the descendants of those children | The declaration right can only be exercised within ten years of the law entering into force (§5(3) StAG). The law entered into force on 20 August 2021, so the window runs out in August 2031. Print the deadline for the user, do not just say "a ten-year window" |
| Austria, §58c | Open | Direct descendants in the descending line of a persecuted Austrian citizen or Austrian resident. The statute says "Nachkomme in direkter absteigender Linie" with no generation cap, so great-grandchildren and beyond are covered | Acquired by filing a written declaration with the Austrian representation where you live, so no residence in Austria is needed. Covers ancestors who left with a main residence in Austria before 15 May 1955, or who had no main residence in Austria between 30 January 1933 and 9 May 1945 because of Nazi persecution. No renunciation of Israeli citizenship |

Germany, dual citizenship: the restitution routes never required giving up another citizenship, and since 27 June 2024 Germany generally permits multiple nationality. Do not tell a restitution applicant they must renounce. Two other changes are worth knowing so you do not repeat stale advice: §12 StAG (the old renunciation rules) now reads "(weggefallen)", and §10(3) StAG (the three-year fast-track for integration achievements) also reads "(weggefallen)". Secondary reporting that says the fast-track survives for special integration achievements is contradicted by the consolidated statute text.

### Tier 2: Citizenship by descent (large Israeli ancestry base)

| Route | Status | Who qualifies | Key catch |
|-------|--------|---------------|-----------|
| Italy | Closed for most, retroactively | Only someone who fits one of the saving conditions in Art. 3-bis of Law 91/1992 | Since DL 36/2025 (converted by Legge 23 maggio 2025 n. 74), a person born abroad who holds another citizenship "e' considerato non avere mai acquistato la cittadinanza italiana", expressly including births before the article entered into force. The saving conditions are: (a) a consular or comune application filed by 23:59 Rome time on 27 March 2025; (a-bis) an appointment for that filing communicated to the applicant by that same instant, which rescues people holding a Prenot@mi slot; (b) a judicial claim filed by that instant; (c) a first- or second-degree ascendant who holds, or held at death, EXCLUSIVELY Italian citizenship; (d) a parent or adopter resident in Italy for at least two continuous years after acquiring Italian citizenship and before the child's birth. Letter (e) was suppressed on conversion |
| Poland | Open | Descendants in an unbroken line of descent from a Polish citizen | This is a confirmation of citizenship you already hold, not a new grant, decided by the wojewoda. The chain commonly breaks for Israeli families: before 1951 a Polish man who served in a foreign army or acquired Mandatory-Palestine or Israeli citizenship lost his Polish citizenship, and citizenship passed through the father. A broken chain is generally fatal to a descendant's claim and has to be argued on the facts |
| Romania | Restricted, hard language gate | Former Romanian citizens who lost citizenship through no fault of their own, and their descendants to the third degree (child, grandchild, great-grandchild) | Prefer restoration under Art. 11 of Law 21/1991 (no residency) over Art. 10. But Legea 14/2025 added a Romanian-language condition: "Acordarea cetateniei romane in temeiul art. 10 si 11 este conditionata de cunoasterea de catre solicitant a limbii romane", proved by a B1 CEFR certificate from a closed list of issuers (accredited Romanian universities running the "An pregatitor de limba romana" programme, Institutul Limbii Romane, Institutul Cultural Roman and Romanian cultural institutes abroad) or a legalized transcript of at least three years of study in Romanian. The exemption covers only people who were themselves Romanian citizens and people aged 65 or over. A descendant who was never personally Romanian gets NO exemption. The filing window for the certificate has been changed by emergency ordinance more than once, so check the current deadline on the ANC announcements page before you rely on any date, and treat a missed deadline as fatal to the file |
| Hungary | Restricted, conversational language check | Descendants of a Hungarian citizen | Simplified naturalization, but Hungarian-language ability is checked by the body receiving the application at the consular interview. This stops most descendants who do not speak Hungarian. Note this is a consular conversation, not a certified exam, so it is a lower bar than Romania's B1 certificate |

**Feasibility note.** Romania used to be the easy no-residency, no-language route and Hungary the harder one. Since Legea 14/2025 that is reversed: Romania now demands a certified B1 exam from a short list of institutions, which is a harder and slower gate than Hungary's consular conversation. Rank accordingly, and do not repeat the old ordering.

**Two Italian traps to state explicitly.** First, the test in letter (c) is "exclusively Italian", not the popular press framing "a parent or grandparent born in Italy". Those are different tests and most families fail the real one, because the ancestor naturalized somewhere. Second, the rule is retroactive, so a great-grandparent line that a lawyer priced as viable in 2024 is now almost certainly out unless a filing, appointment, or court case predates 27 March 2025.

### Tier 3: Smaller descent and restitution routes

| Route | Status | Who qualifies | Key points |
|-------|--------|---------------|------------|
| Czechia | Open | Children and grandchildren of a former Czech or Czechoslovak citizen, by declaration, not open to current Slovak citizens | The ancestor must have lost citizenship by 31 December 2013. Confirm generational reach and current fees with the Czech mission |
| Latvia | Open, narrow | Someone who was a Latvian citizen on 17 June 1940, or a descendant, where that person left Latvia between 17 June 1940 and 4 May 1990 escaping the U.S.S.R. or German occupation regime or was deported, and did not return for permanent residence by 4 May 1990 | Section 8.1 of the Citizenship Law. Critical for Israelis: paragraph (3) says dual citizenship may occur for these registrants, which matters because Israel is not on Latvia's general dual-citizenship list in Section 9. Trap: paragraph (2) covers descendants born until 1 October 2014. An application is examined within four months. A family that emigrated before 1940 is outside Section 8.1 |
| Greece, Holocaust-victim restoration | Open, but the victim only | Living persons of Jewish descent, citizens of Israel or another country, born up to 9 May 1945, who previously held Greek citizenship from birth and lost it for any reason | A dedicated restoration procedure, filed in person at the Greek consulate for the place of residence, decided by the Minister of the Interior and published in the government gazette. Highly relevant to Salonika families. Note carefully: as published this is for the former citizen personally, not for descendants, so an Israeli grandchild cannot use it |
| Lithuania | Verify before relying on it | Descendants of interwar Lithuanian citizens | Reinstatement exists, and Holocaust-era document gaps are the practical hurdle. Generational reach and the dual-citizenship exception change; confirm the current statute with the Lithuanian Migration Department before the user spends money |
| Bulgaria, Slovakia | Verify before relying on it | Descent through a parent or grandparent, sometimes further | Routes exist but the procedure and generational reach vary, and Bulgaria's is a discretionary facilitated naturalization rather than an entitlement. Confirm with the consulate |

### Tier 4: Closed

| Route | Status | What happened |
|-------|--------|---------------|
| Portugal, Sephardic origin | Closed | REPEALED, not merely restricted. Lei Organica n.o 1/2026, de 18 de maio, art. 5.o: "Sao revogados os n.os 5, 7 e 13 do artigo 6.o ... da Lei n.o 37/81". Art. 6(7) was the Sephardic provision, and the republished text now reads "7 - [Revogado.]". The law entered into force the day after publication, so 19 May 2026. Art. 7.o(2) preserves administrative procedures already pending on that date, which are still decided under the old wording, so someone mid-process is not automatically lost. The same law also raised general naturalization residency to seven years for nationals of Portuguese-speaking countries and EU citizens and ten years for everyone else, and added a Portuguese language, culture, history and national symbols test |
| Spain, Sephardic origin | Closed | Ley 12/2015 gave a filing window of three years from entry into force, extendable by one year by the Council of Ministers. It was extended and it expired on 1 October 2019. What survives is ordinary residency-based naturalization, which requires real residence in Spain plus the Spanish exams. That is not a claim an Israeli can file from Israel, and users routinely conflate the two |
| Cyprus, citizenship by investment | Closed | The "golden passport" citizenship-by-investment programme is no longer a route; confirm its exact status and date with the Cypriot authorities before citing one. Descent through a Cypriot parent still exists, and a grandchild may be able to register on an unbroken line of descent, so do not state flatly that a grandparent is never enough. Confirm with the Cypriot authorities |

If the family origin is not in the tables above, check that country's consulate; the same document logic below still applies.

## Israeli document pipeline

The foreign authority will want a documented, translated, apostilled chain from the anchor ancestor to the applicant. This is where most DIY files stall.

**Start with the ancestor's foreign record.** The linchpin, and usually the hardest document, is proof of the ancestor's foreign birth, citizenship, or persecution, not the Israeli paperwork. Obtain it from the country-of-origin civil registry or state archives, and for Nazi-era cases from the Arolsen Archives, Yad Vashem, the Central Archives for the History of the Jewish People, or JewishGen. Without this record the rest of the chain is moot, so chase it first.

**When the records were destroyed.** War, border changes, and archive fires mean the primary record often does not exist. This is common, not disqualifying, and the remedy is secondary evidence assembled deliberately: a negative certificate from the archive or registry stating the record was searched for and not found, Yad Vashem Pages of Testimony, community and burial registers, ship manifests and immigration files, school or army records, sworn witness affidavits from surviving relatives, and where the destination allows it a reconstructed civil-status record obtained through that country's courts. Ask the archive for the negative certificate in writing before anything else, because most authorities will not consider secondary evidence until you can show the primary record is gone.

Then assemble the Israeli side:

1. **Population-registry extract (tamtzit rishum).** Useful for proving lineage, but do not oversell it. Under the Population and Immigration Authority procedure 2.17.0001, the standard extract carries the subject's own registry details (identity number, sex, nationality, personal status, country and locality of birth, date of birth, current address, date of entry to Israel) and, for the parents, their NAMES only. The parental date-of-birth and place-of-birth fields people expect are not there; those fields are the subject's own. The extended extract adds previous addresses and previous names, personal-status date, spouse's name, children's names, dates of birth and sex, religion, mailing addresses, the date the person became a resident, and a digital address. Still no parental date or place of birth. It is in Hebrew with Hebrew-calendar dates, so convert to Gregorian. Treat it as one link in the chain, never as a substitute for the foreign record.
2. **Civil certificates.** Birth, marriage, and death certificates for each link in the chain, as the destination authority specifies.
3. **Apostille, use the correct authority for each document type.** Do NOT assume everything goes through one office. In Israel, public documents issued by Israeli courts and signatures on notarized documents are apostilled through the courts / Ministry of Justice channel, while other public documents issued by state bodies are verified by the Ministry of Foreign Affairs. A notarized translation and the original public certificate may need apostilles from different authorities. Check the current routing on gov.il.
4. **Certified / sworn translation.** Israel uses notarial translations (a notary attests the translation). Some destinations require a sworn or court-registered translator in that country, in which case an Israeli notarial translation may be rejected. The translation itself often needs its own apostille. Confirm the destination's exact translation rule before paying for translations.
5. **Name transliteration.** Hebrew has no single Latin spelling standard, and Yiddish, Polish, Romanian, Hungarian and German registrars each spelled the same name their own way, so an ancestor appears as Rywka / Rivka / Rebeka across three documents and a patronymic drifts into a surname. This is the single most common reason a DIY file stalls. Work it deliberately: build a variants table listing every spelling with the document it came from and the language of that registrar; do not "correct" any of them on the copies you file. Prepare a notarized same-person (name-equivalence) affidavit covering every variant, sworn by the applicant and where possible by an older relative, and have it translated and apostilled like any other document. Where an Israeli name change is in the chain, order the registry record of the change rather than describing it. Ask the receiving consulate whether it wants the affidavit or a court declaration, because some authorities accept only the latter.

## Dual-citizenship implications for an Israeli

Surface these before the user commits, because people routinely misunderstand them:
- **IDF service is unaffected.** A second passport does not reduce Israeli military-service obligations. Anyone unsure of their status should get it determined through the Israeli authorities.
- **Israeli tax does not change.** Israeli tax residency is based on where your life is centred, not which passport you carry. A foreign passport does not, by itself, remove Israeli worldwide-income exposure.
- **Border rule, currently suspended.** The statutory duty for an Israeli citizen to enter and leave Israel on an Israeli passport is suspended, not repealed. The Population and Immigration Authority announced on 17 February 2026 that it decided "להאריך את האפשרות לישראלים להיכנס ולצאת מישראל עם דרכון זר בתוקף עד ל-30.09.2026". Verify this date has not moved again before relying on it: the concession has been extended more than once, and it is scheduled to lapse.
- **The expired-passport / ETA point is an airline check-in rule, not a border rule.** The same announcement says an Israeli citizen who left on a foreign passport will be asked, when checking in for the flight back to Israel with that foreign passport, to present the Israeli passport (even if expired) or an ETA approval. Do not describe this as something the border officer demands on arrival.

## Bundled Resources

- `references/domain-checklist.md` - the full coverage checklist (every route, the Israeli pipeline, and the authoritative sources behind each claim).
- `scripts/eligibility_intake.py` - generates a structured ancestry-and-documents worksheet to run the Step 1 intake and produce a starting document checklist.

## Gotchas

These are mistakes an AI agent makes in this domain if not warned:
- **Presenting Portugal's Sephardic route as merely restricted.** It is repealed. The 2024-era advice that it "now needs three years of residence in Portugal" is obsolete and describes an interim state, not the law. Say repealed, cite Lei Organica n.o 1/2026, and mention that only procedures already pending on 19 May 2026 continue under the old text.
- **Telling an Italian-descent family the old rule.** Do not say "a parent or grandparent born in Italy is enough". Since 2025 the default is that a person born abroad with another citizenship is treated as never having acquired Italian citizenship, retroactively. Check the four saving conditions, and always ask whether a filing, a booked appointment, or a court case predates 27 March 2025, because that is usually the whole case.
- **Recommending Romania as the easy no-language route.** It has a certified B1 requirement from a closed list of issuers, and descendants who were never Romanian citizens are not exempt. Rank it below Hungary, not above.
- **Routing a descendant to Poland's przywrocenie.** Restoration (przywrocenie) is available only to the person who PERSONALLY held Polish citizenship and lost it before 1 January 1999, and it is decided by the Minister of Interior. A descendant cannot use it, and the ancestor is usually deceased. Descendants only ever have confirmation (potwierdzenie), decided by the wojewoda. A broken chain must be argued on the facts, not routed around.
- **Treating Germany and Austria as ordinary naturalization.** They are restitution routes with their own sections (Art. 116(2), §15, §5; §58c). Restitution applicants do not face the renunciation, language, or residency hurdles of standard naturalization.
- **Sending a non-German-origin family down the German route.** German restitution requires the ancestor to have held German citizenship and lost it. A Polish, Hungarian, or Romanian Jew persecuted by the Nazis does NOT qualify for a German passport on that basis; match them to their own country's route. The same nexus rule applies to Austria.
- **Citing a single processing time or fee.** Consular timelines and fees change constantly and differ per consulate. Route the user to the consulate's current figure instead of stating one.
- **Saying "just apostille it at the Foreign Ministry."** Israel splits apostille authority by document type; notarized/translated documents and court documents go through the courts / Justice channel, not the MFA.
- **Promising the tamtzit rishum contains a parent's date or place of birth.** It does not. Check the procedure before telling a user which fields they will get.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Portugal, Lei Organica n.o 1/2026 | https://files.diariodarepublica.pt/1s/2026/05/09500/0000200020.pdf | Art. 5.o repeal of art. 6(7), art. 7.o(2) on pending procedures, art. 8.o entry into force |
| Italy, DL 36/2025 coordinated with Legge 74/2025 | https://www.gazzettaufficiale.it/eli/id/2025/05/23/25A03081/sg | The text of Art. 3-bis and its saving conditions (a), (a-bis), (b), (c), (d) |
| Italy, Law 91/1992 consolidated | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1992-02-05;91 | Where Art. 3-bis sits in the current citizenship law |
| Romania, Art. 11 route and document list | https://www.econsulat.ro/AcordareCetatenie/DescriereServiciu/101000005 | The Art. 11 restoration service on the official MAE consular portal: who it covers, descendants up to the third degree, and the required documents |
| Romania, B1 filing deadline | https://cetatenie.just.ro/category/anunturi/ | The current deadline for filing the language certificate, and who is exempt |
| Romania, accepted language certificates | https://cetatenie.just.ro/comunicat-privind-certificatele-de-competenta-lingvistica-acceptate-in-dosarele-de-cetatenie/ | The closed list of institutions whose certificates ANC accepts |
| Poland, restoration (przywrocenie) | https://www.gov.pl/web/mswia/odzyskaj-utracone-obywatelstwo-polskie | That it is only for a person who personally lost citizenship before 1 January 1999 |
| Poland, confirmation (potwierdzenie) | https://www.gov.pl/web/mswia/potwierdzenie-posiadania-lub-utraty-obywatelstwa-polskiego | The descendant's actual route, filed with the wojewoda |
| Germany BVA, Art. 116(2) and §15 | https://www.bva.bund.de/EN/Services/Citizens/ID-Documents-Law/Citizenship/116GG_15StA.html | Restitution eligibility and the difference between the two routes |
| Germany, §5 StAG | https://www.gesetze-im-internet.de/stag/__5.html | Who may declare, and the ten-year limit in §5(3) |
| Germany, §15 StAG | https://www.gesetze-im-internet.de/stag/__15.html | The four persecution categories and the descendants clause |
| Germany, §10 StAG | https://www.gesetze-im-internet.de/stag/__10.html | That §10(3) now reads "(weggefallen)" |
| Germany, §12 StAG | https://www.gesetze-im-internet.de/stag/__12.html | That the section is repealed |
| Germany, §5 declaration route explainer | https://www.germany.info/us-en/service/03-citizenship/2479488-2479488 | The ten-year declaration right created on 20 August 2021 |
| Germany Federal Foreign Office, dual citizenship | https://www.auswaertiges-amt.de/en/2664476-2664476 | That multiple nationality is allowed since 27 June 2024 |
| Austria, §58c consolidated statute (RIS) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005579 | The direct-descending-line wording in §58c(3), with no generation cap |
| Hungary, simplified naturalization (Tel Aviv) | https://telaviv.mfa.gov.hu/en/egyszerusitett-honositas | The Hungarian-language check at the interview |
| Czechia, children and grandchildren by declaration | https://mzv.gov.cz/losangeles/en/consular_information/czech_citizenship_and_vital_records/children_and_grandchildren_of_former.html | Generational reach and the 31 December 2013 loss date |
| Latvia, Citizenship Law | https://likumi.lv/ta/en/en/id/57512 | Section 8.1 on exiles and their descendants, and the dual-citizenship allowance |
| Greece, Holocaust-victim restoration | https://id.mitos.gov.gr/338062 | Who it covers, that it is filed at the consulate, and that it is for the former citizen personally |
| Spain, Ley 12/2015 | https://www.boe.es/buscar/act.php?id=BOE-A-2015-7045 | The three-year filing window and its one-year extension, both now expired |
| Israel, apostille authorities | https://www.gov.il/en/service/apostille-approval-for-countries | Which Israeli body apostilles which document type |
| Israel, population-registry extract procedure 2.17.0001 | https://www.gov.il/he/pages/summary_info_procedure | Exactly which fields the standard and extended extracts contain |
| Israel, ordering the extract | https://www.gov.il/en/service/summaryinfofromthepopulationregistrylisting | How to order the tamtzit rishum used to prove lineage |
| Israel, foreign-passport border concession | https://www.gov.il/he/pages/news-exit-with-foriegn-passport-300926 | The extension to 30.09.2026 and the check-in requirement |

## Troubleshooting

- **"My grandparent emigrated before WWII, do I still qualify for Germany?"** Only if the ancestor actually held German citizenship and was stripped of it (Art. 116(2) or §15). A grandparent who was, for example, a Polish or Hungarian Jew persecuted by the Nazis does NOT get German citizenship this way; match them to their country of citizenship instead. Where there was a German citizenship loss, its timing matters more than the emigration date. Map the loss event, then confirm with the German mission.
- **"The family name is spelled three different ways across the documents."** Expected, and fixable. Build the variants table, get the notarized same-person affidavit, and ask the consulate whether it wants an affidavit or a court declaration. Do not assume the mismatch disqualifies the claim, and do not silently normalise the spellings.
- **"An agency quoted me thousands of shekels."** It depends entirely on the route, so do not give a blanket "you can do this yourself". Where the work really is assembling, translating and apostilling a document chain (Germany, Austria, Poland, Czechia, Latvia), a motivated applicant can usually do it themselves using the pipeline above. Where the hard part is no longer document assembly, paying for help can be rational: Romania now turns on obtaining a certified B1 certificate from a specific institution, Italy after the 2025 statute usually turns on a legal argument or litigation, and the Greek restoration route runs through a consular procedure measured in many months. Price the actual bottleneck for the user's route before judging the quote, and reserve a lawyer for a genuinely contested lineage or a broken chain.
- **"Which country should I pick if I qualify for several?"** Rank by feasibility from Israel: restitution routes with no residence or language requirement first (Germany, Austria), then confirmation routes that turn only on documents (Poland, Czechia, Latvia), then routes with a conversational language check (Hungary), then routes with a certified language exam (Romania). Drop anything in the Closed table. Then weigh the documents you can actually obtain, because a route you qualify for on paper but cannot document is not a route.
