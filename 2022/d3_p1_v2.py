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
    for line in df:
        line = line.strip()
        for item in line[0 : int(len(line) / 2)]:
            if item in line[int(len(line) / 2) :]:
                total += items.index(item)
                break

    print(f"Total: { total }")


if __name__ == "__main__":
    main()
