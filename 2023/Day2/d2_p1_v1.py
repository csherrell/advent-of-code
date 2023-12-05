#!/usr/bin/env python3

# Advent of Code 2023
# Day 2 Puzzle 1

# Answer
# Attempts
# Final:


"""
Advent of Code 2023 Day 2 Puzzle 1

Usage:
  aoc_d1_p1 <input_file>
        [-h | --help]
        [--version]

Options:
  input_file   Puzzle Input File
  --version    Show version.
  -h --help    Show this screen.
"""

# import pprint
# import math
from docopt import docopt


import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.WARNING)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter("%(levelname)s - %(message)s")
# formatter = logging.Formatter('')
handler.setFormatter(formatter)
root.addHandler(handler)

logging.warning("Log Level: Warning")  # will print a message to the console
logging.info("Log Level: Info")


max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class cmd_arguments:
    pass


def pritty_print(stuff):
    return
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)


def docopt_handler():
    args = cmd_arguments()
    arguments = docopt(__doc__)
    args.input_file = arguments["<input_file>"]
    return args


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df, args):
    games = []
    print(f"Here 1")
    for game in df:
        game = game.split(":")
        game[0] = int(game[0].replace("Game ", ""))
        r = game[1]
        r = r.split(";")
        game[1] = r
        print(f"Game:->{game}")
        print(f"Here 2")
        rounds_list = []
        for r in game[1]:
            print(f"R:->{r}")
            picks = r.split(",")
            picks_list = []
            for pick in picks:
                pick = pick.split()
                pick[0] = int(pick[0])
                print(f"Pick:->{pick}")
                picks_list.append(pick)
            print(f"Picks List:->{picks_list}")
            rounds_list.append(picks_list)
        game[1] = rounds_list
        print(f"Game:->{game}")
        games.append(game)
    print(f"Games:->{games}")

    print(f"\n")
    print(f"{df}\n")
    print(f"\n")

    playable = [True for i in games]
    print(f"Playable: {playable}")
    for game in games:
        print(f"Game: {game}")
        game_number = game[0] - 1
        is_playable = True
        for round in game[1]:
            print(f"Round: {round}")
            for p in round:
                count = p[0]
                color = p[1]
                print(f"Game Number: {game_number}")
                print(f"Count: {count}", end=" ")
                print(f"Color: {color}")
                print(f"Max Colors: {max_colors[color]}")
                if count > max_colors[color]:
                    print(f"Not Playable")
                    is_playable = False
            print(f"Playable: {is_playable}")
        if is_playable:
            playable[game_number] = game_number + 1
        else:
            playable[game_number] = False
        is_playable = True
    print(f"Playable: {playable}")
    print(f"Total: {sum(playable)}")
    return 0


def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    args = docopt_handler()
    df = read_file(args.input_file)
    print(f"{ df }")
    process_data(df, args)


if __name__ == "__main__":
    main()
