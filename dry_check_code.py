
import numpy as np

def is_orthogonal(matrix):
    transpose = np.transpose(matrix)
    product = np.dot(matrix, transpose)
    
    identity_matrix = np.identity(len(matrix))
    
    return np.array_equal(product, identity_matrix)

# Example matrix
matrix1 = np.array([[1, 0],
                     [0, -1]])

matrix2 = np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

if is_orthogonal(matrix1):
    print("Matrix 1 is orthogonal")
else:
    print("Matrix 1 is not orthogonal")

if is_orthogonal(matrix2):
    print("Matrix 2 is orthogonal")
else:
    print("Matrix 2 is not orthogonal")
