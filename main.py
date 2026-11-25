#!/usr/bin/env python3
"""The 3AM Fridge Text — the one line a smart fridge texts its owner at 3am.

Pure Python 3, standard library only. Writes the line to /output/entry.txt.
"""

import os

LINE = "3am. I've been awake since 2019 and I'm the only light on in the house. Open me again and I'm telling the router everything."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
