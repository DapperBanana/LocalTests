
def determinant(matrix):
    n = len(matrix)
    
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    for i in range(n):
        cofactor = matrix[0][i] * determinant([row[:i] + row[i+1:] for row in matrix[1:]])
        det += (-1)**i * cofactor
    
    return det

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

det = determinant(matrix)
print("Determinant of the matrix is:", det)
