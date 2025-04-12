
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    ortho_matrix = np.dot(matrix, matrix.T)
    
    identity_matrix = np.eye(rows)
    
    return np.allclose(ortho_matrix, identity_matrix)

# Test the program with a sample matrix
matrix = np.array([[1, 0],
                   [0, -1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
