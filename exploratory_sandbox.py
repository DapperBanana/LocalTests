
def matrix_multiplication(matrix1, matrix2):
    result = []
    
    # Get the number of rows and columns for each matrix
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    # Check if the matrices can be multiplied
    if cols1 != rows2:
        print("Matrices cannot be multiplied. Make sure the number of columns in the first matrix is equal to the number of rows in the second matrix.")
        return result
    
    # Create a result matrix filled with zeros
    for i in range(rows1):
        result.append([0] * cols2)
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example matrices to multiply
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

result = matrix_multiplication(matrix1, matrix2)
for row in result:
    print(row)
