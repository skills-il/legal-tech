#!/usr/bin/env python3
"""
patent-deadlines.py

Calculates key Israeli patent deadlines given a filing date and optional
priority date. Covers:
  - PCT 30-month national phase entry window
  - Israeli maintenance (renewal) fee due dates
  - Post-allowance objection period (3 months from a Notice of Acceptance date)
  - PCT Article 19 amendment deadline (2 months from ISR establishment)
  - Pharmaceutical PTE filing window (90 days from MOH marketing authorization)

Usage:
    python patent-deadlines.py --filing-date 2024-01-15
    python patent-deadlines.py --filing-date 2024-01-15 --priority-date 2023-01-15
    python patent-deadlines.py --filing-date 2024-01-15 --allowance-date 2027-06-01
    python patent-deadlines.py --filing-date 2024-01-15 --moh-authorization-date 2028-03-10
    python patent-deadlines.py --filing-date 2024-01-15 --isr-date 2024-06-01
    python patent-deadlines.py --help
"""

import argparse
import sys
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def parse_date(date_str: str) -> date:
    """Parse a date string in YYYY-MM-DD format."""
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        print(f"Error: '{date_str}' is not a valid date. Use YYYY-MM-DD format.")
        sys.exit(1)


def add_months(d: date, months: int) -> date:
    """Add a number of calendar months to a date using relativedelta."""
    return d + relativedelta(months=months)


def add_years(d: date, years: int) -> date:
    """Add a number of calendar years to a date."""
    return d + relativedelta(years=years)


def format_deadline(label: str, deadline: date, note: str = "") -> str:
    """Format a single deadline line for display."""
    line = f"  {deadline.isoformat()}  {label}"
    if note:
        line += f"\n                     NOTE: {note}"
    return line


# ---------------------------------------------------------------------------
# Deadline calculation functions
# ---------------------------------------------------------------------------

def pct_national_phase_deadline(priority_date: date) -> date:
    """
    PCT national phase entry deadline for Israel.

    The deadline is 30 calendar months from the EARLIEST PRIORITY DATE.
    This is NOT measured from the PCT international filing date.

    Reference: PCT Rule 39; Israeli Patents Law implementing PCT obligations.
    """
    return add_months(priority_date, 30)


def maintenance_fee_dates(filing_date: date) -> list[tuple[str, date, str]]:
    """
    Israeli patent maintenance fee schedule.

    Returns a list of (label, due_date, note) tuples.

    Structure:
    - Years 1-6: Lump sum paid at grant. Represented here as "due at grant,
      covering years 1-6 from filing date." We return the year-6 anniversary
      as the latest point this covers, not a specific payment date (since
      grant date varies).
    - Year 7 block: paid before the year-7 anniversary of filing
    - Year 11 block: paid before the year-11 anniversary of filing
    - Year 15 block: paid before the year-15 anniversary of filing
    - Year 19 block: paid before the year-19 anniversary of filing
    - Year 20: Maximum patent term; patent expires.

    6-month grace period applies to each payment with a surcharge.
    """
    fees = []

    # Years 1-6 lump sum (paid at grant -- we mark year 6 anniversary as reference)
    fees.append((
        "Maintenance: Years 1-6 lump sum (paid at grant)",
        add_years(filing_date, 6),
        "Pay lump sum for years 1-6 when the grant fee is due. "
        "Patent must be granted before year-6 anniversary or separately renewed."
    ))

    # Year 7-10 block: pay before year-7 anniversary
    fees.append((
        "Maintenance: Years 7-10 (pay before year-7 anniversary)",
        add_years(filing_date, 7),
        "6-month grace period with surcharge if paid late."
    ))

    # Year 11-14 block: pay before year-11 anniversary
    fees.append((
        "Maintenance: Years 11-14 (pay before year-11 anniversary)",
        add_years(filing_date, 11),
        "6-month grace period with surcharge if paid late."
    ))

    # Year 15-18 block: pay before year-15 anniversary
    fees.append((
        "Maintenance: Years 15-18 (pay before year-15 anniversary)",
        add_years(filing_date, 15),
        "6-month grace period with surcharge if paid late."
    ))

    # Year 19-20 block: pay before year-19 anniversary
    fees.append((
        "Maintenance: Years 19-20 (pay before year-19 anniversary)",
        add_years(filing_date, 19),
        "6-month grace period with surcharge if paid late."
    ))

    # Patent expiry
    fees.append((
        "Patent expiry (maximum 20-year term)",
        add_years(filing_date, 20),
        "Maximum statutory term from filing date (not priority date)."
    ))

    return fees


def objection_period_deadline(allowance_date: date) -> date:
    """
    3-month objection window after Notice of Acceptance.

    Any person may file a formal opposition during this period.
    The window is non-extendable.
    """
    return add_months(allowance_date, 3)


def pte_filing_deadline(moh_authorization_date: date) -> date:
    """
    PTE (Patent Term Extension) filing deadline for pharmaceutical patents.

    Must be filed within 90 days of the Israeli Ministry of Health
    marketing authorization date. Non-extendable.
    """
    return moh_authorization_date + timedelta(days=90)


def article19_amendment_deadline(isr_date: date) -> date:
    """
    PCT Article 19 amendment deadline.

    Applicants may amend the claims once under Article 19 within
    2 months of the date the International Search Report (ISR) is
    established (or 16 months from the priority date, whichever is later).
    This function returns the 2-month window from the ISR date;
    the caller should separately check the 16-month priority date window.
    """
    return add_months(isr_date, 2)


def paris_convention_priority_deadline(first_filing_date: date) -> date:
    """
    Paris Convention priority deadline.

    To claim priority from a first national filing, a subsequent
    application must be filed within 12 months of the first filing date.
    """
    return add_years(first_filing_date, 1)


# ---------------------------------------------------------------------------
# Formatting and output
# ---------------------------------------------------------------------------

def print_section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_deadlines(args: argparse.Namespace) -> None:
    filing_date = parse_date(args.filing_date)

    # Priority date defaults to filing date if not provided
    priority_date = parse_date(args.priority_date) if args.priority_date else filing_date

    print(f"\nIsraeli Patent Deadline Calculator")
    print(f"Filing date   : {filing_date.isoformat()}")
    print(f"Priority date : {priority_date.isoformat()}")
    if args.allowance_date:
        print(f"Allowance date: {args.allowance_date}")
    if args.moh_authorization_date:
        print(f"MOH auth date : {args.moh_authorization_date}")
    if args.isr_date:
        print(f"ISR date      : {args.isr_date}")

    # --- PCT deadlines ---
    print_section("PCT Deadlines")

    pct_deadline = pct_national_phase_deadline(priority_date)
    print(format_deadline(
        "30-month PCT national phase entry (Israel)",
        pct_deadline,
        "Measured from PRIORITY DATE, not PCT filing date. Absolute -- no extension."
    ))

    paris_deadline = paris_convention_priority_deadline(priority_date)
    print(format_deadline(
        "12-month Paris Convention priority deadline",
        paris_deadline,
        "Deadline to file a PCT or foreign national application claiming priority."
    ))

    if args.isr_date:
        isr_date = parse_date(args.isr_date)
        art19_deadline = article19_amendment_deadline(isr_date)
        print(format_deadline(
            "PCT Article 19 claim amendment deadline",
            art19_deadline,
            "2 months from ISR establishment. Also check 16-month priority window."
        ))

    # --- Maintenance fees ---
    print_section("Maintenance Fee Schedule (from filing date)")

    for label, due_date, note in maintenance_fee_dates(filing_date):
        print(format_deadline(label, due_date, note))

    print(
        "\n  40% REDUCTION: Applies if annual turnover < NIS 10M or individual inventor."
        "\n  GRACE PERIOD : 6 months with surcharge for late payments (not applicable to expiry)."
    )

    # --- Post-allowance objection period ---
    if args.allowance_date:
        allowance_date = parse_date(args.allowance_date)
        print_section("Post-Allowance Objection Period")
        objection_deadline = objection_period_deadline(allowance_date)
        print(format_deadline(
            "3-month objection window closes",
            objection_deadline,
            "Any person may file a formal opposition. Non-extendable."
        ))

    # --- PTE pharmaceutical window ---
    if args.moh_authorization_date:
        moh_date = parse_date(args.moh_authorization_date)
        print_section("Pharmaceutical PTE Filing Deadline")
        pte_deadline = pte_filing_deadline(moh_date)
        print(format_deadline(
            "90-day PTE filing deadline",
            pte_deadline,
            "Non-extendable. EU-5 SPC linkage required -- see SKILL.md for details."
        ))

    print()


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate key Israeli patent deadlines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python patent-deadlines.py --filing-date 2024-01-15
  python patent-deadlines.py --filing-date 2024-01-15 --priority-date 2023-01-15
  python patent-deadlines.py --filing-date 2024-01-15 --allowance-date 2027-06-01
  python patent-deadlines.py --filing-date 2024-01-15 --moh-authorization-date 2028-03-10
  python patent-deadlines.py --filing-date 2024-01-15 --isr-date 2024-06-01

Notes:
  - All dates must be in YYYY-MM-DD format.
  - Requires the 'python-dateutil' package: pip install python-dateutil
  - This tool is for informational purposes only. Verify all deadlines
    with a licensed Israeli patent attorney before relying on them.
        """,
    )

    parser.add_argument(
        "--filing-date",
        required=True,
        metavar="YYYY-MM-DD",
        help="Date the patent application was filed (or PCT international filing date).",
    )
    parser.add_argument(
        "--priority-date",
        metavar="YYYY-MM-DD",
        help=(
            "Earliest priority date claimed (e.g., date of first national filing). "
            "Defaults to --filing-date if omitted. "
            "IMPORTANT: PCT deadlines are calculated from this date, not the PCT filing date."
        ),
    )
    parser.add_argument(
        "--allowance-date",
        metavar="YYYY-MM-DD",
        help="Date of Notice of Acceptance (allowance) from ILPO. Enables objection period calculation.",
    )
    parser.add_argument(
        "--moh-authorization-date",
        metavar="YYYY-MM-DD",
        help=(
            "Date Israeli Ministry of Health granted marketing authorization "
            "for a pharmaceutical product. Enables PTE filing deadline calculation."
        ),
    )
    parser.add_argument(
        "--isr-date",
        metavar="YYYY-MM-DD",
        help="Date the International Search Report (ISR) was established. Enables Article 19 deadline.",
    )

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    print_deadlines(args)
