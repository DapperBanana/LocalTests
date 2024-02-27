
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    
    # Check if the matrix is square
    if rows != cols:
        return False
    
    # Calculate the transpose of the matrix
    transpose_matrix = np.transpose(matrix)
    
    # Calculate the dot product of the matrix and its transpose
    dot_product = np.dot(matrix, transpose_matrix)
    
    # Check if the dot product is an identity matrix
    identity_matrix = np.identity(rows)
    
    return np.array_equal(dot_product, identity_matrix)


# Test the function
matrix1 = np.array([[1, 0], [0, -1]])
print(is_orthogonal(matrix1))  # Output: True

matrix2 = np.array([[1, 0], [0, 1]])
print(is_orthogonal(matrix2))  # Output: False
