---
name: israeli-workplace-rights-navigator
description: >-
  Understand and exercise employee rights under Israeli labor law, including
  vacation days (chofsha), sick leave (machala), overtime pay, maternity and
  paternity leave, severance pay (pitzuyim), convalescence pay (dmei havra'a),
  and pension contributions. Use when user asks about "employee rights in
  Israel", "how many vacation days", "sick pay Israel", "pitzuyei piturim",
  "dmei havra'a", "chofeshat leidah", "shaat nosafot", or "zchuyot ovdim".
  Covers Annual Leave Law, Sick Pay Law, Hours of Work and Rest Law,
  Employment of Women Law, Severance Pay Law, sexual harassment protections,
  and disability accommodations. Do NOT use for employment contract generation
  (use israeli-employment-contracts), salary negotiation (use
  israeli-tech-salary-negotiator), reserve duty rights (use
  israeli-miluim-manager), or freelancer operations (use israeli-freelancer-ops).
license: MIT
allowed-tools: 'Bash(python:*)'
compatibility: 'No special requirements. Works with Claude Code, Cursor, Windsurf.'
metadata:
  author: skills-il
  version: 1.0.0
  category: legal-tech
  tags:
    he:
      - דיני-עבודה
      - זכויות-עובדים
      - חופשה
      - מחלה
      - פיצויים
      - ישראל
    en:
      - labor-law
      - employee-rights
      - workplace
      - vacation
      - sick-days
      - israel
  display_name:
    he: "ניווט זכויות עובדים"
    en: Israeli Workplace Rights Navigator
  display_description:
    he: >-
      הבנה ומימוש זכויות עובדים לפי דיני העבודה הישראליים. מכסה ימי חופשה,
      ימי מחלה, שעות נוספות, חופשת לידה, פיצויי פיטורים, דמי הבראה, הפרשות
      פנסיה, הגנות מפני פיטורים שלא כדין, הטרדה מינית והתאמות לאנשים עם
      מוגבלות. השתמשו כשמשתמש שואל על זכויות עובדים, חישוב פיצויים, ימי
      חופשה, מחלה, או הליכי פיטורים בישראל.
    en: >-
      Understand and exercise employee rights under Israeli labor law, including
      vacation days (chofsha), sick leave (machala), overtime pay, maternity and
      paternity leave, severance pay (pitzuyim), convalescence pay (dmei havra'a),
      and pension contributions. Covers Annual Leave Law, Sick Pay Law, Hours of
      Work and Rest Law, Employment of Women Law, Severance Pay Law, sexual
      harassment protections, and disability accommodations. Do NOT use for
      employment contract generation (use israeli-employment-contracts), salary
      negotiation (use israeli-tech-salary-negotiator), or reserve duty rights
      (use israeli-miluim-manager).
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# Israeli Workplace Rights Navigator

Understand and exercise employee rights under Israeli labor law. This skill covers the core entitlements every employee in Israel should know: vacation, sick leave, overtime, maternity/paternity leave, severance, convalescence pay, pension, termination protections, harassment prevention, and disability accommodations.

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

Per the **Annual Leave Law, 1951 (Chok Chufsha Shnatit)**, every employee is entitled to paid vacation based on seniority:

| Years of Employment | Minimum Vacation Days (per year) |
|---------------------|----------------------------------|
| 1-4 | 12 days |
| 5 | 14 days |
| 6 | 16 days |
| 7 | 21 days |
| 8+ | 28 days |

**Key rules:**
- Days are calculated based on a 6-day work week. For a 5-day week, multiply by 5/6 (rounded). For example, 12 days becomes 10 working days for a 5-day week
- Part-time employees earn vacation proportionally based on hours worked
- Vacation days can accumulate for up to 2 years if unused, but the employer can require the employee to take them
- Vacation includes Fridays and Saturdays (or the employee's weekly rest day) only if they fall within a continuous vacation period
- The employer sets the vacation schedule but must consider the employee's requests. The employee must receive at least 7 consecutive days per year if requested

**Vacation pay:**
- The employee receives their regular salary during vacation
- Unused vacation days must be paid out (pidyon chufsha) upon termination

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
- Sick days can be used for the employee's own illness or a child's illness (up to 8 days per year per child under 16, or 16 days for a child with a disability)
- An employer cannot fire an employee during sick leave for the first 90 days of accumulated sick days
- Unused sick days are not paid out upon termination (unless a specific agreement states otherwise)

### Step 4: Overtime Pay (Shaat Nosafot)

Per the **Hours of Work and Rest Law, 1951 (Chok Sha'ot Avoda U'Menucha)**:

**Standard work hours:**
- Maximum regular work day: 8 hours (or as defined by collective agreement)
- Maximum work week: 42 hours
- Weekly rest day: at least 36 consecutive hours (typically Friday evening to Saturday evening for Jewish employees)

**Overtime rates:**

| Overtime Hours | Pay Rate |
|----------------|----------|
| First 2 overtime hours in a day | 125% of hourly wage |
| Beyond 2 overtime hours in a day | 150% of hourly wage |
| Work on weekly rest day (Shabbat) | 150% of hourly wage |

**Key rules:**
- Maximum overtime: 4 hours per day, 12 hours per week
- Total work day cannot exceed 12 hours
- Overtime must be compensated in pay, not comp time (unless a valid collective agreement allows it)
- Certain sectors and positions (managers, those requiring a high degree of personal trust) may be exempt from overtime rules under specific legal conditions
- The employer must keep accurate records of work hours

### Step 5: Maternity and Paternity Leave (Chofeshat Leidah)

Per the **Employment of Women Law, 1954 (Chok Avdat Nashim)**:

**Maternity leave:**
- Total duration: 26 weeks from the date of birth
- Paid portion: 15 weeks of maternity allowance (dmei leidah) from Bituach Leumi, for employees who paid national insurance for at least 10 of the 14 months preceding the birth, or 15 of the 22 months
- Employees with less than 10 months of insurance contributions: 8 weeks paid
- The remaining weeks (11 or 18) are unpaid leave
- The employee can start leave up to 7 weeks before the due date (deducted from the 26 weeks)

**Job protection:**
- An employer cannot fire a pregnant employee without a permit from the Ministry of Labor
- An employer cannot fire an employee for 60 days after maternity leave ends
- The employee is entitled to return to the same position or an equivalent one

**Paternity leave:**
- 5 paid days immediately after birth (3 days from the employer, 2 days from vacation balance)
- The father can take up to 6 weeks of the remaining maternity leave (transferred from the mother) after she has taken at least 6 weeks

**Additional protections:**
- Fertility treatments: employees undergoing fertility treatments receive absences as sick days and are protected from termination during treatment
- Adoption: similar leave entitlements apply to adoptive parents
- Nursing mothers: entitled to a reduced work day (1 hour less) for 4 months after returning from maternity leave, with full pay

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
python scripts/severance-calculator.py --help
```

**When severance is owed:**
- Employer-initiated termination (piturim)
- Employee resignation due to health, relocation for marriage, or deteriorated working conditions (in certain cases recognized by law)
- Death of the employer (individual employer)
- Employer bankruptcy

**Section 14 arrangement:**
- Most employers make monthly contributions to a pension or provident fund (kupat gemel) that are designated as severance pay under Section 14 of the Severance Pay Law
- Under this arrangement, the accumulated fund replaces the obligation to pay severance separately
- The standard contribution rate for severance: 8.33% of salary (equivalent to 1/12 of monthly salary)
- Upon termination, the employee receives the accumulated fund balance as severance

**Key rules:**
- Severance must be paid within 15 days of termination
- Late payment accrues penalty interest (pitzuyei halanat pitzuyim)
- An employee who resigns is generally not entitled to severance, except in specific circumstances

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
- Updated annually by the Ministry of Economy. The daily rate for 2025 is NIS 418 (private sector). Check for the most current rate at the time of inquiry
- Public sector employees receive a higher rate per collective agreement

**Payment:**
- Usually paid once a year, typically in June-September
- Appears as a separate line on the pay slip (tlush maskoret)
- Taxable income but not subject to social security deductions
- Part-time employees receive proportional pay based on their work percentage

### Step 8: Pension and Savings (Pnsia)

Since the **Mandatory Pension Law extension order (Tzav Harchava, 2008)**:

**Mandatory contribution rates (as of 2026):**

| Component | Employee Contribution | Employer Contribution |
|-----------|----------------------|----------------------|
| Pension savings | 6% of salary | 6.5% of salary |
| Severance (Section 14) | 0% | 8.33% of salary |
| Disability insurance | Included in employer's 6.5% | Included in employer's 6.5% |

**Key rules:**
- Applies to all employees after 6 months of employment (or immediately if the employee has an existing pension fund)
- The employee chooses the pension fund (keren pensia, bituach menahalim, or kupat gemel)
- Contributions are calculated on the gross salary up to the maximum insurable salary
- An employer who fails to make pension contributions violates the law and faces penalties

### Step 9: Termination Procedures (Halichei Piturim)

Israeli law requires specific procedures before terminating an employee:

**Notice period (hodaa mukdemet):**

| Employment Duration | Notice Period |
|--------------------|---------------|
| First 6 months | 1 day per month worked |
| 6-12 months | 6 days + 2.5 days per month after the 6th |
| 1+ years | 1 month |

**Pre-termination hearing (shima):**
- The employer must hold a hearing before making the final decision to terminate
- The employee must receive written notice of the hearing in advance, including the reasons being considered
- The employee has the right to bring a representative (union rep, lawyer, or colleague)
- The employer must genuinely consider the employee's arguments before deciding
- Failure to hold a proper hearing can render the termination unlawful

**Protected employees:**
- Pregnant women: cannot be terminated without a permit from the Ministry of Labor
- Employees on sick leave: protected during the first 90 days of accumulated sick leave
- Employees on maternity leave: protected during leave and for 60 days after
- Employees during military reserve duty (miluim): protected during and for 30 days after
- Employees who filed complaints (e.g., sexual harassment, safety): protected from retaliatory dismissal

**Wrongful termination remedies:**
- Reinstatement (hashava la'avoda)
- Compensation for damages
- Increased severance pay (up to 150% in cases of particularly egregious termination)

### Step 10: Workplace Harassment (Hatrada Minit)

Per the **Sexual Harassment Prevention Law, 1998 (Chok Meni'at Hatrada Minit)**:

**Employer obligations:**
- Every employer with more than 25 employees must adopt a written sexual harassment prevention policy (takanon)
- Appoint a designated officer (memune) to handle complaints
- Conduct training on harassment prevention
- Employers with fewer than 25 employees must still comply with the law but are not required to have a written policy

**What constitutes sexual harassment under the law:**
- Physical conduct of a sexual nature
- Repeated sexual propositions after the person has shown disinterest
- Repeated references to a person's sexuality when they have shown disinterest
- Degrading or humiliating treatment related to gender, sexuality, or sexual orientation
- Publication of intimate photographs without consent

**Filing a complaint:**
- Internal complaint to the designated officer (memune) at the workplace
- External complaint to the police (for criminal aspects)
- Civil lawsuit in labor court (beit din la'avoda)
- Complaint to the Equal Employment Opportunities Commission (Netzivut Shivyon Hizdamnuyot Ba'avoda)
- Statute of limitations: 3 years for civil claims, 7 years for criminal complaints

**Protections:**
- The complainant is protected from retaliation (cannot be fired, demoted, or have conditions worsened)
- The employer must investigate complaints within a reasonable time
- Failure to act on complaints exposes the employer to liability

### Step 11: Disability Accommodations

Per the **Equal Rights for People with Disabilities Law, 1998 (Chok Shivyon Zchuyot Le'anashim Im Mugbaluyot)**:

**Employer obligations:**
- Provide reasonable accommodations (hat'amot) for employees with disabilities
- Cannot discriminate in hiring, promotion, or termination based on disability
- Must ensure physical accessibility of the workplace

**Reasonable accommodations include:**
- Modified work hours or schedules
- Accessible workstation equipment
- Work-from-home arrangements when feasible
- Modified job duties that do not fundamentally change the role
- Additional break time as needed

**Key rules:**
- Applies to employers with 25+ employees (some provisions apply to smaller employers)
- The employer is not required to make accommodations that impose an "undue burden" (natel bilti savir)
- The employee should notify the employer of the need for accommodations
- Disputes can be brought before the Equal Employment Opportunities Commission or labor court

## Examples

### Example 1: Calculating Vacation Entitlement

User says: "I've worked at my company for 6 years. How many vacation days am I entitled to?"

Actions:
1. Look up seniority in the vacation table (Step 2): 6 years = 16 days per year
2. Clarify work week: if 5-day week, calculate 16 x 5/6 = 13.3, rounded to 14 working days
3. Note any applicable collective agreement that may provide more days
4. Advise on accumulated unused days from prior years

Result: Employee is entitled to 16 calendar days (14 working days for a 5-day week) per year, with any unused days from years 5 and 6 potentially accumulated.

### Example 2: Severance Pay After Termination

User says: "I was fired after 3 years and 4 months. My last salary was 15,000 NIS. How much severance should I get?"

Actions:
1. Confirm employment duration: 3 years and 4 months = 3.33 years
2. Calculate severance: `python scripts/severance-calculator.py --salary 15000 --years 3 --months 4`
3. Check if Section 14 arrangement applies (most common in tech)
4. Advise on the 15-day payment deadline and penalty interest for late payment
5. Verify a proper hearing (shima) was held before termination

Result: Severance of approximately NIS 50,000 (15,000 x 3.33). If Section 14 applies, the accumulated pension/provident fund balance replaces this amount.

### Example 3: Sick Leave Rights

User says: "I've been sick for a week. My employer says I only get paid from day 4. Is that correct?"

Actions:
1. Confirm sick day pay structure (Step 3): day 1 unpaid, days 2-3 at 50%, day 4+ at 100%
2. For a 7-day illness: day 1 = NIS 0, days 2-3 = 50% each, days 4-7 = 100% each
3. Verify the employee has a medical certificate
4. Check accumulated sick day balance (1.5 per month, max 90)

Result: The employer is partially correct. Day 1 is unpaid, but days 2-3 must be paid at 50% (not zero). Days 4-7 are at 100%. The employee should verify their pay slip reflects this.

### Example 4: Pre-Termination Hearing

User says: "My boss told me I'm fired, effective immediately. No hearing, no notice. What are my rights?"

Actions:
1. Explain the hearing requirement (Step 9): the employer must hold a shima before deciding
2. Explain the notice period: after 1+ years, the employer must give 1 month notice
3. Advise on immediate steps: send a written demand to the employer citing the lack of hearing
4. Recommend consulting a labor lawyer or contacting the Histadrut (labor union) for assistance
5. Note that improper termination may entitle the employee to compensation beyond regular severance

Result: The termination may be unlawful. The employee should demand in writing that the employer follow proper procedure, including a hearing and notice period. If the employer refuses, the employee can file a claim in labor court.

## Bundled Resources

### Scripts
- `scripts/severance-calculator.py` -- Calculate severance pay based on salary history and tenure. Supports monthly salary, years, and months of employment. Handles Section 14 scenarios. Run: `python scripts/severance-calculator.py --help`

### References
- `references/labor-laws-summary.md` -- Summary table of all key Israeli labor laws with law names, numbers, and key provisions. Consult when identifying which specific law applies to a situation.
- `references/entitlements-calculator.md` -- Tables for vacation days, sick days, convalescence pay by seniority. Quick-reference tables for all seniority-based entitlements. Consult when calculating specific entitlements by years of service.

## Troubleshooting

### Error: "Employer claims overtime exemption"
Cause: Certain positions (senior managers, positions requiring personal trust) may be exempt from overtime rules under the Hours of Work and Rest Law.
Solution: Verify the employee's actual role and responsibilities. The exemption applies narrowly. Having a "manager" title alone is insufficient; the employee must have genuine managerial authority. If disputed, consult a labor attorney or the labor court.

### Error: "Employer not making pension contributions"
Cause: Employer violating the mandatory pension order, common with small businesses or new employees.
Solution: First, check the pay slip for pension deduction lines. If absent, send a written demand to the employer. If the employer does not comply within 30 days, file a complaint with the Ministry of Labor's enforcement division (agaf ha'akifa). The employee can also file a claim in labor court.

### Error: "Severance not paid within 15 days"
Cause: Employer delay, dispute over amount, or cash flow issues.
Solution: Send a formal written demand (michtav drisha) citing the Severance Pay Law and the 15-day deadline. After 15 days, penalty interest (pitzuyei halanat pitzuyim) accrues automatically. If the employer continues to withhold, file a claim in labor court for the severance amount plus penalty interest.

### Error: "Employer refuses convalescence pay"
Cause: Employer unfamiliar with the obligation or claiming the employee has not completed one year.
Solution: Verify that the employee has completed at least one full year of employment. Calculate the entitlement using the seniority table (Step 7) and the current daily rate. Send a written demand with the specific amounts owed. If unpaid, file a complaint with the Ministry of Labor or a claim in labor court.
