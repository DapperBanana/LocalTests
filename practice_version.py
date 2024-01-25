
def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions"

    # Initialize an empty result matrix
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Perform element-wise addition
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

def subtract_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must have the same dimensions"

    # Initialize an empty result matrix
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Perform element-wise subtraction
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]

    return result

# Test the functions
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Matrix Addition:")
result_addition = add_matrices(matrix1, matrix2)
for row in result_addition:
    print(row)

print("Matrix Subtraction:")
result_subtraction = subtract_matrices(matrix1, matrix2)
for row in result_subtraction:
    print(row)
