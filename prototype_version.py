
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    orthogonal = np.allclose(np.dot(matrix, matrix.T), np.eye(rows))
    
    return orthogonal

# Example matrix to test
A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, -1]])

if is_orthogonal(A):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
