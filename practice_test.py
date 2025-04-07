
def add_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def subtract_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix1 = [[1, 2],
           [3, 4]]
matrix2 = [[5, 6],
           [7, 8]]

print("Matrix1:")
print_matrix(matrix1)

print("Matrix2:")
print_matrix(matrix2)

add_result = add_matrices(matrix1, matrix2)
print("Matrix1 + Matrix2:")
print_matrix(add_result)

subtract_result = subtract_matrices(matrix1, matrix2)
print("Matrix1 - Matrix2:")
print_matrix(subtract_result)
