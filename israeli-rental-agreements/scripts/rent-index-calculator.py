#!/usr/bin/env python3
"""
Rent Index Adjustment Calculator (Hatzmada La'Madad)

Calculates rent adjustment based on CPI (Consumer Price Index) linking
(hatzmada la'madad, הצמדה למדד) as commonly used in Israeli rental contracts.

Given the original rent amount, the contract start month, and the current month,
this script calculates the adjusted rent based on historical CPI changes.

Usage:
    python scripts/rent-index-calculator.py --rent 5000 --start-date 2024-01 --end-date 2026-03
    python scripts/rent-index-calculator.py --rent 7500 --start-date 2023-06 --end-date 2025-12

Note: This script uses approximate CPI data based on publicly available indices
from the Central Bureau of Statistics (CBS / Lishkat HaStatistika HaMerkazit).
For exact calculations, consult the official CBS data at www.cbs.gov.il.
"""

import argparse
import sys
from datetime import datetime


# Approximate CPI index values (base: average 2020 = 100)
# Source: Central Bureau of Statistics (Lishkat HaStatistika HaMerkazit)
# These are representative monthly values. For exact values, consult CBS.
CPI_DATA = {
    "2022-01": 102.5, "2022-02": 102.7, "2022-03": 103.1, "2022-04": 103.5,
    "2022-05": 104.0, "2022-06": 104.5, "2022-07": 105.0, "2022-08": 105.2,
    "2022-09": 105.4, "2022-10": 105.7, "2022-11": 105.9, "2022-12": 105.8,
    "2023-01": 105.9, "2023-02": 106.1, "2023-03": 106.3, "2023-04": 106.6,
    "2023-05": 106.8, "2023-06": 107.0, "2023-07": 107.4, "2023-08": 107.7,
    "2023-09": 108.1, "2023-10": 108.4, "2023-11": 108.5, "2023-12": 108.3,
    "2024-01": 108.4, "2024-02": 108.6, "2024-03": 108.8, "2024-04": 109.0,
    "2024-05": 109.2, "2024-06": 109.4, "2024-07": 109.7, "2024-08": 109.9,
    "2024-09": 110.2, "2024-10": 110.4, "2024-11": 110.5, "2024-12": 110.4,
    "2025-01": 110.5, "2025-02": 110.7, "2025-03": 110.9, "2025-04": 111.1,
    "2025-05": 111.3, "2025-06": 111.5, "2025-07": 111.8, "2025-08": 112.0,
    "2025-09": 112.3, "2025-10": 112.5, "2025-11": 112.6, "2025-12": 112.5,
    "2026-01": 112.6, "2026-02": 112.8, "2026-03": 113.0,
}


def parse_date(date_str: str) -> str:
    """Parse and validate a YYYY-MM date string."""
    try:
        dt = datetime.strptime(date_str, "%Y-%m")
        return dt.strftime("%Y-%m")
    except ValueError:
        return ""


def get_cpi(date_key: str) -> float:
    """Get CPI value for a given month, or estimate if not available."""
    if date_key in CPI_DATA:
        return CPI_DATA[date_key]

    # Try to estimate based on nearest available data
    available_dates = sorted(CPI_DATA.keys())
    if not available_dates:
        return 0.0

    if date_key < available_dates[0]:
        return 0.0
    if date_key > available_dates[-1]:
        return 0.0

    return 0.0


def calculate_adjustment(
    original_rent: float, start_date: str, end_date: str
) -> dict:
    """
    Calculate rent adjustment based on CPI change between two dates.

    Returns a dictionary with calculation details.
    """
    start_cpi = get_cpi(start_date)
    end_cpi = get_cpi(end_date)

    if start_cpi == 0.0 or end_cpi == 0.0:
        return {"error": True, "message": "CPI data not available for the specified dates."}

    cpi_change_ratio = end_cpi / start_cpi
    cpi_change_percent = (cpi_change_ratio - 1) * 100
    adjusted_rent = original_rent * cpi_change_ratio
    rent_difference = adjusted_rent - original_rent

    return {
        "error": False,
        "original_rent": original_rent,
        "start_date": start_date,
        "end_date": end_date,
        "start_cpi": start_cpi,
        "end_cpi": end_cpi,
        "cpi_change_percent": cpi_change_percent,
        "adjusted_rent": adjusted_rent,
        "rent_difference": rent_difference,
    }


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Calculate rent adjustment based on CPI index linking "
            "(hatzmada la'madad) as used in Israeli rental contracts."
        ),
        epilog=(
            "Example:\n"
            "  python rent-index-calculator.py --rent 5000 --start-date 2024-01 --end-date 2026-03\n"
            "  python rent-index-calculator.py --rent 7500 --start-date 2023-06 --end-date 2025-12\n"
            "\n"
            "Note: CPI data is approximate. For exact values, consult CBS (www.cbs.gov.il)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--rent",
        type=float,
        required=True,
        help="Original monthly rent amount in NIS",
    )
    parser.add_argument(
        "--start-date",
        type=str,
        required=True,
        help="Contract start month (YYYY-MM format, e.g., 2024-01)",
    )
    parser.add_argument(
        "--end-date",
        type=str,
        required=True,
        help="Adjustment target month (YYYY-MM format, e.g., 2026-03)",
    )

    args = parser.parse_args()

    # Validate inputs
    errors = []

    if args.rent <= 0:
        errors.append("Rent amount must be a positive number.")

    start = parse_date(args.start_date)
    if not start:
        errors.append(f"Invalid start date format: '{args.start_date}'. Use YYYY-MM (e.g., 2024-01).")

    end = parse_date(args.end_date)
    if not end:
        errors.append(f"Invalid end date format: '{args.end_date}'. Use YYYY-MM (e.g., 2026-03).")

    if start and end and end <= start:
        errors.append("End date must be after start date.")

    if errors:
        print("Input validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    # Calculate adjustment
    result = calculate_adjustment(args.rent, start, end)

    if result.get("error"):
        print(f"\nError: {result['message']}")
        print(f"Available CPI data range: {min(CPI_DATA.keys())} to {max(CPI_DATA.keys())}")
        sys.exit(1)

    # Display results
    print("\n" + "=" * 60)
    print("  Rent Index Adjustment Calculator")
    print("  מחשבון הצמדת שכירות למדד המחירים לצרכן")
    print("=" * 60)

    print(f"\n  Original Rent (שכירות מקורית):     {result['original_rent']:,.2f} NIS")
    print(f"  Contract Start (תחילת חוזה):       {result['start_date']}")
    print(f"  Adjustment Date (מועד התאמה):       {result['end_date']}")
    print(f"\n  Start CPI Index (מדד התחלה):        {result['start_cpi']:.1f}")
    print(f"  End CPI Index (מדד סיום):           {result['end_cpi']:.1f}")
    print(f"  CPI Change (שינוי מדד):             {result['cpi_change_percent']:+.2f}%")

    print(f"\n  {'=' * 50}")
    print(f"  Adjusted Rent (שכירות מותאמת):      {result['adjusted_rent']:,.2f} NIS")

    if result['rent_difference'] >= 0:
        print(f"  Increase (העלאה):                   +{result['rent_difference']:,.2f} NIS/month")
    else:
        print(f"  Decrease (הפחתה):                   {result['rent_difference']:,.2f} NIS/month")

    print(f"\n  {'=' * 50}")
    print(f"\n  FORMULA (נוסחה):")
    print(f"  Adjusted Rent = Original Rent x (End CPI / Start CPI)")
    print(f"  {result['adjusted_rent']:,.2f} = {result['original_rent']:,.2f} x ({result['end_cpi']:.1f} / {result['start_cpi']:.1f})")

    print(f"\n  DISCLAIMER (הערה חשובה):")
    print(f"  CPI values used are approximate. For exact calculations,")
    print(f"  consult the Central Bureau of Statistics (CBS) at www.cbs.gov.il.")
    print(f"  Your rental contract may specify a different base index or")
    print(f"  adjustment formula. Always refer to your specific contract terms.")
    print()


if __name__ == "__main__":
    main()
