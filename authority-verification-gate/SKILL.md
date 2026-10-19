---
name: authority-verification-gate
description: Pass/fail check of legal authorities (statutes, case law, citations) before a legal document is delivered. Seven questions per authority, a control table and explicit uncertainty marking, under Israeli uniform citation rules. Use when user asks to verify legal citations, check precedents or audit authorities in a draft (Hebrew: אמת אסמכתאות). Do NOT use as a substitute for reading the official source or for legal advice.
license: MIT
metadata:
  author: moti-luchim
  version: 1.0.0
  category: legal-research
  tags: [citation-check, case-law, legislation, israeli-law, release-gate]
  tags_he: [בדיקת-ציטוטים, פסיקה, חקיקה, משפט-ישראלי, שער-מסירה]
  display_name_he: שער אימות אסמכתאות
---
# Authority Verification Gate

## 1. Legal disclaimer
This skill is a checking aid for a human reviewer. It is not legal advice and does not replace a lawyer. It addresses Israeli law. The skill cannot by itself confirm that a source is current. Only a direct check in the source confirms it. Do not rely on its output alone.

## 2. Purpose
Check each legal authority in a draft before delivery, and mark what was verified and what was not. The goal is to stop wrong or invented citations from going out.

## 3. When to use
- A research draft, opinion, pleading or ruling is complete and about to be delivered.
- The user asks to verify citations, check whether a rule still stands, or audit authorities.
- As a mandatory step between research and drafting.

## 4. Input
- The draft, or a list of authorities with the paragraph where each appears.
- Access to sources, if available (see section 6 on source types).

## 5. Output
A control table, one row per authority, with the columns: authority, location in draft, normative classification, current status, check status, notes and citation fixes. Below it, an overall result: "gate passed" only if every authority is verified, otherwise "gate not passed, items listed".

Synthetic sample rows (invented cases, for format only, not real authorities):

| Authority | Location | Classification | Current status | Check status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Civil Appeal 111/00 Doe v. Roe (invented) | paragraph 4 | binding majority ruling | in force | verified at source | citation form correct |
| Leave to Appeal 222/00 Poe v. Moe (invented) | paragraph 7 | obiter | later judgments exist | needs clarification | state that it is obiter |
| Section 3(b) of an invented statute | paragraph 11 | primary legislation | not checked | requires verification at source | confirm numbering |

## 6. The seven questions
1. Primary source: was the authority checked directly in an official source, not through a secondary quotation?
2. Identifiers: are the procedure type, number, year and full party names exact?
3. Classification: is the cited statement the binding ratio of the majority, or obiter or a minority view?
4. Good law: was the ruling reversed, limited, narrowed or changed by later legislation?
5. Distinction: are the facts of the precedent close enough to the present matter?
6. Later judgments: do later judgments apply or change the rule in the relevant context?
7. Citation form: does the citation follow the uniform citation rules?

Source types. Keep them apart in the table:
- Official sources: the official legislation records, the courts' own sites. These count as primary.
- Commercial databases and secondary sources: useful for finding material and for later judgments, but a result from them is marked "commercial source" and is not treated as the official text.
Where only a commercial or secondary source was checked, the status is "verified in commercial source, official check pending".

## 7. Release gate rules
- No claim of settled law without verification at a source.
- Every authority not fully checked is marked "requires verification at source" in the table.
- Use round brackets in running text. Keep foreign names and case numbers isolated from Hebrew text.

## 8. Behavior when material is missing
- No access to sources: do not guess. Return the table with all rows marked "not checked" and list what the reviewer must look up.
- Partial citation: mark "identifier incomplete" and do not complete it from memory.
- Never invent a case, a section number or a quotation.

## 9. Privacy of case documents
Authorities are public, but the draft around them may identify real parties. Send only the citation, never the case facts, to any outside search service. Anonymize before sharing output.

## 10. Synthetic example
Input: a draft cites "Civil Appeal 111/00 Doe v. Roe" (invented) for the proposition that a notice must be in writing.
Check: source not available in this session. Row result: "not checked, requires verification at source". Overall: "gate not passed, 1 item open".

## Usage example
User says: "Verify the authorities in this draft before I send it."
Result: a control table with one row per authority and the line "gate not passed" if any row is unverified.

## Troubleshooting

### Error: No access to official sources
Cause: The session has no way to open the official text
Solution: Return all rows as not checked and list what the reviewer must look up. Do not complete citations from memory.

### Error: A citation is incomplete
Cause: The draft gives a name without a number or year
Solution: Mark identifier incomplete and ask for the full citation.

## Hebrew version
The same skill in Hebrew, with the same sections in the same order, is in references/SKILL_HE.md.
