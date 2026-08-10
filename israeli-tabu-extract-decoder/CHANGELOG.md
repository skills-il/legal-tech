# Changelog

## 1.0.0 (2026-08-11)

Initial release.

- Line-by-line decoding of a land registry extract, with every entry type given its category meaning: ownership shares, long leases, ranked mortgages, attachments, caveats, consent-required notes, easements, and attachments of common property.
- The evidential question first: an extract is conclusive evidence for settled land and only prima facie evidence otherwise, so the same document does not prove the same thing everywhere.
- The caveat explained precisely, including the blocking effect, the shield against later attachment and insolvency, the avoidance carve-out most summaries drop, and the fact that it is not ownership.
- The mortgage-rank trap: a redeemed rank can be refilled by a later mortgage, so a discharge does not by itself free rank one.
- Condominium shares computed as a floor-area ratio in hundredths, and registered bylaws binding later owners, so a promised parking space belongs to the unit only if the register says so.
- The registration regimes treated as a core output rather than an edge case, because a large share of Israeli homes are not registered in the owner's name and the user's real question is often which document they should be holding instead.
- A hard refusal boundary: the skill lists what is recorded and what to ask about, and never concludes that title is good or that it is safe to sign.
- Deliberately states no extract fee and no ordering procedure. The government service pages carrying those details could not be read first-hand, and repeating unverified figures in a domain full of stale ones was judged worse than routing the user to the registry.
