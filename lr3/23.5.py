# БСБО-05-19 Салынь Даниил Леонидович
def same_by(characteristic, values):
    f = characteristic
    for i in range(1, len(values)):
        if f(values[i - 1]) != f(values[i]):
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')