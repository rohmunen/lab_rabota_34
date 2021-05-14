#БСБО-05-19 Салынь Даниил Леонидович
def equation(dot_one: str, dot_two: str):
    flag = False
    x1 = float(dot_one[:dot_one.find(";")])
    y1 = float(dot_one[dot_one.find(";") + 1:])
    x2 = float(dot_two[:dot_two.find(";")])
    y2 = float(dot_two[dot_two.find(";") + 1:])
    if x1 == x2:
        flag = True
        print(x1)
    elif y1 == y2:
        flag = True
        print(y1)
    if not flag:
        one_matrix = [[y1, x1, 1], [y2, x2, 1]]
        if x1 == 0:
            b = y1
            k = (y2 - b / x2)
        else:
            temp_matrix = [y2 - y1 * x2 / x1, 0, 1 - 1 * x2/x1]
            b = temp_matrix[0] / temp_matrix[2]
            k = (y1 - b) / x1
        print(k, b)


equation(input("точка 1: "), input("точка 2: "))
