#!/usr/bin/env python3
"""Two deterministic checks for Israeli wills and inheritance.

Offline, stdlib-only. It does NOT give legal advice; it applies two black-letter rules
from the Succession Law so an agent does not get them backwards:

1. order  -- which inheritance order to request (succession vs probate) based on whether
   a will exists.
2. witness -- whether a proposed witness is disqualified because they (or their spouse)
   are a beneficiary of the will.

Usage:
  python3 scripts/inheritance_helper.py order --has-will yes
  python3 scripts/inheritance_helper.py order --has-will no
  python3 scripts/inheritance_helper.py witness --beneficiaries "דנה,יוסי" --witnesses "דנה,השכן רון"
"""

import argparse
import sys


def cmd_order(has_will: str):
    hw = has_will.strip().lower()
    if hw in ("yes", "y", "true", "כן"):
        print("order: צו קיום צוואה (probate / will-execution order)")
        print("reason: a will exists, so it must be given binding effect.")
    elif hw in ("no", "n", "false", "לא"):
        print("order: צו ירושה (succession order)")
        print("reason: no will, so heirs are determined by law.")
    else:
        print(f"unknown value for --has-will: {has_will!r} (use yes/no)", file=sys.stderr)
        sys.exit(1)
    print("file at: the Inheritance Registrar (הרשם לענייני ירושה), online portal inheritance.justice.gov.il")
    print("note: a court only enters if an objection (התנגדות) is filed.")


def cmd_witness(beneficiaries: str, witnesses: str):
    bens = {b.strip() for b in beneficiaries.split(",") if b.strip()}
    wits = [w.strip() for w in witnesses.split(",") if w.strip()]
    if len(wits) < 2:
        print("WARNING: a witnessed will needs at least two witnesses.")
    bad = [w for w in wits if w in bens]
    if bad:
        print(f"INVALID witnesses (they are beneficiaries): {', '.join(bad)}")
        print("A witness, or a witness's spouse, may NOT be a beneficiary. That bequest would be void.")
        print("Fix: use neutral adult witnesses who inherit nothing.")
    else:
        print("witnesses look OK on the beneficiary rule.")
        print("Still confirm: each witness is an adult, and NOT the spouse of any beneficiary.")


def main():
    p = argparse.ArgumentParser(description="Israeli wills/inheritance deterministic checks.")
    sub = p.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("order", help="Which inheritance order to request.")
    o.add_argument("--has-will", required=True, help="yes or no")

    w = sub.add_parser("witness", help="Check witnesses are not beneficiaries.")
    w.add_argument("--beneficiaries", required=True, help="comma-separated names")
    w.add_argument("--witnesses", required=True, help="comma-separated names")

    args = p.parse_args()
    if args.cmd == "order":
        cmd_order(args.has_will)
    elif args.cmd == "witness":
        cmd_witness(args.beneficiaries, args.witnesses)


if __name__ == "__main__":
    main()
