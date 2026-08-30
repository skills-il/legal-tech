# Changelog

All notable changes to this skill.

## [1.0.1] - 2026-08-31

### Fixed

Two substantive corrections found by a late domain review, both verified against the statutory
text before being applied.

- **The six-apartment rule was misread.** v1.0.0 said that for a beit meshutaf of six apartments
  or more the demolition-and-rebuild majority is computed under section 4 of the pinui-binui law
  "NOT under the plain two-thirds rule", implying a different and higher threshold. That is wrong.
  Section 4 is headed "baalut al yoter mi-dira achat" and is a DISCOUNT rule: an owner holding more
  than thirty percent of the apartments is counted as holding thirty percent plus one third of the
  excess. The two-thirds threshold is unchanged; only the counting changes. This mattered because
  most Israeli apartment buildings have six or more apartments. The bundled script encoded the same
  error and has been corrected, and it now shows the discount arithmetic via a new
  `--largest-owner-apartments` flag.
- **The refusal grounds are a named-subset import, and v1.0.0 implied they were not.** All seven
  grounds in s.2(b) apply in pinui-binui, and all seven are imported into the demolition track by
  s.5a(a2). But the new-apartment track imports **only grounds (1), (3) and (4)** via s.5(b1)(2).
  The disability grounds, the kashish alternatives menu and the 75-plus ground do not cross over;
  that track carries a separate flat prohibition at s.5(b1)(1) instead. Telling an owner on the
  new-apartment track that the kashish menu is available to them was wrong.

### Added

- Worked explanation of the section 4 discount, with an example.
- A per-track table of which refusal grounds actually apply.
- Four further entries in the checklist's "Known bad figures", including two errors that were
  present in this skill's own commissioning brief and were caught before they reached the content:
  the pinui-binui tax exemption is perek chamishi 4, not 5, and chok pinui u-vinui (pitzuyim) is
  the same statute as chok pinui u-vinui (idud mizmei pinui u-vinui), renamed by Amendment 6.

## [1.0.0] - 2026-08-31

### Added

Initial release.

Explains Israeli urban renewal from the apartment owner's side: the pinui-binui and
strengthening tracks, the statutory majorities and how they vary by track, work type and
building size, the seven grounds on which the law treats a refusal to sign as reasonable, the
statutory minimum content of the transaction, the organizer's duties to the owners, and the free
statutory ombudsman who investigates complaints of pressure to sign.

Notes on scope, which are deliberate rather than incidental:

- The skill explains and does not advise. It does not read the user's own agreement, value an
  apartment, state what compensation is owed, or rule on whether a refusal is reasonable. Those
  are reserved acts under Israeli law and belong to an advocate, a shamai mekarkein, and the
  court or the mefake'ach.
- Every statutory figure was read from the statute's own text layer rather than from secondary
  guides, which were found to be wrong at a high rate in this domain. See
  `references/domain-checklist.md`, "Known bad figures".
- Both the current and the superseded demolition-and-rebuild thresholds are documented, because
  the superseded four-fifths rule still governs matters measured under the pre-1.7.2023 regime.
- The skill states the correct position on TAMA 38: it stopped taking new permit applications,
  but Amendment 7 in 2022 widened the definition of the strengthening plan so the owner
  protections carry over to the municipal plans that succeeded it.

### Origin

Reframed from a public directory submission that asked for a tool to review a signed pinui-binui
agreement and state what compensation the owner was owed, without legal advice. That shape could
not be published. The underlying need, an owner who cannot fund private representation and does
not understand what is happening, is met here by explaining the law and routing to the free
statutory complaint channel.
