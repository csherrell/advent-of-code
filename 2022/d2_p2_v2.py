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

from enum import Enum


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

    rps_value = {
        "A": 1,  # Player 1 Rock
        "B": 2,  # Player 1 Paper
        "C": 3,  # Player 1 Scissors
    }

    rps_strategy = {
        "X": -1,  # Player 2 - Lose
        "Y": 0,  # Player 2 - Draw
        "Z": 1,  # Player 2 - Win
    }

    rps_move_points = {
        0: 3,  # Scissors
        1: 1,  # Roack
        2: 2,  # Paper
    }

    wld_points = {
        -1: 0,  # Lose
        0: 3,  # Draw
        1: 6,  # Win
    }

    my_score = 0
    for line in df:
        # Swapped me to player 1
        player2, player1 = line.strip().split()
        player1, player2 = rps_strategy[player1], rps_value[player2]

        move = rps_move_points[(player1 + player2) % 3]

        my_score += move + wld_points[player1]

    print(f"My Score: { my_score }")


if __name__ == "__main__":
    main()


# Correcg Answer: 13726
