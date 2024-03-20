
def matrix_multiplication(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if cols1 != rows2:
        return "Matrix multiplication not possible"

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6]]

matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = matrix_multiplication(matrix1, matrix2)

if result != "Matrix multiplication not possible":
    for row in result:
        print(row)
else:
    print(result)
