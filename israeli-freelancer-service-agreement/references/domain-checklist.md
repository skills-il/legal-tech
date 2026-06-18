# Domain Coverage Checklist - Israeli Freelancer Service Agreement

Generated: 2026-06-18. Scope: an agent skill that DRAFTS a service/contractor agreement
(הסכם למתן שירותים / הסכם קבלן עצמאי) from the independent service provider's (עצמאי) side
under Israeli law. This is NOT an employment contract. Source URLs with Hebrew slugs are kept
as plain source names here and as full links in `evidence.json` (to avoid breaking automated
checks); ASCII statute/case URLs are linked directly.

## Must cover (core)

- [ ] Employee-vs-contractor distinction + retroactive reclassification risk. Israeli labor
  courts ignore the contract label and apply the מבחן מעורב (mixed test), dominated by the
  מבחן ההשתלבות (integration test). A "contractor" can be recognized retroactively as an
  employee (הכרה בדיעבד) and claim severance, pension, vacation, sick days, holidays, הבראה.
  Source: כל-זכות, "קביעת קיומם של יחסי עובד-מעסיק" + "הכרה בדיעבד בזכויות עובד שהועסק כעצמאי".
  Why core: the single biggest legal exposure a freelancer service agreement must manage.
- [ ] Independent-contractor declaration + "no employer-employee relationship" + restitution/
  set-off clause (הצהרת קבלן עצמאי). The provider declares it bears its own tax/Bituach
  Leumi/pension; if a court later finds employment, the fee is treated as gross-inclusive and
  the excess is set off. Courts give such clauses evidential weight only (case אורי אייזיק,
  ע"ע 300256/98). Why core: the central protective mechanism, but must be presented honestly.
- [ ] Scope of services + consideration & payment terms under חוק מוסר תשלומים לספקים 2017.
  Statutory default when silent: שוטף+45 (no later than 45 days from end of the invoice month);
  late payment carries interest + דמי פיגורים. Source:
  [nevo statute](https://www.nevo.co.il/law_html/law00/144599.htm). Why core: late payment is
  the #1 freelancer pain point; the contract should set an explicit (shorter) term.
- [ ] IP ownership of work product (יצירה מוזמנת). Under חוק זכות יוצרים 2007 the default first
  owner of a commissioned work is the CREATOR (the freelancer), not the client, unless agreed
  otherwise. Assignment to the client must be express. Source:
  [nevo statute](https://www.nevo.co.il/law_html/law00/3953.htm). Why core: clients routinely
  assume they own deliverables by default; the law says the opposite for contractors.
- [ ] Tax & invoicing context (עוסק פטור / עוסק מורשה, מע"מ, חשבונית). עוסק פטור turnover cap
  is 122,833 ₪ (2026); VAT rate is 18% (from 1 Jan 2025). The price clause must state whether
  it is +VAT. Source: כל-זכות "עוסק פטור" +
  [gov.il VAT decision](https://www.gov.il/he/pages/dec1270-2024). Why core: a wrong VAT
  assumption is a direct financial error in the price clause.
- [ ] Term, termination & notice. Fixed vs at-will, termination for convenience vs breach,
  notice period, effect on accrued fees/work-in-progress. Why core: a complete agreement, and
  an over-long employee-like notice regime is itself a reclassification red flag.
- [ ] Confidentiality (סודיות). Mutual or one-way NDA, survives termination; also anchors the
  legitimate-interest basis for any restraint clause. Why core: standard, expected clause.
- [ ] Withholding tax (ניכוי מס במקור) + certificates. The client may be legally required to withhold
  tax unless the freelancer furnishes a valid אישור ניהול ספרים and ניכוי-מס certificate. Why core:
  a silent contract means the first payment arrives net of withholding and the freelancer is
  surprised. Source: Income Tax withholding regime (background, not a rate).
- [ ] Moral rights (הזכות המוסרית) handled separately from the IP assignment. They are non-assignable
  under the 2007 Copyright Law; assigning "all rights including moral rights" is partly void. Why core:
  a complete IP transfer is otherwise legally incomplete.
- [ ] Acceptance / sign-off + effect of termination on accrued fees + kill fee. Deemed-acceptance
  window, revision rounds, pro-rata payment on termination, and a cancellation fee for a fixed-price
  project. Why core: "what is done" and "what am I owed if cancelled" are the top freelancer disputes.

## Should cover (advanced / edge cases)

- [ ] Non-compete / restraint of trade (אי-תחרות). A bare non-compete is generally NOT
  enforceable in Israel; enforced only for a legitimate interest (chiefly a trade secret) and
  reasonable scope/time/geography (case צ'ק פוינט נ' רדגארד, ע"ע 164/99). Default to a narrow
  trade-secret / non-solicitation clause. Source:
  [afiklaw case summary](https://he.afiklaw.com/caselaw/2573).
- [ ] Liability cap & MUTUAL indemnity. Cap (e.g. fees paid), carve-outs (willful misconduct, IP
  infringement, confidentiality breach), and a client-side indemnity (client-supplied materials,
  client misuse of deliverables), not a one-way cap that only protects the client.
- [ ] Data protection under Amendment 13 (תיקון 13, in force Aug 2025). When the freelancer processes
  the client's personal data, a processor clause with security obligations and breach notification.
- [ ] Public-body payment default. Government / public-body clients carry their own payment-timing
  default and caps under חוק מוסר תשלומים; do not assume שוטף+45 for them.
- [ ] Professional liability insurance (ביטוח אחריות מקצועית). Often a precondition when serving
  companies/public bodies. Source:
  [bizreviews guide](https://www.bizreviews.co.il/article/professional-liability-insurance-guide).
- [ ] Force majeure (כוח עליון); governing law & jurisdiction (note: classification disputes go
  to the labor courts regardless of a forum clause).
- [ ] Anti-reclassification operational hygiene (guidance, not a clause): own tools, own hours,
  no company email, may serve other clients, no exclusivity, invoice per deliverable.

## Out of scope (explicit, with rationale)

- Employment contracts / employee-benefit drafting - opposite legal regime. Related skill:
  `israeli-employment-contracts` handles it.
- Reviewing a contract the user is about to sign - related skill:
  `israeli-employment-contract-reviewer`.
- Personalized tax filing / computing exact VAT or income-tax liability - requires a licensed
  רואה חשבון; the skill states rates as context only.
- Litigating an existing reclassification claim or computing restitution amounts - labor-court
  work for a lawyer.
- Company formation, shareholder agreements, cross-border / non-Israeli governing law, and B2C
  consumer contracts - separate regimes.

## Authoritative sources

- [חוק זכות יוצרים 2007 (nevo)](https://www.nevo.co.il/law_html/law00/3953.htm) - IP default for commissioned works.
- [חוק מוסר תשלומים לספקים 2017 (nevo)](https://www.nevo.co.il/law_html/law00/144599.htm) - payment-timing default.
- [gov.il - VAT to 18% from 1 Jan 2025](https://www.gov.il/he/pages/dec1270-2024) - current VAT rate.
- [ע"ע 164/99 צ'ק פוינט נ' רדגארד (afiklaw)](https://he.afiklaw.com/caselaw/2573) - non-compete standard.
- כל-זכות - "עוסק פטור", "קביעת קיומם של יחסי עובד-מעסיק", "הכרה בדיעבד" (full links in evidence.json).
