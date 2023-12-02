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

# Correct Answer: 12855

from docopt import docopt


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
        section_1, section_2 = line.split(",")
        section_1_start, section_1_end = section_1.split("-")
        section_2_start, section_2_end = section_2.split("-")
        section_1 = set(range(int(section_1_start), int(section_1_end) + 1))
        section_2 = set(range(int(section_2_start), int(section_2_end) + 1))

        intersection = section_1.intersection(section_2)
        if intersection:
            total += 1
    print(f"Total: { total }")


if __name__ == "__main__":
    main()
