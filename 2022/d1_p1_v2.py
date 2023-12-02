#!/usr/bin/env python3


"""
Advent of Code 2022 Day 1 Puzzle 1

Usage:
  aoc_d1_p1 -i <input_file>
  aoc_d1_p1 -h | --help
  aoc_d1_p1 --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -i <input_file> Puzzle Input File
"""

from docopt import docopt


def docopt_handler():
    arguments = docopt(__doc__)
    # print(f'{ arguments }')
    return arguments["-i"]


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df):
    elven_bread = []
    calories = 0
    total_calories = 0
    for line in df:
        line = line.strip()
        if line:
            calories += int(line)
        else:
            elven_bread.append(calories)
            calories = 0
    else:
        elven_bread.append(calories)
    return elven_bread


def print_results(elven_bread):
    print(f"Summary ----------------------")
    print(f"Total: { sum(elven_bread) }")
    print(f"Max: { max(elven_bread) }")

    elven_bread.sort(reverse=True)
    print(f"Top Three: { sum(elven_bread[:3]) }")

    while len(elven_bread) > 3:
        elven_bread.remove(min(elven_bread))
    print(f"Top Three: { sum(elven_bread) }")


def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    print_results(process_data(read_file(docopt_handler())))


if __name__ == "__main__":
    main()
