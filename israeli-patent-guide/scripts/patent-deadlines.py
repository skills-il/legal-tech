#!/usr/bin/env python3
"""
patent-deadlines.py

Calculates key Israeli patent deadlines from the dates you supply. Python 3
standard library only (no third-party packages).

Covers:
  - Priority claim: no later than 2 months after the Israeli filing (Patents Law s.10(a)(2))
  - Priority document: within 12 months after the Israeli filing (Patents Regulations reg 24)
  - Paris Convention 12-month priority year
  - Publication / opening of the file at 18 months (s.16A(c))
  - Defence-related inventions: earliest foreign filing without Defence Ministry
    permission, 6 months after the Israeli filing if no s.94 order (s.98(2))
  - PCT 30-month national phase entry window (from the earliest priority date)
  - PCT Article 19 amendment deadline (PCT Rule 46.1)
  - Section 18 notice response, 4 months from the demand (reg 36(2))
  - Renewal (maintenance) fee due dates, with optional grant date
  - Opposition period: 3 months from publication of acceptance (s.30)
  - Pharmaceutical PTE filing window: 90 days from registration (s.64O(a))

Use --pct when --filing-date is a PCT international filing date entering the
Israeli national phase; the national-filing-only lines are then suppressed.
Dates already past today are marked [PASSED].

Usage:
    python3 patent-deadlines.py --filing-date 2024-01-15
    python3 patent-deadlines.py --pct --filing-date 2025-03-10 --priority-date 2024-03-18
    python3 patent-deadlines.py --filing-date 2024-01-15 --grant-date 2030-05-01
    python3 patent-deadlines.py --filing-date 2024-01-15 --publication-date 2027-06-01
    python3 patent-deadlines.py --filing-date 2024-01-15 --s18-notice-date 2026-02-01
    python3 patent-deadlines.py --filing-date 2024-01-15 --moh-authorization-date 2028-03-10
    python3 patent-deadlines.py --pct --filing-date 2024-01-15 --isr-date 2024-06-01
    python3 patent-deadlines.py --help

Dates are calendar dates. A deadline that falls on a day ILPO is closed may move;
the tool does not adjust for weekends or holidays.
"""

import argparse
import calendar
import sys
from datetime import date, timedelta
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def parse_date(date_str: str, flag: str) -> date:
    """Parse a date string in YYYY-MM-DD format, exiting with a clear error."""
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        print(f"Error: {flag} '{date_str}' is not a valid date. Use YYYY-MM-DD format.")
        sys.exit(1)


def add_months(d: date, months: int) -> date:
    """Add calendar months. If the target month is shorter, use its last day."""
    month_index = d.month - 1 + months
    year = d.year + month_index // 12
    month = month_index % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


def add_years(d: date, years: int) -> date:
    """Add calendar years (29 February maps to 28 February in a non-leap year)."""
    return add_months(d, 12 * years)


TODAY = date.today()


def format_deadline(label: str, deadline: Optional[date], note: str = "") -> str:
    """Format a single deadline line. A date already past today is marked PASSED."""
    if deadline is None:
        line = f"  {'(see note)':10}  {label}"
    else:
        flag = "  [PASSED]" if deadline < TODAY else ""
        line = f"  {deadline.isoformat()}  {label}{flag}"
    if note:
        line += f"\n                     NOTE: {note}"
    return line


# ---------------------------------------------------------------------------
# Deadline calculation functions
# ---------------------------------------------------------------------------

def pct_national_phase_deadline(priority_date: date) -> date:
    """30 months from the EARLIEST PRIORITY DATE (WIPO PCT Applicant's Guide, IL)."""
    return add_months(priority_date, 30)


def priority_claim_deadline(israeli_filing_date: date) -> date:
    """Priority claim no later than 2 months after the Israeli filing (s.10(a)(2))."""
    return add_months(israeli_filing_date, 2)


def priority_document_deadline(israeli_filing_date: date) -> date:
    """Certified copy within 12 months after the Israeli filing (reg 24(a))."""
    return add_months(israeli_filing_date, 12)


def publication_date(filing_date: date, priority_date: date) -> date:
    """File opened to the public 18 months from the earliest of filing/priority (s.16A(c))."""
    return add_months(min(filing_date, priority_date), 18)


def maintenance_fee_dates(filing_date: date, grant_date: Optional[date]) -> List[Tuple[str, Optional[date], str]]:
    """
    Israeli renewal fee schedule (2026 fee notice, item 12; Regulations reg 85-87).

    - Years 1-6: NIS 961, due WITHIN 3 MONTHS OF GRANT.
    - Years 7-10 (NIS 1,921): before the END of year 6 from filing.
    - Years 11-14 (NIS 2,882): before the end of year 10.
    - Years 15-18 (NIS 4,803): before the end of year 14.
    - Years 19-20 (NIS 6,725): before the end of year 18.
    - All-inclusive NIS 14,410 within 3 months of grant (item 12(6)).
    A renewal may not be paid earlier than 3 months before its due date (reg 87(a)).
    Late payment up to 6 months with a surcharge of the extension fee per month or
    part of a month late (s.57, reg 87(c)); NIS 240 per month in 2026.
    """
    fees = []
    if grant_date:
        fees.append((
            "Renewal years 1-6, NIS 961 (within 3 months of grant)",
            add_months(grant_date, 3),
            "Alternative: NIS 14,410 all-inclusive by the same date covers the whole term.",
        ))
    else:
        fees.append((
            "Renewal years 1-6, NIS 961: due within 3 months of GRANT (pass --grant-date)",
            None,
            "No date until the patent is granted. The fee covers years 1-6 from filing.",
        ))

    blocks = [
        ("Renewal years 7-10, NIS 1,921 (before end of year 6)", 6),
        ("Renewal years 11-14, NIS 2,882 (before end of year 10)", 10),
        ("Renewal years 15-18, NIS 4,803 (before end of year 14)", 14),
        ("Renewal years 19-20, NIS 6,725 (before end of year 18)", 18),
    ]
    for label, year in blocks:
        due = add_years(filing_date, year)
        note = "Late: up to 6 months, surcharge per month or part of a month late."
        if not grant_date and due < TODAY:
            note = ("Date passed. If the patent has been granted, rerun with --grant-date; "
                    "if the application is still pending, nothing is payable before grant.")
        elif grant_date and due < TODAY:
            note = (f"Late-payment window (s.57) ends {add_months(due, 6).isoformat()}"
                    + (" and has also passed; if unpaid, the patent has lapsed and only restoration (s.59) remains."
                       if add_months(due, 6) < TODAY else ", with the surcharge."))
        if grant_date and due < add_months(grant_date, 3):
            note = ("This date falls before grant + 3 months, so it is already due or "
                    "past when the patent is granted. Confirm with ILPO how and when "
                    "renewals already due at grant are paid.")
        fees.append((label, due, note))

    fees.append((
        "Patent expiry (maximum 20-year term)",
        add_years(filing_date, 20),
        "Counted from the filing date, not the priority date.",
    ))
    return fees


def objection_period_deadline(publication_of_acceptance: date) -> date:
    """3 months from PUBLICATION of acceptance under s.26 (s.30)."""
    return add_months(publication_of_acceptance, 3)


def pte_filing_deadline(moh_authorization_date: date) -> date:
    """90 days from registration under the Pharmacists Ordinance (s.64O(a))."""
    return moh_authorization_date + timedelta(days=90)


def article19_amendment_deadline(isr_transmittal_date: date, priority_date: date) -> date:
    """Later of 2 months from ISR transmittal or 16 months from priority (PCT Rule 46.1)."""
    return max(add_months(isr_transmittal_date, 2), add_months(priority_date, 16))


def s18_response_deadline(notice_date: date) -> date:
    """Answer the s.18 demand within 4 months of it (Regulations reg 36(2))."""
    return add_months(notice_date, 4)


# ---------------------------------------------------------------------------
# Formatting and output
# ---------------------------------------------------------------------------

def print_section(title: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_deadlines(args: argparse.Namespace) -> None:
    filing_date = parse_date(args.filing_date, "--filing-date")
    priority_date = (parse_date(args.priority_date, "--priority-date")
                     if args.priority_date else filing_date)
    grant_date = parse_date(args.grant_date, "--grant-date") if args.grant_date else None

    if priority_date > filing_date:
        print("Error: --priority-date is later than --filing-date. The priority date is "
              "the EARLIER first filing.")
        sys.exit(1)
    if grant_date and grant_date < filing_date:
        print("Error: --grant-date is earlier than --filing-date.")
        sys.exit(1)
    if grant_date and grant_date >= add_years(filing_date, 20):
        print("Error: --grant-date is on or after the 20-year expiry from --filing-date.")
        sys.exit(1)
    for flag, value, floor, floor_name in (
        ("--s18-notice-date", args.s18_notice_date, filing_date, "--filing-date"),
        ("--publication-date", args.publication_date, filing_date, "--filing-date"),
        ("--isr-date", args.isr_date, filing_date, "--filing-date"),
    ):
        if value and parse_date(value, flag) < floor:
            print(f"Error: {flag} is earlier than {floor_name}.")
            sys.exit(1)
    if args.isr_date and not args.pct:
        print("Error: --isr-date applies to a PCT application; add --pct.")
        sys.exit(1)
    has_priority = bool(args.priority_date) and priority_date < filing_date

    print("\nIsraeli Patent Deadline Calculator")
    mode = ("PCT application entering the Israeli national phase" if args.pct
            else "Israeli national application (use --pct for a PCT national phase entry)")
    print(f"Mode          : {mode}")
    print(f"Today         : {TODAY.isoformat()}")
    print(f"Filing date   : {filing_date.isoformat()}")
    print(f"Priority date : {priority_date.isoformat()}")
    if grant_date:
        print(f"Grant date    : {grant_date.isoformat()}")

    if has_priority and filing_date > add_months(priority_date, 12):
        print("\n  WARNING: the filing is more than 12 months after the priority date, so the")
        print("           Paris priority claim is out of time. Every date below that uses the")
        print("           priority date is unreliable; ask a patent attorney now.")

    if not args.pct:
        # --- Filing and priority (Israeli national application) ---
        print_section("Filing and Priority (Israeli national application)")
        if has_priority:
            print(format_deadline(
                "Priority claim in Israel (no later than 2 months after Israeli filing)",
                priority_claim_deadline(filing_date),
                "s.10(a)(2). Late: only a Registrar extension before acceptance, for a "
                "good-faith mistake (s.164(a)(2)).",
            ))
            print(format_deadline(
                "Certified priority document (12 months after Israeli filing)",
                priority_document_deadline(filing_date),
                "Reg 24(a). Due earlier, with the request, if accelerated examination is requested first.",
            ))
            print(format_deadline(
                "12-month Paris priority year (from the first filing)",
                add_years(priority_date, 1),
                "Last day to file elsewhere claiming the first filing.",
            ))
        else:
            print(format_deadline(
                "12-month Paris priority year: file abroad or PCT claiming this filing",
                add_years(filing_date, 1),
            ))
        print(format_deadline(
            "Publication: file opened to the public (18 months)",
            publication_date(filing_date, priority_date),
            "s.16A(c). From here the specification is public; trade secrecy ends.",
        ))
        print(format_deadline(
            "Defence-related inventions only: earliest foreign filing without permission"
            + (" (if this is the FIRST filing)" if has_priority else ""),
            add_months(filing_date, 6),
            "s.98(2): 6 months after this Israeli filing, if no s.94 order is in force. "
            "Only for inventions of military value; otherwise ignore.",
        ))
    else:
        # --- PCT national phase ---
        print_section("PCT National Phase Entry into Israel")
        entry = pct_national_phase_deadline(priority_date)
        print(format_deadline(
            "30-month national phase entry (Israel)",
            entry,
            "From the EARLIEST PRIORITY DATE, not the PCT filing date.",
        ))
        if entry < TODAY:
            print(format_deadline(
                "Outer limit for PCT Rule 49.6 reinstatement (12 months after the 30-month date)",
                add_months(entry, 12),
                "Rule 49.6(b): the request and the national-phase acts are due within 2 months "
                "from removal of the cause of the failure or by this date, WHICHEVER IS EARLIER. "
                "Due care test; not guaranteed.",
            ))
        print(format_deadline(
            "Publication in Israel after entry",
            None,
            "s.16A(b): within 45 days of national phase entry.",
        ))
        if args.isr_date:
            isr_date = parse_date(args.isr_date, "--isr-date")
            print(format_deadline(
                "PCT Article 19 claim amendment deadline",
                article19_amendment_deadline(isr_date, priority_date),
                "PCT Rule 46.1: later of 2 months from ISR transmittal or 16 months from priority.",
            ))

    # --- Section 18 ---
    if args.s18_notice_date:
        notice = parse_date(args.s18_notice_date, "--s18-notice-date")
        print_section("Section 18 Notice prior to Examination")
        print(format_deadline(
            "Answer the s.18 demand (4 months)",
            s18_response_deadline(notice),
            "Reg 36(2). Extensions NIS 240 per month or part (2026). Third parties may "
            "file material until 2 months after your answer (s.18(b)(3)).",
        ))

    # --- Maintenance fees ---
    print_section("Renewal Fee Schedule (from filing date)")
    for label, due_date, note in maintenance_fee_dates(filing_date, grant_date):
        print(format_deadline(label, due_date, note))
    print(
        "\n  40% REDUCTION: does NOT apply to renewal fees (only to the filing fee and the"
        "\n                 notice-of-acceptance fee, on a FIRST application)."
        "\n  EARLY PAYMENT: a renewal may not be paid earlier than 3 months before it is due (reg 87(a))."
        "\n  LATE PAYMENT : up to 6 months late (s.57), adding NIS 240 (2026) for each month or"
        "\n                 part of a month late (reg 87(c)). After that the patent lapses."
    )

    # --- Opposition ---
    if args.publication_date:
        pub = parse_date(args.publication_date, "--publication-date")
        print_section("Opposition Period")
        print(format_deadline(
            "3-month opposition window closes",
            objection_period_deadline(pub),
            "s.30: runs from PUBLICATION of acceptance (s.26). Not extendable (s.164(a)).",
        ))

    # --- PTE ---
    if args.moh_authorization_date:
        moh_date = parse_date(args.moh_authorization_date, "--moh-authorization-date")
        print_section("Pharmaceutical PTE Filing Deadline")
        print(format_deadline(
            "90-day PTE filing deadline",
            pte_filing_deadline(moh_date),
            "90 days from registration under the Pharmacists Ordinance (s.64O(a)). "
            "Duration limited by recognized-country extensions and a 14-year cap; see references/pte.md.",
        ))

    print("\n  Calendar dates only; no weekend or holiday roll-forward. Informational only:"
          "\n  docket with a licensed Israeli patent attorney.\n")


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate key Israeli patent deadlines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 patent-deadlines.py --filing-date 2024-01-15
  python3 patent-deadlines.py --pct --filing-date 2025-03-10 --priority-date 2024-03-18
  python3 patent-deadlines.py --filing-date 2024-01-15 --grant-date 2030-05-01
  python3 patent-deadlines.py --filing-date 2024-01-15 --publication-date 2027-06-01
  python3 patent-deadlines.py --filing-date 2024-01-15 --s18-notice-date 2026-02-01
  python3 patent-deadlines.py --filing-date 2024-01-15 --moh-authorization-date 2028-03-10
  python3 patent-deadlines.py --pct --filing-date 2024-01-15 --isr-date 2024-06-01

All dates are YYYY-MM-DD. Informational only; verify every deadline with a
licensed Israeli patent attorney before relying on it.
        """,
    )
    parser.add_argument("--filing-date", required=True, metavar="YYYY-MM-DD",
                        help="Israeli filing date, or with --pct the PCT international filing date.")
    parser.add_argument("--pct", action="store_true",
                        help="The application is a PCT international application entering the Israeli "
                             "national phase (suppresses the national-filing-only lines).")
    parser.add_argument("--priority-date", metavar="YYYY-MM-DD",
                        help="Earliest priority date claimed (the first filing). Defaults to --filing-date.")
    parser.add_argument("--grant-date", metavar="YYYY-MM-DD",
                        help="Date the patent was granted. Enables the first renewal due date.")
    parser.add_argument("--publication-date", "--allowance-date", dest="publication_date",
                        metavar="YYYY-MM-DD",
                        help="Date the ACCEPTANCE was published online under s.26 (not the date the "
                             "notice arrived). Enables the opposition period. --allowance-date is an alias.")
    parser.add_argument("--s18-notice-date", metavar="YYYY-MM-DD",
                        help="Date of the s.18 demand (notice prior to examination).")
    parser.add_argument("--moh-authorization-date", metavar="YYYY-MM-DD",
                        help="Date the medicinal product was registered under the Pharmacists Ordinance.")
    parser.add_argument("--isr-date", metavar="YYYY-MM-DD",
                        help="Date the International Search Report was transmitted.")
    return parser


if __name__ == "__main__":
    print_deadlines(build_parser().parse_args())
