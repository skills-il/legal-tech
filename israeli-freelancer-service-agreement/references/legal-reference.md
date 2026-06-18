# Legal Reference - Israeli Freelancer Service Agreement

This reference grounds each clause of the generated agreement in Israeli statute and case law.
It is background for drafting, not legal advice. For ASCII statute links, see the table at the
bottom; Hebrew-slug source pages are named in prose.

## 1. The core risk: employee-vs-contractor reclassification

Israeli labor courts do not treat the words "independent contractor" in a contract as decisive.
They apply the **מבחן מעורב (mixed test)**, whose dominant component is the **מבחן ההשתלבות
(integration test)**: is the provider an integral part of the client's organization, or a
genuinely separate business? Secondary factors: who controls the work and hours, whether the
provider supplies its own tools, personal-performance requirement, exclusivity, and economic
dependence on the single client.

If the relationship looks like employment, a worker hired as a "contractor" can sue for
**retroactive recognition (הכרה בדיעבד)**. On recognition the worker is owed employee social
rights: severance pay, pension contributions, vacation, sick leave, holidays, and recuperation
allowance (הבראה). The contractual label is evidential, not determinative.

The leading case is **ע"ע 300256/98 אורי אייזיק נ' תה"ל**, which set the framework for both
retroactive recognition and the **restitution / set-off (קיזוז)** of the extra "contractor
premium" the worker was paid above a comparable employee wage. Restitution is allowed only in
narrow circumstances (for example, the fee was markedly higher than an employee wage AND the
contract expressly provided for set-off, or the worker insisted on עצמאי status).

Important framing: a set-off / gross-up clause **protects the client, not the freelancer**. It is
the client's mechanism to claw back the contractor premium if the relationship is reclassified, it
is enforced only in those narrow cases, and a court is not bound to honor it. It also cannot waive
non-waivable (cogent) labor rights such as severance or annual leave. So the clause should be
explained honestly, not presented to the freelancer as their protection.

Drafting implication: the freelancer's real protection against a surprise reclassification is the
**facts**, not the wording. Include an honest independent-contractor declaration (evidential only),
and pair it with operational hygiene (own tools, own hours, no company email, freedom to serve
other clients, no exclusivity, invoicing per deliverable, and an express right to use
subcontractors, since a personal-performance requirement is itself an integration-test marker).

## 2. Payment terms: חוק מוסר תשלומים לספקים, התשע"ז-2017

When a business client orders a service and the contract is silent on timing, סעיף 3 imposes a
default of **שוטף+45**: payment no later than 45 days from the end of the month in which the
invoice was submitted. Consideration not paid on time accrues shekel interest, and after a
further 30 days, **דמי פיגורים (late-payment fees)** under חוק פסיקת ריבית והצמדה.

Note: the law sets different defaults by payer type. The general business-to-business default is
the שוטף+45 above, but **government and public-body clients** carry their own (often shorter)
default and the law caps how far the term can be pushed (excessively long terms can be voidable).
For a public-body client, verify the applicable provision rather than assuming שוטף+45.

Drafting implication: the freelancer benefits from setting an explicit, shorter term (for
example שוטף+30 or שוטף+0). State the term explicitly so the statutory maximum is not the
fallback, reference the law so late payment carries interest by default, and reserve the right to
suspend work on non-payment.

### 2a. Withholding tax (ניכוי מס במקור) and certificates

In Israeli B2B practice a client is often legally required to **withhold tax at source** from
payments to a supplier, unless the supplier provides a valid **אישור ניהול ספרים** and an
**אישור פטור / שיעור מופחת מניכוי מס במקור**. A complete agreement therefore states that the
consideration is subject to lawful withholding, that the provider will furnish these certificates,
and that absent valid certificates the client withholds at the statutory rate. Omitting this is a
common, painful surprise: the first payment arrives net of withholding and the contract is silent.
(The skill states the mechanism; it does not compute the user's withholding rate.)

## 3. IP ownership: חוק זכות יוצרים, התשס"ח-2007

The default ownership rule for a **commissioned work (יצירה מוזמנת)** is counter-intuitive for
clients. Under סעיף 35, the first owner of copyright in a commissioned work is the **CREATOR
(the freelancer)**, unless the parties agreed otherwise, expressly or impliedly. Two contrasts:

- סעיף 35 also provides that for a commissioned **portrait or photo of a family/private event**,
  the default owner is the **commissioner** (the opposite default).
- סעיף 34 provides that for a work made by an **employee** in the course of employment, the
  **employer** owns it by default. This is why the contractor case is different: there is no
  automatic transfer to the client.

**Moral rights (הזכות המוסרית)** are separate and **non-assignable**: under the 2007 Copyright Law
the creator's rights of attribution and integrity are personal and cannot be transferred, only
waived in defined circumstances. A clause that assigns "all rights including moral rights" is partly
void; a competent draft separates the assignment of economic rights from a waiver of moral rights.

Drafting implication: if the client is to own the deliverables, the agreement must **expressly
assign** the economic rights (commonly on full payment), add a separate **moral-rights waiver**,
carve out **third-party and open-source components** (which the freelancer can only license, not
assign), and let the freelancer retain rights in pre-existing tools, know-how, and general methods.

## 3a. Data protection: Amendment 13 to the Privacy Protection Law

If the freelancer processes personal data on the client's behalf (a developer touching a user
database, a marketer handling a CRM or mailing list), the Privacy Protection Law and its
**Amendment 13 (in force August 2025)**, together with the information-security regulations, call
for a data-processing clause: the freelancer acts as a holder/processor for the client only, takes
reasonable security measures, notifies the client of a security incident without delay, and returns
or deletes the data at the end of the engagement.

## 4. Tax and invoicing context (background, not tax advice)

- **עוסק פטור** (VAT-exempt dealer): allowed only while annual business turnover does not exceed
  **122,833 ₪ (2026)**. An עוסק פטור does not charge VAT and reports turnover once a year (by
  31 January for the prior year). Above the threshold the provider must register as **עוסק
  מורשה**.
- **מע"מ (VAT)**: the rate is **18%** for transactions whose tax-liability date is on or after
  1 January 2025 (raised from 17%). An עוסק מורשה adds VAT against a חשבונית מס.

Drafting implication: the price clause must state whether the fee is +VAT, and the provider's
status (פטור/מורשה) drives whether VAT is added. The skill states these figures as context; it
does not compute the user's tax liability.

## 5. Non-compete and restraint of trade: ע"ע 164/99 צ'ק פוינט נ' רדגארד

A bare non-compete clause is generally **not enforceable** in Israel. The court enforces a
restraint only where it protects a **legitimate interest**, chiefly a genuine **trade secret
(סוד מסחרי)**, special employer-funded training, special consideration paid for the restriction,
or good-faith/fiduciary duties, AND the restraint is reasonable in scope, duration, and
geography.

Drafting implication: default to a narrow confidentiality + non-solicitation + trade-secret
clause rather than a broad "do not compete" clause that a court will likely strike.

## 6. Liability, indemnity, and insurance

- A **liability cap** (for example, total liability limited to fees paid in the prior 12 months)
  with carve-outs for willful misconduct, IP infringement, and confidentiality breach is
  standard and enforceable by contract freedom.
- **Professional liability insurance (ביטוח אחריות מקצועית)** covers professional negligence,
  errors and omissions, breach of confidentiality, and document loss, including legal costs and
  client compensation. It is frequently a precondition for contracting with companies and public
  bodies, so the agreement may require the provider to carry stated coverage.

## 7. Governing law and forum

Use Israeli law and name a district's courts for general disputes, but note a caveat the skill
should surface: **classification disputes go to the labor courts (בתי הדין לעבודה)** regardless
of a contractual forum clause.

## ASCII source links

| Source | URL | What to check |
|---|---|---|
| חוק זכות יוצרים 2007 | https://www.nevo.co.il/law_html/law00/3953.htm | סעיף 34 (employee) and סעיף 35 (commissioned work) defaults |
| חוק מוסר תשלומים לספקים 2017 | https://www.nevo.co.il/law_html/law00/144599.htm | סעיף 3 default payment period (שוטף+45) and interest |
| חוק מוסר תשלומים (Knesset) | https://main.knesset.gov.il/Activity/Legislation/Laws/pages/lawprimary.aspx?t=lawlaws&st=lawlaws&lawitemid=2016309 | official law page |
| gov.il VAT decision | https://www.gov.il/he/pages/dec1270-2024 | VAT rose to 18% on 1 Jan 2025 |
| ע"ע 164/99 צ'ק פוינט נ' רדגארד | https://he.afiklaw.com/caselaw/2573 | non-compete enforceability standard |
| ביטוח אחריות מקצועית | https://www.bizreviews.co.il/article/professional-liability-insurance-guide | scope of professional liability cover |
