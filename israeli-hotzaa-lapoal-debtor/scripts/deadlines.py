#!/usr/bin/env python3
"""Compute the Hotzaa LaPoal debtor clocks from the date the azhara was served.

The azhara clocks run from service (hamtzaa), not from the date printed on the azhara and not
from the day the debtor noticed the file. The day of service itself is not counted, so the
deadline is the service date plus N calendar days. Figures per references/forms-and-clocks.md.

The dates printed are RAW calendar dates. A last day falling on a Friday, Saturday, holiday or
recess day may move to the next working day, but plan on the raw date. Holidays are not
modelled, so check the calendar yourself.

Usage:
  python3 deadlines.py 2026-08-01 --type shtar
  python3 deadlines.py 2026-08-01 --type katzuv
  python3 deadlines.py 2026-08-01 --type psak-din
  python3 deadlines.py 2026-08-01 --type mezonot --arrest-warning 2026-09-01
  python3 deadlines.py 2026-08-01 --type psak-din --restriction-warning 2026-10-01
  python3 deadlines.py 2026-08-01 --type psak-din --payorder-summons 2026-09-10
"""
import argparse
from datetime import date, datetime, timedelta

# label, objection available, payment-order days, ability-exam days (None = no duty)
TYPES = {
    "shtar":    ("Bill or check (shtar / hamchaa)", True,  20,   21),
    "katzuv":   ("Fixed-sum claim (sechum katzuv)", True,  30,   30),
    "psak-din": ("Money judgment (psak din kaspi)", False, 20,   21),
    "mezonot":  ("Maintenance (mezonot)",           False, None, None),
}


def iso_date(text):
    try:
        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{text}' is not a valid date; use YYYY-MM-DD, e.g. 2026-08-01")


def in_summer_recess(d):
    return date(d.year, 7, 21) <= d <= date(d.year, 9, 5)


def flags(d, objection=False, start=None):
    out = []
    if d.weekday() in (4, 5):
        out.append(f"falls on a {d.strftime('%A')}: may move to the next working day, "
                   "but to be safe file by the Thursday before")
    if in_summer_recess(d):
        out.append("falls in the summer recess (21 July to 5 September): may move, but do not rely on it")
    if objection and start is not None:
        overlap = any(in_summer_recess(start + timedelta(days=i)) for i in range(1, 31))
        if overlap and not in_summer_recess(d):
            out.append("the 30 days overlap the summer recess, which may not be counted for an objection; "
                       "do not rely on the extra days")
    return out


def main():
    p = argparse.ArgumentParser(description="Hotzaa LaPoal debtor deadline calculator")
    p.add_argument("served", type=iso_date, help="date the azhara was served, YYYY-MM-DD")
    p.add_argument("--type", required=True, choices=sorted(TYPES), help="file type")
    p.add_argument("--restriction-warning", type=iso_date, metavar="YYYY-MM-DD",
                   help="date a restriction warning was served (or the restriction was imposed in your presence)")
    p.add_argument("--arrest-warning", type=iso_date, metavar="YYYY-MM-DD",
                   help="maintenance files: date an arrest warning was served")
    p.add_argument("--payorder-summons", type=iso_date, metavar="YYYY-MM-DD",
                   help="date a summons to an ability examination was served after a payment-order request was rejected")
    a = p.parse_args()

    served = a.served
    label, can_object, payorder_days, exam_days = TYPES[a.type]

    print(f"File type    : {label}")
    print(f"Azhara served: {served.isoformat()}")
    print()

    rows = []
    if can_object:
        rows.append(("Objection (form 218)", served + timedelta(days=30),
                     "Timely = automatic stay + transfer to court. Late = no stay.", "objection"))
    else:
        rows.append(("Objection", None,
                     "NOT AVAILABLE on this file type. Consider paraati (form 236) or, for a default "
                     "judgment, a set-aside request in the court that gave it.", "info"))
        if a.type == "psak-din":
            rows.append(("Set-aside of a default judgment (only if given without a defence)", served + timedelta(days=30),
                         "30 days from service of the judgment, in the court that gave it. The azhara attaches the "
                         "judgment, so this assumes the 30 days run from the azhara; if the judgment was served "
                         "earlier, the date is earlier. This is a court filing: the enforcement recess does not apply.", "court"))
    if payorder_days:
        rows.append(("Payment order (form 233)", served + timedelta(days=payorder_days),
                     "Statutory default; if the azhara prints a different date, that date governs. Later "
                     "filing is still possible, but interest and advocate fees may be added.", "filing"))
    if exam_days:
        rows.append(("Ability examination", served + timedelta(days=exam_days),
                     "If the azhara prints a different date, that date governs. Missing it means being treated as "
                     "a debtor with means who evades. A pending payment-order request, a timely objection, or a "
                     "paraati claim filed within 21 days exempts you while it is pending.", "filing"))
        rows.append(("Paraati exemption from the ability examination", served + timedelta(days=21),
                     "A paraati claim filed inside these 21 days exempts you from attending while it is pending.", "filing"))
    if a.type == "mezonot":
        rows.append(("Maintenance file", None,
                     "No ordinary payment order (form 233) and no ability-examination duty. Arrest of up to 21 "
                     "days is possible without an ability examination, carried out only 7 days after an arrest "
                     "warning is served (no new warning if one was sent before an earlier arrest in this file).", "info"))
        if a.arrest_warning:
            rows.append(("Last full day before an arrest order can be carried out", a.arrest_warning + timedelta(days=7),
                         "The order can be carried out once these 7 days have passed. Act now and contact legal aid. "
                         "If a warning was already sent before an earlier arrest in this file, no new warning or "
                         "7-day buffer applies.", "authority"))
    elif a.arrest_warning:
        print("Note: --arrest-warning applies to maintenance files only; ignored.\n")
    if a.restriction_warning:
        note = ("The restriction takes effect at the end of this day. Before then: pay, or ask for an ability "
                "examination on form 400 (code 159). If it was imposed in your presence, the route is paying or "
                "asking the registrar for another decision.")
        if a.type == "mezonot":
            note = ("The restriction takes effect at the end of this day unless the debt is paid or the registrar "
                    "decides otherwise. In a maintenance file the debt itself is the ground, so showing you do not "
                    "evade does not answer it.")
        rows.append(("Restriction takes effect", a.restriction_warning + timedelta(days=30), note, "authority"))
    if a.payorder_summons:
        if a.type == "mezonot":
            print("Note: --payorder-summons does not apply to maintenance files (no form 233); ignored.\n")
        else:
            rows.append(("Ability examination after payment order rejected", a.payorder_summons + timedelta(days=14),
                         "14 days from service of the summons.", "filing"))

    today = date.today()
    for name, when, note, kind in rows:
        print(f"  {name}")
        if when:
            label = "date" if kind == "authority" else "deadline"
            print(f"    {label}: {when.isoformat()} ({when.strftime('%A')}, {(when - today).days:+d} days from today)")
            if kind in ("objection", "filing", "court"):
                for f in flags(when, objection=(kind == "objection"), start=served):
                    if kind == "court" and "summer recess" in f:
                        continue
                    print(f"    ! {f}")
        else:
            print("    deadline: n/a")
        print(f"    {note}")
        print()

    print("Paraati (form 236, relief 119) has NO deadline and stays open at any stage.")
    print("Reminder: a payment order does NOT lift existing restrictions or attachments.")
    print("Filing any request in the file counts as full service of the azhara from that day.")
    print("An online filing after 23:59, or on a Friday, Saturday or rest day, counts as filed on the next weekday.")
    print("Holidays are not modelled: check whether a deadline falls on one.")


if __name__ == "__main__":
    main()
