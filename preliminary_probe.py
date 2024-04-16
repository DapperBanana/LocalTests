
def add_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

def subtract_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)
    return result

# Example matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Addition of matrices
result_add = add_matrices(matrix1, matrix2)
for row in result_add:
    print(row)

# Subtraction of matrices
result_subtract = subtract_matrices(matrix1, matrix2)
for row in result_subtract:
    print(row)
