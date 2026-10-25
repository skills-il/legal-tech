# Changelog

## [2.1.2] - 2026-10-25

### Changed
- Section 22: the body now says, as the reference already did, that a lease may arguably exclude the tenant's right to proceed without consent after an unreasonable refusal (s.22 is outside the 25יד(2) list); the court's power to permit the deal survives any lease term.
- Calculator: when a floor clause applies, the output says "No change" instead of "Increase +0.00".

## [2.1.1] - 2026-10-25

### Changed
- Reworded one checklist line (the condition-report annex) whose wording matched a Tank injection regex across a word boundary, a false positive present since v2.0.0.
- Moved the CBS API URL out of a comment in `scripts/rent-index-calculator.py` into evidence.json; the script makes no network calls. No change to content or figures.

## [2.1.0] - 2026-10-25

First release of this skill read in full by an independent legal reviewer (v1.4.0 and v2.0.0 were
verified by the author only). Two statutory errors were found and corrected, plus the time-sensitive
items now in force.

### Fixed
- Guarantors: chapter 2 of the Guarantee Law (s.21, a guarantee capped at or void without a stated sum; s.27, the protected-guarantor exhaustion rule) applies only where the creditor lends money in the ordinary course of business (ss.18-19). A private landlord normally does not, so the skill no longer tells a guarantor that an unstated sum releases them. Chapter 1 (s.8, demand on the tenant first) is stated as the rule that binds every guarantor.
- Set-off: section 25 makes debts arising from the tenancy set-off-able and 25יד(2) makes that non-waivable against the tenant. Reasonable expenses of a repair done after the landlord missed the 25ח(ב) deadline, with s.9(ב) notice, may be set off against rent. The skill previously said any such deduction was arrears.
- Whether 25י(ג)-(ה) bind a deed signed by a third-party guarantor is now flagged as arguable rather than settled.
- `references/fair-rental-law-summary.md` rewritten: it still carried errors SKILL.md had already corrected (landlord termination "per contract", landlord entry, the wear-and-tear test, an oral lease giving "minimal protection", an invented deposit-interest rule, a wrong Second Schedule list).
- `references/contract-checklist.md`: no statutory "structural" repair list; cancellation and notice rows follow 25יג.
- Reference links: the gov.il page carries the amendment, not a sample contract; Israel has no rent control.
- Replaced the recommended `israel-law` MCP, which is not published, with `israel-statistics`.

### Added
- Eviction: expiry of the term and s.19(א) reasonable notice where no term was agreed or the parties held over; the possession track cited as regulation 81 of the Civil Procedure Regulations 2018 (possession only, defence within 30 days). Self-help: s.11 undisturbed use, Land Law ss.18(ב) and 19.
- The 2026 "noten arvut acher" guarantee in section 25י is now in force (since 30.9.2026).
- Section 25טו(4): the threshold has been indexed every January since 2018, so it is now above 20,000 NIS.
- The model lease under 25ד: a draft was circulated for comment on 2.2.2026; no final regulations found.
- Landlord tax: the 2026 exemption ceiling (5,654 NIS a month, partial below 11,308) and the 10% track.
- Calculator: CPI through 2026-09, a `--floor` option for floor clauses, and help text on the "known index" base convention.

## [2.0.0] - 2026-08-30

Second pass on the same skill, from an expert legal review that followed the v1.4.0 release. v1.4.0
carried the four reported defects plus three found while verifying them; this release adds the
remaining findings. Restructured so SKILL.md stays within its size limit: the section-by-section
statutory text now lives in `references/statutory-provisions.md`.

### Fixed
- Habitability: replaced an invented list of amenities with the closed six-item First Schedule, including the partition between the toilet and the apartment, the lockable main entrance door and the safety/health catch-all. Added 25ו(ב) (delivering an unfit apartment is a BREACH) and 25יד(1) (25ו cannot be varied at all).
- Section 25ט was reduced to the broker fee. Added the closed 25ט(א) list and all three 25ט(ב) prohibitions, notably the bars on charging the tenant for buying or upgrading fixed installations and for building insurance, the two commonest overcharges in the market.
- Eviction: removed "landlord needs the property for personal use", which belongs to protected tenancies and is not a ground for an unprotected residential lease. Named the תביעה לפינוי מושכר track instead of the small claims court, and added an explicit warning that self-help eviction (changing locks, removing belongings, cutting utilities) is unlawful.
- Section 25יד is now stated as the operative list of which provisions may be varied and in which direction, rather than a general assertion that the rules cannot be contracted around.
- Entry and privacy: there is no statutory notice period for landlord entry. The previous "24 hours" figure was presented as a rule.
- Corrected שטר הון to שטר חוב throughout, and removed the non-existent "rent tribunal" (ועדת שכירות) from the dispute-resolution options.

### Added
- Sections 25ד (gap-filling by the model lease), 25ז(ג) (handover instructions), 25יא (written notice before the apartment is handed to a buyer), 25יב (the 90-day landlord and 60-day tenant option deadlines) and 25טו(ג) (sub-letting duties stay with the head landlord), all previously absent.
- Section 25יג(א): a clause letting only the landlord cancel without breach is VOID unless the tenant has an equivalent right. 25יג(ב) fixes the 90/60 minimum notice by statute, previously described as "the standard model".
- Guarantee Law 5727-1967: s.21(ב) releases an ערב יחיד entirely where the deed states no fixed sum, and s.27 bars action against an ערב מוגן before execution against the tenant is exhausted.
- `references/statutory-provisions.md`, a section-by-section reference for 25א-25טו, both Schedules and the guarantor rules.
- An explicit note that on a lease with an option it is unsettled whether "one third of תקופת השכירות" means the initial or the extended term, rather than quoting one ceiling with false confidence.

## [1.4.0] - 2026-08-29

Corrections from a public report (four items, all verified against the consolidated statute), plus
three defects found while verifying them. A larger remediation covering further findings from an
expert legal review is prepared but held pending an independent review pass.

### Fixed
- Section 25י(ב)'s ceiling is scoped to guarantees "involving a monetary outlay by the tenant" (cash, bank guarantee). A promissory note and personal guarantors are not counted in it. The reference file previously said "the total of all guarantees".
- Sections 25י(ג), (ד) and (ה) bind EVERY guarantee, including those outside the ceiling: realisation only on the four closed grounds, advance notice and a chance to cure before realising, and return within 60 days including the guarantee's fruits. Realisation grounds replace the previous loose "damages beyond normal wear" description.
- The 20,000 NIS exclusion threshold in section 25טו(4) is updated every 1 January by the CPI and rounded to the nearest 10 NIS. Both language files previously stated it was not index-linked.
- The landlord's pre-contract disclosure duty is item 7 of the Second Schedule, mandated by section 25ג. It was attributed to section 25ב, which governs the written form of the contract only.
- The repair remedy: section 25ח(ג) applies s.9(א), giving reimbursement of reasonable expenses or a PROPORTIONAL rent reduction. The skill said the tenant may deduct the repair cost from the rent, advice that puts a tenant in arrears and hands the landlord a 25י(ג)(1) realisation ground and an eviction claim.
- Family leases are NOT excluded from the chapter. Section 25טו(ב) disapplies only 25יד(2) for a קרוב, so relatives may contract out but every protection otherwise applies. They were listed alongside hotels and dormitories as excluded.
- The bundled calculator's CPI table was invented data understating 2022-2025 inflation by roughly a third while emitting a shekel figure. Replaced with the official CBS series 120010, chain-linked across the 2020/2022/2024 base changes and extended to 2026-07.
- Replaced the Knesset legislation portal reference link, which returns 401.
- Corrected the 10-year exclusion (it requires that the landlord have no earlier cancellation right) and the 3-month exclusion (no extension option).

### Added
- The 2026 amendment (Sefer HaChukkim 3510, 31.3.2026) adding a "notenn aruvah acher" guarantee to section 25י, in force 30.9.2026.
- A note that where guarantors are used, an ערב יחיד is released entirely if the deed states no fixed sum (Guarantee Law 5727-1967, s.21(ב)).
- Reference links to the consolidated law text and the official Sefer HaChukkim publication.

### Changed
- Evidence entries for the deposit cap, the exclusion threshold, the disclosure duty, the written-form rule and the repair remedy now cite the statute directly instead of a secondary summary.

All notable changes to this skill are documented here.

## [1.3.0] - 2026-08-09

### Added

- נוסף פרק "הבהרה משפטית" בראש SKILL.md ו-SKILL_HE.md, המפרט מה הכלי עושה, מה הוא אינו, ולאיזה בעל מקצוע מוסמך יש לפנות.

### Changed

- התיאור נפתח כעת בהבהרה קצרה, כך שהיא נראית גם בכרטיס ובתוצאות החיפוש.
