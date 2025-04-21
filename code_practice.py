
import numpy as np

def is_orthogonal(matrix):
    if np.allclose(np.dot(matrix, matrix.T), np.eye(matrix.shape[0])):
        return True
    else:
        return False

# Test the function with a sample matrix
matrix = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
