
import numpy as np

def is_orthogonal(matrix):
    transpose = np.transpose(matrix)
    product = np.dot(matrix, transpose)
    
    rows, cols = matrix.shape
    identity_matrix = np.identity(rows)
    
    if np.array_equal(product, identity_matrix):
        return True
    else:
        return False

# example usage
matrix = np.array([[1, 0],
                   [0, -1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
