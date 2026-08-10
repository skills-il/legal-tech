---
name: israeli-tabu-extract-decoder
description: >-
  Not legal advice. Reads an Israeli nesach tabu (land registry extract) and explains it line by
  line: who is registered and in what share, what each mortgage, attachment, caveat, note,
  easement and attachment of common property actually means, and which findings normally warrant a
  lawyer before signing. Also works out whether the property is even in the register, since a large
  share of Israeli homes are held through other regimes. Use when a user pastes or describes a
  nesach, asks what an he'arat azhara or an ikul on it means, asks why the registered area differs
  from the advertised one, or cannot find their apartment in the register at all. It matters
  because an extract is conclusive evidence only for settled land. Do NOT use to value a property,
  for purchase tax or transaction guidance, or to advise whether title is good or whether to buy.
license: MIT
compatibility: >-
  Pure knowledge, no scripts and no network calls. Works identically on every listed agent,
  including the upload-only platforms.
---

# Israeli Tabu Extract Decoder

## Legal notice

This is a free information tool operated by an AI model. It explains what the entries on a land registry extract mean as categories, and helps you organise your own reading of your own document. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion. It is a general explanation only: it does not read the underlying deeds or the file of your matter, does not check current case law, does not verify that the document you supplied is authentic or current, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

This tool does not tell you whether title is good, whether a particular entry is a problem in your transaction, or whether to sign anything. Those questions require a licensed advocate who has seen the whole file. Nothing here may be relied on as evidence, and before signing a contract, paying a deposit, or acting on anything an extract shows, you should consult an advocate. All use of the output is the user's sole responsibility.

## Problem

Almost every Israeli property transaction produces a `נסח טאבו`, and almost nobody can read one. It is a dense page of block and parcel numbers, fractions, ranks, and note types, and the entries that matter most are the ones that look least dramatic. Buyers routinely misread it in both directions: they panic at a mortgage that is about to be discharged, and they miss a note conditioning any dealing on a third party's consent. Two structural facts make it worse. The extract is conclusive evidence only for **settled** land, and merely prima facie evidence otherwise, so the same document does not prove the same thing everywhere. And a very large share of Israeli homes are not in this register at all, so the reader's first problem is often that no `נסח` exists for their property and nobody has told them what they should be holding instead.

## Problem boundary

This skill explains what an extract says and what each entry type means **as a category**. It does not value the property, which is `israeli-property-appraisal`. It does not cover purchase tax, transaction guidance, or rental agreements, which are `israeli-real-estate`. It does not cover defects in a new apartment from a developer, which is `israeli-home-defect-report`.

It also stops firmly short of one line: it will not tell you whether the title is good, whether a specific encumbrance defeats your specific deal, or whether it is safe to sign. That is the practice of law and it needs an advocate with the whole file. The skill's job is to make sure you know what to ask about.

## Instructions

Read `references/entry-types.md` before interpreting any line of an extract, and `references/registration-regimes.md` before answering anything about a property that cannot be found in the register.

### Step 0, establish what document the user actually has

Ask before interpreting. Three different documents get called "the tabu" in conversation:

1. A land registry extract for a property registered in the register.
2. A rights confirmation from the Israel Land Authority, for land it manages that is not registered in the register.
3. A statement from a housing company (`חברה משכנת`), which is not a public register at all.

They prove different things and they are not interchangeable. `references/registration-regimes.md` sets out how to tell them apart and what to do in each case. If the user cannot find their apartment in the register, that is a finding in its own right and it is common, not an anomaly.

### Step 1, establish how much the document proves

This is the question most guides skip entirely.

- For **settled land** (`מקרקעין מוסדרים`, land registered following settlement of title), registration is **conclusive evidence** of its content.
- For **unsettled land** (`מקרקעין לא מוסדרים`), registration is only **prima facie** evidence.

Say which one applies before you characterise anything on the page as established. If you cannot tell from what the user supplied, say so and tell them how to find out, rather than defaulting to the stronger reading.

Then note the extract's **production date**. An extract speaks as at the moment it was produced and nothing later appears on it, so an extract obtained weeks ago is a historical document.

### Step 2, read the identity block

`גוש`, `חלקה`, and in a condominium `תת-חלקה`.

The trap here is that a sub-parcel number is **not** an apartment number. They coincide often enough to be dangerous and differ often enough to send a buyer the wrong neighbour's extract. Where the user is working from an apartment number alone, flag that the mapping needs confirming rather than assuming it.

The `שטח` is the **registered** area. It is not the marketed area, it is not the usable area, and it is computed on a basis that excludes some elements. A mismatch between the registered area and what an agent advertised is a question to raise, not a conclusion to draw.

### Step 3, read the ownership block

For each registered owner, read the name, the identifying number, and the **share** as a fraction.

Check three things and report each as a question rather than a verdict:

- Do the fractions add up to the whole?
- Does every seller in the proposed transaction actually appear here?
- Is a deceased person still registered? If so, the estate has to be dealt with before anything transfers, which is a real and common blocker.

Where the registered owner is the State or a public land body and the resident appears as `חוכר לדורות`, that is a normal registered right, not a defect. A lease over five years is a `חכירה` and over twenty five years a `חכירה לדורות`.

### Step 4, read the encumbrances, one type at a time

Do not summarise this block. Go entry by entry, name the type, and give the category meaning. `references/entry-types.md` carries each one in full. The short version:

| Entry | What it means as a category |
|---|---|
| `משכנתה` with a `דרגה` | A mortgage, ranked. A later transaction by the owner cannot defeat a purchaser at the mortgage's execution sale |
| A discharged rank | Does **not** necessarily mean the rank is free. A vacant rank can be refilled by a later mortgage where its terms so provide |
| `עיקול` | An attachment recorded by a court or enforcement authority |
| `הערת אזהרה` | A note that someone undertook **in writing** to transact. It blocks a contradicting registration and shields the beneficiary against a later attachment or insolvency, subject to an avoidance carve-out. It is **not** ownership |
| Note requiring a third party's consent | Any dealing is conditioned on that party's agreement. Extremely common and easy to skim past |
| `זיקת הנאה` | A charge for someone's benefit that carries **no** right to possess |
| `הצמדה` | A specified part of the common property attached to this unit, treated for all purposes as part of it |
| Registered lease | An encumbrance a buyer inherits |

### Step 5, in a condominium, read the shares and the bylaws separately

The share in the common property attached to a unit is the ratio of its floor area to the total floor area of all units unless the bylaws say otherwise, computed in hundredths. This is why the fraction rarely matches an intuition about size, and it is not an error.

Registered bylaws bind **anyone who later becomes an owner**. So a parking space or storeroom a seller describes as "belonging to the apartment" belongs to it only if the registered position says so. Where the user is relying on a promise, tell them the register is what carries over.

### Step 6, produce the output

Two blocks, in this order:

1. **What is recorded**, as a structured table the user can export: each entry with its type, its date, in whose favour it runs, and the category meaning.
2. **What to ask about**, as questions rather than conclusions: entries that condition dealings on a third party, a deceased registered owner, an area mismatch, an attachment, a ranked mortgage, or anything the user cannot account for.

Never output a verdict on the title. "Nothing here blocks the sale" and "the title is clean" are both outside this skill and both are the practice of law.

### Step 7, when the property is not in the register

Do not treat this as an error. Establish which regime applies, using `references/registration-regimes.md`, and tell the user what document they should be holding instead and who issues it. A contract and a payment receipt are not a registered right, and a transaction is completed by registration, so the gap between the two is exactly what the user needs to understand.

## Examples

### A mortgage and a caveat on the same page

Explain the mortgage rank and the caveat separately: the caveat blocks a contradicting registration and protects its beneficiary against later attachment or insolvency, but it is not ownership and it does not discharge the mortgage. Then stop, and point out that whether this particular combination is safe for this particular deal is an advocate's question.

### The area does not match the listing

The registered area is computed on its own basis and excludes some elements. Report the discrepancy, explain that the register's figure is the registered one, and treat the difference as something to ask about rather than as a misrepresentation you have identified.

### A note conditioning dealings on someone's consent

Name the note, explain that any dealing is conditioned on that party's agreement, and tell the user to obtain the consent position in writing before relying on any timetable. This is usually a public land body, a housing company, or a bank.

### "My apartment is not in the tabu"

Go to Step 7. Establish the regime, name the document that stands in place of an extract, and explain that a purchase contract does not itself constitute a registered right. Do not tell the user this is a problem with their ownership, and do not tell them it is fine.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| חוק המקרקעין | https://he.wikisource.org/wiki/חוק_המקרקעין | Sections 3, 5, 7, 57, 62, 85, 86, 124, 125, 126, 127, 128 |
| תקנות המקרקעין (אגרות) | https://he.wikisource.org/wiki/תקנות_המקרקעין_%28אגרות%29 | The extract categories in the fee schedule, and the current fees |

For how to obtain an extract, its current fee, and the exact set of extract types offered today, send the user to the Land Registry's own service pages. Those pages could not be read first-hand when this skill was written, so this skill deliberately states no fee and no ordering procedure rather than repeating figures it could not verify.

## Bundled Resources

| File | Use it for |
|---|---|
| `references/entry-types.md` | Every entry type, what it means, and what it does not mean |
| `references/registration-regimes.md` | Telling apart the registration regimes and what document each produces |
| `references/domain-checklist.md` | Coverage contract, known bad claims, and what could not be verified |

## Gotchas

- **The extract is not always conclusive.** It is conclusive evidence for settled land and only prima facie evidence otherwise. An agent that treats every extract as conclusive overstates the document.
- **A sub-parcel number is not an apartment number.** Assuming they match is the fastest way to read the wrong neighbour's extract and reason confidently about the wrong property.
- **A caveat is not ownership.** It blocks contradicting registrations and shields against later attachment or insolvency; it does not transfer anything, and a transaction is still completed only by registration.
- **A discharged mortgage does not free its rank.** A vacant rank can be refilled by a later mortgage where that mortgage's terms provide for it.
- **Do not conclude that title is clean.** Listing what is recorded is this skill's job; deciding what it means for a specific transaction is an advocate's.
- **Not being in the register is common, not an anomaly.** A very large share of Israeli homes sit in other regimes. Treating it as an emergency misleads the user as badly as ignoring it.
- **The registered area is not the marketed area.** Report the difference; do not characterise it.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| The user asks whether the title is clean | Outside the skill | Say plainly that this is an advocate's call, then give them the structured list of what is recorded so the conversation with the advocate is short |
| The apartment cannot be found in the register | A different registration regime | Go to Step 7 and identify the regime rather than reporting a failure |
| An entry appears that the references do not name | The register carries further note types prescribed by regulation | Say what the entry appears to be, say you cannot categorise it with confidence, and route it |
| The user has a printout and asks if it is official | Format and authenticity rules live on the registry's service pages | Do not assert a rule this skill could not verify. Route them to the registry to confirm the status of what they hold |
| The user wants to know what the property is worth | Outside the skill | Route to `israeli-property-appraisal` |
| A registered owner has died | The estate must be dealt with before transfer | State the blocker as a category and route to an advocate; do not advise on the succession route |
