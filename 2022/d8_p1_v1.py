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
import numpy as np

def print_grid(grid,rows,columns,transpose=False):
    return
    if transpose:
        grid = np.array(grid).T.tolist()
    for row_i in range(rows):
        for column_i in range(columns):
            print(grid[row_i][column_i], " ", end="")
        print()
    print()

def docopt_handler():
    arguments = docopt(__doc__)
    return arguments["-i"]


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df):
    grid = []
    for line in list(df):
        line = line.strip()
        print(line)
        d = [int(i) for i in [*line]]
        grid.append(d)

    rows = len(grid)
    columns = len(grid[0])
    perimeter = (2 * columns) + (2 * (rows - 2))
    print("Perimeter:", perimeter)

    print("------------------------------------")

    print()
    print(grid)
    print()

    print("------------------------------------")

    for row_i in range(1, rows - 1):
        for column_i in range(1, columns - 1):
            print("Coordinated:", row_i, column_i, grid[row_i][column_i])
            if (
                grid[row_i][column_i] >= grid[row_i + 1][column_i]
                and grid[row_i][column_i] >= grid[row_i - 1][column_i]
                and grid[row_i][column_i] >= grid[row_i][column_i + 1]
                and grid[row_i][column_i] >= grid[row_i][column_i - 1]
            ):
                print("Found Tree")
        print()

    print("------------------------------------")


    print("------------------------------------")

    visable_grid = [[0 for i in range(columns)] for j in range(rows)]

    for row_i in range(rows):
        for column_i in range(columns):
            print(visable_grid[row_i][column_i], " ", end="")
        print()
    print()

    print("Puzzle 1 Solution ------------------")

    for row_i in range(1, rows - 1):
        for column_i in range(1, columns - 1):
            print(
                "Coordinated:",
                row_i,
                column_i,
                grid[row_i][column_i],
                grid[row_i][column_i + 1 :],
                grid[row_i][:column_i],
            )
            if grid[row_i][column_i] > max(grid[row_i][column_i + 1 :]):
                print("Found Tree", row_i, column_i, grid[row_i][column_i], "right")
                visable_grid[row_i][column_i] = 1
            if grid[row_i][column_i] > max(grid[row_i][:column_i]):
                print("Found Tree", row_i, column_i, grid[row_i][column_i], "left")
                visable_grid[row_i][column_i] = 1

    grid = np.array(grid).T.tolist()
    visable_grid = np.array(visable_grid).T.tolist()
    rows, columns = columns, rows

    for row_i in range(1, rows - 1):
        for column_i in range(1, columns - 1):
            print(
                "Coordinated:",
                row_i,
                column_i,
                grid[row_i][column_i],
                grid[row_i][column_i + 1 :],
                grid[row_i][:column_i],
            )
            if grid[row_i][column_i] > max(grid[row_i][column_i + 1 :]):
                print("Found Tree", row_i, column_i, grid[row_i][column_i], "right")
                visable_grid[row_i][column_i] = 1
            if grid[row_i][column_i] > max(grid[row_i][:column_i]):
                print("Found Tree", row_i, column_i, grid[row_i][column_i], "left")
                visable_grid[row_i][column_i] = 1

    seable = perimeter
    for row_i in visable_grid:
        seable += sum(row_i)
    print(seable)

    print("Puzzle 2 Solution ------------------")

    visable_grid = [
        [{"right": 0, "left": 0, "up": 0, "down": 0} for i in range(columns)]
        for j in range(rows)
    ]

    for row_i in range(rows):
        for column_i in range(columns):
            print(visable_grid[row_i][column_i], " ", end="")
        print()
    print()

    for row_i in range(1, rows - 1):
        for column_i in range(1, columns - 1):
            print("-----------")
            print(
                "Coordinated:",
                row_i,
                column_i,
                grid[row_i][column_i],
                grid[row_i][column_i + 1 :],
                grid[row_i][:column_i],
            )
            print("View Right", grid[row_i][column_i], grid[row_i][column_i + 1 :])
            for i in grid[row_i][column_i + 1 :]:
                if grid[row_i][column_i] > i:
                    print(">", row_i, column_i, grid[row_i][column_i], "right")
                    visable_grid[row_i][column_i]["right"] += 1
                elif grid[row_i][column_i] == i:
                    print("=", row_i, column_i, grid[row_i][column_i], "right")
                    visable_grid[row_i][column_i]["right"] += 1
                    break
                else:
                    print("<", row_i, column_i, grid[row_i][column_i], "right")
                    visable_grid[row_i][column_i]["right"] += 1
                    break
            if visable_grid[row_i][column_i]["right"] == 0:
                visable_grid[row_i][column_i]["right"] = 1

            print("Trees Right:", visable_grid[row_i][column_i]["right"])
            print_grid(grid, rows, columns)
            print_grid(visable_grid,rows, columns)


            print("-----------")

            print("View Left", grid[row_i][column_i], grid[row_i][:column_i])
            view = grid[row_i][:column_i]
            view.reverse()
            for i in view:
                if grid[row_i][column_i] > i:
                    print(">", row_i, column_i, grid[row_i][column_i], "left")
                    visable_grid[row_i][column_i]["left"] += 1
                elif grid[row_i][column_i] == i:
                    print("=", row_i, column_i, grid[row_i][column_i], "left")
                    visable_grid[row_i][column_i]["left"] += 1
                    break
                else:
                    print("=", row_i, column_i, grid[row_i][column_i], "left")
                    visable_grid[row_i][column_i]["left"] += 1
                    break
            if visable_grid[row_i][column_i]["left"] == 0:
                visable_grid[row_i][column_i]["left"] = 1

            print("Trees Left:", visable_grid[row_i][column_i]["left"])
            print_grid(grid, rows, columns)
            print_grid(visable_grid,rows, columns)


    print("-----------")
    grid = np.array(grid).T.tolist()
    visable_grid = np.array(visable_grid).T.tolist()
    rows, columns = columns, rows

    for row_i in range(1, rows - 1):
        for column_i in range(1, columns - 1):
            print(
                "Coordinated:",
                row_i,
                column_i,
                grid[row_i][column_i],
                grid[row_i][column_i + 1 :],
                grid[row_i][:column_i],
            )
            print("View Right", grid[row_i][column_i], grid[row_i][column_i + 1 :])
            for i in grid[row_i][column_i + 1 :]:
                if grid[row_i][column_i] > i:
                    print(">", row_i, column_i, grid[row_i][column_i], "right")
                    visable_grid[row_i][column_i]["up"] += 1
                elif grid[row_i][column_i] == i:
                    print("=", row_i, column_i, grid[row_i][column_i], "right")
                    visable_grid[row_i][column_i]["up"] += 1
                    break
                else:
                    print("<", row_i, column_i, grid[row_i][column_i], "right")
                    visable_grid[row_i][column_i]["up"] += 1
                    break
            if visable_grid[row_i][column_i]["up"] == 0:
                visable_grid[row_i][column_i]["up"] = 1

            print("Trees Up:", visable_grid[row_i][column_i]["up"])
            print_grid(grid, rows, columns)
            print_grid(visable_grid,rows, columns)

            print("-----------")

            print("View Left", grid[row_i][column_i], grid[row_i][:column_i])
            view = grid[row_i][:column_i]
            view.reverse()
            for i in view:
                if grid[row_i][column_i] > i:
                    print(">", row_i, column_i, grid[row_i][column_i], "left")
                    visable_grid[row_i][column_i]["down"] += 1
                elif grid[row_i][column_i] == i:
                    print("=", row_i, column_i, grid[row_i][column_i], "left")
                    visable_grid[row_i][column_i]["down"] += 1
                    break
                else:
                    print("<", row_i, column_i, grid[row_i][column_i], "left")
                    visable_grid[row_i][column_i]["down"] += 1
                    break
            if visable_grid[row_i][column_i]["down"] == 0:
                visable_grid[row_i][column_i]["down"] = 1
            print("View down:", visable_grid[row_i][column_i]["down"])
            print_grid(grid, rows, columns)
            print_grid(visable_grid,rows, columns)
            print("-----------")

    trees_in_view = [[0 for i in range(columns)] for j in range(rows)]

    for row_i in range(rows):
        for column_i in range(columns):
            trees_in_view[row_i][column_i] = (
                visable_grid[row_i][column_i]["left"]
                * visable_grid[row_i][column_i]["right"]
                * visable_grid[row_i][column_i]["up"]
                * visable_grid[row_i][column_i]["down"]
            )


#    grid = np.array(grid).T.tolist()
    for row_i in range(rows):
        for column_i in range(columns):
            print(grid[row_i][column_i], " ", end="")
        print()
    print()

#    trees_in_view = np.array(trees_in_view).T.tolist()
    for row_i in range(rows):
        for column_i in range(columns):
            print(trees_in_view[row_i][column_i], " ", end="")
        print()
    print()

#    visable_grid = np.array(visable_grid).T.tolist()
    print_grid(grid,rows, columns)
    print_grid(visable_grid,rows, columns)

    max_value = 0
    for row_i in range(rows):
        for column_i in range(columns):
            if trees_in_view[row_i][column_i] > max_value:
               max_value = trees_in_view[row_i][column_i]
    print("MAX:", max_value)
    print("------------------------------------")


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
