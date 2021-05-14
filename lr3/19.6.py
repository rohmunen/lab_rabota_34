#БСБО-05-19 Салынь Даниил Леонидович
def catalan(n: int):
    if n == 0:
        return 1
    result = 0
    for i in range(n):
        result += catalan(i) * catalan(n - i - 1)
    return result


print(catalan(3))
