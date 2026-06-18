#!/usr/bin/env python3
"""Assemble a Hebrew Israeli freelancer service agreement (הסכם למתן שירותים) skeleton.

This builds a structured, RTL-ready draft from a small set of parameters. It does NOT
provide legal advice and is NOT a substitute for a lawyer: it produces a starting draft
that the freelancer (and ideally a lawyer) should review and adapt.

The clause order follows standard Israeli service-agreement practice:
  preamble, definitions, scope & acceptance, term & termination, consideration & payment,
  taxes/VAT/withholding & invoicing, independent-contractor framing (intended relationship),
  IP ownership + moral-rights waiver, confidentiality, data protection (optional),
  warranties, liability & indemnity (mutual), insurance, general, signatures.

Usage:
  python3 build_agreement.py --example
  python3 build_agreement.py --provider "ישראל ישראלי" --provider-id 000000000 \
      --client "חברת לקוח בעמ" --client-id 510000000 \
      --services "עיצוב גרפי וניהול מותג" --fee 8000 --vat murshe \
      --payment-net 30 --personal-data --out agreement.md
"""

import argparse
import sys
from datetime import date

PAYMENT_DEFAULT_NET = 30  # days; the contract should state an explicit term. See references/legal-reference.md


def build(p):
    today = date.today().strftime("%d/%m/%Y")
    if p.vat == "murshe":
        vat_line = ("התמורה נקובה ללא מע\"מ. לתמורה יתווסף מע\"מ כדין (18% נכון ל-2025) כנגד חשבונית מס. "
                    "מוסכם במפורש כי המחיר אינו כולל מע\"מ.")
    else:
        vat_line = ("נותן השירות הוא עוסק פטור ואינו גובה מע\"מ, וימסור קבלה כדין. "
                    "אם מחזור נותן השירות יחצה את תקרת העוסק הפטור והוא יירשם כעוסק מורשה, יתווסף מע\"מ לתמורה ממועד הרישום.")

    net = p.payment_net or PAYMENT_DEFAULT_NET
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
בתמורה לשירותים ישלם הלקוח לנותן השירות סך של {p.fee:,.0f} ש\"ח {'לחודש' if p.recurring else ''}.
{vat_line}
התשלום יבוצע בתנאי שוטף + {net} מיום קבלת החשבונית, וזאת כתנאי מפורש הגובר על ברירת המחדל שבחוק מוסר תשלומים לספקים, התשע\"ז-2017.
איחור בתשלום יישא הפרשי הצמדה וריבית, ובחלוף 30 ימים נוספים דמי פיגורים, לפי חוק מוסר תשלומים לספקים. נותן השירות רשאי להשהות את מתן השירות כל עוד התמורה לא שולמה במועד.
ניכוי מס במקור: ככל שהלקוח חייב בניכוי מס במקור, ינוכה המס כדין, אלא אם ימסור נותן השירות אישור ניהול ספרים ואישור על פטור/שיעור מופחת מניכוי מס במקור בתוקף. נותן השירות אחראי למסור אישורים אלה.""")

    sections.append("""## מעמד עצמאי וכוונת הצדדים
כוונת הצדדים היא להתקשרות מסחרית בין עסקים, ולא יחסי עובד-מעביד. התמורה גבוהה משכר עובד מקביל ונקבעה על בסיס היות נותן השירות עצמאי הנושא בעלויותיו.
נותן השירות נושא באופן בלעדי בכל תשלומי המס, ביטוח לאומי, מס בריאות וההפרשות הפנסיוניות החלים עליו.
נותן השירות אינו מחויב לעבוד במקום או בשעות שקובע הלקוח, רשאי לתת שירות ללקוחות נוספים, ומשתמש בכליו שלו. אין בלעדיות.
נותן השירות רשאי להיעזר בקבלני משנה לביצוע השירותים, בכפוף לאחריותו לתוצאה ולשמירת הסודיות (היעדר דרישת ביצוע אישי תומך במעמד העצמאי).
קיזוז במקרה של סיווג מחדש: אם על אף כוונת הצדדים תקבע ערכאה מוסמכת כי התקיימו יחסי עובד-מעביד, יחושב ההפרש בין התמורה ששולמה לבין שכר עובד מקביל, וההפרש ניתן לקיזוז כנגד זכויות שייפסקו. מובהר כי סעיף זה הוא לטובת הלקוח, שבית הדין אינו מחויב לכבדו, וכי אין בו כדי לוותר על זכויות קוגנטיות מכוח דין.""")

    sections.append("""## קניין רוחני וזכות מוסרית
זכויות הקניין הרוחני (הזכויות הכלכליות) בתוצרים שנוצרו עבור הלקוח יועברו ללקוח עם קבלת מלוא התמורה. עד לתשלום מלא, הזכויות נותרות בידי נותן השירות.
ברירת המחדל בחוק זכות יוצרים, התשס\"ח-2007 ליצירה מוזמנת היא שהבעלות נותרת ביוצר; העברה זו גוברת עליה בהסכמה מפורשת.
הזכות המוסרית של היוצר (ייחוס ושלמות היצירה) היא אישית ואינה ניתנת להעברה; ככל שנדרש, נותן השירות מוותר על אכיפתה כלפי הלקוח בקשר לתוצרים, בכפוף לדין.
נותן השירות שומר לעצמו זכויות בכלים, בידע ובשיטות הכלליים שהיו לו מראש. רכיבי צד שלישי וקוד פתוח יימסרו ברישיון בלבד, ולא יועברו בבעלות, ויפורטו בנספח.""")

    sections.append("""## סודיות
כל צד ישמור בסודיות כל מידע סודי של הצד האחר, ולא יעשה בו שימוש אלא לצורך ההסכם. חובת הסודיות תעמוד בתוקפה גם לאחר סיום ההתקשרות.
הגבלת עיסוק תוגבל להגנה על סוד מסחרי ולאי-פנייה יזומה ללקוחות/עובדים, ולא תהווה איסור תחרות גורף.""")

    if getattr(p, "personal_data", False):
        sections.append("""## הגנת הפרטיות ואבטחת מידע
ככל שנותן השירות מעבד מידע אישי מטעם הלקוח, הוא יפעל כמחזיק/מעבד מטעמו בלבד, ינקוט אמצעי אבטחת מידע סבירים, לא יעשה במידע שימוש החורג מההסכם, יודיע ללקוח על אירוע אבטחה ללא דיחוי, וימחק או יחזיר את המידע בתום ההתקשרות, בהתאם לחוק הגנת הפרטיות ותיקון 13 לו.""")

    sections.append("""## אחריות, שיפוי וביטוח
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
    ap.add_argument("--payment-net", dest="payment_net", type=int, default=PAYMENT_DEFAULT_NET)
    ap.add_argument("--recurring", action="store_true")
    ap.add_argument("--personal-data", dest="personal_data", action="store_true",
                    help="Include a data-protection clause (use when the freelancer processes the client's personal data)")
    ap.add_argument("--out")
    ap.add_argument("--example", action="store_true")
    a = ap.parse_args()

    if a.example:
        a = EXAMPLE
    if not (a.provider and a.client and a.services and a.fee):
        print("Missing required fields. Try --example, or pass --provider --client --services --fee.", file=sys.stderr)
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
