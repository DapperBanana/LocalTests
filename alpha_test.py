
def determinant(matrix):
    size = len(matrix)
    
    if size == 1:
        return matrix[0][0]
    
    det = 0
    for i in range(size):
        minor = [row[:i] + row[i+1:] for row in matrix[1:]]
        det += ((-1) ** i) * matrix[0][i] * determinant(minor)
    
    return det

# Test the program
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
          
det = determinant(matrix)
print("Determinant of the matrix is:", det)
