---
name: israeli-employment-contract-reviewer
description: "Pre-signing red-flag audit of an Israeli employment contract (chozeh avoda) from the employee's defensive perspective. Scans a pasted contract for illegal clauses, missing mandatory protections, and unfair terms, then produces an annotated review with citations to Israeli labor law. Flags Section 14 (Saif 14) waiver traps, unenforceable non-competes, hoda'at mukdemet below statutory minimum, missing or late pension, missing keren hishtalmut, at-will language, and gross vs net ambiguity. Produces a negotiating points memo for the employer. Use when about to sign an Israeli employment contract and wanting an independent review before committing. Do NOT use for generating new contracts (use israeli-employment-contracts), post-hire workplace rights (use israeli-workplace-rights-navigator), payroll calculations (use israeli-payroll-calculator), or unemployment benefits (use israeli-unemployment-benefits-navigator)."
license: MIT
allowed-tools: ''
compatibility: Works with Claude, Claude Code, ChatGPT, Cursor. Optional pairing with the kolzchut or knesset MCP for live legal citations. No network required for core red-flag detection.
---

# Israeli Employment Contract Reviewer

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem
Israeli employees routinely sign employment contracts with clauses that are either illegal under Israeli labour law or that quietly transfer risk from the employer to them. The most expensive traps cost tens of thousands of shekels over a career, and several of them are perfectly lawful terms rather than illegal ones: a Section 14 waiver on a base-only salary definition, pension computed on the average wage rather than the full gross, an option grant with a 90-day exercise window. This skill scans a contract before signing, flags every red flag with a specific citation, and generates a negotiating points memo the employee can take back to the employer.

## Instructions

### Step 1: Collect the Contract

Ask the user to paste the full contract text in Hebrew or English (or both). If they only have a PDF, ask them to paste the text extracted from it. Also ask:

| Input | Required | Used for |
|-------|----------|----------|
| Full contract text, with every annex and document it incorporates (an NDA or IP-assignment agreement, the option plan and grant letter, referenced policies) | Yes | The audit subject. In tech offers the non-compete, IP, non-solicitation, monitoring and equity terms usually sit in the annexes, so a review of the offer letter alone is incomplete |
| Target role (engineer, marketer, sales, etc.) | Yes | Determines which clauses are reasonable |
| Annual gross compensation | Yes | Spot unusual ratios (e.g., unreasonable non-compete duration vs pay) |
| Employment scope (`heikef misra`), full-time or a percentage | Yes | Havra'a, the pension base, sick accrual and the minimum-wage floor pro-rate to scope. Leave DAYS do not pro-rate for reduced daily hours, only their value. Skipping this produces false blockers on part-time contracts |
| Is this for a tech startup, corporate, or traditional company? | Yes | Startups are more likely to include illegal non-competes |
| Pension insurance at hire, age, and who the employer is | Yes | The pension wait turns on whether the candidate held pension insurance when starting, not on "first job", and on whether a branch extension order covers the employer. Mandatory pension starts at 21 for men and 20 for women, and the minimum wage is lower under 18. A manpower contractor as employer changes the analysis (`references/additional-clause-checks.md`) |
| Any clauses the user already finds suspicious | No | Prioritizes user's concerns |

Do NOT draft a new contract. This skill reviews existing contracts only. If the user wants to generate one, point them to the `israeli-employment-contracts` skill.

### Step 2: Run the Red-Flag Checklist

Scan the contract for each item in the checklist below. For every finding, record:
- Location (quote the exact clause)
- Rule violated (cite the law and section)
- Severity (blocker, major, minor)
- Negotiation recommendation

#### Mandatory protections (look for their PRESENCE)

| Item | Must include | If missing | Citation |
|------|-------------|------------|----------|
| Job title and scope | Clear role description | Major: employer can reassign arbitrarily | Notice to Employee and Job Candidate (Employment Conditions and Screening/Hiring Procedures) Law, 5762-2002 |
| Start date | Exact date | Blocker: contract is incomplete | - |
| Gross monthly salary | Explicit number | Blocker: negotiate before signing | Notice to Employee and Job Candidate (Employment Conditions and Screening/Hiring Procedures) Law, 5762-2002 |
| Working hours | Weekly total and daily range | Major: overtime calculation becomes ambiguous | Hours of Work and Rest Law 1951 |
| Pension contribution | Contribution clause | Blocker if missing entirely. From day 1 for a candidate who held pension insurance before starting; after 6 months for one who held none. A "pension after 6 months" clause is lawful only in the second case, and only if no branch order gives day 1 | Mandatory Pension Order 2008 / Expansion Order |
| Hoda'at mukdemet (advance notice) | At least statutory minimum | Major: defaults to law anyway, but absence is a red flag | Prior Notice of Dismissal and Resignation Law 2001 |
| Dmei havra'a (convalescence pay) | Day count and rate | Major if the rate or day count is below statutory: 451.5 NIS/day private sector for havra'a year 2026, 511.6 public, owed only after 12 months of employment, 5 days rising to 10 by seniority. Ladder, the 418 NIS top-up and dates: `references/numerical-sanity-checks.md` | Extension Order (convalescence pay) |
| Travel reimbursement (`hechzer hotzaot nesia`) | A reimbursement clause | Major if absent. Owed for each working day at any job scope, at the discounted bus fare up to 22.60 NIS/day or a monthly pass, whichever is cheaper. An "all-inclusive salary" does not settle it | Extension Order (travel expenses) |
| Choice of pension product and provider | No clause naming a single fund or agent | Major. The employee is entitled to choose the TYPE of pension insurance (since September 2023 managers' insurance carries preconditions) (pension fund, provident fund, or managers' insurance) AND the specific institution that will manage it. A clause naming one fund or one agent and barring a move is unenforceable against that right | Mandatory Pension Order 2008 / Expansion Order |
| Annual vacation days | At least statutory minimum by tenure | Major: employer may be trying to under-provide | Annual Leave Law 1951 |
| Sick leave | At least statutory minimum | Major | Sick Pay Law 1976 |

#### Notice to Employee Law disclosure checklist (mandatory written terms)

The Notice to Employee and Job Candidate Law 5762-2002 requires a defined list of terms in writing within 30 days of the start date (7 days for a worker under 18), and a further notice whenever a term changes. Apply the list as a presence check: a missing pay or hours term is major, anything else minor. See `references/notice-to-employee-disclosures.md` for the full list and citation.

#### Illegal or unfair clauses (look for their ABSENCE)

| Red flag | Why it is a problem | Action |
|----------|--------------------|---------|
| "At-will" employment | Israeli law does NOT recognize at-will. Dismissal requires due process (shimua), hoda'at mukdemet, and severance. Clause is unenforceable but signals a foreign-drafted contract the employer may try to enforce in practice | Flag as major. Ask for the clause to be removed or explicitly replaced with "subject to Israeli labor law" |
| A penalty/fine deduction, a training-cost clawback on resignation, equipment-loss, or cash-register shortfall deducted from pay | Wage Protection Law 1958 section 25 sets a CLOSED list of lawful deductions, and an employee-authorised debt is capped at a quarter of the wage per pay period. A disciplinary fine is on the list only when imposed under legislation or a collective agreement, never under the individual contract. The s.25(b) final-wage exception needs an undisputed debt. Section 25 governs only what is TAKEN FROM THE WAGE: a free-standing repayment undertaking can still be enforced as a debt. Full rule and detection terms: `references/red-flag-checklist.md` A9 | Blocker. Strike the clause. Anything outside the closed list is unlawful even if the employee "agreed" |
| At-will / unilateral dismissal clause with no carve-out for a pregnant employee, an employee on maternity leave, or one in fertility treatment | Employment of Women Law 5714-1954 section 9 requires a Ministry of Labour permit (heter) to DISMISS such an employee at 6+ months tenure, and the separate section 9A requires one to cut her pay or job scope. Protection continues through maternity leave and the 60 days after return. A dismissal-at-discretion clause cannot override this, and its absence leaves the employee unaware of it | Minor (informational) when the contract is merely silent, since the protection applies regardless; Major when a clause contradicts it. Either way, tell the employee the protection exists |
| Contract implies cash pay or omits any payslip (tlush sachar) obligation | Wage Protection Law s.24 requires a monthly detailed payslip listing every pay component and deduction. Cash-in-hand or payslip-silent contracts enable hidden deductions and unreported pension and BTL. Check too that the payday is no later than the 9th of the following month, after which the wage is delayed (`mulan`) under sections 9-10 and carries delay compensation | Major. Require an explicit detailed monthly payslip and a lawful payday |
| "All-inclusive" salary clause declaring the gross "includes" pension, havra'a, overtime, or vacation | Bundling cogent statutory components into one all-inclusive figure is void as to those components: pension, dmei havra'a, overtime and annual leave must each be stated and funded separately, on top of base pay. Detect on "inclusive of all social benefits", "כולל הכל", "includes pension and vacation" | Major. Require each statutory component to be a separate, separately funded line, not "included" in gross |
| Contractor/freelancer (kablan) agreement that carries employee hallmarks | Misclassification risk under the subordination and integration test (`mivchan ha'hishtalvut`): fixed hours, a manager, integration and exclusivity point to employment whatever the label, and a court can reclassify retroactively | Major. State the exposure; recommend a genuine independent arrangement or an employee contract |
| Pension below the mandatory minimum | The minimum is employer 6.5% tagmulim + employer 6% severance + employee 6% = 18.5%. 8.33% severance is NOT a legal minimum, only the rate at which a Section 14 waiver fully replaces severance. On a product that is not a pension fund, employer tagmulim may lawfully be as low as 5% with disability cover (detail: `references/numerical-sanity-checks.md`) | Blocker only if a component is below its floor. Below 8.33% severance is "does not fully fund a Section 14 waiver", not illegal. Always check the salary BASE as well as the rates |
| Section 14 (Saif 14) waiver without matching salary clause | Replaces statutory severance with pension contributions. If the waiver's "salary" excludes a fixed component that enters the severance base (a fixed professional or seniority increment, for example), the employee loses money. Bonuses and overtime generally do not enter that base, so adding them is an above-statute ask | Major. Require "salary" to include all fixed components subject to pension |
| Hoda'at mukdemet set below statutory minimum | E.g., "7 days" for an employee of 2 years | Blocker. Statutory minimum is 30 days after year 1 |
| Non-compete (`ekronot i-tachrut`), any length | Usually void, though it chills the job search. A court may uphold a reasonable restriction (time, place, field) only on a legitimate interest: a genuine trade secret, special consideration paid for the restriction, special training the employer funded, or a good-faith duty. Any ONE can suffice, so a PAID non-compete is more likely to be enforced, not less | Major. Ask for removal, or narrow to 6 months, a narrow field and Israel only. If the employee proposes pay for the period, say plainly that this trades enforceability for money |
| Assignment of "all inventions ever" including personal projects | Patents Law 5727-1967 s.132 vests only a SERVICE invention (reached as a result of and during the service) in the employer, and Copyright Law 2007 s.34 only works made for and in the course of the work. "All inventions ever" takes more. Separately, s.134 leaves compensation for a service invention to the parties' agreement, so a clause waiving it settles the question at signing | Major. Narrow to the statutory definition, and flag any waiver of service-invention compensation or royalties explicitly |
| Stated gross salary below the statutory minimum wage | As of 1 April 2026 the minimum wage is 6,443.85 NIS/month full-time. The hourly minimum is 35.40 NIS/hour for a 182-hour month; for a 186-hour month it is 34.64 NIS/hour (the monthly 6,443.85 figure is unchanged). A contract cannot set pay below this cogent floor; the figure is updated every April | Blocker. The salary must be raised to at least the current minimum wage. Verify the current rate, since it changes each April |
| "Global" or "comprehensive" overtime (`shaot globaliyot`) bundled into the base salary with no breakdown | Base pay may not include overtime pay (Wage Protection Law s.5) unless a collective agreement says so. A global overtime supplement holds only if the employee agreed to it and to the average hours it covers, it reflects overtime actually worked, it pays at least 125% for those hours, and it is a separate payslip line | Major. Explain the remedy: a supplement paid whether or not overtime is worked is treated as part of base pay, so social contributions, pension included, are owed on it, and hours beyond those it covers are paid on top. Require overtime as a separate line with an hour cap and stated rates, or hourly tracking |
| Salary defined as "gross" or "net" ambiguously | The gap between gross and net is large once income tax, National Insurance, health levy and the employee pension share come out, so the ambiguity is worth real money and the drafting employer benefits from it | Blocker. Require explicit "gross" (brutto) and state the components |
| Bonus described as "at the sole discretion of the employer" without trigger | Employer can deny forever. If it's labeled "bonus" it is not deferred compensation | Minor if user accepts the risk. Major if the role was pitched with a large bonus component |
| Working hours beyond 42/week without overtime clause | The 42-hour week comes from a general extension order in force since 1 April 2018, NOT from the statute (Hours of Work and Rest Law s.3 still reads 45 hours). On a 5-day week the daily norm is 8.6 net hours on four days and 7.6 on the short day, so four days of 8.6 net hours and one of 7.6 is not overtime, while 8.6 on all five days owes one overtime hour on the short day; on a 6-day week it is 8 hours, and 7 on Friday | Major only when the hours exceed those norms with no overtime clause. Overtime is 125% for the first 2 extra hours of the DAY and 150% after; the split resets daily, not weekly |
| Clauses waiving the employee's rights under Israeli law | Unenforceable but signal bad faith | Major. Remove |
| Probation period (`tkufat nisayon`) treated as a rights-free window | There is no statutory probation. It does not shorten notice, suspend pension or remove the duty to hold a hearing (shimua); it can only gate a contractual benefit | Major if it purports to waive notice, pension or a hearing; Minor otherwise |
| Confidentiality clause extending forever | The term matters less than the scope: a definition wide enough to cover general skills and know-how works like a non-compete | Minor. Accept if narrowly scoped to trade secrets |
| No keren hishtalmut (education fund) for tech/professional roles | Standard in Israeli tech. Not legally required but expected | Major for tech roles. Negotiate to add with 7.5% employer / 2.5% employee split |
| Lawful but expensive clauses (each is a real finding, full detail in `references/high-value-clause-traps.md`) | Nine legal patterns that cost more than most illegal clauses: (1) pension "in accordance with law" with no salary base, stopping at the average wage (13,769 NIS/month in 2026); (2) a s.30(a)(5) "special personal trust" recital; (3) a fixed term with no early exit, or one ending just short of 12 months; (4) an employer right to recover the severance component; (5) termination and re-hire on a sale or group transfer; (6) an unrestricted right to vary role, terms or location; (7) silence on miluim, or reserve absence as unpaid leave; (8) options with no Section 102 route, exercise window or acceleration; (9) keren hishtalmut above the tax ceiling (15,712 NIS/month in 2026): a note, not a defect, since the excess is still the employee's money and is only taxed as income | Major on each unless the reference file says otherwise, and (4) is a blocker. Raise them together in the memo |
| Clauses with their own analysis (full detail in `references/additional-clause-checks.md`) | Non-solicitation of customers or staff; on-call or rest-day work; an employee notice period longer than the statute; leave forfeiture or no-redemption; a manpower contractor as employer; pay secrecy; a minor's contract; privacy and monitoring | Grade per the reference file |
| Arbitration or foreign-forum clause | Labour Court Law 5729-1969 s.24 gives the labour courts exclusive subject-matter jurisdiction among Israeli courts; it does not void arbitration. The objection to a FOREIGN forum or law is that cogent Israeli protections attach to work done in Israel | Major for a foreign forum or law. Minor for domestic arbitration |

#### Numerical sanity checks

Compute the numerical checks in `references/numerical-sanity-checks.md` from the contract figures and flag anomalies: the minimum-wage floor, the pension rates AND the salary base they apply to, the keren hishtalmut split and ceiling, total employer cost, advance-notice days, annual vacation, sick leave and dmei havra'a. `scripts/contract_sanity_check.py` automates the pension, notice, vacation and sick-day checks. Every figure in that table moves on a fixed calendar (minimum wage each April, private-sector havra'a each July, the average wage and tax ceilings each January), so re-verify before quoting one as current.

### Step 3: Classify Severity

For each finding, assign:

- **Blocker**: illegal or grossly unfair. Do not sign without fixing.
- **Major**: below market standard or legally questionable. Negotiate before signing.
- **Minor**: acceptable but non-ideal. Note for future reference.

If the contract has 1+ blockers, the top-line recommendation is "do not sign until fixed."
If the contract has 0 blockers and only minor findings, the recommendation is "safe to sign, with these notes."

### Step 4: Produce the Annotated Review

Output format:

```
DISCLAIMER
This is an automated review, not legal advice. It is produced by an AI model with no
involvement or approval by an advocate, does not examine your full circumstances, and may
err. Before signing, consult an Israeli labour attorney (orech din avoda), and do so in any
case for a contract with significant blockers or for a senior or executive position.

# Contract Review Summary
**Overall recommendation:** <Do not sign | Negotiate | Safe to sign>
**Blockers:** N
**Major findings:** N
**Minor findings:** N

## Blockers (must fix before signing)
1. [Clause quote]
   - **Rule violated:** [law and section]
   - **Why it matters:** [consequence]
   - **Negotiation language:** [specific replacement text]

## Major findings (negotiate)
[same format]

## Minor findings (note)
[same format]

## Missing mandatory items
[list of protections that should appear but don't]

## Negotiating points memo (copy this to the employer)
1. Please update [clause] because [reason]
2. ...
```

### Step 5: Add Specific Negotiation Language

For each blocker and major finding, write a specific Hebrew or English replacement the employee can ask the employer to use. Do not just say "negotiate this" - give them the exact words.

### Step 6: Final Warnings

The disclaimer block at the TOP of the Step 4 template is mandatory and must appear above the summary, never only below it. Repeat it at the end as well:

```
DISCLAIMER
This is an automated review, not legal advice. For contracts with significant
blockers, or for senior / executive positions, consult an Israeli labour
attorney (orech din avoda) before signing. Sources: kolzchut.org.il,
nevo.co.il, Bituach Leumi official guidance.
```

## Examples

### Example 1: Section 14 waiver with a base-only salary definition

**Clause as written:** "The employee agrees to the arrangement under Section 14 of the Severance Pay Law. The employer's contributions to the pension fund, calculated on the base salary, replace severance pay in full."

**Finding:** Major. Since 2008 Section 14 applies automatically to the employer's mandatory severance deposits under the pension Expansion Order, so the clause adds little by itself. The trap is "calculated on the base salary": the employee's role pays a 12,000 NIS base plus a recurring 4,000 NIS fixed professional increment (`tosefet miktzo'it`), which enters the severance base. Because the waiver covers only the base, the employee loses the severance value of the increment, and on termination receives less than the statutory calculation would yield.

**Recommended replacement:** "The Section 14 arrangement applies to the employee's full salary, including all fixed components subject to pension contributions (base salary, fixed allowances, and any other regular fixed payment), and not to the base salary alone."

### Example 2: Advance notice set below the statutory minimum

**Clause as written:** "Either party may terminate this agreement by giving 7 days written notice."

**Finding:** Blocker. The contract is for a permanent role with no tenure cap. A flat 7-day notice is below the statutory minimum for any employee past the first 7 months: after one full year the minimum is 30 calendar days (see `references/hoda-at-mukdemet-table.md`). The clause is unenforceable against the employee, but it signals the employer is not drafting to Israeli law.

**Recommended replacement:** "Advance notice of termination, by either party, shall be the statutory minimum under the Prior Notice of Dismissal and Resignation Law, 5761-2001, by length of service: in the first six months, one day per month worked; in months seven to twelve, six days plus two and a half days for each month after the sixth; and from one year of service onward, 30 calendar days."

## Bundled Resources

### References

| File | Purpose |
|------|---------|
| `references/red-flag-checklist.md` | Full list of illegal, unfair, and missing clauses to scan for |
| `references/hoda-at-mukdemet-table.md` | Statutory advance notice days by tenure for monthly and hourly workers |
| `references/section-14-trap-guide.md` | Detailed explanation of the Saif 14 waiver, when it helps, and when it hurts |
| `references/standard-negotiation-language.md` | Ready-to-use Hebrew and English replacement clauses for common red flags |
| `references/notice-to-employee-disclosures.md` | Mandatory written-disclosure list under the Notice to Employee Law 2002 |
| `references/numerical-sanity-checks.md` | The numerical check table with current rates and ceilings |
| `references/high-value-clause-traps.md` | Lawful but expensive clauses: pension ceiling, Section 102 options, fixed term, severance forfeiture, seniority continuity, miluim |
| `references/additional-clause-checks.md` | Non-solicitation, on-call and rest-day work, longer contractual notice, leave forfeiture, manpower contractors, pay secrecy, minors, privacy and monitoring |
| `references/domain-checklist.md` | Coverage checklist used to audit this skill |

### Scripts

| File | Purpose |
|------|---------|
| `scripts/contract_sanity_check.py` | Quick numerical validator for pension %, hoda'at mukdemet days, and vacation days |

## Recommended MCP Servers

| MCP | When to pair | Purpose |
|-----|--------------|---------|
| [kolzchut](https://agentskills.co.il/he/mcp/kolzchut) | For plain-language rule summaries and exceptions | Cross-references findings against the All-Rights database, including the rates that move every April and June |
| [knesset](https://agentskills.co.il/he/mcp/knesset) | For the current text and amendment history of a statute | Confirms which amendment of a labour statute is in force before you cite a section number |

The skill works without these MCPs using the built-in reference tables, but the citations become less specific. Whichever you use, spot-check a quoted rate against the live source before presenting it as current.

## Gotchas

1. **Mistaking "at-will" clauses for enforceable terms**. Agents trained on US corporate templates assume at-will is normal. In Israel, it is unenforceable but common in foreign-drafted contracts. Always flag it.

2. **Telling the user a 2-year non-compete is enforceable**. Israeli courts apply the Frumer and Check Point v. Radguard precedent (Labour Court appeal 164/99) and treat a non-compete as void unless a legitimate interest backs it: a trade secret the employer can identify specifically and show it protected, special consideration paid for the restriction, special funded training, or a good-faith duty. Most unpaid 2-year non-competes are aspirational. Do not scare the user into refusing a good job over an unenforceable clause, but do flag it and recommend negotiation.

3. **Confusing Saif 14 with being a net positive**. Section 14 waivers CAN benefit the employee (monthly pension contributions instead of lump sum at termination) but ONLY if the waiver's "salary" covers every fixed component that enters the severance base. If it covers only base, the employee loses severance on a fixed increment. Do not tell the user they lose severance on bonuses or overtime: those generally do not enter the base at all. Also note that salary for which nothing was deposited (for example a lawful 6-month waiting period) carries full statutory severance outside the waiver.

4. **Ignoring keren hishtalmut absence for tech roles**. KH is not legally mandatory, but in Israeli tech it is universal and tax-advantaged. A tech contract without KH is a red flag even though it is "legal."

5. **Calculating hoda'at mukdemet in business days**. The law uses calendar days. A 30-day notice period means 30 actual days, including weekends and holidays. Agents sometimes quote business days, which is wrong.

6. **Accepting "discretionary bonus" at face value**. If the role was pitched with a 20% bonus component, a "fully discretionary" clause means the employer can pay zero forever. Flag this as major and suggest converting to a formulaic bonus tied to measurable KPIs.

7. **Getting the pension start date wrong**. The test is not "first job" but whether the candidate held pension insurance when starting, and whether a branch extension order applies. If so, contributions run from day 1 (deposited after 3 months or at the end of the tax year, whichever is earlier, retroactively). If not, the right starts after 6 months, unless a branch extension order (industry, for one) gives day 1 anyway. Regional labour courts have treated a policy with no deposits for more than 5 months before hire as uninsured, but no binding ruling exists. So ASK before grading: a "pension after 6 months" clause is a blocker for an insured candidate or under a day-1 branch order, and lawful otherwise for an uninsured one. Below 21 (men) or 20 (women) there is no mandatory pension yet.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kolzchut: Hoda'at Mukdemet law | https://www.kolzchut.org.il/he/הודעה_מוקדמת_לפיטורים | Statutory advance notice days by tenure |
| Nevo: Prior Notice Law full text | https://www.nevo.co.il/law_html/law00/71704.htm | Official legal text |
| Kolzchut: Overtime pay (gmul sha'ot nosafot) | https://www.kolzchut.org.il/he/גמול_עבור_שעות_נוספות | 125% / 150% overtime rates and the 42-hour extension order |
| Kolzchut: Section 14 of the Severance Pay Law | https://www.kolzchut.org.il/he/סעיף_14_לחוק_פיצויי_פיטורים | Section 14 waiver rules and 8.33% requirement |
| Kolzchut: Non-compete clauses after employment ends | https://www.kolzchut.org.il/he/איסור_הגבלת_עובד_לעבוד_אצל_מעסיק_אחר_לאחר_סיום_עבודתו_%28הסכם_אי_תחרות%29 | When a non-compete clause is enforceable |
| Bituach Leumi: For salaried workers rates | https://www.btl.gov.il/English%20Homepage/Insurance/Ratesandamount/Pages/forSalaried.aspx | National Insurance contribution rates |
| Kolzchut: Mandatory pension insurance for employees | https://www.kolzchut.org.il/he/חובת_ביטוח_פנסיוני_לעובדים | 18.5% total (6.5% + 6% + 6%) and the day-1 vs 6-month rule |
| Kolzchut: Dmei havra'a (convalescence pay) | https://www.kolzchut.org.il/he/דמי_הבראה | 451.5 NIS/day private-sector rate (updated 18.08.2026), 511.6 public, day count by seniority |
| Kolzchut: Minimum wage | https://www.kolzchut.org.il/he/שכר_מינימום | 6,443.85 monthly, 35.40/34.64 hourly |
| Kolzchut: Notice to Employee on employment conditions | https://www.kolzchut.org.il/he/הודעה_על_תנאי_העבודה | Mandatory written-disclosure list |
| Kolzchut: Deductions from wages | https://www.kolzchut.org.il/he/ניכויים_משכר_העובד | Section 25 closed list of lawful deductions and the 25% debt cap |
| Kolzchut: Dismissal of a pregnant employee | https://www.kolzchut.org.il/he/איסור_פיטורי_עובדת_בהיריון | Employment of Women Law permit (heter) requirement at 6+ months |
| Kolzchut: Payslip (tlush sachar) | https://www.kolzchut.org.il/he/תלוש_שכר | Detailed monthly payslip obligation (Wage Protection Law s.24) |

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Review found 15 "blockers" in a standard contract | Over-flagging, probably labeling minor issues as blockers | Re-classify using strict severity: blocker = illegal, major = below market, minor = style |
| Contract is in Hebrew only, Hebrew quality is poor | Employer used a template translation | Flag as major: request a clean Hebrew or bilingual version |
| Salary quoted as "12,000 NIS" with no brutto/neto | Ambiguous | Ask user if they confirmed with employer. Flag as blocker to force clarity |
| Non-compete looks scary to user | User feels legally bound | Explain the Frumer and Check Point v. Radguard precedent (appeal 164/99): void without a legitimate interest such as a specifically identified trade secret or pay for the restriction. Still negotiate, but do not refuse the job over it alone |
| Section 14 clause without waiver text | Since 2008 Section 14 applies automatically to the mandatory severance deposits | Not a defect by itself. Check the severance rate (6% leaves a top-up owed on dismissal; 8.33% replaces severance in full only with the employer's written notice to the fund) and the salary base |
| Contract is for a contractor (kablan), not employee | Different set of rules | Apply the subordination/integration test (mivchan ha'hishtalvut): fixed hours + subordination + integration + exclusivity point to an employee relationship that a court can reclassify retroactively. Flag the hallmarks you find and the reclassification exposure, then recommend a labor attorney for the borderline call |
