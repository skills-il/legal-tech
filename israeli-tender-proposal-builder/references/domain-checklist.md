# Domain Coverage Checklist - Israeli Tender Proposal Builder

Canonical coverage contract for a skill that builds proposal packages for Israeli public-sector tenders (michrazim) governed by the Mandatory Tenders Law and its regulations. This is the reviewer's yardstick: a competent build must cover every Must item; Should items are expected in a mature build; Out-of-scope items must be deflected, not attempted.

Scope boundary: supply, services, works, and framework tenders subject to חוק חובת המכרזים, התשנ"ב-1992 and its regulations. NOT land-allocation tenders (RMI), NOT bid-protest litigation, NOT private RFPs.

---

## Must (a defect here can disqualify a bid or mislead the bidder)

1. **Identify the governing statute and confirm the issuer is a covered body.** The law binds the State, government ministries, statutory corporations, government companies, and health funds; local authorities run on a parallel municipal regime; private bodies are not bound. Getting this wrong applies the wrong rulebook. [חוק חובת המכרזים התשנ"ב-1992; kolzchut overview]

2. **Classify the tender track: open (פומבי) vs closed/zuta (זוטא/מוגבל) vs framework (מסגרת) vs exemption (פטור ממכרז).** The track changes who may bid and what process applies. The regulations enumerate ~30 exemption cases. [תקנות חובת המכרזים, תשנ"ג-1993, תקנה 3 ואילך]

3. **Treat current monetary thresholds as unverified.** The open/zuta split and the mandatory-tender floor are under active reform (devolution of exemption authority, a reported rise in the floor). The skill must refuse to classify from a remembered number and route the user to verify against the regulations / mr.gov.il. [תקנות חובת המכרזים; מינהל הרכש הממשלתי]

4. **Extract threshold conditions (תנאי סף) verbatim and split them into Takana 6(a) statutory vs 6(b) discretionary.** Statutory conditions cannot be waived; discretionary ones are set per tender. Failing any one disqualifies before the price envelope opens. Paraphrasing the wording is itself a disqualification risk. [תקנות חובת המכרזים, תשנ"ג-1993, תקנה 6]

5. **Enumerate the 6(a) statutory bucket:** registration in every legally required registry, valid statutory licenses, compliance with applicable official Israeli standards, and the certificates/declarations under חוק עסקאות גופים ציבוריים. [תקנה 6(א); חוק עסקאות גופים ציבוריים התשל"ו-1976]

6. **Cover the workers'-rights / fair-employment declaration regime for labor-intensive contracts.** A written declaration by the bidder and its related parties on compliance with workers'-rights obligations, plus the minimum-wage / foreign-workers no-conviction declaration under the Public Bodies Transactions Law. [תקנה 6(א)(4); חוק עסקאות גופים ציבוריים, סעיף 2ב]

7. **Explain בעלי זיקה (related/affiliated parties).** Statutory declarations and threshold tests reach controlling shareholders and affiliated companies, not just the bidding entity. The bidder must map its corporate structure or a clean entity-level filing is still defective. [חוק עסקאות גופים ציבוריים, הגדרת "בעל זיקה"]

8. **Assemble the mandatory declarations (תצהירים) block** and state the formal validity requirements: a תצהיר must be sworn before a lawyer (or other authorized person) with the criminal-liability warning and a completed verification block, must be dated on or before the submission deadline, must copy the tender's template verbatim, and must be signed by the correct authorized signatory. A merely-signed, undated, or post-dated affidavit is defective. [תקנה 6; פקודת הראיות (נוסח חדש), סעיף 15; tender annexes]

9. **Cover the bid guarantee (ערבות מכרז / ערבות הצעה) as a disqualification trap:** correct amount, autonomous bank guarantee (ערבות בנקאית אוטונומית) callable on demand, validity through the required date (commonly submission + 90 days), and template-exact wording (right beneficiary, tender number, indexation clause). Israeli case law treats even minor deviations as grounds for disqualification. [פסיקת בתי המשפט המנהליים; tender guarantee annex]

10. **Cover the performance / execution guarantee (ערבות ביצוע) the winner must post on award**, and distinguish it from the bid guarantee. The bid guarantee secures the offer; the performance guarantee (typically a higher percentage of the contract value, sometimes with a separate warranty/maintenance guarantee, ערבות טיב/בדק) secures performance and is a condition of contract signature, not of bid submission. A skill that conflates the two, or omits the performance guarantee, leaves the winner unprepared to close. [tender contract annex; standard government contract terms]

11. **Cover the three statutory preference regimes correctly and keep them distinct in mechanism:**
   - **Israeli-product preference (העדפת תוצרת הארץ), 5755-1995** - a *price* preference for goods: an Israeli-made offer wins the price criterion if its price is not more than 15% above the imported offer; the committee divides the Israeli price by 1.15 for the comparison. Note the separate national-priority-area preference may stack. [תקנות חובת המכרזים (העדפת תוצרת הארץ), תשנ"ה-1995]
   - **Women-controlled business (עסק בשליטת אישה), Amendment 15 / Section 2B, 2002** - an *identical-score tie-breaker*, not a price discount; requires an accountant's certificate plus the controlling woman's affidavit attached to the bid. [תיקון 15 לחוק חובת המכרזים, סעיף 2ב]
   - **Active-reserve-service business (עסק בשליטת משרת מילואים פעיל), Amendment 26** - a parallel identical-score tie-breaker; eligibility is ≥50% control by an active reserve servicemember who served ≥20 days in the prior 12 months; declared within the bid; approved 5 Nov 2024, not retroactive. The interaction order between the two tie-breakers is unresolved and must be flagged, not guessed. [תיקון 26 לחוק חובת המכרזים]

12. **Match the proposal's section order and numbering to the tender document**, and never add or remove line items from the supplied price template. Mismatched numbering and altered price templates are common disqualification grounds. [tender structural requirements]

13. **Handle two-envelope (דו-מעטפתי) tenders:** qualifications/quality in one sealed envelope, price in a separate sealed envelope; any price leak into the qualifications envelope is automatic disqualification. [tender submission rules]

14. **Pricing arithmetic must reconcile to the agora** across every line, subtotal, VAT line, and grand total; a one-shekel mismatch has been used as a disqualification ground. [pricing-worksheet discipline]

15. **Treat published clarification answers (תשובות הבהרה) as binding amendments** to the tender document; any draft built from the original text alone is stale and must be re-reconciled before submission. [tender clarification procedure]

16. **Identify the submission path: physical tender box vs the digital tender box** (מינהל הרכש הממשלתי portal mr.gov.il, the Yahalom/יהלום system on the Merkava/מרכבה platform), including early portal registration and whether a scanned wet-ink affidavit suffices or a qualified e-signature certificate is mandatory. Late is late regardless of path. [מינהל הרכש הממשלתי; tender submission instructions]

---

## Should (expected in a mature build; absence is a quality gap, not a fatal flaw)

1. **Quality-vs-price evaluation methodology (אמות מידה / מדד איכות).** Explain that many tenders score on a weighted quality-and-price formula (e.g. 70/30, 60/40), that the bidder should map every professional requirement to a scored criterion, and how the price score is computed relative to the lowest/benchmark offer. [tender evaluation chapter]

2. **Past-experience table discipline.** One row per genuinely matching contract (client, subject, value in NIS, period, reference contact); padding with non-matching entries is a red flag and risks the experience threshold being read narrowly. [תקנה 6(ב) ניסיון]

3. **Mandatory site visit / contractors' tour (סיור קבלנים/מציעים).** When the tender makes the tour a precondition, non-attendance is itself a disqualification; record every statement and preserve the minutes. [tender procedural conditions]

4. **Clarification-question discipline.** Submit in writing, in the required format, by the deadline; do not rely on verbal answers. [tender clarification procedure]

5. **Conflict-of-interest and no-prior-convictions declarations** (ניגוד עניינים, היעדר הרשעות) and corporate signing-authority certification (אישור עו"ד/רו"ח על זכויות חתימה). [tender annexes; administrative-law principles]

6. **Tender-specific declarations:** confidentiality, privacy/data-protection (חוק הגנת הפרטיות), subcontractor disclosure, and the insurance undertaking (התחייבות לקיום ביטוחים / נספח ביטוח). [tender annexes; חוק הגנת הפרטיות התשמ"א-1981]

7. **Local-authority regime differences.** Flag that municipal tenders run under תקנות העיריות (מכרזים) / פקודת העיריות with different thresholds, templates, committees, and challenge channels. [פקודת העיריות; תקנות העיריות (מכרזים)]

8. **Price-intelligence framing.** Benchmark historical contracts (BudgetKey / IL Budget) as intelligence only; never tell the bidder a number, to avoid any appearance of price coordination. [BudgetKey / OpenBudget data]

9. **Validity/extension of the offer and guarantees on committee request** (הארכת תוקף ההצעה והערבות), since committees routinely request extensions and a lapsed guarantee mid-process disqualifies. [tender terms]

---

## Out of scope (the skill must deflect, not attempt)

1. **RMI / Israel Land Authority land-allocation tenders** - route to `israeli-land-tenders`. [skill boundary]
2. **Bid protests / petitions to the tenders committee or administrative court** (השגה/עתירה מנהלית) - route to an administrative-law attorney. [skill boundary]
3. **Private commercial RFPs** not subject to the Mandatory Tenders Law. [skill boundary]
4. **Telling the bidder a specific price to submit** - price coordination / collusion risk. [competition-law hygiene]
5. **Drafting original declaration text from scratch** - templates come from the tender pack; if missing, stop and tell the user. [tender annex dependency]

---

## Authoritative sources

| Source | URL | Used for |
|--------|-----|----------|
| חוק חובת המכרזים, התשנ"ב-1992 | https://www.nevo.co.il/law_html/law01/151_001.htm | Covered bodies, preference sections (2ב), amendment framework |
| תקנות חובת המכרזים, תשנ"ג-1993 (Nevo) | https://www.nevo.co.il/law_html/law01/242_002.htm | Takana 6 threshold conditions, tender tracks, exemptions |
| תקנות חובת המכרזים (העדפת תוצרת הארץ), תשנ"ה-1995 (Nevo) | https://www.nevo.co.il/law_html/law00/72502.htm | Israeli-product 15% price-preference mechanism |
| חוק עסקאות גופים ציבוריים, התשל"ו-1976 | https://www.nevo.co.il/law_html/law01/055_001.htm | Bookkeeping/withholding certificate, fair-employment declaration, בעלי זיקה |
| חוק חובת המכרזים (כל זכות) | https://www.kolzchut.org.il/he/חוק_חובת_המכרזים | Plain-language scope, covered bodies, Takana 6 |
| תיקון 15 / סעיף 2ב - עסק בשליטת אישה | https://www.michrazim-law.co.il/woman-controlled-business-preference/ | Women-controlled tie-breaker + affidavit/certificate |
| תיקון 26 - עסק בשליטת משרת מילואים (SFA) | https://www.sfa.law/עדכון-לקוחות-תיקון-מס-26-לחוק-חובת-מכרזי/ | Reserve-service tie-breaker: 50% / 20 days / 5.11.2024 |
| מינהל הרכש הממשלתי | https://www.mr.gov.il/ | Yahalom digital tender box, current thresholds |
| פקודת העיריות / תקנות העיריות (מכרזים) | https://www.nevo.co.il/law_html/law01/P182_001.htm | Local-authority parallel regime |
| מכרז - ויקיפדיה | https://he.wikipedia.org/wiki/מכרז | Overview of scope and covered bodies |
