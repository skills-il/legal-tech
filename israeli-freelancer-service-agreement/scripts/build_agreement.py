#!/usr/bin/env python3
"""Assemble a Hebrew Israeli freelancer service agreement (הסכם למתן שירותים) skeleton.

This builds a structured, RTL-ready draft from a small set of parameters. It does NOT
provide legal advice and is NOT a substitute for a lawyer: it produces a starting draft
that the freelancer (and ideally a lawyer) should review and adapt.

The clause order follows standard Israeli service-agreement practice:
  preamble, definitions, scope & acceptance, term & termination, consideration & payment,
  taxes/VAT/withholding & invoicing, independent-contractor framing (intended relationship),
  IP ownership + moral rights, confidentiality, data protection (optional),
  defects/set-off limits/lien, liability & indemnity (mutual), insurance, general, signatures.

Flags:
  --provider / --provider-id / --client / --client-id   parties
  --services                                            scope summary
  --fee                                                 amount in NIS (0 is allowed)
  --vat murshe|patur                                    drives the VAT wording
  --payment-net N                                       שוטף+N; 0 is allowed and means שוטף+0
  --recurring                                           renders the fee as a monthly amount
  --personal-data                                       adds the data-protection clause
  --example                                             fill every field with sample values
  --out FILE                                            write to FILE (works with --example)

Usage:
  python3 build_agreement.py --example
  python3 build_agreement.py --provider "ישראל ישראלי" --provider-id 000000000 \
      --client "חברת לקוח בעמ" --client-id 510000000 \
      --services "עיצוב גרפי וניהול מותג" --fee 8000 --vat murshe \
      --payment-net 30 --recurring --personal-data --out agreement.md
"""

import argparse
import sys
from datetime import date

PAYMENT_DEFAULT_NET = 30  # days; the contract should state an explicit term. See references/legal-reference.md


def build(p):
    today = date.today().strftime("%d/%m/%Y")
    if p.vat == "murshe":
        vat_line = ("התמורה נקובה ללא מע\"מ. לתמורה יתווסף מע\"מ כדין (18% נכון ל-2026) כנגד חשבונית מס. "
                    "מוסכם במפורש כי המחיר אינו כולל מע\"מ.")
    else:
        vat_line = ("נותן השירות הוא עוסק פטור ואינו גובה מע\"מ, וימסור קבלה כדין. "
                    "אם מחזור נותן השירות יחצה את תקרת העוסק הפטור והוא יירשם כעוסק מורשה, יתווסף מע\"מ לתמורה ממועד הרישום.")

    # Must be an explicit None check: --payment-net 0 is a documented, recommended
    # option (שוטף+0) and a falsy test would silently rewrite it to the default.
    net = PAYMENT_DEFAULT_NET if p.payment_net is None else p.payment_net
    recurring_suffix = " לחודש" if p.recurring else ""
    sections = []

    sections.append(f"""# הסכם למתן שירותים

נחתם ביום {today}

**בין:**
{p.provider}{f', ת.ז./ע.מ. {p.provider_id}' if p.provider_id else ''} (להלן: "**נותן השירות**")

**לבין:**
{p.client}{f', ח.פ./ע.מ. {p.client_id}' if p.client_id else ''} (להלן: "**הלקוח**")

**הואיל** ונותן השירות הוא עוסק עצמאי המנהל עסק עצמאי ומספק שירותי {p.services};
**והואיל** והלקוח מעוניין לקבל מנותן השירות את השירותים, ונותן השירות מסכים לספקם כעוסק עצמאי המעניק שירות ללקוחות נוספים, ולא במסגרת יחסי עובד-מעביד;

**לפיכך הוסכם והותנה בין הצדדים כדלקמן:**""")

    sections.append("""## מבוא והגדרות
המבוא להסכם זה והנספחים לו מהווים חלק בלתי נפרד ממנו. כותרות הסעיפים נועדו לנוחות בלבד.
"השירותים" הם השירותים המפורטים בסעיף השירותים ובנספח א'. "התוצרים" הם תוצרי העבודה שנמסרים ללקוח.""")

    sections.append(f"""## השירותים, היקף ומסירה
נותן השירות יספק ללקוח את השירותים הבאים: {p.services}.
היקף השירותים, אבני הדרך, התוצרים, מספר סבבי התיקונים ולוח הזמנים יפורטו בנספח א' (תיאור עבודה / SOW).
מסירה ואישור קבלה: הלקוח יבדוק כל תוצר ויעביר הערות בכתב בתוך 7 ימי עסקים. אם לא נמסרו הערות במועד, יראו את התוצר כמאושר.
נותן השירות יספק את השירותים במקצועיות ובהתאם לכל דין.""")

    sections.append("""## תקופת ההתקשרות וסיומה
ההסכם ייכנס לתוקף במועד חתימתו ויימשך עד השלמת השירותים, אלא אם הסתיים קודם לכן.
כל צד רשאי לסיים את ההתקשרות בהודעה מוקדמת בכתב של 30 יום מראש; כל צד רשאי לסיים מיידית בשל הפרה יסודית שלא תוקנה בתוך 14 יום.
תשלום עבור עבודה שבוצעה: עם סיום ההתקשרות מכל סיבה, ישלם הלקוח לנותן השירות את התמורה עבור כל השירותים והתוצרים שסופקו או שהושלמו עד מועד הסיום, באופן יחסי, וכן הוצאות שאושרו מראש.
בפרויקט במחיר קבוע שבוטל לאחר תחילת העבודה, ישולם לנותן השירות לפי שיעור ההתקדמות בפועל, ולא פחות מדמי ביטול שייקבעו בנספח א'.""")

    sections.append(f"""## התמורה, מע\"מ, חשבונית וניכוי מס
בתמורה לשירותים ישלם הלקוח לנותן השירות סך של {p.fee:,.0f} ש\"ח{recurring_suffix}.
{vat_line}
התשלום יבוצע בתנאי שוטף + {net}, כלומר לא יאוחר מ-{net} ימים מתום החודש שבו הומצאה החשבונית ללקוח, וזאת כתנאי מפורש הגובר על ברירת המחדל שבחוק מוסר תשלומים לספקים, התשע\"ז-2017.
המצאת החשבונית תיעשה בדואר אלקטרוני לכתובת שתימסר בנספח א', עם אישור מסירה, או בכל דרך אחרת מהדרכים הקבועות בחוק.
בדיקת החשבונית: הלקוח רשאי להחזיר חשבונית שחסר בה פרט מהותי, ובלבד שיפרט בכתב את הליקויים ויעשה זאת בתוך 23 ימי עסקים ממועד ההמצאה. לא הוחזרה החשבונית במועד ובאופן זה, יראו אותה כשלמה ומאושרת לתשלום.
איחור בתשלום יישא הפרשי הצמדה וריבית שקלית, ובחלוף 30 ימים נוספים דמי פיגורים, וזאת כתנאי חוזי מוסכם בין הצדדים, במצטבר ומבלי לגרוע מכל סעד לפי חוק מוסר תשלומים לספקים. נותן השירות רשאי להשהות את מתן השירות כל עוד התמורה לא שולמה במועד.
ניכוי מס במקור: ככל שהלקוח חייב בניכוי מס במקור, ינוכה המס כדין, אלא אם ימסור נותן השירות אישור ניהול ספרים ואישור על פטור/שיעור מופחת מניכוי מס במקור בתוקף. נותן השירות אחראי למסור אישורים אלה.""")

    sections.append("""## מעמד עצמאי וכוונת הצדדים
כוונת הצדדים היא להתקשרות מסחרית בין עסקים, ולא יחסי עובד-מעביד. התמורה גבוהה משכר עובד מקביל ונקבעה על בסיס היות נותן השירות עצמאי הנושא בעלויותיו.
נותן השירות נושא באופן בלעדי בכל תשלומי המס, ביטוח לאומי, מס בריאות וההפרשות הפנסיוניות החלים עליו.
נותן השירות אינו מחויב לעבוד במקום או בשעות שקובע הלקוח, רשאי לתת שירות ללקוחות נוספים, ומשתמש בכליו שלו. אין בלעדיות.
נותן השירות רשאי להיעזר בקבלני משנה לביצוע השירותים, בכפוף לאחריותו לתוצאה ולשמירת הסודיות (היעדר דרישת ביצוע אישי תומך במעמד העצמאי).
קיזוז במקרה של סיווג מחדש: אם על אף כוונת הצדדים תקבע ערכאה מוסמכת כי התקיימו יחסי עובד-מעביד, יחושב ההפרש בין התמורה ששולמה לבין שכר עובד מקביל, וההפרש ניתן לקיזוז כנגד זכויות שייפסקו. מובהר כי סעיף זה הוא לטובת הלקוח, שבית הדין אינו מחויב לכבדו, וכי אין בו כדי לוותר על זכויות קוגנטיות מכוח דין.""")

    sections.append("""## קניין רוחני וזכות מוסרית
זכויות הקניין הרוחני (הזכויות הכלכליות) בתוצרים שנוצרו עבור הלקוח יועברו ללקוח עם קבלת מלוא התמורה. עד לתשלום מלא, הזכויות נותרות בידי נותן השירות. העברה זו נעשית במסמך בכתב כנדרש בדין.
ברירת המחדל בחוק זכות יוצרים, התשס\"ח-2007 ליצירה מוזמנת היא שהבעלות נותרת ביוצר, אלא אם הוסכם אחרת במפורש או במשתמע. הצדדים מסכימים כי הסדר הבעלות הקבוע בהסכם זה הוא ההסדר המלא והבלעדי ביניהם, וכי לא תישמע טענה להעברה או לשמירה של זכויות מכללא מעבר לאמור בו.
זכות מוסרית: הזכות המוסרית של היוצר (ייחוס ושלמות היצירה) היא אישית ואינה ניתנת להעברה. מובהר כי לפי הדין אין זכות מוסרית בתוכנת מחשב. ככל שהתוצרים כוללים יצירה שחלה עליה זכות מוסרית, נותן השירות מסכים מראש לביצוע התאמות, עריכה, שינויי פורמט ושילוב התוצרים במוצרי הלקוח, ואלה ייחשבו סבירים בנסיבות העניין; הסדר קרדיט וייחוס ייקבע בנספח א'.
נותן השירות שומר לעצמו זכויות בכלים, בידע ובשיטות הכלליים שהיו לו מראש. רכיבי צד שלישי וקוד פתוח יימסרו ברישיון בלבד, ולא יועברו בבעלות, ויפורטו בנספח.""")

    sections.append("""## סודיות
כל צד ישמור בסודיות כל מידע סודי של הצד האחר, ולא יעשה בו שימוש אלא לצורך ההסכם. חובת הסודיות תעמוד בתוקפה גם לאחר סיום ההתקשרות.
הגבלת עיסוק תוגבל להגנה על סוד מסחרי ולאי-פנייה יזומה ללקוחות/עובדים, ולא תהווה איסור תחרות גורף.""")

    if getattr(p, "personal_data", False):
        sections.append("""## הגנת הפרטיות ואבטחת מידע
ככל שנותן השירות מעבד מידע אישי מטעם הלקוח, הוא יפעל כמחזיק/מעבד מטעמו בלבד, ינקוט אמצעי אבטחת מידע סבירים, לא יעשה במידע שימוש החורג מההסכם, יודיע ללקוח על אירוע אבטחה ללא דיחוי, וימחק או יחזיר את המידע בתום ההתקשרות, בהתאם לחוק הגנת הפרטיות ותיקון 13 לו.""")

    sections.append("""## ליקויים, תיקונם והגבלת קיזוז
על הסכם זה חלות הוראות חוק חוזה קבלנות, התשל\"ד-1974, ככל שלא נקבע בו אחרת.
הודעה על ליקוי: הלקוח יודיע לנותן השירות בכתב על כל ליקוי בתוך זמן סביר מרגע שגילה אותו או שהיה עליו לגלותו, ויעניק לו הזדמנות נאותה לתקנו.
תיקון: נותן השירות יתקן ליקוי בר-תיקון בתוך 14 ימי עסקים ממועד ההודעה, או בתוך פרק זמן אחר שיוסכם בכתב.
הגבלת קיזוז: לא יקזז הלקוח סכום כלשהו מהתמורה ולא יבצע תיקון על חשבון נותן השירות, אלא לאחר שמסר הודעה כאמור, חלף מועד התיקון, ופירט בכתב את הליקוי ואת אופן חישוב ירידת הערך הנטענת. סכום הקיזוז המצטבר לא יעלה על התמורה ששולמה בפועל בעד התוצר שבו נמצא הליקוי. מחלוקת בעניין ליקוי תתברר בהליך המוסכם בהסכם זה ולא בדרך של עשיית דין עצמית.
זכות עיכבון: לנותן השירות תעמוד זכות עיכבון על נכסים וחומרים שמסר לו הלקוח לצורך ביצוע השירותים, להבטחת סכומים המגיעים לו לפי הסכם זה. אין באמור בסעיפי המסירה או השבת החומרים כדי לוותר על זכות זו.

## אחריות, שיפוי וביטוח
נותן השירות יתקן על חשבונו ליקויים שנבעו מרשלנותו, תוך זמן סביר.
אחריותו הכוללת של נותן השירות לא תעלה על התמורה ששולמה בפועל ב-12 החודשים שקדמו לאירוע, למעט במקרים של זדון, הפרת סודיות או הפרת קניין רוחני.
הלקוח ישפה את נותן השירות בגין תביעות הנובעות מחומרים שהלקוח סיפק או משימוש של הלקוח בתוצרים בניגוד להסכם. השיפוי הדדי בכפוף להודעה ולשיתוף פעולה.
אם נדרש בנספח א', יחזיק נותן השירות בביטוח אחריות מקצועית בהיקף שיוסכם.""")

    sections.append("""## שונות
הסכם זה משקף את מלוא ההסכמות בין הצדדים. כל שינוי ייעשה בכתב ובחתימת שני הצדדים.
על ההסכם יחולו דיני מדינת ישראל. סמכות השיפוט תהיה לבתי המשפט המוסמכים במחוז שיוסכם; מחלוקות בדבר סיווג ההעסקה נתונות לבית הדין לעבודה על פי דין.""")

    sections.append("""## חתימות

| נותן השירות | הלקוח |
|---|---|
| שם: ____________ | שם: ____________ |
| חתימה: ____________ | חתימה: ____________ |
| תאריך: ____________ | תאריך: ____________ |

---
*טיוטה זו נוצרה ככלי עזר ואינה מהווה ייעוץ משפטי. מומלץ שעורך דין יעבור על ההסכם לפני חתימה.*""")

    return "\n\n".join(sections)


EXAMPLE = argparse.Namespace(
    provider="ישראל ישראלי", provider_id="000000000",
    client='חברת לקוח בעמ', client_id="510000000",
    services="עיצוב גרפי וניהול מותג", fee=8000, vat="murshe",
    payment_net=30, recurring=False, personal_data=False, out=None,
)


def main():
    ap = argparse.ArgumentParser(description="Build an Israeli freelancer service agreement skeleton")
    ap.add_argument("--provider"); ap.add_argument("--provider-id", dest="provider_id")
    ap.add_argument("--client"); ap.add_argument("--client-id", dest="client_id")
    ap.add_argument("--services")
    ap.add_argument("--fee", type=float)
    ap.add_argument("--vat", choices=["murshe", "patur"], default="murshe")
    ap.add_argument("--payment-net", dest="payment_net", type=int, default=PAYMENT_DEFAULT_NET,
                    help="שוטף+N payment term counted from month end; 0 is valid (שוטף+0)")
    ap.add_argument("--recurring", action="store_true",
                    help="Render the fee as a monthly amount (retainer) rather than a one-off")
    ap.add_argument("--personal-data", dest="personal_data", action="store_true",
                    help="Include a data-protection clause (use when the freelancer processes the client's personal data)")
    ap.add_argument("--out")
    ap.add_argument("--example", action="store_true")
    a = ap.parse_args()

    if a.example:
        # Preserve --out (and only --out) so `--example --out FILE` writes a file
        # instead of silently discarding the flag and printing to stdout.
        out = a.out
        a = argparse.Namespace(**vars(EXAMPLE))
        a.out = out
    # Explicit None checks: --fee 0 is legitimate (pro bono / placeholder draft)
    # and a truthiness test would reject it as "missing".
    missing = [n for n in ("provider", "client", "services", "fee")
               if getattr(a, n, None) is None]
    if missing:
        print("Missing required fields: " + ", ".join("--" + m for m in missing),
              file=sys.stderr)
        print("Try --example, or pass --provider --client --services --fee.", file=sys.stderr)
        sys.exit(1)

    doc = build(a)
    if getattr(a, "out", None):
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(doc)
        print(f"Wrote {a.out}")
    else:
        print(doc)


if __name__ == "__main__":
    main()
