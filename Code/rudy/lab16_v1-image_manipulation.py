#   Lab 16.1    Image Manipulation

# y = 0.299 * r + 0.587 * g + 0.114 * b

from PIL import Image
img = Image.open("../../1 - Python/labs/lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299 * r + 0.587 * g + 0.114 * b

        #r = int(y)
        #g = int(y)
        #b = int(y)

        pixels[i, j] = (255-r, 255-g, 255-b)

img.show()



