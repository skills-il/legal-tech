---
name: israeli-wills-inheritance
description: >-
  Draft a legally-valid Israeli will and navigate the inheritance process under the
  Succession Law 1965. Drafts a witnessed will (צוואה בעדים), which Israeli law does
  not require a lawyer for (one is still recommended): the testator writes the wishes,
  dates and signs, and two witnesses (who may not be beneficiaries or their spouses)
  sign. Explains the four will types, depositing the will with the Inheritance
  Registrar, and obtaining a succession order (צו ירושה, when there is no will) or a
  probate order (צו קיום צוואה, when there is a will). Use when a user asks to "write
  a will", "deposit my will", "get a succession order", "my parent died without a will",
  "צוואה", "צו ירושה", or "צו קיום צוואה". Prevents common self-made-will mistakes.
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

Most Israelis put off writing a will because they assume it needs an expensive lawyer, and the ones who try it alone often void part of it without knowing: the most common mistake is letting a beneficiary (or a beneficiary's spouse) sign as a witness, which cancels that bequest. People also confuse the two inheritance orders, asking for a succession order when there is a will or a probate order when there is none, and waste weeks at the wrong door. This skill drafts a correctly-structured witnessed will (which the Succession Law lets you make yourself, though having an inheritance lawyer draft or review it is recommended), keeps the witnesses valid, and routes the user to the right order at the Inheritance Registrar.

## Instructions

The skill does three jobs. Identify which the user needs.

### Job 1: Draft a will (focus on the witnessed will, צוואה בעדים)

Israel's Succession Law recognises four will forms. Pick the right one, then draft it.

| Will type | When it fits | Lawyer required by law? |
|-----------|--------------|----------------|
| צוואה בעדים (witnesses) | The default for most people. Typed or written, signed before 2 witnesses. | No (but recommended) |
| צוואה בכתב יד (handwritten) | Written entirely in the testator's own hand, dated, signed. No witnesses. | No (but recommended) |
| צוואה בפני רשות (before an authority) | Stated aloud to, OR handed in writing personally to, a judge, court registrar, Inheritance Registrar, or religious-court judge (Section 22). A notary counts as a judge. The authority reads it back, the testator declares it is their will, and the authority certifies that on the will's face. | An authority, e.g. a notary, takes it |
| צוואה בעל פה (oral / שכיב מרע) | Only for someone on their deathbed or in mortal danger. The two witnesses must record the words, the date and the circumstances in a memorandum (זכרון דברים), sign it, and deposit it with the Registrar as soon as practicable (Section 23). It lapses one month after the danger passes if the testator is still alive. | No, but very limited |

**The witnessed will is the skill's main deliverable.** The Succession Law does not require a lawyer for it, but using an inheritance lawyer to draft or review the will is recommended, especially to reduce the chance it is later challenged. It has FOUR formal elements (Section 20), and missing any one exposes the will to challenge. State all four:
1. **In writing** (typed is fine).
2. **Dated.**
3. The testator **declares before two witnesses** that this is their will and **signs** it.
4. The two witnesses **confirm in writing on the will itself, by their signature**, that the testator declared and signed. This witness-confirmation clause is not optional boilerplate; a will where the witnesses just sign a blank line without the confirmation language is defective.

**Defective is not the same as void (Section 25).** Draft all four elements every time, but never tell a user that a flawed will is dead. Section 25 lets the Inheritance Registrar or the court admit a will despite a missing or faulty element, by reasoned decision, if they have no doubt it reflects the testator's free and true intent. What cannot be cured is the מרכיב היסוד: for a witnessed will, that the will is in writing and the testator brought it before two witnesses; for a handwritten will, that the whole will is in the testator's own handwriting. A missing date, and a missing signature, are curable defects in both forms.

**Who can make it (Section 26):** the testator must be an adult (18+) and of sound mind. A will made by a minor, by a person declared legally incompetent (פסול דין), or by someone who at the time did not understand what a will is, is VOID. The "sound mind" line in the template is a declaration, not a substitute for actual capacity.

**The rules that void a bequest (state them every time):**
- A witness must be an adult and not legally incompetent (Section 24).
- A beneficiary, or a beneficiary's spouse, must NOT be a witness. More broadly (Section 35), a bequest in favour of anyone who **wrote the will, witnessed it, or otherwise took part in making it**, or in favour of that person's spouse, is VOID. This matters here: if a beneficiary dictates or prepares the will, the gift to them can be attacked. So have a neutral person handle the wording, and use two neutral adult witnesses who inherit nothing.

To draft, collect: the testator's full name + Teudat Zehut, the bequests (who gets what), any guardian wish for minor children, and whether to name an executor (מנהל עיזבון). Then produce the Hebrew will using the structure in `references/will-templates.md`: a clear-mind declaration, a clause revoking earlier wills, numbered bequests, an optional executor clause, date and place, the testator's signature line, and the two-witness confirmation clause (the Section 20 wording) with name/ID/signature lines.

**What the will does NOT control (state this every time you draft one):**
- **Pension, provident funds and life insurance are outside the estate (Section 147).** Money payable on death under an insurance contract, a pension fund (קופת קיצבה), or a provident fund (קופת גמל) is not part of the estate unless the contract says it goes to the estate. The will does not override the beneficiary designation (מוטבים) held by the fund or insurer. For most Israelis this is the largest asset they own. Tell the user to update the מוטבים separately with each institution; a will that contradicts them does not win.
- **You cannot contract about a future inheritance (Section 8).** An agreement about a living person's estate, and a waiver of a future inheritance, are both void. A gift meant to take effect only on death is void unless it is made as a will under this law. Section 27 adds that an undertaking to make, change, or revoke a will has no effect, and a will clause purporting to bar its own revocation is void.
- **Mutual wills between spouses (צוואה הדדית, Section 8א)** are a separate regime, not just two wills signed together. While both spouses are alive, a spouse who wants to revoke must give the other written notice, and that cancels BOTH wills. After one spouse dies, the survivor can only revoke by disclaiming what they were due under the deceased's mutual will (before distribution) or by returning everything they inherited under it (after distribution). A clause completely barring revocation during both lives is itself void. Recommend a lawyer before drafting one.

Always tell the user: print it, sign by hand in front of both witnesses at the same sitting (everyone signs the same copy, in each other's presence), and keep the original safe. Remind them to update the will after a major life change (marriage, divorce, a new child), because Israeli law does NOT automatically cancel a gift to an ex-spouse on divorce. For anything beyond simple bequests (a business, foreign assets, a trust, minor children needing a guardian, or a likely dispute), recommend a licensed inheritance lawyer.

### Job 2: Deposit the will with the Inheritance Registrar

Depositing the will with the Inheritance Registrar (הרשם לענייני ירושה) is OPTIONAL, a will is fully valid without it. Deposit safeguards the original from loss or tampering and records that it existed. Walk the user to the gov.il will-deposit service / the Registrar's online portal (inheritance.justice.gov.il). The deposit can be made either by attending a Registrar office in person or remotely online, but only the testator can do it, and only the testator can take the will back. Make clear deposit is not a stamp of validity, the will still has to meet the form requirements above.

**The deposit fee, and when it is waived.** The fee schedule lists 126 NIS for depositing a will, but item 5א exempts the deposit entirely if the testator has not deposited an earlier will in the five years before. In practice a first deposit, or one made five or more years after the last, is free. Say this rather than quoting the 126 alone, because most users depositing a will are exempt.

Also tell the testator: they may take a deposited will back at any time, at no charge, and retrieving it does NOT revoke it, the will stays in force until it is actually revoked or a newer will is signed in its place. Only one will can be on deposit at a time, so depositing a new one requires withdrawing the old one first. And if no application about the will is filed, the Registrar opens the deposited will three months after the death and notifies the beneficiaries named in it. Separately, anyone holding a will must hand it over once they learn the testator has died; failing to do so is a criminal offence.

### Job 3: Get the right inheritance order after a death

This is where users go to the wrong door. The rule is simple:

| Situation | Order to request | What it does |
|-----------|------------------|--------------|
| The deceased left NO will | Succession order (צו ירושה) | Declares the legal heirs (spouse, children, parents, per the Succession Law order) and their shares. |
| The deceased left a will | Probate / will-execution order (צו קיום צוואה) | Gives the will binding effect and distributes the estate as written in it. |

Both applications go to the **Inheritance Registrar** (הרשם לענייני ירושה), filed online at the Registrar's portal. The Registrar, not a court, issues most orders.

**Three doors, not two.** A file leaves the Registrar for the **Family Court** only on the grounds listed in Section 67א: an objection was filed; the State or one of its institutions is a party; the Attorney General or their representative opens or joins a proceeding; the Public Trustee (האפוטרופוס הכללי) represents someone whose property it manages; or the Registrar decides to transfer it. The AG and Public Trustee grounds are the practical ones, they routinely pull in files with minor or legally incapacitated heirs. Separately, a **religious court** (rabbinical, sharia, druze) may issue a succession order or a probate order under Section 155, but only if every party concerned has consented in writing.

**Fees.** State the rule, not just one number, because the amounts reindex every 1 January by CPI. The base fee for a succession-order or probate-order application is 597 NIS, and filing online costs 85% of the listed fee, which is where the commonly-quoted 507 NIS comes from. A separate publication fee of 66 NIS applies. The full schedule, the other seven fee rows, and the exemptions are in `references/orders-and-process.md`. Bereaved first-degree relatives (spouse, child, parent, sibling) of someone who died in war operations or in a hostile act, or in military service, are exempt from the fee entirely. Once granted, the digital order is transmitted to banks, the Land Registry (Tabu), and other bodies so heirs can act on it.

**The objection window:** the Registrar publishes notice of the application and sets a period for objections which by law cannot be shorter than two weeks; in practice this is 14 days. An objection (התנגדות) can be filed within that period as long as the order has not yet been issued. Tell heirs to expect this waiting period.

**Tax:** there is no estate or inheritance tax in Israel. The estate tax law was repealed for anyone who died after 31 March 1981, and receiving an inheritance is not itself a taxable event. Do not let a user think otherwise. The real tax exposure comes later, on SELLING an inherited asset, where מס שבח (land appreciation tax) or capital gains tax can arise. Route that question to a tax professional rather than answering it here.

**Who inherits when there is NO will (Section 11):** the surviving spouse takes the household chattels including the family car, and of the rest of the estate the spouse takes one-half when the deceased left children (or their descendants) or parents, two-thirds when the deceased left only siblings (or their descendants) or grandparents, and the whole estate if none of those relatives survive. The children share the remaining portion equally (a deceased child's share passes to their own children). If the deceased left no children, that remaining portion goes to the parents and their line, then to grandparents and their line (see `references/orders-and-process.md`). Give the actual fraction, not just "spouse and children".

Two things that change the spouse's real take, and that agents routinely omit:
- **The apartment proviso, inside Section 11(a)(2).** In the two-thirds case, if the spouse had been married to the deceased for three years or more and was living with them at that time in an apartment that is wholly or partly part of the estate, the spouse takes the deceased's ENTIRE share in that apartment, plus two-thirds of what remains of the rest. For a childless couple facing the deceased's siblings this decides whether the widow or widower owns the home outright.
- **Marital property is settled before heirs take.** What a spouse is owed under חוק יחסי ממון or a property agreement is an estate DEBT ranked in Section 104(a)(4), paid out before any heir receives a share, and Section 11(c) separately deducts a כתובה from the spouse's share. Quoting "half" without this understates the spouse's position.

**An unmarried partner inherits too (Section 55).** Where a man and a woman lived a family life in a shared household without being married, and neither was married to anyone else at the time of death, the survivor is treated as if the deceased had left them by will whatever they would have inherited by law had they been married. A contrary provision in an actual will, express or implied, overrides this. Do not tell a ידוע/ה בציבור they have no claim.

**Two things a will cannot do, and one fear it does not justify:**
- **Maintenance from the estate (Section 56):** a spouse, children, or parents of the deceased who genuinely need support are entitled to maintenance from the estate, whether the estate passes by law or by will. A will cannot simply cut off a dependent who needs maintenance.
- **Debts:** heirs receive what is left of the estate after its debts; if the user fears the debts may be larger than the assets, tell them to get advice before accepting, an heir can disclaim their share (הסתלקות) rather than take on a negative estate.

**If you recommend disclaiming, give the rules with it (Section 6).** A disclaimer is filed in writing with the Inheritance Registrar (or with the court once the file has moved there), only after the death and only while the estate has not yet been distributed. It can cover all or part of the share. The disclaiming heir is treated as never having been an heir at all. Crucially, a disclaimer CANNOT be made in favour of a chosen person: only in favour of the deceased's spouse, child, or sibling. A conditional disclaimer is void, and a minor or a legally incapacitated person needs court approval. Two further traps: under Section 7(c) an heir who has already transferred or charged their share loses the right to disclaim, and Section 6א (added 2024) widens the permitted beneficiaries of a disclaimer where the deceased died in the war or in a hostile act.

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

### Scripts
- `scripts/inheritance_helper.py` -- two deterministic checks: which order to request (based on whether a will exists) and whether a proposed witness is a beneficiary. Run: `python3 scripts/inheritance_helper.py order --has-will no`

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
| Succession Law 1965 (full text) | https://he.wikisource.org/wiki/חוק_הירושה | Sections 6, 8, 8א, 11, 19, 20, 22, 23, 24, 25, 26, 27, 35, 39, 55, 56, 67, 67א, 147, 155 |
| Registrar fee regulations (full schedule) | https://he.wikisource.org/wiki/תקנות_הירושה_%28אגרות_הרשם_לעניני_ירושה%29 | Every fee row, the 85% online rule, the 1 January indexation, the exemptions |
| Estate Tax Law (repealed) | https://he.wikisource.org/wiki/חוק_מס_עזבון | Confirms the repeal for deaths after 31 March 1981 |
| Inheritance Registrar portal | https://inheritance.justice.gov.il/ | Where the orders are filed online |

## Gotchas

- **The witnessed will has FOUR elements, not three (Section 20).** Agents routinely write "testator declares and signs, witnesses sign" and drop the fourth: the witnesses must CONFIRM IN WRITING ON THE WILL, by their signature, that the testator declared and signed. Without that confirmation clause the will is defective. Always include the Section 20 witness-confirmation wording.
- **A beneficiary, their spouse, OR anyone who helped prepare the will must not benefit if they were involved in making it (Section 35).** The witness rule is the common case, but Section 35 is broader: a gift to whoever wrote, witnessed, or took part in making the will (or their spouse) is void. Since an AI is helping draft, make sure a beneficiary is not the one preparing it, and use two neutral witnesses.
- **The testator must be 18+ and of sound mind (Section 26).** A will by a minor, a legally incompetent person, or someone who did not understand what they were signing is void. Do not draft for a minor.
- **A witnessed will is not legally required to go through a lawyer or notary, but recommend one anyway.** The Succession Law allows a witnessed will with just the testator and two qualified witnesses, so agents should not claim notarization is mandatory. Still advise the user that an inheritance lawyer's review reduces the risk of a later challenge.
- **Do not confuse the two orders.** Succession order (צו ירושה) is for NO will; probate order (צו קיום צוואה) is for WHEN there IS a will. The Inheritance Registrar issues both online; the Family Court enters only on a Section 67א ground (objection filed, the State is a party, the Attorney General initiates or joins, the Public Trustee represents a party, or the Registrar transfers it), not as the default.
- **A will does nothing until the probate order issues (Section 39).** No right can be claimed under a will, and the will cannot be relied on as a will, unless a probate order has been granted. Heirs holding the paper cannot make a bank move on it.
- **Never tell a user a flawed will is void.** Section 25 lets the Registrar or the court admit a will despite a missing date, a missing signature, or a witness-competence problem, so long as the מרכיב היסוד survives and the decision-maker has no doubt about the testator's true intent. Draft properly, but describe defects as curable.
- **The will does not reach the pension or the life policy (Section 147).** Those pass by the מוטבים designation held at the fund or insurer, outside the estate.
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
Solution: a typed witnessed will is legally valid if the testator dates and signs it and declares before two qualified witnesses who also confirm it in writing. The law does not require a lawyer for a simple estate, but having an inheritance lawyer review the will is recommended to reduce the chance it is challenged.
