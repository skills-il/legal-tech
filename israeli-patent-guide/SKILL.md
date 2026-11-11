---
name: israeli-patent-guide
description: "Not a patent application. Guidance through the Israeli patent process: prior art search on the ILPO database, national application filing, PCT international filing via ILPO, fees, deadlines, and maintenance. Use when you need to check invention novelty, prepare to file a patent in Israel, track payment deadlines, or understand pharmaceutical patent term extension (PTE). Saves hours of research and helps avoid common filing mistakes. Do NOT use for trademark registration, registered designs, or as a substitute for a licensed patent attorney."
license: MIT
---

# Israeli Patent Guide

## Legal notice

This is a free information tool operated by an AI model. It explains patent procedure and helps you organise your own material. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by a patent attorney or advocate. The output is not a patent application prepared by a patent attorney and not a professional opinion, but an explanation and raw material for the user's own preparation only: it does not perform an exhaustive prior-art search and does not draft patent claims or any document for filing. An AI model may err, omit data, or present a wrong conclusion.

Drafting patent claims and representation before the Registrar of Patents are reserved by law to a patent attorney. Publication or faulty drafting can damage rights irreversibly, on deadlines that cannot be extended. Consult a patent attorney before any filing. All use of its output is the user's sole responsibility.

## Overview

This skill covers the patent process in Israel as administered by the Israel Patent Office (ILPO, רשות הפטנטים). It is scoped to:

- National patent application filing under the Patents Law, 5727-1967, and the Patents Regulations (Office Practice, Rules of Procedure, Documents and Fees), 5728-1968
- Prior art search using ILPO's public database and international resources
- PCT international filing routed through ILPO as Receiving Office
- The official fee schedule, the 40% reduction for qualifying applicants, and the renewal structure
- Patent Term Extension (PTE) for pharmaceutical products
- Key deadlines: priority claim, the Section 18 notice prior to examination, publication, opposition, renewals

This skill does NOT cover trademark registration, industrial design registration, copyright, or utility models. It does not replace a licensed Israeli patent attorney for prosecution decisions.


## When to Use

- **Novelty check**: before investing in a full application, search ILPO's database and WIPO PatentScope to assess whether an invention is likely new.
- **Filing preparation**: what a national application must contain, and what to hand the patent attorney.
- **PCT national phase entry**: timelines and requirements for entering the Israeli national phase.
- **Deadline tracking**: the 2-month priority claim, the 30-month PCT window, renewals, and the 3-month opposition period from publication of acceptance.
- **PTE calculation**: eligibility and maximum extension for pharmaceutical patents.
- **Fee estimation**: whether the 40% reduction applies, and the official fees along the way.


## Instructions

1. **Collect the facts first.** Who invented it and under what relationship (employee, contractor, founder still employed elsewhere, university staff); every public disclosure and its date; any earlier filing anywhere (that date is the priority date); any military or security use; target markets; budget.
2. **Ownership.** Apply "Who Owns the Invention" below before anything is filed in a company's name.
3. **Disclosure.** If anything was disclosed before filing, apply Gotcha 0, including the s.6 exceptions.
4. **Eligibility.** For software, algorithms or data processing, apply "Software and Algorithms" below.
5. **Route.** Israel first, abroad first, or PCT. If the invention has any military use, the s.98 gate in "Before Filing Abroad" comes before any foreign filing.
6. **Deadlines.** Run `scripts/patent-deadlines.py` with the dates the user has, and list every date it prints.
7. **Costs.** Quote official fees from the fee table with their date stamp, and say that attorney fees are separate and usually larger.
8. **Stay on the explaining side of the line.** Do not write a claim set, a filing-ready specification, or an office-action response for filing. Section 154 of the Patents Law gives patent attorneys the exclusive right to handle patent applications for remuneration and to prepare documents filed with the Registrar or a foreign industrial-property office (advocates keep the same right under s.154(b)). When asked to "write our claims" or "file this for us", say so, and offer an **invention-disclosure memo** for the attorney instead: the problem, how the invention solves it, embodiments and alternatives, what the founders believe is new, prior art they know, disclosure history, and open questions.


## Israeli Patent Filing Process

### Who Owns the Invention: Service Inventions (Sections 132-135)

Section 132(a): an invention made by an employee during and in consequence of employment belongs to the employer by default. Section 134 routes compensation disputes to the Compensation and Royalties Committee at ILPO when the contract is silent. The employer loses title if the employee's s.131 notice says the invention will be the employee's absent a contrary reply within 6 months and the employer stays silent (s.132(b)); disputes over whether it is a service invention go to the Registrar (s.133). A contractor is not an employee, so the default does not apply to them: settle ownership in writing. A founder who conceived the idea while still employed elsewhere, including at a university, may have handed it to that employer under the same s.132(a) default; resolve this before filing.

Detail, including the contractor trap and drafting guidance: `references/service-inventions.md`.

### Application Requirements

A complete patent application filed with ILPO must include:

1. **Request form** (Form P/1): applicant name, inventor name(s), title of invention, an address for service in Israel (s.11(a)), and any claim of priority.
2. **Specification** structured as:
   - **Description**: technical field, background, summary, detailed description of embodiments, and reference to drawings.
   - **Claims**: numbered, beginning with an independent claim. Claims define the legal scope of protection. A patent covers one invention only (s.8).
   - **Abstract**: a short summary used for search purposes.
   - **Drawings** (if applicable), referenced in the description.
3. **Priority**: the priority claim must be filed no later than **2 months after the Israeli filing** (s.10(a)(2)), and the certified copy of the earlier specification within **12 months after the Israeli filing**, or together with an accelerated-examination request if that comes first (reg 24).

### Language and Address

The Regulations accept documents in an "official language" or English (regs 25 and 36(2)), and a priority document in any other language needs a translation within 3 months of the Registrar's demand (reg 25). Confirm with ILPO before filing in any other language. Every applicant needs an address for service in Israel (s.11(a)); foreign applicants in practice use an Israeli patent attorney or advocate. A corporate applicant (other than a defence body), and a licensed professional filing in the course of practice, must file only through the online filing site (reg 10A(b)); paper filing remains open to individuals filing for themselves.

### Duty of Disclosure (Sections 18, 18A, 18C)

Before examination the examiner demands two lists (s.18(a)-(b)): the citations that foreign patent offices relied on in examining applications for the same invention, and publications before the application date known to the applicant that directly concern the invention. Until acceptance the applicant must update ILPO on any change to those lists (s.18A). If the answer contained a misleading detail, or the applicant knowingly failed to update a significant change, the court or Registrar may revoke or refuse the patent, grant a licence, or shorten its term (s.18C). There is no prescribed IDS form; a letter listing the documents is the norm.

### Publication at 18 Months (Section 16A)

Every application file is opened to public inspection online 18 months from filing, or from the earliest priority date (s.16A(c)); a PCT application in the national phase is published within 45 days of entry (s.16A(b)). From then on the specification is public, so whatever it discloses can no longer be kept as a trade secret.


## Prior Art Search

### ILPO Database

ILPO's online system at **israelpatents.justice.gov.il** is free and bilingual. It combines patent search (full text, IPC codes, applicant and inventor names, status) with the journal and the e-filing requests area.

For international databases (PatentScope, Espacenet, Google Patents) and a search strategy, see `references/prior-art-search.md`.

### What the Examiner Will Test (Sections 3, 4, 5, 7)

An invention, product or process, **in any field of technology**, is patentable if it is new, useful, industrially applicable and involves an inventive step (s.3). It is new only if it was not published anywhere, in writing, orally, or by use or display, before the application date (s.4). Inventive step means it is not obvious to an average person skilled in the art (s.5). No patent is granted for a method of medical treatment of the human body, or for new plant or animal varieties other than non-natural microorganisms (s.7).

### Software and Algorithms

ILPO's guidelines for computer-implemented inventions (in force since 15 March 2012) read "in any field of technology" in s.3 as requiring a **tangible technological process**: some physical property is evident in the object the invention affects or in the activity it carries out. A discovery, scientific theory, mathematical formula, game rules or thought process is an abstract idea in itself, whether done by hand or by computer. In practice, a sensor or signal-processing algorithm is usually framed around the physical data it processes and the technical effect it produces, not the mathematics alone. The patent attorney decides the framing; the agent should raise the question early, and also the alternative of keeping the algorithm a trade secret, since publication at 18 months ends secrecy.


## PCT International Filing from Israel

### Before Filing Abroad: Defence-Related Inventions (Sections 94-113)

**Check this before any foreign or PCT filing.** Chapter Six of the Patents Law (sections 94 to 113) governs inventions of potential military significance. Under s.98, an Israeli citizen, permanent resident, or other person owing allegiance to the State may not file abroad, directly or indirectly, for an invention concerning weapons, ammunition or other military value (or of a class under s.95), unless **(1) the Minister of Defence gave prior written permission, or (2) an Israeli application was filed and 6 months have passed with no s.94 order in force**. Filing a national application at ILPO first and waiting 6 months is the usual lawful route; ask a patent attorney before relying on a PCT filing at RO/IL for this.

This bites disproportionately in Israel because so much of the startup base works in cyber, optics, UAV and drone systems, RF and communications, sensors, and advanced materials. An Israeli founder who files a US provisional or an ePCT application first, without clearance, may commit an offence rather than merely lose a right.

Practical rule: if the invention has any plausible military or security application, get an opinion from a licensed Israeli patent attorney on sections 94-113 **before** the first foreign filing.

### ILPO as Receiving Office

ILPO acts as Receiving Office (RO/IL) for Israeli nationals and residents, who may also file with WIPO's International Bureau. An international application filed at RO/IL must be in **English**. Filing via ePCT (pct.wipo.int) is recommended over paper.

### International Searching Authority (ISA) Options

The competent ISAs for an application filed at RO/IL are ILPO (ISA/IL), the EPO (ISA/EP) and the USPTO (ISA/US); each of them can be the IPEA only if it carried out the international search. The choice affects cost and how the search report is perceived in later national phases.

Fees at RO/IL in the WIPO PCT Applicant's Guide, Israel chapter, valid as from **1 August 2026**: **ISA/IL search fee 4,203 ILS** (published as 1,446 USD), transmittal fee 656 ILS, and the international filing fee of 1,667 USD plus 19 USD per sheet over 30. Confirm the current figures in the Guide before filing, since WIPO updates them periodically.

### National Phase Entry in Israel

National phase entry must occur within **30 months from the earliest priority date** (not the PCT filing date). Steps:

1. File a national phase entry request with ILPO.
2. Pay the national fee (fee notice item 13).
3. If the international application was not filed or published in English, submit a **verified English translation** (s.48D(b)(2)); otherwise the application is treated as withdrawn. The Registrar may extend this deadline by up to 3 months (s.48D(c)).
4. Give an address for service in Israel.

### Israel or Abroad First, and Paying Fees

An Israeli patent protects only Israel. To protect other markets, use the 12-month Paris priority year to file abroad directly or through PCT, which defers national-phase costs to month 30. Official ILPO fees are in NIS and are paid through the government payments site (ecom.gov.il/patents).


## Section 18 Notice prior to Examination and Office Actions

### The Section 18 Notice

Examination is queued automatically: there is no EPO-style request for examination and no separate examination fee for a normal application. About **4 months before** the application comes up for examination, ILPO sends the s.18 demand (the "notice prior to examination"), asking for the countries where protection was sought, the foreign citations and the known publications described above (reg 36(1)).

- **Response deadline**: **4 months** from the demand (reg 36(2)). No answer is treated as a failure to remedy defects under s.20 (reg 36(4)).
- **Extensions**: NIS 240 per month or part thereof (fee notice item 9); confirm the maximum with ILPO.
- **Third parties**: may file s.18 material until 2 months after the applicant answers the demand (s.18(b)(3)).
- **Deferral**: ILPO practice lets an applicant ask to defer examination in response to the notice. No regulation sets this general deferral (regs 37-39 cover narrower cases), so confirm the current practice with ILPO.

### Office Action Response Deadlines

The applicant may answer an examination report and fix the defects within **4 months** of the notice (reg 42); the period is extendable for a fee.

### Current Examination Backlog

The wait from filing to the end of examination runs to years, with biotechnology typically slower than other fields. ILPO publishes pendency figures in its annual report (the 2024 report was the latest published on 11 November 2026); read the current report rather than a figure quoted second hand.


## Patent Law Amendment No. 15 Bill (lapsed)

The government published the **Patents Law (Amendment No. 15) Bill, 5786-2025** on 30 December 2025 (Government Bills 1920). It proposed examination on request, a domestic provisional application, and a 12-month grace period. It was tabled for first reading in the 25th Knesset and never received one. The 25th Knesset's last session ended on 17 July 2026 and the 26th Knesset opened on 10 November 2026; as of 11 November 2026 the Knesset database holds no patents bill in the 26th Knesset. **None of it is law.** If a new government revives it, re-check the text. Background on what it proposed: `references/amendment-15.md`.


## Divisional, Accelerated Examination, and the Absence of a True Provisional

### Divisional Applications

A patent covers one invention only (s.8). If an application claims more than one, or the applicant wants to pursue subject matter separately, a **divisional application** can be filed out of a pending parent, keeping the parent's filing date. Division may be requested only **while the parent has not yet been accepted** (s.24(a)), so not during the opposition period; it carries its own filing fee.

### Accelerated (Expedited) Examination

Section 19A(a) lets the applicant ask for immediate examination on reasonable grounds, including: (1) advanced age or health; (2) a Registrar notice allowing acceleration because a parallel application was examined abroad (the PPH route); (3) someone else is exploiting the claimed invention, or there is a well-founded fear of it; (4) an unreasonably long time since filing or national-phase entry; (5) public interest; (6) special circumstances. The fee notice charges NIS 357 for the request plus NIS 834 for the examination only for grounds (3) to (6). Asking for an extension or a suspension during accelerated examination sends the application back to the regular queue, unless the Registrar finds an extension was needed for reasons beyond the applicant's control (s.19A(b)). For a PCT national-phase application, accelerated examination cannot start before 30 months from filing or priority (s.19A(e)). ILPO also runs a green-applications priority track for environment-related inventions; the pilot below uses that channel.

Since 1 June 2026 ILPO runs a **Bio-Convergence pilot**: applications classified in that field get priority, with examination starting within 3 months of classification, filed through the green-applications channel, and no accelerated-examination fee.

### No True Provisional Application

Israel has no US-style provisional application. The practical substitute is the **12-month Paris priority year**: file a first application (in Israel or elsewhere), then file the full national or PCT application within 12 months claiming priority, and claim it in Israel within 2 months of the Israeli filing (s.10(a)(2)). The Amendment 15 bill that proposed an Israeli provisional lapsed (see above).


## Fees and Cost Savings

### 40% Fee Reduction (pay 60% of the amount)

Applies to the FILING fee and the NOTICE-OF-ACCEPTANCE fee only, and only on a FIRST patent application for that invention. It does NOT apply to renewals, accelerated examination, PTE, oppositions, or extensions of time. For the PCT national fee, see the note under the table.

Eligible: (a) any applicant that is not a company or partnership; (b) a company or partnership whose turnover in the PRECEDING year did not exceed NIS 10 million; (c) an institution recognised under s.9 of the Council for Higher Education Law; (d) a technology-transfer company wholly owned by such an institution.

Full eligibility text and worked examples: `references/ilpo-fee-schedule.md`.

### Fee Structure Overview

ILPO fees are CPI-indexed and normally change on 1 January. The figures below are from the **official fee notice dated 22 December 2025, in force from 1 January 2026**, still the current notice on 11 November 2026 (https://www.gov.il/BlobFolder/news/ilpo-fees/he/news_fees-2026.pdf, landing page https://www.gov.il/he/pages/ilpo-fees). Do not estimate 2027 amounts; check the landing page for a new notice. Amounts in NIS.

| Fee Type | Full Fee (2026, NIS) | With Reduction (60%) |
|---|---|---|
| National application filing, first 50 claims (examination included) | 2,402 | 1,441 |
| Additional fee per claim, from the 51st claim | 616 each | not reduced |
| PCT national fee, s.48D(a) (examination included) | 2,402 | see note |
| Notice of acceptance | 841 | 505 |
| Renewal, years 1-6 (due within 3 months of grant) | 961 | not reduced |
| Renewal, years 7-10 (due before end of year 6) | 1,921 | not reduced |
| Renewal, all periods at once (due within 3 months of grant) | 14,410 | not reduced |

**PCT national fee note**: the notice's 60% clause appears only in items 1 and 10, not in item 13, while WIPO's IL chapter says a 40% reduction applies for applications first filed in Israel by a qualifying applicant. Confirm with ILPO before paying a reduced national fee.

Full 2026 schedule (all rows, PTE ladder, PCT-phase fees, inter partes): `references/ilpo-fee-schedule.md`. Patent-attorney drafting and prosecution fees are private and usually dominate the budget; get a written quote. The claim and page supplements also apply to PCT applications entering Israel.

### Maintenance Fee Structure

- **Years 1 through 6**: a lump sum of **NIS 961**, due **within 3 months of the grant date**, covering the first 6 years from the filing date.
- **Subsequent years**: paid in blocks covering years 7-10, 11-14, 15-18, and 19-20.
- **Each renewal is due before the END of the year PRECEDING the block it covers**: before the end of year 6, 10, 14 and 18. Paying "before the year-7 anniversary" is a full year late. A renewal may not be paid earlier than 3 months before its due date (reg 87(a)).
- **Grant after a renewal date**: given the examination queue, grant often comes after the end of year 6. Confirm with ILPO how the renewals already due at grant are paid.
- **All-inclusive option**: NIS 14,410 paid within 3 months of grant keeps the patent in force for its entire term, versus NIS 17,292 band by band.
- **Late payment**: up to 6 months late (s.57), with a surcharge equal to the extension fee for each month or part of a month late, NIS 240 in 2026 (reg 87(c)). After that the patent lapses. Restoration under section 59 costs NIS 841 and requires showing the fee was unpaid for reasonable causes, the lapse was unintended, and the request was filed as soon as possible after the non-payment became known (s.60); anyone who began using the invention after the lapse was published may keep doing so (s.63).
- **No small-entity discount** on any renewal fee.
- **Maximum term**: 20 years from the filing date (not the priority date).


## Objection Period

After an application is accepted, ILPO publishes the acceptance online (section 26). Any person may file an opposition within **3 months from the date of that publication** (section 30), not from the date the applicant received the notice. The Registrar may not extend it (s.164(a) excludes s.30). If an opposition is filed, opposition proceedings run before ILPO before the patent can be granted. Budget the notice-of-acceptance fee (NIS 841, or 505 reduced) at acceptance.


## Patent Term Extension (Pharma)

Sections 64A to 64Q of the Patents Law let the Registrar extend a basic patent covering a medicinal product or regulated medical device. Four rules drive most decisions:

- **Filing window**: no later than **90 days** from registration of the medicinal product under the Pharmacists Ordinance (s.64O(a)).
- **Recognized-country linkage**: where marketing approval was given in the United States or a recognized European state (First Schedule), a matching extension must also have been granted there and not expired (s.64D(5)-(7)). The Israeli extension lasts as long as the SHORTEST extension granted in the recognized countries (s.64I(a)).
- **Israel-only registration is not a bar**: if registration was sought only in Israel, the extension equals the period from filing the registration application to registration, provided it was pursued in good faith and with due diligence (s.64I(b)).
- **Caps** (s.64J): at most **5 years** beyond the s.52 term, and total protection ends no later than **14 years** from the first marketing approval in any recognized country.

Details, opposition, and the fee ladder: `references/pte.md` and `references/ilpo-fee-schedule.md`.


## Examples

### Example 1: Founder with a sensor algorithm

User says: "We built a new vibration-sensor algorithm. We pitched it at a demo day two weeks ago. How do we patent it in Israel and the US?"

Actions: collect the facts (step 1); flag that the demo-day pitch is a public disclosure that may already defeat novelty in Israel and that s.6 does not cover a pitch, so a patent attorney must assess it now; raise the s.3 software question and the trade-secret alternative; check s.132 if a founder was employed elsewhere; ask whether the sensor has military uses (s.98); then prepare an invention-disclosure memo and a deadline docket. Do not draft claims.

### Example 2: PCT national phase docket

User says: "Our PCT was filed 2025-03-10 claiming a US provisional of 2024-03-18. When must we enter Israel, and what will it cost?"

Actions: run `scripts/patent-deadlines.py --pct --filing-date 2025-03-10 --priority-date 2024-03-18`. The 30-month date is 2026-09-18, counted from priority, and the script marks it PASSED as of 11 November 2026, so it also prints the 12-month outer limit for Rule 49.6 reinstatement. Quote the 2026 national fee (NIS 2,402; whether the reduction applies needs ILPO confirmation, see the fee note), the claim supplement from the 51st claim, and the English translation rule (s.48D). If the date has passed, explain Rule 49.6 reinstatement (Troubleshooting).


## Bundled Resources

- `scripts/patent-deadlines.py`: deadline calculator (Python 3 standard library only). Inputs: `--filing-date`, `--pct` (PCT national phase entry), `--priority-date`, `--grant-date`, `--publication-date`, `--s18-notice-date`, `--isr-date`, `--moh-authorization-date`. Run `--help` for examples.
- `references/ilpo-fee-schedule.md`: the full 2026 fee notice.
- `references/pct-israel-checklist.md`: PCT filing and national-phase checklist.
- `references/prior-art-search.md`: databases and search strategy.
- `references/service-inventions.md`, `references/pte.md`, `references/amendment-15.md`, `references/domain-checklist.md`.


## Gotchas

### 0. There Is No Grace Period Today: Disclose Publicly and You Lose the Patent

Under **current** Israeli law there is no general grace period. Any public disclosure before the filing date destroys novelty, wherever in the world it happened, in any language, **including a disclosure by the inventors themselves**. A demo day pitch, a conference talk, a paper, a public GitHub repository, a product launch, or a trade show booth can each end the possibility of a valid patent.

- File first, disclose second. A disclosure under a signed NDA is not a public disclosure.
- Section 6 saves only narrow cases: material taken from the inventor and published without consent, if the application is filed within a reasonable time after learning of it; display at an industrial or agricultural exhibition in Israel or at a recognized exhibition notified to the Registrar before it opened, if filed within 6 months of the opening; and the inventor's lecture to a scientific society, if the Registrar was notified before the lecture and the application is filed within 6 months.
- The 12-month grace period of the Amendment 15 bill never became law.
- Registered designs under the Designs Law, 5777-2017 **do** have a 12-month grace period, so the design route may still be open after a public showing. Ask a licensed Israeli patent attorney promptly.

### 1. The Disclosure Lists Must Be Updated Until Acceptance

The s.18 lists are not a one-time filing. If a US or EP counterpart draws an office action citing new art after the Israeli answer, update ILPO (s.18A). A misleading detail, or a knowing failure to update a significant change, exposes the patent to revocation, a licence or a shorter term (s.18C).

### 2. No Examination Request, But the Section 18 Notice Has a 4-Month Deadline

Do not tell a client "there is nothing to do until the first office action." The s.18 demand must be answered within 4 months (reg 36(2)), and, under ILPO practice (no regulation sets it), it is also the moment to ask to defer examination; confirm with ILPO.

### 3. The 40% Fee Reduction Threshold is NIS 10M Turnover, Not Profit

The threshold is turnover in the **preceding** year that **did not exceed** NIS 10 million, so exactly NIS 10 million still qualifies. Recognised higher-education institutions and their wholly-owned technology-transfer companies also qualify. The reduction applies **only to a first application for that invention**, not to divisionals, and **only to the filing fee and the notice of acceptance fee**.

### 4. PCT 30-Month Deadline Runs From Priority Date, Not PCT Filing Date

Agents sometimes calculate from the international filing date, which can be up to 12 months later. A miss is curable only by a PCT Rule 49.6 reinstatement request under the strict "due care" test, which is not guaranteed and has its own time limit (see Troubleshooting).

### 5. Israeli PTE Is Capped by Foreign Extensions and a 14-Year Ceiling

The Israeli extension is limited to the shortest extension granted in the recognized countries, and ends no later than 14 years from the first marketing approval in any of them (ss.64I, 64J). Do not quote a flat 5 years.

### 6. The Priority Claim Has Its Own 2-Month Deadline

Filing in Israel within the Paris year is not enough. The priority claim itself must be filed no later than 2 months after the Israeli filing (s.10(a)(2)). A late claim can be rescued only by asking the Registrar to extend the period, which is possible only before acceptance and only for a good-faith mistake (s.164(a)(2)); act at once through a patent attorney.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Israel Patent Office | https://www.gov.il/he/departments/ilpo | Forms, fee notices, announcements, annual reports |
| ILPO fee notice 2026 | https://www.gov.il/BlobFolder/news/ilpo-fees/he/news_fees-2026.pdf | Every official fee, in force from 1 January 2026 |
| Patents Law 5727-1967 (Hebrew, Wikisource) | https://he.wikisource.org/wiki/חוק_הפטנטים | Current consolidated sections (also on WIPO Lex: https://www.wipo.int/wipolex/en/text/495413) |
| Patents Regulations 5728-1968 (Hebrew, Wikisource) | https://he.wikisource.org/wiki/תקנות_הפטנטים_(נוהלי_הרשות,_סדרי_דין,_מסמכים_ואגרות) | Regs 10A, 24, 25, 36, 42, 87 |
| WIPO PCT Applicant's Guide, Israel | https://pctlegal.wipo.int/eGuide/view-doc.xhtml?doc-code=IL | RO/ISA/IPEA fees, national phase, Rule 49.6 |
| Israel Patents Online (search and e-filing) | https://israelpatents.justice.gov.il/en | Israeli applications and patents |
| ePCT and PatentScope | https://pct.wipo.int and https://patentscope.wipo.int/search/en/search.jsf | PCT filing; international prior art |

## Recommended MCP Servers

This Model Context Protocol server, available in the skills-il directory, pairs well with this skill:

- **boi-exchange**: Bank of Israel exchange-rate data. Use it to convert ILPO fees to a foreign currency when a foreign applicant is budgeting a filing.

Always confirm fee figures against the official ILPO notice, since the schedule is CPI-indexed and changes each year.

## Troubleshooting

**Problem**: ILPO database search returns no results for a known Israeli patent.
**Solution**: Try searching by application or publication number directly. A file only becomes publicly visible once it is opened to inspection at 18 months (s.16A), so a recent application may simply not be public yet. Older patents may not be fully digitized; this is a likely cause, not a confirmed one.

**Problem**: ILPO rejected a priority document as insufficient.
**Solution**: The priority document must be a certified copy of the earlier specification (s.10(a)(3), reg 24). Uncertified copies or printouts may not satisfy ILPO; confirm acceptable formats, including WIPO DAS, with an Israeli patent attorney before relying on them.

**Problem**: Applicant is not sure whether they qualify for the 40% fee reduction (company is a subsidiary of a larger group).
**Solution**: The fee notice applies the turnover test to the applicant. Whether a subsidiary is measured alone or with its group is fact-specific; verify with a licensed Israeli patent attorney.

**Problem**: PCT national phase entry deadline appears to have passed.
**Solution**: Confirm the earliest priority date carefully. Israel permits reinstatement of rights under PCT Rule 49.6 on the "due care" criterion, with a reinstatement fee of 240 ILS (WIPO PCT Applicant's Guide, Israel chapter, version applicable from 1 August 2026). The request, together with the national-phase acts, must be filed within 2 months from removal of the cause of the failure or 12 months from the expiry of the 30-month limit, whichever expires first (PCT Rule 49.6(b)). Reinstatement is not guaranteed; have a patent attorney file it at once.


## Disclaimer

This skill provides informational guidance only. It does not constitute legal advice and does not create an attorney-client relationship. Israeli patent law involves jurisdiction-specific nuances, fact-specific determinations, and professional judgment. For any specific patent matter, consult a licensed Israeli patent attorney registered with the Israeli Patent Office.
