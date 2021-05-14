# БСБО-05-19 Салынь Даниил Леонидович
from PIL import Image, ImageDraw


def board(num, size):
    for i in range(num):
        for j in range(num):
            new_image = Image.new("RGB", (num * size, num * size), (0, 0, 0))
            draw = ImageDraw.Draw(new_image)
            for i in range(0, num * size, size):
                for j in range(0, num * size, size):
                    if (j // size) % 2  != (i // size) % 2 :
                        draw.rectangle((i, j, i + size, j + size), fill=(255, 255, 255))
    new_image.save("rect.png", "PNG")


board(8, 50)
