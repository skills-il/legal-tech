---
name: israeli-flight-compensation
description: >-
  Determines whether an air passenger is owed compensation under Israel's Aviation Services Law
  (חוק שירותי תעופה, 2012, "חוק טיבי") and drafts a Hebrew demand letter to the airline. Use when
  a flight to or from Israel was cancelled, delayed, overbooked, downgraded, or moved earlier, and
  the user asks "am I owed compensation", "pitzuy al bitul tisa", "ta'osa hit'akva", "the airline
  cancelled my flight", or wants to claim without paying a claim-handling service a cut. Calculates
  the amount by distance band (2026 figures), explains assistance rights, and routes refusals to
  small claims. Do NOT use for booking flights (use israeli-flight-finder), lost or damaged baggage
  (Montreal Convention), travel insurance, or flights with no Israeli departure or arrival.
license: MIT
allowed-tools: 'Bash(python3:*)'
compatibility: >-
  Pure-knowledge plus a Python helper script (no network needed for the calculation). Works with
  Claude Code, Claude.ai, Cursor, and other listed agents.
---

# Israeli Flight Compensation

## Problem

Israeli passengers are owed real money when a flight to or from Israel is cancelled, badly delayed, or overbooked, but most people never claim it, and those who do often hand 20 to 35 percent of the payout to a claim-handling service for a letter they could send themselves. The rights come from Israel's own Aviation Services Law (חוק טיבי), which is different from the European rules people half-remember, with different amounts and a different delay threshold. This skill works out exactly what the law owes the passenger and writes the demand letter for free.

## Instructions

You help a passenger determine their entitlement under the Aviation Services Law (Compensation and Assistance for Flight Cancellation or Change of Conditions), 2012, and produce a demand letter. Read `references/compensation-table.md` for the full rate table and thresholds before quoting any figure.

### Step 1: Confirm the law even applies (scope gate)

The Aviation Services Law applies only to a flight that departs from Israel OR arrives to Israel (including itineraries with a stopover), on any carrier, Israeli or foreign. Domestic Israeli flights are covered under separate regulations with a 3-hour threshold.

If the flight neither departs from nor arrives to Israel, STOP and tell the user this law does not apply. A flight within or out of the EU may be covered by EU Regulation 261/2004 instead, which has different amounts (250/400/600 EUR) and a 3-hour delay threshold. Never apply the Israeli amounts to a non-Israel flight, and never apply EU261 amounts to an Israeli claim.

### Step 2: Classify the disruption

Ask what happened and map it to one trigger:

- Cancellation: the airline cancelled. Compensation is owed when notice was less than 14 days before departure and no qualifying alternative was offered.
- Delay treated as cancellation: the flight departed 8 or more hours late (international), or 3 or more hours late (domestic).
- Denied boarding (overbooking): the passenger was bumped and did NOT volunteer to give up the seat.
- Early departure: the flight was moved earlier by more than 8 hours with less than 14 days notice.
- Downgrade: the passenger was moved to a lower class than booked.

### Step 3: Gather the inputs for the amount

Collect: the origin and final destination (to get the distance band), the length of the delay, how much notice the airline gave, whether the passenger accepted an alternative flight and how late that alternative arrived versus the original, and the flight date (to check the Iron Swords war-period exemption windows).

### Step 4: Compute the entitlement

Use the figures in `references/compensation-table.md`, or run the helper for a clean breakdown:

```bash
python3 scripts/compensation_calc.py --distance-km 3000 --delay-hours 9
python3 scripts/compensation_calc.py --distance-km 6000 --delay-hours 9 \
    --alternative-accepted --alternative-arrival-delay-hours 3
```

The monetary amount is set by distance band (2026 figures): up to 2,000 km, then 2,000 to 4,500 km, then over 4,500 km. Quote the band amount from the reference file and tell the user these amounts are CPI-updated every January so they should confirm the current-year figure. Apply the 50 percent reduction only if the passenger accepted an alternative that arrived within the per-distance window.

Separately from the money, explain the assistance the airline owed during the wait (food and communication after 2 hours; accommodation and transport, or a refund-or-alternative choice, after 5 hours). Assistance is owed even when an exemption removes the monetary compensation.

### Step 5: Check exemptions before promising money

The airline owes no monetary compensation if the cause was an extraordinary circumstance beyond its control and it did everything it could to operate the flight. Israeli case law reads this narrowly, a routine technical fault is usually not an exemption, so do not concede an exemption just because the airline asserts one. Also check the flight date against the Iron Swords (Amendment 2) exempt war-period windows: for those specific dates the monetary compensation is statutorily waived, though assistance and the refund or alternative-flight choice still stand.

### Step 6: Draft the demand letter

Write a short, firm Hebrew letter to the airline that states the flight details, the trigger, the exact amount owed with the legal basis (חוק שירותי תעופה), and a statement that the passenger will file a small claims suit if unpaid. Cite the statutory payment deadlines so the demand has teeth: a fare refund is due within 21 days of a written request, and the First Schedule monetary compensation (cancellation, long delay, early departure) is due within 45 days of a written request. If the disruption caused real extra costs (an unplanned hotel night, a missed connection, replacement tickets), note that these consequential losses are claimed in addition to the statutory amount, with receipts. Keep Hebrew natural and direct. Attach the booking, the boarding pass or check-in proof, and any evidence of the disruption (the airline's cancellation or delay notice, an SMS, or a screenshot of the airport board).

### Step 7: Route the escalation

If the airline refuses or ignores the demand, the next step is a small claims suit (תביעה קטנה). Hand the user off to the israeli-small-claims-court skill for drafting and filing. In parallel, a complaint can go to the Civil Aviation Authority and the Israeli Consumer Council. Remind the user that the limitation period for a claim under this law is 4 years from the disruption.

## Examples

### Example 1: Long-delayed flight from Europe

User says: "My TLV to Rome flight left 9 hours late. Am I owed anything?"
Actions:
1. Scope: TLV departure, the law applies.
2. Trigger: 9-hour delay is over the 8-hour international threshold, treated as a cancellation.
3. Distance: TLV to Rome is under 2,000 km, so the band is the first one (1,530 NIS as of 2026).
4. Run `python3 scripts/compensation_calc.py --distance-km 1500 --delay-hours 9`.
Result: Explain the amount, the assistance the airline owed during the wait, and draft the demand letter.

### Example 2: Cancelled flight with last-minute notice

User says: "El Al cancelled our flight to New York 3 days before. Family of four."
Actions:
1. Scope and trigger: cancellation with under 14 days notice, the law applies.
2. Distance: TLV to New York is over 4,500 km, so the top band (3,670 NIS as of 2026), per passenger.
3. Explain the refund-versus-rebooking choice and that each passenger has a separate claim.
Result: Compute the total, explain the choice, draft a single demand letter listing all four passengers.

### Example 3: Old disruption, still claimable

User says: "A flight got cancelled on me about 3 years ago, too late to do anything?"
Actions:
1. Check the date against the 4-year limitation period.
2. If within 4 years, proceed to classify and compute as normal.
Result: Confirm it is still claimable and draft the demand letter.

## Recommended MCP Servers

| MCP | Why | Source |
|---|---|---|
| ben-gurion-flights | Pull real-time and recent Ben Gurion (TLV) arrivals and departures from the Israel Airports Authority feed to evidence that a flight was delayed or cancelled, which strengthens the demand letter and a later small claims filing. | https://www.iaa.gov.il/ |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Aviation Services Law (full statute, Nevo) | https://www.nevo.co.il/law_html/law00/119611.htm | Distance bands, the 50 percent windows, the 4-year limitation, the scope clause |
| Statutory passenger-rights notice (El Al PDF) | https://www.elal.com/SiteCollectionDocuments/About-ELAL/Passengers-Rights/Aviation-Services-Law-HE-200918.pdf | The 2, 5, and 8-hour assistance ladder, denied boarding, downgrade, early departure |
| Kol Zchut, compensation for a cancelled flight | https://www.kolzchut.org.il/he/פיצוי_במקרה_של_טיסה_שהתבטלה | The 2026 amounts, extraordinary circumstances, the limitation period |
| Civil Aviation Authority of Israel | https://www.gov.il/he/departments/civil_aviation_authority_of_israel | The regulator and the complaint channel |
| Israeli Consumer Council, aviation rights | https://www.consumers.org.il/category/aviation-law-benefits | Consumer-side guidance and the complaint route |

## Bundled Resources

### Scripts
- `scripts/compensation_calc.py` -- Computes the entitlement (amount by distance band, the 8/3-hour thresholds, the 50 percent reduction, exemptions). Run: `python3 scripts/compensation_calc.py --example`

### References
- `references/compensation-table.md` -- The full 2026 rate table, assistance ladder, exemptions, and scope. Consult before quoting any figure.
- `references/domain-checklist.md` -- The coverage contract for this skill.

## Gotchas

- Do not use EU261 numbers. The single most common error is quoting 250/400/600 EUR or the EU261 3-hour delay threshold for an Israel flight. Israel's law is NIS-denominated (1,530 / 2,450 / 3,670 as of 2026) with an 8-hour international delay threshold. They are different regimes.
- The amounts change every January. They are CPI-linked and rounded to the nearest 10 NIS. A figure that was right last year may be stale. Always say "as of 2026, confirm the current-year amount."
- Assistance and money are separate. A passenger can be owed food, accommodation, and a refund even when an exemption (or the Iron Swords window) removes the monetary compensation. Do not collapse the two.
- An accepted alternative can halve the money, but only if it arrived within the 2, 3, or 4-hour window for the distance. Outside the window, the full amount stands. Do not apply the 50 percent reduction automatically just because a rebooking happened.
- Do not concede an "extraordinary circumstances" exemption on the airline's say-so. Israeli case law reads it narrowly; a routine technical or crewing fault usually does not qualify.
- Per-passenger, not per-booking. Each passenger on the reservation has their own claim. A family of four is four claims.

## Troubleshooting

### Error: "The user is sure it is 600 euros"
Cause: They are thinking of EU261, not the Israeli law.
Solution: Explain that for a flight to or from Israel, the Israeli Aviation Services Law governs, with NIS amounts. EU261 only applies to qualifying EU flights, and the two cannot be combined for the same flight.

### Error: "The airline says it was weather / a technical fault, so nothing is owed"
Cause: The airline is asserting an extraordinary-circumstances exemption.
Solution: Assistance is still owed regardless. For the money, the exemption only holds if the cause was genuinely beyond the airline's control AND it did everything possible. A routine technical fault usually does not qualify. Keep the demand and let the airline prove the exemption.

### Error: "I cannot find the exact flight distance"
Cause: Borderline distance between two bands.
Solution: Use a great-circle distance lookup for the origin-to-final-destination pair. For a connecting itinerary use the whole-journey distance. If still borderline, state both possible amounts and note which band applies at the exact distance.
