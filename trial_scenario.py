
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
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Addition
result_addition = add_matrices(matrix1, matrix2)
print("Matrix Addition:")
for row in result_addition:
    print(row)

# Subtraction
result_subtraction = subtract_matrices(matrix1, matrix2)
print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)
