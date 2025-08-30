
def multiply_matrices(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix for multiplication.")
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = multiply_matrices(matrix1, matrix2)
for row in result:
    print(row)
