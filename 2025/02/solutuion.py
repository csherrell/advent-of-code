#!/usr/bin/env python
"""
solution.py

Usage:
  solution.py <input_file>
    [-v | --version]
    [-h | --help]

Options:
  input_file    Input File
  -v --version  Show this version
  -h --help     Show this screen

Examples:
  ./solution.py ../test_data/test.txt

Notes:
  PyLint and Black Compliant
  Print the doc strings. Module name without ".py"
  pydoc solution

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
from enum import Enum


# Third-party imports ---------------------------------------------------------

# User Defined imports ---------------------------------------------------------------


# -----------------------------------------------------------------------------
# GLOBALS
# -----------------------------------------------------------------------------
DIAL_START = 50
UNITS = 100
#DIAL_START = 2
#UNITS = 4
DIRECTION = {"L": -1, "R": 1}

# -----------------------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------------------
__all__ = ["docopt_handler", "local_process"]
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
    print(f"Processing: {input_file}")
    with open(input_file, encoding="UTF-8") as file:
        data_file = file.readlines()
#        data_file = data_file.split(",")
    print(f"{data_file=}")
    return data_file


def d1td(data_file, cmdargs):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :param cmdargs: dict - command line arguments
    :return: string - "All Done"
    """
    print(f"{cmdargs}")
    solution = 0
    for line in list(data_file):
        line = line.strip()
        print(f"{line}")
        start, end = line.split("-")
        for i in range(int(start), int(end)+1):
            i_as_string = str(i)
            i_len = len(i_as_string) // 2
            #print(f"{i_as_string[:i_len]}, {i_as_string[i_len:]}")
            if i >= 11:
                if i_as_string[:i_len] == i_as_string[i_len:]:
                    solution += i
                    print(f"{i=}")
    print(f"{solution=}")
    return "All Done"


def d1p2(data_file, cmdargs):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :param cmdargs: dict - command line arguments
    :return: string - "All Done"
    """
    duplicates = []
    for line in list(data_file):
        line = line.strip()
        print(f"{line}")
        start, end = line.split("-")
        for number in range(int(start), int(end)+1):
            print(f"{number=}")
            splitlist = []
            word = str(number)
            for i in range(len(word)):
                for j in range(i+1,len(word)+1):
                    splitlist.append(word[i:j])
            if len(splitlist) != len(set(splitlist)):
                duplicates.append(number)
            print(f"{duplicates=}")
        
#    print(f"The solution is: {SOLUTION}")

    return "All Done"

def d1p1(data_file, cmdargs):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :param cmdargs: dict - command line arguments
    :return: string - "All Done"
    """

    print(f"The solution is: {solution}")
    
    return "All Done"


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
    print(f"{d1p2(data_file,arguments)}")


if __name__ == "__main__":
    main()
