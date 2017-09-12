from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here Y = 0.299*r + 0.587*g + 0.114*b
        '''Y = 0.299*r + 0.587*g + 0.114*b
        r = int(Y)
        g = int(Y)
        b = int(Y)'''

        pixels[i, j] = (r, g, b)

img.show()