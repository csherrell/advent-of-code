#!/usr/bin/env python3


"""
Advent of Code 2022 Day 1 Puzzle 1

Usage:
  aoc_d1_p1 -i <input_file>
        [--cm=<crate_mover_model>]
        [-h | --help]
        [--version]

Options:
  -i input_file  Puzzle Input File
  --cm=crate_mover_model  Crate Mover Model [default: 9000]
  --version  Show version.
  -h --help  Show this screen.
"""

from docopt import docopt


def docopt_handler():
    arguments = docopt(__doc__)
#    print(f'{ arguments }')
    return arguments["-i"], int(arguments["--cm"])


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df, cm):

    # Setup Stacks
    line = df[0]
    stacks = []
    for i in range(1, len(line), 4):
        stacks.append([])
#    print(stacks)
#    print(df)

    # Load Stacks
    for line in list(df):
#        print(f"Line: { line }")
        df.pop(0)
        if line[1] == "1":
            break
        stack_counter = 0
        for i in range(1, len(line), 4):
            item = line[i].strip()
            if item:
                stacks[stack_counter].append(item)
            stack_counter += 1
#        print(stacks)
#    print(df)
    df.pop(0)

    # Generate Moves
    moves = []
    for line in df:
        line = line.replace("move ","")
        line = line.replace(" from ",",")
        line = line.replace(" to ",",")
        move = line.split(",")
        move[0] = int(move[0])
        move[1] = int(move[1]) - 1
        move[2] = int(move[2]) - 1
        moves.append(move)
#        print(f"Line: { line }")
#    print(f"Moves: { moves }")

    # Do Moves
    for move in moves:
        quantity, move_from, move_to = move
#        print(quantity, move_from, move_to)
        stack_slice = stacks[move_from][:quantity]
        if cm == 9000:
            stack_slice.reverse()
#        print("Start:", stacks)
#        print(stack_slice)
        del(stacks[move_from][:quantity]) 
        #stacks[move_to].extend(stack_slice)
        #a[len(a):] = iterable
        stacks[move_to] = stack_slice + stacks[move_to]
#        print("End:  ", stacks)
            
    for crate in stacks:
        print(crate[0],end="")
    print()
    exit(0)
    return

def print_results(elven_bread):
    print(f"Summary ----------------------")
    print(f"Total: { sum(elven_bread) }")
    print(f"Max: { max(elven_bread) }")

    elven_bread.sort(reverse=True)
    print(f"Top Three: { sum(elven_bread[:3]) }")

    while len(elven_bread) > 3:
        elven_bread.remove(min(elven_bread))
    print(f"Top Three: { sum(elven_bread) }")


def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    file_name, cm = docopt_handler()
    process_data(read_file(file_name),cm)
    # print_results(process_data(read_file(docopt_handler())))


if __name__ == "__main__":
    main()
