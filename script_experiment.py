
def add_matrices(matrix1, matrix2):
    result = []
    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def subtract_matrices(matrix1, matrix2):
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

# Example matrices
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

print("\nMatrix 1 + Matrix 2:")
result_add = add_matrices(matrix1, matrix2)
print_matrix(result_add)

print("\nMatrix 1 - Matrix 2:")
result_subtract = subtract_matrices(matrix1, matrix2)
print_matrix(result_subtract)
