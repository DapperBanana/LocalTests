
import numpy as np

def is_orthogonal(matrix):
    product = np.dot(matrix, matrix.T)
    num_rows, num_cols = product.shape
    
    if num_rows != num_cols:
        return False
    
    identity = np.eye(num_rows)
    
    return np.allclose(product, identity)

# Test the function
matrix1 = np.array([[1, 0],
                    [0, 1]])

matrix2 = np.array([[1, 0],
                    [0, -1]])

print(is_orthogonal(matrix1))  # Output: True
print(is_orthogonal(matrix2))  # Output: True
