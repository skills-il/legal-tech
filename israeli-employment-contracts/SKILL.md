---
name: israeli-employment-contracts
description: Draft Israeli employment contracts (chozeh avoda) with all mandatory clauses per Israeli labor law. Use when user asks to create or generate an employment contract, calculate mandatory benefits for a contract, or asks about "chozeh avoda", "Section 14", "Saif 14", "Keren Hishtalmut", "Dmei Havra'a", "convalescence pay", "severance", "pitzuim", Israeli pension obligations, non-compete clauses in Israel, or Israeli employment compliance. Covers full-time, part-time, and contractor classification. Do NOT use for reviewing or auditing an existing contract (use israeli-employment-contract-reviewer), employee-rights questions (use israeli-workplace-rights-navigator), freelance service agreements, commercial contracts, or non-Israeli employment law.
license: MIT
allowed-tools: Bash(python:*)
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex. Python 3.8+ required for generate_contract.py script.
---

# Israeli Employment Contracts

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Instructions

### Step 1: Determine Employment Type

Ask the user what type of employment relationship they need to document:

| Type | Hebrew | Key Indicators | Contract Needed |
|------|--------|-----------------|-----------------|
| Full-time employee | avod mashara mlea | Fixed hours, employer control, tools provided | Full employment contract (chozeh avoda) |
| Part-time employee | avod mashara chelkit | Reduced hours, same rights pro-rata | Full contract with adjusted hours |
| Fixed-term employee | oved le-tkufa ktzuva | Contract with an end date | Full contract plus the end date and renewal terms. Non-renewal of a 12-month-plus term (or a shorter one renewing prior work) counts as dismissal for pregnancy protection |
| Domestic/household worker | oved meshek bayit | Cleaner, nanny, or caregiver employed directly by a household | Full contract plus the domestic-worker clauses below |
| Contractor (atzmai) | kablan atzmai | True independence, multiple clients, own tools | Service agreement (NOT this skill) |

**Contractor misclassification warning:** Israeli courts apply a multi-factor test. If a worker has fixed hours, uses employer equipment, works exclusively for one company, and receives regular monthly payments, they are likely an employee regardless of what the contract states. Misclassification exposes the employer to retroactive benefits, severance, and penalties.

### Step 1b: Domestic and Household Workers (Oved Meshek Bayit)

A salaried cleaner, nanny, or caregiver employed directly by a household is a regular employee: "עובדות ועובדים במשק בית זכאים לכל הזכויות שמוענקות לעובדים שכירים". The full contract applies, plus domestic clauses detailed in `references/household-workers.md`: the household reports and pays National Insurance on the Bituach Leumi meshek-bayit track (its own rates, paid QUARTERLY, not Step 6's monthly Form 102 rates); a signed hours log, since the burden of proving hours is on the employer; weekly rest of at least 36 hours (live-in caregivers: courts recognized at least 25); live-in caregivers whose hours cannot be supervised get a genuine global overtime payment instead of per-hour 125%/150%, while a live-out worker on a fixed schedule gets per-hour overtime; lodging and meals in kind never push cash pay below the minimum wage. A FOREIGN caregiver (permit, licensed bureau, deposit fund) is the `foreign-caregiver-payroll` skill.

### Step 2: Calculate Mandatory Benefits

All rates below are current as of 2025-2026. Verify rates annually as they may be updated by extension orders (Tzav Harchava).

**Minimum wage (Chok Schar Minimum, 1987):**
- As of 1 April 2026 the minimum wage is **6,443.85 NIS per month** for a full-time position and **35.40 NIS per hour**. The stated gross salary in any contract must meet or exceed this floor
- The minimum is updated every April (set at no less than 47.5% of the national average wage). Verify the current rate annually before finalizing a contract
- For part-time positions, the hourly minimum applies and the monthly figure is pro-rated

**Pension (mandatory per Tzav Harchava 2008):**

| Component | Employer | Employee | Notes |
|-----------|----------|----------|-------|
| Pension fund contribution | 6.5% of salary | 6% of salary | Mandatory from day 1 if the employee has prior pension coverage (money actually deposited after 3 months or at tax-year end, whichever is earlier, retroactive to day 1); otherwise only after 6 months, with nothing owed for those first 6 months |
| Severance component (within pension) | 6% minimum; 8.33% (1/12) fully funds the month-per-year rate | -- | 8.33% comes from the General Authorization under Section 14, NOT from Section 14 itself. At 6% the fund covers about 72% of the statutory figure and the balance is still owed |
| Total employer cost | Up to 14.83% | -- | If Section 14 applies |

**Pension salary base:** the extension order compels contributions only on the LOWER of the employee's base gross salary (fixed components, no overtime) and the national average wage, **13,769 NIS per month in 2026**. Above that, contributions on the full salary are owed only if the contract says so. So a contract for a 30,000 NIS salary must state which base it uses: "on the full salary" is a contractual promise beyond the statutory minimum, and silence lets the employer contribute on 13,769 only.

**Section 14 (Saif 14) arrangement:**
Section 14 is a PROHIBITION with exceptions, not a permission. It provides that a payment to a provident fund, pension fund or similar `לא יבוא במקום פיצויי פיטורים` UNLESS an applicable collective agreement so provides, or the Minister of Labour has approved it (the General Authorization, אישור כללי, י"פ תשנ"ח 4394). Since 2008 the pension extension order applies Section 14 AUTOMATICALLY to the mandatory 6% severance deposits, with no separate agreement. To apply it to the 2.33% top-up as well (8.33% in total, which fully funds the month-per-year rate), the employer notifies the fund in writing with a copy to the employee. When it applies:
- Deposits count as severance for the salary and period they cover
- On termination the employee receives the fund balance instead of calculated severance for that salary and period: in full at 8.33%; below that only for its share, the employer owing the balance
- The contract should state the fund, whether severance deposits are 6% or 8.33%, and that the 2.33% notice to the fund is given

**Statutory severance (Pitzuei Piturin, Severance Pay Law 1963):**
- Every employee gets one month's last salary per year of employment with the same employer or workplace, pro-rated for partial years. Section 12(א) by itself gives an `עובד בשכר` (hourly or daily paid) only two weeks, but the Severance Pay (Rates for a Wage Worker) Regulations, 1983, made under s.12(ב), raised it to `שכר חודש אחד לכל שנת עבודה` for all work from 1 August 1983. Never draft a two-week clause. For an hourly worker with fluctuating hours, the last salary is figured on the average position scope over the whole employment period
- If severance deposits started after day 1 (for example the 6-month pension wait), and the employment ends in circumstances that entitle the employee to severance, the employer also pays severance at the last salary for the unfunded period
- Severance is normally owed on dismissal. Some resignations are also recognized as entitling the employee to severance: a move of residence (mostly for a spouse's relocation), poor health of the employee or a family member, a tangible worsening of employment terms by the employer, and resignation within the protected window after giving birth or adoption to care for the child
- When Section 14 applies, the monthly pension/insurance deposits stand in for this statutory severance for the salary and period they cover. When Section 14 does NOT apply, the employer still owes the full Section 12 calculation on termination

**Keren Hishtalmut (education fund):**

| Component | Rate | Tax Benefit Cap |
|-----------|------|-----------------|
| Employer contribution | 7.5% of salary | Tax-exempt up to ceiling (updated annually) |
| Employee contribution | 2.5% of salary | Deducted from gross salary |
| Vesting period | 6 years (3 years for designated purposes) | -- |

**Dmei Havra'a (convalescence pay):**

| Seniority | Days Per Year | Payment |
|-----------|---------------|---------|
| Year 1 (paid only once 12 months are completed) | 5 days | Per-day rate x days |
| Years 2-3 | 6 days | Per-day rate x days |
| Years 4-10 | 7 days | Per-day rate x days |
| Years 11-15 | 8 days | Per-day rate x days |
| Years 16-19 | 9 days | Per-day rate x days |
| Year 20+ | 10 days | Per-day rate x days |

The per-day rate is updated by extension order. The private-sector rate for havra'a year 2026 (1.7.2025 to 30.6.2026) is **451.5 NIS per day**, raised from 418 by the extension order published on 18 August 2026. An employer who already paid at 418 owes the difference of 33.50 NIS for each havra'a day. The rate follows the havra'a year the payment is for, not the date it was paid.

**Annual leave (Chofsha) per Annual Leave Law:**

Seniority is counted in CALENDAR years (a year starting 1 January), not anniversaries: someone who started in October is in "year 2" the following January. Figures below are WORK days for a 5-day week (net); the statute itself counts calendar days including Fridays and Saturdays, so do not mix the two columns.

| Seniority (calendar year) | Annual Leave Law (net work days, 5-day week) | Where the Shortened Work Week extension order applies |
|-----------|---------------------------|---------------------------|
| Years 1-5 | 12 days | 12 days |
| Year 6 | 14 days | 17 days (years 6-8) |
| Year 7 | 15 days | 17 days |
| Year 8 | 16 days | 17 days |
| Year 9 | 17 days | 23 days (year 9 onward) |
| Year 10 | 18 days | 23 days |
| Year 11 | 19 days | 23 days |
| Year 12+ | 20 days | 23 days |

The Shortened Work Week extension order covers most private workplaces that moved to a 5-day week, and the employee gets whichever figure is higher. It does NOT cover, among others, workplaces with fewer than 4 employees, government and municipal companies, collectively-agreed 5-day weeks, and household workers, which fall back to the statutory column. Employees under 18 get 18 days a year regardless of seniority. These are minimums; many employers offer more. Under 200 work days in the year, the entitlement is days worked / 200 x the calendar-day figure, rounded down.

**Sick leave (Machala):**
- Accrual: 1.5 days per month of employment (18 days per year)
- Maximum accumulation: 90 days
- Payment: Day 1 unpaid, days 2-3 at 50% salary, day 4 onward at 100% salary
- Requires a medical certificate as the employer reasonably specifies (commonly from the first day of absence)
- Family illness, charged to the employee's own sick days: a child under 16, up to 8 days a year (16 for a single parent); a spouse, up to 6; a parent, up to 6

**Notice periods:**

| Seniority | Monthly-paid employee | Daily/hourly-paid employee |
|-----------|----------------------|---------------------------|
| Months 1-6 | 1 day per month worked | 1 day per month worked |
| Months 7-11 | 6 days + 2.5 days per full month from month 7 | 1 day per month worked |
| Year 2 | 1 month | 14 days + 1 day per 2 months worked in year 2 |
| Year 3 | 1 month | 21 days + 1 day per 2 months worked in year 3 |
| After 3 years | 1 month | 1 month |

The two columns differ for the first THREE years, not just the first. A monthly-paid employee earns 1 day per month for months 1-6, then 6 days plus 2.5 days for each full month from month 7, and a full month from year 2. A daily/hourly-paid employee (oved be'sachar) earns a flat 1 day per month across the first year (up to 12 days), then 14 days plus a day per two months during year 2, 21 days plus a day per two months during year 3, and a full month only after 3 years. Notice days are calendar days, and unpaid leave does not count toward seniority.

**Overtime (per Hours of Work and Rest Law):**
- Standard work week: 42 hours (since April 2018)
- Standard work day, 5-day week: 8.6 hours on four days plus one fixed short day of 7.6 hours. 6-day week: up to 8 hours a day and 7 on Friday
- First 2 overtime hours: 125% of regular hourly rate
- Additional overtime hours: 150% of regular hourly rate
- Weekly rest: at least 36 consecutive hours (typically Friday-Saturday or Saturday)

**Travel expenses (extension order):**
- Mandatory for every employee, at any position scope, for each day they need transport to work: the reduced bus fare up to 22.60 NIS a day, or a monthly pass if cheaper. Cannot be waived
- Taxable: income tax, National Insurance and health tax are withheld from it

**Hourly and daily paid workers:**
- Holiday pay (dmei chagim) after 3 months of work, for a holiday they were due to work but did not, regardless of position scope. Cannot be waived
- Annual leave only if employed at least 75 consecutive days (or under a written contract for more than 74); otherwise at least 4% of pay in lieu

### Step 3: Generate Contract Clauses

Generate bilingual contract clauses covering all mandatory provisions. Use the script for automation:

```bash
python israeli-employment-contracts/scripts/generate_contract.py \
  --employee-name "Israel Israeli" \
  --position "Software Engineer" \
  --salary 25000 \
  --start-date 2026-04-01 \
  --work-percent 100
```

The contract must include these sections:

1. **Parties** -- Employer and employee full details, ID numbers
2. **Position and description** -- Title, responsibilities, reporting line
3. **Start date and probation** -- Tkufat Nisayon, commonly 6 months (no statutory requirement). Probation never removes the notice period or pregnancy protection: dismissal for pregnancy is barred from day one, and from 6 months a pregnant employee cannot be dismissed without a permit from the Employment of Women Law supervisor, including when notice given during probation takes effect after 6 months. Any dismissal, in probation or after, requires a prior hearing (shimua) with written notice of the reasons
4. **Work hours** -- Daily/weekly hours, overtime policy
5. **Salary** -- Gross monthly amount, payment date (no later than the 9th of the following month per Protection of Wages Law)
6. **Pension and severance** -- Fund name, contribution rates, Section 14 election
7. **Keren Hishtalmut** -- Fund name, contribution rates, vesting terms
8. **Convalescence pay** -- Per seniority table, payment month
9. **Annual leave** -- Days per seniority, accrual rules
10. **Sick leave** -- Accrual rate, payment tiers, certificate requirements
11. **Notice period** -- Per seniority, mutual obligations
12. **Confidentiality** -- Scope, duration, reasonable limitations
13. **Intellectual Property** -- Assignment of work product to employer (critical for tech companies)
14. **Non-compete** -- See Step 4 for enforceability analysis
15. **General provisions** -- Governing law (Israeli law), jurisdiction (Israeli labor courts), entire agreement

See references/mandatory-clauses.md for exact bilingual clause templates.

### Step 4: Review Non-Compete and IP Sections

**Non-compete clauses in Israel -- very limited enforceability:**

Israeli courts consistently restrict non-compete clauses. The National Labor Court (particularly the Check Point ruling, ע"ע 164/99 Frumer and Check Point v. Radguard, and subsequent case law) held that a restriction on post-employment work is generally void, and is given effect only if it is reasonable AND at least ONE of these circumstances exists (an open list, and even then the court weighs the whole case):

1. A genuine trade secret of the employer (not the employee's general know-how), with a real probability it would be misused
2. A special, costly investment in the employee's training (not training gained in ordinary work)
3. Special consideration paid for the restriction itself (for example a dedicated grant or salary supplement)
4. A duty of good faith or fiduciary duty that justifies it

Freedom of occupation (Basic Law: Freedom of Occupation, and Human Dignity and Liberty) prevails where none applies.

**Practical guidance:**
- Duration: as short as the protected interest justifies
- Scope: Must be narrowly defined (specific competitors, specific field)
- Geography: Israel-wide restrictions are disfavored; global restrictions almost never enforced
- Recommendation: Use robust confidentiality clauses instead, which are far more enforceable

**Intellectual Property assignment:**
- Default rule: the employer owns an employee's service invention and a work made for and during the work, unless agreed otherwise. The s.132 test is causal (as a result of and during the service), not job description or hours. A contractor keeps copyright absent assignment (s.35)
- Patent Law Section 132: a service invention (reached as a result of and during the service) belongs to the employer. Absent an agreement on compensation, the Compensation and Royalties Committee decides it (s.134), so state them expressly
- Copyright Law 2007, Section 34: the employer is first owner of a work the employee made for and during the work
- An explicit IP clause still sets the scope (side projects, pre-existing IP) and the s.134 terms
- Consider including a pre-existing IP disclosure schedule

### Step 5: Compliance Checklist Before Signing

Run through this checklist before finalizing any employment contract:

- [ ] Written notice of employment terms given (Notice to Employee and Job Candidate (Employment Conditions and Screening and Hiring Procedures) Law, 5762-2002); a contract serves as the notice only if it contains every detail the Law lists
- [ ] All mandatory benefits included (pension, convalescence, leave, sick days)
- [ ] Section 14 terms stated (6% or 8.33% severance deposits) and, for 8.33%, the written notice to the fund given
- [ ] Travel expenses clause; for hourly/daily workers, holiday pay
- [ ] Keren Hishtalmut terms specified (if offered -- not mandatory but very standard in tech)
- [ ] Work hours and overtime policy clearly stated
- [ ] Notice period matches statutory minimum or better
- [ ] Salary meets or exceeds minimum wage (verify current rate)
- [ ] Payment date specified (by the 9th of following month)
- [ ] Non-compete clause reviewed for enforceability (see Step 4)
- [ ] IP assignment clause included (for tech roles)
- [ ] Probation period terms clear (if applicable)
- [ ] Contract language: Must be in a language the employee understands; bilingual (Hebrew + English) recommended

### Step 6: Post-Signing Obligations

After the contract is signed, the employer must complete:

1. **Employer file and Bituach Leumi (National Insurance Institute):**
   - A first-time employer opens a deductions file (tik nikuyim) with the Tax Authority; Bituach Leumi receives it from the Tax Authority and opens the matching employer file automatically. There is no separate per-employee "registration within 7 days" with Bituach Leumi
   - Report and pay monthly by the 15th for the previous month on Form 102. Form 126 is the semi-annual and annual employer report (by 18 July and 18 January, plus the annual return), not the monthly one
   - Employer pays 4.51% on the part of the salary up to 7,703 NIS and 7.6% on the part from 7,703 to 51,910 NIS (2026 brackets)

2. **Pension fund enrollment:**
   - Enroll employee in chosen pension fund
   - Deposit within 7 business days of paying the salary, or within 15 days after the end of the month the money is for, whichever is earlier
   - For employees with no prior pension: entitlement starts after 6 months. With prior pension coverage: from day 1, deposited after 3 months (or at tax-year end) retroactively

3. **Tax Authority (Mas Hachnasa) reporting:**
   - Employee must submit Form 101 (employee tax declaration) within 7 days of starting work or of receiving the first salary, whichever is earlier, and a new one within 7 days of any change in personal details
   - Employer responsible for income tax withholding per tax brackets
   - Report new employee to Tax Authority

4. **Provide written notification:**
   - Per the Notice to Employee and Job Candidate (Employment Conditions and Screening and Hiring Procedures) Law, 5762-2002 (formerly the Notification to Employee Law), the employer must provide written details of employment terms within 30 days of start

5. **Record keeping:**
   - Maintain attendance records (Hours of Work and Rest Law)
   - Keep payslips so the employee can get printed payslips for at least 7 years back
   - Retain the contract copy during employment and after it ends

## Examples

### Example 1: Standard Tech Employee Contract
User says: "Create an employment contract for a senior developer, 30,000 NIS monthly salary, starting next month"
Actions:
1. Determine: Full-time employee, tech sector
2. Calculate: Pension 6.5%/6% on the full salary if the contract promises it (1,950/1,800 NIS); the statutory minimum is on 13,769 NIS only (895/826 NIS), so state the base explicitly. Keren Hishtalmut 7.5%/2.5% (2,250/750 NIS), 5 Dmei Havra'a days (first year)
3. Generate: Full contract with Section 14 arrangement, IP assignment, limited non-compete
4. Review: Flag non-compete for scope review, ensure IP clause covers software
5. Checklist: All 12 mandatory items verified
6. Post-signing: deductions file and monthly Form 102, pension enrollment, Form 101
Result: Complete bilingual employment contract ready for legal review and signing.

### Example 2: Part-Time Employee
User says: "I need a contract for a part-time marketing person, 3 days a week, 15,000 NIS"
Actions:
1. Determine: Part-time employee (60% position, mashara chelkit)
2. Calculate: All benefits pro-rata. If 15,000 is the actual pay for the 3-day role, pension is statutorily on 13,769 (the average wage) unless the contract says full salary, and the script takes the FULL-TIME equivalent (`--salary 25000 --work-percent 60`). Leave days proportional to days worked; havra'a pro-rated to 60%
3. Generate: Contract specifying 3 work days, which days, daily hours
4. Review: Ensure part-time rights clearly stated (same hourly benefits as full-time)
Result: Part-time contract with pro-rata benefits correctly calculated.

### Example 3: Drafting a Contract from an Existing Draft
User says: "Here is a rough offer letter, turn it into a full employment contract"
Actions:
1. Parse: Read the offer letter for the terms already agreed (role, salary, start date, work percentage)
2. Build: Generate the full contract using Step 3, filling every mandatory section the offer letter omitted (Section 14 election, pension fund, Keren Hishtalmut, convalescence, leave, sick days, notice period, IP assignment)
3. Calculate: Apply current benefit rates from Step 2, verifying the gross salary meets the minimum wage floor
4. Checklist: Run Step 5 to confirm all mandatory items are present
Result: A complete bilingual employment contract built from the partial draft, ready for legal review and signing. For an independent audit of someone else's draft, use `israeli-employment-contract-reviewer`.

### Example 4: Contractor vs. Employee Assessment
User says: "I have someone working for me full-time from our office, should they be a contractor or employee?"
Actions:
1. Apply: Multi-factor test -- fixed location (employer's office), full-time hours, likely uses employer equipment
2. Assess: Strong indicators of employment relationship, high misclassification risk
3. Present: the indicators pointing to an employment relationship; the labor court decides by substance, not by the contract label. Offer an employment contract
4. Warn: Misclassification liability includes retroactive benefits, severance, Bituach Leumi penalties
Result: The classification indicators, the misclassification risk, and next steps.

### Example 5: Salaried Nanny Employed by a Household
User says: "We are hiring a nanny 4 days a week, draft the employment contract"
Actions: Draft the full contract, then add the Step 1b domestic clauses: Bituach Leumi meshek-bayit registration, a signed hours log (the burden of proof is on the household), and the 36-hour weekly rest. She is a local salaried worker, so foreign-caregiver rules do not apply.

## Bundled Resources

### Scripts
- `scripts/generate_contract.py` -- Generates an Israeli employment contract template with calculated benefit rates. Accepts employee details (name, position, salary, start date, work percentage) and outputs a structured contract with all mandatory Israeli clauses pre-filled. Includes Section 14 arrangement text, pension and Keren Hishtalmut rates, and notice period calculations. Run: `python scripts/generate_contract.py --help`

### References
- `references/labor-law.md` -- Comprehensive summary of Israeli labor laws governing employment contracts: Severance Pay Law (1963), Annual Leave Law (1951), Sick Pay Law (1976), Hours of Work and Rest Law (1951), the Notice to Employee and Job Candidate (Employment Conditions and Screening and Hiring Procedures) Law, 5762-2002, Protection of Wages Law (1958), and key extension orders (Tzav Harchava). Consult when verifying statutory requirements or resolving disputes about employee entitlements.
- `references/household-workers.md` -- Domestic and household worker clauses: Bituach Leumi household-employer track, hours log and burden of proof, weekly rest, live-in caregivers and overtime, live-in vs live-out.
- `references/mandatory-clauses.md` -- Bilingual (Hebrew and English) employment contract clause templates covering all mandatory provisions: parties, position, salary, pension with Section 14, Keren Hishtalmut, convalescence pay, leave, sick days, notice period, confidentiality, IP assignment, and non-compete. Consult when drafting or reviewing specific contract sections.

## Gotchas

- Israeli non-compete clauses are nearly unenforceable unless very narrowly scoped. Agents trained on US employment law will draft broad non-competes that Israeli courts routinely strike down. Always prefer robust confidentiality clauses instead.
- Section 14 (Saif 14) of the Severance Pay Law is Israel-specific and has no equivalent in US or European law. Agents unfamiliar with it will omit this critical clause, leaving employers exposed to double severance liability.
- The mandatory pension contribution rates (employer 6.5%, employee 6%) are set by extension order and change periodically. Agents may use outdated rates from their training data. Always verify against the current Tzav Harchava.
- IP ownership is not ambiguous without a clause: ss.132 and 34 vest service inventions and works made for the job in the employer. Draft for scope and s.134 terms; any own-time carve-out must be subject to s.132.
- The convalescence pay (Dmei Havra'a) rate for havra'a year 2026 is 451.5 NIS/day, raised from 418 by the extension order of 18 August 2026. An employer who paid at 418 owes 33.50 NIS per havra'a day.
- Annual leave tables in training data often mix calendar-day and work-day figures (e.g. "16 days in year 5"). For a 5-day week the statutory minimum is 12 WORK days through year 5; 16 is the calendar-day figure. Never write a calendar-day number into a work-day clause.
- Section 14 only covers severance for the salary and period its deposits cover. If deposits start mid-employment, the earlier period still owes severance at the last salary; do not present a mid-tenure Section 14 arrangement as wiping out prior-year severance liability.
- Hourly and daily workers are owed one month's severance per year since 1983, not the two weeks in Section 12(א). An agent reading the statute alone will halve their severance.

## Troubleshooting

### Error: "Missing mandatory clause"
Cause: Contract is missing one or more legally required provisions (pension, convalescence, leave, etc.)
Solution: Run through the compliance checklist in Step 5. Add missing clauses using templates from references/mandatory-clauses.md.

### Error: "Non-compete clause too broad"
Cause: Non-compete exceeds enforceable scope under Israeli case law
Solution: Tie it to one of the recognized circumstances in Step 4, shorten it, name specific competitors, limit geography. Consider replacing with a stronger confidentiality clause per Step 4 guidance.

### Error: "Section 14 not properly documented"
Cause: The contract does not say whether severance deposits are 6% or 8.33%, or the 2.33% top-up was never notified to the fund
Solution: The 6% is covered automatically by the pension extension order. For 8.33%, include the Section 14 clause with the fund details and send the written notice to the fund with a copy to the employee. See references/mandatory-clauses.md for template.

### Error: "Salary below minimum wage"
Cause: Stated salary falls below the current Israeli minimum wage
Solution: Verify current minimum wage rate (updated periodically by government order). For part-time employees, calculate the hourly equivalent to ensure compliance.

### Error: "Missing Bituach Leumi registration"
Cause: A first-time employer never opened a deductions file, so no monthly Form 102 reports or payments were made for the employee
Solution: Open the deductions file with the Tax Authority (Bituach Leumi opens its file from that automatically) and report and pay the missed months. An employer who fails to register may be sued by Bituach Leumi to repay benefits it paid or will pay to the employee.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kol Zchut: personal employment contract | https://www.kolzchut.org.il/he/%D7%97%D7%95%D7%96%D7%94_%D7%A2%D7%91%D7%95%D7%93%D7%94_%D7%90%D7%99%D7%A9%D7%99 | Plain-language explanation of contract terms and mandatory clauses |
| Kol Zchut: employment and workers' rights portal | https://www.kolzchut.org.il/he/תעסוקה_וזכויות_עובדים | Employment rights hub: wage components, terms, sickness, leave, end of employment |
| Nevo: Notice to Employee Law full text | https://www.nevo.co.il/law_html/law00/71702.htm | Notice to Employee and Job Candidate Law, 5762-2002 statutory text |
| Kol Zchut: Severance Pay (Pitzuei Piturin) | https://www.kolzchut.org.il/he/פיצויי_פיטורים | Severance Pay Law, 1963 explained (Section 14, calculation, payment deadline) |
| Bituach Leumi: employer registration | https://www.btl.gov.il/Insurance/Maasik/MToshavYisrael/Pages/PtichatTik.aspx | Opening an employer deductions file with National Insurance |
| Bituach Leumi: reporting a domestic worker | https://www.btl.gov.il/Insurance/National%20Insurance/type_list/House_keeper/Pages/divuachVetashlum.aspx | Household-employer (meshek bayit) reporting and payment track for a domestic worker |
| Kol Zchut: domestic workers' rights | https://www.kolzchut.org.il/he/זכותון_עובדים_במשק_בית_%28עוזרות_בית_ומטפלים/ות%29 | Rights of cleaners, nannies, and caregivers; employer duty to report to Bituach Leumi |
| Kol Zchut: Form 101 | https://www.kolzchut.org.il/he/טופס_101 | Employee tax declaration form (kartis oved) for new hires |

## Recommended MCP Servers

| MCP | When to pair | Purpose |
|-----|--------------|---------|
| `israel-law` | For authoritative citations to statute text | Looks up the exact text of the Severance Pay Law, Annual Leave Law, Hours of Work and Rest Law, and the Notice to Employee Law |
| `kolzchut` | For plain-language rule summaries and exceptions | Cross-references contract clauses against the All-Rights (Kol Zchut) database |

The skill works without these MCPs using the built-in reference tables, but the citations become less specific.
