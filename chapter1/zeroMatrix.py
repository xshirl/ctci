def zeroMatrix(matrix):
    matrixHeight = len(matrix)
    matrixWidth = len(matrix[0])
    rows = []
    cols = []
    for i in range(matrixHeight):
        for j in range(matrixWidth):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)

    for row in rows:
        nullify_row(matrix, row)

    for col in cols:
        nullify_col(matrix, col)

    return matrix


def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


testMatrix = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]


print(zeroMatrix(testMatrix))
