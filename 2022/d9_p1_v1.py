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
import math
from math import fabs

import numpy

X = 0
Y = 1

# Compute Head Tail Vection 
def compute_vector(H, T):
    return (T[X] - H[X]), (T[Y] - H[Y])

# Compute Head Tail Vection 
def compute_vector_inverse(H, T):
    return (-1 * (T[X] - H[X])), (-1 * (T[Y] - H[Y]))

def print_grid(grid, rows, columns, transpose=False):
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
        #return numpy.degrees(numpy.arctan2(y_diff, x_diff))
        return numpy.arctan2(y_diff, x_diff)

def get_circle_point(r, theta):
    print(f"R: {r}")
    print(f"Theta: {theta}")
    #theta = numpy.radians(theta)
    print(f"Theta: {theta}")
    x = r * numpy.cos(theta)
    y = r * numpy.sin(theta)
    print(f" {numpy.floor(x),numpy.floor(y)}")
    return [numpy.round(x,5),numpy.round(y,5)]

def process_data(df):
    H = [0,0]
    T = [0,0]
# Answer: 13
# Answer: 6332
    MAX_DISTANCE = 2
#    MAX_DISTANCE = 10
#    MAX_DISTANCE = 3
#    MAX_DISTANCE = 4

    SPAN = MAX_DISTANCE - 1
#    SPAN = MAX_DISTANCE - 1 if MAX_DISTANCE - 1 > 1 else MAX_DISTANCE
#    SPAN = MAX_DISTANCE
    MAX_STEP = 1
#    RADIUS =  MAX_DISTANCE / 2
    ####  MAX SPAN *** 
#    MAX_DISTANCE = 1
#    MAX_DISTANCE = 3 - 1
#    MAX_DISTANCE = 5.75 
#    RADIUS =  numpy.linalg.norm(point1 - point2)ist([0,0],[MAX_DISTANCE,MAX_DISTANCE])
# 𝑥=𝑟∗𝑠𝑖𝑛(θ),𝑦=𝑟∗𝑐𝑜𝑠(θ)
    #r 2 pi R
    print(f"MAX_DISTANCE: { MAX_DISTANCE }")
    print(f"SPAN: { SPAN }")
#    print(f"Radius: { RADIUS }")
#    CIRCLE_RADIUS = get_circle_point(SPAN, numpy.radians(45))         # Works on Axis

#    CIRCLE_RADIUS = get_circle_point(2 * MAX_DISTANCE, numpy.radians(45))         # Works on Axis
    CIRCLE_RADIUS = get_circle_point(2 * SPAN, numpy.radians(45))         # Works on Axis
    print(f"CIRCLE_RADIUS: { CIRCLE_RADIUS }")
    CIRCLE_RADIUS = numpy.round(numpy.sqrt(SPAN  ** 2 + SPAN ** 2),5)
#            t_h_distance = numpy.round(math.dist(T,H),10)
#    CIRCLE_RADIUS = math.sqrt(MAX_DISTANCE  ** 2 + MAX_DISTANCE ** 2)

    print(f"CIRCLE_RADIUS: { CIRCLE_RADIUS }")
    
    d = 1
#    for c in [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1, -1], [0, -1], [1, -1]]:
    for c in [[d,0], [d,d], [0,d], [-d,d], [-d,0], [-d, -d], [0, -d], [d, -d]]:
        print(f"C: {c}")
        theta = get_angle([0,0],c)
        print(f"Theta:  { theta }")
        print(f"Theta:  { print_theta(numpy.degrees(theta)) }")
        print(f"Distance: {numpy.linalg.norm([0,0],c)}")
        print(f"Circle Point: { get_circle_point(2*d, theta)}")
        print()
# 3226
# 2552 Too Hight
# 3468
# 2884
# 2305 NO
# 2450 NO
# 2249 Too Low
# 2275
# 2220
# 2164
# 1810
# 2144

    series = [[0,0]]
    distance = 0

    print(f"-------------------- START APP --------------------")

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


        print(f"H Start: { H }    T Start: { T }")
        print(f"Direction: { direction }    Spaces: { spaces }")

        for i in range(spaces):
            print(f"---------- loop ----------")
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

            vector = compute_vector(H, T)
            # vector = compute_vector_inverse(H,T)
            
            print(f"H End: { H }")
            
            theta = get_angle(T, H)
            print(f"Theta: {numpy.degrees(theta)}")
            cp = get_circle_point(2 * SPAN, theta)           # Works on angle
#            cp = get_circle_point(SPAN/2, theta)         # Works on Axis
#            cp = get_circle_point(MAX_DISTANCE,theta)    # Works on angle 
#            cp = get_circle_point(MAX_DISTANCE/2,theta)  # Works on Axis

#            if numpy.degrees(theta).is_integer():
#                print("Theta IS int")
#                cp = get_circle_point(SPAN/2, theta)         # Works on Axis
#            else:
#                print("Theta NOT int")
#                cp = get_circle_point(SPAN, theta)           # Works on angle
#            cp = get_circle_point(SPAN, theta)           # Works on angle

            print(f"C ABS:  { cp }")
#            cp = cp[X] + T[X], cp[Y] + T[Y]
            cp =  T[X] + cp[X] * numpy.sign(vector[X]), T[Y] + cp[Y] * numpy.sign(vector[Y])


#                T[X] += -1 * (MAX_DISTANCE - MAX_STEP) * numpy.sign(vector[X]) 
#                T[Y] += -1 * (MAX_DISTANCE - MAX_STEP) * numpy.sign(vector[Y])

            #distance = math.dist(H,T) - math.dist(H,T)
            t_h_distance = numpy.round(math.dist(T,H),5)
            t_max_distance = numpy.round(math.dist(T,cp),5)
            t_cp_distance = numpy.round(math.dist(T,cp),5)
            print(f"H End:  { H }   T Start: { T }")
            print(f"C Shift : { cp }")
            print(f"SPAN: { SPAN }")
            print(f"t_h_distance: { t_h_distance }")
            print(f"t_cp_distance: { t_cp_distance }")
            print(f"t_max_distance: { t_max_distance }")
            print(f"Vector: { vector }")
            print(f"CIRCLE_RADIUS: { CIRCLE_RADIUS }")
            #distance =  numpy.dist(H,T)
            
#            if numpy.dist(H,T) > MAX_DISTANCE:
#            if numpy.dist(H,T) >= RADIUS:
#            if cp[X] <= H[X] or cp[Y] <= H[Y]:
#            if ht_distance >= t_max_distance:
#            if H[X] <= cp[X] and H[Y] <= cp[Y]:
            print(f"Theta:  { print_theta(numpy.degrees(theta)) }")

#            if ht_distance > t_max_distance:
#            if H[X] - cp[X] > SPAN or H[Y] - cp[Y] > SPAN:
#            if t_c_distance >= SPAN:
#            if t_h_distance > t_cp_distance:
#            if cp[X] - H[X] > 0 and cp[Y] - H[Y] > 0:
#            if H[X] - cp[X] > 0 or H[Y] - cp[Y] > 0:
#            x_diff = fabs(H[X]) - fabs(cp[X])
#            y_diff = fabs(H[Y]) - fabs(cp[Y])

#            x_diff = H[X] - cp[X]
#            y_diff = H[Y] - cp[Y]
#            print(f"D Diff:{ x_diff } , Y Diff: { y_diff }")
#            if fabs(H[X]) - fabs(cp[X]) > 0 or fabs(H[Y]) - fabs(cp[Y]) > 0:

            if t_h_distance > CIRCLE_RADIUS:
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

#                T[X] += -1 * (MAX_DISTANCE - MAX_STEP) * numpy.sign(vector[X]) 
#                T[Y] += -1 * (MAX_DISTANCE - MAX_STEP) * numpy.sign(vector[Y])
#                T[X] += -1 * (RADIUS - MAX_STEP) * numpy.sign(vector[X]) 
#                T[Y] += -1 * (RADIUS - MAX_STEP) * numpy.sign(vector[Y])
# DOES WORK
#                T[X] += -1 * MAX_STEP * numpy.sign(vector[X]) 
#                T[Y] += -1 * MAX_STEP * numpy.sign(vector[Y])
                if [T[X],T[Y]] not in series:
                    series.append([T[X],T[Y]])

#            if H[X] > cp[X]:
#               print("Need to do something with X")
#               T[X] += -1 * MAX_STEP * numpy.sign(vector[X]) 
#            elif H[Y] > cp[Y]:
#               print("Need to do something with Y")
#               T[Y] += -1 * MAX_STEP * numpy.sign(vector[Y])
            print(f"H End: { H }   T End: { T }")

            print(f"Distance: { math.dist(H,T) }")

#        print(
#            f"Distance: { numpy.linalg.norm(H,T) }, Is Integer: { numpy.linalg.norm((H,T).is_integer() }"
#        )
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
