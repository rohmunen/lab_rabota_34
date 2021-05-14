#БСБО-05-19 Салынь Даниил Леонидович
def transpose(matrix: list):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[j].append(matrix[i][j])
    matrix.clear()
    for i in range(len(new_matrix)):
        matrix.append(new_matrix[i])


matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
