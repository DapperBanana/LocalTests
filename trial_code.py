
def check_symmetric(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Check if the matrix is symmetric
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Test the function
matrix1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matrix2 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 7]
]

if check_symmetric(matrix1):
    print("Matrix 1 is symmetric")
else:
    print("Matrix 1 is not symmetric")

if check_symmetric(matrix2):
    print("Matrix 2 is symmetric")
else:
    print("Matrix 2 is not symmetric")
