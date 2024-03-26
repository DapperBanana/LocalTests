
def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def sub_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example matrices
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

addition_result = add_matrices(matrix1, matrix2)
print("\nAddition Result:")
print_matrix(addition_result)

subtraction_result = sub_matrices(matrix1, matrix2)
print("\nSubtraction Result:")
print_matrix(subtraction_result)
