#   Lab 16.2  Image Manipulation



import colorsys


from PIL import Image
img = Image.open("../../1 - Python/labs/lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        #y = 0.299 * r + 0.587 * g + 0.114 * b       # brightness in an RGB triplet to convert to greyscale

        #r = int(y)
        #g = int(y)
        #b = int(y)

        # colorsys uses colors in the range [0, 1]


        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h += .3     # hue of entire picture
        s += 1      # saturation of entire picture
        v += .3     # value of entire picture
        # do some math on h, s, v


        r, g, b = colorsys.hsv_to_rgb(h, s, v)


        # convert back to [0, 255]

        r = int(r*255)
        g = int(g*0)   # <------- removes all green
        b = int(b*0)   # <------- removes all blue

        pixels[i, j] = (r, g, b)

img.show()