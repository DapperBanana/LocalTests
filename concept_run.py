
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def sub_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

print("Matrix 1:")
print_matrix(matrix1)
print("\nMatrix 2:")
print_matrix(matrix2)

addition_result = add_matrices(matrix1, matrix2)
print("\nAddition of Matrix 1 and Matrix 2:")
print_matrix(addition_result)

subtraction_result = sub_matrices(matrix1, matrix2)
print("\nSubtraction of Matrix 1 and Matrix 2:")
print_matrix(subtraction_result)
