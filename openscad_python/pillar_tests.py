import openpyscad as ops
import numpy as np
import itertools


def build_array_of_cylinders(params):
    # Create an array of cylinders
    cylinders = ops.Union()
    for x, y, h, r in params:
        cyl = ops.Cylinder(h, r, r)
        cyl = cyl.translate([x, y, 0])
        cylinders.append(cyl)

    cylinders.write('cylinders.scad', with_print=True)

def build_array_of_squares(params):
    # Create an array of squares
    squares = ops.Union()
    for x, y, h, w in params:
        square = ops.Cube([w, w, h])
        square = square.translate([x, y, 0])
        squares.append(square)

    squares.write('squares.scad', with_print=True)

def build_array_of_rectangles(params):
    # Create an array of rectangles
    rectangles = ops.Union()
    for x,y,h,w,l in params:
        rectangle = ops.Cube([w, l, h])
        rectangle = rectangle.translate([x, y, 0])
        rectangles.append(rectangle)

    rectangles.write('rectangles.scad', with_print=True)

if __name__ == '__main__':

    r = np.arange(100, 300, 1)

    x = [1100 * i for i in range(len(r))]
    y = [1100 * i for i in range(len(r))]
    h = 500

    # Generate all combinations of x and y coordinates
    locations = list(itertools.product(x, y))
    
    # Repeat h for each location
    h_repeated = [h for _ in locations]
    
    # Repeat r values such that all x=0 have the same r value, x=1 ...
    r_repeated = np.repeat(r, len(y)).tolist()
    
    # Combine into final list of tuples (x, y, h, r)
    final = [(loc[0], loc[1], h_repeated[i], r_repeated[i]) for i, loc in enumerate(locations)]
    
    build_array_of_cylinders(final)

    w = np.arange(200, 600, 2)
    # Repeat w values such that all x=0 have the same w value, x=1 ...
    w_repeated = np.repeat(w, len(y)).tolist()

    final = [(loc[0], loc[1], h_repeated[i], w_repeated[i]) for i, loc in enumerate(locations)]

    build_array_of_squares(final)

    # Generate all combinations of w and l
    l = np.arange(200, 600, 2)
    w = np.arange(200, 600, 2)
    wl = list(itertools.product(w, l))

    # Create the locations
    locations = list(itertools.product(x, y))

    # Repeat h for each location
    h_repeated = [h for _ in locations]

    # Combine into final list of tuples (x, y, h, w, l)
    final = [(loc[0], loc[1], h_repeated[i], wl[i][0], wl[i][1]) for i, loc in enumerate(locations)]

    build_array_of_rectangles(final)

