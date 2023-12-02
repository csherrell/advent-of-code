#!/usr/bin/env python3


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

def docopt_handler():
    arguments = docopt(__doc__)
    return arguments["-i"]

def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df

def process_data(instuctions):
    latch = 1
    register = 1
    register_hold = None
    clock = 1
    print(f"Clock: { clock }")

    signal_check = 20
    signal_strength = []

    while True:
        print(f"--------------------------------------")
        print(f"Clock: { clock }")
        print(f"Register: { register }")
        print(f"Signal Strength: { register * clock}")
        if clock >= signal_check:
            signal_check += 40
            signal_strength.append(register * clock)
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
    print(f"Signal Strength: { signal_strength }, Sum: { sum(signal_strength) } ")

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
