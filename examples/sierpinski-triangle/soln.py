#!/usr/bin/env python3

"""
Sierpinski Triangle
By GregS

This program demonstrates drawing a famous and interesting shape using
recursion.  It starts with an equilateral triangle, and at each level
breaks the triangle into four smaller equilateral triangles, colors the
middle one, and recurses on the other three.

"""

import tkinter
import math

# How much empty space to leave around the biggest triangle in pixels
TRIANGLE_BORDER = 20

# How big to make our window, as a percentage of the screen size
WINDOW_SCREEN_PERCENTAGE = 85

# How big the smallest triangle's edge can be, in pixels
MIN_TRIANGLE = 9


def midpoint(p1, p2):
    """
    Takes two points, each of which is [x, y] coordinates, and returns a
    point halfway between them.
    """
    return [(p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0]


def distance(p1, p2):
    """
    Takes two points, each of which is [x, y] coordinates, and returns
    the distance between them.
    """
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def tri_color(level):
    """
    Given a level number, returns what color to fill the triangle with.
    Takes a zero-based level number, and returns a color string suitable
    for tkinter.
    """

    # These colors are arbitrary, but have the same lightness and
    # saturation, just different hues, so they "go together".
    tri_colors = ["#f76d6d", "#f76dd4", "#b26df7", "#6d90f7",
                  "#6df7f7", "#6df790", "#b2f76d", "#f7d46d"]

    return tri_colors[level % len(tri_colors)]


def draw_tri_inner(canvas, level, p1, p2, p3):
    """
    Given a canvas to draw on, a level indicating how many times we've
    been called, and three points (p1, p2, and p3) which form an
    equilateral triangle, break this triangle into four equal
    equilateral triangles, color in the middle one, and recursively call
    ourselves to decompose and color the other three triangles.

    This function should only be called by draw_triangle() , which will
    construct the initial triangle points p1, p2, and p3 (each of which
    are [x,y] coordinates), and pass in a level of 0.  "level" is only
    used for choosing triangle colors.
    """

    # We are given points p1, p2, p3 , which make an equilateral triangle.
    # We break this triangle down into four equilateral triangles, s0, s1,
    # s2, and s3 as follows:
    #
    #                        p2
    #                        /\
    #                       /  \
    #                      /    \
    #                     /  s2  \
    #                    /        \
    #                p4 /----------\ p5
    #                  /\          /\
    #                 /  \   s0   /  \
    #                /    \      /    \
    #               /      \    /      \
    #              /  s1    \  /   s3   \
    #             /__________\/__________\
    #            p1          p6           p3
    #
    # Each new point (p4, p5, and p6) is at the midpoint of the side it
    # is on.
    #
    # On this level, we only color in s0, the middle triangle with points
    # (p4, p5, p6), and then call ourselves recursively on each of triangles
    # s1, s2, and s3, in turn breaking them up and coloring each of them
    # this same way.  Each time we add one to the level to get a different
    # color for each size of triangle.

    p4 = midpoint(p1, p2)
    p5 = midpoint(p2, p3)
    p6 = midpoint(p1, p3)

    # We stop if the triangle we were asked to color is too small
    if distance(p4, p5) < MIN_TRIANGLE:
        return

    new_color = tri_color(level)

    canvas.create_polygon(p4, p5, p6, fill=new_color, width=0)

    draw_tri_inner(canvas, level + 1, p1, p4, p6)  # s1
    draw_tri_inner(canvas, level + 1, p4, p2, p5)  # s2
    draw_tri_inner(canvas, level + 1, p6, p5, p3)  # s3


def draw_triangle(canvas, xsize, ysize):
    """
    We are given a canvas to draw on, and the size of that canvas.

    We will figure out the biggest equilateral triangle that fits on it,
    with a little border, and kick off drawing a Sierpinski triangle.

    We only draw the largest triangle here, in black, and then call
    draw_tri_inner() with the points of that largest triangle.  That
    function will recursively break up this triangle and color it, as
    described there.
    """

    # Note that in tkinter the upper left is (0, 0) and coordinates grow
    # down and to the right.
    #
    # We are drawing an equilateral triangle (p1,p2,p3), which looks like:
    #
    #                        p2   (triedge / 2, 0)
    #                         .
    #                        /.\
    #                       / . \
    #                      /  .  \
    #                     /   .   \
    #                    /    .    \
    #                   /_____.___ _\
    #  (0, triheight)  p1     a    p3   (triedge, triheight)
    #
    #
    # The dots are an altitude of this triangle (which we do not draw,
    # just to explain here).  Angle (p2,p1,p3) is 60 degrees (it's an
    # equilateral triangle), angle (p1,a,p2) is 90 degrees, leaving
    # angle (a,p2,p1) as 30 degrees. This means that the height (p2,a)
    # is the edge length (p1,p2) * sqrt(3) / 2 .
    #
    # Calculate the triangle edge length and height, which are all we
    # need to calculate our vertices (see picture above).  The triangle
    # has to fit in our xsize by ysize canvas.  This is for the top
    # (first) triangle, and so should take up as much of the canvas as
    # it can.  The ysize is scaled down by sqrt(3)/2 as we have to
    # multiply it by that same amount to find the height.  We round
    # triedge to a multiple of 32 so that it can be evenly divided by 2
    # a number of times.

    b = TRIANGLE_BORDER
    triedge = int(min(xsize, ysize / (math.sqrt(3.0) / 2.0)) - b * 2)
    triedge = triedge - triedge % 32
    triheight = int(triedge * math.sqrt(3.0) / 2.0)

    # These are the points from our picture above, with a border added in
    p1 = [0 + b, triheight + b]
    p2 = [triedge / 2 + b, 0 + b]
    p3 = [triedge + b, triheight + b]

    # Our triangle is black, every other level will be a color
    canvas.create_polygon(p1, p2, p3, fill="black", width=0)

    draw_tri_inner(canvas, 0, p1, p2, p3)


def setup_graphics():
    """
    This function does all the graphics setup.  We are using tkinter.
    It returns the window it made (which the caller should simply call
    mainloop() on), a canvas to draw on, and the dimensions of that
    canvas.
    """

    win = tkinter.Tk()
    win.title("Sierpinski Triangle")

    # To keep things simpler, make our window non-resizable, and some
    # percentage of the screen dimension.  We try to make the xsize 15%
    # bigger than the ysize just so there is less wasted space around
    # our triangle.  This 15% is roughly sqrt(3)/2 , see draw_triangle()
    # for an explanation of why this ratio.
    ysize = int(win.winfo_screenheight() * WINDOW_SCREEN_PERCENTAGE / 100.0)
    xsize = int(min(ysize * 1.15,
                    win.winfo_screenwidth() * WINDOW_SCREEN_PERCENTAGE / 100.0))
    win.geometry("{}x{}".format(xsize, ysize))
    win.resizable(False, False)

    frame = tkinter.Frame(win)
    frame.pack(fill=tkinter.BOTH, expand=True)
    canvas = tkinter.Canvas(frame, width=xsize, height=ysize,
                            bg="white", border=0, highlightthickness=0)
    canvas.pack()
    win.update()

    return win, canvas, xsize, ysize


def main():
    """
    Draw a Sierpinski Triangle.
    """

    win, canvas, xsize, ysize = setup_graphics()
    draw_triangle(canvas, xsize, ysize)
    win.mainloop()


if __name__ == "__main__":
    main()
