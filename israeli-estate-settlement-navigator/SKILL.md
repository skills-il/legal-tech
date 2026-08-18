---
name: israeli-estate-settlement-navigator
description: "Operational project manager for settling an estate after a death in Israel. Use when someone has died and the family or estate administrator needs to know what to do and in what order: it builds a personalized dated bureaucratic timeline (first 72 hours, first 30 days, first year), a document-collection checklist, and ready-to-send bilingual Hebrew notification and account-closure letters. It covers the death certificate, the burial grant, the institution notification cascade, and the asset transfers that happen after the order. Do NOT use it to write or deposit a will or to obtain a succession order (צו ירושה) or probate order (צו קיום צוואה): route those to the skill israeli-wills-inheritance. Do NOT use it to check survivor-allowance or life-insurance eligibility: route those to israeli-survivor-benefits-navigator. For contested estates or foreign assets, state the facts and still recommend a licensed lawyer."
license: MIT
---

# Israeli Estate Settlement Navigator

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Problem

When someone dies in Israel, the family is grieving and, at the same time, is handed a maze of offices, forms, and phone numbers with no map. People visit the bank before they have the certified copies they need, wait months for a survivor allowance they were never told they had to actively claim, and pay for things the state already covers. This skill is the calm project manager: it turns the chaos into a dated to-do list, tells the user which office to visit in which order, and drafts the letters so nothing is missed and nothing is paid for twice.

## Instructions

You are an operational guide, not a lawyer and not a benefits calculator. Your job is to sequence the bureaucracy and generate paperwork. Ask only for what you need to personalize the plan, then produce the three deliverables. Never invent a form number, a fee, or a deadline: if you are unsure, point the user to the official source instead.

### What to ask first (keep it short)

1. Date of death, and did the death happen in Israel or abroad.
2. Was the deceased an Israeli resident.
3. Is there a known will, or is the family unsure.
4. What assets are involved at a high level (bank account, apartment, vehicle, pension, business).
5. Who is the user in relation to the deceased (spouse, child, named executor, other).

Use the answers to tailor the timeline and the checklist. Do not railroad: if the family already handled the burial, skip straight to the notification cascade.

### Deliverable 1: the personalized dated timeline

Anchor every milestone to the date of death. The helper `scripts/generate_timeline.py` computes the dates. Present it as three horizons.

**First 72 hours (burial and the first documents)**
- Obtain the הודעת פטירה (death notice) from the doctor or hospital that confirmed the death. This medical document is what lets the burial proceed; it is not the official certificate.
- Contact the Chevra Kadisha or the local religious council (or a civil-burial society) to arrange the burial. The burial grant (דמי קבורה) is paid by Bituach Leumi directly to the burial society, so basic burial is free to the family: the regulations bar the society from charging the family for the burial and the customary services.
- Do NOT tell the family that every charge is unlawful. The Bituach Leumi (Burial Grant) Regulations, 5736-1976 enumerate a closed list of cases where a burial society MAY lawfully charge on top of the grant. A service fee or other payment is permitted only for (regulation 3(a)) burial in one of the closed cemeteries listed in the annex to the agreement, burial in defined premium sections agreed between Bituach Leumi and the society, or burial in a grave plot the deceased purchased in their lifetime; and a further payment other than a service fee is permitted only for (regulation 4(a)) special costs of transferring the deceased from outside the society's area, a detour or stop requested by the family en route to the cemetery, or non-standard shrouds supplied at the family's request. Check the demand against that list: outside it, refuse; inside it, the charge is lawful.
- One thing the burial grant does NOT cover: the headstone (מצבה). Setting up the headstone is not part of the burial services funded by Bituach Leumi, so it is a separate cost the family pays privately (except in specific cases, such as a solitary deceased with no close relatives, where the state funds it). Do not let anyone imply the headstone is included in the free burial. Separately, tell whoever pays out of pocket that funeral, burial, and headstone costs rank FIRST among the estate's debts under section 104(a)(1) of the Succession Law, so the payer can normally be reimbursed from the estate ahead of every other creditor. Keep the receipts.
- If the family wants a non-religious burial, alternative civil burial (קבורה אזרחית חלופית) is a legal right and is offered by dedicated societies.

**First 30 days (registration, certificate, notification cascade)**
- Confirm the death is registered at Misrad HaPnim (Population and Immigration Authority). The doctor/hospital death notice feeds this; the official תעודת פטירה is then issued.
- Order the official death certificate. It is issued free of charge, and a first-degree relative can now download it immediately from the personal area on gov.il rather than waiting for the post. Order several certified copies anyway: banks, pension funds, insurers, and the Land Registry each want their own original or certified copy.
- Start from the government's own one-stop service rather than office by office. gov.il runs "ליווי לאחר פטירה (צעד אחר צעד)", an authenticated step-by-step service for first-degree relatives that downloads the death certificate, files and retrieves the succession or probate order, surfaces personally-matched benefits and rights, and runs the bank-account and insurance-policy locators. Send the user there first; it collapses several of the steps below.
- Find every account and policy before you start closing things. Two free government tools locate assets the family may not know about, by the deceased's ID:
  - **Har HaKesef (הר הכסף)**, run by the Ministry of Finance, is a search engine for lost/dormant pension savings, life-insurance policies, and bank accounts.
  - **Har HaBituach (הר הביטוח)**, run by the Capital Market, Insurance and Savings Authority, aggregates all of a person's insurance policies (life, health, pension, provident, vehicle, home) in one place.
  Run both before the cascade so no fund, policy, or account is missed.
- Work through the notification cascade below. Note that Misrad HaPnim forwards the death to many bodies automatically, so much of the cascade is confirmation and claiming, not first notice.
- If the family needs money NOW for the funeral, the headstone, or other death-related costs, do not assume they must wait for the order. Banks will generally release limited, reasonable sums from the deceased's account for immediate estate expenses before any order is produced, at the bank's discretion, with the surviving joint owner's consent, or against an indemnity letter signed by the potential heirs where all account owners have died. Ask the branch for this explicitly by name; it is rarely offered unprompted. (This dovetails with the debt priority above: these are the estate's first-ranking debts.)
- Cancel standing orders (הוראות קבע) for utilities and subscriptions with both the bank and the provider, so charges stop.
- Stop the deceased's OWN Bituach Leumi allowance. If the deceased received an old-age or disability allowance (קצבת זקנה / נכות), that personal allowance ends on death; only the amount that was due up to the date of death is still payable, and it is paid to the survivors, not for months after death. Make sure Bituach Leumi has stopped it so payments credited after death do not have to be sorted out later. (The separate death grant and survivor benefits belong to `israeli-survivor-benefits-navigator`.)
- If the deceased rented their home, notify the landlord, settle the estate's liability for the remaining rent, and terminate the lease so rent does not keep accruing against the estate.

**First year (orders, asset transfer, benefits)**
- The succession order (צו ירושה, when there is no will) or probate order (צו קיום צוואה, when there is a will) is obtained from the Registrar of Inheritance Affairs. That process is out of scope here: route the user to the `israeli-wills-inheritance` skill.
- Once the order is in hand, do the asset transfers (see the transfer checklist). A sole account in the deceased's name (and the deceased's share of any account with no survivorship clause) stays frozen until the order is presented; a joint account where the co-owners signed a survivorship clause in advance stays accessible to the surviving co-owner (see the bank note below).
- Survivor benefits must be actively claimed; they are not automatic. Route eligibility and amounts to `israeli-survivor-benefits-navigator`.

### Deliverable 2: the document-collection checklist

Generate it with `scripts/checklist.py` or use `references/institution-checklist.md`. The core documents the family will reuse everywhere:

| Document (He) | Document (En) | Where it comes from |
|---|---|---|
| תעודת פטירה (מספר עותקים) | Death certificate (several certified copies) | Population and Immigration Authority (free) |
| תעודת זהות של הנפטר | Deceased's national ID | Family / to be surrendered per office rules |
| תעודות זהות של היורשים | Heirs' national IDs | Family |
| צו ירושה / צו קיום צוואה | Succession order / probate order | Registrar of Inheritance Affairs (out of scope: `israeli-wills-inheritance`) |
| פירוט חשבונות, פנסיה, ביטוחים | List of accounts, pensions, insurance | Bank / funds / mislaka |
| נסח טאבו / הסכמי הלוואה ומשכנתה | Land Registry extract / loan and mortgage agreements | Land Registry / lenders |

### Deliverable 3: the notification and closure letters

Use the bilingual templates in `references/notification-letter-templates.md` (bank account closure, standing-order cancellation, utility/subscription cancellation, employer notification). Fill in the deceased's details, attach a certified death certificate copy, and, where the institution requires it, note that the succession/probate order will follow.

### The notification cascade (rough order)

| # | Institution (He) | Institution (En) | Why / note |
|---|---|---|---|
| 1 | ביטוח לאומי | Bituach Leumi | Often learns from Misrad HaPnim, but survivor benefits must be actively claimed |
| 2 | בנקים | Banks | Sole accounts (and a joint account with no survivorship clause) freeze until the order; a joint account with a pre-signed survivorship clause stays open to the surviving co-owner; cancel standing orders |
| 3 | קופות גמל / פנסיה / חברות ביטוח | Pension, gemel, insurers | Beneficiary payouts and claims |
| 4 | מעסיק | Employer | Final salary, unused-vacation redemption, and severance. Note the recipient: under section 5 of the Severance Pay Law, 5723-1963 severance on death is paid by the employer to the statutory שאירים, a defined set (spouse including a common-law partner living with them, and a dependent child; failing those, dependent children and parents, and siblings who lived in the home for at least twelve months and were wholly dependent). Those are NOT necessarily the יורשים, and the money is not paid out of the estate |
| 5 | קופת חולים | HMO (kupat cholim) | Deregister the member |
| 6 | חברות תשתית (חשמל, מים, גז) | Utilities (electricity, water, gas) | Transfer or close the account holder |
| 7 | עירייה / ארנונה | Municipality / arnona | Change holder; a survivor-allowance-linked discount may apply |
| 8 | משרד הרישוי | Licensing Bureau (vehicle) | Vehicle transfer after the order |
| 9 | סלולר / אינטרנט / מנויים דיגיטליים | Cellular, internet, digital subscriptions | Cancel to stop recurring charges |
| 10 | משטרה / האגף לרישוי כלי ירייה | Israel Police / firearms licensing division | The deceased's personal firearms license lapses on death; deal with any licensed weapon (see the firearm note below) |

### Asset-transfer checklist (only AFTER the order)

- Bank funds and securities: present the succession or probate order to release the frozen accounts.
- Real estate: re-register at the Land Registry (טאבו / לשכת רישום המקרקעין) with the order. Reassure the family up front: Israel does NOT levy an estate or inheritance tax, so simply inheriting is not taxed. Receiving real estate by inheritance is not treated as a taxable sale, so the heirs pay no purchase tax and no betterment tax at the moment of inheritance. A tax question (מס שבח / betterment tax) can arise only later, if and when an heir SELLS the inherited property.
- Vehicle: transfer at Misrad HaRishui with the death certificate and the order (a surviving spouse may have a simplified route). Warning before anyone drives the car in the interim: the licensing bureau will renew the vehicle license (רישיון רכב) for the relatives for ONE further year from its expiry, to give the family time to regularize the registration, and the annual license fee (אגרת רישוי) still has to be paid. The hard stop is that no second renewal is issued: if the year passes without the transfer being completed, the licensing authority will not reissue the license at all. Transferring registration by inheritance does not add a "hand" (יד) to the vehicle's ownership count. Because the mandatory insurance (ביטוח חובה) and license are tied to the registered owner, the car may be uninsured or unlawful to drive until things are regularized. Confirm valid insurance with the insurer before anyone drives it.

**Bank note (joint vs sole accounts).** The blanket "everything is frozen" is not quite right. A sole account in the deceased's name is frozen once the bank learns of the death and is released only against the order. A joint account is also frozen by default, UNLESS the co-owners signed a survivorship clause (טופס "אריכות ימים" / סעיף "היוותרות בחיים") in advance: with that clause the surviving co-owner can keep operating the account for routine activity before the order. Two caveats: the clause must have been signed in advance (you cannot add it after the death), and it does not override inheritance law, so a court may later require the survivor to return amounts that belong to the heirs.

**Safe-deposit box (כספת).** A safe-deposit box is treated like the account: a box in the deceased's sole name (or a jointly-held box with no advance arrangement) is inaccessible until the order is presented. This creates a chicken-and-egg problem when the original will is kept inside the box, because opening it may itself need the order or a registrar/court route. Raise this early if the family suspects the will is in a bank box.

**Firearm (כלי ירייה).** The deceased's personal firearms license lapses on death, so a licensed weapon cannot simply stay in the home. Section 5(b)(5) of the Firearms Law, 5709-1949 exempts an heir or estate administrator from the licence requirement for exactly 30 days from the death: that is a grace period, and holding the weapon after it without a licence is an offence. An heir may keep it beyond that only after it is temporarily deactivated by a licensed dealer through the licensing bureau. If no one wants it, a family member surrenders it to the police within those 30 days, bringing the weapon, the death certificate, and the deceased's firearms license; the police issue a deposit confirmation that is sent to the firearms licensing division.

**Mortgage life insurance (ביטוח חיים ללווים).** Most Israeli mortgages carry bundled borrower life insurance, whose purpose is to guarantee the bank receives the entire remaining loan balance if the borrower dies. Before anyone keeps paying the mortgage out of pocket, check whether the loan had this cover and notify the lender and the insurer: the policy may pay off the outstanding balance, so the heirs and the surviving spouse do not have to keep paying it or sell the home.

### The debts question (reassure correctly)

Heirs never pay the deceased's debts from their own pocket: liability is capped by the value of estate assets, never by the heir's personal wealth. This is the Succession Law, 5725-1965, Chapter Six (sections 126 to 134). Funeral, burial, and gravestone costs rank first in the debt priority order under section 104(a)(1), ahead of the costs of the orders themselves and ahead of the deceased's ordinary creditors.

**But do not give the flat reassurance, because the cap depends on HOW the estate was divided.** Three regimes:

- **Before division** (section 126): heirs are not liable for estate debts at all except out of estate assets.
- **Divided AFTER creditors were invited** under section 99 or 123 and the then-known debts were settled (section 127(a)): an heir is liable for an unsettled debt only if it is proved they knew of it at the time of division, and only up to the value of **what that heir received**.
- **Divided WITHOUT inviting creditors** (section 128(a)): each heir is liable for the unsettled debts up to the value of the **whole estate** at the time of division, not merely their own share. Only an heir who proves they did not know of a particular debt drops back to the value of what they received, and section 128(b) puts the burden of proving value on the heir, not on the creditor. Concealing assets or a debt (section 129) exposes the heir to the whole estate's value regardless.

So the protective advice is procedural, not reassurance: invite the creditors before dividing, settle the known debts, and keep the division schedule. A family that quietly splits the money is in the section 128 regime. Section 133 lets a court relieve an heir who acted in good faith and received little, but that is a discretionary remedy, not a right. For a contested claim, an insolvent estate, or any division where debts are suspected, state these facts and still recommend a licensed lawyer.

### What this skill does NOT cover (say so, do not improvise)

Four things a family in this situation commonly needs are outside this skill, and the
failure mode is not silence but improvisation: an agent that does not know the procedure
will invent one. Name the gap and route it.

- **The deceased's tax position.** A final-year income-tax return for the deceased, tax on
  income the estate earns after the death, and closing the file of a deceased who was
  self-employed (עוסק) at מס הכנסה, מע"מ, and ביטוח לאומי. These carry their own deadlines
  and penalties. This skill does not state those procedures. Send the user to the Tax
  Authority and to a רואה חשבון or יועץ מס. Do not guess a form number or a filing window.
- **Appointing an estate administrator (מנהל עיזבון).** Typically raised where the estate is
  contested, complex, has business assets, or cannot be settled by the heirs between
  themselves. This skill does not run that application. Route to a licensed lawyer.
- **Minor heirs, absent heirs, and heirs abroad.** Distribution touching a minor's share
  engages the guardianship regime and the אפוטרופוס הכללי. Do not tell the family they can
  simply divide. Route to a licensed lawyer.
- **A deceased who was a foreign resident, or an estate holding assets abroad.** Route to a
  licensed lawyer, as the domain checklist already records.

State the facts you do know, name which of these applies, and hand off. A confident wrong
procedure in this area costs the family more than an honest "this skill does not cover it".

## Bundled Resources

- `references/domain-checklist.md`: the full Must-cover / Should-cover / Out-of-scope map used to build this skill.
- `references/institution-checklist.md`: the institution-by-institution notification and document table.
- `references/notification-letter-templates.md`: ready-to-fill bilingual Hebrew letter templates.
- `scripts/generate_timeline.py`: prints a dated 72h / 30-day / 1-year task timeline from a date of death.
- `scripts/checklist.py`: emits the document-collection checklist, optionally tailored by asset type.

## Recommended MCP Servers

| MCP | What it's for |
|---|---|
| kolzchut | Pulling the up-to-date Kol-Zchut rights pages for bereavement, burial, and estate procedures |
| israel-vehicles | Looking up the deceased's vehicle details before a Misrad HaRishui transfer |
| nadlan | Checking real-estate records before a Land Registry (Tabu) re-registration |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Bituach Leumi: burial grant | https://www.btl.gov.il/benefits/dmaykvura/Pages/zacautKvura.aspx | Who is eligible and that the family pays nothing for standard burial |
| gov.il: death certificate | https://www.gov.il/he/service/death_certificate | How to order the free certificate and additional copies |
| gov.il: death registration | https://www.gov.il/he/service/death_registration | How the death is registered at Misrad HaPnim |
| Kol-Zchut: heirs rights guide | https://www.kolzchut.org.il/he/זכותון_ליורשים_ולקרובי_אדם_שנפטר_לתקופה_הסמוכה_למוות | The notification cascade and order of steps |
| Kol-Zchut: settling the deceased's debts | https://www.kolzchut.org.il/he/הסדרת_חובות_אדם_שנפטר | Heir liability limited to estate value; debt priority |
| Succession Law, 5725-1965 (full text) | https://www.nevo.co.il/law_html/law00/72178.htm | Section 104(a)(1) debt priority; sections 126 to 134 heir liability |
| Legal Capacity and Guardianship Law, 5722-1962 | https://www.nevo.co.il/law_html/law00/70325.htm | Section 32kd(b): the 90-day residual authority of an enduring power of attorney |
| Bituach Leumi (Burial Grant) Regulations, 5736-1976 | https://www.nevo.co.il/law_html/law01/039_109.htm | Regulations 3(a) and 4(a): the closed list of lawful burial-society charges |
| Firearms Law, 5709-1949 | https://www.nevo.co.il/law_html/law00/72225.htm | Section 5(b)(5): an heir may hold the weapon licence-free for 30 days from the death |
| gov.il: post-death accompaniment (one-stop) | https://www.gov.il/he/service/post-death-accompaniment | Certificate download, order filing, matched benefits, account and policy locators |
| gov.il: vehicle transfer after death | https://www.gov.il/he/service/modification_registration_vehicle_following_death | Vehicle license lapses on death; one-year renewal for relatives; confirm insurance before driving |
| Har HaKesef (Ministry of Finance) | https://itur.mof.gov.il/ | Locate the deceased's lost pension savings, life-insurance policies, and bank accounts |
| Har HaBituach (Capital Market Authority) | https://harb.cma.gov.il/ | Locate all of the deceased's insurance policies and pension/provident savings |

## Gotchas

- Do not confuse the two orders: צו ירושה is for an estate with no will; צו קיום צוואה is for an estate with a will. Using the wrong term sends the family down the wrong application.
- Do not tell the family they are personally on the hook for the deceased's debts, and do not give the opposite flat reassurance either. They never pay from their own money, but an estate divided without inviting the creditors exposes each heir up to the value of the WHOLE estate, with the burden of proving value on the heir. Give the procedural advice: invite creditors, settle known debts, then divide.
- Do not tell the family they must pay the burial society, and do not tell them every charge is unlawful either. The grant covers standard burial directly, but the regulations list six specific cases where a society may lawfully charge on top (closed cemeteries, agreed premium sections, a pre-purchased plot, out-of-area transfer, a requested detour, non-standard shrouds). Check the demand against the list instead of refusing on principle.
- Do not say "notify Bituach Leumi and the survivor allowance will start." Bituach Leumi often already knows of the death, but survivor benefits must be actively claimed, and eligibility belongs to `israeli-survivor-benefits-navigator`.
- Do not hand over a generic global "after a death" checklist. The value here is the Israeli, institution-specific sequence (Misrad HaPnim, Bituach Leumi, Chevra Kadisha, the Registrar of Inheritance Affairs, the Land Registry, Misrad HaRishui).
- Do not tell the family they owe an "inheritance tax" or "estate tax": Israel does not levy one. Do reassure them, but note that selling an inherited property later can trigger betterment tax.
- Do not say all bank accounts are frozen. A joint account with a pre-signed survivorship clause stays accessible to the surviving co-owner; only sole accounts (and joint accounts without that clause) freeze until the order.
- Do not let anyone drive the deceased's car on the assumption it is still insured. The license lapses on death and the mandatory insurance is tied to the owner; confirm cover with the insurer first.
- Do not assume the free burial includes the headstone. The headstone (מצבה) is a separate, family-paid cost.

## Troubleshooting

- The bank refuses to release funds: for a sole account that is expected, and it stays frozen until the succession or probate order is presented. Route the order process to `israeli-wills-inheritance`. But if it is a joint account and the co-owners signed a survivorship clause (אריכות ימים / היוותרות בחיים) in advance, the surviving co-owner should be able to keep operating it for routine activity before the order; if the branch still blocks it, point them to that signed clause.
- The family only has one death certificate and offices keep asking for originals: order more certified copies (they are free) rather than photocopying.
- An enduring power of attorney (ייפוי כוח מתמשך) that the deceased signed: do not tell the family it is simply dead. It does expire on death under section 32kb(2) of the Legal Capacity and Guardianship Law, 5722-1962, but section 32kd(b) then gives the attorney for property matters a residual authority, for up to 90 days from the death and without applying to court, to pay ongoing charges for services rendered to the deceased or relating to their property, to pay reasonable burial and mourning expenses, and to run a rented property or a business that needs ongoing management. It applies unless the principal directed otherwise and only while no one else is lawfully authorized, so it ends the moment an estate administrator is appointed or the succession or probate order is produced. In the first weeks this is often the only lawful way to keep the mortgage paid and the shop open.
- The estate looks like it owes more than it holds: reassure that heirs are not personally liable beyond the estate value, then recommend a licensed lawyer for an insolvent or contested estate.
