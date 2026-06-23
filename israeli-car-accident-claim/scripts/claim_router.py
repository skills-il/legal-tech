#!/usr/bin/env python3
"""Route an Israeli car-accident claim to the right insurance / fund and surface time limits.

This does NOT compute compensation amounts (bodily-injury sums are set by a medical
committee and the courts). It tells the user which regime applies, where to claim, and
which deadlines matter, based on Israel's PLATD Law 1975, the Insurance Contract Law,
the Limitation Law, and the Traffic Regulations.

Usage:
  python3 claim_router.py --injuries --my-fault no
  python3 claim_router.py --damage property --my-fault yes --other-insured yes
  python3 claim_router.py --damage property --hit-and-run --injuries
  python3 claim_router.py --example
"""

import argparse
import json
import sys

LIMITATION_YEARS = 7
MINOR_CLAIM_UNTIL_AGE = 25


def route(injuries, hit_and_run, damage, my_fault, other_insured, my_comprehensive):
    out = {"bodily_injury": None, "property_damage": None, "police": None,
           "time_limits": [], "notes": []}

    # Bodily injury: no-fault (PLATD). Claim from your OWN compulsory insurer regardless of fault.
    if injuries:
        if hit_and_run or other_insured is False:
            out["bodily_injury"] = (
                "Bodily injury is no-fault under PLATD. Normally you claim from your OWN "
                "vehicle's compulsory insurance (ביטוח חובה) regardless of fault. Because the "
                "at-fault vehicle is untraced or uninsured, Karnit (קרנית), the road-accident "
                "victims fund, is the address."
            )
        else:
            out["bodily_injury"] = (
                "Bodily injury is no-fault under PLATD: each injured person (driver, passengers, "
                "pedestrian) claims from the compulsory insurance (ביטוח חובה) of the vehicle they "
                "were in or hit by, regardless of who caused the accident."
            )
        out["notes"].append(
            "A bodily-injury claim with lasting disability usually needs a lawyer and a medical "
            "committee assessment. This skill helps document and understand rights, it does not replace a lawyer."
        )

    # Property damage: fault-based.
    if damage == "property":
        if my_fault == "yes":
            out["property_damage"] = (
                "Property damage is fault-based. As the at-fault driver, the other party claims "
                "against your third-party (צד ג') cover. Your OWN car's damage is covered only by "
                "your comprehensive (מקיף) policy, not by compulsory insurance."
            )
        elif my_fault == "no":
            if my_comprehensive:
                out["property_damage"] = (
                    "Property damage is fault-based and you are not at fault. Fastest path: claim "
                    "from your own comprehensive (מקיף), pay the deductible (השתתפות עצמית); your "
                    "insurer then recovers from the at-fault party by subrogation (שיבוב) and "
                    "refunds your deductible once paid in full. Alternative: claim directly against "
                    "the at-fault driver's third-party cover."
                )
            else:
                out["property_damage"] = (
                    "Property damage is fault-based and you are not at fault, but you have no "
                    "comprehensive policy. Claim directly against the at-fault driver's third-party "
                    "(צד ג') cover, or sue the at-fault driver (small claims for smaller sums)."
                )
        else:
            out["property_damage"] = (
                "Property damage is fault-based: whoever caused the damage (or their insurer) pays. "
                "Determine fault first, then claim from the at-fault party's third-party cover or "
                "your own comprehensive."
            )

    # Police involvement.
    if injuries or hit_and_run:
        out["police"] = (
            "Police involvement is MANDATORY: stop, render aid, and report. A police confirmation "
            "(אישור משטרתי) is a precondition for the insurance claim. The gov.il online light-accident "
            "report only applies when there are no injuries (or injured released within 24 hours)."
        )
    else:
        out["police"] = (
            "Property-only with no injuries: exchange details on the spot. You can file the gov.il "
            "online light-accident report to obtain the police confirmation for the claim."
        )

    out["time_limits"] = [
        "Notify your insurer immediately after the accident (Insurance Contract Law Section 22).",
        f"Statute of limitations: {LIMITATION_YEARS} years for property and bodily-injury claims "
        f"(a minor can sue until about age {MINOR_CLAIM_UNTIL_AGE}).",
    ]
    out["notes"].append(
        "Dispute with the insurer: complain to the Public Inquiries Unit at the Capital Market, "
        "Insurance and Savings Authority (does not bar court), or file in small claims."
    )
    return out


def main():
    p = argparse.ArgumentParser(description="Israeli car-accident claim router")
    p.add_argument("--injuries", action="store_true", help="Anyone injured")
    p.add_argument("--hit-and-run", action="store_true", help="Other driver fled / untraced")
    p.add_argument("--damage", choices=["property", "none"], default="property")
    p.add_argument("--my-fault", choices=["yes", "no", "unknown"], default="unknown")
    p.add_argument("--other-insured", choices=["yes", "no", "unknown"], default="unknown")
    p.add_argument("--my-comprehensive", action="store_true", help="You hold a comprehensive (מקיף) policy")
    p.add_argument("--example", action="store_true")
    args = p.parse_args()

    if args.example:
        demo = route(True, False, "property", "no", True, True)
        print(json.dumps(demo, ensure_ascii=False, indent=2))
        return 0

    other_insured = {"yes": True, "no": False, "unknown": None}[args.other_insured]
    result = route(args.injuries, args.hit_and_run, args.damage, args.my_fault,
                   other_insured, args.my_comprehensive)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
