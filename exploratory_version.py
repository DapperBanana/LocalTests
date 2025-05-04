
def determinant(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for col_idx in range(n):
            minor = [row[:col_idx] + row[col_idx+1:] for row in matrix[1:]]
            det += ((-1) ** col_idx) * matrix[0][col_idx] * determinant(minor)
        
        return det

# Example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Determinant of the matrix:", determinant(matrix))
