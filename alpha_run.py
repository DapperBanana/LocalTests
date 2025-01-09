
import numpy as np

def is_orthogonal(matrix):
    transpose_matrix = np.transpose(matrix)
    identity_matrix = np.dot(matrix, transpose_matrix)
    
    rows, cols = identity_matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i == j and not np.isclose(identity_matrix[i][j], 1):
                return False
            elif i != j and not np.isclose(identity_matrix[i][j], 0):
                return False
    
    return True

# Example matrix
matrix = np.array([[1, 0], [0, -1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
