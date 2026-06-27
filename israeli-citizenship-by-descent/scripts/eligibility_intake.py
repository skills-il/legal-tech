#!/usr/bin/env python3
"""
eligibility_intake.py - build a structured ancestry-and-documents worksheet for a
European citizenship-by-descent / restitution case, from the Israeli side.

This does NOT decide eligibility and contains no legal thresholds or country
rules (those live in SKILL.md and change often). It only organizes the family
chain and produces a starting document checklist the user can take to the
relevant consulate or a lawyer.

Usage:
    python eligibility_intake.py            # interactive
    python eligibility_intake.py --blank    # print an empty worksheet to fill in
"""

import argparse
import sys

GENERIC_DOCS = [
    "Anchor ancestor's birth certificate (or archival birth record)",
    "Anchor ancestor's marriage certificate (if relevant to the chain)",
    "Anchor ancestor's proof of emigration / loss or denial of citizenship "
    "(ship manifest, naturalization file, expulsion or persecution record, "
    "Yad Vashem or national-archive reference)",
    "Each intermediate link's birth and marriage certificates (unbroken chain)",
    "Your own birth certificate",
    "Your Israeli population-registry extract (tamtzit rishum, standard or extended)",
    "Your valid Israeli passport / teudat zehut",
    "Name-equivalence (same-person) notarized affidavit if any name is spelled "
    "differently across documents",
]

NEXT_STEPS = [
    "Identify the candidate route(s) by matching the family story to the country "
    "table in SKILL.md (a family can qualify under more than one).",
    "For each document above, determine the correct Israeli apostille authority "
    "(courts / Ministry of Justice channel for notarized and court documents; "
    "Ministry of Foreign Affairs for other public documents).",
    "Confirm the destination country's translation rule: an Israeli notarial "
    "translation, or a sworn/court translator registered in that country.",
    "Check the relevant consulate's current published requirements and timeline.",
    "For a contested lineage or a broken chain, consult a licensed immigration "
    "lawyer before filing.",
]


def field(label):
    try:
        return input(f"{label}: ").strip()
    except EOFError:
        return ""


def run_interactive():
    print("== Ancestry and documents worksheet ==\n")
    anchor = field("Anchor ancestor (name + relationship, e.g. 'paternal grandfather')")
    origin = field("Their country/region of origin")
    story = field("What happened and when (emigration / flight / persecution / loss of citizenship + dates)")
    docs_have = field("Documents you already have (comma-separated)")
    chain = field("Living chain from the ancestor to you (each birth/marriage/name change)")

    print("\n----------------------------------------")
    print("CASE SUMMARY")
    print("----------------------------------------")
    print(f"Anchor ancestor : {anchor or '(fill in)'}")
    print(f"Origin          : {origin or '(fill in)'}")
    print(f"Family story    : {story or '(fill in)'}")
    print(f"Documents on hand: {docs_have or '(none listed)'}")
    print(f"Chain           : {chain or '(fill in)'}")

    print("\n----------------------------------------")
    print("STARTING DOCUMENT CHECKLIST (generic - refine per route)")
    print("----------------------------------------")
    for i, d in enumerate(GENERIC_DOCS, 1):
        print(f"  [ ] {i}. {d}")

    print("\n----------------------------------------")
    print("NEXT STEPS")
    print("----------------------------------------")
    for i, s in enumerate(NEXT_STEPS, 1):
        print(f"  {i}. {s}")
    print("\nNote: this worksheet does not determine eligibility. Confirm every "
          "route-specific rule with the consulate or a licensed lawyer.")


def run_blank():
    print("== Ancestry and documents worksheet (blank) ==\n")
    for label in [
        "Anchor ancestor (name + relationship)",
        "Country/region of origin",
        "What happened and when",
        "Documents you already have",
        "Living chain from the ancestor to you",
    ]:
        print(f"{label}:\n    ____________________\n")
    print("Starting document checklist:")
    for i, d in enumerate(GENERIC_DOCS, 1):
        print(f"  [ ] {i}. {d}")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--blank", action="store_true", help="print an empty worksheet")
    args = p.parse_args()
    if args.blank or not sys.stdin.isatty():
        run_blank()
    else:
        run_interactive()


if __name__ == "__main__":
    main()
