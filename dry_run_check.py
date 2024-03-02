
def is_symmetric(matrix):
    row = len(matrix)
    col = len(matrix[0])

    if row != col:
        return False

    for i in range(row):
        for j in range(i + 1, col):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Test the program
matrix1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matrix2 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 6, 7]
]

print("Matrix 1 is symmetric:", is_symmetric(matrix1))
print("Matrix 2 is symmetric:", is_symmetric(matrix2))
