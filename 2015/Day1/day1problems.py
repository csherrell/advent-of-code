#!/usr/bin/env python
"""
day1problems.py

Usage:
  day1problems.py <input_file>
    [-p problem | --problem problem ]
    [-v | --version]
    [-h | --help]

Options:
  input_file    Input File
  -p problem --problem PROBLEM  Select the problem
  -v --version  Show this version
  -h --help     Show this screen

Examples:
  ./day1problems.py ../test_data/test.txt

Notes:
  Avdent of Code: 2015 Day 1
  PyLint and Black Compliant
  Print the doc strings. Module name without ".py"
  pydoc day1problems

References:
  http://docopt.org/
  https://pypi.org/project/docopt/
  https://realpython.com/python-constants/

"""


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# stdlib imports --------------------------------------------------------------
from docopt import docopt

# Third-party imports ---------------------------------------------------------

# User Defined imports ---------------------------------------------------------------


# -----------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------
BASEMENT = -1

# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------
__all__ = ["main", "docopt_handler", "read_file", "day1problem1", "day1problem2"]
__author__ = "Chad S. Sherrell"
__version__ = "0.0.1"


# -----------------------------------------------------------------------------
# LOCAL UTILITIES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# CLASSES
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------


def docopt_handler():
    """
    Process the docopt docstring arguments
    :param: None
    :return: docopt arguments dictionary
    """
    arguments = docopt(__doc__, version=__version__)
    return arguments


def read_file(input_file):
    """
    Read an input file
    :param: input_file Name
    :return: List of lines in the file
    """
    with open(input_file, encoding="UTF-8") as file:
        data_file = file.readlines()
    return data_file


def day1problem1(data_file):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :return: string - "All Done"
    """
    for line in list(data_file):
        line = line.strip()
        floor = 0
        for character in line:
            if character == "(":
                floor += 1
            elif character == ")":
                floor -= 1
        print(f"2015 Day 1 Problem 1 Solution: {floor}")


def day1problem2(data_file):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :return: string - "All Done"
    """
    for line in list(data_file):
        line = line.strip()
        floor = 0
        character_counter = 1
        for character in line:
            if character == "(":
                floor += 1
            elif character == ")":
                floor -= 1
            if floor == BASEMENT:
                print(f"2015 Day 1 Problem 2 Solution: {character_counter}")
                break
            character_counter += 1


# -----------------------------------------------------------------------------
# RUNTIME PROCEDURE
# -----------------------------------------------------------------------------
def main():
    """
    Main Function
    : Process the docopt doc string
    : Read the input_file
    : Process the data
    """
    # description of the operations to be performed
    arguments = docopt_handler()
    data_file = read_file(arguments["<input_file>"])
    if arguments.problem == "1":
        day1problem1(data_file)
    elif arguments.problem == "2":
        day1problem2(data_file)
    else:
        day1problem1(data_file)
        day1problem2(data_file)


if __name__ == "__main__":
    main()
