---
name: israeli-wills-inheritance
description: >-
  Draft a legally-valid Israeli will and navigate the inheritance process under the
  Succession Law 1965. Drafts a witnessed will (צוואה בעדים), which needs NO lawyer:
  the testator writes the wishes, dates and signs, and two witnesses (who may not be
  beneficiaries or their spouses) sign. Explains the four will types, depositing the
  will with the Inheritance Registrar, and obtaining a succession order (צו ירושה,
  when there is no will) or a probate order (צו קיום צוואה, when there is a will).
  Use when a user asks to "write a will", "draft a will leaving X to Y", "deposit my
  will", "get a succession order", "my parent died without a will", "צוואה", "צו ירושה",
  or "צו קיום צוואה". Prevents the common self-made-will mistakes that void bequests.
  Do NOT use for binding enduring power of attorney (ייפוי כוח מתמשך needs a certified
  attorney, see israeli-elder-care-navigator), guardianship, contested-estate litigation
  between heirs (use a lawyer), or formal legal advice on complex estates.
license: MIT
allowed-tools: ''
compatibility: >-
  Pure text generation (drafts a will document, walks the Registrar process). No local
  shell, API key, or network access required. Works on Claude Code, Claude.ai, Claude
  Desktop, Cursor, ChatGPT, Gemini CLI, and other agents.
---

# Israeli Wills & Inheritance Navigator

## Problem

Most Israelis put off writing a will because they assume it needs an expensive lawyer, and the ones who try it alone often void part of it without knowing: the most common mistake is letting a beneficiary (or a beneficiary's spouse) sign as a witness, which cancels that bequest. People also confuse the two inheritance orders, asking for a succession order when there is a will or a probate order when there is none, and waste weeks at the wrong door. This skill drafts a correctly-structured witnessed will (which the Succession Law allows with no lawyer at all), keeps the witnesses valid, and routes the user to the right order at the Inheritance Registrar.

## Instructions

The skill does three jobs. Identify which the user needs.

### Job 1: Draft a will (focus on the witnessed will, צוואה בעדים)

Israel's Succession Law recognises four will forms. Pick the right one, then draft it.

| Will type | When it fits | Lawyer needed? |
|-----------|--------------|----------------|
| צוואה בעדים (witnesses) | The default for most people. Typed or written, signed before 2 witnesses. | No |
| צוואה בכתב יד (handwritten) | Written entirely in the testator's own hand, dated, signed. No witnesses. | No |
| צוואה בפני רשות (before an authority) | Declared before a judge, registrar, notary, or religious-court official. | An authority, not necessarily a private lawyer |
| צוואה בעל פה (oral / שכיב מרע) | Only for someone on their deathbed or in mortal danger; expires if they recover. | No, but very limited |

**The witnessed will is the skill's main deliverable.** Under the Succession Law it requires NO lawyer, but it has FOUR formal elements (Section 20), and missing any one risks voiding the will. State all four:
1. **In writing** (typed is fine).
2. **Dated.**
3. The testator **declares before two witnesses** that this is their will and **signs** it.
4. The two witnesses **confirm in writing on the will itself, by their signature**, that the testator declared and signed. This witness-confirmation clause is not optional boilerplate, it is a constitutive requirement; a will where the witnesses just sign a blank line without the confirmation language is defective.

**Who can make it (Section 26):** the testator must be an adult (18+) and of sound mind. A will made by a minor, by a person declared legally incompetent (פסול דין), or by someone who at the time did not understand what a will is, is VOID. The "sound mind" line in the template is a declaration, not a substitute for actual capacity.

**The rules that void a bequest (state them every time):**
- A witness must be an adult and not legally incompetent (Section 24).
- A beneficiary, or a beneficiary's spouse, must NOT be a witness. More broadly (Section 35), a bequest in favour of anyone who **wrote the will, witnessed it, or otherwise took part in making it**, or in favour of that person's spouse, is VOID. This matters here: if a beneficiary dictates or prepares the will, the gift to them can be attacked. So have a neutral person handle the wording, and use two neutral adult witnesses who inherit nothing.

To draft, collect: the testator's full name + Teudat Zehut, the bequests (who gets what), any guardian wish for minor children, and whether to name an executor (מנהל עיזבון). Then produce the Hebrew will using the structure in `references/will-templates.md`: a clear-mind declaration, a clause revoking earlier wills, numbered bequests, an optional executor clause, date and place, the testator's signature line, and the two-witness confirmation clause (the Section 20 wording) with name/ID/signature lines.

Always tell the user: print it, sign by hand in front of both witnesses at the same sitting (everyone signs the same copy, in each other's presence), and keep the original safe. Remind them to update the will after a major life change (marriage, divorce, a new child), because Israeli law does NOT automatically cancel a gift to an ex-spouse on divorce. For anything beyond simple bequests (a business, foreign assets, a trust, minor children needing a guardian, or a likely dispute), recommend a licensed inheritance lawyer.

### Job 2: Deposit the will with the Inheritance Registrar

Depositing the will with the Inheritance Registrar (הרשם לענייני ירושה) is OPTIONAL, a will is fully valid without it. Deposit safeguards the original from loss or tampering and records that it existed. Walk the user to the gov.il will-deposit service / the Registrar's online portal (inheritance.justice.gov.il); the testator must deposit it in person with ID. Make clear deposit is not a stamp of validity, the will still has to meet the form requirements above.

### Job 3: Get the right inheritance order after a death

This is where users go to the wrong door. The rule is simple:

| Situation | Order to request | What it does |
|-----------|------------------|--------------|
| The deceased left NO will | Succession order (צו ירושה) | Declares the legal heirs (spouse, children, parents, per the Succession Law order) and their shares. |
| The deceased left a will | Probate / will-execution order (צו קיום צוואה) | Gives the will binding effect and distributes the estate as written in it. |

Both applications go to the **Inheritance Registrar** (הרשם לענייני ירושה), filed online at the Registrar's portal. The Registrar (not a court) issues most orders; if an objection is filed the matter is decided by the Family Court, and certain other cases also go to court rather than the Registrar. As of 2026 the online application fee is about 507 NIS plus a 66 NIS publication fee (fees are updated by regulation, usually each January, so confirm the current amount on the Registrar site before paying). Once granted, the digital order is transmitted to banks, the Land Registry (Tabu), and other bodies so heirs can act on it.

**The objection window:** after the Registrar publishes notice of the application, an objection (התנגדות) must be filed within 14 days, as long as the order has not yet been issued. Tell heirs to expect this waiting period.

**Who inherits when there is NO will (Section 11):** the surviving spouse takes the household chattels including the family car, and of the rest of the estate the spouse takes one-half when the deceased left children (or their descendants) or parents, two-thirds when the deceased left only siblings (or their descendants) or grandparents, and the whole estate if none of those relatives survive. The children share the remaining portion equally (a deceased child's share passes to their own children). If the deceased left no children, that remaining portion goes to the parents and their line, then to grandparents and their line (see `references/orders-and-process.md`). Give the actual fraction, not just "spouse and children".

**Two things a will cannot do, and one fear it does not justify:**
- **Maintenance from the estate (Section 56):** a spouse, children, or parents of the deceased who genuinely need support are entitled to maintenance from the estate, whether the estate passes by law or by will. A will cannot simply cut off a dependent who needs maintenance.
- **Debts:** heirs receive what is left of the estate after its debts; if the user fears the debts may be larger than the assets, tell them to get advice before accepting, an heir can disclaim their share (הסתלקות) rather than take on a negative estate.

## Examples

### Example 1: Draft a simple will
User says: "Draft a will leaving my apartment to my two children equally."
Actions:
1. Collect the testator's name + Teudat Zehut and the children's names.
2. Produce a Hebrew witnessed will: clear-mind declaration, revocation of prior wills, a bequest splitting the apartment 50/50, date/place, signature line, and the two-witness clause.
3. Warn: the two witnesses must NOT be the children, their spouses, or anyone inheriting. Use two neutral adults. Sign by hand in front of both.
Result: A ready-to-print Hebrew will plus the signing instructions.

### Example 2: Deposit a will
User says: "How do I make sure my will can't be lost or thrown out?"
Actions:
1. Explain deposit with the Inheritance Registrar is optional but protects the original.
2. Point to the gov.il will-deposit service / the Registrar portal; the testator deposits in person with ID.
3. Note deposit safeguards the document but does not by itself prove validity; the form requirements still apply.
Result: Clear steps to deposit, with the right expectation.

### Example 3: Death with no will
User says: "My father passed away and did not leave a will. How do I inherit?"
Actions:
1. Identify this as the no-will path, so the order is a succession order (צו ירושה), not a probate order.
2. Walk through the online application to the Inheritance Registrar, the 2026 fees, and who the legal heirs are.
3. Mention an objection would move the file to the Family Court.
Result: The correct order, where to file it, and what it costs.

## Bundled Resources

### References
- `references/will-templates.md` -- ready-to-fill Hebrew templates for the witnessed will and the handwritten will, plus the witness attestation clause. Consult when drafting.
- `references/orders-and-process.md` -- the succession-order vs probate-order decision, the Registrar application steps, fees, and the legal-heir order. Consult when handling a death.
- `references/domain-checklist.md` -- coverage contract for this skill (used by maintenance).

## Recommended MCP Servers

| MCP | Use |
|-----|-----|
| `kolzchut` | Look up the All-Rights (כל-זכות) pages on wills, deposit, and the inheritance orders for current procedure and Hebrew terms. |
| `israel-law` | Pull the text of the Succession Law (חוק הירושה) sections when a user needs the statute itself. |

These help confirm current procedure and terminology; the will drafting itself is done by this skill from the user's instructions.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Kol-Zchut: witnessed will | https://www.kolzchut.org.il/he/צוואה_בעדים | No-lawyer requirement, signing procedure, witness disqualification |
| Kol-Zchut: will types | https://www.kolzchut.org.il/he/צוואה | The four valid will forms |
| Kol-Zchut: will deposit | https://www.kolzchut.org.il/he/הפקדת_צוואה_אצל_רשם_הירושה_במשרד_המשפטים | Deposit is optional, how it works |
| Kol-Zchut: succession order | https://www.kolzchut.org.il/he/הגשת_בקשה_מקוונת_לקבלת_צו_ירושה | The no-will order, online application, fees |
| Kol-Zchut: probate order | https://www.kolzchut.org.il/he/הגשת_בקשה_מקוונת_לקבלת_צו_קיום_צוואה | The with-will order |
| Kol-Zchut: objection to an order | https://www.kolzchut.org.il/he/התנגדות_למתן_צו_ירושה | The 14-day objection window |
| Succession Law 1965 (full text) | https://he.wikisource.org/wiki/חוק_הירושה | Sections 11, 19, 20, 24, 26, 35, 56 |
| Inheritance Registrar portal | https://inheritance.justice.gov.il/ | Where the orders are filed online |

## Gotchas

- **The witnessed will has FOUR elements, not three (Section 20).** Agents routinely write "testator declares and signs, witnesses sign" and drop the fourth: the witnesses must CONFIRM IN WRITING ON THE WILL, by their signature, that the testator declared and signed. Without that confirmation clause the will is defective. Always include the Section 20 witness-confirmation wording.
- **A beneficiary, their spouse, OR anyone who helped prepare the will must not benefit if they were involved in making it (Section 35).** The witness rule is the common case, but Section 35 is broader: a gift to whoever wrote, witnessed, or took part in making the will (or their spouse) is void. Since an AI is helping draft, make sure a beneficiary is not the one preparing it, and use two neutral witnesses.
- **The testator must be 18+ and of sound mind (Section 26).** A will by a minor, a legally incompetent person, or someone who did not understand what they were signing is void. Do not draft for a minor.
- **A witnessed will needs no lawyer and no notary.** The Succession Law explicitly allows a witnessed will with just the testator and two qualified witnesses.
- **Do not confuse the two orders.** Succession order (צו ירושה) is for NO will; probate order (צו קיום צוואה) is for WHEN there IS a will. The Inheritance Registrar issues both online; the Family Court enters when an objection is filed (and in certain other cases), not as the default.
- **Deposit is not validity.** Depositing the will with the Registrar protects the paper, it does not make an otherwise-defective will valid, and skipping deposit does not make a valid will invalid.

## Troubleshooting

### Error: "I had my spouse witness the will and they also inherit"
Cause: a beneficiary or their spouse signed as a witness.
Solution: that bequest to them can be voided. Re-sign the will with two neutral adult witnesses who inherit nothing, in everyone's presence.

### Error: "There is a will but they told me to apply for a succession order"
Cause: succession order (צו ירושה) is for estates with NO will.
Solution: when a will exists, apply for a probate order (צו קיום צוואה) instead, at the Inheritance Registrar.

### Error: "Is my typed will valid without a lawyer?"
Cause: assuming a lawyer or notary is required.
Solution: a typed witnessed will is valid if the testator dates and signs it and declares before two qualified witnesses who also sign. No lawyer is needed for a simple estate.
