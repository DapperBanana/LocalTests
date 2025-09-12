
def matrix_multiplication(matrix_1, matrix_2):
    result = [[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
    
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    
    return result

# Example matrices
matrix_1 = [[1, 2],
            [3, 4]]

matrix_2 = [[5, 6],
            [7, 8]]

result = matrix_multiplication(matrix_1, matrix_2)
for row in result:
    print(row)
