
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    transpose_matrix = np.transpose(matrix)
    identity_matrix = np.dot(matrix, transpose_matrix)
    
    if np.array_equal(identity_matrix, np.identity(rows)):
        return True
    else:
        return False

# Example matrix
matrix = np.array([[1, 0], [0, -1]])

if is_orthogonal(matrix):
    print("The given matrix is orthogonal.")
else:
    print("The given matrix is not orthogonal.")
