# Periods, burdens and remedies

Source of every period and rule below: the consolidated text of חוק המכר (דירות), תשל"ג-1973 at https://www.nevo.co.il/law_html/law00/72490.htm (version current to 18-09-2023, following Amendment 9), the Knesset texts of Amendment 3 (1990, https://fs.knesset.gov.il/12/law/12_lsr_210782.pdf, which enacted the pre-2011 Schedule and the pre-2011 wording of ss.4, 4a, 4b and 7A) and Amendment 5 (2011, https://fs.knesset.gov.il/18/law/18_lsr_300642.pdf), and Kol Zchut at https://www.kolzchut.org.il/he/אחריות_קבלן_לליקויים_בדירה_חדשה.

## Which schedule applies

The Schedule of periods was rewritten by Amendment 5, which took effect on 06.04.2011. Which version governs depends on the sale contract and on when the BUILDING was completed, not on when the defect appeared. s.11(c), verbatim:

> "חוק המכר (דירות) (תיקון מס' 5), התשע"א-2011 (בסעיף קטן זה – תיקון מס' 5), לא יחול על דירה בבניין שבנייתו הסתיימה או שחוזה המכר לגביה נכרת לפני תחילתו של תיקון מס' 5; על דירה כאמור יחולו הוראות חוק המכר (דירות), התשל"ג-1973, כנוסחו ערב יום התחילה של תיקון מס' 5."

| Condition | Schedule and text |
|---|---|
| Sale contract concluded on or after 06.04.2011 AND construction of the building did not finish before that date | Current |
| Sale contract concluded before 06.04.2011 | Pre-2011 |
| Contract after the split but construction of the building finished before it | Pre-2011 |

Note what s.11(c) actually carries over: the WHOLE law as worded on the eve of Amendment 5, not only the old Schedule. See "Pre-2011 apartments run on the pre-2011 text" below.

The periods attach to the apartment, not to the owner: a pre-2011 apartment keeps the pre-2011 periods even if it was sold on afterwards. Whether a sub-buyer of such an apartment can rely on the old text at all is an advocate question (see below); if they can, it is the older, shorter table.

## Current Schedule (contract on/after 06.04.2011)

The clock starts at handover of possession, in the statute's words "בעת העמדת הדירה לרשות הקונה".

| # | Defect row | Bedek | Warranty ends at | Script key |
|---|---|---|---|---|
| 1 | מסגרות ונגרות, incl. aluminium and plastic | 2 yr | 5 yr | `frames` |
| 2 | ריצוף וחיפוי פנים, incl. subsidence and wear | 2 yr | 5 yr | `flooring` |
| 3 | מכונות ודוודים, function and durability | 3 yr | 6 yr | `machines` |
| 4 | פיתוח חצר, EXPRESSLY including שקיעות "בין השאר של מרצפות בקומת קרקע, בחניות, במדרכות ובשבילים בשטח הבניין", finish-material surfaces, and the yard's water, sewage, drainage, electricity, lighting and communications systems | 3 yr | 6 yr | `yard` |
| 5 | בידוד תרמי components | 3 yr | 6 yr | `thermal` |
| 6 | צנרת, incl. water, heating, gutters, waste and sewage. "כשל" expressly includes leaks | 4 yr | 7 yr | `pipes` |
| 7 | איטום המבנה, incl. underground spaces, walls, ceilings and roofs, "לרבות גגות קלים עם סיכוך" | 4 yr | 7 yr | `sealing` |
| 8 | סדקים wider than 1.5 mm in NON-load-bearing elements | 5 yr | 8 yr | `cracks` |
| 9 | חיפויי חוץ, detachment, peeling or crumbling | 7 yr | 10 yr | `cladding` |
| 10 | Any other non-conformity that is not fundamental | 1 yr | 4 yr | `other` |

**Sunken floor tiles are row 4, not row 2.** The statute puts שקיעת מרצפות on the ground floor, in parking, on pavements and on paths inside item (4) פיתוח חצר at THREE years, not inside item (2) ריצוף וחיפוי פנים at two. Routing them to row 2 understates the buyer's window by a year at each stage. The pre-2011 table gave these their own rows (`floor_ground`, `floor_outdoor`); under the current Schedule the script accepts those keys and redirects them to `yard`.

## Pre-2011 Schedule

**Source.** The consolidated statute shows only the CURRENT Schedule. The rows below were checked against the primary text, the Schedule as enacted by תיקון מס' 3, התש"ן-1990 (ספר החוקים 1327, 2.8.1990, p.185), read from the Knesset PDF image, and they match Kol Zchut row for row.

Different rows, and several materially shorter periods.

| Defect row | Bedek | Warranty ends at | Script key |
|---|---|---|---|
| צנרת incl. heating and gutters | 2 yr | 5 yr | `pipes` |
| חדירת רטיבות in roof, walls, shelter | 3 yr | 6 yr | `damp` |
| מכונות, מנועים ודוודים | 3 yr | 6 yr | `machines` |
| קילוף חיפויים in stairwells | 3 yr | 6 yr | `stairwell` |
| שקיעת מרצפות on the ground floor | 3 yr | 6 yr | `floor_ground` |
| שקיעת מרצפות in parking, pavements, paths | 3 yr | 6 yr | `floor_outdoor` |
| סדקים עוברים in walls and ceilings | 5 yr | 8 yr | `cracks` |
| קילופים ניכרים in exterior cladding | 7 yr | 10 yr | `cladding` |
| Any other non-fundamental non-conformity | 1 yr | 4 yr | `other` |

## Pre-2011 apartments run on the pre-2011 text

Amendment 5 did far more than replace the Schedule. Its own amending instructions quote the 1990 wording they replace, which shows that text was in force on the eve of 2011, and s.11(c) applies exactly that text to a pre-2011 apartment. For such an apartment:

| Provision | Current law | Pre-2011 text |
|---|---|---|
| Fundamental (load-bearing) non-conformity | 20 years with the burden on the seller, then actionable if the buyer proves origin (s.4(a)(4)-(5)) | No 20-year period. Old s.4(a)(4): "התגלתה, אף לאחר תקופת האחריות, אי-התאמה יסודית שבגללה אין הדירה מתאימה ליעודה" |
| Hidden fundamental defect, notice | Own limb, s.4a(b) | No s.4a(b). A defect that could not be found by reasonable inspection at handover falls under s.4a(a)(2), reasonable time after discovery |
| Self-repair at the seller's expense | Two gateways, s.4b(b) | No s.4b(b). Only the duty to give a proper opportunity to repair |
| Waiver | s.7A(a) no contracting out; s.7A(b) waiver as a condition void | s.7A(a) only: "אין להתנות על הוראות חוק זה, אלא לטובת הקונה" |
| Sub-buyer (קונה משנה) | Named throughout | Not named. Whether a sub-buyer can rely on the old text is a question for an advocate |
| Maintenance instructions | Failure to deliver them is a breach, s.4(a)(6), and s.2 requires them to be attached to the contract | Old s.4(a)(5): a breach where the circumstances required warnings or maintenance and use instructions and none were given |
| No compliant specification, s.5 | Seller must prove the item is of high quality ("באיכות גבוהה") | Seller must prove the item is suitable to what is customary ("מתאים למקובל בנסיבות העניין") |

The Schedule-period burdens (s.4(a)(2) and (3)) and the one-year notice limb read the same in both texts. So the practical rule: the period arithmetic for a pre-2011 apartment changes only through the old Schedule, but every statement about the 20-year regime, s.4a(b), s.4b(b), s.7A(b) and the sub-buyer must be dropped or replaced for that buyer.

Apartments whose contract or building predates Amendment 3 itself (02.08.1990) are under the law as worded before 1990 (s.11(b)). That case is practically moot; route it to an advocate.

## The route that bypasses the Schedule entirely

Before working out which row and which period, check s.4(א)(1). The seller has not performed if:

> "הדירה או כל דבר שבה (להלן - הדירה) שונים מן האמור במפרט, בתקן רשמי או בתקנות הבניה"

A deviation from the מפרט, from an official standard, or from the building regulations is a breach in its own right. It is not tied to a Schedule row or a bedek period, but the buyer must still prove the deviation, normally with an engineer. It does NOT escape s.4a: s.4(b) deems it an אי-התאמה, so the notice clocks run on it exactly as on any other defect. So when a Schedule window has closed, do not stop: ask whether the apartment actually matches the specification and the standards. The Registrar of Contractors lists "אי-ביצוע מה שהובטח במפרט הטכני" as its own complaint category.

## The two periods and who proves what

The warranty period is three years starting at the END of that row's bedek period, so the "warranty ends at" column above is the bedek period plus three, measured from handover.

| Stage | Rule | Burden |
|---|---|---|
| Bedek | The contractor must repair | On the CONTRACTOR, to prove the buyer caused the defect (s.4(a)(2)) |
| Warranty | The contractor must repair only if origin is shown | On the BUYER, to prove origin in planning, workmanship or materials (s.4(a)(3)) |

The practical consequence: inside the bedek period a buyer can often succeed with photographs and a letter. Once the warranty period starts, they generally need a licensed engineer's opinion, because they now have to prove causation.

## Load-bearing defects, the separate regime (current law)

For a pre-2011 apartment none of this section applies; see the table above.

"אי-התאמה יסודית" is defined as a non-conformity in the parts of the building that carry and transfer loads to the ground and that concerns the building's stability and safety.

- Discovered within 20 years of handover: the burden is on the CONTRACTOR to prove the buyer caused it (s.4(a)(4)).
- Discovered after 20 years: still actionable where the BUYER proves origin in planning, workmanship or materials (s.4(a)(5)). There is no absolute cut-off. Note the drafting: limbs (2), (3) and (4) say "הקונה או קונה המשנה" while limb (5) says only "הקונה", so whether a sub-buyer can rely on it past 20 years is an open question for an advocate, not one to answer here.

This skill must not decide whether a defect belongs in this category, in either direction. That classification is a licensed engineer's professional judgment and it carries a safety risk.

## Notice duties, a second and independent clock

| Situation | Deadline |
|---|---|
| The defect COULD have been discovered at handover | Notice to the contractor within ONE YEAR of handover (s.4a(a)(1)) |
| The defect could NOT have been found by reasonable inspection at handover, for example internal piping | Notice within a reasonable time after discovering it, even if more than a year has passed since handover (s.4a(a)(2)) |
| An אי-התאמה יסודית (load-bearing) that could not have been found by reasonable inspection at handover | Notice within a reasonable time after discovering it. s.4a(b) is a SEPARATE limb with NO one-year cut-off (current law; under the pre-2011 text the same defect falls under s.4a(a)(2)) |
| The contractor KNEW or ought to have known of the facts and did not disclose them | The notice bar falls away. s.4(b) deems these non-conformities to be אי-התאמה under the Sale Law 1968, and s.16 of that Act ("העלמת אי-התאמה") lets the buyer rely on it despite ss.14-15 or any agreement, provided notice was given immediately on discovery |

s.4a has THREE limbs, not two. The third matters most in the worst cases: never tell a user whose defect may be load-bearing that a missed one-year deadline ends the matter, because s.4a(b) does not impose one. Verbatim:

> "הקונה או קונה המשנה יהיה זכאי להסתמך על אי-התאמה יסודית שלא היה ניתן לגלותה בבדיקה סבירה בעת העמדת הדירה לרשותו, אם הודיע עליה למוכר בתוך זמן סביר לאחר שגילה אותה"

Concealment is the other answer to a missed deadline, and it is the strongest one a buyer usually has. s.16 of חוק המכר, התשכ"ח-1968, imported by s.4(b):

> "היתה אי־ההתאמה נובעת מעובדות שהמוכר ידע או היה עליו לדעת עליהן בעת גמירת החוזה ולא גילה אותן לקונה, זכאי הקונה להסתמך עליה על אף האמור בסעיפים 14 ו־15 או בכל הסכם, ובלבד שנתן למוכר הודעה עליה מיד לאחר שגילה אותה"

So never present a missed one-year deadline as the end of the matter. Ask whether the contractor papered over something it knew about, and route that to an advocate.

Both the notice duty and the defect period must be satisfied. A defect well inside its bedek period can still fail if a reasonable inspection would have found it on handover day and nobody wrote to the contractor within the year.

Send notice in writing by a method that proves delivery and keep the proof. Date everything.

## Waiver, and what a signature really does

- s.7A(a): the law cannot be contracted out of, except in the buyer's favour. A contract clause shortening a bedek period is ineffective.
- s.7A(b): a waiver, including a written one, of defect or late-delivery rights that is made a CONDITION of handover, of carrying out repairs, or of transferring rights, is void. The defect limb was added by Amendment 5, so it applies only to apartments under the current law. The late-delivery limb was added by Amendment 9 and reaches contracts concluded from 07.07.2022.
- Kol Zchut states the position plainly: liability cannot be waived, cancelled or reduced even where the buyer agreed, and the scope may be varied only in the buyer's favour. That covers the common "we gave you a discount, you signed away the defects" scenario, where a price concession at signing or handover is traded for contracting out of the law (s.7A(a)). A compromise of a concrete, known dispute AFTER handover is a different question, see "Settlement offers after handover" below.

So a signature does not extinguish liability. What it can do is evidential: a signed statement that the apartment was received with no comments is a factual admission about the apartment's condition on that day, and a court will weigh it. The protection is to record reservations rather than to refuse to sign.

### Settlement offers after handover

s.7A(b) is tied to three conditions: handover, carrying out repairs, transfer of rights. A settlement the buyer signs freely AFTER handover, for payment, to close defects they already know about is not one of those, and may bind them for what it covers. So:

- Never tell a user a settlement is "void anyway".
- If the contractor makes the remaining repairs conditional on signing, that IS the s.7A(b) case for an apartment under the current law. A pre-2011 apartment has no s.7A(b); route that situation to an advocate.
- Before signing, the user should know what the sum is traded against (an engineer's repair estimate), the release should list the defects it covers, and it should not release hidden defects found later, the load-bearing regime, or common property.
- A release for money has lasting legal effect. Route it to an advocate before signing. Do not draft or approve settlement wording.

Two further contractor obligations worth raising:

- s.2(a) and (a1) require a specification (מפרט) and maintenance and use instructions, attached to the contract at signing (the maintenance-instructions duty and s.2(a1) came with Amendment 5). Under s.5(c), where no compliant specification was given, the burden of proving the item was of high quality falls on the SELLER. For a pre-2011 apartment the standard the seller must prove is the older one, that the item was suitable to what is customary in the circumstances ("מתאים למקובל בנסיבות העניין"); Amendment 5 replaced it with "באיכות גבוהה".
- s.4(a)(6) makes failure to deliver maintenance and use instructions a breach in its own right (current law; the pre-2011 equivalent is old s.4(a)(5), see above).

## The right to repair, and the only two routes to self-help

s.4b(a): where a defect is repairable, the buyer must give the contractor a proper opportunity to repair, and the contractor must repair within a reasonable time.

s.4b(b): the buyer may repair at the contractor's expense only where one of these holds:

1. the defect recurred after the contractor repaired it once or more, within two years starting from the buyer's notice, or
2. the repair is urgent and the contractor did not carry it out within a reasonable time of the notice.

These gateways exist only under the current law (s.4b(b) was added by Amendment 5).

What happens when the buyer repairs, or sues, WITHOUT first giving the contractor a proper opportunity to repair was held by the Supreme Court in August 2026 (Justice Alex Stein, Justices Mintz and Wilner concurring, buyers against שמי אשקלוני, reversing the Tel Aviv District Court and restoring the Bat Yam Magistrates' Court), as reported by Bizportal on 18.08.2026 (https://www.bizportal.co.il/takdin/news/article/20039450): the claim is NOT forfeited, but compensation is limited to what the repair would have cost the seller, not the market price of an outside contractor. In that case the gap was about 20%, and the court said it could reach far more. Full denial is reserved for extreme bad faith that deliberately frustrated the repair; at the other edge, a deep breakdown of trust may justify refusing the contractor's repair. The judgment itself was not read and its case number was not verified, so do not cite one, and check the judgment before relying on any detail beyond the core holding. The holding concerns a buyer who gave NO proper opportunity, in a claim filed during the bedek period. Where the contractor WAS given a proper opportunity and let it pass, the reduction does not apply on its face; what the buyer then recovers is a question for an advocate.

> "הפיצוי שייפסק לטובתו יהא מוגבל לעלות התיקון למוכר הדירה - סכום שנופל באופן משמעותי ממחיר השוק"

So the advice is unchanged (give the opportunity first, in writing) but the stated consequence is a reduced award, never "you lose". Track repair attempts and dates, because gateway 1 is a counting exercise nobody performs unless told to.

## Escalation routes

| Route | Cost | Gives | Limits |
|---|---|---|---|
| Written demand to the contractor | None | The statutory opportunity to repair under s.4b(a), and the evidence every later route rests on | Not itself a remedy. Always do it first |
| Registrar of Contractors, Ministry of Construction and Housing | None | Disciplinary pressure on a registered contractor | Disciplinary only. Does not arbitrate, does not resolve the dispute, does not handle monetary disputes, does not touch matters already in court. Contractor must be in the register |
| Civil claim | Court fees, advocate, engineer | Money and enforceable orders | Reserved work: needs an advocate, and in practice an engineer's opinion |

### What the Registrar route does and does not require

Correcting a widespread misstatement, including in earlier versions of this skill: **a prior written demand to the contractor is NOT a precondition for filing.** The Ministry's own service page states eligibility as "כל אזרח המעוניין להגיש תלונה כנגד קבלן רשום" and imposes no such condition. Prior correspondence appears only as one of six suggested attachments ("העתקים מן ההתכתבות בנושא התלונה בין המתלונן לבין הקבלן"). Send the demand letter first because it is the statutory opportunity to repair and because it is the best evidence, not because the Registrar will refuse you without it.

Likewise, **an individual owner is not barred from complaining about common property.** The page says a common-property complaint "מומלץ להגיש באמצעות אחד מחברי ועד הבית" - recommended, not required. Route through the house committee where one exists and functions, but never tell a user with no functioning committee that they have no route.

The page also frames the defect track as complaints filed during the bedek period:

> "תלונות שהוגשו במהלך תקופת הבדק בגין עבודות לקויות שביצע קבלן רשום, לפי המפורט בתיקון לחוק המכר (דירות) (תיקון מס' 3), התש"ן-1990, או לפי תקופת הבדק הקבועה בהסכם המכר או בפסק דין חלוט שלפיו הקבלן עבר על הנוהג המקובל."

A warranty-stage defect may therefore fall outside the Registrar's defect track; the civil routes remain.

Verbatim scope limits from the same page:

> "הטיפול בתלונה נעשה במישור המשמעתי" / "אין לראות בטיפול בתלונה הליך של בוררות, והרשם אינו מכריע במחלוקות בין הצדדים בחוזה" / "הרשם אינו מטפל במחלוקות כספיות בין בעל הנכס לבין הקבלן" / "הרשם אינו מטפל בתלונות שעבורן הוגשו תביעות שנידונות בבתי המשפט"

Service page: https://www.gov.il/he/service/complaint-about-constractor

s.7 preserves every other right the buyer has under any other law, so the statute is a floor and not a ceiling.

Filing address for the Registrar complaint: https://govforms.gov.il/mw/forms/complaint-about-contractor@moch.gov.il

## Limitation is a THIRD clock, and it must be said out loud

The bedek and warranty windows say when a defect is covered. They do not say how long the buyer has to SUE. The general limitation regime (התיישנות) runs separately and can bite well before a warranty end-date. Whenever the skill reports an end-date years out, it must say that this is the cover period and not a deadline to file, and that the time limit for suing is a question for an advocate. Reporting "protected until 2028" without that sentence is the same two-clocks error this file spends a whole section warning about.

## Adjacent matters this file deliberately excludes

- Late-delivery compensation under s.5A: a separate money claim with its own formula.
- בטוחות and the Sale Law Supervisor: protects the buyer's payments against contractor insolvency, unrelated to defects.
- התיישנות: see the warning above. Excluded here only as to the calculation; it must still be surfaced to the user whenever a window end-date is reported.
