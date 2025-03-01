
def get_matrix_minor(matrix, row, col):
    return [row[:col] + row[col+1:] for row in (matrix[:row]+matrix[row+1:])]

def calculate_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    determinant = 0
    for col in range(len(matrix)):
        minor = get_matrix_minor(matrix, 0, col)
        determinant += ((-1)**col) * matrix[0][col] * calculate_determinant(minor)
    
    return determinant

# Example matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix:", matrix)
print("Determinant:", calculate_determinant(matrix))
