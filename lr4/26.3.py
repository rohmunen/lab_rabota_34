# БСБО-05-19 Салынь Даниил Леонидович
from PIL import Image, ImageDraw


def makeanagliph(filename, delta):
    im = Image.open("image.jpg")
    pixels = im.load()
    width, height = im.size
    new_im = Image.new('RGB', (width, height), (0, 0, 0))
    pixels_new = new_im.load()
    for i in range(width):
        for j in range(height):
            if i < delta:
                _, g, b = pixels[i, j]
                pixels_new[i, j] = 0, g, b
            else:
                _, g, b = pixels[i, j]
                r = pixels[i - delta, j][0]
                pixels_new[i, j] = r, b, g
    new_im.save("new_im.png", "PNG")


makeanagliph("image.jpg", 10)
