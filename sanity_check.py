
import numpy as np

def is_orthogonal(matrix):
    transpose_matrix = matrix.transpose()
    identity_matrix = np.dot(matrix, transpose_matrix)
    
    if np.array_equal(identity_matrix, np.eye(matrix.shape[0])):
        return True
    else:
        return False

# Test the program
matrix1 = np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

matrix2 = np.array([[1, 0, 0],
                     [0, 1, 0],
                     [1, 0, 1]])

print("Matrix 1 is orthogonal:", is_orthogonal(matrix1))
print("Matrix 2 is orthogonal:", is_orthogonal(matrix2))
