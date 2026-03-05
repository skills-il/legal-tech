---
name: israeli-rental-agreements
description: >-
  Guide users through Israeli rental agreements, tenant and landlord rights,
  and lease negotiation. Use when user asks about rental contracts (chozeh
  schirut), tenant rights, landlord obligations, deposits (arancia), rent
  increases, index-linked rent (hatzmada la'madad), the Fair Rental Law 2017,
  eviction procedures, or common red flags in Israeli leases. Covers essential
  contract elements, guarantees, dispute resolution, and the Tenant Protection
  Law. Do NOT use for commercial leases, property purchase transactions, or
  mortgage advice.
license: MIT
compatibility: No network required. Works offline with reference data.
metadata:
  author: skills-il
  version: 1.0.0
  category: legal-tech
  tags:
    he:
      - שכירות
      - חוזה
      - זכויות-דייר
      - משכיר
      - נדלן
      - ישראל
    en:
      - rental
      - lease
      - tenant-rights
      - landlord
      - real-estate
      - israel
  display_name:
    he: חוזי שכירות ישראליים
    en: Israeli Rental Agreements
  display_description:
    he: מדריך לחוזי שכירות, זכויות דיירים ומשכירים בישראל
    en: >-
      Guide to Israeli rental agreements, tenant and landlord rights, Fair
      Rental Law, deposits, and lease negotiation.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# Israeli Rental Agreements

## Instructions

### Step 1: Israeli Rental Law Framework
Israel's residential rental market is governed by several key laws:

| Law | Hebrew | Year | Key Provisions |
|-----|--------|------|----------------|
| Fair Rental Law (Chok Schirut Hogenet) | חוק שכירות הוגנת | 2017 | Minimum habitation standards, landlord obligations |
| Tenant Protection Law (Chok Haganat HaDayar) | חוק הגנת הדייר | 1972 | Applies to pre-1968 protected tenancies (rare today) |
| Contract Law (General Part) (Chok HaChozim) | חוק החוזים (חלק כללי) | 1973 | General contract principles |
| Sale Law (Chok HaMecher) | חוק המכר | 1968 | Implied terms for transactions |
| Pledge Law (Chok HaMashkon) | חוק המשכון | 1967 | Governs deposit and guarantee mechanisms |

**Fair Rental Law 2017 key provisions:**

| Provision | Details |
|-----------|---------|
| Minimum habitation standards (tna'ey dira tikniyim) | Property must have functioning plumbing, electricity, ventilation, structural integrity |
| Landlord repair obligations | Landlord must fix structural issues, plumbing, electrical systems |
| Tenant repair obligations | Tenant responsible for day-to-day maintenance and minor repairs |
| Maximum deposit | Cannot exceed 3 months' rent (for bank guarantee or checks) |
| Written contract required | Oral agreements technically valid but strongly inadvisable |
| Termination notice | Must follow contract terms; typically 60-90 days |

**Important:** The Fair Rental Law applies to residential rentals only. There is no statutory cap on rent amounts in Israel. Landlords set rent based on market conditions.

### Step 2: Essential Contract Elements
Every Israeli rental contract (chozeh schirut) should include these elements:

| Element | Hebrew | What to Verify |
|---------|--------|---------------|
| Landlord details (Mashkir) | משכיר | Full name, Teudat Zehut number, contact information |
| Tenant details (Socher) | שוכר | Full name, Teudat Zehut number, contact information |
| Property address (Ktovet HaNechess) | כתובת הנכס | Exact address, apartment number, floor |
| Property description | תיאור הנכס | Number of rooms, included fixtures, parking, storage |
| Lease term (Tkufat HaSchirut) | תקופת השכירות | Start date, end date, renewal option (optzia) |
| Monthly rent (Dmey Schirut) | דמי שכירות | Amount in NIS, payment date, payment method |
| Deposit/Guarantee (Arancia/Pikadon) | ערבות/פיקדון | Type, amount, return conditions |
| Arnona responsibility | ארנונה | Who pays municipal tax (usually tenant) |
| Va'ad Bayit (Building Committee fees) | ועד בית | Who pays building maintenance fees |
| Utilities (Cheshbonot) | חשבונות | Electricity, water, gas responsibility |
| Maintenance obligations | חובות תחזוקה | Which repairs are landlord vs. tenant responsibility |
| Termination clause (Si'uf Biitul) | סעיף ביטול | Notice period, early termination conditions |
| Option to renew (Optzia) | אופציה | Terms for extending the lease |

**Standard lease term patterns in Israel:**

| Pattern | Duration | Common Usage |
|---------|----------|-------------|
| Fixed term (Tkufa Kvua) | 12 months | Most common residential lease |
| Fixed + Option (Tkufa + Optzia) | 12 months + 12 months option | Very common, gives flexibility |
| Short term | 3-6 months | Sublets, temporary housing |
| Long term | 2-5 years | Less common, sometimes with rent adjustments |

### Step 3: Deposits and Guarantees
Israeli rental deposits (arancia or pikadon) are the most critical financial element of a lease:

| Guarantee Type | Hebrew | Description | Risk Level for Tenant |
|---------------|--------|-------------|----------------------|
| Bank Guarantee (Aruvah Bankai't) | ערבות בנקאית | Bank issues guarantee letter, funds frozen in your account | Low (controlled release) |
| Post-Dated Checks (Hamcha'ot Dchuyot) | המחאות דחויות | Blank or post-dated checks held by landlord | Medium (can be cashed) |
| Cash Deposit (Pikadon Mezuman) | פיקדון מזומן | Cash or bank transfer held by landlord | Medium (risk of non-return) |
| Promissory Note (Shtar Hon) | שטר הון | Legal promissory note for a set amount | High (enforceable as debt) |
| Personal Guarantors (Arevim) | ערבים | Third parties guarantee obligations | Varies (personal liability for guarantors) |

**Deposit amounts and rules:**

| Rule | Details |
|------|---------|
| Typical deposit | 1-3 months' rent |
| Maximum allowed (Fair Rental Law) | 3 months' rent for guarantee instruments |
| Return timeline | Within 60 days of lease end, per Fair Rental Law |
| Deduction conditions | Documented damages beyond normal wear, unpaid rent, unpaid utilities |
| Dispute over deductions | Landlord must provide itemized list; tenant can contest in court |

**What to insist on for deposit protection:**
- Get a signed receipt (kabala) for any deposit paid
- Photograph the entire apartment at move-in (before and after, with timestamps)
- Document pre-existing damage in writing, attached to the contract (nispach l'chozeh)
- Ensure the contract specifies exact return conditions and timeline
- For bank guarantee: verify the guarantee terms match the contract terms
- Never provide a shtar hon (promissory note) without legal advice

### Step 4: Rent Increases and Index Linking
Understanding how rent changes work in Israel:

| Mechanism | Hebrew | Description |
|-----------|--------|-------------|
| Index-linked rent (Hatzmada La'Madad) | הצמדה למדד | Rent adjusts based on Consumer Price Index (CPI) changes |
| Fixed increase clause | סעיף העלאה קבוע | Predetermined increase percentage at renewal |
| Market adjustment | התאמה לשוק | Renegotiation at lease renewal based on market rates |
| No increase (during lease term) | ללא העלאה בתקופת החוזה | Landlord cannot raise rent during active lease unless contract allows |

**Index-linking (Hatzmada) details:**

| Aspect | Details |
|--------|---------|
| What is indexed | Rent adjusts to reflect changes in the CPI (Madad HaMechirim LaTzarchan) |
| Published by | Central Bureau of Statistics (Lishkat HaStatistika HaMerkazit) |
| Frequency | Usually calculated annually or at lease renewal |
| Direction | Can go up or down (deflation reduces rent) |
| Typical clause | "Rent will be adjusted according to the change in the CPI from [base month] to [adjustment month]" |
| Base index | The CPI value at the contract start date |

**Key rules on rent increases:**

| Scenario | Rule |
|----------|------|
| During active lease | Landlord CANNOT increase rent unless the contract explicitly permits it |
| At lease renewal (with option) | If option clause specifies terms, those terms apply |
| Between lease terms (new contract) | No legal cap; landlord can set any market rate |
| With index-linking clause | Automatic adjustment per CPI; no separate negotiation needed |
| Without index-linking | Rent stays fixed for the lease term |

### Step 5: Tenant Rights and Landlord Obligations
Rights and obligations under Israeli law:

**Tenant rights (Zkhuyot HaSocher):**

| Right | Hebrew | Details |
|-------|--------|---------|
| Habitable property | נכס ראוי למגורים | Property must meet minimum standards (plumbing, electricity, structure) |
| Privacy (Pratiyut) | פרטיות | Landlord must give notice before entering (typically 24 hours) |
| Quiet enjoyment (Hana'a Shketah) | הנאה שקטה | Landlord cannot interfere with normal use of property |
| Structural repairs | תיקונים מבניים | Landlord responsible for structural, plumbing, electrical repairs |
| Deposit return | החזרת פיקדון | Right to full deposit return within 60 days if no valid deductions |
| Written notice for termination | הודעה כתובה | Landlord must provide written notice per contract terms |
| Subletting (if permitted) | השכרת משנה | Subject to contract terms; some contracts prohibit |

**Landlord obligations (Chovot HaMashkir):**

| Obligation | Details |
|------------|---------|
| Deliver habitable property | Property must be in the condition described in the contract |
| Maintain structural elements | Roof, exterior walls, plumbing, electrical wiring |
| Fix pre-existing defects | Known defects must be disclosed and remedied |
| Provide receipts for rent | Written receipt (kabala) for each payment |
| Return deposit per terms | Within 60 days, with itemized deductions if any |
| Register contract with tax authority | Landlord must report rental income to Mas Hachnasa |

**Tenant obligations (Chovot HaSocher):**

| Obligation | Details |
|------------|---------|
| Pay rent on time | Per contract schedule |
| Pay utilities and Arnona | Unless contract states otherwise |
| Maintain property (day-to-day) | Minor repairs, cleanliness, prevent damage |
| No unauthorized modifications | Cannot make structural changes without permission |
| Return property in original condition | Normal wear and tear excepted (blai savir) |
| Notify landlord of needed repairs | Report structural issues promptly |

### Step 6: Termination, Eviction, and Dispute Resolution
How leases end and disputes are resolved in Israel:

| Termination Type | Hebrew | Process |
|-----------------|--------|---------|
| Natural expiry (Siyum Tkufa) | סיום תקופה | Lease ends on end date; tenant vacates or renews |
| Mutual agreement (Haskama Hadadit) | הסכמה הדדית | Both parties agree to early termination |
| Tenant early termination | ביטול מוקדם על ידי השוכר | Per contract terms; may require finding replacement tenant |
| Landlord eviction (Pinui) | פינוי | Requires legal grounds and court order |
| Breach of contract (Hafarat Chozeh) | הפרת חוזה | Non-payment, property damage, illegal use |

**Eviction process (Pinui):**

| Step | Details | Timeline |
|------|---------|----------|
| 1. Written notice (Hoda'a) | Landlord sends formal written notice | Per contract (60-90 days typical) |
| 2. Attempt resolution | Negotiate or mediate | During notice period |
| 3. File lawsuit (Tvi'a) | Small claims or magistrate court | If tenant refuses to vacate |
| 4. Court hearing (Diyun) | Both parties present case | Court schedules hearing |
| 5. Court order (Tzav Pinui) | Judge issues eviction order | After hearing |
| 6. Enforcement (Hotza'a LaPo'al) | Execution office enforces if tenant still refuses | Post-order |

**Legitimate grounds for eviction:**
- Non-payment of rent (typically after notice and grace period)
- Significant property damage
- Illegal use of property
- Breach of material contract terms
- Lease term expired and tenant refuses to vacate
- Landlord needs property for personal use (subject to conditions)

**Dispute resolution options:**

| Method | Hebrew | Best For | Cost |
|--------|--------|----------|------|
| Direct negotiation | משא ומתן ישיר | Minor disputes, communication issues | Free |
| Mediation (Gishur) | גישור | Moderate disputes, relationship preservation | Low-moderate |
| Small Claims Court (Tvi'ot Ktanot) | תביעות קטנות | Claims up to NIS 38,900 | Filing fee (~1% of claim) |
| Magistrate Court (Beit Mishpat Shalom) | בית משפט שלום | Larger claims, eviction orders | Court fees + potential lawyer |
| Rent Tribunal (if applicable) | ועדת שכירות | Protected tenancies (pre-1968, rare) | Minimal |

### Step 7: Common Red Flags in Rental Contracts
Warning signs to watch for when reviewing a lease:

| Red Flag | Hebrew Term | Why It's Problematic |
|----------|------------|---------------------|
| No written contract | ללא חוזה כתוב | No legal protection, hard to prove terms |
| Shtar Hon (promissory note) required | דרישת שטר הון | Can be enforced as debt without court hearing |
| Deposit exceeds 3 months | פיקדון מעל 3 חודשים | Exceeds Fair Rental Law maximum |
| No itemized property condition report | ללא פרוטוקול מצב דירה | Landlord can claim pre-existing damage is tenant's fault |
| Waiver of tenant rights clause | סעיף ויתור על זכויות | May be legally void but creates confusion |
| Automatic renewal without notice | חידוש אוטומטי ללא הודעה | Tenant may be locked into unwanted extension |
| Landlord retains unlimited entry rights | זכות כניסה בלתי מוגבלת | Violates privacy rights |
| Tenant pays for all repairs | השוכר משלם לכל התיקונים | Landlord shirking legal obligation for structural repairs |
| No option clause | ללא סעיף אופציה | Less flexibility, potential rent hike at renewal |
| Penalty clause for early termination | קנס על ביטול מוקדם | May be enforceable; negotiate reasonable terms instead |
| Unclear Arnona responsibility | אחריות ארנונה לא ברורה | Can lead to surprise bills |
| No receipts for payments | ללא קבלות | Difficult to prove payments were made |

**Before signing any lease:**
- Have a lawyer or knowledgeable advisor review the contract
- Photograph the entire apartment and document existing condition
- Verify the landlord's ownership via Tabu (Land Registry) extract or Rasham HaChevrut
- Check Arnona classification and amount with the local municipality (iriya)
- Confirm building committee (va'ad bayit) fees and what they cover
- Meet the neighbors if possible to learn about the building

## Examples

### Example 1: Reviewing a Lease Before Signing
**Input:** "I got a rental contract, what should I check before signing?"
**Output:** Walk through the essential checklist: verify landlord identity and ownership (request Tabu extract), check all required elements are present (addresses, dates, amounts, deposit terms), review the maintenance clause (landlord should cover structural repairs), check for index-linking (hatzmada) terms, verify deposit type and amount (should not exceed 3 months), look for an option clause for renewal, check the early termination clause, and flag any red flags (shtar hon requirement, waiver of rights, unlimited landlord entry). Recommend photographing the apartment and attaching a condition report (nispach matzav dira) to the contract.

### Example 2: Deposit Dispute at Lease End
**Input:** "My landlord won't return my deposit, claims there's damage I didn't cause."
**Output:** Explain tenant rights: the landlord must return the deposit within 60 days per the Fair Rental Law. Ask if the tenant documented the apartment condition at move-in (photos, written report). If yes, this is evidence against false claims. The landlord must provide an itemized list of claimed damages with cost estimates. The tenant can dispute deductions and demand receipts for any repair work. If unresolved, the tenant can file a claim in small claims court (tvi'ot ktanot) for amounts up to NIS 38,900. Recommend sending a formal written demand (mikhtav drishah) via registered mail before going to court.

### Example 3: Rent Increase During Lease
**Input:** "My landlord wants to raise my rent in the middle of the lease, can they do that?"
**Output:** Explain that during an active lease term, the landlord CANNOT increase rent unless the contract explicitly includes a provision for it (such as a hatzmada clause linking rent to the CPI). If no such clause exists, the rent is fixed for the entire lease period. At renewal or between lease terms, the landlord can propose a new rent amount, and the tenant can negotiate or choose not to renew. If the contract has an option clause, the renewal terms (including rent) are usually specified in that clause.

### Example 4: Early Termination by Tenant
**Input:** "I need to break my lease early, what are my options?"
**Output:** Review the contract's early termination clause (si'uf biitul mukdam). Common scenarios: (1) If the contract requires finding a replacement tenant, start searching immediately and notify the landlord in writing. (2) If there is a penalty clause, negotiate a reduced penalty if possible. (3) If the landlord is in breach (failed to make required repairs, violated privacy), the tenant may have grounds to terminate without penalty. (4) Attempt mutual agreement (haskama hadadit) with the landlord. Send all communications in writing (email or registered mail) and keep copies. Note that simply vacating without following the contract terms can result in forfeiting the deposit and potential legal claims.

## Bundled Resources

### References
- `references/contract-checklist.md` -- Detailed checklist of every clause to verify in an Israeli rental contract, organized by section (parties, property, lease term, rent, deposits, maintenance, utilities, termination). Includes Hebrew terms, common pitfalls, and red flags. Consult when a user is reviewing or negotiating a rental contract.
- `references/fair-rental-law-summary.md` -- Summary of the Fair Rental Law 2017 (Chok Schirut Hogenet) including minimum habitation standards, landlord and tenant obligations, deposit limitations, termination rules, and enforcement options. Consult when a user asks about tenant rights, landlord obligations, or what the Fair Rental Law covers.

### Scripts
- `scripts/rent-index-calculator.py` -- Calculates rent adjustment based on CPI index linking (hatzmada la'madad). Given original rent, start date, and current date, calculates the adjusted rent using historical CPI data. Run: `python scripts/rent-index-calculator.py --help`

## Troubleshooting

### Error: "Landlord refuses to provide a written contract"
Cause: Some landlords, particularly in informal arrangements, avoid written contracts to evade tax reporting.
Solution: Never rent without a written contract. A verbal agreement provides minimal legal protection and makes it nearly impossible to prove lease terms in a dispute. The lack of a written contract is a significant red flag. If the landlord insists, consider finding a different property. If already in a verbal arrangement, document all communications (emails, messages) and request a written contract immediately.

### Error: "Landlord enters the apartment without notice"
Cause: Some landlords believe property ownership gives unlimited access rights.
Solution: Tenants have a legal right to privacy. The landlord must provide reasonable notice (typically 24 hours) before entering, except in genuine emergencies (water leak, fire). Send the landlord a written notice citing the right to quiet enjoyment (hana'a shketah) under Israeli law. If the behavior continues, this may constitute grounds for early termination or a complaint to the police for trespassing (hasagat gvul).

### Error: "Contract requires a shtar hon (promissory note) as guarantee"
Cause: Some landlords prefer shtar hon because it is easily enforceable without a court hearing.
Solution: A shtar hon is a high-risk guarantee instrument for tenants. It can be submitted to the execution office (Hotza'a LaPo'al) and enforced as a debt without a full court process. Strongly recommend negotiating for a bank guarantee (aruvah bankai't) instead, which offers controlled release conditions. If the landlord insists on a shtar hon, consult a lawyer before signing. At minimum, ensure the contract clearly limits the conditions under which the shtar hon can be used.
