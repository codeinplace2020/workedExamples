from simpleimage import SimpleImage

K1 = -10 # Distortion factor. Negative for bulging; positive for contraction
RGB_MAX = 255 # Max RGB value. 255 for 24-bit RGB image
EPSILON = 1E-10 # A very small positive float
FILE_DIR = 'images/quad.jpg'


def main():
    # Load original image
    img = SimpleImage(FILE_DIR)
    width = img.width
    height = img.height
    
    # Image center
    xc = width // 2
    yc = height // 2

    # Generate distorted image
    distorted = SimpleImage.blank(width, height)
    for pixel in distorted:
        x = pixel.x
        y = pixel.y
        xu, yu = get_coordinates(x, y, xc, yc, K1, width, height)
        if 0 <= xu < width and 0 <= yu < height:
            distorted.set_pixel(x, y, img.get_pixel(xu, yu))
        else: # Set to white color
            pixel.red = RGB_MAX
            pixel.green = RGB_MAX
            pixel.blue = RGB_MAX
    
    # Display images
    img.show()
    distorted.show()


def get_coordinates(xd, yd, xc, yc, k1, width, height):
    """
    Given coordinates (xd, yd) in the distorted image and the
    center of distortion (xc, yc), returns the corresponding 
    coordinates in the undistorted image, (xu, yu).
    k1 is the distortion factor. The width and height specify
    the dimension of the undistorted image. For details, see:
    https://en.wikipedia.org/wiki/Distortion_(optics)
    """
    r_squared = ((xd - xc)**2 + (yd - yc)**2) / (width**2 + height**2)
    denominator = max(EPSILON, 1 + k1 * r_squared) # Prevent division by 0
    xu = xc + (xd - xc) / denominator
    yu = yc + (yd - yc) / denominator
    return (round(xu), round(yu))


if __name__ == "__main__":
    main()