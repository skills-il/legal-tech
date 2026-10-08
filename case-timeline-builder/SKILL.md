---
name: case-timeline-builder
description: Builds a dated chronology from several case documents, grades date certainty, and flags contradictions and gaps. Organizes facts only, with no automatic legal conclusions. Use when user asks to build a case timeline, map dates across documents or find date contradictions (Hebrew: בנה ציר זמן לתיק). Do NOT use to decide limitation, delay or any other legal question.
license: MIT
metadata:
  author: moti-luchim
  version: 1.0.0
  category: legal-analysis
  tags: [timeline, chronology, evidence, contradictions, israeli-law]
  tags_he: [ציר-זמן, כרונולוגיה, ראיות, סתירות, משפט-ישראלי]
  display_name_he: בניית ציר זמן לתיק
---
# Case Timeline Builder

## 1. Legal disclaimer
This skill organizes facts for a human reviewer. It is not legal advice. It does not decide limitation periods, delay, notice or any other legal question. Relevance notes are prompts for the reviewer, not conclusions. Check every date against the source document. Do not rely on its output alone.

## 2. Purpose
Extract events, dates, actions, correspondence and exhibits from several documents and arrange them in one chronological table, with a second table for contradictions and gaps.

## 3. When to use
- Reviewing a multi-document file (pleadings, exhibits, protocols, expert opinions, correspondence).
- The user asks for a timeline, a date map, or a search for contradictions between versions.
- As preparation for a reviewer who will later look at limitation, delay, damage onset or prior notice.

## 4. Input
- The case documents, each with a name or exhibit label.
- Optional: the question the timeline serves, so entries can be flagged as relevant to it.

## 5. Output
Two tables.

A. Chronological table: exact date, event, exact source in the document, party involved, evidence status, relevance note for the reviewer.

B. Contradictions and gaps table: issue, version A and its source, version B and its source, apparent size of the gap, check needed.

Synthetic sample (invented facts, for format only):

| Date | Event | Source | Party | Evidence status | Relevance note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01/01/2026 | first defect noticed | statement of claim, section 4 | plaintiff | claimed, no contemporaneous photos | may matter to when the claim arose, reviewer to decide |
| 15/01/2026 | first written letter to the other side | exhibit B | plaintiff to defendant | backed by a source (email) | may bear on prior notice, reviewer to decide |

| Issue | Version A | Version B | Gap | Check needed |
| :--- | :--- | :--- | :--- | :--- |
| start of the event | January 2026 (statement of claim) | March 2026 (expert opinion) | high | contemporaneous photos and work logs |

## 6. Date certainty grades
1. Backed by a source: supported by a document such as a received stamp, receipt, delivery note or service confirmation. "Backed by a source" does not mean beyond dispute. A party may still challenge the document.
2. Claimed: appears only in one party's pleading, with no objective document. Treated as disputed.
3. Estimated: derived from context or a season or year without an exact day. Marked clearly as an estimate.

Rules:
- Never place an event in the order without a documented date.
- Cross-check pleadings against expert opinions and prior correspondence to find contradictions.
- Do not write a legal conclusion into the table. Relevance notes use wording such as "may bear on" and leave the decision to the reviewer.
- Round brackets in running text. Each Hebrew sentence ends with a full Hebrew word.

## 7. Behavior when material is missing
- Event without a date: list it in a separate "undated events" block, not in the chronology.
- Document unreadable or cut off: say so and do not infer its content.
- Only one party's documents available: state that the timeline is one-sided.

## 8. Privacy of case documents
The timeline holds names, dates and sensitive facts. Use it only for the review. Do not post it, paste it in public places or send it to a third-party service. Anonymize names and identifiers before sharing.

## 9. Synthetic example
Inputs (invented): a claim says the defect appeared in January, an expert report says first seen in March.
Result: row in table B, issue "start of the event", gap "high", check "contemporaneous photos and logs". No statement about which date is correct.

## Usage example
User says: "Build a timeline from these four documents and flag contradictions."
Result: two tables: a chronology with certainty grades and a contradictions table, with no legal conclusion.

## Troubleshooting

### Error: An event has no date
Cause: The documents mention it without a date
Solution: List it under undated events, not in the chronology.

### Error: A document is unreadable
Cause: Scan quality or a cut-off file
Solution: State which document, do not infer its content, and ask for a better copy.

## Hebrew version
The same skill in Hebrew, with the same sections in the same order, is in references/SKILL_HE.md.
