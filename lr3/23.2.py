# БСБО-05-19 Салынь Даниил Леонидович
import math


def find_farthest_orbit(orbits: list):
    for i in orbits:
        if i[0] == i[1]:
            orbits.remove(i)
    orbit_count = lambda x: x[0] * x[1] * math.pi
    mapObj = map(orbit_count, orbits)
    mappedList = list(mapObj)
    return orbits[mappedList.index(max(mappedList))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
