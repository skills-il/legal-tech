#!/usr/bin/env python3
"""
Israeli Small Claims Court Filing Fee Calculator

Calculates the filing fee (agrah, אגרה) for Israeli small claims court
based on the claim amount. The fee is 1% of the claim amount, with a
minimum of NIS 50.

Usage:
    python scripts/filing-fee-calculator.py --amount 15000
    python scripts/filing-fee-calculator.py --amount 3000
    python scripts/filing-fee-calculator.py --amount 38900

Small claims court in Israel handles claims up to NIS 38,900.
For claims exceeding this amount, the case must be filed in
Magistrate Court (Beit Mishpat Shalom).
"""

import argparse
import math
import sys


# Constants
SMALL_CLAIMS_MAX = 38900  # Maximum claim amount in NIS (as of January 2025)
MINIMUM_FEE = 50  # Minimum filing fee in NIS
FEE_PERCENTAGE = 0.01  # 1% of claim amount


def calculate_filing_fee(amount: float) -> dict:
    """
    Calculate the filing fee for a given claim amount.

    Returns a dictionary with fee details.
    """
    if amount <= 0:
        return {"error": True, "message": "Claim amount must be a positive number."}

    exceeds_limit = amount > SMALL_CLAIMS_MAX

    # Calculate fee (still calculate even if exceeds limit, for informational purposes)
    capped_amount = min(amount, SMALL_CLAIMS_MAX)
    calculated_fee = capped_amount * FEE_PERCENTAGE
    actual_fee = max(calculated_fee, MINIMUM_FEE)
    # Round up to nearest shekel
    actual_fee = math.ceil(actual_fee)

    return {
        "error": False,
        "claim_amount": amount,
        "exceeds_limit": exceeds_limit,
        "small_claims_max": SMALL_CLAIMS_MAX,
        "calculated_fee_raw": calculated_fee,
        "actual_fee": actual_fee,
        "minimum_applied": calculated_fee < MINIMUM_FEE,
    }


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Calculate the filing fee for Israeli small claims court "
            "(Beit Mishpat LeTvi'ot Ktanot). Fee is 1% of claim amount, "
            "minimum NIS 50."
        ),
        epilog=(
            "Examples:\n"
            "  python filing-fee-calculator.py --amount 15000\n"
            "  python filing-fee-calculator.py --amount 3000\n"
            "  python filing-fee-calculator.py --amount 38900\n"
            "\n"
            "Small claims court maximum: NIS 38,900 (as of January 2025).\n"
            "For larger claims, file in Magistrate Court (Beit Mishpat Shalom)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--amount",
        type=float,
        required=True,
        help="Claim amount in NIS",
    )

    args = parser.parse_args()

    # Validate
    if args.amount <= 0:
        print("Error: Claim amount must be a positive number.")
        sys.exit(1)

    result = calculate_filing_fee(args.amount)

    if result.get("error"):
        print(f"Error: {result['message']}")
        sys.exit(1)

    # Display results
    print("\n" + "=" * 60)
    print("  Small Claims Court Filing Fee Calculator")
    print("  מחשבון אגרת הגשה לבית משפט לתביעות קטנות")
    print("=" * 60)

    print(f"\n  Claim Amount (סכום תביעה):          {result['claim_amount']:,.2f} NIS")
    print(f"  Small Claims Maximum:                {result['small_claims_max']:,} NIS")

    if result['exceeds_limit']:
        print(f"\n  WARNING (אזהרה):")
        print(f"  Your claim of {result['claim_amount']:,.2f} NIS EXCEEDS the small claims")
        print(f"  court limit of {result['small_claims_max']:,} NIS.")
        print(f"\n  Options:")
        print(f"  1. Reduce claim to {result['small_claims_max']:,} NIS (waive the excess)")
        print(f"  2. File in Magistrate Court (Beit Mishpat Shalom) for full amount")
        print(f"  3. Split into separate claims ONLY if genuinely separate transactions")
        print(f"\n  If you reduce to {result['small_claims_max']:,} NIS:")

    print(f"\n  Fee Calculation:")
    print(f"  {'=' * 50}")

    if result['minimum_applied']:
        print(f"  1% of {min(result['claim_amount'], SMALL_CLAIMS_MAX):,.2f} = {result['calculated_fee_raw']:.2f} NIS")
        print(f"  Minimum fee applies: {MINIMUM_FEE} NIS")
        print(f"\n  Filing Fee (אגרת הגשה):              {result['actual_fee']} NIS")
    else:
        print(f"  1% of {min(result['claim_amount'], SMALL_CLAIMS_MAX):,.2f} = {result['actual_fee']} NIS")
        print(f"\n  Filing Fee (אגרת הגשה):              {result['actual_fee']} NIS")

    # Additional cost summary
    print(f"\n  Cost Summary:")
    print(f"  {'=' * 50}")
    print(f"  Filing fee:                          {result['actual_fee']} NIS")
    print(f"  Registered mail (demand letter):     ~15-30 NIS")
    print(f"  Document copies:                     ~10-30 NIS")
    print(f"  {'=' * 50}")
    total_est = result['actual_fee'] + 30 + 20
    print(f"  Estimated total cost:                ~{total_est} NIS")

    # Helpful information
    print(f"\n  Filing Information:")
    print(f"  {'=' * 50}")
    print(f"  Where to file: gov.il (online), by mail, or in person")
    print(f"  Online filing: gov.il > 'tvi'ot ktanot' (תביעות קטנות)")
    print(f"  Payment methods: credit card (online), bank transfer, or check")
    print(f"  Defendant's counterclaim: same fee calculation applies")

    if not result['exceeds_limit']:
        print(f"\n  Potential recovery if you win:")
        print(f"  {'=' * 50}")
        print(f"  Claim amount:                        {result['claim_amount']:,.2f} NIS")
        print(f"  Filing fee (recoverable):             {result['actual_fee']} NIS")
        print(f"  Interest (from judgment date):        Per court decision")
        print(f"  Court costs (at judge's discretion):  Variable")

    print(f"\n  DISCLAIMER (הערה חשובה):")
    print(f"  Fee amounts are based on regulations as of January 2025.")
    print(f"  Verify current fee with the court or gov.il before filing.")
    print(f"  The small claims maximum (NIS 38,900) is updated periodically.")
    print()


if __name__ == "__main__":
    main()
