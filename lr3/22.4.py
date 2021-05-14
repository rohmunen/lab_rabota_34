# БСБО-05-19 Салынь Даниил Леонидович
import math


def roots_of_quadratic_equation(*nums):
    roots = []
    if len(nums) == 3:
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a == b == c == 0:
            roots.append("ALL")
        else:
            d = b * b - 4 * a * c
            if d > 0:
                roots.append((-1 * b + math.sqrt(d)) / (2 * a))
                roots.append((-1 * b - math.sqrt(d)) / (2 * a))
            elif d == 0:
                roots.append(-1 * b / (2 * a))
    elif len(nums) == 2:
        b = nums[0]
        c = nums[1]
        roots.append(-1 * c / b)
    elif len(nums) == 1:
        c = nums[0]
        if c == 0:
            roots.append("ALL")
        else:
            return None
    else:
        return None
    return roots


result = roots_of_quadratic_equation(1)
if result is not None:
    print(*sorted(result))
else:
    print(None)

result = roots_of_quadratic_equation(1, 1)
if result is not None:
    print(*sorted(result))
else:
    print(None)

result = roots_of_quadratic_equation(1, -3, 2)
if result is not None:
    print(*sorted(result))
else:
    print(None)
