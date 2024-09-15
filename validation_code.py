
import numpy as np

def is_orthogonal(matrix):
    transpose_matrix = np.transpose(matrix)
    product_matrix = np.dot(matrix, transpose_matrix)
    
    identity_matrix = np.identity(len(matrix))
    
    return np.array_equal(product_matrix, identity_matrix)

matrix = np.array([[1, 0],
                   [0, -1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
