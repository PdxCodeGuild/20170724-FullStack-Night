


# G = 0.299*R + 0.587*G + 0.114*B

# invert the image

# blurred = original.filter(ImageFilter.BLUR)

from PIL import Image
import colorsys
import math


def crop(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    return x


def invert_image():
    img = Image.open("../../1 - Python/labs/lenna.png")
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            '''di = i - width/2
            dj = j - height/2
            d = math.sqrt(di*di + dj*dj)
            if d < 100:
                g = r
                b = r'''

            pixels[i, j] = (255-r, 255-g, 255-b)

    img.show()



def part2():
    img = Image.open("../../1 - Python/labs/lenna.png")
    width, height = img.size
    pixels = img.load()

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

            if h < 0.5 or h > 0.9:
                s = 0

            r, g, b = colorsys.hsv_to_rgb(h, s, v)


            # convert back to [0, 255]
            r = int(r*255)
            g = int(g*255)
            b = int(b*255)

            pixels[i, j] = (r, g, b)

    img.show()


