
import numpy as np

def is_orthogonal(matrix):
    # Transpose the matrix
    matrix_transpose = np.transpose(matrix)
    
    # Multiply the matrix with its transpose
    result = np.dot(matrix_transpose, matrix)
    
    # Check if the result is the identity matrix
    return np.allclose(result, np.eye(matrix.shape[1]))

# Test the program
matrix1 = np.array([[1, 0], [0, -1]])
print(is_orthogonal(matrix1))  # True

matrix2 = np.array([[1, 1], [0, 1]])
print(is_orthogonal(matrix2))  # False
