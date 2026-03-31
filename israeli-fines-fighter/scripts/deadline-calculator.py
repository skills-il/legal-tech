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

PARKING_APPEAL_DAYS = 30
TRAFFIC_APPEAL_DAYS = 90
LATE_PAYMENT_DAYS = 90  # After this, collection proceedings begin


def calculate_deadline(receipt_date: str, fine_type: str) -> dict:
    """Calculate appeal and payment deadlines for an Israeli fine."""
    try:
        date = datetime.strptime(receipt_date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{receipt_date}'. Use YYYY-MM-DD.")
        sys.exit(1)

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    if fine_type == "parking":
        appeal_deadline = date + timedelta(days=PARKING_APPEAL_DAYS)
        late_payment_deadline = date + timedelta(days=LATE_PAYMENT_DAYS)
    else:
        appeal_deadline = date + timedelta(days=TRAFFIC_APPEAL_DAYS)
        late_payment_deadline = date + timedelta(days=TRAFFIC_APPEAL_DAYS)

    days_to_appeal = (appeal_deadline - today).days
    days_to_late = (late_payment_deadline - today).days

    return {
        "receipt_date": date.strftime("%Y-%m-%d"),
        "fine_type": fine_type,
        "appeal_deadline": appeal_deadline.strftime("%Y-%m-%d"),
        "days_remaining_appeal": max(days_to_appeal, 0),
        "can_appeal": days_to_appeal > 0,
        "late_payment_deadline": late_payment_deadline.strftime("%Y-%m-%d"),
        "days_remaining_late": max(days_to_late, 0),
        "in_collection": days_to_late <= 0,
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
        help="Type of fine: parking (30-day appeal) or traffic (90-day appeal)",
    )

    args = parser.parse_args()
    result = calculate_deadline(args.date, args.type)

    fine_label = "Parking fine" if result["fine_type"] == "parking" else "Traffic fine"
    window = PARKING_APPEAL_DAYS if result["fine_type"] == "parking" else TRAFFIC_APPEAL_DAYS

    print(f"\n{'='*50}")
    print(f"  {fine_label} Appeal Deadline Calculator")
    print(f"{'='*50}")
    print(f"  Receipt date:      {result['receipt_date']}")
    print(f"  Appeal window:     {window} days")
    print(f"  Appeal deadline:   {result['appeal_deadline']}")

    if result["can_appeal"]:
        print(f"  Days remaining:    {result['days_remaining_appeal']} days")
        print(f"  Status:            WITHIN APPEAL WINDOW")
    elif not result["in_collection"]:
        print(f"  Status:            APPEAL WINDOW EXPIRED")
        print(f"  Late payment by:   {result['late_payment_deadline']}")
        print(f"  Days to pay:       {result['days_remaining_late']} days")
    else:
        print(f"  Status:            IN COLLECTION PROCEEDINGS")
        print(f"  Action:            Pay immediately or contact enforcement office")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
