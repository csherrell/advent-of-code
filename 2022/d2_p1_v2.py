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

    # Rock, Paper, Scissors
    rps_move = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }

    rps_name = {
        1: "Rock",
        2: "Paper",
        3: "Scissors",
    }

    rps_value = {
        "A": 1,  # Player 1 Rock
        "B": 2,  # Player 1 Paper
        "C": 3,  # Player 1 Scissors
        "X": 1,  # Player 2 Rock
        "Y": 2,  # Player 2 Paper
        "Z": 3,  # Player 2 Scissors
    }

    # Win, Lose, Draw
    win = 6  # Win
    lose = 0  # Lose
    draw = 3  # Draw

    my_score = 0
    for line in df:
        # Swapped me to player 1
        player2, player1 = line.strip().split()

        player1, player2 = rps_value[player1], rps_value[player2]

        print(f"Scissors > Paper > Rock > Scissors")
        print(f"{ rps_name[player1] }, { rps_name[player2] }")
        print(player1 - player2)

        current_round = 0
        match player1 - player2:
            case -2:
                print("Win")
                current_round = win
            case -1:
                print("Lose")
                current_round = lose
            case 0:
                print("Draw")
                current_round = draw
            case 1:
                print("Win")
                current_round = win
            case 2:
                print("Lose")
                current_round = lose
        my_score += player1 + current_round
    print(f"My Score: { my_score }")


if __name__ == "__main__":
    main()
