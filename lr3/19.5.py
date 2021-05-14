#БСБО-05-19 Салынь Даниил Леонидович
def prime(number: int):
    count = 1
    for i in range(2, number + 1):
        if (number / i) % 1 == 0:
            count += 1
    if number == 1:
        print("ни простое ни составное число")
    elif count == 2:
        print("Простое число")
    else:
        print("Составное число")


prime(int(input()))
