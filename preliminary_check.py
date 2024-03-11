
import numpy as np

def is_orthogonal(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        return False
    
    # Check if the transpose of the matrix multiplied by itself is equal to the identity matrix
    return np.allclose(np.dot(matrix.T, matrix), np.identity(rows))

# Example usage
matrix1 = np.array([[1, 0],
                    [0, -1]])
print(is_orthogonal(matrix1)) # True

matrix2 = np.array([[1, 1],
                    [0, 1]])
print(is_orthogonal(matrix2)) # False
