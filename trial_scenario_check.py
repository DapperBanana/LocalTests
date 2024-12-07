
def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def get_matrix_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    determinant = 0
    
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * get_matrix_determinant(get_matrix_minor(matrix, 0, c))
    
    return determinant

# Input a square matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

determinant = get_matrix_determinant(matrix)
print(f"Determinant of the matrix is: {determinant}")
