# БСБО-05-19 Салынь Даниил Леонидович
import random

dots = []


def get_random_num(density):
    return random.randint(0, density) / density, random.randint(0, density) / density


def add_dot_if_not_present(x, y):
    if (x, y) not in dots:
        dots.append((x, y))


def check_if_dot_in_circle(x, y):
    if x ** 2 + y ** 2 < 1:
        add_dot_if_not_present(x, y)

for i in range(15000):
    x,y = get_random_num(1000000)
    check_if_dot_in_circle(x,y)
print(len(dots) * 4 / 15000)