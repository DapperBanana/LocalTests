
def is_symmetric(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows != num_cols:
        return False

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Example matrix
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
