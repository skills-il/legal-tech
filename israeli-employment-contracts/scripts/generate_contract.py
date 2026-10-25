#!/usr/bin/env python3
"""Generate Israeli employment contract templates with calculated benefit rates.

Produces a structured employment contract with all mandatory Israeli clauses
pre-filled based on employee details: name, position, salary, start date,
and work percentage.

Usage:
    python generate_contract.py --help
    python generate_contract.py \
        --employee-name "Israel Israeli" \
        --position "Software Engineer" \
        --salary 25000 \
        --start-date 2026-04-01 \
        --work-percent 100

    python generate_contract.py \
        --employee-name "Dana Cohen" \
        --position "Marketing Manager" \
        --salary 15000 \
        --start-date 2026-05-01 \
        --work-percent 60 \
        --output contract_dana.md
"""

import argparse
import sys
import calendar
from datetime import datetime, timedelta
from typing import Optional


# --- Current rates ---
# Last verified: 2026-10-25. Update annually when extension orders change.
# Sources:
#   Minimum wage: Histadrut announcement, effective 2026-04-01
#     https://global.histadrut.org.il/news/israels-minimum-wage-to-rise-by-3-3/
#   Dmei Havra'a (private sector): Kolzchut -- 451.5 NIS/day from havra'a year 2026,
#     retroactively, per the extension order published 18.08.2026
#     https://www.kolzchut.org.il/he/%D7%93%D7%9E%D7%99_%D7%94%D7%91%D7%A8%D7%90%D7%94
#   Work hours: Hours of Work and Rest Law, 1951, as amended by extension order
#     effective 2018-04-01 (workweek reduced from 43 to 42 hours)

PENSION_EMPLOYER_RATE = 0.065       # 6.5%
PENSION_EMPLOYEE_RATE = 0.06        # 6%
SEVERANCE_RATE = 0.0833             # 8.33%
HISHTALMUT_EMPLOYER_RATE = 0.075    # 7.5%
HISHTALMUT_EMPLOYEE_RATE = 0.025    # 2.5%
HAVRA_A_DAILY_RATE = 451.5          # NIS per day, private-sector rate for havra'a year 2026
                                    # (1.7.2025-30.6.2026), per the extension order published 18.08.2026
                                    # (raised from 418). Verify before use for a later havra'a year.
MINIMUM_WAGE_MONTHLY = 6443.85      # NIS, effective 2026-04-01 (prior: 6,247.67)
MINIMUM_WAGE_HOURLY = 35.40         # NIS, based on 182 hours/month (42h x 52 / 12)
PENSION_SALARY_CAP_2026 = 13769     # NIS, national average wage: the statutory pension base is the
                                    # LOWER of base salary and this figure, unless the contract says more
STANDARD_WORK_HOURS_DAY = 8.6       # hours on 4 days of a 5-day week, plus one short day:
STANDARD_SHORT_DAY_HOURS = 7.6      # (4 x 8.6 + 7.6 = 42), per the shortened-work-week extension order
TRAVEL_DAILY_CEILING = 22.60        # NIS per day, travel-expenses extension order (verify before use)
STANDARD_WORK_HOURS_WEEK = 42.0     # hours per week (since 2018-04-01)
STANDARD_WORK_DAYS_WEEK = 5         # days

# Convalescence days by seniority year
HAVRA_A_DAYS = {
    1: 5,
    2: 6, 3: 6,
    4: 7, 5: 7, 6: 7, 7: 7, 8: 7, 9: 7, 10: 7,
    11: 8, 12: 8, 13: 8, 14: 8, 15: 8,
    16: 9, 17: 9, 18: 9, 19: 9,
}
HAVRA_A_DAYS_20_PLUS = 10

# Annual leave, net WORK days for a 5-day week, by calendar year of seniority.
# Statutory (Annual Leave Law, 1951, converted from calendar days to work days):
ANNUAL_LEAVE_DAYS = {
    1: 12, 2: 12, 3: 12, 4: 12, 5: 12,
    6: 14, 7: 15, 8: 16, 9: 17, 10: 18, 11: 19,
}
ANNUAL_LEAVE_DAYS_12_PLUS = 20
# Where the Shortened Work Week extension order applies (the higher figure wins):
SHORT_WEEK_ORDER_LEAVE = {1: 12, 2: 12, 3: 12, 4: 12, 5: 12, 6: 17, 7: 17, 8: 17}
SHORT_WEEK_ORDER_LEAVE_9_PLUS = 23

SICK_DAYS_PER_MONTH = 1.5
SICK_DAYS_MAX = 90


def get_havra_a_days(seniority_years: int) -> int:
    """Return convalescence days for given seniority."""
    if seniority_years >= 20:
        return HAVRA_A_DAYS_20_PLUS
    return HAVRA_A_DAYS.get(seniority_years, 5)


def get_annual_leave_days(seniority_years: int, short_week_order: bool = False) -> int:
    """Return minimum annual leave WORK days for a 5-day week.

    By default returns the statutory figure. With short_week_order=True, returns
    the higher of the statute and the Shortened Work Week extension order.
    """
    statutory = (ANNUAL_LEAVE_DAYS_12_PLUS if seniority_years >= 12
                 else ANNUAL_LEAVE_DAYS.get(seniority_years, 12))
    if not short_week_order:
        return statutory
    order = (SHORT_WEEK_ORDER_LEAVE_9_PLUS if seniority_years >= 9
             else SHORT_WEEK_ORDER_LEAVE.get(seniority_years, 12))
    return max(statutory, order)


def calculate_notice_period_days(seniority_months: int, pay_basis: str = "monthly") -> float:
    """Calculate notice period in days based on seniority and pay basis.

    The first-year ladder differs by pay basis (Prior Notice for Dismissal and
    Resignation Law, 2001):
      - monthly-paid (oved be'mascoret): months 1-6 = 1 day/month;
        months 7-11 = 6 days + 2.5 days per full month from month 7;
        30 days (1 month) from 12 completed months.
      - daily/hourly-paid (oved be'sachar): 1 day per month worked in year 1;
        in year 2, 14 days + 1 day per 2 months worked in year 2; in year 3,
        21 days + 1 day per 2 months worked in year 3; after 3 years, 30 days.
    A monthly-paid worker reaches 30 days (1 month) from year 2.
    """
    # seniority_months = COMPLETED months. A completed year moves the worker into
    # the next band (12 completed months = first month of year 2).
    if pay_basis == "hourly":
        if seniority_months < 12:
            return seniority_months  # 1 day per month worked
        if seniority_months < 24:
            return 14 + (seniority_months - 12) // 2
        if seniority_months < 36:
            return 21 + (seniority_months - 24) // 2
        return 30

    if seniority_months >= 12:
        return 30  # monthly-paid: 1 month from one year of seniority

    # Monthly-paid worker.
    if seniority_months <= 6:
        return seniority_months  # 1 day per month
    months_after_6 = seniority_months - 6
    return 6 + months_after_6 * 2.5  # e.g. 9 months = 13.5 days, not rounded down


def calculate_benefits(salary: float, work_percent: float) -> dict:
    """Calculate all mandatory benefit amounts."""
    adjusted_salary = salary * (work_percent / 100.0)

    pension_employer = adjusted_salary * PENSION_EMPLOYER_RATE
    pension_employee = adjusted_salary * PENSION_EMPLOYEE_RATE
    severance_component = adjusted_salary * SEVERANCE_RATE
    hishtalmut_employer = adjusted_salary * HISHTALMUT_EMPLOYER_RATE
    hishtalmut_employee = adjusted_salary * HISHTALMUT_EMPLOYEE_RATE
    # Pro-rated to position scope; owed only after 12 months, then retroactively.
    havra_a_first_year = get_havra_a_days(1) * HAVRA_A_DAILY_RATE * (work_percent / 100.0)

    total_employer_cost = (
        adjusted_salary
        + pension_employer
        + severance_component
        + hishtalmut_employer
    )

    return {
        "adjusted_salary": adjusted_salary,
        "pension_employer": pension_employer,
        "pension_employee": pension_employee,
        "severance_component": severance_component,
        "hishtalmut_employer": hishtalmut_employer,
        "hishtalmut_employee": hishtalmut_employee,
        "havra_a_first_year": havra_a_first_year,
        "total_employer_cost": total_employer_cost,
        "annual_leave_days_year1": get_annual_leave_days(1),
        "sick_days_per_month": SICK_DAYS_PER_MONTH,
        "notice_period_month1": calculate_notice_period_days(1),
        "notice_period_month6": calculate_notice_period_days(6),
        "notice_period_year2": calculate_notice_period_days(24),
        "notice_period_hourly_month18": calculate_notice_period_days(18, pay_basis="hourly"),
        "notice_period_hourly_month30": calculate_notice_period_days(30, pay_basis="hourly"),
        # Daily/hourly-paid (oved be'sachar) first-year notice differs: 1 day/month.
        "notice_period_hourly_month12": calculate_notice_period_days(12, pay_basis="hourly"),
        "notice_period_monthly_month12": calculate_notice_period_days(12, pay_basis="monthly"),
    }


def format_currency(amount: float) -> str:
    """Format amount as NIS currency."""
    return f"{amount:,.2f} NIS"


def generate_contract(
    employee_name: str,
    position: str,
    salary: float,
    start_date: str,
    work_percent: float,
    employer_name: str = "[EMPLOYER NAME]",
    employer_id: str = "[EMPLOYER ID]",
    employee_id: str = "[EMPLOYEE ID]",
) -> str:
    """Generate a full employment contract template."""

    benefits = calculate_benefits(salary, work_percent)
    adj_salary = benefits["adjusted_salary"]

    # Parse start date
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        start_dt = datetime.now()
    start_formatted = start_dt.strftime("%d/%m/%Y")

    # Probation end date: 6 calendar months, ending the day before the same date
    # 6 months later; when that date does not exist (31 Aug -> no 31 Feb), the
    # period ends on the last day of the target month.
    month = start_dt.month - 1 + 6
    year = start_dt.year + month // 12
    month = month % 12 + 1
    last_day = calendar.monthrange(year, month)[1]
    if start_dt.day <= last_day:
        probation_end = datetime(year, month, start_dt.day) - timedelta(days=1)
    else:
        probation_end = datetime(year, month, last_day)
    probation_formatted = probation_end.strftime("%d/%m/%Y")

    position_percent = f"{work_percent:.0f}%"
    work_type = "Full-time" if work_percent == 100 else f"Part-time ({position_percent})"

    contract = f"""# Employment Contract / Chozeh Avoda
# חוזה עבודה

---

**Date / Taarich:** {start_formatted}

---

## 1. Parties / HaTzedadim / הצדדים

**Employer / Ma'asik / מעסיק:**
- Name: {employer_name}
- Company ID (Chet-Peh): {employer_id}
- Address: [EMPLOYER ADDRESS]

**Employee / Oved / עובד:**
- Name: {employee_name}
- ID Number (Teudat Zehut): {employee_id}
- Address: [EMPLOYEE ADDRESS]

---

## 2. Position / Tafkid / תפקיד

The Employee is hired for the position of **{position}**.
The Employee shall report to [MANAGER NAME / TITLE].
The Employee's responsibilities include: [DESCRIBE RESPONSIBILITIES].

---

## 3. Start Date and Probation / Taarich Hatchala VeTkufat Nisayon / תאריך התחלה ותקופת ניסיון

- **Start date:** {start_formatted}
- **Employment type:** {work_type}
- **Probation period (Tkufat Nisayon):** 6 months, ending {probation_formatted}
- During probation, either party may terminate; the statutory notice period applies (there is no statutory "shortened notice" during probation).
- Probation does not affect statutory protections, including the Employment of Women Law (from 6 months a pregnant employee may be dismissed only with a permit).
- Successful completion of probation does not require formal notice; employment continues automatically.

---

## 4. Work Hours / She'ot Avoda / שעות עבודה

- **Work days:** Sunday through Thursday (5-day work week)
- **Daily hours (full-time):** {STANDARD_WORK_HOURS_DAY} hours on four days and {STANDARD_SHORT_DAY_HOURS} hours on one fixed short day (42-hour week since April 2018)
- **Weekly hours (full-time):** {STANDARD_WORK_HOURS_WEEK} hours{"" if work_percent == 100 else f"; this position: {STANDARD_WORK_HOURS_WEEK * work_percent / 100:.1f} hours [ADJUST DAYS / HOURS]"}
- **Position scope:** {position_percent} of full-time position
- **Overtime:** Per Hours of Work and Rest Law -- 125% for first 2 extra hours, 150% thereafter.
- **Weekly rest:** at least 36 consecutive hours, including the Employee's day of rest [Friday-Saturday].

---

## 5. Salary / Sachar / שכר

- **Gross monthly salary:** {format_currency(adj_salary)}
- **Payment date:** No later than the 9th of the following month (per Protection of Wages Law / Chok Haganat HaSachar)
- **Payment method:** Bank transfer to Employee's designated account
- **Travel expenses:** reimbursed per the travel-expenses extension order, the reduced bus fare up to {format_currency(TRAVEL_DAILY_CEILING)} a day or a monthly pass if cheaper (taxable)
- **Holiday pay (hourly/daily paid only):** after 3 months, for holidays the Employee was due to work but did not

---

## 6. Pension and Severance / Pensia VePitzuim / פנסיה ופיצויים

**Pension fund contributions (per Tzav Harchava / Extension Order):**

| Component | Employer | Employee |
|-----------|----------|----------|
| Pension (Tagmulim) | {PENSION_EMPLOYER_RATE*100:.1f}% = {format_currency(benefits['pension_employer'])} | {PENSION_EMPLOYEE_RATE*100:.1f}% = {format_currency(benefits['pension_employee'])} |
| Severance (Pitzuim) | {SEVERANCE_RATE*100:.2f}% = {format_currency(benefits['severance_component'])} | -- |

Amounts above are computed on the full gross salary. **Salary base for contributions:**
[the full gross base salary / the base salary up to the national average wage].
The statutory minimum is the lower of the base salary and the national average
wage ({format_currency(PENSION_SALARY_CAP_2026)} in 2026); contributing on the full
salary is a contractual undertaking and must be stated expressly.

**Pension fund:** [FUND NAME, e.g., Meitav Dash, Menora, Harel, Migdal]

### Section 14 Arrangement / Hasdarot Saif 14 / הסדרות סעיף 14

In accordance with Section 14 of the Severance Pay Law, 1963, and the General
Authorization under it as applied by the pension extension order (automatic for
the mandatory 6%), the Employer's contributions to the pension fund / insurance
policy as detailed above shall come in place of severance pay in respect of the
salary on which said contributions were made and for the period they were made:
in full where the severance component is 8.33%, and only in proportion to the
amount deposited where it is 6% (about 72%, the balance remaining owed).

The Employee hereby agrees and acknowledges that the Employer's contributions
to the pension insurance fund shall come in lieu of the severance pay the
Employee is entitled to for said salary components. At 8.33% the Employer is
released from any additional severance payment obligation for that salary and
period; below 8.33% (such as 6%) the Employer is released only for the share the
deposits cover (deposit rate / 8.33%) and, where the Employee is entitled to
severance, pays on termination the completion: the difference between 8.33% and
the rate deposited in each year, multiplied by the last salary. For the 2.33% completion (8.33% in total), the Employer
shall notify the fund in writing, with a copy to the Employee, that Section 14
also applies to it.

**Employee acknowledgment:** _____________________ Date: __________

**Severance basis (for any salary or period not covered by Section 14
deposits):** The Employee's statutory severance under the Severance Pay Law,
1963 (Section 12, and for an hourly or daily paid Employee the 1983 Regulations
under s.12(b)) is one month's last salary for each year of employment with the
Employer, pro-rated for partial years, payable on termination. Any period for
which no severance deposits were made (for example the pension waiting period)
is owed at the last salary when the employment ends in circumstances that
entitle the Employee to severance.

---

## 7. Education Fund / Keren Hishtalmut / קרן השתלמות

| Component | Rate | Monthly Amount |
|-----------|------|----------------|
| Employer contribution | {HISHTALMUT_EMPLOYER_RATE*100:.1f}% | {format_currency(benefits['hishtalmut_employer'])} |
| Employee contribution | {HISHTALMUT_EMPLOYEE_RATE*100:.1f}% | {format_currency(benefits['hishtalmut_employee'])} |

**Fund:** [FUND NAME]
**Vesting:** 6 years (3 years for designated educational purposes)

---

## 8. Convalescence Pay / Dmei Havra'a / דמי הבראה

The Employee shall receive convalescence pay (Dmei Havra'a) per the applicable
extension order, based on seniority:

- **Year 1:** 5 days = {format_currency(benefits['havra_a_first_year'])} (daily rate {format_currency(HAVRA_A_DAILY_RATE)} for havra'a year 2026{"" if work_percent == 100 else f", pro-rated to {position_percent}"})
- Owed only after 12 months of employment, then retroactively from the start date, at the rate in force for the havra'a year paid
- Payment: Annual lump sum, typically in June-July
- Days increase with seniority per the extension order table

---

## 9. Annual Leave / Chofsha Shnatit / חופשה שנתית

No less than the Annual Leave Law (1951) and, where it applies, the extension
order on the shortened work week, whichever is higher. Work days per calendar
year of seniority, 5-day week:

| Seniority | Statute | Shortened Work Week extension order |
|-----------|---------|-------------------------------------|
| Years 1-5 | {get_annual_leave_days(1)} | {get_annual_leave_days(1, True)} |
| Year 6 | {get_annual_leave_days(6)} | {get_annual_leave_days(6, True)} |
| Year 7 | {get_annual_leave_days(7)} | {get_annual_leave_days(7, True)} |
| Year 8 | {get_annual_leave_days(8)} | {get_annual_leave_days(8, True)} |
| Year 9 | {get_annual_leave_days(9)} | {get_annual_leave_days(9, True)} |
| Year 10 | {get_annual_leave_days(10)} | {get_annual_leave_days(10, True)} |
| Year 11 | {get_annual_leave_days(11)} | {get_annual_leave_days(11, True)} |
| Year 12+ | {get_annual_leave_days(12)} | {get_annual_leave_days(12, True)} |

{"Part-time: an employee working fewer HOURS on every work day accrues the same number of leave days; an employee who works fewer than 200 days in the year accrues days worked / 200 x the calendar-day entitlement, rounded down. A first calendar year that starts mid-year is pro-rated." if work_percent < 100 else ""}

---

## 10. Sick Leave / Yemei Machala / ימי מחלה

- **Accrual:** {SICK_DAYS_PER_MONTH} days per month ({SICK_DAYS_PER_MONTH * 12:.0f} days per year)
- **Maximum accumulation:** {SICK_DAYS_MAX} days
- **Payment tiers:**
  - Day 1: No payment
  - Days 2-3: 50% of daily salary
  - Day 4 onward: 100% of daily salary
- **Medical certificate:** As the Employer reasonably specifies (commonly from day 1 of absence)

---

## 11. Notice Period / Tkufat Hodaa Mukdemet / תקופת הודעה מוקדמת

Either party may terminate this agreement by providing written notice:

| Seniority | Monthly-paid (oved be'mascoret) | Daily/hourly-paid (oved be'sachar) |
|-----------|----------------------------------|-------------------------------------|
| Months 1-6 | 1 day per month of employment | 1 day per month worked |
| Months 7-11 | 6 days + 2.5 days per additional full month | 1 day per month worked |
| Year 2 | 30 days (1 month) | 14 days + 1 day per 2 months worked in year 2 |
| Year 3 | 30 days (1 month) | 21 days + 1 day per 2 months worked in year 3 |
| After 3 years | 30 days (1 month) | 30 days (1 month) |

The ladders differ by pay basis for the first three years: a daily/hourly-paid
worker reaches a full month of notice only after 3 years.

---

## 12. Confidentiality / Sodiyut / סודיות

The Employee undertakes to maintain the confidentiality of all proprietary
information, trade secrets, business plans, customer lists, technical data,
and any other confidential information of the Employer, both during and after
the term of employment.

This obligation shall survive the termination of employment for a period of
[DURATION, recommended: 24-36 months].

---

## 13. Intellectual Property / Kinyan Ruchani / קניין רוחני

(a) All works, software, documentation, designs and other work product created
by the Employee for the purposes of and in the course of the employment, and
every service invention under Patents Law s.132 (an invention reached as a
result of and during the service), belong to the Employer ("Work Product"). To
the extent any right does not vest in the Employer by law, the Employee hereby
irrevocably assigns it to the Employer, worldwide, including patents,
copyrights, trade secrets and other intellectual property rights.

(b) Subject to and without derogating from Patents Law s.132, work outside the
scope of the employment, made on the Employee's own time, without use of the
Employer's resources or confidential information, and that is not a service
invention, is not Work Product. [OPTIONAL, NEGOTIATED: also treat as Work
Product any work made using the Employer's confidential information or
resources.]

(c) The Employee shall notify the Employer IN WRITING of every invention reached
as a result of or during the service (Patents Law s.131), shall not include a
s.132(b) "vests in me absent reply" statement in such a notice. The Employee shall sign all documents and
take all reasonable actions needed to perfect the Employer's rights, during and
after the employment.

(d) Compensation for service inventions (Patents Law s.134): [DEFAULT: the Salary
is full and final consideration and no further compensation or royalties are
due; this is an agreement within the meaning of s.134 / OR STATE AGREED TERMS].

(e) All pre-existing IP, whether or not listed in Schedule A, remains the
Employee's. Incorporating
it, or third-party or open-source material, into Work Product requires the
Employer's prior written approval; the Employee grants the Employer a
non-exclusive, perpetual, irrevocable, worldwide, royalty-free, fully paid-up,
transferable and sublicensable licence to use, reproduce, modify, create
derivative works of, distribute and otherwise exploit it as part of or in
connection with the Work Product, surviving termination.

(f) Moral rights (works other than software) are personal and not transferable;
to the extent the law permits, the Employee consents to the Employer's
attribution practice and to modifications in the ordinary course of business.

**Pre-existing IP (Schedule A):** [ATTACH OR WRITE "NONE"]

---

## 14. Non-Compete / Ee Tcharut / אי-תחרות

For a period of [NUMBER, as short as the protected interest justifies] months following termination of employment,
the Employee shall not directly engage with the following specific competitors:
[LIST SPECIFIC COMPETITORS].

This restriction is limited to [DESCRIBE SPECIFIC SCOPE/FIELD].

Note: Under the National Labor Court's Check Point ruling (ע"ע 164/99), a
post-employment restriction is generally void and is given effect only if it is
reasonable and protects a recognized interest such as a genuine trade secret,
special costly training, or special consideration paid for the restriction
[STATE WHICH ONE APPLIES].

---

## 15. General Provisions / Horaot Klaliyot / הוראות כלליות

- **Governing law:** The laws of the State of Israel
- **Jurisdiction:** The Regional Labor Court of [CITY]
- **Entire agreement:** This contract constitutes the entire agreement between
  the parties and supersedes all prior agreements, written or oral
- **Amendments:** Any amendment to this contract must be in writing and signed
  by both parties

---

## Cost Summary for Employer / Sikum Aluyot LeMa'asik / סיכום עלויות למעסיק

| Component | Monthly Amount |
|-----------|----------------|
| Gross salary | {format_currency(adj_salary)} |
| Pension (employer) | {format_currency(benefits['pension_employer'])} |
| Severance (Saif 14) | {format_currency(benefits['severance_component'])} |
| Keren Hishtalmut (employer) | {format_currency(benefits['hishtalmut_employer'])} |
| **Total employer cost** | **{format_currency(benefits['total_employer_cost'])}** |

*Note: Does not include Bituach Leumi (employer portion), Dmei Havra'a,
travel expenses (mandatory, up to {format_currency(TRAVEL_DAILY_CEILING)} a day), or other variable costs.*

---

## Signatures / Chatimot / חתימות

**Employer / Ma'asik / מעסיק:**

Name: {employer_name}
Title: ____________________
Signature: ____________________
Date: ____________________

**Employee / Oved / עובד:**

Name: {employee_name}
Signature: ____________________
Date: ____________________

---

*This contract template is generated for informational purposes. It should be
reviewed by a qualified Israeli labor law attorney before execution.*

*תבנית חוזה זו נוצרה למטרות מידע בלבד. יש לבדוק אותה על ידי עורך דין
המתמחה בדיני עבודה ישראליים לפני חתימה.*
"""
    return contract


def main():
    parser = argparse.ArgumentParser(
        description="Generate Israeli employment contract templates with calculated benefit rates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s --employee-name "Israel Israeli" --position "Software Engineer" --salary 25000 --start-date 2026-04-01
  %(prog)s --employee-name "Dana Cohen" --position "Designer" --salary 15000 --start-date 2026-05-01 --work-percent 60
  %(prog)s --employee-name "Test User" --position "QA Lead" --salary 20000 --start-date 2026-04-01 --output contract.md

Current rates (2025-2026):
  Pension (employer):      6.5%%
  Pension (employee):      6.0%%
  Severance (Saif 14):     8.33%%
  Keren Hishtalmut (emp):  7.5%%
  Keren Hishtalmut (ee):   2.5%%
  Dmei Havra'a daily rate: {HAVRA_A_DAILY_RATE:.2f} NIS
  Minimum wage (monthly):  {MINIMUM_WAGE_MONTHLY:.2f} NIS
"""
    )

    parser.add_argument(
        "--employee-name",
        required=True,
        help="Full name of the employee",
    )
    parser.add_argument(
        "--position",
        required=True,
        help="Job title / position",
    )
    parser.add_argument(
        "--salary",
        type=float,
        required=True,
        help="Gross monthly salary in NIS (for 100%% position)",
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help="Employment start date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--work-percent",
        type=float,
        default=100.0,
        help="Position scope as percentage (default: 100)",
    )
    parser.add_argument(
        "--employer-name",
        default="[EMPLOYER NAME]",
        help="Employer / company name",
    )
    parser.add_argument(
        "--employer-id",
        default="[EMPLOYER ID]",
        help="Employer company ID (Chet-Peh number)",
    )
    parser.add_argument(
        "--employee-id",
        default="[EMPLOYEE ID]",
        help="Employee ID number (Teudat Zehut)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output file path (default: print to stdout)",
    )

    args = parser.parse_args()

    # Validate salary against minimum wage
    adjusted_min = MINIMUM_WAGE_MONTHLY * (args.work_percent / 100.0)
    if args.salary * (args.work_percent / 100.0) < adjusted_min:
        print(
            f"WARNING: Adjusted salary ({args.salary * args.work_percent / 100.0:.2f} NIS) "
            f"is below minimum wage for {args.work_percent:.0f}% position "
            f"({adjusted_min:.2f} NIS).",
            file=sys.stderr,
        )

    # Validate date format
    try:
        datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError:
        print(
            f"ERROR: Invalid date format '{args.start_date}'. Use YYYY-MM-DD.",
            file=sys.stderr,
        )
        sys.exit(1)

    contract = generate_contract(
        employee_name=args.employee_name,
        position=args.position,
        salary=args.salary,
        start_date=args.start_date,
        work_percent=args.work_percent,
        employer_name=args.employer_name,
        employer_id=args.employer_id,
        employee_id=args.employee_id,
    )

    # Self-test: drafter notes must never appear in the contract body.
    if "DRAFTING NOTE" in contract:
        sys.exit("internal error: a drafting note leaked into the contract body")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(contract)
        print(f"Contract written to {args.output}", file=sys.stderr)
    else:
        print(contract)

    # Drafting note for the user, kept out of the contract body.
    print(
        "\nDRAFTING NOTE (not part of the contract): section 13(d) is the s.134 "
        "compensation agreement. Absent an agreement, the Compensation and Royalties "
        "Committee decides compensation; whether a waiver is enforceable in particular "
        "circumstances is a question for counsel. The Employer should answer every "
        "invention notice in writing within six months: Patents Law s.132(b) operates "
        "by statute and the contract cannot be relied on to override it.",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
