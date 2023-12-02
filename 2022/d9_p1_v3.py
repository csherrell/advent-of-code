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

from pynput import keyboard
from docopt import docopt
import math
from math import fabs

from string import ascii_lowercase, ascii_uppercase
import numpy

X = 0
Y = 1

#MAX_DISTANCE = 2
MAX_DISTANCE = 3
#MAX_DISTANCE = 4
#MAX_DISTANCE = 10

# Compute Head Tail Vection 
def compute_vector(H, T):
    return (T[X] - H[X]), (T[Y] - H[Y])

# Compute Head Tail Vection 
def compute_vector_inverse(H, T):
    return (-1 * (T[X] - H[X])), (-1 * (T[Y] - H[Y]))



def print_grid(H, T, move, series):
    print("----- graphY -----")
    print(f"Move: ", move)

    print(f"Head: ", H)
    print(f"Tail: ", T)

    H = tuple(H)
    T = tuple(T)
    #H = H[1], H[0]
    #T = T[1], T[0]

#    rows = max([P[Y] for P in series])
    rows = 15
#    columns = max([P[X] for P in series])
    columns = 16
    grid = {}
    for column in range(columns, -1 * (columns+1), -1):
        for row in range(-1 * rows, rows + 1, +1):
#    for row in range(-1 * rows, rows + 1, +1):
#        for column in range(columns, -1 * (columns+1), -1):
            #print(f"{row: 3}, {column: 3}")
            if [row, column] in series: 
                grid[row, column] = "#"
                #print("# ", end="")
            else:
                #grid[x,y] = (x,y)
                grid[row, column] = "."
                #grid[x,y] = ascii_uppercase[y]
                #print(". ", end="")
#            print()
        #print()
    #print()

#    print(f"Head: ", H)
#    print(f"Tail: ", T)
#    print(grid[T])
#    print(grid[H])
#

#    x x x
#    x x x
#    x x x
#
#    (-1,  1) ( 0,  1)  (1,  1)
#    (-1,  0) ( 0,  0)  (1,  0)
#    (-1, -1) ( 0, -1)  (1, -1)
#
    
#    grid[-2,2] = "W "
#    grid[-2,-2] = "X "
#    grid[2,-2] = "Y "
#    grid[2,2] = "Z "
#    grid[0,0] = "0 "
#    grid[1, 0] = "A "
#    grid[ 1,1] = "B "
#    grid[ 0,1] = "C "
#    grid[-1,1] = "D "
#    grid[-1,0] = "E "
#    grid[-1,-1] = "F "
#    grid[0,-1] = "G "
#    grid[1,-1] = "H "
    grid[0,0] = "S"
    grid[T] = "T"
#
#    print(grid[T])
#    print(grid[H])
#
    grid[H] = "H"
#
#    print(grid[T])
#    print(grid[H])
#
#    print(grid)
#

#   print(grid)
#    for row in range(rows, -1 * rows, -1):
#        for column in range(columns, -1 * columns, -1):
#    for x in range(-1 * rows, rows + 1):
#        for y in range(-1 * columns, columns + 1):
#    for row in range(rows + 1 , -1 * rows, -1):
#        for column in range(-1 * columns, columns + 1 , +1):
#    for row in range(-1 * rows, rows + 1, +1):
#        for column in range(columns, -1 * (columns+1), -1):
    for column in range(columns, -1 * (columns+1), -1):
        for row in range(-1 * rows, rows + 1, +1):
            #print("X:", row, "Y:", column, grid[row,column])
            print(grid[row,column], end='')
        print()
    print()

#    for x in range(-1 * rows, rows):
#        for y in range(-1 * columns, columns):
#            if T == [x,y]:
#                print("T ", end='')
#        print()
#    print()


def docopt_handler():
    arguments = docopt(__doc__)
    return arguments["-i"]


def read_file(input_file):
    with open(input_file) as file:
        df = file.readlines()
    return df


def process_data(df):
    H = [0, 0]
    T = [0, 0]

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

#def print_coverage(coverage):
#    print("Coverage Area")
#    for y in coverage:
#        for x in y:
def update_coverage(offset):
    coverage = []
    #dist = int(numpy.round(MAX_DISTANCE / 2))
    # dist = MAX_DISTANCE -5
    dist = MAX_DISTANCE
    print("Dist:", dist)
    for y in range(dist * -1  + offset[Y], dist + offset[Y]+1):
        for x in range(dist * -1 + offset[X], dist + offset[X]+1):
            coverage.append([x,y])
    print(coverage)
    return coverage

def process_data(df):
    global MAX_DISTANCE
    H = [0,0]
    T = [0,0]
    MAX_STEP = 1
    print(f"MAX_DISTANCE: { MAX_DISTANCE }")
    #print(f"SPAN: { SPAN }")
    
    series = [[0,0]]
    distance = 0

    print(f"-------------------- START APP --------------------")
    MAX_DISTANCE = input("Max Distance: ")
    MAX_DISTANCE = int(MAX_DISTANCE)
    coverage = update_coverage([0,0])

    move = None
    #print_grid(H, T, None, series)
    for line in list(df):
        line = line.strip()
        if line[:7] == "# NOTE:":
            print(line)
            continue
        # Sort Circuit Evaluation elif line[0] ==  "#" or line == "" will fail.
        elif line == "" or line[0] == "#":
            continue
        direction, spaces = line.split()
        direction = direction.strip()
        spaces = int(spaces.strip())

        with keyboard.Events() as events:
            # Block for as much as possible
            direction = events.get(1e6)
            direction = str(direction.key)
            direction = direction.upper().strip("'")
            if direction == 'Q':
                exit(0)

        print(f"Direction: ->{ direction }<-    Spaces: { spaces }")
        print(f"Direction: { type(direction) }    Spaces: { spaces }")
        spaces = 1

        for i in range(spaces):
            print(f"---------- loop ----------")

            print(f"H Start: { H }    T Start: { T }")
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

            #vector = compute_vector(H, T)
            
            #print(f"H End: { H }")
            
            theta = get_angle(T, H)
            print(f"Theta: {numpy.degrees(theta)}")
            #cp = get_circle_point(2 * SPAN, theta)           # Works on angle

            #print(f"C ABS:  { cp }")
            #cp =  T[X] + cp[X] * numpy.sign(vector[X]), T[Y] + cp[Y] * numpy.sign(vector[Y])


            #t_h_distance = numpy.round(math.dist(T,H),5)
            #t_max_distance = numpy.round(math.dist(T,cp),5)
            #t_cp_distance = numpy.round(math.dist(T,cp),5)
            #print(f"H End:  { H }   T Start: { T }")
            #print(f"C Shift : { cp }")
            #print(f"SPAN: { SPAN }")
            #print(f"t_h_distance: { t_h_distance }")
            #print(f"t_cp_distance: { t_cp_distance }")
            #print(f"t_max_distance: { t_max_distance }")
            #print(f"Vector: { vector }")
            print(f"Theta:  { print_theta(numpy.degrees(theta)) }")
    
            #print("Coverage:")
            #print(coverage)

            if H not in coverage:
                print("Need to do something")
                theta = numpy.degrees(theta)
                print(f"Logic: Print Theta: {theta}")
                if theta == 0:
                    print(f"Logic: On Positive X Axis")
                    T[X] += 1
                elif theta > 0 and theta < 90:
                    print(f"Logic: In Quadrant 1")
                    T[X] += 1
                    T[Y] += 1
                elif theta ==  90:
                    print(f"Logic: On Positive Y Axis")
                    T[Y] += 1
                elif theta > 90 and theta < 180:
                    print(f"Logic: In Quadrant 2")
                    T[X] -= 1
                    T[Y] += 1
                elif theta == 180:
                    print(f"Logic: On Negative X Axis")
                    T[X] -= 1
                elif theta > -180 and theta < -90:
                    print(f"Logic: In Quadrant 3")
                    T[X] -= 1
                    T[Y] -= 1
                elif theta == -90:
                    print(f"Logic: On Negative Y Axis")
                    T[Y] -= 1
                elif theta > -90:
                    print(f"Logic: In Quadrant 4")
                    T[X] += 1
                    T[Y] -= 1
                #print("T:", T)
                coverage = update_coverage(T)
                #print("Update Coverage:")
                #print(coverage)

                if [T[X],T[Y]] not in series:
                    series.append([T[X],T[Y]])

            print_grid(H, T, direction, series)
            print(f"H End: { H }   T End: { T }")

            print(f"Distance: { math.dist(H,T) }")

        print(f"Series: { len(series) }")

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
