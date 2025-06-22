
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

def display_matrix(matrix):
    for row in matrix:
        print(row)

# Define two matrices
matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[5, 6],
           [7, 8]]

# Add matrices
print("Matrix1 plus Matrix2:")
result_add = add_matrices(matrix1, matrix2)
display_matrix(result_add)

# Subtract matrices
print("\nMatrix1 minus Matrix2:")
result_sub = sub_matrices(matrix1, matrix2)
display_matrix(result_sub)
