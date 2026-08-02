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

    Structure (ILPO 2026 fee schedule, item 12):
    - Years 1-6: NIS 961 lump sum, due WITHIN 3 MONTHS OF GRANT. Because the
      grant date varies, we return the year-6 anniversary of filing only as a
      coverage reference, not as the payment date.
    - Years 7-10 block (NIS 1,921): pay before the END OF YEAR 6 from filing
    - Years 11-14 block (NIS 2,882): pay before the END OF YEAR 10 from filing
    - Years 15-18 block (NIS 4,803): pay before the END OF YEAR 14 from filing
    - Years 19-20 block (NIS 6,725): pay before the END OF YEAR 18 from filing
    - Year 20: Maximum patent term; patent expires.

    NOTE: each renewal is due before the end of the year PRECEDING the block it
    covers, not on the block's first anniversary. Paying "before the year-7
    anniversary" is one year too late and the patent lapses.

    Alternative: a single all-inclusive renewal fee of NIS 14,410 may be paid
    within 3 months of grant to keep the patent in force for its entire term
    (item 12(6)), versus NIS 17,292 paid band by band.

    6-month grace period applies to each payment with a surcharge.
    """
    fees = []

    # Years 1-6 lump sum, NIS 961, due within 3 months of grant.
    # Year-6 anniversary shown as a coverage reference only.
    fees.append((
        "Maintenance: Years 1-6 lump sum, NIS 961 (due within 3 months of grant)",
        add_years(filing_date, 6),
        "Date shown is the end of the period covered, NOT the payment date. "
        "The lump sum is due within 3 months of the grant date. "
        "Alternative: NIS 14,410 all-inclusive, also within 3 months of grant, "
        "covers the entire term."
    ))

    # Years 7-10 block: pay before END OF YEAR 6
    fees.append((
        "Maintenance: Years 7-10, NIS 1,921 (pay before end of year 6)",
        add_years(filing_date, 6),
        "6-month grace period with surcharge if paid late."
    ))

    # Years 11-14 block: pay before END OF YEAR 10
    fees.append((
        "Maintenance: Years 11-14, NIS 2,882 (pay before end of year 10)",
        add_years(filing_date, 10),
        "6-month grace period with surcharge if paid late."
    ))

    # Years 15-18 block: pay before END OF YEAR 14
    fees.append((
        "Maintenance: Years 15-18, NIS 4,803 (pay before end of year 14)",
        add_years(filing_date, 14),
        "6-month grace period with surcharge if paid late."
    ))

    # Years 19-20 block: pay before END OF YEAR 18
    fees.append((
        "Maintenance: Years 19-20, NIS 6,725 (pay before end of year 18)",
        add_years(filing_date, 18),
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
    if args.priority_date:
        paris_note = (
            "Paris year measured from the first filing. Already exercised by the "
            "filing analysed here, shown for reference only."
        )
    else:
        paris_note = "Deadline to file a PCT or foreign national application claiming priority."
    print(format_deadline(
        "12-month Paris Convention priority deadline",
        paris_deadline,
        paris_note
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
        "\n  40% REDUCTION: Does NOT apply to renewal fees. It applies only to the"
        "\n                 filing fee and the notice-of-acceptance fee, and only on a"
        "\n                 FIRST application for a particular invention. See SKILL.md."
        "\n  GRACE PERIOD : 6 months with surcharge for late payments (not applicable to expiry)."
        "\n  WARNING      : each renewal is due before the END of the year preceding the"
        "\n                 block it covers (years 6/10/14/18), not on the block's first"
        "\n                 anniversary. Extensions cost NIS 240 per month or part thereof."
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
