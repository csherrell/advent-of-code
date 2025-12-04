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
    return data_file


def d1_td(data_file, cmdargs):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :param cmdargs: dict - command line arguments
    :return: string - "All Done"
    """
    print(f"{cmdargs}")
    for line in list(data_file):
        line = line.strip()
        print(f"{line}")
    return "All Done"


def d4p1(data_file, cmdargs):
    """
    Process a list of lines from a file
    Loop over the lines and strip the white space from beginning and end of string
    :param data_file: list - List of lines from the input file
    :param cmdargs: dict - command line arguments
    :return: string - "All Done"
    """
    print(f"{cmdargs}")
    length = len(data_file)
    width = len(data_file[0].strip())
    print(f"{length},{width}")
    print(f"{data_file}")
    print(f"{data_file[0]}")
    matrix = [[0 for _ in range(length+2)] for _ in range(width+2)]
    print(f"{matrix=}")

    row = 1
    # Create Matrix
    for line in list(data_file):
        line = list(line.strip())
        print(f"{row=}")
        new_list = [0 if item == "." else 1 for item in line]
        matrix[row][1:-1] = new_list
        row += 1

    print(f"{matrix=}")
    for row in matrix:
        for col in row:
            print(f"{col} ",end="")
        print(f"")
    print(f"")

    solution = 0
    for row in range(1, len(matrix) - 1):
        rolls = 0
        for col in range(1, len(matrix[row]) - 1):
                print(f"{matrix[row - 1][col - 1]} ",end="")
                print(f"{matrix[row - 1][col    ]} ",end="")
                print(f"{matrix[row - 1][col + 1]}")

                print(f"{matrix[row    ][col - 1]} ",end="")
                print(f"X ",end="")
                print(f"{matrix[row    ][col + 1]} ")

                print(f"{matrix[row + 1][col - 1]} ",end="")
                print(f"{matrix[row + 1][col    ]} ",end="")
                print(f"{matrix[row + 1][col + 1]}")
                
                if matrix[row][col]:
                    rolls = (
                           matrix[row - 1][col - 1]
                         + matrix[row - 1][col    ]
                         + matrix[row - 1][col + 1]
                         + matrix[row    ][col - 1]
                         + matrix[row    ][col + 1]
                         + matrix[row + 1][col - 1]
                         + matrix[row + 1][col    ]
                         + matrix[row + 1][col + 1]
                    )
                    print(f"{rolls=}\n")
                    if rolls < 4:
                        solution += 1
        #
        #            -- -0 -+  row-1,col-1   row-1,col  row-1,col+1
        #            0- 00 0+  row,  col-1           row,  col+1
        #            +- +0 ++  row+1,col-1   row+1,col  row+1,col+1
        print(f"")
    # print(f"{}")

    print(f"The solution is: {solution}")

    return "All Done"


def d4p2(data_file, cmdargs):
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
        print(f"{line=}")

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
    print(f"{d4p1(data_file,arguments)}")


if __name__ == "__main__":
    main()
