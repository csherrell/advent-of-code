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


def process_data(df):
    for line in list(df):
        line = line.strip()
        print(line)
        buffer = [*line]
        sync_bytes = []
        sync_bytes.append(buffer.pop(0))
        sync_char_counter = 2
        for i in list(buffer):
            print("sync_bytes",sync_bytes)
            print("test",i)
            if i not in sync_bytes:
                print(i, "not in")
                if len(sync_bytes) == 13:
                    break
            else:
                print(i, "in")
                location = sync_bytes.index(i)
                sync_bytes = sync_bytes[location+1:]
                    
            sync_bytes.append(i)
            if len(sync_bytes) > 13:
                sync_bytes.pop(0)
            print("sync_char_counter:", sync_char_counter)
            print("len:", len(sync_bytes))
            #sync_bytes.append(buffer.pop(0))
            #sync_bytes.pop(0)
            print()
            #print("sync_bytes",sync_bytes," ", end="")
            sync_char_counter += 1
        print("Final: sync_char_counter:", sync_char_counter)
            
#                print('loc', location)
#                ####location = sync_bytes.index(i)
#                # [i,x in enumerate([1,2,3,2]) if x==2]
#                idx = [j for j,x in enumerate(sync_bytes) if x==i] # => [1, 3]
#                print('idx', idx[-1])



def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    process_data(read_file(docopt_handler()))


if __name__ == "__main__":
    main()
