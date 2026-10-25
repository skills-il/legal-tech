#!/usr/bin/env python3
"""
Rent Index Adjustment Calculator (Hatzmada La'Madad)

Calculates rent adjustment based on CPI (Consumer Price Index) linking
(hatzmada la'madad, הצמדה למדד) as commonly used in Israeli rental contracts.

Given the original rent amount, the contract start month, and the current month,
this script calculates the adjusted rent based on historical CPI changes.

Usage:
    python scripts/rent-index-calculator.py --rent 5000 --start-date 2024-01 --end-date 2026-03
    python scripts/rent-index-calculator.py --rent 7500 --start-date 2025-08 --end-date 2026-09 --floor

--floor applies a floor clause (rent never falls below the base rent), which
many Israeli leases include. Without it, a fall in the CPI lowers the rent.

Note: CPI values are the official CBS series 120010, chain-linked (see CPI_DATA).
Rounding in the published index means results can differ from the CBS online
calculator by a few agorot. Your lease may fix a different base index (for
example the index "known" on the signing date rather than the index for the
signing month): always follow the contract's own definition.
"""

import argparse
import sys
from datetime import datetime


CPI_DATA = {
    # Chain-linked Consumer Price Index, general index (CBS series 120010).
    # Retrieved from the official CBS price-index API (series 120010) on
    # 2026-08-29, extended to 2026-09 on 2026-10-25. The source URL is recorded
    # in evidence.json (claim cbs-cpi-api); this script makes no network calls.
    # The published series changes base periodically (2020, 2022 and 2024
    # averages all appear in this range), so raw published values are NOT
    # comparable across a base change. These figures are chain-linked to a
    # single continuous scale with 2022-01 = 100, using exact index ratios
    # within each base and the published monthly change at each base change.
    # Only RATIOS between two months are meaningful; the absolute level is
    # an artefact of the 2022-01 = 100 normalisation.
    "2022-01": 100.00, "2022-02": 100.68, "2022-03": 101.26, "2022-04": 102.04,
    "2022-05": 102.63, "2022-06": 103.02, "2022-07": 104.18, "2022-08": 103.89,
    "2022-09": 104.09, "2022-10": 104.67, "2022-11": 104.77, "2022-12": 105.06,
    "2023-01": 105.37, "2023-02": 105.89, "2023-03": 106.30, "2023-04": 107.12,
    "2023-05": 107.33, "2023-06": 107.33, "2023-07": 107.64, "2023-08": 108.15,
    "2023-09": 108.05, "2023-10": 108.57, "2023-11": 108.26, "2023-12": 108.15,
    "2024-01": 108.15, "2024-02": 108.57, "2024-03": 109.18, "2024-04": 110.11,
    "2024-05": 110.32, "2024-06": 110.42, "2024-07": 111.04, "2024-08": 112.07,
    "2024-09": 111.86, "2024-10": 112.38, "2024-11": 111.97, "2024-12": 111.66,
    "2025-01": 112.33, "2025-02": 112.33, "2025-03": 112.88, "2025-04": 114.10,
    "2025-05": 113.77, "2025-06": 114.10, "2025-07": 114.54, "2025-08": 115.31,
    "2025-09": 114.65, "2025-10": 115.20, "2025-11": 114.65, "2025-12": 114.65,
    "2026-01": 114.32, "2026-02": 114.54, "2026-03": 114.98, "2026-04": 116.31,
    "2026-05": 115.98, "2026-06": 115.98, "2026-07": 116.31, "2026-08": 117.08,
    "2026-09": 116.53
}


def parse_date(date_str: str) -> str:
    """Parse and validate a YYYY-MM date string."""
    try:
        dt = datetime.strptime(date_str, "%Y-%m")
        return dt.strftime("%Y-%m")
    except ValueError:
        return ""


def get_cpi(date_key: str) -> float:
    """Return the CPI value for a given month.

    This function does NOT estimate or interpolate. The bundled CPI_DATA
    table covers a fixed range only (see CPI_DATA above). If the requested
    month is outside that range, or otherwise missing from the table, the
    function returns 0.0 and the caller treats that as "data not available"
    rather than guessing a value. To support dates beyond the table, extend
    CPI_DATA with verified figures from the Central Bureau of Statistics.
    """
    return CPI_DATA.get(date_key, 0.0)


def calculate_adjustment(
    original_rent: float, start_date: str, end_date: str, floor: bool = False
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
    floor_applied = floor and adjusted_rent < original_rent
    if floor_applied:
        adjusted_rent = original_rent
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
        "floor_applied": floor_applied,
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
            "  python rent-index-calculator.py --rent 7500 --start-date 2025-08 --end-date 2026-09 --floor\n"
            "\n"
            "Note: CPI data is the official CBS series 120010, chain-linked across base changes."
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
        help=(
            "Base index month, as the lease defines it (YYYY-MM). Many leases use the "
            "index KNOWN at signing, i.e. the last one published (one or two months "
            "before the signing month), not the signing month itself"
        ),
    )
    parser.add_argument(
        "--end-date",
        type=str,
        required=True,
        help=(
            "Index month for the adjustment (YYYY-MM), again as the lease defines it: "
            "often the index known on the payment or adjustment date"
        ),
    )

    parser.add_argument(
        "--floor",
        action="store_true",
        help="Apply a floor clause: the rent never falls below the original rent",
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
    result = calculate_adjustment(args.rent, start, end, floor=args.floor)

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
    print(f"  Base index month (חודש מדד בסיס):  {result['start_date']}")
    print(f"  Adjustment index month (מדד התאמה): {result['end_date']}")
    print(f"\n  Start CPI Index (מדד התחלה):        {result['start_cpi']:.2f}")
    print(f"  End CPI Index (מדד סיום):           {result['end_cpi']:.2f}")
    print(f"  CPI Change (שינוי מדד):             {result['cpi_change_percent']:+.2f}%")

    print(f"\n  {'=' * 50}")
    print(f"  Adjusted Rent (שכירות מותאמת):      {result['adjusted_rent']:,.2f} NIS")

    if result['floor_applied']:
        print(f"  Floor clause applied: the CPI fell, rent stays at the base")
        print(f"  (סעיף רצפה: המדד ירד, השכירות נשארת בסכום הבסיס)")
    if result['rent_difference'] >= 0:
        print(f"  Increase (העלאה):                   +{result['rent_difference']:,.2f} NIS/month")
    else:
        print(f"  Decrease (הפחתה):                   {result['rent_difference']:,.2f} NIS/month")

    print(f"\n  {'=' * 50}")
    print(f"\n  FORMULA (נוסחה):")
    print(f"  Adjusted Rent = Original Rent x (End CPI / Start CPI)")
    indexed = result['original_rent'] * result['end_cpi'] / result['start_cpi']
    print(f"  {indexed:,.2f} = {result['original_rent']:,.2f} x ({result['end_cpi']:.2f} / {result['start_cpi']:.2f})")
    if result['floor_applied']:
        print(f"  Floor clause: {indexed:,.2f} is below the base, so the rent stays {result['original_rent']:,.2f}")

    print(f"\n  DISCLAIMER (הערה חשובה):")
    print(f"  CPI values are the official CBS series, chain-linked; small")
    print(f"  rounding differences from the CBS online calculator are possible.")
    print(f"  Enter the index months your lease names: 'known index' clauses")
    print(f"  mean an index one or two months before that month.")
    print(f"  Your rental contract may specify a different base index or")
    print(f"  adjustment formula. Always refer to your specific contract terms.")
    print()


if __name__ == "__main__":
    main()
