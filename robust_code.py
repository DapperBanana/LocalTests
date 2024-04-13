
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    product = np.dot(matrix, matrix.T)
    
    identity_matrix = np.eye(rows)
    
    return np.allclose(product, identity_matrix)

# Example matrix
matrix = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
