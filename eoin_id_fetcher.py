#!/usr/bin/env python3
"""
Dummy EOIN ID fetcher — returns a hardcoded EOIN ID.

Usage:
    python eoin_id_fetcher.py

This prints the EOIN ID to stdout (suitable for capturing in Octopus)
and also writes it to eoin_id.txt in the current directory.
"""

import sys

def get_dummy_eoin():
    # Hardcoded dummy EOIN ID — change as needed
    return "EOIN-0000-TEST"

def main():
    eoin = get_dummy_eoin()
    # Print so Octopus (or any wrapper) can capture stdout
    print(eoin)
    # Optional: write to file for later use
    try:
        with open("eoin_id.txt", "w", encoding="utf-8") as f:
            f.write(eoin)
    except Exception as ex:
        # Do not fail the script on file-write errors; just log to stderr
        print(f"Warning: failed to write eoin_id.txt: {ex}", file=sys.stderr)

if __name__ == "__main__":
    main()
