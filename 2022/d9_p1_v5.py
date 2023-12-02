#!/usr/bin/env python3

# Answer 2511

"""
Advent of Code 2022 Day 1 Puzzle 1

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

import getch
from docopt import docopt
import math
from math import fabs

from string import ascii_lowercase, ascii_uppercase
import numpy

X = 0
Y = 1

Hi = 0 
Ni = 1

class cmd_arguments():
    pass

# Compute Head Tail Vection 
def compute_vector(H, T):
    return (T[X] - H[X]), (T[Y] - H[Y])

# Compute Head Tail Vection 
def compute_vector_inverse(H, T):
    return (-1 * (T[X] - H[X])), (-1 * (T[Y] - H[Y]))

def print_grid(rope, series):
    print("----- graphY -----")

    rows = 40
    columns = 20
#    rows = 8
#    columns = 6
    grid = {}
    rope_loc = [ t for t in rope ]
    print(f"rope_loc: {rope_loc}")
    print(f"Grid: {rope}")
    for column in range(columns, -1 * (columns+1), -1):
        for row in range(-1 * rows, rows + 1, +1):
            if (row, column) in series: 
                grid[row, column] = "#"
            else:
                grid[row, column] = "."
    print(f"PG: rope: {rope}")
    grid[0,0] = "S"
    for link in reversed(rope):
        grid[rope[link]] = link
    grid[rope[Hi]] = "H"

    for column in range(columns, -1 * (columns+1), -1):
        for row in range(-1 * rows, rows + 1, +1):
            print(grid[row,column], end='')
        print()
    print()


def docopt_handler():
    args = cmd_arguments()
    arguments = docopt(__doc__)
    args.input_file = arguments['<input_file>']
    args.distance = int(arguments['--distance'])
    args.interactive = int(arguments['--interactive'])
    args.print_grid = int(arguments['--print-grid'])
    return args


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def print_theta(theta):
    print(f"Print Theta: {theta}")
    if theta == 0:
        print(f"On Positive X Axis")
    elif theta > 0 and theta < 90:
        print(f"In Quadrant 1")
    elif theta ==  90:
        print(f"On Positive Y Axis")
    elif theta > 90 and theta < 180:
        print(f"In Quadrant 2")
    elif theta == 180:
        print(f"On Negative X Axis")
    elif theta > -180 and theta < -90:
        print(f"In Quadrant 3")
    elif theta == -90:
        print(f"On Negative Y Axis")
    elif theta > -90:
        print(f"In Quadrant 4")
    

def get_angle(H, T):
    print(f"{T}, {H}")
    x_diff = T[X] - H[X]
    y_diff = T[Y] - H[Y]
    print(f"Diff: {x_diff}, {y_diff}")
    print(f"Theta: {numpy.degrees(numpy.arctan2(y_diff, x_diff))}")
    return numpy.arctan2(y_diff, x_diff)

def get_circle_point(r, theta):
    print(f"R: {r}")
    print(f"Theta: {theta}")
    print(f"Theta: {theta}")
    x = r * numpy.cos(theta)
    y = r * numpy.sin(theta)
    print(f" {numpy.floor(x),numpy.floor(y)}")
    return [numpy.round(x,5),numpy.round(y,5)]

def slide(rope, distance):
    print(f"S1: distance: {distance}")
    print(f"S1: rope: {rope}")
    #head = rope[Hi]
    #neck = rope[Ni]
    #print(f"S1: head: {head}")
    #if rope[1] != neck:
    r = list(range(distance -1, 0, -1))
    print(f"S1 Range: { r }")

    for link in range(distance -1, 1, -1):
        print(f"S1: link: {link}")
        rope[link] = rope[link - 1]
    print(f"S1: rope: {rope}")
    return rope

def update_coverage(offset,dist):
    coverage = []
    dist = dist - 1
    for y in range(dist * -1  + offset[Y], dist + offset[Y]+1):
        for x in range(dist * -1 + offset[X], dist + offset[X]+1):
            coverage.append((x,y))
    return coverage

def touching(H,N):
    coverage = []
    dist = 1
    for y in range(dist * -1  + N[Y], dist + N[Y]+1):
        for x in range(dist * -1 + N[X], dist + N[X]+1):
            coverage.append((x,y))

    print(f"H: {H}")
    print(f"N: {N}")
    print(f"coverage: {coverage}")
    

    if tuple(H) in coverage:
        return True
    else:
        return False

def optimize_route(H, direction):
    pass

def update_locations(rope,distance):
    r = list(range(Hi, distance))
    print(f'UL Range: {r}')
    print(f'UL Hi: {Hi}')
    print(f'UL Distance: {distance}')
    print(f'UL Rope Start: {rope}')
    for r in range(Hi, distance-1):
        link_h = r
        link_n = r + 1
        print(f'UL Rope Hi i: {link_h}')
        print(f'UL Rope Ni i: {link_n}')
        print(f'UL Rope Hi: {rope[link_h]}')
        print(f'UL Rope Ni: {rope[link_n]}')
        if not touching(rope[link_h],rope[link_n]):
            print("Need to do something")
            N = [rope[link_n][0],rope[link_n][1]]
            theta = get_angle(rope[link_n], rope[link_h])
            theta = numpy.degrees(theta)
            print(f"Logic: Print Theta: {theta}")
            if theta == 0:
                print(f"Logic: On Positive X Axis")
                N[X] += 1
            elif theta > 0 and theta < 90:
                print(f"Logic: In Quadrant 1")
                N[X] += 1
                N[Y] += 1
            elif theta ==  90:
                print(f"Logic: On Positive Y Axis")
                N[Y] += 1
            elif theta > 90 and theta < 180:
                print(f"Logic: In Quadrant 2")
                N[X] -= 1
                N[Y] += 1
            elif theta == 180:
                print(f"Logic: On Negative X Axis")
                N[X] -= 1
            elif theta > -180 and theta < -90:
                print(f"Logic: In Quadrant 3")
                N[X] -= 1
                N[Y] -= 1
            elif theta == -90:
                print(f"Logic: On Negative Y Axis")
                N[Y] -= 1
            elif theta > -90:
                print(f"Logic: In Quadrant 4")
                N[X] += 1
                N[Y] -= 1
            rope[link_n] = tuple(N)
        else:
            print(f'Are Touching')
            break
    print(f'UL Rope End: {rope}')
    return rope

def process_data(df,args):
    MAX_STEP = 1
    max_distance = args.distance
    print(f"max_distance: { max_distance }")
    
    H = [0,0]
    N = [0,0]
    series = [(0,0)]
    rope = {}
    for link in range(0,max_distance):
        rope[link] = (0,0)
    print(f"Rope: { rope }")
        

    print(f"-------------------- START APP --------------------")

    # slide
    if print_grid:
        print_grid(rope, series)

    for line in list(df):
        line = line.strip()
        if line[:7] == "# NOTE:":
            print(line)
            continue
        # Sort Circuit Evaluation elif line[0] ==  "#" or line == "" will fail.
        elif line == "" or line[0] == "#":
            continue
        direction, spaces = line.split()

        if args.interactive:
            direction = getch.getch().strip().upper()
            if direction == 'Q':
                exit(0)
            spaces = '1'
            print(f"MyDirection: ->{direction}<-")
            match direction:
                case "L":
                    print(f"Move Right")
                    direction = 'R'
                case "H":
                    print(f"Move Left")
                    direction = 'L'
                case "K":
                    print(f"Move Up")
                    direction = 'U'
                case "J":
                    print(f"Move Down")
                    direction = 'D'

        direction = direction.strip()
        spaces = int(spaces.strip())

        for i in range(spaces):
            print(f"---------- loop ----------")

            #print(f"H Start: { H }    N Start: { N }")
            print(f"Direction: { direction }    Spaces: { spaces }")
            match direction:
                case "R":
                    print(f"Move Right")
                    H[X] += 1
                case "L":
                    print(f"Move Left")
                    H[X] -= 1
                case "U":
                    print(f"Move Up")
                    H[Y] += 1
                case "D":
                    print(f"Move Down")
                    H[Y] -= 1
                case _:
                    print(f"You Should Not Be Here")
            rope[Hi] = tuple(H)
            rope = update_locations(rope,max_distance)
            print(f"Main Rope: {rope}")

            print(f"new_head: { rope[Hi] }")
            print(f"new_neck: { rope[Ni] }")
            print(f"Rope: { rope }")
            print(f"max_distance: { max_distance }")

            #rope = slide(rope, max_distance)

#            if rope[max_distance -1] not in series:
#                series.append(rope[max_distance -1])
            print(f"Rope: { rope }")

            if args.print_grid:
                print_grid(rope, series)

        print(f"Series: { len(series) }")
    print_grid(rope, series)

def main():
    """Main Function
    - Handle docopt parameters
    - Read input File
    - Compute Result
    - Print Output
    """
    args = docopt_handler()
    df = read_file(args.input_file)
    process_data(df,args)


if __name__ == "__main__":
    main()
