---
name: israeli-car-accident-claim
description: >-
  Guides a driver through the aftermath of a car accident in Israel: what to do and document at
  the scene, which insurance to claim under (compulsory vs comprehensive vs third-party), how the
  no-fault bodily-injury rule (PLATD) differs from fault-based property damage, how to fill the
  הודעה על תאונה report, the time limits, and when Karnit applies. Use when a user says "I had a
  car accident", "te'unat derachim", "the other driver hit me", "what do I do after a crash",
  "claim car damage from insurance", or "hit and run". Produces a scene checklist and a claim plan.
  Do NOT use for vehicle registration, test, or insurance shopping (use israeli-vehicle-manager),
  serious injury litigation (needs a lawyer), or DUI / criminal defense.
license: MIT
allowed-tools: 'Bash(python3:*)'
compatibility: >-
  Knowledge plus a Python decision-helper script (no network needed). Works with Claude Code,
  Claude.ai, Cursor, and other listed agents.
---

# Israeli Car Accident Claim

## Problem

A car accident in Israel is stressful and the rules are counter-intuitive: bodily injury is compensated with no regard to fault, while property damage is entirely fault-based, and people routinely claim from the wrong policy or miss the steps that the insurer later uses to reject the claim. Many drivers do not know that a police confirmation is a precondition for the claim, that there is a fund (Karnit) for hit-and-run and uninsured cases, or how long they have to act. This skill walks the driver through the scene and routes the claim to the right place.

## Problem boundary

This skill is about the accident and the claim. For registration renewal, the annual test (טסט), used-car checks, ownership transfer, or choosing an insurance policy, use the israeli-vehicle-manager skill, which owns that side and deliberately excludes accidents.

## Instructions

You help a driver act correctly after a road accident and route the claim. Read `references/claims-guide.md` for the full detail before advising. The single most important distinction to get right: bodily injury is no-fault, property damage is fault-based. Keep them separate at every step.

### Step 1: Safety and the first minutes at the scene

Tell the user to secure the scene (hazard lights, warning triangle, move to safety only if the vehicle is drivable and there are no injuries), check everyone for injuries, and call emergency services if anyone is hurt. If there are injuries or a death, or the other driver fled, police involvement is mandatory: the driver must stop, render aid, and report. Failing to stop or to help an injured person is a serious criminal offense under the Traffic Ordinance.

### Step 2: Document everything

Have the user photograph all vehicles, the damage, the license plates, the position on the road, signage, and any skid marks, and collect: the other driver's name, ID, phone, plate number, and their insurer and policy number, plus the names and phones of any witnesses. In a property-only accident the legal duty is to exchange these details on the spot (תקנה 145). In an injury accident there is the added duty to report to the police (תקנה 144).

If anyone is hurt, the medical paper trail matters more than the car photos for the claim: get examined the same day (ER or doctor), describe every affected body part to the doctor, and keep every medical record. An injury first mentioned weeks later is easy for the insurer or Karnit to dispute. If the accident happened on the way to or from work, it may also be a work accident, so report it to the National Insurance Institute (ביטוח לאומי) as well.

### Step 3: Get the police confirmation

A police confirmation (אישור משטרתי) is required for an injury claim and is standard for the online flow. For a property-only claim many insurers process on the basis of the הודעה על תאונה alone, but it is safest to obtain the confirmation, especially whenever anyone was hurt. When there are no injuries (or injured people were treated and released within 24 hours), the driver can file the gov.il online light-accident report and receive the confirmation by email. In more serious cases, report by phone or in person at a police station.

### Step 4: Route the claim to the right regime

This is the core decision. Run the helper for a clean routing, or apply the logic from `references/claims-guide.md`:

```bash
python3 scripts/claim_router.py --injuries --my-fault no --my-comprehensive
python3 scripts/claim_router.py --damage property --my-fault yes --other-insured yes
python3 scripts/claim_router.py --damage property --hit-and-run --injuries
```

- Bodily injury (anyone hurt): no-fault. The allocation rule (PLATD Section 3) decides which compulsory insurer pays: a driver and the passengers in a vehicle claim against that vehicle's own compulsory insurance (ביטוח חובה), and in a multi-vehicle crash each driver's own injury goes to his own vehicle's insurer, regardless of who was at fault. A pedestrian or cyclist claims against the vehicle that hit them. Do not chase the other driver's compulsory insurer for your own injuries. Compulsory insurance covers bodily injury only, never property.
- No-fault has hard exceptions (PLATD Section 7): a person is NOT entitled to bodily-injury compensation if they caused the accident deliberately, drove without a valid licence (a licence lapsed only for non-payment of the fee still counts), drove a vehicle without permission or a stolen one, used the vehicle for a felony, or drove with no valid compulsory insurance. If any applies, the "covered regardless of fault" framing does not hold; flag it and route to a lawyer.
- Property damage: fault-based. The at-fault driver or their insurer pays. A not-at-fault driver can claim from their own comprehensive (מקיף) and let the insurer recover from the at-fault party by subrogation (the deductible is refunded once that succeeds), or claim directly against the at-fault driver's third-party (צד ג') cover.
- Hit-and-run, untraced, or uninsured at-fault driver: for the bodily-injury side, Karnit (קרנית), the road-accident victims fund, is the address.

### Step 5: Fill the accident report and submit

Walk the driver through the standard insurer report (הודעה על תאונה). It is one-sided, filed with their own insurer (Israel has no joint two-driver form). It captures the insured and policy details, the driver, the accident details with a scene diagram and the impact zones and witnesses, the third-party details, and the insured's signed declaration. Notify the insurer immediately after the accident, then submit the form with the photos, the police confirmation, and a damage assessment.

### Step 6: Time limits and escalation

The driver must notify the insurer immediately. The statute of limitations is 7 years for both property and bodily-injury claims; a minor injured in an accident can sue until age 25 (the clock runs from age 18). If the insurer underpays or rejects unfairly, the driver can complain to the Public Inquiries Unit at the Capital Market, Insurance and Savings Authority (which does not bar going to court) and, for smaller property sums, file in small claims. Hand off to the israeli-small-claims-court skill for that.

### Step 7: Know when a lawyer is needed

A bodily-injury claim with lasting disability is decided by a medical committee and the courts and typically requires a lawyer. The law does not require a lawyer to start a claim, but for anything beyond minor injury you should still consult one. Frame this honestly: the skill helps document and understand rights, it does not replace a lawyer.

## Examples

### Example 1: Rear-ended, not at fault, minor damage

User says: "Someone hit me from behind at a light. My bumper is cracked, nobody's hurt."
Actions:
1. Property-only, no injuries: exchange details, photograph, file the gov.il light-accident report for the police confirmation.
2. Route: not at fault. Claim from your own comprehensive and let them subrogate, or claim against the other driver's third-party cover.
3. Run `python3 scripts/claim_router.py --damage property --my-fault no --my-comprehensive`.
Result: A scene checklist and a claim plan, plus the deductible-refund explanation.

### Example 2: Injury accident

User says: "I was in a crash, my passenger hurt her neck and went to the ER."
Actions:
1. Injuries: police involvement is mandatory, get the police confirmation.
2. Route: bodily injury is no-fault. The passenger claims from the compulsory insurance of the car she was in, regardless of fault.
3. Flag that a lasting-injury claim should go to a lawyer.
Result: The no-fault explanation, the documentation list, and a lawyer referral for the injury side.

### Example 3: Hit and run

User says: "Someone scraped my car in a lot and drove off, and I twisted my wrist getting out."
Actions:
1. Hit-and-run with injury: report to police, get the confirmation.
2. Route: for the bodily injury, Karnit is the address since the driver is untraced. The property scrape may fall on your own comprehensive.
Result: Explain Karnit for the injury and the comprehensive route for the property.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Road Accident Victims Compensation Law 1975 (PLATD, Nevo) | https://www.nevo.co.il/law_html/law00/4554.htm | The no-fault liability rule and the Karnit fund |
| Insurance Contract Law (Nevo) | https://www.nevo.co.il/law_html/law00/71902.htm | The duty to notify and the subrogation rule |
| Limitation Law 1958 (Nevo) | https://www.nevo.co.il/law_html/law00/71809.htm | The 7-year period and the minors rule |
| Traffic Regulations (Nevo) | https://www.nevo.co.il/law_html/law01/p230_011.htm | The scene duties for injury and property accidents |
| gov.il online accident report | https://www.gov.il/he/service/traffic-accident-notice | Eligibility for the online report and the police confirmation |
| Kol Zchut, hit-and-run and Karnit compensation | https://www.kolzchut.org.il/he/פיצוי_על_תאונת_פגע_וברח | When Karnit pays bodily-injury compensation |

## Bundled Resources

### Scripts
- `scripts/claim_router.py` -- Routes the claim to the right insurance or to Karnit and lists the time limits, from the injury/fault/insured inputs. Run: `python3 scripts/claim_router.py --example`

### References
- `references/claims-guide.md` -- The full guide: the 3 insurance types, no-fault vs fault, the scene duties, Karnit, time limits, subrogation, and escalation.
- `references/domain-checklist.md` -- The coverage contract for this skill.

## Gotchas

- Bodily injury is no-fault, property is fault-based. The most damaging error is mixing them. Injuries are claimed from the compulsory insurance regardless of fault; property damage follows fault. Never tell an injured passenger they cannot claim because the driver was at fault.
- Compulsory insurance never covers property. ביטוח חובה is bodily injury only. Your own car's dents are covered only by comprehensive (מקיף), and damage you cause to others' property by third-party (צד ג'). Do not promise a compulsory-insurance payout for a fender.
- The police confirmation is a precondition. Without the אישור משטרתי the insurer will not process the claim. Get it early, via the gov.il online report when eligible.
- The online report is only for light accidents. It applies when there are no injuries, or injured people were released within 24 hours. Anything more serious needs a phone or in-person police report.
- Karnit is for bodily injury, not property. The fund covers the injury side of hit-and-run, untraced, or uninsured-driver cases. It is not a route for repairing your car.
- Do not say "no lawyer needed" for an injury claim. A lasting-injury claim goes through a medical committee and usually needs a lawyer. State the rights, but recommend a lawyer for anything beyond minor injury.

## Troubleshooting

### Error: "The other driver was at fault, so my injuries are their insurance's problem"
Cause: Applying property (fault) logic to bodily injury.
Solution: Bodily injury is no-fault. The injured person claims from the compulsory insurance of the vehicle they were in or hit by, regardless of who was at fault. Fault matters for the property side, not the injury side.

### Error: "My own car is damaged but I only have compulsory insurance"
Cause: Expecting compulsory insurance to cover the vehicle.
Solution: Compulsory insurance covers bodily injury only. Your own car's damage is covered only if you hold comprehensive (מקיף). If you are not at fault, you can still claim your car's damage against the at-fault driver's third-party cover or sue them directly.

### Error: "The other driver drove off and I have no details"
Cause: Hit-and-run.
Solution: Report to the police immediately and get the confirmation. For bodily injury, Karnit (קרנית) compensates victims when the driver is untraced or uninsured. For your car's property damage, your own comprehensive policy is the route if you have one.
