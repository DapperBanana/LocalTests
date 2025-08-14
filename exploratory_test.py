
def matrix_multiply(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            temp = 0
            for k in range(len(matrix2)):
                temp += matrix1[i][k] * matrix2[k][j]
            row.append(temp)
        result.append(row)
    return result

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = matrix_multiply(matrix1, matrix2)

for row in result:
    print(row)
