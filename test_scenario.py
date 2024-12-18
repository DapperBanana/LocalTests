
import numpy as np

def is_orthogonal(matrix):
    transpose = np.transpose(matrix)
    product = np.dot(matrix, transpose)
    
    identity_matrix = np.identity(matrix.shape[0])
    
    return np.array_equal(product, identity_matrix)

# Example matrix
matrix = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, -1]])

if is_orthogonal(matrix):
    print("The given matrix is orthogonal.")
else:
    print("The given matrix is not orthogonal.")
