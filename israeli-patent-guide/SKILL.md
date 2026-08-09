---
name: israeli-patent-guide
description: "Full guidance through the Israeli patent process: prior art search on ILPO database, national application filing, PCT international filing via ILPO, fees, and maintenance. Use when you need to check invention novelty, file a patent in Israel, track payment deadlines, or understand pharmaceutical patent term extension (PTE). Saves hours of research and prevents costly filing mistakes. Do NOT use for trademark registration, design patents, or legal advice replacing a licensed patent attorney."
license: MIT
version: 1.4.0
---


## Legal notice

This is a free information tool operated by an AI model. It explains patent procedure and helps you organise your own material. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by a patent attorney or advocate. The output is not a patent application prepared by a patent attorney and not a professional opinion, but an explanation and a draft only: it does not perform an exhaustive prior-art search and does not draft enforceable patent claims. An AI model may err, omit data, or present a wrong conclusion.

Drafting patent claims and representation before the Registrar of Patents are reserved by law to a patent attorney. Publication or faulty drafting can damage rights irreversibly, on deadlines that cannot be extended. Consult a patent attorney before any filing. All use of its output is the user's sole responsibility.
## Overview

This skill covers the end-to-end patent process in Israel as administered by the Israeli Patent Office (ILPO, also known as Rashut HaPatenTim - רשות הפטנטים). It is scoped to:

- National patent application filing under the Israeli Patents Law, 5727-1967
- Prior art search using ILPO's public database and international resources
- PCT international filing routed through ILPO as Receiving Office
- Official fee schedule, the 40% reduction for qualifying applicants, and maintenance fee structure
- Patent Term Extension (PTE) for pharmaceutical products under Israeli law
- Key deadlines, the Section 18 Notice prior to Examination, objection windows, and IDS (Information Disclosure Statement) obligations unique to Israeli practice

This skill does NOT cover trademark registration, industrial design registration, copyright, or utility model protection. It does not replace a licensed Israeli patent attorney for prosecution decisions.


## When to Use

- **Novelty check**: Before investing in a full application, search ILPO's database and WIPO PatentScope to assess whether an invention is likely new.
- **Filing guidance**: Step-by-step walkthrough of requirements for filing a national patent application in Israel.
- **PCT national phase entry**: Understanding timelines and requirements for entering the Israeli national phase from a PCT application.
- **Deadline tracking**: Calculating maintenance fee due dates, the 30-month PCT window, and the 3-month objection period after allowance.
- **PTE calculation**: Determining eligibility and maximum extension duration for pharmaceutical patents.
- **Fee estimation**: Checking whether you qualify for the 40% reduction and estimating total filing and prosecution costs.


## Israeli Patent Filing Process

### Who Owns the Invention: Service Inventions (Sections 132-135)

Section 132(a): an invention made by an employee during and in consequence of employment belongs to the employer by default. Section 134 routes compensation disputes to the Compensation and Royalties Committee at ILPO when the contract is silent. Waivable by express contract (*Bayer v. Plurality*). A contractor is not an employee, so the default does not apply to them: settle ownership in writing.

Detail, including the contractor trap and drafting guidance: `references/service-inventions.md`.

### Application Requirements

A complete patent application filed with ILPO must include:

1. **Request form** (Form P/1): applicant name, inventor name(s), title of invention, and claim of priority if applicable.
2. **Specification** structured as:
   - **Description**: technical field, background, summary, detailed description of embodiments, and reference to drawings.
   - **Claims**: numbered, beginning with an independent claim. Claims define the legal scope of protection.
   - **Abstract**: 150 words or fewer; not part of the legal scope but used for search purposes.
   - **Drawings** (if applicable): black-and-white line drawings, A4 format, referenced in the description.
3. **Priority document**: if claiming Convention priority under the Paris Convention, the certified copy must be submitted within 16 months of the priority date (or with the application if filed after 16 months).

### Language

Hebrew and English are both accepted as filing languages. If the application is filed in any other language, a Hebrew or English translation must be submitted within 3 months of the filing date. The translation becomes the official text for prosecution purposes.

### Address in Israel

Foreign applicants (those without a place of business or domicile in Israel) must appoint a registered Israeli patent attorney or agent as their address for service in Israel. Correspondence from ILPO is sent to this address.

### IDS Duty (Section 18, Israeli Patents Law)

Under Section 18 of the Israeli Patents Law, an applicant has a **continuing duty** to disclose all material prior art known to the applicant throughout prosecution, up to and including the Notice of Acceptance. This duty is substantially broader than USPTO practice:

- The duty applies to all material prior art, including art discovered during foreign prosecution of the same or related applications.
- Failure to disclose material prior art known to the applicant can be raised as a ground for patent revocation, even after grant.
- There is no prescribed form for the IDS in Israel; a letter to the examiner listing the relevant documents is sufficient.
- Best practice: file an IDS when receiving Office Actions or Search Reports from the USPTO, EPO, or any other office examining a counterpart application.

### Examination is Queued Automatically (No Early Examination-Request Election)

Unlike the EPO (where the applicant actively files a request for examination) or systems with a deferred-examination election made at filing, in Israel substantive examination is **queued automatically**. The applicant does not file an early examination-request form at the time of filing, and there is no separate examination fee beyond the filing fee.

However, this does NOT mean the applicant has nothing to do before examination. About 12 months before substantive examination begins, ILPO issues a **Notice prior to Examination under Section 18** of the Israeli Patents Law. The applicant must respond within a **4-month deadline** (extendable, with fees, up to a total of 12 months). The Section 18 notice is also the trigger for an applicant who wants to **defer** examination to file a deferral request. See the dedicated section below.

So the accurate framing is: examination is queued automatically (no EPO-style request-for-examination filing and no early deferred-examination election at filing), BUT there is a Section 18 Notice prior to Examination with a real response deadline. Telling an applicant "there is nothing to do until the first Office Action" is incorrect.


## Prior Art Search

### ILPO Database

The ILPO online patent search is available at **israelpatents.justice.gov.il**. It is free, publicly accessible, and bilingual (Hebrew and English). Key features:

- Full-text search of Israeli patent applications and granted patents
- IPC (International Patent Classification) code filtering
- Applicant/inventor name search
- Status information (pending, granted, lapsed, opposed)

### International Databases

| Database | URL | Coverage |
|---|---|---|
| WIPO PatentScope | patentscope.wipo.int | 110M+ documents, PCT applications, national collections |
| Google Patents | patents.google.com | 120M+ documents, machine-translated content |
| Espacenet (EPO) | worldwide.espacenet.com | European and international collections |
| USPTO Full-Text | patents.google.com or USPTO.gov | US patents and published applications |

### Search Strategy

1. **IPC classification**: Identify the relevant IPC subgroups for your invention. ILPO search supports IPC filtering. Use WIPO's official IPC classification resource at https://www.wipo.int/classifications/ipc/en/ to find the right codes.
2. **Keyword synonyms**: Draft a synonym list covering technical terms, trade names, and common alternatives. Run multiple keyword searches; do not rely on a single query.
3. **Assignee/inventor search**: If you know of competitors or related inventors, search by name in PatentScope and ILPO.
4. **Non-patent literature**: For biotech and pharma, also search PubMed, journal databases, and conference proceedings. Published scientific papers constitute prior art.
5. **Date cutoff**: Prior art includes anything publicly available before your priority date, anywhere in the world, in any language.


## PCT International Filing from Israel

### Before Filing Abroad: Defence-Related Inventions (Sections 94-113)

**Check this before any foreign or PCT filing.** Chapter Six of the Israeli Patents Law (sections 94 to 113) governs inventions of potential military significance. Where an invention may be of defence interest, the applicant must bring it to the attention of the Minister of Defence, the Minister may impose a secrecy order, and **filing the application abroad without permission is prohibited and carries criminal liability**.

This bites disproportionately in Israel because so much of the startup base works in cyber, optics, UAV and drone systems, RF and communications, sensors, and advanced materials. An Israeli founder who files a US provisional or an ePCT application first, without clearance, may commit an offence rather than merely lose a right.

Practical rule: if the invention has any plausible military or security application, get an opinion from a licensed Israeli patent attorney on sections 94-113 **before** the first foreign filing, not after. This is a gate, not a formality, and no other section of this skill substitutes for it.

### ILPO as Receiving Office

Israel is a member of the Patent Cooperation Treaty (PCT). ILPO acts as a Receiving Office (RO/IL) for PCT applications filed by Israeli applicants (or applicants with a place of business or residence in Israel). Applications can also be filed directly with WIPO's IB as receiving office.

Filing via ePCT (pct.wipo.int) is strongly recommended over paper filing.

### International Searching Authority (ISA) Options

ILPO was recognized as an ISA/IPEA in 2012. Applicants filing through RO/IL can choose:

| ISA | Notes |
|---|---|
| ILPO (ISA/IL) | Often lower cost for Israeli applicants; examination in Hebrew or English; familiarity with Israeli practice |
| EPO (ISA/EP) | Widely respected; higher cost; English, French, or German required |
| USPTO (ISA/US) | Available for Israeli applicants; search report in English |

The choice of ISA affects search quality perception in national phases and the cost of the international phase. The **ISA/IL international search fee** is set at **USD 1,333** effective **1 March 2026** (WIPO PCT Applicant's Guide, Israel chapter). Always confirm the current PCT fee in the WIPO Applicant's Guide before filing, since WIPO updates the dollar-denominated fee periodically.

### National Phase Entry in Israel

For PCT applications designating Israel, national phase entry must occur within **30 months from the earliest priority date** (not the filing date of the PCT application). This is the absolute deadline under Israeli law. Specific steps:

1. File a national phase entry request with ILPO (Form PCT/IL/01 or equivalent).
2. Pay the national phase entry fee.
3. Submit a Hebrew or English translation of the specification if the PCT application was filed in another language.
4. Appoint an Israeli address for service if required.

### Fee Payment in NIS

All official ILPO fees are denominated in New Israeli Shekel (NIS). For foreign applicants paying from abroad, fees are converted at the Bank of Israel official exchange rate on the payment date.


## Section 18 Notice prior to Examination and Office Actions

### The Section 18 Notice

After filing, the application waits in the examination queue. Roughly 12 months before substantive examination is scheduled to begin, ILPO sends a **Notice prior to Examination under Section 18** of the Israeli Patents Law. The notice both tells the applicant the estimated examination date and asks the applicant to bring relevant prior art (including foreign search/examination results on counterpart applications) to ILPO's attention.

- **Response deadline**: 4 months from the date of the notice.
- **Extensions**: the 4-month deadline is extendable, with extension fees, up to a total of 12 months from the original notice date.
- **Deferral option**: the Section 18 notice is also the point at which an applicant who wants to push examination later can file a request to defer. ILPO will generally grant deferral of up to about 2 years, and the request is handled through the ILPO online portal. Deferral is an active choice made in response to the Section 18 notice, not an automatic state.

Missing the Section 18 response deadline without an extension can lead to the application being deemed abandoned, so it must be docketed like any other hard deadline.

### Office Action Response Deadlines

Once substantive examination starts, ILPO issues examination reports (Office Actions). The applicant must respond within the deadline stated in each report. As a general rule the response period is a few months and is extendable on payment of extension fees, but the exact period and the maximum cumulative extension depend on the specific report and current ILPO practice, so confirm the deadline printed on each Office Action rather than assuming a fixed number. The continuing IDS duty under Section 18 runs in parallel through this whole phase, up to the Notice of Acceptance.

### Current Examination Backlog

According to the ILPO 2024 Annual Report, the average elapsed time from filing to the end of substantive examination is around **43 months**. The figure varies materially by technology:

- **Biotechnology**: around **51.3 months** on average
- **Mechanical, electronics, and physics**: around **39.3 months** on average

These are averages, not commitments. They explain why accelerated examination (PPH, green-tech, competitor-on-market, age/health) is a real lever for applicants whose business cannot wait three to four years for an enforceable patent. They are also part of the policy backdrop for the pending Amendment 15 reform discussed below.


## Pending Patent Law Amendment No. 15 (2025-2026 reform)

On **30 December 2025** the Israeli government published the **Patents Law (Amendment No. 15) Bill, 5786-2025**, the most substantial overhaul of Israeli patent procedure in decades. As of May 2026 the bill is **in the Knesset Constitution, Law and Justice Committee following first reading**; it is not yet in force. Practitioners should track it because the proposed changes touch filing strategy, queue management, and grace-period reliance.

### Amendment 15 (proposed)

Status unconfirmed as of this revision; not in force. Proposed changes and their filing implications: `references/amendment-15.md`.

### Practical implications for filing today (May 2026)

- **Do not assume the new regime is in force.** Until the bill clears second and third readings and is published, the automatic-queue + Section 18 Notice model still governs. Continue docketing Section 18 deadlines.
- **Reconsider US-only provisional reliance.** If a domestic provisional becomes available in Israel, future filings may be structured to claim priority from an Israeli provisional rather than a US one. This is a strategy decision to revisit once the law is in force.
- **Track the grace-period commencement.** A 12-month grace is helpful only if the conversion deadline is met. Even after Amendment 15 enters into force, public disclosure remains risky in jurisdictions without an equivalent grace (most of the EU and China).
- **Monitor Reinhold Cohn, IAM, and ILPO portal updates** for the final version of the text as it moves through the Constitution Committee.


## Divisional, Accelerated Examination, and the Absence of a True Provisional

### Divisional Applications

If an application claims more than one invention, or the applicant wants to pursue subject matter separately, a **divisional application** can be filed out of a pending parent. The divisional keeps the parent's filing date for the carved-out subject matter. A divisional must be filed while the parent is still pending (before the parent is granted or finally refused), and it carries its own filing fee.

### Accelerated (Expedited) Examination

ILPO can move an application to the front of the examination queue on an accepted ground, for example applicant age or health, a competing product on the market, an application that is the basis for others, green technology, or via the Patent Prosecution Highway (PPH) using favorable results from a partner office. Accelerated examination is requested with a dedicated fee. This is the route to use when the default queue wait is too long for the applicant's business needs.

### No True Provisional Application

Israel does not have a US-style provisional application **today**. The practical substitute is the **12-month Paris Convention priority year**: file a first application (in Israel or elsewhere), then file the full national or PCT application within 12 months while claiming priority back to that first filing. There is no separate cheaper "provisional" filing track at ILPO under the current law.

This may change. The pending **Patents Law (Amendment No. 15) Bill, 5786-2025** (published 30 December 2025) proposes a new Israeli domestic provisional application with relaxed formal requirements, with a staged effective date of one year after publication once enacted. See the dedicated "Pending Patent Law Amendment No. 15" section above. Until the bill is enacted and the effective date arrives, treat the lack of a domestic provisional as the binding rule.


## Fees and Cost Savings

### 40% Fee Reduction (pay 60% of the amount)

Applies to the FILING fee and the NOTICE-OF-ACCEPTANCE fee only, and only on a FIRST patent application for that invention. It does NOT apply to renewals, accelerated examination, PTE, oppositions, or extensions of time.

Eligible: (a) any applicant that is not a company or partnership; (b) a company or partnership whose turnover in the PRECEDING year did not exceed NIS 10 million; (c) an institution recognised under s.9 of the Council for Higher Education Law; (d) a technology-transfer company wholly owned by such an institution.

Full eligibility text and worked examples: `references/ilpo-fee-schedule.md`.

### Fee Structure Overview

ILPO fees are CPI-indexed and change at the start of each year. The figures below are transcribed from the **official fee notice dated 22 December 2025, in force from 1 January 2026** (https://www.gov.il/BlobFolder/news/ilpo-fees/ar/news_fees-2026.pdf, landing page https://www.gov.il/he/pages/ilpo-fees). Amounts are in NIS.

Substantive examination is **included in the filing fee**; there is no separate "examination fee" for a normal application. A separate fee applies only when **accelerated** examination is requested.

| Fee Type | Full Fee (2026, NIS) | With Reduction (60%) |
|---|---|---|
| National application filing, first 50 claims (examination included) | 2,402 | 1,441 |
| Additional fee per claim, from the 51st claim | 616 each | not reduced |
| PCT national phase entry (examination included) | 2,402 | 1,441 |
| Renewal, years 1-6 (due within 3 months of grant) | 961 | not reduced |
| Renewal, years 7-10 (due before end of year 6) | 1,921 | not reduced |
| Renewal, all periods at once (due within 3 months of grant) | 14,410 | not reduced |

Full 2026 schedule (all rows, PTE ladder, PCT-phase fees, inter partes): `references/ilpo-fee-schedule.md`.

The PCT claim and page supplements apply to international applications designating Israel as well, and are the most commonly missed line items on national phase entry.

For the ILPO fees in the PCT international phase (ISA search 4,203, transmittal 656, IPEA preliminary examination 1,801), the full PTE fee ladder, and the miscellaneous inter partes fees, see `/references/ilpo-fee-schedule.md`.

### Maintenance Fee Structure

Patent maintenance (renewal) fees in Israel follow a unique schedule compared to most jurisdictions:

- **Years 1 through 6**: a lump sum of **NIS 961**, due **within 3 months of the grant date**, covering the first 6 years from the filing date.
- **Subsequent years**: fees are paid every 4 years in advance, covering years 7-10, 11-14, 15-18, and 19-20.
- **Each renewal is due before the END of the year PRECEDING the block it covers.** The renewal covering years 7-10 is due before the end of year 6, the one covering years 11-14 before the end of year 10, then before the end of year 14 and year 18. Paying "before the year-7 anniversary" is a full year late and the patent lapses.
- **All-inclusive option**: NIS 14,410 paid within 3 months of grant keeps the patent in force for its entire term. Band-by-band payment totals NIS 17,292, so the single payment saves NIS 2,882 and removes four dockets.
- **Grace period**: a 6-month grace period is available for late maintenance payments, subject to a surcharge. After the grace period the patent lapses, and restoration under section 59 costs NIS 841 and is discretionary.
- **No small-entity discount**: the 40% reduction does not apply to any renewal fee.
- **Maximum term**: 20 years from the filing date (not the priority date).


## Objection Period

After ILPO issues a Notice of Acceptance (analogous to a Notice of Allowance), there is a **3-month objection period** during which any person may file a formal opposition (objection) to the grant. This period is non-extendable. If an opposition is filed, the patent enters opposition proceedings before ILPO before the patent can be granted. If no opposition is filed within 3 months, the patent is granted.


## Patent Term Extension (Pharma)

### Overview

Israel provides for Patent Term Extension (PTE) for pharmaceutical products, similar in concept to Supplementary Protection Certificates (SPCs) in the EU. The PTE compensates patentees for time lost during regulatory approval proceedings before the Israeli Ministry of Health.

### Filing Window

The application for PTE must be filed with ILPO within **90 days** of the date on which the Ministry of Health grants marketing authorization (registration) for the pharmaceutical product in Israel. This 90-day window is **non-extendable**. Missing it forfeits the right to a PTE entirely.

### EU-5 Linkage Requirement

This is a feature unique to Israeli PTE law and is not found in US or standard EU SPC practice. Israeli PTE duration is capped by reference to the shortest patent term extension (or SPC) granted in any of the **EU-5 jurisdictions**: United Kingdom, Germany, France, Italy, and Spain.

In practice:
- You must obtain SPC or equivalent protection in at least one EU-5 jurisdiction before or concurrent with the Israeli PTE application.
- The Israeli PTE cannot exceed the duration of the shortest EU-5 extension granted for the same product.
- If no EU-5 jurisdiction has granted an extension (e.g., the product was approved only in Israel and not in the EU), the EU-5 linkage requirement effectively prevents PTE in Israel.

### Duration Caps

- Maximum PTE duration: **5 years**
- Maximum total patent term including PTE: **25 years** from the original filing date
- The extension is limited to the shortest EU-5 extension, which may further reduce the available term below 5 years.


## Key Databases and Resources

| Resource | URL | Purpose |
|---|---|---|
| ILPO Patent Search | https://israelpatents.justice.gov.il/en | Search Israeli patent applications and grants |
| ILPO Portal (Ministry of Justice) | https://patents.justice.gov.il | Official forms, fee schedules, announcements (the older israelpatents.justice.gov.il host still resolves) |
| PCT ePCT Filing | https://pct.wipo.int | Online PCT application filing and management |
| WIPO PatentScope | https://patentscope.wipo.int | International prior art search (110M+ documents) |
| WIPO PCT Guide for Israel | https://pctlegal.wipo.int/eGuide/view-doc.xhtml?doc-code=IL | Country-specific PCT requirements for Israel |
| IPC Classification (WIPO) | https://www.wipo.int/classifications/ipc/en/ | Find IPC codes for prior art searches |
| Bank of Israel Exchange Rates | https://www.boi.org.il/en/markets/exchange-rates/ | Official exchange rates for fee conversion |


## Gotchas

### 0. There Is No Grace Period Today: Disclose Publicly and You Lose the Patent

Under **current** Israeli law there is no general grace period. Any public disclosure of the invention before the filing date destroys novelty, wherever in the world it happened, in any language, and **including a disclosure made by the inventors themselves**. A demo day pitch, a conference talk, a published paper, a public GitHub repository, a product launch, or a trade show booth can each end the possibility of a valid patent.

This is the most expensive mistake founders make, and it is invisible until years later when the patent is challenged.

- File first, disclose second. If timing forces disclosure first, use a signed NDA, which is not a public disclosure.
- The 12-month grace period described in the Amendment 15 section below is **proposed, not in force**. Do not rely on it.
- Even if Amendment 15 is enacted, most of the EU and China still have no equivalent grace, so a public disclosure would remain fatal in those markets.
- One asymmetry worth knowing: registered designs under the Designs Law, 5777-2017 **do** have a 12-month grace period. If a product has already been shown publicly, the patent route may be closed while the design route is still open. Ask a licensed Israeli patent attorney promptly rather than assuming everything is lost.

### 1. IDS Duty is Continuous Until Notice of Acceptance

Unlike the USPTO where an IDS is typically filed once at defined stages, Israeli law (Section 18) imposes a **continuing duty** of disclosure throughout the entire prosecution lifecycle, from filing through the date of Notice of Acceptance. This means that if your US counterpart receives an Office Action citing new art after you filed your Israeli IDS, you must file a supplemental disclosure in Israel. Agents unfamiliar with Israeli practice routinely miss this. Failing to disclose material prior art known to the applicant can result in the patent being held invalid even after grant.

### 2. No EPO-Style Examination Request, But the Section 18 Notice Still Has a Deadline

Agents trained on EPO procedure often instruct clients to file a "request for examination" by a fixed deadline. In Israel there is no such examination-request filing and no early deferred-examination election at filing time. But it is equally wrong to tell a client "there is nothing to do until the first Office Action." About 12 months before examination, ILPO issues a **Section 18 Notice prior to Examination**, and the applicant must respond within **4 months** (extendable with fees up to 12 months total). The Section 18 notice is also the moment to file a deferral request if the applicant wants to push examination later. Treat the Section 18 notice as a hard, dockable deadline.

### 3. The 40% Fee Reduction Threshold is NIS 10M Turnover, Not Profit

Many agents default to quoting full official fees without checking eligibility for the reduction. The threshold is turnover (gross revenue) in the **preceding** year that **did not exceed** NIS 10 million, so exactly NIS 10 million still qualifies. Universities recognised under section 9 of the Council for Higher Education Law and their wholly-owned technology transfer companies also qualify, which covers every Israeli TTO.

Two traps agents fall into in the other direction: the reduction applies **only to a first application for that particular invention** (not to divisionals), and it covers **only the filing fee and the notice of acceptance fee**, not renewals, accelerated examination, PTE, oppositions, or extensions. Quoting a discounted renewal fee is wrong. Always verify eligibility at filing; the declaration cannot be added retroactively after fees are paid at full rate.

### 4. PCT 30-Month Deadline Runs From Priority Date, Not PCT Filing Date

The 30-month national phase entry window in Israel is measured from the **earliest priority date** claimed in the PCT application. Agents sometimes mistakenly calculate from the international (PCT) filing date, which can differ by up to 12 months from the priority date. A miscalculation here means a missed absolute deadline with no remedy.

### 5. PTE EU-5 Linkage is Unique to Israel

Attorneys and AI tools trained on US or EU patent law have no frame of reference for the Israeli PTE EU-5 linkage requirement. An agent providing PTE advice without mentioning this requirement is providing incomplete guidance. The practical consequence: if a pharmaceutical product is approved only in Israel without EU-5 SPC protection, PTE in Israel is unavailable, regardless of how long the regulatory approval process took.



## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Israel Patent Office | https://www.gov.il/he/departments/israel_patent_office | Official patent filing procedures, forms, fees, examiner contacts |
| Patents Law 5727-1967 (WIPO Lex) | https://www.wipo.int/wipolex/en/text/495413 | Patents Law 1967 and amendments, patentability requirements, ss.18, 94-113, 132-135 |
| WIPO PCT (international filings) | https://www.wipo.int/pct/en/ | Patent Cooperation Treaty, international application routes from Israel |
| Israel Patent Office search | https://israelpatents.justice.gov.il/en | Free Israeli patent database search, published applications |
| Ministry of Justice - IP | https://www.gov.il/he/departments/units/ip_office | Trademark, design, patent policy and regulations |

## Recommended MCP Servers

These Model Context Protocol servers, available in the skills-il directory, pair well with this skill:

- **israel-law**: programmatic access to Israeli primary legislation. Use it to pull the current text of the Patents Law, 5727-1967, and its amendments when you need to confirm a section reference (for example Section 18 on the duty of disclosure and the Notice prior to Examination).
- **boi-exchange**: Bank of Israel exchange-rate data. Use it to convert ILPO fees to a foreign currency at the official rate when a foreign applicant is budgeting a filing.

Always confirm fee figures against the official ILPO portal, since the schedule is CPI-indexed and changes each year.

## Troubleshooting

**Problem**: ILPO database search returns no results for a known Israeli patent.
**Solution**: Try searching by publication number directly. The database can lag by 2-4 weeks for new publications. Also check whether the application was filed before the database's coverage start date; older patents may not be fully digitized.

**Problem**: ILPO rejected a priority document as insufficient.
**Solution**: The priority document must be a certified copy issued by the priority office. Uncertified copies, digital printouts, or WIPO DAS digital access codes may not satisfy ILPO's requirements in all cases. Confirm acceptable formats with an Israeli agent before relying on DAS.

**Problem**: Applicant is not sure whether they qualify for the 40% fee reduction (company is a subsidiary of a larger group).
**Solution**: ILPO applies the turnover test to the **applicant entity** as filed, not to a consolidated group. A wholly-owned subsidiary with its own financial statements showing under NIS 10M turnover may qualify even if the parent group is much larger. Verify with a licensed Israeli patent attorney, as this analysis can be fact-specific.

**Problem**: PCT national phase entry deadline appears to have passed.
**Solution**: Confirm the earliest priority date carefully (it may differ from the PCT filing date). Also confirm whether Israel has ratified Rule 49.6 of the PCT Regulations, which allows reinstatement of the national phase in cases of unintentional failure to meet the deadline. As of the date of this skill, ILPO does accept reinstatement petitions under Rule 49.6, but reinstatement is not guaranteed.


## References

- Israeli Patents Law, 5727-1967 (as amended): WIPO Lex https://www.wipo.int/wipolex/en/text/495413 ; Hebrew consolidated text via Nevo https://www.nevo.co.il/law_html/law01/p187_005.htm
- ILPO Official Fee Notice 2026: https://www.gov.il/BlobFolder/news/ilpo-fees/ar/news_fees-2026.pdf (dated 22 December 2025, in force 1 January 2026; CPI-indexed). Landing page: https://www.gov.il/he/pages/ilpo-fees
- ILPO portal (English): https://www.gov.il/en/departments/israel_patent_office
- ILPO 2024 Annual Report (filing-to-end-of-examination averages): see the publications listing at https://www.gov.il/he/Departments/israel_patent_office
- Patents Law (Amendment No. 15) Bill, 5786-2025, published 30 December 2025: Reinhold Cohn Group client alert, https://rcip.co.il/articles/client-alert-comprehensive-overview-of-the-proposed-israel-patent-law-amendment-no-15-2025/ ; IAM 2026 Patent Prosecution Review (Israel chapter), https://www.iam-media.com/review/the-patent-prosecution-review/2026/article/israel-essential-updates-national-prosecution-processes
- WIPO PCT Applicant's Guide, Israel Chapter (valid from 1 March 2026, ISA/IL search fee USD 1,333): https://pctlegal.wipo.int/eGuide/view-doc.xhtml?doc-code=IL
- Patent Cooperation Treaty Regulations, Rule 49.6 (reinstatement)
- Israeli Patents Regulations, 5729-1969
- See also: `/references/ilpo-fee-schedule.md`, `/references/pct-israel-checklist.md`


## Disclaimer

This skill provides informational guidance only. It does not constitute legal advice and does not create an attorney-client relationship. Israeli patent law involves jurisdiction-specific nuances, fact-specific determinations, and professional judgment. For any specific patent matter, consult a licensed Israeli patent attorney registered with the Israeli Patent Office.
