def transpose_matrix(matrix):
    rows = len(matrix)
    if rows == 0:
        cols = 0
    else:
        cols = len(matrix[0])

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed
