from simpleimage import SimpleImage
from random import randint

RGB_MAX = 255 # Maximum RGB value; 255 for 24-big images


def main():
    # Load an image from file
    img_H = SimpleImage('images/H.png')
    img_H_stereo = get_stereogram(imgH)
    img_H.show()
    img_H_stereo.show() 

    # Create a dome
    dome = draw_hemisphere(512, 512, 200)
    dome_stereo = get_stereogram(dome)
    dome.show()
    dome_stereo.show()


def draw_hemisphere(width, height, radius):
    """
    Returns a SimpleImage object with specified dimensions
    (width, height), where a hemisphere with the provided
    radius is drawn in the center of the image. The pixel
    outside the hemisphere is white, while pixel values
    within the hemisphere corresponds to the z-dimension
    height (grayscale image, so rgb share the same value). 
    The tallest point corresponds to black.
    """
    img = SimpleImage.blank(width, height)
    # Image center
    xc = width // 2
    yc = height // 2
    for pixel in img:
        x = pixel.x
        y = pixel.y
        # Distance to the image center
        dist = ((x - xc)**2 + (y - yc)**2)**0.5
        if dist > radius:
            pixel.red = RGB_MAX
            pixel.green = RGB_MAX
            pixel.blue = RGB_MAX
        else:
            depth = (radius**2 - dist**2)**0.5
            val = (1 - depth/radius) * RGB_MAX
            pixel.red = val
            pixel.green = val
            pixel.blue = val
    return img

############################################################
#### The following function is provided. Do not modify. ####
#### You are encouraged to check out the original paper ####
#### if you want to understand the Magic Eye algorithm. ####
############################################################

def get_stereogram(img):
    """
    Takes a SimpleImage object and returns a random dot stereogram
    (also a SimpleImage object) with the same width and height.
    It uses the algorithm by H. W. Thimbleby, S. Inglis, and I. H.
    Witten in their paper 'Displaying 3D Images: Algorithms for 
    Single Image Random Dot Stereograms.' The code is a translation
    from the C code published in the paper.
    """
    DPI = 72 # Output device has 72 pixels per inch (typical resolution)
    EYE_SEP = 2.5 * DPI # Assume eye separation is 2.5 inches
    MU = 1 / 3.0 # Depth of field (fraction of viewing distance)

    def separation(z):
        """
        Stereo separation corresponding to position z.
        The farthest point (from viewer) has z = 0;
        The closest point has z = 1. See the publication
        for the formula derivation.
        """
        return round((1 - MU * z) * EYE_SEP / (2 - MU * z))

    def depth(pixel):
        """
        Returns the z value based on the RGB value of a Pixel
        object in the simpleimage module. Uses the red channel
        alone (rgb is the same for grayscale image). The return
        value satisfies 0 <= z <= 1: black pixel corresponds to
        z = 1 (closest to viewer) and white pixel corresponds to
        z = 0 (farthest from viewer)
        """
        return (RGB_MAX - pixel.red) / RGB_MAX

    width = img.width
    height = img.height
    stereo = SimpleImage.blank(width,height)

    for y in range(height):
        # same stores the index of the corresponding pixel
        # on the right. It's initialized to point to itself
        same = list(range(width))
        for x in range(width):
            z = depth(img.get_pixel(x, y))
            s = separation(z)
            left = x - s // 2 # Index of left and right pixels...
            right = left + s  # ...that should have the same value
            if 0 <= left and right < width:
                # Perform hidden surface removal (see publication)
                visible = True
                zt = 0.0
                t = 1
                while visible and zt < 1:
                    zt = z + 2 * (2 - MU * z) * t / (MU * EYE_SEP)
                    visible = (depth(img.get_pixel(x - t, y)) < zt and 
                               depth(img.get_pixel(x + t, y)) < zt)
                    t += 1
                # If the surface is not hidden, link up the
                # corresponding pixels in the 'same' list
                if visible:
                    l = same[left]
                    while l != left and l != right:
                        if l < right:
                            left = l
                        else:
                            same[left] = right
                            left = right
                            right = l
                        l = same[left]
                    same[left] = right
        # Set pixel values in a row, from right to left
        for x in range(width - 1, -1, -1):
            px = stereo.get_pixel(x, y)
            if same[x] == x:
                px.red = randint(0, RGB_MAX)
                px.green = randint(0, RGB_MAX)
                px.blue = randint(0, RGB_MAX)
            else:
                stereo.set_pixel(x, y, stereo.get_pixel(same[x], y))
    return stereo


if __name__ == '__main__':
    main()