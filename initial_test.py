
def matrix_multiplication(matrix1, matrix2):
    result = []

    num_rows1 = len(matrix1)
    num_cols1 = len(matrix1[0])
    num_cols2 = len(matrix2[0])

    for i in range(num_rows1):
        row = []
        for j in range(num_cols2):
            sum = 0
            for k in range(num_cols1):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)

    return result

# Example usage
matrix1 = [[1, 2],
           [3, 4]]

matrix2 = [[5, 6],
           [7, 8]]

result = matrix_multiplication(matrix1, matrix2)

for row in result:
    print(row)
