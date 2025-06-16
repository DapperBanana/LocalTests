
def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        print("Cannot perform matrix multiplication. Number of columns in first matrix does not match number of rows in second matrix.")
        return None
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = matrix_multiplication(matrix1, matrix2)
if result:
    for row in result:
        print(row)
