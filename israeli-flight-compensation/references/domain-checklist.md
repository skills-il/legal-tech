# Domain Coverage Checklist, israeli-flight-compensation

Generated: 2026-06-23 via research on: nevo.co.il (statute text), El Al statutory passenger-rights notice PDF, kolzchut.org.il, Civil Aviation Authority (gov.il), Israeli Consumer Council, practitioner sources (rotbaumlaw).

Law: Aviation Services Law (Compensation and Assistance for Flight Cancellation or Change of Conditions), 2012 (חוק שירותי תעופה (פיצוי וסיוע בשל ביטול טיסה או שינוי בתנאיה), התשע"ב-2012), known as "חוק טיבי" / the Tibi Law. DISTINCT from EU Regulation 261/2004.

## Must cover (core)

- [x] Eligibility triggers, classify the event: cancellation with under 14 days notice and no qualifying alternative; delay treated as cancellation (international 8 hours+, domestic 3 hours+); involuntary denied boarding (overbooking) where the passenger did not give up the seat; downgrade to a lower class; early departure (5 to 8 hours, refund or alternative; over 8 hours, also money). Source: nevo statute, El Al notice. Why core: the entire entitlement turns on which trigger applies.
- [x] Full compensation table by distance band (2026 in force): up to 2,000 km is 1,530 NIS; 2,000 to 4,500 km is 2,450 NIS; over 4,500 km is 3,670 NIS. Source: kolzchut, rotbaumlaw. Why core: this is the money figure the user is owed.
- [x] CPI annual update: amounts updated on January 1 each year, rounded to nearest 10 NIS. Source: rotbaumlaw / statute. Why core: a stale figure misstates the amount owed; the skill must caveat "as of 2026".
- [x] Delay-hour thresholds (international): 2 hours (food + communication), 5 hours (adds accommodation + ground transport, or refund/alternative choice), 8 hours (treated as cancellation, monetary compensation). Source: El Al notice. Why core: the assistance ladder.
- [x] Assistance obligations: meals/refreshments, communication (2 calls + fax/email), hotel accommodation + transfers, the passenger's choice between full refund and an alternative flight. Owed even when monetary compensation is exempt. Source: El Al notice, kolzchut. Why core: assistance is a separate entitlement from the money.
- [x] The 50% reduction rule: airline may pay half if it offered an accepted alternative arriving within up to 2h (<=2,000 km), 3h (<=4,500 km), 4h (>4,500 km). Source: nevo, El Al. Why core: directly halves the payout.
- [x] Exemptions: extraordinary circumstances beyond the airline's control where it did everything possible; plus the Iron Swords (Amendment 2) statutory exemption of specific war-period date windows from monetary compensation (assistance still owed). Source: kolzchut, rotbaumlaw. Why core: a valid exemption means zero money; getting this wrong over-promises.
- [x] Scope: flights departing from OR arriving to Israel (including stopovers); domestic flights under separate regulations. Source: nevo. Why core: the skill must reject non-Israel-nexus flights and never apply EU261 amounts.
- [x] Statute of limitations: 4 years from when the entitlement arose. Source: kolzchut. Why core: claimability cutoff.
- [x] How to file: written demand letter to the airline first (the skill's core output), then a small-claims suit (תביעה קטנה) if unpaid. Route the small-claims step to the israeli-small-claims-court skill. Source: practitioner guidance. Why core: the action path.
- [x] Regulator: Civil Aviation Authority of Israel (CAA) enforces and receives complaints; the Israeli Consumer Council also helps. Source: gov.il, consumers.org.il. Why core: escalation channel.

## Should cover (advanced / edge cases)

- [x] Connecting flights: distance band computed by origin-to-final-destination, not per leg.
- [x] Package-deal / charter flights: the organizer (מארגן) shares the obligation with the operator.
- [x] Montreal Convention for baggage: routed OUT (separate regime).
- [x] Post-October-2023 security-situation cancellations: explain the Amendment 2 exempt date windows and that assistance is still owed.
- [x] Voluntary give-up of seat vs involuntary denied boarding (only involuntary triggers statutory rights).
- [x] Downgrade compensation: the Second Schedule percentages (First to Business 60%, Business to Economy 80%, First to Economy 90%, First or Business to Economy over 4,500 km 100%) are verified from the statute and quoted in references/compensation-table.md.
- [x] Statutory payment deadlines: fare refund within 21 days of a written request, First Schedule compensation within 45 days of a written request, downgrade compensation within 21 days of the flight date.
- [x] Consequential losses (extra hotel, missed connection, replacement tickets) are claimable in addition to the fixed statutory amount, with receipts, in the same small claims suit.

## Out of scope (explicit, with rationale)

- Finding / booking flights, related skill: israeli-flight-finder handles search/booking. This skill is rights/claims only.
- Travel insurance claims, a private contractual matter, not the Aviation Services Law.
- Lost / damaged / delayed baggage, governed by the Montreal Convention, a distinct regime.
- Non-Israel-nexus flights (neither departing nor arriving Israel), the law does not apply; for intra-EU flights EU261 applies with DIFFERENT amounts (250/400/600 EUR, 3-hour threshold). The skill must never conflate the two.
- Criminal / safety / security incidents, regulator and police matters.

## Authoritative sources

- https://www.nevo.co.il/law_html/law00/119611.htm , full statute: distance bands, the 50% windows, the 4-year limitation, the scope clause, extraordinary-circumstances rule.
- https://www.elal.com/SiteCollectionDocuments/About-ELAL/Passengers-Rights/Aviation-Services-Law-HE-200918.pdf , statutory passenger-rights notice: the 2/5/8-hour assistance ladder, denied boarding, downgrade, early departure.
- https://www.kolzchut.org.il/he/פיצוי_במקרה_של_טיסה_שהתבטלה , plain-language: the 2026 amounts, extraordinary circumstances, the 4-year limitation.
- https://www.kolzchut.org.il/he/פיצוי_במקרה_של_טיסה_שהמריאה_באיחור_או_שהוקדמה , delay/early-departure rules, communication-services definition, domestic 3-hour rule.
- https://www.gov.il/he/departments/civil_aviation_authority_of_israel , regulator and complaint channel.
- https://www.consumers.org.il/category/aviation-law-benefits , consumer-side guidance and complaint route.
