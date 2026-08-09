#!/usr/bin/env python3
"""Work out which statutory window a defect falls into under the Israeli
Sale (Apartments) Law, 1973, and who carries the burden of proof.

Pure local logic. No network, no third-party packages, so it also runs on
sandboxed hosts. It answers a timing question only. It never decides whether
something IS a defect, and it never assesses structural safety.

Usage:
  python3 defect_window.py --handover 2021-03-15 --discovered 2026-01-10 --type pipes
  python3 defect_window.py --handover 2009-06-01 --contract 2009-01-20 --discovered 2013-02-02 --type pipes
  python3 defect_window.py --list
  python3 defect_window.py --example
"""

import argparse
import datetime as dt
import sys

# The Schedule split. Contracts concluded on or after this date use the current
# table, provided construction did not finish earlier.
SPLIT = dt.date(2011, 4, 6)

# Current Schedule (contract on/after 06.04.2011). Ten items, verbatim scope.
CURRENT = {
    "frames":    (2, "ליקוי במוצרי מסגרות ונגרות, לרבות אלומיניום ופלסטיק"),
    "flooring":  (2, "ליקוי בריצוף וחיפוי פנים לרבות שקיעות ושחיקה"),
    "machines":  (3, "כשל בתפקוד ובעמידות של מכונות ודוודים"),
    "yard":      (3, "ליקוי בפיתוח חצר, לרבות שקיעות ומערכות מים, ביוב, ניקוז, חשמל, תאורה ותקשורת"),
    "thermal":   (3, "כשל בתפקוד ובעמידות של מרכיבי מערכות הבידוד התרמי"),
    "pipes":     (4, "כשל במערכות צנרת, לרבות מים, מערכת הסקה ומרזבים, דלוחין וביוב (כשל לרבות נזילות)"),
    "sealing":   (4, "כשל באיטום המבנה, לרבות בחללים תת-קרקעיים, בקירות, בתקרות ובגגות"),
    "cracks":    (5, "סדקים ברוחב גדול מ-1.5 מ\"מ ברכיבים לא נושאים"),
    "cladding":  (7, "התנתקות, התקלפות או התפוררות של חיפויי חוץ"),
    "other":     (1, "כל אי-התאמה אחרת שאינה אי-התאמה יסודית"),
}

# Pre-2011 Schedule. Different rows AND different periods.
LEGACY = {
    "pipes":         (2, "צנרת כולל מערכת הסקה ומרזבים"),
    "damp":          (3, "חדירת רטיבות בגג, בקירות ובמקלט"),
    "machines":      (3, "מכונות, מנועים ודוודים"),
    "stairwell":     (3, "קילוף חיפויים בחדרי מדרגות"),
    "floor_ground":  (3, "שקיעת מרצפות בקומת קרקע"),
    "floor_outdoor": (3, "שקיעת מרצפות בחניות, במדרכות, בשבילים בשטח הבניין"),
    "cracks":        (5, "סדקים עוברים בקירות ובתקרות"),
    "cladding":      (7, "קילופים ניכרים בחיפויים חיצוניים"),
    "other":         (1, "כל אי-התאמה אחרת שאינה אי-התאמה יסודית"),
}

WARRANTY_YEARS = 3          # s.4(c): runs from the END of the bedek period
FUNDAMENTAL_BEDEK_YEARS = 20  # s.4(a)(4)


def add_years(d: dt.date, n: int) -> dt.date:
    try:
        return d.replace(year=d.year + n)
    except ValueError:          # 29 Feb
        return d.replace(year=d.year + n, day=28)


def resolve_table(contract: dt.date | None, construction_finished: dt.date | None):
    """Pick the Schedule. Defaults to the current table when the contract date
    is unknown, and says so, because that is the common modern case."""
    if contract is None:
        return CURRENT, "current", (
            "Contract date not supplied, assumed the current Schedule. "
            "If the sale contract predates 06.04.2011, re-run with --contract, "
            "because several periods are SHORTER under the old table."
        )
    if contract < SPLIT:
        return LEGACY, "legacy", (
            f"Sale contract {contract} predates 06.04.2011, so the pre-2011 "
            "Schedule applies, even if the apartment was resold later."
        )
    if construction_finished and construction_finished < SPLIT:
        return LEGACY, "legacy", (
            "Contract is post-split but construction finished before 06.04.2011, "
            "so the pre-2011 Schedule applies."
        )
    return CURRENT, "current", "Current Schedule applies (contract on/after 06.04.2011)."


def analyse(handover, discovered, kind, contract=None, construction_finished=None,
            visible_at_handover=None, notified=None):
    table, which, note = resolve_table(contract, construction_finished)

    if kind not in table:
        alt = "legacy" if which == "current" else "current"
        raise SystemExit(
            f"Defect type '{kind}' is not a row in the {which} Schedule.\n"
            f"Rows available: {', '.join(sorted(table))}\n"
            f"(Note the {alt} Schedule has different rows. Use --list.)"
        )

    years, hebrew = table[kind]
    bedek_end = add_years(handover, years)
    warranty_end = add_years(bedek_end, WARRANTY_YEARS)
    fundamental_end = add_years(handover, FUNDAMENTAL_BEDEK_YEARS)

    out = {
        "schedule": which,
        "schedule_note": note,
        "row": hebrew,
        "handover": handover,
        "discovered": discovered,
        "bedek_years": years,
        "bedek_end": bedek_end,
        "warranty_end": warranty_end,
        "fundamental_bedek_end": fundamental_end,
    }

    if discovered <= bedek_end:
        out["stage"] = "bedek"
        out["burden"] = ("SELLER. During the bedek period the contractor must repair "
                         "unless the contractor proves you caused the defect (s.4(a)(2)).")
    elif discovered <= warranty_end:
        out["stage"] = "warranty"
        out["burden"] = ("BUYER. During the warranty period the contractor must repair only "
                         "if you prove the defect originates in planning, workmanship or "
                         "materials (s.4(a)(3)). This normally needs a licensed engineer.")
    else:
        out["stage"] = "expired"
        out["burden"] = ("Both statutory windows for this defect row have closed. Two routes may "
                         "still be open: a hidden defect you could not reasonably have found "
                         "earlier, and the separate 20-year regime for load-bearing defects. "
                         "Both are lawyer and engineer questions.")

    # The notice duty is a SECOND, independent clock.
    notice_deadline = add_years(handover, 1)
    if visible_at_handover is True:
        out["notice_rule"] = (
            f"Visible at handover, so notice was due by {notice_deadline} "
            "(one year from handover, s.4a(a)(1)).")
        if notified is not None:
            out["notice_status"] = ("MET" if notified <= notice_deadline
                                    else "MISSED, this is a serious problem, take advice")
        else:
            out["notice_status"] = "UNKNOWN, supply --notified"
    elif visible_at_handover is False:
        out["notice_rule"] = ("Hidden at handover, so notice is due within a reasonable time "
                              "after you discovered it, even if more than a year has passed "
                              "since handover (s.4a(a)(2)). Act now and date your notice.")
        out["notice_status"] = "N/A"
    else:
        out["notice_rule"] = ("Not stated whether the defect was visible at handover. This "
                              "selects the notice rule, so it changes the answer. "
                              "Supply --visible yes or --visible no.")
        out["notice_status"] = "UNKNOWN"
    return out


def render(r):
    print()
    print("=" * 68)
    print(f"  Schedule in use : {r['schedule']}")
    print(f"  {r['schedule_note']}")
    print("-" * 68)
    print(f"  Schedule row    : {r['row']}")
    print(f"  Handover        : {r['handover']}")
    print(f"  Discovered      : {r['discovered']}")
    print("-" * 68)
    print(f"  Bedek period    : {r['bedek_years']} years, ends {r['bedek_end']}")
    print(f"  Warranty ends   : {r['warranty_end']}  (bedek end + 3 years)")
    print(f"  STAGE           : {r['stage'].upper()}")
    print(f"  Burden of proof : {r['burden']}")
    print("-" * 68)
    print(f"  Notice duty     : {r['notice_rule']}")
    print(f"  Notice status   : {r['notice_status']}")
    print("-" * 68)
    print("  Load-bearing / stability / safety defects are a SEPARATE regime:")
    print(f"  20-year window runs to {r['fundamental_bedek_end']}, and a claim can survive")
    print("  even beyond it. This script does NOT decide whether a defect is")
    print("  load-bearing. Only a licensed engineer can. If you see cracks in")
    print("  structural elements, sagging, movement, or water near electrics,")
    print("  stop and get a licensed engineer.")
    print("=" * 68)
    print()


def main():
    p = argparse.ArgumentParser(description="Israeli new-apartment defect window calculator")
    p.add_argument("--handover", help="date the apartment was handed over, YYYY-MM-DD")
    p.add_argument("--discovered", help="date the defect was discovered, YYYY-MM-DD")
    p.add_argument("--type", dest="kind", help="Schedule row key, see --list")
    p.add_argument("--contract", help="date the sale contract was concluded, YYYY-MM-DD")
    p.add_argument("--construction-finished", help="date construction finished, YYYY-MM-DD")
    p.add_argument("--visible", choices=["yes", "no"], help="was the defect visible at handover")
    p.add_argument("--notified", help="date you notified the contractor, YYYY-MM-DD")
    p.add_argument("--list", action="store_true", help="list both Schedules and exit")
    p.add_argument("--example", action="store_true", help="run a worked example and exit")
    a = p.parse_args()

    if a.list:
        for title, tbl in (("CURRENT Schedule (contract on/after 06.04.2011)", CURRENT),
                           ("PRE-2011 Schedule (contract before 06.04.2011)", LEGACY)):
            print(f"\n{title}")
            for k, (y, h) in sorted(tbl.items(), key=lambda kv: kv[1][0]):
                print(f"  {k:<14} {y} yr   {h}")
        print("\nWarranty adds 3 years after the bedek period ends, per row.")
        print("Load-bearing defects: separate 20-year regime, engineer territory.\n")
        return

    if a.example:
        print("\nExample: pipe leak found 4 years and 10 months after a 2021 handover.")
        render(analyse(dt.date(2021, 3, 15), dt.date(2026, 1, 10), "pipes",
                       contract=dt.date(2020, 11, 1), visible_at_handover=False))
        print("Same leak, but the apartment was bought in 2009 (old Schedule):")
        render(analyse(dt.date(2009, 6, 1), dt.date(2013, 2, 2), "pipes",
                       contract=dt.date(2009, 1, 20), visible_at_handover=False))
        return

    missing = [f for f in ("handover", "discovered", "kind") if not getattr(a, f)]
    if missing:
        p.error("missing required: " + ", ".join("--" + m.replace("kind", "type") for m in missing))

    d = dt.date.fromisoformat
    render(analyse(
        d(a.handover), d(a.discovered), a.kind,
        contract=d(a.contract) if a.contract else None,
        construction_finished=d(a.construction_finished) if a.construction_finished else None,
        visible_at_handover={"yes": True, "no": False}.get(a.visible),
        notified=d(a.notified) if a.notified else None,
    ))


if __name__ == "__main__":
    sys.exit(main())
