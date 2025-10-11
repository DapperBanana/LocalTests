
def matrix_addition(A, B):
    result = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

def matrix_subtraction(A, B):
    result = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] - B[i][j]
    
    return result

# Example matrices
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Perform addition
result_addition = matrix_addition(matrix1, matrix2)
print("Matrix Addition:")
for row in result_addition:
    print(row)

# Perform subtraction
result_subtraction = matrix_subtraction(matrix1, matrix2)
print("\nMatrix Subtraction:")
for row in result_subtraction:
    print(row)
