#БСБО-05-19 Салынь Даниил Леонидович
import math


def roots_of_quadratic_equation(a: int, b: int, c: int):
    roots = []
    if a == 0:
        roots.append(-1 * c / b)
    elif a == b == c == 0:
        roots.append("ALL")
    else:
        d = b * b - 4 * a * c
        if d > 0:
            roots.append((-1 * b + math.sqrt(d)) / (2 * a))
            roots.append((-1 * b - math.sqrt(d)) / (2 * a))
        elif d == 0:
            roots.append(-1 * b / (2 * a))
    return roots


result = roots_of_quadratic_equation(int(input()), int(input()), int(input()))
print(*sorted(result))

