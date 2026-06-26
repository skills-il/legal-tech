# Domain Coverage Checklist: Israeli Employment Contract Reviewer

Canonical coverage contract for an agent that **reviews/audits** an existing Israeli employment contract from the employee's defensive, pre-signing perspective. Each Must / Should item below is a topic the reviewer must be able to detect, classify, and explain. A reviewer that silently omits a Must-cover item produces a wrong review outcome (it misses an illegal clause or a missing mandatory protection) and fails.

This file is the coverage spec, not legal advice. Rates change every April; always verify the current figure.

---

## Must cover

These are core to a correct review. Omitting any one can flip the review outcome (a missed blocker, a wrongly-cleared contract, or an illegal clause passed as fine).

1. **Mandatory pension contribution structure (18.5% total).** Employer benefits (tagmulim) 6.5% + employer severance 6% + employee 6% = 18.5%. The 6% severance component is legal on its own. 8.33% severance is NOT a legal floor; it is only the rate needed to fully fund a Section 14 waiver. Flag any component below 6.5% / 6% / 6% as a blocker. *Cite: Mandatory Pension Expansion Order 2008; Kolzchut, חובת ביטוח פנסיוני לעובדים.*
2. **Pension waiting-period nuance (day 1 vs 6 months).** Employee with a prior active fund: contributions from day 1 (paid retroactively after 3 months). True first job (no prior fund): mandatory only after 6 months. A "pension after 6 months" clause is legal for a first job and must NOT be auto-flagged a blocker. *Cite: Mandatory Pension Expansion Order 2008; Kolzchut, חובת ביטוח פנסיוני לעובדים.*
3. **Severance pay (pitzuyei piturin) and Section 14 waiver.** Statutory severance = one month's salary per year of service, paid at termination. Section 14 replaces the lump sum with monthly contributions; the waiver only fully replaces statutory severance at 8.33% severance, and only when the "salary" base for the waiver covers all fixed components (not base-only). Detect base-only definitions, one-sided waivers, and retroactive waivers. *Cite: Severance Pay Law 1963 ss. 14 & general rule; General Authorization under s.14 (Nevo); Kolzchut, סעיף 14.*
4. **Hoda'at mukdemet (advance notice) - monthly schedule.** 1 day/month in months 1-6; 6 days + 2.5 days/month in months 7-12; 30 calendar days flat after one year. Calendar days, not business days; applies to both sides. Below-minimum is a finding even though the statute overrides the clause. *Cite: Prior Notice of Dismissal and Resignation Law 5761-2001; Kolzchut, הודעה מוקדמת לפיטורים.*
5. **Hoda'at mukdemet - hourly/daily schedule is DIFFERENT.** Year 1: 1 day/month. Year 2: 14 days + 1 day per 2 months. Year 3: 21 days + 1 day per 2 months. 3+ years: 30 days flat. Do not borrow the monthly formula for an hourly worker. *Cite: Prior Notice Law 5761-2001; Kolzchut, הודעה מוקדמת לפיטורים.*
6. **Minimum wage floor (cogent).** Monthly 6,443.85 NIS full-time as of 1 April 2026; hourly 35.40 NIS (182h month) or 34.64 NIS (186h month). Pay below this floor is a blocker; updated every April, verify the current rate. *Cite: Minimum Wage Law 1987; Kolzchut, שכר מינימום; BTL minimum-wage page.*
7. **Dmei havra'a (convalescence pay).** Private-sector rate 418 NIS/day (June 2026), pending increase to 451.5 NIS/day on signature of the extension order (then retroactive). Entitlement scales 5 days (year 1) to 10 days (20+ years). Below the rate or day count is a finding. *Cite: Extension Order on convalescence pay; Kolzchut, דמי הבראה.*
8. **Keren hishtalmut (education fund).** Not legally mandatory but universal/expected in tech and many professional roles; tax-advantaged. Standard split 7.5% employer / 2.5% employee. Absence in a tech role is a major finding. *Cite: Industry standard; Kolzchut, קרן השתלמות.*
9. **Notice-to-Employee Law disclosure list.** The employer must put a defined list of terms in writing within 30 days (7 days for a minor): parties, start date (and duration if fixed-term), role + description, pay components + payday, basis of pay, normal hours, weekly rest day, social-benefit contributions + receiving bodies, applicable extension orders / collective agreements. Missing pay/hours items = major; softer items = minor. *Cite: Notice to Employee and Job Candidate Law 5762-2002; Kolzchut, הודעה על תנאי העבודה.*
10. **Non-compete (i-tachrut) enforceability.** Israeli courts (Check Point / Redguard precedent) rarely enforce non-competes beyond a genuine trade secret, special training, or special compensation for the restriction. Flag 12+ month or compensation-free clauses as major; do not tell the user a 2-year non-compete is binding, but do flag the chilling effect. *Cite: Check Point v. Redguard (Labor Court precedent); Kolzchut, הסכם אי תחרות.*
11. **Illegal / unauthorized wage deductions and penalty clauses.** Only deductions permitted under s.25 of the Wage Protection Law are lawful (mandatory tax/BTL/health, pension, union dues, employee-authorized debts). A debt deducted under a written undertaking is capped at 25% of wages. Liability-shifting "penalty", "fine", training-cost-clawback, equipment-loss, or cash-register-shortfall clauses that deduct from wages are generally unlawful. Flag any clause that lets the employer dock pay outside s.25. *Cite: Wage Protection Law 1958 s.25; Kolzchut, ניכויים אסורים משכר עבודה.*
12. **Gross vs net (brutto/netto) clarity.** A salary figure that does not state gross or net is itself a disclosure defect and can cost the employee 30%+ in unexpected deductions. Require explicit "brutto" plus the components that form the pension/severance base. *Cite: Notice to Employee Law 5762-2002; general practice.*
13. **Overtime and the standard workweek.** Standard workweek capped at 42 hours (5-day week); overtime 125% for the first 2 hours, 150% thereafter. "Global"/comprehensive overtime folded into base with no cap/breakdown is routinely struck; a valid global-overtime clause is a separate, quantified, capped line item no less than statutory rates for hours actually worked. *Cite: Hours of Work and Rest Law 1951; Kolzchut, שעות נוספות.*
14. **At-will language.** Israel does not recognize at-will employment; dismissal requires due process (shimua), advance notice, and severance. An at-will clause is unenforceable but signals a foreign-drafted contract; always flag it. *Cite: general Israeli labor law; case law on shimua.*
15. **Annual leave and sick pay minimums.** Annual leave at least the statutory minimum by tenure (12 working days for a 5-day week in years 1-4, rising toward 23). Sick pay accrues 1.5 days/month (18/year), first day unpaid, days 2-3 at 50%, day 4+ at 100%. Below minimum is a finding. *Cite: Annual Leave Law 1951; Sick Pay Law 1976.*
16. **Maternity / pregnancy / fertility dismissal protection.** Under the Women's Employment Law, an employer needs a Ministry of Labor permit (heter) to dismiss or cut the pay/scope of a worker who is pregnant, on/after maternity leave, or in fertility treatment, once the worker has 6 months' tenure (no tenure threshold for the pregnancy-period protection itself in some cases; the 6-month floor governs the broad protection). A contract clause purporting to allow such dismissal, or one conditioning hiring on pregnancy/marital status, is unlawful. Flag it. *Cite: Women's Employment Law 5714-1954; Equal Employment Opportunities Law 1988; Kolzchut, פיטורי עובדת בהריון.*
17. **Right to a payslip (tlush sachar).** The employer must give a detailed monthly payslip listing every pay component and every deduction. A contract that contemplates "cash" pay or no payslip is a red flag. *Cite: Wage Protection Law 1958 (Amendment 24, 2008); Kolzchut, תלוש שכר.*
18. **Severity classification + negotiation output.** The reviewer must classify each finding blocker / major / minor with a consistent rule (blocker = illegal or grossly unfair; major = below market or legally questionable; minor = stylistic), produce the annotated review, list missing mandatory items, and supply concrete replacement language, not "negotiate this".

## Should cover

Valuable for a complete review but not outcome-flipping if briefly handled.

1. **Employee inventions / IP assignment scope.** Off-work, own-resource, unrelated inventions stay the employee's unless directly job-related; "all inventions ever" clauses should be narrowed to service inventions. *Cite: Patents Law 1967 ss.132-134 (service inventions).*
2. **Probation period (tkufat nisayon).** No statutory cap, but 3-6 months is standard; 12+ months is unusual and usually unenforceable. *Cite: case law / practice.*
3. **Confidentiality duration.** Perpetual confidentiality is over-broad; 3-5 years scoped to trade secrets is standard. *Cite: practice; trade-secret law.*
4. **Discretionary bonus framing.** A "sole discretion" bonus can be paid as zero forever; if the role was pitched with a material bonus, push to a formulaic/KPI structure. *Cite: practice; case law distinguishing bonus vs deferred wage.*
5. **Forum / arbitration / governing law.** Israeli labor courts are cheaper and more employee-friendly; arbitration or foreign-jurisdiction clauses shift risk and may be void for cogent disputes. *Cite: Labor Courts Law 1969.*
6. **Section 45a pension tax credit context.** 35% credit on the employee's mandatory pension contribution up to the annual ceiling; contributions above 7% do not earn the credit. Useful for sanity-checking quoted net figures. *Cite: Income Tax Ordinance s.45a; Kolzchut, זיכוי פנסיוני.*
7. **Total-employer-cost sanity ratio.** Gross + employer pension + KH + BTL employer ≈ 120-125% of gross; a much higher implied figure suggests items were already netted out of "gross". *Cite: derived from the contribution rates above.*
8. **Misclassification risk (employee vs kablan/contractor).** If the contract is styled as a freelance/contractor agreement but the relationship has employee hallmarks (subordination, integration, exclusivity), flag misclassification and the back-pay/benefit exposure; refer to a labor attorney. *Cite: case law on the mixed/subordination test (mivchan ha'hishtalvut).*
9. **Equal Opportunity / anti-discrimination clauses.** Conditioning employment on age, religion, marital/pregnancy status, etc. is prohibited. *Cite: Equal Employment Opportunities Law 1988.*
10. **Benefit-bundling / "all-inclusive salary" traps.** A clause declaring the salary "includes all social benefits" (pension, havra'a, overtime, vacation redemption) to dodge separate statutory entitlements is generally void; statutory components cannot be packaged away. Flag it. *Cite: Wage Protection Law; case law voiding inclusive-salary packaging of cogent rights.*

## Out of scope

- Drafting/generating a new contract (use israeli-employment-contracts).
- Post-hire workplace-rights navigation and live disputes (use israeli-workplace-rights-navigator).
- Payroll/net-salary computation engines (use israeli-payroll-calculator).
- Unemployment benefits eligibility/amounts (use israeli-unemployment-benefits-navigator).
- Independent-contractor (kablan) agreements as such, beyond flagging misclassification risk.
- Collective-agreement-specific entitlements for unionized workplaces (note their existence; do not adjudicate).
- Tax-return optimization beyond the pension-credit sanity note.
- Foreign-law employment contracts not governed by Israeli law.

## Authoritative sources

- **Severance Pay Law 1963** (חוק פיצויי פיטורים) - severance + Section 14. Kolzchut: https://www.kolzchut.org.il/he/סעיף_14_לחוק_פיצויי_פיטורים ; General Authorization (Nevo): https://www.nevo.co.il/law_html/law01/055_001.htm
- **Prior Notice of Dismissal and Resignation Law 5761-2001** (חוק הודעה מוקדמת). Kolzchut: https://www.kolzchut.org.il/he/הודעה_מוקדמת_לפיטורים ; Nevo: https://www.nevo.co.il/law_html/law00/71704.htm
- **Mandatory Pension Expansion Order 2008** + **Kolzchut pension obligation**: https://www.kolzchut.org.il/he/חובת_ביטוח_פנסיוני_לעובדים
- **Notice to Employee and Job Candidate Law 5762-2002** (חוק הודעה לעובד). Kolzchut: https://www.kolzchut.org.il/he/הודעה_על_תנאי_העבודה
- **Minimum Wage Law 1987** + rate. Kolzchut: https://www.kolzchut.org.il/he/שכר_מינימום ; BTL: https://www.btl.gov.il/Mediniyut/GeneralData/Pages/שכר מינימום.aspx
- **Hours of Work and Rest Law 1951** + overtime. Kolzchut: https://www.kolzchut.org.il/he/שעות_נוספות
- **Annual Leave Law 1951** (חוק חופשה שנתית).
- **Sick Pay Law 1976** (חוק דמי מחלה).
- **Wage Protection Law 1958** (חוק הגנת השכר) - s.25 deductions, payslip (Amendment 24). Kolzchut: https://www.kolzchut.org.il/he/ניכויים_אסורים_משכר_עבודה ; Nevo: https://www.nevo.co.il/law_html/law00/71689.htm
- **Women's Employment Law 5714-1954** (חוק עבודת נשים) - dismissal permit. Kolzchut: https://www.kolzchut.org.il/he/פיטורי_עובדת_בהריון ; Nevo: https://www.nevo.co.il/law_html/law00/74249.htm
- **Equal Employment Opportunities Law 1988** (חוק שוויון הזדמנויות בעבודה).
- **Patents Law 1967 ss.132-134** (service inventions / המצאות שירות).
- **Income Tax Ordinance s.45a** - pension tax credit. Kolzchut: https://www.kolzchut.org.il/he/זיכוי_ממס_הכנסה_בגין_הפרשות_לביטוח_פנסיוני
- **Non-compete precedent**: Check Point v. Redguard / 164/99 (National Labor Court). Kolzchut: https://www.kolzchut.org.il/he/איסור_הגבלת_עובד_לעבוד_אצל_מעסיק_אחר_לאחר_סיום_עבודתו_(הסכם_אי_תחרות)
- **Dmei havra'a** extension order. Kolzchut: https://www.kolzchut.org.il/he/דמי_הבראה
- **Keren hishtalmut**. Kolzchut: https://www.kolzchut.org.il/he/קרן_השתלמות
