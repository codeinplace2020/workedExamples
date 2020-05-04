from simpleimage import SimpleImage

PYRAMID_LEVEL = 6 # Should be a positive integer
RGB_MAX = 255     # Max RGB value. 255 for 24-bit RGB image


def main():
    # Load images
    img1 = SimpleImage('images/apple.jpg')
    img2 = SimpleImage('images/orange.jpg')
    if img1.width != img2.width or img1.height != img2.height:
        print('Mismatched image dimensions! Abort.')
        return -1
    
    # Build and combine pyramids    
    pyramid1 = build_pyramid(img1, PYRAMID_LEVEL)
    pyramid2 = build_pyramid(img2, PYRAMID_LEVEL)
    pyramid_combined = []
    for i in range(len(pyramid1)):
        pyramid_combined.append(combine(pyramid1[i], pyramid2[i]))
    
    # Reconstruct blended image
    img_blended = reconstruct_image(pyramid_combined)
    img_blended.show()

    # Combine without blending
    img_combined = combine(img1, img2)
    img_combined.show()


def reconstruct_image(pyramid):
    """
    Reconstructs an image from a Laplacian-like image pyramid.
    Returns the reconstructed SimpleImage object
    """
    curr_layer = pyramid[-1]
    for i in range(len(pyramid)-1, 0, -1):
        prev_layer = pyramid[i-1]
        w = prev_layer.width
        h = prev_layer.height
        curr_layer = subtract(resize(curr_layer, w, h), prev_layer)
    return curr_layer


def build_pyramid(img, level):
    """
    Builds a Laplacian-like image pyramid with 'level' levels for
    a given img. Returns a list of SimpleImage objects, where the
    first entry corresponds to level 0 of the pyramid (largest size)
    and the last entry is the highest level of the pyramid (smallest
    size). The length of the list is (level+1)
    """
    pyramid = []
    curr_layer = img
    for i in range(level):
        w = curr_layer.width
        h = curr_layer.height
        next_layer = resize(curr_layer, w//2, h//2)
        diff = subtract(resize(next_layer, w, h), curr_layer)
        pyramid.append(diff)
        curr_layer = next_layer
    pyramid.append(curr_layer)
    return pyramid


def resize(img, width, height):
    """
    Returns a new SimpleImage object, which is a resized version
    of img. Parameters width and height specify the new size
    """
    blank = SimpleImage.blank(width, height)
    resized = copy_image(img)
    resized.make_as_big_as(blank)
    return resized


def subtract(img1, img2):
    """
    Returns a new SimpleImage object, which is a result of
    subtracting img2 from img1 for each RGB channel in each pixel
    """
    res = SimpleImage.blank(img1.width, img1.height)
    for pixel in res:
        x = pixel.x
        y = pixel.y
        px1 = img1.get_pixel(x, y)
        px2 = img2.get_pixel(x, y)
        pixel.red = max(0, px1.red - px2.red)
        pixel.green = max(0, px1.green - px2.green)
        pixel.blue = max(0, px1.blue - px2.blue)
    return res


def combine(img1,img2):
    """
    Returns a new SimpleImage object whose left half is
    taken from img1 and right half taken from img2
    """
    w = img1.width
    h = img1.height
    img = SimpleImage.blank(w, h)
    for x in range(w):
        for y in range(h):
            if x < w // 2:
                img.set_pixel(x, y, img1.get_pixel(x, y))
            else:
                img.set_pixel(x, y, img2.get_pixel(x, y))
    return img


def copy_image(img):
    """
    Returns a new SimpleImage object, which has the same
    pixel values as img, which is also a SimpleImage object
    """
    copy = SimpleImage.blank(img.width, img.height)
    for pixel in copy:
        x = pixel.x
        y = pixel.y
        copy.set_pixel(x, y, img.get_pixel(x, y))
    return copy


if __name__ == '__main__':
    main()