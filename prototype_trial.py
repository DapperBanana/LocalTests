
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    
    if rows != cols:
        return False

    orthogonal_check = np.dot(matrix, matrix.T)
    
    return np.allclose(orthogonal_check, np.eye(rows))

# Example matrix
matrix = np.array([[1, 0], [0, -1]])

if is_orthogonal(matrix):
    print("The given matrix is orthogonal.")
else:
    print("The given matrix is not orthogonal.")
