#!/usr/bin/env python3
"""Quick sanity checks for Israeli employment contract numerical fields.

Validates:
- Pension contribution rates against Mandatory Pension Order 2008 minimums
  (with the lower tagmulim floor for a non-pension-fund product)
- Hoda'at mukdemet days against Prior Notice Law 2001 schedule
- Annual vacation days against the higher of Annual Leave Law 1951 and the Shortened Work Week extension order
- Sick days against Sick Pay Law 1976

Usage:
    python contract_sanity_check.py --pension-employer 6.5 --pension-severance 8.33 --pension-employee 6 --notice-days 30 --tenure-months 24 --worker-type monthly --vacation 12 --sick 18
    python contract_sanity_check.py --example
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

MANDATORY_PENSION_EMPLOYER_BENEFITS_MIN = 6.5
# On a product that is not a pension fund (typically managers' insurance) the
# employer's tagmulim may be lower, because its share must also buy disability
# cover for 75% of the determining wage. Tagmulim alone may not fall below 5%.
NON_PENSION_FUND_EMPLOYER_BENEFITS_MIN = 5.0
MANDATORY_PENSION_SEVERANCE_MIN = 6.0  # Below this is not enough for severance coverage
MANDATORY_PENSION_SEVERANCE_FULL = 8.33  # Standard for full Section 14 waiver
MANDATORY_PENSION_EMPLOYEE_STD = 6.0
MANDATORY_PENSION_EMPLOYEE_MIN = 6.0  # Expansion Order floor. 7% is credit-optimal under s.45a.
KH_EMPLOYER_STD = 7.5
# Under 18: Youth Labour Law s.27(a) reads 18 days into Annual Leave Law s.3(a),
# which counts GROSS days (weekly rest included). Converted like the adult ladder,
# that is 14 net working days on a 5-day week.
MINOR_VACATION_GROSS_DAYS = 18
KH_EMPLOYEE_STD = 2.5


@dataclass
class Finding:
    severity: str  # "blocker" | "major" | "minor"
    field: str
    observed: str
    expected: str
    rule: str


def required_notice_days_monthly(tenure_months: int) -> float:
    """Statutory advance notice for a monthly worker, by COMPLETED months.

    Kol Zchut counts full months only and gives a month's notice from one
    completed year onward, so 12 completed months is already 30 days.
    """
    if tenure_months <= 0:
        return 0
    if tenure_months <= 6:
        return float(tenure_months)
    if tenure_months <= 11:
        return 6 + 2.5 * (tenure_months - 6)
    return 30.0


def required_notice_days_hourly(tenure_months: int) -> float:
    """Statutory advance notice for hourly/daily workers (oved sha'ati/yomi).

    This is a DIFFERENT schedule from monthly workers, per the Prior Notice Law
    2001 as summarized by Kolzchut:
      - Year 1 (0-11 completed months):  1 day per month worked.
      - Year 2 (12-23 completed months): 14 days + 1 day for every 2 months worked in year 2.
      - Year 3 (24-35 completed months): 21 days + 1 day for every 2 months worked in year 3.
      - 3 completed years (36 months) onward: 30 days, flat.
    """
    if tenure_months <= 0:
        return 0
    if tenure_months <= 11:
        return float(tenure_months)
    if tenure_months <= 23:
        months_into_year = tenure_months - 12
        return 14 + (months_into_year // 2)
    if tenure_months <= 35:
        months_into_year = tenure_months - 24
        return 21 + (months_into_year // 2)
    return 30.0


def extension_order_net_vacation_days(tenure_years: int) -> int:
    """Net leave days per the Shortened Work Week extension order (5-day week).

    The order states NET days (actual absence days, excluding the weekly rest):
    12 for years 1-5, 17 for years 6-8, and 23 from year 9. It covers most
    5-day workplaces but NOT domestic work, workplaces with fewer than four
    employees, government or municipal companies, or workplaces whose move to a
    5-day week was settled by a collective agreement.
    """
    if tenure_years <= 5:
        return 12
    if tenure_years <= 8:
        return 17
    return 23


def gross_vacation_days(tenure_years: int) -> int:
    """Statutory gross leave days per Annual Leave Law 1951 s.3(a)."""
    if tenure_years <= 5:
        return 16
    if tenure_years == 6:
        return 18
    if tenure_years == 7:
        return 21
    return min(28, 21 + (tenure_years - 7))


def statutory_net_vacation_days(tenure_years: int) -> int:
    """The statutory gross ladder converted to net absence days on a 5-day week.

    Gross days are converted by calendar weeks, as Kol Zchut's statute-only
    table does: each full week of 7 gross days is 5 net days, and the leftover
    gross days count one-for-one up to the 5 working days of a week. So 18 gross
    days is 14 net, 25 is 19 and 26 is 20 (a straight 5/7 ratio gives 13, 18, 19).
    """
    gross = gross_vacation_days(tenure_years)
    return 5 * (gross // 7) + min(gross % 7, 5)


def required_vacation_days(tenure_years: int, extension_order_applies: bool = True) -> int:
    """Minimum annual leave in NET working days for a 5-day week.

    Two ladders apply and the employee is entitled to the HIGHER of them: the
    Annual Leave Law and, where it covers the workplace, the Shortened Work
    Week extension order. Encoding only the statute understates the minimum
    from year 6 onward for most private-sector employees.
    """
    statutory = statutory_net_vacation_days(tenure_years)
    if not extension_order_applies:
        return statutory
    return max(statutory, extension_order_net_vacation_days(tenure_years))


def check(
    pension_employer_benefits: float,
    pension_severance: float,
    pension_employee: float,
    notice_days: float,
    tenure_months: int,
    worker_type: str,
    vacation_days: int,
    sick_days_per_year: int,
    kh_employer: float | None = None,
    extension_order_applies: bool = True,
    non_pension_fund: bool = False,
    full_section_14: bool = False,
    leave_year: int | None = None,
    minor: bool = False,
) -> list[Finding]:
    findings: list[Finding] = []
    # Leave ladders are indexed by the year of service being worked, and the
    # Annual Leave Law counts that year by CALENDAR year (January to December,
    # the starting year being year 1). Completed months + 1 can still lag a
    # mid-year starter by one, so pass leave_year when the start date is known.
    tenure_years = leave_year if leave_year else tenure_months // 12 + 1

    employer_floor = (
        NON_PENSION_FUND_EMPLOYER_BENEFITS_MIN if non_pension_fund else MANDATORY_PENSION_EMPLOYER_BENEFITS_MIN
    )
    if pension_employer_benefits < employer_floor:
        findings.append(
            Finding(
                severity="blocker",
                field="Employer pension (benefits component)",
                observed=f"{pension_employer_benefits}%",
                expected=f">= {employer_floor}%",
                rule="Mandatory Pension Expansion Order 2008",
            )
        )
    elif non_pension_fund and pension_employer_benefits < MANDATORY_PENSION_EMPLOYER_BENEFITS_MIN:
        findings.append(
            Finding(
                severity="minor",
                field="Employer pension (benefits component)",
                observed=f"{pension_employer_benefits}% on a non-pension-fund product",
                expected="Disability cover for 75% of the determining wage, tagmulim plus disability capped at 7.5%",
                rule="Mandatory Pension Expansion Order 2008 (non-pension-fund product). Confirm the disability cover is in the contract or that the employee chose a product without it",
            )
        )

    if pension_employee < MANDATORY_PENSION_EMPLOYEE_MIN:
        findings.append(
            Finding(
                severity="blocker",
                field="Employee pension (employee component)",
                observed=f"{pension_employee}%",
                expected=f">= {MANDATORY_PENSION_EMPLOYEE_MIN}%",
                rule="Mandatory Pension Expansion Order 2008 (6% is the minimum, not a maximum)",
            )
        )

    if pension_severance < MANDATORY_PENSION_SEVERANCE_MIN:
        findings.append(
            Finding(
                severity="blocker",
                field="Employer pension (severance component)",
                observed=f"{pension_severance}%",
                expected=f">= {MANDATORY_PENSION_SEVERANCE_MIN}%",
                rule="Mandatory Pension Expansion Order 2008",
            )
        )
    elif full_section_14 and pension_severance < MANDATORY_PENSION_SEVERANCE_FULL:
        findings.append(
            Finding(
                severity="major",
                field="Employer pension (severance component)",
                observed=f"{pension_severance}%",
                expected=f"{MANDATORY_PENSION_SEVERANCE_FULL}% for a full Section 14 waiver (6% is lawful, the waiver is then partial)",
                rule="Severance Pay Law 1963 Section 14 + General Authorization",
            )
        )

    if pension_employee > 7.0:
        findings.append(
            Finding(
                severity="minor",
                field="Employee pension contribution",
                observed=f"{pension_employee}%",
                expected="6% minimum, 7% is the ceiling that still earns the s.45a credit",
                rule="Income Tax Ordinance s.45a: contributions above 7% earn no further credit",
            )
        )

    required_notice = (
        required_notice_days_monthly(tenure_months)
        if worker_type == "monthly"
        else required_notice_days_hourly(tenure_months)
    )
    if notice_days < required_notice:
        findings.append(
            Finding(
                severity="blocker",
                field="Hoda'at Mukdemet",
                observed=f"{notice_days} days",
                expected=f">= {required_notice} days at tenure {tenure_months} months ({worker_type})",
                rule="Prior Notice of Dismissal and Resignation Law 2001",
            )
        )

    required_vacation = (
        5 * (MINOR_VACATION_GROSS_DAYS // 7) + min(MINOR_VACATION_GROSS_DAYS % 7, 5)
        if minor
        else required_vacation_days(tenure_years, extension_order_applies)
    )
    if vacation_days < required_vacation:
        findings.append(
            Finding(
                severity="major",
                field="Annual vacation days",
                observed=f"{vacation_days} days",
                expected=(
                    f">= {required_vacation} days (minor)"
                    if minor
                    else f">= {required_vacation} days in leave year {tenure_years}"
                ),
                rule="Annual Leave Law 1951 + Shortened Work Week extension order (higher of the two)",
            )
        )

    if sick_days_per_year < 18:
        findings.append(
            Finding(
                severity="major",
                field="Sick days per year",
                observed=f"{sick_days_per_year} days",
                expected=">= 18 days per year of accrual (1.5 x 12) for a full-time worker; it pro-rates for part-time and hourly work. This is an accrual figure, NOT a statutory annual cap, and unused days accumulate up to 90.",
                rule="Sick Pay Law 1976 s.4 (1.5 days/month accrual, 90-day balance). Check the payment ladder separately: day 1 unpaid, days 2-3 half, day 4+ full (s.2; the accrual and 90-day cap are s.4).",
            )
        )

    if kh_employer is not None and kh_employer < KH_EMPLOYER_STD:
        findings.append(
            Finding(
                severity="minor",
                field="Keren Hishtalmut employer %",
                observed=f"{kh_employer}%",
                expected=f"~{KH_EMPLOYER_STD}% standard split",
                rule="Industry standard (not mandatory)",
            )
        )

    return findings


def format_findings(findings: list[Finding]) -> str:
    if not findings:
        return "No sanity-check issues found. The numerical fields are within Israeli labor law minimums and industry standards."
    lines = ["=== Contract Sanity Check Findings ===", ""]
    by_severity = {"blocker": [], "major": [], "minor": []}
    for f in findings:
        by_severity[f.severity].append(f)
    for sev in ("blocker", "major", "minor"):
        if not by_severity[sev]:
            continue
        lines.append(f"[{sev.upper()}] ({len(by_severity[sev])})")
        for f in by_severity[sev]:
            lines.append(f"  - {f.field}")
            lines.append(f"      Observed: {f.observed}")
            lines.append(f"      Expected: {f.expected}")
            lines.append(f"      Rule: {f.rule}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanity check numerical fields in an Israeli employment contract")
    parser.add_argument("--pension-employer", type=float, help="Employer pension benefits %%")
    parser.add_argument("--pension-severance", type=float, help="Employer severance contribution %%")
    parser.add_argument("--pension-employee", type=float, help="Employee pension %%")
    parser.add_argument("--notice-days", type=float, help="Hoda'at mukdemet days in contract")
    parser.add_argument("--tenure-months", type=int, help="Expected tenure in months for notice calc")
    parser.add_argument("--worker-type", choices=("monthly", "hourly"), default="monthly")
    parser.add_argument("--vacation", type=int, help="Annual vacation days")
    parser.add_argument("--sick", type=int, help="Annual sick days")
    parser.add_argument("--kh-employer", type=float, help="Keren Hishtalmut employer %%", default=None)
    parser.add_argument(
        "--no-extension-order",
        action="store_true",
        help="The Shortened Work Week extension order does NOT cover this workplace (domestic work, fewer than 4 employees, a government or municipal company, or a 5-day week set by a collective agreement). Scores annual leave on the Annual Leave Law alone.",
    )
    parser.add_argument(
        "--non-pension-fund",
        action="store_true",
        help="The pension product is not a pension fund (typically managers' insurance): employer tagmulim floor is 5%% plus disability cover.",
    )
    parser.add_argument(
        "--full-section-14",
        action="store_true",
        help="The contract intends a FULL Section 14 waiver: flag a severance component below 8.33%%.",
    )
    parser.add_argument(
        "--leave-year",
        type=int,
        default=None,
        help="Calendar leave year of service (the starting calendar year is year 1). Defaults to completed years + 1.",
    )
    parser.add_argument("--minor", action="store_true", help="The employee is under 18: 18 gross leave days (14 net on a 5-day week) regardless of seniority.")
    parser.add_argument("--example", action="store_true", help="Run with a sample contract")
    parser.add_argument("--self-test", action="store_true", help="Run golden-case assertions for the notice schedules")
    args = parser.parse_args()

    if args.self_test:
        # Monthly worker golden cases.
        assert required_notice_days_monthly(3) == 3.0, "monthly m3"
        assert required_notice_days_monthly(6) == 6.0, "monthly m6"
        assert required_notice_days_monthly(9) == 13.5, "monthly m9 = 6 + 2.5*3"
        assert required_notice_days_monthly(11) == 18.5, "monthly m11 = 6 + 2.5*5"
        assert required_notice_days_monthly(12) == 30.0, "monthly one completed year = a month"
        assert required_notice_days_monthly(24) == 30.0, "monthly 2yr flat"
        # Hourly worker golden cases (different schedule).
        assert required_notice_days_hourly(1) == 1.0, "hourly m1"
        assert required_notice_days_hourly(11) == 11.0, "hourly 11 months"
        assert required_notice_days_hourly(12) == 14.0, "hourly one completed year: year 2 starts at 14"
        assert required_notice_days_hourly(13) == 14.0, "hourly 13 months = 14 + (1//2)"
        assert required_notice_days_hourly(18) == 17.0, "hourly 18 months = 14 + (6//2)"
        assert required_notice_days_hourly(23) == 19.0, "hourly 23 months = 14 + (11//2)"
        assert required_notice_days_hourly(24) == 21.0, "hourly two completed years: year 3 starts at 21"
        assert required_notice_days_hourly(35) == 26.0, "hourly 35 months = 21 + (11//2)"
        assert required_notice_days_hourly(36) == 30.0, "hourly three completed years = a month"
        # Annual Leave Law s.3(a) gross ladder and its 5-day-week net conversion.
        assert gross_vacation_days(1) == 16, "gross y1"
        assert gross_vacation_days(5) == 16, "gross y5 (band is years 1-5, not 1-4)"
        assert gross_vacation_days(6) == 18, "gross y6"
        assert gross_vacation_days(7) == 21, "gross y7"
        assert gross_vacation_days(14) == 28, "gross y14 caps at 28"
        assert gross_vacation_days(30) == 28, "gross cap holds"
        # Statute-only net days, matching Kol Zchut's table row for row.
        assert statutory_net_vacation_days(1) == 12, "statute net y1 (16 gross)"
        assert statutory_net_vacation_days(6) == 14, "statute net y6 (18 gross)"
        assert statutory_net_vacation_days(7) == 15, "statute net y7 (21 gross)"
        assert statutory_net_vacation_days(8) == 16, "statute net y8 (22 gross)"
        assert statutory_net_vacation_days(9) == 17, "statute net y9 (23 gross)"
        assert statutory_net_vacation_days(10) == 18, "statute net y10 (24 gross)"
        assert statutory_net_vacation_days(11) == 19, "statute net y11 (25 gross)"
        assert statutory_net_vacation_days(12) == 20, "statute net y12 (26 gross)"
        assert statutory_net_vacation_days(13) == 20, "statute net y13 (27 gross)"
        assert statutory_net_vacation_days(14) == 20, "statute net y14+ (28 gross)"
        # Where the extension order applies it is higher from year 6 on, and it wins.
        assert required_vacation_days(1) == 12, "combined y1"
        assert required_vacation_days(5) == 12, "combined y5"
        assert required_vacation_days(6) == 17, "combined y6, order beats statute"
        assert required_vacation_days(9) == 23, "combined y9, order beats statute"
        assert required_vacation_days(9, extension_order_applies=False) == 17, "statute-only y9"
        assert required_vacation_days(6, extension_order_applies=False) == 14, "statute-only y6"
        # Employee 6 percent is a floor, not a maximum: anything under it must be a blocker.
        low = check(6.5, 6.0, 4.0, 30, 24, "monthly", 12, 18, 7.5)
        assert any(f.severity == "blocker" and "Employee pension" in f.field for f in low), "employee floor"
        # Managers' insurance: 5% tagmulim is lawful, anything below it is not.
        mi = check(5.0, 6.0, 6.0, 30, 24, "monthly", 12, 18, 7.5, non_pension_fund=True)
        assert not any(f.severity == "blocker" for f in mi), "5% on a non-pension-fund product is lawful"
        mi_low = check(4.5, 6.0, 6.0, 30, 24, "monthly", 12, 18, 7.5, non_pension_fund=True)
        assert any(f.severity == "blocker" and "benefits" in f.field for f in mi_low), "below 5% is a blocker"
        # 6% severance is lawful: only a finding when a full Section 14 waiver is intended.
        plain = check(6.5, 6.0, 6.0, 30, 24, "monthly", 12, 18, 7.5)
        assert not any("severance" in f.field for f in plain), "6% severance alone is not a finding"
        s14 = check(6.5, 6.0, 6.0, 30, 24, "monthly", 12, 18, 7.5, full_section_14=True)
        assert any(f.severity == "major" and "severance" in f.field for f in s14), "partial s14 flagged"
        # Leave year: 66 completed months is the 6th year of service, so 17 net days.
        y6 = check(6.5, 6.0, 6.0, 30, 66, "monthly", 12, 18, 7.5)
        assert any("vacation" in f.field for f in y6), "year 6 needs 17 under the order"
        assert not any("vacation" in f.field for f in check(6.5, 6.0, 6.0, 30, 66, "monthly", 17, 18, 7.5)), "17 in year 6 passes"
        # A minor is owed 18 gross days regardless of seniority: 14 net on a 5-day week.
        assert any("vacation" in f.field for f in check(6.5, 6.0, 6.0, 30, 6, "monthly", 12, 18, 7.5, minor=True)), "minor 12 < 14"
        assert not any("vacation" in f.field for f in check(6.5, 6.0, 6.0, 30, 6, "monthly", 14, 18, 7.5, minor=True)), "minor 14 net is enough"
        print("All golden cases passed.")
        return 0

    if args.example:
        print("Example: 2-year contract, pension 6.5%/8.33%/6%, 30 days notice, 12 days vacation, 18 sick, KH 7.5%")
        print("")
        findings = check(
            pension_employer_benefits=6.5,
            pension_severance=8.33,
            pension_employee=6.0,
            notice_days=30,
            tenure_months=24,
            worker_type="monthly",
            vacation_days=12,
            sick_days_per_year=18,
            kh_employer=7.5,
        )
        print(format_findings(findings))
        print()
        print("Now with a broken contract (low notice, low pension):")
        print("")
        findings = check(
            pension_employer_benefits=5.0,
            pension_severance=6.0,
            pension_employee=6.0,
            notice_days=7,
            tenure_months=24,
            worker_type="monthly",
            vacation_days=10,
            sick_days_per_year=12,
            kh_employer=None,
        )
        print(format_findings(findings))
        return 0

    required = [
        "pension_employer",
        "pension_severance",
        "pension_employee",
        "notice_days",
        "tenure_months",
        "vacation",
        "sick",
    ]
    for r in required:
        if getattr(args, r) is None:
            parser.print_help()
            print(f"\nError: --{r.replace('_', '-')} is required (or use --example)", file=sys.stderr)
            return 1

    findings = check(
        pension_employer_benefits=args.pension_employer,
        pension_severance=args.pension_severance,
        pension_employee=args.pension_employee,
        notice_days=args.notice_days,
        tenure_months=args.tenure_months,
        worker_type=args.worker_type,
        vacation_days=args.vacation,
        sick_days_per_year=args.sick,
        kh_employer=args.kh_employer,
        extension_order_applies=not args.no_extension_order,
        non_pension_fund=args.non_pension_fund,
        full_section_14=args.full_section_14,
        leave_year=args.leave_year,
        minor=args.minor,
    )
    print(format_findings(findings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
