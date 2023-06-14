def rotate_matrix(matrix, n):
    rows = len(matrix)
    cols = len(matrix[0])

    # Normalize n to be within the range [0, 3]
    n = n % 4

    # Perform rotation
    for _ in range(n):
        # Create a new matrix with transposed dimensions
        new_rows = cols
        new_cols = rows
        new_matrix = [[0] * new_cols for _ in range(new_rows)]

        # Fill the new matrix with rotated values
        for i in range(rows):
            for j in range(cols):
                new_matrix[j][new_cols - i - 1] = matrix[i][j]

        # Update the original matrix with the rotated values
        matrix = new_matrix
        rows, cols = new_rows, new_cols

    return matrix
