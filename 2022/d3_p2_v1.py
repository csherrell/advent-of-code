#!/usr/bin/env python3

"""
Advent of Code 2022 Day 1 Puzzle 1

Usage:
  aoc_d2_p1 -i <input_file>
  aoc_d2_p1 -h | --help
  aoc_d2_p1 --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -i <input_file> Puzzle Input File
"""

from docopt import docopt

import string


items = list(string.ascii_letters)
items.insert(0, None)


def docopt_handler():
    arguments = docopt(__doc__)
    # print(f'{ arguments }')
    return arguments["-i"]


def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute
    - Exit with proper return code
    """

    input_file = docopt_handler()

    with open(input_file) as file:
        df = file.readlines()

    total = 0
    while df:
        elf_1 = df.pop(0).strip()
        elf_2 = df.pop(0).strip()
        elf_3 = df.pop(0).strip()

        elf_1 = [*elf_1]
        elf_2 = [*elf_2]
        elf_3 = [*elf_3]

        # Find shortest list
        elf_s = elf_1 if len(elf_1) < len(elf_2) else elf_2
        elf_s = elf_s if len(elf_s) < len(elf_3) else elf_3

        for item in elf_s:
            if item in elf_1 and item in elf_2 and item in elf_3:
                total += items.index(item)
                break

    print(f"Total: { total }")


if __name__ == "__main__":
    main()
