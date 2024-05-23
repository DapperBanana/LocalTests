
import numpy as np

def is_orthogonal(matrix):
    transpose = np.transpose(matrix)
    
    # Checking if the product of the matrix and its transpose is equal to the identity matrix
    product = np.dot(matrix, transpose)
    identity = np.identity(len(matrix))
    
    # Checking if the product of the matrix and its transpose is close enough to the identity matrix
    # This is necessary due to floating point errors
    return np.allclose(product, identity)

# Example usage
matrix = np.array([[1, 0], [0, -1]])
if is_orthogonal(matrix):
    print("The matrix is orthogonal")
else:
    print("The matrix is not orthogonal")
