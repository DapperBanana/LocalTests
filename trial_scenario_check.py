
def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

def subtract_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

# Initialize matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

# Add matrices
result_add = add_matrices(matrix1, matrix2)
print("\nMatrix Addition:")
print_matrix(result_add)

# Subtract matrices
result_subtract = subtract_matrices(matrix1, matrix2)
print("\nMatrix Subtraction:")
print_matrix(result_subtract)
