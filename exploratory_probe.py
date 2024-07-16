
def is_symmetric(matrix):
    if len(matrix) != len(matrix[0]):
        return False

    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Test the function
matrix1 = [
    [1, 2, 3],
    [2, 1, 4],
    [3, 4, 5]
]

matrix2 = [
    [1, 2, 3],
    [2, 1, 4],
    [3, 4, 5]
]

print(is_symmetric(matrix1))  # False
print(is_symmetric(matrix2))  # True
