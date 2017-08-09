


# G = 0.299*R + 0.587*G + 0.114*B

# invert the image


# blurred = original.filter(ImageFilter.BLUR)

from PIL import Image
import math

def crop(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    return x


img = Image.open("../../1 - Python/labs/lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        di = i - width/2
        dj = j - height/2
        d = math.sqrt(di*di + dj*dj)
        if d < 100:
            g = r
            b = r

        pixels[i, j] = (r, g, b)

img.show()
