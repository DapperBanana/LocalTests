
import numpy as np

def is_orthogonal(matrix):
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    
    if rows != cols:
        return False
    
    transpose_matrix = np.transpose(matrix)
    product_matrix = np.dot(matrix, transpose_matrix)
    
    identity_matrix = np.eye(rows)
    
    if np.array_equal(product_matrix, identity_matrix):
        return True
    else:
        return False

# Test the function with a sample matrix
sample_matrix = [[1, 0], [0, -1]]
print(is_orthogonal(sample_matrix))  # Output: True

sample_matrix_2 = [[1, 1], [0, 1]]
print(is_orthogonal(sample_matrix_2))  # Output: False
