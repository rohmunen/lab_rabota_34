from PIL import Image


# БСБО-05-19 Салынь Даниил Леонидович
def make_preview(size, n_colors):
    one_size = size[0]
    two_size = size[1]

    try:
        original = Image.open("image.jpg")
    except FileNotFoundError:
        print("Файл не найден")
    original = original.quantize(n_colors)
    resized_image = original.resize((one_size, two_size), Image.ANTIALIAS)
    resized_image.save("imagee.bmp")


make_preview((400, 200), 64)
