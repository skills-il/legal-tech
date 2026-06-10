---
name: divorce-actuary
description: >-
  Expert actuarial and forensic accounting skill for Israeli divorce proceedings and asset
  division. Use when user uploads bank statements, salary slips, pension reports, provident
  fund documents, tax forms (106/135), or asks about "izun mishaba'im", "halakat nechasim",
  "knas girushin", "chovat tashlum", "pitzui gerushin", "chelek bapensiya", "divorzio",
  "mah magiya li", "hafrashat pitzuim", "yom hakera", or requests actuarial expert opinion
  for family court. Performs full asset mapping, pension valuation, suspicious transfer
  detection, and post-separation activity analysis. Produces court-ready Word reports.
  Do NOT use for general tax returns or business accounting (use tax-refund-106 instead).
license: MIT
allowed-tools: 'Bash(python:*)'
compatibility: >-
  No network required for document analysis. docx skill required for Word output.
  Works with Claude Code, Claude.ai, Cursor.
metadata:
  author: skills-il
  version: 2.0.0
  category: legal-tech
  tags:
    he:
      - גירושין
      - איזון-משאבים
      - אקטואר
      - פנסיה
      - חוות-דעת
      - בית-משפט
      - ישראל
    en:
      - divorce
      - asset-division
      - actuarial
      - pension
      - expert-opinion
      - family-court
      - israel
  display_name:
    he: "חוות דעת אקטוארית — גירושין ואיזון משאבים"
    en: Divorce Actuarial Expert Opinion
  display_description:
    he: "ניתוח אקטוארי מקצועי לאיזון משאבים בגירושין. מזהה נכסים, חשבונות סמויים, העברות חשודות ומפיק דוחות לבית המשפט."
    en: >-
      Professional actuarial analysis for Israeli divorce asset division. Identifies
      assets, hidden accounts, suspicious transfers, and produces court-ready reports.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# חוות דעת אקטוארית — גירושין ואיזון משאבים

## Instructions

### Step 0: Document Intake and Mode Detection

On receiving any documents, immediately catalog them:

```
📁 מסמכים שהתקבלו:
├── דפי חשבון בנק (PDF/CSV): [בנק, מס' חשבון, תקופה, בעלים]
├── תלושי שכר / טופס 106:   [בן זוג א' / ב' / שניהם]
├── מסמכי פנסיה:             [שמות קרנות, בעלים]
├── קרנות השתלמות:           [שמות קרנות, בעלים]
├── ני"ע / תיקי השקעות:      [חשבון, בעלים]
├── כרטיסי אשראי:            [מנפיק, בעלים]
└── אחר:                     [פרט]
```

**מועד הקרע — חובה ראשונה**: לפני כל ניתוח, ברר את מועד הקרע (יום הפרידה הרשמי). אם לא צוין — עצור ושאל. אין לנתח ולחשב ללא תאריך זה.

**זיהוי מצב הניתוח:**

| מצב | תיאור | פעולה |
|-----|-------|-------|
| מצב א | מסמכי צד אחד בלבד | ניתוח מלא לצד הידוע, שדות הצד השני כ"ממתין" |
| מצב ב | מסמכי שני הצדדים | ניתוח מלא + טבלת איזון סופית |
| מצב ג | מסמכי איזון קיים לבדיקה | ניתוח עצמאי → השוואה סעיף-מול-סעיף → ממצאי סטייה |

**כלל ברירת מחדל — ספקנות מקצועית**: הנח ניסיון הסתרה עד שהוכח אחרת. כל סכום נמוך מהצפוי, ניסוח עמום, או מסמך חסר — רשום כממצא לבדיקה.

---

### Step 1: Spouse Profile

| פרמטר | בן זוג א' | בן זוג ב' |
|-------|-----------|-----------|
| שם מלא | | |
| ת.ז. | | |
| מקור הכנסה עיקרי | | |
| שכר חודשי ברוטו | | |
| שכר חודשי נטו | | |
| חשבונות בנק | | |
| תאריך נישואין | | |
| מועד הקרע | | |
| תקופה משותפת (שנים) | | |

---

### Step 2: Bank Account Analysis

#### 2.1 Account Mapping
For each account: number, bank, owner, type (checking / savings / deposit), opening balance, closing balance.

#### 2.2 Income Classification
Scan every credit and classify: salary, self-employment, government benefits, internal transfers, unidentified income 🔴.

#### 2.3 Expense Anomaly Detection

Regular expenses to classify: mortgage/rent, food, children's education, vehicle, insurance, loan repayments.

**🔴 Flag immediately:**
1. Transfers to unidentified accounts — record date, amount, destination account number
2. Cash withdrawals above ₪2,000 in a single transaction
3. Payments to unknown or ambiguous entities
4. High-frequency transfers to the same recipient (possible hidden account)
5. Jewelry stores, luxury restaurants, hotels, travel — non-family expenses
6. **New accounts opened within 6 months before separation** — classic asset concealment pattern
7. Securities or funds purchased in children's names close to separation date
8. **All activity after yom hakera** — flag separately, does not enter balance calculation

#### 2.4 Post-Separation Activity (Critical)
Any transaction after yom hakera that reduces joint assets requires special attention:

| תאריך | תיאור | סכום | חשבון | סיווג | דגל |
|-------|-------|------|-------|-------|-----|
| | | | | | |

Patterns that indicate deliberate asset depletion: locking funds in fixed deposits after separation, transfers to unidentified accounts post-separation, credit card debt payment from joint assets after separation, furniture or property purchases the day after separation.

#### 2.5 Credit Card Analysis
For each card: issuer, holder, total charges per period, categorize by: food, health, transport, insurance, entertainment, unidentified. Flag non-family expenditures and PayPal/foreign payments to unknown recipients.

---

### Step 3: Pension Funds

For each pension fund (both spouses):

| פרמטר | קרן |
|-------|-----|
| שם הקרן | |
| מספר פוליסה | |
| תאריך הצטרפות | |
| יתרה ביום הנישואין | |
| יתרה ביום הקרע | |
| רכיב לאיזון | |

**Actuarial calculation:**
```
שיטה 1 — ערך נוכחי מהוון:
  רכיב לאיזון = (שנות נישואין / סה"כ שנות עבודה) × יתרה ביום הקרע

שיטה 2 — מועד היגמלן:
  רכיב נזיל   = קרנות השתלמות נזילות → תשלום עכשיו
  רכיב עתידי  = קרנות פנסיה → פסיקתאות (חוק חלוקת חסכון בין בני זוג שנפרדו)
```

Note: If no annual report exists for the year of marriage, flag the gap and recommend obtaining confirmation from the fund.

---

### Step 4: Provident Funds (Keren Hishtalmut)

For each fund: name, policy number, owner, vesting status (6-year rule), balance at marriage, balance at separation.

```
סכום לאיזון = (יתרה ביום הקרע − יתרה ביום הנישואין) / 2
```

Flag funds redeemed near separation date — verify balance before redemption, not after.

---

### Step 5: Additional Assets

Check and record where data exists:
- Real estate: market value, mortgage balance, pre/post-marriage acquisition
- Investment portfolios / securities — including children's custodial accounts (verify when opened and source of funds)
- Vehicles: market value per Levi Yitzhak price guide at separation date
- Debts and loans (deduct from assets)
- Private businesses: goodwill, inventory, equipment
- Extra-banking accounts (Tria, savings clubs, digital wallets)

---

### Step 6: Undisclosed Income and Asset Detection

#### Cross-checks
- Compare salary per pay slip vs. actual bank deposits — does all salary arrive?
- Look for cash income not appearing in account
- Identify bank accounts referenced in expense records but not provided as documents
- Check if new accounts were opened in the 3–6 months before separation

#### Suspicion Patterns

| תבנית | משמעות אפשרית |
|-------|---------------|
| העברה חוזרת לחשבון לא מזוהה | חשבון סמוי |
| שכר גבוה + חשבון ריק | הסטת כספים לפני ההליך |
| "הלוואה לחבר/קרוב" | הסתרת נכסים |
| ירידה פתאומית בהכנסות לפני הפרידה | הנמכת הכנסה מכוונת |
| פתיחת חשבון חדש + נעילה בפקדון | ניסיון להקשות על עיקול |
| רכישת ני"ע "לילדים" סמוך לקרע | הסרת נכסים מאיזון |

---

### Step 7: Asset Balance Table and Payment Calculation

#### 7.1 Balance Table

| נכס | בן זוג א' | בן זוג ב' | פער | מחצית הפער |
|-----|-----------|-----------|-----|-----------|
| חשבונות בנק | | | | |
| פנסיה (נזיל) | | | | |
| פנסיה (עתידי) | | | | |
| קרן השתלמות | | | | |
| ני"ע / השקעות | | | | |
| כלי רכב | | | | |
| נדל"ן | | | | |
| **סה"כ** | | | | **← תשלום לאיזון** |

#### 7.2 Payment Calculation
```
תשלום לאיזון = |נכסי א' − נכסי ב'| / 2
← בן הזוג בעל הנכסים הגבוהים יותר משלם לשני
```

#### 7.3 Assumptions and Gaps
List every assumption made in absence of a document, every missing document, and every anomalous finding requiring further legal review.

---

### Step 7b: Comparison Against Existing Expert Opinion (Mode C Only)

When an existing actuarial report is provided, perform independent analysis first, then compare:

| נכס / סעיף | ערך בחוות הדעת הקיימת | ערך לפי ניתוחנו | סטייה | פרשנות |
|------------|----------------------|----------------|-------|---------|
| | | | | |

**Deviation categories:**
- 🔴 נכס חסר לחלוטין — not mentioned at all in existing report
- 🔴 הערכת חסר מהותית — more than 15% gap
- 🟠 טעות חישוב — correct data, wrong calculation
- 🟡 תאריך שגוי — not calculated to yom hakera
- 🟡 סיווג שגוי — exempt asset classified without proof (e.g., "inheritance" without documentation)
- 🟢 תואם — consistent with our findings

```
השפעה על תשלום האיזון = (ניתוחנו − קיים) / 2  [חובת השלמה לצד המקופח]
```

---

### Step 8: Red Flags Summary

List all anomalies by severity:

🔴 **דחוף — מצריך בירור משפטי**: unexplained transfers, unknown accounts, suspected concealment, post-separation asset depletion.

🟠 **לבדיקה**: unidentified recipients, new accounts near separation, securities in children's names.

🟡 **לתשומת לב**: high cash withdrawals, income decline, missing documents.

🟢 **תקין**: explained after review.

---

### Step 9: Missing Documents Checklist

For each missing item, state: what it is, which finding it affects, and recommended action.

| # | מסמך חסר | ממצא שנפגע | פעולה מומלצת | עדיפות |
|---|---------|-----------|--------------|--------|
| | | | | |

---

## Examples

### Example 1: Single-Spouse Document Analysis

User says: "uploaded my husband's bank statements and pension — what do I get?"

Actions:
1. Catalog documents, confirm yom hakera
2. Map all accounts, classify income and expenses
3. Flag suspicious transfers and post-separation activity
4. Calculate pension component for the joint period
5. Present balance table with spouse B as "pending data"
6. Offer Word report

### Example 2: Full Bilateral Analysis with Existing Report

User says: "הנה חוות הדעת של המומחה ומסמכי שני הצדדים — בדוק אם יש טעויות"

Actions:
1. Set Mode C, confirm yom hakera
2. Independently analyze all raw documents
3. Build own balance table
4. Compare line-by-line against expert report
5. Flag deviations with monetary impact
6. Recommend actions for each gap

### Example 3: Suspicious Activity Deep-Dive

User says: "יש לי חשד שהוא הסתיר כספים לפני הגירושין"

Actions:
1. Analyze all transfers in 6 months before separation
2. Map all accounts referenced in transactions but not provided
3. Check for new accounts opened near separation
4. Examine securities purchases in children's names
5. Analyze post-separation activity for asset depletion
6. Produce suspicion report with recommended legal actions

---

## Reference Links

- [חוק יחסי ממון בין בני זוג, תשל"ג-1973](https://www.nevo.co.il/law_html/Law01/P222_001.htm)
- [חוק חלוקת חסכון פנסיוני בין בני זוג שנפרדו, תשע"ד-2014](https://www.nevo.co.il/law_html/Law01/500_1372.htm)
- [המסלקה הפנסיונית — משרד האוצר](https://www.mof.gov.il/en/ProfessionalDivisions/FinancialPension/Pages/PensionClearingHouse.aspx)
- [מחירון לוי יצחק לרכבים](https://www.leviyitzhak.co.il)
- [רשות שוק ההון, ביטוח וחיסכון](https://www.gov.il/he/departments/capital_market_insurance_and_savings_authority)

---

## Troubleshooting

### "Separation date not in documents"
Stop analysis. Ask user directly: "מהו מועד הקרע?" Do not estimate or assume.

### "Pension report shows current balance only, no historical"
Note the gap. Use the available balance with a disclaimer. Recommend requesting a historical report from the fund for the marriage date.

### "Document is in image format, text not extractable"
Use the pdf-reading skill to rasterize and extract. If still unreadable, describe visible figures from the image and flag as "manually transcribed — verify."

### "Suspicious transfer to unknown account"
Record exact account number, date, amount. Note in red flags. Recommend the attorney request court order to identify account holder from the bank.
