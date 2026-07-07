#!/usr/bin/env python3
"""Generate a dated bureaucratic timeline for settling an estate in Israel.

Anchors every milestone to the date of death and prints three horizons:
first 72 hours, first 30 days, and first year. The dates are calendar offsets
to help a bereaved family plan, not legal deadlines. Always confirm any real
deadline against the official source (btl.gov.il, gov.il, kolzchut.org.il).

Pure standard library. No network calls, no external services.

Usage:
    python3 generate_timeline.py --date-of-death 2026-07-01
    python3 generate_timeline.py --date-of-death 2026-07-01 --lang he
    python3 generate_timeline.py --example
"""

import argparse
import datetime as dt
import sys

# Each milestone: (day offset from death, English label, Hebrew label, horizon key)
MILESTONES = [
    (0, "Obtain the death notice (medical) from the doctor/hospital",
        "הוצאת הודעת פטירה (רפואית) מהרופא או בית החולים", "72h"),
    (1, "Arrange burial with the Chevra Kadisha / religious council / civil burial society",
        "תיאום קבורה עם חברה קדישא / מועצה דתית / עמותת קבורה אזרחית", "72h"),
    (7, "Confirm the death is registered at Misrad HaPnim and order the death certificate",
        "אימות רישום הפטירה במשרד הפנים והזמנת תעודת פטירה", "30d"),
    (10, "Order several certified copies of the death certificate (free)",
        "הזמנת מספר עותקים מאושרים של תעודת הפטירה (חינם)", "30d"),
    (14, "Notify banks; expect account freeze; request statements",
        "יידוע הבנקים; צפו להקפאת חשבון; בקשת פירוט", "30d"),
    (14, "Notify pension funds, provident funds, and insurers",
        "יידוע קופות גמל, פנסיה וחברות ביטוח", "30d"),
    (14, "Notify the employer; claim final salary, notice pay, vacation, severance",
        "יידוע המעסיק; דרישת שכר אחרון, דמי הודעה, פדיון חופשה, פיצויים", "30d"),
    (21, "Cancel standing orders; notify utilities, HMO, municipality, subscriptions",
        "ביטול הוראות קבע; יידוע תשתיות, קופת חולים, עירייה, מנויים", "30d"),
    (30, "Confirm with Bituach Leumi and actively claim survivor benefits (separate skill)",
        "אימות מול ביטוח לאומי ותביעת קצבת שאירים באופן פעיל (סקיל נפרד)", "30d"),
    (60, "Obtain the succession order / probate order (separate skill, out of scope here)",
        "הוצאת צו ירושה / צו קיום צוואה (סקיל נפרד, מחוץ לתחום כאן)", "1y"),
    (120, "After the order: release bank funds and securities",
        "אחרי הצו: שחרור כספים וניירות ערך בבנק", "1y"),
    (150, "After the order: re-register real estate at the Land Registry (Tabu)",
        "אחרי הצו: רישום מקרקעין מחדש בלשכת רישום המקרקעין (טאבו)", "1y"),
    (150, "After the order: transfer the vehicle at Misrad HaRishui",
        "אחרי הצו: העברת רכב במשרד הרישוי", "1y"),
]

HORIZON_TITLES = {
    "72h": ("First 72 hours: burial and first documents",
            "72 שעות ראשונות: קבורה ומסמכים ראשונים"),
    "30d": ("First 30 days: registration, certificate, notification cascade",
            "30 ימים ראשונים: רישום, תעודה, שרשרת יידוע"),
    "1y": ("First year: orders, asset transfer, benefits",
           "שנה ראשונה: צווים, העברת נכסים, קצבאות"),
}

ORDER = ["72h", "30d", "1y"]


def parse_date(text):
    try:
        return dt.date.fromisoformat(text)
    except ValueError:
        sys.exit("error: --date-of-death must be YYYY-MM-DD, e.g. 2026-07-01")


def build_timeline(dod, lang):
    lines = []
    for key in ORDER:
        en_title, he_title = HORIZON_TITLES[key]
        lines.append("")
        lines.append("=== " + (he_title if lang == "he" else en_title) + " ===")
        for offset, en, he, hkey in MILESTONES:
            if hkey != key:
                continue
            when = dod + dt.timedelta(days=offset)
            label = he if lang == "he" else en
            day_word = "יום" if lang == "he" else "day"
            lines.append(f"  {when.isoformat()} (+{offset} {day_word})  {label}")
    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Dated estate-settlement timeline for Israel.")
    p.add_argument("--date-of-death", help="Date of death, format YYYY-MM-DD")
    p.add_argument("--lang", choices=["en", "he"], default="en", help="Output language")
    p.add_argument("--example", action="store_true", help="Run with a sample date")
    args = p.parse_args()

    if args.example:
        dod = dt.date(2026, 7, 1)
        print("Example: date of death 2026-07-01")
    elif args.date_of_death:
        dod = parse_date(args.date_of_death)
    else:
        p.print_help()
        sys.exit(0)

    print(build_timeline(dod, args.lang))
    note = ("\nNote: dates are planning offsets, not legal deadlines. "
            "Confirm real deadlines at btl.gov.il, gov.il, and kolzchut.org.il.")
    print(note)


if __name__ == "__main__":
    main()
