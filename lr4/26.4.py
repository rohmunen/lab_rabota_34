# БСБО-05-19 Салынь Даниил Леонидович
import random

from PIL import Image
from PIL import ImageDraw

image = Image.new('RGB', (800, 220), (0, 0, 0))
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw = ImageDraw.Draw(image)

draw.line([(250, 150), (200, 50), (150, 150)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(300, 150), (100, 150)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(300, 150), (280, 170)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(100, 150), (120, 170)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(450, 170), (400, 50), (350, 170)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(450, 150), (350, 150)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(600, 50), (600, 170)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(500, 50), (500, 170)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(500, 110), (600, 110)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(650, 170), (700, 100)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(700, 170), (700, 50)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(650, 50), (700, 50)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(650, 50), (650, 100)], width=3, fill=font_color)
font_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.line([(650, 100), (700, 100)], width=3, fill=font_color)

image.save('name.png', 'PNG')
