# Changelog

## [1.5.0] - 2026-10-25

### Fixed
- Pension waiting period: the test is whether the candidate held pension insurance at hire (and whether a branch extension order gives day 1), not "first job". Step 1 now asks it, with the age threshold (21 men, 20 women).
- Non-compete: any ONE legitimate interest (trade secret, special consideration, special funded training, good faith) can support a restriction, so a paid non-compete is more likely to be enforced, not less. The test was stated as cumulative.
- Section 14: applies automatically since 2008 to the mandatory severance deposits; the "double liability" row and the "needs the General Authorization" framing are gone. The loss from a narrow salary definition is on fixed components that enter the severance base, not bonuses or overtime. Added the salary-raise trade-off.
- Inventions: "Employee Inventions Law" does not exist. Now Patents Law s.132 and s.134 (compensation waiver) and Copyright Law s.34.
- Notice: 12 completed months carries a month's notice (partial months are not counted); the hourly schedule moves at 12, 24 and 36 completed months.
- Annual leave: the statute alone gives 17 net days in year 9, not 15. The script's gross-to-net conversion now matches Kol Zchut row for row, leave seniority counts by calendar year, part-time workers accrue the same number of days, and a minor gets 18.
- Overtime: the 42-hour week is from an extension order in force since 1 April 2018; added the 5-day (8.6 / 7.6) and 6-day (8 / 7) daily norms so a lawful Sunday to Thursday schedule is not flagged. Global overtime remedy re-sourced.
- Keren hishtalmut above the tax ceiling is a note, not a defect, and is no longer negotiated down.
- Payslip duty re-cited to Wage Protection Law s.24; payday to ss.9-10. The Notice to Employee list now follows s.2 (direct supervisor, workers' organisation, contractor terms, the no-derogation statement).
- Pregnancy carve-out graded Minor when the contract is merely silent, since the protection applies regardless.
- Severity labels aligned between SKILL.md and the red-flag checklist. Unsourced figures removed (confidentiality "3-5 years", the 120-125% employer-cost band).
- `scripts/contract_sanity_check.py`: `--non-pension-fund` (5% tagmulim floor), `--full-section-14` (8.33% only when a full waiver is intended), `--leave-year`, `--minor`.

### Added
- `references/additional-clause-checks.md`: non-solicitation, rest-day work and on-call duty (s.9D1), longer contractual notice, leave forfeiture, manpower contractors, pay secrecy, minors, privacy and monitoring.
- Miluim: the 29.4.2026 extension order adds 30 days of dismissal protection and bars unpaid leave for reservists with 60+ days in the year.
- Youth minimum wage table (from 1 April 2026), Notice to Employee Law consequences (s.5, s.5A), ten more negotiation clauses, `references/domain-checklist.md`.
- Step 1 asks for every annex (NDA and IP assignment, option plan, policies).

### Changed
- Descriptions no longer open with "Not legal advice" / "אינו ייעוץ משפטי", per the owner decision of 2026-10-08/09. The legal notice section is unchanged.

## [1.4.0] - 2026-08-30

### Fixed
- The Section 14 finding implied the waiver is freestanding. Section 14 replaces severance only where a collective agreement or the Minister's General Authorization provides for it.
- Re-sourced the Section 14 claim from a secondary rights summary to the statute.

All notable changes to this skill are documented here.

## [1.3.0] - 2026-08-26

### Fixed

- דמי הבראה: התעריף במגזר הפרטי עודכן ל-451.5 ש"ח ליום לפי צו ההרחבה שפורסם ב-18.08.2026, כולל השלמה של 33.50 ש"ח ליום למי ששולם לפי 418, ותעריף 511.6 ש"ח במגזר הציבורי.
- דמי הבראה: הובהר שהזכאות קמה רק אחרי 12 חודשי עבודה, ולא "5 ימים בשנה הראשונה".
- חופשה שנתית: הטבלה תוקנה לסולם הסטטוטורי לפי סעיף 3(א) לחוק חופשה שנתית (16 ימי ברוטו בכל אחת מחמש השנים הראשונות, 18 בשישית, 21 בשביעית, עד 28), במקום "12 ימים בשנים 1-4 ו-23 מהשנה החמישית".
- ימי מחלה: הוסרה "תקרה שנתית של 18 יום" שאינה קיימת בחוק, והוסף סולם התשלום (יום ראשון ללא תשלום, ימים 2-3 בחצי, מהיום הרביעי מלא) ותקרת 90 הימים המצטברת.
- שבוע עבודה: 42 השעות יוחסו לצו ההרחבה ממרץ 2018 ולא לחוק, שקובע 45 שעות בסעיף 3 ותקרה יומית של 8 שעות בסעיף 2.
- אי-תחרות: הלכת "ויכמן" הוחלפה בהלכה המאומתת, ע"ע 164/99 פרומר וצ'ק פוינט נ' רדגארד.
- פנסיית עובד: 6% הוא המינימום החוקי ולא מקסימום; 7% ממצה את זיכוי סעיף 45א.
- סעיף בוררות: מוסגר מחדש לפי סעיף 24 לחוק בית הדין לעבודה, שאינו כלל שמבטל בוררות.
- תקופת ניסיון: מוסגרה מחדש, אין תקופת ניסיון סטטוטורית והיא אינה מקצרת הודעה מוקדמת, פנסיה או שימוע.
- MCP: ההמלצה על `israel-law` שאינו קיים בספרייה הוחלפה ב-`knesset`.
- סעיף 25(ב): הובהר שניכוי מלוא החוב מהשכר האחרון אפשרי רק כשהחוב אינו שנוי במחלוקת, והופרדה שאלת הניכוי משאלת האכיפות של התחייבות להחזר עלות הכשרה.
- הרשימה הסגורה של הניכויים: נוסף קנס משמעתי שהוטל לפי חוק או הסכם קיבוצי ולפיהם בלבד, ולא לפי חוזה אישי.
- ימי מחלה: הוסרה גם מ-B10 ומהסקריפט ההצגה של 18 יום כתקרה שנתית.
- `scripts/contract_sanity_check.py`: `--help` ומסלול הארגומנט החסר קרסו בגלל `%` במחרוזות העזרה; נוספה בדיקת רצפת 6% להפרשת העובד; סולם החופשה תוקן.

### Added

- שורת דגל אדום לתקרת השכר לפנסיה: צו ההרחבה מחייב הפרשות רק עד השכר הממוצע במשק (13,769 ש"ח ב-2026).
- שורות דגל אדום חדשות: סעיף 30(א)(5) "משרת אמון", חוזה לתקופה קצובה וסעיף 9, שלילת פיצויים לפי סעיפים 16-17, איפוס ותק בשינוי שליטה, סעיף שינוי חד-צדדי וסעיף 11(א), מילואים לפי סעיף 41א, אופציות ומסלול סעיף 102, ויתור על שימוע, ותקרת קרן השתלמות.
- הובהרה צורת התרופה בשעות גלובליות: סיווג מחדש של כל הסכום כשכר רגיל, ולא תיקון תעריף.
- `references/high-value-clause-traps.md` ו-`references/numerical-sanity-checks.md`.
- החזר הוצאות נסיעה כזכות חובה (עד 22.60 ש"ח ליום), וזכות העובד לבחור את סוג המוצר הפנסיוני ואת הגוף המנהל.
- החריג של מוצר שאינו קרן פנסיה: כיסוי אכ"ע ל-75% מהשכר הקובע, רצפת תגמולים של 5% ותקרה משולבת של 7.5%.
- כפיית חופשה בתקופת ההודעה המוקדמת (לפחות 14 ימים מחוץ לחופשה), חלף הודעה מוקדמת, ואיסור הפיטורים בתקופת הזכאות לדמי מחלה לפי סעיף 4א.
- טבלת ימי ההבראה המלאה לפי ותק, והיקף המשרה כקלט חובה בשלב 1.
- ההבהרה עברה לראש תבנית הפלט של שלב 4, לפי כלל המיקום שההבהרה מקדימה את התוצאה ואינה נגררת אחריה.

## [1.2.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.
