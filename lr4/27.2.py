# БСБО-05-19 Салынь Даниил Леонидович
import random

from PIL import Image


def image_filter(pixels, i, j):
    return tuple(map(lambda x: (x + random.randint(0, 150)) % 256, pixels[i, j]))


image = Image.open('image.jpg')
x, y = image.size
pixels = image.load()

new_image = Image.new('RGB', (x, y), (0, 0, 0))
new_image_pixels = new_image.load()
for i in range(x):
    for j in range(y):
        new_image_pixels[i, j] = image_filter(pixels, i, j)

new_image.save('imagee.bmp', 'bmp')
