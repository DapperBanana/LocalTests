
import numpy as np

def is_orthogonal(matrix):
    transpose = np.transpose(matrix)
    product = np.dot(matrix, transpose)
    
    # Check if the product of the matrix and its transpose is equal to the identity matrix
    identity_matrix = np.identity(matrix.shape[0])
    
    if np.allclose(product, identity_matrix):
        return True
    else:
        return False

# Test the function with a sample matrix
matrix = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, -1]])

if is_orthogonal(matrix):
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
