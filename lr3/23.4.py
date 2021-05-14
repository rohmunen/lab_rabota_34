# БСБО-05-19 Салынь Даниил Леонидович
import math

t = 0
calc_dist = lambda x, y: math.hypot(x-0.75, y-0)
while t < 2 * math.pi:
    x = math.cos(t) ** 3
    y = math.sin(t) ** 3

    if t == 0:
        dist = calc_dist(x, y)
    elif (new_dist := calc_dist(x, y)) < dist:
        dist = new_dist
    t += .0001
print(dist)