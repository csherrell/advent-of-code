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
    return arguments["-i"]

def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df):
    # Rock, Paper, Scissors
    rps_move = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }

    rps_value = {
        "A": 1,  # Player 1 Rock
        "B": 2,  # Player 1 Paper
        "C": 3,  # Player 1 Scissors
        "X": 1,  # Player 2 Rock
        "Y": 2,  # Player 2 Paper
        "Z": 3,  # Player 2 Scissors
    }

    rps_name = {
        "A": "Rock",  # Player 1 Rock
        "B": "Paper",  # Player 1 Paper
        "C": "Scissors",  # Player 1 Scissors
        "X": "Rock",  # Player 2 Rock
        "Y": "Paper",  # Player 2 Paper
        "Z": "Scissors",  # Player 2 Scissors
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

        current_round = 0
        # Short Circuit Evaluation
        if player1 == rps_move["Rock"] and player2 == rps_move["Scissors"]:  # Win
            current_round = win
        elif player1 == rps_move["Scissors"] and player2 == rps_move["Rock"]:  # Lose
            current_round = lose
        elif player1 > player2:  # Win
            current_round = win
        elif player1 < player2:  # Lose
            current_round = lose
        else:  # Draw
            current_round = draw
        my_score += player1 + current_round
    return my_score

def print_results(my_score):
    print(f"My Score: { my_score }")


def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute
    - Exit with proper return code
    """

    print_results(process_data(read_file(docopt_handler())))


if __name__ == "__main__":
    main()
