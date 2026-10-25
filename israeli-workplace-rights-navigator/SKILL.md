---
name: israeli-workplace-rights-navigator
description: Understand and exercise employee rights under Israeli labor law, including vacation days (chofsha), sick leave (machala), overtime pay, the Birth and Parenting Period and paternity leave, severance pay (pitzuyim), convalescence pay (dmei havra'a), minimum wage, and pension contributions. Use when user asks about "employee rights in Israel", "how many vacation days", "sick pay Israel", "pitzuyei piturim", "dmei havra'a", "minimum wage Israel", "shaat nosafot", or "zchuyot ovdim". Covers Annual Leave Law, Sick Pay Law, Hours of Work and Rest Law, Employment of Women Law, Severance Pay Law, and Minimum Wage Law. Do NOT use for drafting an employment contract (use israeli-employment-contracts), reviewing or auditing an existing employment contract (use israeli-employment-contract-reviewer), salary negotiation (use israeli-tech-salary-negotiator), reserve duty rights (use israeli-miluim-manager), or freelancer operations (use israeli-freelancer-ops).
license: MIT
allowed-tools: Bash(python:*)
compatibility: No special requirements. Works with Claude Code, Cursor, Windsurf.
---

# Israeli Workplace Rights Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


Understand and exercise employee rights under Israeli labor law: vacation, sick leave, overtime, birth and parenting leave, severance, convalescence pay, pension, termination protections, harassment prevention, and disability accommodations.

## Instructions

### Step 1: Identify the Employee's Situation

Before providing guidance, determine the employee's circumstances:

| Factor | Options | Impact |
|--------|---------|--------|
| Employment type | Full-time, part-time, shift-based | Affects overtime and vacation calculations |
| Seniority | Years of continuous employment with current employer | Determines vacation days and convalescence days |
| Sector | Private, public, unionized (heskemim kibbutziyim) | Collective agreements may provide better terms |
| Reason for inquiry | Entitlement question, dispute, termination, harassment | Determines which laws and procedures apply |
| Monthly salary | Base salary (maskoret basis) | Needed for severance, overtime, and benefit calculations |

All entitlements below are **minimum legal requirements**. Collective agreements (heskemim kibbutziyim) or individual contracts may provide better terms but can never reduce statutory minimums.

### Step 2: Vacation Days (Chofsha Shnatit)

Per the **Annual Leave Law, 1951 (Chok Chufsha Shnatit)**, paid vacation rises with seniority. The statute counts GROSS days, which include the weekly rest days, so the days an employee can actually take off depend on the work week. Most 5-day workplaces are also covered by the shortened-work-week extension order (tzav harchava, maavar leshavua avoda mekutzar), which states NET days and is more generous; the employee gets the higher of the two.

| Years | Gross (statute) | 6-day week: actual days | 5-day week, statute only | 5-day week, extension order |
|-------|-----------------|--------------------------|--------------------------|-----------------------------|
| 1-5 | 16 | 14 | 12 | 12 |
| 6 | 18 | 16 | 14 | 17 |
| 7 | 21 | 18 | 15 | 17 |
| 8 | 22 | 19 | 16 | 17 |
| 9 | 23 | 20 | 17 | 23 |
| 10 | 24 | 21 | 18 | 23 |
| 11 | 25 | 22 | 19 | 23 |
| 12 | 26 | 23 | 20 | 23 |
| 13 | 27 | 24 | 20 | 23 |
| 14+ | 28 | 24 | 20 | 23 |

**Key rules:**
- The extension-order column applies to most 5-day workplaces. It does NOT cover domestic work, workplaces with fewer than 4 employees, government or municipal companies, or workplaces whose move to a 5-day week was settled by a collective agreement; those use the statute-only column
- Seniority is counted in calendar years (January to December): someone who started in October has year 2 from the next 1 January
- Accrual is the same for full and partial work days. A full-year employee who worked fewer than 200 days gets a proportional share of the gross days, rounded down
- Working youth (under 18) get 18 calendar days a year regardless of seniority: 14 days off on a 5-day week, 16 on a 6-day week
- Unused vacation days can carry forward with employer consent, typically over the next two years of employment; beyond that the employer may require the employee to use them
- The employer sets the vacation schedule but must consider the employee's requests. The employee must receive at least 7 consecutive days per year if requested
- Collective agreements (heskemim kibbutziyim) in sectors and many individual contracts grant more generous leave than the table above

**Vacation pay:**
- The employee receives their regular salary during vacation
- Unused vacation days must be paid out (pidyon chufsha) upon termination

Emergency and reserve-duty carry-forward is an exception to the employer-consent rule; see the reference file.

### Step 3: Sick Leave (Yemei Machala)

Per the **Sick Pay Law, 1976 (Chok Dmei Machala)**, employees accrue sick days and receive graduated pay:

**Accrual:**
- 1.5 sick days per month of employment (18 days per year)
- Maximum accumulation: 90 days total (unless a collective agreement provides more)

**Pay during sick leave:**

| Sick Day | Pay Rate |
|----------|----------|
| Day 1 | 0% (unpaid) |
| Days 2-3 | 50% of daily wage |
| Day 4 onward | 100% of daily wage |

**Key rules:**
- A medical certificate (ishur machala) is required from the first day of absence
- Sick days can be used for the employee's own illness or a child's illness. The child-illness quota is up to 8 days per year for a child under 16, and it is PER PARENT, not per child: a parent of five children still has 8 days, and the quota does not scale with part-time hours. The second parent has their own quota only where they also work AND did not take leave for the child on the same days, so do not promise a household 8 + 8. Where the child has a serious illness or a permanent disability the quota is 18 days per year, not 8
- An employer cannot fire an employee during sick leave for the first 90 days of accumulated sick days
- Unused sick days are not paid out upon termination (unless a specific agreement states otherwise)

A short absence may be covered by an HMO short sick certificate, no doctor's visit; see the reference file.

### Step 4: Overtime Pay (Shaat Nosafot)

Per the **Hours of Work and Rest Law, 1951 (Chok Sha'ot Avoda U'Menucha)**:

**Standard work hours:**
- Regular work day (private sector): on a 5-day week 8.6 hours on four days and 7.6 on the short day; on a 6-day week 8 hours, 7 on Friday. Overtime starts above these, or above 42 hours a week. The public sector works a 40-hour week
- Maximum work week: 42 hours
- Weekly rest day: at least 36 consecutive hours (typically Friday evening to Saturday evening for Jewish employees)

**Overtime rates:**

| Overtime Hours | Pay Rate |
|----------------|----------|
| First 2 overtime hours in a day | 125% of hourly wage |
| Beyond 2 overtime hours in a day | 150% of hourly wage |
| Work on weekly rest day (Shabbat), ordinary hours | 150% of hourly wage |
| First 2 overtime hours on the weekly rest day | 175% of hourly wage |
| Each overtime hour beyond the first 2 on the weekly rest day | 200% of hourly wage |

**Key rules:**
- Rest-day and overtime premiums stack on the ordinary wage, capped at 200%, so a long Shabbat shift is never a flat 150%
- Those rest-day rates are the hourly or daily employee's full rate. A monthly salaried employee gets a 50% addition to the daily wage instead, plus paid compensatory rest. Detail in `references/entitlements-calculator.md`
- Under the general overtime permit of 14 March 2018: no more than 16 overtime hours in a work week
- Total work day, including overtime, cannot exceed 12 hours
- Overtime must be compensated in pay, not comp time (unless a valid collective agreement allows it)
- Certain sectors and positions (managers, those requiring a high degree of personal trust) may be exempt from overtime rules under specific legal conditions
- The employer must keep accurate records of work hours
- Holiday (chag) work is not the rest-day premium: 150% (a monthly employee gets +50% of the daily wage) plus a substitute rest day. Separately, hourly and daily employees with 3 months' service get holiday pay (dmei chagim) for holidays they do not work, and one made to work the holiday gets both, 250% in total
- A global overtime payment (gmul globali) is lawful only if agreed, genuine, shown separately on the pay slip, and matched to the overtime actually worked; hours beyond it are still owed
- Employing a youth on the weekly rest day is prohibited outright, but the employer still owes the overtime premium for those hours
- Detail on all three: `references/entitlements-calculator.md`

**Minimum wage (Chok Schar Minimum, 1987):**
- As of 1 April 2026 the minimum wage is **6,443.85 NIS per month** for a full-time position and **35.40 NIS per hour**
- The monthly minimum is updated each April; verify the current rate annually
- For part-time employees the hourly minimum applies and the monthly figure is pro-rated
- Employees under 18 and apprentices have their own lower minimum, set as a percentage of the adult monthly figure under the Minimum Wage Regulations (Working Youth and Apprentices), 1987: 70% up to age 16, 75% up to 17, 83% up to 18, and 60% for an apprentice (chanich). A youth full-time week is 40 hours and the youth hourly rate is the youth monthly figure divided by 173, not 182. Shekel figures per band, the birthday-month split and the apprentice definition are in `references/entitlements-calculator.md`
- Paying below the minimum wage exposes the employer to criminal penalties and civil liability; the floor cannot be waived in a contract

### Step 5: Birth and Parenting Period and Paternity Leave (Tkufat Leidah VeHorut)

Per the **Employment of Women Law, 1954 (Chok Avdat Nashim)**. The leave is now officially called the **Birth and Parenting Period (tkufat leidah vehorut)**, not "maternity leave" (chofshat leidah); the older term is still common in everyday speech.

**Birth and Parenting Period (the parent who gave birth):**
- Total duration: 26 weeks from the date of birth
- Paid portion: 15 weeks of birth allowance (dmei leidah) from Bituach Leumi, on national insurance for at least 10 of the 14 months, or 15 of the 22 months, before the work stoppage
- At least 6 of the 14 months but not enough for the full allowance gives a partial allowance of 56 days (8 weeks)
- The remaining weeks (11 or 18) are unpaid leave
- The daily birth allowance equals the employee's average daily wage, capped at a statutory maximum of NIS 1,752.33 per day in 2026
- The employee can start leave up to 7 weeks before the due date (deducted from the 26 weeks)
- **Complex-disability extension (from 1 April 2026):** a parent of a child born with a complex disability recognized by Bituach Leumi is entitled to an additional 5 paid weeks. Total extension periods of the birth allowance are capped at 20 weeks combined

**Job protection:**
- Under the Employment of Women Law s.9(a), from 6 months of tenure the employer cannot dismiss a pregnant employee or cut her position scope without a Ministry of Labor permit, whatever the reason
- Below 6 months no permit is needed, but dismissal because of the pregnancy is still unlawful discrimination under the Equal Employment Opportunities Law and can be challenged on that ground
- No dismissal for 60 days after the Birth and Parenting Period ends, and the employee returns to the same or an equivalent position

**Paternity leave / second parent (the parent who did not give birth):**
- Up to 5 calendar days right after the birth (plus the birth day), no employer consent needed
- Plus one concurrent week of the Birth and Parenting Period with a birth allowance from Bituach Leumi
- May take a longer transferred share after the other parent has used at least 6 weeks

See `references/labor-laws-summary.md` for how the 5 days are charged (vacation vs sick) and the full transfer rules.

**Additional protections:** fertility treatments, adoption, nursing mothers (1 hour less per day for 4 months, full pay), and the same protected period after a miscarriage, where a cut in hours breaches the law. Conditions in `references/labor-laws-summary.md`.

### Step 6: Severance Pay (Pitzuyei Piturim)

Per the **Severance Pay Law, 1963 (Chok Pitzuyei Piturim)**:

**Entitlement:**
- One month's salary per year of employment (or proportional for partial years)
- Applies after at least 1 year of continuous employment with the same employer
- "Month's salary" means the last monthly salary (maskoret akhronah), including all fixed components

**Calculation:**
```
Severance = Last Monthly Salary x Years of Employment
```

For variable components or salary changes, use:
```bash
python3 scripts/severance-calculator.py --help
```

**When severance is owed:**
- Employer-initiated termination (piturim)
- Employee resignation due to health, relocation for marriage, or materially worsened conditions. CRITICAL on the last: the employee must FIRST give written notice and a real chance to correct. Resigning without that forfeits the severance entirely (in certain cases recognized by law)
- A parent who resigns within 9 months of the birth (or of receiving a child for adoption, surrogacy or foster care) to care for the child: treated as dismissal (a father or second parent only under extra conditions)
- Death of the employee (paid to the survivors) or of an individual employer
- Employer bankruptcy

**Section 14 arrangement:**
- Section 14 is a prohibition, not a permission: fund contributions replace severance only under a collective agreement or the General Authorization (י"פ תשנ"ח 4394)
- Under this arrangement, the accumulated fund replaces the obligation to pay severance separately
- Two severance rates get confused and the gap is money. The minimum is **6%**, and **8.33%** (1/12) fully funds the statutory month-per-year, the rate a FULL release requires (from the General Authorization, not Section 14). At 6% the fund covers about 72%, so a **completion payment (hashlamat pitzuyim)** is owed. Read the deposit rate off the pay slip
- Upon termination, the employee receives the fund balance, plus the completion where deposits were below 8.33%; fund returns never offset that completion

**Tax exemption on severance:**
- Severance pay is exempt from income tax up to a ceiling per year of tenure. The 2026 ceiling is **13,750 NIS per year of employment** (the exempt amount is the lower of this figure times years of service, or 1.5 times the last monthly salary times years of service). Verify the current ceiling, which is updated annually
- Severance above the exemption ceiling is taxable; the employee can request tax-spreading (perisat mas) to reduce the tax

**Key rules:**
- Severance must be paid within 15 days of termination
- Late payment accrues penalty interest (pitzuyei halanat pitzuyim)
- An employee who resigns is generally not entitled to severance, except in specific circumstances

Severance usually sits in a pension fund; getting it out has its own paperwork chain and an irreversible tax election. Before quoting an amount, walk the termination workflow in the reference file.

### Step 7: Convalescence Pay (Dmei Havra'a)

Every employee who has completed at least one year of employment is entitled to annual convalescence pay.

**Number of convalescence days by seniority:**

| Years of Employment | Convalescence Days |
|---------------------|-------------------|
| 1 | 5 days |
| 2-3 | 6 days |
| 4-10 | 7 days |
| 11-15 | 8 days |
| 16-19 | 9 days |
| 20+ | 10 days |

**Daily rate:**
- Updated by extension order. The private-sector rate for havra'a year 2026 (1.7.2025 to 30.6.2026) is NIS 451.5 per day, raised from 418; an employer who paid at 418 owes NIS 33.50 per havra'a day. The rate follows the havra'a year, not the payment date. Public sector: NIS 511.6.
- Rate updated on 18.08.2026, retroactive to 1.7.2025. Public-sector employees also get MORE days than the table above, by grade (Takshir ch. 28.2)
- In 2024 and 2025 a temporary statute (Freeze and Reduction of Convalescence Pay Law) made employers deduct one convalescence day and pass it to the Tax Authority for reservist benefits; domestic workers of a private individual were excluded. No such law was found for 2026, so do not apply the deduction to 2026 without checking

**Payment:**
- Usually paid once a year, typically in June-September
- Appears as a separate line on the pay slip (tlush maskoret)
- Subject to income tax, national insurance and health tax, but not part of the wage for pension deposits or for severance
- Part-time employees receive proportional pay based on their work percentage

### Step 8: Pension and Savings (Pnsia)

Since the **Mandatory Pension Law extension order (Tzav Harchava, 2008)**:

**Mandatory contribution rates (as of 2026):**

| Component | Employee Contribution | Employer Contribution |
|-----------|----------------------|----------------------|
| Pension savings | 6% of salary | 6.5% of salary |
| Severance | 0% | 6% minimum (8.33% where a full Section 14 arrangement applies) |
| Disability insurance | Included in employer's 6.5% | Included in employer's 6.5% |

**Key rules:**
- Applies to all employees after 6 months of employment for those without prior pension coverage (contributions are then paid retroactively to day 1), or immediately if the employee already has a pension fund
- The employee chooses the fund (keren pensia, bituach menahalim, or kupat gemel)
- Contributions are calculated on the gross salary up to the maximum insurable salary

**Tax benefit on the employee's 6% contribution (Section 45a):**
- The employee's 6% pension contribution qualifies for a 35% income-tax credit under Section 45a of the Income Tax Ordinance
- The credit is applied automatically by the payroll system on the pay slip, subject to the annual ceiling (approximately NIS 8,148 in 2026)
- A pay slip showing the 6% deduction with no matching credit line may entitle the employee to a retroactive correction. Employee contributions above 7% of salary earn no credit

### Step 9: Termination Procedures (Halichei Piturim)

Israeli law requires specific procedures before terminating an employee:

**Notice period (hodaa mukdemet):**

| Employment Duration | Notice Period |
|--------------------|---------------|
| First 6 full months | 1 day per month worked |
| 7 to 11 full months | 6 days + 2.5 days per full month after the 6th |
| 12 full months and more | 1 month |

Month-by-month figures, including the separate scale for hourly and daily employees: `references/entitlements-calculator.md`.

**Pre-termination hearing (shima):**
- The employer must hold a hearing before deciding, after advance written notice stating the reasons under consideration, and must genuinely weigh the employee's answer
- The employee may bring a representative (union rep, lawyer, or colleague). Failure to hold a proper hearing can render the termination unlawful

**Protected employees:**
- Pregnant women with at least 6 months of tenure: cannot be terminated without a permit from the Ministry of Labor (Employment of Women Law s.9(a)). Below 6 months no permit is needed, but a dismissal because of the pregnancy is still unlawful discrimination
- Employees on sick leave: protected during the first 90 days of accumulated sick leave
- Employees on the Birth and Parenting Period: protected during leave and for 60 days after
- Employees on reserve duty (miluim): protected during the service and 30 days after (60 after long Swords of Iron call-ups); dismissal in the window needs committee approval. Windows and approvals: israeli-miluim-manager
- Employees who filed complaints (e.g., sexual harassment, safety): protected from retaliatory dismissal

**Wrongful termination remedies:** reinstatement (hashava la'avoda) or compensation for damages; a collective agreement may add enhanced severance.

For hearing requirements, the remedy where it was defective (damages without proof of damage), limitation periods, and which court to file in, see the termination workflow in the reference file.

### Step 10: Workplace Harassment (Hatrada Minit)

Per the **Sexual Harassment Prevention Law, 1998**: an employer with more than 25 employees must adopt a written prevention policy (takanon), and every employer must appoint a complaints officer (memune), act on complaints within a reasonable time, and not retaliate against a complainant. Routes: the internal officer, the police for criminal aspects, a labour-court claim, or the Equal Employment Opportunities Commission; the filing deadline differs by route. Duties also reach a business that uses contractor or agency staff (mazminey sherut). What counts as harassment and the full complaint path: `references/harassment-and-disability.md`.

### Step 11: Disability Accommodations

Per the **Equal Rights for People with Disabilities Law, 1998**: the employer must provide reasonable accommodations (modified hours, equipment, remote work where feasible, adjusted duties) unless they impose an undue burden, and may not discriminate in hiring, promotion or dismissal. Disputes go to the Equal Employment Opportunities Commission or the labour court. Detail: `references/harassment-and-disability.md`.

A reservist's partner may have their own paid-absence entitlement under the 29 April 2026 extension order; see the reference file.

### Step 12: Travel Reimbursement, Pay Slip, and Post-Dismissal Benefits

**Travel reimbursement (Dmei Nesia / Hechzer Hotza'ot Nesia):**

Under the Travel-to-Work Extension Order, almost every employee who needs transport to reach the workplace is entitled to a monthly travel reimbursement.

- The employer pays the LOWER of the actual public-transport fare or the statutory daily cap, for each day transport was actually needed. The 2026 cap is **22.60 NIS per day**; verify it before relying on it
- Carve-out: no entitlement where the employee does not need public transport (walking distance, or employer-provided transport). Detail in `references/entitlements-calculator.md`

**Pay slip (Tlush Maskoret):**

Under the Wage Protection Law s.24 the employer must give a detailed pay slip for each pay period, no later than the ninth day after payday, itemizing every pay component and deduction. It is the main tool for checking that the entitlements above were paid.

**Post-dismissal and injury paths (Bituach Leumi):**

- **Unemployment benefit (dmei avtala):** register at the Employment Service, then claim from Bituach Leumi; timing matters (reference file)
- **Work-injury benefit (nifgaei avoda):** an injury at work or on the commute, or an occupational illness, is claimed from Bituach Leumi

## Examples

### Example 1: Calculating Vacation Entitlement

User says: "I've worked at my company for 6 years. How many vacation days am I entitled to?"

From the Step 2 table, year 6 is 18 gross days: 16 days off on a 6-day week, and on a 5-day week 17 days where the shortened-week extension order applies (most workplaces) or 14 where it does not. Ask which applies and quote the days they can actually take off. Check for a collective agreement giving more, and cover carry-forward (normally needs employer consent, except in the reference file's emergency and reserve-duty cases).

### Example 2: Severance Pay After Termination

User says: "I was fired after 3 years and 4 months. My last salary was 15,000 NIS. How much severance should I get?"

Actions:
1. Run `python3 scripts/severance-calculator.py --salary 15000 --years 3 --months 4`
2. Check the deposit rate on the pay slip (Section 14 covers the 6% mandatory deposit automatically; the completion to 8.33% needs the employer's written notice to the fund): at the 6% minimum the fund covers only about 72% of the statutory figure, so a completion payment is owed
3. Advise on the 15-day deadline and penalty interest, and on the 60-day limitation that kills the penalty claim
4. Verify a hearing (shima) was held before termination

Result: approximately NIS 50,000 (15,000 x 3.33). A full 8.33% Section 14 arrangement replaces this with the fund balance; at 6% the employer adds about NIS 14,000 (28%) on top of the fund, whatever its returns. Full termination workflow in `references/entitlements-calculator.md`.

### Example 3: Sick Leave Rights

User says: "I've been sick for a week. My employer says I only get paid from day 4. Is that correct?"

Partially. Day 1 is unpaid, but days 2-3 must be paid at 50% (not zero), and days 4-7 at 100%. Check the accrued balance (1.5 days accrued per month, capped at 90) and confirm a medical certificate exists. For a short absence an HMO short sick certificate may suffice; see the reference file.

### Example 4: Pre-Termination Hearing

User says: "My boss told me I'm fired, effective immediately. No hearing, no notice. What are my rights?"

Two separate breaches. The employer must hold a shimua BEFORE deciding, and compensation for a defective hearing needs no proof of damage, so the claim stands even if no money was lost. After a year the employer also owes a month's notice; paying it out in cash is lawful but carries no pension or severance accrual. Send a written demand citing both, and do not sign anything at the exit meeting. Procedure, remedy and filing route: `references/entitlements-calculator.md`.

## Bundled Resources

### Scripts
- `scripts/severance-calculator.py` -- Severance from salary and tenure, or a salary history (per-period vs last-salary). Handles Section 14 and the completion payment. Run with `--help`.

### References
- `references/labor-laws-summary.md` -- Key Israeli labour laws with names, years and provisions. Use to identify which law applies.
- `references/entitlements-calculator.md` -- Seniority tables for vacation, sick and convalescence pay, plus the termination workflow: Section 14 validity, Form 161, proportional havraa, pay in lieu of notice, unemployment timing, the hearing remedy, limitation periods, where to file. Read it on any dismissal question.
- `references/harassment-and-disability.md` -- Sexual-harassment definitions and complaint routes, and disability-accommodation detail.

## Gotchas

- Israeli sick pay is graduated: 0% day 1, 50% days 2-3, 100% from day 4. Agents trained on US or European norms assume 0% or 100% throughout and get this wrong.
- The work week is 42 hours (since April 2018). Older training data says 43 or 45, which corrupts every overtime calculation.
- Vacation days in the statute are GROSS (they include rest days). Never quote the gross figure as days off, and never use a 5/6 multiplier: read the work-week column in Step 2, and for a 5-day week check the extension order, which gives up to 23 days where the statute gives 17 to 20.
- Severance is due within 15 days of termination, after which penalty interest accrues automatically. Do not cite a 30-day or "reasonable time" standard from another jurisdiction.
- The pre-termination hearing (shimua) is mandatory and has no US at-will equivalent. Omitting it can render a dismissal unlawful regardless of the grounds.


- The child-illness sick-day quota is per parent, not per child, and does not scale with part-time hours. A parent of three still has 8 days, not 24.

- **The halana penalty EXPIRES**: 60 days from receiving the late payment (court may extend to 90), or one year from the sum falling due, whichever is earlier. Telling an employee to demand it without the deadline is worse than silence, because negotiating past it forfeits the claim.
- **Do not let the employee sign a general waiver (kitav vitur) to get their money.** An employer may not condition severance on one, and signing extinguishes every other right here. Take it away, read it, do not sign at the meeting.
- Vacation redemption is capped: on termination the employee redeems the unused days of the final year plus the 3 preceding calendar years. But check the pay slip, since days the employer's own record shows may still be redeemable beyond that.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kol Zchut | https://www.kolzchut.org.il/he | Plain-language entitlement explanations |
| Ministry of Labor | https://www.gov.il/he/pages/aboutlabor | Labor regulations, minimum wage, enforcement |
| Minimum wage | https://www.kolzchut.org.il/he/שכר_מינימום | Monthly and hourly minimum wage |
| Nevo: Severance Pay Law | https://www.nevo.co.il/law_html/law01/p189_001.htm | Severance Pay Law 1963 text |
| Bituach Leumi | https://www.btl.gov.il/benefits/maternity/Pages/default.aspx | Birth allowance eligibility and amounts |
| Labor courts | https://www.kolzchut.org.il/he/בתי_הדין_האזוריים_לעבודה | Court jurisdiction and filing |

## Recommended MCP Servers

| MCP | When to pair | Purpose |
|-----|--------------|---------|
| `kolzchut` | Plain-language summaries and exceptions | Cross-checks entitlements against All-Rights |
| `israel-law` | Statute citations | Exact text of the Annual Leave, Sick Pay, Hours of Work and Rest, Severance Pay and Minimum Wage Laws |

## Troubleshooting

### Error: "Employer claims overtime exemption"
Cause: Senior managers and positions of trust can be exempt under the Hours of Work and Rest Law.
Solution: The exemption is narrow and turns on actual authority, not a "manager" title. Where the employer kept no time records the burden shifts to them, which is what makes most overtime claims winnable. If disputed, go to the labour court.

### Error: "Employer not making pension contributions"
Cause: Breach of the mandatory pension order, common in small businesses.
Solution: Check the pay slip for pension lines and the deposit RATE (6% minimum to severance). If absent or short, send a written demand; if unmet in 30 days, complain to the Ministry of Labour enforcement division or file in the labour court.

### Error: "Severance not paid within 15 days"
Cause: Employer delay, dispute over amount, or cash flow.
Solution: Send a formal written demand (michtav drisha) citing the Severance Pay Law and the 15-day deadline, after which penalty interest (pitzuyei halanat pitzuyim) accrues automatically. State the deadline too: the penalty claim dies 60 days after the late payment is received (court may extend to 90), or one year from the sum falling due, whichever is earlier. The severance itself stays claimable for 7 years. File in labor court for both.

### Error: "Employer refuses convalescence pay"
Cause: Unfamiliarity with the duty, or a claim under one year of service.
Solution: Confirm one full year, then compute from the seniority table (Step 7) and the current daily rate, using the correct sector rate. On termination add the proportional part of the current year. Demand in writing; if unpaid, complain to the Ministry of Labour or file in the labour court.
