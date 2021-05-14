# БСБО-05-19 Салынь Даниил Леонидович
from PIL import Image, ImageDraw


def gradient(color):
    new_color = (0, 0, 0)
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for i in range(0, 512, 2):
        if color == "R":
            draw.line((i, 0, i + 2, 0), fill=((i + 2) // 2, 0, 0), width=512)
        if color == "G":
            draw.line((i, 0, i + 2, 0), fill=(0, (i + 2) // 2, 0), width=512)
        if color == "B":
            draw.line((i, 0, i + 2, 0), fill=(0, 0, (i + 2) // 2), width=512)
    new_image.save('grad.png', "PNG")


gradient(input().upper())
