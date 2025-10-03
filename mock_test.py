
def is_symmetric(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    # Check if the matrix is symmetric
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Test the program with a sample matrix
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if is_symmetric(matrix):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
