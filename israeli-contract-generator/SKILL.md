---
name: israeli-contract-generator
description: >-
  Generate legally-informed contract drafts compliant with Israeli law including
  rental agreements, freelancer contracts, NDAs, SaaS terms, and employment
  agreements. Use when a user asks to draft, review, or create a contract for
  Israeli parties. Covers Chok HaChozim, Chok HaSchirut, Chok Hagnat HaTzarchan,
  freelancer vs employee tests, and NDA enforceability under Israeli case law.
license: MIT
metadata:
  author: skills-il
  version: 1.0.0
  tags:
    he:
      - חוזים
      - הסכם-שכירות
      - עצמאי
      - סודיות
      - משפט-ישראלי
      - הגנת-צרכן
    en:
      - contracts
      - rental-agreement
      - freelancer
      - nda
      - israeli-law
      - consumer-protection
  display_name:
    he: מחולל חוזים ישראלי
    en: Israeli Contract Generator
  display_description:
    he: >-
      יצירת טיוטות חוזים בהתאם לדין הישראלי כולל שכירות, פרילנס,
      הסכמי סודיות ותנאי שירות
    en: >-
      Generate legally-informed contract drafts under Israeli law including rental
      agreements, freelancer contracts, NDAs, and SaaS terms of service
---

# Israeli Contract Generator

## Instructions

### Step 1: Identify Contract Type

When a user asks to draft a contract, classify the request:

| Contract Type | Primary Law | Key Considerations |
|--------------|------------|-------------------|
| Rental (residential) | Chok HaSchirut (Tenant Protection), Chok Schirut V'She'ila 5731-1971 | Unprotected tenancy rules, deposit limits, exit clauses |
| Rental (commercial) | Chok HaChozim (Takanot Klaliyot), 5733-1973 | Freedom of contract, index-linked rent |
| Freelancer/Contractor | Chok HaChozim + labor law tests | Kablan Atzmai vs employee distinction |
| Employment | Chok HaChozim + all labor laws | Must meet statutory minimums |
| NDA | Chok Avgat Patentim 5727-1967, case law | Trade secret protection, reasonable scope |
| SaaS/Terms of Service | Chok Hagnat HaTzarchan 5741-1981 | Standard contract rules (chozeh achid) |
| Partnership | Pkudat HaShutafuyot (Nusach Chadash) 5735-1975 | Profit sharing, liability |
| Sales | Chok HaMecher 5728-1968 | Warranty, delivery, risk transfer |

### Step 2: Gather Required Information

For each contract type, collect:

**Rental Agreement (Hozeh Schirut):**
- Parties: landlord (maskhir) and tenant (sokher) full names and ID numbers
- Property address and description (gush, chelka if available)
- Monthly rent amount and payment method
- Lease period (start and end dates)
- Security deposit (pikadon) amount (market standard: 1-3 months' rent)
- Guarantees: bank guarantee (arva bankit), guarantors (arevim), or promissory notes (shtarot chov)
- Option to extend (optzia le'ha'arcaha) terms
- Maintenance responsibilities (achriyut le'tikun)
- Exit clause conditions (tnai yetzia)

**Freelancer Agreement (Hozeh Kablanit):**
- Parties and business registration details (osek murshe/osek patur)
- Scope of work (hithayvut la'avoda)
- Payment terms and amount (plus VAT if applicable)
- Intellectual property assignment (haavarat zchuyot yotzrim)
- Confidentiality terms
- Independent contractor declaration (hatzahar atzma'it)
- Tax withholding provisions (nikui be'makor)

**NDA (Hozeh Sodiyut):**
- Definition of confidential information (meida sodi)
- Duration of obligation
- Exceptions (publicly available information, independently developed, legally compelled)
- Remedies for breach
- Jurisdiction clause

### Step 3: Generate the Contract Draft

Apply Israeli law requirements to each clause:

**General Contract Law (Chok HaChozim, Takanot Klaliyot, 5733-1973):**
- Section 12: duty of good faith (tom lev) in negotiation and performance
- Section 14-15: mistake (taut) and fraud (mirma) as grounds for cancellation
- Section 17-18: duress (kfiya) and undue influence (hashpaa bilti hogenet)
- Section 25: interpretation according to the parties' intent
- Section 39: performance in good faith is mandatory

**Rental-Specific (Chok Schirut V'She'ila, 5731-1971):**
- Tenant's right to sublease only with landlord's written consent
- Landlord must maintain structural elements; tenant maintains daily wear items
- Written notice periods for termination (typically 60-90 days by agreement)
- Deposit return within timeframe specified (standard: 60 days)
- Index linking (hatzmada le'madad) for leases over 12 months

**Freelancer vs Employee Test (Kablan Atzmai):**
Israeli courts use a multi-factor test (Mivhan ha'Meshulav) to determine status:
- Integration into the workplace (mivhan ha'hishtalbut)
- Economic dependence (tluya kalkalit)
- Control over work methods (pikuach al derech ha'bitzua)
- Provision of own tools (klei avoda)
- Bearing business risk (sichun iskit)
- Tax treatment (doch 106 vs cheshbonit mas)
If reclassified as employee, the "employer" owes all retroactive social benefits

**Consumer Protection for SaaS (Chok Hagnat HaTzarchan, 5741-1981):**
- Standard contracts (chozeh achid) reviewed by Attorney General's Standard Contracts Tribunal
- Unfair terms (tnai mekapaach) may be voided
- Section 4: prohibition on misleading representation
- Remote transaction (iska me'rachok) cancellation rights: 14 days for digital services
- Privacy compliance: Chok Hagnat HaPratiyut 5741-1981 and privacy regulations

**NDA Enforceability:**
- Israeli courts enforce NDAs if scope is reasonable
- Overbroad definitions of "confidential" may be narrowed by courts
- Non-compete clauses (tnai mugbal) face strict judicial scrutiny per Supreme Court ruling in Tzuk Or v. Katz
- Duration typically limited to 6-12 months post-termination
- Must demonstrate legitimate trade secret (sod miskhari) per Chok Avgat Patentim

### Step 4: Format the Output

Generate the contract with:
1. Title in Hebrew and English
2. Date and place of signing
3. Party identification with ID/registration numbers
4. "Whereas" (Ho'il ve) recitals
5. Numbered clauses organized by topic
6. Signature blocks with witness lines
7. Appendices for schedules, property descriptions, etc.

Always include a disclaimer: "This is a draft template for informational purposes. It is not legal advice. Have an Israeli attorney (orech din) review before signing."

## Examples

### Example 1: Rental Agreement
**Input**: "Draft a rental agreement for my apartment in Tel Aviv. Rent is 5,500 NIS/month, 12-month lease."
**Output**: A complete Hozeh Schirut with standard clauses: parties, property description placeholder, 5,500 NIS rent (CPI-indexed after 12 months), 2-month deposit, 60-day mutual notice for early termination, landlord structural maintenance obligations, tenant daily maintenance, no subletting without consent, Beit Mishpat Shalom Tel Aviv jurisdiction.

### Example 2: Freelancer Contract
**Input**: "I need a contract for a freelance web developer, 3-month project, 25,000 NIS."
**Output**: A Hozeh Kablanit with: scope of work section (to be filled), 25,000 NIS + VAT payment in milestones, IP assignment to client upon payment, contractor's independent status declaration, tax compliance (contractor provides cheshbonit mas), 30-day post-project confidentiality, mutual termination with 14-day notice, Israeli law governs.

### Example 3: NDA for Startup
**Input**: "We need an NDA for discussing our fintech idea with a potential partner."
**Output**: A mutual NDA (Hozeh Sodiyut Hadadi) defining confidential information broadly but with standard carve-outs (public info, prior knowledge, independent development), 2-year duration, obligation to return/destroy materials, injunctive relief clause, Tel Aviv District Court jurisdiction, governed by Israeli law.

## Troubleshooting

- **Issue**: User asks for a contract type not covered
  **Solution**: Provide the general Chok HaChozim framework (offer, acceptance, consideration/gmirut da'at, specificity/masmaut) and adapt clauses to the specific need. Always recommend attorney review.

- **Issue**: User needs contract in Hebrew only
  **Solution**: Generate in Hebrew. Use standard legal Hebrew terminology (lashon mishpatit). Structure: "ho'il ve" recitals, "le'fichach huskem" operative clauses.

- **Issue**: User asks about enforceability of a specific clause
  **Solution**: Cite the relevant law and explain judicial tendency. Note that Israeli courts have broad discretion to void unconscionable terms (tnai mekapaach) under Section 3 of Chok HaChozim Ha'Achidim 5743-1982.
