
import numpy as np

def is_orthogonal(matrix):
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        return False
    
    # Compute the dot product of the matrix with its transpose
    dot_product = np.dot(matrix, matrix.T)
    
    # Check if the dot product is equal to the identity matrix
    identity_matrix = np.eye(matrix.shape[0])
    
    return np.array_equal(dot_product, identity_matrix)

# Test the program with a sample matrix
matrix = np.array([[1, 0], [0, -1]])
result = is_orthogonal(matrix)

if result:
    print("The matrix is orthogonal.")
else:
    print("The matrix is not orthogonal.")
