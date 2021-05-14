#БСБО-05-19 Салынь Даниил Леонидович
def Fibonachi(i):
    fib_numbers = [1, 1]
    if i < 3:
        return fib_numbers[i - 1]
    else:
        for j in range(1, i):
            fib_numbers.append(fib_numbers[j] + fib_numbers[j - 1])
        return fib_numbers[i - 1]


def golden_ratio(i):
    return Fibonachi(i + 1) / Fibonachi(i)


print(golden_ratio(int(input())))
