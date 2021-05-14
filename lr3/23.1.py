# БСБО-05-19 Салынь Даниил Леонидович
transformation = lambda x: x
values = [2, 3, 5, "asdfg"]
transformed_values = list(map(transformation, values))

if values == transformed_values:
    print("ok")
else:
    print("fail")
