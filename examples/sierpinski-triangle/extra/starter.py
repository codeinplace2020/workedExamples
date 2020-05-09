#!/usr/bin/env python3

"""
Sierpinski Triangle

This program demonstrates drawing a famous and interesting shape.
"""

import tkinter


# How big to make our window, as a percentage of the screen size
WINDOW_SCREEN_PERCENTAGE = 85


def draw_triangle(canvas, xsize, ysize):
    """
    We are given a canvas to draw on, and the size of that canvas.

    We will kick off drawing a Sierpinski triangle.


    NOTE: the body of this function should be replaced with your code,
    this is just examples of drawing.
    """

    # Note that in tkinter the upper left is (0, 0) and coordinates grow
    # down and to the right.

    # An example of how to draw a triangle on the canvas
    p1 = [0, 50]  # x, y
    p2 = [29, 0]
    p3 = [58, 50]
    canvas.create_polygon(p1, p2, p3, fill="red", width=0)

    # Some other things you can draw, which are not necessarily needed for
    # this problem:

    canvas.create_line([0, ysize / 4], [xsize - 1, 0], fill="blue", width="10")

    canvas.create_text([300, 50], fill="#20f040", font="Arial 20", text="Some text")


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
    # our triangle.  This 15% is roughly sqrt(3)/2 .
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
