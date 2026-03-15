#!/usr/bin/env python3
"""
Israeli Severance Pay Calculator

Calculate severance pay (pitzuyei piturim) based on salary and tenure,
per the Severance Pay Law 1963 (Chok Pitzuyei Piturim).

Usage:
    python severance-calculator.py --salary 15000 --years 3 --months 4
    python severance-calculator.py --salary 20000 --years 5 --section14 --fund-balance 95000
    python severance-calculator.py --salary-history '12000:2,14000:1,15000:0.33'
"""

import argparse
import sys
from datetime import datetime


def calculate_basic_severance(monthly_salary: float, years: int, months: int) -> float:
    """Calculate severance using the basic formula: last salary x tenure."""
    total_years = years + months / 12.0
    return monthly_salary * total_years


def calculate_salary_history_severance(salary_history: list[tuple[float, float]]) -> float:
    """
    Calculate severance with variable salary history.

    When an employee's salary changed during employment, severance is calculated
    per period at the rate that applied during that period, or at the last salary
    (whichever method yields a higher amount, per case law).

    Args:
        salary_history: List of (salary, years_at_that_salary) tuples,
                       ordered from earliest to most recent.

    Returns:
        Severance amount using the last-salary method (standard approach).
    """
    total_years = sum(years for _, years in salary_history)
    last_salary = salary_history[-1][0]
    return last_salary * total_years


def format_nis(amount: float) -> str:
    """Format amount as NIS with comma separators."""
    return f"NIS {amount:,.2f}"


def main():
    parser = argparse.ArgumentParser(
        description="Israeli Severance Pay Calculator (Chok Pitzuyei Piturim, 1963)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Basic calculation:
    %(prog)s --salary 15000 --years 3 --months 4

  With Section 14 fund balance comparison:
    %(prog)s --salary 20000 --years 5 --section14 --fund-balance 95000

  With salary history (salary:years pairs):
    %(prog)s --salary-history '12000:2,14000:1,15000:0.33'

Notes:
  - Severance applies after 1+ year of continuous employment
  - "Monthly salary" includes all fixed components (base, fixed bonuses)
  - Payment deadline: 15 days from termination date
  - Late payment accrues penalty interest (pitzuyei halanat pitzuyim)
        """,
    )

    parser.add_argument(
        "--salary",
        type=float,
        help="Last monthly salary in NIS (maskoret akhronah)",
    )
    parser.add_argument(
        "--years",
        type=int,
        default=0,
        help="Full years of employment",
    )
    parser.add_argument(
        "--months",
        type=int,
        default=0,
        help="Additional months beyond full years",
    )
    parser.add_argument(
        "--salary-history",
        type=str,
        help="Salary history as 'salary1:years1,salary2:years2,...' (earliest to latest)",
    )
    parser.add_argument(
        "--section14",
        action="store_true",
        help="Include Section 14 analysis (employer pension contributions as severance)",
    )
    parser.add_argument(
        "--fund-balance",
        type=float,
        help="Accumulated pension/provident fund balance for Section 14 comparison",
    )
    parser.add_argument(
        "--monthly-contribution-rate",
        type=float,
        default=8.33,
        help="Monthly severance contribution rate as percentage (default: 8.33%%)",
    )

    args = parser.parse_args()

    if not args.salary and not args.salary_history:
        parser.error("Either --salary or --salary-history is required")

    if args.salary and args.salary <= 0:
        print("Error: Salary must be a positive number.", file=sys.stderr)
        sys.exit(1)

    if args.years < 0 or args.months < 0:
        print("Error: Years and months must be non-negative.", file=sys.stderr)
        sys.exit(1)

    if args.months >= 12:
        print("Error: Months should be 0-11. Use --years for full years.", file=sys.stderr)
        sys.exit(1)

    total_years = args.years + args.months / 12.0

    if total_years < 1.0:
        print("Warning: Severance pay generally requires at least 1 year of employment.")
        print("The calculation below is for reference only.\n")

    print("=" * 60)
    print("  Israeli Severance Pay Calculator")
    print("  Chok Pitzuyei Piturim, 1963")
    print("=" * 60)
    print()

    if args.salary_history:
        try:
            pairs = args.salary_history.split(",")
            salary_history = []
            for pair in pairs:
                salary_str, years_str = pair.strip().split(":")
                salary_history.append((float(salary_str), float(years_str)))
        except ValueError:
            print(
                "Error: Invalid salary history format. Use 'salary1:years1,salary2:years2,...'",
                file=sys.stderr,
            )
            sys.exit(1)

        total_tenure = sum(y for _, y in salary_history)
        last_salary = salary_history[-1][0]
        severance = calculate_salary_history_severance(salary_history)

        print("Salary History:")
        print("-" * 45)
        for i, (salary, period_years) in enumerate(salary_history, 1):
            period_months = int(period_years * 12)
            print(f"  Period {i}: {format_nis(salary)}/month for {period_years:.2f} years ({period_months} months)")
        print("-" * 45)
        print(f"  Total tenure:     {total_tenure:.2f} years")
        print(f"  Last salary:      {format_nis(last_salary)}")
        print()
        print(f"Severance (last salary method):")
        print(f"  {format_nis(last_salary)} x {total_tenure:.2f} = {format_nis(severance)}")

        total_years = total_tenure
        args.salary = last_salary

    else:
        severance = calculate_basic_severance(args.salary, args.years, args.months)

        print(f"  Monthly salary:   {format_nis(args.salary)}")
        print(f"  Employment:       {args.years} years, {args.months} months ({total_years:.2f} years)")
        print()
        print(f"Severance Calculation:")
        print(f"  {format_nis(args.salary)} x {total_years:.2f} = {format_nis(severance)}")

    print()

    if args.section14:
        print("-" * 60)
        print("Section 14 Analysis:")
        print()

        contribution_rate = args.monthly_contribution_rate / 100.0
        estimated_contributions = args.salary * contribution_rate * total_years * 12
        # Simplified: actual contributions vary by salary over time

        print(f"  Employer contribution rate: {args.monthly_contribution_rate}%")
        print(f"  Estimated total contributions: {format_nis(estimated_contributions)}")
        print(f"    (Based on last salary, actual may differ)")

        if args.fund_balance:
            print(f"  Actual fund balance: {format_nis(args.fund_balance)}")
            difference = args.fund_balance - severance

            if difference >= 0:
                print(f"  Fund balance EXCEEDS statutory severance by {format_nis(difference)}")
                print(f"  Employee receives the fund balance: {format_nis(args.fund_balance)}")
            else:
                print(f"  Fund balance is BELOW statutory severance by {format_nis(abs(difference))}")
                print(f"  If Section 14 fully applies: employee receives fund balance ({format_nis(args.fund_balance)})")
                print(f"  If Section 14 partially applies: employer may owe the difference ({format_nis(abs(difference))})")
        else:
            print("  (Use --fund-balance to compare with actual accumulated amount)")

        print()

    print("-" * 60)
    print("Payment Summary:")
    print(f"  Statutory severance:  {format_nis(severance)}")

    if args.section14 and args.fund_balance:
        print(f"  Section 14 balance:   {format_nis(args.fund_balance)}")
        effective = max(severance, args.fund_balance) if args.fund_balance < severance else args.fund_balance
        print(f"  Effective amount:     {format_nis(effective)}")

    print()
    print("Important Reminders:")
    print("  - Payment deadline: 15 days from termination date")
    print("  - Late payment: penalty interest applies (pitzuyei halanat pitzuyim)")
    print("  - Tax: severance up to a ceiling is tax-exempt (ceiling updated annually)")
    print("  - Verify: confirm a proper hearing (shima) was conducted before termination")
    print(f"  - Calculated on: {datetime.now().strftime('%Y-%m-%d')}")
    print()


if __name__ == "__main__":
    main()
