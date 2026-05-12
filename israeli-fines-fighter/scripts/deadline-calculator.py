#!/usr/bin/env python3
"""
Israeli Fine Appeal Deadline Calculator

Calculates remaining days in the appeal window based on fine receipt date.
Supports both parking fines (30-day window) and traffic fines (90-day window).

Usage:
    python deadline-calculator.py --date 2026-03-15 --type parking
    python deadline-calculator.py --date 2026-03-15 --type traffic
    python deadline-calculator.py --help
"""

import argparse
from datetime import datetime, timedelta
import sys

# Bakasha le-bitul (cancellation request) window: 30 days, applies to BOTH
# parking and traffic fines. Bakasha le-hishafet (court-hearing request)
# window: 90 days from receipt, also for both. After day 90 the fine carries
# a +50% surcharge (NOT collection enforcement; that typically kicks in only
# around month 12 via Hotza'a Lapoal). +5% additional every 6 months thereafter.
PARKING_CANCEL_DAYS = 30
TRAFFIC_CANCEL_DAYS = 30
COURT_HEARING_DAYS = 90
SURCHARGE_STARTS_DAYS = 90  # +50% surcharge accrues from this day onward

# NOTE on parking model limitation: parking fines technically share the same
# 30/90-day windows as traffic fines, but municipal practice varies. Some
# municipalities apply their own internal "reconsideration" timelines on top
# of the statutory 30-day cancellation window, and surcharge schedules can
# differ slightly per municipality. Treat this calculator's parking output as
# a baseline; verify with the specific municipality for edge cases.


def calculate_deadline(receipt_date: str, fine_type: str) -> dict:
    """Calculate appeal and surcharge milestones for an Israeli fine."""
    try:
        date = datetime.strptime(receipt_date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{receipt_date}'. Use YYYY-MM-DD.")
        sys.exit(1)

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    cancel_window = PARKING_CANCEL_DAYS if fine_type == "parking" else TRAFFIC_CANCEL_DAYS
    appeal_deadline = date + timedelta(days=cancel_window)
    court_deadline = date + timedelta(days=COURT_HEARING_DAYS)
    surcharge_deadline = date + timedelta(days=SURCHARGE_STARTS_DAYS)

    days_to_appeal = (appeal_deadline - today).days
    days_to_court = (court_deadline - today).days
    days_to_surcharge = (surcharge_deadline - today).days

    return {
        "receipt_date": date.strftime("%Y-%m-%d"),
        "fine_type": fine_type,
        "appeal_deadline": appeal_deadline.strftime("%Y-%m-%d"),
        "days_remaining_appeal": max(days_to_appeal, 0),
        "can_appeal": days_to_appeal > 0,
        # Kept for backwards compatibility with earlier CLI consumers.
        "late_payment_deadline": court_deadline.strftime("%Y-%m-%d"),
        "days_remaining_late": max(days_to_court, 0),
        "court_hearing_deadline": court_deadline.strftime("%Y-%m-%d"),
        "days_remaining_court": max(days_to_court, 0),
        "surcharge_deadline": surcharge_deadline.strftime("%Y-%m-%d"),
        "days_until_surcharge": max(days_to_surcharge, 0),
        "surcharge_started": days_to_surcharge <= 0,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate Israeli fine appeal deadlines"
    )
    parser.add_argument(
        "--date",
        required=True,
        help="Date fine was received (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=["parking", "traffic"],
        help=(
            "Type of fine: parking (municipal) or traffic (police/camera). "
            "Both have a 30-day cancellation window and a 90-day court-hearing window."
        ),
    )

    args = parser.parse_args()
    result = calculate_deadline(args.date, args.type)

    fine_label = "Parking fine" if result["fine_type"] == "parking" else "Traffic fine"

    print(f"\n{'='*50}")
    print(f"  {fine_label} Appeal Deadline Calculator")
    print(f"{'='*50}")
    print(f"  Receipt date:           {result['receipt_date']}")
    print(f"  Cancellation window:    30 days (bakasha le-bitul)")
    print(f"  Cancellation deadline:  {result['appeal_deadline']}")
    print(f"  Court-hearing deadline: {result['court_hearing_deadline']} (bakasha le-hishafet, 90 days)")
    print(f"  +50% surcharge starts:  {result['surcharge_deadline']}")

    if result["can_appeal"]:
        print(f"  Status:                 WITHIN 30-DAY CANCELLATION WINDOW")
        print(f"  Days remaining:         {result['days_remaining_appeal']} days")
    elif not result["surcharge_started"]:
        print(f"  Status:                 CANCELLATION WINDOW EXPIRED, court window still open")
        print(f"  Days to court request:  {result['days_remaining_court']} days")
    else:
        print(f"  Status:                 +50% SURCHARGE HAS STARTED")
        print(f"  Action:                 Pay, or document a justified-delay exception (sec. 230 CPL)")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
