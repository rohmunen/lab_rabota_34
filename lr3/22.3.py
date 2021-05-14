# БСБО-05-19 Салынь Даниил Леонидович
scoring = {1: [8, 2], 2: [6, 2], 3: [42, 56], 20: [50, 3]}


def score(name: str, sector=-1):
    if name == "Яблочко":
        return 50
    elif name == "Зеленое кольцо":
        return 25
    elif name == "Внешнее кольцо":
        return scoring[sector][0]
    else:
        return scoring[sector][1]


print(score("Яблочко"))
print(score("Внешнее кольцо", 1))