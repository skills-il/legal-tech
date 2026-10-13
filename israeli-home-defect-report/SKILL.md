---
name: israeli-home-defect-report
description: >-
  Not legal advice. Helps a buyer of a new Israeli apartment document construction defects and act in time. Builds
  a room-by-room handover walkthrough, turns findings into a dated defect log for the protokol
  mesira, works out which statutory window each defect falls in under the Sale (Apartments) Law
  1973 and who must prove what, and drafts a Hebrew repair-demand letter. Use when a user says
  "bedek bait", "protokol mesira", "likuyim badira", "the contractor will not fix", or "is it
  too late to complain". It matters because periods run from handover, differ by defect type,
  and differ again for flats bought before April 2011, so a missed notice deadline can forfeit
  a good claim. Produces a log and a letter, not an engineering opinion.
  Do NOT use to assess structural safety or load-bearing damage (needs a licensed engineer), to
  value repairs, for late-delivery compensation, for rental defects (use
  israeli-rental-agreements), or for a self-built home (use israeli-private-home-construction).
license: MIT
allowed-tools: 'Bash(python3:*)'
compatibility: >-
  Knowledge plus a Python date-window helper (pure local logic, no network, no binaries).
  Works with Claude Code, Claude.ai, ChatGPT, Cursor, Gemini Spark, and the other listed agents.
---

# Israeli New-Apartment Defect Log

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate or an engineer. The output is not legal advice, not a legal opinion, and not an engineering opinion (chavat daat handasit). It is a general explanation and a template only: it does not inspect your apartment, does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. A claim that the contractor disputes, and anything intended for a court, needs a licensed engineer (mehandes) for the opinion and a licensed advocate (orech din) for the claim. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. All use of its output is the user's sole responsibility.

## Problem

Buyers of a new apartment are handed the keys under time pressure, asked to sign a handover protocol on the spot, and told that anything they do not raise now is their own problem. Almost none of that pressure reflects the law: liability cannot be waived, the periods run for years, and the burden of proof sits on the contractor for most of them. What buyers actually lose rights to is narrower and more specific, a one-year notice deadline for anything a reasonable inspection would have found on the day. The periods themselves are widely misreported, they differ per defect type, and they are different again for apartments bought before April 2011, so buyers routinely give up on claims that are still live and chase claims that closed years ago. This skill turns a walkthrough into a dated log, works out which window each defect is actually in, and drafts the written demand that every later remedy depends on.

## Problem boundary

This skill documents and times defects in a new apartment bought from a contractor. It does not assess structural safety and does not decide whether a defect is load-bearing, because that is a licensed engineer's call and getting it wrong is dangerous. For a home you are building yourself on your own land, use `israeli-private-home-construction`. For defects in a rented apartment, use `israeli-rental-agreements`. For the separate money claim over late delivery, and for guarantees protecting your payments, see the Gotchas section, both are out of scope here.

## Instructions

You help a buyer document defects, work out the timing, and write the demand letter. Read `references/periods-and-burdens.md` before answering any timing question and `references/walkthrough-and-letter.md` before building a log or drafting a letter.

### Step 0, safety gate, run this first and every time

Before anything else, scan what the user describes for these signals:

- cracks in a load-bearing element, or any crack that is growing, stepped, or runs through a beam, column or ceiling slab
- floors or ceilings sagging, doors or windows suddenly binding, visible movement of the structure
- water reaching electrical fittings, a distribution board, or a socket
- a smell of gas, or an exposed live conductor
- anything falling from an exterior facade or a balcony

If any appear, stop the documentation workflow and say so plainly. Tell the user this needs a licensed engineer now, and where there is an immediate hazard, emergency services. Do not classify the defect, do not estimate severity, do not put it in the log as though it were an ordinary snag, and do not continue to the letter. You may resume the normal workflow for the user's other, unrelated defects once you have flagged this.

Stopping the classification does NOT mean stopping the clock. Notice for a hidden fundamental defect is due within a reasonable time of DISCOVERY (s.4a(b); for a pre-2011 apartment, s.4a(a)(2) to the same effect), and engaging an engineer takes weeks. So still tell the user to send the contractor a short dated written notice now, describing only what they observed and saying an engineer's opinion will follow. Describe, date, send. Do not classify.

Never tell the user whether a defect is or is not an "ai hat'ama yesodit" (fundamental non-conformity). That classification decides whether the 20-year regime applies and it belongs to an engineer. Tell them the category exists, that under the current law it runs 20 years (the pre-2011 text has no fixed period for it), and that only an engineer can place a defect in it.

### Step 1, establish the four dates

Everything downstream depends on these. Ask for whichever are missing and do not guess:

| Date | Why it matters |
|---|---|
| Handover (hadmadat hadira lirshut hakone) | Starts every bedek period. It is the date you actually got possession, not the contract date, and not the protocol date if that differs |
| Sale contract signature | Selects WHICH schedule of periods applies, and which TEXT of the law. It is the ORIGINAL contract with the contractor, not a sub-buyer's resale contract. The old schedule governs if EITHER the contract was signed before 06.04.2011 OR construction of the building finished before it, so ask about both |
| Discovery of the defect | Places the defect in the bedek window, the warranty window, or outside both |
| Written notice to the contractor, if already sent | Tests the one-year notice deadline |

If the user is at the handover and has not received the keys yet, the handover date is today and you go to Step 2. If they already live there, go to Step 3.

One case people get wrong: a buyer who bought a nearly-new apartment from its first owner rather than from the contractor (a kone mishne) still holds these rights against the contractor. The clock does not restart on resale, it runs from the ORIGINAL handover to the first buyer, so ask for that date and not the date of their own purchase. Likewise the contract that selects the schedule is the first buyer's ORIGINAL contract with the contractor, not the sub-buyer's own. The sub-buyer was written into the statute in 2011, so for an apartment under the pre-2011 law whether a sub-buyer can rely on it is a question for an advocate.

### Step 2, the walkthrough (before or at handover)

Work room by room. Use the checklist in `references/walkthrough-and-letter.md`, and adapt it, do not read it out mechanically. For every finding record: room, what it is, whether a reasonable inspection today would find it, a photograph with something for scale, and the date. That question is not bookkeeping, it selects which notice rule applies later, so ask it for every item. The statutory test is whether the defect COULD have been discovered at handover, not whether the user noticed it; when unsure, treat it as discoverable for deadline purposes.

Raise the professional inspection here, not later. A בדק בית report from a licensed engineer (מהנדס), commissioned BEFORE the protocol is signed and attached to it, is both the cheapest and the most probative it will ever be: inside the bedek period the burden is on the contractor, so the report is doing its work at the moment the law is already on the buyer's side. Say it is worth considering and let the user decide. A report by an inspector who is not an engineer may carry little weight as an expert opinion. You still never classify anything yourself.

Then, on the protocol itself:

- The contractor cannot lawfully strip its liability, so do not let a signature panic the user. A contract clause that cuts the buyer's statutory rights is ineffective even if the buyer signed it freely (s.7A(a)), and for an apartment under the current law a waiver made a condition of getting the keys is void outright (s.7A(b)). A settlement signed AFTER handover is a different matter, see Step 5.
- What a signature CAN do is create an evidentiary problem. Signing a statement that the apartment is defect-free is a factual admission a court will weigh, whatever the waiver rules say.
- So the advice is not "refuse to sign". It is: attach the written defect list, have it referenced on the protocol, keep a signed or photographed copy, and never sign wording like "the apartment was received to my full satisfaction" or "I have no comments" while there are open items.
- If the contractor refuses to record the reservations, note in handwriting on the protocol that the signature confirms receipt of possession only and not acceptance of the apartment's condition, and photograph it before handing it back.
- If the user ALREADY signed with no remarks and finds a defect days or weeks later: notify in writing now, with dated photos and anything that dates the defect to before move-in (delivery receipts, the date furniture arrived). The one-year deadline is still open; the real risk is the contractor arguing, during the bedek period, that the buyer caused the damage (s.4(a)(2)), and the clean protocol helps that argument.

### Step 3, work out the window for each defect

First check whether the Schedule is even needed. Under s.4(a)(1) the contractor is in breach if the apartment differs from the מפרט, from an official standard (תקן רשמי), or from the building regulations. That is not tied to a Schedule row or period, but the buyer must prove the deviation, in practice with an engineer. It is the route to raise when a Schedule window has closed, and it is the one most buyers never hear about. It escapes the Schedule, NOT the notice duty: s.4(b) deems it an אי-התאמה, so s.4a still applies and a specification deviation discoverable on handover day is barred by the same one-year rule. Run the notice analysis on it too.

Then use the helper script rather than doing the arithmetic in your head:

```bash
python3 scripts/defect_window.py --handover 2021-03-15 --contract 2020-11-01 \
  --discovered 2026-01-10 --type pipes --visible no
```

`python3 scripts/defect_window.py --list` prints both schedules. If a host cannot run scripts, do the arithmetic yourself from the tables in `references/periods-and-burdens.md`, and show your working so the user can check it.

Two clocks run independently and BOTH have to be satisfied. This is the single most common mistake in this domain, so state both explicitly every time:

1. The period for that defect type, which decides who must prove what.
2. The notice duty, which has three limbs. Discoverable at handover means notice was due within one year of handover (s.4a(a)(1)). Not discoverable by a reasonable inspection means within a reasonable time after discovery, however long after handover that falls (s.4a(a)(2)). And a hidden FUNDAMENTAL defect has its own limb with no one-year cut-off at all (s.4a(b)), so never report a missed one-year deadline as final where a load-bearing defect may be involved. Separately, s.16 of the Sale Law 1968 (imported by s.4(b)) lifts the notice bar entirely where the contractor knew of the facts and did not disclose them, so a missed deadline is a question for an advocate, never a closed door.

Sunken floor tiles on the ground floor, in parking, on pavements and on paths are row 4 at three years, not row 2 (see Gotchas); the script redirects `floor_ground` and `floor_outdoor`.

Damp is the classic multi-row defect. Under the current Schedule its CAUSE decides the row: sealing (4 years), piping (4 years) or thermal insulation (3 years), and cause is an engineer's call. `--type damp` prints all three; report the range, and where they give different stages say that who must prove what depends on the cause.

**A pre-2011 apartment runs on the pre-2011 TEXT of the law, not only on the old Schedule.** s.11(c) applies the law as worded on the eve of Amendment 5 (2011). That text has no 20-year period: a fundamental non-conformity discovered even after the warranty period is a breach if it makes the apartment unfit for its purpose. It also has no s.4a(b) limb, no s.4b(b) self-repair gateways, no s.7A(b), and does not name the sub-buyer. Never quote those to a pre-2011 buyer. Details in `references/periods-and-burdens.md`.

There is also a THIRD clock the periods do not describe: limitation (התיישנות) governs how long the user has to SUE, and it runs separately. Whenever you report an end-date, say that it is the cover period and not a filing deadline, and that the time to sue is a question for an advocate.

Report the result as: which schedule applied and why, the period for that row, the stage the defect is in, who carries the burden there, and the notice position. If the contract date is unknown: a handover before 06.04.2011 means the pre-2011 table and text apply (the building was finished before the split); otherwise say you assumed the current schedule, that a pre-2011 contract or a building completed before the split would shorten several periods, and ask about both, especially for a handover in 2011 to 2014.

### Step 4, draft the demand letter

The letter is not a formality. The law requires the buyer to give the contractor a proper opportunity to repair. A buyer who skips that step does not lose the claim, but the Supreme Court held in August 2026 (Justice Stein, as reported) that compensation is then cut to what the repair would have cost the CONTRACTOR, which can be far below the market price the buyer pays; full denial is reserved for extreme bad faith. Send the letter before escalating anywhere. It is not, however, a formal precondition for a Registrar complaint, so never tell a user they must restart with a letter before they may file.

Build it from the template in `references/walkthrough-and-letter.md`. It must contain the apartment and contract identifiers, the handover date, an itemised defect table with dates, an explicit demand to repair, a reasonable deadline for a response, a statement that the buyer is giving the opportunity to repair as the law requires, and delivery by a traceable method. Keep the tone factual. The letter is signed by the buyer in their own name; never add a representative line or legal argument. Do not assert a legal conclusion the user cannot back, and do not quantify damages. Do not put the skill's own statutory-row analysis into the letter either. The timing analysis is for the buyer's understanding; the letter states the dates and the buyer's own assertion of liability.

### Step 5, escalate

If the contractor does not respond or does not fix, lay out the routes and their real limits:

| Route | What it gives | What it will not do |
|---|---|---|
| Complaint to the Registrar of Contractors | Free. Disciplinary pressure on a registered contractor. Open to any citizen against a registered contractor. Its defect track covers complaints filed during the bedek period | Will not award money, will not arbitrate, will not resolve the dispute, will not touch a matter already in court |
| Self-repair at the contractor's expense | Available as of right only on two narrow statutory gateways | Not a general option. Repairing without first giving the contractor a proper opportunity typically cuts the award to the contractor's own repair cost |
| Civil claim | Money and enforceable orders | Needs an advocate, and in practice an engineer's opinion |

Self-repair at the contractor's expense is open only where the defect came back after the contractor repaired it at least once within two years of the notice, or the repair is urgent and the contractor did not act within a reasonable time of the notice (s.4b(b), current law only). Say so precisely. A user who repairs WITHOUT first giving the contractor a proper opportunity keeps a claim but, per the August 2026 ruling, recovers only what the repair would have cost the contractor, not what they paid. Where the contractor WAS given a proper opportunity and let it pass, that ruling's reduction does not apply on its face, and what the user recovers is a question for an advocate. If a repair truly cannot wait, notify first, wait a reasonable time, and keep invoices and before-and-after photos.

Common property is a separate track. Roof sealing, exterior cladding and yard development usually sit in the common property, and the Ministry recommends that a common-property complaint be filed through a member of the elected house committee. Recommended, not required: an individual owner is not barred. Route through the committee where one exists, and never tell a user with no functioning committee that they have no route.

**Settlement offers after handover.** s.7A(b) voids a waiver made a CONDITION of handover, of repairs, or of a transfer of rights. A settlement the buyer freely signs after handover, for payment, to close known defects is a different thing and may bind them for what it covers, so never tell a user it is "void anyway". If the contractor will repair only once the user signs, that is the s.7A(b) case for an apartment under the current law; for a pre-2011 apartment, which has no s.7A(b), route that situation to an advocate. Before signing: get an engineer's repair estimate so the user knows what the sum is traded against, make the release list the defects it covers, and keep hidden defects found later, the load-bearing regime and common property out of it. A release for money has lasting legal effect: route it to an advocate before signing, and do not draft or approve settlement wording.

### What actually happens after the letter

Most users' real question starts here, and the answer is not "get a lawyer".

- **The repair visit is the thing being counted.** The contractor usually responds by sending someone. Tell the user to be present, photograph before and after, write down the date and who attended, and not to sign anything describing the repair as accepted or the matter as closed. The s.4b(b) self-repair gateway (current law) turns on whether the defect RECURRED after a repair within two years of the notice, and nobody can prove a recurrence they did not record.
- **Re-inspect after a few weeks**, especially for damp, sealing and piping, where a failed repair reappears slowly. A recurrence is a new dated entry in the same log, not a new complaint.
- **The engineer's opinion** must come from a licensed מהנדס. It becomes worth its cost once the burden has shifted to the buyer in the warranty period, and it is what a court and a contractor actually respond to.
- **Small claims (תביעות קטנות)** takes low-value defect claims without an advocate. It is the realistic route for a handful of snags the contractor ignored, and the skill should name it rather than routing everything to a civil claim.
- **Distress (עוגמת נפש)** is a recognised head of damage in construction-defect claims, awarded separately from repair cost. Say it exists; never estimate it.

Where a claim is contested or quantified, it needs an advocate, and in practice a court-appointed expert (מומחה מטעם בית המשפט) will decide the technical dispute.

## Examples

### A leak at four years, current schedule

User bought in 2020, took possession March 2021, finds a pipe leak in January 2026 and assumes it is far too late.

Run Step 1, then the script. Pipes under the current schedule carry four years, so the bedek period closed in March 2025 and the warranty runs to March 2028. The defect is inside the warranty period, so it is live, but the burden has moved to the buyer, who now has to show the leak originates in planning, workmanship or materials. Because a leak inside internal piping could not have been found by a reasonable inspection at handover, the one-year notice rule does not bar it, and notice is due within a reasonable time of discovery, which means now. Advise: send the demand letter this week, and because the burden has shifted, this is the point at which a licensed engineer's opinion becomes worth paying for.

### The same leak in an older apartment

The sale contract was signed in January 2009, the keys were handed over in June 2009, and the leak appears in January 2026. The pre-2011 schedule applies, where piping is two years, not four, and the clock still runs from handover. Bedek closed in June 2011 and the warranty in June 2014. Both windows are shut. Do not stop there: a deviation from the specification, the old law's route for a fundamental non-conformity that makes the apartment unfit for its purpose (no 20-year limit under the old text), and rights under other law where the contractor concealed what it knew can still be open, and all are questions for an advocate and an engineer. Hidden-ness alone does not reopen a closed period; it affects only the notice clock. Never present the closed window as the end of the matter.

### Handover next week

User is collecting keys and is anxious about signing. Build the room-by-room list, explain that liability cannot be contracted away and that a waiver demanded as the price of the keys is void, and then give the practical instruction that actually protects them: attach the written list, get it referenced on the protocol, photograph everything, and refuse only the blanket "no comments" wording. Set the one-year notice deadline for everything discoverable on the day and tell them the date.

### Cracks above a doorway

User reports a widening diagonal crack running through the ceiling above a door. Step 0 fires. Stop, tell the user this is not something to log as a snag, and route to a licensed engineer. Do not say whether it is structural, do not say whether the 20-year regime applies, and do not draft a letter about it yet.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Sale (Apartments) Law 1973, consolidated | https://www.nevo.co.il/law_html/law00/72490.htm | The Schedule's ten items, s.4 burdens, s.4a notice, s.4b repair, s.7A waiver. Check the "current to" banner for a newer amendment |
| Kol Zchut, contractor liability for defects | https://www.kolzchut.org.il/he/אחריות_קבלן_לליקויים_בדירה_חדשה | The 06.04.2011 split, the pre-2011 table, the waiver FAQ |
| Registrar of Contractors, official service page | https://www.gov.il/he/service/complaint-about-constractor | Who may file, the attachment list, the disciplinary scope limits. This is the authority on the process, above any secondary summary |
| Kol Zchut, complaint to the Registrar of Contractors | https://www.kolzchut.org.il/he/הגשת_תלונה_לרשם_הקבלנים_במשרד_הבינוי_והשיכון | Practice guidance. Treats a prior written demand as expected; the Ministry does not require it |
| Registrar of Contractors complaint form | https://govforms.gov.il/mw/forms/complaint-about-contractor@moch.gov.il | That the form is still live at this address |

## Bundled Resources

| File | Use it for |
|---|---|
| `references/periods-and-burdens.md` | Both schedules in full, the burden rules, the notice rules, waiver and escalation detail |
| `references/walkthrough-and-letter.md` | The room-by-room checklist, the defect log format, the Hebrew demand-letter template |
| `references/domain-checklist.md` | The coverage contract this skill is maintained against, including figures known to be wrong in secondary sources |
| `scripts/defect_window.py` | Deterministic window and burden calculation. `--list` for both schedules, `--example` for worked cases |

## Gotchas

These are failure modes for the agent, not user errors.

- **Do not use the blog figures.** Widely repeated summaries give plumbing as 2 years, roof sealing as 3, and "structure" as 7. Under the current schedule piping is 4 and sealing is 4, the 3-year damp figure is the pre-2011 row, and the 7-year row is exterior cladding, not structure. Load-bearing structure is the separate 20-year regime. Check `references/periods-and-burdens.md`, not memory.
- **Sunken floor tiles are row 4, not row 2.** שקיעת מרצפות on the ground floor, in parking, on pavements and on paths is expressly inside פיתוח חצר at three years. Putting it in ריצוף וחיפוי פנים at two costs the buyer a year at both stages. `floor_ground` and `floor_outdoor` are pre-2011 row names, but the defects they describe are covered under the current schedule too.
- **Do not go hunting for a recent reform.** The last substantive change to the defect regime is Amendment 5 of 2011; Amendment 9 of 2022 touched late delivery and waiver. Later amendments listed against this law are indirect ones that changed a named Knesset committee and nothing about defects.
- **There are two schedules, and two texts of the law.** Defaulting to the current table for an apartment bought before 6 April 2011 overstates the buyer's rights, sometimes by years, and quoting the 20-year regime, s.4b(b) or s.7A(b) to that buyer quotes provisions that do not apply to them. Ask for the contract date.
- **The warranty runs from the end of the bedek period, not from handover.** Total cover per row is its bedek period plus three years, so piping under the current schedule is protected for seven years in total. Treating the warranty as three years from handover understates protection badly.
- **The notice deadline and the defect period are different clocks.** A defect can be comfortably inside its bedek period and still be dead because a defect discoverable at handover was not notified within a year of it. Always answer both.
- **Do not tell the user that signing the protocol waived their rights.** It did not, liability cannot be contracted away except in the buyer's favour. Explain the evidentiary problem instead, which is the real and much narrower risk.
- **Never classify a defect as load-bearing or fundamental, in either direction.** Saying "this is not structural" is as dangerous as the opposite, and it is an engineer's call.
- **Do not draft a letter that skips the opportunity to repair.** A demand that jumps straight to compensation or announces self-repair damages the user's position, because the law requires giving the contractor a proper chance to fix it first. But do not overstate the cost either: skipping it reduces the award, it does not forfeit the claim.
- **Do not advise withholding contract payments or offsetting a defect claim against them.** Withholding can put the buyer in breach and expose them to contractual late-payment interest (s.5B). If the contract has its own retention mechanism for defects, use that; otherwise it is a question for the advocate who handled the purchase.

## Troubleshooting

| Symptom | Cause | What to do |
|---|---|---|
| Script exits saying the defect type is not a row in that schedule | The two schedules have different row NAMES. `stairwell` exists only in the pre-2011 table | Run `--list` and pick from the schedule that applies. `floor_ground`, `floor_outdoor` and `damp` are accepted under the current schedule, and `sealing`, `flooring`, `frames`, `thermal` and `yard` under the pre-2011 one, each redirected with a note. If nothing fits use `other`, which is one year. Never conclude from a rejected key that the defect is uncovered |
| User cannot produce the sale contract date | Common with inherited or resold apartments | If the handover itself was before 06.04.2011, the contract was too, so the pre-2011 table and text apply (the script does this). Otherwise say you are assuming the current schedule, give the answer, and state plainly that a pre-2011 contract would shorten several periods. Suggest the contract can be obtained from the conveyancing advocate or the land registry file |
| Contractor says the warranty "expired after 3 years" | Contractor is treating the warranty as running from handover | The warranty starts when that row's bedek period ends. Give the arithmetic for the specific row in writing |
| Contractor refuses to record reservations on the protocol | Routine pressure tactic at handover | Handwrite on the protocol that the signature confirms receipt of possession only, photograph it before returning it, and send the defect list separately the same day by a traceable method |
| Registrar complaint rejected | Most likely a scope limit: it is a money dispute, it is already in court, or it asks the Registrar to arbitrate. Or the contractor is not in the register | Check the register, and re-read the complaint against the disciplinary framing. A missing demand letter is NOT a ground of rejection, so do not tell the user to restart with one |
| Defect is in the roof or the facade and the neighbours are affected | It is almost certainly common property | Prefer the house committee track, which the Ministry recommends. If no committee exists or it will not act, the owner may still file, so do not present this as a dead end |
| The contractor has vanished, is in liquidation, or the company was struck off | Common with single-project companies | Say plainly that this changes the problem. Still send the written notice and date it, still document, and route the user to an advocate now, because who can be pursued (a parent company, directors, insurers, or a guarantee) is a legal question this skill cannot answer. Note that the sale-law guarantees protect the money paid, not defect repairs |
