#!/usr/bin/env python3

# Advent of Code 2023
# Day 1 Puzzle 1

# Answer
# Attempts
# Low: 55188
# Final: 55218


"""
Advent of Code 2023 Day 1 Puzzle 1

Usage:
  aoc_d1_p1 <input_file>
        [-d <distance> | --distance=<distance>]
        [-i | --interactive]
        [-i | --print-grid]
        [-h | --help]
        [--version]

Options:
  input_file   Puzzle Input File
  -i --interactive  Interactive Mode 
  -p --print-grid  Print Grid
  -d <distance> --distance=<distance>  Length of rope [default: 2]
  --version    Show version.
  -h --help    Show this screen.
"""

import pprint
import math
from docopt import docopt
import yaml
import operator

ops = {"+": operator.add, "*": operator.mul}


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

numbers_as_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# twone
# eightwo
# eighthree
# threeight

print(f"{'one' in numbers_as_words.keys()}")

number_len_max = 5
number_len_min = 3

BIG_INT = 9999999999999


print(f"Numbers as Words: {numbers_as_words}")


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
    calibration_document = df
    total = []
    for calibration in calibration_document:
        calibration = calibration.strip()
        print(f"Start Calibration: {calibration}")
        first_word_idx = BIG_INT
        last_word_idx = -1
        first_word = ""
        last_word = ""
        #print(f"Find First Word")
        for word in numbers_as_words:
            index = calibration.find(word)
            if index >= 0:
                #print(f"Word: {word}")
                #print(f"Index: {index}")
                if first_word_idx > index:
                    first_word = word
                    first_word_idx = index
                    #print(f"First Word: {first_word}")
                    #print(f"First Index: {first_word_idx}")
        #print(f"Find Last Word")
        if first_word_idx != BIG_INT:
            calibration = (
                calibration[:first_word_idx]
                + numbers_as_words[first_word]
                + calibration[first_word_idx:]
            )
        #print(f"calibration: {calibration}")
        for word in numbers_as_words:
            index = calibration.rfind(word)
            if index >= 0:
                #print(f"Word: {word}")
                #print(f"Index: {index}")
                if last_word_idx < index:
                    last_word = word
                    last_word_idx = index
                    #print(f"Last Word: {last_word}")
                    #print(f"Last Index: {last_word_idx}")
        if last_word_idx != -1:
            calibration = (
                calibration[:last_word_idx+len(last_word)]
                + numbers_as_words[last_word]
                + calibration[last_word_idx+len(last_word):]
            )
        #print(f"calibration: {calibration}")
        #twone
        #calibration = (
        #    calibration[last_word_idx+len(last_word):]
        #    + numbers_as_words[last_word]
        #    + calibration[:last_word_idx + len(last_word)]
        #)
        ## calibration = calibration + numbers_as_words[first_word]
        print(f"End Calibration: {calibration}")
        numbers = [i for i in calibration if i.isdigit()]
        print(f"Numbers: {numbers}")
        total.append(int(numbers[0] + numbers[-1]))

    # print(f"Numbers: {numbers}")
    # print(f"Adding: {total[-1]}")
    print(f"List: {len(total)}")
    print(f"List: {total}")
    print(f"Total: {sum(total)}")

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
    # print(f"{ df }")
    process_data(df, args)


if __name__ == "__main__":
    main()
