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

    rps_name = {
        0: "Scissors",
        1: "Rock",
        2: "Paper",
    }

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

    # Win, Lose, Draw
    wld_points = {
        "win": 6,  # Win
        "lose": 0,  # Lose
        "draw": 3,  # Draw
    }

    my_score = 0
    for line in df:
        # Swapped me to player 1
        player2, player1 = line.strip().split()
        player1, player2 = rps_strategy[player1], rps_value[player2]

        move = rps_move_points[(player1 + player2) % 3]

        current_round = 0
        match player1:
            case -1:
                current_round = wld_points["lose"]
            case 0:
                current_round = wld_points["draw"]
            case 1:
                current_round = wld_points["win"]
        my_score += move + current_round
    print(f"My Score: { my_score }")


if __name__ == "__main__":
    main()


# Correcg Answer: 13726
#        print(f"Scissors > Paper > Rock > Scissors")
#        print(f"{ player1 }, { player2 }")
#        print(f"P1 + P2 = { (player1 + player2) % 3}")
#        print(f"Move: { move }")
