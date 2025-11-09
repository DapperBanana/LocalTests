
import numpy as np

def is_matrix_orthogonal(matrix):
    if not isinstance(matrix, np.ndarray):
        print("Input is not a valid matrix")
        return False
    
    num_rows, num_cols = matrix.shape
    
    if num_rows != num_cols:
        print("Input matrix is not square")
        return False
    
    dot_product = np.dot(matrix, matrix.T)
    identity_matrix = np.eye(num_rows)
    
    return np.allclose(dot_product, identity_matrix)

# Example usage
matrix1 = np.array([[1, 0], [0, 1]])  # Identity Matrix
print(is_matrix_orthogonal(matrix1))  # Output: True

matrix2 = np.array([[1, 0], [0, -1]])  # Orthogonal matrix
print(is_matrix_orthogonal(matrix2))  # Output: False

matrix3 = np.array([[1, 2], [3, 4]])
print(is_matrix_orthogonal(matrix3))  # Output: False
