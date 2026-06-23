#!/usr/bin/env python3
"""Compute flight compensation under Israel's Aviation Services Law, 2012 (Tibi Law).

All amounts are the in-force figures as of 2026. They are CPI-updated every
January 1 and rounded to the nearest 10 NIS, so confirm the current-year amount
before relying on the output. This is Israel's own law, NOT EU261. Do not use
EU261 amounts for an Israel-nexus flight.

Usage:
  python compensation_calc.py --distance-km 3000 --delay-hours 9
  python compensation_calc.py --distance-km 1500 --event cancellation --notice-days 5
  python compensation_calc.py --distance-km 6000 --delay-hours 9 \
      --alternative-accepted --alternative-arrival-delay-hours 3
  python compensation_calc.py --example
"""

import argparse
import json
import sys

# 2026 in-force monetary compensation by distance band (NIS).
BANDS = [
    {"max_km": 2000, "amount": 1530, "alt_window_hours": 2},
    {"max_km": 4500, "amount": 2450, "alt_window_hours": 3},
    {"max_km": None, "amount": 3670, "alt_window_hours": 4},  # over 4,500 km
]

INTL_DELAY_CANCELLATION_HOURS = 8
DOMESTIC_DELAY_CANCELLATION_HOURS = 3
CANCELLATION_NOTICE_DAYS = 14
LIMITATION_YEARS = 4

EVENTS = ("cancellation", "delay", "denied_boarding", "early_departure", "downgrade")


def band_for_distance(distance_km):
    for b in BANDS:
        if b["max_km"] is None or distance_km <= b["max_km"]:
            return b
    return BANDS[-1]


def assess(distance_km, event, delay_hours, notice_days, domestic,
           alternative_accepted, alternative_arrival_delay_hours, exemption):
    band = band_for_distance(distance_km)
    base = band["amount"]
    notes = []

    # Decide whether a monetary trigger applies.
    eligible = False
    if event == "delay":
        threshold = DOMESTIC_DELAY_CANCELLATION_HOURS if domestic else INTL_DELAY_CANCELLATION_HOURS
        if delay_hours is not None and delay_hours >= threshold:
            eligible = True
            notes.append(
                f"Delay of {delay_hours}h meets the {threshold}h "
                f"{'domestic' if domestic else 'international'} threshold; treated as a cancellation."
            )
        else:
            notes.append(
                f"Delay under the {threshold}h threshold: assistance only, no monetary compensation."
            )
    elif event == "cancellation":
        if notice_days is not None and notice_days < CANCELLATION_NOTICE_DAYS:
            eligible = True
            notes.append(f"Cancellation with {notice_days} days notice (under 14): monetary compensation applies if no qualifying alternative was offered.")
        else:
            notes.append("Cancellation with 14+ days notice: generally no monetary compensation.")
    elif event == "denied_boarding":
        eligible = True
        notes.append("Involuntary denied boarding (no voluntary give-up of seat): monetary compensation applies.")
    elif event == "early_departure":
        if delay_hours is not None and delay_hours > INTL_DELAY_CANCELLATION_HOURS:
            eligible = True
            notes.append("Early departure of more than 8h with short notice: monetary compensation applies.")
        else:
            notes.append("Early departure of 8h or less: refund/alternative only, no monetary compensation.")
    elif event == "downgrade":
        notes.append("Downgrade: compensation is a percentage of the ticket price per the law's Second Schedule. See references/compensation-table.md for the exact percentages by class transition.")
        return {
            "eligible_for_money": False,
            "amount_nis": None,
            "band_distance_km": distance_km,
            "notes": notes,
            "limitation_years": LIMITATION_YEARS,
        }

    amount = base if eligible else 0

    # 50% reduction for an accepted alternative arriving within the window.
    if eligible and alternative_accepted:
        window = band["alt_window_hours"]
        if alternative_arrival_delay_hours is not None and alternative_arrival_delay_hours <= window:
            amount = round(base / 2)
            notes.append(
                f"Accepted alternative arrived within {window}h of original: airline may pay half ({amount} NIS)."
            )
        else:
            notes.append(
                f"Accepted alternative arrived beyond the {window}h window: full amount stands."
            )

    if eligible and exemption:
        notes.append(
            f"Exemption claimed ({exemption}): monetary compensation may be reduced to 0, "
            "but assistance, refund, and the alternative-flight choice are still owed."
        )
        amount = 0

    return {
        "eligible_for_money": eligible and amount > 0,
        "amount_nis": amount,
        "band_distance_km": distance_km,
        "notes": notes,
        "limitation_years": LIMITATION_YEARS,
    }


def main():
    p = argparse.ArgumentParser(description="Israel Aviation Services Law compensation calculator (2026 figures)")
    p.add_argument("--distance-km", type=float)
    p.add_argument("--event", choices=EVENTS, default="delay")
    p.add_argument("--delay-hours", type=float, default=None,
                   help="Hours of delay at departure (for delay/early_departure events)")
    p.add_argument("--notice-days", type=int, default=None,
                   help="Days of advance notice (for cancellation)")
    p.add_argument("--domestic", action="store_true", help="Domestic Israeli flight (3h threshold)")
    p.add_argument("--alternative-accepted", action="store_true")
    p.add_argument("--alternative-arrival-delay-hours", type=float, default=None)
    p.add_argument("--exemption", default=None,
                   help="Exemption reason if the airline claims one (e.g. extraordinary, iron_swords)")
    p.add_argument("--example", action="store_true")
    args = p.parse_args()

    if args.example:
        demo = assess(3000, "delay", 9, None, False, False, None, None)
        print(json.dumps(demo, ensure_ascii=False, indent=2))
        return 0

    if args.distance_km is None:
        p.error("--distance-km is required (or use --example)")

    result = assess(
        args.distance_km, args.event, args.delay_hours, args.notice_days,
        args.domestic, args.alternative_accepted, args.alternative_arrival_delay_hours,
        args.exemption,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
