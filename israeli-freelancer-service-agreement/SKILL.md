---
name: israeli-freelancer-service-agreement
description: "Draft a tailored Israeli freelancer service agreement (heskem matan sherutim) between an independent service provider (osek patur or osek murshe) and their client. Covers scope of services, payment terms under the 2017 Prompt Payment to Suppliers Law, the independent-contractor declaration that lowers the risk of a court reclassifying the relationship as employment (yachasei oved-maavid), IP ownership, confidentiality, termination, and indemnity. Use when a freelancer, consultant, designer, or developer needs a written contract before a project, or asks to draft a heskem hitkashrut or contractor agreement. Prevents costly retroactive employee-reclassification and unpaid-invoice disputes. Do NOT use for employment contracts (use israeli-employment-contracts), auditing a contract before signing (use israeli-employment-contract-reviewer), day-to-day invoicing (use israeli-freelancer-ops), or leases (use israeli-rental-agreements)."
license: MIT
compatibility: "Knowledge-only skill, no external tools or network required. Works with Claude Code, Claude.ai, Claude Desktop, Cursor, and other agents. Produces a Hebrew RTL contract draft; legal review by a lawyer is recommended before signing."
---

# Israeli Freelancer Service Agreement

## Problem

Israeli freelancers (עצמאים) routinely start projects on a handshake or a one-line email, then get
burned two ways: a client pays 90 days late with no recourse, or, worse, a long engagement ends with
the "contractor" suing for retroactive recognition as an employee and winning severance, pension, and
back-benefits because the relationship looked like employment. A generic downloaded contract does not
account for Israeli law: the reclassification tests, the default copyright rule that leaves IP with the
freelancer, the statutory payment timing, or the VAT framing. This skill drafts a service agreement
built around exactly those Israeli rules.

## Instructions

This skill drafts a bilateral **service / contractor agreement (הסכם למתן שירותים)** from the
**freelancer's side**. Work through the steps; produce the contract in Hebrew (RTL) because it is
governed by Israeli law and will be read by Israeli parties.

> Always tell the user, once, that this is a drafting aid and not legal advice, and that a lawyer
> should review the agreement before signing. This is especially important when money or IP is
> significant.

### Step 1: Gather the deal facts

Collect the minimum needed to draft:

| Field | Why it matters |
|---|---|
| Provider name + ת.ז./ע.מ., status (עוסק פטור / עוסק מורשה) | Drives the VAT and invoicing clause |
| Client name + ח.פ./ע.מ., business or private | Drives payment-law applicability (the 2017 law applies to business clients) |
| Services / deliverables | The scope clause and IP clause |
| Fee + structure (fixed, hourly, monthly, milestones) | The consideration clause |
| Payment term wanted (e.g. שוטף+30) | Overrides the statutory default |
| Who keeps the IP | Decides whether to assign or license deliverables |
| Term and notice | Termination clause |

If the user does not know a field, use a sensible default and flag it in a "review these" list at
the end. Never invent the parties' identifying numbers.

### Step 2: Decide the independent-contractor framing (the most important step)

Israeli labor courts ignore the contract's label and apply the **מבחן מעורב (mixed test)**, dominated
by the **מבחן ההשתלבות (integration test)**: is the freelancer a separate business, or an integrated
part of the client's organization? If it looks like employment, the freelancer can later sue for
**retroactive recognition (הכרה בדיעבד)** and collect severance, pension, vacation, sick days,
holidays, and הבראה.

What actually protects the freelancer from a *surprise* reclassification is the **real facts**, not
the contract wording. So:

1. Include an **independent-contractor declaration** stating the provider runs its own business,
   bears its own tax, Bituach Leumi, and pension, and that the parties intend a commercial, not an
   employment, relationship. Courts give this **evidential weight only** (per ע"ע 300256/98 אורי
   אייזיק) and will apply the integration test to the real facts, so never present the label as
   decisive.
2. Build in **operational separation** that the contract reflects: own tools, own hours, freedom to
   serve other clients, no company email, no exclusivity, invoicing per deliverable, and an express
   right to use **subcontractors** (no personal-performance requirement, which itself helps the
   contractor case).
3. Understand the **set-off / gross-up clause** correctly before using it. It says that if a court
   later finds employment, the fee is treated as already inclusive of social rights and the excess
   over a comparable employee wage is set off against any award. This clause **protects the client,
   not the freelancer**: it is the client's tool to claw back the "contractor premium", it is enforced
   only in narrow cases (express term plus a fee markedly above a comparable salary), and a court is
   not bound to honor it. Do not sell it to the freelancer as their shield. It also cannot waive
   non-waivable (cogent) labor rights.

### Step 3: Draft the consideration, payment, VAT, and withholding clause

State the fee and structure, then set an **explicit payment term**. Under חוק מוסר תשלומים לספקים,
התשע"ז-2017, if the contract is silent and the client is a business, the default is **שוטף+45** (no
later than 45 days from the end of the month the invoice was submitted). A freelancer is better off
naming a shorter term (e.g. שוטף+30 or שוטף+0). Note that for **government and public-body clients**
the law sets its own (often shorter) default and caps how far the term can be pushed, so verify the
applicable provision rather than assuming שוטף+45. Reference the law so late payment carries interest
and, after a further 30 days, דמי פיגורים, by default, and reserve the right to suspend work on
non-payment.

State VAT correctly and unambiguously, because a wrong VAT framing is a direct error in the price:
- **עוסק מורשה**: "the fee is exclusive of VAT; VAT at 18% (as of 2025) will be added against a
  חשבונית מס." Say "exclusive of VAT" explicitly, since a bare number with no "+VAT" wording can be
  read as VAT-inclusive.
- **עוסק פטור**: "the provider is an עוסק פטור and does not charge VAT; a receipt will be issued." Add
  that if the provider crosses the turnover cap (122,833 ₪ for 2026) and converts to עוסק מורשה, VAT
  applies from that point.

Add a **withholding-tax clause (ניכוי מס במקור)**: in Israeli B2B, the client may be legally required
to withhold tax from the payment unless the freelancer hands over a valid **אישור ניהול ספרים** and an
**אישור פטור / שיעור מופחת מניכוי מס במקור**. State that the provider will furnish these certificates,
failing which the client withholds at the statutory rate. Without this clause the freelancer is
blindsided when the first payment arrives net of withholding.

### Step 4: Draft the IP clause

This is the clause clients get wrong. Under חוק זכות יוצרים, התשס"ח-2007 (סעיף 35), the default owner
of a **commissioned work** is the **CREATOR (the freelancer)**, not the client, unless the contract
says otherwise. (Contrast: סעיף 34 gives an employer the copyright in an employee's work; a commissioned
portrait or family-event photo defaults to the commissioner.)

So decide and draft explicitly:
- If the client should own the deliverables, **expressly assign** the economic rights, typically on
  full payment.
- **Moral rights (הזכות המוסרית)** of attribution and integrity are personal under the 2007 Copyright
  Law and **cannot be assigned**, only waived. Handle them with a separate waiver clause, not by
  lumping "all rights including moral rights" into the assignment (that part is void).
- The freelancer keeps rights in pre-existing tools, know-how, and general methods, and **third-party
  / open-source components are licensed, not assigned** (the freelancer often cannot transfer them).

### Step 5: Add the scope-protection and standard clauses

- **Acceptance and revisions**: define how the client signs off on a deliverable, a deemed-acceptance
  window (e.g. silence for 7 business days = accepted), and how many revision rounds are included.
  "What counts as done" is where payment disputes live, so do not push it into an empty annex.
- **Termination and accrued fees**: state the notice period AND that on termination the freelancer is
  paid pro-rata for work done and approved expenses; for a cancelled fixed-price project, add a
  **kill / cancellation fee** based on progress. Without this, a designer terminated mid-project gets
  nothing.
- **Confidentiality (סודיות)**, surviving termination.
- **Restraint of trade**: default to a narrow trade-secret + non-solicitation clause, NOT a broad
  non-compete. A bare non-compete is generally unenforceable in Israel; courts enforce a restraint
  only to protect a legitimate interest like a real trade secret and only if reasonable in scope,
  time, and geography (ע"ע 164/99 צ'ק פוינט נ' רדגארד).
- **Liability cap + mutual indemnity**, with carve-outs for willful misconduct, IP infringement, and
  confidentiality breach. Make indemnity **mutual**: the client should indemnify the freelancer for
  client-supplied materials and for client misuse of the deliverables. Optionally require
  **professional liability insurance (ביטוח אחריות מקצועית)** if the client is a company or public
  body.
- **Data protection**: if the freelancer processes the client's personal data (a developer touching a
  user database, a marketer handling a CRM or mailing list), add a clause defining the freelancer as a
  processor with security obligations and breach notification, per the Privacy Protection Law and its
  Amendment 13 (in force August 2025).
- **Term, termination, and notice**; **governing law (Israeli) and jurisdiction**, noting that
  classification disputes go to the labor courts regardless of a forum clause.

### Step 6: Generate and hand off the draft

Assemble the Hebrew agreement. You can produce it directly, or use the helper script for a
consistent skeleton:

```bash
python3 scripts/build_agreement.py --provider "ישראל ישראלי" --provider-id 000000000 \
  --client "חברת לקוח בעמ" --client-id 510000000 \
  --services "עיצוב גרפי וניהול מותג" --fee 8000 --vat murshe --payment-net 30 \
  --out agreement.md
```

End with a short "review these before signing" list (any defaulted fields, the IP choice, and the
recommendation to have a lawyer review).

## Examples

### Example 1: Designer with a new client

User says: "I'm a freelance graphic designer (עוסק מורשה). New client wants a 6,000 ₪/month brand
retainer. Draft me a contract."

Actions:
1. Gather facts; set fee 6,000 ₪/month +VAT, payment שוטף+30, designer keeps IP until paid then
   assigns deliverables.
2. Add the independent-contractor declaration + set-off clause, with the honest caveat.
3. Generate the Hebrew agreement and list "review these": notice period, insurance requirement.

Result: A ready Hebrew הסכם למתן שירותים the designer can send, with VAT and IP handled correctly.

### Example 2: Developer worried about reclassification

User says: "I've been a 'contractor' for one company full-time for 2 years. They want a new contract.
What should it say so I'm not treated like an employee?"

Actions:
1. Flag the elevated reclassification risk (single client, full-time, long duration = strong
   integration-test markers).
2. Draft the declaration + set-off clause, AND advise concrete operational changes (own tools, serve
   other clients, no company email), explaining the clause alone is not decisive.
3. Suggest, where relevant, the user consult a lawyer given the exposure.

Result: A contract plus a practical risk-reduction checklist, with realistic expectations.

## Bundled Resources

### Scripts
- `scripts/build_agreement.py` -- Assembles a Hebrew service-agreement skeleton from parameters.
  Run: `python3 scripts/build_agreement.py --example`

### References
- `references/legal-reference.md` -- Clause-by-clause grounding in Israeli statute and case law
  (reclassification, payment law, IP default, VAT, non-compete, insurance).
- `references/domain-checklist.md` -- Coverage checklist the agreement is drafted against.

## Gotchas

- **Do not promise the contract label protects against reclassification.** Agents tend to write "the
  parties agree there is no employment relationship" as if it settles the matter. It does not: Israeli
  courts treat the label as evidence only and apply the integration test to the real facts. Always add
  the honest caveat.
- **Do not assume the client owns the deliverables by default.** The intuition from many jurisdictions
  is wrong here: under סעיף 35 of the 2007 Copyright Law, a commissioned work defaults to the
  freelancer. If the agreement does not expressly assign IP, the client may not own it.
- **Do not leave payment timing silent and "rely on the law."** The statutory default (שוטף+45) is the
  worst case for the freelancer. Always set an explicit, shorter term.
- **Do not draft a broad non-compete.** A sweeping "shall not compete for 2 years" clause is usually
  unenforceable in Israel and signals an employment-like relationship. Use a narrow trade-secret /
  non-solicitation clause.
- **Do not state VAT generically.** Whether VAT is added depends on the provider's status (עוסק פטור
  charges none). Getting this wrong is a direct error in the price the client pays. The rate is 18%
  (from 1 January 2025), not the old 17%. State the fee as "exclusive of VAT" so a bare number is not
  read as VAT-inclusive.
- **Do not forget withholding tax (ניכוי מס במקור).** Israeli business clients often must withhold tax
  unless the freelancer provides a valid אישור ניהול ספרים and ניכוי-מס certificate. If the contract
  is silent, the freelancer is surprised by a payment that arrives net of withholding. Always include
  the certificate clause.
- **Do not sell the set-off clause as the freelancer's protection.** It is the client's tool to claw
  back the contractor premium if the relationship is reclassified, it is rarely enforced, and it
  cannot waive non-waivable labor rights. The freelancer's real protection is operational separation,
  not contract wording.
- **Do not assign moral rights.** Moral rights (הזכות המוסרית) are personal and non-assignable under
  the 2007 Copyright Law. Assigning "all rights including moral rights" is partly void; use a separate
  waiver and carve out third-party / open-source components the freelancer can only license.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| חוק זכות יוצרים 2007 | https://www.nevo.co.il/law_html/law00/3953.htm | סעיף 34 / סעיף 35 ownership defaults |
| חוק מוסר תשלומים לספקים 2017 | https://www.nevo.co.il/law_html/law00/144599.htm | default payment timing and interest |
| gov.il VAT decision | https://www.gov.il/he/pages/dec1270-2024 | VAT is 18% from 1 Jan 2025 |
| ע"ע 164/99 צ'ק פוינט נ' רדגארד | https://he.afiklaw.com/caselaw/2573 | non-compete enforceability standard |
| ביטוח אחריות מקצועית | https://www.bizreviews.co.il/article/professional-liability-insurance-guide | professional liability cover |

## Troubleshooting

### Error: "The client says they own everything I make for them"
Cause: The client assumes a work-for-hire default that does not exist for contractors in Israel.
Solution: Point to סעיף 35 of the 2007 Copyright Law (commissioned work defaults to the creator).
The contract must expressly assign IP for the client to own it; negotiate assignment on full payment.

### Error: "Is the no-employment clause enough to protect me?"
Cause: Over-reliance on the contract label.
Solution: No. It is evidential only. Combine the clause with real operational separation (own tools,
own hours, multiple clients, no company email) and, for high exposure, advise a lawyer.

### Error: "The client wants to pay 'when they pay their client', is that allowed?"
Cause: Pay-when-paid terms that push beyond the statutory default.
Solution: The 2017 Prompt Payment law sets a default of שוטף+45 for business clients when silent.
Set an explicit term in the contract; very long terms may conflict with the law's protections.
