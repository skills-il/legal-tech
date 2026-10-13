# Changelog

## 1.2.0 (2026-10-12)

Correctness release. Two statements of law were wrong for whole groups of users, and the pre-2011 Schedule is now checked against its primary text.

- Pre-2011 apartments run on the pre-2011 TEXT of the law, not only on the old Schedule. s.11(ג) applies the law as worded on the eve of Amendment 5, and that text (Amendment 3, 1990, read from the Knesset PDF) has no 20-year fundamental-defect period, no s.4א(ב), no s.4ב(ב) self-repair gateways, no s.7א(ב), and does not name the sub-buyer. The skill and the script quoted all of these to pre-2011 buyers. The old route, a fundamental non-conformity found even after the warranty that makes the apartment unfit for its purpose, is now stated instead.
- Denying the contractor its opportunity to repair no longer "loses the claim". Per the Supreme Court in August 2026 (Justice Stein, as reported), the claim survives and compensation is limited to the contractor's own repair cost. Corrected in every place the skill said otherwise.
- Settlement offers after handover: s.7א(ב) voids only a waiver made a condition of handover, repairs or transfer. A freely signed post-handover settlement may bind, so the skill no longer implies any waiver is void, and routes settlements to an advocate.
- The notice test is whether a defect COULD have been discovered at handover, not whether it was visible. Added guidance for a buyer who signed the protocol with no remarks and found a defect weeks later.
- The pre-2011 worked example now states its handover date; its arithmetic contradicted its own "same facts".
- Pre-2011 Schedule: all nine rows verified against the 1990 primary text (was Kol Zchut only, four rows unevidenced).
- Registrar of Contractors: its defect track covers complaints filed during the bedek period.
- Gotcha added: do not advise withholding contract payments or offsetting defect claims against them.
- `defect_window.py`: pre-2011 output no longer prints the 20-year regime or s.4א(ב); `--type damp` under the current Schedule shows sealing, piping and thermal side by side instead of silently picking one; pre-2011 accepts current row names with a redirect note; `--notified` is reported for hidden defects with the discovery-to-notice gap; warnings for a notice date before discovery and for "discoverable" defects found years later.

## 1.1.0 (2026-08-26)

Correctness release. First review since publication; four statements of law were wrong.

- Schedule item (4) פיתוח חצר was transcribed without its שקיעת מרצפות limb, so sunken floor tiles on the ground floor, in parking, on pavements and on paths were routed to item (2) at two years instead of item (4) at three. The skill also asserted that `floor_ground` exists only in the pre-2011 table, which is the opposite of the statute. Both tables, the script and the checklist corrected; the script now accepts `floor_ground`, `floor_outdoor` and `damp` under the current Schedule and redirects them.
- s.4א(ב) was missing. A hidden אי-התאמה יסודית has its own notice limb with no one-year cut-off, so the skill could tell a claimant with a live 20-year claim that they had missed the deadline. Added to the notice table, the instructions and the script's output.
- The claim that a written demand is a mandatory precondition for a complaint to the Registrar of Contractors was removed from all six places it appeared. The Ministry imposes no such condition; the demand letter is the statutory opportunity to repair under s.4ב(א) and the evidence base, and is still sent first.
- The claim that an individual owner's common-property complaint "will not be accepted" was removed. The Ministry states that any citizen may file and that the house-committee route is recommended, not required.
- Added s.4(א)(1): deviation from the מפרט, an official standard or the building regulations is an independent breach that does not depend on a Schedule row or period.
- Step 0 no longer suspends the notice clock: it now instructs a short dated written notice while an engineer is engaged.
- Added the practical middle of a claim: conduct at the contractor's repair visit, re-inspection, when an engineer's opinion earns its cost, the small-claims track, מומחה מטעם בית המשפט, and עוגמת נפש.
- Limitation (התיישנות) surfaced as a third clock wherever a window end-date is reported.
- Schedule item (7) restored "לרבות גגות קלים עם סיכוך"; noted that s.4(א)(5) says only הקונה, and that s.7א(ב)'s late-delivery limb reaches contracts from 07.07.2022.
- `defect_window.py`: friendly errors for malformed dates instead of a traceback, and a guard against a discovery date earlier than handover.

## 1.0.0 (2026-08-10)

Initial release.

- Room-by-room handover walkthrough checklist and a dated defect log format.
- Both statutory schedules of bedek periods, current and pre-06.04.2011, with the split rule.
- Burden-of-proof analysis across the bedek and warranty periods, and the separate 20-year regime for load-bearing defects (routing only, never classified by the skill).
- The one-year notice duty for defects visible at handover, treated as a clock independent of the defect period.
- Hebrew repair-demand letter template that preserves the statutory opportunity to repair.
- Escalation map covering the Registrar of Contractors route and its limits.
- `scripts/defect_window.py`, a pure-local deterministic window and burden calculator.
