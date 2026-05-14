---
name: israeli-employment-contract-reviewer
description: "Pre-signing red-flag audit of an Israeli employment contract (chozeh avoda) from the employee's defensive perspective. Scans a pasted contract for illegal clauses, missing mandatory protections, and unfair terms, then produces an annotated review with citations to Israeli labor law. Flags Section 14 (Saif 14) waiver traps, unenforceable non-competes, hoda'at mukdemet below statutory minimum, missing pension, missing keren hishtalmut, at-will language, and gross vs net ambiguity. Produces a negotiating points memo for the employer. Use when about to sign an Israeli employment contract and wanting an independent review before committing. Do NOT use for generating new contracts (use israeli-employment-contracts), post-hire workplace rights (use israeli-workplace-rights-navigator), payroll calculations (use israeli-payroll-calculator), or unemployment benefits (use israeli-unemployment-benefits-navigator)."
license: MIT
allowed-tools: ''
compatibility: Works with Claude, Claude Code, ChatGPT, Cursor. Optional pairing with israel-law or kolzchut MCP for live legal citations. No network required for core red-flag detection.
---

# Israeli Employment Contract Reviewer

## Problem
Israeli employees routinely sign employment contracts with clauses that are either illegal under Israeli labor law or that quietly transfer risk from the employer to them. The most expensive traps (a Section 14 waiver without a proper salary clause, hoda'at mukdemet below the statutory minimum, missing pension from day 1, an unenforceable non-compete the employee later feels bound by) can cost tens of thousands of shekels over a career. This skill scans a contract before signing, flags every red flag with a specific Israeli labor law citation, and generates a negotiating points memo the employee can take back to the employer. It is the defensive counterpart to contract generation.

## Instructions

### Step 1: Collect the Contract

Ask the user to paste the full contract text in Hebrew or English (or both). If they only have a PDF, ask them to paste the text extracted from it. Also ask:

| Input | Required | Used for |
|-------|----------|----------|
| Full contract text | Yes | The audit subject |
| Target role (engineer, marketer, sales, etc.) | Yes | Determines which clauses are reasonable |
| Annual gross compensation | Yes | Spot unusual ratios (e.g., unreasonable non-compete duration vs pay) |
| Is this for a tech startup, corporate, or traditional company? | Yes | Startups are more likely to include illegal non-competes |
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
| Pension from day 1 | Contribution clause | Blocker: employer is legally required | Mandatory Pension Order 2008 / Expansion Order |
| Hoda'at mukdemet (advance notice) | At least statutory minimum | Major: defaults to law anyway, but absence is a red flag | Prior Notice of Dismissal and Resignation Law 2001 |
| Dmei havra'a (convalescence pay) | Annual accrual | Minor: defaults to law | Extension Order (convalescence pay) |
| Annual vacation days | At least statutory minimum by tenure | Major: employer may be trying to under-provide | Annual Leave Law 1951 |
| Sick leave | At least statutory minimum | Major | Sick Pay Law 1976 |

#### Illegal or unfair clauses (look for their ABSENCE)

| Red flag | Why it is a problem | Action |
|----------|--------------------|---------|
| "At-will" employment | Israeli law does NOT recognize at-will. Dismissal requires due process (shimua), hoda'at mukdemet, and severance. Clause is unenforceable but signals a foreign-drafted contract the employer may try to enforce in practice | Flag as major. Ask for the clause to be removed or explicitly replaced with "subject to Israeli labor law" |
| Pension below Mandatory Pension Order rates | Employer benefits below 6.5% + severance below 8.33% | Blocker. Employer cannot contract below the minimum |
| Section 14 (Saif 14) waiver without matching salary clause | Waives right to statutory severance in exchange for pension contributions, but if the "salary" definition excludes bonuses/overtime, the employee loses money | Major. Require "salary" to include all fixed components subject to pension |
| Hoda'at mukdemet set below statutory minimum | E.g., "7 days" for an employee of 2 years | Blocker. Statutory minimum is 30 days after year 1 |
| Non-compete (`ekronot i-tachrut`) exceeding 6-12 months | Israeli courts rarely enforce non-competes beyond protecting trade secrets. Clauses of 2+ years are typically unenforceable, but create chilling effect | Major. Negotiate down to 6 months max, narrow geographic scope, narrow competitor definition |
| Non-compete without compensation during the restriction period | Unenforceable unless trade secret is genuinely at stake and the employee was compensated for the restriction | Major. Remove or demand compensation equal to salary during the restricted period |
| Assignment of "all inventions ever" including personal projects | Employee Inventions Law protects off-work inventions unless directly related to the job | Major. Narrow to inventions made during work hours using work resources, related to the employer's business |
| Stated gross salary below the statutory minimum wage | As of 1 April 2026 the minimum wage is 6,443.85 NIS/month full-time (35.40 NIS/hour). A contract cannot set pay below this cogent floor; the figure is updated every April | Blocker. The salary must be raised to at least the current minimum wage. Verify the current rate, since it changes each April |
| "Global" or "comprehensive" overtime (`shaot globaliyot`) bundled into the base salary with no breakdown | Israeli courts often strike clauses that fold an unspecified, open-ended amount of overtime into one flat figure, because they mask unpaid overtime and defeat the Hours of Work and Rest Law. A global-overtime arrangement is only valid when it is a separate, quantified, capped component that is genuinely no less than the statutory 125%/150% rates for the hours actually worked | Major. Require overtime to be a separate line item with a stated hour cap and explicit 125%/150% rates, or removed in favor of hourly overtime tracking |
| Salary defined as "gross" or "net" ambiguously | Can cost the employee 30%+ in unexpected deductions | Blocker. Require explicit "gross" (brutto) and state the components |
| Bonus described as "at the sole discretion of the employer" without trigger | Employer can deny forever. If it's labeled "bonus" it is not deferred compensation | Minor if user accepts the risk. Major if the role was pitched with a large bonus component |
| Working hours beyond 42/week without overtime clause | Hours of Work and Rest Law caps standard workweek at 42 hours for 5-day weeks | Major. Overtime must be 125% for first 2 hours, 150% after |
| Clauses waiving the employee's rights under Israeli law | Unenforceable but signal bad faith | Major. Remove |
| Probation period (`tkufat nisayon`) longer than 12 months | Unusual and usually unenforceable. Standard is 3-6 months | Minor. Negotiate down to 3-6 months |
| Confidentiality clause extending forever | Standard is 3-5 years post-employment | Minor. Accept if narrowly scoped to trade secrets |
| No keren hishtalmut (education fund) for tech/professional roles | Standard in Israeli tech. Not legally required but expected | Major for tech roles. Negotiate to add with 7.5% employer / 2.5% employee split |
| Arbitration clause forcing disputes out of Israeli labor court | Labor courts are cheaper and more employee-friendly. Arbitration shifts risk | Major. Prefer standard labor court jurisdiction |

#### Numerical sanity checks

Compute these from the contract figures and flag anomalies:

| Check | Formula | Expected |
|-------|---------|----------|
| Minimum wage floor | Stated gross monthly salary (or hourly rate) | At least 6,443.85 NIS/month full-time, or 35.40 NIS/hour, as of 1 April 2026. Below this is a blocker. Verify the current rate |
| Employer pension contribution | Claimed % of gross | At least 6.5% benefits + 6% or 8.33% severance component |
| Employee pension contribution | Claimed % of gross | Max 6% (above is rare and unusual) |
| Keren hishtalmut split | Employer / employee % | Standard 7.5% / 2.5% |
| Total employer cost | Gross + 6.5% + severance + 7.5% KH + BL employer | Approx 120-125% of gross; above this suggests items already deducted from gross |
| Hoda'at mukdemet days | Days in contract | At least statutory minimum by tenure (see reference) |
| Annual vacation | Days in contract | At least 12 working days for 5-day week in years 1-4, rising to 23 after year 5 |
| Sick days | Days in contract | At least 1.5 per month = 18 per year accrual |

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

At the end of the review, always include:

```
DISCLAIMER
This is an automated review, not legal advice. For contracts with significant
blockers, or for senior / executive positions, consult an Israeli labor attorney
(orech din avoda) before signing. Review retrieved from:
- kolzchut.org.il
- nevo.co.il (legal database)
- Bituach Leumi official guidance
```

## Examples

### Example 1: Section 14 waiver with a base-only salary definition

**Clause as written:** "The employee agrees to the arrangement under Section 14 of the Severance Pay Law. The employer's contributions to the pension fund, calculated on the base salary, replace severance pay in full."

**Finding:** Major. The Section 14 waiver itself is legitimate, but "calculated on the base salary" is the trap: the employee's role pays a 12,000 NIS base plus a recurring 4,000 NIS fixed travel-and-role allowance. Because the waiver covers only the base, the employee loses the severance value of the allowance, and on termination receives less than the statutory calculation would yield.

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

### Scripts

| File | Purpose |
|------|---------|
| `scripts/contract_sanity_check.py` | Quick numerical validator for pension %, hoda'at mukdemet days, and vacation days |

## Recommended MCP Servers

| MCP | When to pair | Purpose |
|-----|--------------|---------|
| `israel-law` | For authoritative citations to statute text | Looks up exact text of Severance Pay Law, Notice Period Law, Hours of Work and Rest Law |
| `kolzchut` | For plain-language rule summaries and exceptions | Cross-references findings against All-Rights database |

The skill works without these MCPs using the built-in reference tables, but the citations become less specific.

## Gotchas

1. **Mistaking "at-will" clauses for enforceable terms**. Agents trained on US corporate templates assume at-will is normal. In Israel, it is unenforceable but common in foreign-drafted contracts. Always flag it, even if the rest of the contract is fine.

2. **Telling the user a 2-year non-compete is enforceable**. Israeli courts apply the Vichman precedent and rarely enforce non-competes beyond genuine trade-secret protection. Most 2-year non-competes are aspirational. Do not scare the user into refusing a good job over an unenforceable clause, but do flag it and recommend negotiation.

3. **Confusing Saif 14 with being a net positive**. Section 14 waivers CAN benefit the employee (monthly pension contributions instead of lump sum at termination) but ONLY if the "salary" definition for the waiver includes all compensation components. If it only covers base, the employee loses bonus-based severance. Always check the salary definition before endorsing the waiver.

4. **Ignoring keren hishtalmut absence for tech roles**. KH is not legally mandatory. But in Israeli tech, it is universal and a tax-advantaged benefit worth ~10% of salary. A tech contract without KH is a red flag even though it is "legal."

5. **Calculating hoda'at mukdemet in business days**. The law uses calendar days. A 30-day notice period means 30 actual days, including weekends and holidays. Agents sometimes quote business days, which is wrong.

6. **Accepting "discretionary bonus" at face value**. If the role was pitched with a 20% bonus component, a "fully discretionary" clause means the employer can pay zero forever. Flag this as major and suggest converting to a formulaic bonus tied to measurable KPIs.

7. **Forgetting that pension applies from day 1 in 2026**. As of post-2017 rules, employers must contribute to pension from day 1 of employment for employees with any prior pension fund. Agents sometimes quote a 3- or 6-month waiting period from older sources.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kolzchut: Hoda'at Mukdemet law | https://www.kolzchut.org.il/he/%D7%94%D7%95%D7%93%D7%A2%D7%94_%D7%9E%D7%95%D7%A7%D7%93%D7%9E%D7%AA_%D7%9C%D7%A4%D7%99%D7%98%D7%95%D7%A8%D7%99%D7%9D | Statutory advance notice days by tenure |
| Wikipedia: Prior Notice of Dismissal and Resignation Law | https://he.wikipedia.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%95%D7%93%D7%A2%D7%94_%D7%9E%D7%95%D7%A7%D7%93%D7%9E%D7%AA_%D7%9C%D7%A4%D7%99%D7%98%D7%95%D7%A8%D7%99%D7%9D_%D7%95%D7%9C%D7%94%D7%AA%D7%A4%D7%98%D7%A8%D7%95%D7%AA | Overview of the 2001 law |
| Nevo: Prior Notice Law full text | https://www.nevo.co.il/law_html/law00/71704.htm | Official legal text |
| Workrights.co.il: Advance notice rules | https://www.workrights.co.il/%D7%97%D7%95%D7%A7_%D7%94%D7%95%D7%93%D7%A2%D7%94_%D7%9E%D7%95%D7%A7%D7%93%D7%9E%D7%AA | Practical guide |
| Kolzchut: Section 14 of the Severance Pay Law | https://www.kolzchut.org.il/he/%D7%A1%D7%A2%D7%99%D7%A3_14_%D7%9C%D7%97%D7%95%D7%A7_%D7%A4%D7%99%D7%A6%D7%95%D7%99%D7%99_%D7%A4%D7%99%D7%98%D7%95%D7%A8%D7%99%D7%9D | Section 14 waiver rules and 8.33% requirement |
| CWS Israel: Employment contracts in Israel | https://www.cxcglobal.com/global-hiring-guide/israel/employment-contracts-in-israel/ | Contract structure and mandatory clauses |
| Bituach Leumi: For salaried workers rates | https://www.btl.gov.il/English%20Homepage/Insurance/Ratesandamount/Pages/forSalaried.aspx | National Insurance contribution rates |

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| Review found 15 "blockers" in a standard contract | Over-flagging, probably labeling minor issues as blockers | Re-classify using strict severity: blocker = illegal, major = below market, minor = style |
| Contract is in Hebrew only, Hebrew quality is poor | Employer used a template translation | Flag as major: request a clean Hebrew or bilingual version |
| Salary quoted as "12,000 NIS" with no brutto/neto | Ambiguous | Ask user if they confirmed with employer. Flag as blocker to force clarity |
| Non-compete looks scary to user | User feels legally bound | Explain Vichman precedent: rarely enforced beyond trade secrets. Still negotiate, but do not refuse the job over it alone |
| Section 14 clause without waiver text | Employer may be assuming it applies | Flag as major: require explicit Saif 14 language or clarify that standard severance applies |
| Contract is for a contractor (kablan), not employee | Different set of rules | This skill is for employment contracts only. Recommend the user consult a labor attorney about misclassification risk |
