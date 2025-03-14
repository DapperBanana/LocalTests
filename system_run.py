
import numpy as np

def is_invertible(matrix):
    if np.linalg.matrix_rank(matrix) == matrix.shape[0]:
        return True
    else:
        return False

# Input matrix
matrix = np.array([[1, 2], [3, 4]])

if is_invertible(matrix):
    print("The matrix is invertible.")
else:
    print("The matrix is not invertible.")
