#БСБО-05-19 Салынь Даниил Леонидович
def defractalize(fractal: list):
    n = len(fractal)
    for i in fractal:
        if type(i) is list:
            fractal.remove(i)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)
fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)
