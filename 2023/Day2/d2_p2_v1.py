#!/usr/bin/env python3

# Advent of Code 2023
# Day 2 Puzzle 1

# Answer: 76008

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

import numpy
from docopt import docopt
import logging
import sys

# Python log levels
# NOTSET=0.
# DEBUG=10.
# INFO=20.
# WARN=30.
# ERROR=40.
# CRITICAL=50.

root = logging.getLogger()
root.setLevel(logging.WARN)

handler = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter("%(levelname)s - %(message)s")
# formatter = logging.Formatter('')
handler.setFormatter(formatter)
root.addHandler(handler)

logging.warning("Log Level: Warning")  # will logging.debug a message to the console
logging.info("Log Level: Info")


class cmd_arguments:
    pass


def pritty_print(stuff):
    return
    pp = pprint.debug.PrettyPrinter(indent=4)
    pp.pprint.debug(stuff)


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
    for game in df:
        game = game.split(":")
        game[0] = int(game[0].replace("Game ", ""))
        r = game[1]
        r = r.split(";")
        game[1] = r
        logging.debug(f"Game:->{game}")
        rounds_list = []
        for r in game[1]:
            logging.debug(f"R:->{r}")
            picks = r.split(",")
            picks_list = []
            for pick in picks:
                pick = pick.split()
                pick[0] = int(pick[0])
                logging.debug(f"Pick:->{pick}")
                picks_list.append(pick)
            logging.debug(f"Picks List:->{picks_list}")
            rounds_list.append(picks_list)
        game[1] = rounds_list
        logging.debug(f"Game:->{game}")
        games.append(game)
    logging.debug(f"Games:->{games}")

    logging.debug(f"\n")
    logging.debug(f"{df}\n")
    logging.debug(f"\n")

    logging.debug(f"Starting Game\n")
    power_product = []
    for game in games:
        min_colors = {
            "red": -1,
            "green": -1,
            "blue": -1,
        }
        logging.debug(f"New Game: {game}")
        game_number = game[0] - 1
        for round in game[1]:
            logging.debug(f"Round: {round}")
            for p in round:
                count = p[0]
                color = p[1]
                logging.debug(f"Game Number: {game_number}")
                logging.debug(f"Count: {count}")
                logging.debug(f"Color: {color}")
                logging.debug(f"Min Colors: {min_colors[color]}")
                if count > min_colors[color]:
                    logging.debug(f"Updating")
                    min_colors[color] = count
                logging.debug(f"Updated Min Colors: {min_colors}")
        power_product.append(
            min_colors["red"] * min_colors["green"] * min_colors["blue"]
        )
    logging.warning(f"End Game: {sum(power_product)}")
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
    logging.debug(f"{ df }")
    process_data(df, args)


if __name__ == "__main__":
    main()
