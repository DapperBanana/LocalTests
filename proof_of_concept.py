
def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Sample matrices
matrix1 = [
    [2, 3],
    [4, 5]
]

matrix2 = [
    [1, 2],
    [3, 4]
]

result = matrix_multiplication(matrix1, matrix2)
for row in result:
    print(row)
