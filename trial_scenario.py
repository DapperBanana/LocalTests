
def matrix_multiplication(matrix1, matrix2):
    result = []
    
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)
    
    return result

# Example matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[1, 2], [3, 4]]

result = matrix_multiplication(matrix1, matrix2)
for row in result:
    print(row)
