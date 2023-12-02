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

from __future__ import print_function
import json
import json
from docopt import docopt

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k

def find_values(id, json_repr):
    results = []
    print("Find Values")

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results

def find_values_with_name(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict)
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results

def docopt_handler():
    arguments = docopt(__doc__)
    return arguments["-i"]


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df):
    root = {"/":{'NAME': "/", 'TOTALSIZE': 0, 'RECURSIVE': 0}}
    parent = []
    parent.append(root["/"])
    
    child = None

    depth = 0
    for line in list(df):
        line = line.strip()
        if line == "":
            continue
        match line[:4]:
            case "$ cd":
                directory = line[4:].strip()
                if line[4:].strip() == "/":
                    parent = []
                    parent.append(root["/"])
                    child = None
                elif line[4:].strip() == "..":
                    if len(parent) > 1:
                        child = parent.pop()
                else:
                    parent.append(parent[-1][directory])
            case "$ ls":
                pass
            case "dir ":
                directory = line[4:].strip()
                if directory not in parent[-1]:
                    parent[-1][directory] = {'NAME': directory, 'TOTALSIZE': 0, 'RECURSIVE': 0}
            case _:
                size, filename = line.split(" ")
                filename = filename.strip()
                size = int(size)
                if filename not in parent[-1]:
                    parent[-1][filename] = size
                    parent[-1]['TOTALSIZE'] += size
                    for i in parent:
                        i['RECURSIVE'] += size

#################

    total = 0
    for i in find_values('RECURSIVE', json.dumps(root)):
        if i <= 100000:
            total += i
    print("P1 Total:", total)

#################

    max_space = 70000000
    free_space = max_space - root["/"]['RECURSIVE']
    print("Free Space:", free_space)
    needed_space = 30000000 - free_space
    print("Required:", needed_space )
    directory = max_space
    directory_name = None
    kvp = find_values_with_name('RECURSIVE', json.dumps(root))
    kvp.pop()
    for i in kvp:
        if  i["RECURSIVE"] > needed_space and i["RECURSIVE"] < directory:
            directory_name = i["NAME"]
            directory = i["RECURSIVE"]
    print(directory_name)
    print(directory)
    

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
