#!/usr/bin/env python3
"""Property-balancing (izun mashabim) worksheet for Israeli divorce.

Computes the equal-value balance under the Spousal Property Relations Law,
5733-1973 (chok yachasei mamon), section 5. Each spouse is entitled to half
the value of ALL the couple's assets, EXCEPT a closed list of exclusions
(assets owned before the marriage, gifts and inheritances received during
the marriage, National Insurance benefits, personal-injury compensation, and
anything agreed in writing not to balance). The script balances VALUE, so one
spouse keeps an asset and pays the other half its value.

The 50/50 default can be varied by the court under section 8 of the law (for
example an unequal division where an equal split would be unjust). This script
does not model that; it computes only the equal balance. Treat the equal split
as a starting point a court can adjust, and confirm the result with a lawyer.

This is a preparation tool, not a court filing or legal advice. Classification
of each item (balanceable vs. excluded, commingling questions) and the final
settlement must be confirmed with a family lawyer.

No third-party dependencies. Python 3.8+.

Usage:
  python3 izun_mashabim.py --example
  python3 izun_mashabim.py --file assets.json
  python3 izun_mashabim.py --asset "Family home:A:1800000:balanceable" \
                           --asset "Inheritance:B:400000:excluded" \
                           --debt "Mortgage:A:900000"

JSON input shape (see --example output for a full sample):
  {
    "spouse_a": "Spouse A",
    "spouse_b": "Spouse B",
    "assets": [
      {"label": "Family home", "owner": "A", "value": 1800000, "balanceable": true}
    ],
    "debts": [
      {"label": "Mortgage", "owner": "A", "value": 900000}
    ]
  }
Owner is "A" or "B". Excluded assets (balanceable=false) stay with the owner
and do not enter the pool. Debts are always netted against the pool.
"""

import argparse
import json
import sys


def normalize_owner(owner):
    """Return 'A' or 'B' for a range of owner spellings, or raise ValueError."""
    key = str(owner).strip().upper()
    if key in ("A", "B"):
        return key
    raise ValueError("owner must be 'A' or 'B', got: %r" % owner)


def build_worksheet(data):
    """Compute the balance. Returns a result dict with per-spouse figures."""
    name_a = data.get("spouse_a", "Spouse A")
    name_b = data.get("spouse_b", "Spouse B")

    # Value of balanceable assets currently held by each spouse.
    held = {"A": 0.0, "B": 0.0}
    # Value of excluded assets (kept out of the pool, shown for transparency).
    excluded = {"A": 0.0, "B": 0.0}
    # Marital debts netted against the pool, tracked per spouse.
    debts = {"A": 0.0, "B": 0.0}

    for asset in data.get("assets", []):
        owner = normalize_owner(asset["owner"])
        value = float(asset["value"])
        if asset.get("balanceable", True):
            held[owner] += value
        else:
            excluded[owner] += value

    for debt in data.get("debts", []):
        owner = normalize_owner(debt["owner"])
        debts[owner] += float(debt["value"])

    # Pool = balanceable assets of both spouses minus marital debts.
    gross_pool = held["A"] + held["B"]
    total_debt = debts["A"] + debts["B"]
    net_pool = gross_pool - total_debt
    half_share = net_pool / 2.0

    # Net position of each spouse: what they hold minus what they owe.
    net_a = held["A"] - debts["A"]
    net_b = held["B"] - debts["B"]

    # The spouse above the half share pays the difference down to equal halves.
    # A positive number means A pays B; a negative number means B pays A.
    payment_a_to_b = net_a - half_share

    return {
        "name_a": name_a,
        "name_b": name_b,
        "held": held,
        "excluded": excluded,
        "debts": debts,
        "gross_pool": gross_pool,
        "total_debt": total_debt,
        "net_pool": net_pool,
        "half_share": half_share,
        "net_a": net_a,
        "net_b": net_b,
        "payment_a_to_b": payment_a_to_b,
    }


def shekels(value):
    """Format a number as rounded shekels with thousands separators."""
    return "{:,} ILS".format(int(round(value)))


def print_worksheet(result):
    name_a = result["name_a"]
    name_b = result["name_b"]
    line = "-" * 56

    print(line)
    print("PROPERTY-BALANCING WORKSHEET (izun mashabim, section 5)")
    print(line)
    print("Balanceable assets held by %s: %s" % (name_a, shekels(result["held"]["A"])))
    print("Balanceable assets held by %s: %s" % (name_b, shekels(result["held"]["B"])))
    print("Excluded (kept by %s):        %s" % (name_a, shekels(result["excluded"]["A"])))
    print("Excluded (kept by %s):        %s" % (name_b, shekels(result["excluded"]["B"])))
    print(line)
    print("Gross balanceable pool:       %s" % shekels(result["gross_pool"]))
    print("Marital debts netted:         %s" % shekels(result["total_debt"]))
    print("Net pool:                     %s" % shekels(result["net_pool"]))
    print("Each spouse's half share:     %s" % shekels(result["half_share"]))
    print(line)
    print("Net position of %s:           %s" % (name_a, shekels(result["net_a"])))
    print("Net position of %s:           %s" % (name_b, shekels(result["net_b"])))
    print(line)

    payment = result["payment_a_to_b"]
    if abs(payment) < 1:
        print("Equalizing payment: none, both spouses are already at the half share.")
    elif payment > 0:
        print("Equalizing payment: %s pays %s %s" % (name_a, name_b, shekels(payment)))
    else:
        print("Equalizing payment: %s pays %s %s" % (name_b, name_a, shekels(-payment)))
    print(line)
    print("Preparation tool only. Confirm classification and the settlement")
    print("with a family lawyer. Pension division goes to israeli-pension-advisor.")


def example_data():
    """A worked case: family home plus savings, one inheritance excluded."""
    return {
        "spouse_a": "Dana",
        "spouse_b": "Yossi",
        "assets": [
            {"label": "Family home", "owner": "A", "value": 1800000, "balanceable": True},
            {"label": "Joint savings", "owner": "B", "value": 300000, "balanceable": True},
            {"label": "Yossi car", "owner": "B", "value": 90000, "balanceable": True},
            {"label": "Dana inheritance", "owner": "A", "value": 400000, "balanceable": False},
        ],
        "debts": [
            {"label": "Mortgage", "owner": "A", "value": 900000},
        ],
    }


def parse_cli_items(asset_args, debt_args):
    """Parse repeated --asset and --debt flags into a data dict."""
    data = {"spouse_a": "Spouse A", "spouse_b": "Spouse B", "assets": [], "debts": []}
    for raw in asset_args or []:
        parts = raw.split(":")
        if len(parts) != 4:
            raise ValueError("--asset must be label:owner:value:balanceable|excluded")
        label, owner, value, flag = parts
        data["assets"].append({
            "label": label,
            "owner": owner,
            "value": float(value),
            "balanceable": flag.strip().lower() != "excluded",
        })
    for raw in debt_args or []:
        parts = raw.split(":")
        if len(parts) != 3:
            raise ValueError("--debt must be label:owner:value")
        label, owner, value = parts
        data["debts"].append({"label": label, "owner": owner, "value": float(value)})
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Israeli property-balancing (izun mashabim) worksheet.")
    parser.add_argument("--example", action="store_true",
                        help="run a built-in worked example")
    parser.add_argument("--file", help="path to a JSON input file")
    parser.add_argument("--asset", action="append",
                        help="label:owner:value:balanceable|excluded (repeatable)")
    parser.add_argument("--debt", action="append",
                        help="label:owner:value (repeatable)")
    args = parser.parse_args(argv)

    if args.example:
        data = example_data()
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    elif args.asset or args.debt:
        data = parse_cli_items(args.asset, args.debt)
    else:
        parser.print_help()
        return 1

    result = build_worksheet(data)
    print_worksheet(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
