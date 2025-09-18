
import numpy as np

def is_orthogonal(matrix):
    matrix_transpose = np.transpose(matrix)
    matrix_product = np.dot(matrix, matrix_transpose)
    
    identity_matrix = np.identity(matrix.shape[0])
    
    return np.array_equal(matrix_product, identity_matrix)

# Test the function with a sample matrix
matrix = np.array([[1, 0], [0, -1]])
if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
