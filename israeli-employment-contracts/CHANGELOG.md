# Changelog

## [1.4.2] - 2026-10-25

### Fixed
- IP ownership: the skill said Israeli law has no automatic work-for-hire and that ownership without an IP clause is ambiguous. By default the employer owns a service invention (Patents Law s.132) and a work an employee made for and during the work (Copyright Law s.34), unless agreed otherwise. Neither rule covers work outside the job, and a contractor keeps copyright absent assignment (s.35). An explicit IP clause sets the scope (side projects, pre-existing IP) and the s.134 compensation terms.
- The IP clause template and generator no longer claim work merely because Employer resources were used, or deem unlisted pre-existing IP assigned. They now cover work made for the purposes of and during the employment plus service inventions; pre-existing IP stays the employee's, under a licence placeholder.

## [1.4.1] - 2026-10-25

### Fixed
- The Section 14 clause (template, generator and the Step 2 summary) said deposits are "full and complete" severance. They replace severance in full only at 8.33%; at 6% they replace it only in proportion (about 72%), and the balance stays owed.
- Monthly-paid notice rows relabelled months 7-11: a full month applies from 12 completed months, as the Prior Notice Law says. For an hourly worker, 12 completed months is already the second year (14 days).
- Leave under 200 work days now states the formula: days worked / 200 x the calendar-day entitlement, rounded down.

### Added
- A hearing (shimua) is required before any dismissal, including during probation.
- Patents Law s.134: without an agreement on service-invention compensation, the Compensation and Royalties Committee decides it. The IP clause now has a placeholder for the agreed terms.
- The 6-day-week statutory leave table, in references/labor-law.md.

## [1.4.0] - 2026-10-25

### Fixed
- Annual leave table mixed calendar days with work days (it said 16 days in year 5, 18 in year 6, 21 from year 7). For a 5-day week the Annual Leave Law gives 12 work days through year 5, then 14, 15, 16, 17, 18, 19 and 20 from year 12; where the Shortened Work Week extension order applies the figures are 12, then 17 for years 6-8 and 23 from year 9, and the employee gets the higher. Seniority counts in calendar years. Fixed in SKILL.md, SKILL_HE.md, both references and the contract generator.
- Notice for a daily or hourly paid employee did not reach a full month after one year. Year 2 is 14 days plus a day per two months worked in year 2, year 3 is 21 days plus a day per two months, and a full month only after 3 years. Fixed in the tables, the clause template and the generator, which also no longer rounds the monthly-paid 2.5-day steps down.
- Severance for an hourly or daily paid employee was stated as two weeks per year (the 1.3.0 change). The Severance Pay (Rates for a Wage Worker) Regulations, 1983, made under section 12(ב), set it at one month per year for all work since 1 August 1983, so every employee gets one month per year.
- Travel expenses were described as optional and tax-exempt. Under the extension order they are mandatory at any position scope (reduced bus fare up to 22.60 NIS a day, or a monthly pass if cheaper), cannot be waived, and are taxable.
- Section 14 was described as needing a signed consent. Since 2008 the pension extension order applies it automatically to the mandatory 6%; the 2.33% top-up needs a written notice to the fund with a copy to the employee. Severance for any unfunded period (such as the 6-month pension wait) is still owed.
- The 5-day work day is 8.6 hours on four days plus one 7.6-hour short day, not 8.4 hours. Child-illness absence is up to 8 days (16 for a single parent), not 6. The non-compete test is "reasonable and one of an open list of circumstances" (Check Point), not four cumulative conditions.
- Post-signing steps said to register each new employee with Bituach Leumi within 7 days and report monthly on Form 126. A new employer opens a deductions file with the Tax Authority and Bituach Leumi opens its file automatically; the monthly report and payment is Form 102 by the 15th, and Form 126 is the semi-annual and annual report. The 7-day deadline belongs to Form 101.

### Added
- Pension salary base: mandatory contributions apply only to the lower of base salary and the national average wage (13,769 NIS in 2026) unless the contract promises more, with a matching clause placeholder.
- Holiday pay for hourly and daily paid workers after 3 months; the 75-day rule for their annual leave; family-illness sick days; pregnancy protection against the probation clause; a fixed-term contract row; 18 leave days for employees under 18; a travel and holiday-pay clause and an hourly-rate option in the clause templates.
- The household-worker clauses moved to references/household-workers.md, with a summary kept in Step 1b.
- Pension deposit deadline (7 business days after paying salary or 15 days after month end, whichever is earlier), the 2026 National Insurance brackets (7,703 and 51,910 NIS), and that convalescence pay is owed only after a full year.

## [1.3.0] - 2026-08-30

### Fixed
- Section 14 of the Severance Pay Law was stated as a permission. It is a prohibition with exceptions: a payment to a pension or provident fund does NOT replace severance unless an applicable collective agreement so provides or the Minister of Labour approved it, in practice through the General Authorization (י"פ תשנ"ח 4394). The 8.33% full-funding rate comes from that Authorization, not from section 14.
- Section 12 sets TWO severance rates and only one was stated. An עובד במשכורת (pay computed on a monthly or longer basis) gets one month per year; an עובד בשכר (hourly or daily) gets two weeks per year, and section 12(ב) lets the Minister raise that by regulation. Stating only the month rate overstates what an hourly worker is owed.
- Re-sourced both claims from a secondary rights summary to the statute itself.

All notable changes to this skill are documented here.

## [1.2.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.
