#!/usr/bin/env python3
"""Route an Israeli car-accident claim to the right insurance / fund and surface time limits.

This does NOT compute compensation amounts (the non-pecuniary head is a share of a
CPI-linked statutory maximum, and lasting disability is assessed by a court-appointed
medical expert). It tells the user which regime applies, where to claim, and which
deadlines matter, based on Israel's PLATD Law 1975, the Insurance Contract Law, the
Limitation Law, and the Traffic Regulations.

Usage:
  python3 claim_router.py --damage none --injuries --my-fault no
  python3 claim_router.py --damage property --my-fault yes --other-insured yes
  python3 claim_router.py --damage property --hit-and-run --injuries --my-insured no
  python3 claim_router.py --example
"""

import argparse
import json
import sys

# TWO regimes, deliberately separate constants. Merging them into one number is the
# error that time-bars a user's own comprehensive claim at year four.
# Insurance Contract Law Section 31: a claim for insurance benefits against your own
# insurer prescribes three years after the insured event.
INSURANCE_BENEFITS_LIMITATION_YEARS = 3
# Limitation Law Section 5: the tort claim against the at-fault driver and the PLATD
# bodily-injury claim prescribe in seven years.
TORT_AND_PLATD_LIMITATION_YEARS = 7
# Limitation Law Section 10 suspends the clock while the claimant is a minor, so the
# seven-year tort figure is available until roughly this age. Derived, not statutory.
MAJORITY_AGE = 18
MINOR_CLAIM_UNTIL_AGE = MAJORITY_AGE + TORT_AND_PLATD_LIMITATION_YEARS
# PLATD Section 5(b): urgent payment due within 60 days of a written demand.
URGENT_PAYMENT_DAYS = 60
# PLATD Section 5e(b): no urgent payment for a period beyond two years from the accident.
URGENT_PAYMENT_MAX_YEARS = 2


def route(injuries, hit_and_run, damage, my_fault, other_insured, my_comprehensive,
          my_compulsory=True):
    out = {"bodily_injury": None, "property_damage": None, "police": None,
           "time_limits": [], "notes": []}

    # Bodily injury: no-fault (PLATD). Claim from your OWN compulsory insurer regardless
    # of fault. Karnit is available ONLY where the victim has no insurer of their own,
    # which is the express condition in PLATD Section 12(a).
    if injuries:
        untraced_or_uninsured = hit_and_run or other_insured is False
        if untraced_or_uninsured and my_compulsory is False:
            out["bodily_injury"] = (
                "Bodily injury is no-fault under PLATD. You have no compulsory insurer of "
                "your own (pedestrian, cyclist, or an occupant of an uninsured vehicle) and "
                "the responsible vehicle is untraced or uninsured, so Karnit (קרנית) is the "
                "address: Section 12(a) covers a victim who has no insurer to claim from. "
                "Karnit also pays the hospital its treatment costs."
            )
        else:
            out["bodily_injury"] = (
                "Bodily injury is no-fault under PLATD: each injured person claims from the "
                "compulsory insurance (ביטוח חובה) of the vehicle they were in or hit by, "
                "regardless of who caused the accident (allocation rule, Section 3(a)). "
                "Liability is absolute and there is no contributory-negligence reduction "
                "(Section 2(c))."
            )
            if untraced_or_uninsured:
                out["bodily_injury"] += (
                    " The other driver being untraced or uninsured does NOT send you to "
                    "Karnit: you have a compulsory insurer of your own, so Karnit is closed "
                    "to you (Section 12(a) requires that the victim has no insurer to claim "
                    "from). Karnit is for a pedestrian or cyclist hit by an untraced vehicle, "
                    "or an occupant of an uninsured vehicle."
                )
        out["notes"].append(
            "The PLATD claim is exclusive (Section 8): you have no tort claim against the "
            "other driver for bodily injury, except where someone caused the accident "
            "deliberately."
        )
        out["notes"].append(
            "Lasting disability is assessed by a single medical expert appointed by the court "
            "(Section 6a), NOT by a ועדה רפואית. Beware Section 6b: a disability percentage "
            "fixed under any other law (typically a Bituach Leumi work-injury determination) "
            "before the evidence stage binds this claim too. Take legal advice first."
        )
        out["notes"].append(
            "A bodily-injury claim with lasting disability usually needs a lawyer. The fee is "
            "capped by statute (Section 16(a)) at 8% of an agreed sum, or 13% where there were "
            "legal proceedings, and any overpayment is refundable. This skill helps document "
            "and understand rights, it does not replace a lawyer."
        )

    # Property damage: fault-based, and outside PLATD entirely.
    if damage == "property":
        if my_fault == "yes":
            out["property_damage"] = (
                "Property damage is fault-based and sits outside PLATD (Torts Ordinance). As "
                "the at-fault driver, the other party claims against your third-party (צד ג') "
                "cover. Your OWN car's damage is covered only by your comprehensive (מקיף) "
                "policy, not by compulsory insurance."
            )
        elif my_fault == "no":
            if my_comprehensive:
                out["property_damage"] = (
                    "Property damage is fault-based and you are not at fault. Fastest path: claim "
                    "from your own comprehensive (מקיף), pay the deductible (השתתפות עצמית); your "
                    "insurer then recovers from the at-fault party by subrogation (שיבוב) under "
                    "Insurance Contract Law Section 62 and refunds your deductible once paid in "
                    "full. Alternative: claim directly against the at-fault driver's third-party "
                    "cover, or sue them."
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
            "(אישור משטרתי) is a precondition for the compensation claim. The gov.il online "
            "light-accident report only applies when there are no injuries (or injured released "
            "within 24 hours). If anyone was hurt, ATTACH the medical documents: the police page "
            "warns that a report filed without them is classified as a damage-only event and not "
            "as a road accident, which can matter against insurers and in civil claims."
        )
    else:
        out["police"] = (
            "Property-only with no injuries: exchange details on the spot. If the vehicle you hit "
            "was parked or its owner absent, leave a written note AND report to the police within "
            "24 hours. You can file the gov.il online light-accident report to obtain the police "
            "confirmation for the claim."
        )

    out["time_limits"] = [
        "Notify your insurer immediately after the accident (Insurance Contract Law Section 22).",
        f"Claim for insurance benefits against YOUR OWN insurer (including a comprehensive "
        f"property claim): {INSURANCE_BENEFITS_LIMITATION_YEARS} years from the accident "
        f"(Insurance Contract Law Section 31). It runs from the insured event, NOT from the "
        f"insurer's rejection, and handing the claim in does not stop the clock.",
        f"Tort claim against the at-fault driver, and the PLATD bodily-injury claim: "
        f"{TORT_AND_PLATD_LIMITATION_YEARS} years (Limitation Law Section 5). A minor's clock is "
        f"suspended below {MAJORITY_AGE}, so on that figure a minor can sue until about age "
        f"{MINOR_CLAIM_UNTIL_AGE}.",
        "Liability insurance (a third-party route) does not prescribe while the third party's "
        "claim against the insured is still alive (Insurance Contract Law Section 70), so it "
        "tracks the longer period.",
        "Your insurer must warn you in writing 12 months and again 3 months before the period "
        "ends (Insurance Contract Law Section 31a). Do not rely on that warning arriving.",
    ]
    if injuries:
        out["time_limits"].insert(1, (
            f"URGENT PAYMENT (תשלום תכוף, PLATD Section 5): the liable party and their insurer "
            f"must pay medical and hospitalization expenses plus monthly living and nursing costs "
            f"within {URGENT_PAYMENT_DAYS} days of a written demand with an affidavit. If the "
            f"{URGENT_PAYMENT_DAYS} days pass, apply to the Magistrates' Court, separately from "
            f"the main claim if you wish (Section 5a). Late payment carries linkage plus 12% "
            f"annual interest (Section 5d). No urgent payment is awarded for a period beyond "
            f"{URGENT_PAYMENT_MAX_YEARS} years from the accident (Section 5e), and a repeat "
            f"application needs 6 months plus changed circumstances. This is the only deadline "
            f"that runs AGAINST the insurer, so raise it early."
        ))
        out["time_limits"].append(
            "If it is also a work accident, claim from Bituach Leumi as well: it does not "
            "subrogate against the motor insurer, the benefit is simply deducted from the award "
            "(National Insurance Law Section 328a(b))."
        )
    out["notes"].append(
        "Dispute with the insurer: complain to the Public Inquiries Unit at the Capital Market, "
        "Insurance and Savings Authority (does not bar court), or file in small claims."
    )
    out["notes"].append(
        "Electric bikes and scooters are not motor vehicles under PLATD per the case law, so an "
        "injured rider has no no-fault claim: the routes are ordinary negligence or דמי תאונה "
        "לנפגעי תאונות אישיות from Bituach Leumi."
    )
    return out


def main():
    p = argparse.ArgumentParser(description="Israeli car-accident claim router")
    p.add_argument("--injuries", action="store_true", help="Anyone injured")
    p.add_argument("--hit-and-run", action="store_true", help="Other driver fled / untraced")
    p.add_argument("--damage", choices=["property", "none", "unknown"], default="unknown",
                   help="Was there property damage. Default 'unknown' so an injury-only "
                        "accident does not silently get a property-damage plan.")
    p.add_argument("--my-fault", choices=["yes", "no", "unknown"], default="unknown")
    p.add_argument("--other-insured", choices=["yes", "no", "unknown"], default="unknown")
    p.add_argument("--my-insured", choices=["yes", "no"], default="yes",
                   help="Do YOU have compulsory insurance of your own for this ride "
                        "(no for a pedestrian, a cyclist, or an occupant of an uninsured "
                        "vehicle). This is what gates Karnit under PLATD Section 12(a).")
    p.add_argument("--my-comprehensive", action="store_true", help="You hold a comprehensive (מקיף) policy")
    p.add_argument("--example", action="store_true")
    args = p.parse_args()

    if args.example:
        demo = route(True, False, "property", "no", True, True, True)
        print(json.dumps(demo, ensure_ascii=False, indent=2))
        return 0

    other_insured = {"yes": True, "no": False, "unknown": None}[args.other_insured]
    my_compulsory = args.my_insured == "yes"
    result = route(args.injuries, args.hit_and_run, args.damage, args.my_fault,
                   other_insured, args.my_comprehensive, my_compulsory)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
