#!/usr/bin/env python3

# Answer: BZPAJELK


"""
Advent of Code 2022 Day 1 Puzzle 1

Usage:
  aoc_d1_p1 -i <input_file>
        [-h | --help]
        [--version]

Options:
  -i input_file  Puzzle Input File
  --version  Show version.
  -h --help  Show this screen.
"""

from docopt import docopt
import math

def docopt_handler():
    arguments = docopt(__doc__)
    return arguments["-i"]

def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df

columns = 40
rows = 6
display = [[ "." for column in range(40)] for row in range(6)]

def print_display():

    global display
    global columns
    global rows

    for row in range(rows):
        for column in range(columns):
            print(display[row][column], end="")
        print()

def process_data(instuctions):
    latch = 1
    register = 1
    register_hold = None
    clock = 1
    print(f"Clock: { clock }")

    # Something like
    sprite = [-1, 0, 1]
    sprite_write = 0
    sprite_center = 1

    display_row = 0

    # Temp
    sprite_counter = 0
    pixel = 0

    while True:
        print(f"-------------------- While Loop --------------------")
        print(f"Clock: { clock }")
#        pixel = register + sprite[(clock - 1 ) % 3]
        sprite_val = sprite[(clock - 1 ) % 3]
        print(f"Sprite Val: { sprite_val }")
        print(f"Display Row: { display_row }")
        print(f"Clock % 40: { clock % 40 }")

        print(f"Register: { register }")
        print(f"Pixel: { pixel }")
        sprint_range = [ register -1, register, register + 1]
        print(f"Sprint Range: { sprint_range }")

        if pixel in sprint_range:
            display[display_row][pixel] = '#'

        if clock % 40 == 0:        
            display_row += 1
            pixel = -1

        print_display()

        if instuctions:
            instruction = instuctions.pop(0)
        else:
            break

        print(f"Line { instruction }")
        instruction = instruction.split()
        instruction[0] = instruction[0].strip()
        match instruction[0]:
            case 'noop':
                print(f"In noop");
            case 'latch':
                print(f"In latch");
                register += register_hold
                print(f"Register Updated: { register }")
            case 'addx':
                print(f"In addx");
                instruction[1] = instruction[1].strip()                   
                register_hold = int(instruction[1])
                instuctions.insert(0,"latch")
            case _:
                print(f"You Really Shouldn't Be Here!")
        clock += 1
        pixel += 1

def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    file_name = docopt_handler()
    process_data(read_file(file_name))


if __name__ == "__main__":
    main()
