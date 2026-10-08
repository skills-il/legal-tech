---
name: legal-drafting-qc
description: Graded quality review of Israeli legal drafts (pleadings, rulings, memos, administrative submissions): factual basis, authority, counterarguments, consistency, terminology and format. Returns a defect report and does not rewrite. Use when user asks for QC of a legal draft, a consistency check, or a check for contradictions before filing or delivery (Hebrew: בקרת איכות לטיוטה משפטית). Do NOT use to approve a document for filing or to give legal advice.
license: MIT
metadata:
  author: moti-luchim
  version: 1.0.0
  category: legal-review
  tags: [legal-drafting, quality-control, israeli-law, hebrew, review]
  tags_he: [ניסוח-משפטי, בקרת-איכות, משפט-ישראלי, עברית, סקירה]
  display_name_he: בקרת איכות לטיוטות משפטיות
---
# Legal Drafting QC

## 1. Legal disclaimer
This skill supports a human reviewer. It is not legal advice and does not replace a lawyer. It targets Israeli legal drafting. Any citation or legal claim it mentions must be checked against the primary source. A passing result is not approval to file. Do not rely on its output alone.

## 2. Purpose
Review a legal draft and return a structured defect report, graded by severity, with concrete suggested fixes for the user to approve. The skill points out problems. It does not rewrite the draft on its own.

## 3. When to use
- A draft pleading, ruling, memo, appeal or letter is complete and about to be handed over.
- The user asks for QC, a consistency check, or a check for contradictions.
- Before signature, filing or delivery to a court or academic reader.

## 4. Input
- The draft (Word, PDF or text).
- Optional: the underlying pleadings, exhibits, expert opinions and the opponent's arguments, so facts can be checked against them.
- Optional: a style profile (see section 8).
If the supporting material is missing, see section 7.

## 5. Output
A report with four parts:
1. Overall status: "passed checks, human decision required" or "blocking defects remain". The skill never declares a draft "approved for delivery".
2. Table of blocking and substantive defects: exact location, description, suggested fix.
3. Editorial and format notes.
4. Final checklist.

Severity grades: blocking, substantive, editorial, format and RTL.

## 6. Eight mandatory checks
1. Factual basis: each material fact is supported by a pleading, exhibit or expert opinion.
2. Legal authority: each legal claim rests on a statute, regulation or precedent that was verified (see the authority-verification-gate skill).
3. Counterarguments: the draft answers the opponent's main points.
4. Internal consistency: no contradictions between background and conclusion, no date mismatches.
5. Logical chain: the operative conclusion follows from the analysis.
6. Terminology and numbering: party numbering and terms stay fixed across the document.
7. Register: the wording fits the genre (judicial, administrative, pleading).
8. Punctuation, direction and RTL:
   - Hebrew geresh and gershayim (׳ and ״), not keyboard quotes, in abbreviations.
   - No invisible direction characters (LRM, RLM) in the text.
   - In Word files: paragraph-level bidi, consistent alignment, complex-script size and bold properties set, Hebrew and Latin fonts defined.
   - Round brackets in running text, except where a citation standard requires otherwise.

## 7. Behavior when material is missing
- If the supporting documents are absent, check only internal consistency and form, and say so at the top of the report.
- Mark every factual or legal claim that could not be checked as "not verified, source missing".
- If the draft appears truncated, report it as blocking.
- Never fill gaps by guessing facts, dates or citations.

## 8. Optional modules
### 8.1 Style profile (optional)
Only when the user supplies one. Examples of preferences a user may set: avoiding specific verbs, a fixed first or third person, fixed phrases. Without a profile, skip this check. These preferences are the user's own, not a general rule of legal writing.

### 8.2 Module A - administrative appeals and municipal or traffic fines (optional)
Use only when the draft is an objection or request to cancel a fine or notice. Checks:
1. Standing: the applicant details match the registered owner shown in the vehicle license and the original notice, or a transfer request is attached. Verify the legal basis for any ownership presumption in the primary source.
2. Evidentiary level: check timestamps of enforcement photos and signage before reading the explanations.
3. Payment versus presence: a parking-app payment shows payment, not physical presence of the vehicle. Do not let the draft imply otherwise.
4. Alternative relief: the draft asks first for cancellation of the notice and, in the alternative, for conversion to a warning as a discretionary step. Source basis: Attorney General Guideline 4.3040, "Cancellation of fine payment notices - guideline for prosecutors" (index no. 52.0003A, last updated 4.12.2011), listed in the State Comptroller's Annual Report 71C (2021) on municipal prosecution, https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/2021/71C/2021-71c-401-Tviah-Ironit.pdf. The same report states that the guidelines to municipal prosecutors set no criteria for converting a notice to a warning, and that in practice a conversion is recorded as a cancellation with a warning note. So do not write that the guideline requires or entitles anyone to a warning. The guideline's own official text was not retrieved, so open it and verify before quoting it.

## 9. Privacy of case documents
Case files may hold names, ID numbers, addresses and medical or financial details. Process them only for this review. Do not copy them into examples, logs, public repositories or third-party services. Anonymize before sharing any output.

## 10. Synthetic example
Draft excerpt (invented): "Defendant 2 failed to appear. The court finds that Defendant 3 was served on 1 March." Background section says service was on 10 March.
Report row: location "discussion, paragraph 4"; defect "service date contradicts the background section"; grade "blocking"; fix "align the date to the proof of service, source needed".
Status line: "blocking defects remain".

## Usage example
User says: "Run a QC pass on this draft response to the claim."
Result: a defect report with the status line "blocking defects remain" and one row for the service-date contradiction.

## Troubleshooting

### Error: The draft or its sources are missing or cut off
Cause: The file was truncated or only the draft was supplied
Solution: Say so at the top of the report, check only internal consistency and form, and mark unverified claims.

### Error: Hebrew brackets look reversed
Cause: Latin text or numbers sit inside bracketed Hebrew
Solution: Report it as a format and RTL defect and suggest isolating the foreign text.

## Hebrew version
The same skill in Hebrew, with the same sections in the same order, is in references/SKILL_HE.md.
