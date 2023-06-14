def kth_smallest_in_matrix(matrix, k):
    m = len(matrix)
    if m > 0:
        n = len(matrix[0])
    else:
        return None

    if m * n < k:
        return None
    
    # Flatten the matrix into a 1D array
    flattened = [element for row in matrix for element in row]

    # Sort the flattened array in ascending order
    flattened.sort()

    # Return the kth smallest element
    return flattened[k - 1]
