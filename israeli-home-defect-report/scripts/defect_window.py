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
# table, provided construction of the BUILDING did not finish earlier (s.11(c)).
SPLIT = dt.date(2011, 4, 6)

# Current Schedule (contract on/after 06.04.2011). Ten items, scope text follows
# the statutory row wording, abridged only where marked.
CURRENT = {
    "frames":    (2, "ליקוי במוצרי מסגרות ונגרות, לרבות אלומיניום ופלסטיק"),
    "flooring":  (2, "ליקוי בריצוף וחיפוי פנים לרבות שקיעות ושחיקה"),
    "machines":  (3, "כשל בתפקוד ובעמידות של מכונות ודוודים"),
    "yard":      (3, "ליקוי בפיתוח חצר, לרבות שקיעות, בין השאר של מרצפות בקומת קרקע, בחניות, במדרכות ובשבילים בשטח הבניין, וכן ליקויים במשטחים מחומרי גימור שונים; \"פיתוח חצר\" לרבות מערכות מים, ביוב, ניקוז, חשמל, תאורה ותקשורת"),
    "thermal":   (3, "כשל בתפקוד ובעמידות של מרכיבי מערכות הבידוד התרמי"),
    "pipes":     (4, "כשל במערכות צנרת, לרבות מים, מערכת הסקה ומרזבים, דלוחין וביוב (כשל לרבות נזילות)"),
    "sealing":   (4, "כשל באיטום המבנה, לרבות בחללים תת-קרקעיים, בקירות, בתקרות ובגגות, לרבות גגות קלים עם סיכוך"),
    "cracks":    (5, "סדקים ברוחב גדול מ-1.5 מ\"מ ברכיבים לא נושאים"),
    "cladding":  (7, "התנתקות, התקלפות או התפוררות של חיפויי חוץ"),
    "other":     (1, "כל אי-התאמה אחרת שאינה אי-התאמה יסודית"),
}

# Pre-2011 Schedule, as enacted by Amendment 3 (1990). Different rows AND
# different periods.
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

# Sunken floor tiles on the ground floor, in parking, on pavements and on paths
# are EXPRESSLY inside current-Schedule item (4) פיתוח חצר (3 yr), not item (2)
# ריצוף וחיפוי פנים (2 yr). The pre-2011 table gave them their own rows, so those
# keys are accepted under the current Schedule and redirected to `yard`.
CURRENT_ALIASES = {"floor_ground": "yard", "floor_outdoor": "yard", "damp": "sealing"}

# Damp is the classic multi-row defect: its CAUSE decides the row, and cause is
# an engineer's call. So never pick one silently. The old 'damp' row covers the
# roof, walls and shelter only; damp from a leaking pipe is the pipes row.
DAMP_CANDIDATES = {"current": ("sealing", "pipes", "thermal"),
                   "legacy": ("damp", "pipes", "other")}

# Current-Schedule row names typed for a pre-2011 contract. The old table has
# fewer rows, so redirect with a note instead of hard-erroring.
LEGACY_ALIASES = {
    "sealing": ("damp", "The old table's nearest row is damp penetration in the roof, walls and shelter "
                        "(3 years). Sealing elsewhere, for example a wet-room floor, falls under 'other'."),
    "flooring": ("other", "The old table has no interior-flooring row, so 'other' applies. If this is "
                          "SUBSIDENCE on the ground floor or outdoors, use floor_ground or floor_outdoor (3 years)."),
    "frames": ("other", "The old table has no frames/carpentry row, so 'other' applies."),
    "thermal": ("other", "The old table has no thermal-insulation row, so 'other' applies."),
    "yard": ("other", "The old table has no general yard row. If this is sunken paving, use floor_ground "
                      "or floor_outdoor (3 years); otherwise 'other' applies."),
}

WARRANTY_YEARS = 3            # s.4(c): runs from the END of the bedek period
FUNDAMENTAL_BEDEK_YEARS = 20  # s.4(a)(4), CURRENT law only (added by Amendment 5, 2011)
NOTICE_GAP_FLAG_DAYS = 90     # a discovery-to-notice gap worth flagging, not a legal threshold


def add_years(d: dt.date, n: int) -> dt.date:
    """Add n years. A 29 Feb anniversary falls on 1 March in a non-leap year:
    rounding DOWN to 28 Feb would shorten every period and every notice deadline
    by a day, always against the buyer."""
    try:
        return d.replace(year=d.year + n)
    except ValueError:          # 29 Feb into a non-leap year
        return dt.date(d.year + n, 3, 1)


def resolve_table(contract: dt.date | None, construction_finished: dt.date | None,
                  handover: dt.date | None = None):
    """Pick the Schedule. A handover before the split settles it whatever contract
    date is given: an apartment handed over before 06.04.2011 is in a building
    whose construction had finished by then (the building limb of s.11(c)), and
    in practice the original sale contract was earlier still. A later contract
    date is usually a resale, which does not change the schedule. Otherwise
    defaults to the current table when the contract date is unknown, and says so."""
    if handover is not None and handover < SPLIT:
        extra = ""
        if contract is not None and contract >= SPLIT:
            extra = (f" The contract date given ({contract}) is after the split and after "
                     "handover, which usually means a resale: the schedule follows the original "
                     "sale and the building, not the resale. Check the dates.")
        return LEGACY, "legacy", (
            f"Handover {handover} predates 06.04.2011, so the building was finished before the "
            "split and the pre-2011 Schedule AND the pre-2011 text of the law apply (s.11(c))."
            + extra)
    if contract is not None and handover is not None and contract > handover:
        tbl, which, note = resolve_table(None, construction_finished, handover)
        return tbl, which, (
            f"WARNING: contract date {contract} is AFTER handover {handover}, so it is almost "
            "certainly a resale contract. The schedule follows the ORIGINAL contract with the "
            "contractor: re-run with that date. Meanwhile, treating the original contract date as "
            "unknown: " + note.replace("Contract date not supplied, assumed", "Assumed"))
    if construction_finished is not None and construction_finished < SPLIT:
        return LEGACY, "legacy", (
            "Construction of the building finished before 06.04.2011, so the pre-2011 Schedule "
            "and the pre-2011 text of the law apply (s.11(c)), whatever the contract date.")
    if contract is None:
        if handover is not None and handover < add_years(SPLIT, 3):
            return CURRENT, "current", (
                "Contract date not supplied, assumed the current Schedule. But handover was within "
                "three years of 06.04.2011, so a pre-2011 contract or a building completed before "
                "then is LIKELY. Ask for both and re-run with --contract and --construction-finished, "
                "because several periods are SHORTER under the old table and the old text applies.")
        return CURRENT, "current", (
            "Contract date not supplied, assumed the current Schedule. "
            "If the sale contract predates 06.04.2011, re-run with --contract, "
            "because several periods are SHORTER under the old table and the old "
            "text of the law applies.")
    if contract < SPLIT:
        return LEGACY, "legacy", (
            f"Sale contract {contract} predates 06.04.2011, so the pre-2011 "
            "Schedule AND the pre-2011 text of the law apply (s.11(c)).")
    if construction_finished is None:
        return CURRENT, "current", (
            "Current Schedule applies (contract on/after 06.04.2011), ASSUMING this is the ORIGINAL "
            "contract with the contractor (a sub-buyer's resale contract does not count; use the "
            "first buyer's contract date) AND that construction of the "
            "building finished on or after that date. If the building was completed earlier, the "
            "pre-2011 Schedule and text apply (s.11(c)); re-run with --construction-finished.")
    return CURRENT, "current", (
        "Current Schedule applies (contract on/after 06.04.2011), assuming this is the ORIGINAL "
        "contract with the contractor, not a sub-buyer's resale contract.")


def stage_of(handover, discovered, years):
    bedek_end = add_years(handover, years)
    warranty_end = add_years(bedek_end, WARRANTY_YEARS)
    if discovered <= bedek_end:
        stage = "bedek"
    elif discovered <= warranty_end:
        stage = "warranty"
    else:
        stage = "expired"
    return bedek_end, warranty_end, stage


def analyse(handover, discovered, kind, contract=None, construction_finished=None,
            visible_at_handover=None, notified=None):
    table, which, note = resolve_table(contract, construction_finished, handover)

    if discovered < handover:
        raise SystemExit(
            f"Discovered date {discovered} is BEFORE the handover date {handover}. "
            "Every period runs from handover, so one of the two dates is wrong. "
            "Check them and re-run.")

    alias_note = None
    damp_range = None
    if kind == "damp" or (which == "legacy" and kind == "sealing"):
        damp_range = []
        for k in DAMP_CANDIDATES[which]:
            y, h = table[k]
            be, we, st = stage_of(handover, discovered, y)
            damp_range.append((k, y, be, we, st))
        names = ", ".join(f"{k} ({y} yr)" for k, y, *_ in damp_range)
        alias_note = (f"Damp is not one row. Its CAUSE decides the row: {names}. Cause is an "
                      "engineer's call, so every candidate is shown; report the range, never one row.")
        if which == "legacy":
            alias_note += (" The old damp row covers the roof, walls and shelter only; sealing "
                           "elsewhere, for example a wet-room floor, falls under 'other' (1 yr).")
        kind = "damp_multi"
    elif which == "current" and kind not in table and kind in CURRENT_ALIASES:
        alias_note = (f"'{kind}' is a pre-2011 row name. Under the current Schedule this "
                      f"falls in item '{CURRENT_ALIASES[kind]}'. Using that row.")
        kind = CURRENT_ALIASES[kind]
    elif which == "legacy" and kind not in table and kind in LEGACY_ALIASES:
        target, why = LEGACY_ALIASES[kind]
        alias_note = f"'{kind}' is a current-Schedule row name. {why} Using '{target}'."
        kind = target

    if kind != "damp_multi" and kind not in table:
        alt = "legacy" if which == "current" else "current"
        raise SystemExit(
            f"Defect type '{kind}' is not a row in the {which} Schedule.\n"
            f"Rows available: {', '.join(sorted(table))}\n"
            f"(Note the {alt} Schedule has different rows. Use --list.)"
        )

    if kind == "damp_multi":
        ys = [y for _, y, *_ in damp_range]
        bes = [be for _, _, be, _, _ in damp_range]
        wes = [we for _, _, _, we, _ in damp_range]
        years = f"{min(ys)}-{max(ys)}" if min(ys) != max(ys) else str(ys[0])
        hebrew = "depends on cause, see the range below"
        bedek_end = f"{min(bes)} to {max(bes)}" if min(bes) != max(bes) else str(bes[0])
        warranty_end = f"{min(wes)} to {max(wes)}" if min(wes) != max(wes) else str(wes[0])
        stages = {st for *_, st in damp_range}
        stage = stages.pop() if len(stages) == 1 else "depends on cause"
    else:
        years, hebrew = table[kind]
        bedek_end, warranty_end, stage = stage_of(handover, discovered, years)

    out = {
        "schedule": which,
        "schedule_note": note,
        "row": hebrew,
        "handover": handover,
        "discovered": discovered,
        "bedek_years": years,
        "bedek_end": bedek_end,
        "warranty_end": warranty_end,
        "fundamental_bedek_end": add_years(handover, FUNDAMENTAL_BEDEK_YEARS),
        "alias_note": alias_note,
        "damp_range": damp_range,
        "stage": stage,
        "warnings": [],
    }

    if stage == "bedek":
        out["burden"] = ("SELLER. During the bedek period the contractor must repair "
                         "unless the contractor proves you caused the defect (s.4(a)(2)).")
    elif stage == "warranty":
        out["burden"] = ("BUYER. During the warranty period the contractor must repair only "
                         "if you prove the defect originates in planning, workmanship or "
                         "materials (s.4(a)(3)). This normally needs a licensed engineer.")
    elif stage == "depends on cause":
        out["burden"] = ("DEPENDS ON CAUSE. The candidate rows put this defect in different stages "
                         "(see the range), so who must prove what depends on what is causing the "
                         "damp. Say so; do not report the most favourable row as the answer.")
    else:
        fundamental = ("the separate 20-year regime for load-bearing defects" if which == "current"
                       else "the pre-2011 law's route for a fundamental non-conformity that makes "
                            "the apartment unfit for its purpose, which has no fixed end date")
        out["burden"] = ("Both statutory windows for this defect row have closed. What may still be "
                         f"open: {fundamental}; a deviation from the specification, an official "
                         "standard or the building regulations under s.4(a)(1), which is not tied "
                         "to a Schedule period; and rights under other law, which s.7 preserves "
                         "(for example a claim where the contractor knew of a defect and concealed "
                         "it). Separately, a defect being hidden, and s.16 concealment, only relax "
                         "the NOTICE clock; they do not extend these periods. All are lawyer and "
                         "engineer questions. A closed window is not the end of the matter.")

    # The notice duty is a SECOND, independent clock.
    notice_deadline = add_years(handover, 1)
    if notified is not None:
        if notified < handover:
            out["warnings"].append(
                f"Notice date {notified} is before handover {handover}. A pre-handover list is "
                "useful evidence, but check whether a written notice was also sent after handover.")
        elif notified < discovered:
            out["warnings"].append(
                f"Notice date {notified} is before the discovery date {discovered}. One of the two "
                "dates is probably wrong; check them.")

    if visible_at_handover is True:
        out["notice_rule"] = (
            f"Discoverable at handover, so notice was due by {notice_deadline} "
            "(one year from handover, s.4a(a)(1)).")
        if notified is not None:
            out["notice_status"] = ("MET" if notified <= notice_deadline
                                    else "MISSED, this is a serious problem, take advice")
        else:
            out["notice_status"] = "UNKNOWN, supply --notified"
        if discovered > notice_deadline:
            out["warnings"].append(
                f"You said a reasonable inspection at handover would have found this defect, but it "
                f"was discovered on {discovered}, more than a year later. The statutory test is whether "
                "it COULD have been found at handover, not whether anyone noticed it. If a reasonable "
                "inspection would not have found it, re-run with --visible no.")
        if which == "current":
            out["notice_caveat"] = (
                "This one-year bar applies to an ordinary non-conformity. It does NOT apply to a "
                "FUNDAMENTAL (load-bearing) non-conformity that could not have been found by "
                "reasonable inspection at handover: s.4a(b) gives that its own rule, notice within "
                "a reasonable time after discovery, with no one-year cut-off.")
        else:
            out["notice_caveat"] = (
                "Pre-2011 text: there is no separate s.4a(b) limb, but a defect that could not have "
                "been found by reasonable inspection at handover, fundamental or not, falls under "
                "s.4a(a)(2), notice within a reasonable time after discovery.")
        out["notice_caveat"] += (
            " Never report a missed deadline as final where a load-bearing defect is in play. Only "
            "an engineer classifies. Separately, s.16 of the Sale Law 1968 lifts the notice bar where "
            "the contractor knew of the facts and did not disclose them, provided notice was given "
            "immediately on discovery, so a missed deadline is a question for an advocate.")
    elif visible_at_handover is False:
        out["notice_rule"] = ("Not discoverable at handover, so notice is due within a reasonable "
                              "time after you discovered it, even if more than a year has passed "
                              "since handover (s.4a(a)(2)).")
        if notified is None:
            out["notice_status"] = "NOT SUPPLIED. If not yet sent, act now and date your notice"
        elif notified >= discovered:
            gap = (notified - discovered).days
            if gap <= NOTICE_GAP_FLAG_DAYS:
                out["notice_status"] = f"Sent {gap} days after discovery."
            else:
                out["notice_status"] = (
                    f"Sent {gap} days after discovery. Whether that is a 'reasonable time' is a "
                    "question for an advocate, NOT a pass. Do not tell the user notice is fine.")
        else:
            out["notice_status"] = "CHECK DATES, notice precedes discovery"
    else:
        out["notice_rule"] = ("Not stated whether a reasonable inspection at handover could have "
                              "found the defect. This selects the notice rule, so it changes the "
                              "answer. Supply --visible yes or --visible no. When unsure, treat it "
                              "as discoverable for deadline purposes (the conservative choice).")
        out["notice_status"] = "UNKNOWN"
    return out


def render(r):
    print()
    print("=" * 68)
    print(f"  Schedule in use : {r['schedule']}")
    print(f"  {r['schedule_note']}")
    print("-" * 68)
    if r.get("alias_note"):
        print(f"  NOTE            : {r['alias_note']}")
    print(f"  Schedule row    : {r['row']}")
    print(f"  Handover        : {r['handover']}")
    print(f"  Discovered      : {r['discovered']}")
    print("-" * 68)
    print(f"  Bedek period    : {r['bedek_years']} years, ends {r['bedek_end']}")
    print(f"  Warranty ends   : {r['warranty_end']}  (bedek end + 3 years)")
    print(f"  STAGE           : {r['stage'].upper()}")
    print(f"  Burden of proof : {r['burden']}")
    if r.get("damp_range"):
        print("-" * 68)
        print("  Damp, by possible cause (an engineer decides which):")
        for k, y, be, we, st in r["damp_range"]:
            print(f"    {k:<8} {y} yr  bedek ends {be}  warranty ends {we}  stage {st.upper()}")
        if r["stage"] == "depends on cause":
            print("  The candidate rows give DIFFERENT stages, so who must prove what depends")
            print("  on the cause. Say so; do not pick the row most favourable to the buyer.")
    print("-" * 68)
    print(f"  Notice duty     : {r['notice_rule']}")
    print(f"  Notice status   : {r['notice_status']}")
    if r.get("notice_caveat"):
        print(f"  Notice caveat   : {r['notice_caveat']}")
    for w in r.get("warnings", []):
        print(f"  WARNING         : {w}")
    print("-" * 68)
    if r["schedule"] == "current":
        print("  Load-bearing / stability / safety defects are a SEPARATE regime:")
        print(f"  20-year window runs to {r['fundamental_bedek_end']}, and a claim can survive")
        print("  even beyond it if the buyer proves origin (s.4(a)(4)-(5)).")
    else:
        print("  Pre-2011 law: there is NO 20-year period. The old s.4(a)(4) covers a")
        print("  fundamental non-conformity discovered even after the warranty period")
        print("  that makes the apartment unfit for its purpose. The old text also has")
        print("  no s.4b(b) self-repair gateways and no s.7A(b), and does not name the")
        print("  sub-buyer. Route those questions to an advocate.")
    print("  This script does NOT decide whether a defect is load-bearing. Only a")
    print("  licensed engineer can. If you see cracks in structural elements,")
    print("  sagging, movement, or water near electrics, stop and get a licensed engineer.")
    print("  End dates are COVER periods, not deadlines to sue (limitation is separate).")
    print("  Dates on a boundary day are arguable: never plan to the last day.")
    print("=" * 68)
    print()


def main():
    p = argparse.ArgumentParser(description="Israeli new-apartment defect window calculator")
    p.add_argument("--handover", help="date the apartment was handed over, YYYY-MM-DD")
    p.add_argument("--discovered", help="date the defect was discovered, YYYY-MM-DD")
    p.add_argument("--type", dest="kind", help="Schedule row key, see --list")
    p.add_argument("--contract", help="date the ORIGINAL sale contract with the contractor was concluded (not a resale), YYYY-MM-DD")
    p.add_argument("--construction-finished",
                   help="date construction of the BUILDING finished, YYYY-MM-DD")
    p.add_argument("--visible", choices=["yes", "no"],
                   help="could a reasonable inspection at handover have found the defect")
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
        print("'damp' is shown across its candidate rows: sealing, pipes and thermal (current);")
        print("damp, pipes and other (pre-2011).")
        print("Load-bearing defects: separate regime, engineer territory. 20 years under the")
        print("current law; no fixed period under the pre-2011 text.\n")
        return

    if a.example:
        print("\nExample: pipe leak found 4 years and 10 months after a 2021 handover.")
        render(analyse(dt.date(2021, 3, 15), dt.date(2026, 1, 10), "pipes",
                       contract=dt.date(2020, 11, 1), visible_at_handover=False))
        print("Same kind of leak, but contract January 2009 and handover June 2009 (old Schedule):")
        render(analyse(dt.date(2009, 6, 1), dt.date(2026, 1, 10), "pipes",
                       contract=dt.date(2009, 1, 20), visible_at_handover=False))
        return

    missing = [f for f in ("handover", "discovered", "kind") if not getattr(a, f)]
    if missing:
        p.error("missing required: " + ", ".join("--" + m.replace("kind", "type") for m in missing))

    def d(value, flag):
        try:
            return dt.date.fromisoformat(value)
        except ValueError:
            raise SystemExit(
                f"{flag} must be a date as YYYY-MM-DD, got '{value}'. "
                "If the date is genuinely unknown, leave the flag off: --contract may be "
                "omitted (the current Schedule is assumed and the answer says so), but "
                "--handover and --discovered are required.")

    render(analyse(
        d(a.handover, "--handover"), d(a.discovered, "--discovered"), a.kind,
        contract=d(a.contract, "--contract") if a.contract else None,
        construction_finished=(d(a.construction_finished, "--construction-finished")
                               if a.construction_finished else None),
        visible_at_handover={"yes": True, "no": False}.get(a.visible),
        notified=d(a.notified, "--notified") if a.notified else None,
    ))


if __name__ == "__main__":
    sys.exit(main())
