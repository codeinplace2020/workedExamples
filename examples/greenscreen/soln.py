"""
This program shows an example of "greenscreening", well
actually "bluescreening" in this case, where we replace the
pixels of a certain color intensity in a particular channel
(here, we use red) with the pixels from another image.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6

def bluescreen(main_filename, back_filename):
    """
    Implements the notion of "bluescreening". That is,
    the image in the main_filename has its "sufficiently"
    blue pixels replaced with pixel from the corresponding x, y
    location in the image in the file back_filename.
    Returns the resulting "bluescreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" red
        if pixel.blue >= average * INTENSITY_THRESHOLD:
            # If so, we get the corresponding pixel from the
            # back image and overwrite the pixel in the
            # main image with that from the back image.
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))
    return image


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    original_stop = SimpleImage('images/stop.png')
    original_stop.show()

    original_leaves = SimpleImage('images/leaves.png')
    original_leaves.show()

    stop_leaves_replaced = bluescreen('images/stop.png', 'images/leaves.png')
    stop_leaves_replaced.show()


if __name__ == '__main__':
    main()