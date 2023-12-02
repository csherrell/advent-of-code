#!/usr/bin/env python3

# Advent of Code 2023
# Day 1 Puzzle 1

# Answer 
# Attempts
# Final 32398920008


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
ops = { "+": operator.add, "*": operator.mul }


import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.WARNING)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(levelname)s - %(message)s')
#formatter = logging.Formatter('')
handler.setFormatter(formatter)
root.addHandler(handler)

logging.warning('Log Level: Warning')  # will print a message to the console
logging.info('Log Level: Info')


class cmd_arguments():
    pass

def pritty_print(stuff):
    return
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)

def docopt_handler():
    args = cmd_arguments()
    arguments = docopt(__doc__)
    args.input_file = arguments['<input_file>']
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
        print(f"Calibration: {calibration}")
        numbers = [i for i in calibration if i.isdigit()]
        print(f"Numbers: {numbers}")
        total.append(int(numbers[0] + numbers[-1]))
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
    print(f"{ df }")
    process_data(df,args)

if __name__ == "__main__":
    main()
